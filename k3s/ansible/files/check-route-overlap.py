#!/usr/bin/env python3
"""Fail when an existing IPv4 route overlaps a requested cluster CIDR."""

from __future__ import annotations

import ipaddress
import subprocess
import sys


def routed_networks() -> list[ipaddress.IPv4Network]:
    output = subprocess.run(
        ["ip", "-4", "route", "show", "table", "all"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    networks: list[ipaddress.IPv4Network] = []
    for line in output.splitlines():
        fields = line.split()
        if not fields:
            continue
        route_types = {"local", "broadcast", "unreachable", "blackhole", "prohibit", "throw"}
        destination = fields[1] if fields[0] in route_types else fields[0]
        if destination == "default":
            continue
        try:
            network = ipaddress.ip_network(destination, strict=False)
        except ValueError:
            continue
        if isinstance(network, ipaddress.IPv4Network):
            networks.append(network)
    return networks


def main() -> int:
    requested = [ipaddress.ip_network(value, strict=True) for value in sys.argv[1:]]
    conflicts = [
        f"{route} overlaps {cluster}"
        for route in routed_networks()
        for cluster in requested
        if route.overlaps(cluster)
    ]
    if conflicts:
        print("Existing routes overlap the requested Kubernetes networks:", file=sys.stderr)
        print("\n".join(f"- {conflict}" for conflict in conflicts), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
