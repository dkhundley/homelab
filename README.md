![](assets/homelab-banner.png)
# My Raspberry Pi Homelab

> [!NOTE]
> I am just getting up and going with my homelab! I intend to continue adding content to this repo likely all the way through the end of 2026. I'll remove this note once I feel relatively solidified.

## Intention
My primary intention with building this homelab is simply to **learn and have fun**. For folks who work in a large organization, you likely work amongst either cloud services or managed on-premises environments. In both instances, the environment is largely managed for you, which is ideal if a company is looking to apply specific standards across all software engineering efforts. The "downside" to this (although it's not really a downside) is that most developers are not exposed to managing physical IT infrastructure.

While I don't know if I'll ever be in a formal position to manage physical IT infrastructure, I thought it'd be fun to learn these skills myself by building / maintaining this homelab. I intend to learn things like Ansible, managing a Kubernetes (k8s) cluster, and more. What I do **not** intend on using this homelab for is local LLM hosting. While there could be some value in learning that, the reality is that I would need highly specialized hardware that would get far too expensive for me to purchase on my own. Everything I intend to manage in my homelab has low computational needs.

## Livestreams
Throughout my build process, I intend to livestream as much of it as I can. This will likely take place over the course of several months. These streams will likely breakdown into one of two categories: streams specifically dedicated to this homelab and streams dedicated to skills that would go into supporting the homelab.

### Direct Homelab Streams
- **Part 1: The Hardware** ([Link](https://www.youtube.com/live/giuC7GGIl5E?si=JmSnEAJfPBgQZ_kP)): This introductory stream covers my intention behind building my homelab, resources I used to help with researching what I wanted to build, and a thorough review of all the hardware going into my homelab.

### Skill-Adjacent Homelab Streams
None yet, but I will add them once I get here!

## Hardware
In this section, I'll share all the hardware for my personal homelab build. I have included links for purchase plus component prices, but please be aware that pricing / availability is likely subject to change. Prices also do not include tax nor shipping. All my components were purchased during summer 2026.

| Product | Link | Price | Considerations |
|---------|------|-------|----------------|
| **Compute** | | | |
| Raspberry Pi 5 (x4) | [4GB model CanaKit link](https://www.canakit.com/raspberry-pi-5-4gb.html)<br><br>[8GB model CanaKit link](https://www.canakit.com/raspberry-pi-5-8gb.html) | $635.00 (3x 8GB Pi 5s at $175 each, 1 4GB Pi 5 at $110) | Building with Raspberry Pi 5s. I was very uncertain which RAM sizes to choose. Originally, I thought to build the whole thing with all 4GB models, but then I decided I wanted more headroom. I originally purchased just 1 4GB model but then decided that it would be best if the other 3 had more RAM at 8GB. All in all, my homelab has 3 8GB Raspberry Pi 5s and 1 4GB Raspberry Pi 5. |
| **Case** | | | |
| GeeekPi DeskPi RackMate T0 Plus<br>10-inch 4U Mini Server Cabinet (Black) | [Amazon link](https://a.co/d/04l6uONa) | $99.99 | Looking to keep as small as possible. Opted for the DeskPi RackMate T0 Plus over the standard T0 since it is a little deeper, giving me more wiggle room for components and cabling. |
| **Storage** | | | |
| OEM Samsung 256GB M.2 PCI-e NVME SSD GEN 4X4 Internal Solid State Drive 30mm 2230 Form Factor| [Amazon link](https://a.co/d/02pP6kUk) | $247.80 ($61.95 each) | Opting for 256GB NVMe SSDs. Would have preferred 128GB, but they’re not readily available. Options I found for 128GB were only roughly $4 cheaper, at which point, why not just go for 256GB? (Note: The link in which I bought these is now showing as "No longer available". Not sure if they will come available again, but there are other similar options on Amazon.) |
| **Cooling / HAT** | | | |
| GeeekPi P31 M.2 NVME M-Key PoE+ HAT with Official Active Cooler for Raspberry Pi 5, Support M.2 NVMe SSD 2230 2242| [Amazon link](https://a.co/d/0hqzuAcu) | $143.96 ($35.99 each) | Opting for NVMe PoE+ HAT, specifically GeeekPi’s P31 version. They do offer a P33, but it looks like that is more recommended if you’re going to use 1TB+ storage. Also it appears that P31 is slightly smaller. P31 suffices for my use. <br><br> This also comes with a standard Raspberry Pi fan for cooling purposes. |
| **Networking** | | | |
| NETGEAR 5-Port Gigabit Ethernet Unmanaged PoE Switch (GS305PP) - with 4 x PoE+ @ 83W, Desktop or Wall Mount | [Amazon link](https://a.co/d/0hqzuAcu) | $79.99 | I wanted something to both support networking and provide sufficient power to the Pis through power over ethernet (PoE). This switch has enough power for my needs. Under super heavy workloads, this may not be enough, but I think I’ll be fine for my purposes. |
| **Power** | | | |
| Blazin3D 1U 10-Inch Rack Mount Power Hub – 6/12 Outlet PDU with USB-A & USB-C Ports – Optimized for Mini-Racks, Raspberry Pi Clusters & Networking (Black) | [Amazon link](https://a.co/d/05ugkQ7L) | $39.99 | I landed on this option specifically because I really like the USB ports options, which I intend to power the screen since the screen didn’t come with a brick. ChatGPT struggled to determine if this was UL certified, but on receiving the item myself, I can confirm that it is. |
| **Mounting** | | | |
| GeeekPi 10 inch 2U Rack Mount for Raspberry Pi 5/4B/3B+/3B, with Removable Front Brackets | [Amazon link](https://a.co/d/01XIQubW) | $44.99 | Simply put, this rack mount was specifically made to work with the case I purchased and can seamlessly hold 4 Raspberry Pis in place. (We'll share a special thing I had to do to make this mount work with the Pis per the pin extender below.) |
| 13.5mm GPIO and PoE Pin Header Height Extender for RPi (Pack of 2) for RPi 5 4B 3B+ 3B | [Amazon link](https://a.co/d/0geRES5M) | $13.98 (2 packs of 2 extenders at $6.99 each) | The GeeekPi P31 HAT comes with extenders to mount it to a Raspberry Pi, but in order to make it work with the rack mount from the line item above, the provided extenders were too tall. These particular extenders here are shorter and have a better fit for the rack mount. |
| 3D printed 10 inch Mount Rack for Netgear GS305PP Switch | N/A | ~$40 | I could not find an off-the-shelf option for mounting the Netgear switch to my case, so I had to have one custom 3D printed. Fortunately, I did find [a schematic online](https://www.printables.com/model/1295100-10-rack-mount-for-netgear-gs305pp/files) which could be simply fed into a 3D printer. Unfortunately, I do not have a 3D printer myself, so I had to use an online service for this, which cost me around $40. I am not mentioning the name of that service here because I am not sure they did all that quality of a job, so my recommendation would be ideally that you find a friend with a 3D printer and have them do this for you. |
| 0.5U Vented Blank Panel - 10 Inch Rack Mount - Mesh Filler Plate | [Etsy link](https://www.etsy.com/listing/4443494756/05u-vented-blank-panel-10-inch-rack) | $14.99 | This was honestly completely unnecessary, but I didn't like that there was an empty gap showing at the bottom of my homelab. This is sometimes where people may mount a patch panel. I personally don't have a need for a patch panel, so I added this mesh filler plate instead. |
| **Screen** | | | |
| GeeekPi 6.91 inch 1424x280 LCD Touch Screen 1U Rack Mount Monitor for DeskPi RackMate T0/T1/T2/T0 Plus/T1 Plus/TL1 Server Cabinet and 10 inch Server Rack | [Amazon link](https://a.co/d/0doRAYfH) | $80.99 | This is honestly completely unnecessary, but I thought it would be fun to be able to display things like cluster status or even just the weather when sitting idly on my shelf behind my desk. This screen also does support touchscreen gestures. |
| **Cables** | | | |
| StarTech 6in CAT6 Ethernet Cable - Black CAT 6 Gigabit Ethernet Wire -250Mhz 100W PoE RJ45 UTP Network Patch Cord | [Amazon link](https://a.co/d/0bzcRQfX) | $23.72 ($5.93 each) | These cables connect each respective Raspberry Pi to the network switch to support both general networking and power over ethernet (PoE). Because of the short travel distance, I opted for these smaller 6 inch cables. |
| etguuds USB to USB C Cable 1ft, 2-Pack Short USB A to Type C Charger Cord | [Amazon link](https://a.co/d/02kcpsDJ) | $6.99 | In order to support the touchscreen functionality on the screen, the screen needs connected to one of the USB-A ports on the Raspberry Pi. The screen itself takes in a USB-C port, hence my recommendation for this USB-A to USB-C cable. Full transparency: I actually did not purchase this cable. I personally have a ton of these cables lying around, so I made use of my own, but I provided this link as the option I would have gone with if I didn't already own this cable. |
| Twozoh 4K Micro HDMI to HDMI Cable 1FT, Short High-Speed Full HDMI to Micro HDMI Braided Cord | [Amazon link](https://a.co/d/04vvaQHc) | $8.59 | This cable is used to connect the screen (HDMI) to one of the Raspberry Pis (micro HDMI). |
| **Miscellaneous** | | | |
| GeeekPi 30PCS #10-32 x 5/16" Pan Head Screws with Washers for DeskPi RackMate T1/T0/T2/TL1 Server Cabinet (Black) | [Amazon link](https://a.co/d/0c8IznaX) | $7.99 | These are extra screws for mounting things to my 10 inch case. The case itself does come with some screws but not necessarily enough. I went to my local Lowe's to see if I could find something similar but unfortunately couldn't find something that matched the size and also maintained that black color, so I went with this pack instead. |
| UGREEN SSD Enclosure, Tool-Free USB C External, 10Gbps M.2 NVMe to USB Adapter/Reader | [Amazon link](https://a.co/d/0542cw14) | $17.99 | Of all items on this list, this is the only one that actually doesn't go into maintaining the homelab itself. It's still necessary though as I used this adapter to image each of the respective NVMes. |


## Helpful Resources
This section covers a few of the helpful resources I used along the way when building my homelab.

- **Any content from Jeff Geerling** ([Link](https://github.com/geerlingguy/mini-rack)): If you've ever built your own homelab, chances are you've come across Jeff Geerling's content. Jeff is a wealth of knowledge here, and I would highly recommend checking out any of his work. The link here takes you to his `mini-rack` GitHub, which contains a wealth of information that helped me in my own build. Jeff also has great videos on his YouTube channel.
- **Matt Jarrett's homelab** ([Link](https://github.com/cujarrett/homelab)): Matt is a friend I know through my day job, and he has his own write up for his build on his GitHub linked above. It's relatively complementary toward Jeff Geerling's content.
- **ChatGPT**: Okay, not going to lie, ChatGPT was a great help here. I have over 20 threads created as part of a singular ChatGPT Project that helped me in my decision making process.