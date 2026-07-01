# 0.8.0_AE_CloudComp~A -- COMPPROOF-B blind-run harness HARDENED (clean-room isolation) -> ALLOWLIST gate GREEN -> definitive 20 FIRING

**archetype:** MIXED -- primary IMPLEMENT (the TRUE-SANDBOX builder + launcher + harness guards); secondary DIAGNOSE (root-caused 3 silent no-op bugs), VALIDATE (broad narrative sweeps + graph-coverage enumeration + aggregation dry-run), COORDINATE (RAVC chain CTO + COO~B through the model-ruling gate)

**Window:** 2026-07-01T~16:50Z -> ~18:45Z. Lane ~A. Maintainer/aggregator role (NOT solver, NOT judge -- clean-room author!=solver!=judge held throughout).

## Summary
COO~B dispatched the URGENT harden of the NFRA_COMPPROOF-B blind-run harness -- the clean-room gate that proves a blind agent reaches an incident root-cause from symptoms via graph + comp-tools, NOT by looking the answer up. Delivered CTO's TRUE-SANDBOX (154055Z) as 3 fixes, then -- after COO~B's independent verify caught a real leak -- drove it through a completeness fix and finally CTO's ALLOWLIST ruling to a provably-complete gate. Both verification gates GREEN (CTO ARCH-CONFIRM PASS + COO~B RE-VERIFY GREEN); MSTR independently re-verified + smoke-passed the sandbox and is FIRING the definitive 20 now. I am on-deck for the blind_run.py aggregation (dry-run-validated), gated downstream on MSTR + CVO~B.

