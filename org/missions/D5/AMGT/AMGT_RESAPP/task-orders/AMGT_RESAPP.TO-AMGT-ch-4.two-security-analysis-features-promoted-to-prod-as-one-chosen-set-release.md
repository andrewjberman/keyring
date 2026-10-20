# AMGT_RESAPP task order -- `AMGT-ch-4` -- THE TWO SECURITY ANALYSIS FEATURES (PLAIN WORDS FOR THE PEERS READ STATUS AND THE EXPORT ERROR; PLAIN WORDS FOR THE POSTURE CITE MISSES) ARE PROMOTED TO PROD AS ONE CHOSEN-SET RELEASE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ch-4</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DT_ClientPlatform~H2</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ch-4.two-security-analysis-features-promoted-to-prod-as-one-chosen-set-release</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one release build and one promote; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- git push of PROD in the portal repository under the DT's standing grant (a DT serial may push PROD in Opal-Capital/portal); no AWS call.
comp-adversary: RUN at the cut (2026-10-20 ~02:4xZ) -- `python .tools/open-calls.py approval-status --branch cand/dell1/amgt-sa-reader-words` reads `state=APPROVED valid=yes row=dell1-20261019T224555Z-fbb9 by=1.0.0_SA_CTO~DELL1 head_sha=c8cd2da0ebbb3cb8b27c4b34d161118a2913083c commits=1 class=opal-internal`; `... --branch cand/dell1/amgt-sa-status-words` reads `state=APPROVED valid=yes row=dell1-20261020T013211Z-07df by=1.0.0_SA_CTO~DELL1 head_sha=ebd7b44720f2a9210d91e247072cac21654282a0 commits=2 class=opal-internal`; both branches are on origin and both are on DEV (`5552e2197f`, the issuer's read). The CTO's msg 8584 ruled the promote ("promote cg-2 and ch-1 in the chosen-set PROD promote (Opal-internal, approved by me)") after the issuer's forced-state reads on the running DEV build. PROD is `ba2c341279` (the issuer's read at the cut; it was `facddeb6` when both branches were cut, so PROD moved by one dell2 release merge touching other pages). The two branches share NO path (15 paths and 4 paths, every one under `src/pages/SecurityAnalysis/`). AC1 at the base reads `DIFFERS` on the paths (PROD carries neither feature), AC2 reads the current PROD head `ba2c3412`, which the criterion refuses, and AC3 reads a missing receipt: each FAILS at the base as expected. EGRESS CLASS, declared: git fetch and push of PROD in Opal-Capital/portal, the CI read; no other egress.
</preflight>

## 1. THE CELL -- `AMGT-ch-4` (round 126, decomposition s.135)

