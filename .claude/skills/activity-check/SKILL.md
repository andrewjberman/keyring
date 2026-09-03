---
name: activity-check
description: Recent-commit activity per ACTIVE agent (last N days, default 7) with three pie charts (macros, projects, agents). `/activity-check`; the HTML dashboard via render_activity_dashboard.py. Read-only. Sister to /registry-check (project axis) and /to-check (task-order axis). Engine `.tools/activity-check.py`.
---

# /activity-check -- recent-commit activity by active agent + where it's directed

The commit-activity companion to `/registry-check` (project axis) and `/to-check`
(task-order axis). Where those answer "what's on the board" and "who owns which TO",
`/activity-check` answers **"what has each active agent actually been committing, and
where is that recent activity concentrated?"** -- straight from git.

## Invocation

| Form | Shows |
|---|---|
| `/activity-check` | Text lens: each active agent's 5 latest commits + the three top-lists |
| `/activity-check --days N` | Change the activity window (default 7) |
| `/activity-check --json` | Machine-readable (what the dashboard consumes) |

Mechanically: `python .tools/activity-check.py` (add `--days N` / `--json`).

## What it computes

- **Active agent** = a git author whose name is a fabric serial (`N.N.N_ROLE_*`) with
  >=1 commit in the last `--days`. Pod numbers collapse to the **role-agent** (the three
  `AE_PartnerETL` pods -> one `AE_PartnerETL`), matching `/to-check`'s convention.
- **Cards** = for each active agent, their **5 most recent commits** (project-code
  resolved, with age + a macro-colored tag), busiest agent first.
- **Three aggregations, each top-4 + "Other" (5th slice):**
  1. **Macros** -- which macros get the most **project-directed** commits.
  2. **Projects** -- which projects get the most commits.
  3. **Agents** -- which agents commit the most (**all** commits = raw volume).

## Directed vs all (the load-bearing distinction)

A commit is **project-directed** if its message references a known `org/projects/*.json`
code (token-exact, most-specific match -- `SCTY_MCPGUARD` beats `SCTY`). An exec
`drive cycle N` / `/govern` / `log` commit references **no** project, so it is:
- **excluded** from the MACRO and PROJECT charts (it is directed at no project), but
- **counted** in the AGENT chart (it is a real commit -- "most commits" = raw volume).

So the AGENT chart is typically topped by the execs (COO/CTO drive+govern volume),
while the MACRO/PROJECT charts reflect where the *project* work is going. That gap is
itself a signal, not a bug.

## The HTML dashboard (card + pie-chart view)

For the visual -- one card per active agent (its 5 latest commits) plus the three
top-4+Other pie charts with legends + percentages -- use the companion renderer
**`render_activity_dashboard.py`** (this skill dir). Born from Andrew's 2026-07-06 ask.

```bash
python .claude/skills/activity-check/render_activity_dashboard.py            # 7d -> Desktop/Opal_Activity_Dashboard.html
python .claude/skills/activity-check/render_activity_dashboard.py --days 3    # tighter window
python .claude/skills/activity-check/render_activity_dashboard.py --out PATH.html
```

**LIVE + HARDENED:** the renderer consumes the stable `activity-check.py --json` public
contract -- NOT the engine's internal functions -- so an engine refactor cannot silently
break it (only a --json schema change would, which is a loud/deliberate break). No
hand-curated data: re-run and it's current. Default output lands on the Desktop
(`Opal_Activity_Dashboard.html`). Pie slice colors are position-based (top1..4 + gray
Other) so slices never collide.

## Notes

- **Read-only.** Pure git + filesystem, no MCP, no dispatch. A lens, like its sisters.
  (The renderer WRITES one HTML file on explicit ask; the text lens itself writes nothing.)
- **Window semantics.** "Active" and the pie aggregations use the `--days` window
  (default 7); the per-agent cards show each agent's 5 *most recent* commits within it.
  A holiday-spanning 7d window naturally includes the pre-holiday burst -- that is the
  real recent activity.
- **When to use which:** `/registry-check` = "what's on the board" (project axis).
  `/to-check` = "who owns which task order" (TO axis). `/activity-check` = "what has each
  active agent been committing + where is the activity going" (commit axis). Any agent, any time.
- Engine + thresholds: `.tools/activity-check.py` (tune in one place).
