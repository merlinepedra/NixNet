---
layout: page
title: Tor Nodes
description: Tor exits operated under NixNet
subtitle: Tor exits operated under NixNet
permalink: /tor-nodes/
cover: /assets/pages/tor.png
---
# Why am I here
You're likely seeing this page because you had some issue with traffic from one of the following IP addresses:
* 209.141.34.95
* 104.244.78.231
* 199.195.251.84

The machines at those addresses are part of the [Tor Anonymity Network](https://www.torproject.org/) and dedicated to [providing privacy](https://www.torproject.org/about/overview) to the people who need it most: average computer users. Unless they've been compromised, you should be seeing no other traffic originating from them.

You can verify that they are, in fact, part of Tor by looking at the relevant pages on The Tor Project's [Relay Search](https://metrics.torproject.org/rs.html). I've also listed them below.
* 209.141.34.95 - [Illana](https://metrics.torproject.org/rs.html#details/7731E125924324B7405BA20E2759EE16780237E2)
* 104.244.78.231 - [Nika](https://metrics.torproject.org/rs.html#details/B135DDBA0C309640D8311575A334157EA28E3FAF)
* 199.195.251.84 - [Alina](https://metrics.torproject.org/rs.html#details/324E13FD795713BDD6E8B4DF02438742CA1FDBF1)

# Who's running this
The [exit relay](https://trac.torproject.org/projects/tor/wiki/TorRelayGuide#Exitrelay) that directed you here is run by Amolith (me) under NixNet, a network of sites and services available to anyone free of charge. Despite the potential legal ramifications, I decided to run them because I am *very* passionate about online privacy, anonymity, and freedom of speech. In today's society, Tor is one of the very few ways to truly achieve that and I wanted to directly help those that need it by running fast exits.
# Who is it for
Tor sees use by many important [segments of the population](https://www.torproject.org/about/torusers), including whistle blowers, journalists, Chinese dissidents skirting the Great Firewall and oppressive censorship, abuse victims, stalker targets, the US military, and law enforcement, just to name a few. While Tor is not designed for malicious computer users, it is true that they can use the network for malicious ends. In reality however, the actual amount of [abuse](https://www.torproject.org/docs/faq-abuse) is quite low. This is largely because criminals and hackers have significantly better access to privacy and anonymity than do the regular users whom they prey upon. Criminals can and do [build, sell, and trade](http://voices.washingtonpost.com/securityfix/2008/08/web_fraud_20_tools.html) far larger and [more powerful networks](http://voices.washingtonpost.com/securityfix/2008/08/web_fraud_20_distributing_your.html) than Tor on a daily basis. Thus, in my mind, the social need for easily accessible censorship-resistant private, anonymous communication trumps the risk of unskilled bad actors, who are almost always more easily uncovered by traditional police work than by extensive monitoring and surveillance anyway.
# Legal ramifications
 In terms of applicable law, the best way to understand Tor is to consider it a network of routers operating as common carriers, much like the Internet backbone. However, unlike the Internet backbone routers, Tor routers explicitly do not contain identifiable routing information about the source of a packet, and no single Tor node can determine both the origin and destination of a given transmission.

As such, there is little I can do to help you track the connection further. These routers maintain no logs of any of the Tor traffic so there is little that can be done to trace either legitimate or illegitimate traffic (or to filter one from the other). Attempts to seize any of these will accomplish nothing.

Furthermore, these machines also serve as a carriers of email, which means that their contents are further protected under the ECPA. [18 USC 2707](http://www.law.cornell.edu/uscode/text/18/2707) explicitly allows for civil remedies ($1000/account **plus** legal fees) in the event of a seizure executed without good faith or probable cause (it should be clear at this point that traffic originating from the IPs listed above should not constitute probable cause to seize the machine). Similar considerations exist for 1st amendment content on this machine.
# You're violating DMCA!
If you are a representative of a company who feels that this router is being used to violate the DMCA, please be aware that this machine does not host or contain any illegal content. Also be aware that network infrastructure maintainers are not liable for the type of content that passes over their equipment, in accordance with DMCA [safe harbor](http://www.law.cornell.edu/uscode/text/17/512) provisions. In other words, you will have just as much luck sending a takedown notice to the Internet backbone providers. Please review the EFF's [prepared response](https://www.torproject.org/eff/tor-dmca-response) for more information on this matter.

For general information, please consult the following documentation:
1. [Tor Overview](https://www.torproject.org/about/overview)
2. [Tor Abuse FAQ](https://www.torproject.org/docs/faq-abuse)
3. [Tor Legal FAQ](https://www.torproject.org/eff/tor-legal-faq)

# I still have an issue
 That being said, if you still have a complaint about these routers, you may [contact me](/contact). If complaints are related to a particular service that is being abused, I will consider removing that service from my exit policy, which would prevent my router from allowing that traffic to exit through it. I can only do this on an IP+destination port basis, however.
You also have the option of blocking this IP address and others on the Tor network if you so desire. The Tor project provides a [web service](https://check.torproject.org/cgi-bin/TorBulkExitList.py) to fetch a list of all IP addresses of Tor exit nodes that allow exiting to a specified IP:port combination, and an official [DNSRBL](https://www.torproject.org/tordnsel/dist/) is also available to determine if a given IP address is actually a Tor exit server. Please be considerate when using these options. It would be unfortunate to deny all Tor users access to your site indefinitely simply because of a few bad apples.
