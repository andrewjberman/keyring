---
name: prd-delta
description: Per-project PRD-vs-reality completeness: for each not-closed project, cross-reference the PRD's promised deliverables against real TO status and commit evidence -> a completeness percentage, what is still missing, registry-mismatch and undocumented-activity flags. Runs in the main session (no subagent fan-out); mechanics in `.tools/prd-delta.py`, judgment the session's. Text report + Desktop HTML dashboard. Read-only.
---

# /prd-delta -- per-project PRD-vs-reality completeness assessment

Answers a question none of its sibling lenses answer: **for each project, how much
of what the PRD actually promises has landed** -- not "is there a PRD" (`/registry-check`),
not "what TOs exist" (`/to-check`), not "what got committed" (`/activity-check`), but
*PRD deliverables cross-referenced against real TO status + real commit evidence*,
scored and itemized. It is an LLM judgment pass, not a keyword count -- a strong
triage signal, not a certified audit.

**This runs in the MAIN SESSION as a single agent -- it is NOT a subagent fan-out.**
That is deliberate and load-bearing (see "Why single-agent" below): the completeness
judgment needs the session's accumulated context (the conventions, prior findings, and
project history built up this session), the live **comp-tool rails** (Rule 20/21 -- the
graph/estate/blast tools are the right way to resolve a genuinely-ambiguous "did
this actually land" question, not raw grep), and **CLAUDE.md awareness** (verify against
served/live state not self-report, ground the mechanism, firm-separation, etc.). A cold
subagent has none of that, which is exactly why the earlier fan-out version was both less
accurate and far more expensive -- it was retired.

**Directly serves D-001 PHASE 2** (`org/tier0/DIRECTIVES.md`): "validate each project
... confirm every key number is correct and reasonable ... apply the same methodology
retroactively to the HISTORICAL Completed / Archived rows." `/prd-delta --project CODE`
on a closed project is exactly that retroactive check, mechanically enabled.

## Invocation

