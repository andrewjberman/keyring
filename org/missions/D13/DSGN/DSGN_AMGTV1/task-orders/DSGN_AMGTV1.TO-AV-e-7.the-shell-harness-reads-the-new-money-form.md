# DSGN_AMGTV1 task order -- `AV-e-7` -- DIRECT ACT: THE SHELL HARNESS READS THE MONEY FORM THE PAGE NOW PRINTS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-e-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~6</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN by the issuer -- AC1 reads 2 of 3 on the merged round-2 DEV 1a1e8162 (shell 9 of 10: card_window_carries_provenance false) and read 3 of 3 (shell 10 of 10) at the round's base f1a90a9b, so it discriminates both ways. Blind spot: static markup only.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-e-7` (round 2, direct act, decomposition v2 ADDENDUM 2)

Your AV-e-3 is right: every money figure in the header now prints its own served currency code, then the amount. But
`portal/src/pages/SecurityAnalysis/__harness__/shell.harness.cjs` (10 of 10 at the round's base) still anchors one check on
the old form: `card_window_carries_provenance` (`:295-299`) renders `HeaderCardDetail({ cardKey: 'price', bundle: baseOverlay })`
and requires `priceWindow.includes('>$162B<')` beside `data-card-figure-mnemonic="CUR_MKT_CAP"`. It now reads false (9 of
10). This is the issuer's cut defect -- AV-e-3's bound did not name this harness -- not yours.

Build: re-anchor that ONE check onto the money form the page now prints for the fixture's market cap -- its served currency
code then the amount (e.g. `>USD 162B<`), or the amount and "currency not stated" if the fixture's figure carries no
currency (read the fixture the harness loads; do not guess). Keep its claim: the price window carries the mnemonic in an
attribute and the value formatted for reading. Nothing else in the harness moves.

**Your worktree first:** it holds AV-e-3 on the round's base. Bring it to the merged round before you edit:
`git -C /c/tmp/wk-dsgn-amgtv1-6 merge --no-edit CLOUD` (the outer repository; it carries this order) and
`git -C /c/tmp/wk-dsgn-amgtv1-6/portal merge --no-edit DEV` (site-Z portal DEV, 1a1e8162 or later). Both are merges, never a
rebase. If either stops on a conflict, abort it and file a BLOCKING row.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy.
2. Only `shell.harness.cjs` under `portal/` changes.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/__harness__/shell.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~6/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, and the issuer's checks under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/checks/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-e-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round2/checks/bound.cjs" SHELL shell.harness.cjs:10 errorEmpty.harness.cjs:12 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>SHELL BOUND: 3 of 3 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1: on the merged round, the shell harness reads 10 of 10 again and the two sibling harnesses stay green at their floors.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~6/DSGN_AMGTV1.TO-AV-e-7.the-shell-harness-reads-the-new-money-form.proof_of_spec.json`.
Report once: the re-anchor (old -> new), the AC1 output lines, the two merge results, the portal and outer commit hashes.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** decomposition v2 ADDENDUM 2 (issuer rules inside its own decomposition). Direct act, no round element (the
AV-t-4 / NFRA_OPALAI OA-f-* precedent: a direct act stands outside the round's single issuance). Base (DEV 1a1e8162): AC1
2 of 3 (FAIL as expected).

<status>complete</status>
<slot>~6</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
