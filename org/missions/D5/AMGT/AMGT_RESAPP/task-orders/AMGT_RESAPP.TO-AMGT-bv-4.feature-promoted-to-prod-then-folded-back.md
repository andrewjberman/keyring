# AMGT_RESAPP task order -- `AMGT-bv-4` -- THE ROUND-115 SECURITY ANALYSIS FEATURE (THE REMAINING DATE BYPASSES) IS PROMOTED TO PROD AS ONE CHOSEN-SET RELEASE, THEN PROD IS FOLDED BACK INTO DEV UNDER THE CTO'S NAMED WAIVER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bv-4</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DT_ClientPlatform~H2</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bv-4.feature-promoted-to-prod-then-folded-back</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one promote and one fold-back; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- git push of PROD in the portal repository under the DT's standing /prod-deploy grant; no AWS call.
comp-adversary: RUN at the cut (2026-10-18 ~03:1xZ) -- `python .tools/open-calls.py approval-status --branch cand/dell1/amgt-sa-remaining-date-bypasses` reads `state=APPROVED valid=yes by=1.0.0_SA_CTO~DELL1` (row 3155 at aa20718421); the head is in origin/DEV (`merge-base --is-ancestor`, read: yes; DEV `a2bdeb78`, the merge-forward pushed); `origin/DEV..origin/PROD` reads 0 and PROD is `26d998f7`. AC1 at the base reads `DIFFERS` on all 5 paths (PROD does not carry the feature), AC2 reads the PROD head `26d998f7`, which the criterion refuses, AC3 reads a missing receipt, and AC4 prints nothing and exits 1 at the base (PROD is still `26d998f7`): each FAILS at the base as expected. EGRESS CLASS, declared: git fetch and push of PROD in Opal-Capital/portal, the CI read, and (a later step 7) the merge-forward push to DEV by `portal-merge-forward.sh`; no other egress.
</preflight>

## 1. THE CELL -- `AMGT-bv-4` (round 115, decomposition s.124)

