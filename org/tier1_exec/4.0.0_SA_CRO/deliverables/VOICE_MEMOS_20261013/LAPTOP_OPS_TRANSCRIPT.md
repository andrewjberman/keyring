# LAPTOP OPS — Voice Memo Transcript

- **Source audio:** LAPTOP_OPS.m4a
- **Recorded:** October 13, 2026 (morning)
- **Speaker:** Andrew Berman
- **Recipient:** MSTR on cloud-local (via Taildrop)
- **Note:** Auto-transcript, delivered verbatim. CTLPLN = control plane; DVPLN / EVPLN = developer plane (dev merges, box merges, portal dev/prod branches); comms assist = agent assistant; "news" = the NWS messaging channel; tailnet ops.

---

Now finally moving on to the laptop cloud dash vocal box and the expectations on what we're trying to do here. There are three projects that matter on the laptop box. They are CTLPLN, the control plane, they are the EVPLN, the developer plane or how we're going to manage the dev merges and the various box merges for the portal for the portals dev branch and prod branch. Finally the comms underscore assist how we are going to have a agent assistant that is helpful for me to manage all of this stuff. So control plane, CTLPLN, I think we're working through that, that's a decent space, DVPLN. We need to, I think we can figure that out today in one session that's not a big project that should be very, very simple to get implemented. Finally the comms assist. So the issue with this is that the kimi agent simply doesn't really have a harness, it's not really intelligent, it's very limited in its capability simply because we just haven't built it out that much and it's a little bit hacky to go through the QUO quow channel and doing all that. It's this very rigid and rickety. It's like so I think that there should be a way to handle this all through news and tailnet. So I think a big focus here is not only moving forward to the various control planes, CTL and DVPLNs but also establishing definitively tailnet ops throughout the cluster. We want to establish how tailnet works, we want to establish how news works, all of that needs to get done today.