| Form | Scope |
|---|---|
| `/prd-delta` | Hot projects (registry-check's HOT set -- worked <72 working-h, not closed) |
| `/prd-delta --all` | Hot + cold (every not-closed project) |
| `/prd-delta --project CODE` | One project, any status -- including closed/archived (retroactive-sweep use) |

Default (`/prd-delta`) is ~30+ projects -- a real sweep, not instant. `--project CODE`
is the fast path for a single project; use it when triaging one thing.

## Mechanics (the session agent follows this directly -- no subagents)

**Step 1 -- determine scope (mechanical):**

```bash
python .tools/prd-delta.py --list-scope             # hot (default)
python .tools/prd-delta.py --list-scope --all        # hot + cold
python .tools/prd-delta.py --list-scope --project CODE
```

Returns `[{code, status, prd_found, prd_count, prd_source, prd_paths}, ...]`.
`prd_source` is `"registry"` when `org/projects/{code}.json`'s own `prds` field
resolved it (authoritative -- includes parent-project PRDs for sub-projects and
multi-doc PRD histories), or a `"filename-*"` value on fallback. A `prd_found:false`
project is genuinely spec-less -- record it as NO-PRD, do not fabricate deliverables.

**Step 2 -- assess each project, ONE AT A TIME (this is the session agent's work):**

For each scope entry with `prd_found:true`, run:

```bash
python .tools/prd-delta.py --evidence {CODE}
```

It returns the full evidence bundle: `prd_docs` (an ARRAY -- every registry-declared
PRD doc, each `{path, label, date, exists, text}`; **read all of them**, a sub-project's
real spec may be its parent's PRD, and a project may have amendments), `registry`
(`org/projects/{CODE}.json`), `tos` (every task-order's parsed fields --
`to_id`/`title`/`status_class`/`assigned_to`/`issued_date`), and `commits` (every git
commit whose message references the code -- `sha`/`iso`/`author`/`subject`).

**Then judge it -- this is where the session context earns its keep:**

- Read every `prd_docs[].text` (skip `exists:false` -- a stale registry pointer, not a
  deliverable source). Extract each discrete deliverable: look at Scope, Goal, "TO
  candidates", "Acceptance criteria", numbered phases, enumerated lists (PRDs here
  structure work this way). Later-dated docs amend/supersede earlier ones on conflict.
- For each deliverable, cross-reference: (a) is there a TO covering it, and its
  `status_class`? (b) is there a commit whose subject shows it was actually BUILT/LANDED
  (not merely a TO-filing / decomposition / registry-bookkeeping commit)? (c) does the
  registry phase/status corroborate?
- **Be conservative (CLAUDE.md discipline):** a filed TO with zero matching landed-work
  commits is *queued, not done*; a commit that only adds/edits a TO file is not landed
  work; a self-report of "complete" without an artifact commit does not count. When "did
  X actually land" is genuinely ambiguous from the bundle, **resolve it the workspace
  way** -- `comp-which "<plain-English question>"` to route to the right comp-tool
  (`comp-pipescript`/`comp-blast`/`comp-freshness`/`comp-kuzu` etc.), or verify against
  the served/live artifact -- NOT a raw grep (Rule 21). You have these tools; the old
  fan-out did not. Prefer one grounded comp-tool check over three guesses.
- Efficiency: process and emit per-project, then move on -- do **not** hold all 30+ raw
  bundles in context at once. Keep only the compact assessment object per project.

Compute `completeness_pct = round(100 * landed-deliverables / total-deliverables)`.
Label: `0`=NOT-STARTED, `1-30`=EARLY, `31-70`=IN-PROGRESS, `71-99`=MOSTLY-COMPLETE,
`100`=COMPLETE. Set `registry_mismatch` (short string, else null) when the registry's
claimed status/phase disagrees with the evidence. Set `undocumented_activity` (array,
else empty) for TOs/commits referencing the code that map to no PRD deliverable
(scope-creep or a stale PRD). Write `missing[]` as short, standalone natural-language
bullets a non-specialist can read.

**Step 3 -- assemble + persist.** Build one object:

```json
{ "generated_scope": N, "with_prd": N, "no_prd": N, "results": [
  { "code", "completeness_pct", "completeness_label",
    "items": [ {"item","verdict","evidence"} ],
    "missing": [ ... ], "registry_mismatch": null|"...",
    "undocumented_activity": [ ... ], "status": "assessed" }
] }
```

Each `prd_found:false` project gets a stub result: `completeness_pct:null`,
`completeness_label:"NO-PRD"`, `status:"no-prd"`, and a `missing[]` line naming the gap.
Write the whole object to `org/mcp/prd_delta_results/latest.json` (**UTF-8 no BOM** --
the renderers tolerate a BOM via `utf-8-sig` but write clean). The report + dashboard
read ONLY this file, so persist before rendering.

**Step 4 -- render both views** (always both unless the user says text-only):

```bash
python .tools/prd-delta-report.py                                   # text lens, stdout
python .claude/skills/prd-delta/render_prd_delta_dashboard.py       # -> Desktop/Opal_PRDDelta_Dashboard.html
```

Then `SendUserFile` the dashboard with `display: render`.

## What the dashboard shows

One card per project, sorted worst-completeness first: a colored horizontal completion
bar (red <50%, amber 50-89%, green >=90%, gray = no PRD), a `Missing` bullet list, a red
`REGISTRY MISMATCH` banner when the registry disagrees with the evidence, and a purple
`Undocumented activity` note when TOs/commits exist that no PRD item explains.

## Why single-agent (not a fan-out)

- **Accuracy > parallelism for judgment work.** The completeness call is holistic
  judgment against a prose PRD -- the kind of task where shared context and the live
  harness matter more than wall-clock speed. A cold per-project subagent re-derives the
  workspace conventions from scratch every time, has no comp-tool rails or CLAUDE.md
  discipline injected, and (given tools + a fuzzy task) burns tokens on unbounded
  exploration with no natural stop condition. The empirical result when this ran as a
  32-agent fan-out: ~2.2M tokens and a real accuracy risk (confident mis-reads of
  "filed" as "landed"). Retired in favor of this.
- **The split that IS right stays:** mechanical evidence-gathering is a deterministic
  script (`.tools/prd-delta.py` -- zero judgment, no drift from the sibling lenses); only
  the judgment is the agent's, and it belongs in the session that has the context to make
  it well.
- **Cost/latency tradeoff, stated honestly:** single-agent is sequential, so a full
  `/prd-delta` sweep of 30+ projects takes a while and consumes main-session context.
  That is the accepted cost of doing it accurately. Use `--project CODE` for a fast
  single-project pass; use the full sweep when you actually want the whole board.

## Design notes

- **Engine (`.tools/prd-delta.py`) does ONLY mechanical evidence-gathering** -- reuses
  `registry-check.py`'s `--json -all` contract for scope/status and `to-check.py`'s
  `parse_to_file()`/`find_all_to_files()` for TOs (nothing drifts from the sibling
  lenses). PRD resolution reads the registry's authoritative `prds` field first, filename
  guessing only as fallback. Commit resolution is `git log --all -i --grep CODE` (cap 80).
- **No-PRD projects are reported, not skipped** -- a project with real TOs/commits but no
  written spec is itself a finding.
- Read-only. Never dispatches, never edits a PRD or a TO. A lens, like its siblings.
