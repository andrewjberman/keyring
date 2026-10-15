# AMGT_RESAPP task order -- `AMGT-bn-3` -- THE TEAM ESTIMATE MARK FEATURE IS PROMOTED TO PROD FROM THE APPROVED LIST, WITH ITS RECEIPT AND THE CI CONCLUSION

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bn-3</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DT_ClientPlatform~H1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bn-3.the-team-estimate-mark-feature-is-promoted-to-prod-from-the-approved-list</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one promote; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- git push of PROD in the portal repository under the DT's standing /prod-deploy grant; no AWS call.
comp-adversary: RUN at the cut -- `python .tools/open-calls.py approval-status --branch cand/dell1/amgt-sa-team-estimate-mark` reads `state=APPROVED valid=yes row=dell1-20261015T221629Z-a333 by=1.0.0_SA_CTO~DELL1 head_sha=bb56c53d12a506bf3441bf7e4b2efb197a9e752f commits=2 class=opal-internal`; the candidate's own diff against its PROD base `33ad65ee` reads five paths, all under `src/pages/SecurityAnalysis/` (`tabs/ModelTab.tsx` modified; `__harness__/teamEstimateMark.harness.cjs` and three `__harness__/teamMarkFixture.*.json` added); origin/PROD reads `e0b43076d9` and origin/DEV `ad7c100b5c` at the cut (2026-10-15 ~22:3xZ), and the candidate is NOT yet in DEV: the merge-forward is the box manager's, asked of `0.0.0_AB_MSTR~DELL1` (msg of 22:29Z). EGRESS CLASS, declared: git fetch and push of PROD in Opal-Capital/portal, and the CI read; no other egress.
</preflight>

## 1. THE CELL -- `AMGT-bn-3` (round 107, decomposition s.116)

The CTO closed the approval row `dell1-20261015T221629Z-a333` APPROVED at head `bb56c53d12a506bf3441bf7e4b2efb197a9e752f` (class Opal-internal, route `/security-analysis` is staff-only: no word from Andrew; record `org/missions/D5/AMGT/AMGT_RESAPP/ledger/CTO_APPROVAL_A333_TEAM_ESTIMATE_MARK_20261015.md`, CTO msgs 6289 and 6293) and named this seat for the promote. The feature: a Key Figures P/E cell that the page fills from the research team's sheet, where the vendor ratio is withheld, prints a visible `research team estimate` line. Do, in order:
1. **Wait for the merge-forward.** It is the box manager's act (`0.0.0_AB_MSTR~DELL1`, asked at 22:29Z), never yours. Run `git -C C:/dev/ajb_workspace/portal fetch origin DEV -q && git -C C:/dev/ajb_workspace/portal merge-base --is-ancestor bb56c53d12a506bf3441bf7e4b2efb197a9e752f origin/DEV && echo IN-DEV`. If it does not print `IN-DEV`, wait 120 seconds and run it again, for up to 20 minutes in all; do not freeze DEV pushes while you wait (the merge-forward IS a DEV push, and it is what you are waiting for). If it still does not print `IN-DEV` after 20 minutes, STOP and report that the merge-forward is not done: do not build, do not promote.
2. In the portal repository (`C:/dev/ajb_workspace/portal`), run `bash .tools/portal-release-build.sh --features cand/dell1/amgt-sa-team-estimate-mark` from the workspace root. It refuses the whole release on any of its pinned tokens (not-approved, stale-head, commits-differ, unapproved-commits, ...): if it refuses, STOP, file a BLOCKING row naming the token, and do not promote.
3. Promote the release with `/prod-deploy`. The release carries ONE feature, five files under `src/pages/SecurityAnalysis/` (the `research team estimate` mark and its harness with three fixtures); no other candidate is in it. Your receipt names `/security-analysis` as Opal-internal. The PROD head may have moved since the cut (other seats promote too): build on the PROD head you read, and name any deviation from this order's numbers in the receipt.
4. Read the CI conclusion on the PROD head (`gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status`) until it is not in progress, and record it as read.
5. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H1/PROMOTE_RECEIPT_BN3.md` with the sections `## Release` (the release branch, the PROD head before and after, the push state as an `ls-remote` read), `## Pages changed` (a table page | route | class: Security Analysis | /security-analysis | Opal-internal), `## CI` (the conclusion and the run it came from, as read).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. One feature only, exactly the approved list; never `--features` anything else, never live DEV whole, never a client-facing page.
2. The push is PROD in `Opal-Capital/portal` by `/prod-deploy`; never DEV, never a force push, never a rebase. Portal DEV is written only by `.tools/portal-merge-forward.sh cand/<box>/<slug>` on an approved row (CLAUDE.md Portal section): the merge-forward in step 1 is that script's run by the box manager.
3. Edit no product file. The receipt and the deploy ledger entry the skill opens are the only things you write.

