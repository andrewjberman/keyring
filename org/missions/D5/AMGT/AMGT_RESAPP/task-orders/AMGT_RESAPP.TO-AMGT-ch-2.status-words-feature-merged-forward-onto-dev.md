# AMGT_RESAPP task order -- `AMGT-ch-2` -- THE ROUND-126 SECURITY ANALYSIS FEATURE (PLAIN WORDS FOR THE POSTURE CITE MISSES) IS MERGED FORWARD ONTO DEV BY THE APPROVED ROUTE; NO PROMOTE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ch-2</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DT_ClientPlatform~H2</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ch-2.status-words-feature-merged-forward-onto-dev</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one branch push and one merge-forward; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- git push of one candidate branch and of DEV in the portal repository under the DT's standing grant (a DT serial may push DEV in Opal-Capital/portal); no AWS call.
comp-adversary: RUN at the cut (2026-10-20 ~01:3xZ) -- `python .tools/open-calls.py approval-status --branch cand/dell1/amgt-sa-status-words` reads the row `dell1-20261020T013211Z-07df` approved by `1.0.0_SA_CTO~DELL1` (msg 8579, class opal-internal); the candidate head is `ebd7b44720f2a9210d91e247072cac21654282a0`, TWO commits on PROD `facddeb6`, 4 paths all under `src/pages/SecurityAnalysis/`. AC1 at the base reads that the head is NOT yet an ancestor of `origin/DEV` (prints nothing); AC2 reads a missing receipt: each FAILS at the base as expected. EGRESS CLASS, declared: git fetch and push of the candidate branch and DEV (the approved merge-forward route only) in Opal-Capital/portal; no other egress.
</preflight>

## 1. THE CELL -- `AMGT-ch-2` (round 126, decomposition s.135)

