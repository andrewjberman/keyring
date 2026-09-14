---
name: daily-sprint
description: Rewrite Andrew's DAILY SPRINT text for the day as a highlight reel, not a change log: every line a win tied to a directive's headliner; never invent one; nothing shipped = one line. Grounded on a compiled packet (comp-state, both fabrics' git census, the directives dashboard, open-TO totals, the day's records). `/daily-sprint`; `--date YYYY-MM-DD`; `--packet` (packet only). Engine `.tools/daily-sprint.py`; MSTR-base primary, any exec may run it.
---

# /daily-sprint — the day's status text, rewritten against a grounded packet

**What it is for (Andrew, 2026-08-20):** *"run comp-state and generally do a scan over the repo and
directives, the work done both by the local fabric and the sitez fabric and rewrite the attached
pasted text... a skill that does that process of assessing progress on the day and rewrites these
things in text because we are going to be doing it every single day."*

The deliverable is PROSE in a FIXED SHAPE (`org/ref/DAILY_SPRINT_TEMPLATE.md`), one file per day at
`org/sprints/DAILY_SPRINT_YYYY-MM-DD.md`, rewritten from yesterday's. The packet is machine; the
sentences are yours; every sentence traces to a packet line, a commit, or a record you read today.

## Procedure

1. **Packet first:** `python .tools/daily-sprint.py` (today) — prints the grounding packet and
   scaffolds today's file from yesterday's if absent. **`comp-state` self-test must read PASS**
   in the packet header; if not, say so in the text's fabric line and lean on git + records.
2. **Read the packet's denominators** — commits/authors (both fabrics, all refs), directives
   live/retired with per-row freshness + flags, open-TO totals, the day's Andrew-direct records,
   projects closed, ledger entries. These are the numbers the text may quote.
3. **Read yesterday's file** (the packet names it). Today's text is a REWRITE of it, not an append:
   every Item line is re-stated against today's evidence. **"No movement today" is legitimate and
   is always better than invented progress** (a directive row whose `Last` is yesterday did not
   move) — **but it is the fallback, NOT the target. Look for the win first.** If the day held a
   fix, a build, a decision or a number that got better, **that is the line**; a quiet item gets
   one short sentence and the space goes to the items that moved.
4. **Rewrite today's file in the template's exact shape** — headings, `Item N – Name – text`
   grammar, terse register, Today-Sprint bullets highest-consequence first, Blocks = genuine
   external blocks or human-only acts (an inter-item dependency is Process, not a Block).
   **THE FIRST RULE IS LAYMAN + SHORT (Andrew-direct, verbatim in the template): very short
   lines a non-engineer reads once; no serials, hashes, AWS resource names, tool names, or
   process vocabulary; a component of an achievement appears only when the reader needs it, in
   plain words; ~25 words per bullet. The test: would Andrew paste the line to a partner
   unedited?** The packet is the GROUNDING, not the prose — translate it, never transcribe it.
5. **Cross-fabric:** site-Z landings come from ferried records at parity (cite the record/commit);
   the packet's `--all` git census already covers both branches.
