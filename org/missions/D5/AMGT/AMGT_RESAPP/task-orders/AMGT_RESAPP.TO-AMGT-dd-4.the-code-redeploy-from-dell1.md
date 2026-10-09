# AMGT_RESAPP task order -- `AMGT-dd-4` -- THE ROUND-80 REDEPLOY OF `opal-amgt-scoped-api`: CLEAN CITATION HEADINGS SERVED, AND THE FUNCTION'S SOURCE-MAP RECORD FILLED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-dd-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~DELL1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no new cron, alarm, monitor or cadence; one redeploy by hand. The daily snapshot schedule is unchanged.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM line moves; the plan STOPs on any IAM change.
comp-adversary: RUN by the issuer at the cut -- the live function reads CodeSha256 ltXvElwZ4iyRx6bJLDQRWksbDoiTesc8xvu1h+p3QI0= (applied 2026-10-08T17:35:08Z at build pin 63f0605039; site-Z COO handoff @a784000437). It serves 4 of 272 citations with a letterless heading (round80/GROUP_R2_NOTES.md). Its source-map entry carries no last_deployed_commit and no artifact_sha256, so comp-lambdamap files it NO-RECORD (row Z-S374, CTO~Z round-79 analysis R5).
EGRESS CLASS, declared: NONE. The build fetches nothing from the internet.
</preflight>

## 1. THE ACT -- `AMGT-dd-4` (round 80, decomposition s.88)

Under ONE NEVER-2 entry and ONE never-widen pair, ONE code leg:

1. **The live package's bytes.** `aws lambda get-function --function-name opal-amgt-scoped-api` and download
   `Code.Location` to a kept path. Its sha256, base64, must equal the live CodeSha256; if it does not, STOP. That file is
   `AMGT_DEPLOYED_ZIP` for the build.
2. **Build** from a DETACHED worktree at EXACTLY the commit the GO names, never "at or after" it, with
   `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only <a kept path>`. `memory_size` stays as live.
   The build fetches nothing: `PIP_NO_INDEX=1`, `PIP_FIND_LINKS` naming the wheel folder the GO gives (its hashes must
   equal `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/BB18_WHEEL_FOLDER_SHA256_20261008.txt`),
   and `PIP_LOG` naming a file you attach. If a pip step cannot resolve from that folder the build STOPS; no variable is
   unset to get past it.
3. **Before the upload:** the CONTENT-DIFF the build prints against the live package lists exactly the files the pair
   names (`lib/research/filings/passages.py` and `lib/research/api/scoped_amgt.py`, plus any the pair adds with its
   reason). A file not on the list is a STOP.
4. Upload THAT built file, then ONE `safe-apply` on `infra/aws/terraform/harvest/`, the plan graded UNTARGETED. It may move
   exactly ONE resource: the function's code (`module.scoped_amgt_api.aws_lambda_function.this`, its artifact object and
   hash). Any other resource is a STOP before the apply.
5. The new CodeSha256 differs from the live one AND equals the built file's. An unchanged hash is a 0-diff deploy: STOP.
6. **The source-map record (R5).** Run `record-terraform-deploy.sh` and the build's upload record so the function's entry in
   `infra/aws/lambda/ci/lambda-source-map.json` carries `last_deployed_commit` and `artifact_sha256` for THIS deploy. Then
   `comp-lambdamap` no longer files `opal-amgt-scoped-api` under NO-RECORD; quote its line.

**Begin only when** the GO names the build commit and both halves of the pair are committed. Read every live worktree's
`.open_deploys/` (`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`)
and measure the artifact before acting on any entry you find. `r80_deployed_cells.txt` (beside the round-80 checks) lists
the round's deployed checks; the GO states how many lines it holds.

A failing criterion is the ROLLBACK trigger: the kept live package (step 1) through the module, one `safe-apply`.

## 2. BOUNDS

1. The act and nothing else. No memory change, no IAM change, no route, no schedule, no S3 delete, no vendor or SEC call,
   no push of shared branches, no portal promote, nothing fetched from the internet.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~DELL1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-dd-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round80/checks/r80_deployed.py"; echo "exit=$?"</invocation><expect>every listed round-80 deployed check passes; R80 DEPLOYED: YES n of n with n equal to the count the GO states; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-dd-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_deployed.py" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_deployed.py"; echo "exit=$?"</invocation><expect>R78 DEPLOYED: YES and R79 DEPLOYED: YES on the deployed function (no regression); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~DELL1/AMGT_RESAPP.TO-AMGT-dd-4.the-code-redeploy-from-dell1.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the prior and new CodeSha256, and the kept paths of the live package and the built file;
- the CONTENT-DIFF and size, and the pip log's index-request count (expected 0);
- every criterion's output lines;
- the source-map entry's two new values and comp-lambdamap's line for the function.

Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** serves AMGT-dd-2 (CTO~Z round-79 R2) on the live function, and carries R5's term (the source-map record) as
this deploy's step 6. STAGED until dd-2 drains and the pair is signed. Applier RULED 0.7.0_AE_CloudOps~DELL1 by 1.0.0_SA_CTO~DELL1 msg 1394 (each box
deploys its own; the function is not a census producer). The wheel folder is a site-Z path (`C:/tmp/bb18-wheels`): it is copied to
dell1 and each wheel's sha256 verified against the round-78 record before the build; the GO names that dell1 folder.
Check dry-run at the base: AC1 base: `R80 DEPLOYED: NO CELLS LISTED`, exit=2 (never a pass until the GO fills the list).
AC2 is round 79's regression arm.

<status>staged</status>
<round>80</round>
<slot>0.7.0_AE_CloudOps~DELL1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
