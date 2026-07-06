# TH-A cadence + F-1 close, and a full utf-8-log lint shipped to block-mode

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE

## Summary
Delta since the 1543Z log (TH-A probe landing). This window closed TH-A end-to-end (cadence wiring
+ CVO F-1 resolution + accuracy refinement) and then built a NEW durable-hygiene deliverable start-to-
finish on COO/CTO GO: the utf-8-log lint that catches the exact class that bricked COMPLEARN corpus load
fabric-wide -- carried all the way to a gated, safeguarded BLOCK-MODE in the shared ds-commit-gate. Every
piece committed, pushed, RAVC'd, and independently verified (CVO on TH-A/F-1; CTO on the lint gates).

## What happened

### TH-A cadence wired (CTO GO) -- consumption-driven, HOST=local (commit f5c6263a7)
CTO ruled HOST=local + TRIGGER=consumption-driven with a 7d staleness ceiling (NOT cron/SessionEnd/cloud).
Wired `tool_probe.ensure_fresh` (reuse if <=7d, run-fresh-then-read if >7d/missing/force) + a pure
`_is_stale` decision (self-tested without a live run) + `--ensure-fresh`/`--ceiling-days`/`--force`. Both
paths exercised (REUSE on the 0d feed; RAN under --force). CTO RAVC-CLOSED, no rework.

### CVO TH-V VALIDATED + F-1 resolved (commits 46658953f, 697155165)
CVO independently blind-re-ran the probe -> VALIDATED (isolation 4/4, flip reproduces). Finding F-1: the
comp-freshness FIX rested on a 0.3% timing margin (90.28s vs 90s cap) = load-non-deterministic. Owned it,
Rule-22 grounding: MEASURED true latency (uncapped) = 190s->rc2-empty (author) and, on CVO's independent
run, 144s->rc1-with-content -- both ~5-6x past any interactive SLA. Set the cap 90->30s (~6x below measured
= robust margin). CVO re-verified -> F-1 RESOLVED. Applied her accuracy refinement (rc is intermittent
1<->2; too-slow ALONE is the robust determinant; the tool is UNRELIABLE = a stronger fix-TO). COO closed TH-A.

### utf-8-log lint -- built to BLOCK-MODE (COO GO + CTO gate, commits 388047b5a -> 7aed944b6)
The durable-hygiene lint COO GO'd from the corpus-brick incident. Full arc:
- BUILT (388047b5a): AST lint flagging a text-read open() with encoding= but no errors= on a log-shaped
  path OR inside a log-parser function. The enclosing-function path was ESSENTIAL -- the real crash sites
  take the log path via a bare param (parse_rail(path)), so a path-only heuristic MISSED all 3 (caught in
  validation). Self-test 12 AST cases + a RUNTIME em-dash demo. Home: compproof/ (org/modules/graph/ top
  is exec-lane; owned-paths guard correctly blocked me, moved to my lane).
- VALIDATED vs the REAL incident: flags all 3 pre-fix opens (0191f9c9f~1), clean post-fix.
- ADVISORY SWEEP (CTO ask): 8396 estate .py -> 2 flags, both FALSE POSITIVES (a HAR capture, a config
  manifest -- coincidental token matches). TIGHTENED 2 over-broad tokens without weakening the real catch
  -> re-sweep 0 flags, 3/3 TP preserved (97d1f0c5a).
- --advisory mode + WIRED scoped-advisory into ds-commit-gate (f3192b9ca, b1b47da59), mirroring the
  comp-manifest-check pattern; self-scoping = 0 noise on non-log commits.
- CTO GO'd BLOCK-MODE gated on 2 safeguards -> SHIPPED both (840567c80): an audited
  `# log-open-ok: <reason>` override escape-valve (-> org/mcp/log-open-ok-override.log, gitignored) +
  crash-fail-open (exit 1 ONLY on a genuine finding; per-file + top-level try/except). Then FLIPPED the
  gate to block-mode (7aed944b6). Tested end-to-end through the real gate: clean->PASS, violation->BLOCK,
  override->PASS+audit.

## Compiler Tools
| Tool | Command | Result |
|---|---|---|
| tool_probe (F-1) | run_tool uncapped 200s on comp-freshness chain bd | 190s->rc2 empty (measured latency = the F-1 grounding) |
| tool_probe | --self-test (staleness gate added) / --run / --ensure-fresh (reuse+force) | PASS; flip robust at 30s cap |
| comp_tool_health | --tool comp-freshness/comp-which --effective-feed | KEEP->FIX flip holds post-F-1 |
| log_open_lint | --self-test (14 cases incl. override+crash), estate sweep (8396 files) | PASS; 0-FP after tightening; 3/3 TP on the real incident |
| ds-commit-gate | wired + block-mode tested (clean/violation/override) | PASS; blocks only genuine findings, crash-fail-open |
| ds-commit-gate.sh | gate on all committed .py | clean every commit |
| comp-surface-check | auto via safe-commit (all commits) | no critical surface touched |

**What worked:** validating the lint against the REAL incident (not a synthetic test) surfaced the
path-only false-negative; the FP-sweep-then-tighten loop got to 0-FP honestly; mirroring the existing
comp-manifest-check advisory pattern made the shared-gate wiring low-risk. **What failed:** the audit
_WS path was one dirname short (wrote to a non-existent dir, silently fail-open) -- caught by verifying
the audit actually landed, fixed. **Gap surfaced (bonus fix-TO):** comp-freshness `chain bd` is UNRELIABLE
for the whole-chain query (144-190s, rc flaps 1<->2) -- a real optimize/repair candidate.

## Blockers
None. Lint thread CLOSED (block-mode live). Next: SFNBRIDGE (COO-GO'd, deps met) -- a SEV1 comp-blast/
comp-iam surface change; oracle owner (~A) + certifier (CVO~B) are holiday-dormant, so I build +
self-verify vs the known 26-invoke oracle (def_hash 5082ce9dba1318fd), cert follows async.

## Current State
- TH-A fully closed (build + FIX-catch + cadence + F-1), CVO-validated, COO/CTO-accepted.
- utf-8-log lint LIVE in ds-commit-gate BLOCK-MODE with audited override + crash-fail-open (7aed944b6).
- HEAD 7aed944b6 synced to origin/CLOUD.

## Next Steps
1. **[me]** SFNBRIDGE: ground comp_aws_cli._sfn_task_invokes + trace_graph edge model -> bridge sfn_invokes
   edges, comp-surface-check before/after, self-verify vs ~A's 26-invoke oracle, RAVC COO (CVO cert async).
2. **[1.0.0_SA_CTO]** block-mode spot-check of the override audit path (offered).
3. **[2.0.0_SA_COO]** the utf-8-log-lint durable is CLOSED; SFNBRIDGE next per your sequence.
