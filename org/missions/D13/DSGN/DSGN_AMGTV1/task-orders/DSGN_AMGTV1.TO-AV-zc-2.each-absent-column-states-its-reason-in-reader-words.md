# DSGN_AMGTV1 task order -- `AV-zc-2` -- EACH ABSENT COLUMN STATES ITS REASON IN READER WORDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zc-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~75</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal 41eeda55 -- reasonclass.cjs 1 of 3 (FAIL as expected: every item reads the bare "is not available for these peers", no data-absent-reason-class; arm 3 PASS by design).
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-zc-2` (round 25, decomposition v25; serves FWD-16 and FWD-8)

DIRECT ACT. The CTO's round-23 analysis (`org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round23.md` @876dfcadb8, ruling 1;
read it): the Peers "Absent columns (N)" disclosure gives EACH column its REASON in reader words -- one plain clause per reason class
-- because "<Column> is not available for these peers" states the absence without the reason. FWD-8 still forbids system vocabulary.

Today (`portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx`, the disclosure `<li data-absent-column=... data-absent-column-reason=...>`)
every item reads "<label> is not available for these peers." R-1's served reasons (`peers.csc_columns.absent[].reason`) are one global
map -- the same 11 reasons over 12 columns for every name:
- "no share-count factor code and no share-count row field" (Shares)
- "the solvency category carries only RATIOS, never an absolute debt level" (Debt)
- "no preferred-equity code among the 289 registry factors" (Preferred)
- "no minority-interest code among the 289 registry factors" (Minority)
- "cash_mv is 'Cash to Market Value', a ratio; no absolute cash level" (Cash)
- "the value category carries trailing (ey) and NTM (ey_ntm) only -- no second-forward-year estimate at any grain" (P/E 2027)
- "the registry names 'leverage' only 'Leverage' (category solvency) and states no numerator or denominator, so reading it AS
  debt/equity would be inferred, not measured; debt_assets is debt to ASSETS" (Debt/Equity)
- "no net-debt code among the 289 registry factors" (Net Debt/Equity, Net Debt/Capital)
- "the growth category tops out at a THREE-year window" (5-yr growth Revenue)
- "no EBIT growth code at any window (ebitev is a yield, ebit_est_rev_45d an estimate revision)" (5-yr growth EBIT)
- "no FCF growth code at any window (fcfy / fcf_ev are yields)" (5-yr growth FCF)
Build, in the page (a small class table keyed by the served reason, in `reasonWords.ts` or `PeersTab.tsx`):
1. each served reason maps to a CLASS and each class to ONE plain reader clause that gives the REASON, e.g.
   "the data source does not report <thing> for these peers", "only a ratio is reported, not the amount", "estimates go out one year
   only", "growth is reported over at most three years", "the source's leverage measure is not defined as debt to equity";
2. each item reads "<label>: <clause>" (or "<label> -- <clause>"), carries `data-absent-reason-class="<class>"`, and keeps
   `data-absent-column-reason` (the served reason);
3. a served reason with no class renders class `unmapped` and a generic plain clause (e.g. "the data source does not report this for
   these peers") -- never a code;
4. no clause says "factor code", "row field", "registry", "comparison map", "R-1", a field code, or a capitals word (EBIT is fine).
Do not rewrite the served reason string itself; it stays in the attribute. Presentation only.
Do not edit `tabs/ModelTab.tsx`, `tabs/ExecManagementTab.tsx` or `__harness__/posture.harness.cjs`.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- a reader clause composed from a served reason's class
is presentation. **Design law (portal `DESIGN.md`):** a code may sit in a data attribute, never in visible text; no light ink on white.

**Harness changes:** a peers harness listed in `<paths>` may be RE-ANCHORED where it asserts the old visible words -- never a deleted
check, never a weakened expectation.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/reasonWords.ts
portal/src/pages/SecurityAnalysis/__harness__/peersPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/peersCarry.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/peersReadFailed.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~75/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round24/`,
`round23/`, `round22/` and `round15/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zc-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round24/checks/reasonclass.cjs"; echo "exit=$?"</invocation><expect>EACH ABSENT COLUMN STATES ITS REASON IN READER WORDS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zc-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round23/checks/peerwords.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round22/checks/codeface.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round22/checks/subjectrow.cjs" &amp;&amp; cd portal &amp;&amp; node node_modules/typescript/bin/tsc -b --noEmit &amp;&amp; cd .. &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" ALL leadPanelPattern.harness.cjs errorEmpty.harness.cjs tabs.harness.cjs shell.harness.cjs drafting.harness.cjs execFallback.harness.cjs execPattern.harness.cjs execText.harness.cjs peersCarry.harness.cjs peersPattern.harness.cjs peersReadFailed.harness.cjs modelPattern.harness.cjs posturePattern.harness.cjs thesisLadder.harness.cjs; echo "exit=$?"</invocation><expect>THE PEERS ABSENT-COLUMN REASONS ARE IN READER WORDS: 3 of 3 arms, then NO CODE ON THE EXEC, POSTURE OR PEERS FACE: 3 of 3 arms, then THE PEERS SUBJECT ROW CARRIES THE HEADER'S PRICE AND EV: 3 of 3 arms, then tsc rc 0 (no output), then ALL BOUND: 14 of 14 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 renders PeersTab over five captured payloads: arm 1 every absent column has a classed reader clause, one clause per class, 0
unmapped, no bare "not available", no system term or code; arm 2 an unknown served reason renders `unmapped` with a plain clause;
arm 3 the comparator rejects a bare clause, a registry clause and two clauses for one class. AC2 keeps rounds 22-23 and all 14.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~75/DSGN_AMGTV1.TO-AV-zc-2.each-absent-column-states-its-reason-in-reader-words.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W75-S<k>`, and its `surfaced_at` is the real UTC time.
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (LOCAL). CTO round-23 analysis @876dfcadb8 row 1. Chain ~75 alone. Base reasonclass 1 of 3 on 41eeda55.

<status>complete</status>
<round>25</round>
<slot>~75</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker</worker_class>
