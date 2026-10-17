# AMGT_RESAPP task order -- `AMGT-bu-5` -- THE THREE ROUND-114 SECURITY ANALYSIS FEATURES ARE PROMOTED TO PROD AS ONE CHOSEN-SET RELEASE, THEN PROD IS FOLDED BACK INTO DEV UNDER THE CTO'S NAMED WAIVER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bu-5</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DT_ClientPlatform~H2</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bu-5.three-features-promoted-to-prod-then-folded-back</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one promote and one fold-back; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- git push of PROD in the portal repository under the DT's standing /prod-deploy grant; no AWS call.
comp-adversary: RUN at the cut (2026-10-17 ~23:4xZ) -- `python .tools/open-calls.py approval-status --branch <b>` reads APPROVED for all three branches (rows 55a2 at a3f2b727, 5b5e at 9a8ef5e451, c1c6 at dac528b0; the duplicate 0008 is withdrawn); all three heads are in origin/DEV (the merge-forwards 858ca07e, e04c54ac, d2d98f8f, pushed; DEV `d2d98f8f`); `origin/DEV..origin/PROD` reads 0 and PROD is `d1bed0fb`. AC1 at the base reads `DIFFERS` on all 27 paths (PROD does not carry the features), AC2 reads the PROD head `d1bed0fb`, which the criterion refuses, AC3 reads a missing receipt, and AC4 prints nothing and exits 1 at the base (PROD is still `d1bed0fb`): each FAILS at the base as expected. EGRESS CLASS, declared: git fetch and push of PROD in Opal-Capital/portal, the CI read, and (a later step 7) the merge-forward push to DEV by `portal-merge-forward.sh`; no other egress.
</preflight>

## 1. THE CELL -- `AMGT-bu-5` (round 114, decomposition s.123)

