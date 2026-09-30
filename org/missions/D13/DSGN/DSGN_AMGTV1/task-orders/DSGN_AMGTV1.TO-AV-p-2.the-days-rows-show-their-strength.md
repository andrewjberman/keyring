# DSGN_AMGTV1 task order -- `AV-p-2` -- EACH ARTICLE ROW OF AN OPENED DAY SHOWS THE STRENGTH THAT ORDERS IT, AND ITS TIME IN THE ONE FORM

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-p-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~33</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 29c8226a -- strength.cjs 1 of 3 (FAIL as expected: no "named N times"; the time prints "2026-08-13T04:55:00+00:00 (instant)"; the served-order arm passes at base by design); green arm 3 of 3; bound Q2 4 of 4 at base and, with the one loader line below, on the green arm; portal tsc -b rc=0 on the green arm. Blind spot: static markup with the estate chrome stubbed; a precision other than "instant" is reached only by the labelled variant.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-p-2` (round 9, decomposition v9; serves AMGT_HARVST FWD-5 and FWD-11)

The CTO's rulings (round-8 analysis, rulings 2 and 3): the served `/timeline/day` rows are ordered by the server -- tier, then
`mention_count` descending, then time -- and the page never re-sorts them. On the issuer's walk both 992 HK days showed two rows
with the same visible marks (A, in headline yes, in lead yes), so a PM could not see why a row leads; `mention_count` (8 and 5 on
2026-08-13) is served and was not shown. The time printed as the raw ISO string plus "(instant)". Build, in the article row of
`portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx` (`ArticleRow`):
1. **The strength, in words:** each row shows its `mention_count` as "named <N> times" ("named 8 times"); 1 reads "named once";
   null reads "not counted" (never "named null", "undefined" or "NaN"). You may carry the number in a data attribute as well.
2. **The time in the estate's one form:** a row whose `published_precision` is "instant" shows
   `formatPanelTimestamp(published_utc)` from `portal/src/lib/dateUtils.ts` ("August 13th, 2026, 12:55a ET"); a row with any other
   non-null precision shows the long date only, no clock (`formatPanelTimestamp(null, <the YYYY-MM-DD of published_utc>)` with its
   appended ", h:mm[ap] ET" stripped -- the pattern `LeadPanel.tsx` `sourceFooterContent` already uses); a null time reads "time
   not carried". No ISO timestamp, no "+00:00" and no "(instant)" / "(day)" on the face.
3. **Nothing else moves:** the served order (never re-sorted), the tier mark, the publisher and the "in headline" / "in lead"
   words stay as they are.

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
(old anchor -> new) in the instance. Measured on the green arm, the required change NECESSARILY breaks exactly this one, granted:
- `timelineFourStates.harness.cjs` -- its loader cannot resolve the new `../../../lib/dateUtils` import. ONE loader line in its
  `source()`'s `load(name)`, after `if (Object.prototype.hasOwnProperty.call(STUBS, name)) return STUBS[name];`:
  `if (name === '../../../lib/dateUtils') return source('src/lib/dateUtils.ts');`

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change; every other page, component, tab and harness is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx
portal/src/pages/SecurityAnalysis/__harness__/timelineFourStates.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~33/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/lib/dateUtils.ts`, `portal/DESIGN.md`,
`portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx` (the date-only pattern), `lib/research/harvest/timeline_api.py:132-139`
(the server's sort key), and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round9/` (never edit them; the fixtures are the served payloads the
checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-p-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round9/checks/strength.cjs"; echo "exit=$?"</invocation><expect>ARTICLE ROWS SHOW STRENGTH AND TIME: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-p-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round9/checks/bound.cjs" Q2 timelineFourStates.harness.cjs errorEmpty.harness.cjs:12 shell.harness.cjs:10 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>Q2 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-p-2" judgment="true"/>
</proof_of_spec>

AC1 is the built row on the SERVED 992 HK 2026-08-13 day (expected times computed by the estate's own formatter) plus labelled
variants (a count of 1, a null count, a day-precision time, a null time), with the served order checked unchanged; AC2 the bound
on every harness that loads the timeline or the page around it. AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's
signed-in re-walk (`--day "992 HK=2026-08-13"` plus one event open), never self-graded: a PM sees on each row why the rows run in
the order they do, and each row's time reads like every other time on the page (AMGT_HARVST FWD-5, FWD-11). Portal typecheck, if
you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/` (`tsc -p .` lists no files and checks nothing).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~33/DSGN_AMGTV1.TO-AV-p-2.the-days-rows-show-their-strength.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 9 = the round-8 analysis s.4 item 2 with ruling 2, plus ruling 3's first residual (the article time), placed
here because it sits in the same row component (decomposition v9). Base 29c8226a: strength.cjs 1 of 3; green 3 of 3; Q2 4 of 4 at
base, and on green with the one loader line (before it: timelineFourStates RED, MODULE_NOT_FOUND on the dateUtils import).

<status>pending</status>
<round>9</round>
<slot>~33</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
