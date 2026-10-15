# IRPT_DASHBD -- decomposition, workstream B-IN (Inflection), issuer 2.0.0_SA_COO~I2

This file is the B-IN workstream's own decomposition. The shared file `IRPT_DASHBD_DECOMP.md` stays `2.0.0_SA_COO~D2`'s (workstream B, its
sections 1 to 115), so two issuers never append to one file. Cell ids here are `DB-i-<n>`; worker slots `~301` and up are this seat's
(D2's run `~184` and up; the two ranges do not meet). Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md`
(@a6d9baacaf) and msg 7899. FWDs are unchanged; no PRD change.

## 1. ROUND 114, WORKSTREAM B-IN (2026-10-15 ~01:4xZ)

**Where B-IN stands (measured from the tree, not from a status word).** The Inflection adapter (account_dim, household key) is done in rounds
108-109. The sample (DB-b-222) and the render (DB-b-223) passed the CVO's regrade (round 111 J1 PASS). The household return comes from Orion's
client-grain factor (contract 0.5.0). What is NOT done: Inflection's ACCOUNT-grain return. Round 109's derivation (`DB-b-216`, record
`deliverables/0.9.0_WK_IRPT_DASHBD~174/TWR_TIEOUT_R109.json`) derived 926 accounts and tied the accounts, aggregated per client, to Orion's client
return: QTD compares 287 of 320 households, of which 16 sit under 5 bp, 87 at 5 to 25 bp, 175 at 25 to 100 bp and 9 at 100 bp or more; YTD, the last
12 months and since inception compare NONE. The CTO's round-109 analysis ruled "this seat rules the tolerance on that read" and the account pages
stay "Account-level returns are not available for this firm yet." until it does. Two open rows block the ruling: `IRPT_DASHBD-D2-W174-S2`
(Orion has no `fact_positions` partition for two NYSE trading days, so every longer window is not comparable) and `IRPT_DASHBD-D2-W174-S5` (rows with
`isActive` false carry non-zero value and the value basis includes them until the CTO rules).

**Round 114 is the two reads that make the CTO's tolerance ruling possible. Both are LOCAL, both are reads, and nothing is written to AWS.**

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-1` | The QTD tie-out under three value bases: all rows (round 109's basis, the control), active rows only, cash lines excluded. Per basis the gap distribution; the count of households that move down at least one bin against the control | FWD-2 | LOCAL (a read; a private table; counts only in the repo) | none | I-A |
| `DB-i-2` | The two missing `fact_positions` days: whether any Orion layer holds them (every silver table, and bronze under the granted prefix), whether each is a trading day, how many accounts a bridge across the gap would touch and how many of those had an external flow in the gap, and the producer and schedule that writes the Orion silver | FWD-2 | LOCAL (a read) | none | I-B |

**Decisions inside this decomposition (the issuer's, stated).** (a) Cell `DB-i-1` reuses round 109's cached per-account-day values
(`positions_daily_cache.parquet`, a private file with the value under three bases already summed), so it reads `fact_transactions` and `fact_performance`
once each and no positions partition; the control criterion makes the `all` basis reproduce round 109 household by household, so a wrong reuse fails.
(b) Only QTD is re-run: it is the only window with any comparable household, and YTD, 12 months and since inception wait on `DB-i-2`'s answer.
(c) `DB-i-2` measures the bridge's exposure and does NOT bridge: whether a no-flow link across a missing day is an admissible method is the CTO's
ruling on the read. (d) The enrichment that follows the ruling (the tolerance applied, the account pages switched to derived figures, the gold
partition and its schedule) is NOT cut now: each waits on the CTO's tolerance ruling, and the gold partition is a WORLD act under a never-widen pair.

**fanout:** 2 of 2 chains, cap 8, reason: the two cells are dependency-independent with disjoint write sets (each its own worker folder and private folder). Workers `0.9.0_WK_IRPT_DASHBD~301` (`DB-i-1`) and `~302` (`DB-i-2`).

## 2. ROUND 115, WORKSTREAM B-IN (2026-10-15 ~02:3xZ, issuer 2.0.0_SA_COO~I2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_115_20261015.md`, msg 7956, answering the round-114 drain-end packet @fe51225396: 2 of 2 PASS, 0 judgment criteria)

The CTO's one cell is cut as ONE order. No tolerance is set and the account pages stay `NO_SOURCE_YET`; no no-flow bridge across a missing day (windows over 2026-07-01 and 2026-09-28 carry `SOURCE_BREAK` words until `~P2`'s re-pull); the two missing Orion days are `~P2`'s (msg 7913).

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-3` | The gap decomposition read: about 12 households across the QTD gap bins (every household at 100 bp or more plus the lowest-sha household of each other bin), five named differences between the Opal derivation and Orion's client factor each tested ALONE against the round-109 baseline (gross against net of fees, trade against settlement date, flow timing inside a day in two forms, income accrual, the cash sweep in two forms), and the explained share per household per variant | FWD-2 | LOCAL (a read; a private table; counts, bp and shares only in the repo) | none | I-C |

**Decisions inside this decomposition (the issuer's, stated).** (a) The sample is a RULE, not a choice, so the checker recomputes it from round 114's private variant file (all 9 households at 100 bp or more, plus one per other bin: 12). (b) The differences are tested through nine variants (`base`, `identity`, `gross_fees`, `settle_timing`, `flow_start_of_day`, `flow_midday`, `income_accrual`, `ex_cash_value`, `ex_cash_no_flows`): the CTO's "flow treatment inside a day" and "cash sweep" each take two forms so a single reading is not mistaken for the difference. `identity` is the difference control: a variant that changes nothing must change nothing. (c) A difference the Orion frame cannot support (no settlement-date column, no accrual date) is reported NOT_TESTABLE with the reason in words, never invented. (d) The share is the SIGNED form `(base - variant) / base`, unclipped, so an overshoot or a widening is visible.

**fanout:** 1 of 1 chains, cap 8, reason: one independent read cell with a disjoint write set (its own worker folder and private folder). Worker `0.9.0_WK_IRPT_DASHBD~303` (`DB-i-3`).

## 3. ROUND 116, WORKSTREAM B-IN (2026-10-15 ~03:2xZ, issuer 2.0.0_SA_COO~I2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_116_20261015.md`, msg 7978, answering the round-115 drain-end packet @d64cf8f469: 1 of 1 PASS, 0 judgment criteria)

