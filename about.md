---
layout: page
title: About
subtitle: 'A little bit about NixNet and the guys who run it'
description: A little bit about NixNet and the guys who run it
permalink: /about/
---
**NixNet** is a network of websites and services hosted by the pseudonymous **Amolith** (me) and a close friend of his, Manton. The main reason we run these sites is because we like to be in control of our own data where feasible. The easiest way to accomplish that is to host the services we use. We make them public and maintain them simply because we want to; the Linux and FLOSS community has completely changed ours lives and we feel like this is a small way we can do our part and give back.

Our [bus factor](https://en.wikipedia.org/wiki/Bus_factor) is currently 4. Should something happen to both Amolith and Manton, there are two additional individuals that can step up to maintain these services.

Amolith's *personal* corner of the internet is [Secluded.Site](https://secluded.site).

For our financial information, check [the Finance](/finance) page.

## Some technical details

Our main server is the [AX51-NVME](https://www.hetzner.com/dedicated-rootserver/ax51-nvme) provided by [Hetzner](https://www.hetzner.com/) and located in Finland. The BigBlueButton server and its accompanying TURN server are Hetzner's CX22 and CX21 VPSes respectively; check their [cloud pricing page](https://www.hetzner.com/cloud) for more information. Our authoritative nameservers are each [Slice 1024](https://buyvm.net/kvm-dedicated-server-slices/) from [BuyVM](https://buyvm.net) and hosted in Las Vegas, New York, and Luxembourg. Daily backups are automated with [Tarsnap](https://tarsnap.com/) and [ACTS](https://github.com/alexjurkiewicz/acts/); we keep ~30 daily backups, 12 monthly backups, and manually delete yearly backups when we feel they're no longer necessary.

Our processes for setting Debian-based VPSes up is described in [our wiki](https://docs.nixnet.services/Debian), as is our process for [bare metal servers](https://docs.nixnet.services/Debian/Hetzner) and [Tarsnap](https://docs.nixnet.services/Tarsnap). Other resources pertaining to our setup can be found by exploring the wiki.
