# TO NFRA_SCHWABBF.TO-AL-r7 -- deploy the converter that knows the Cottonwood masters (build, upload, targeted apply) and redrive the held Cottonwood events

<to_id>NFRA_SCHWABBF.TO-AL-r7</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~SA</issued_by>
<issued_date>2026-10-21</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>alongside-deploy</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `AL-r-7` (`decompositions/NFRA_SCHWABBF_DECOMP_AL1.md`) | **outcome_ref:** FWD-8 |
**depends_on:** cells `AL-c-4`, `AL-k-5` (merged; pin `4724bc6017f`). **GO:** this order is `staged`. The issuer writes the GO line when BOTH never-widen halves are signed AND `2.0.0_SA_COO~SB` has told the issuer her R8 closed. Do not act before the flip to `pending`.

---

## WORKER FACE

### GO

(not yet written; it names the two halves, the pin and the window.)

### THE CELL

`AL-r-7`. The Alongside box landed 305 Cottonwood bronze objects (four masters, 2026-10-21). Each fires the shared converter `opal-assets-silver-schwab` through the live event rule `silver-schwab-cottonwood`; the live converter raises `ManifestError: master '<m>' has no basis label` (its `BASIS_LABEL` knows only the three 49F masters) and the events go to the dead-letter queue `https://sqs.us-east-1.amazonaws.com/313476888478/opal-assets-silver-dlq`. Cell `AL-c-4` gave the converter the four labels (`conversion_manifest.py`, `silver_registry.py`, source and Lambda twin); cell `AL-k-5` moved the build pin in `silver.tf` to `be55cb3071`. The module reads its code from S3, so the pin alone stamps new text on old code: you build and upload the artifact, apply the function, verify one event converts, then redrive the held Cottonwood events. Precedents to read first: `2.0.0_SA_COO~SB`'s order `org/missions/D8/NFRA/NFRA_SCHWABBF/task-orders/NFRA_SCHWABBF.TO-BF-r3.fence-and-converter-apply.md` steps B3a and B3 (her exact build, upload and targeted-apply wording), and the ledgers `org/critical_paths/change_management/20261010T2337Z_nfra-oplgtw-og-pn-1-converter_deploy_completion.md` and `20261014T2316Z_nfra-oplgtw-eclipse-converter_deploy_completion.md`.

### DO, IN THIS ORDER (laptop; every Terraform command from the pinned worktree)

