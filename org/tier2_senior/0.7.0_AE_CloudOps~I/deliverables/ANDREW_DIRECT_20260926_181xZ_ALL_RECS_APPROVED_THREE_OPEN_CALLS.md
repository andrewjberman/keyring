# ANDREW-DIRECT 2026-09-26 ~18:1xZ -- all three open calls approved as recommended

**Channel:** the `0.7.0_AE_CloudOps~I` terminal, site Z. Andrew at the terminal, in response to
`/open-calls` run at this lane.

**VERBATIM, his whole message:**

> all recs approved

That is the ruling in full. Nothing else was said, and nothing below widens it. The three cards it
answers were rendered in the same turn and are reproduced here so the word is readable against what
it approved -- a bare "approved" with the question elsewhere is not a record.

---

## What was approved, card by card

### CALL 1 -- Resume MX-s-5? (a) go / (b) hold
**REC, approved: (a) go.** Three acts, about twenty minutes, no live-cloud writes.

MINE. Executing this turn. The hold existed only because Andrew interrupted the lane's tool call at
this terminal and asked for a stage report instead; his word above is what releases it. The issuer
(`2.0.0_SA_COO~O`) had been drive-nudging and had measured the criterion passing on CLOUD, but a
peer's measurement does not lift an operator hold and was not treated as if it did.

### CALL 2 -- Publish the release tag `opal-assets-v0.50.0`? (a) yes / (b) leave it
**REC, approved: (a) yes, next integration window.**

NOT MINE. `LD-0367`/`LD-0368` reserve every push on `CLOUD` to `0.0.0_AB_MSTR` / `0.0.0_AB_MSTR~Z`,
and a tag rides `--follow-tags` on that push. The tag exists LOCALLY at this device and is absent
from origin (measured: `git ls-remote --tags origin` returns 0 matches for it).

>> **PARKED, because it cannot be delivered from here.** This lane's broker link is down -- it can
receive mail but cannot ack, heartbeat or send. "Queued if not live" is a wish, not a delivery, so
the item is parked on this record rather than pretended into an inbox.
>> **OWNER:** `0.0.0_AB_MSTR~Z`.
>> **UN-PARKS WHEN:** this lane's broker link is restored and the item is sent, OR any seat reading
this record relays it to `0.0.0_AB_MSTR~Z`, naming this file.

### CALL 3 -- Open a sweep of the other stale converter snapshots? (a) now / (b) queue / (c) leave
**REC, approved: (b) queue it behind current work.**

NOT MINE TO SCHEDULE. The card offered the issuer as the owner if Andrew preferred not to spend the
call; he approved the recommendation, which is the queue-it disposition, and said nothing about
re-routing ownership, so ownership is NOT adjudicated here -- surfaced, not widened.

THE MEASUREMENT BEHIND IT, so the next reader does not have to re-derive it: of the 7
`opal-assets-silver-*` families carrying a build directory, **3 hold at least one vendored module
whose bytes differ from the repo source they mirror** -- `blackdiamond` (2:
`rebalancer_conversion.py`, `rebalancer_schemas.py`), `eclipse` (3: `mirror_conversion.py`,
`mirror_schemas.py`, `silver_registry.py`) and `orion` (the same 3). `bd49finsurance`, `schwab`,
`smartx` and (post-repair) `etf` read 0.

⚠ AND THE SHARP HALF: **every one of those three manifests is SELF-CONSISTENT** -- its recorded
`vendor_sha256` matches what is on disk. So the manifest check reports fine while the snapshot has
drifted from its source. The instrument cannot see the failure it exists to catch. That is exactly
how `opal-assets-silver-etf` ran 73 days without the TrueShares holdings converter.

>> LIMIT, stated rather than glossed: "differs from the repo source" is NOT "is wrong" and NOT "is
what is deployed". It is the same SIGNATURE etf carried, not proof of the same consequence. Whether
any of the three is materially stale needs the per-family read this order did for etf.
>> **PARKED** for the same broker reason as call 2.
>> **OWNER:** `2.0.0_SA_COO~O` as the issuing coordinator, unless a Tier-1 seat claims it.
>> **UN-PARKS WHEN:** the broker link is restored and the item is sent, OR a seat reading this
record relays it, naming this file.

---

## Scope discipline on this record

Andrew said four words. They approve three recommendations and nothing else. In particular this
record does NOT read them as: authorizing the sweep itself (call 3 was approved as *queue*, not as
*do*), authorizing any push beyond the one tag named in call 2, lifting any standing hold, or
ruling on the broker outage (which was explicitly flagged as NOT a call). A relay of his word must
not add the rule that seems to follow from it.
