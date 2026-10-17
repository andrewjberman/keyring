# AMGT_RESAPP task order -- `AMGT-br-5` -- THE THREE ROUND-111 SECURITY ANALYSIS FEATURES ARE PROMOTED TO PROD AS ONE CHOSEN-SET RELEASE, THEN PROD IS FOLDED BACK INTO DEV UNDER THE CTO'S NAMED WAIVER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-br-5</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DT_ClientPlatform~H2</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-br-5.three-features-promoted-to-prod-then-folded-back</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one promote and one fold-back; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- git push of PROD in the portal repository under the DT's standing /prod-deploy grant; no AWS call.
comp-adversary: RUN at the cut (2026-10-17 ~18:2xZ) -- `python .tools/open-calls.py approval-status --branch <b>` reads `state=APPROVED valid=yes by=1.0.0_SA_CTO~DELL1` for all three branches (rows 887f at 164c9fd5, f0a9 at 3eb64c26, b4db at 259da4c4); all three heads are ancestors of origin/DEV (`merge-base --is-ancestor`, read: yes, yes, yes; DEV `990164ae`, the three merge-forwards `8b3f2ee6`, `b8799fef`, `990164ae`); `origin/DEV..origin/PROD` reads 0 and PROD is `99d2b2a7`. AC1 at the base reads `DIFFERS` on all thirteen paths (EQUAL 0, DIFFERS 13: PROD does not carry the features), AC2 reads the PROD head `99d2b2a7`, which the criterion refuses, AC3 reads a missing receipt, and AC4 prints nothing and exits 1 at the base (PROD is still `99d2b2a7`): each FAILS at the base as expected. EGRESS CLASS, declared: git fetch and push of PROD in Opal-Capital/portal, the CI read, and (a later step 7) the merge-forward push to DEV by `portal-merge-forward.sh`; no other egress.
</preflight>

## 1. THE CELL -- `AMGT-br-5` (round 111, decomposition s.120)

