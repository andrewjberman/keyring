# DSGN_AMGTV1 task order -- `AV-t-4` -- DIRECT ACT: THE TABS HARNESS STUBS THE ESTATE DIALOG AND LOADS THE PAGE AGAIN

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-t-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~3</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN by the issuer -- AC1 reads 3 of 4 on the merged round-1 DEV 5fac7a37 (tabs rc=1, MODULE_NOT_FOUND on HeroGraphic; the other three green) and read 4 of 4 (tabs 20 of 20) at the round's base 8fa7abde, so it discriminates both ways. Blind spot: static markup only.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-t-4` (round 1, direct act; disarms row DSGN_AMGTV1-Z-W3-S1)

Your row W3-S1 named it: `portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs` (CHECKS-OK 20 of 20 at the
round's base) now dies at load with MODULE_NOT_FOUND, because its `STUBS` table (`:73` onward) has no entry for
`@/ui/components/graphic/HeroGraphic`, and the page reaches that module through `components/ThesisCards.tsx` (and
`components/HeaderCards.tsx`, which loads it lazily).

Build: add ONE `STUBS` entry for `'@/ui/components/graphic/HeroGraphic'` -- `HeroDialog` renders its children only when its
`open` prop is truthy (else nothing), `DialogStamp` renders nothing, and every other export the page's files import from that
module (read `ThesisCards.tsx` and `HeaderCards.tsx` for the names) is an inert stub -- so the harness loads the merged page
again. No check is removed, re-anchored or loosened; the 20 claims stay exactly as they are.

**AMENDMENT 1 (issuer, on your row W3-S2):** ONE check is re-anchored, and only it: `thesis_sentences_and_one_chart`
(`tabs.harness.cjs:314-319`) counted `data-drafted-sentence` markers on the Thesis tab's render, and AV-t-3 moved every
sentence into the card windows. Re-anchor it to the Thesis face PLUS each card window body (`ThesisCardDetail` from
`components/ThesisCards.tsx`, rendered statically for `investment_thesis`, `risks` and `recommendation`, as you did for the
drafting harness): the marker count over face + windows must equal each fixture's own sentence count (38, 35, 38, 36, 38),
and its `data-driver-chart` half stays exactly as it is. Its claim is unchanged; nothing else in the harness moves.

**Your worktree first:** it was cut from the round's base. Before you edit, bring it to the merged round:
`git -C /c/tmp/wk-dsgn-amgtv1-3 merge --no-edit CLOUD` (the outer repository; it carries this order) and
`git -C /c/tmp/wk-dsgn-amgtv1-3/portal merge --no-edit DEV` (the portal: the merged round-1 DEV, 5fac7a37 or later). Both are
merges, never a rebase. If either stops on a conflict, abort it and file a BLOCKING row.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy.
2. Only `tabs.harness.cjs` under `portal/` changes.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. When AC1 passes, append a DISARMED disposition for row `DSGN_AMGTV1-Z-W3-S1` to the channel file, naming this order and
   your portal commit.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~3/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, and the issuer's checks under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round1/checks/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-t-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round1/checks/bound.cjs" TABS tabs.harness.cjs:20 errorEmpty.harness.cjs:12 drafting.harness.cjs:8 thesisLadder.harness.cjs:10; echo "exit=$?"</invocation><expect>TABS BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1: on the merged round, the tabs harness reads 20 of 20 again and the three sibling harnesses stay green at their floors.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~3/DSGN_AMGTV1.TO-AV-t-4.the-tabs-harness-stubs-the-dialog.proof_of_spec.json`.
Report once: the stub you added, the AC1 output lines, the two merge results, the portal and outer commit hashes, and the row's disposition.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** decomposition ADDENDUM 1, ruling on row W3-S1 (issuer rules inside its own decomposition). Direct act: one
cell, ~20 lines, LOCAL -- no L2/L4-R/L8-L10 of its own; its close is the round's one real run. No round element: a
direct act stands outside round 1's single issuance (the NFRA_OPALAI OA-f-4..OA-f-8 addendum precedent, 2.0.0_SA_COO~AI).

<status>pending</status>
<slot>~3</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
