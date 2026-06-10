# /prd-check -- PRD coverage view (which hot projects have TOs filed)

Shows all open projects with PRDs issued within the last 14 days, grouped by
whether they have active (non-complete) TO files. The hot complement to
`/registry-check`'s status view and `/to-check`'s TO drill-down.

## Invocation

| Form | Shows |
|---|---|
| `/prd-check` | Hot projects (PRDs <=14d, not closed), grouped by active-TO vs no-TO |
| `/prd-check --all` | All open projects with any PRD (no age filter) |
| `/prd-check --project CODE` | Single project (any age) |

Mechanically: `python .tools/prd-check.py` (add `--all` / `--project CODE`).

## The format

Two sections:

```
== ACTIVE TOs (N projects) ==
#: N
Project: CODE
Status:  status
PRD:     "label" (YYYY-MM-DD)
TOs (N active):
  [ACTIVE] TO_ID
    -> assignee (short)
    title (truncated)
--------------------------------------------------------

== NO ACTIVE TOs (N projects) ==
#: N
Project: CODE
Status:  status
PRD:     "label" (YYYY-MM-DD)
TOs:     none filed | N total (all closed)
--------------------------------------------------------
```

- **ACTIVE TOs** -- at least one TO file with non-complete status exists for this project.
- **NO ACTIVE TOs** -- either no TO files exist ("none filed") or all filed TOs are complete.
- "none filed" is the signal that TOs have been MCP-inline dispatched but not formalized as TO files -- a filing-discipline gap per CTO ruling (Option D, 2026-06-10).
- Ordered newest PRD date first within each section.

## Status classification (from TO file `<status>` tag)

| Class | First word of status |
|---|---|
| ACTIVE | active, dispatched, in_progress, staged, go, partial |
| PENDING | pending, hold, queued, waiting |
| BLOCKED | blocked |
| COMPLETE | complete, closed, cancelled, done, merged, archived, shipped, superseded |
| ?? (UNKNOWN) | no status tag / unrecognized -- surfaces, never drops |

## Data sources

- **Projects:** `org/projects/*.json` -- `prds[].date` for age filter, `status` for open/closed gate.
- **TO files:** `org/**/task_orders/*.md` -- all 1,319 files, two XML schemas + Markdown format supported.
- **prds entries:** can be `{path, label, date}` dicts OR bare path strings (older format).

## Two robustness properties

1. **Malformed project JSONs surface** under `MALFORMED-JSON` header -- never silently dropped.
2. **Unparseable TO files surface** under `TO-PARSE-ERROR` header -- counted in the footer.

## Notes

- Read-only. Never dispatches. Use `/to-check` to see the full TO detail for any project.
- When "none filed" appears for a hot project: the right fix is to backfill the inline-dispatched TO as a TO file (the canonical form per org/XXX.md); the skill accurately reports the filing state.
- ASCII-only output (Windows console safe, grep/awk safe, no emoji).
- Engine: `.tools/prd-check.py` (tune thresholds and status words there).
