# Automated k3s installation with Ansible

This directory automates the initial four-node installation described in the
[k3s runbook](../README.md). The runbook remains the source of truth for the
architecture, security boundaries, manual recovery, backups, and upgrades.

The automation is intentionally specific to this homelab:

- one controller at `10.10.10.10` using SQLite;
- three workers at `10.10.10.11` through `10.10.10.13`;
- cluster traffic on isolated `eth0` and administration/Internet access on
  `wlan0`;
- k3s `v1.36.2+k3s1`; and
- the documented kubelet reservations, including worker3's larger host
  reservation for the DeskPi kiosk.

The playbook does not image Raspberry Pis, configure Wi-Fi or a firewall,
install worker3's kiosk packages, manage backups, or perform k3s upgrades.

## Prerequisites

On the admin Mac, install:

- `ansible-core` 2.18 or newer;
- `kubectl`;
- the SSH private key at `~/.ssh/homelab`; and
- the Ansible collection declared in `requirements.yml`.

Each Pi must already run 64-bit Raspberry Pi OS Lite from its NVMe SSD, have the
hostname in `inventory/hosts.yml`, connect to Wi-Fi, resolve through its `.local`
name, and accept SSH as `dkhundley`. The account must have passwordless sudo or
the playbook must be run with `--ask-become-pass`.

From this directory, install the Ansible dependency and inspect the inventory:

```shell
ansible-galaxy collection install -r requirements.yml
ansible-inventory --graph
ansible all -m ansible.builtin.ping
```

Host-key checking is enabled. Connect to every Pi with `ssh` first and verify its
fingerprint if it is not already present in `~/.ssh/known_hosts`.

## Run the installation

Review `inventory/hosts.yml` and `group_vars/` before the first run. Then execute
the complete, ordered installation:

```shell
ansible-playbook site.yml
```

The playbook performs OS and available Raspberry Pi EEPROM updates, so nodes can
reboot during `prepare`. Host preparation and worker joins run one node at a
time. If sudo requires a password, use:

```shell
ansible-playbook site.yml --ask-become-pass
```

The resulting administrator credential is written atomically to
`~/.kube/k3s-homelab.yaml` with mode `0600`. The playbook also idempotently adds
an export using the resolved absolute path to `~/.zshrc`, equivalent to:

```shell
export KUBECONFIG="$HOME/.kube/k3s-homelab.yaml"
```

Open a new terminal or source `~/.zshrc` after the first run.

## Run individual stages

The entrypoint exposes the following tags:

| Tag | Purpose |
|---|---|
| `preflight` | Validate the Mac, inventory, host identity, architecture, NVMe root, and interfaces. |
| `prepare` | Upgrade Raspberry Pi OS and EEPROM, configure cgroups, disable swap, and enable trim. |
| `network` | Configure and validate the isolated static Ethernet network. |
| `server` | Configure and install the single k3s controller. |
| `agents` | Configure and serially join all three workers. |
| `kubeconfig` | Refresh the Mac administrator kubeconfig and shell export. |
| `validate` | Validate host services, routes, nodes, add-ons, labels, storage, and encryption. |
| `smoke` | Run opt-in disposable networking, DNS, egress, and persistence tests. |

For example:

```shell
ansible-playbook site.yml --tags preflight
ansible-playbook site.yml --tags prepare,network
ansible-playbook site.yml --tags server,agents,kubeconfig,validate
ansible-playbook site.yml --tags smoke
```

Stages depend on the state produced by earlier stages. Use the complete command
for a fresh installation; tags are primarily for inspection and targeted
reruns. The `smoke` tag is marked `never` and cannot run accidentally as part of
the normal playbook.

## Safety and reruns

The controller creates its agent-only token once. Ansible transfers it to each
worker with task output and diffs suppressed; the token is never written inside
this repository. The administrator kubeconfig likewise remains outside the
repository.

The playbook is designed to converge when rerun. Configuration changes restart
only the affected k3s service. If k3s is already installed at a version other
than `k3s_version`, the run stops rather than upgrading, downgrading, or
uninstalling the cluster. Follow the runbook's manual upgrade procedure instead.

## Validate the automation

Useful local checks include:

```shell
ansible-playbook site.yml --syntax-check
ansible-playbook site.yml --list-hosts
ansible-playbook site.yml --list-tasks
ansible-playbook site.yml --list-tags
ansible-lint site.yml
```

Ansible check and diff modes can preview many declarative changes:

```shell
ansible-playbook site.yml --check --diff --limit dkhundley-homelab-worker1
```

Check mode cannot fully simulate installer execution, service startup, reboots,
or checks that depend on state created earlier in the same run. Diff output is
disabled for token and kubeconfig tasks so credentials are not disclosed.
