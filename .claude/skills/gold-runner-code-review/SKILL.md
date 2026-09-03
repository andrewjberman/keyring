---
name: gold-runner-code-review
description: Exhaustive per-script code review of a whole gold runner (INF / 49F / COT): one reviewer subagent per script for type, incremental-vs-full, unguarded-read, dtype and served-number defects; adversarial verification of each material finding; per-agent reports persisted to a colocated folder; then fix-or-flag one by one with a FIX_LOG and commit.
---

# /gold-runner-code-review -- exhaustive gold-runner review (fan-out + drive)

Reviews EVERY script in a pipeline's gold runner for defects that either FAIL the gold run
(crash/abort the no-timeout hard-fail chain) or SILENTLY CORRUPT a served number, then works the
findings to landed fixes. Four phases: **enumerate -> fan-out -> persist -> drive**. Designed to run
identically for INF, 49F, and COT -- pass the pipeline; the framework is the same.

## Invocation

`/gold-runner-code-review <pipeline>` where `<pipeline>` in `{inf, 49f, cot}` (or an explicit gold-dir).
Optional: `... resume` (re-persist + continue the drive from an existing reports folder without re-running
the fan-out), `... fanout-only` (stop after persist -- produce the reports, defer the drive).

## Pipeline config (Step 0 -- RESOLVE, do not assume)

Only INF is confirmed from the abstraction session; **resolve + verify** the others before fanning out
(don't hardcode a wrong tree -- a review of the wrong dir is worse than useless). Use
`comp-estate --resource <name>` / `comp-which "where is the <pipeline> gold runner"` / a Glob to confirm the gold
dir + the dispatcher + the served bucket.

| pipeline | gold scripts dir | dispatcher (chain runner) | served bucket | reports root |
|---|---|---|---|---|
| **inf** | `data/inf/scripts/gold/INF_*.py` | `data/inf/scripts/gold/orion-gold-dispatch.sh` (CHAIN_FULL / CHAIN_INCREMENTAL) | `opal-data-inf` | `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/<TAG>_bughunt_reports/` |
| **49f** | RESOLVE (likely `data/black_diamond/scripts/gold/*.py`) | RESOLVE (the BD gold dispatcher) | RESOLVE (`opal-data-bd`?) | RESOLVE (owner's deliverables dir) |
| **cot** | RESOLVE (Cottonwood / ADVI_COTETL gold tree) | RESOLVE | RESOLVE (cot bucket -- **cot is a SEPARATE firm pipeline from bd**, never mirror) | RESOLVE |

Confirm each RESOLVE against the graph/comp-tools before Step 1. Record the resolved config in the run.

## Step 1 -- enumerate the gold scripts (CHAIN ORDER)

Glob the gold dir for the runner's scripts. Order them in **chain execution order** (dimensions ->
canonical -> client/account -> served/D), not alphabetical -- the drive proceeds in this order so an
upstream fix lands before its consumers are reviewed. Read the dispatcher's chain string to get the
true order when the filename prefixes are ambiguous. Exclude non-runner files (deprecated no-ops still
count -- they review as CLEAN fast). Produce a JSON array of script paths.

## Step 2 -- fan out the review workflow

Call the **Workflow** tool with the bundled engine and the script list as `args`:

```
Workflow({
  scriptPath: ".claude/skills/gold-runner-code-review/gold_runner_review_workflow.js",
  args: {
    pipeline:   "inf",
    dispatcher: "data/inf/scripts/gold/orion-gold-dispatch.sh",
    full_chain: "CHAIN_FULL",
    incr_chain: "CHAIN_INCREMENTAL",
    scripts:    ["data/inf/scripts/gold/INF_A_-1.materialize_txn_cache.py", ...],  // ACTUAL JSON array, not a string
    context:    "<pipeline-specific notes: known defect classes, silver dtype conventions, etc.>"
  }
})
```

Pass `args.scripts` as a **real JSON array** (a stringified list breaks the engine). The engine runs one
reviewer per script (schema-forced structured output) and, for each critical/high finding, an
adversarial-verify agent (try-to-refute; default refuted if no concrete trigger). It returns
`{pipeline, reviewed, total, confirmed_defects, all}`. Workflow runs in the background; you're notified
on completion. The result and per-agent journal live under `<session>/subagents/workflows/<runId>/`.

## Step 3 -- persist the granular per-agent reports (colocated, retained)

The workflow return is large; the AUTHORITATIVE per-agent source is the run's `journal.jsonl` (one
`result` line per agent). Persist with the bundled helper:

```
python .claude/skills/gold-runner-code-review/persist_reports.py \
  <session>/subagents/workflows/<runId>/journal.jsonl \
  <reports_root> <pipeline> <runId>
```

