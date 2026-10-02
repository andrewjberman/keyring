# DSGN_AMGTV1 task order -- `AV-zb-1` -- THE PEERS ABSENT-COLUMN REASONS ARE IN READER WORDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zb-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~71</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV a730d8ce (= 419ef41d for src/pages/SecurityAnalysis) -- peerwords.cjs 2 of 3 (FAIL as expected: 19 system terms per fixture; RATIOS and THREE in reasons; arms 2-3 PASS by design); bound 14/14 and tsc rc 0 (controls PASS). Blind spot: HelperTip content is not in a static render; the issuer's close walk hovers nothing, so the tips are graded by reading the source.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-zb-1` (round 23, decomposition v23; serves FWD-8)

DIRECT ACT. The CTO's round-22 analysis (`org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round22.md` @eee9380be7, ruling 1;
read it): the Peers face never says "factor code", "row field", "registry", "289 registry factors", "comparison map", "R-1" or a
category in capitals ("RATIOS", "THREE-year"). Each absent column's reason says what the reader is missing and why, in ONE plain
clause, e.g. "Shares outstanding is not reported for these peers."

Where the words come from (measured at the cut, all under `portal/src/pages/SecurityAnalysis/`):
1. `tabs/PeersTab.tsx`, the "Absent columns" disclosure: each `<li data-absent-column=...>` prints
   `{column}: not in the comparison map -- {guardedReason(served reason)}`. The served reasons are R-1's words
   (`peers.csc_columns.absent[].reason`: "no share-count factor code and no share-count row field", "the solvency category carries
   only RATIOS, never an absolute debt level", "no preferred-equity code among the 289 registry factors" ...). Do NOT rewrite a
   served reason on the page (a served string is fixed at its producer). Instead the item's VISIBLE text is one plain clause the
   page composes from the column's label, for example "Shares outstanding is not reported for these peers" or "<label> is not
   available for these peers". The served reason stays in `data-absent-column-reason` (it is there today; keep it).
2. `tabs/PeersTab.tsx`, the counts line under the table ("... absent of 17 declared column(s) in the comparison map; ... carry a
   per-member value ..."): say it without "comparison map" (for example "5 of 17 columns are shown; 12 are not available for
   these peers").
3. The column-head tips: `NOT_CARRIED_FALLBACK` ("This column is in the factor registry, ...") and any tip text built from
   `cscTable.ts` reasons must not say "registry", "R-1" or "factor code".
Keep: the column count, one item per absent column, AV-z-1's guard, and the subject row. Presentation only; no served value moves.
Do not edit `tabs/ModelTab.tsx`, `tabs/ExecManagementTab.tsx` or any harness not in `<paths>`.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served (words
composed from a served column label are presentation). **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour law):** a code
or field name may sit in a data attribute, never in visible text; no light ink on a white panel. The shared Friday CONTRACT:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md`.

**Harness changes:** a peers harness listed in `<paths>` may be RE-ANCHORED where it asserts the old visible words -- never a deleted
check, never a weakened expectation.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c` (a heredoc turns a regex `\b` into a 0x08 byte).

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/cscTable.ts
portal/src/pages/SecurityAnalysis/__harness__/peersPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/peersCarry.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/peersReadFailed.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~71/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round23/`,
`round22/` and `round15/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zb-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round23/checks/peerwords.cjs"; echo "exit=$?"</invocation><expect>THE PEERS ABSENT-COLUMN REASONS ARE IN READER WORDS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zb-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round22/checks/codeface.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round22/checks/subjectrow.cjs" &amp;&amp; cd portal &amp;&amp; node node_modules/typescript/bin/tsc -b --noEmit &amp;&amp; cd .. &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" ALL leadPanelPattern.harness.cjs errorEmpty.harness.cjs tabs.harness.cjs shell.harness.cjs drafting.harness.cjs execFallback.harness.cjs execPattern.harness.cjs execText.harness.cjs peersCarry.harness.cjs peersPattern.harness.cjs peersReadFailed.harness.cjs modelPattern.harness.cjs posturePattern.harness.cjs thesisLadder.harness.cjs; echo "exit=$?"</invocation><expect>NO CODE ON THE EXEC, POSTURE OR PEERS FACE: 3 of 3 arms, then THE PEERS SUBJECT ROW CARRIES THE HEADER'S PRICE AND EV: 3 of 3 arms, then tsc rc 0 (no output), then ALL BOUND: 14 of 14 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 renders PeersTab over five captured payloads: arm 1 reads 0 system terms on the face and 0 capitals in a reason clause, with
one item and a reason clause per absent column; arm 2 proves the census catches each phrase; arm 3 proves each item still carries
the served reason in `data-absent-column-reason`. AC2 keeps round 22's outcomes, the TYPECHECK and all 14 page harnesses.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~71/DSGN_AMGTV1.TO-AV-zb-1.peers-absent-column-reasons-in-reader-words.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W71-S<k>`.
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (LOCAL). CTO round-22 analysis @eee9380be7 row 1. Chain ~71 alone. Base peerwords 2 of 3 on DEV a730d8ce.

<status>complete</status>
<round>23</round>
<slot>~71</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker</worker_class>
