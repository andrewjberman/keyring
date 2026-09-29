# DSGN_AMGTV1 task order -- `AV-v-6` -- ONE DATE FORM FOR THE PAGE'S OWN DATES, AND THE TIMELINE LEGEND READABLE ON THE BAND

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-v-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~20</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 09bd04b1 -- datecontrast.cjs 1 of 3 (FAIL as expected: both panel headers print "Sep 29, 2026" beside ISO dates; the legend's partial/denied words use the light-canvas --status-* tokens; the fills arm passes); green arm 3 of 3; bound 4 of 4 (PASS). Blind spot: contrast is graded by token class (the band's own lightened family), not by pixel -- the walk's design:contrast check is the pixel read.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-v-6` (round 5, decomposition v5; serves FWD-11)

This is the THIRD order of your slot. The first two (AV-v-4: whose Base case; AV-v-7: the served Model words) are already committed
on your branches by this slot; build on top of them and do not change what they built.

1. **The page's own dates, one form.** The page prints dates it formats itself in two forms: ISO "2026-02-26" (every served as-of /
   filed date) and a short month form "Sep 29, 2026" -- the Thesis and Model panel headers (`ThesisPanelHeader` in
   `tabs/ThesisTab.tsx`, `ModelPanelHeader` in `tabs/ModelTab.tsx`, both `toLocaleDateString('en-US', { month: 'short', ... })`),
   which print "the 20-F filed 2026-02-26 ... Updated Sep 29, 2026" on ONE line. Build: both headers print their "Updated" date as
   ISO YYYY-MM-DD (UTC, the same day as today's form). Dates INSIDE served prose (filing passages, drafted sentences: "December
   31, 2025") are the producer's words and are NOT rewritten (C-PRESENTATION-ONLY).
2. **The Mention timeline legend on the identity band.** `components/TimelinePanel.tsx`'s legend (`<span data-timeline-legend>`:
   "complete -- partial -- denied") colours its "partial" and "denied" words with the day fills' tokens, `hsl(var(--status-warning))`
   and `hsl(var(--status-danger))` -- the light-canvas family: "DENIED" measured 2.59:1 on the band (rgb(190,45,54) on
   rgb(25,38,67)). Build: the legend WORDS use the band-scoped tokens that `index.css`'s `.dark-band` block lightens for the band --
   `hsl(var(--warning))` (5.27:1) and `hsl(var(--danger))` (4.80:1) -- or the band's own ink with the colour on a swatch beside the
   word. The chart's day FILLS (`PARTIAL_BASE`, `DENIED_BASE` and their hatch patterns) are unchanged: the charts keep their colour
   (C6).

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
2. Only the files in `<paths>` under `portal/` change; every other page, component, tab and harness is unchanged. In `ModelTab.tsx`
   change only the panel header's date.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx
portal/src/pages/SecurityAnalysis/__harness__/thesisLadder.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/timelineFourStates.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~20/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/index.css` (the `.dark-band` token block), `portal/DESIGN.md`, and the
issuer's checks and fixtures under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-v-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/checks/datecontrast.cjs"; echo "exit=$?"</invocation><expect>ONE DATE FORM AND A READABLE LEGEND: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-v-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/checks/bound.cjs" V6 tabs.harness.cjs:20 thesisLadder.harness.cjs:10 timelineFourStates.harness.cjs modelPattern.harness.cjs:12; echo "exit=$?"</invocation><expect>V6 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-v-6" judgment="true"/>
</proof_of_spec>

AC1 is the built behaviour on the served SAP GY payload and the legend's own source; AC2 the bound. AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots, never self-graded: the page's own dates read in one form and the timeline legend reads on the band (FWD-11).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~20/DSGN_AMGTV1.TO-AV-v-6.one-date-form-and-a-readable-legend.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 5 = the round-4 analysis's enrichment list @177c576c80 section 4 item 6. Decomposition v5. NARROWED at the
cut, by measurement: (a) the walker's "September 22nd, 2026" long form is SERVED PROSE (its date check matches any full month name
in body text; the page itself formats none) -- a NOT-cell like "$1,234"; the page's own second form is the short "Sep 29, 2026"
the walker cannot see. (b) walk C's contrast samples: "DENIED" on the identity band is the one page-authored hit; the dialog
samples ("OPAL CAPITAL / THESIS" eyebrow, the white HeroDialog title, "What each line rests on") read the white body under the
dark gradient hero -- the estate HeroDialog fixture (C-ESTATE-FIXTURES), dropped as a heuristic false positive. Slot ~20's third
order (ModelTab.tsx). Base 09bd04b1: datecontrast 1 of 3; green arm (ISO headers + legend words on --warning/--danger) 3 of 3;
V6 bound 4 of 4 (round5 `_load.cjs` reads timelineFourStates' `"failures": []` verdict).

<status>complete</status>
<round>5</round>
<slot>~20</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
