# AMGT_RESAPP task order -- `AMGT-cb-3` -- THE ROUND-121 SECURITY ANALYSIS FEATURE (THE THREE-STATE CEO PROFILE) IS MERGED FORWARD ONTO DEV, PROMOTED TO PROD AS ONE CHOSEN-SET RELEASE, THEN PROD IS FOLDED BACK INTO DEV UNDER THE CTO'S NAMED WAIVER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-cb-3</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DT_ClientPlatform~H2</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-cb-3.feature-merged-forward-promoted-to-prod-then-folded-back</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one merge-forward, one promote and one fold-back; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- git push of DEV and PROD in the portal repository under the DT's standing grant (a DT serial may push PROD or DEV in Opal-Capital/portal); no AWS call.
comp-adversary: RUN at the cut (2026-10-18 ~17:3xZ) -- `python .tools/open-calls.py approval-status --branch cand/dell1/amgt-sa-ceo-three-states` reads `state=APPROVED valid=yes row=dell1-20261018T171501Z-a713 by=1.0.0_SA_CTO~DELL1 head_sha=43762e0d999d3b67a7a955dc16ac638bbfcdea88 commits=1` (the CTO's msg 8168, approval record addendum 10 @810925204e); PROD is `ff611566` (portal-v2.1.240), DEV `3a7791c1`, `origin/DEV..origin/PROD` reads 0. AC1 at the base reads `DIFFERS` on all 7 paths (PROD does not carry the feature), AC2 reads the PROD head `ff611566`, which the criterion refuses, AC3 reads a missing receipt, and AC4's guard (`PROD != ff611566`) fails and prints nothing at the base: each FAILS at the base as expected. EGRESS CLASS, declared: git fetch and push of the feature branch, DEV (the approved merge-forward route only) and PROD in Opal-Capital/portal, the CI read; no other egress.
</preflight>

## 1. THE CELL -- `AMGT-cb-3` (round 121, decomposition s.130)

The box CTO approved the approval row (class Opal-internal: `/security-analysis` is staff-only; msg 8168, record `org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_APPROVAL_DEV_BP1_BP4_SECURITY_ANALYSIS_20261017.md` addendum 10 @810925204e: it covers the DEV merge-forward AND this PROD promote, then the byte tie and the fold-back under a named waiver). The ONE feature, a candidate cut from PROD `ff611566`: `cand/dell1/amgt-sa-ceo-three-states` (head `43762e0d999d3b67a7a955dc16ac638bbfcdea88`, ONE commit, 7 paths, every path under `src/pages/SecurityAnalysis/`: `tabs/ExecManagementTab.tsx`, `types.ts`, the harness `__harness__/threeStateCeoProfile.harness.cjs`, the census `__harness__/ceoConsumerCensus.json` and three served-object fixtures): the Exec Management tab prints a sentence of its own for a never-written profile (`NOT_WRITTEN`) and for a failed read (`UNREADABLE_OBJECT`), keeps the searched sentence, and an unknown or absent reading prints a third sentence. The branch exists LOCALLY in the nested portal repository at `C:/dev/ajb_workspace/portal` (the issuer built it through a worker's linked worktree; it is not on origin yet). The issuer cannot push DEV or the portal's branches (the push hook admits a DT or the integrator only). Do, in order:
1. **Confirm the approval.** `python .tools/open-calls.py approval-status --branch cand/dell1/amgt-sa-ceo-three-states` from `C:/dev/ajb_workspace` must read `state=APPROVED valid=yes` with `head_sha=43762e0d999d3b67a7a955dc16ac638bbfcdea88`; and `git -C C:/dev/ajb_workspace/portal rev-parse cand/dell1/amgt-sa-ceo-three-states` must read `43762e0d999d3b67a7a955dc16ac638bbfcdea88`. Otherwise STOP and report: do not push, do not build, do not promote.
2. **Push the feature branch** (the contributing flow's step 3): `git -C C:/dev/ajb_workspace/portal push origin cand/dell1/amgt-sa-ceo-three-states`; print `git -C C:/dev/ajb_workspace/portal ls-remote origin refs/heads/cand/dell1/amgt-sa-ceo-three-states` (it must read `43762e0d999d3b67a7a955dc16ac638bbfcdea88`).
3. **The merge-forward onto DEV, by the one approved route only.** `git -C C:/dev/ajb_workspace/portal fetch origin DEV PROD -q`; print `git -C C:/dev/ajb_workspace/portal rev-parse origin/DEV` (read `3a7791c1` at the cut: a different value means DEV moved; name it in the receipt and go on only if the register and the script accept) and then, from the workspace root `C:/dev/ajb_workspace`, `bash .tools/portal-merge-forward.sh cand/dell1/amgt-sa-ceo-three-states --push`. Print its result line (it ends with `merge=<sha>`; `merge=-` is a REFUSAL: STOP, file a BLOCKING row naming the refusal token, and do not go on). After a fetch print `git -C C:/dev/ajb_workspace/portal merge-base --is-ancestor 43762e0d999d3b67a7a955dc16ac638bbfcdea88 origin/DEV && echo IN-DEV` and `git -C C:/dev/ajb_workspace/portal ls-remote origin DEV`.
4. In the portal repository, from the workspace root, run `bash .tools/portal-release-build.sh --features cand/dell1/amgt-sa-ceo-three-states`. It refuses the whole release on any of its pinned tokens (not-approved, stale-head, commits-differ, unapproved-commits, ...): if it refuses, STOP, file a BLOCKING row naming the token, and do not promote. If its `PROMOTE-CLIENT-FACING` line reads a count above zero, STOP: the set holds a client-facing page and waits on Andrew's word.
5. Promote the release with `/prod-deploy`. The release carries exactly this ONE feature and no other candidate; your receipt names `/security-analysis` as Opal-internal. The PROD head may have moved since the cut (other seats promote too): build on the PROD head you read, and name any deviation from this order's numbers in the receipt.
6. Read the CI conclusion on the PROD head (`gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status`) until it is not in progress, and record it as read.
7. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/PROMOTE_RECEIPT_CB3.md` with the sections `## Merge-forward` (the approval-status line, the `ls-remote` of the feature branch, the merge-forward result line, DEV before and after as `ls-remote` reads), `## Release` (the release branch, the PROD head before and after, the push state as an `ls-remote` read), `## Pages changed` (a table page | route | class: Security Analysis | /security-analysis | Opal-internal), `## CI` (the conclusion and the run it came from, as read).
8. **The fold-back, PREPARATION ONLY (the issuer holds the next step on the CTO's named waiver).** In `C:/dev/ajb_workspace/portal`: `git fetch origin DEV PROD -q`; `git worktree add -b cand/dell1/prod-into-dev-fold-r121 <a temporary path> origin/DEV` (cut from `origin/DEV`, never from PROD); in it `git merge --no-ff origin/PROD` with a message file written with the Write tool (one line naming the fold-back of the round-121 release merge); the merge must be clean. PROOF, printed: `git diff --quiet origin/DEV HEAD && echo TREE-EQUALS-DEV` (a tree that differs from `origin/DEV` is a STOP: file a BLOCKING row with the `git diff --stat`, do not go on); `git rev-list --count origin/DEV..HEAD`. Write `git rev-list origin/PROD..origin/DEV` (one sha per line, the commits DEV holds that PROD does not, measured AFTER your promote and fetch) to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/FOLDBACK_OVERLAP_SHAS_R121.txt` and its count to the receipt under `## Fold-back (prepared)` with the fold branch, the fold merge sha and the two proof lines. **Then STOP and report (a report, not a failure): do NOT register an approval row and do NOT run `portal-merge-forward.sh` for the fold-back in this order as it stands.** The register will refuse `dev-overlap` on any DEV-based branch until the CTO's named waiver exists; the issuer asks the CTO for it and amends this order with the waiver's file and a step 9.

**AMENDMENT 1 (issuer, 2026-10-18 ~17:4xZ), on your report (msg 8180) and the CTO's waiver (msg 8182): step 9, the fold-back lands under the CTO's one-time named waiver.** The CTO's waiver `org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_WAIVER_FOLDBACK_DEV_OVERLAP_R121_20261018.md` (@3e87382a48, `1.0.0_SA_CTO~DELL1`) names exactly the 132 `origin/PROD..origin/DEV` shas, for the branch `cand/dell1/prod-into-dev-fold-r121` (fold merge `d8473c5b4634`, tree equal to DEV) ONLY; the issuer checked that its set equals your `FOLDBACK_OVERLAP_SHAS_R121.txt` (sorted diff: equal, 132 of 132), that DEV is `522985ef` and PROD `d729ee6d`. The waiver is never a precedent for a feature branch. Do, in order:
9. (a) `git fetch origin DEV PROD -q`; re-print `git rev-list origin/PROD..origin/DEV | wc -l` (must still read 132) and `git rev-parse --short=8 origin/DEV` (must still read `522985ef`) and `git rev-parse --short=8 origin/PROD` (`d729ee6d`); a different value means DEV or PROD moved: STOP and report. (b) Run the register `--check-only` first, then without it ONCE (a second run registers a duplicate row; if the register refuses for ANY reason, STOP and report; never widen the waiver): `python .tools/open-calls.py add --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/prod-into-dev-fold-r121 --purpose "AMGT_RESAPP cb-3 fold-back: DEV contains the round-121 PROD release merge; the tree equals DEV" --pages none --class opal-internal --how "git diff origin/DEV cand/dell1/prod-into-dev-fold-r121 is empty" --portal portal --waive-overlap "$(git -C portal rev-list origin/PROD..origin/DEV | paste -sd, -)" --waiver-ref org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_WAIVER_FOLDBACK_DEV_OVERLAP_R121_20261018.md --asked-by 0.4.0_DT_ClientPlatform~H2`; print the `--check-only` output and the registered row id. (c) The CTO approves the row on sight: wait for `python .tools/open-calls.py approval-status --branch cand/dell1/prod-into-dev-fold-r121` to read `state=APPROVED valid=yes` (poll every 120 seconds for up to 30 minutes, then report and stand down). (d) Re-print `git diff --quiet origin/DEV cand/dell1/prod-into-dev-fold-r121 && echo TREE-EQUALS-DEV` IMMEDIATELY before the merge-forward (a tree that differs is a STOP). (e) From the workspace root run `bash .tools/portal-merge-forward.sh cand/dell1/prod-into-dev-fold-r121 --push` (the one approved route onto DEV; run it ALONE from the right worktree as you did for the feature branch); print its result line, then after a fetch `git -C portal rev-list --count origin/DEV..origin/PROD` (must read `0`) and `git -C portal ls-remote origin DEV`. Add to `PROMOTE_RECEIPT_CB3.md` a section `## Fold-back (landed)` (the register output, the row id, the proof line, the merge-forward result line, DEV head after as an `ls-remote` read, the `DEV..PROD` count); AC4 then reads `0`. Re-run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` after you update the instance (AC4 recorded with its output) and report its verdict line.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>` (a seat order's rows), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. One feature only, exactly the approved one; never `--features` anything else, never live DEV whole, never a client-facing page.
2. DEV is written only by `.tools/portal-merge-forward.sh <branch> --push` on the approved row (step 3); PROD only by `/prod-deploy` of the chosen-set release (step 5); never a force push, never a rebase, never a hand merge into DEV.
3. Edit no product file. The receipt, the overlap-sha file and the deploy ledger entry the skill opens are the only things you write; never `--waive-overlap` unless the issuer's amendment hands you the waiver.

## 3. SURFACES

<paths>
org/devices/state/dell1/
org/critical_paths/.open_deploys/
org/critical_paths/change_management/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; AC4 is a fourth criterion for the one reason that the fold-back is a separate act with its own outcome)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-cb-3"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin PROD -q &amp;&amp; for f in $(git diff --name-only ff611566 43762e0d999d3b67a7a955dc16ac638bbfcdea88); do a=$(git rev-parse origin/PROD:$f); b=$(git rev-parse 43762e0d999d3b67a7a955dc16ac638bbfcdea88:$f); [ "$a" = "$b" ] &amp;&amp; echo "EQUAL $f" || echo "DIFFERS $f"; done</invocation><expect>seven lines `EQUAL <path>`, none `DIFFERS`</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-cb-3"><invocation>gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status</invocation><expect>one JSON row whose `status` is `completed` and `conclusion` is `success`, with `headSha` equal to `git -C C:/dev/ajb_workspace/portal rev-parse origin/PROD` after a fetch, and `headSha` NOT beginning `ff611566` (the pre-promote head at the cut: at the base this criterion reads the old head)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-cb-3"><invocation>grep -c -E "security-analysis|Opal-internal|completed|success" "C:/dev/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/PROMOTE_RECEIPT_CB3.md"</invocation><expect>a count of at least 4 (the route, the class and the CI words each present)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-cb-3"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin DEV PROD -q &amp;&amp; [ "$(git rev-parse --short=8 origin/PROD)" != ff611566 ] &amp;&amp; git rev-list --count origin/DEV..origin/PROD</invocation><expect>the single number `0` (PROD has moved off `ff611566` AND DEV contains PROD, so the fold-back has landed; at the base the guard fails and nothing prints)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE (this stage)

Commit the receipt, the overlap-sha file and the ledger entry under your own lane. Write the proof-of-spec instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/AMGT_RESAPP.TO-AMGT-cb-3.feature-merged-forward-promoted-to-prod-then-folded-back.proof_of_spec.json` (`to_id` equal to the `<to_id>` line character for character, `decomp_ref` from the order's block; AC1 to AC3 with your own outputs, AC4 recorded as not yet met with the count read; only this folder admits you), commit it, run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line, THEN stand down until the issuer's amendment (step 9) arrives.

Report once:
- the approval-status line, the `ls-remote` of the feature branch and the merge-forward result line with DEV before and after;
- the release branch, the PROD head before and after, and the `ls-remote` read of PROD;
- AC1's, AC2's and AC3's output lines;
- the CI conclusion as read;
- the fold branch, the fold merge sha, the two proof lines and the overlap-sha count and file;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-120 analysis item 1 and msg 8168 (the row approved: "merge-forward and one chosen-set promote may proceed, then the byte tie and the fold-back under a named waiver"). Cut as `bv-4` was (the step-6/step-7 split: the waiver's shas exist only after the promote), with the merge-forward INCLUDED as step 3 because the issuer cannot push DEV (the hook refused my own `portal-merge-forward.sh --push` and the branch push at 17:2xZ: DT or integrator only; nothing was pushed). The fold-back's overlap: `origin/PROD..origin/DEV` reads 131 at the cut (DEV carries other approved features), so the fold-back needs a NEW named CTO waiver as in round 115 ("never a precedent for a feature branch"). Seat `~H2` (live, IDLE since `bv-4`); the order carries `<workstream>PROMOTE_SA</workstream>`. The grade ON THE RUNNING PAGE is the issuer's (`AMGT-cb-2`) after the landing and the byte tie.

<status>complete</status>
<round>121</round>
<workstream>PROMOTE_SA</workstream>
<slot>0.4.0_DT_ClientPlatform~H2</slot>
<fabric>dell1</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
