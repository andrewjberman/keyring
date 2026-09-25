# Deploy Completion Record
**Date opened:** 2026-08-25T10:32:43.583357+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260825T104029Z
**Deploy:** WSE_COTMDL.TO-R2-AE cot-rebalancer-runner: scope=all UNIONs roster with child descent (code change + TF deploy)
**Authored by:** 0.7.0_AE_CloudOps~H
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | lambda_function.py:316 guard removed + test updated, committed on CLOUD | commit hash in HEAD + 15/15 tests + mutant fired | lambda_function.py :316 guard removed (scope now selects SEED SET only; descent runs in BOTH scopes) + module/function docstrings corrected + test_scope_all_pulls_full_roster -> test_scope_all_unions_roster_and_closure, committed @b56ec0e8ce. commit-gate.sh RC0 (py_compile + ds-precommit + ruff). Suite 15/15 green. MUTANT (guard restored, isolated scratch copy, one line): union test FAILED precisely on the children (AssertionError GRANDKID/USTX missing), all -> 4 = roster only; opal_closure test STILL PASSED under the mutant, proving the mutation surgical. :316 PROVEN operative. | CLOSED 20260825T103712Z |
| L2 | s3-prefix | artifact opal-assets/cot-rebalancer-runner.zip rebuilt+uploaded, source-map artifact_sha256 current | build-and-upload output + s3api head-object + source-map commit | build-and-upload.sh opal-assets cot-rebalancer-runner RC0; source_dir resolved from the source map (BUILD INPUT, not filename); import-closure OK 2 packaged .py; sha256 gdW/oQJlKLIaREk8DhEBOv7/kPxIcHuguJhk4KmGE8Y= uploaded to s3://opal-313476888478-lambda-artifacts/opal-assets/cot-rebalancer-runner.zip with write VERIFIED (size=10478, sha256 object-metadata match). source-map artifact_sha256 committed @77ab810b71 (Rule 4). | CLOSED 20260825T103712Z |
| L3 | activation | safe-apply -target module.cot_rebalancer_runner.aws_lambda_function.this (code update from S3) | apply RC0 | safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply -target=module.cot_rebalancer_runner.aws_lambda_function.this -auto-approve: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' RC0, Modifications complete after 6s. TARGETED per COO amendment @12caf0a92f / R2 AC4 -- the 3 foreign committed-but-unapplied changes in this workspace remain untouched and STILL ARMED (CTO owns naming disarm owners). HALTGT: 7 routine pending msgs reviewed, none STOP-class, HALT_ACK=1. | CLOSED 20260825T104028Z |
| L4 | verify | Rule 22a CODE layer: DEPLOYED PACKAGE BYTES carry the union (no :316 guard), diffed against the BUILD INPUT resolved via source-map source_dir -- never by filename | deployed lambda_function.py sha256 == repo sha256 AND guard absent in deployed bytes | Rule 22a CODE LAYER on the DEPLOYED PACKAGE BYTES (downloaded via get-function Code.Location, not inferred): deployed lambda_function.py sha256 41c12d1327e5ec231613e32b24e5827db264332e026b3dad67c272dec9a6afcf (21695 B) == BUILD INPUT sha256, byte-identical RAW and LF-NORMALISED. Build input resolved through the source map source_dir (infra/aws/lambda/cot-pipeline/cot-rebalancer-runner), NEVER by filename. Guard assertion in deployed bytes: occurrences of MODEL_DETAIL_SCOPE != "all" = 0 (required 0); POSITIVE CONTROL MODEL_DETAIL_SCOPE == "all" = 1 (seed-set select, required 1); descent loop _child_model_ids(json.loads(raw)) = 1 (required 1) at deployed :324, unguarded. APPLIED CodeSha256 gdW/oQJlKLIaREk8DhEBOv7/kPxIcHuguJhk4KmGE8Y=, LastModified 2026-08-25T10:38:32.000+0000, env MODEL_DETAIL_SCOPE=all (R1 intact). DESIRED re-plan: 0-diff ON THE TARGET, 3 foreign changes named and counted. | CLOSED 20260825T104028Z |

## Log

- 20260825T103243Z OPENED by 0.7.0_AE_CloudOps~H with 4 leg(s)
- 20260825T103712Z LEG L1 closed: lambda_function.py :316 guard removed (scope now selects SEED SET only; descent runs in BOTH scopes) + module/function d
- 20260825T103712Z LEG L2 closed: build-and-upload.sh opal-assets cot-rebalancer-runner RC0; source_dir resolved from the source map (BUILD INPUT, not fil
- 20260825T104028Z LEG L3 closed: safe-apply.sh -chdir=infra/aws/terraform/opal-assets apply -target=module.cot_rebalancer_runner.aws_lambda_function.this
- 20260825T104028Z LEG L4 closed: Rule 22a CODE LAYER on the DEPLOYED PACKAGE BYTES (downloaded via get-function Code.Location, not inferred): deployed la
- 20260825T104029Z CLOSED -- all 4 legs proven
