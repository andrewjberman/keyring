# The review found my in-kind unit price was a whole position's market value, and the calibration I committed was measuring my own defect -- 0.4.0_DS_ClientPlatform~S

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, VALIDATE, IMPLEMENT, SCRIBE

**Date:** 2026-10-01 03:25Z to 04:20Z
**Task Order:** `IRPT_DASHBD.TO-DB-b-1` (pending, amendment 4 @b116670d7c); `TO-DB-b-3` pending
**Status:** IN PROGRESS -- two deterministic defects repaired; emit still HELD; three findings routed out of lane
**Workspace CLOUD commits:** `35e325eedc` (the two repairs + quarantine), `d8c2bad446` (rows S3-S6), `48d3647120` (row S7).
All three LOCAL; origin/CLOUD `0abf99fcd4` (ls-remote read, positive control passed).

---

## Objective

Startup, then the work Andrew brought: a methodology review he commissioned of the round-1 daily
return package (`REVIEW.md`, `source_evidence.html` in Downloads). Twelve findings, five called
publication blockers. Triage every one against the real bytes, repair what is this seat's, route
what is not.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read | `--for` on the producer, the order, the doctrine; `--enumerate 'fee'`, `'FEE'` | PASS | `--enumerate` with a printed denominator was the right instrument for the fee question: 9 hits, all substring, which is itself the finding -- an anchored probe would have returned zero. |
| comp-find | `"SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811" --files` | PASS | Found the second consumer (`a05_ref_txn_classification.py`, the SERVED chain). That one read is what turned S6 limb (e) from a round-1 issue into a served-data question. |
| commit-gate | on the producer edit | PASS | clean first try |
| safe-commit + naming-gate + surprise-row-gate + missions-tree-check | 3 commits | PASS | the row gate validated 4 new rows, then 1, against the schema |
| owned-paths registry read | `.owned-paths.yaml` lane resolution | PASS | the instrument that produced row S7 |
| PATH shim check | the XXX.md A.3 block | PASS | 104 of 104 comp-tools resolve bare; forwarder exercised live |

**What worked:** `comp-read --enumerate` over a single file with its band breakdown; it answers
"how many and where" without the pipe that the rail (correctly) denies.
**What failed:** two `comp-read | tail` calls denied by the rail. Both were my error, not the
rail's -- `--width` is the native flag and it exists precisely so a census is not truncated.
**Gap found:** none new this session.

---

## Work Completed

### 1. Startup (`/watcher` + `org/XXX.md` A-F)

Lane `~S` was NOT REGISTERED; registered (PID 9776), armed the inbox Monitor (task `b5ka6lypb`,
script pid 10552), re-armed on expiry (`by4dy4imp`). Inbox empty, delivery ledger 9 of 9 READ.
Session serial file written, audit-archive invoker rc=0 / 0 findings, hook present, `.agent_context`
set. `to-check --all --assignee` returns exactly 2 TOs. The `ADVI_INSURE` order in the base folder
is `issued_to 0.4.0_DS_ClientPlatform~R`, NOT this lane -- the broker's pending list is folder-keyed
and was misleading exactly as XXX.md B.1 warns.

### 2. F01, confirmed at bytes, and it is mine (`35e325eedc`)

`FlowCache._closes()` read `src.get("price_column")`; `sources.json` never declared one, so it fell
back to `position_value_column` = `market_value_settled_unsettled` -- a WHOLE POSITION'S MARKET
VALUE -- which `classify_and_sum` multiplied by the transferred quantity (`value = qty * eff`).

Measured over all 561 partitions (2024-07-08..2026-09-29), 558 carrying an in-kind leg:

| | contaminated | corrected |
|---|---|---|
| admitted in-kind value | $10,136,513,746,276.56 | $3,092,518,713.75 |
| legs reaching the fallback | 32,587 of 43,447 | same |
| UNVALUED legs | 4,487 | **579** |

