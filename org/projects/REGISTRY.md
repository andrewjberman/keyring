# Project Registry

All active and completed projects. Each project has a code, a PRD, and a thread log.
Thread serials are `{CODE}-{NNN}` — they join threads to projects across all agent folders.

| Code | Project | Status | PRD | Threads |
|------|---------|--------|-----|---------|
| ADVI | AdvisorIntelligence | active | `docs/architecture/ADVISOR_INTELLIGENCE_COMPLETION.md` | ADVI-001, ADVI-002, ADVI-003 |

---

## Adding a new project

1. Create `org/projects/{CODE}.json` (copy ADVI.json as template)
2. Set `code`, `name`, `prd`, `status`, `pods`, `description`
3. Set `thread_counter` to 0, `threads` to []
4. Add a row to this table

## Thread serial format

`{CODE}-{NNN}` where NNN is zero-padded to 3 digits.
Thread folder: `org/threads/{CODE}-{NNN}-{slug}/`
Receipt in agent folder: `{CODE}-{NNN}-{slug}_{other_serials}.md`

When creating a thread for a project, pass `--project {CODE}` to `create-thread.sh`.
The script auto-assigns the next serial and updates this project file.
