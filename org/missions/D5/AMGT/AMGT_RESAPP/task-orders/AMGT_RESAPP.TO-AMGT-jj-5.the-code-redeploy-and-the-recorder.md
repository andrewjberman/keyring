# AMGT_RESAPP task order -- `AMGT-jj-5` -- THE ROUND-85 REDEPLOY OF `opal-amgt-scoped-api` (THE ISSUER COLLAPSE) AND THE RECORDER THAT STOPS WRITING `_last_deploy_recorded`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-jj-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no new cron, alarm or cadence; one redeploy and a recorder edit.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM line moves; the plan STOPs on any IAM change.
comp-adversary: RUN at the cut -- live 66MDfT5i answers "ASML" with two candidates; the recorders write the source map's top-level `_last_deploy_recorded` at three lines in two files (row D1-S7).
EGRESS CLASS, declared: NONE for the build (wheels local).
</preflight>

## 1. THE ACT -- `AMGT-jj-5` (round 85, decomposition s.93)

1. **The redeploy:** the same act as round 82's AMGT-gg-7 (`task-orders/AMGT_RESAPP.TO-AMGT-gg-7.the-code-redeploy.md` -- read its
   face whole, and round 81's ee-6 it cites), ONE code leg at the build commit the GO names, after AMGT-jj-4 has published the list.
   The pair lists the CONTENT-DIFF. A failing AC1 or AC3 is the ROLLBACK trigger.
2. **The recorder (row AMGT_RESAPP-D1-S7; CTO~DELL1 msgs 2169, 2197):** `infra/aws/lambda/ci/record-terraform-deploy.sh` (:346,
   :438) and `record-deploy-scope.py` (:219) stop writing `lambda-source-map.json`'s top-level `_last_deploy_recorded`; remove the
   key from `lambda-source-map.json` (the newest `functions[*].last_deployed_at` is its derived value). The shared-infra resource
   map's own key (`record-resource-deploy.sh`, `rm[...]`) is out of scope. Do the recorder edit BEFORE the redeploy so this deploy's
   own record step runs on it.

## 2. BOUNDS

1. The acts and nothing else. No memory change, no IAM change, no route added, no schedule change, no S3 delete, no vendor or SEC
   call, no push of shared branches, no portal promote.
2. (dell1 IAM parity, CTO~DELL1 ADDENDUM 3 @947dd446e5) A send that writes a firm data bucket, or assumes the 49F principal
   outside the runner's own job, is told to the laptop FIRST.
3. Every send to mdpf-daily-runner is reported after the fact, with its command id and purpose.
4. 49 Financial data never goes into another firm's tree.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/ci/record-terraform-deploy.sh
infra/aws/lambda/ci/record-deploy-scope.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-jj-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round84_prep/checks/r84_listing.py" --crit AC1 --where deployed; echo "exit=$?"</invocation><expect>on the deployed function, "ASML" resolves to ASML_NA_Equity naming the other listing, "Micro" still lists, and the other answers are byte-equal to the base; R84 LISTING AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-jj-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round85_prep/checks/r85_sourcemap.py" --crit AC1; echo "exit=$?"</invocation><expect>no recorder writes the source map's top-level _last_deploy_recorded, the key is gone, and the derived last deploy still reads; R85 SOURCEMAP AC1: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-jj-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round84_prep/checks/r84_store.py" --key ASML_NA_Equity,BABA_US_Equity,NU_US_Equity,PBR_US_Equity,SAP_GY_Equity --crit AC2 --where deployed; echo "exit=$?"</invocation><expect>every 20-F name's live /thesis still answers 200 from its business item in English (no regression); R84 STORE AC2 ALL: YES 5 of 5; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-jj-5.the-code-redeploy-and-the-recorder.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the prior and new CodeSha256, and the kept paths;
- the CONTENT-DIFF and the pip log's index-request count;
- the recorder lines changed;
- every criterion's output lines.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Serves AMGT-jj-3 on the live function (hop 3 of 3) and carries row D1-S7. STAGED: waits for jj-3 merged, jj-4 published, and a NEW pair (COO + 1.0.0_SA_CTO~DELL1). Checks dry-run at the base: AC1 base FAIL (R1 NO), AC2 base FAIL (3 lines, key present), AC3 base PASS (a bound).

