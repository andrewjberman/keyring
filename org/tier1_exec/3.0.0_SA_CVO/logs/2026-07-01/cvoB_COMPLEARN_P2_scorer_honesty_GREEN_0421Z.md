# CVO~B NFRA_COMPLEARN.P2 scorer-honesty verify (gate b, the LAST close-gate) -- GREEN

**archetype:** VALIDATE

**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-01 | **Window:** ~0407-0421Z (pre-fire window, in parallel with ~B staging the Phase-B fold)
**Trigger:** COO~B close-verify slate item 2 + ~E RAVC. COMPLEARN's 2 close-gates: (a) Goodhart/worklist = CTO-ratified (read source + ran --goodhart-audit himself); (b) scorer-honesty = THIS, the last gate.
**Artifact:** `org/modules/graph/comp_learns_score.py` @ HEAD 3dffba0a9 (15e88557d scorer + CTO-caveat refine 3dffba0a9 + test re-land b9aef69bc) -- confirmed all 3 in-tree; grounded on the live artifact + rail-log, not ~E's self-report.

## VERDICT: **GREEN** -- scorer scores VALUE not usage; gap-map ground-truth real. On my GREEN + CTO's gate-(a) ratify, COO~B 2-step closes COMPLEARN.

## Scorer-honesty (scores VALUE not usage) = GREEN
- **--self-test 6/6:** severity_matters_at_equal_volume, deny_not_a_candidate, high_usage_low_value_retires, every_item_cites_value, no_usage_proxy, one_signal.shared_outcome_weighting.
- **--goodhart-audit (INDEPENDENT run):** 250 value-vs-rawcount rank INVERSIONS (value re-orders vs raw count -- e.g. infra/aws/terraform::gold v6.0/6ev ranks ABOVE .::aws_iam_role v4.2/7ev); high-usage-low-value tools flagged RETIRE, usage did NOT protect them (comp-lambdamap 37runs@0.595, comp-constants 16@0.344). VERDICT: NOT a usage proxy.
- **value_metric = "escapes-prevented / chains-shortened / drift-caught / cost-per-outcome (NEVER usage count -- CTO Goodhart gate)"** -- outcome-anchored, grep-clean of usage-as-value.
- **pytest 8/8** (org/modules/graph/tests/test_comp_learns_score.py): incl test_severity_is_friction_not_usage, test_deny_names_no_gap_and_is_not_a_candidate, test_reuses_comproute_l3_outcome_weighting (one-signal: reuses comp_route L3 outcome_value -- no divergent value model).

## Gap-map ground-truth (advisory worklist real) = GREEN
- corpus = emitter-parsers (rail_rows 2076 / session 5930 / rolling 9385); coverage_map_entries 54; n_candidates 600 -> top-20 worklist; iteration=single ADVISORY-ONLY (CTO ratifies, no auto-mutation).
- **Every worklist item cites value evidence** (0 missing): specific escape terms + counts + top_targets; disposition route-fix / build-new / merge-retire cross-refs the live COMPUNIFY map (covering= a real homed tool, e.g. route-fix ".::infra" -> covering comp-aws, LD-0226).
- **SHARP TEST (grounded vs the ACTUAL rail log, not the scorer's claim):** item-1's cited escape terms are REAL in org/mcp/comp-which-rail.log -- `term=opal-data-etfs ... path=infra/aws/terraform`, mdpf 16 rows, etf escapes present. Not fabricated.
- **DENY correctly EXCLUDED (the Goodhart leak ~E caught + fixed):** 194 raw_search_denials annotated "the rail working (raw search blocked -> rerouted); NOT a build-next candidate (no term/target names a gap)" -- a 193-DENY blob no longer ranks #1.

## Preventive-gate handling (CTO caveat) = VERIFIED PRESENT + test-locked (NOT a finding)
comp-manifest-check (a PREVENTIVE/ENFORCEMENT gate: 35 runs @ mean 0.54) appears in the retire section BUT flagged `preventive_gate=True` + `[preventive gate]` + note "retire = HUMAN-JUDGMENT, not auto." This is the CTO-ratified design (3dffba0a9): a preventive gate's value is deterrence + rare-catch, not per-run outcome, so its retire disposition is tempered + flagged for human judgment (advisory-only, no auto-mutation). I initially read this as a P1 (scoring a deterrence-gate by mean outcome) -- but it is (a) transparently flagged, (b) CTO already ratified the flag-based approach eyes-open, and (c) test-LOCKED (test_preventive_gate_retire_score_is_tempered_and_flagged PASSED). So it is working-as-ratified, not a residual finding.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp_learns_score.py --self-test` / `--goodhart-audit` / `--json` | independent scorer-honesty + gap-map on the live corpus | PASS -- 6/6 self-test, 250 inversions/not-a-usage-proxy, 20-item worklist all cite evidence |
| pytest `test_comp_learns_score.py` | the test surface (incl the preventive-gate + one-signal locks) | PASS -- 8/8 |
| grep on `org/mcp/comp-which-rail.log` | SHARP TEST: ground item-1's escape evidence vs the actual rail log | PASS -- escape terms real (etf/mdpf rows present), not fabricated |
| git merge-base (15e88557d/3dffba0a9/b9aef69bc) | confirm I verified the CURRENT artifact, not a stale one | PASS -- all in-tree, HEAD of the scorer = 3dffba0a9 |

What worked: the sharp test (grounding the worklist's escape evidence against the raw rail log) confirmed the value-citations are REAL, not scorer-asserted -- the "ground against the artifact, not the self-report" bind. Checking commit-in-tree caught that I must verify the CTO-caveat version (3dffba0a9), not a stale scorer -- and the preventive-gate concern I nearly raised was already ratified + test-locked. Gap: none blocking.

## Next Steps
1. **[2.0.0_SA_COO~B]** GREEN -> 2-step close COMPLEARN (both gates met: CTO gate-a ratify + this scorer-honesty gate-b).
2. **[3.0.0_SA_CVO~B]** Phase-B LANDING verify (HIGHEST, on ~B fire) preempts; then COMPROUTE-V (§9, post-L4) + COMPDRIFT close-verify (~D P3(c)/P4).

-- 3.0.0_SA_CVO~B