The box CTO approved the three approval rows (class Opal-internal: `/security-analysis` is staff-only; the CTO's msg 7777 and its approval record addendum 8 @ab0d02c46f cover the DEV merge-forward AND this PROD promote as ONE set). The three features, each a candidate cut from PROD `d1bed0fb` and already merged forward onto DEV: (1) `cand/dell1/amgt-sa-peers-subject-currency` (head `a3f2b7277bdb24e29cb4723de502fc0862e281f1`, 3 paths): the Peers subject row's money cells read their currency code through one trimming helper; (2) `cand/dell1/amgt-sa-page-dates-long-form` (head `9a8ef5e451e118735e819682c32de816c84a16a8`, 21 paths): the page's date sites print in the house long form; (3) `cand/dell1/amgt-sa-model-grid-scroll-cue` (head `dac528b05e1f4ec8697be2de819674cfa83cfd7e`, 3 paths): the All figures grid carries a cue line and a visible scrollbar thumb. 27 paths in all, every one under `src/pages/SecurityAnalysis/`. Do, in order:
1. **Confirm the features are in DEV and approved.** `git -C C:/dev/ajb_workspace/portal fetch origin DEV PROD -q` and for each of the three heads `git -C C:/dev/ajb_workspace/portal merge-base --is-ancestor <head> origin/DEV && echo IN-DEV`; and `python .tools/open-calls.py approval-status --branch <branch>` for each branch reads `state=APPROVED valid=yes`. If any is not `IN-DEV` or not APPROVED, STOP and report: do not build, do not promote. You never write DEV in this stage.
2. In the portal repository, from the workspace root `C:/dev/ajb_workspace`, run `bash .tools/portal-release-build.sh --features cand/dell1/amgt-sa-peers-subject-currency,cand/dell1/amgt-sa-page-dates-long-form,cand/dell1/amgt-sa-model-grid-scroll-cue`. It refuses the whole release on any of its pinned tokens (not-approved, stale-head, commits-differ, unapproved-commits, ...): if it refuses, STOP, file a BLOCKING row naming the token, and do not promote. If its `PROMOTE-CLIENT-FACING` line reads a count above zero, STOP: the set holds a client-facing page and waits on Andrew's word.
3. Promote the release with `/prod-deploy`. The release carries exactly these THREE features and no other candidate; your receipt names `/security-analysis` as Opal-internal. The PROD head may have moved since the cut (other seats promote too): build on the PROD head you read, and name any deviation from this order's numbers in the receipt.
4. Read the CI conclusion on the PROD head (`gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status`) until it is not in progress, and record it as read.
5. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/PROMOTE_RECEIPT_BU5.md` with the sections `## Release` (the release branch, the PROD head before and after, the push state as an `ls-remote` read), `## Pages changed` (a table page | route | class: Security Analysis | /security-analysis | Opal-internal), `## CI` (the conclusion and the run it came from, as read).
6. **The fold-back, PREPARATION ONLY (the issuer holds the next step on the CTO's named waiver).** In `C:/dev/ajb_workspace/portal`: `git fetch origin DEV PROD -q`; `git worktree add -b cand/dell1/prod-into-dev-fold-r114 <a temporary path> origin/DEV` (cut from `origin/DEV`, never from PROD); in it `git merge --no-ff origin/PROD` with a message file written with the Write tool (one line naming the fold-back of the round-114 release merges); the merge must be clean. PROOF, printed: `git diff --quiet origin/DEV HEAD && echo TREE-EQUALS-DEV` (a tree that differs from `origin/DEV` is a STOP: file a BLOCKING row with the `git diff --stat`, do not go on); `git rev-list --count origin/DEV..HEAD`. Write `git rev-list origin/PROD..origin/DEV` (one sha per line, the commits DEV holds that PROD does not, measured AFTER your promote and fetch) to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/FOLDBACK_OVERLAP_SHAS_R114.txt` and its count to the receipt under `## Fold-back (prepared)` with the fold branch, the fold merge sha and the two proof lines. **Then STOP and report (a report, not a failure): do NOT register an approval row and do NOT run `portal-merge-forward.sh` in this order as it stands.** The register will refuse `dev-overlap` on any DEV-based branch until the CTO's named waiver exists; the issuer asks the CTO for it and amends this order with the waiver's file and step 7.

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
  <criterion id="AC1" cell_refs="AMGT-bu-5"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin PROD -q &amp;&amp; for h in a3f2b7277bdb24e29cb4723de502fc0862e281f1 9a8ef5e451e118735e819682c32de816c84a16a8 dac528b05e1f4ec8697be2de819674cfa83cfd7e; do for f in $(git diff --name-only d1bed0fb $h); do a=$(git rev-parse origin/PROD:$f); b=$(git rev-parse $h:$f); [ "$a" = "$b" ] &amp;&amp; echo "EQUAL $f" || echo "DIFFERS $f"; done; done</invocation><expect>27 lines `EQUAL <path>` (three for the first head, 21 for the second, three for the third, none `DIFFERS`)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bu-5"><invocation>gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status</invocation><expect>one JSON row whose `status` is `completed` and `conclusion` is `success`, with `headSha` equal to `git -C C:/dev/ajb_workspace/portal rev-parse origin/PROD` after a fetch, and `headSha` NOT beginning `d1bed0fb` (the pre-promote head at the cut: at the base this criterion reads the old head)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bu-5"><invocation>grep -c -E "security-analysis|Opal-internal|completed|success" "C:/dev/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/PROMOTE_RECEIPT_BU5.md"</invocation><expect>a count of at least 4 (the route, the class and the CI words each present)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-bu-5"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin DEV PROD -q &amp;&amp; [ "$(git rev-parse --short=8 origin/PROD)" != d1bed0fb ] &amp;&amp; git rev-list --count origin/DEV..origin/PROD</invocation><expect>the single number `0` (PROD has moved off `d1bed0fb` AND DEV contains PROD, so the fold-back has landed; at the base the guard fails and nothing prints)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE (this stage)

Commit the receipt, the overlap-sha file and the ledger entry under your own lane. Write the proof-of-spec instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H2/AMGT_RESAPP.TO-AMGT-bu-5.three-features-promoted-to-prod-then-folded-back.proof_of_spec.json` (`to_id` equal to the `<to_id>` line character for character, `decomp_ref` from the order's block; AC1 to AC3 with your own outputs, AC4 recorded as not yet met with the count read; only this folder admits you), commit it, run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line, THEN stand down until the issuer's amendment (step 7) arrives.

Report once:
- the release branch, the PROD head before and after, and the `ls-remote` read of PROD;
- AC1's, AC2's and AC3's output lines;
- the CI conclusion as read;
- the fold branch, the fold merge sha, the two proof lines and the overlap-sha count and file;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-113 R1-track analysis item 5 and msg 7777 (the three rows approved "for DEV and one chosen-set promote", then the byte tie, then the PROD..DEV list). Cut as `bt-5` was (the step-6/step-7 split: the waiver's shas exist only after the promote). AC4's invocation carries a guard (`PROD != d1bed0fb`) so it FAILS at the base, where `origin/DEV..origin/PROD` already reads 0. Seat `~H2`; the order carries `<workstream>PROMOTE_SA</workstream>` (the round-issuer gate keys a second issuance into a round by workstream). The printed pack (`bu-3`) is NOT part of this release: it is served only through `AMGT-bu-7`. The real-browser walk of the three candidates integrated is `deliverables/2.0.0_SA_COO~R1/round114/CLOSE_WALK_INTEGRATED.md`; the CTO asked that the thumb be read on the running page in the post-promote walk.

<status>pending</status>
<round>114</round>
<workstream>PROMOTE_SA</workstream>
<slot>0.4.0_DT_ClientPlatform~H2</slot>
<fabric>dell1</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
