# The skipped closed day renders client cash as performance -- and the new adapter has the same shape -- 0.4.0_DS_ClientPlatform~S

**archetype:** DIAGNOSE

**Date:** 2026-09-30
**Task Order:** none held (TO-IB-pr-263 superseded @ed0be5b557); off-task finding + read-in for IRPT_DASHBD wsB r1
**Status:** COMPLETE for this block
**Workspace CLOUD commit:** `58a8c9e489` (row S237). LOCAL; origin/CLOUD `410818259a` by `git ls-remote`.

---

## Objective

Andrew approved the `/next-calls` sequence (OPTION 2 then OPTION 1). OPTION 2 was to give the
non-trading-day observation its own carrier. Grounding it turned a partition-inventory note into a
measured served-data defect, so the block is mostly that. OPTION 1 was the read-in for the inbound
IRPT_DASHBD workstream B order, which landed as a decomposition mid-block.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read | `comp-read IRPT_DASHBD_PRD.md --for "..."` | PASS | Surfaced C-METHOD and C-GUARD from a 346-line PRD in one call; C-METHOD is what connected S237 to my own next cell. |
| comp-read | `comp-read IRPT_DASHBD_DECOMP.md --for "..."` | PASS | Gave the seating line (`DB-b-1` and `DB-b-3` to this lane) and the acceptance window. |
| comp-read | `comp-read pipeline_cli.py --for "..."` | PASS | Found `cmd_postdeps:3536`'s `UNCOVERED` branch, which is what makes the gap below a real defect rather than a correct refusal. |
| comp-pipescript postdeps | `postdeps c02_twr_engine.py --firm 49financial` | FAIL | `--firm` enum is `{bd,inf,cot,mdpf}`; `advi` absent. See Gap. |
| rail (comp-tool HUD) | two denied segments | PASS | Correctly refused `comp-read ... | head` twice. Both were mine piping a census into a receiver that erases its denominator. The rail was right; I re-ran with the tool's own output. |

**What worked:** `comp-read --for` three times, each replacing a multi-file read with one call. The
PRD read is the one that mattered: it turned an IRPT_BCKEND finding into a pre-build warning on my
own next cell, which is value the finding would not have had an hour later.

**What failed:** `comp-pipescript postdeps --firm` rejects `advi` at argparse.

