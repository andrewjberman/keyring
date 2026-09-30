# DSGN_AMGTV1 task order -- `AV-s-3` -- THE TIMELINE: "NOT SEARCHED" IN WORDS, THE SERVED EVENTS MARKED, AND A NAMED DAY WALKED BY DATE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-s-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~28</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV fd4deb75 -- timeline7.cjs 0 of 3 (FAIL as expected: the 992 HK 2026-08-13 dissection reads "Denied day -- retrieval was denied for this day"; VLO's all-DENIED range is captioned "every day above is a real, honest zero"; 0 [data-timeline-event] of 3 served); walkday.cjs 0 of 3 (no --day option); green arms 3 of 3 and 3 of 3; bound U3 3 of 3 at base and on the green arm. Blind spot: static markup with react-query and recharts stubbed; the walker half is read statically -- the issuer's walk is its live run.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-s-3` (round 7, decomposition v7; serves AMGT_HARVST FWD-5 and FWD-6)

The CTO's ruling (round-6 analysis, ruling 4): by AMGT_HARVST's rule a DENIED day is one no publisher's listing SEARCH reached --
not a failed retrieval, and not a zero (992 HK 2026-08-13 is DENIED and serves 2 articles). Build, in
`components/TimelinePanel.tsx`:
1. **DENIED reads "Not searched on this day"** -- the day dissection's status line (today "Denied day -- retrieval was denied for
   this day"), and a day with articles lists them UNDER that line as served (strongest first is the served order); the day
   tooltip ("not searched on this day", and "-- N found anyway" when `articles_total` > 0); and the legend's word for the state
   ("not searched" -- keep `data-timeline-legend-swatch="denied"` and the swatch colour). No visible "denied" or "retrieval".
2. **The all-quiet caption never calls an unsearched range a zero** (today: "No coverage found in this range yet -- every day above
   is a real, honest zero."). When every day is DENIED it says the range was not searched (e.g. "Every day in this range was not
   searched yet, so no articles were looked for -- a blank day here is not a quiet day."); when some days were searched it states
   the SERVED counts (e.g. "No articles were found on the 74 searched day(s); the other 198 were not searched."). Counts are the
   producer's own day statuses, counted -- nothing else derived.
3. **The event layer.** The served `/timeline` carries `events` (`first_day`, `last_day`, `articles_total`, `lead_headline`) that the
   panel never draws. Mark each served event with ONE element carrying `data-timeline-event="<first_day>..<last_day>"` and its
   `lead_headline` in visible text (with its dates and article count in words); pressing it opens that event's first day (the day
   dissection lists its articles). No event served -> no element.
And in `.claude/skills/ui-walk/walk.mjs` (the round's walk grades HARVST FWD-5 "on pixels" on 992 HK 2026-08-13, 2 articles):
4. A repeatable `--day "<security>=<YYYY-MM-DD>"` option (into `opt.days`). In the timeline walk, for each named day of an opened
   `--security`: press `[data-day-bar="<date>"]` (click, else dispatchEvent), settle, read the opened dissection's article rows in
   the order the page lists them (`[data-timeline-selected-day] li` inner texts), run `checks(page, "<sec>-timeline-day-<date>")`
   (so the sign-in guard and the screenshot run on it), and record `{security, date, pressed, article_rows_in_page_order}`; a date
   with no bar records a measured finding `timeline:day-not-found`. Write all of them to `timeline-days.json` in the walk's output
   folder beside findings.json. One line in `.claude/skills/ui-walk/SKILL.md` documenting `--day` and `timeline-days.json`.
The chart's day FILLS and hatch patterns are unchanged: the charts keep their colour (C6). No harness needs a re-anchor for this
cell (measured on the green arm: every page harness at its base count).

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: no figure is computed,
converted or guessed, no name is looked up or joined, and a value the payload does not carry reads as a designed empty state
naming, in plain words, what is missing and which team fills it -- never a project code, serial or storage path.
C-ESTATE-FIXTURES -- windows are the estate's HeroDialog + DialogStamp, panels and states are the estate's; nothing forked.
**Design law (portal `DESIGN.md`):** white panels with navy ink (C3); ONE dark band per page; no translucent white (C5.8); no
shadow (C11). A code, field name or path may sit in a data attribute or in code, never in visible text -- and text inside a
collapsed `<details>` is still visible text.

**If a bound harness check is anchored on the raw text this cell removes,** re-anchor that ONE check onto the same fact as the
page now states it (the words, or a data attribute), keep its claim, never drop it; the harness keeps at least its base
check count (the floor in the bound criterion). Only a harness named in `<paths>` may be edited. Record each re-anchor
(old anchor -> new) in the instance.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change; every other page, component, tab and harness is unchanged.
3. Never run the walker signed in; never arm, disarm or read the secret of the walker account. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx
.claude/skills/ui-walk/walk.mjs
.claude/skills/ui-walk/SKILL.md
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~28/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round7/` (never edit them; the fixtures are the served payloads the checks render).
Also read-only: `lib/research/harvest/timeline_api.py` (the served shapes), `.claude/skills/ui-walk/signin_detect.mjs`, `.claude/skills/ui-walk/ui_walker_account.py` (never run it).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-s-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round7/checks/timeline7.cjs"; echo "exit=$?"</invocation><expect>TIMELINE NOT SEARCHED AND EVENTS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-s-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round7/checks/walkday.cjs"; echo "exit=$?"</invocation><expect>WALK OPENS A DAY BY DATE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-s-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round7/checks/bound.cjs" U3 timelineFourStates.harness.cjs shell.harness.cjs:10 posture.harness.cjs:32; echo "exit=$?"</invocation><expect>U3 BOUND: 3 of 3 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-s-3" judgment="true"/>
</proof_of_spec>

AC1 is the built page behaviour on SERVED /timeline payloads (992 HK with 3 events, VLO all DENIED, ASML) and the served 992 HK 2026-08-13 day (plus one labelled all-quiet variant); AC2 the walker's new step, read statically (never run the walker signed in; never touch the walker account); AC3 the bound. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk (--day "992 HK=2026-08-13"), never self-graded: a PM opens a day and reads its articles strongest first under "Not searched on this day", and the name's coverage bursts appear as marked events with a headline (AMGT_HARVST FWD-5, FWD-6). Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/` (`tsc -p .` lists no files and checks nothing).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~28/DSGN_AMGTV1.TO-AV-s-3.not-searched-and-the-event-layer.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 7 = the round-6 analysis s.4 item 3 with ruling 4. Base fd4deb75: timeline7.cjs 0 of 3, walkday.cjs 0 of 3.

<status>complete</status>
<round>7</round>
<slot>~28</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
