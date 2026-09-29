# DSGN_AMGTV1 task order -- `AV-r-3` -- FWD-30'S PAGE/EXPORT PARITY HARNESS KEYS ON DATA AND READS THE CARD WINDOWS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-r-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~11</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 670f29e4 -- AC1 NO (FAIL as expected: ABSENCES page 7 vs export 17, CITES page 0); AC2 YES (PASS: the control, deleting one counted export absence moves the export 17 -> 16 and the harness fails). No scratch green arm was fed this round. Blind spot: static markup with the estate chrome stubbed; bands, contrast and layout are the walk's (the judgment criterion).
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AV-r-3` (round 3, decomposition v3; serves FWD-30 parity (W4-S1 (a)))

`portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs` is FWD-30's instrument (AMGT_RESAPP PRD: the page and the rich
export carry "the SAME figures, the SAME cites and the SAME absences, with NOTHING in the export that is not on the page"). On
the current page it reads ABSENCES page 7 vs export 17 (missing 2, extra 12), because DSGN_AMGTV1 round 2 words the Model tab's
refused lines and case formula while the export prints them verbatim, and CITES page 0, because the harness never renders the
click-open card windows where the cites now live (AMGT_RESAPP row Z-S297). 1.0.0_SA_CTO~Z ruled (W4-S1 (a), @06d51bce50):
parity compares DATA, not label wording.

Build, in `exportCompare.harness.cjs` only:
1. The page side of ABSENCES and CASES keys on the data the page carries -- `data-model-line-refusal` (a refused line's served
   reason), `data-model-case-formula` (a case's served formula), `data-model-row` (the line identity) -- not on the page's
   words; the export side is unchanged.
2. The page side of CITES renders each Thesis card's window body (`ThesisCardDetail` from `components/ThesisCards.tsx`, for
   `investment_thesis`, `risks` and `recommendation`, as `drafting.harness.cjs` does) so the cites inside the windows are read.
3. Nothing drops out of a compared set to reach parity, and no export figure, cite or absence is dropped; a real difference
   must still fail (AC2 proves it on a deleted export absence).

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: no figure is computed,
converted or guessed, no name is looked up or joined, and a value the payload does not carry reads as a designed empty state
naming, in plain words, what is missing and which team fills it -- never a project code, serial or storage path.
C-ESTATE-FIXTURES -- windows are the estate's HeroDialog + DialogStamp, panels and states are the estate's; nothing forked.
**Design law (portal `DESIGN.md`):** white panels with navy ink (C3); ONE dark band per page; no translucent white (C5.8); no
shadow (C11). A code or path may sit in a data attribute or in code, never in visible text.

**If a bound harness check is anchored on the raw text this cell removes,** re-anchor that ONE check onto the same fact as the
page now states it (the words, or a data attribute), keep its claim, never drop it; the harness keeps at least its base
check count (the floor in the bound criterion). Record each re-anchor (old anchor -> new) in the instance.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` under `portal/` change; every other page, component, tab and harness is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~11/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx`, `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx`, `portal/src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs` (the window-render pattern), AMGT_RESAPP's fixtures under `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/fixtures/` and its check `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-5.AC1.sh` (never edit them), `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round3/` (never edit them; the fixtures are the served payloads the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-r-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-5.AC1.sh"; echo "exit=$?"</invocation><expect>FWD-30 HARNESS READS THE REDESIGNED PAGE: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-r-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round3/checks/parity-ctl.sh"; echo "exit=$?"</invocation><expect>PARITY CONTROL: a deleted export absence is caught: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-r-3" judgment="true"/>
</proof_of_spec>

The mechanical criteria are the built behaviour on the served payloads and the bound (the page harnesses that load this
surface stay green at their base check counts). AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in
walk screenshots, never self-graded: the harness now reads the page's data and its card windows, and a real difference still fails it (FWD-30's instrument, read by the CVO against its own ACCEPT).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~11/DSGN_AMGTV1.TO-AV-r-3.the-parity-harness-keys-on-data.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 3 = the round-2 analysis's enrichment list @172d3d9600 section 4 (CTO msg 26551) + ruling @06d51bce50. Decomposition v3.
Base 670f29e4: AC1 NO (FAIL as expected: ABSENCES page 7 vs export 17, CITES page 0); AC2 YES (PASS: the control, deleting one counted export absence moves the export 17 -> 16 and the harness fails).

<status>complete</status>
<round>3</round>
<slot>~11</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
