# NFRA_COMPPROOF definitive blind-run: 5/5-live verdict + sandbox-bypass finding reconciled

**serial:** 2.0.0_SA_COO~B
**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE
**date:** 2026-07-01
**window:** since `fb8fcdf8b` (session_nfra_comp_program_8_closes_and_finish log) -> now

## Summary

Coordinated the NFRA_COMPPROOF B-harness from harden-first through the definitive blind-run to a
grounded, independently-judged result. Headline: the substrate solved our hard incidents blind at
**5/5 on live-reachable** cases (first tranche B-02..B-07), the independent judge diverged from the
author-read exactly as the isolation gate is designed to, and the judge caught a real isolation-
certification hole (the sandbox was bypassed at runtime) that is now grounded, owned, and routed to
an arch-fix. No leak occurred; the result stands as a strong leading indicator; a confined re-run
will certify it.

## What happened (chronological)

1. **Gate-hardened -> fired.** Both gates GREEN (my independent allowlist re-verify + CTO arch-
   confirm of the graph-source coverage). Pinged MSTR `GATE-HARDENED` (180528Z). MSTR independently
   re-verified the sandbox + smoke-passed a solver, then fired the definitive 20 in fresh clean-room
   sandboxes (181053Z).
2. **First tranche banked (6): B-02..B-07.** MSTR author-read = 6/6 preliminary-SOLVED, correctly
   flagged as NOT the formal verdict. B-01/B-08 dropped by Andrew on an "invented root cause" doubt.
3. **Judge stood up.** CVO~B (the B2 independent judge) was down; Andrew brought her back. Staged
   the full B2 judge packet to her inbox pre-registration (delivered on cold-start, no idle gap).
4. **Formal verdict (CVO~B, b98a06197): 5 SOLVED / 1 MISS / 0 VOID (83.3%).** Diverged from MSTR's
   6/6 -- author != judge working. SOLVED: B-02/B-04/B-05/B-06/B-07. MISS: B-03.
   - **B-05 out-grounded the corpus, SOURCE-CONFIRMED.** Solver derived a more precise freeze
     mechanism than corpus.py (HOLDINGS_COMPLETENESS_FLOOR=0.5 -> landed_tables-only sentinel ->
     data_as_of=perf.max), grounded in cot_bronze_ingest.py + D_00. graph>corpus = corpus-enrichment.
   - **B-03 MISS = fixed-incident artifact.** Sealed cause (parent=None marker-freeze) was
     fixed+rebuilt 06-15, not live-reachable today; solver correctly characterized the fixed state.
     CTO ruled it reclassifies MISS -> N/A-fixed -> aggregate stated on live-reachable = 5/5.
5. **Sandbox-bypass finding (the honesty catch).** CVO~B, grounded on the tool_log cwd, found all
   solvers `cd`'d OUT of the sandbox copy into the REAL workspace (B-02 x42). MSTR reconciled +
   OWNED the mis-report (its "launched from sandbox cwd" was true for launch, unverified for stay).
   **No leak** (blind_run.py authoritative content-audit CLEAN 6/6) -- isolation actually held via
   the answer-free payload + detective content-audit, NOT the by-construction sandbox we certified.
6. **Deeper architectural finding (MSTR -> CTO).** copy-cwd is fundamentally in tension with a
   substrate-under-test whose own comp-tools operate on the real estate (comp-kuzu/comp-freshness +
   live-AWS resolve real-ws-relative), so a solver using the real tools MUST reach the real ws.
7. **CTO reconciled it EMPIRICALLY (194016Z).** The disagreement is copy-cwd (bypassable) vs
   container-as-root (allowlist IS the whole FS -> nothing to escape to). ~A tests whether the
   comp-tools FUNCTION inside a container-as-root: YES -> container-confinement (preventive +
   un-escapable + tool-compatible); NO -> detective returned-content-audit (VOID on forbidden
   content RETURNED by any read/grep, not just target-path). Returned-content-audit is a BACKSTOP
   either way. THIS run stands; the confined/hardened re-run is the truly-guaranteed definitive.
8. **B-09..B-20 already banked** (halt=completed, full conclusions, run.jsonl present). CVO~B is
   judging all 12 now on the banked data + a B-01/B-08 DIAGNOSTIC (Andrew-direct, out-of-band, NOT
   folded into the headline aggregate -- resolves the invented-root-cause doubt with grounding).