The CTO's one cell is cut as ONE order. The ruling: stop reconstructing Inflection account returns; read whether Orion itself exposes an account-level performance series. If it does, `~P2` adds that feed to the Orion pull under a never-widen pair and the accounts switch to Orion's figure (`source: orion`); if not, the account pages stay `NO_SOURCE_YET` and the reconstruction is not shipped. The round-114 and round-115 decomposition stays recorded as the reason.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-4` | The Orion account-level performance read: the endpoint, the grain, the fields (return, period, gross or net) and whether the pull's credential reaches it, from the estate's pull code, the investor-reporting performance adapter, its fixtures and the repo docs; the endpoint inventory of those directories as the denominator | FWD-2 | LOCAL (a read of repo code and docs; no vendor call, no AWS call, no secret read) | none | I-D |

**Decisions inside this decomposition (the issuer's, stated).** (a) The CTO's phrase "as the existing pull reaches it" is read as BOTH code families that reach Orion: the `inf-pipeline` pull that feeds the silver, and the investor-reporting performance adapter, whose header already names `POST /api/v1/Reporting/Scope` with "native household and account scopes"; the answer to "does the pull call it" and "does the estate already hold it" are different facts and the order asks for both. (b) The endpoint inventory is the DENOMINATOR (every `/api/vN/` literal in the `*.py` files directly inside each `inf-pipeline` directory and the performance directory), so a "no such endpoint" cannot rest on a partial read. (c) The credential question is answered from code only, since the CTO ruled no new vendor call; the record names the secret and never reads it, and says what the code cannot prove. (d) Each section carries a claim word and verified evidence lines (the checker opens each cited line and requires the quote on it).

**fanout:** 1 of 1 chains, cap 8, reason: one independent read cell with a disjoint write set (its own worker folder). Worker `0.9.0_WK_IRPT_DASHBD~304` (`DB-i-4`).

## 4. ROUND 117, WORKSTREAM B-IN (2026-10-15 ~03:3xZ, issuer 2.0.0_SA_COO~I2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_117_20261015.md`, msg 7985, answering the round-116 drain-end packet @e14658f347: 1 of 1 PASS, answer YES)

The CTO's one cell is cut as ONE order. The ruling: Scope (not ExcelReports) is the source for Inflection account returns; ONE probe settles the three unknowns of round 116 (does the Account grouping return one group per account with a daily series for a multi-account household; is the fee flag honoured; is the credential accepted and from which store). If (a) and (c) pass, `~P2` adds the feed in the Orion pair and the accounts show Orion's figure with the fee basis stated; if (a) fails, one call per account if `~P2` costs it acceptable.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-5` | The Scope probe: the household (lowest-sha with 2 or more accounts), at most 4 paced POSTs to `/api/v1/Reporting/Scope` (fee flag false, then true) over 2026-10-01 to 2026-10-13, the raw responses private, three verdicts recomputed by the checker from the saved bodies | FWD-2 | WORLD (a vendor read: no write, no deploy; the output is LOCAL) | none | I-E |

**Decisions inside this decomposition (the issuer's, stated).** (a) The class is WORLD, the CTO's own word ("a WORLD read, LOCAL output, no write"), though no infrastructure path or deploy verb forces it: a call to the vendor with the estate's credential is not a LOCAL record. (b) The household is a RULE (lowest sha256 among households with 2 or more accounts in the private dimension), so the checker recomputes it and the worker cannot choose a convenient one. (c) The three verdicts are defined by exact rules over the saved response bodies, so the checker recomputes them without a vendor call; the fee verdict `NET_WHEN_FALSE` needs the gap to tie to the summed `feeAmount` over the start value, as the CTO's ruling says. (d) The pace and the cap are in the order (at most 4 calls, at least 5 s apart, one retry per flag on a timeout or 5xx, no retry on a 4xx), and a refusal stops the cell; no other principal is tried. (e) The token is used in memory and never written anywhere.

**fanout:** 1 of 1 chains, cap 8, reason: one independent probe cell with a disjoint write set (its own worker folder and private folder). Worker `0.9.0_WK_IRPT_DASHBD~305` (`DB-i-5`).

## Cells

| cell id | owner |
|---|---|
| DB-i-1 | 0.9.0_WK_IRPT_DASHBD~301 |
| DB-i-2 | 0.9.0_WK_IRPT_DASHBD~302 |
| DB-i-3 | 0.9.0_WK_IRPT_DASHBD~303 |
| DB-i-4 | 0.9.0_WK_IRPT_DASHBD~304 |
| DB-i-5 | 0.9.0_WK_IRPT_DASHBD~305 |