6. **BUILD THE STRUCTURED JSON + RENDER — the visual deliverable (Andrew-direct 2026-08-27,
   supersedes the 08-26 `render_sprint.py` step; that renderer is retired):**
   a. `python daily_reports/scripts/commit_census.py --date <DAY> --window et --json` — the
      by-author-seat cut (the `commit_kind` enum, a declared PROXY for kind of work; Rule-24
      record in `daily_reports/README.md`) **and** `python daily_reports/scripts/project_census.py
      --date <DAY> --window et --json` — the by-directive cut from the FILES each commit touched,
      with its residual NAMED as `unattributed` (never parked on a row). Both emit a `timeline`
      (00:00 Eastern → now, 30-min bins) for the page's stacked area charts; merge both into
      `team_activity` verbatim — the renderer asserts every series sums to its count. `--window
      et` is the page's population (Andrew's day); the TEXT volume line keeps its UTC rule.
   b. Write `daily_reports/data/DAILY_REPORT_<DAY>.json` against
      `daily_reports/schema/DAILY_REPORT.schema.json`. **`display_date` is DERIVED from `date` by the
      renderer (`Saturday, August 29, 2026` form) and a typed value that disagrees FAILS the render** -- Andrew-direct
      2026-08-30: "however dates are put together for the sprint render ... accurate to calendar"; 3 of 3 reports
      had carried the wrong weekday, each one day early, from a hand-typed field beside the ISO date. **The JSON maps 1:1 to the visual —
      author to the shape checklist below.**

   b-i. ⛔ **EVERY DIRECTIVE IN THE REGISTER GETS A ROW IN *BOTH* `projects[]` AND `process[]`,
      WORKED OR NOT — EXACTLY ONCE IN EACH.**
      Andrew-direct 2026-09-11 ~21:5xZ, VERBATIM: *"i notice that \"Process\" seems to be kind of
      random and haphazard with what is displayed. It should list every single directive."*
      ⚠ **`process[]` WAS THE HALF NOBODY ENFORCED.** The PROCESS/BLOCKED bullet below has always
      said "the same 1:1 register mapping", but `check_directive_coverage()` read `projects[]` and
      nothing else, so the section drifted to whatever subset the author happened to pick and it
      LOOKED arbitrary because it WAS. Measured 2026-09-11: `projects[]` carried 14 of 14 while
      `process[]` carried 5, and the report rendered clean. A rule stated in prose and checked
      nowhere is a convention, and conventions decay silently.
      A quiet `process` row carries `state: "idle"` and a short no-work note (the `projects`
      equivalent is `quiet: true`); `state` is one of `ok|act|hold|idle` and nothing else.
      **The check now covers BOTH sections and also refuses a DUPLICATE row** — two cards for one
      directive passes a set-based check while the section still misreads its own denominator.
      Andrew-direct 2026-09-10 ~21:2xZ, VERBATIM: *"we need to display \*ALL\* Directives cards on
      'Projects' segment, regardless if work was done or not. This is important to see what did not
      get work done (greyed out with short 'no work on this today'-style bullet\" because it shows
      priority."*
      ⭐ **THE ABSENCE IS THE SIGNAL.** A directive with no commits says what did NOT get attention,
      and a list of only what moved cannot express it — omission and "nothing happened" render
      identically when the row is simply not there.
      **`n` IS THE DIRECTIVE NUMBER AND `name` IS ITS CANONICAL TITLE FROM
      `org/missions/DIRECTIVES.yaml`** — never a sequential index, never a name you invented.
      A quiet directive carries `"quiet": true` (the templates already style it dashed and greyed,
      `.card.quiet`, both variants) plus a SHORT no-work line; say WHY it was quiet when the
      register knows. Build the set BY SUBTRACTION from the register, never by listing what moved.
      ⚠ **MECHANISM, not convention:** `render_daily_report.check_directive_coverage()` REFUSES a
      report missing any register directive, and refuses an `n` that is not a directive number. It
      is FAIL-CLOSED — if it cannot read the register it errors rather than skipping. A scheduled
      run that has no repo sets `OPAL_DIRECTIVES_YAML` to the copy its packet carries.
      *Measured 2026-09-10: `projects[]` was authored with a sequential index 0..6 and seven
      invented names, none of which exists in any register, and it rendered fine.*

   b-ii. ⛔ **DO NOT AUTHOR A `viz` FROM YESTERDAY'S JSON. READ THE CONTRACT.**
      Andrew-direct 2026-09-10 ~21:2xZ, VERBATIM: *"make sure that whatever it is that causes
      'undefined' tags in the diagrams, that there is a stable solution provided to that end
      because it happens almost every single day."*
      **THE DIAGRAMS ARE BUILT BY JAVASCRIPT IN THE BROWSER** from `templates/_shared_viz.js` at
      VIEW time, which is why a JSON that renders cleanly can still paint the word `undefined` on
      the served page. Print the contract before authoring:
      ```
      python daily_reports/scripts/viz_contract.py            # every generator's real params
      python daily_reports/scripts/viz_contract.py --self-test
      ```
      It DERIVES each generator's required params, row keys and nested keys from the JS source, so
      it cannot drift the way the hand-maintained table did. `render_daily_report.py` consumes it
      and refuses, fail-closed.
      ⛔ **A WRONG ROW SHAPE IS NOT ALWAYS LOUD.** `compare` rows must be OBJECTS
      (`{label, before, after}`) — it is a before-to-after BAR CHART, so **an item with no genuine
      historical pair needs a different diagram, not an invented `before` number.** `steps` rows
      need `state` in `{done, now, next}`; a wrong value renders every node grey and prints a FALSE
      "0 of N done", which reads as a measurement and is worse than `undefined`.
      *Measured 2026-09-10: FIVE of seven diagrams were malformed. Andrew saw the two that printed
      the word; the other three failed silently.*
   c. `python daily_reports/scripts/render_daily_report.py --date <DAY>` — validates and writes
      **BOTH** `daily_reports/out/Desktop_DAILY_REPORT_<DAY>.html` and
      `daily_reports/out/Mobile_DAILY_REPORT_<DAY>.html` (Andrew-direct 2026-08-28: every render
      produces both, and the FIRST word of the filename names the variant because Teams truncates
      attachment names). Same JSON, one shared grammar (`templates/_shared_viz.js`). **A
      validation failure is a content defect: fix the JSON, never the template.** Surface both
      pages (open them); the mobile one is what he reads on a phone.
   d. **PHOTOS OF LIVE FEATURES (Andrew-direct 2026-08-28 ~21:5xZ, verbatim: *"if there's a live feature
      on the frontend, we take a photo of it and superimpose that"*):** every `live` item whose subject is
      a portal page gets `viz.type: screens`. `python daily_reports/scripts/capture_screens.py --date
      <DAY> --route <route> --name <name> [--frame phone]` captures it through the portal's own headless
      renderer into `daily_reports/shots/<DAY>/`; READ the PNG (the LOC line must be the route you
      asked for), reference it as `shots/<DAY>/<name>.png` in the JSON, commit the shot with the JSON.
      **Pick from the diagram catalog** (`daily_reports/README.md`): screens / flow / coverage / tree /
      link / compare / steps / matrix -- the shape that tells the item's REAL story; repeating `link`
      and `tree` across a page is the defect the catalog exists to end.
7. **PUBLISH to the web client (Andrew-direct 2026-08-28):** `python daily_reports/scripts/
   publish_daily_report.py --date <DAY>` — puts BOTH pages at `s3://opal-data-portal-v2/
   daily-reports/<DAY>/` and reads each back (size + ETag MATCH x2 is the proof; the put's rc is
   not). They are then live at **https://mcp.opalinvest.dev/sprint** (latest) and `/sprint/<DAY>`
   behind Entra sign-in — the viewer picks Desktop/Mobile per device. The Teams link is that
   URL; nothing else is posted. **UNTIL LDT fixes the App-1 redirect URI (IT_REQUEST.md Incident
   #3), add `--presign`** (Andrew-direct 2026-08-28, "option 1 works here. go"): it also writes
   `daily-reports/latest/` + a chooser page and prints a 7-day no-login presigned link — the
   TEAMS LINK line is what goes in the post; it keeps serving each day's overwrite until it
   expires. Then **commit** the day's file + JSON + rendered html under your author line
   (`safe-commit`).

## The visual shape (Andrew-direct 2026-08-27 — rigidly templated; the runner looks FOR these)

Template `daily_reports/templates/daily_report_template.html` is the ONE design (CTO surface;
frozen). A /daily-sprint run AUTHORS, it never styles. What the runner is looking for:

- **HEADLINE — a STANDALONE feature, not a sprint item:** what kind of day it was, carried by
  the biggest win or an amalgamation (`headline.kind`: biggest_win | amalgamation | day_summary).
  Never wraps.
- **SPRINT ITEMS (3–8), IN FIXED CATEGORY ORDER: live → build → fix → verify → scope**
  (Andrew-direct 2026-08-27 ~23:4xZ, verbatim: *"always lead with built, then serving, then
  fixed, then verified, then scoped"* -- AMENDED 2026-08-28 ~21:5xZ, verbatim: *"change \"Serving\" to \"Live\" and thats what leads in sprint order and in legend order"*; the renderer rejects an out-of-order JSON; highest
  consequence first within a category; `hero` marks the biggest item where it falls). Each
  carries a category (live/build/fix/verify/scope), a **card headline that fits whole — max 52
  chars, no ellipsis ever (hard law, renderer rejects)**, a stage title, **WHO / WHAT / WHERE /
  WHY** (one short line each; touchpoints a reader knows — firms, platforms, dashboard pages,
  **B2B only, never an individual investor**), a **viz type** (flow / coverage / tree / screens /
  link / orbit — **the shape that tells the item's REAL story, filled with measured facts**: a
  fix = flow with the break where it actually was, a who-sees-what build = tree, a connection =
  link, a completion = coverage over its true denominator; a generic shape with placeholder
  nodes is a content defect; params in JSON), and exactly **3 stat chips**.
- **TEAM ACTIVITY:** the stable every-day element — a layman verdict line on the day's shape,
  plus two cuts of ONE commit population (by kind of work, by project; both must sum to
  `commits` — the renderer asserts it). Colors are stable: project N is always the same color.
- **PROJECTS:** one card per DIRECTIVES.yaml row, name = the register `title:` verbatim, short
  subtext against the headliner; `quiet: true` for no-movement rows.
- **PROCESS:** the same 1:1 register mapping as PROJECTS — **every directive, exactly once, worked
  or not** (b-i; enforced by `check_directive_coverage()`, fail-closed). A no-movement row is
  `state: "idle"` with a one-line note, never an omission.
  **BLOCKED:** genuine external blocks or human-only acts only — never the register mapping, and
  an inter-item dependency is Process, not a Block.
- All prose fields obey the FIRST–FOURTH RULES (layman, highlight reel, Andrew's voice, volume).

**SUPERSEDED 2026-08-26 ~23:0xZ — THE DELIVERABLE IS AN IMAGE, NOT TEXT.** Every Teams-text
formatting workaround (`&nbsp;` gap-holders, `---` rules, spacer bullets carrying a non-breaking
space, the no-heading rule, the PROCESS table) is RETIRED: presentation moved out of prose and into
`render_sprint.py`, where a reader cannot tidy it away by accident. The clause below is preserved
for the division-of-labour half, which still binds — the visual dashboard is `/directives-check`,
this skill produces the day's report:

**(prior text-only clause, Andrew-direct ~2105Z, VERBATIM):** *"there are two skills involved here.
/directives-check which is for me internally and shows the current state of directives + creates a
render for visible analysis. Then there should also be /daily-sprint which essentially is just a
formatted text version i can copy/paste of directives-check for the Opal teams channel."* The
visual render lives in `/directives-check`; this skill produces the copy/paste text and nothing
else.

## Forms

| Form | Behavior |
|---|---|
| `/daily-sprint` | packet + scaffold/rewrite today's file + print |
| `/daily-sprint --date YYYY-MM-DD` | same for a named day |
| `/daily-sprint --packet` | `daily-sprint.py --packet-only` — grounding only, no file |

## Discipline

- **WRITTEN IN ANDREW'S VOICE (Andrew-direct 2026-08-26 ~21:2xZ, VERBATIM):** *"These have to be
  written in my voice, do not refer to me as im the one who is allegedly saying these things."*
  He pastes the text as HIS OWN channel message — **never write "Andrew ruled/approved/set…"**;
  decisions render as bare outcomes ("Ruled: …", "Approved: …", "Target moved to today") or first
  person where ownership is the point, and a "For Andrew" block renders "**Pending my call:** …".
  The test: read every line as if you are Andrew posting it. Full form + before/after table: the
  template's **THIRD RULE**.
- **HIGHLIGHTS, AND MAKE IT SOUND GOOD (Andrew-direct 2026-08-26).** *"if we fix a bug that sounds
  good, if we build something that sounds good, we do not want pedantic stuff, and we want to tie
  it back to directives.yaml headliner items for the most part."*
  **DO NOT NARRATE THE BUG — DO CLAIM THE FIX.** A repair is delivery and reads as a win; the
  mechanism that produced it does not appear. Confident, plain, active register.
  ⛔ **Register only, never content: NEVER invent a win.** Nothing shipped on an item = say so in
  one line. The rule bites the other way — **when there IS a win, do not bury it in hedging or in
  the machinery behind it.**
  **NO PEDANTRY:** internal counts, sequencing, lane attribution, caveats a partner would not act
  on. Precision lives in the logs and certs; this text is the highlight reel.
  Full rule + worked before/after table: the template's **SECOND RULE, AMENDED**.
- **THE VOLUME LINE CLOSES `TODAY SPRINT` (Andrew-direct 2026-08-26 ~21:5xZ):** *"how many commits
  over how many agents today? i think that should be the final line of the 'Sprint' section."*
  **Always last, always present, bare and flat:** `• N commits across M agents today.`
  `git log --all --since='<DAY>T00:00:00Z'` — **`--all` is load-bearing (both fabrics, every ref)**;
  commits = `| wc -l`, agents = `--pretty='%an' | sort -u | wc -l`.
  ⛔ **NARROWS the 08-25 cut, does not reverse it** — ONE line, LAST, in TODAY SPRINT only; never in
  an Item line, PROCESS, BLOCKS, or as a lead bullet, and **a count never stands in for a highlight.**
  ⚠ **M is DISTINCT AUTHOR IDENTITIES, not a headcount** — lanes committing under a base author line
  are invisible to `%an` (measured 08-26: one base serial showed 62 commits of which that seat wrote
  10). **Write "across M agents", never "M agents were running."** Full rule: the template's
  **FOURTH RULE**.
- **Tie each line to the directive's HEADLINER** — its `title:` in `org/missions/DIRECTIVES.yaml`
  (*"MDPF asset-category views"*, *"ADVI 49F end-to-end"*, *"Model Portfolios Pipeline
  Fortification"*…). Write the day as **progress against that headline**, in its own words where
  they fit. **"For the most part" is deliberate: a genuine win with no directive to hang on still
  goes in.** The tie is the default, not a filter.
- The packet gates the prose; never write a number the packet or a cited read does not carry.
- **Items map 1:1 to `org/missions/DIRECTIVES.yaml` D0-D11, and the item NAME IS THE DIRECTIVE
  `title:` VERBATIM** — since 2026-08-26 the register's titles ARE Andrew's operating-report names,
  so the tie-to-the-headliner rule is a STRING MATCH, not a paraphrase. A mismatch means one of the
  two is wrong. A RETIRED directive keeps its Item line marked DONE/RETIRED until Andrew drops it.
- Yesterday's file is never edited; today's is the snapshot.
- Compiler Tools line in your session log: `comp-state` (self-test N/N) + `directives-check` +
  `to-check` via the packet.

## Cross-references

Engine `.tools/daily-sprint.py` · text template `org/ref/DAILY_SPRINT_TEMPLATE.md` · **visual
system `daily_reports/` (README = the law + the commit_kind Rule-24 record; schema, template,
scripts, data, out)** · first instance `org/sprints/DAILY_SPRINT_2026-08-20.md` · first visual
instance `daily_reports/out/Desktop_DAILY_REPORT_2026-08-27.html` (+ `Mobile_...`) · siblings `/exec-sum` (card+draw,
whole-fabric), `/directives-check` (the register dashboard), `/comp-state`.
