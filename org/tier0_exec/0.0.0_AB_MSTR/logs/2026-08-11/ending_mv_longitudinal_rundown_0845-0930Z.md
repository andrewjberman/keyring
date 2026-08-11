# MSTR session log — ending_mv longitudinal run-down, 0845-0930Z

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE

## Summary
Andrew-direct ~0846Z handed COO's commissioned brief (@5e9c253613) to this seat: "please run
this down." Executed the full longitudinal investigation read-only over at-rest S3 (zero
egress). VERDICT: the five hypotheses collapse — populated ending_mv equals current AUA to the
cent (485/485, max diff $0.00); the entire $68,321,011.74 firm gap is vendor ABSENCE coerced to
$0.00 at parse (312 asset-holding accounts; $59.56M of it on FEE-EARNING accounts), not a basis
mixing, not staleness, not a reconciliation gap. Patrick: $695,956.41 current vs $127,852.75
emv = same valuation minus 9 of 12 accounts. Full findings:
deliverables/ENDING_MV_LONGITUDINAL_FINDINGS_20260811.md + the schema-valid PROOF_OF_SPEC
instance beside it (validated pre-commit).

## Work record
1. Pulled billing (2025 monthly + 2026: 97 nonempty of 102 dirs), positions_mv (223 daily),
   representatives, bronze billing.csv 2026-08-11 — all to scratchpad, read-only.
2. Replicated DS's cohort to the cent (127,852.75 / 695,956.41 / 568,103.66) before extending.
3. Longitudinal features per cohort account; step-date histogram; fee-flip census (102/907).
4. Bronze-vs-silver parse control: first pass contaminated (multi-firm 3,052 vs INF 907 ->
   1,264 false losses), corrected to 0/907 honest losses — mutant fired, recorded.
5. Bronze period-metadata read: the discriminator. Zero class = vendor-empty billing blocks;
   partition 259 in-cycle-fee / 52 empty-block / 1 past-period.
6. Firm restatement ties the gap to the cent; wrote findings + instance + this log.

## Defects found (routed, not fixed)
- build_billing_dim.py rename map misses "Billing Period Start Date"/"End Date"/"Billing
  Cycle"/"As Of"/"Days In Cycle" -> silver silently lacks every period column.
- parse_dollar(empty) -> 0.00 conflates vendor-absent with vendor-zero (the $68.3M mechanism).
- Surprise channel: a .parquet under opal-data-inf bronze/ (17a class); PROOF_OF_SPEC phase
  enum lacks an investigation value; brief's partition count was a dir count.

## Compiler Tools
| tool | invocation | result |
|---|---|---|
| rail-checked aws ls/cp | partition census + at-rest pulls | no comp-tool fits an at-rest grid census; markers audited |
| proof-of-spec-check.py | on the instance | schema-valid |
No comp-estate/comp-kuzu: the question was data-content longitudinal, not estate-graph; the
mechanism source reads were direct file reads of the named builder (brief sec11 pointers).

## Blockers
None. At Andrew: the basis ruling (findings sec 2e is its input); the per-use Orion egress ask
if he wants the vendor-side WHY (declared exclusion 1).

## Current State (handoff-grade)
Findings + instance + log committed under 0.0.0_AB_MSTR deliverables/logs. Scratchpad
mv_invest/ holds the scripts + data copies (session-local, disposable). Serving untouched;
no fix landed; routing: builder defects -> P1 wave owners via COO/CTO; basis ruling -> Andrew.

## Next Steps
1. [Andrew] Basis ruling (sec 2e input); optional per-use Orion egress word for the WHY.
2. [2.0.0_SA_COO] Fold findings into the P1 register (the two builder defects are P1-scripts
   acts on the ratified forms); the fee-side $59.6M understatement is the business-weight line.
3. [0.4.0_DS_ClientPlatform] Owns build_billing_dim.py per Rule 13 when the P1 act lands.
