# DSGN_AMGTV1 task order -- `AV-o-1` -- ONE HOUSE DATE FORM ACROSS THE PAGE: EVERY DATE A PERSON READS IN THE REFERENCE PAGES' LONG FORM

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-o-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~39</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut (read-only invokes).
comp-adversary: RUN by the issuer at the cut on portal DEV b6634ba0 -- dates.cjs 1 of 3 (FAIL as expected: 224 visible ISO dates on 44 of 45 walked surfaces; the long-form arm fails on every header, the event dates and both bare-date stamps; the data- attribute control passes at base by design); green arm 3 of 3 (0 visible ISO dates over 45 surfaces, 162 data- attributes still carry the ISO value) on the drain state of o-2, o-3 and o-4 plus this cell; bound ALL 16 of 16 at base and, with the six named harness changes below, on the green arm; portal tsc -b rc=0 on the green arm. Blind spot: static markup with the estate chrome stubbed; chart ticks and tooltips are the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-o-1` (round 10, decomposition v10; serves FWD-11)

The CTO's ruling (round-9 analysis, ruling 1, "the house date form", which settles the date form for the whole page): **every date
a person reads uses the reference pages' LONG FORM** -- "September 28th, 2026", and with a time "..., 10:47p ET" where one is
served. ISO stays only where no one reads it: `data-` attributes, URLs and export fields. Where the reference pages use a compact
form for the same element (chart axis ticks, for example), the page may use that compact form, taken from the reference page's own
formatter, never invented. It covers every surface: identity as-of, posture as-of, the timeline axis, the event dates, the lead
rows' movement windows, "Updated", "filed", the day heading and tooltip, and the bare-date "Dated" paths in `HeaderCards.tsx` and
`ThesisCards.tsx`. Build, in `portal/src/pages/SecurityAnalysis/`:
1. **ONE helper module**, `dateWords.ts`, exporting `longDate(iso)` -- a bare day (`YYYY-MM-DD`, or the first 10 characters of a
   longer value) as `formatPanelTimestamp(null, day)` from `portal/src/lib/dateUtils.ts` with its appended ", h:mm[ap] ET"
   stripped ("September 28th, 2026"); null reads '' -- and `longStamp(value)` -- a bare day as `longDate`, a timestamp with a time
   as `formatPanelTimestamp(value)` ("September 28th, 2026, 10:47p ET"), anything that is not a date returned as it came. It imports
   the estate formatter as `'../../lib/dateUtils'`.
2. **Every site where a person reads a date** uses it, with the ISO value kept (or added) on a `data-` attribute of the same
   element. Measured at the cut, the sites are: `components/IdentityLine.tsx` (identity as of), `components/SecurityOverlay.tsx`
   (posture as of; identity as of), `components/LeadPanel.tsx` (the lead posture line's as of), `components/GenerationCaption.tsx`
   ("ranked <date>"), `components/HeaderBrief.tsx` (the News window "newest first (<from> to <to>)" and a news item's time),
   `components/ProvenanceLine.tsx` and `components/StatTile.tsx` ("as of <vintage>"), `components/RankedList.tsx` (a row's movement
   window "(<from> -> <to>)"), `components/RankedChart.tsx` ("the latest is <date>", its axis ticks and tooltip label),
   `components/ThesisCards.tsx` ("filed <date>"; `thesisWindowStamp`'s bare date without "Dated"), `components/HeaderCards.tsx`
   (`footerTime`'s bare date without "Dated"), `components/TimelinePanel.tsx` ("dense from <date>", the axis end labels, the
   coverage-event dates, the "<date>'s articles" heading and its loading / error text, the day tooltip), `postureCites.ts` ("at the
   <date> snapshot"), and the tabs `ThesisTab.tsx` ("filed", "Updated"), `ModelTab.tsx` ("Updated"), `PostureTab.tsx` ("drafted by a
   machine on <date>", "Snapshot as of"), `ExecManagementTab.tsx` ("as of <date>") and `PeersTab.tsx` (universe vintage, as of).
   A bare day reads without a clock; a timestamp keeps its ET clock; a range reads both ends in the long form.
3. Nothing else moves: no value, order, count or other word changes; a label that is not a date (e.g. a coverage vintage word in
   the collapsed machine detail) stays as it is.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: no figure is computed,
converted or guessed, no name is looked up or joined, and a value the payload does not carry reads as a designed empty state
naming, in plain words, what is missing and which team fills it -- never a project code, serial or storage path.
C-ESTATE-FIXTURES -- windows are the estate's HeroDialog + DialogStamp, panels and states are the estate's; nothing forked.
**Design law (portal `DESIGN.md`):** white panels with navy ink (C3); ONE dark band per page; no translucent white (C5.8); no
shadow (C11). A code, field name or path may sit in a data attribute or in code, never in visible text -- and text inside a
collapsed `<details>` is still visible text.

**If a bound harness check is anchored on the raw text this cell changes,** re-anchor that ONE check onto the same fact as the
page now states it (the words, or a data attribute), keep its claim, never drop it; the harness keeps at least its base
check count (the floor in the bound criterion). Only a harness named in `<paths>` may be edited. Record each re-anchor
(old anchor -> new) in the instance. Measured on the green arm, the required change NECESSARILY breaks exactly these six, each
granted with its exact change (the loaders cannot resolve the new `../dateWords` module, nor the `../../lib/dateUtils` path it
imports):
- `drafting.harness.cjs` -- two loader lines: `if (name === '../../lib/dateUtils') return loaded.dateUtils;` and
  `if (name === '../dateWords') return source('src/pages/SecurityAnalysis/dateWords.ts');`
- `errorEmpty.harness.cjs` and `timelineFourStates.harness.cjs` -- two loader lines each:
  `if (name === '../../lib/dateUtils') return source('src/lib/dateUtils.ts');` and
  `if (name === '../dateWords') return source('src/pages/SecurityAnalysis/dateWords.ts');`
- `execFallback.harness.cjs` -- two loader lines:
  `if (name === '../dateWords') return loadTab(fs.readFileSync(path.join(base, 'src/pages/SecurityAnalysis/dateWords.ts'), 'utf8'), 'dateWords.ts', box_, current);`
  and the same form for `'../../lib/dateUtils'` pointing at `src/lib/dateUtils.ts` (`'dateUtils.ts'`).
- `execText.harness.cjs` -- the same two lines as execFallback, calling `loadTab(..., current)` with no `box_` argument.
- `tabs.harness.cjs` check `peers_csc_table_absent_marked` -- add `const { longStamp } = source('src/pages/SecurityAnalysis/dateWords.ts');`
  and re-anchor ``peersHtml.includes(`universe vintage ${esc(fixture.peers.universe_vintage)}`)`` ->
  ``peersHtml.includes(`universe vintage ${esc(longStamp(fixture.peers.universe_vintage))}`)`` (same fact, in the house form).

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change; every other page, component, tab and harness is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Your portal branch starts from the drain state of this round's o-2, o-3 and o-4 (the dossier blocks, the team cases and the
   unresolved-unit display are already on it) -- keep them whole.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/dateWords.ts
portal/src/pages/SecurityAnalysis/postureCites.ts
portal/src/pages/SecurityAnalysis/components/GenerationCaption.tsx
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx
portal/src/pages/SecurityAnalysis/components/IdentityLine.tsx
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/components/ProvenanceLine.tsx
portal/src/pages/SecurityAnalysis/components/RankedChart.tsx
portal/src/pages/SecurityAnalysis/components/RankedList.tsx
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/components/StatTile.tsx
portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx
portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/timelineFourStates.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execText.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~39/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/lib/dateUtils.ts` (`formatPanelTimestamp`), `portal/DESIGN.md`, and the
issuer's checks and fixtures under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round10/` (never edit them; the
fixtures are the served payloads the checks render; `surfaces.cjs` renders every walked surface).

