# NFRA_COMPPROOF B -- blind-solver AFFORDANCE SPEC (clean-room mechanism; CTO FINAL)

The spine's validity rests on the blind-solver reaching root cause from the SUBSTRATE, not by
looking the answer up. Because these are REAL historical incidents whose root-cause is documented in
the repo, there are **THREE** leak vectors -- all closed (CTO ruling chain 143421Z / 143701Z /
143953Z / **154055Z TRUE-SANDBOX**; MSTR /seams enforcement ground-truth found the residual 2):

- **Vector 1 -- CONTEXT-INJECTION (no tool-call):** a fabric-lane spawn auto-injects CLAUDE.md +
  memory-recall + org/XXX.md via system-reminders. CLAUDE.md states several corpus root-causes
  VERBATIM (incl. #1 ADVI_BREAKS). Invisible to a file-read audit. -> closed by the **sanitized
  bare-launch** + the `assert_clean_context()` / `assert_live_context_clean()` gates AND (TRUE-SANDBOX)
  the injection-marker files (CLAUDE.md / org/XXX.md / memory) are ABSENT from the solver's sandbox cwd.
- **Vector 2 -- FILE-READ answer-lookup:** the solver Reads/Greps the incident's narrative/resolution
  record -- OR the compproof answer-key `corpus.py`, which used to sit in the ALLOWED org/modules/graph
  tree (MSTR finding-1). -> closed PRIMARILY by the **TRUE-SANDBOX**: the solver runs in a FILTERED REPO
  COPY where the ENTIRE forbidden set is PHYSICALLY ABSENT (+ no `.git`, so no `git show HEAD:<forbidden>`
  recover), so a broad `grep -r X .` finds nothing forbidden. The **tool-log path-audit** (`cheat_check`,
  now incl. `org/modules/graph/compproof/`) stays as the post-hoc backstop for any absolute-path read.
- **Vector 3 -- GRAPH-CONTENT answer-lookup (MSTR finding-2):** comp-kuzu / comp-blast are ALLOWED, so
  if the derive ever indexed narrative prose as node CONTENT, the answer could arrive via the graph. ->
  closed by `assert_graph_no_narrative()` (fail-loud if any node name/props carries a narrative marker;
  the structural graph asserts 0 today; guards a future derive regression).

TRUE-SANDBOX (prevention) + context-gate + graph-check + the post-hoc file-audit (backstop) =
DEFENSE-IN-DEPTH. NOT claimed "airtight" -- these are layered guards MSTR /seams re-tests, not a proof.

## The allow / deny boundary (CTO clean-room)

**ALLOWED** (the substrate B tests -- reaching root cause via these = a valid GRAPH-SOLVED; it is what
the real ADVI_BREAKS solve used):
- comp-tools: comp-which / kuzu / blast / trace / xref / platinum / drift / freshness / pipescript /
  lambdamap / iam / routes / depth
- the graph DB (Nessie / Kuzu @ marker HEAD)
- LIVE / served estate reads: S3 / SSM / DynamoDB / served artifacts (read-only)
- SOURCE CODE: `data/*/scripts`, `infra/`, `portal/`, `org/modules/graph` (the module source)

**FORBIDDEN** (answer-lookup = a FALSE solve; reading one VOIDs the run). LOCATION-AGNOSTIC + NAME-
VARIANT-aware -- the org/docs-scoping was a completeness bug (COO~B 171554Z: a top-level `logs/` +
a `session_logs/` variant leaked past `find org`/`find docs`). The TRUE-SANDBOX removes ALL of these
ANYWHERE in the tree:
- ANY narrative-container DIR, any location + name variant: `logs/`, `session_logs/`, `sessions/`,
  `threads/`, `handoffs/`, `daily_log/`, `change_management/`, `org/critical_paths/**`
- ANY `*postmortem*` (file or dir), any location -- documented incident resolutions
- `org/modules/graph/debtscan/**` (incident debtscan ledgers)
- `memory/**`; `CLAUDE.md` + `org/XXX.md` (incident-prose / fabric-injection markers); any `*compiler-tools-log*`
- the answer-key `org/modules/graph/compproof/**` (corpus.py = the sealed root-causes)
- EACH corpus incident's DEFINITE citation record (`harness.resolution_artifacts`) wherever it lives,
  incl. under otherwise-allowed trees (e.g. `docs/architecture/*_PRD.md`, `org/projects/*.json`)
- a broad answer-bearing narrative `.md` name sweep (incident/retrospective/reconciliation/session_log/
  handoff/closeout/ledger), any location

CTO RULED ALLOWLIST (175214Z) -- now THE model (build_sandbox.sh default). The sandbox COPIES ONLY the
allowed source substrate: `data/*/scripts` + `infra/` + `portal/` + `org/modules/graph` (MINUS the
answer-key + debtscan). DOCS DROPPED; all `org/` except `org/modules/graph` dropped; project-JSONs
dropped. The forbidden narrative/answer set is absent BY CONSTRUCTION (never copied) -> PROVABLY
complete (a blocklist cannot be -- narrative scatters through otherwise-"allowed" trees; the real
ADVI_BREAKS solve used SOURCE + live SSM/S3 + graph + comp-tools, NOT arch-docs-for-the-answer, so
docs-absent does not change what B measures). The FORBIDDEN list above is retained by the fallback
blocklist mode (`COMPPROOF_SANDBOX_MODE=blocklist`) + as the belt-scrub WITHIN the allowlist's copied
trees (answer-key/debtscan under org/modules/graph). LOAD-BEARING GUARD (CTO guard #1): build_sandbox.sh
asserts GRAPH-COVERAGE -- every graph-referenced repo-source ROOT + every data-firm-with-scripts is
present in the template; an under-enumerated allowlist would false-MISS a reachable source -> B
UNDER-scores. (Guard #2: a specific non-narrative reference genuinely needed = an explicit reviewed +
narrative-checked add; default is docs-absent.)

Enforced in code: **TRUE-SANDBOX** `build_sandbox.sh` (ALLOWLIST copy-only-allowed default -> forbidden
absent BY CONSTRUCTION + GRAPH-COVERAGE guard; blocklist fallback mode; no `.git`; fail-closed self-verify)
+ `spawn_solver.sh` (per-solver sandbox cwd); `harness._is_forbidden_path()`
(now incl. `org/modules/graph/compproof/`) + `harness.cheat_check()` (post-hoc backstop audit) +
`harness.resolution_artifacts()` (THIS incident's citation) + `harness.assert_graph_no_narrative()`
(Vector-3 graph-content check).

## 1. LAUNCH -- sanitized bare-launch (Vector-1 close)

Spawn each solver as a SEPARATE PROCESS via `claude -p "<solver-view>"`, in a **sanitized cwd**:
- a temp dir OUTSIDE the workspace tree (so `claude` walks up and finds NO CLAUDE.md / memory / org/XXX.md)
- memory auto-recall OFF; NO org/XXX.md fabric register/startup; NO fabric-lane spawn wrapper
  (spawn-agent.ps1 does fabric-startup; a subagent inherits the spawner's answer-saturated context --
  BOTH disqualified per MSTR).
- FULL file-access to the substrate is RETAINED -- the solver reads source / runs comp-tools / queries
  live AWS by absolute path + PATH tools. Only the AUTO-INJECTED context is suppressed.

**Pre-flight gate (NEVER#4 PROXY):** `harness.assert_clean_context(launch_cwd)` must return
`clean=True` before any real spawn -- it walks up from the cwd and asserts no injection marker
(CLAUDE.md/org-XXX/memory) is discoverable. `reference: spawn_solver.sh`.

**Standing per-run gate (NEVER#4 DIRECT, CTO 144725Z belt-and-suspenders):**
`harness.assert_live_context_clean(injected_context, incident)` reads the launched solver's ACTUAL
initial injected context (captured from its transcript's system prompt + first system-reminders,
pre-traversal) and asserts it is narrative-free -- no generic fabric marker AND none of the incident's
sealed root-cause distinctive terms. This is STRONGER than the file-presence proxy: it catches a
runtime-injection vector the proxy misses (e.g. a global ~/.claude hook injecting answer-bearing
content with no file up-tree). Wired into `run_incident` (VOID on any injected narrative/answer) when
the launch captures `injected_context`. A false-clean silently false-SOLVES the whole corpus.

## 2. CAPTURE -- the actual tool-log (not self-report)

Capture EVERY Read / Grep / comp-tool call the solver makes (its actual tool-log), not just its
self-reported `traversal_path`. This captured log is what the judge audits. (`claude -p` with a
tool-call-logging output mode; `spawn_solver.sh` captures it to `tool_log_<case>.jsonl`.)

## 3. AUDIT -- the tool-log path-audit VOID-gate (Vector-2 close, B2 judge HARD gate)

`harness.cheat_check(tool_log, incident)` -> VOID the run if the captured tool-log includes ANY
Read/Grep of a FORBIDDEN path (citation-specific OR narrative-category). VOID = answer-lookup, NOT
SOLVED. Wired into `harness.run_incident` (prefers `solver_result["tool_log"]` over self-reported path).

## Data contract (keyed by opaque case_id B-NN)

```json
solver_results[case_id] = {
  "concluded_root_cause": "<mechanism>",
  "traversal_path": ["<self-reported step>", "..."],
  "tool_log": ["<actual Read/Grep/comp-tool call>", "..."],   // authoritative for the file-read audit
  "injected_context": "<the solver's INITIAL system prompt + system-reminders, pre-traversal>",  // live-context gate
  "confidence": "low|med|high"
}
judge_axes[case_id] = { "reach": "yes|narrowed|no", "usability": "usable|too-slow|fell-back",
                        "grounding_resilience": "resist|trip" }   // CVO/TO-B2
```

## Run flow

1. `assert_clean_context(cwd)` clean + live canary clean  ->  MSTR fires.
2. MSTR: per case, `spawn_solver.sh <case_id>` (emit answer-free payload -> sanitized `claude -p` ->
   capture tool_log) -> `solver_results[case_id]`.
3. CVO~B (TO-B2): judge concluded-root-cause + path vs the sealed judge-view -> `judge_axes[case_id]`.
4. ~D (author, DRIVER only): `blind_run.py --solver-results ... --judge-axes ...` -> isolation-gate +
   tool-log path-audit + 3-axis score + aggregate + gap-charters. ~D never solves/judges.

Author: 0.8.0_AE_CloudComp~D (NFRA_COMPPROOF.B1). 2026-07-01.
