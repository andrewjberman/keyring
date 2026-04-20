# Compiler Tools - Engineer Onboarding Brief

**Date:** 2026-04-15
**Author:** 1.0.0_SA_CTO
**For:** Incoming engineer working on the `comp-*` tools

---

## What this is

Opal Capital runs a fleet of "compiler" CLIs that do static-graph analysis across
the workspace: gold pipeline scripts, portal components, S3 artifact contracts,
Lambda routes, IAM, React Query keys, and related serving/data paths.

The tools live in two layers:

- Operator-facing entrypoints in `.tools/comp-*` (in PATH on every dev machine)
- Builders, indexers, and query code in `org/modules/graph/`

The canonical graph rebuild entrypoint is `comp-build`.

The current tool family includes:

- `comp-blast`
- `comp-trace`
- `comp-platinum`
- `comp-pipescript`
- `comp-routes`
- `comp-cache`
- `comp-iam`
- `comp-pii`
- `comp-transform`
- `comp-validate`

These tools answer questions like:

- what breaks if I change X?
- what platinum keys does this component consume?
- what script writes this artifact?
- is the deployed S3 copy current?

Full catalog and deep-dive docs: `org/modules/graph/comp-tools.yaml`.
Situation-to-command trigger map: `org/XXX.md` ("Compiler Tools - Trigger Table").

---

## Why this matters right now

We just locked a discipline on every task order issued in the org: each TO
carries a `<compiler_tools_mandate>` block of structured
`<run>/<expect>/<if_mismatch>` triads in three phases:

- before-write
- before-commit
- after-commit

Agents must reproduce each `<run>`, record observed output, and log pass/fail
against `<expect>` in the session-log Compiler Tools section. The governing
standard is `org/standards/TO_COMPILER_GATE.md` (Rules 1-7, with Rule 7 added
2026-04-15 for acceptance-criteria flex pre-flagging).

This makes the org a corpus generator for compiler-tool quality signal.
Every TO now produces structured evidence. Gaps between `<expect>` and observed
output expose tool limitations in a machine-readable way.

Andrew's directive: mine that corpus to drive comp-tool optimizations.

---

## Where the feedback lives

**Primary corpus:**

| Source | Path | What's there |
|---|---|---|
| Auto-append log | `org/compiler-tools-log.md` | One row per `comp-*` invocation. Auto-written via `.comp-graph/.agent_context` hook on every tool run. Contains agent serial, TO ID, command, observed result. This is the haystack. |
| Session logs | `org/tier2_senior/{agent}/logs/{date}/*.md` | Each agent's daily logs include a Compiler Tools section reproducing every `<run>` from their TO mandate with explicit pass/fail vs. `<expect>`. Search for "Compiler Graph Gaps Flagged" subsections - those are the explicit tool-limitation callouts. |
| Standard / discipline | `org/standards/TO_COMPILER_GATE.md` | Rules 1-7. Read in full. Rule 7 (acceptance-flex pre-flag) and the failure-mode table at the bottom are the most directly compiler-relevant. |
| Compiler tool specs | `org/modules/graph/comp-tools.yaml` | Per-tool description, intended outputs, and deep docs. |
| Trigger table | `org/XXX.md` ("Compiler Tools - Trigger Table") | Situation-to-command mapping. Also acts as a coverage map: anything we want to ask but cannot is a candidate for a new tool. |
| Improvement history | `org/tier1_exec/1.0.0_SA_CTO/logs/2026-04-14/compiler_toolchain_improvements*.md` | Two recent rounds of CTO-driven comp-tool improvements. Use as format precedent for upgrade proposals. |

**TO mandate examples (good triads):**

- `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_ROLLUP.RF01.ds-d04-window-nna-delta-fix.md`
- `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_ROLLUP.RA-P0.ds-role-aua-canonical-schema.md`
- `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/BDPL_CNPRCS.WP-3.ae-cusip-backfill-silver-transactions.md`

**Read this session log first:**