The box CTO approved the approval row (class Opal-internal: `/security-analysis` is staff-only; the CTO's msg 7854 and its approval record addendum 9 @e0e133a15b cover the DEV merge-forward AND this PROD promote). The ONE feature, a candidate cut from PROD `26d998f7` and already merged forward onto DEV: `cand/dell1/amgt-sa-remaining-date-bypasses` (head `aa20718421e537acf43fc58628d37dcbe545f984`, 5 paths): the date sites the round-114 census deferred in `ModelTab.tsx` and `PeersTab.tsx`, and five further raw reason prints, print in the house long form (the census reads zero bypassing in the two tabs). Every path is under `src/pages/SecurityAnalysis/`. Do, in order:
1. **Confirm the features are in DEV and approved.** `git -C C:/dev/ajb_workspace/portal fetch origin DEV PROD -q` and for the head `git -C C:/dev/ajb_workspace/portal merge-base --is-ancestor aa20718421e537acf43fc58628d37dcbe545f984 origin/DEV && echo IN-DEV`; and `python .tools/open-calls.py approval-status --branch cand/dell1/amgt-sa-remaining-date-bypasses` reads `state=APPROVED valid=yes`. If it is not `IN-DEV` or not APPROVED, STOP and report: do not build, do not promote. You never write DEV in this stage.
2. In the portal repository, from the workspace root `C:/dev/ajb_workspace`, run `bash .tools/portal-release-build.sh --features cand/dell1/amgt-sa-remaining-date-bypasses`. It refuses the whole release on any of its pinned tokens (not-approved, stale-head, commits-differ, unapproved-commits, ...): if it refuses, STOP, file a BLOCKING row naming the token, and do not promote. If its `PROMOTE-CLIENT-FACING` line reads a count above zero, STOP: the set holds a client-facing page and waits on Andrew's word.
3. Promote the release with `/prod-deploy`. The release carries exactly this ONE feature and no other candidate; your receipt names `/security-analysis` as Opal-internal. The PROD head may have moved since the cut (other seats promote too): build on the PROD head you read, and name any deviation from this order's numbers in the receipt.
4. Read the CI conclusion on the PROD head (`gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status`) until it is not in progress, and record it as read.
5. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/PROMOTE_RECEIPT_BV4.md` with the sections `## Release` (the release branch, the PROD head before and after, the push state as an `ls-remote` read), `## Pages changed` (a table page | route | class: Security Analysis | /security-analysis | Opal-internal), `## CI` (the conclusion and the run it came from, as read).
6. **The fold-back, PREPARATION ONLY (the issuer holds the next step on the CTO's named waiver).** In `C:/dev/ajb_workspace/portal`: `git fetch origin DEV PROD -q`; `git worktree add -b cand/dell1/prod-into-dev-fold-r115 <a temporary path> origin/DEV` (cut from `origin/DEV`, never from PROD); in it `git merge --no-ff origin/PROD` with a message file written with the Write tool (one line naming the fold-back of the round-115 release merge); the merge must be clean. PROOF, printed: `git diff --quiet origin/DEV HEAD && echo TREE-EQUALS-DEV` (a tree that differs from `origin/DEV` is a STOP: file a BLOCKING row with the `git diff --stat`, do not go on); `git rev-list --count origin/DEV..HEAD`. Write `git rev-list origin/PROD..origin/DEV` (one sha per line, the commits DEV holds that PROD does not, measured AFTER your promote and fetch) to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/FOLDBACK_OVERLAP_SHAS_R115.txt` and its count to the receipt under `## Fold-back (prepared)` with the fold branch, the fold merge sha and the two proof lines. **Then STOP and report (a report, not a failure): do NOT register an approval row and do NOT run `portal-merge-forward.sh` in this order as it stands.** The register will refuse `dev-overlap` on any DEV-based branch until the CTO's named waiver exists; the issuer asks the CTO for it and amends this order with the waiver's file and step 7.

**AMENDMENT 1 (issuer, 2026-10-18 ~03:3xZ), on your report (msg 7857) and the CTO's waiver (msg 7860): step 7, the fold-back lands under the CTO's one-time named waiver.** The CTO's waiver `org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_WAIVER_FOLDBACK_DEV_OVERLAP_R115_20261018.md` (@0336e55623, `1.0.0_SA_CTO~DELL1`) names exactly the 129 `origin/PROD..origin/DEV` shas, for the branch `cand/dell1/prod-into-dev-fold-r115` (fold merge `39d439fbc1c9`) ONLY; the issuer checked that its set equals your `FOLDBACK_OVERLAP_SHAS_R115.txt`, and that DEV (`a2bdeb78`) and PROD (`ff611566`) are unchanged. The waiver is never a precedent for a feature branch. Do, in order:
7. (a) `git fetch origin DEV PROD -q`; re-print `git rev-list origin/PROD..origin/DEV | wc -l` (must still read 129) and `git rev-parse origin/DEV` (must still read `a2bdeb78`); a different value means DEV or PROD moved: STOP and report. (b) Run the register `--check-only` first, then without it ONCE (a second run registers a duplicate row; if the register refuses for ANY reason, STOP and report; never widen the waiver): `python .tools/open-calls.py add --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/prod-into-dev-fold-r115 --purpose "AMGT_RESAPP bv-4 fold-back: DEV contains the round-115 PROD release merge; the tree equals DEV" --pages none --class opal-internal --how "git diff origin/DEV cand/dell1/prod-into-dev-fold-r115 is empty" --portal portal --waive-overlap "$(git -C portal rev-list origin/PROD..origin/DEV | paste -sd, -)" --waiver-ref org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_WAIVER_FOLDBACK_DEV_OVERLAP_R115_20261018.md --asked-by 0.4.0_DT_ClientPlatform~H2`; print the `--check-only` output and the registered row id. (c) The CTO approves the row on sight: wait for `python .tools/open-calls.py approval-status --branch cand/dell1/prod-into-dev-fold-r115` to read `state=APPROVED valid=yes` (poll every 120 seconds for up to 30 minutes, then report and stand down). (d) Re-print `git diff --quiet origin/DEV cand/dell1/prod-into-dev-fold-r115 && echo TREE-EQUALS-DEV` IMMEDIATELY before the merge-forward (a tree that differs is a STOP). (e) From the workspace root run `bash .tools/portal-merge-forward.sh cand/dell1/prod-into-dev-fold-r115 --push` (the one approved route onto DEV); print its result line, then after a fetch `git -C portal rev-list --count origin/DEV..origin/PROD` (must read `0`) and `git -C portal ls-remote origin DEV`. Add to `PROMOTE_RECEIPT_BV4.md` a section `## Fold-back (landed)` (the register output, the row id, the proof line, the merge-forward result line, DEV head after as an `ls-remote` read, the `DEV..PROD` count); AC4 then reads `0`. Re-run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` after you update the instance (AC4 recorded with its output) and report its verdict line.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>` (a seat order's rows), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. One feature only, exactly the approved one; never `--features` anything else, never live DEV whole, never a client-facing page.
2. The push is PROD in `Opal-Capital/portal` by `/prod-deploy`; never DEV (until an amendment gives step 7), never a force push, never a rebase. Portal DEV is written only by `.tools/portal-merge-forward.sh cand/<box>/<slug>` on an approved row (CLAUDE.md Portal section): the feature's merge-forward is already done (step 1 only reads them).
3. Edit no product file. The receipt, the overlap-sha file and the deploy ledger entry the skill opens are the only things you write; never `--waive-overlap` unless the amendment hands you the waiver.

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
  <criterion id="AC1" cell_refs="AMGT-bv-4"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin PROD -q &amp;&amp; for f in $(git diff --name-only 26d998f7 aa20718421e537acf43fc58628d37dcbe545f984); do a=$(git rev-parse origin/PROD:$f); b=$(git rev-parse aa20718421e537acf43fc58628d37dcbe545f984:$f); [ "$a" = "$b" ] &amp;&amp; echo "EQUAL $f" || echo "DIFFERS $f"; done</invocation><expect>five lines `EQUAL <path>`, none `DIFFERS`</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bv-4"><invocation>gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status</invocation><expect>one JSON row whose `status` is `completed` and `conclusion` is `success`, with `headSha` equal to `git -C C:/dev/ajb_workspace/portal rev-parse origin/PROD` after a fetch, and `headSha` NOT beginning `26d998f7` (the pre-promote head at the cut: at the base this criterion reads the old head)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bv-4"><invocation>grep -c -E "security-analysis|Opal-internal|completed|success" "C:/dev/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/PROMOTE_RECEIPT_BV4.md"</invocation><expect>a count of at least 4 (the route, the class and the CI words each present)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-bv-4"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin DEV PROD -q &amp;&amp; [ "$(git rev-parse --short=8 origin/PROD)" != 26d998f7 ] &amp;&amp; git rev-list --count origin/DEV..origin/PROD</invocation><expect>the single number `0` (PROD has moved off `26d998f7` AND DEV contains PROD, so the fold-back has landed; at the base the guard fails and nothing prints)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE (this stage)

Commit the receipt, the overlap-sha file and the ledger entry under your own lane. Write the proof-of-spec instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/AMGT_RESAPP.TO-AMGT-bv-4.feature-promoted-to-prod-then-folded-back.proof_of_spec.json` (`to_id` equal to the `<to_id>` line character for character, `decomp_ref` from the order's block; AC1 to AC3 with your own outputs, AC4 recorded as not yet met with the count read; only this folder admits you), commit it, run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line, THEN stand down until the issuer's amendment (step 7) arrives.

Report once:
- the release branch, the PROD head before and after, and the `ls-remote` read of PROD;
- AC1's, AC2's and AC3's output lines;
- the CI conclusion as read;
- the fold branch, the fold merge sha, the two proof lines and the overlap-sha count and file;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-114 R1-track analysis item 5 and msg 7854 (the row approved, "the merge-forward, one promote, the byte tie with its negative control, then the fold-back under a named waiver"). Cut as `bu-5` was (the step-6/step-7 split: the waiver's shas exist only after the promote). AC4's invocation carries a guard (`PROD != 26d998f7`) so it FAILS at the base, where `origin/DEV..origin/PROD` already reads 0 after the round-114 fold-back (DEV `a2bdeb78` holds the one merge-forward of this feature). Seat `~H2`; the order carries `<workstream>PROMOTE_SA</workstream>`. The pack and export redeploy (`bv-2`) is NOT part of this release: it is served only through `AMGT-bv-5`. The CTO asked in round 114 that the scroll-cue thumb be read on the running page after a promote; that read is owed to `bv-3`.

<status>pending</status>
<round>115</round>
<workstream>PROMOTE_SA</workstream>
<slot>0.4.0_DT_ClientPlatform~H2</slot>
<fabric>dell1</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