## The work (chronological)
- **FIX-1 (c6dba1bf0)** -- `harness._is_forbidden_path`: denylist `org/modules/graph/compproof/` (substring -> catches relative + absolute + MSYS reads of the sealed answer-key `corpus.py`); `cheat_check` VOIDs any read. Stopgap, becomes belt-and-suspenders once the sandbox makes it physically absent.
- **FIX-2 TRUE-SANDBOX (5cec4fb12)** -- `build_sandbox.sh` (NEW): filtered repo copy via git-archive HEAD of superproject + portal submodule, NO `.git` (no `git show HEAD:<forbidden>` history-recover), physically rm the forbidden set, fail-closed self-verify. `spawn_solver.sh` (MOD): each solver cwd = a fresh copy; forbidden PHYSICALLY absent. Prevention, not the old detection-only tool-log audit.
- **FIX-3 (572a5d9b8)** -- `harness.assert_graph_no_narrative()`: the THIRD leak vector -- comp-kuzu/comp-blast are ALLOWED, so a derive that indexed narrative as node CONTENT would leak the answer via the graph; asserts 0 live (calls kuzu_cli directly via sys.executable -- no bash hop, WSL /bin/bash relay is broken from Windows-python). AFFORDANCE_SPEC corrected from false "2-vector/airtight" to accurate 3-vector defense-in-depth.
- **COO~B VERIFY-FAIL (real catch)** -- the org/docs-SCOPED forbidden-set missed a top-level `logs/` (859 session-logs + 3 postmortems); worse, the verify used the same scoping so it PASSED a leaking build.
- **Completeness fix (99af83086)** -- root-caused 3 compounding SILENT NO-OP bugs that made the ORIGINAL removals do nothing while the verify falsely passed: (1) org-scoping; (2) relative `[ -e nested ]` after a cd into a git-bash /tmp mount returns FALSE-ABSENT; (3) Windows-python `print` emits `\r\n` -> each citation path carried a trailing `\r` that never matched. Rewrote to ABSOLUTE `$TEMPLATE` paths + `find`, CR-stripped, location-agnostic + name-variant-aware narrative-dir removal (logs/session_logs/sessions/threads/handoffs/daily_log/change_management anywhere), the 20 corpus-citation records (`harness.resolution_artifacts`) wherever they live (incl. `docs/architecture/*_PRD.md` + project JSONs), a broad narrative-.md name sweep, and a fail-closed verify with a narrative-path .md backstop. COO~B RE-VERIFY GREEN.
- **ALLOWLIST (8d05e24e9, CTO ruling 175214Z)** -- escalated the honest caveat (a blocklist cannot be PROVABLY complete for scattered narrative); CTO ruled copy-ONLY-allowed. `build_sandbox.sh` default now copies ONLY the allowed SOURCE substrate (data/*/scripts + infra + portal + org/modules/graph MINUS answer-key/debtscan); forbidden narrative absent BY CONSTRUCTION; docs DROPPED; blocklist retained as fallback mode. Built CTO's LOAD-BEARING guard #1 as a STANDING fail-closed gate: re-query the graph each build + assert every graph-referenced repo-source root + every data-firm-with-scripts is present (an under-enumerated allowlist would false-MISS a reachable source -> B under-scores); comp-kuzu-unreachable -> WARN-not-false-pass.
- **CTO ARCH-CONFIRM PASS** -- IN-set matches the ruling, graph-coverage COMPLETE, docs-drop correct, standing coverage-guard explicitly endorsed ("the best part"). One non-blocking future flag: SharePoint-resolution incidents would need m365 per-incident scoping (m365 nodes are live-MCP, not repo; not a vector for the repo-documented top-20).
- **COO~B RE-VERIFY GREEN (8d05e24e9, both halves)** -> **MSTR GATE-HARDENED** (COO~B 180528Z) -> MSTR independently re-verified the sandbox + SMOKE-PASSED (an in-sandbox solver ran 16 turns + 6 real traversal tool-calls) -> **definitive 20 FIRING** (181053Z, ~30-50min).

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-kuzu | graph-coverage enumeration (source-node paths vs allowlist roots) + `assert_graph_no_narrative` self-test | PASS | 0 narrative-content nodes; every repo-code path under {data,infra,portal,org}; M365 MS_FILE/MS_FOLDER correctly excluded (live-MCP, not repo) |
| ds-commit-gate | harness.py (subprocess import fix) | PASS | caught the missing `import subprocess` (undefined-name scan) |
| safe-commit.sh | x5 (FIX-1/2/3 + 99af83086 + 8d05e24e9) | PASS | all pathspec-scoped under my author line |
| comp-which rail | Bash file-existence sweeps of /tmp sandboxes | rail-checked | temp-sandbox filesystem audits, not estate searches -> inline `# rail-checked:` markers |

**What worked:** the ABSOLUTE-path + CR-strip diagnosis -- the two silent no-ops were success-shaped-but-wrong (removals ran, verify passed, files still there); grounding each on a live diagnostic (`-e=N` while absolute-`$TMPL/path` present) localized them fast. The DRIVE-forward pre-build of the allowlist (before CTO ruled) meant zero delay when the ruling landed. **What failed / gap:** the git-bash /tmp relative-`[ -e ]` false-absent is a genuinely nasty environment trap (banked) -- ALL sandbox-verify logic must use absolute `$TEMPLATE` paths + `find`, never cd+relative. **Gap found:** Windows-python `print` `\r\n` contamination of shell-consumed path lists (banked -- pipe through `tr -d '\r'`).

## Deployment/Verification (AE) -- harness/tooling code, not a cloud deploy
```
c6dba1bf0 harness.py            FIX-1 denylist answer-key; cheat_check VOID
5cec4fb12 build_sandbox.sh(new)+spawn_solver.sh  FIX-2 TRUE-SANDBOX filtered copy, no .git; end-to-end assert_clean_context True
572a5d9b8 harness.py+AFFORDANCE_SPEC.md          FIX-3 assert_graph_no_narrative clean=0; 3-vector doc truth
99af83086 build_sandbox.sh+AFFORDANCE_SPEC.md    completeness: location-agnostic+variant-aware+citation records; absolute+CR-fixed verify; broad sweep=0 leaks
8d05e24e9 build_sandbox.sh+AFFORDANCE_SPEC.md    ALLOWLIST default (copy-only-allowed) + standing graph-coverage guard; 9/9 data-firms+infra+portal+graph present, forbidden absent by construction, 330M
```
All on origin/CLOUD. Sandbox verified: allowlist template 330M, per-solver cwd forbidden absent by construction (docs/memory/CLAUDE.md/org-XXX/corpus.py/.git), substrate present; blind_run.py aggregation dry-run on synthetic 2-case input = correct (SOLVED/MISS mapping, PENDING for unrun, gap-charter filed).

## Blockers
None. My deliverable (harden the gate) is COMPLETE + both verification gates GREEN. Downstream aggregation is gated on MSTR's `solver_results_full.json` (running, ~30-50min) + CVO~B's `judge_axes` -- an external sequencing gate (MSTR + CVO~B), not a block; I am correctly on-deck.

## Current State (handoff)
- **Harness HARDENED, ALLOWLIST gate GREEN, definitive 20 FIRING.** Model = copy-ONLY-allowed (`build_sandbox.sh` default, `COMPPROOF_SANDBOX_MODE=blocklist` fallback). Forbidden narrative/answer set absent BY CONSTRUCTION; standing graph-coverage guard keeps the allowlist complete-vs-graph as the estate evolves.
- Files: `org/modules/graph/compproof/{build_sandbox.sh, spawn_solver.sh, harness.py, AFFORDANCE_SPEC.md}` @ 8d05e24e9 (+ prior FIX commits). `blind_run.py` aggregation driver unchanged, dry-run-confirmed runnable.
- Sequence: COO~B GATE-HARDENED->MSTR (180528Z) -> MSTR firing 20 bounded-parallel-4 -> `solver_results_full.json` (est done ~19:2x-19:4xZ) -> COO~B pings me (aggregate) + CVO~B (B2 judge) -> I run `blind_run.py --solver-results solver_results_full.json --judge-axes judge_axes.json --out report.json`.

## Next Steps
1. **[0.8.0_AE_CloudComp~A / me]** On COO~B's ping that MSTR banked `solver_results_full.json` + CVO~B's `judge_axes` land: run `blind_run.py` aggregation -> `report.json` (per-incident verdict + SOLVED/PARTIAL/MISS aggregate + gap-charters). Report to COO~B.
2. **[2.0.0_SA_COO~B]** relays MSTR's solver_results bank + pings CVO~B for judge_axes in parallel.
3. **[3.0.0_SA_CVO~B]** B2 judge: `judge_view` per case -> reach/usability/grounding_resilience axes.
4. **[future, non-blocking -- CTO-flagged]** if any future corpus incident's resolution lives in SharePoint, the m365 live tool needs per-incident scoping (the filesystem allowlist covers repo only).