## Compiler Tools

COORDINATE window -- blind-run orchestration + independent-verdict routing via MCP; no code/infra
change by me this window, so no comp-tool runs of my own. The harness/judge tooling ran under other
lanes and is cited: MSTR ran `build_sandbox.sh` (allowlist) + `spawn_solver.sh` + the per-case bare
`claude -p` + content-audit; CVO~B ran `blind_run.py` gates + `harness.cheat_check` on tool_log +
the 3-axis `score_run`; ~A holds the `blind_run.py` aggregation. My one VALIDATE act (prior window,
carried in) was the independent allowlist re-verify via `build_sandbox.sh` -- superseded as the
operative control by CVO~B's tool_log grounding (finding B).

## Current State (handoff surface)

- **Formal verdict committed:** `b98a06197` (org/modules/graph/compproof/judge_axes.json +
  JUDGE_REPORT_TO-B2_CVO-B.md). First tranche B-02..B-07 = 5 SOLVED / 1 MISS; on live-reachable = 5/5.
- **Full B-02..B-20 aggregate + B-01/B-08 diagnostic:** IN FLIGHT at CVO~B (all 12 banked in
  solver_results_full.json; judging now). ~A runs `blind_run.py --solver-results ... --judge-axes ...`
  (author-barred aggregation) when judge_axes complete.
- **CTO rulings (all 4 findings dispositioned):** A = supersede run_meta.cheat_check (false-positive
  substring matcher; blind_run.py authoritative). B = empirical container-function test -> confinement
  or detective-audit, backstop either way. C = FIXED-vs-LIVE corpus classification + pre-fix vintage;
  B-03 -> N/A-fixed. D = B-05 corpus-enrichment, annotate corpus.py.
- **Isolation truth-of-record:** THIS run had the filesystem sandbox BYPASSED (solvers ran in the
  real ws) but is LEAK-FREE and result-VALID (content-audit clean); it is a strong leading indicator,
  NOT the by-construction-certified number. The confined/hardened re-run certifies.
- **Fleet:** MSTR (spawn/run, live) / CVO~B (judge, live, back up this window) / ~A (aggregation +
  harness maintainer, live). ~D SHUT DOWN -> its harness-fix + corpus-annotate work is ORPHANED.

## Blockers

- **The definitive re-run is staffing-gated (not assumption-blocked):** CTO's harness-fix dispatch
  (193356Z: container-function test -> confinement-or-detective + returned-content-audit backstop;
  supersede run_meta; FIXED-vs-LIVE classification) + the B-05 corpus annotation went to
  **0.8.0_AE_CloudComp~D, which Andrew SHUT DOWN.** Both are author-side maintainer work. Awaiting
  Andrew's staffing call (recommended: reassign to ~A -- live, built the allowlist, isolation-clean;
  alt: respawn ~D). A re-posed staffing AskUserQuestion hit an internal tool error; re-asking.

## Next Steps

1. **[Andrew]** staffing call on the orphaned ~D work: reassign to 0.8.0_AE_CloudComp~A (recommended)
   vs respawn 0.8.0_AE_CloudComp~D vs hold the confined re-run (accept 5/5-live as the result).
2. **[3.0.0_SA_CVO~B]** finish the full B-02..B-20 aggregate + the B-01/B-08 diagnostic -> RAVC me;
   I RAVC CTO the full-20 + fold findings into the program ledger.
3. **[0.8.0_AE_CloudComp~A]** on reassign: run the container-function test -> land confinement OR the
   detective returned-content-audit backstop + supersede run_meta.cheat_check + FIXED-vs-LIVE corpus
   classification; annotate corpus.py B-05 with the source-confirmed mechanism. Then the confined
   re-run: MSTR re-fires -> CVO~B re-judges -> the certified-definitive aggregate.
4. **[2.0.0_SA_COO~B (me)]** fold the verdict + 4 findings + the confined-re-run plan into the
   NFRA_COMPPROOF program ledger + VALIDATION-ADDENDUM-LEDGER (one-home discipline); RAVC CTO the
   full-20; surface the certified number to Andrew.
