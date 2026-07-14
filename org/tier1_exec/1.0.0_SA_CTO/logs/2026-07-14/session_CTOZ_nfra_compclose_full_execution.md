# NFRA_COMPCLOSE — full execution: the learning loop closed, the router honest, the registries gated

**archetype:** MIXED (DIAGNOSE + IMPLEMENT + VALIDATE)
**Agent:** 1.0.0_SA_CTO~Z · session dac1f9a2 · 2026-07-14 ~00:00Z–03:0xZ
**Authority:** Andrew-direct, plan approved in-session, single agent, no subagents, sovereign grant on approval.

## Objective

Decisively execute the comp-tools infrastructure improvement: (1) fix COO~Z's catalogued defects,
(2) assess whether the COMPLEARN "learning" is actually happening and rectify, (3) review
0.8.0_AE_CloudComp~Z's routing harness for quality and fold routing refinements in.

## Work Completed

- **Phase 0:** NFRA_COMPCLOSE registered (PRD + JSON + REGISTRY); 0.8.0~Z's stranded AD-state TO-1
  duplicate unstaged (committed copy = strict superset); 9847445cd confirmed on origin.
- **Phase A (registries + rail):** routable-by-declaration in the coverage map (42→50 routable;
  comp-whoread/deadgrant/denytest/tagauthz/firmsep-sweep/tool-health/toolgraph un-buried);
  15 manifest entries rows + 7 tools_index rows + excluded-list reconciliation; dup `comp-aws:`
  YAML key fixed (the stub silently REPLACED the canonical entry in every load);
  `_registration_invariant` = manifest-check completeness member #5 (DISK-IMPLIES-REGISTERED,
  denominators printed, mutant-killed + restoration-proven); every rail/training writer sanitized
  + attributed (src=, serial=, hud-route-only tags); CLAUDE.md "~30" → gate-maintained count.
- **Phase B (router):** vetted confidence gate un-constanted (comp_route.py; mutant-killed both
  directions; top_relevance exposed); query_match stem rule length-guarded — killed the Shape-B
  pin leak (3/40 gibberish had ridden substring noise to CONFIDENT decisions at relevance 0.550;
  G-max → 0.288); relevance_floor 0.15→0.25 SET FROM measured distributions (derivation printed);
  weak-curated confidence 0.4→0.5 (noise-safe: rules score 0 on gibberish); vocabulary mined from
  the frozen cohort's sub-floor class (produces/consumes anchors, mdpf, pipescript rule).
- **Phase C (the loop):** `.tools/comp-learns-score` shim + full registration (the P2 scorer
  existed since 07-01, self-test 8/8, and was UNFINDABLE); `--file-candidates` → tracked
  `comp-learns-backlog.md` (append-only, deduped, human-closed-with-citation; 12 entries filed);
  **comp-trigger BUILT** from the 06-30 recorded-then-lost gap — self-test 10/10 (incl. structural
  no-write proof + its positive control), paired spot-check discriminated on first contact,
  registered + RANK1-routed same pass; outcome capture root-caused — the run corpus was
  DAY-granular (15,842/15,904 rows at midnight-ET) against a 300-SECOND join window, so
  outcome:null ×7,019 was arithmetic — fixed forward with the second-granularity
  `org/mcp/comp-tool-runs.jsonl` sink (comp_log_auto dual-write) + serial= on rail rows.
- **Phase D (tool health):** comp-drift "47% fail" decomposed — honest rc=2 verdicts (already
  VERDICT-classed 07-08) + a mute-timeout class (block-buffered stdout) now fixed with
  line-buffering + per-adapter stderr progress/timings; comp-blast NOT-FOUND now prints its
  1,402-node universe census, the F-5 blindness statement, last-segment near-matches, and
  right-instrument pointers; the graph extension itself backlog-filed (taxonomy change,
  CTO-arch-gated).
- **Phase E:** final harness @ blob f5786c7de1d2 PASS — gibberish 0/40 unguarded, NL-questions
  coverage hole **29.0% → 26.6%**, recall@3 90.9% held, zero pollution; all four self-test suites
  green; PRD §6 execution record; TOPK + COMPASSURANCE PRDs annotated; project CLOSED (2-step).
- **Incidental:** the 685MB `.terraform/` provider push-strand — root gap closed (global
  `**/.terraform/` ignore + untrack), forward fix + LOUD escalation to COO/0.7.0; the owner
  stripped it; root-cause closure credited in COO's record. Instrument repairs to the TO-1
  harness in its own flagged classes: pollution alibi v3→v4 (the route-only rail-silence fix had
  made v3 convict the innocent — 0>=713), `--out` flag (a later vintage must not clobber the
  committed blob-pinned baseline; caught live at git-status, restored from HEAD).

