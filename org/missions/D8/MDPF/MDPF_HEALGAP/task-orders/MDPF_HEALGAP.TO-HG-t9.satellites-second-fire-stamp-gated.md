# TO MDPF_HEALGAP.TO-HG-t9 -- round 3 HG-t-9: the satellites producer's second fire, gated on the runner's complete stamp
<to_id>MDPF_HEALGAP.TO-HG-t9</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.9.0_WK_MDPF_HEALGAP~7</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-9` (`decompositions/MDPF_HEALGAP_DECOMP.md`, ROUND 3) |
**outcome_ref:** FWD-5 (prerequisite), row D1-S7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`HG-t-9`. The satellites registry producer (`cot-satellites-registry-producer`) fires once a day at `cron(0 7 * * ? *)`. On a day the
Cottonwood runner lands bronze AFTER 07:00Z the registry serves the previous day until the next morning. This cell adds ONE more
scheduled fire at `cron(15 13 * * ? *)` that rebuilds ONLY when the runner's completion stamp for today exists. The 07:00Z fire and its
event are NOT changed. Nothing is chained off the runner's success: both fires are wall-clock schedules.

**The estate, read at the base.**
- `infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf`: one rule `cot_satellites_registry_producer_daily`
  (`cron(0 7 * * ? *)`), one target, one permission; the role policy `cot_satellites_registry_producer_s3` reads only
  `bronze/rebalancer_models/*` and `bronze/rebalancer_model_detail/*` and has NO `s3:ListBucket`.
- `infra/aws/lambda/cot-pipeline/cot-satellites-registry-producer/lambda_function.py`: `lambda_handler` passes no event field to
  `producer.main`.
- **AMENDMENT A2 (issuer, 2026-10-11 ~04:5xZ, after the CTO half refusal msg 3485): the stamp is read by a LISTING, not a HEAD.**
  Round-3 commit `85fe77beb7` merged a HEAD-based handler and a `GetObject` + prefix-conditioned `ListBucket` pair. A `s3:prefix`
  condition is populated only on a LIST request: a HEAD on an absent key therefore reads 403 and `STAMP-ABSENT` would never log.
  The fix, in this order and not a new cell: the handler calls `list_objects_v2(Prefix=<exact stamp key>, MaxKeys=1)` and reads
  presence from `Contents`; the role gets ONE statement, `s3:ListBucket` on the bucket with `s3:prefix` = `<meta prefix>*`; the
  `GetObject` statement is REMOVED (the stamp's content is never read, so no object grant is needed). A listing on an absent key
  returns an empty result, so an absent stamp is logged and a missing grant raises 403 and stays loud.
- **Why the key is not typed in the handler:** the naming gate refuses a new hand-kept `cottonwood` literal. The handler DERIVES the
  bucket and the prefix from the producer module's own constants (`producer.ASSETS_BUCKET`, `producer.ROSTER_KEY`). The new rule's name
  is built by the `opal_name` module, never typed.

**Build -- the tree you start from already carries the round-3 v1 change (merged at `85fe77beb7`). The issuer prepared and
pre-validated two v2 reference patches against that HEAD (they apply cleanly to a pristine checkout and every criterion below reads
OK on them). Apply them, run the criteria, and fix minimally only if something differs in your tree:**
1. `git apply org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_PATCHES/t9_v2_producer_tf.patch` -- the Terraform: removes
   the `ReadRunnerCompleteStamp` GetObject statement, makes the `ListStampPrefix` condition `s3:prefix = ["${local.cot_meta_prefix}*"]`
   (the listing's Prefix is the exact stamp key, under `meta/`), and rewrites the "ONE EXCEPTION" comment. The rule, target,
   permission and the `opal_name` module call stay as merged.
2. `git apply org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_PATCHES/t9_v2_handler.patch` -- the handler: on
   `event.get("require_stamp")` only, `list_objects_v2(Bucket=producer.ASSETS_BUCKET, Prefix=<prefix>/meta/<today UTC>-complete.json,
   MaxKeys=1)` at CALL time and an exact-key match on `Contents`; not listed -> ONE log line beginning `STAMP-ABSENT`, return
   without calling `producer.main`; an AccessDenied raises. No `head_object`/`get_object`, and the now-unused `ClientError` import is
   removed. With no `require_stamp` the handler makes NO S3 call and behaves exactly as at the base.
3. Your earlier proof instance for this order was VALID against the v1 criteria: rebuild it for the same three criterion ids against the
   current checks (the checks changed: `hg_t9_stamp_gate.py` has five arms; `--t9-iam` reads the ListBucket statement exactly),
   re-validate, and flip the order `complete` in the same commit as the instance. Your prior commits `d90794efd4` and `334c1287ac` are
   the inherited state; the surprise rows `MDPF_HEALGAP-D1-W7-S1..S4` are filed and stay; add a new row only for a new finding.

Printed names (builder output, rule 30): `etfs-cot-satellites-registry-producer-stamp-gated-daily` (`python lib/opal_naming.py` `name()`
over system `etfs`, scope `cottonwood`, function `satellites-registry-producer`, qualifier `stamp-gated`, kind `daily`). Confirm the
module's output equals it: `terraform init` and `plan` are NOT yours, so confirm by reading `modules/opal_name/main.tf`'s format.

### ACCEPTANCE

<criterion id="HG3-t9-AC1" cell_refs="HG-t-9"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_CHECKS/hg_r3_rules.py --t9</invocation><expect>T9-OK</expect></criterion>
`HG3-t9-AC1` -- the existing rule stays at `cron(0 7 * * ? *)`; exactly one other rule at `cron(15 13 * * ? *)` targets the producer, is named by the `opal_name` module and carries a permission.

<criterion id="HG3-t9-AC2" cell_refs="HG-t-9"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_CHECKS/hg_r3_rules.py --t9-iam</invocation><expect>T9IAM-OK</expect></criterion>
`HG3-t9-AC2` -- the role gains exactly one ListBucket statement (Resource the bucket ARN, `s3:prefix` = `blackdiamond/cottonwood/meta/*`), NO GetObject or any resource under `meta/`, and no Put or Delete on the assets bucket.

<criterion id="HG3-t9-AC3" cell_refs="HG-t-9"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_CHECKS/hg_t9_stamp_gate.py</invocation><expect>GATE-OK</expect></criterion>
`HG3-t9-AC3` -- four stub arms on the handler: no event field -> no S3 call and the producer runs; stamp present -> the producer runs; 404 -> one `STAMP-ABSENT` line and no rebuild; 403 -> raises.

<expected_criteria>HG3-t9-AC1 HG3-t9-AC2 HG3-t9-AC3</expected_criteria>

Run each invocation from the worktree root. All three FAIL at the base (`T9-BAD ...`, `T9IAM-BAD ...`, `GATE-BAD ...`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no Lambda invoke, no vendor call, no `terraform init`/`plan`/`apply`, no `safe-apply`.** Every deploy and apply is the
  issuer's, at the drain, under its own never-widen pair. Read-only AWS reads are allowed where a criterion names them.
- **NEVER ADD** an alarm, SNS topic, SES send, freshness checker or monitor (standing moratorium). The `STAMP-ABSENT` log line is the whole record.
- **Do not edit** `data/assets/scripts/gold/build_satellites_registry.py` (DS's producer; the handler only reads two of its constants).
- **Restore mechanisms (CTO round-1 analysis 2.2):** you arm no timer, background task or OS task. If you ever arm one, name it in your
  report with its state at your close.
- **Refusal clause.** If a criterion cannot be met as written (a patch does not apply, a gate refuses a name), stop, write the reason in
  your report and a surprise row (id `MDPF_HEALGAP-D1-W7-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or
  `BLOCKING`) in the investigation file below, and do not weaken a check. Rows are APPEND-ONLY: never edit an existing row. Write the
  file with LF line endings and check `git diff --stat` shows only your added lines before committing.

<paths>
infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf
infra/aws/lambda/cot-pipeline/cot-satellites-registry-producer/lambda_function.py
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 3, the enrichment), cell `HG-t-9`.
<owned_cells>HG-t-9</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG3-t9-AC1, HG3-t9-AC2, HG3-t9-AC3. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~7/MDPF_HEALGAP.TO-HG-t9.satellites-second-fire-stamp-gated.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG3-t9-AC1 HG3-t9-AC2 HG3-t9-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits, and every row you filed.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE comp-schedule is the gate ledger and this order arms no gate; the new fire `cron(15 13 * * ? *)` is placed after a 12:45Z landing and 15 minutes before the 13:30Z floor (CTO ruling K), and the 07:00Z fire is unchanged.
comp-iam: RUN -- `comp-iam service cot-satellites-registry-producer` 2026-10-11 03:39Z, DESIRED plane only: 564 .tf files in 3 trees scanned; 64 policy blocks NOT ATTACHED and 10 deny statements unparsed were never seen; it detected NO AWS operations in the handler at the base (the producer's boto3 calls are in a cross-file module it cannot trace), so it is BLIND to the two added statements. The widening (GetObject on the stamp pattern; one prefix-conditioned ListBucket) is graded by AC2, not by the tool; the never-widen half names both statements, the writers of registry.json and holdings.json counted (N printed) and the rollback (revert the policy). The apply is the issuer's at the drain.
comp-adversary: RUN -- `comp-adversary compose` over this order 2026-10-11 03:40Z: 1 cited commit verified, 10 cited paths (1 GONE: this order's own proof instance, not yet written), neighborhood 2 members (decomposition, PRD), 0 proof instances; it has no view of the Lambda's live behaviour. The 403-vs-404 distinction is what separates "stamp absent" from "grant missing"; the stub test pins both arms. A day the runner lands after 13:15Z still serves yesterday until the next 07:00Z fire (named residual).
risk: WORLD -- an infrastructure path and a role grant; the apply is the issuer's at the drain.
direct_act: false -- the class is WORLD.
</preflight>

Source: PRD v0.3 FWD-5; CTO round-2 analysis @1974b85f4e section 3 item 1 and section 2.2; rulings D and K; decomposition round 3.
