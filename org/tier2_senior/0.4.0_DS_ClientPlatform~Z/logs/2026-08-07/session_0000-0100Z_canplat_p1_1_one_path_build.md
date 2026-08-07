# 0.4.0_DS_ClientPlatform~Z — MDPF_CANPLAT.P1-1 one-path build (fresh-reset session)

**archetype:** IMPLEMENT
**Session:** 2026-08-06T23:30Z → 2026-08-07T00:5xZ · fresh reset (Andrew-direct), watcher task bst635bxo
**TO:** MDPF_CANPLAT.P1-1 @f123fbf6e (GO COO~Z 235814Z) — the only live dispatch on this seat

## What happened

1. Startup per org/XXX.md (register PID 10304, Monitor confirmed, zero crons); HOLD held
   until the COO~Z GO landed 235814Z; read order executed (§0 → PRD @24d3eb2f8 →
   CONTRACT @a3106d585 → adopted body @a6ae64326 + 7 deltas).
2. Read the FULL port closure before writing (~9,400 lines: spine, 3 dims, A7 producer,
   cottonwood trio, crosswalk, stage trio, bridge grammar, route_bindings, roster
   resolvers, lib/trading_calendar, tie-out deliverable).
3. **Wave 1 @d136d5bb1 (atomic, both trees):** one-path spine
   (`build_firm_timeseries` + FIRM_BUILD_CONFIG; builders dissolved to delegators),
   `mdpf_gold_consolidator.py` (A2–A9 per CONTRACT §A), `mdpf_calendar_binding.py`
   (WS-1 bind + `assert_pmc_backend`), shim DELETED, fee_scope 2→1 (Δ7),
   both-operand ternary as THE derivation (W-8 chosen semantic, Guard 3),
   slice `_cot_window` fail-closed (criterion 4a, behavioral change recorded).
4. **Wave 2:** 23/23 criterion tests + pinned calendar tie-out harness (T1 10/10 2027
   coverage, T2 horizon guard, T3 falsifier fired-and-localized) + build record
   deliverable (Δ5 classification: all five canonical-for-all; Δ6 confirmations incl.
   the `cottonwood_aua.py` CORRECTION — it is C10/registry lineage, not MDPF closure).
5. Cross-domain closed same-session: AE~Z (FLAT confirmed, hash-tie pair in A6,
   model_registry in package, manifest prefix live-simulated, deploy sequencing);
   CVO~Z (G2 canonicalisation confirmed + the null→0 gold-side mutant class requested
   into the fixture record).

## Live measurements (denominators)

cottonwood non_model 8/446 · custody 38/446 · model 52/446 (staged artifact,
as_of_last 2026-08-03); W-1 three fields confirmed ABSENT in today's staged cottonwood.

## Compiler Tools

| tool | result |
|---|---|
| `comp-pipescript io <6 mdpf gold scripts> --pipeline mdpf` | manifests read pre-write (spine reads incl. HARDCODED mdpf_revamp keys + monolith silver facts); no unrecorded COLUMN GAP relevant to the port (shape-only change; no column set changed) |
| `comp-blast dim_mdpf_account_distribution` | NOT-FOUND (denominator 20585 nodes) — the TO PREDICTED this absence: the cross-tree private-symbol import is invisible to the extractor; atomicity (family inside this TO) is the control. Recorded as the Phase-1 finding. |
| `comp-xref _distribution_stats` | only bd/inf same-named cousins (5 nodes) — confirms the blindness |
| `comp-grep` (shim importers, WS-1/pin lookups) | importer census drove the rebind set; OWNTS residual flagged |
| `comp-validate` | DEFERRED to the QA cycle — no built artifact exists on this box (pmc absent; `assert_pmc_backend` correctly refuses); NOT signaling SAFE |
| `comp-pipescript deployed` | deliberately NOT run as a post-upload check — no upload this wave (mdpf deploy-gated; Lambda package is AE~Z's P1-2) |

## Gates / discipline

commit-gate PASS on all 7 touched .py (py_compile + AST + ruff); risk-reflex CLEAN
(8 files vs 1662 danger nodes); safe-commit `-F` msgfile, single lane, no push
(MSTR~Z integrates); working files in scratchpad throughout.

## Open / next

- QA comparison run (9c/R7) awaits AE~Z package + CVO~Z baseline; §E adjudication is
  program-level on one unattended scheduled cycle.
- R2 ruled extra (`inflection_non_model_aua`) + global-custody honest-absence decision
  recorded in the build record for CTO~Z's eyes.
