---
name: registry-check
description: Human-readable What/Where/Why view of the active project registry: `/registry-check` (HOT, worked <72h); `/registry-check -all` (HOT + COLD). One numbered row per project with the long phase text parsed into What / Where / Why, ordered by most recent ascribed commit; malformed JSONs surfaced, never dropped. Read-only, no MCP. Sister to /fabric-check. Engine `.tools/registry-check.py`.
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

## DEFAULT: every invocation ALSO renders + surfaces the dashboard (Andrew-direct 2026-07-07)

**The dashboard renderer is PART OF THE INVOCATION, not an optional companion.** Unless the
user explicitly says text-only (`--no-render` / "just the text"), running `/registry-check`
does BOTH, in order:
1. the text lens -- `python .tools/registry-check.py` (respecting `-all`);
2. the live dashboard -- `python .claude/skills/registry-check/render_dashboard.py` (pass through
   `-all` / `--days`), THEN **`SendUserFile` the resulting `Desktop/Opal_Project_Dashboard.html`
   with `display: render`** so the user sees it inline.

Exceptions (text-only, no render): `--json` (machine-readable), or the user says so.

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

## Branded SVG board (poster view)

For a visual, shareable rendering of the HOT portfolio (vs. the text lens), use the
companion renderer **`render_board_svg.py`** (lives in this skill dir). It emits a
single Opal-branded SVG poster -- navy header + KO-white interlock logo, cluster
sections, one card per project (status pill + a one-line WHAT + a one-line NOW +
owner/last-commit footer), brand palette + Lato pulled from
`deck_generation/brand_spec/brand.json` and the logo package.

```bash
python .claude/skills/registry-check/render_board_svg.py [OUTPUT.svg]   # default: ./opal_project_board.svg
```

**Snapshot, not live:** the per-project WHAT/NOW one-liners and the cluster grouping
are HAND-CURATED inside the script's `clusters` list (richer than `--json` carries).
To refresh: run `/registry-check` for the current status/owner/age, edit `clusters`,
re-run. The styling layer (palette/logo/Lato/card layout) is reusable as-is; only the
data list is the curated snapshot (last: 2026-06-25, 22 HOT projects). Born from
Andrew's 2026-06-25 ask to render the board "/draw style" as a branded SVG.

## Branded HTML dashboard (live card + activity-bar view)

The scannable **dashboard** the invocation renders by default (see "DEFAULT" above) --
one card per not-closed project, macro-colored, **sized by a real ACTIVITY BAR** (commits
referencing the project in the last N days), sorted busiest -> quietest, with status pills +
owner + last-touch. Renderer **`render_dashboard.py`** (this skill dir). Born from
Andrew's 2026-07-01 ask ("nice cards, easy to read, bars for how much activity...
a dashboard view of everything we've got going on"); made a default-of-invocation 2026-07-07.

```bash
python .claude/skills/registry-check/render_dashboard.py            # HOT, 7d window -> Desktop/Opal_Project_Dashboard.html
python .claude/skills/registry-check/render_dashboard.py --all      # include COLD (>72h)
python .claude/skills/registry-check/render_dashboard.py --days 14  # activity window
python .claude/skills/registry-check/render_dashboard.py --out PATH.html
```

**LIVE, not a snapshot (the key difference from the SVG board):** it LOADS the
canonical engine (`.tools/registry-check.py`) and reuses `build_rows()`, so
What/Where/status/owner/age stay in ONE place; the only thing it adds is the
**7-day git-activity count** (the one signal the text lens doesn't compute) and the
presentation. No hand-curated data list to keep fresh -- re-run and it's current.
Default output lands on the Desktop (`Opal_Project_Dashboard.html`); `SendUserFile
--display render` to surface it. The `expected_cadence`-style caveat is in the
footer: a low bar on a fresh PRD means "just chartered," not "stalled." The
`/to-check` skill has a parallel `render_to_dashboard.py` (TO-load-by-agent + by-project).

## Notes

- **Read-only.** Never writes, never dispatches. A lens, like `/fabric-check`.
  (The SVG renderer above WRITES one file -- the board image -- on explicit ask; the
  registry lens itself stays read-only.)
- **Schema-tolerant.** Handles the rich JSON schema (`name`/`description`/`phase`)
  AND the thin one (`status`/`current_phase`/`macro`). Thin JSONs produce thinner
  Why/What lines (they lack a `name`/`description`) -- that is a data-hygiene
  signal worth fixing at the source, not a bug here.
- **When to use which:** `/fabric-check` answers "who is working and what is
  stuck" (agent axis + raw project axis, for COO `/drive`). `/registry-check`
  answers "what is on the board and where does each thing stand" (clean project
  reading view, for a human scanning the portfolio). Any agent, any time.
- Engine + thresholds: `.tools/registry-check.py` (tune in one place).
