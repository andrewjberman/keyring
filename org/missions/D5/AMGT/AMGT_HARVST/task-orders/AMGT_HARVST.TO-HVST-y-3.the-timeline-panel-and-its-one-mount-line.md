# AMGT_HARVST task order -- `HVST-y-3` -- ROUND 10 cell 3 of 3: the timeline PANEL, and ONE mount line in the page header

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-y-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~30</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on the portal paths below; this cell deploys nothing and pushes nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- the render runs against the harness/dev server over fixtures and the API module; no AWS call from this cell.
comp-adversary: RUN at L5 -- the adversary is a mount that quietly RE-ORDERS or REMOVES something in Andrew's header. AC3 is written as that adversary's test.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO VENDOR CALL. NO S3 WRITE OR DELETE. NO PROD PUSH.** Dev only.
2. ⛔ **DEV BUILDS USE PORT 5174 ONLY** (Andrew-direct 2026-09-24). Resolve `bun` via the profile; do not bake a
   path.
3. ⛔ **THIS CELL TOUCHES A PRODUCT FILE, so it is NOT the author-lands-on-DEV case.** Build and prove it; **do not
   push**. `1.0.0_SA_CTO` reviews it.
4. **Scripts in** `.../deliverables/0.9.0_WK_AMGT_HARVST~30/scripts/` -- **never `.scratch/`.**
5. ⛔ **INSTANCE NAMED EXACTLY**
   `.../deliverables/0.9.0_WK_AMGT_HARVST~30/AMGT_HARVST.TO-HVST-y-3.the-timeline-panel-and-its-one-mount-line.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-y-3.the-timeline-panel-and-its-one-mount-line`.

<paths>
portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~30/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. WHERE IT GOES, AND WHY IT IS NOT THE COVERAGE TAB

⛔ **READ THIS BEFORE THE SPEC, because the spec's placement lines were AMENDED under you.** The spec originally
said "the top of the Coverage tab." **`AMGT_RESAPP` RETIRED that tab into the header feed and deleted it** -- the
built page carries five tabs (`ExecManagement`, `Model`, `Peers`, `Posture`, `Thesis`) and no `CoverageTab.tsx`.
**Row `AMGT_HARVST-Z-S33`.**

**RULING** (`ledger/CTO_RULING_TIMELINE_PLACEMENT_20260928.md` @`277b0795ac`): **the timeline mounts in the PAGE
HEADER, directly above the company feed's article list** -- a **panel of the feed, not a tab**, because the feed is
the surface that now holds Coverage's content. Spec amended at `:21` and `:250` (@`325d43457f`). **FWD-5 itself is
NOT amended** -- its ENDPOINT never named a tab.

⚠ **`HeaderBrief.tsx` IS `AMGT_RESAPP`'s FILE.** The ruling authorises **ONE MOUNT SITE** there, as CTO of both
projects. **The component and its API wiring are ours; the mount line is the only edit to their file.** It
**re-orders nothing and removes nothing** in Andrew's header (description, Posture line, feed). **Any second edit
to that file is out of bounds -- file a row instead.**

## 2. WHAT TO BUILD

**A `TimelinePanel` component** over `w-3`'s existing server module
`lib/research/harvest/timeline_api.py` (`get_timeline`, `get_timeline_day`, `get_timeline_event`) -- **do not
modify that module; it is not in your `<paths>`.** Implement the spec's honest-state discipline, which is the
substance and is already ratified:

- **dense from `2026-01-01`, never a gap** -- a day with no coverage is a real zero row.
- **default measure `mention_score`**; the tier stack and `articles_total` toggles are optional this round.
- ⛔ **quiet-`COMPLETE`, `PARTIAL` and `DENIED` must NEVER share a visual encoding**, and `DENIED`'s height is the
  count of what retrieval was DENIED for, not what happened.
- ⛔ **A FAILED CALL IS NEVER RENDERED AS DATA and never as an empty series.** `w-3` already proved the envelope
  server-side (`error: true` + `error_code`, 9 of 9 injected failures); **your job is that the CLIENT honours it**
  -- a distinct page-level error state with a retry, never a blank or zero-height chart, because "we hold nothing"
  and "we do not know what we hold" are different facts.