0. DISK: `df` on `C:` at least 5 GB free, else stop and report.
1. Pinned worktree: `git worktree add --detach <scratch> 4724bc6017f` with a sparse checkout of `.tools`, `lib`, `infra/aws/terraform/opal-assets`, `infra/aws/terraform/modules`, `infra/aws/lambda`, `infra/logic`, `org/standards`, `org/critical_paths`, `data/assets/scripts` and this project folder. `git -C <scratch> rev-parse HEAD` equals `4724bc6017f...`, `status --porcelain` empty.
2. Open the ledger entry `nfra-schwabbf-converter-cottonwood-labels-20261021` (`python .tools/deploy_ledger.py open ...`): legs L1 build and upload, L2 targeted apply, L3 redrive. Commit entry and sentinel before step 5.
3. BEFORE reads saved to `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/r7/before.txt`: `get-function-configuration` of `opal-assets-silver-schwab` (`CodeSha256`, `LastModified`, `OPAL_BUILD_COMMIT`), `head-object` of `s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-silver-schwab.zip` (VersionId, `Metadata.content-sha256`: the ROLLBACK copy), the DLQ `ApproximateNumberOfMessages` / `NotVisible`, and the converter's `AsyncEventAge` Maximum for the last 10 minutes. If `OPAL_BUILD_COMMIT` is not `27acf60210`, STOP and report (someone else deployed).
4. Build only (L1): from the clean pinned worktree (`git status --short` over `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/`, `data/assets/scripts/silver/`, `data/assets/scripts/lib/` shows nothing) run `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh opal-assets opal-assets-silver-schwab` and print the sha256 it computes; unzip-list the zip and print, for `conversion_manifest.py` and `silver_registry.py`, whether the four Cottonwood masters appear in the zipped text (`08719286`, `08134043`, `08165601`, `08480305`): all must.
5. Upload (L1): the same script WITHOUT `BUILD_ONLY`; `head-object` again: the new `Metadata.content-sha256` MUST equal the built hash, else STOP. The script may rewrite `infra/aws/lambda/ci/function-map/` files in your worktree: do not commit that churn unless the precedent ledgers show a commit of it.
6. Plan (L2): `TF_DATA_DIR` a NEW scratch dir outside every git tree; in `infra/aws/terraform/opal-assets`: `terraform init -input=false` (a migrate or reconfigure prompt = STOP); FIRST a FULL saved plan (no `-target`, no `-var`), printed whole (CTO condition 1). Use `-target` only if the full plan shows drift beyond the schwab function, and then record WHY in the report; find the function's address in `silver.tf` (about lines 770-900, as `TO-BF-r3` B3 says) and save a second plan `-target=<that address>`. **Branch A:** the plan applied (the full plan, or the targeted one when drift forced it) updates exactly one resource in place, the schwab function: its code hash (`source_code_hash` or the S3 object version, per the module) and the `OPAL_BUILD_COMMIT` environment value `27acf60210` to `be55cb3071`, nothing else (and `aws_lambda_permission.silver_s3_invoke["schwab"]` only if listed with no change). **Anything else: Branch B, do not apply, report the plan.**
7. Apply (L2): `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply <saved plan>`. Then `get-function-configuration`: `OPAL_BUILD_COMMIT` equals `be55cb3071`; print `CodeSha256`; the post-apply targeted plan shows no change. Save to `.../r7/after_apply.txt`.
8. ONE event first (L3): `aws sqs receive-message` on the DLQ (`--max-number-of-messages 10`, `--visibility-timeout 600`, `--attribute-names All --message-attribute-names All`; the body is the Lambda destination record: its `requestPayload` holds the original S3 event). Save ALL received message bodies for Cottonwood keys (a `requestPayload` Record whose object key starts `schwab/cottonwood/bronze/`) to `.../r7/dlq_cottonwood_bodies.jsonl` BEFORE any other step, and note any message that is NOT a Cottonwood key (leave those untouched, do not delete them). Take ONE Cottonwood message: `aws lambda invoke --function-name opal-assets-silver-schwab --invocation-type Event --payload fileb://<its requestPayload file> /dev/null` (print the 202); wait 2 minutes; read the result from the laptop: for that key's master and AsOf day, the `schwab/cottonwood/silver/<table>/date=<D>/<master>.parquet` objects that now exist (print the count and 3 keys), the state manifest `s3://opal-data-cottonwood/schwab/cottonwood/state/conversions/date=*/<master>.*` (print one key), and the converter log group: filter `ERROR` since the invoke (print the count; it must be 0 for this key). **If this one event errors or writes nothing: STOP, do not redrive more, report the log lines.**
9. Redrive the rest (L3), only if step 8 was clean: for each remaining saved Cottonwood message, invoke the same way, at most ONE invocation per 2 seconds; every 50 invocations re-read the converter `Errors` Sum and the queue oldest age: if `Errors` for an existing master's key appear, or the oldest age passes 2 hours, STOP. Delete a DLQ message (`aws sqs delete-message`) ONLY after its invocation returned 202 AND its body is in the saved file; do not delete any non-Cottonwood message; never purge the queue.
10. After the last: census from the laptop per master: silver object count by table for the AsOf days landed, the DLQ depth now versus the step-3 baseline (the Cottonwood part must be 0 and the rest unchanged), the converter `Errors` sum since step 7. Save `.../r7/census.txt`. Close the ledger legs L1, L2, L3 with proofs, close the entry, commit with `safe-commit.sh` paths-only, remove the worktree if clean, and report to `2.0.0_SA_COO~SA`: the artifact hash, the apply summary line, the one-event result, the redrive counts (invoked, deleted, left), the census, the commit hash.
ROLLBACK (same window, report before): restore the saved previous artifact version as the current object (`aws s3api copy-object` from the saved VersionId onto the same key, with its metadata), then re-apply the previous pin by `-target` apply from a worktree at `a8c1153b8c` (the commit before the pin bump) for this one function. Cottonwood events then queue to the DLQ as before; nothing is lost.

