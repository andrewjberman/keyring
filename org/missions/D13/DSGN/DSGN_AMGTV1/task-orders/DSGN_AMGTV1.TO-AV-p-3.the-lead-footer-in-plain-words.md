# DSGN_AMGTV1 task order -- `AV-p-3` -- THE LEAD SOURCE LINE DROPS ITS LONE "Dated", AND THE OLDER-LIST LINE READS IN PLAIN WORDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-p-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~34</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 29c8226a -- oneform.cjs 0 of 3 (FAIL as expected: "Dated" leads the four lead lines; the second line reads "this list is older than the date requested, shown as such rather than silently"; census 14 of 18); green arm 3 of 3 (census 18 of 18); bound Q3 5 of 5 at base and, with the two re-anchors below, on the green arm; portal tsc -b rc=0 on the green arm. Blind spot: static markup with the estate chrome stubbed; the rendered footer is the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-p-3` (round 9, decomposition v9; serves FWD-11)

The CTO's ruling (round-8 analysis, ruling 3): the lead panel's footer is the only footer on the page that starts "Dated" -- the
header card windows and the Positioning footers read "<long date>[, <time> ET] | Source: ..." -- and the line beneath it, "this
list is older than the date requested, shown as such rather than silently", is in the system's voice. Build, in
`portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx` only:
1. `sourceFooterContent` drops "Dated": the line reads "<long as_of_date> | Source: <served words>" (e.g. "September 28th, 2026 |
   Source: ranked from Bloomberg prices (32 names); requested for September 30th, 2026"). Everything after "Source: " stays as it
   is; a list with no `as_of_date` still starts "Source: " and invents no date; no clock is added.
2. `sourceDisclosureText` -- fired exactly when it fires today (`dated` true and `requested_as_of` differing from `as_of_date`) --
   reads in plain words: **"This list is from <long as_of_date>, the newest available."** (the long date from the estate formatter,
   `formatPanelTimestamp(null, as_of_date)` with its appended clock stripped, as `sourceFooterContent` already does). It stays its
   own line beneath the footer; every other list shows no second line.

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
(old anchor -> new) in the instance. Measured on the green arm, the required change NECESSARILY breaks exactly these, each granted
(both in `leadPanelPattern.harness.cjs`, which already loads `longDay` from the estate formatter):
- `source_footer` -- `expectedFooterPrefix` drops its leading `'Dated ' +` (it becomes `longDay(RANKINGS.as_of_date) + ' | Source: '
  + expectedGeneration + ...`), and `footerCarriesAll`'s `universeHtml.includes('Dated ' + longDay(RANKINGS.as_of_date))` becomes
  `universeHtml.includes(longDay(RANKINGS.as_of_date) + ' | Source: ')`.
- `stale_dated_said` -- `universeHtml.includes('older than the date requested')` becomes
  `universeHtml.includes('This list is from ' + longDay(RANKINGS.as_of_date))` (same fact: the older list is said in words).

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change; every other page, component, tab and harness is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~34/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/lib/dateUtils.ts`, `portal/DESIGN.md`,
`portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx` and `ThesisCards.tsx` (the other footers, not edited here), and the
issuer's checks and fixtures under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round9/` (never edit them; the
fixtures are the served payloads the checks render). The round-8 `sourceline.cjs` arm 1 expects "Dated" and is superseded by this
ruling; it is not a criterion.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-p-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round9/checks/oneform.cjs"; echo "exit=$?"</invocation><expect>ONE FOOTER FORM, PLAIN WORDS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-p-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round9/checks/bound.cjs" Q3 leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12 shell.harness.cjs:10 tabs.harness.cjs:20 posture.harness.cjs:32; echo "exit=$?"</invocation><expect>Q3 BOUND: 5 of 5 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-p-3" judgment="true"/>
</proof_of_spec>

AC1 is the built line on the four SERVED lead lists (expected dates computed by the estate's own formatter) plus one labelled
dateless variant, the plain-words second line on every served list that fires it, and the census of every footer on the page (lead
lines, header card windows over VLO / SAP GY / 992 HK, Thesis windows over VLO / 992 HK) in the one form with none starting "Dated";
AC2 the bound on every harness that loads LeadPanel. AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in
walk screenshots (the lead panel footer beside a header card window), never self-graded: the lead footer reads like every other
footer on the page, and the line about an older list reads as plain words to a PM (FWD-11). Portal typecheck, if you run one:
`node_modules/.bin/tsc -b --noEmit` inside `portal/` (`tsc -p .` lists no files and checks nothing).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~34/DSGN_AMGTV1.TO-AV-p-3.the-lead-footer-in-plain-words.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 9 = the round-8 analysis s.4 item 3 with ruling 3 ("Dated" and the system-voice line; the article time rides
AV-p-2, the Positioning model window's source is not cut). Base 29c8226a: oneform.cjs 0 of 3; green 3 of 3 (18 of 18); Q3 5 of 5 at
base, and on green with the two named re-anchors (before them: leadPanelPattern RED, CHECKS-WRONG-WAY source_footer,
stale_dated_said).

<status>complete</status>
<round>9</round>
<slot>~34</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
