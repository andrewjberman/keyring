# ADDENDUM — C02-g-7 HALTED at a06, and the 12:50Z read this seat owes

**Date:** 2026-08-30 · **Seat:** `0.7.0_AE_CloudOps~L` · **Cell:** C02-g-7 (B-4)
**Status:** HALTED. Date 1 PARTIAL. One timed obligation outstanding.

> **WHY THIS FILE EXISTS.** The obligation below fires at **12:50Z**, roughly 4.5 hours after it
> was incurred, and this session may not survive that long. A duty that lives only in a broker
> thread and one agent's context is a duty that quietly lapses. This is its durable carrier.

---

## ⏱ THE OBLIGATION — READ THE 12:45Z FIRE AT 12:50Z, 2026-08-30

The issuer deliberately did **NOT** hold the floor (`2.0.0_SA_COO` 86470): the Sunday fire is the
**falsifier** for this seat's prediction, and holding it would have hidden the natural evidence.

**THE PREDICTION, on the record at 86456 before the event:** today's 12:45Z fire **aborts at
`a06_dim_identity_crosswalk`** on the empty Saturday allocation map, and produces nothing
downstream.

**HOW TO READ IT — and the instrument matters:**

```
gold/advi/_logs/chain_<ts>.log        <- THE COMPLETE RECORD. Read THIS.
aws ssm get-command-invocation        <- truncates stdout at ~24 KB; the abort line
                                         fell PAST the cut on date 1 and was invisible.
```

**WHAT FALSIFIES IT:** a **populated** `fact_allocation_account_map` partition for `2026-08-30`
landing **before** 12:45Z. The map lands ~13:15–13:17Z daily, i.e. *after* the fire — which is
the whole mechanism — so falsification requires an off-schedule write. Check the map's newest
partition size before concluding: **4,507 B = empty (header-only); ~775–780 KB = populated.**

**THE OTHER WAY IT IS FALSIFIED:** `0.4.0_DS_ClientPlatform~N` deploys the a06 fix and it is read
on the running artifact before 12:45Z. Then the fire becomes the fix's first scheduled exercise
instead, and the read reports *that* — not a silent pass.

**REPORT TO:** `2.0.0_SA_COO`, `1.0.0_SA_CTO`, `3.0.0_SA_CVO`, `0.4.0_DS_ClientPlatform~N`,
`0.0.0_AB_MSTR` (that seat carries the Andrew-facing line).

---

## THE FINDING THIS CAME FROM

`a06` reads the **newest** allocation-map partition regardless of the chain's date. Census of all
46 partitions of `s3://opal-data-assets/smartx/platform/silver/fact_allocation_account_map/`:

| | count | weekdays |
|---|---|---|
| EMPTY (4,507 B) | 13 | **Sat 7, Sun 6 — every one** |
| POPULATED (~778 KB) | 33 | Mon–Fri — none |

The map lands **after** the 12:45Z fire, so the fire always reads *yesterday's* map.

⛔ **CORRECTED 2026-08-30T08:2xZ — I FIRST WROTE THIS AS A SUNDAY-ONLY HAZARD. IT IS SUNDAY *AND*
MONDAY.** Propagating the measured empty set (Sat, Sun) through my own stated mechanism:

| fire day | reads map of | map state | outcome |
|---|---|---|---|
| **Mon** | Sun | **EMPTY** | **ABORT at a06** |
| Tue–Sat | Mon–Fri | populated | runs |
| **Sun** | Sat | **EMPTY** | **ABORT at a06** |

**Two fires abort per week, not one.** I had the Sat+Sun empty census and the "fire reads
yesterday's map" mechanism in the *same message* and propagated only one of the two forward.
Caught by `0.4.0_DS_ClientPlatform~N` 86498 — who did better than correct the reasoning and went
to the logs.

⛔ **AND IT IS NOT A PREDICTION AT ALL — IT HAS ALREADY FIRED TWICE IN PRODUCTION.** That seat
censused every floor-form chain log and found **Sun 2026-08-23 and Mon 2026-08-24 both ABORTED at
`a06_identity_crosswalk`**. So today is the *third* instance and tomorrow is the *fourth*. My
"masked by the hold" reading was wrong for those two dates: they were not masked, they failed in
the open and nothing read the logs.

**DISARMED to `0.4.0_DS_ClientPlatform~N`** (a06 is a DS-lane gold stage, Rule 13). *Disarmed is
not remediated.* The guard that fired is **correct** — it refused to build a crosswalk from an
empty map rather than writing an empty one.

---

## STATE OF C02-g-7 AT THE HALT

- **Date 1 (`2026-08-11`) PARTIAL** — 6 of 16 tables written before the abort:
  - NEW KEYS: `dim_account` 08:03:31Z · `dim_relationship` 08:03:32Z · `ref_txn_classification` 08:04:30Z
  - DECLARED OVERWRITES (admitted by the gate at 86149 (A)): `dim_boundary` 08:04:27Z · `dim_security` 08:04:28Z · `dim_calendar` 08:04:29Z