<status>staged</status>
<round>85</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
<status>pending -- GO 2026-10-09T13:1xZ by the issuer, on 1.0.0_SA_CTO~DELL1's half @a3440434f5. Build pin 4c929a2ffe exactly (carries AMGT-jj-3 @37677d8c5f; cut AFTER jj-4's publish and its post-put read passed -- CTO condition 10), from a DETACHED worktree; wheels C:/tmp/r80-wheels re-hashed; pair COO @621f07b79a + CTO @a3440434f5: gg-7 conditions 1-7 carried (content-diff list or STOP; registry members admitted only on a printed closure reason with one address() byte-equal; analyze.py printed = STOP; kept rollback package 66MDfT5i; ledger opened before apply, closed after, record-terraform-deploy.sh run) PLUS 8 the source-map diff removes ONE top-level line, every functions[*] entry byte-equal; 9 record-resource-deploy.sh NOT edited; 10 after the code leg, ASML serves ASML_NA_Equity naming ASML_US_Equity, Micro byte-equal, every 20-F /thesis unchanged. The recorder edit goes FIRST. Graded by no gate limb (a modification).</status>
<status>pending -- RULING relayed 2026-10-09T13:1xZ (1.0.0_SA_CTO~DELL1 msg 2468, on 0.7.0_AE_CloudOps~RA1 msg 2463): CTO condition 8 reads as a TWO-line source-map diff -- remove the top-level `_last_deploy_recorded` line AND drop the one trailing comma it leaves on the `functions` object's closing brace; the file must parse, every functions[*] entry byte-equal; a third changed line is still a STOP. The source-map edit is RELEASED. Graded by no gate limb (a modification).</status>
<status>pending -- RULING relayed 2026-10-09T13:4xZ on row AMGT_RESAPP-D1-S13: the four closure-carried modules lib/research/identity/{build_universe,one_pager_precedence,positioning_chain,resolver}.py are ADMITTED -- COO ADDENDUM 1 @734476e427 + 1.0.0_SA_CTO~DELL1 ADDENDUM 2 @22bc71e80c (msg 2495), on the applier's measured read (msg 2496: load_issuer_sources has one call site, the CLI main; a call graph seeded at both request entrypoints reaches it 0 times of 1,134 functions). Any further OFF-LIST member is still a STOP. Act 2 (the code leg at pin 4c929a2ffe, from the retained build) is RELEASED. Graded by no gate limb (a modification).</status>
<status>complete -- landed by 0.7.0_AE_CloudOps~RA1, both acts. ACT 1 (row D1-S7, first): the two recorders no longer assign lambda-source-map.json's top-level `_last_deploy_recorded` (record-terraform-deploy.sh python + JS heredocs, record-deploy-scope.py) and the key is removed; commit-gate rc=0; condition 9 verified two ways (record-resource-deploy.sh byte-identical, git diff empty). CONDITION 8 was HELD as unsatisfiable-as-written -- the key is the LAST top-level member, so a 1-line removal leaves invalid JSON -- and RELEASED by 1.0.0_SA_CTO~DELL1 msg 2468 as the TWO-line diff, met exactly: numstat 1+/2-, the file parses, functions object equal on a parsed compare, no third line. ACT 2 STOPPED CORRECTLY at the content-diff on 4 OFF-LIST members (row D1-S13 filed; nothing uploaded, nothing applied, live and S3 re-read to prove it), then ADMITTED by COO ADDENDUM 1 @734476e427 + CTO ADDENDUM 2 @22bc71e80c on this seat's 0-reach call-graph read: load_issuer_sources has ONE call site in the built package (crosswalk.py:1682, main()), and a function-level graph over 212 packaged .py seeded at both request entrypoints reaches 1134 functions and includes it 0 times. Resumed from the RETAINED build -- nothing rebuilt. Live CodeSha256 66MDfT5iFHYD9EHhmiiDc2hyzx1tIDqF2OT9/jGIjHU= -> HZoC2xAifZQGMcEhp6Aso9DH7e5jdqQxHqM6oPXAt9U= at 2026-10-09T13:43:11Z from pin 4c929a2ffe; memory 1769 / python3.11 / timeout 29 unchanged; untargeted plan 0 add / 1 change / 0 destroy applied from the SAVED plan; re-plan 0-diff; pip index requests 0; analyze.py absent (0 mentions). The deploy's own record step then ran on the EDITED recorder and did NOT re-add the top-level key -- act 1's first live exercise -- with AC2's derived stamp advancing to this deploy's 13:45:16Z. AC1 R84 LISTING AC1 YES (ASML serves ASML_NA_Equity naming ASML_US_Equity; Micro still lists AMD/MSFT/MU; 3 of 3 byte-equal); AC2 R85 SOURCEMAP AC1 YES; AC3 R84 STORE AC2 ALL YES 5 of 5. Ledger amgt-resapp-r85-jj5-scoped-api-dell1 CLOSED 11 of 11, committed at open @95342df312. Instance VALID rc=0, 12 of 12 controls discriminate. BOUNDS 2-4 touched by nothing (no store object written by either act). Row D1-S7 corroborated a THIRD time: last_deployed_commit still 271e8f8b43 while the sha fields moved.</status>
