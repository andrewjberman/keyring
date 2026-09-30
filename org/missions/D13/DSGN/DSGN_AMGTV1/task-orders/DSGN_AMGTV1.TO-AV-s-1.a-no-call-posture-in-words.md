# DSGN_AMGTV1 task order -- `AV-s-1` -- A NO-CALL POSTURE IS THE DESIGNED EMPTY STATE -- NEVER THE SERVED REASON

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-s-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~26</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV fd4deb75 -- absent.cjs 1 of 3 (FAIL as expected: the 992 HK header prints the served reason verbatim -- "comparable null: R-1 ... no landed model_block_992_HK_Equity.json (AMGT-s-1 ... F2/G-24)"; the tab prints "ABSENT"; no data-posture-reason-class; the VLO control passes); green arm (a scratch portal at fd4deb75 with the cell built) 3 of 3; bound U1 8 of 8 at base and on the green arm; vv-5.AC1 YES at base and on the green arm (after the exportCompare re-anchor below). Blind spot: static markup with the estate chrome stubbed.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-s-1` (round 7, decomposition v7; serves FWD-11)

The CTO's ruling (round-6 analysis, ruling 1): the page never prints a served posture reason verbatim when there is no call. On
992 HK (served `/thesis`, captured at the cut) the posture is `{status: "SERVED", verdict: "absent", comparable: null}` and its
`reason` is the producer's own prose -- a file name (`model_block_992_HK_Equity.json`), a project code (`AMGT-s-1`) and ruling ids
(`F2/G-24`); the header's posture line prints it whole. Build -- a posture with NO CALL (status `ABSENT`, or `SERVED` with verdict
`"absent"`) reads, on the Posture tab AND in the header's one posture line, as the estate's designed empty state
**"No call on this name yet"** plus ONE plain reason class taken from the served STATUS only, carried on
`data-posture-reason-class`:
- `not-drafted` -- status `ABSENT` ("no posture has been drafted for this name yet; the research team adds one");
- `no-comparable` -- `SERVED`, verdict `absent`, `comparable` null ("no comparable company could be matched to this name yet");
- `no-call-made` -- `SERVED`, verdict `absent`, a comparable served ("the evidence did not support a call against the comparable").
The served `reason` rides `data-posture-reason` (tab AND header line), never visible text; no "ABSENT" word on the face (the tab's
large verdict word reads e.g. "NO CALL"). A posture that makes a call (better / worse / hold / steer_clear) is unchanged.
Surfaces: `tabs/PostureTab.tsx` (the ABSENT branch -- `PanelEmpty` with the words -- and the served verdict tile when verdict is
`absent`), `components/SecurityOverlay.tsx` `PostureHeaderLine` (the live header line) and `components/LeadPanel.tsx`'s exported
`PostureHeaderLine` (the copy the page harnesses read; keep the two identical in behaviour).
**Put the small class helper INSIDE each of the three files (restated per file, as this page already restates the posture
sentence) -- NOT in a new shared module: `errorEmpty.harness.cjs`'s loader cannot resolve a new sibling module** (measured at the
cut: "Cannot find module"), and that harness is not yours to edit.

**Two harness checks this change NECESSARILY moves (both granted in `<paths>`; re-anchor exactly these, claims unchanged):**
1. `__harness__/posture.harness.cjs` `absent_arm_explicit` (`refusedOk`, ~line 505): it looks for the visible
   "ABSENT -- no call was made: <reason>" in the tab and the header. Re-anchor onto: visible "No call on this name yet" AND
   `data-posture-reason="<the same reason>"` in the tab and in the header, keeping the claim-count-0 and `data-header-posture="SERVED"`
   conditions. Floor 32.
2. `__harness__/exportCompare.harness.cjs` `pageAbsences` (~line 358): its regex requires `data-posture-reason` to be the LAST
   attribute of `<div data-posture-status="ABSENT" ...>` and keys a second absence on the visible "Nothing is rendered in its
   place.". Re-anchor: read the ABSENT block with its attributes in any order, key `ABSENT: <reason>` from `data-posture-reason`,
   and key the export's own `<reason>. Nothing is rendered in its place.` from `data-posture-reason-class="not-drafted"` (the same
   fact, never page prose); the matching `scan.replace` likewise. AC3 must still read all four sets exact.

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
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/__harness__/posture.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~26/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round7/` (never edit them; the fixtures are the served payloads the checks render).
Also read-only: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-5.AC1.sh` (the parity criterion).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-s-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round7/checks/absent.cjs"; echo "exit=$?"</invocation><expect>NO-CALL POSTURE IN WORDS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-s-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round7/checks/bound.cjs" U1 posture.harness.cjs:32 posturePattern.harness.cjs:13 peersPattern.harness.cjs:13 peersCarry.harness.cjs peersReadFailed.harness.cjs tabs.harness.cjs:20 errorEmpty.harness.cjs:12 leadPanelPattern.harness.cjs:15; echo "exit=$?"</invocation><expect>U1 BOUND: 8 of 8 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-s-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-5.AC1.sh"; echo "exit=$?"</invocation><expect>FWD-30 HARNESS READS THE REDESIGNED PAGE: YES -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-s-1" judgment="true"/>
</proof_of_spec>

AC1 is the built behaviour on the served 992 HK posture (the positive control: its reason must never be visible), an ABSENT issuer variant, and the VLO call as the control; AC2 the bound on every harness that loads the three files; AC3 the page/export parity (the one further criterion this cell needs: it re-anchors that harness). AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots (992 HK), never self-graded: a name with no call reads as a designed empty state in words, with no file name, code or id on the face (FWD-11). Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/` (`tsc -p .` lists no files and checks nothing).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~26/DSGN_AMGTV1.TO-AV-s-1.a-no-call-posture-in-words.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 7 = the round-6 analysis s.4 item 1 with ruling 1 @378fd0c04b (CTO msg 26790). Base fd4deb75: absent.cjs 1 of 3.

<status>pending</status>
<round>7</round>
<slot>~26</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
