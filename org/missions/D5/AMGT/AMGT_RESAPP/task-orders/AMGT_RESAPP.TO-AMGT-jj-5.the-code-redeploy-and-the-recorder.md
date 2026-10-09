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