`org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-15/advi_rollup_rf01_d04_window_nna_delta_fix.md`

DS~A wrote a "Compiler Graph Gaps Flagged" subsection that surfaced concrete
tool limitations during retroactive triad execution. This is the current best
pattern.

---

## Open gap signals already on the backlog

Four live findings as of 2026-04-15. Logged but not yet fully closed:

1. **`comp-blast` does not index function-level Python nodes.**
   Script-level and S3-artifact-level only. `comp-blast _compute_window_decomposition`
   returns "no nodes matching" on a freshly-built graph. This forces audit
   closure at the script grain when the `<expect>` clause asks for a
   function-level answer.

   Candidate fix: extend the graph builder (`comp-build`) to index Python `def`
   AST nodes with parent-script edges. Big lift.

2. **`comp-platinum reverse` does not index nested dict keys.**
   Bare `rfs` and dotted `rfs.decomposition_max.nna` both return empty
   PRODUCER/SERVED/CONSUMED sets. This forces consumer enumeration via the
   `comp-platinum page <Component>` proxy.

   Candidate fix: dotted-path indexing in the platinum reverse-index builder.
   Moderate lift.

3. **`comp-pipescript deployed` subprocess env isolation.**
   The tool spawns `aws` by bare name; the subprocess loses PATH; result is
   "aws CLI not found" despite `aws` being on the parent shell PATH. Manual
   `aws s3api head-object --query ETag` works.

   Candidate fix: pass the full environment to the subprocess or resolve `aws`
   with `shutil.which()` at call site. Small lift.

4. **`comp-pipescript deployed` historically only scanned `code/gold/`, not
   `code/silver/`.**
   Silver-layer enforcer scripts such as `bd_price_update.py` and
   `inject_scoped_overrides.py` were invisible to the deploy-status check.

   Existing TO:
   `org/tier1_exec/1.0.0_SA_CTO/task_orders/comp-pipescript-deployed-silver-scope-extension.md`

   Routed to: `0.7.0_AE_CloudOps`

   Item 3 can fold into the same work, since both gaps live in
   `comp-pipescript deployed`.

---

## How to propose an upgrade

1. Read the gap signal from the corpus - not from your gut.
2. Confirm the gap is reproducible: run the failing `comp-*` command yourself
   against the same target and capture the empty/wrong output.
3. Trace the relevant builder/indexer in `org/modules/graph/`. The
   `.tools/comp-*` shims are usually thin wrappers; the interesting code is
   almost always the builder/indexer/query module under `org/modules/graph/`.
4. Write a one-page proposal under `docs/architecture/COMPILER_*.md` with:
   - Gap statement plus reproduction
   - Affected `<expect>` clauses
   - Proposed fix plus estimated lift
   - Acceptance criteria
5. CTO (`1.0.0_SA_CTO`) ratifies; COO (`2.0.0_SA_COO`) decomposes into a TO
   with the standard triad mandate.

---

## Who owns what

| Role | Who | Responsibility |
|---|---|---|
| Comp-tool authorship history | `1.0.0_SA_CTO` | Wrote most of the original `.tools/comp-*` scripts and `org/modules/graph/` builders |
| `.tools/` infrastructure maintenance | `0.7.0_AE_CloudOps` | Canonical maintenance lane per workspace MEMORY.md |
| Discipline enforcement | `2.0.0_SA_COO` | Reviews TO completion reports against compiler-tool gate rules |
| Corpus consumer (you) | new engineer | Mine the corpus, propose upgrades, partner with AE CloudOps for execution |

---

## Quick start

1. Skim `org/standards/TO_COMPILER_GATE.md` (Rules 1-7).
2. Skim `org/XXX.md` "Compiler Tools - Trigger Table" to feel the surface area.
3. Tail `org/compiler-tools-log.md` to see live tool-invocation rows.
4. Read the DS~A gap-flag session log cited above for the current pattern.
5. Pick one of the four open gaps, reproduce it locally, and pitch a fix
   proposal back to me.
