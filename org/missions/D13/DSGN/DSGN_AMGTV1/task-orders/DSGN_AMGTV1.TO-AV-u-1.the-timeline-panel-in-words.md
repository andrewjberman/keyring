# DSGN_AMGTV1 task order -- `AV-u-1` -- THE TIMELINE PANEL: A FAILED CALL IN WORDS, A PARTIAL DAY SAYS WHAT WAS SEARCHED, A LEGIBLE LEGEND

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-u-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~22</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 4f927ad0 -- timeline.cjs 0 of 3 (FAIL as expected: a failed call prints "Cause: API request failed: 500 ..." / the error_code; the PARTIAL tooltip reads "[PARTIAL] stored height 0 -- coverage WAS captured ..."; DayDissection not exported; the legend's partial / denied words read 4.31:1 / 3.93:1 on the tile rung); green arm 3 of 3; bound 2 of 2 (PASS). Blind spot: static markup with react-query and recharts stubbed (the tooltip is rendered through recharts' `content` prop; pixels are the walk's).
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-u-1` (round 6, decomposition v6; serves FWD-5, FWD-11)

`components/TimelinePanel.tsx` draws the mention timeline on the identity band. Three things, all on this one panel:

1. **A failed call reads in words.** On a non-200 / thrown fetch, and on a served error body (`{error: true, error_code, message}`),
   the panel already renders the estate's `PanelError` (`data-timeline-panel="ERROR"`, never the loading skeleton) -- keep that --
   but it prints the transport text as the visible cause ("Cause: API request failed: 500 Internal Server Error -", or
   "UPSTREAM_TIMEOUT: ..."). Build: the visible error reads in words only (the existing message and hint are words); the raw
   reason rides a data attribute (e.g. `data-timeline-error-cause` on the `data-timeline-panel="ERROR"` wrapper). No HTTP status
   number, no "API request failed" / "Internal Server Error", no error_code in visible text. The same rule for the day
   dissection's own failure.
2. **A PARTIAL day says which publishers were SEARCHED and what was found.** The served series entry and the served day body carry
   `publishers_covered` (a count) and `publishers_covered_codes` (e.g. `["wsj"]`, `["sa"]`). By the producer's definition a
   publisher "covers" a day when its listing SEARCH for the name reached that day -- NOT that it wrote about the name; every
   PARTIAL day read so far serves 0 articles. Build: a PARTIAL day reads, in the day tooltip and in the day dissection,
   "Searched: <publisher names in words> -- nothing found." (0 articles) or "-- <N> found." (N = the served `articles_total` for the
   tooltip, the served article count for the dissection). Publisher names come from a FIXED, NAMED display map in this file
   (`sa` -> "Seeking Alpha", `wsj` -> "The Wall Street Journal"); an unmapped code reads in words (e.g. "a publisher this page has
   no name for yet"), never the raw code. The payload serves NO count of publishers NOT reached, so the page states none (no
   "Not reached: <number>"). The word "covered" never appears in visible text (the API field names are unchanged). The tooltip's
   other lines drop the machine text too: no `mention_score` field name, no bracketed status ("[PARTIAL]"). Declare the two
   optional fields on `TimelineSeriesEntry` / `TimelineDayResponse` (`publishers_covered?: number | null`,
   `publishers_covered_codes?: string[] | null`). **Export `DayDissection`** (the check renders it).
3. **The legend reads on the band.** The legend's state words ("complete -- partial -- denied", `<span data-timeline-legend>`)
   measured 4.1:1 for "partial" on the walk (CVO); the band-scoped `--warning` / `--danger` reach only 4.31:1 / 3.93:1 on the
   lighter tile rung the panel can sit on. Build: every legend word clears 4.5:1 on BOTH `--layer-body` and `--layer-tile` --
   e.g. the band's own ink (`currentColor`) with the state's colour on a small swatch beside the word. The chart's day FILLS
   (`PARTIAL_BASE`, `DENIED_BASE` and their hatch patterns) are unchanged: the charts keep their colour (C6).

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
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx
portal/src/pages/SecurityAnalysis/__harness__/timelineFourStates.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~22/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round6/` (never edit them; the fixtures are the served payloads the checks render).
Also read-only: `lib/research/harvest/timeline_api.py` (the served shapes: `publishers_covered`, `publishers_covered_codes`) and
`portal/src/index.css` (the `.dark-band` and `body` layer tokens).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-u-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round6/checks/timeline.cjs"; echo "exit=$?"</invocation><expect>TIMELINE PANEL IN WORDS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-u-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round6/checks/bound.cjs" U1 timelineFourStates.harness.cjs tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>U1 BOUND: 2 of 2 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-u-1" judgment="true"/>
</proof_of_spec>

AC1 is the built behaviour on the SERVED /timeline payloads captured at the cut (992 HK: one PARTIAL day, searched wsj; ASML: 74 PARTIAL days, searched sa) plus one labelled issuer variant for the unmapped-code branch; AC2 the bound. AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots, never self-graded: a failed timeline reads as a designed error in words, a PARTIAL day tells a PM which publishers were searched and that nothing (or N articles) was found -- never "covered" -- and the legend reads on the band (FWD-5, FWD-11).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~22/DSGN_AMGTV1.TO-AV-u-1.the-timeline-panel-in-words.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 6 = round-5 analysis s.4 item 1 with section 2a (the "covered" correction, CTO~Z msg 26748). The walk's INTU "skeleton" (walk D shot 054) was the in-flight LOADING state; the panel's designed ERROR state rendered on the next steps (shot 059: "The timeline could not be loaded ... Cause: API request failed: 500 Internal Server Error -"), so the build is the ERROR state's words, not its existence (the issuer's round-5 drain-end read item 1 mis-read shot 054). Fixtures timeline.*.json / timelineDay.*.json captured at the cut by a read-only invoke of opal-amgt-scoped-api (CodeSha256 uv0oTSMa...Ng=, LastModified 2026-09-29T21:57:59Z). Base 4f927ad0: timeline 0 of 3; green 3 of 3; U1 bound 2 of 2.

<status>pending</status>
<round>6</round>
<slot>~22</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