Overstatement 3,277.8x; worst leg 941,822.4x (2025-12-30, $204.4B against a corrected $327,862.68).
Per-position on date=2026-09-25 the multiplier `market_value / closing_price` is median 71.0x,
p90 718.0x, max 5,353,077.5x over 106,578 rows.

**The repair, and why `closing_price` is not a guess:** `quantity_settled_unsettled x closing_price`
reproduces `market_value_settled_unsettled` to within ONE BASIS POINT on 106,307 of 106,578
comparable rows, so it is the price the custodian's own value is built from. Declared as
`price_column`; `_closes()` now REFUSES when none is declared rather than substituting a different
quantity. Coverage IMPROVES (unvalued 4,487 -> 579), which is the control separating a fix from a
narrowing.

### 3. F06, confirmed, and also mine (`35e325eedc`)

The income filter read `inc[keycols[1]]` = `tr_cd` while the `WD` withholding marker is on
`sb_cd` = `keycols[2]`; every income row carries `tr_cd == FC`, so the exclusion was always true and
withholding was never excluded from income on any run. Now declared (`withholding_code_column`) and
read by name, with a refusal if the declaration does not name a real transaction key.

### 4. The calibration is quarantined, not corrected

`MEASURED_THRESHOLDS_R1.json` -> `MEASURED_THRESHOLDS_R1.SUPERSEDED_CONTAMINATED_INKIND_UNIT_PRICE.json`
carrying the reason, root cause and validating measurement. Its tails -- tolerance max 214.58,
large_flow max 217.996, `observed_r_p001` -0.912047 -- were recorded in my own log as "the data's own
distribution" and were artifacts of F01. No live thresholds file now exists, so the producer fails
closed on any emit by the order's own rule.

### 5. All twelve findings triaged and routed (`d8c2bad446`, `48d3647120`)

Rows grouped by REMEDY OWNER, not by finding, because a row whose remedy nobody owns is a backlog
entry: **S3** mine, repaired (F01, F06). **S4** the issuer's -- the account boundary, the fee basis
and the timing selection are in the ORDER'S OWN TEXT (F05, F07, F11). **S5** the CTO's -- the PRD
mandates the partial-basket substitution and nothing validates the selected value (F02, F03).
**S6** five more, split (F04, F08, F09, F10, F12). **S7** corrects S6's own routing of limb (d).

### 6. Two claims of mine the review refuted, withdrawn on the record

- "The two calculations share no input" (my defence of the guard) -- **wrong**: the holdings producer
  uses balance-derived cash and the in-kind path uses positions. Withdrawn in row S5.
- "Conditional in-kind transfers share the cash matcher's failure" (told to the issuer last session)
  -- **wrong**: the cash matcher does not pair IC rows; conditional IC rows fall to EXTERNAL.
  Corrected in row S4's notes.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Quarantine the thresholds before anything else | A committed deliverable that any seat could promote into policy was measuring my own defect. That is the only item where delay had a cost. |
| Repair F01 by declaring the real price, not by deleting the lookup | `closing_price` exists and validates against the book's own market value to 1bp. Deleting the lookup would have cost 32,008 legs of coverage for no correctness gain. |
| Make the absent-declaration case REFUSE | The defect was silent because a missing key fell back. A future declaration dropping `price_column` must fail loudly, not resurrect it. |
| Do NOT re-measure the thresholds | The account-boundary defect is in the order's own method text, so recalibrating now bakes a second known defect into the numbers. A specification dependency, not an approval gate. |
| Do NOT patch F05/F07/F11 | Each departs from the order's face; amending task-order criteria is the issuer's act. Recommended shapes given in the row instead. |
| Do NOT touch the classification table | It is a CRO deliverable consumed by the SERVED 49F engine as well as this adapter. |
| Grade S6 limb (e) INERT on magnitude, with `disarm_owner` the issuer | It DOES reach served data, but $39,818.98 over 2,578 rows is ~$15/row. I stated the grading basis so the grader can disagree with the grading rather than with a verdict, and put the judgement on the issuer because it concerns served client numbers. |
| One message, to the CTO only | Rule 31: one ask. `2.0.0_SA_COO~P` is dark, so S4/S6 are parked on the channel with the issuer named -- the carrier, not an inbox. |

