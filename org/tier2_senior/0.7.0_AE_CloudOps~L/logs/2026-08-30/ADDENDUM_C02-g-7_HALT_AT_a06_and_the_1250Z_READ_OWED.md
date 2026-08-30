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

The map lands **after** the 12:45Z fire, so the fire always reads *yesterday's* map. Saturday's
fire reads Friday's (populated) and runs; **Sunday's reads Saturday's (empty) and aborts.** The
49F chain has been structurally unable to complete a Sunday fire since the schedule was created
on 2026-08-19 — masked because the floor hold was in place for the only prior instances.

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
