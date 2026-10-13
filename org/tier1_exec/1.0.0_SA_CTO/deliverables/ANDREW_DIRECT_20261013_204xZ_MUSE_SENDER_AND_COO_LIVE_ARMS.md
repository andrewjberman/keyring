# Andrew-direct 2026-10-13 ~20:4xZ (laptop, 1.0.0_SA_CTO terminal) -- muse registered as an agentbus sender; every active COO in the live arms

## VERBATIM

> "I will address the open calls but first, see the below from Muse: [Muse's request, below] . Second, we need COO~C added to the
> live arms group, as well as any other active COO on the various boxes, so they can run canonical-drive properly. once these are
> handled, we can move on to those open calls and the ambiguity you alluded to regarding muse/kimi in comm_assist"

Muse's request, as Andrew pasted it: add a sender-only entry "ms" (name `ms`, tailnet_name `ms`, role sender-only, no inbound
queue) to `org/devices/DEVICES.json`, because the agentbus consumer refuses a message whose `from_tailnet` is not a tailnet name the
register holds. Muse will send a test message stamped `from_tailnet=ms` once the entry propagates.

## Applied

1. **muse as a sender, not a box.** Eleven tools iterate `devices[]`, including box lists, placement values, queue lookup, SSH
   verification, crossbox and the pipeline gate's box enum (comp-find census, 18 files). A sender-only entry there would make `ms`
   a fifth box in every one of them. So `ms` goes in a new top-level `senders` list.
   - `lib/devices.py` gains `senders()` and `held_tailnet_names()`, which return the boxes' tailnet names and then the senders'.
   - The two sender checks read it: `.tools/agentbus-consumer.py held_tailnet_names()` and `.tools/agentbus-sqs.sh _tailnet all`.
   - Read before landing:
     - held = cloud-local, sitez, dell1, dell2, ms.
     - `names()` and `placement_values()` are unchanged (4 boxes).
     - `classify`: `ms` delivers, an unknown name is refused, `dell1` delivers.
     - The shell body prints the same five names.
     - The register and agentbus tests pass, 14 of 14.
   - Muse's own test message is the end-to-end read. It needs the register on each consuming box, carried by box-sync.
2. **COO live arms:** `org/ref/LIVE_ARMS.md` @ad352da57c. Every COO lane on a non-terminal project, on every box, runs
   `/canonical-drive 60m` over its own project. 24 lanes are named at landing.
3. Next: the open calls and the muse/Kimi question (laptop row `87a2`, held for Andrew).
