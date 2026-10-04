# DSGN_AMGTV1 task order -- `AV-zl-1` -- REPAIRS: NO LABEL CROSSES A MARK; A MOVE NAMES ITS WINDOW; A CHANGE PRINTS AT ITS PRECISION; THE AXIS MEETS THE INK LAW; ONE NAME FOR THE SUBJECT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zl-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~93</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks render page sources statically from fixtures captured on the deployed route.
comp-adversary: RUN by the issuer at the cut on portal PROD dbd29c6320 -- labels34.cjs 2 of 4, repairs34.cjs 1 of 4, peername34.cjs 3 of 4 (graded arms FAIL as expected; PLANTED arms pass). Each reads N of N with a scratch reference fix loaded through CHECK_SRC_OVERRIDE.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zl-1` (round 34, decomposition v34; a batched repair cell; serves FWD-21 and FWD-27)

The CTO graded rounds 29-33 on PROD and found five things still wrong. Repair all five in
`portal/src/pages/SecurityAnalysis/`. The checks (section 4) name every fault they find, by label text or row.

1. **No chatter label crosses another mark (FWD-21: "no label clips or overlaps").** `components/ChatterBubbles.tsx`, window
   mode (no `month` prop), at 30, 90 and 365 days on the served payloads. At base there are 34 collisions, for example the leader
   line of "Taiwan Semiconductor Manufacturing Co Ltd" running through "HERMES INTERNATIONAL". The placement code to fix:
   - `:278`: a placement stage lets a label sit over other circles (`overCircles: true`);
   - `:291-311`: a leader line is drawn without being tested against any label;
   - `:344-346`: the outside-placement test;
   - `:352-370`: the last-resort placement skips the circle test and falls back to the bubble centre (`:370`).
   Requirements:
   - No label box meets another label's box, or any bubble other than its own. A label inside its own bubble is fine.
   - No leader line crosses any label box except its own label's.
   - Every label box stays inside the SVG viewBox.
   - Keep the existing width estimate (0.6 x font-size per character) and keep the layout deterministic (no clock, no random).
   - A label that cannot be placed cleanly may drop. Its bubble keeps its hover, so the name stays readable on hover.
   **The full name on a shortened label:** the label text has `pointerEvents="none"` (`:561`), so a shortened label has no
   reachable full name. Give each label its own `<g>` carrying a `<title>` with the full served name, with pointer events
   reachable. Put the `<title>` on the label's `<g>`, NOT inside the `<text>`: round29's `collage.cjs` reads text inside
   `<text>` as the label and would fail.
   **Month mode** (a caller that hands `month`) keeps working for the round-29/30 checks that render it.
2. **The header's move names its window (FWD-27).** `components/SecurityOverlay.tsx`:
   - The breakout price reading prints a move such as "+6.65%" with no window, beside the Price face's "Change over the last 30
     days".
   - Print the served window in words: "+6.65% over the last 30 days". Read `window_days` from the same served axis read (`:372`;
     the move prints at `:479-481`).
   - A move whose window is not served prints no number.
3. **What changed prints its change at the row's display precision (FWD-27).** `components/model/WhatChangedPanel.tsx`
   (`moveSize` at `:145-153`, `movement` at `:157-168`):
   - The signed change prints at raw precision against rounded before/after values, for example `+0.1321` beside 2.90 -> 3.04,
     and `-USD 6.32B` beside 162B -> 156B.
   - Print each change with no digit finer than its row's before/after, in the same unit and format.
   - The percent move stays as it is.
4. **The timeline axis meets the ink law (FWD-27).** `components/TimelinePanel.tsx`:
   - `AXIS_TEXT_FILL = '#A8B0C0'` (`:188`, used at `:623`, `:631` and `:633`) is a band ink on the redesign's light panel:
     2.18:1 on #FFFFFF.
   - Use the panel's navy ink, an existing chart colour or token reaching at least 4.5:1 on the panel ground.
   - Keep round29 `timeline/chart.cjs` passing.
5. **One name for the subject in Peers (FWD-27 "one display name per security").** The Peers subject row prints the served
   `peers.subject.name` ("BOEING CO/THE (subject)"). The header and every other tab print the served overlay `display_name` ("The
   Boeing Co").
   - In `cscTable.ts`, `buildCscTable(peers, subjectName?)` labels the subject row with `subjectName` when it is a non-empty
     string, else with the served `peers.subject.name`.
   - In `tabs/PeersTab.tsx`, `CscBody` passes `overlay?.data?.display_name`, from the query the tab already makes.
   - The page rewrites no served text; it chooses which served name to print.

**Contracts:**
- C-PRESENTATION-ONLY: served values are formatted, never changed, and rounding is display precision.
- One purple action per view.
- No hard-coded colour outside `lib/chartColors.ts` tokens and the panel ink tokens the file already uses.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file. Keep each
   file's existing line endings.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/ChatterBubbles.tsx
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx
portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx
portal/src/pages/SecurityAnalysis/cscTable.ts
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~93/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zl-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round34/checks/collage/labels34.cjs"; echo "exit=$?"</invocation><expect>NO CHATTER LABEL CLIPS OR OVERLAPS: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zl-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round34/checks/repairs/repairs34.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round34/checks/names/peername34.cjs"; echo "exit=$?"</invocation><expect>ONE NAME FOR THE SUBJECT IN PEERS: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zl-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

AC2 runs repairs34.cjs first, and it must read "A MOVE NAMES ITS WINDOW, A CHANGE ITS PRECISION, THE AXIS ITS INK: 4 of 4 arms". The
KEEP arms inside these checks run the round-29/30/31/32 checks over the same files, and each must exit 0. battery29 now includes
the CI's ESLint step.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~93/DSGN_AMGTV1.TO-AV-zl-1.repairs-labels-windows-precision-ink-names.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W93-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Sources:**
  - CTO round-33 analysis section 3 (@ff31355b93);
  - the gap read (round34/walk/read-20261004T001928Z, GAP_READ.md) for item 5;
  - the check author's line map (repairs34 / labels34 at base).
- **Not graded here** (the issuer's close walk): how the collage reads with dropped labels; the header move's words in place; the
  navy axis on the panel.
- **The gap walk is the issuer's real run, not this cell** (decomposition v34). The six-state ui-smoke capture and FWD-24's
  positive control are still owed by the issuer.

<status>complete</status>
<round>34</round>
<slot>~93</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
