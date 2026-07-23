# CVO~Z independent acceptance — NFRA_MSBEFF.R1R3 (full AC-1..7)

**archetype:** VALIDATE
**Serial:** `3.0.0_SA_CVO~Z` · **Vintage:** `@546f8c0e7` (ancestor-of-HEAD confirmed) = core `@926487fe6` + AC-5 `@325841910` + AC-6 tool `@da0d5679e` + rc2/comp-constants corrections `@546f8c0e7`
**GO:** CTO~Z hold-release 181204Z. Grounded at source / exercised, never the report.

## Verdict: PASS on AC-1..6 (6 of 7); AC-7 pending 0.8.0's session log (the one open item).

| AC | Verdict | Evidence (grounded/exercised) |
|---|---|---|
| **1** one helper, consumers derived at run time, denominator printed | **PASS** | `comp_output_contract.py` is ONE module; `classify_exit` is the single classification point; manifest invariant printed the live denominator `63 tools_index tool(s)` (not a hand-list). |
| **2** both gate mutants on the record | **PASS** | `test_output_contract.py` 20/20. Live-exercised: undeclared tool `classify_exit('comp-not-a-real-tool',1)=UNKNOWN` (NOT laundered to VERDICT/REFUSE) + `coverage_line`='COVERAGE: UNKNOWN -- no output contract declared' (loud, not silent). |
| **3** registration invariant live + mutant-proven | **PASS** | `_output_contract_invariant` (manifest_check_cli.py:865). **MUTANT-PROVEN both directions in-memory**: real state -> rc0 PASS (63 tools = 15 declared + 48 pending); injected undeclared `comp-PHANTOM-mutant` -> rc1 BLOCK (names it). Fail-closed, denominator printed. |
| **4** M3 derivation + supersession history preserved | **PASS** | frozen `VERDICT_EXIT_TOOLS` retired; classify_exit derives from the contracts yaml. Supersession note preserved comp_log_auto.py:185-199 ("07-08 freeze + 07-23 interim +3 were hand-patches ... do NOT re-freeze a verdict set here or anywhere") -- condition (c) met, a future reader is warned. All 3 REFUSE bindings source-cited (below). |
| **5** comp-validate tree registry derived + cot-isolation | **PASS** | DERIVED from `PIPELINE_MAP` (validate_cli.py:52,87) -- source-confirmed. cot-isolation (firm-sep-binding) **EXERCISED**: `_MERGE_GROUP_BD_INF=(black_diamond,inf)`, cot NOT in it; `_load_raw_cot_configs` is a SEPARATE function; cot map (2 ids) and bd+inf map (21 ids) built disjointly, never one namespace. A new firm auto-isolates (merging is opt-in, the dangerous direction). *Residual: the PIPELINE_MAP end-to-end discovery I could not run in my scratch (import path); the isolation SAFETY limb -- the one CTO~Z flagged as firm-sep-binding -- is proven.* |
| **6** re-baseline off jsonl real rc | **PASS -- independently re-derived** | Ran `comp_msbeff_rebaseline.py` MYSELF (did not accept 0.8.0's numbers). **3 corrections EXACT**: FAIL 542->37, REFUSE 1->61, UNKNOWN 0->31; CHANGED=517 exact. VERDICT reads 111->525 vs their 108->522 -- **the +3 is the post-snapshot vintage drift I flagged** (jsonl grew 7108->7135; 3 of 27 new rows are verdict-class; CHANGED unchanged because new rows append with correct class). REFUSE by_rule: comp-blast 39 + comp-iam 12 + comp-constants 10 = 61 (population); 60 changed + 1 pre-existing = "1->61". |
| **7** session log + compiler-tools-log line | **PENDING (open)** | 0.8.0's logs/2026-07-23/ carries only the prior `session_item7_...` log -- no R1R3 session log yet. NOT a failure; pending 0.8.0's session close. The one AC not yet deliverable. |

## The 3 REFUSE bindings — each source-cited & confirmed
- **(comp-blast, rc3) -> REFUSE**: cli.py NOT-FOUND exit-3 ("nothing traced, so nothing concluded; NOT a clean nothing-downstream"). CONFIRMED.
- **(comp-iam, rc3) -> REFUSE**: iam_cli.py:858 ("COVERAGE refusal: nothing was compared, so nothing is concluded") + :900 (stale-derive REFUSED). CONFIRMED -- the doctrine instance #6.
- **(comp-constants, rc3) -> REFUSE**: comp_constants_cli.py:415 + the CC2 sovereign-held guard :511-524 (fail-closed refusal, "an honest could-not-check, NOT a verdict about the estate"). CONFIRMED -- the 3rd binding CTO~Z flagged holds.

## VL#6 reconciliation (a number I chased, then grounded)
My tool run showed comp-constants:rc3 "9 rows" against 0.8.0's "10." No discrepancy: **10 is the rc3 REFUSE POPULATION; 9 is the re-verdicted DELTA** (rows that CHANGED FAIL->REFUSE); the 10th (`interim-probe-rc3`) was ALREADY REFUSE. "Enumerate what a number is OF before explaining why it differs." The append-only jsonl only grows, so a *lower* count could never have been vintage -- which is what pushed me to ground it rather than hand-wave.

## Two honesty notes (neither a blocker)
1. **Two false gaps I nearly reported, grounded away**: (a) artifact rows read `ts=None/session=None` -- my parse used the wrong keys; the jsonl/artifact use `ts_epoch`/`session_id`, both present. (b) "artifact carries no vintage" -- softened: no SNAPSHOT-level vintage header, but every row is `ts_epoch`+`session_id` stamped, so the 61 rows are individually identifiable and re-derivable (the substance of the bar met). **Recommendation (not a blocker)**: add a snapshot-vintage header (jsonl row-total / sha / as-of) so the artifact self-pins without relying on per-row ts.
2. Enumeration artifact keys: `refuse_rows_total`, `by_rule`, `binding_rules` (with exit_source citations), `rows` (row-level). Faithful to its described schema once the right keys are used.

## Compiler Tools
`comp-glob`/`comp-grep` (on-rails, rail-logged) to locate sources · `git show`/`git merge-base` (vintage pin @546f8c0e7) · `python comp_msbeff_rebaseline.py` (independent AC-6 re-derive) · `pytest test_output_contract.py` 20/20 · in-memory mutant of `_output_contract_invariant` (AC-3, both directions) · live exercise of `validate_cli` cot-isolation (AC-5) + `comp_output_contract` classify/coverage (AC-2). Gap found: AC-7 not yet delivered (0.8.0 log); artifact lacks a snapshot-vintage header (rec).
