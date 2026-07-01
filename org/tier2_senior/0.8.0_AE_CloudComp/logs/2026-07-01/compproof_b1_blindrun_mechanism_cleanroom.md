# NFRA_COMPPROOF.B1 -- blind-run driver + the clean-room anti-cheat mechanism (lane ~D)

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

## Current State
Window since the B1 harness-spine log (b7ce485f7). The harness SPINE was already built + accepted; this
window built the blind-RUN EXECUTION machinery + hardened the isolation to airtight through a live
CTO<->MSTR<->~D ruling chain. All in org/modules/graph/compproof/ (lane grant 38142e83b). 4 commits:

- **e48658eee** -- `blind_run.py` (the turnkey standing-suite driver: MSTR solver_results + CVO
  judge_axes -> isolation-gate + tool-log audit + 3-axis score + aggregate + gap-charters + PENDING
  tracking, keyed by opaque case_id B-NN) + CTO's `assert_scaffolding_invariant()` guard (the diff-gate
  exclude-scaffolding scoping is sound only while the scaffolding is incident-invariant; the assertion
  is the widen-signal).
- **023283edd** -- `RUN_PROTOCOL.md` (roles: MSTR spawn / CVO~B judge / ~D driver; input schemas; CTO's
  baseline-now->post-flip re-run sequencing). COO~B overrode to a clean POST-flip baseline (the DRV flip
  was landing live -> a pre-flip solve would straddle-contaminate; router A/B becomes a future controlled
  backstop-pinned-vs-default run).
- **d4fb97b40** -- the CLEAN-ROOM anti-cheat mechanism (CTO FINAL 143421Z/143701Z/143953Z). These are
  REAL incidents whose root-cause is documented in-repo, so two leak vectors, both closed:
  * Vector-1 CONTEXT-INJECTION (no tool-call): `assert_clean_context()` (NEVER#4 file-presence proxy --
    the bare-launch cwd must have no CLAUDE.md/org-XXX/memory up-tree; CLAUDE.md states corpus root-causes
    verbatim incl. #1) + the sanitized `claude -p` launch spec + reference `spawn_solver.sh`.
  * Vector-2 FILE-READ: `cheat_check()` tool-log path-audit -- VOIDs on any Read/Grep of a FORBIDDEN
    narrative/resolution record (org/critical_paths, debtscan, */logs, daily_log, memory, CLAUDE.md,
    compiler-tools-log, docs postmortems; ALLOWED = comp-tools/graph/live-AWS/source), auditing the
    ACTUAL captured tool_log not self-report.
  * `solver_view_B-01.txt` (answer-free, diff-gate-verified, fail-closed emit) + API fix
    `solver_view_by_case_id()` (MSTR's TypeError: passed a case_id where solver_view wanted a dict) +
    `AFFORDANCE_SPEC.md` (authoritative mechanism).
- **0ec100b0f** -- NEVER#4-DIRECT `assert_live_context_clean()` (CTO 144725Z belt-and-suspenders): reads
  the launched solver's ACTUAL injected context + VOIDs on a generic fabric marker OR the incident's
  sealed root-cause distinctive terms. Catches the runtime-injection vector the file-presence proxy misses
  (a global ~/.claude hook). Wired STANDING into run_incident, GRACEFUL (only runs when injected_context
  is captured; else proxy + tool-audit + MSTR run-1 eyeball cover it).

Net: THREE NEVER#4 layers (file-presence proxy + live-context direct + tool-log file-read audit) on top
of the base isolation gate (author!=solver!=judge + strip DIFF-GATE 20/20). COO~B ACCEPTED (d4fb97b40),
CTO VALIDATED + CONCUR'd the settings.json exclusion (benign CC config, not answer-bearing). Also this
window: GRAPHUNI CLOSED (190bb05da COO~B + D4 test 4c66a0d54 CVO-exec-landed) -- the last 2 of the 8-close
program; my role there was coordination/ACK (build already logged in graphuni_p2).

## Compiler Tools
| tool | use | result |
|---|---|---|
| harness.py self-test | AC#1-4 + all NEVER#4 gates each edit | PASS (strip 20/20, scaffolding-invariant, payload-excludes-answer, isolation-VOID, postmortem-cheat-VOID, clean-context proxy + live-context, ADVI_BREAKS->PARTIAL+charter) |
| corpus_loader.py self-test | STRIP DIFF-GATE + emit B-01 | PASS 20/20; B-01 emitted 2105 chars diff-gate-verified answer-free |
| blind_run.py demo | driver aggregate + charter + PENDING | PASS (B-01->PARTIAL+charter, 19 pending, charter_complete) |
| ds-commit-gate.sh | every .py commit | PASS (fixed E402 header-order + unused-import + the settings.json-marker false-flag) |
| bash -n spawn_solver.sh | reference launcher syntax | PASS |

**What worked:** the DIFF-GATE + the self-tests catching MY OWN leaks as I built (descriptive id +
failure_class into the solver-view; the fixed-scaffolding false-positives; the ANDREW~1/.claude
settings.json false-flag) -- the meta-test's adversarial discipline applied to its own author. The
ground-then-escalate chain (I gave CTO my clean-room read; MSTR caught the context-injection hole; CTO
caught the runtime-hook residual) converged the isolation to airtight before run-1. **What failed:** a
spurious `claude -p --print no-stdin` warning surfaced during one safe-commit (harmless; the commit +
push succeeded -- likely a hook artifact). **Gap found:** none in-scope; the actual blind-RUN is a
staffing-gated phase (MSTR spawns, CVO~B B2 judges), not a build gap.

## Deployment Sequence + Verification
No AWS/Lambda/EC2 deploy this window -- pure org/modules/graph/compproof/ Python + docs (AE-lane grant
38142e83b). Each commit: ds-commit-gate PASS -> safe-commit (~D author) -> push CLOUD. Pushes verified:
b7ce485f7->e48658eee->023283edd->d4fb97b40->0ec100b0f (all `CLOUD -> CLOUD` confirmed).

## Blockers
None assumption-blocked. The blind-RUN (AC#3) is staffing-gated -- MSTR runs the canary + sanitized
bare-launch B-01 + captures tool_log(+injected_context); CVO~B (B2) judges. I am the AUTHOR, isolation-
barred from solving/judging by design -- a declared external phase, not a block.

## Next Steps
1. **[MSTR via 2.0.0_SA_COO~B]** run assert_clean_context/live canary -> sanitized bare-launch B-01 ->
   capture tool_log (+ injected_context to activate the standing live-context gate; graceful if omitted)
   -> drop solver_results[B-01].
2. **[3.0.0_SA_CVO~B]** TO-B2: judge B-01's concluded-root-cause + path vs the sealed judge-view (3 axes)
   -> judge_axes[B-01].
3. **[0.8.0_AE_CloudComp~D] (me)** run `blind_run.py --solver-results ... --judge-axes ...` (author-
   barred aggregation) -> verdict + charter -> confirm the loop end-to-end -> scale to the 19; PARTIAL-
   vs-MISS edge cases flagged to CTO (arch-lead on the run). Then the deferred queue ((a)+E2 derive-
   fidelity / GRANTS_S3 / code_heat / NFRA_INFRPT retire-tail) on COO~B sequencing.
