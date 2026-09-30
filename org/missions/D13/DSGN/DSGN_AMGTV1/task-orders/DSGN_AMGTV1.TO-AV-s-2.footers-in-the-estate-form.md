# DSGN_AMGTV1 task order -- `AV-s-2` -- EVERY WINDOW FOOTER READS IN THE ESTATE'S ONE FOOTER FORM

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-s-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~27</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV fd4deb75 -- footer.cjs 0 of 3 (FAIL as expected: the stamp builders are not exported, and the base stamps are ISO -- "2026-09-29" on the header windows, "Pack read 2026-09-29" on the Thesis windows, whose source reads "Machine draft from ..."); green arm 3 of 3; bound U2 5 of 5 at base and on the green arm; vv-5.AC1 YES on both. Blind spot: the header window is lazy-loaded, so the check reads the exported builders, not the rendered window.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-s-2` (round 7, decomposition v7; serves FWD-11)

The CTO's ruling (round-6 analysis, ruling 2): FWD-11's footer form is the REFERENCE pages' form -- the estate's shared footer
component with `@/lib/dateUtils` `formatPanelTimestamp`: "September 28th, 2026, 5:00p ET | Source: Bloomberg". Security Analysis's
two window footers (the estate `DialogStamp`) print "2026-09-29 | Source: Bloomberg" (the header card windows,
`components/HeaderCards.tsx` `stampOf`) and "Pack read 2026-09-29 | Machine draft from ..." (the Thesis windows,
`components/ThesisCards.tsx`). Build:
1. Each stamp goes through the estate's `formatPanelTimestamp`: a served value that carries a time (the header figures' `vintage`,
   the thesis `generated_at`) prints `formatPanelTimestamp(value)` whole; a served value that is a bare date (`YYYY-MM-DD`) prints
   the SAME long date with no invented clock and says it is a date (e.g. "Dated September 28th, 2026" -- strip the ", 5:00p ET"
   `formatPanelTimestamp(null, date)` appends, as `pages/InvestorReporting/format.ts` `formatPageDate` does). Keep the header's
   "latest carried vintage" choice, but keep the vintage WHOLE (today it is cut to 10 characters).
2. Each source begins "Source: " (the Thesis source becomes e.g. "Source: machine draft from VLO US's 10-K, filed 2026-02-25" --
   the filed date inside it is data and stays ISO).
3. Export the two pure builders the windows use: `headerCardStamp(bundle, cardKey)` from `HeaderCards.tsx` and
   `thesisWindowStamp(bundle)` from `ThesisCards.tsx`, each returning `{ stamp, source }` -- the check reads them.
The page's in-body data dates stay ISO (round-5 v-6 stands for data; this supersedes it for footers only).
**Import the formatter RELATIVELY -- `import { formatPanelTimestamp } from '../../../lib/dateUtils'` -- not `@/lib/dateUtils`:**
measured at the cut, the page harnesses' loaders (drafting, posture, shell, tabs) cannot resolve an unknown `@/` module; with the
relative path every loader but `drafting`'s resolves it (`dateUtils.ts` has no imports of its own). `drafting.harness.cjs` (granted)
needs ONE loader line: `if (name === '../../../lib/dateUtils') return <src/lib/dateUtils.ts loaded with its own source()>`.
This slot's NEXT order (AV-s-4) also edits `ThesisCards.tsx` and `drafting.harness.cjs`: change only the stamp, the source and the
loader line.

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
portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx
portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx
portal/src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~27/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round7/` (never edit them; the fixtures are the served payloads the checks render).
Also read-only: `portal/src/lib/dateUtils.ts`, `portal/src/ui/components/graphic/HeroGraphic.tsx` (`DialogStamp`), `portal/src/pages/InvestorReporting/format.ts`.
Also read-only: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-5.AC1.sh` (the parity criterion).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-s-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round7/checks/footer.cjs"; echo "exit=$?"</invocation><expect>ONE FOOTER FORM: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-s-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round7/checks/bound.cjs" U2 drafting.harness.cjs:8 thesisLadder.harness.cjs:10 shell.harness.cjs:10 tabs.harness.cjs:20 posture.harness.cjs:32; echo "exit=$?"</invocation><expect>U2 BOUND: 5 of 5 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-s-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-5.AC1.sh"; echo "exit=$?"</invocation><expect>FWD-30 HARNESS READS THE REDESIGNED PAGE: YES -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-s-2" judgment="true"/>
</proof_of_spec>

AC1 is the built behaviour on the served VLO / SAP GY / 992 HK overlays and VLO / 992 HK theses (expected values computed by the estate's own formatter) plus labelled date-only variants; AC2 the bound on every harness that loads the two files; AC3 the page/export parity (both files render in it). AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots (a header card window and a Thesis window beside a Market / Positioning / Philosophy window), never self-graded: every footer reads as a time and a source in the reference pages' one form (FWD-11). Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/` (`tsc -p .` lists no files and checks nothing).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~27/DSGN_AMGTV1.TO-AV-s-2.footers-in-the-estate-form.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 7 = the round-6 analysis s.4 item 2 with ruling 2. Base fd4deb75: footer.cjs 0 of 3.

<status>pending</status>
<round>7</round>
<slot>~27</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