This writes, into ONE colocated folder: `review_<script>.md` per reviewer (findings formatted),
`verify_NN_<target>.md` per verify agent, `INDEX.md` (navigation table only), and a `FIX_LOG.md`
scaffold (only if absent -- it never clobbers an in-progress drive log). **Commit the folder** via
`safe-commit.sh` so the analysis artifacts are durable + shareable BEFORE the drive starts.
Granularity is deliberate -- do NOT collapse to an aggregated summary; the per-report files are the
working surface, and aggregation/triage is a later, optional step.

## Step 4 -- DRIVE the reports one-by-one (ground-truth -> fix / flag -> log -> commit)

Work the reports in chain order, one at a time. For each report:

1. **Read the report**, then **ground-truth every finding against the actual SOURCE** -- never fix off
   the reviewer's claim alone (reviewers over- and under-call; verify the mechanism at the cited line +
   trace the dtype/control flow). A "clean" verdict gets a quick structural sanity glance, not a re-review.
2. **Classify each finding:**
   - **SAFE FIX (apply autonomously):** a guard/normalization with NO correct-case behavior change --
     dtype coercion (`to_numeric(...).astype('Int64')`), unguarded-read guard / fail-open, fail-loud on a
     systematic-or-newest-partition failure (vs `except->WARN->return 0` that serves stale as "success"),
     `groupby(dropna=False)` / catch-all bucket to stop a silent NA-key row-drop, deterministic dtype pin
     across partitions, an observability WARN that surfaces a silent drop with its count + $ magnitude.
   - **DESIGN ITEM (flag, do NOT patch):** anything that CHANGES a served tax / AUA / NNA / cost-basis
     number through a cross-script data-lineage or data-semantics decision (which universe anchors a
     calc; union-vs-inner spine; whether reversals reuse a type_desc; retire/re-point a derivation).
     A naive patch here can worsen a served number. Write it up as a DESIGN ITEM in the FIX_LOG and
     ROUTE it to the owning exec (CVO for served-cert, CTO for architecture, COO to sequence). If it
     hits served tax/AUA, flag EARLY, not at end-of-sweep.
   - **NO-FIX:** reviewer refuted / not-actionable in isolation / inert (e.g. a skip-gate bug gated
     behind a disabled feature flag) / genuinely clean -- record it in the FIX_LOG no-fix section with why.
3. **Apply the safe fixes**, respecting the pipeline's rules (silver = dedup+dtype only; `from __future__
   import annotations`; no emojis/non-ASCII in AWS-run code; ground the MECHANISM, not just the symptom).
4. **Gate + commit + deploy** via the pipeline's cycle: `.tools/commit-gate.sh <file>` ->
   `.tools/safe-commit.sh --author "<serial> <...>" -m "<msg>" -- <file>` -> `HALT_ACK=1 git push origin
   <branch>` (the safe-deploy pre-push hook auto-deploys gold code). **Batch commits** across a few
   reports for speed (git is slow); push periodically so nothing strands. VERIFY a served-facing deploy
   against the live artifact (`comp-pipescript deployed` / md5-vs-S3), never against the graph alone.
5. **Log every fix in the FIX_LOG** the moment it lands: `FIX-NNN -- <script>: <one-line> (report N,
   finding K, <severity>)` + file/function + defect + fix + **commit hash** + verify verdict. Cite which
   report it originated from. Keep the DESIGN ITEMS + no-fix sections current too. The FIX_LOG is the
   deliverable's spine -- it must always reflect what actually landed.
6. **Present each report's analysis** to the user as you go (validated finding, verdict, action) so they
   can steer -- this is a one-at-a-time collaborative drive, not a silent batch.

## Discipline (why this framework, banked from the INF pass)

- **Fan-out beats solo** for coverage: one reviewer per script in parallel finds more than a single
  serial pass, and the adversarial-verify layer kills plausible-but-wrong criticals before they waste a fix.
- **Ground-truth before fixing.** The reviewer's severity is a hypothesis. The INF pass had a "critical"
  merge-crash that was actually inert (the dtypes align in practice -- proven by a populated served
  number, not the reviewer's dtype inference). Verify the live/served state, then the source mechanism.
- **Safe-fix vs design-item is the load-bearing split.** Guards and observability never worsen a correct
  number; a served-number-changing lineage change can. The INF pass surfaced a 13.6x-overstated served
  client-tax (a derivation vs an existing native dim) that was CORRECTLY escalated (CVO -> CTO -> COO
  re-point), never autonomously patched.
- **The FIX_LOG + colocated reports ARE the retained artifact.** One folder, one file per agent, a
  running fix log citing report+commit, a design-items register. Repeatable per pipeline; that folder is
  the audit trail and the handoff surface.

## Notes

- Scale the fan-out to the runner size (INF = 46 scripts). The Workflow concurrency cap (~10-16) queues
  the rest; all complete.
- Deprecated no-op scripts still get a reviewer (they return CLEAN fast) -- coverage completeness matters.
- If the workflow's output-file parse looks empty, read `journal.jsonl` directly -- it is the reliable
  per-agent source (the wrapped output file is not a plain JSON of the return).
