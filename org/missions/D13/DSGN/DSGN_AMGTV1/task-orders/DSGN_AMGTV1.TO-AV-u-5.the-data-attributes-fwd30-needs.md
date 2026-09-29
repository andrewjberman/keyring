# DSGN_AMGTV1 task order -- `AV-u-5` -- THE DATA ATTRIBUTES FWD-30 NEEDS (AMGT_RESAPP r49's ASK)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-u-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~23</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 4f927ad0 -- attrs.cjs 0 of 3 (FAIL as expected: 0 sheet cells carry a value/year, the Base case no value/currency; no identity / description-reason / driver-series attribute; 0 of 12 absent columns carry their reason; no no-call reason attribute); green arm 3 of 3 (visible text unchanged against the base snapshot); bound 7 of 7 (PASS); vv-5.AC1 YES (PASS). Blind spot: static markup with the estate chrome stubbed; AMGT_RESAPP's own grade (round45/checks/sweep.py) reads AWS (lambda invoke), so it is NOT a criterion here -- the issuer runs it at the drain.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-u-5` (round 6, decomposition v6; serves FWD-11 and AMGT_RESAPP's FWD-30)

This is the SECOND order of your slot. The first (AV-u-2, Posture's words) is already committed on your branches by this slot;
build on top of it and do not change what it built.

AMGT_RESAPP's FWD-30 grade (`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/sweep.py`) now reads
this page ONLY through data attributes. Seven facts the page shows carry none (AMGT_RESAPP rows Z-W173-S1..S4), so the grade
matches them on identity, not value. Build ONE data attribute per fact carrying the served value or reason -- **no visible change**:
- M1 `tabs/ModelTab.tsx` `ModelCell`: `<td data-model-cell>` carries `data-model-cell="<the figure's served value, String(value)>"`
  and `data-model-year="<its fiscal_year>"`.
- M2 `ModelTab.tsx` `ModelCaseLine`: a SERVED case line carries `data-model-case-value="<String(served value)>"` and
  `data-model-case-currency="<the currency the line prints (caseCurrency), '' when none>"`.
- H1 `components/SecurityOverlay.tsx` `IdentityHeader`: the sector/country line carries `data-identity-sector`,
  `data-identity-country`, `data-identity-currency` (the served GICS_SECTOR_NAME, CNTRY_OF_DOMICILE, CRNCY header figures).
- H2 `components/HeaderBrief.tsx`: the ABSENT description `<p data-header-description="ABSENT">` carries
  `data-header-description-reason="<description.reason>"`.
- H3 `components/ThesisDriverChart.tsx`: the ABSENT chart `<div data-driver-chart="ABSENT">` carries
  `data-driver-chart-series="<chart.driver_series>"` (the key the export shares: it names the series).
- P1 `tabs/PeersTab.tsx`: each `<li data-absent-column>` carries `data-absent-column-reason="<column.reason>"`.
- P2 `tabs/PostureTab.tsx`: a no-call verdict `[data-posture-verdict="absent"]` carries `data-posture-reason="<posture.reason>"`.
Attribute values are the served values exactly as served (never reformatted); an attribute whose served value is absent is
omitted, never filled.

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
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
portal/src/pages/SecurityAnalysis/components/ThesisDriverChart.tsx
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~23/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round6/` (never edit them; the fixtures are the served payloads the checks render).
Also read-only: the AMGT_RESAPP rows Z-W173-S1..S4 in `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md`
and `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-5.AC1.sh` (AC3's check).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-u-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round6/checks/attrs.cjs"; echo "exit=$?"</invocation><expect>FWD-30 ATTRIBUTES: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-u-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round6/checks/bound.cjs" U5 modelPattern.harness.cjs:12 peersPattern.harness.cjs peersCarry.harness.cjs peersReadFailed.harness.cjs shell.harness.cjs:10 posture.harness.cjs:32 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>U5 BOUND: 7 of 7 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-u-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-5.AC1.sh"; echo "exit=$?"</invocation><expect>FWD-30 HARNESS READS THE REDESIGNED PAGE: YES -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 is the built behaviour: each attribute present AND equal to the served fixture value (SAP GY, Valero; two in-memory issuer variants -- an ABSENT description and a no-call posture -- because no served fixture carries either state), with each surface's visible text unchanged against the base snapshot; AC2 the bound on every harness that loads a file this cell touches; AC3 the page/export parity (the one further criterion this cell needs: it adds attributes the parity reader walks). No judgment criterion: nothing visible changes; AMGT_RESAPP grades the facts through its own sweep.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~23/DSGN_AMGTV1.TO-AV-u-5.the-data-attributes-fwd30-needs.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** AMGT_RESAPP r49 ask (msg 26753 from 2.0.0_SA_COO~Z; rows Z-W173-S1..S4), added to round 6 by the issuer. Queued LAST on slot ~23 because it writes PostureTab.tsx with AV-u-2; its other files are written by no other round-6 cell. sweep.py (merged @525e045932) reads AWS -- not an offline criterion; the issuer runs it at the drain. Base 4f927ad0: attrs 0 of 3; green 3 of 3 (six scratch sources, visible text unchanged); U5 bound 7 of 7; vv-5 YES.

<status>pending</status>
<round>6</round>
<slot>~23</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