**Gap found:** `postdeps` already HAS the right verdict for an unconfigured tree -- `cmd_postdeps:3536`
prints `UNCOVERED: tree {firm!r} has no postdeps config registered`, and `mdpf` sits in the enum
precisely so it can report that honestly. `advi` is not in the enum, so the call dies at argparse with
a message that blames the caller -- the exact class `pipeline_cli.py:4140` warns about ("THAT MESSAGE
IS FALSE FOR THOSE TREES, and falsely blames the caller"). The one-word fix is admitting `advi` to the
enum so it reports UNCOVERED. NOT TAKEN: I hold no order on that file and it is another seat's tool;
surfaced here and carried into the DB-b-1 report, where it bites -- the DS role minimum names
`postdeps` before any ad-hoc run, and DB-b-1 is explicitly an ad-hoc round-1 run.

---

## Work Completed

### 1. Row S237 -- the closed day orphans its flow_ledger (the block's real finding)

Grounding S236's "2025-01-09 is not a trading day" produced a chain of measurements that ended
somewhere I did not expect:

| step | measurement |
|---|---|
| chain-wide sweep | 26,078 keys, 23 date-partitioned tables under `gold/advi/`. Each of the 18 CHAIN tables holds EXACTLY ONE non-NYSE-trading-day partition, and it is `2025-01-09` in every one. (`reference/bd_legacy_*` are calendar-day-partitioned legacy snapshots, excluded by name.) |
| is the day real? | `canonical_valuation` 2025-01-09 is 98.3% identical to 01-08 (4,717 of 4,801); the 84 that differ move $3,116,562.14 absolute, large deltas at round figures, median $49.26. A custodian book moving on a BANK day while the NYSE was shut. Real data, not fabrication. |
| the mechanism | `dim_calendar` correctly omits 2025-01-09, so `prev_map['2025-01-10'] = '2025-01-08'` and c02 takes BMV from 01-08. But `c02_twr_engine.py:460` reads `flow_ledger/date={args.date}` -- **date D only**. 2025-01-09's own run emitted 4,808 of 4,808 `NO-PRIOR-TRADING-DAY`, so it consumed no CF either. The skipped day's flows are read by NOBODY. |
| the harm, served | Account `0093614544`: $1,125,000.00 EXTERNAL deposit on 2025-01-09. Served `twr_daily` 2025-01-10: status OK, bmv $1,995,191.90, emv $3,114,480.00, **cf_net $0.00**, r_net **+56.10%** for one day. |
| the population | 46 accounts with orphaned CF ($2,890,299.37 abs) under c02's own account-grain filter; 44 carry a served OK return on 01-10. Error max **+91.13 pp**, median 1.34 pp, 22 accounts over 1 pp, 13 over 10 pp, against 4,091 OK returns served that day. Both signs occur. |

Filed as `IRPT_BCKEND-S237`, class BLOCKING, `hazard_standing` ARMED, `disarm_owner` `2.0.0_SA_COO~P`.
Committed `58a8c9e489`, `surprise-row-gate` PASS.

**Not resolved, and named in the row as the thing that decides the blast radius:** whether the error
propagates into PERIOD returns. `link_geometric:286-291` refuses a window containing any non-OK
subperiod, and 2025-01-09's partition is 4,808 of 4,808 non-OK -- so if callers load by partition
listing the harm stops at the daily grain (a protective accident), and if they enumerate trading days
from `dim_calendar` the hole is invisible and the error flows into every spanning window. I did not
read the five live callers.

### 2. Read-in for IRPT_DASHBD workstream B round 1 -- and the connection

The decomposition landed mid-block (`b6cfb3316e`, 15:5xZ). **`DB-b-1` and `DB-b-3` are seated on this
lane**, citing pr-263's supersede. `DB-b-1` is the 49F adapter into gold `account_return_daily` under
its contract with C-GUARD; acceptance is the five sample accounts over **2024-07-09 .. the frontier**,
which spans 2025-01-09.

The PRD's **C-METHOD** binds `r_t = (V_t - F_t) / V_(t-1) - 1` with daily returns geometrically linked
-- the same form as the retiring engine. C-SHADOW confirms `c02_twr_engine.py` is "prior art, not
imported", so this is a fresh build: the defect is a design risk to avoid, and the right moment to say
so is before the cell is cut.

I then removed the conditional from that warning by measuring the adapter's own inputs:
**16 of 20 Schwab silver tables under `s3://opal-data-assets/schwab/08335338/silver/` hold a
`date=2025-01-09` partition -- including `dim_position`, `dim_balance` and `fact_trn`, exactly the
three inputs C-ADAPTERS names for the 49 Financial adapter.** Each of the 16 has exactly one
non-NYSE-trading-day partition and it is that date. The four with none are the low-frequency tables.

So if `DB-b-1` enumerates trading days from `trading_calendar` (which C-METHOD's geometric linking
requires) and reads `fact_trn` at date=D only, the new table reproduces S237 on day one, inside its own
acceptance window. Sent to `2.0.0_SA_COO~P` before the cut, with one ask: let the cell's face say how
`F_t` is gathered.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Escalate S237 to BLOCKING/ARMED rather than file it as the OBSERVATION I set out to write | The measurement changed the finding's class. Served client returns are wrong by up to 91 pp; that is not an observation. |
| Do not disarm it this turn | No act under this lane's own grant corrects the served rows: a re-emit needs a ruling on WHICH remedy, and I hold no order on that table. Named in `disarm_owner` instead of pretending otherwise. |
| Recommend remedy (1) and warn against (3) in the row | Deleting non-trading-day partitions looks tidy and DISCARDS $2.89M of real custodian flow. Reading `flow_ledger` across `(prev_trading_day, D]` fixes the class, not just the instance. |
| Send a second message to ~P on the same subject | Message discipline is one ask per message; this was the same ask with the discriminator that decides it, and the order was being cut in that window. Timing beat tidiness. |
| **Drop OPTION 3** from the approved sequence instead of executing it | The `REFUSED-NO-BMV` status-vocabulary finding sits on `c02_twr_engine`, which C-SHADOW names as the retiring engine and whose reader ~P just ruled no longer serves 49F. Executing it would have been dead work on a retiring surface. Reported rather than silently skipped. |
| Surface the `postdeps` gap, do not fix it | Another seat's tool, no order held, and CLAUDE.md forbids manufacturing friction. It rides with the DB-b-1 report where it actually bites. |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md` | Appended row `IRPT_BCKEND-S237` (+34 lines) | Yes -- `58a8c9e489` |

**No production file changed. No S3 object written.** Every measurement in this block was a read.

---

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| Row S237 (the carrier) | `.../IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md` | `2.0.0_SA_COO~P` (disarm owner), `1.0.0_SA_CTO` (method) |

---

## Blockers

None at this lane. `DB-b-1` and `DB-b-3` are seated here and the order has not yet landed; `2.0.0_SA_COO~P`
said no act is owed until it does.

---

## Current State

`IRPT_BCKEND-S237` at `58a8c9e489` is a live BLOCKING/ARMED row against served 49F data: 44 account
returns on `s3://opal-data-49financial/gold/advi/canonical/twr_daily/date=2025-01-10` carry client cash
flows as performance, up to +91.13 pp, because the 2025-01-09 NYSE closure is skipped by the calendar
while its `flow_ledger` partition exists and is read by nothing. `2.0.0_SA_COO~P` holds it and has been
told twice, the second time with the measurement that it reproduces in `DB-b-1` unless that cell's face
says how `F_t` is gathered. This lane is seated on `DB-b-1` and `DB-b-3` of IRPT_DASHBD workstream B
round 1 (decomp `b6cfb3316e`) and is read in on the PRD's contracts, awaiting the order.

---

## Next Steps

1. **[`2.0.0_SA_COO~P`] Read S237 before cutting DB-b-1** -- and state in the cell's face whether `F_t`
   is gathered over `(prev_trading_day, D]` or at date=D only. The second choice reproduces the defect.
2. **[`2.0.0_SA_COO~P`] Disarm S237** -- rule the remedy for the served 2025-01-10 rows. Three candidates
   with costs are in the row; I recommend reading `flow_ledger` across the skipped span plus a re-emit of
   2025-01-10.
3. **[`0.4.0_DS_ClientPlatform~S`] Read the five twr_daily callers** -- `perfrp_emit_core`,
   `perfrp_rollup`, `parity_period_returns`, `c04_validation_battery`, `holdings_performance.py` -- to
   settle whether period returns inherit the error. Cheap, and it is the number the disarm owner needs.
   Not started: it is off any order I hold, and S237 names it as the owner's first act.
4. **[comp-tool owner] Admit `advi` to `comp-pipescript postdeps --firm`** so it reports `UNCOVERED`
   (the branch already exists at `cmd_postdeps:3536`) instead of dying at argparse and blaming the caller.
