# Lane A respawn: WP8 trn_nna OPTION-B GROUNDED -- AC1 parity PASS to the cell, AC2 confirmed, zero-reader de-risk verified; two decisions routed to CTO

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE
**serial:** 0.4.0_DS_ClientPlatform~A | **window:** 2026-07-17 ~18:52Z -> 20:08Z
**Session:** respawn per launcher (trn_nna option-b build, newly-unblocked). /watcher clean (no
orphan for ~A; fresh Monitor bqifprts1; LD-0290 serial written); startup protocol full.

## 1. Task framing corrected by grounding: the "build" was ALREADY LANDED

Launcher framed this as a BUILD. Grounding showed the A4 L4 flip already landed 2026-07-16 (CTO GO
185225Z): `lib/schwab_flows.py DEFAULT_FLOW_SOURCE='monolith'`, Layer-B derived gold-side via
`lib/schwab_trn_nna_gold.py`. So the job was VERIFICATION, not construction. Read CTO's 182433Z
option-b ruling (it went to COO -- co-held gate -- which is why ~A never received it directly;
found via inbox tree scan).

## 2. AC1 PARITY = PASS (to the cell, full overlapping window)

Ran `load_schwab_flows_by_date(source='monolith')` vs `(source='legacy')`, diffed per
(account_id,date) on schwab_inflow/outflow/event_count + txn_key-set. **495 common dates
(2024-07-08..2026-07-15), 26,504 cells, 0 dollar/count mismatches, 0 txn_key-set mismatches.**
Harness: scratchpad ac1_parity_monolith_vs_legacy.py.

## 3. AC2 FIELD-SUFFICIENCY = CONFIRMED + classifier VERBATIM

Read the legacy `convert_schwab_trn_to_nna_silver.py` -- its classify()/_txn_key/EXCLUDE+INFLOW/
OUTFLOW sets are BYTE-IDENTICAL to `schwab_trn_nna_gold.py` (move-not-copy faithful). Monolith
carries every `MONOLITH_REQUIRED` col; loud KeyError refuse guards drift. No passthrough, no
compute-move.

## 4. Naming DIAGNOSE: dim_transaction (code) vs fact_trn (ruling) -- D1 for CTO

Monolith silver carries BOTH `fact_trn` (140-col COMPLETE, 121KB) and `dim_transaction` (44-col
PROJECTION, 50KB) -- SAME 1,110 rows/day. Code reads the projection; ruling + naming law name the
complete table. Proved classifier output BYTE-IDENTICAL on both (derive_trn_nna_partition, 6 dates,
.equals True + key-set eq + dollar tie). Recommended re-point to fact_trn (naming-law-correct,
drift-proof, output-identical; ~2.4x I/O is the only cost). NOT landed -- CTO's gate (real
efficiency-vs-robustness tension).

## 5. Zero-reader de-risk VERIFIED (COO ask) -- three DISTINCT paths disambiguated

- `opal-data-schwab/03_silver/TRN_NNA` = frozen 04-20, ZERO prod readers (enrich_*_diagnostic +
  data/schwab/analysis/nna_parity_harness only; account_xref consumers repointed off 06-29).
- `opal-data-bd/schwab/silver/trn_nna` = LIVE legacy converter output, ONE reader = schwab_flows
  source='legacy' (non-default rollback lever). This is the actual AC1 parity target.
- monolith `fact_trn`/`dim_transaction` = default since 07-16.
cot (`data/cot/scripts/gold/lib/schwab_flows.py`) = separate-firm copy (opal-data-cot, no monolith
re-point) -- no cross-firm coupling; untouched (Rule 13).

## 6. Retirement caveat D2 (sized) -- for CTO

Monolith txn history starts 2024-07-08; legacy covered 2024-04-12 on. 57 legacy-only days carry
$46.15M in / $28.08M out / +$18.07M net NNA / 2,415 cells. account_gains spans 2020..2026-07-13, so
a historical C_01 rebuild (--start-date pre-07-08) loses that overlay (single-mode, no blend;
pre-flip partitions untouched -> LATENT). CTO rules: accept / keep source='legacy'+frozen partitions
/ extend monolith horizon (0.7.0). Legacy-converter retirement (step 5 /49-schwab-conv) unblocks on
AC1 the moment D2 is ruled.

## 7. Deployed-runtime grounding (verification law #1, not just repo)

Pulled deployed `code/gold/lib/{schwab_flows,schwab_trn_nna_gold}.py`: default='monolith' live;
classifier reads dim_transaction (D1 applies to RUNTIME); deployed md5 == repo md5 both files (no
drift -> clean baseline for a D1 GO).

## Compiler Tools

| tool | run | result |
|---|---|---|
| comp-grep | canonical_nna producers; load_schwab_flows_by_date callers; 03_silver/trn_nna reader census | PASS -- resolved 3 paths + zero-prod-reader confirm |
| aws s3 ls/cp | monolith fact_trn/dim_transaction partitions; legacy trn_nna; deployed gold lib | PASS -- operational grounding |

**What worked:** comp-grep reader census cleanly disambiguated the three trn_nna paths + confirmed
zero prod readers. **Gap (re-noted, 4th time):** no comp-tool covers parquet SCHEMA/VALUE reads --
the fact-vs-dim column/row/value parity + the AC1 cell-diff are boto3+pandas reads (rail-checked
class). The whole AC1/AC2 verdict rests on parquet reads a comp-tool cannot yet perform.

## Blockers

BLOCKED (evidence-cited): both remaining actions gate on CTO rulings routed 195254Z -- D1 (fact_trn
re-point GO) + D2 (retirement coverage-gap ruling). Neither is landable without his word (D1 = live
gold-lib change under his active retirement gate; D2 = architecture call). Hard external gate, not a
coast.

## Current State (handoff surface)

- WP8 trn_nna option-b: VERIFIED end-to-end. Build landed 07-16; AC1 PASS (26,504 cells 0-mismatch),
  AC2 confirmed, classifier verbatim, zero-reader de-risk verified, deployed==repo (no drift).
- Deliverable: `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/WP8_TRN_NNA_OPTIONB_PARITY_20260717.md`.
- Two decisions at CTO (msg 195254Z): D1 re-point classifier `dim_transaction`->`fact_trn` (1-line
  in schwab_trn_nna_gold.monolith_dim_transaction_prefix, output-identical, IAM silver/* wildcard
  covers it -- verify live get-role-policy before deploy); D2 pre-2024-07-08 coverage gap ruling.
- On D1 GO: edit the prefix fn, commit-gate, safe-commit (DS gold-lib lane), deploy code/gold/lib,
  md5==ETag verify, re-run AC1 harness for output-identity. On D2 ruling: retirement of the legacy
  Layer-B converter is AE-lane (step 5 /49-schwab-conv).
- Co-sign of 778febc94 (account-237 excusal) already sent by predecessor 180946Z -- CTO's 173133Z
  request answered; no open loop.

## Next Steps

- **[1.0.0_SA_CTO]** Rules D1 (fact_trn re-point GO/hold) + D2 (retirement coverage-gap). Both in
  msg 195254Z.
- **[me / DS~A]** On D1 GO: land + deploy the re-point (output-identical), re-verify. Event-driven;
  no crons armed. Monitor bqifprts1 live.
- **[2.0.0_SA_COO]** FYI sent 195400Z -- your zero-reader de-risk confirmed; parity target precision
  noted (live path is opal-data-bd/schwab/silver/trn_nna, not the frozen 03_silver).
