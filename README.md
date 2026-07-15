![](assets/homelab-banner.png)
# My Raspberry Pi Homelab

> [!NOTE]
> I am just getting up and going with my homelab! I intend to continue adding content to this repo likely all the way through the end of 2026. I'll remove this note once I feel relatively solidified.

## Intention
My primary intention with building this homelab is simply to **learn and have fun**. For folks who work in a large organization, you likely work amongst either cloud services or managed on-premises environments. In both instances, the environment is largely managed for you, which is ideal if a company is looking to apply specific standards across all software engineering efforts. The "downside" to this (although it's not really a downside) is that most developers are not exposed to managing physical IT infrastructure.

While I don't know if I'll ever be in a formal position to manage physical IT infrastructure, I thought it'd be fun to learn these skills myself by building / maintaining this homelab. I intend to learn things like Ansible, managing a Kubernetes (k8s) cluster, and more. What I do **not** intend on using this homelab for is local LLM hosting. While there could be some value in learning that, the reality is that I would need highly specialized hardware that would get far too expensive for me to purchase on my own. Everything I intend to manage in my homelab has low computational needs.

## Hardware
In this section, I'll share all the hardware for my personal homelab build. I have included links for purchase plus component prices, but please be aware that pricing / availability is likely subject to change. All my components were purchased during summer 2026. (Note: I am still updating this table. Will remove this note once my purchases are settled.)

| Product | Link | Price | Considerations |
|---------|------|-------|----------------|
| **Compute** | | | |
| Raspberry Pi 5 (x4) | [4GB model link](https://www.canakit.com/raspberry-pi-5-4gb.html)<br><br>[8GB model link](https://www.canakit.com/raspberry-pi-5-8gb.html) | TBA (Haven’t decided on RAM sizes for all 4 yet) | Building with Raspberry Pi 5s. I will come back and update this later once I’ve settled on RAM sizes. |
| **Case** | | | |
| GeeekPi DeskPi RackMate T0 Plus<br>10-inch 4U Mini Server Cabinet (Black) | [Amazon link](https://a.co/d/04l6uONa) | $99.99 | Looking to keep as small as possible. Opted for the DeskPi RackMate T0 Plus over the standard T0 since it is a little deeper, giving me more wiggle room for components and cabling. |
| **Storage** | | | |
| OEM Samsung 256GB M.2 PCI-e NVME SSD GEN 4X4 Internal Solid State Drive 30mm 2230 Form Factor M Key Steam Deck | [Amazon link](https://a.co/d/02pP6kUk) | $247.80 ($61.95 each) | Opting for 256GB NVMe SSDs. Would have preferred 128GB, but they’re not readily available. Options I found for 128GB were only roughly $4 cheaper, at which point, why not just go for 256GB? |
| **Cooling / HAT** | | | |
| GeeekPi P31 M.2 NVME M-Key PoE+ HAT with Official Active Cooler for Raspberry Pi 5, Support M.2 NVMe SSD 2230 2242| [Amazon link](https://a.co/d/0hqzuAcu) | $143.96 ($35.99 each) | Opting for NVMe PoE+ HAT, specifically GeeekPi’s P31 version. They do offer a P33, but it looks like that is more recommended if you’re going to use 1TB+ storage. Also it appears that P31 is slightly smaller. P31 suffices for my use. |
| **Networking** | | | |
| NETGEAR 5-Port Gigabit Ethernet Unmanaged PoE Switch (GS305PP) - with 4 x PoE+ @ 83W, Desktop or Wall Mount | [Amazon link](https://a.co/d/0hqzuAcu) | $79.99 | I wanted something to both support networking and provide sufficient power to the Pis through power over ethernet (PoE). This switch has enough power for my needs. Under super heavy workloads, this may not be enough, but I think I’ll be fine for my purposes. |
| **Power** | | | |
| Blazin3D 1U 10-Inch Rack Mount Power Hub – 6/12 Outlet PDU with USB-A & USB-C Ports – Optimized for Mini-Racks, Raspberry Pi Clusters & Networking (Black) | [Amazon link](https://a.co/d/05ugkQ7L) | $39.99 | I landed on this option specifically because I really like the USB ports options, which I intend to power the screen since the screen didn’t come with a brick. ChatGPT struggled to determine if this was UL certified, but on receiving the item myself, I can confirm that it is. |


## Helpful Resources
This section covers a few of the helpful resources I used along the way when building my homelab.

- **Any content from Jeff Geerling** ([Link](https://github.com/geerlingguy/mini-rack)): If you've ever built your own homelab, chances are you've come across Jeff Geerling's content. Jeff is a wealth of knowledge here, and I would highly recommend checking out any of his work. The link here takes you to his `mini-rack` GitHub, which contains a wealth of information that helped me in my own build. Jeff also has great videos on his YouTube channel.
- **Matt Jarrett's homelab** ([Link](https://github.com/cujarrett/homelab)) Matt is a friend I know through my day job, and he has his own write up for his build on his GitHub linked above. It's relatively complementary toward Jeff Geerling's content.
- **ChatGPT**: Okay, not going to lie, ChatGPT was a great help here. I have over 20 threads created as part of a singular ChatGPT Project that helped me in my decision making process.