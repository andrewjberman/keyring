# DSGN_AMGTV1 task order -- `AV-v-5` -- EXEC "READ DETAIL" WITHOUT THE MACHINE REASON

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-v-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~21</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 09bd04b1 -- execdetail.cjs 2 of 3 (FAIL as expected: the served machine reason is visible, 17 of 17 windows, and on no attribute); green arm 3 of 3; bound 4 of 4 (PASS). Blind spot: static markup with the estate chrome stubbed.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-v-5` (round 5, decomposition v5; serves FWD-7, FWD-11)

Round 4 put Exec Management's "Read detail" drawer (`tabs/ExecManagementTab.tsx`) into words: on INTU it reads "Where we looked:
the company's 10-K, section 'Item 10. Directors, Executive Officers and Corporate Governance' (filing 0000896878-26-000037). The
section did not list officers in a form this page can read." -- and then appends the served machine reason verbatim: "no declared
shape read this section (4 usable line(s), 0 candidate(s)): neither a narrative entry per officer nor a Name/Age/Position or
Name/Year/Year table." (`management.reason ?? management.roster_reason`). The Bloomberg-fallback line on a served table does the
same with `roster_reason`.
Build: the served machine reason leaves the visible text and rides a data attribute on its element (e.g. `data-exec-reason` on the
drawer's paragraph; `data-exec-roster-reason` on the fallback line). The drawer keeps "Where we looked: ..." with the filing number
and "The section did not list officers in a form this page can read." The fallback line keeps its words ("This table is the
Bloomberg fallback: the filing roster did not resolve."). A served table (Valero) is unchanged.

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
2. Only the files in `<paths>` under `portal/` change; every other page, component, tab and harness is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/execPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execText.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~21/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-v-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/checks/execdetail.cjs"; echo "exit=$?"</invocation><expect>EXEC DETAIL WITHOUT THE MACHINE REASON: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-v-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/checks/bound.cjs" V5 execPattern.harness.cjs:9 execText.harness.cjs execFallback.harness.cjs tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>V5 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-v-5" judgment="true"/>
</proof_of_spec>

The mechanical criteria are the built behaviour on two served payloads (INTU absent, Valero resolved) and the bound. AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots, never self-graded: Exec Management's detail says where the officer list was looked for in words, with no machine reason on the face (FWD-7, FWD-11).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~21/DSGN_AMGTV1.TO-AV-v-5.exec-detail-without-the-machine-reason.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 5 = the round-4 analysis's enrichment list @177c576c80 section 4 item 5. Decomposition v5. Base 09bd04b1:
execdetail 2 of 3; green arm (scratch: reason to `data-exec-reason`, removed from the drawer's text) 3 of 3; V5 bound 4 of 4.
FWD-7's officer-from-a-second-source half is AMGT_RESAPP's producer ask (b) -- not this cell.

<status>complete</status>
<round>5</round>
<slot>~21</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