The box CTO approved the three approval rows (class Opal-internal: `/security-analysis` is staff-only; the CTO's messages 7695 and 7697 and the approval record `org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_APPROVAL_DEV_BP1_BP4_SECURITY_ANALYSIS_20261017.md` addenda 2 and 3 cover the DEV merge-forward AND this PROD promote). The three features, each a candidate cut from PROD `99d2b2a7` and already merged forward onto DEV: (1) `cand/dell1/amgt-sa-changed-object-cells` (head `164c9fd58da4a5fae9ebb3d1ee5aa984c918886f`): an object-valued What Changed cell renders as readable text, never raw JSON; (2) `cand/dell1/amgt-sa-pe-footer-words` (head `3eb64c263ade1093c0d18b5b4df241e655ac68da`): the Key Figures `P/E not shown` footer names the missing figure in plain words, never a vendor mnemonic; (3) `cand/dell1/amgt-sa-peers-currency` (head `259da4c4aafd36f14b9939dbbcd86140cc2c6efe`): the Peers tab prints a money figure's currency code when it is not the page name's price currency. Thirteen paths in all (4, 2 and 7), every one under `src/pages/SecurityAnalysis/`. Do, in order:
1. **Confirm the features are in DEV and approved.** `git -C C:/dev/ajb_workspace/portal fetch origin DEV PROD -q` and for each of the three heads `git -C C:/dev/ajb_workspace/portal merge-base --is-ancestor <head> origin/DEV && echo IN-DEV`; and `python .tools/open-calls.py approval-status --branch <branch>` for each branch reads `state=APPROVED valid=yes`. If any is not `IN-DEV` or not APPROVED, STOP and report: do not build, do not promote. You never write DEV in this stage.
2. In the portal repository (`C:/dev/ajb_workspace/portal`), run `bash .tools/portal-release-build.sh --features cand/dell1/amgt-sa-changed-object-cells,cand/dell1/amgt-sa-pe-footer-words,cand/dell1/amgt-sa-peers-currency` from the workspace root. It refuses the whole release on any of its pinned tokens (not-approved, stale-head, commits-differ, unapproved-commits, ...): if it refuses, STOP, file a BLOCKING row naming the token, and do not promote. If its `PROMOTE-CLIENT-FACING` line reads a count above zero, STOP: the set holds a client-facing page and waits on Andrew's word.
3. Promote the release with `/prod-deploy`. The release carries exactly these THREE features and no other candidate; your receipt names `/security-analysis` as Opal-internal. The PROD head may have moved since the cut (other seats promote too): build on the PROD head you read, and name any deviation from this order's numbers in the receipt.
4. Read the CI conclusion on the PROD head (`gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status`) until it is not in progress, and record it as read.
5. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/PROMOTE_RECEIPT_BR5.md` with the sections `## Release` (the release branch, the PROD head before and after, the push state as an `ls-remote` read), `## Pages changed` (a table page | route | class: Security Analysis | /security-analysis | Opal-internal), `## CI` (the conclusion and the run it came from, as read).
6. **The fold-back, PREPARATION ONLY (the issuer holds the next step on the CTO's named waiver).** In `C:/dev/ajb_workspace/portal`: `git fetch origin DEV PROD -q`; `git worktree add -b cand/dell1/prod-into-dev-fold-r111 <a temporary path> origin/DEV` (cut from `origin/DEV`, never from PROD); in it `git merge --no-ff origin/PROD` with a message file written with the Write tool (one line naming the fold-back of the round-111 release merges); the merge must be clean. PROOF, printed: `git diff --quiet origin/DEV HEAD && echo TREE-EQUALS-DEV` (a tree that differs from `origin/DEV` is a STOP: file a BLOCKING row with the `git diff --stat`, do not go on); `git rev-list --count origin/DEV..HEAD`. Write `git rev-list origin/PROD..origin/DEV` (one sha per line, the commits DEV holds that PROD does not, measured AFTER your promote and fetch) to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/FOLDBACK_OVERLAP_SHAS_R111.txt` and its count to the receipt under `## Fold-back (prepared)` with the fold branch, the fold merge sha and the two proof lines. **Then STOP and report (a report, not a failure): do NOT register an approval row and do NOT run `portal-merge-forward.sh` in this order as it stands.** The register will refuse `dev-overlap` on any DEV-based branch until the CTO's named waiver exists; the issuer asks the CTO for it and amends this order with the waiver's path and the exact register flags; step 7 is added then, and AC4 stays open until it is done.

**AMENDMENT 1 (issuer, 2026-10-17 ~18:3xZ), on your report (msg 7701) and the CTO's waiver (msg 7702): step 7, the fold-back lands under the CTO's one-time named waiver.** The CTO's waiver `org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_WAIVER_FOLDBACK_DEV_OVERLAP_R111_20261017.md` (@6b8d7c76cc, `1.0.0_SA_CTO~DELL1`) names exactly the 111 `origin/PROD..origin/DEV` shas, for the branch `cand/dell1/prod-into-dev-fold-r111` (fold merge `f3aa4207de`) ONLY; the issuer checked that its set equals your `FOLDBACK_OVERLAP_SHAS_R111.txt`, and that DEV (`990164ae`) and PROD (`932cea99`) are unchanged. The waiver is never a precedent for a feature branch. Do, in order:
7. (a) `git fetch origin DEV PROD -q`; re-print `git rev-list origin/PROD..origin/DEV | wc -l` (must still read 111) and `git rev-parse origin/DEV` (must still read `990164aecc45c314dfe76d36cfb80de354d35760`); a different value means DEV or PROD moved: STOP and report. (b) Run the register `--check-only` first, then without it: `python .tools/open-calls.py add --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/prod-into-dev-fold-r111 --purpose "AMGT_RESAPP br-5 fold-back: DEV contains the round-111 PROD release merges; the tree equals DEV" --pages none --class opal-internal --how "git diff origin/DEV cand/dell1/prod-into-dev-fold-r111 is empty" --portal portal --waive-overlap "$(git -C portal rev-list origin/PROD..origin/DEV | paste -sd, -)" --waiver-ref org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_WAIVER_FOLDBACK_DEV_OVERLAP_R111_20261017.md --asked-by 0.4.0_DT_ClientPlatform~H2`; print the `--check-only` output and the registered row id (if the register refuses for ANY reason, STOP and report; never widen the waiver). (c) The CTO approves the row on sight: wait for `python .tools/open-calls.py approval-status --branch cand/dell1/prod-into-dev-fold-r111` to read `state=APPROVED valid=yes` (poll every 120 seconds for up to 30 minutes, then report and stand down). (d) Re-print `git diff --quiet origin/DEV cand/dell1/prod-into-dev-fold-r111 && echo TREE-EQUALS-DEV` IMMEDIATELY before the merge-forward (a tree that differs is a STOP). (e) From the workspace root run `bash .tools/portal-merge-forward.sh cand/dell1/prod-into-dev-fold-r111 --push` (the one approved route onto DEV); print its result line, then after a fetch `git -C portal rev-list --count origin/DEV..origin/PROD` (must read `0`) and `git -C portal ls-remote origin DEV`. Add to `PROMOTE_RECEIPT_BR5.md` a section `## Fold-back (landed)` (the register output, the row id, the proof line, the merge-forward result line, DEV head after as an `ls-remote` read, the `DEV..PROD` count); AC4 then reads `0`. Re-run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` after you update the instance (AC4 recorded with its output) and report its verdict line. The gate limb that graded this amendment is GATE (viii) (a modify on an order already declaring placeholders).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>` (a seat order's rows), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Three features only, exactly the approved list; never `--features` anything else, never live DEV whole, never a client-facing page.
2. The push is PROD in `Opal-Capital/portal` by `/prod-deploy`; never DEV (until an amendment gives step 7), never a force push, never a rebase. Portal DEV is written only by `.tools/portal-merge-forward.sh cand/<box>/<slug>` on an approved row (CLAUDE.md Portal section): the three feature merge-forwards are already done (step 1 only reads them).
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
  <criterion id="AC1" cell_refs="AMGT-br-5"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin PROD -q &amp;&amp; for h in 164c9fd58da4a5fae9ebb3d1ee5aa984c918886f 3eb64c263ade1093c0d18b5b4df241e655ac68da 259da4c4aafd36f14b9939dbbcd86140cc2c6efe; do for f in $(git diff --name-only 99d2b2a7 $h); do a=$(git rev-parse origin/PROD:$f); b=$(git rev-parse $h:$f); [ "$a" = "$b" ] &amp;&amp; echo "EQUAL $f" || echo "DIFFERS $f"; done; done</invocation><expect>thirteen lines `EQUAL <path>` (four for the first head, two for the second, seven for the third, none `DIFFERS`)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-br-5"><invocation>gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status</invocation><expect>one JSON row whose `status` is `completed` and `conclusion` is `success`, with `headSha` equal to `git -C C:/dev/ajb_workspace/portal rev-parse origin/PROD` after a fetch, and `headSha` NOT beginning `99d2b2a7` (the pre-promote head at the cut: at the base this criterion reads the old head)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-br-5"><invocation>grep -c -E "security-analysis|Opal-internal|completed|success" "C:/dev/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/PROMOTE_RECEIPT_BR5.md"</invocation><expect>a count of at least 4 (the route, the class and the CI words each present)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-br-5"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin DEV PROD -q &amp;&amp; [ "$(git rev-parse --short=8 origin/PROD)" != 99d2b2a7 ] &amp;&amp; git rev-list --count origin/DEV..origin/PROD</invocation><expect>the single number `0` (PROD has moved off `99d2b2a7` AND DEV contains PROD, so the fold-back has landed; at the base the guard fails and nothing prints)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE (this stage)

Commit the receipt, the overlap-sha file and the ledger entry under your own lane. Write the proof-of-spec instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/AMGT_RESAPP.TO-AMGT-br-5.three-features-promoted-to-prod-then-folded-back.proof_of_spec.json` (`to_id` equal to the `<to_id>` line character for character, `decomp_ref` from the order's block; AC1 to AC3 with your own outputs, AC4 recorded as not yet met with the count read; only this folder admits you), commit it, run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line, THEN stand down until the issuer's amendment (step 7) arrives.

Report once:
- the release branch, the PROD head before and after, and the `ls-remote` read of PROD;
- AC1's, AC2's and AC3's output lines;
- the CI conclusion as read;
- the fold branch, the fold merge sha, the two proof lines and the overlap-sha count and file;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-110 analysis item 5 and msgs 7695, 7697 (rows approved) and 7694 (the waiver order stands: after H2's promote the issuer sends the CTO the measured PROD..DEV sha list and the TREE-EQUALS-DEV print; the CTO issues the named waiver the same tick). The step-6/step-7 split is the issuer's design so H2 is not held mid-order for a waiver whose shas only exist after the promote. AC4's invocation carries a guard (`PROD != 99d2b2a7`) so it FAILS at the base, where `origin/DEV..origin/PROD` already reads 0. Seat `~H2` as in `bq-2` (`~H1` holds another project's orders).

<status>pending</status>
<round>111</round>
<workstream>PROMOTE</workstream>
<slot>0.4.0_DT_ClientPlatform~H2</slot>
<fabric>dell1</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
