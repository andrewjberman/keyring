# PENDING -- mdpf known-bad-dates STAMPING is COMMITTED but NOT IN FORCE

**Opened:** 2026-08-20T~0007Z by `2.0.0_SA_COO`. **Producer-owner:** `0.4.0_DS_ClientPlatform`
(self-flagged; the honesty is theirs, the carry is mine).

## The gap, stated as Rule 22a's CODE layer
`mdpf_aggregate_aua.py` now carries `KNOWN_BAD_INPUT_DATES` (enumerated literal, never a predicate;
LABEL not exclude; retirement condition NEVER; kind declared `CLOSED-PERIOD-IMMUTABLE` per Rule 25's
ratified vocabulary). Landed **@4a032871a4**.

⛔ **THE CODE IS COMMITTED. THE PRODUCER-SIDE STAMPING IS NOT EXECUTING.** `mdpf_aggregate_aua` runs
**bundled inside `mdpf-gold-lambda`**, so a repo commit does not reach the executing plane. This is
the same family as tonight's instrument-repair batch: **a record that reads authoritative --
committed, tested, idempotent, value-identity proven -- while the RUNNING BYTES know nothing about
it.** DS explicitly did NOT claim it was in force; do not let a later reader infer that it is.

## What IS live (do not re-do)
The **two existing artifacts for 2026-08-09 / 2026-08-10 ARE stamped** -- written directly, under a
precondition gate that refuses unless `opal_aggregate_aua==0` AND vintage `UNKNOWN` AND
`partners==0`, with a per-file value-identity proof (`ADDED=={data_quality}`, `REMOVED==[]`,
`CHANGED==[]`), read back after write, idempotent on re-run. Control: 2026-08-11 left unstamped and
still carrying its real $1,786,248,242.08.

## Disposition -- RIDES THE NEXT `mdpf-gold-lambda` PACKAGE REBUILD. No special deploy.
Deliberately proportionate, and the reasoning is the part to inherit: the gap bites **only** on a
future date where **all six feeders are absent** (one prior occurrence, 08-09/08-10 consecutive).
Its failure mode if it recurs unstamped is **an unlabelled $0 partition -- which is the status quo**,
detectable by the same drive read that found it, and manually recoverable by the same stamping act
already proven. **Forcing a deploy for a low-frequency labelling improvement would be
disproportionate; losing the item would not be acceptable. Hence: carried, not cut.**

## The close condition
`mdpf-gold-lambda` package rebuilt + deployed -> **verify on the EXECUTING plane, not the repo**
(Rule 22a: the deployed package's own bytes must contain `KNOWN_BAD_INPUT_DATES`; a plan 0-diff and
a green run both pass on the old code). Then delete this file.

## ⛔ THE CLASS IS NOW FOUR MEMBERS, AND ITS SEVERITY IS NOT FLAT (added 2026-08-20 ~0130Z)
Tonight produced four committed-not-deployed instances. **Three were RECOVERABLE** -- code sitting
undeployed, found later, deployed later, nothing lost in the interval:
1. this one (`mdpf_aggregate_aua` known-bad stamping, bundled in `mdpf-gold-lambda`)
2. `build_fact_taxsma_report.py` + `build_dim_taxsma_report.py` (silver/gold, since minted)
3. WS-R3's registry read in `opal-assets-bd49f-reporting-pull` (~29 days, since deployed)

**THE FOURTH IS NOT RECOVERABLE AND IT NEARLY SHIPPED.** `TS_HOLDINGS_ENABLED` read **2 in repo, 0 in
the deployed package**. COO sequenced the TrueShares enable as *"a ONE-LINE env flip"* (DS relayed it
identically -- both readings taken from the repo plane). **A flag-only apply would have succeeded:
clean apply, 0-diff, variable visible in console, GREEN run at 22:00Z -- fetching NOTHING.** On a
**current-day-only, forward-only source** that is not "not working yet"; it is **PERMANENT DAILY DATA
LOSS BEHIND A HEALTHY GREEN.** Caught by `0.7.0_AE_CloudOps` reading the deployed package before
arming; landed instead as **one atomic apply** (code + flag together), verified on both planes.

> **THE DISCRIMINATOR THIS ADDS, AND IT IS THE POINT OF THE ENTRY: A COMMITTED-NOT-DEPLOYED ITEM'S
> SEVERITY IS SET BY WHETHER ITS UNDERLYING SOURCE IS REPLAYABLE.** Against a replayable source the
> gap costs latency. Against a **forward-only** source it costs data that cannot be re-fetched, one
> day per day, while every instrument reads healthy. **Triage this class by source replayability
> FIRST, not by how stale the artifact is** -- the freshest instance here was the dangerous one.

**AND THE URGENCY WAS THE HAZARD'S CARRIER, NOT ITS COUNTERWEIGHT.** The reason the TrueShares ask
reached Andrew at all is that the feed loses unrecoverable history daily -- and that same urgency is
what justified jumping it ahead of the TAXSMA chain and would have pushed a flag-only apply out the
door unread. **A correct priority and a plane-wrong instruction compose into a fast mistake.**

## Why this file exists at all
I told DS, in the same turn, that **a gap that lives only in a message evaporates; a gap in the
close is inherited.** This is me holding to that on my own side rather than trusting a drive log I
may not re-read. DS carries it in their TO close; I carry it here.
