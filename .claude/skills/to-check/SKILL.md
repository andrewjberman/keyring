# /to-check -- active task order view

Enumerates non-complete TO files, grouped by project. Default scope: TOs for
projects with PRDs issued <=14d (the "hot PRD projects"). Drill-down companion
to `/prd-check`'s coverage view.

## Invocation

| Form | Shows |
|---|---|
| `/to-check` | Active TOs for hot PRD projects (PRDs <=14d, not closed) |
| `/to-check --all` | All non-complete TOs across the workspace |
| `/to-check --project CODE` | TOs for one project (any age) |
| `/to-check --assignee SERIAL` | TOs matching agent serial (partial match) |

Filters compose: `--all --assignee DS` shows all workspace TOs assigned to any DS lane.

Mechanically: `python .tools/to-check.py` (add flags as needed).

## The format

```
TO-CHECK  TIMESTAMP  |  N active TOs  |  N projects  |  scope: ...

Project: CODE  (N ACTIVE, N PENDING, N BLOCKED, N UNKNOWN)
  #N  [STATUS]  TO_ID  (AGE)
       Title:  title (truncated to 64 chars)
       To:     assignee serial
       By:     issuer serial
       Issued: YYYY-MM-DD
       Status: status text (truncated to 80 chars)
--------------------------------------------------------

TO-CHECK-RESULT total=N projects=N blocked=N parse_errors=N
```

- **AGE:** days since issued_date. `?` if no issued_date in the file.
- **STATUS labels:** `[ACTIVE]`, `[PENDING]`, `[BLOCKED !!]`, `[DONE]` (shouldn't appear -- filtered), `[??]` (unrecognized status).
- `[??] UNKNOWN` TOs are older files without a parseable status tag -- surfaced, not dropped.
- Projects sorted alphabetically; TOs sorted by issued_date descending within project.

## Status classification (same as /prd-check)

| Label | First word of `<status>` tag |
|---|---|
| ACTIVE | active, dispatched, in_progress, staged, go, partial (default for unrecognized) |
| PENDING | pending, hold, queued, waiting |
| BLOCKED !! | blocked |
| DONE | complete, closed, cancelled, done, merged, archived, shipped, superseded (filtered out) |
| ?? | no status tag / empty |

## Data source and schema variants

TO files live in `org/**/task_orders/*.md` (1,319 files across all agent dirs).
Two XML schemas are supported:

**New schema (canonical):**
- `<to_id>`, `<assigned_to>`, `<issued_date>`, `<title>`, `<project>`, `<issued_by>`, `<status>`

**Old schema (fallback):**
- `<id>`, `<issued_to>`, `<date>`, `<project_code>` (same fields, different tag names)

**Markdown format (oldest):**
- `**Owner:** \`serial\``, `**From:** \`issuer\``, `**Status:** VALUE`
- Title from first H1 header

Project code resolution order: `<to_id>` prefix > `<project>` / `<project_code>` > filename prefix.

## Robustness

- Never drops a TO file -- parse errors surface with `PARSE-ERROR:` label.
- ASCII-only output (Windows console safe, grep/awk safe, no emoji).
- Encoding issues (cp1252/utf-8 mismatch in older files) handled with `errors='replace'`.

## Relationship to /prd-check

```
/prd-check     Which hot projects have TOs filed vs. not?
               (project-level coverage summary)

/to-check      What are those TOs and who owns them?
               (TO-level detail drill-down)
```

Use `/prd-check` first to identify the hot projects; use `/to-check` to see their
TO workload. Use `/to-check --all` for a workspace-wide active-TO audit.

## Notes

- Read-only. Never dispatches.
- "none filed" TOs (projects showing up in /prd-check NO-ACTIVE-TOs) won't appear
  here at all -- they have no TO files to enumerate.
- Engine: `.tools/to-check.py` (tune thresholds and status words there).
