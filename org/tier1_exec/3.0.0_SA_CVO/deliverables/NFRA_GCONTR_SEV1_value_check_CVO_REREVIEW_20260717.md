# NFRA_GCONTR SEV1 value-check -- INDEPENDENT CVO RE-REVIEW (LD-0308: a stand-in is not a substitute)

**Reviewer / signature:** `3.0.0_SA_CVO` (the actual CVO instantiation, live PID 39288)
**Re-reviews:** `NFRA_GCONTR_SEV1_value_check_results_20260717.md` -- the value-check EXECUTED by
`0.0.0_AB_MSTR` standing in for the CVO lane (audited override da4517195) while a fresh CVO was
hanging. Per LD-0308, a stand-in is not a substitute; this is the owed independent pass.
**Andrew-direct via MSTR** (spawn brief 2026-07-17T21:54:56Z). **Method:** RE-EXERCISED every limb
against live served state at 2026-07-17 ~22:45-23:05Z -- did NOT take the deliverable's numbers on
trust (RV-0047 F-015 / LD-0278 discipline, same as the RV-0051 pass).

## VERDICT: CONCUR -- all four limbs independently reproduced. The stand-in value-check is SOUND.

**DEPLOY REMAINS HELD to MDPF (Andrew-direct "i dont want to deploy this until MDPF is totally
done").** This re-review VALIDATES the value-limb; it does NOT lift the hold and triggered NO load.
Read-only throughout: no writes, no ad-hoc gold runs, no `--load-contracts`.

| limb | deliverable claim | my independent re-exercise (live) | verdict |
|---|---|---|---|
| (1) benchmark | value CLEAN 250/250; 1M/1Q discriminating; contract-TEXT drift | re-ran `value_check_benchmark_period_defs.py` (exit 0): **CHECKED 250 (expected 250) \| VIOLATIONS 0**; 1M `\|D\|=0.7200`, 1Q `\|D\|=7.8100` (tol 0.01) DISCRIMINATING; YAML lines 82-83 `1M=trailing-1-calendar-month / 1Q=trailing-3-calendar-months` carry the `!!! DRIFT -- DO NOT LOAD` block vs the 30/91-cal-day methodology-of-record (Andrew 631d8d0d9) | **CONFIRMED** |
| (2) headline (MDPF agg AUA) | convergence CLEAN, as_of 07-17, current, 18.7h, lag 0 | GET `platinum/mdpf/aggregate_aua_timeseries.json`: `as_of_last=2026-07-17`, `source_vintage_last.status="current"`, `age_hours_at_generation=18.7` (<26h), `lag_vs_as_of_days=0`, feeders (model_aua_positions, non_model_aua incl 49financial+inflection) all 07-17 | **CONFIRMED** |
| (3) advisor_intelligence | inf 07-16/5 clean; bd 07-13/167 frozen-known; cot absent | GET actual content (not write-time): inf `data_as_of=2026-07-16`/5 advisors; bd `data_as_of=2026-07-13`/167; cot **404 Not Found** (12 other firm artifacts present, none is advisor_nna_canonical) | **CONFIRMED** |
| (4) empty-hash / load-state | graph_contracts 745h (06-16); 2 SEV1 rows never loaded | comp-kuzu marker vintage: `graph_contracts last-write 748.2h ago` (= 06-16) -> the 2 SEV1 rows are STILL NOT LOADED; the HOLD is intact | **CONFIRMED** |

## VACUITY GATE (409d9a85a) -- PASS
Benchmark reproduced **250 real cells**, not "CHECKED 0". The check is DISCRIMINATING at this as-of
(1M/1Q would differ by 0.72/7.81 under the reverted SmartX last-complete-calendar-period method), so
the pass has power today -- it is not a vacuous green over an empty set.

## VALUE-LIMB corroboration on the clean firm (inf) -- beyond presence
- **inf `reconciliation.all_pass=true, max_abs_delta=0.0, series_tie_max_abs_delta=0.0`** (sum(leaves)==parent, tol 0.01 USD) -- a real value-limb signal, not just presence.
- **no-silent-bd-fallback: PASS** -- inf `firm_id="inflection"` (Inflection Wealth Mgmt) vs bd `firm_id="49financial"` (49 Financial): distinct payloads, so inf is not serving bd's data. cot's NNA is ABSENT, not falling back to bd either.

## TRADING-CALENDAR discipline (NEVER#1) -- resolved BEFORE any staleness call
2026-07-17 = Friday; expected T-1 frontier for a daily pipeline = 2026-07-16 (Thu).
- **inf `data_as_of=2026-07-16` = T-1 = HEALTHY** (not stale).
- **bd `data_as_of=2026-07-13` (Mon) = a REAL freeze**: 3 trading days behind the 07-16 frontier (Tue/Wed/Thu), NOT a weekend artifact. **Known, Andrew-acknowledged cause** = the bd-exporter allocations-outage (07-13 -> login-fail P1, deprecated); bd gold is gated on silver/allocations, so advisor_nna_canonical froze with the chain. The "fresh per firm" limb currently FAILS for bd until the consolidation freshness-gate re-key lands. Not a new defect; not a false alarm.

## OPEN ITEMS FOR ANDREW (surfaced, NOT adjudicated -- these gate the eventual post-MDPF load)
1. **benchmark contract-TEXT drift.** Served data is CORRECT (30/91-cal-day canonical, 250/250 clean); only the YAML `period_defs` text is wrong (`1-calendar-month`/`3-calendar-months`). NOT in the 1655Z "SIGN BOTH" (that was headline + advisor_intelligence). Decision: re-sign with corrected 30/91d text, OR load-with-drift (advisory-WARN v1, no hard-block per LD-0273). **I recommend re-sign with corrected text** -- the contract text is the semantic-of-record and should not encode a value it does not mean.
2. **cot advisor-NNA scope.** Contract declares firm scope `{bd, inf, cot}`; cot serves NO `advisor_nna_canonical.json` (its `platinum/firm/` serves leaderboard/dashboard/partner_analytics/... instead). **CVO/domain call: scope the contract to `{bd, inf}`, OR locate cot's NNA at a different served key.** cot is a separate firm pipeline (bd<->cot<->inf never mirror), so a missing artifact here is a scope-definition question, not a producer defect. Surfaced for Andrew/CTO; I do not silently re-scope a signed contract.
3. **bd freshness on load-day.** Before any post-MDPF load, confirm the consolidation freshness-gate re-key restored bd advisor_nna_canonical to a T-1 `data_as_of` (currently 07-13 frozen). advisory-WARN v1 will not hard-block, so this is a read-and-confirm, not a gate.

## Grounding (Rule 22a -- desired / applied / exercised)
- **desired:** the TO-3 contract rows (`NFRA_GCONTR_TO3_contract_rows_20260626.md`) + `!!! DRIFT` correction (`NFRA_GCONTR_SEV1_amendment_package_20260709.md`); PRD sec-9 homes `value_check` at CVO.
- **applied:** comp-kuzu marker vintage `graph_contracts last-write 748.2h` (06-16) -- confirms the 2 SEV1 rows unloaded; the hold is intact. (In-VPC per-ROW hashes of the 3 loaded rows = COO's in-VPC read 150336Z; I could not re-read the DDB rows from outside the VPC -- stated as a coverage boundary, not a pass. The decision-relevant fact -- that NOTHING loaded despite today's signature -- IS independently verified via the last-write vintage.)
- **exercised:** re-ran `value_check_benchmark_period_defs.py` (exit 0, 250/250, discriminating); live GET `aggregate_aua_timeseries.json` (as_of 07-17, current); live head+GET `advisor_nna_canonical.json` x {inf 07-16/5, bd 07-13/167 gzip-decoded}, head cot (404) + `s3 ls opal-data-cot/platinum/firm/` (absent, 12 other artifacts); inf reconciliation self-report (all_pass, 0.0 delta); comp-kuzu graph_contracts vintage. Read-only; no writes, no loads.

-- `3.0.0_SA_CVO`, 2026-07-17. Independent re-review CONCURS; value-check SOUND; deploy HELD to MDPF.
