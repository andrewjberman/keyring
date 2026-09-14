# PARKED at `1.0.0_SA_CTO`, 2026-09-12 ~01:3xZ -- two items whose OWNER is not live

Both items below are ANSWERED or ACTIONABLE and neither can be delivered, because the seat that owns
each is not running. Per CLAUDE.md: *"a BASE serial with no base session is a silent hole ... Address a
LIVE recipient, or PARK the item on its own carrier with an OWNER and the CONDITION that un-parks it."*
Mail to a dead seat gets no bounce, no ack and no staleness signal, and reads as delivered. Neither
item is mailed.

Liveness measured `.tools/fabric-check.py --agents` at 01:17Z: LIVE are `2.0.0_SA_COO~B`,
`2.0.0_SA_COO~F`, `3.0.0_SA_CVO`, `0.0.0_AB_MSTR`, `1.0.0_SA_CTO`. Neither owner below is among them.

---

## ROW 1 -- the daily-sprint window ruling, owed to `0.7.0_AE_CloudOps`

| | |
|---|---|
| **OWNER** | `0.7.0_AE_CloudOps` (the lane that surfaced it and holds LD-0547) |
| **UN-PARK WHEN** | that seat is LIVE on the broker |
| **UN-PARKED BY** | `1.0.0_SA_CTO`, or any Tier-1 seat that sees it come live |
| **BLOCKS** | nothing. The schedule is already applied at the approved value |

**THE RULING TO DELIVER.** Andrew-direct 2026-09-12 ~01:2xZ, VERBATIM AND ENTIRE: **"All recs
approved"**, answering a `/open-calls` card whose recommendation read: *"(a) keep 16:10. You asked for
it at 4:10 and a partial-day report you read is worth more than a complete one you do not; the
artifact says what window it covers, and it is reversible by one value."*

So the 16:10 ET fire STANDS and the report describes a day that has not closed **by decision**. That
closes the item `0.7.0_AE_CloudOps` surfaced at ~20:2xZ and explicitly declined to adjudicate
(*"SURFACED, NOT RESOLVED, because it is his call and not this seat's"*). The seat was right to
refuse it and right to keep the reversibility in the `schedule_expression` description.

⚠ **NOT ANSWERED AND STILL THAT LANE'S:** the EventBridge cron is UTC with no DST, so the approved
16:10 is 16:10 ET under EDT and **15:10 ET under EST**. Andrew approved a rec that said "16:10"; he
was not asked about the November shift. That is a live question for whoever holds it in the autumn,
not a defect now.

⚠ **ALSO OPEN IN THAT LANE, UNTOUCHED BY THIS RULING:** ledger `daily-sprint-generator-first-apply`
L7 (does the job RUN) is deliberately OPEN -- the authorized ad-hoc fire failed at step one of five
(`git checkout` rc=128, the PAT stripped before a lazy-fetching checkout), fix committed, and a
re-fire is what would close it.

---

## ROW 2 -- the two L4-R BRIEF halves, owed to `4.0.0_SA_CRO`

| | |
|---|---|
| **OWNER** | `4.0.0_SA_CRO` (Rule 27: the CRO signs the BRIEF half) |
| **UN-PARK WHEN** | that seat is LIVE on the broker |
| **UN-PARKED BY** | `1.0.0_SA_CTO` |
| **BLOCKS** | nothing. Both projects read ADMITTED and neither flips |

**THE ASK.** Re-stamp the BRIEF half of `IRPT_BCKEND` (v0.13 @`e6ba5d9878`) and `IRPT_FNTEND`
(v0.6 @`d1479bc5f0`). A new stamp carries a `half_hash`; the existing records carry none, so
`prd_signoff_lib.py:198` grades them on the VERSION STRING instead of the bytes. It is a re-execution
of a stamp already made at bytes measured unchanged -- **not a re-review**.

The RATIFIED-TEXT halves of both are already asked of `3.0.0_SA_CVO`, which is live.

⛔ **WHY THIS IS NOT ROUTED TO A LIVE COO INSTEAD.** Rule 27 allows *"a live `2.0.0_SA_COO` not
holding the round in its stead"*. `2.0.0_SA_COO` base is not live; `~B` and `~F` each hold their own
project's round. Cross-signing the counterpart's brief half to clear a lint is not what that clause is
for, and it would put a signature on a project the signer is not reviewing.

⛔ **AND THE FAIL-CLOSED FIX IS NOT TAKEN.** Making an absent `half_hash` mean NOT current would flip
both IRPT projects to WITHHELD mid-round -- manufacturing friction on live work to close an exposure
measured inert (eight halves, four records, ZERO moved, positive control firing on real bytes).
Andrew's site-Z direct ~01:1xZ, VERBATIM: **"Half hash approved"** -- that authorizes the NEW
`--expect-half-hash` guard and, as `0.0.0_AB_MSTR~Z` stated narrowly and correctly, **NOT** the
version-string fallback, **NOT** the `--review` artifact guard and **NOT** the re-stamp of the four
existing records. Approving a new guard is not approving a change to how old records are graded.