- **Prior VersionIds captured BEFORE the send** → `scratchpad/g7_before.json`; the CVO before/after
  content diff is still computable and nothing is unrecoverable (versioned bucket).
- **Dates 2–5 NEVER SENT.** Re-driving now would abort at the same stage on every one of them —
  a06's read does not depend on the chain date.
- **No `twr_daily` partition was touched. No partition outside `2026-08-11` was touched.**
- **Ledger `20260830T0554Z_advi-49f-c02g7-five-date-forward-production` stays OPEN**, G1 CLOSED
  (the date-list control passed at send time), G2–G6 open. Not closed on a halt.
- **Re-drive is idempotent** from date 1 once a06 is resolved.

## THE OPEN CLAIM THIS RUN COULD NOT TEST

I claimed `bridge_group_account` and `dim_portfolio_group` are NOT chain-written, falsifiable as:
after a **full** date completes they must hold zero partitions at the five dates. **This run does
not test it** — it stopped at stage 6 of 17, and their absence is what a chain halted that early
predicts under either hypothesis. The inclusion of `ref_txn_classification` in the 16 IS empirical
(the chain wrote it at 08:04:30Z, `STAGE OK a05_ref_txn_class`); the exclusion of the other two
remains inference until a full date lands.

---

## ⛔ UPDATE 09:25Z — THE SECOND FALSIFIER BRANCH FIRED. READ THIS BEFORE THE SECTIONS ABOVE.

Everything above was written at 08:2xZ, when the a06 fix did not exist. **It is now stale in its
framing, and this section governs where the two differ.** The file is kept whole rather than
rewritten, because the superseded prediction is part of the record.

**WHAT CHANGED.** The section "THE OTHER WAY IT IS FALSIFIED" anticipated exactly this and it
happened: `0.4.0_DS_ClientPlatform~N` served the a06 fix at **2026-08-30T08:42:34Z**, four hours
before the fire. Verified independently at this seat, not accepted on report — md5 recomputed from
the downloaded bytes `f8763326799bba70dac9edf5c55bdaf8` = the ETag, 11,148 B, 0 CR, VersionId
`mUbfPzyUaEiYJPVJ2jbhmG4QbocOgg_N`, sitting above the 6,263 B 2026-08-19T01:22:34Z baseline that
aborted on 08-23 and 08-24.

**SO THE 12:50Z READ IS NO LONGER AN ABORT PREDICTION.** It is the fix's **first SCHEDULED
exercise**, sitting on top of six ad-hoc ones this seat already ran (five chain dates + the 08-18
mirror-pull), all of which passed.

### WHAT TO EXPECT AT 12:50Z, and what would be a finding

Grounded on the map plane read at 09:2xZ — newest partition `date=2026-08-29` **4,507 B
HEADER-ONLY** (landed 08-29T13:17:42Z), `date=2026-08-28` **779,487 B POPULATED**. The 08-30 map
lands ~13:16Z, i.e. *after* the 12:45Z fire, so the fire still reads a weekend partition. Expect:

```
map resolution: chose date=2026-08-28 of 46 partition(s); SKIPPED header-only: 2026-08-29
map date=2026-08-28: 7,359 rows | ... | map_carried=True
STAGE OK a06_identity_crosswalk rc=0
```

**A FINDING, reported as one, would be:** a06 aborting anyway · a different `map_date` ·
`map_carried` false · `2026-08-29` selected. Those are findings **against the fix**, owned by
`0.4.0_DS_ClientPlatform~N` (M-4), not against this campaign.
⚠ The Sunday fire derives **D = 2026-08-28** (the most recent trading day), as Saturday's did — so
it is expected to REWRITE the 08-28 partitions. That is normal floor behaviour, not a finding.

**INSTRUMENT, unchanged and still the whole point:** `gold/advi/_logs/chain_<TS>.log` (floor form,
no date segment). **NOT** SSM stdout — it truncates at ~24 KB and the original abort line fell past
the cut, which is why the halt was invisible on the first read.

### THE OPEN CLAIM ABOVE IS NOW SETTLED — by measurement, not by inference

The final section says `bridge_group_account` and `dim_portfolio_group` being chain-written could
not be tested by a run that halted at stage 6 of 17. **Five complete dates have now landed.** Both
prefixes gained **zero** keys and zero partition-dates across all five, while 16 of 23 prefixes
gained keys and no date outside the five was touched. The exclusion is now **empirical**, and the
16 IN / 7 OUT list is confirmed on two independent axes (object counts and distinct dates).

### STATE AT THIS UPDATE

C02-g-7 **CLOSED**: B-1..B-6 all PASS, proof instance VALID rc=0 read unpiped @`3948c766a7`, deploy
ledger `20260830T0554Z` CLOSED with all six legs proven and its sentinel removed. The five dates
exist; 2026-08-18 moved from 0 OK rows to 6,382. **The 12:50Z read is the only obligation left, and
it is TIMED, not blocked.**
