# DSGN_AMGTV1 task order -- `AV-zb-2` -- THE EXEC FACE NAMES THE FILING, NEVER ITS ACCESSION NUMBER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zb-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~72</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check renders page sources statically from a fixture.
comp-adversary: RUN by the issuer at the cut on portal DEV a730d8ce (= 419ef41d for src/pages/SecurityAnalysis) -- accession.cjs 1 of 3 (FAIL as expected: the accession is on the face, no 10-K or date, no attribute on the served branch; arm 3 PASS by design); bound 14/14 and tsc rc 0 (controls PASS). Blind spot: the fixture is BA; the issuer's close walk reads VLO's Exec face.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-zb-2` (round 23, decomposition v23; serves FWD-11)

DIRECT ACT. The CTO's round-22 analysis (`org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round22.md` @eee9380be7, ruling 2;
read it): the SEC accession number is an id and comes off the visible face. The face names the filing in words -- its form and
filing date -- as the Thesis citations already do ("VLO US's 10-K, filed February 25th, 2026"); the accession rides a `data-`
attribute (or a link target).

Where it prints (measured at the cut, `portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx`):
- the officers line (~line 269-273): `{n} officer(s) from {source_item}, filing {filingNumber(source_accession)}, as of {date}`
  (on VLO: "5 OFFICER(S) FROM ITEM 10. ..., FILING 0001628280-26-011499, AS OF SEPTEMBER 18TH, 2026");
- the no-officers branch's "Read detail" paragraph (~line 254-257): `... (filing ${filingNumber(...)})`.
The served form and date: the thesis bundle (`useThesisBundle(securityKey)`, the hook this tab already calls) carries
`drafting_provenance` = {accession, form, filing_date}. Use its form and filing date ONLY when `drafting_provenance.accession` equals
`management.source_accession`; then the line names the filing as, for example, "from the 10-K filed January 30th, 2026" (dates in the
page's own long form, `longStamp` in `dateWords.ts`). When they differ (or either is missing) name the filing without a form or date
("from the company's filing"): never borrow a date from another filing. In every case put the accession in a `data-` attribute on
the line (e.g. `data-exec-source-accession`), never in its text. Presentation only; no fetch change.
Do not edit `tabs/ModelTab.tsx`, `tabs/PeersTab.tsx` or any harness not in `<paths>`.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served.
C-FRIDAY -- the page never constructs a date; it prints a served date. **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour
law):** an id may sit in a data attribute, never in visible text; no light ink on a white panel. The shared Friday CONTRACT:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md`.

**Harness changes:** an exec harness listed in `<paths>` may be RE-ANCHORED where it asserts the old filing words -- never a deleted
check, never a weakened expectation.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/execPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execText.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~72/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round23/`,
`round22/` and `round15/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zb-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round23/checks/accession.cjs"; echo "exit=$?"</invocation><expect>THE EXEC FACE NAMES THE FILING, NOT ITS ACCESSION: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zb-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round22/checks/codeface.cjs" &amp;&amp; cd portal &amp;&amp; node node_modules/typescript/bin/tsc -b --noEmit &amp;&amp; cd .. &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" ALL leadPanelPattern.harness.cjs errorEmpty.harness.cjs tabs.harness.cjs shell.harness.cjs drafting.harness.cjs execFallback.harness.cjs execPattern.harness.cjs execText.harness.cjs peersCarry.harness.cjs peersPattern.harness.cjs peersReadFailed.harness.cjs modelPattern.harness.cjs posturePattern.harness.cjs thesisLadder.harness.cjs; echo "exit=$?"</invocation><expect>NO CODE ON THE EXEC, POSTURE OR PEERS FACE: 3 of 3 arms, then tsc rc 0 (no output), then ALL BOUND: 14 of 14 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 renders ExecManagementTab over the BA fixture: arm 1 (served match) 0 accession digits on the face, "10-K" and "January 30th,
2026" shown, the accession in a data- attribute; arm 2 (another filing's provenance) no accession, no borrowed date, the attribute
kept; arm 3 the census catches a dashed accession and an 18-digit run. AC2 keeps round 22's Exec outcome, the TYPECHECK and all 14.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~72/DSGN_AMGTV1.TO-AV-zb-2.the-exec-face-names-the-filing-not-its-accession.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W72-S<k>`.
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (LOCAL). CTO round-22 analysis @eee9380be7 row 2. Chain ~72 alone. Base accession 1 of 3 on DEV a730d8ce.

<status>pending</status>
<round>23</round>
<slot>~72</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
