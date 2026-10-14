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
| **One walk, one password, one lease** | `arm` first takes a lease (one conditional DynamoDB write of `armedBy` = `<hostname>:<pid>:<8 hex>` and `armedAt`; a live lease under 60 minutes prints `HELD by <armedBy> since <armedAt>` and mints nothing), then mints a random password into SSM `/opal/ui-walker/password`, sets the row active and prints `HOLDER <id>`. `disarm <holder>` runs only for that holder (a non-holder is refused and nothing changes); it sets it disabled, replaces the hash, and proves a login is refused; it never deletes the parameter (the Dells hold GetParameter only, and a delete is unrecoverable). The walker arms and disarms ITSELF, and the disarm runs in a `finally` block. |
| **Nobody sees the password** | Nothing prints it. The walker reads it in-process through `ui_walker_account.py secret`, which refuses unless the walker spawned it. **Never run `secret` by hand.** |
| **Read-only by construction** | A browser-side network guard admits only GET/HEAD/OPTIONS and the POSTs `/auth/login`, `/auth/refresh`, `/auth/logout`, `.../directory/resolve` and `.../selections`. Every other request is aborted and logged (`guard.tsv`), and the portal's telemetry is answered locally (never sent). Buttons matching export, generate, submit, upload, delete, save, send, approve, reset, sign-out and contact-support are never clicked. |
| **Protected channel** | `--base` must be `http://localhost:<port>`: the local `bun run dev:live` build, which reaches the live data and auth front door through CloudFront. |
| **Client data stays local** | Output goes to `tmp/ui-walk/<stamp>/` (gitignored at `.gitignore:89`). Never commit a walk's screenshots, never paste them into a message, and never send them off Opal infrastructure. A brief quotes findings in words. |

**If a walk dies mid-run** (the terminal closed, the machine slept), run
`python .claude/skills/ui-walk/ui_walker_account.py status` and, if it reads `status=active`, `disarm <armedBy from status>` at once. `status`
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
/ui-walk --route /portfolios --hover '<css>' -> first hover the first 3 matches: a viewport shot + the checks each
/ui-walk --deep --client "..."             -> also press every enabled button on each tab once (period presets, variant
                                              cards, map chips, sort headers, toggles); never a DO_NOT_CLICK word
/ui-walk --periods-per-account --client ".." -> on the Performance tab, select EACH picker account (first 8) and press
                                              YTD / QTD / 1Y / 3Y / Since inception once each, checks after every press
