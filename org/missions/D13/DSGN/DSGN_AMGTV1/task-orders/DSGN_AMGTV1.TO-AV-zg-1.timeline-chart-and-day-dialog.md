# DSGN_AMGTV1 task order -- `AV-zg-1` -- THE TIMELINE IS A RECHARTS CHART OF ARTICLES PER DAY; THE DAY OPENS IN THE HERO DIALOG; HEADER BRIEF IS THE NEWS CARD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zg-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~80</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks render page sources statically (recharts, the tooltip and the dialog stubbed) from captured and planted fixtures.
comp-adversary: RUN by the issuer at the cut on portal dcdc89b1 (= DEV ec65c5d6 for src/pages/SecurityAnalysis) -- chart.cjs 1 of 4, dayopen.cjs 1 of 4 (FAIL as expected; PLANTED arms pass by design).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zg-1` (round 29, decomposition v29; serves FWD-5 v0.9 and FWD-27 on the timeline and the news card)

PRD `org/missions/D13/DSGN/DSGN_AMGTV1/prd/DSGN_AMGTV1_PRD.md` FWD-5 (lines ~107-128) and FWD-27 (~387-402); register rows SAUX-06, 07,
08, 09, 11, 13, 14, plus SAUX-30 ("day(s) rendered (no gap)") and 31 ("Social: no source measured", "MOST-DISCUSSED: NOT MEASURED")
(`docs/briefs/amgt-security-analysis-ui-findings-20261002.json`). Today `components/TimelinePanel.tsx` is a recharts `BarChart` plotting
`mention_score` with status-coloured hatched fills, 140px tall, with `tick={false}`. Below it sit a text list of coverage events and the
selected day drawn inline. `components/HeaderBrief.tsx` mounts a timeline of its own and prints the description, a posture slot and
no-source lines at rest. Cell `AV-zg-2` (SecurityOverlay) will render, in order: identity, key figures, `<HeaderBrief bundle={bundle} />`,
then `<TimelinePanel securityKey={bundle.security_key} />`.

Build (the checks grade exactly this):
1. **`components/TimelinePanel.tsx`** keeps the export `TimelinePanel` and the prop `securityKey`. Helpers may go in `components/timeline/**`.
   - **Chart:** a recharts `BarChart` or `ComposedChart` whose `data` is the whole served `series`, with exactly ONE
     `<Bar dataKey="articles_total">`. The `YAxis` label contains "Articles per day". The `XAxis` has a `tickFormatter` (or tick
     component) giving a month word or M/D, e.g. `dateWords.chartTick`; never `tick={false}` or the raw ISO date. Height at least 200px
     (`ResponsiveContainer height={N}`, or a wrapper `h-[Npx]` / `h-N` / style height).
   - **One hue:** every bar's `fill` (and `stroke`) is one colour and never a status colour. That rules out `--status-*`,
     `--danger/warning/success/info`, `#BE2D36`, `#D37C17`, `#257E55`, `#2970A3`, and red/orange/amber Tailwind classes. Search state
     is `fillOpacity` or a pattern in that same colour.
   - **Opening a day:** each bar element carries `data-day-bar="<YYYY-MM-DD>"` and its own `onClick`; a Bar-level or chart-level
     `onClick` also works. The handler sets React `useState`.
   - **Tooltip:** `<Tooltip content=...>` renders `DataTooltip` from `@/components/DataTooltip`. Its header carries the date in words
     (`longDate`). Its rows' labels contain "article" (`articles_total`), "publisher" (`publishers_distinct`), "mention"
     (`mention_count_total`) and "headline". The strongest headline is `articles[0].headline` from the day query (the day route serves
     strongest first), or the `lead_headline` of a served event covering that day. No codes (DENIED, PARTIAL, COMPLETE, any snake_case).
   - **Markers:**
     - Each served event becomes an element with `data-timeline-marker="coverage_event"` and `data-marker-day="<first_day>"`, drawn
       INSIDE the chart: a `ReferenceDot`/`ReferenceLine` `shape` or `label` function, a `Scatter` shape, or `Customized`.
     - A marker carries the full `lead_headline` as visible text, an SVG `<title>`, `title=` or `aria-label=`. Its `onClick` (on the
       element, or on the `Reference*` element) opens that day.
     - When `range.markers` is served (AMGT_RESAPP FWD-37, not served yet), read both kinds from it, one marker per date. An
       `earnings_release` row with a date becomes `data-timeline-marker="earnings_release"` carrying its `label`; a row whose date is
       null draws nothing. While no earnings date is served, render exactly ONE `[data-timeline-earnings-empty]` whose words include
       "earnings".
     - Remove the `data-timeline-event` list, the "press one to open its first day" line and the "day(s) rendered (no gap)" caption.
   - **Day dialog:** import `HeroDialog` at the top of the file from `@/ui/components/graphic/HeroGraphic`, not with `React.lazy`; its
     `open` is driven by `useState`. The rows are `[data-timeline-article="<article_key>"]` in served order, and none renders outside the
     dialog.
   - **Rows (SAUX-13):** at rest a row shows the headline, `publisherName(publisher)` and `longStamp(published_utc)` (with the ET clock,
     e.g. "10:06a"); no mention, named, in-headline, in-lead, tier or signal words. The mention count, both flags and "Tier X" go in
     `[data-article-detail="<key>"]`, inside a closed native `<details>` or shown only after pressing `[data-article-more="<key>"]`
     (its handler sets `useState`).
   - **Status colour (SAUX-14):** no text anywhere in the panel is in a status colour. A status colour may sit only on an icon with no
     text, and a search-state note is navy beside its icon.
2. **`components/HeaderBrief.tsx`.**
   - **Props:** keep the export `HeaderBrief`; `bundle` is required, `postureLine` optional and ignored.
   - **No timeline:** it mounts NO TimelinePanel and no chart (the overlay mounts the one timeline).
   - **News card:** `[data-header-feed="<coverage_status>"]` exactly once, with `data-feed-item` and an `href` on each item.
   - **Description:** `[data-header-description]` exactly once, inside a closed `<details>` whose `<summary>` is in plain reader words.
   - **Words:** no visible "most-discussed", "Social:", "no source measured" or "not measured". Keep `data-header-social="<served status>"`
     as an attribute on an element that prints nothing; the battery's tabs harness reads it.
3. **`__harness__/timelineFourStates.harness.cjs`.** Not in the battery, but it asserts the old status hatch fills. Re-anchor ONLY its
   fill clause to item 1's one-hue rule, so it still fails a page that paints a bar in a status colour; show one planted run.
4. **Shared helpers you read and do not edit:** `dateWords.longDate` / `longStamp` / `chartTick` (cell `AV-zg-5` owns `dateWords.ts` and
   keeps their output unchanged), `publisherName` (`components/publisherNames.ts`) and `DataTooltip`.

**Contracts:** C-PRESENTATION-ONLY. The page computes no count, publisher number, headline or date; it plots and labels the served
series. Design law: a code may sit in a data attribute, never in visible or tooltip text.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change; in the harness file only the fill clause changes.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
portal/src/pages/SecurityAnalysis/components/timeline/
portal/src/pages/SecurityAnalysis/__harness__/timelineFourStates.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~80/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zg-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/timeline/chart.cjs"; echo "exit=$?"</invocation><expect>THE TIMELINE IS A RECHARTS CHART OF ARTICLES PER DAY WITH THE SHARED TOOLTIP AND MARKERS ON IT: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zg-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/timeline/dayopen.cjs"; echo "exit=$?"</invocation><expect>THE DAY OPENS IN THE HERO DIALOG AND THE HEADER BRIEF IS THE NEWS CARD ABOVE THE ONE TIMELINE: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zg-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)" --skip tabs,namecard,postureharness,posturezero; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (4 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

AC3 skips two items whose re-anchor belongs elsewhere:
- `tabs`: its `header_posture_line_matches_payload` clause is re-anchored by cell `AV-zg-3`.
- `namecard`: the issuer's round-20 check finds the ticker inside the posture line you remove. The issuer re-reads it on the merged
  candidate.
- `postureharness` and `posturezero` (AMENDMENT 1, issuer, 2026-10-02 ~21:3xZ, on row Z-W80-S1): both run `posture.harness.cjs`, which reads
  the posture line `IdentityHeader` renders. With HeaderBrief's posture slot gone, that line returns only when cell `AV-zg-2` renders its
  single `[data-header-posture]` inside its details control. The two cells land together, so these items are read on the merged
  candidate.
The issuer runs the full battery, with no skip, on the merged candidate.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~80/DSGN_AMGTV1.TO-AV-zg-1.timeline-chart-and-day-dialog.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W80-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, the re-anchored harness clause
with its planted-failure run, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Not graded by the checks** (L9 PNG read): the news card's look apart from the dialog; chart readability above 200px and tick
  density; the colour and the search-state cue's legend; marker shape, label legibility and x placement (the stub positions nothing);
  the tooltip and dialog look; the summary wording; and the navy search-state note beside its icon.
- **Must land together:** `AV-zg-1` and `AV-zg-2`. HeaderBrief stops mounting the timeline here, and SecurityOverlay mounts it there,
  so the merged candidate has exactly one.
- **Surprises:** no per-day headline is served (the hover reads the day route); `range.markers` is not served yet (RESAPP FWD-37), so the
  earnings shape is planted from the FWD-37 wording and arm 3 may need a re-cut if the served shape differs; for 992 HK 2026-09-23 the
  series serves 2 articles and the captured day route 0 (a SAUX-12 kind of disagreement, RESAPP's).

<status>pending</status>
<round>29</round>
<slot>~80</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