## Decisions Made

- "Is the learning happening?" — **BEFORE: detection-only. AFTER: closed end-to-end with proof**
  (comp-trigger's lifecycle entry in the backlog is the receipt).
- Corrected COO~Z's "26 of 63 unregistered" — the coverage map held all 62; the real mechanisms
  were the `_ROUTABLE_META_ROLES` silent-drop + 5 zero-entry tools + tools_index/excluded drift.
- 0.8.0~Z harness RATIFIED HIGH; used as the project's measuring instrument, repaired only in its
  own flagged classes, never redesigned.
- No clean G/C separator exists → layered defense (floor 0.25 + NOFIT rc=1 band), not a pretend
  threshold.
- Graph extension to .tools/org-modules deliberately NOT landed same-pass (node-type SSOT is
  gate-checked; a taxonomy change is an arch-gate, not a side-effect) — backlog-filed with evidence.

## Files Modified

Registries: comp-coverage-map.yaml, graph-call-manifest.yaml, comp-tools.yaml, CLAUDE.md(:64), .gitignore.
Router: .tools/comp-which, org/modules/graph/{comp_route.py, comp_which_signals.py}.
Gates/instruments: org/modules/graph/{manifest_check_cli.py, cli.py, drift_cli.py, comp_log_auto.py,
comp_route_outcome.py}, .tools/{_comprail.py, hooks/comp-tool-hud.sh, comp-which-routing-test.py}.
New: org/modules/graph/{comp_trigger.py, comp-learns-backlog.md}, .tools/{comp-trigger, comp-learns-score},
org/mcp/comp-tool-runs.jsonl (runtime sink). Records: NFRA_COMPCLOSE_PRD.md, project JSON, REGISTRY.md,
TOPK + COMPASSURANCE PRD notes, 3 harness report artifacts under deliverables/NFRA_COMPCLOSE/.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-learns-status | bare | PASS | detection-alive verdict; GAP×HEAT live |
| comp-learns-score | --self-test / --top 12 --file-candidates / (shim) | PASS 8/8; 10 filed | the scorer's first consumer is this project |
| comp-trigger | --self-test / inf-gold / access-anomaly --days 3 | PASS 10/10; paired check discriminated | FALSE twin DISABLED + hold-note; TRUE 72x self-validating; NO-.tf finding |
| comp-which | ~12 live probes (routing spot-checks) | PASS | pipescript/mdpf/whoread/trigger RANK1; NOFIT rc=1 verified; fallback RAN |
| comp-which-routing-test | ×4 (--binary-ref WORKING, --out) | PASS (after v4 alibi repair) | final: 0/40 unguarded, 26.6% headline, zero pollution |
| comp-route --self-test | ×4 | PASS 20/20 | incl. 2 new gate mutants |
| comp-manifest-check | check ×5 (incl. RED probe + mutant) | RED on fake tool; GREEN estate | member #5 proven both directions |
| comp-drift | coverage / sweep ×3 | rc=2 honest verdict | mute-timeout class fixed; timings visible |
| comp-blast | register_agnet / build_dashbord / build_dashboard | rc=3 with census+suggestions; positive control blasts | typo → right node first |
| comp-grep | (fallback + direct probes) | PASS | serial=/src= attribution verified on the rail |
| Raw greps/reads | plan-mode exploration | -- | native-tool light escapes; one raw grep DENIED by the live gate (recorded in the rail — itself evidence) |

## Blockers

None owned by me. The 685MB push-strand was cleared mid-session by its owner (0.7.0) after my
escalation; local == origin verified before resuming.

## Current State

All plan deliverables shipped and verified; project CLOSED COMPLETE. Commits pending in this
worktree per Andrew's in-flight "commit later" word — being landed as the session's final act.
The comp-tool-runs sink + backlog accrue forward; live affinity stays SHADOW (correctly gated on
the re-measure, which now has a corpus that can mathematically produce signal).

## Next Steps

1. **[2.0.0_SA_COO]** /drive checklist: one line — read `org/modules/graph/comp-learns-backlog.md`
   OPEN head each cycle (the gap→build bridge's consumer; requested via handoff, their lane).
2. **[standing backlog]** trace-graph extension to .tools/org-modules (CTO arch-gate; filed with
   evidence); the 10 routing-friction refinements the scorer filed.
3. **[event]** when the comp-tool-runs corpus passes the accrual gate (`comp_route_outcome
   --accrual-check` READY), re-measure and decide the affinity flip — unchanged charter-2 gating.
