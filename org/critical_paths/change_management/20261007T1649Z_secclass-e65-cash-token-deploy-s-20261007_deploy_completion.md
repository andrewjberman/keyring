# Deploy Completion Record
**Date opened:** 2026-10-07T16:49:27.700165+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / the BD E_18 run at 2026-10-07T23:00Z (bd-gold-nightly-fallback cron(0 23 ? * MON-SAT) UTC -> bd-gold-trigger) -- CTO half af8fa774f3 condition 3, its cash_token plan lines (held since 2026-10-07T17:00:27.834139+00:00)
**Deploy:** MDPF_SECCLASS SC-e-65 (C-CASH-TOKEN, PRD v0.16): the cash-token _shared module released from the LAPTOP to its TWO firm copies, in the same window as 0.0.0_AB_MSTR's merge of q/dell1/secclass-r11-held-e65 (candidate 16092a4806, md5 3f1e6be8910952f33c88bf100c610ab6). TREE DEVIATION, STATED: the merge IS on origin (16092a4806 is an ancestor of origin/CLOUD efc2e63467, whose tip is 'merge(0.0.0_AB_MSTR): laptop CLOUD commits into the trunk') but the SHARED laptop CLOUD is 459 commits behind and does not carry it, and the shared-tree sync is 0.0.0_AB_MSTR's act, not this seat's. So steps 1, 2 and 4 all run from a scratch worktree detached at origin/CLOUD efc2e63467 -- the same technique TO-DEPLOY-e42 directed for the same reason. STEP 1 at that worktree: the file on disk reads 3f1e6be8910952f33c88bf100c610ab6. STEP 2 at that worktree: 8 of 8 keys read, ZERO STOPs -- both moving keys live at base cfe898d1 with the order's exact rollback VersionIds, both carriers MATCH (bd a7820a20, cot cb10e3cd) and all four unchanged members MATCH (3a033c04 and 4cc11d3e in both buckets), so the 459-commit difference touches none of the eight keys. TWO MOVING KEYS: opal-data-bd code/gold/lib/_shared/etf_classification_scheduled.py, rollback VersionId P9g4.GzldooFjJgeyMTfk2YlTzT5sQUg; and opal-data-cot same key, rollback VersionId 893RBl4.9fYgJGC7j0qjLTXzVkCQaPX1. Both read ETag cfe898d1b8677c0765a7f5ee8026761c (31,082 B) before the act. ROLLBACK per key: aws s3api copy-object --copy-source <bucket>/<key>?versionId=<that id> back over the key; and for any cash_token row an E_18 run wrote in between, delete that row by its key from the run log (input=cash_token). Halves: COO @00e7bf2cb5 SIGNED, CTO af8fa774f3 SIGNED-with-the-act-corrected (merge PLUS an explicit safe-deploy, because the push gate ships _shared members only beside a gold script). Window 9h because the verify leg cannot close before the BD 23:00Z E_18 run.
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 9.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-data-bd code/gold/lib/_shared/etf_classification_scheduled.py -- MOVES ETag cfe898d1 -> 3f1e6be8; rollback VersionId P9g4.GzldooFjJgeyMTfk2YlTzT5sQUg | comp-pipescript deployed MATCH row + head-object ETag 3f1e6be8910952f33c88bf100c610ab6 | UPLOADED 2026-10-07T16:5xZ, ONE safe-deploy run from the scratch worktree at origin/CLOUD efc2e63467. Output line: 'DEPLOYED-SHIPPED infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py -> s3://opal-data-bd/code/gold/lib/_shared/etf_classification_scheduled.py'; gate 'OK: safe-deploy gate PASS -- all 2 file(s) deployed and verified'; carrier verified 'VERIFY OK comp-pipescript deployed data/black_diamond/scripts/gold/E_18.detect_new_securities.py'. head-object AFTER: ETag 3f1e6be8910952f33c88bf100c610ab6 (the candidate), new VersionId 0aE1FGTSH.2rsPdoj.3mtrBuHmmByxAu. AC1: 'E65-SHIPPED ok=True head=3f1e6be8910952f33c88bf100c610ab6 bd=3f1e6be8910952f33c88bf100c610ab6 cot=3f1e6be8910952f33c88bf100c610ab6 control=MATCH'. ROLLBACK LIVE: head-object --version-id P9g4.GzldooFjJgeyMTfk2YlTzT5sQUg still returns ETag cfe898d1b8677c0765a7f5ee8026761c, 31082 B. | CLOSED 20261007T165854Z |
| L2 | s3-prefix | opal-data-cot code/gold/lib/_shared/etf_classification_scheduled.py -- MOVES ETag cfe898d1 -> 3f1e6be8; rollback VersionId 893RBl4.9fYgJGC7j0qjLTXzVkCQaPX1 | comp-pipescript deployed MATCH row + head-object ETag 3f1e6be8910952f33c88bf100c610ab6 | UPLOADED in the same run. Output line: 'DEPLOYED-SHIPPED ... -> s3://opal-data-cot/code/gold/lib/_shared/etf_classification_scheduled.py'; carrier verified 'VERIFY OK comp-pipescript deployed data/cot/scripts/gold/A_00.accounts_dimension.py'. head-object AFTER: ETag 3f1e6be8910952f33c88bf100c610ab6, new VersionId 0e4OsubYyRdw4RnmCvfMYM0SZtLLM9z9. AC1 reads cot=3f1e6be8910952f33c88bf100c610ab6 in the same line as bd. ROLLBACK LIVE: head-object --version-id 893RBl4.9fYgJGC7j0qjLTXzVkCQaPX1 still returns ETag cfe898d1b8677c0765a7f5ee8026761c, 31082 B. | CLOSED 20261007T165855Z |
| L3 | verify | the SIX byte-identical re-uploads the one safe-deploy run also makes (the two carriers E_18.detect_new_securities.py in bd and A_00.accounts_dimension.py in cot, plus etf_classification.py and etf_classifications_dynamodb.py in BOTH buckets) -- each must come back at the SAME ETag it had before, so the act moves two keys by content and none by content outside those two | head-object ETag per key equal to the pre-act value: bd carrier a7820a205692444dadb59e526200bff6, cot carrier cb10e3cd255db2c58363b6b911aef6cc, etf_classification.py 3a033c04678f1c96d116b641545b17bb both buckets, etf_classifications_dynamodb.py 4cc11d3e74486730febb7e6b4a0ba916 both buckets | THE SIX BYTE-IDENTICAL RE-UPLOADS ALL CAME BACK AT THEIR PRE-ACT ETags -- so the act moved exactly two keys BY CONTENT. head-object after the run, each against the value read before it: opal-data-bd code/gold/E_18.detect_new_securities.py a7820a205692444dadb59e526200bff6 (new VersionId wb5QYkh7QEfrvMEscg.EgAui0MeBaNwB); opal-data-cot code/gold/A_00.accounts_dimension.py cb10e3cd255db2c58363b6b911aef6cc (xsdLG12jt3jBPpWqziwijB9EoKeATW97); code/gold/lib/_shared/etf_classification.py 3a033c04678f1c96d116b641545b17bb in BOTH buckets (bd VBAyhhC5AQPAUTXXPwL3D.H2YQEI6m29, cot DR2_GLcXEPI2wCIr.U3zG1uctEnfofpW); code/gold/lib/_shared/etf_classifications_dynamodb.py 4cc11d3e74486730febb7e6b4a0ba916 in BOTH buckets (bd 2UxuZVruEvP_Vurtwy8SYPvPAe5_tLsf, cot ZFUpv1B8F7NByIpCScoitWaHhfJZmPBi). 8 of 8 keys read, 0 off expectation. Each carries a NEW VersionId because a byte-identical PUT to a versioned bucket still mints one; the CONTENT is unmoved, which is what the half signed. | CLOSED 20261007T165855Z |
| L4 | verify | the FIRST BD E_18 run after the upload (bd-gold-nightly-fallback cron(0 23 ? * MON-SAT) UTC -> bd-gold-trigger, so 2026-10-07T23:00Z) read for its cash_token plan lines (CTO condition 3): every row written names its key; any row whose class is not cash/Cash, or whose key is not a cash token, triggers rollback of the key AND the row | the run id, its cash_token plan lines, and the per-row class check |  | OPEN |

