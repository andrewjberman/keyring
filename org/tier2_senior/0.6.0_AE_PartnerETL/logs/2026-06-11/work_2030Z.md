# 0.6.0_AE_PartnerETL — work cycle 2026-06-11 2030Z

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

Andrew-direct (sovereign) escalation: convert all 7 BD gold full-recompute
scripts to incremental — "fix all of them ... make sure your logic in doing so
does not break the outputs, so be careful and go one by one." Started the
multi-day ADHC_GLDINC incremental workstream; script #1 (A_02) additive code +
offline parity proof DONE this session.

## Lead-in: Andrew-requested GLDINC nightly telemetry diagnosis
- Watermarking VERIFIED working + not stuck: A_00/B_00/B_01b/C_06 all read
  wm=2026-06-09 (= true silver data frontier; the "06-10" was a LastModified
  date, not a data partition). Evidence of BOTH behaviors: 22:00Z run advanced
  wm 06-08->06-09 on +1 new partition; 04:00Z run correctly no-op'd.
- Found 7 full-recompute scripts (~29min redundant c6i on no-new-data nights);
  cost concentrated in B_01 (731s) + A_03 (563s).

## Method (COO-endorsed in full)
ADDITIVE --incremental path + cold-start->full fallback; full path untouched +
authoritative => code change cannot alter live outputs. Parity via --shadow on
scheduled nightly (no manufactured c6i runs). Cutover (flip dispatch
INCREMENTAL_CAPABLE) = separate gated step, needs clean-night evidence + Andrew
nod. DS owns deploy (Rule 13); AE does engineering + plan.

## Rule 20 (graph-before-change) — applied
comp-pipescript io + comp-blast on candidates BEFORE any edit. Caught: (1) A_03
docstring is stale — it actually reconciles vs LATEST Schwab RPS/unrealized/
realized (retroactive historical-partition touches), so NOT a clean naive
incremental; (2) positions_cube blast radius = 46 consumers. Re-sequenced:
intricate ones (A_03 retroactive / B_01 daily-revaluation / A_04 90-day sliding
window) LAST with hybrid designs; cleanest SCD-2 (A_02) FIRST to prove machinery.

## Script #1: A_02 fee_rate_history — DONE (additive + parity proven)
Cost = reads all 1,881 silver/fees files every run. Incremental insight: the SCD
output IS the compressed change-point stream; reconstruct change-points from
existing history + read only new+14d-window files, re-run the UNCHANGED
build_fee_rate_history() => identical SCD. Restatement = etag-fingerprint guard
-> full fallback.

Files (additive):
- lib/s3_layout.py: + FEE_RATE_HISTORY_WATERMARK (gold/meta/) + Rule 15 future-import
- A_02.fee_rate_history.py: + --incremental (watermark/restatement/merge),
  + --shadow self-contained parity proof, load_fee_files(keys=None) default =
  identical full behavior, full path writes watermark sidecar (separate key,
  output identical). + Rule 15 future-import + 3 pre-existing lint fixes.

Gate: ds-commit-gate CLEAN (py_compile + ds-precommit-check + ruff) on both files.

PARITY PROOF (offline --shadow, local S3 read, NOT a c6i run):
| sim gap | files read (of 1,881) | identical | sym_diff | cell_mismatches |
|---|---|---|---|---|
| 1 day  | 15 | True | 0 | 0 |
| 3 days | 17 | True | 0 | 0 |
| 10 days| (running at log time) | - | - | - |
10,773 records both paths, 0 row-count delta. Byte-identical.

## Compiler Tools
| Tool | Result |
|------|--------|
| comp-pipescript io A_03/A_02/A_01 | I/O manifests; caught A_03 stale-docstring reconciliation reads (Rule 20) |
| comp-blast positions_cube | 46-consumer blast radius (B_00/B_01/C_02/C_04/D_04 + INF_* firm copies) |
| comp-pipescript deployed (cot) | bd-only/blind to opal-data-cot (known gap; used aws events for cot pre-check) |
| ds-commit-gate (A_02 + s3_layout) | CLEAN after Rule 15 + lint fixes |

## Open / next
1. DS deploy-coordination for A_02 additive path (sequence around DS 9-RED bundle).
2. RAVC2 conversion plan (docs/briefs/gldinc-incremental-conversion-plan-7-scripts-20260611.md) -> COO+DS.
3. Then scripts #2-7 one-by-one (A_01 -> B_02 -> B_03 -> A_03 -> B_01 -> A_04).
4. Unchanged: ADVI_COTETL.NIGHTLY-VERIFY + ADVI_PRTORG.AC-CLOSEOUT nightly-gated to AM (event-driven).

## Cutover gate (hard)
No flip of any script to INCREMENTAL_CAPABLE without: clean-night nightly --shadow
parity + Andrew's explicit nod. Additive code lands anytime (zero live risk).