The box CTO approved the approval row (class Opal-internal: `/security-analysis` is staff-only; msg 8579): the DEV merge-forward is approved and PROD remains a chosen-set promote that is NOT asked in this round. The ONE feature, a candidate cut from PROD `facddeb6`: `cand/dell1/amgt-sa-status-words` (head `ebd7b44720f2a9210d91e247072cac21654282a0`, TWO commits, 4 paths, every path under `src/pages/SecurityAnalysis/`): the Posture tab's cite misses read `management block could not be read` / `is not on file` / `(the model is not recorded)` instead of a raw lowercase status, with a new helper `statusWords.ts`, its harness and its census. The branch exists LOCALLY in the nested portal repository at `C:/dev/ajb_workspace/portal` (the issuer built it through a worker's linked worktree; it is not on origin yet). The issuer cannot push DEV or the portal's branches (the push hook admits a DT or the integrator only). Do, in order:
1. **Confirm the approval.** `python .tools/open-calls.py approval-status --branch cand/dell1/amgt-sa-status-words` from `C:/dev/ajb_workspace` must read `state=APPROVED valid=yes` with `head_sha=ebd7b44720f2a9210d91e247072cac21654282a0`; and `git -C C:/dev/ajb_workspace/portal rev-parse cand/dell1/amgt-sa-status-words` must read the same sha. Otherwise STOP and report: do not push.
2. **Push the feature branch** (the contributing flow's step 3). The push gate reads the CHECKED-OUT branch (your row `AMGT_RESAPP-D1-S64` of round 125): from the main portal tree, which sits on DEV, the push is denied; add a linked worktree on the branch (`git -C C:/dev/ajb_workspace/portal worktree add <a temporary path> cand/dell1/amgt-sa-status-words`) and push from it, then remove that worktree: `git -C <that path> push origin cand/dell1/amgt-sa-status-words`; print `git -C C:/dev/ajb_workspace/portal ls-remote origin refs/heads/cand/dell1/amgt-sa-status-words` (it must read the sha above).
3. **The merge-forward onto DEV, by the one approved route only.** `git -C C:/dev/ajb_workspace/portal fetch origin DEV PROD -q`; print `git -C C:/dev/ajb_workspace/portal rev-parse origin/DEV` (read `f6f1fe5b` at the cut: a different value means DEV moved; name it in the receipt and go on only if the register and the script accept) and then, from the workspace root `C:/dev/ajb_workspace`, `bash .tools/portal-merge-forward.sh cand/dell1/amgt-sa-status-words --push`. Print its result line (it ends with `merge=<sha>`; `merge=-` is a REFUSAL: STOP, file a BLOCKING row naming the refusal token, and do not go on). After a fetch print `git -C C:/dev/ajb_workspace/portal merge-base --is-ancestor ebd7b44720f2a9210d91e247072cac21654282a0 origin/DEV && echo IN-DEV` and `git -C C:/dev/ajb_workspace/portal ls-remote origin DEV`.
4. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/MERGE_FORWARD_RECEIPT_CH2.md` with the sections `## Merge-forward` (the approval-status line, the `ls-remote` of the feature branch, the merge-forward result line, DEV before and after as `ls-remote` reads, the IN-DEV line) and `## Pages changed` (a table page | route | class: Security Analysis | /security-analysis | Opal-internal), `## Not done` (one line: no release build, no PROD promote, no fold-back: none is asked in this order).

Do NOT run `portal-release-build.sh`, `/prod-deploy`, or any fold-back; do not register an approval row; do not use `--waive-overlap`. Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>` (a seat order's rows), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. One feature only, exactly the approved one; never live DEV whole, never a client-facing page.
2. DEV is written only by `.tools/portal-merge-forward.sh <branch> --push` on the approved row (step 3); never a force push, never a rebase, never a hand merge into DEV, never PROD.
3. Edit no product file. The receipt and its instance are the only things you write.

## 3. SURFACES

<paths>
org/devices/state/dell1/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ch-2"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin DEV -q &amp;&amp; git merge-base --is-ancestor ebd7b44720f2a9210d91e247072cac21654282a0 origin/DEV &amp;&amp; echo IN-DEV</invocation><expect>the single line `IN-DEV` (at the base the head is not an ancestor of `origin/DEV` and nothing prints)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ch-2"><invocation>grep -c -E "IN-DEV|merge=|security-analysis|Opal-internal" "C:/dev/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/MERGE_FORWARD_RECEIPT_CH2.md"</invocation><expect>a count of at least 4 (the IN-DEV line, the merge result, the route and the class each present)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit the receipt under your own lane. Write the proof-of-spec instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/AMGT_RESAPP.TO-AMGT-ch-2.status-words-feature-merged-forward-onto-dev.proof_of_spec.json` (`to_id` equal to the `<to_id>` line character for character, `decomp_ref` from the order's block; AC1 and AC2 with your own outputs; only this folder admits you), commit it, run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line.

Report once:
- the approval-status line, the `ls-remote` of the feature branch and the merge-forward result line with DEV before and after;
- AC1's and AC2's output lines;
- the proof verdict line;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the DEV landing of the CTO's round-125 item 1 (msg 8573); approval msg 8579 (row `dell1-20261020T013211Z-07df`). Cut as `cb-3` was, WITHOUT the release, the PROMOTE and the fold-back: the CTO asked for the DEV merge only ("its DEV merge waits only on the building box's CTO"). The issuer cannot push DEV (the hook admits a DT or the integrator only). Seat `~H2` (live, IDLE); the order carries `<workstream>PROMOTE_SA</workstream>`. DEV is 140+ commits ahead of PROD; a later chosen-set promote and its fold-back are a different order and the CTO's call. The grade ON THE RUNNING PAGE is the issuer's (`AMGT-ch-3`, after the landing, under a real staff login).

<status>pending</status>
<round>126</round>
<workstream>PROMOTE_SA</workstream>
<slot>0.4.0_DT_ClientPlatform~H2</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
