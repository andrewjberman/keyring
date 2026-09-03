# Session Log Standard

Full template and role-specific additions. Referenced from XXX.md.

---

## Base Template

```markdown
# [Thesis Title] — [Agent Serial]

**Date:** YYYY-MM-DD
**Task Order:** {project_code}.{task_id} or ad-hoc slug
**Status:** COMPLETE | IN PROGRESS | BLOCKED

---

## Objective

[1-3 sentences: what was set out to accomplish and why.]

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-pipescript io | io D_XX | PASS/WARN/FAIL/SKIPPED | one-line description |

Results: PASS=accurate+useful | PARTIAL=present but noisy | FAIL=wrong/crash/silent | SKIPPED=explain why | WARN=empty+correct WARN message

**What worked:** [which tools saved time, replaced manual grepping]
**What failed:** [wrong output, silent failure, missing coverage]
**Gap found:** [new pattern the tools couldn't answer — or "none"]

**DO NOT append to or commit `org/compiler-tools-log.md`.** The auto-append was RETIRED Andrew-direct
2026-07-29 (LD-0348, killed at source in `comp_log_auto.py:_append_log`). The file is PRESERVED at its
committed state as readable history — never commit it, never re-point a writer at it. This section
stands on its own; there is no second place to write it.
*(Corrected 2026-07-30 by 2.0.0_SA_COO — this line still instructed the append while `org/XXX.md` said
RETIRED in three separate places. The contradiction lived in the doc agents follow WHILE WRITING a log,
so it was the copy most likely to be obeyed.)*

---

## Work Completed

[Numbered sections for distinct work units. Be specific: function names, S3 paths,
commit hashes, actual output. Use tables for structured data.]

### 1. [First work unit]
...

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| [What was decided] | [Why — alternatives considered if significant] |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `path/to/file.py` | What changed | Yes — `abc1234` / No — local only |

---

## Blockers

[See Blocker Verification Protocol below before writing BLOCKED.]

- BLOCKED on [agent serial]: [task order path] — waiting for [specific deliverable].

---

## Current State

> Primary handoff point. Write as if briefing someone with zero prior context.

[2-4 dense sentences. Name files, functions, AWS resources, commit hashes, S3 paths.]

---

## Next Steps

1. **[Action verb] [specific thing]** — [why]
2. **[0.4.0_DE_ClientPlatform] [specific action]** — [cross-agent handoff]
```

---

## Role-Specific Additions

### DE — add to header:
```
**Portal DEV commits:** `abc1234` → `def5678`
**Workspace CLOUD commit:** `jkl3456`
```
Files Modified table must include commit hash. When work breaks something, add a
`## Postmortem` section between Work Completed and Decisions Made: Root Cause, shape/contract
mismatch table, Resolution tracking.

### DS — add before Current State:
```markdown
## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| DevOps brief | `docs/briefs/devops-brief-{feature}.md` | DevOps |
| Data contract | `docs/briefs/dashboard-engineer-{feature}-data-contract.md` | DE |
```
Next Steps must name the receiving agent in brackets: `[0.4.0_DT_ClientPlatform] Deploy to EC2`.

### DT/AE — replace Work Completed with Deployment Sequence table:
```markdown
## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit source | `abc1234` |
| 2 | build-and-upload.sh | SHA256: `AbCdEf...=` |
| 3 | Commit source map | `def5678` |
| 4 | terraform plan | N changed |
| 5 | terraform apply | N added, N changed |
| 6 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 7 | Update core doc | deployment_map.xml |
| 8 | record-deploy + tag + push | `ghi9012`, tag `pipeline-vX.Y.Z` |

## Verification
[Paste actual output — S3 sizes, data checksums, API snippet, or CLI output.]
```

### RD — add to header:
```
**Portal DEV commit:** `abc1234`
```

---

## Compiler Tools — Role Minimums

| Role | Minimum — run before starting work | Skip only if |
|------|-------------------------------------|--------------|
| DS | `comp-pipescript io {script}` for every gold script touched | No s3_layout imports (run anyway, report WARN) |
| DS | `comp-blast {script}` before any schema change to a write target | |
| DE | `comp-transform schema-check {Component}` before touching data props | Pure layout/style change |
| DE | `comp-blast {endpoint_fn}` before deleting any function | |
| DE | `comp-cache collisions` before adding any React Query key | |
| DT | `comp-pipescript io {script}` for every script deployed | |
| AE | `comp-pipescript io {script}` + `comp-routes trace {fn}` for Lambda/CF changes | |
| RD | `comp-transform fields {Component}` for every component rendering data | Pure style change |

If no tools were run: write one sentence explaining why. Blank is not acceptable.

---

## Blocker Verification Protocol

Never declare BLOCKED based on assumption. Before writing a blocker:

**Step 1 — Check the blocking agent's directory:**
```
{agent_folder}/logs/{most_recent_date}/    — what they last worked on
{agent_folder}/task_orders/                — what they have been asked to do
```

**Step 2 — Classify:**

| Evidence | Classification | What to write |
|----------|---------------|---------------|
| Log/task order confirms dependency is delivered | Not blocked | Use the output and proceed |
| Log/task order confirms it is in progress | BLOCKED | Name agent, task order, specific deliverable |
| Nothing corroborates either state | AMBIGUOUS | Escalate to DE/COO |

**BLOCKED format:**
```
- BLOCKED on [agent serial]: [task order path] — waiting for [specific deliverable].
  Evidence: [log or task order path that confirms it is in flight].
```

**AMBIGUOUS format:**
```
- AMBIGUOUS: [agent serial] has no log/task order corroborating status of [deliverable].
  Escalate to DE/COO.
```

If checking the directory resolves the question — proceed, don't write a blocker.

---

## Step log — the per-seat INPUT/OUTPUT record of an end-to-end pass of the canonical fabric workflow

Distinct from the session log above. When a round of the canonical fabric workflow
(`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`) reaches its L10 stamp, **every seat that acted on the
project** writes ONE machine-readable step log — one row per act, each row carrying the limb, the act, its
inputs and outputs as typed references, and the spine clause followed or `NONE`. The seat RECORDS; it never
assigns a quadrant. `1.0.0_SA_CTO` compiles every seat's file against the spine into the four quadrants
(on-plan efficient · on-plan deficient = plan improvement · off-plan efficient = flexibility or plan improvement ·
off-plan deficient = gate candidate).

- **Schema (normative):** `org/standards/STEP_LOG.schema.json`.
- **Home:** `org/missions/D<n>/<MACRO>/<CODE>/ledger/STEP_LOG.<serial>.round<N>.json` (lane ANY).
- **Trigger:** the round's L10 stamp; nothing about the step log gates the stamp or the next round.
- **Authority:** Andrew-direct 2026-09-03 ~04:2xZ at the `2.0.0_SA_COO` terminal
  (`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260903_042xZ_PER_AGENT_STEP_LOGS_INPUT_OUTPUT_FOR_CTO_LOOP_COMPILATION.md`).