/ui-walk --firm "Inflection" --client "..."  -> on /investor-reporting, press the header Firm option whose visible label is that text (FIRM_OPTION_ABSENT lists the labels shown), then search that client
/ui-walk --firm "Inflection" --first-client  -> the same Firm pick, then walk the FIRST client the empty search lists (its name is kept out of the terminal)
```

`--periods-per-account` exists because a period figure is otherwise read only for whichever account the select loop
left selected; it presses presets by exact label, so a preset the page does not show is not pressed, and no new write
is reachable. Use it for a per-account AFTER read after a provider or adapter switch.

`--deep` presses one button per round, re-reading the tab each time, and presses Escape after each press, so a
dialog never blocks the next tab. File pickers are `<input type=file>` and are never pressed. A deep walk takes
about 12-15 minutes per client.

The lead-panel walk steps the Friday faces (Trending only): 'Chatter' (reads the month bubbles, presses 'Earlier month', step `lead-Trending-Chatter-cursor`) and 'Price' (reads each `[data-price-bar]` into `lead-lists.json`).

`--thread "<company name>"` (with `--route /security-analysis`) picks that company out of the Trending x Price bars BY THE NAME its price-bar row prints (never by ticker) and walks five steps `thread-1-list` .. `thread-5-recommendation-window` (a name no row prints records `thread:name-not-found`); the Price bars are written to `lead-lists.json` beside `findings.json`; each `--security` also presses its newest timeline day (`<sec>-timeline-day`) and opens the first event span (`<sec>-timeline-event`), else records `timeline:no-event-element`.

`--day "<security>=<YYYY-MM-DD>"` (repeatable, with `--security <name>`) presses that name's timeline bar `[data-day-bar="<date>"]` (else records `timeline:day-not-found`), runs the checks step `<sec>-timeline-day-<date>`, and writes each day's article rows in the order the page lists them to `timeline-days.json` beside `findings.json`.

Every opened timeline day (the `--day` step, the newest day and the first event) waits for the day's STATE, not for time: `waitForDayState(page, date)` polls the opened day's container `[data-timeline-selected-day="<date>"]` for article rows (`state: "rows"`), the designed empty day (`"empty"`) or the failed dissection (`"failed"`), every 250 ms, and shoots at the first state seen; if none appears within `DAY_STATE_CEILING_MS` (20,000 ms; the deployed `/timeline/day` answers in about 5.5 s for a day with articles) the result is `"ceiling"`, recorded as its own result and never graded as rows. `timeline-days.json` is written whenever any day was opened, one record per opened day with `via` (`day`, `newest` or `event`), `security`, `date`, `pressed`, `state` and `waited_ms`; the `--day` records also carry `article_rows_in_page_order`, read only when `state` is `rows`.

`--model-scope` (with `--client`) runs one step on the Holdings tab: it opens the card's buttons one at a time (a breakdown opener first) until a model pick control `[data-slot="breakdown-row-scope"]` appears, presses it, and writes `model-scope.json` beside `findings.json` with the scope line, the map chips, the Sleeve select and the table's SECURITY row count before and after (the class-totals block's rows are not counted). No pick offered records `model-scope:no-pick-offered`. A pick is page state only.

`--account-drill` (with `--client`) runs one step on the Holdings tab's default view, BEFORE the generic drill: it waits
until the tab's background one-account reads are done (no holdings read out for 2.5 s, up to 60,000 ms), presses the
card's first tile, and polls every 40 ms until the one-account view shows ("Back to all accounts", no "Opening" line). It
writes `account-drill.json`: the background reads (count and ms each), the wait, and for the drill the ms to the account
view, whether the tab body ever left the page (recorded as `account-drill:page-reload`), whether "Opening" showed, and the
reads after the press. Counts and times only. It returns to every account afterwards.

`--composer-picker` (with `--client`) runs one step on the Analysis tab's default view: the Client portfolio card, then the
Multi-Comp card (the picker must open at once, Done closed at 0 picks; the first two Opal models; Done), the Comparison
card ('spy', the first ETF; Done) and Overview. It writes `composer-picker.json`: the served catalogue read (status, ms,
entries by kind), the input boxes outside the picker at rest and at the end (`composer:loose-input`), whether the card
opened the picker (`composer:no-picker`), and the names and variant line the composer prints. Page state only; Generate
is never pressed.

`--dashboard-window` (with `--client`) runs one step on the Performance tab. Its clock starts at the tab's own press (the
account picker has no "All accounts" entry, so the tab opens on an account). It times the default account from the press,
every other account from its select (first 8), and the default one again last (warm). Per account it records the
dashboard's `manifest` and `series` reads (status, ms, the series' transfer bytes), the ms to the painted chart (a drawn
area in `dashboard-performance-chart`, up to 60,000 ms) or to the tab's own body, the "Data through" words and the chart's
day count. On a painted dashboard it presses each window preset once and counts every `/api/` request in the next 1.5 s,
which must be 0; any request is recorded as `dashboard:window-request`. Writes `dashboard-window.json`. Counts, times and
sizes only, never a figure.

`--press "<label>"` (repeatable, with `--route` on a plain route) presses the tab, radio or button with that exact label
after the load, waits `PRESS_SETTLE_MS` (12,000 ms), then shoots and checks the step `<route>-press-<label>`. A label
carrying a DO_NOT_CLICK word is refused and recorded as `walker:press-refused`. Use it to reach a chart behind a tab.

`--hover-after-press "<css>@<xfrac>"` (repeatable, plain routes) runs AFTER every `--press`. It moves the mouse onto the
first match of `<css>` at x = `xfrac` (0 to 1) of its width, at mid-height, waits 600 ms, then writes
`shots/hover-after-press-<k>-viewport.png` and checks the step `<route>-hover-after-press-<k>`. A selector with no match
or no visible box is recorded as `hover:no-match`. Use it for a hover-only popup behind page state that no URL carries,
for example a chart tooltip on a toggled view:
`--press "Trend" --hover-after-press ".recharts-wrapper@0.3"`. `--hover` runs before the presses and cannot reach these.

`--security-press "<css>"` (repeatable, on `/security-analysis` with `--security`) presses the first visible match for that selector
after the name's overlay shot, waits 2.5 s and the load state, then shoots and checks the step `<security>-press-<k>`. A text carrying
a DO_NOT_CLICK word is refused (`walker:press-refused`); no visible match is `walker:press-not-found`. GETs only: the guard is unchanged.

`--window-press "<css>"` (repeatable, same route) opens the Investment-thesis card on the Thesis tab, shoots `<security>-Thesis-window`,
presses the first visible match inside the dialog (same refused and not-found rules), waits 1.5 s, reads the focused element
(`document.activeElement`: tag, id, `data-thesis-passage`) and whether its top is in the viewport, shoots
`<security>-Thesis-window-press-<k>`, then presses Escape. One record per press is written to `window-press.json`.

`--open-request <REQ-id>` (with `--client`) opens ONE listed analysis request on the Analysis tab, by `data-request-id`, else the first row whose state reads Ready, and writes `analysis-request.json` with what the dialog shows (status words, section blocks, the correction sentence) and the wait in ms, up to `REQUEST_DETAIL_CEILING_MS` (90,000). Opening a request issues GETs only. The record counts the dialog by the page's own markers -- `section_cards` (`[data-row="native-section"]`) and `section_value_rows` -- beside `coverage_gap_items` (the `<li>` rows of the extraction-coverage panel behind Technical details); the older `section_items` counts that gap list plus its panel and never a card. It also carries `marks` (ms from the press to the dialog, to the status words, to the sections block) and `hops`: each analysis or status request the page made after the press, with `sent_ms`, `answered_ms`, `took_ms`, `queued_ms` (waiting for a connection) and `server_ms` (to the first byte) from the browser's own timing, the HTTP status, on a status read whether `X-IRPT-Status-Dates` was sent (beside an Authorization control) and, for the sections answer, the served `sections` and `undated_sections` counts. The hops run from the Analysis tab's own click (`press_ms` places the press), so the list read and the per-row status reads are in them; `row_states_at_press` and `hops_sent_by_kind` say what the list showed and what was still unanswered. `position_in_list` is the asked request's 1-based place in the list as the page draws it (null when it is not listed). Counts and times only.

`--probe-get <path>` (repeatable) takes a same-origin `/api/` path, e.g. `/api/scoped/.../leaf.json?firm=bd`. After sign-in, it GETs that path from inside the page with the headers the page itself sent on its last scoped read (held in-process; only their NAMES are written), and once without them as the control. It writes `probe-get.json`: the status, byte count, header names, the control's status, and, for a non-2xx answer only, its first 200 characters. A 2xx body is never kept. It issues GETs only, so the guard is unchanged. With no `--route`, the run walks no route. Use the page's own form of the path: an Opal user's scoped advisor reads need `?firm=<bucket suffix>`, and without it the route answers 400.

`--contrast-table` (plain routes) grades every visible interactive control's (ground, ink) pair against WCAG 2.1 SC
1.4.3, after each `--press` (or once after the load):
- states: at rest, on hover, and as selected where the control says so (aria-pressed / aria-selected / aria-current);
- the pair is the text the control actually shows: every text-holding element inside it, its ink composited over its
  own ground by the ink's alpha, and the control reports its weakest text;
- colours are read through a 1x1 canvas, so `oklab`, `color-mix` and any other syntax grade like `rgb`;
- the bar is 4.5:1, or 3:1 for large text.
It writes `contrast-table.json` (control labels are page copy). DSGN_REBRND round 3 E4 (FWD-13).

`--map-tiles` (with `--client`) runs one step on the Holdings tab's default view, before the drill. It counts the Securities
map's drawn tile rects (`[data-slot="treemap-chart"]`, the small text-less ones included) against the distinct map-eligible
securities in the served snapshot that view shows. The snapshot is the holdings answer with the most of them; the tab's
background one-account reads are subsets. A security is map-eligible when it is a SECURITY or CASH node of any basis, with
a served `of_total` and a non-zero amount, counted once per `security_id`, else once per node id. That is the page's own
map rule. The step writes `map-tiles.json`: tiles, small tiles, the served count, `equal`, and whether a grouped-tile word
is on the page. Counts only.

`--holdings-aggregates` reads every holdings answer the walk receives and writes `holdings-aggregates.json`: per selection, how many served `security_aggregates` items equal the sum of their ACTUAL member nodes (basis OBSERVED or ASSIGNED), how many equal the page's own fold (every security node of that id, a model's TARGET nodes included), how many page identities have no served aggregate, and whether `class_totals` plus the remainder equals the custody total. Counts only: no client name and no figure is written.

`--expect-text "<words>"` (repeatable, with `--open-request`) counts, case-sensitively, how often the opened dialog carries each string: `in_dialog` over the whole dialog and `inside_closed_details` for the part of it that sits in a closed `<details>`. `--reload-reopen` (with `--open-request`) then reloads the page and opens the SAME request again: the record's `reload` says whether the client selection survived, and a second record (label `...-after-reload`) carries the same counts and hops for the re-open. Both issue GETs only.

`--card-census` (with `--open-request`) adds `card_census` to the opened request's record: cards whose title reads a name or an `S<nn>` code, the Unit words with counts, cards grouped by title and Label (`largest_group`), and whether the validation and "Source" lines stand on the face or inside a closed `<details>`. The sections hop gains `served_shape`: the answer's `data` keys, a section's keys, `section_type` and `units` tokens with counts, and the validation object's keys. Key names and category tokens only, never a value.

`--performance-state` (with `--client`) waits on the Performance tab for the tab's STATE rather than for time: a worded refusal (`[data-slot="reporting-refusal-words"]`, state `refusal`), an answer (`[data-slot="reporting-body"]`, state `body`), or neither within `PERFORMANCE_STATE_CEILING_MS` (45,000 ms; state `ceiling`, its own result). It shoots the state as step `<client>-performance-answered` and writes `performance-state.json` with the state, the wait in ms, the refusal's own sentence and whether the code disclosure stands open. No client figure is written. It issues no request of its own.

Every `--client` search also records when the typed search ANSWERS (the box stops reading "Loading"), up to `SEARCH_ANSWER_CEILING_MS` (30,000 ms), in `search-timings.json`; the 2.5 s screenshot stays what a person sees first, and a slower answer gets its own `search-<client>-answered` step.

The skill runs:

```
node .claude/skills/ui-walk/walk.mjs [--route R]... [--client "text"]... [--max-minutes 40] [--headed]
```

`--no-login` skips the account and sign-in (the signed-out control); any step that lands on the sign-in page prints `WALK VOID: step <label> landed on the sign-in page`, records `walker:signed-out` and exits 3.

Repeat `--client` for several clients. Use a client with several accounts: most defects live there. The whole
Investor Reporting walk takes about 5 minutes per client.

## Step 1 -- Walk

Run the walker and read its last lines: `SUMMARY`, `DISARM ... REFUSED`, `OUT`. **If DISARM does not print `REFUSED`,
stop and run `disarm <holder>` again. Escalate if it still fails.**

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

- `.claude/skills/ui-walk/ui_walker_account.py`: status | provision | arm | disarm <holder> (and `secret`, walker only).
- `.claude/skills/ui-walk/walk.mjs`: the walker.
- `docs/briefs/irpt-ui-review-coverage-check.py`: the register coverage check.