- **Day click** opens that day's articles **strongest first** (tier A,B,C,D then `mention_count` desc then
  `published_utc`), each row showing headline, publisher, tier, and `mention_in_title`/`mention_in_lead`
  **present-even-when-false**.

## 3. BOUNDS

1. **Three mechanical criteria, no fourth.** The round's JUDGMENT criterion is on `HVST-y-1`, not here.
2. **One edit to `HeaderBrief.tsx`: the mount.** Nothing else.
3. **No new tab, no route change, no PROD push.**
4. **Do not modify `timeline_api.py` or any producer.** A defect there is a surprise ROW.

## 4. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical criteria

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-y-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~30/scripts/ac1_render_and_read.py</invocation><expect>THE PANEL RENDERS AND THE SCREENSHOT IS READ, not merely captured. Build/serve on PORT 5174 ONLY, render the security page for the validation security, capture the header region, and READ the image back: state what is visibly present -- the dense day line, its first and last day, and that the panel sits ABOVE the feed's article list. Print the rendered day count against the days-in-range denominator and show they are equal (no gap). A criterion that saves a PNG without reporting what it shows FAILS. If the render cannot run, say which step failed with its error text rather than substituting a component unit test</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-y-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~30/scripts/ac2_three_states_and_a_failed_call.py</invocation><expect>FOUR STATES, FOUR DISTINGUISHABLE RENDERS, proved over CONSTRUCTED inputs: quiet-COMPLETE (a real zero day), PARTIAL, DENIED, and A FAILED CALL. Print, for each, the encoding the client produces, and the PREDICATE that separates it from the other three -- quiet-COMPLETE vs PARTIAL vs DENIED must differ visually, and the failed call must reach NEITHER a blank chart NOR a zero-height line NOR an empty series. Show the error-envelope body (error:true + error_code) going in and the page-level error state with its retry coming out. 4 of 4 distinguishable or the criterion FAILS</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-y-3"><invocation>git -C . diff --stat HEAD -- portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx</invocation><expect>THE MOUNT ADDED AND REMOVED NOTHING ELSE IN ANDREW'S HEADER. The diffstat shows HeaderBrief.tsx with INSERTIONS ONLY and no deletions, and the inserted lines are the mount alone. Then print the full diff hunk and state in one line what each inserted line does. If any line is DELETED or MOVED, the criterion FAILS and it is a BLOCKING row -- the ruling authorises a mount, not a re-order, and the header's description, Posture line and feed are Andrew's word (AMGT_RESAPP_PRD.md:1891). Also state the harness result for the header: it still RENDERS (data-header-brief present)</expect></criterion>
</proof_of_spec>

## 5. WHAT THIS CELL DOES NOT DO

No vendor call, no S3 write, no PROD push, no new tab, no producer change. It does not grade FWD-5 -- it serves
it; the grade is `1.0.0_SA_CTO`'s at L10 and the judgment sits on `y-1`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **This cell existed as a BLOCKER for ~25 minutes and the order was drafted before the ruling arrived**, so it
   could issue the moment the placement was settled. The blocker was found by checking the paths a criterion would
   name -- `s.14x`'s run-it-first clause working on a surface, not a command.
2. **AC3 is a diffstat, not a script, on purpose.** The adversary is a well-meaning tidy-up of someone else's
   component. **Insertions-only is mechanically checkable; "I did not change anything else" is not.**
3. **`HeaderBrief.tsx`'s real path is `components/HeaderBrief.tsx`** -- the ruling wrote the bare filename, and the
   order names the measured path so the worker does not create a second file at the page root.
4. **AC1 demands the screenshot be READ.** A captured-but-unread PNG is the frontend equivalent of a green column
   over an empty denominator.

<risk>LOCAL</risk>
<status>pending</status>
<round>10</round>
<slot>~30</slot>
<fabric>site-z</fabric>
