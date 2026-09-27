---
name: ui-walk
description: "Walk a portal page like a person, signed in as the dormant Opal UI walker service account on the LOCAL dev build (localhost:5174, the protected dev channel), screenshot every step, and flag frontend defects (dropdowns behind nav bars, unnecessary drill layers, unconnected fields showing 'unavailable' / 'Not supplied', duplicate choices, design-law breaks), then turn the walk into a machine-readable frontend brief. Read-only by construction. Use for frontend development and brief-writing, not as acceptance evidence."
---

# /ui-walk -- sign in as the UI walker, walk the page, find what is wrong, write it down

**Andrew-direct 2026-09-26 ~22:0xZ, VERBATIM** (record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260926_220xZ_UI_WALKER_SERVICE_ACCOUNT.md`): *"we need a
service account setup that can walk these pages visually, I need you to just build it, and then create a skill that
logs in through a protected dev channel and walks these pages for development purpose, to see what is going on on the
frontend (test fixtures, dropdowns, pages, modals, expands, etc.), with the intent of developing briefs specific to
frontend dev. Should be looking for UI failures, dropdowns that appear behind nav bars, unnecessary drilldown layers,
unconnected endpoints (showing "unavailable" or "Not supplied" because there is no connection for a given field),
breaks from canonical design patterns, etc."*

## What it is, and what it is not

- **It is** a development instrument. It signs in with real login and real data, on the local build, and walks one or
  more routes: search, tabs, identity expands, dropdowns, account pickers, drill rows and `<details>`. It screenshots
  every step and runs in-page checks for the defect classes Andrew named.
- **It is NOT** acceptance evidence. A walk grades nothing, and a CVO still grades pinned candidates on its own
  evidence. It is NOT a PROD-site walk: the walker refuses any base URL that is not `localhost`.

## The safety model (read before the first run)

| Guard | How |
|---|---|
| **The account is dormant at rest** | `opal-users-v2` `USER#usr_opal_ui_walker` (`opal-ui-walker@opal.test`, role admin, internal, Dev) sits at `status disabled` with a password hash nobody knows, and no SSM parameter exists. |
| **One walk, one password** | `arm` mints a random password into SSM `/opal/ui-walker/password` and sets the row active. `disarm` sets it disabled, replaces the hash, deletes the parameter, and proves a login is refused. The walker arms and disarms ITSELF, and the disarm runs in a `finally` block. |
| **Nobody sees the password** | Nothing prints it. The walker reads it in-process through `ui_walker_account.py secret`, which refuses unless the walker spawned it. **Never run `secret` by hand.** |
| **Read-only by construction** | A browser-side network guard admits only GET/HEAD/OPTIONS and the POSTs `/auth/login`, `/auth/refresh`, `/auth/logout`, `.../directory/resolve` and `.../selections`. Every other request is aborted and logged (`guard.tsv`), and the portal's telemetry is answered locally (never sent). Buttons matching export, generate, submit, upload, delete, save, send, approve, reset, sign-out and contact-support are never clicked. |
| **Protected channel** | `--base` must be `http://localhost:<port>`: the local `bun run dev:live` build, which reaches the live data and auth front door through CloudFront. |
| **Client data stays local** | Output goes to `tmp/ui-walk/<stamp>/` (gitignored at `.gitignore:89`). Never commit a walk's screenshots, never paste them into a message, and never send them off Opal infrastructure. A brief quotes findings in words. |

**If a walk dies mid-run** (the terminal closed, the machine slept), run
`python .claude/skills/ui-walk/ui_walker_account.py status` and, if it reads `status=active`, `disarm` at once. `status`
warns when the account has been armed for more than 60 minutes.

## Prerequisites

1. The local dev build on port 5174 (portal law: dev builds use 5174 only). Check `curl -s -o /dev/null -w "%{http_code}"
   http://localhost:5174/`. If it is not up, start it in the background: `cd portal && bun run dev:live --port 5174`.
2. Microsoft Edge (Playwright's `msedge` channel) or Playwright's own Chromium. `playwright-core` is loaded from
   `portal/node_modules`.
3. AWS credentials that can write `opal-users-v2` and SSM (the laptop's profile), and Python with `bcrypt` and `boto3`.
4. The account is provisioned ONCE (already done 2026-09-26): `python .claude/skills/ui-walk/ui_walker_account.py
   provision`.

## Invocation

```
/ui-walk                                   -> /investor-reporting, empty search only
/ui-walk --client "anna thiessen"          -> plus that client's identity, every tab, drill and pickers
/ui-walk --route /model-portfolios         -> any other route (generic explore: details, selects, popups)
/ui-walk --deep --client "..."             -> also press every enabled button on each tab once (period presets, variant
                                              cards, map chips, sort headers, toggles); never a DO_NOT_CLICK word
```

`--deep` presses one button per round, re-reading the tab each time, and presses Escape after each press, so a
dialog never blocks the next tab. File pickers are `<input type=file>` and are never pressed. A deep walk takes
about 12-15 minutes per client.

The skill runs:

```
node .claude/skills/ui-walk/walk.mjs [--route R]... [--client "text"]... [--max-minutes 40] [--headed]
```

Repeat `--client` for several clients. Use a client with several accounts: most defects live there. The whole
Investor Reporting walk takes about 5 minutes per client.

## Step 1 -- Walk

Run the walker and read its last lines: `SUMMARY`, `DISARM ... REFUSED`, `OUT`. **If DISARM does not print `REFUSED`,
stop and run `disarm` again. Escalate if it still fails.**

## Step 2 -- LOOK at every screenshot (the checks are pointers, not the verdict)

Read each `tmp/ui-walk/<stamp>/shots/*.png` with the Read tool. The in-page checks find what DOM rules can see. A person
sees the rest:
- awkward or system wording;
- an unnecessary layer;
- two numbers that disagree;
- a percentage with no stated base;
- a chart that says nothing;
- colours that mean two things;
- anything that breaks `portal/DESIGN.md` (C1-C12) or the colour law in `portal/CLAUDE.md`.

For every check hit in `findings.json`, confirm it on the screenshot before it becomes a finding. A false positive is
dropped, with the reason noted.

What the checks flag (the `check` field):

| check | what it means |
|---|---|
| `occluded-popover` | An open listbox, menu or dialog is covered by another element at some of 9 sample points. `covered_by` names the element, e.g. a sticky tab strip: the "dropdown behind the nav bar" class. |
| `unconnected-field` | Visible "not supplied", "unavailable", "value pending", "Unknown", "withheld" or "n/a": a field with no connection behind it. |
| `raw-code` | A SYSTEM_CODE on the face (FWD-15). |
| `sample-content` | Illustrative sample content on a live page. |
| `duplicate-options` | A list offers two identical choices. |
| `drill:single-child-level`, `chart:single-slice` | A drill level with one child, or a one-slice pie: an unnecessary layer. |
| `chart:duplicate-colour`, `chart:unknown-label` | Two slices share a colour, or a slice is labelled "Unknown". |
| `design:bands`, `design:contrast`, `design:tinted-status` | More than one #0A1733 band (C3); text under 3:1 contrast; a tinted status block (C12). |
| `format:money`, `format:dates` | Two money formats or several date formats on one page. |
| `layout:truncated`, `layout:horizontal-scroll` | Ellipsized labels; a page that scrolls sideways. |
| `search:ranking`, `search:no-match` | The option matching every typed token is not first, or is absent. |
| `api_issues` (top level) | An API answer that is not READY or not ok, with its reason code. It pairs an "unavailable" on screen with the endpoint behind it. |
| `console_errors`, `guard_aborts` (top level) | Page errors; a write the page tried that the guard blocked (a button that would have changed data). |

## Step 3 -- Write the frontend brief (machine-readable first)

1. **Build a register** `docs/briefs/<topic>-findings-<YYYYMMDD>.json` in the shape of
   `docs/briefs/irpt-ui-review-findings-20260926.json` (schema_version 1.0). Each finding carries:
   - `id` (a stable prefix + number);
   - the screenshot (a local path, never committed);
   - `surface`, `observed`, `outcome`;
   - `owner_project` and `owner_seat`;
   - `status` (new or known, with `known_ref`);
   - `design_rule`;
   - `cause` with `claim: measured|inferred` and `evidence`;
   - a testable `acceptance` line.

   Every walk check hit you keep maps to one register finding.
2. **Write the brief** with `/brief-create --midstream <PROJECT>`. Generate its tables from the register so the two
   cannot drift.
3. **Coverage:** `python docs/briefs/irpt-ui-review-coverage-check.py --register <your register> <file that must cite
   every id>`. It exits 0 only when every id is cited. Run it on the brief, and later on the PRD addendum.
4. Send the brief to `1.0.0_SA_CTO`: one message, the path plus one line, under 150 words.

## Known limits

- **Native `<select>` popups are drawn by the OS.** They never appear in a screenshot and cannot be tested for
  occlusion. Their options are read from the DOM (duplicates are still caught).
- The occlusion check samples 9 points, so a popover clipped only at a corner can pass.
- The contrast check is a heuristic: it reads the nearest opaque ancestor background, not layered transparency.
- Anything behind a guarded write (export, upload, generate, submit) is out of reach by design.
- The walk follows the first drillable row per top-level row, down to 4 levels. It is a sample, not a census of every
  path.
- A walk reads the build that is running on 5174. Name its commit in the brief (`git -C portal rev-parse HEAD` is the
  working copy, not necessarily the running bundle).

## Files

- `.claude/skills/ui-walk/ui_walker_account.py`: status | provision | arm | disarm (and `secret`, walker only).
- `.claude/skills/ui-walk/walk.mjs`: the walker.
- `docs/briefs/irpt-ui-review-coverage-check.py`: the register coverage check.
