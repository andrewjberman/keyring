# NFRA_COMPPROOF B -- blind-solver AFFORDANCE SPEC (clean-room mechanism; CTO FINAL)

The spine's validity rests on the blind-solver reaching root cause from the SUBSTRATE, not by
looking the answer up. Because these are REAL historical incidents whose root-cause is documented in
the repo, there are TWO leak vectors -- and both are closed (CTO ruling chain 143421Z / 143701Z /
143953Z; MSTR enforcement ground-truth):

- **Vector 1 -- CONTEXT-INJECTION (no tool-call):** a fabric-lane spawn auto-injects CLAUDE.md +
  memory-recall + org/XXX.md via system-reminders. CLAUDE.md states several corpus root-causes
  VERBATIM (incl. #1 ADVI_BREAKS). Invisible to a file-read audit. -> closed by the **sanitized
  bare-launch** (below) + the `assert_clean_context()` standing gate.
- **Vector 2 -- FILE-READ answer-lookup:** the solver deliberately Reads/Greps the incident's
  narrative/resolution record. -> closed by the **tool-log path-audit VOID-gate** (below).

Context-suppress + file-audit = airtight (belt AND suspenders).

## The allow / deny boundary (CTO clean-room)

**ALLOWED** (the substrate B tests -- reaching root cause via these = a valid GRAPH-SOLVED; it is what
the real ADVI_BREAKS solve used):
- comp-tools: comp-which / kuzu / blast / trace / xref / platinum / drift / freshness / pipescript /
  lambdamap / iam / routes / depth
- the graph DB (Nessie / Kuzu @ marker HEAD)
- LIVE / served estate reads: S3 / SSM / DynamoDB / served artifacts (read-only)
- SOURCE CODE: `data/*/scripts`, `infra/`, `portal/`, `org/modules/graph` (the module source)

**FORBIDDEN** (answer-lookup = a FALSE solve; reading one VOIDs the run):
- `org/critical_paths/**` (change-management ledgers + critical-path records)
- `org/modules/graph/debtscan/**` (incident debtscan ledgers -- resolution records under an otherwise-allowed tree)
- `org/**/logs/**` (session logs) and `org/daily_log/**` (daily narrative)
- `memory/**` (fabric memory)
- `CLAUDE.md` (incident-prose / NEVER-history) and any `*compiler-tools-log*`
- `docs/**` postmortem docs (arch/PRD docs stay ALLOWED -- only postmortems are forbidden)

Enforced in code: `harness._is_forbidden_path()` + `harness.resolution_artifacts()` (THIS incident's
citation, the definite record).

## 1. LAUNCH -- sanitized bare-launch (Vector-1 close)

Spawn each solver as a SEPARATE PROCESS via `claude -p "<solver-view>"`, in a **sanitized cwd**:
- a temp dir OUTSIDE the workspace tree (so `claude` walks up and finds NO CLAUDE.md / memory / org/XXX.md)
- memory auto-recall OFF; NO org/XXX.md fabric register/startup; NO fabric-lane spawn wrapper
  (spawn-agent.ps1 does fabric-startup; a subagent inherits the spawner's answer-saturated context --
  BOTH disqualified per MSTR).
- FULL file-access to the substrate is RETAINED -- the solver reads source / runs comp-tools / queries
  live AWS by absolute path + PATH tools. Only the AUTO-INJECTED context is suppressed.

**Pre-flight gate (NEVER#4):** `harness.assert_clean_context(launch_cwd)` must return `clean=True`
before any real spawn -- it walks up from the cwd and asserts no injection marker
(CLAUDE.md/org-XXX/memory/.claude) is discoverable. A live canary (`claude -p "print your initial
injected context"` in the sanitized cwd, assert no CLAUDE.md/NEVER/memory text) is the belt check MSTR
runs once before firing the corpus. `reference: spawn_solver.sh`.

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
  "tool_log": ["<actual Read/Grep/comp-tool call>", "..."],   // authoritative for the audit
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
