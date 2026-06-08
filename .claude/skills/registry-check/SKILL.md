---
name: registry-check
description: Clean, human-readable What/Where/Why view of the active (not-closed) project registry. `/registry-check` shows HOT projects only (worked <72h); `/registry-check -all` shows HOT + COLD (cold = >72h since work, still not closed). Each project renders as a numbered title row (code / status / last ascribed-commit timestamp / owner) with the long phase/description blocks PARSED OUT into three one-line fields -- What (what the project is), Where (where it is at now), Why (why we are/were doing it) -- ordered by most recent ascribed commit. Schema-tolerant (handles both the rich name/description/phase JSONs and the thin status/current_phase ones) and SURFACES malformed JSONs instead of silently dropping them. Read-only; pure filesystem + git, no MCP, no writes. Sister to /fabric-check (which is the agent-axis + raw project-axis lens); /registry-check is the cleaned-up, reading-optimized project view. Engine: `.tools/registry-check.py`.
---

# /registry-check -- clean project-registry view (What / Where / Why)

The reading-optimized companion to `/fabric-check`'s project axis. Where
`fabric-projects.py` dumps the raw 2-sentence phase blob per project,
`/registry-check` **parses the long blocks out of the title rows** and presents
each project as a numbered header plus three tight one-line fields.

## Invocation

| Form | Shows |
|---|---|
| `/registry-check` | **HOT only** -- projects worked in the last 72h, not closed |
| `/registry-check -all` | **HOT + COLD** -- adds the >72h-stale-but-still-open projects |
| `/registry-check --json` | machine-readable rows (respects `-all`) |

Mechanically: `python .tools/registry-check.py` (add `-all` / `--json`).

## The format

Vertical field-per-line record (Andrew-direct 2026-06-08 — every field on its
own labeled line; What/Where/Why never run together; ASCII-only separators):

```
#: N
Project: PROJECT_CODE
Status: status
Last commit: HH:MM (Xh) - OWNER        (today; older shows M/DD (X.Xd); OWNER = role token e.g. CTO/COO/AE)
What:  what the project IS              (one line)
Where: where it is at right now         (one line)
Why:   why we are / were doing it       (one line)
--------------------------------------------------------   (ASCII separator between records)
```

- **Ordering:** by most recent **ascribed commit** (a commit whose message
  references the project code), newest first. HOT then COLD, continuously
  numbered.
- **What** <- JSON `name` -> REGISTRY name column -> project code.
- **Where** <- JSON `phase` | `current_phase` -> REGISTRY narrative -> latest
  commit subject. (First sentence, truncated to one line.)
- **Why** <- JSON `description` rationale -> REGISTRY narrative. (The
  motivation / who-asked-for-it, e.g. "Andrew-direct ...".)

## Definitions (shared with /fabric-check)

- **Not closed** = JSON `status` not in
  {complete, completed, closed, cancelled, merged, superseded, done}.
  (Tolerant of the `completed` vs canonical `complete` drift -- both count as closed.)
- **HOT / COLD cut** = 72h on the most-recent ascribed-commit age.
- **Last activity** here is commit-based (the ascribed commit). `fabric-projects.py`
  uses max(JSON mtime, commit); the two can differ by a touch -- this view favors
  the commit because that is what "ascribed commit timestamp" means to a reader.

## Two robustness properties (both earned from real incidents)

1. **Malformed JSONs are SURFACED, never silently dropped.** A project JSON that
   fails to parse shows up under a `MALFORMED JSON` section with the parse error,
   instead of vanishing or masquerading as `unknown`/cold. (2026-06-08:
   `ADVI_INFLV2` + `ADVI_ORIAPI` were both completed projects hidden for weeks by
   a stray `",` and unescaped inner quotes -- a silent-drop tool would never have
   shown them.)
2. **ASCII-folded output.** Em-dashes / ellipses / smart-quotes in the source
   text are folded to ASCII so the Windows console charmap codec never mangles a
   line to `?`/U+FFFD or truncates it (CLAUDE.md Code Quality).

## Notes

- **Read-only.** Never writes, never dispatches. A lens, like `/fabric-check`.
- **Schema-tolerant.** Handles the rich JSON schema (`name`/`description`/`phase`)
  AND the thin one (`status`/`current_phase`/`macro`). Thin JSONs produce thinner
  Why/What lines (they lack a `name`/`description`) -- that is a data-hygiene
  signal worth fixing at the source, not a bug here.
- **When to use which:** `/fabric-check` answers "who is working and what is
  stuck" (agent axis + raw project axis, for COO `/drive`). `/registry-check`
  answers "what is on the board and where does each thing stand" (clean project
  reading view, for a human scanning the portfolio). Any agent, any time.
- Engine + thresholds: `.tools/registry-check.py` (tune in one place).