---

## Files Modified

`data/assets/scripts/gold/irpt_reporting/account_return_daily.py`,
`.../sources.json`, the deliverables quarantine, and the channel. See the three commit messages.

---

## MCP traffic

1 message sent: to `1.0.0_SA_CTO`, the S5 decision (delivered
`20261001T035756Z_...DECISION_owed__row_IRPT_DASHBD-S5...`). Refused twice first -- once for a
wrong parameter name (`message` vs `body`), once at 159 words against the 150 cap. Both refusals
were correct and loud.

---

## Blockers

- **`2.0.0_SA_COO~P` DARK** -- rows S4, S6 and S7 are parked on the channel for it. Not a wait this
  seat can convert into work: every remaining producer repair depends on the boundary or interval
  decision in those rows.
- **`1.0.0_SA_CTO`** -- row S5 asked this session.
- **Nothing is HELD on Andrew.** The method review he commissioned has been acted on in full.

---

## Current State

The producer at `35e325eedc` no longer values an in-kind leg with a position total and no longer
drops a dead withholding filter, and both repairs are measured against live data rather than
asserted. It is still NOT fit to emit: the account boundary, the fee basis, the guard substitution,
the valuation intervals and the selected-value validation are all open, and three of those five sit
in text this seat does not own. Nothing is in S3 under `irpt/49financial/gold/account_return_daily/`
or `dim_return_method/`; no thresholds file exists; the change-management ledger for the emit is not
opened. `IRPT_BCKEND-S237`/`S239` remain open with the issuer and remain the materially urgent
served-data item -- S6 limb (e) is the same SHAPE at 1/1000th the magnitude and must not be
conflated with it.

---

## Next Steps

1. **[`2.0.0_SA_COO~P`]** Rows S4 and S6 -- amend the boundary, the fee basis, the timing selection
   and the valuation interval, or rule that each stands. Every further producer repair is downstream.
2. **[`1.0.0_SA_CTO`]** Row S5 -- the guard substitution and the missing post-selection eligibility
   check. Sent this session.
3. **[`2.0.0_SA_COO~P`]** Row S7 -- the four acceptance checks, with the counterexamples supplied.
4. **[`0.4.0_DS_ClientPlatform~S`]** On those rulings: rebuild the flow term at account grain, make
   unknown cash propagate instead of becoming zero, make inception durable, replay every cited
   extreme on pinned snapshots, THEN re-measure, write the method contract, open the ledger, emit,
   and grade `DB-1-AC1`/`AC2`/`AC3`; then `TO-DB-b-3`.
5. **[`4.0.0_SA_CRO` / served engine lane]** S6 limb (e) -- `FTP/FC/WD` and `FTR/FC/WD` are EXTERNAL
   in the shared classification table and reach served `twr_daily`.

---

## The lesson worth keeping

I read an improvement as a correctness proof. The prior session's in-kind fix moved the return p99.9
from +108% to +4.4%, and I treated that as evidence the term was right; it was evidence only that it
had CHANGED. The arithmetic underneath was dimensionally wrong the whole time, and a before/after on
a distribution cannot tell those apart. The control that settles it in one minute is a units
identity against the source's own columns -- `quantity x price == the book's market value`, with a
denominator -- and I ran it only after being told to look. Worse, the thresholds are defined as
percentiles OF THE PRODUCER'S OWN OUTPUT, so the calibration could not have caught the defect: it
absorbed it and reported it as the data's nature. A calibration whose population is its own
producer's output is not a check on that producer.