## 4. PROOF OF SPEC (literal; timeout 180)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-o-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round10/checks/dates.cjs"; echo "exit=$?"</invocation><expect>ONE HOUSE DATE FORM: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-o-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round10/checks/bound.cjs" Q1 drafting.harness.cjs:8 errorEmpty.harness.cjs:12 execFallback.harness.cjs execPattern.harness.cjs:9 execText.harness.cjs leadPanelPattern.harness.cjs:15 modelPattern.harness.cjs:12 peersCarry.harness.cjs peersPattern.harness.cjs:13 peersReadFailed.harness.cjs posture.harness.cjs:32 posturePattern.harness.cjs:13 shell.harness.cjs:10 tabs.harness.cjs:20 thesisLadder.harness.cjs:10 timelineFourStates.harness.cjs; echo "exit=$?"</invocation><expect>Q1 BOUND: 16 of 16 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-o-1" judgment="true"/>
</proof_of_spec>

AC1 is the built page on SERVED fixtures over 45 walked surfaces (the lead lists and footers, the lead chart, eight identity
headers, the mention timeline and 992 HK's day, and the four tabs of eight names): 0 visible ISO dates, the ISO values still on
`data-` attributes (the control), and the long form read from the estate formatter on every header's identity and posture as-of,
the event dates and both bare-date stamps; AC2 the bound on every page harness. AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9
on the issuer's signed-in walk, never self-graded: every date on the page reads like the reference pages' dates (FWD-11). Portal
typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/` (`tsc -p .` lists no files and checks nothing).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~39/DSGN_AMGTV1.TO-AV-o-1.one-house-date-form.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 10 = the round-9 analysis s.4 item 1 with ruling 1. QUEUED chain: every page file this cell writes is also
written by o-2, o-3 or o-4, so it starts only after those three drain, on the post-drain DEV (cut rule (a), queue-aware base). Base
b6634ba0: dates.cjs 1 of 3; the green arm (the issuer's scratch r10-green-b by a helper agent, merged over r10-green-a, 3 import-line
conflicts resolved) reads 3 of 3 with ALL 16 of 16 and tsc rc=0.

<status>complete</status>
<round>10</round>
<slot>~39</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
