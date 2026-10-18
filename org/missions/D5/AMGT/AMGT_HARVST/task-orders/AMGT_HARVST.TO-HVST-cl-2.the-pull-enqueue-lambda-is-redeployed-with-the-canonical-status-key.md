# AMGT_HARVST task order -- `HVST-cl-2` -- ROUND 97, workstream PULLENQ-DEPLOY: THE `opal-research-pull-enqueue` LAMBDA IS REDEPLOYED SO THAT IT WRITES A SLASH TICKER'S STATUS OBJECT UNDER THE CANONICAL PREFIX (TERRAFORM; STAGED behind a signed never-widen pair) (row `D1-W173-S1`; CTO round-96 analysis enrichment item 1, msg 8092)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cl-2.the-pull-enqueue-lambda-is-redeployed-with-the-canonical-status-key</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cl-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task is touched; the seat reads the scheduled-task list for any task that applies Terraform to `infra/aws/terraform/harvest` in its window.
comp-iam: RUN at L5 -- the apply uses the principal the seat's existing Terraform tooling already holds (`safe-apply`); no grant is created or widened; the only write is the replacement of one Lambda function's code (S3 artifact version and `source_code_hash`) and one new object version in the artifact bucket. The BLAST RADIUS is the one function `opal-research-pull-enqueue` (the private research-pull route), named in the never-widen pair with its rollback.
comp-adversary: RUN at L5 -- the adversary is a plan that shows more than the one in-place update of the function (another resource, another attribute, a create or a destroy), an artifact with a second zip entry or a file other than the merged source, a bare `terraform apply` or an apply of a plan other than the saved one, a probe invoke run before the deployed bytes are proved equal to the new source (on the old code the probe's ticker writes a status object and enqueues a message), a probe ticker that the shared rule ACCEPTS (it would enqueue a real pull request), a Bloomberg call, a change to the environment variables, and a half-landed deploy (NEVER-2).
</preflight>

## 0. THE CELL

`HVST-cl-1` (merged `349e7ee0da`) changed `infra/aws/lambda/research/pull_enqueue/lambda_function.py` so that a slash ticker's status object is written at `packs/<slash_safe_key>/status.json` (the raw key stays in the status body and the SQS message). Nothing is deployed yet: the live function still runs the OLD bytes (`CodeSha256` `cWiraC3EeuTU9WDIpc5RXzpw6+RT9WxoeqfH/eZiaxo=` at the issuer's last read), which write the RAW spelling. **This cell deploys it, by Terraform only (`aws lambda update-function-code` is forbidden), with the plan read first.** **State plainly in `cl2_before.out`:** for a ticker with no slash nothing changes; for a slash ticker the status key changes from `packs/BP/_LN_Equity/status.json` to `packs/BP-SLASH-_LN_Equity/status.json`; a ticker the shared rule refuses (non-ASCII or containing `-SLASH-`) now gets a 400 with zero writes where the old code wrote and enqueued.

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-cl-1` is `<status>complete</status>` and merged (`349e7ee0da`).
- (b) The never-widen pair is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round97/NEVER_WIDEN_HALF_COO_CL2_PULL_ENQUEUE_CANONICAL_STATUS_KEY.md` (the issuer prints its sha256 in the GO) and the CTO half named in the GO. Read both; their conditions bind you. The order is STAGED until the issuer sends GO.
- (c) A deploy ledger entry is open at the start and CLOSED and COMMITTED at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-cl2-pull-enqueue-canonical-status.json`), with the window and the rollback.

## 2. THE ACT (dell1)

Read the COO half first: it is the specification of this act. Work from a worktree at `349e7ee0da` or a later commit on which `infra/aws/lambda/research/pull_enqueue/lambda_function.py` has md5 `45c83ddf74640e90368e8bebf712b52c` (print it). Read `docs/deployment/` and `infra/aws/terraform/harvest/` (its `CHANGELOG.json` and the build script) before acting.
0. **Before-state, read only (`cl2_before.out`):** the function's `CodeSha256`, `LastModified`, runtime, handler and environment KEYS; the live artifact's version id, size and sha256 and its zip entries; the queue's approximate message count; whether `packs/ZZ-SLASH-PROBE_US_Equity/status.json` exists (expected: no); a local copy of the previous zip (the rollback bytes; print its sha256, equal to the BEFORE `CodeSha256` in base64); the scheduled-task list with its control. DO NOT call `etfs_compare_peers`; make NO Bloomberg use.
1. **Build and upload** with `infra/aws/terraform/harvest/build-and-upload.sh` (`cl2_upload.out`): the new zip's entries (exactly one, `lambda_function.py`), size, sha256, and that the entry's sha256 equals the source file's.
2. **The plan, read first (`cl2_plan.out`):** plan `infra/aws/terraform/harvest` through the repository's wrapper to a saved plan file; print every resource line that has an action. **Exactly ONE in-place update of the `aws_lambda_function` inside `module.harvest_enqueue`, changing `s3_object_version` and `source_code_hash` only (plus computed values), and NOTHING else.** Any other action or attribute: STOP, do not apply, print the plan, file one row and tell the issuer.
3. **Apply the SAVED plan with `safe-apply`** (never a bare `terraform apply`).
4. **Read after (`cl2_after.out`):** `CodeSha256` equals the new zip's sha256 (base64); environment KEYS, runtime and handler equal the before values; the deployed code (downloaded read-only through the function's code location) equals the source file byte for byte.
5. **The refusal probe, ONLY after step 4 has passed (`cl2_probe.out`):** one direct invoke as the `internal` tier (the event shape of `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~2/check_e2e.py`) with the ticker `ZZ-SLASH-PROBE US Equity`: expected response status 400 with the body `{"error": "missing or invalid 'ticker' in request body"}`; the queue's approximate message count and the absence of `packs/ZZ-SLASH-PROBE_US_Equity/status.json` before and after. **Never invoke with a ticker the shared rule accepts** (it would write a status object and enqueue a real pull request for the box consumer to drain): the CTO's half may allow ONE real invoke for a name the harvest already pulls; absent his word, none.
6. Write `cl2_served.out` ending with exactly these lines: `PLAN_ONE_CHANGE=PASS|FAIL`, `DEPLOYED_BYTES_EQUAL_SOURCE=PASS|FAIL`, `ENV_AND_CONFIG_UNCHANGED=PASS|FAIL`, `REFUSAL_PROBE_NO_SIDE_EFFECT=PASS|FAIL`. A FAIL is rolled back at once if the cause is the deploy (the COO half's rollback), and the cell stays `pending`. State in the ledger close what the grade does NOT prove (the slash write itself is proved offline by `HVST-cl-1` and, in the world, by the first organic slash request).
7. Commit the ledger close. Tell the issuer when the apply has landed and when `cl2_served.out` is written. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>`, then keep working.

