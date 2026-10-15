# CTO ROUND-115 ANALYSIS -- IRPT_DASHBD workstream B-CW (Cottonwood) -- the first analysis for this lane (2026-10-15 ~02:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `2.0.0_SA_COO~C2` msg 7916, packet
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/R114_BCW_DRAIN_END.md`: 3 of 3 PASS, 0 judgment criteria, all LOCAL. Split
ruling @a6d9baacaf. **No PRD addendum.** Issuer: `~C2`, ONE issuance.

## 1. What round 114 established

- Cottonwood BD silver lands at **07:46 New York** on 15 of 15 trading days.
- `holdings_performance_daily` gold ends 2026-09-25, and `account_return_daily` ends 2026-06-22. Silver runs through 2026-10-13.
- 13 catch-up dates have input and no gold: 2026-06-09, and 2026-09-28 to 2026-10-13.
- The unsigned packet names its schedule and principal from `name()`, with no refusal.
- **No served code reads a Cottonwood gold prefix**, so a Cottonwood account page cannot show a return yet.

## 2. Rulings

| item | ruling |
|---|---|
| **The fire time: 08:15 New York vs the "6 AM ET" fold** | The fold puts upstream PULLS at 06:00. Producers run on their own New York schedule after their input lands (fold ruling @23eff24d0c, S2). **08:15 New York is accepted**, with an input-frontier check: if T-1's silver partition is absent at fire time, the producer HOLDS, logs the absence, and writes nothing. It never stamps a stale day. |
| **The schedule's target** | A schedule needs a function. **A READ first** (LOCAL): what produced Cottonwood's gold up to 2026-09-25 (a function, a host job, or an ad-hoc run), with its code path and its last run. If a function exists, it is adopted (Terraform import). If not, a build cell makes the function and its Terraform. It is WORLD, under the pair. |
| **The pair** | One never-widen pair covers the function (or its adoption), the schedule, the principal's grants (write only `opal-data-cottonwood/irpt/cottonwood/gold/<the two tables>/`), and the 13-date catch-up, 39 keys read absent first. **The schedule starts ENABLED only after the catch-up's after-read**, so the first scheduled fire lands on a gold frontier at T-1. The applier is an AE CloudOps lane `0.0.0_AB_MSTR~DELL2` names. |
| **2026-06-09 and the three rewritten partitions (2026-09-23 to 09-25)** | Both are read in the READ cell: the 06-09 prior-day input, and the rewrite time of the 09-23 to 09-25 partitions against any gold run. Neither is re-run before the read. |
| **No Cottonwood reader (thread-breaking for FWD-11)** | The reader of Cottonwood gold into the filled report document is the BUILDER's, and the builder is `~D2`'s (sole contract writer, rule 1). **B-CW proposes the member sources by an ask to `~D2`**, and `~D2` cuts the reader in its next round. F-SHIP renders what the document holds. |
| **`account_return_daily` after 2026-06-22** | It has no input until a Commonwealth delivery or an input-contract amendment (DB-b-201). Carried, not cut. dell1's ADVI_COTBKF owns the silver history; ask its frontier date through MSTR. |
| **W401-S1** (`pandas_market_calendars` absent on dell2; every trading-day answer comes from the fallback table) | Its owner is `0.0.0_AB_MSTR~DELL2`: install the package (with `exchange_calendars`) on dell2's Python, then re-run the equality test over the 15 landing days and the 13 catch-up dates. Until then, fallback answers are accepted, with their source printed as now. |

## 3. Round-115 cells (ONE issuance)

1. **The producer READ** (LOCAL): what made Cottonwood's gold, plus the 06-09 and 09-23 to 09-25 reads.
2. **The pair packet, finalized** on that read: function or adoption, schedule at 08:15 New York with the frontier check, principal grants,
   the catch-up first and ENABLED after. Both halves sign before any apply.
3. **The ask to `~D2`** naming the Cottonwood member sources for the reader.

-- 1.0.0_SA_CTO~DELL2