TWO approved features, each a candidate cut from PROD `facddeb6`, both already pushed to origin and already merged forward onto DEV: `cand/dell1/amgt-sa-reader-words` (head `c8cd2da0ebbb3cb8b27c4b34d161118a2913083c`, ONE commit, 15 paths: the Peers tab prints `(read failed)` for a failed read, a failed export and a failed print say so in words) and `cand/dell1/amgt-sa-status-words` (head `ebd7b44720f2a9210d91e247072cac21654282a0`, TWO commits, 4 paths: the Posture tab's cite misses read `management block could not be read` and the like). Class Opal-internal: `/security-analysis` is staff-only. Do, in order:
1. **Confirm the approvals.** From `C:/dev/ajb_workspace` run `python .tools/open-calls.py approval-status --branch <b>` for each of the two branches; each must read `state=APPROVED valid=yes` with the `head_sha` named above, and `git -C C:/dev/ajb_workspace/portal ls-remote origin refs/heads/<b>` must read the same head. Otherwise STOP and report: do not build, do not promote.
2. `git -C C:/dev/ajb_workspace/portal fetch origin DEV PROD -q`; print `git -C C:/dev/ajb_workspace/portal rev-parse --short=10 origin/PROD` (read `ba2c341279` at the cut; a different value means PROD moved: name it in the receipt and go on, the release is built on the head you read).
3. From the workspace root run `bash .tools/portal-release-build.sh --features cand/dell1/amgt-sa-reader-words,cand/dell1/amgt-sa-status-words`. It refuses the whole release on any of its pinned tokens (not-approved, stale-head, commits-differ, unapproved-commits, conflict, ...): if it refuses, STOP, file a BLOCKING row naming the token, and do not promote. If its `PROMOTE-CLIENT-FACING` line reads a count above zero, STOP: the set holds a client-facing page and waits on Andrew's word.
4. Promote the release with `/prod-deploy`. The release carries exactly these TWO features and no other candidate; your receipt names `/security-analysis` as Opal-internal. Name any deviation from this order's numbers in the receipt.
5. Read the CI conclusion on the PROD head (`gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status`) until it is not in progress, and record it as read.
6. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/PROMOTE_RECEIPT_CH4.md` with the sections `## Approvals` (the two approval-status lines and the two `ls-remote` reads), `## Release` (the builder's lines verbatim, the release branch, the PROD head before and after, the tag, the push state as an `ls-remote` read), `## Pages changed` (a table page | route | class: Security Analysis | /security-analysis | Opal-internal), `## CI` (the conclusion and the run it came from, as read).
7. **The fold-back, PREPARATION ONLY (the CTO ruled it, msg 8587; the issuer holds the next step on the CTO's named waiver).** In `C:/dev/ajb_workspace/portal`: `git fetch origin DEV PROD -q`; `git worktree add -b cand/dell1/prod-into-dev-fold-r126 <a temporary path> origin/DEV` (cut from `origin/DEV`, never from PROD); in it `git merge --no-ff origin/PROD` with a message file written with the Write tool (one line naming the fold-back of the round-126 release merge and the dell2 release merge it also carries); the merge must be clean. PROOF, printed: `git diff --quiet origin/DEV HEAD && echo TREE-EQUALS-DEV` (a tree that differs from `origin/DEV` is a STOP: file a BLOCKING row with the `git diff --stat`, do not go on; DEV holds unpromoted features, so never compare against PROD's tree); `git rev-list --count origin/DEV..HEAD`. Write `git rev-list origin/PROD..origin/DEV` (one sha per line, measured AFTER your promote and fetch) to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/FOLDBACK_OVERLAP_SHAS_R126.txt` and its count to the receipt under `## Fold-back (prepared)` with the fold branch, the fold merge sha and the two proof lines. **Then STOP and report (a report, not a failure): do NOT register an approval row and do NOT run `portal-merge-forward.sh` for the fold-back in this order as it stands.** The register refuses `dev-overlap` on a DEV-based branch until the CTO's named waiver exists; the issuer asks the CTO for it and amends this order with the waiver's file and a step 8.

**AMENDMENT 2 (issuer, 2026-10-20 ~02:5xZ), on your report (msg 8589) and the CTO's waiver (msg 8591): step 8, the fold-back lands under the CTO's one-time named waiver.** The CTO's waiver `org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_WAIVER_FOLDBACK_DEV_OVERLAP_R126_20261020.md` (@b6328c50dd, `1.0.0_SA_CTO~DELL1`) names exactly the 153 `origin/PROD..origin/DEV` shas, for the branch `cand/dell1/prod-into-dev-fold-r126` (fold merge `8de015fca648`, tree equal to DEV) ONLY; the issuer re-measured that its set equals your `FOLDBACK_OVERLAP_SHAS_R126.txt` (sorted diff empty, 153 of 153), that DEV is `7d5ba57e` and PROD `e890aaa9`. The waiver is never a precedent for a feature branch. Do, in order:
8. (a) `git fetch origin DEV PROD -q`; re-print `git rev-list origin/PROD..origin/DEV | wc -l` (must still read 153), `git rev-parse --short=8 origin/DEV` (`7d5ba57e`) and `git rev-parse --short=8 origin/PROD` (`e890aaa9`); a different value means DEV or PROD moved: STOP and report. (b) Run the register `--check-only` first, then without it ONCE (a second run registers a duplicate row; if the register refuses for ANY reason, STOP and report; never widen the waiver): `python .tools/open-calls.py add --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/prod-into-dev-fold-r126 --purpose "AMGT_RESAPP ch-4 fold-back: DEV contains the round-126 PROD release merge and dell2's release merge; the tree equals DEV" --pages none --class opal-internal --how "git diff origin/DEV cand/dell1/prod-into-dev-fold-r126 is empty" --portal portal --waive-overlap "$(git -C portal rev-list origin/PROD..origin/DEV | paste -sd, -)" --waiver-ref org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_WAIVER_FOLDBACK_DEV_OVERLAP_R126_20261020.md --asked-by 0.4.0_DT_ClientPlatform~H2`; print the `--check-only` output and the registered row id. (c) The CTO approves the row on sight: wait for `python .tools/open-calls.py approval-status --branch cand/dell1/prod-into-dev-fold-r126` to read `state=APPROVED valid=yes` (poll every 120 seconds for up to 30 minutes, then report and stand down). (d) Re-print `git diff --quiet origin/DEV cand/dell1/prod-into-dev-fold-r126 && echo TREE-EQUALS-DEV` IMMEDIATELY before the merge-forward (a tree that differs is a STOP). (e) From the workspace root run `bash .tools/portal-merge-forward.sh cand/dell1/prod-into-dev-fold-r126 --push` ALONE; print its result line, then after a fetch `git -C portal rev-list --count origin/DEV..origin/PROD` (must read `0`) and `git -C portal ls-remote origin DEV`. Add to `PROMOTE_RECEIPT_CH4.md` a section `## Fold-back (landed)` (the register output, the row id, the proof line, the merge-forward result line, DEV head after as an `ls-remote` read, the `DEV..PROD` count); AC4 then reads `0`. Update the instance (AC4 recorded with its output), re-run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` and report its verdict line.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>` (a seat order's rows), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Two features only, exactly the approved ones; never `--features` anything else, never live DEV whole, never a client-facing page.
2. PROD is written only by `/prod-deploy` of the chosen-set release (step 4); never a force push, never a rebase, never a hand merge into PROD; DEV is not written by this order (the fold-back is prepared in a local branch only).
3. Edit no product file. The receipt and the deploy ledger entry the skill opens are the only things you write.

## 3. SURFACES

<paths>
org/devices/state/dell1/
org/critical_paths/.open_deploys/
org/critical_paths/change_management/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ch-4"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin PROD -q &amp;&amp; for b in c8cd2da0ebbb3cb8b27c4b34d161118a2913083c ebd7b44720f2a9210d91e247072cac21654282a0; do for f in $(git diff --name-only facddeb6 $b); do a=$(git rev-parse origin/PROD:$f); c=$(git rev-parse $b:$f); [ "$a" = "$c" ] &amp;&amp; echo "EQUAL $f" || echo "DIFFERS $f"; done; done</invocation><expect>nineteen lines `EQUAL <path>` (15 and 4), none `DIFFERS`</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ch-4"><invocation>gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status</invocation><expect>one JSON row whose `status` is `completed` and `conclusion` is `success`, with `headSha` equal to `git -C C:/dev/ajb_workspace/portal rev-parse origin/PROD` after a fetch, and `headSha` NOT beginning `ba2c3412` (the PROD head at the cut: at the base this criterion reads the old head)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ch-4"><invocation>grep -c -E "security-analysis|Opal-internal|completed|success" "C:/dev/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/PROMOTE_RECEIPT_CH4.md"</invocation><expect>a count of at least 4 (the route, the class and the CI words each present)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-ch-4"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin DEV PROD -q &amp;&amp; [ "$(git rev-parse --short=8 origin/PROD)" != ba2c3412 ] &amp;&amp; git rev-list --count origin/DEV..origin/PROD</invocation><expect>the single number `0` (PROD has moved off `ba2c3412` AND DEV contains PROD, so the fold-back has landed; at the base the guard fails and nothing prints; recorded as not yet met until the issuer's step-8 amendment lands the fold-back)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit the receipt and the ledger entry under your own lane. Write the proof-of-spec instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/AMGT_RESAPP.TO-AMGT-ch-4.two-security-analysis-features-promoted-to-prod-as-one-chosen-set-release.proof_of_spec.json` (`to_id` equal to the `<to_id>` line character for character, `decomp_ref` from the order's block; AC1 to AC3 with your own outputs and AC4 recorded as not yet met with the count read; only this folder admits you), commit it, run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line.

Report once:
- the two approval-status lines and the `ls-remote` reads;
- the builder's `RELEASE-CHECK`, `PROMOTE-LIST`, `PROMOTE-CLIENT-FACING` and `RELEASE` lines, the PROD head before and after, the tag, and the `ls-remote` read of PROD;
- AC1's, AC2's and AC3's output lines;
- the CI conclusion as read;
- the fold branch, the fold merge sha, the two proof lines and the overlap-sha count and file;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's msg 8584 (promote cg-2 and ch-1 in the chosen-set PROD promote, Opal-internal, approved by the CTO; then the issuer reads them on PROD). Cut as `cb-3` was, minus its merge-forward (both branches are already on DEV); the fold-back preparation (step 7) was added by AMENDMENT 1 at the CTO's msg 8587 (`cand/dell1/prod-into-dev-fold-r126`, the usual no-new-code merge; the landing needs the CTO's named waiver and is a later step 8). Seat `~H2` (live); the order carries `<workstream>PROMOTE_SA_PROD</workstream>`. The grade ON THE RUNNING PAGE is the issuer's: PROD under a real login, reading the Peers suffix on a served name and the plain wording on the Posture tab; row `AMGT_RESAPP-D1-W532-S1` (the PROD-only Peers gap) disarms on that read.

<status>pending</status>
<round>126</round>
<workstream>PROMOTE_SA_PROD</workstream>
<slot>0.4.0_DT_ClientPlatform~H2</slot>
<fabric>dell1</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