### ACCEPTANCE (read by the issuer from your committed files)

<criterion id="AL2-r7-AC1" cell_refs="AL-r-7"><invocation>python .tools/proof-of-spec-check.py org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-AL-r7.converter-cottonwood-deploy-and-redrive.proof_of_spec.json AL2-r7-AC1</invocation><expect>VALID</expect></criterion>
`AL2-r7-AC1` -- the proof instance records the artifact hash equality, the targeted plan and apply, the deployed `OPAL_BUILD_COMMIT`, the one-event result, the redrive counts and the post-run census as artifact rows.

<expected_criteria>AL2-r7-AC1</expected_criteria>

## CTO CONDITIONS (half signed @805121f7e7, msg 110167; they bind this order)

1. Full plan first; `-target` only if the plan drifts beyond the Lambda, with the reason recorded (step 6).
2. The label `"08719286": "Cottonwood firm master basis"` is INFERRED (from the FA prefix and Andrew's words), not measured: every report, ledger line and census of this order calls the 08719286 designation "inferred". Do not edit the label.
3. Start only after `2.0.0_SA_COO~SB`'s R8 closes and never while the 0840 queue's oldest event age is past 2 hours (read it at step 3 and again before step 8); end before 21:45Z.
4. Redrive paced, Cottonwood events only, stop at a 2-hour queue age, no rule enabled.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder, the ledger folders, and this order's file. Terraform only in `infra/aws/terraform/opal-assets`, only `-target`ed, only through steps 6 and 7.
- **Never:** an untargeted apply; changing reserved concurrency, event rules, IAM or the fence; touching any bronze key; purging the DLQ; deleting a message you have not saved and re-invoked; redriving a non-Cottonwood message; running the puller or any Schwab call; enabling a rule; starting the backfill.
- **A surprise row you file is committed AT ONCE** with `bash .tools/safe-commit.sh ... -- <the investigations file and your r7/ files>` (paths only) and its hash sent to `2.0.0_SA_COO~SA`.
- **Refusal clause.** If a step cannot be met as written, stop, write the reason and output in your report and a surprise row, and do not improvise.

<paths>
org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_AL1.md</decomp_doc> (Alongside workstream, enrichment), cell `AL-r-7`.
<owned_cells>AL-r-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AL2-r7-AC1. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_SCHWABBF.TO-AL-r7.converter-cottonwood-deploy-and-redrive.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> AL2-r7-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message and a message to `2.0.0_SA_COO~SA`):** as step 10.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change; the window avoids the 21:45Z pull fires and the 12:15Z sweep.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the converter's Cottonwood silver and state writes were granted and fenced by BF-g-5, BF-i-4 and BF-h-5; a PutObject denial is a stop condition.
comp-adversary: DECLARED-NOT-APPLICABLE -- findings: (1) the module reads code from S3, so the pin without the upload would misstate what runs: the order builds, uploads, then applies; (2) the DLQ is shared with the 0840 drain: Cottonwood messages only, saved before any delete; (3) the redrive pace and the 2-hour age stop protect the 0840 events queued behind.
lane: the <paths> block IS the grant; CloudOps seats build and apply under a task order (rule 34).
</preflight>

Source: `2.0.0_SA_COO~SB` msg 110155 (the redeploy is this project's change; precedent her B3a and B3); the COO and CTO never-widen halves; decomposition cell AL-r-7.