## 3. STOPS AND EXPECTED QUESTIONS (the CTO's S51 rule: they live here, before the run; do not ask me for an answer inside the window)

- **STOP, deploy nothing, file one row and tell me:** the source md5 differs; the new zip has a second entry or its entry differs from the source; the plan shows anything beyond the one in-place update (print it); the apply fails; `CodeSha256` after differs from the new zip; the environment keys differ; the probe returns anything but the 400, or the queue count or the status object moved.
- **After the deploy, a difference not named here:** write it plainly, do NOT self-grade the criterion; roll back at once if the cause is the deploy; finish the read-only steps; tell me; I rule.
- **Expected and NOT a failure:** the artifact bucket gets a new object version; the function's `LastModified` and version move; `terraform plan` may print computed values for the changed attributes.
- **Window:** from my GO, the seat states its own window (start and end UTC) in the ledger; there is no service restart.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round97/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round97/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cl2-pull-enqueue-canonical-status.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cl-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round97/cl2_served.out</invocation><expect>(?m)^PLAN_ONE_CHANGE=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cl-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round97/cl2_served.out</invocation><expect>(?m)^DEPLOYED_BYTES_EQUAL_SOURCE=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cl-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round97/cl2_served.out</invocation><expect>(?m)^ENV_AND_CONFIG_UNCHANGED=PASS$</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-cl-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round97/cl2_served.out</invocation><expect>(?m)^REFUSAL_PROBE_NO_SIDE_EFFECT=PASS$</expect></criterion>
</proof_of_spec>

- A fourth criterion, with its reason: AC4 is the only served proof the new code is live without a side effect (a refused ticker writes nothing); AC1 to AC3 are the release's own controls (the live-diff discipline of the CTO's ruling).
- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cl-2.the-pull-enqueue-lambda-is-redeployed-with-the-canonical-status-key.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-cl-2.the-pull-enqueue-lambda-is-redeployed-with-the-canonical-status-key` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cl-2.the-pull-enqueue-lambda-is-redeployed-with-the-canonical-status-key.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads N insertions and 0 deletions; run the row gate against your row WITHOUT any override first (the `Z-S106` override must cover that pre-existing pair only).
- Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them (the Lambda and the artifact bucket are AMGT_RESAPP's own, tag `AMGT_RESAPP`).

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- **STAGED, not sent.** It waits on the CTO half, SC1 being free (it may be mid-`HVST-cl-4` or another lane's work; one order at a time) and my GO. Receiving seat: `0.7.0_AE_CloudOps~SC1` (CLAUDE.md rule 34).
- Authority: the CTO's round-96 analysis (msg 8092) enrichment item 1. Decomposition section 132. The function belongs to the `AMGT_RESAPP` system (its Terraform module sets `system_tag = "AMGT_RESAPP"`): the RESAPP COO is told by the CTO's half or by me before the GO if the pair names it (a cross-project notice, not a gate).
- **The CTO's S51 rules are applied:** every stop and expected question is section 3; I check SC1's READ ack within 10 minutes of the handing and type a nudge if the seat is idle.
- Dry run at the base: all four criteria FAIL as expected (the file does not exist).

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>pending</status>
<round>97</round>
<workstream>PULLENQ-DEPLOY</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
