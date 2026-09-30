# DSGN_AMGTV1 task order -- `AV-q-2` -- THE LEAD-LIST SOURCE LINE READS IN THE ONE FOOTER FORM, DATE ONLY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-q-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~30</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV ab7e1e49 -- sourceline.cjs 0 of 3 (FAIL as expected: the line reads "Source: ranked 2026-09-28 ... (requested 2026-09-29)", ISO inside the source; census 14 of 18 footers in the one form, the four lead lines the misses); green arm 3 of 3 (census 18 of 18); bound Q2 5 of 5 at base and, with the two re-anchors below, on the green arm; portal tsc -b rc=0 on the green arm. Blind spot: static markup with the estate chrome stubbed; the rendered footer is the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-q-2` (round 8, decomposition v8; serves FWD-11)

The CTO's ruling (round-7 analysis, ruling 4): the lead panel's source line ("Source: ranked 2026-09-28 from Bloomberg prices (32
names) (requested 2026-09-30)") sits where a window's footer sits, and FWD-11 reads "every footer". It takes the one form -- the date
in words through `formatPanelTimestamp`, then "Source: ..." -- DATE ONLY (a ranking carries a date and no time; never invent one);
the requested date may follow as a second clause in words. Build, in
`portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx` `sourceFooterContent(fields)`:
1. When the list serves `as_of_date`, the line starts `Dated <long date> | Source: ` -- the long date is
   `formatPanelTimestamp(null, as_of_date)` with the ", h:mma ET" it appends stripped (the round-7 `HeaderCards.tsx` pattern:
   `.replace(/,\s*\d{1,2}:\d{2}[ap]\s*ET$/i, '')`). No ISO date and no clock anywhere in the line. No `as_of_date` -> the line starts
   `Source: ` and carries no "Dated".
2. The source keeps the served words (`generationCaptionWords` with the date taken out of it, so the date is not said twice): the
   vendor and "(N names)" stay. When `requested_as_of` is served and differs from `as_of_date`, append `; requested for <long date>`
   inside the source.
Import the formatter RELATIVELY -- `import { formatPanelTimestamp } from '../../../lib/dateUtils'` (the page harness loaders cannot
resolve an unknown `@/` module; `dateUtils.ts` has no imports of its own). Every other footer on the page is unchanged.

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
(old anchor -> new) in the instance. Measured on the green arm, the required change NECESSARILY breaks exactly these, each granted:
- `errorEmpty.harness.cjs` -- its loader cannot resolve the new import. ONE loader line, after
  `if (name === './GenerationCaption') return loaded.caption;`:
  `if (name === '../../../lib/dateUtils') return source('src/lib/dateUtils.ts');`
- `leadPanelPattern.harness.cjs` `source_footer` -- expected `'Source: ' + generationCaptionWords(RANKINGS) + ' (requested <ISO>)'`
  -> `'Dated ' + longDay(as_of_date) + ' | Source: ' + generationCaptionWords({...RANKINGS, as_of_date: null})`, plus
  `'requested for ' + longDay(requested_as_of)` when the requested day differs; `longDay` is the estate formatter loaded with
  `source('src/lib/dateUtils.ts')` and stripped of its clock as above.
- `leadPanelPattern.harness.cjs` `caption_facts_unchanged` -- `generationLine.includes(<ISO as_of_date>)` and
  `includes(<ISO requested_as_of>)` -> `includes(longDay(as_of_date))` and, when the requested day differs,
  `includes(longDay(requested_as_of))`.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change; every other page, component, tab and harness is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~30/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round8/` (never edit them; the fixtures are the served payloads the checks render).
Also read-only: `portal/src/lib/dateUtils.ts`, `portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx` (the round-7 date-only footer pattern), `portal/src/pages/SecurityAnalysis/components/GenerationCaption.tsx`.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-q-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round8/checks/sourceline.cjs"; echo "exit=$?"</invocation><expect>LEAD SOURCE LINE IN THE FOOTER FORM: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-q-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round8/checks/bound.cjs" Q2 leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12 shell.harness.cjs:10 tabs.harness.cjs:20 posture.harness.cjs:32; echo "exit=$?"</invocation><expect>Q2 BOUND: 5 of 5 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-q-2" judgment="true"/>
</proof_of_spec>

AC1 is the built line on the four SERVED lead lists (expected values computed by the estate's own formatter) plus one labelled
dateless variant, and the census of every footer on the page (lead lines, header card windows over VLO / SAP GY / 992 HK, Thesis
windows over VLO / 992 HK) in the one form; AC2 the bound on every harness that loads LeadPanel. AC3 is JUDGMENT, graded by
`3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots (the lead panel beside a header card window and a Market /
Positioning window), never self-graded: every footer on the page reads as a date and a source in the reference pages' one form
(FWD-11). Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/` (`tsc -p .` lists no files and
checks nothing).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~30/DSGN_AMGTV1.TO-AV-q-2.the-lead-source-line-in-the-footer-form.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 8 = the round-7 analysis s.4 item 2 with ruling 4. Base ab7e1e49: sourceline.cjs 0 of 3 (census 14 of 18);
green 3 of 3 (18 of 18); Q2 5 of 5 at base, 5 of 5 on green with the three named re-anchors (before them: leadPanelPattern RED on
source_footer + caption_facts_unchanged, errorEmpty RED MODULE_NOT_FOUND).

<status>complete</status>
<round>8</round>
<slot>~30</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
