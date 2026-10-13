# TO MDPF_HEALGAP.TO-HG-t16 -- round 4 HG-t-16: the characteristics producer's re-attempt, served when the T-1 Bloomberg partition lands
<to_id>MDPF_HEALGAP.TO-HG-t16</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.9.0_WK_MDPF_HEALGAP~13</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-16` (`decompositions/MDPF_HEALGAP_DECOMP.md`, ROUND 4) |
**outcome_ref:** row D1-S16, FWD-1's pattern on the characteristics producer, FWD-6 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`HG-t-16`. The characteristics producer (`cot-satellites-characteristics-producer`) fires once a day at `cron(25 13 * * ? *)` and reads the
Bloomberg T-1 partition `bbg/<T-1>/characteristics.parquet` and `run_manifest.json` from `opal-data-etfs`. On a day that partition has not landed
by 13:25Z the producer raises `NoSuchKey` three times (the fire plus two async retries) and the served `characteristics.json` stays the previous
day's until the next 13:25Z. This cell adds ONE more scheduled rule, `cron(25 14-23 * * ? *)` (ten fires, 14:25Z-23:25Z), whose target input is
`{"require_partition": true}`. On that input only, the handler serves the day when the partition has landed and does nothing on a day that is
already complete. The 13:25Z fire, its event and its loud failure are NOT changed. Nothing is chained off an upstream's success: both rules are
wall-clock schedules.

**The estate, read at the base.**
- `infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf`: one rule `cot_satellites_characteristics_producer_daily`
  (`cron(25 13 * * ? *)`), one target, one permission; the role policy `cot_satellites_characteristics_producer_s3` holds ONE `s3:ListBucket`
  statement, `ListBloombergHistoryPrefixes`, on `arn:aws:s3:::opal-data-etfs` conditioned to `bbg/*` and `bbg-testpull/tickers/*`. It has NO
  `ListBucket` on the cot bucket and, by CTO PRD ruling 13c, NO `GetObject` on its own output `platinum/satellites/characteristics.json`.
- `infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/lambda_function.py`: `lambda_handler` calls `producer.main(argv)` for
  every event; it reads no event field except `dry_run` and `bbg_as_of`.
- The producer module (`data/assets/scripts/gold/build_satellites_characteristics.py`, NOT yours) exports the constants the handler needs:
  `OUT_BUCKET`, `OUT_KEY`, `BBG_BUCKET`, `BBG_CHARACTERISTICS_KEY` (`bbg/%s/characteristics.parquet`), `BBG_MANIFEST_KEY`
  (`bbg/%s/run_manifest.json`) and `resolve_bbg_as_of()` (the T-1 trading day from `lib.trading_calendar`, as an ISO string).
- **Why the reads are LISTINGS (the lesson of HG-t-9, again):** an `s3:prefix` condition is populated on a LIST request only, so a HEAD or GET
  on an absent key under a prefix-conditioned grant reads 403, indistinguishable from a missing grant. A `list_objects_v2(Prefix=<exact key>,
  MaxKeys=1)` returns an empty result for an absent key and raises 403 for a missing grant, so a grant fault stays loud. The output's freshness is
  its LastModified read from that listing (the listing returns the key and its LastModified, never its bytes), which is why no GetObject on the
  output is added.
- **Why nothing is typed in the handler:** the naming gate refuses a new hand-kept bucket or key literal. The handler DERIVES every bucket and key
  from the producer module's constants. The new rule's name is built by the `opal_name` module, never typed.

**Build -- the issuer prepared and pre-validated two reference patches against the HEAD you start from (they apply cleanly to a pristine
checkout, and every criterion below reads OK on them). Apply them, run the criteria, and fix minimally only if something differs in your tree:**
1. `git apply org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R4_PATCHES/t16_characteristics_tf.patch` -- the Terraform: one new
   `ListBucket` statement `ListSatellitesCharacteristicsKey` (cot bucket ARN, `StringEquals` `s3:prefix` = the exact output key), and the
   `reattempt_rule_name` module call, the rule `cot_satellites_characteristics_producer_reattempt` at `cron(25 14-23 * * ? *)`, its target
   (`input = jsonencode({ require_partition = true })`) and its `aws_lambda_permission`. The existing rule, target, permission and every other
   statement stay as they are.
2. `git apply org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R4_PATCHES/t16_handler.patch` -- the handler: `import boto3` and a
   `datetime`, helper `_listed` (exact-key match on a listing) and `_reattempt_skip`, called first in `lambda_handler`. On
   `event.get("require_partition")` only: the output listing's LastModified UTC date == today -> one `SKIP-COMPLETE` log line and a skip result;
   else either T-1 key not listed -> one `PARTITION-ABSENT` line and a skip result (no raise); else fall through to the producer exactly as the
   scheduled fire runs it. With no `require_partition` the handler makes NO S3 call and behaves exactly as at the base.
3. Run the three criteria. If a patch does not apply or a criterion reads BAD on it, stop: write the reason and a surprise row; do not weaken a
   check and do not edit anything outside `<paths>`.

Printed name (builder output, rule 30): `etfs-cot-satellites-characteristics-producer-reattempt-hourly` (`lib/opal_naming.py` `name()` over system
`etfs`, scope `cottonwood`, function `satellites-characteristics-producer`, qualifier `reattempt`, kind `hourly`). `terraform init` and `plan`
are NOT yours: confirm the module call's arguments equal that tuple by reading `infra/aws/terraform/modules/opal_name/main.tf`.

### ACCEPTANCE

<criterion id="HG4-t16-AC1" cell_refs="HG-t-16"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R4_CHECKS/hg_r4_rules.py --t16</invocation><expect>T16-OK</expect></criterion>
`HG4-t16-AC1` -- the existing rule stays at `cron(25 13 * * ? *)`; exactly one other rule targets the producer, at `cron(25 14-23 * * ? *)`, named by the `opal_name` module, input `{ require_partition = true }`, with a permission.

<criterion id="HG4-t16-AC2" cell_refs="HG-t-16"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R4_CHECKS/hg_r4_rules.py --t16-iam</invocation><expect>T16IAM-OK</expect></criterion>
`HG4-t16-AC2` -- the role gains exactly one ListBucket statement (Resource the cot bucket ARN, `StringEquals` `s3:prefix` = `platinum/satellites/characteristics.json`), the existing `bbg/*` list is unchanged, and there is NO GetObject on the output and no new Put or Delete.

<criterion id="HG4-t16-AC3" cell_refs="HG-t-16"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R4_CHECKS/hg_t16_gate.py</invocation><expect>GATE-OK</expect></criterion>
`HG4-t16-AC3` -- nine stub arms on the handler: scheduled event makes no S3 call and the producer runs; a landed partition and an unwritten day runs the producer by listings only; a half-landed or absent partition logs one `PARTITION-ABSENT` and runs nothing; a day written today logs one `SKIP-COMPLETE`; 403 on either listing raises; a sibling key is never the key.

<expected_criteria>HG4-t16-AC1 HG4-t16-AC2 HG4-t16-AC3</expected_criteria>

Run each invocation from the worktree root. All three FAIL at the base (`T16-BAD ...`, `T16IAM-BAD ...`, `GATE-BAD ...`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no Lambda invoke, no vendor call, no `terraform init`/`plan`/`apply`, no `safe-apply`.** Every package build, upload and apply is
  the issuer's, at the drain, under its own never-widen pair. Read-only AWS reads are allowed where a criterion names them.
- **NEVER ADD** an alarm, SNS topic, SES send, freshness checker or monitor (standing moratorium). The `SKIP-COMPLETE` and `PARTITION-ABSENT` log
  lines are the whole record.
- **Do not edit** `data/assets/scripts/gold/build_satellites_characteristics.py` (DS's producer; the handler only reads constants and the
  calendar function from it) or `lib/trading_calendar.py`.
- **Do not change** the existing 13:25Z rule, its target, its permission or what the scheduled event does (it still raises on an absent
  partition: that is the loud failure the scheduled fire keeps).
- **Restore mechanisms (CTO round-1 analysis 2.2):** you arm no timer, background task or OS task. If you ever arm one, name it in your report with
  its state at your close.
- **Refusal clause.** If a criterion cannot be met as written (a patch does not apply, a gate refuses a name), stop, write the reason in your
  report and a surprise row (id `MDPF_HEALGAP-D1-W13-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`)
  in the investigation file below, and do not weaken a check. Rows are APPEND-ONLY: never edit an existing row. Write the file with LF line
  endings and check `git diff --stat` shows only your added lines before committing.

<paths>
infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf
infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/lambda_function.py
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 4, the enrichment), cell `HG-t-16`.
<owned_cells>HG-t-16</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG4-t16-AC1, HG4-t16-AC2, HG4-t16-AC3. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~13/MDPF_HEALGAP.TO-HG-t16.characteristics-reattempt-on-partition-arrival.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG4-t16-AC1,HG4-t16-AC2,HG4-t16-AC3 --governing-order <this order file>` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits, and every row you filed.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE comp-schedule is the gate ledger and this order arms no gate; the new fires are `cron(25 14-23 * * ? *)`, the first 60 minutes after the scheduled 13:25Z fire (whose declared worst case, a 120 s timeout and two async retries, is about 8 minutes), so no re-attempt overlaps the fire it backs up.
comp-iam: RUN -- `comp-iam service cot-satellites-characteristics-producer` 2026-10-13 14:13Z, DESIRED plane only: 571 .tf files in 3 trees scanned; 64 policy blocks NOT ATTACHED and 10 deny statements unparsed were never seen, so it cannot say what is denied. The one added statement (a `ListBucket` on the cot bucket, `StringEquals` on the exact output key) is graded by AC2, not by the tool; the never-widen half names it, the writers of `characteristics.json` counted (N printed) and the rollback (revert the policy). The apply is the issuer's at the drain.
comp-adversary: RUN -- `comp-adversary compose` over this order 2026-10-13 14:13Z: 0 cited commits, 11 cited paths (1 GONE: this order's own proof instance, not yet written), neighborhood 2 members (decomposition, PRD), 0 proof instances, 0 unproven dependencies; it has no view of the Lambda's live behaviour. The empty-listing versus 403 distinction is what separates "partition absent" from "grant missing"; the stub test pins both on both buckets. A partition that lands after 23:25Z is served by the next day's scheduled fire (named residual).
risk: WORLD -- an infrastructure path, a role grant and a handler's new branch; the package build, upload and apply are the issuer's at the drain.
direct_act: false -- the class is WORLD.
</preflight>

Source: CTO round-3 analysis `ledger/ROUND_ANALYSIS.round3.md` section 2 and 3 item 1, ADDENDUM 1 (msg 4866); row D1-S16; FWD-1's pattern; decomposition round 4.