## Log

- 20261007T164927Z OPENED by 0.7.0_AE_CloudOps~S with 4 leg(s)
- 20261007T165854Z LEG L1 closed: UPLOADED 2026-10-07T16:5xZ, ONE safe-deploy run from the scratch worktree at origin/CLOUD efc2e63467. Output line: 'DEPL
- 20261007T165855Z LEG L2 closed: UPLOADED in the same run. Output line: 'DEPLOYED-SHIPPED ... -> s3://opal-data-cot/code/gold/lib/_shared/etf_classificat
- 20261007T165855Z LEG L3 closed: THE SIX BYTE-IDENTICAL RE-UPLOADS ALL CAME BACK AT THEIR PRE-ACT ETags -- so the act moved exactly two keys BY CONTENT. 
- 20261007T170027Z HELD-SOVEREIGN-GATED gate=external/the BD E_18 run at 2026-10-07T23:00Z (bd-gold-nightly-fallback cron(0 23 ? * MON

## Disjointness of write sets -- 1.0.0_SA_CTO msg 106466's condition, both lists printed

The CTO's reading of its own merge rule (msg 106466): an entry reading "apply legs proven, only verify
open; tracked-not-stranded" counts as CLOSED for the e57e61 merge gate **if** TO-DEPLOY-e57e61's write
set shares nothing with what this entry's leg L4 reads. Read below from the two orders' own literal
lists, measured 2026-10-07 ~17:3xZ by `0.7.0_AE_CloudOps~S`.

**WHAT LEG L4 READS** (TO-DEPLOY-e65, CTO half af8fa774f3 condition 3):
- the 2026-10-07T23:00Z BD `E_18.detect_new_securities.py` run's `cash_token` plan lines -- rows written
  put-on-absence into the `etf-classifications` DynamoDB table with `input=cash_token`, class `cash`/`Cash`,
  for held keys matching `^(BD|F)?CASH(IN|OUT)?$` or whose whole normalized name is one of the eight
  `CASH_NAME_PHRASES`;
- the code behind those rows: `s3://opal-data-bd/code/gold/lib/_shared/etf_classification_scheduled.py`
  at ETag `3f1e6be8910952f33c88bf100c610ab6`, plus its bd gold carrier
  `s3://opal-data-bd/code/gold/E_18.detect_new_securities.py`.

**WHAT TO-DEPLOY-e57e61 WRITES** (its own `<the_act>` and `<bounds>`):
- ONE Lambda function, `mdpf-secclass-new-security-lambda`: one artifact upload via
  `infra/aws/lambda/ci/build-and-upload.sh mdpf-secclass mdpf-secclass-new-security-lambda`, and ONE
  `safe-apply` on `infra/aws/terraform/mdpf-secclass/new-security-classifier` whose plan must show
  exactly one in-place update, `source_code_hash`;
- bounds, verbatim: "This one function only. No other root, no IAM, no schedule, no layer, **no table
  write**."

**VERDICT: DISJOINT**, on three axes, each measured rather than inferred.

1. **S3 keys.** Neither repo file e57e61 changes resolves to any firm-bucket deploy target:
   `safe_deploy_core.file_to_s3_target` returns `None` for both
   `infra/aws/lambda/v2_portal/_shared/rivalfunds_classification.py` and
   `infra/aws/lambda/v2_portal/new-security-classifier/lambda_function.py`, `second_targets_for` is `[]`
   and `bundle_for_member` is `None`. The bd+cot shipped `_shared` set is exactly SIX rows (denominator
   printed): `etf_classification.py`, `etf_classification_scheduled.py` and
   `etf_classifications_dynamodb.py`, each to `opal-data-bd` and `opal-data-cot`.
   `rivalfunds_classification.py` is NOT among them and appears in no tree's `shipped_artifacts`. So the
   e57e61 merge cannot move a key leg L4's read depends on. The Lambda artifact goes to the Lambda
   artifacts bucket, not to a firm bucket.
2. **Table rows.** e57e61's act writes NO table row, by its own bounds. It cannot put a row into
   `etf-classifications` during the act, so it cannot add or alter a row the 23:00Z read would grade.
3. **Time.** Nor can the newly applied function's own writes confound the read: the producer's schedule
   is `cron(0 10 ? * MON-FRI *)` America/New_York = 14:00Z, which already fired today, so its next fire
   is 2026-10-08T14:00Z -- after the 23:00Z read. e57e61 step 5 is an APPLY, not an invoke.

**THE ONE RESIDUAL, NAMED:** axis 3 holds only while nobody invokes `mdpf-secclass-new-security-lambda`
ad hoc between the apply and 23:00Z. Nothing in either order does so, and this seat will not.

On the CTO's own stated rule, therefore, the gate is SATISFIED and the e57e61 merge need not wait for
23:00Z. The reading of the rule remains the CTO's; what is asserted here is only the fact it turns on.

### CORRECTION to the disjointness section above (`0.7.0_AE_CloudOps~S`, 2026-10-07 ~18:2xZ)

**The section above claims disjointness on THREE independent axes. That overstates it. There is ONE.**

`infra/aws/lambda/ci/lambda-source-map.json`, entry `mdpf-secclass-new-security-lambda`, `staged_from`:
the producer's artifact bundles `etf_classification_scheduled.py`, staged from
`infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` and packaged flat beside
`etf_classification.py`, `etf_classifications_dynamodb.py` and `rivalfunds_classification.py`.
**That is the module TO-DEPLOY-e65 moved.** So after the e57e61 build the producer Lambda carries the
cash-token rule too, and becomes a SECOND writer of cash-class rows into `etf-classifications` -- the
very table leg L4 grades.

Why the original axes do not cover it:
- **Axis 1 (S3 keys) is literally true but answers a narrower question than the section implies.**
  `file_to_s3_target` does return `None` for both repo files e57e61 changes, and
  `rivalfunds_classification.py` is in no tree's shipped set. What that establishes is that the e57e61
  merge moves no FIRM-BUCKET key. It says nothing about what the e57e61 BUILD stages into a Lambda zip,
  and the staging is where the two orders meet. Reading a deploy map answers "which keys does a push
  move"; it does not answer "which source files does a build bundle", and the section used the first to
  claim the second.
- **Axis 2 (no table write) remains true of the ACT** and false of the artifact's future runs, which is
  the distinction that matters here.
- **Axis 3 (timing) is the axis actually carrying the verdict.**

**The verdict does not change: the 23:00Z read is still clean.** The producer's schedule is
`cron(0 10 ? * MON-FRI *)` America/New_York = 14:00Z, which already fired today, so its next fire is
2026-10-08T14:00Z, after the read. `E_18` writes put-on-absence, so had a producer row landed first,
`E_18` would plan nothing for that key and the 23:00Z read would UNDER-count -- the confound is real in
shape, and only the clock prevents it.

**What changes is the margin and the weight of the residual.** The residual named above -- that nobody
invokes `mdpf-secclass-new-security-lambda` ad hoc between the apply and 23:00Z -- was presented as a
footnote beside three independent guarantees. It is in fact the only thing standing between the apply
and a confounded read, together with the cron. Recorded here at that weight.

Put to `1.0.0_SA_CTO` as msg 106497 with `0.0.0_AB_MSTR` copied, and `MDPF_SECCLASS.TO-DEPLOY-e57e61` is
HELD BY THIS SEAT pending that answer -- run now, or apply after 23:00Z for zero coupling. The order
reads `pending` at `origin/CLOUD` (the issuer's GO is given); the hold is this seat's own, on this
finding, and is not a gate on anybody else.