## 3. SURFACES

<paths>
org/devices/state/dell1/
org/critical_paths/.open_deploys/
org/critical_paths/change_management/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`)

<proof_of_spec>
  <!-- the graded instance, under a short name because this order's own file name would make the canonical path pass this box's MAX_PATH: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H1/AMGT-bn-3.proof_of_spec.json` -->
  <criterion id="AC1" cell_refs="AMGT-bn-3"><invocation>cd C:/dev/ajb_workspace/portal &amp;&amp; git fetch origin PROD -q &amp;&amp; for f in src/pages/SecurityAnalysis/tabs/ModelTab.tsx src/pages/SecurityAnalysis/__harness__/teamEstimateMark.harness.cjs src/pages/SecurityAnalysis/__harness__/teamMarkFixture.SHOP_CN_Equity.json src/pages/SecurityAnalysis/__harness__/teamMarkFixture.PBR_US_Equity.json src/pages/SecurityAnalysis/__harness__/teamMarkFixture.GOOGL_US_Equity.json; do a=$(git rev-parse origin/PROD:$f); b=$(git rev-parse bb56c53d12a5:$f); [ "$a" = "$b" ] &amp;&amp; echo "EQUAL $f" || echo "DIFFERS $f"; done</invocation><expect>five lines `EQUAL <path>` (one per path, none `DIFFERS`)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bn-3"><invocation>gh run list --repo Opal-Capital/portal --branch PROD --limit 1 --json conclusion,headSha,status</invocation><expect>one JSON row whose `status` is `completed` and `conclusion` is `success`, with `headSha` equal to `git -C C:/dev/ajb_workspace/portal rev-parse origin/PROD` after a fetch, and `headSha` NOT beginning `e0b43076` (the pre-promote head at the cut: at the base this criterion reads the old head)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bn-3"><invocation>grep -c -E "security-analysis|Opal-internal|completed|success" "C:/dev/ajb_workspace/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H1/PROMOTE_RECEIPT_BN3.md"</invocation><expect>a count of at least 4 (the route, the class and the CI words each present)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit the receipt and the ledger entry under your own lane. Then write the proof-of-spec instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.4.0_DT_ClientPlatform~H1/AMGT-bn-3.proof_of_spec.json` (a SHORT name on purpose: this order's canonical file name makes a path past this box's MAX_PATH, so the `<proof_of_spec>` block above NAMES this path and the pipeline gate reads the instance by it; `to_id` equal to the `<to_id>` line character for character, `decomp_ref` from the order's block, AC1 to AC3 with your own outputs; only this folder admits you), commit it, run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line, THEN stand down.

Report once:
- the release branch, the PROD head before and after, and the `ls-remote` read of PROD;
- AC1's, AC2's and AC3's output lines;
- the CI conclusion as read;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut 2026-10-15 ~22:3xZ, after the CTO's approval of row `a333` (msgs 6289, 6293: "a Tier-2 seat hears an act only as a task order, so issue it TO-bn-3 citing approval a333 @8703ec5e86"). THE FLOW is `portal/CONTRIBUTING-BOXES.md` step 7 (the promote takes a list, never live DEV whole). The merge-forward was asked of `0.0.0_AB_MSTR~DELL1` at 22:29Z (the DT's own message 6296 said it would hold DEV pushes until its receipt: step 1 tells it not to, because the merge-forward is a DEV push it is waiting on). The DT is a Tier-2 SEAT, not a worker: it holds this order in its own home, commits under its own lane, and reports to `2.0.0_SA_COO~R1` and `1.0.0_SA_CTO~DELL1`. The class is Opal-internal: no word from Andrew. LESSON CARRIED from `bn-1`: a task-order file name this long makes the instance's canonical path exceed MAX_PATH on this box, and `to-pipeline-gate.py check_complete_flip` has no override; the instance is therefore given a short name, and the issuer's flip is graded on it (the block names it from the cut, which `bn-1` needed an amendment to do). `bn-4` (the ten-name walk, the grid opened with `--open-first "All figures"`) waits on THIS promote and on `bn-2` (merged).

<status>complete</status>
<round>107</round>
<workstream>PROMOTE</workstream>
<slot>0.4.0_DT_ClientPlatform~H1</slot>
<fabric>dell1</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
