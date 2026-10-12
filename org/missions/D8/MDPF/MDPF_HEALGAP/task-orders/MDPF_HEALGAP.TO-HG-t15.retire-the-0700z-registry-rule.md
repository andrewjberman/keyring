# TO MDPF_HEALGAP.TO-HG-t15 -- round 3 HG-t-15: retire the 07:00Z registry rule (its work is done by the 13:15Z stamp-gated fire)
<to_id>MDPF_HEALGAP.TO-HG-t15</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.9.0_WK_MDPF_HEALGAP~12</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>RULERETIRE</workstream>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-15` (`decompositions/MDPF_HEALGAP_DECOMP.md`, ROUND 3, AMENDMENT 2) |
**outcome_ref:** FWD-5 (consequence of the runner move; CTO ADDENDUM 5 `0c9f67d92d`, msg 3898) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`HG-t-15`. The satellites registry producer has two schedules: the original `cot_satellites_registry_producer_daily` at `cron(0 7 * * ? *)`
and the stamp-gated `cron(15 13 * * ? *)` (HG-t-9). Since the cottonwood runner's scheduled fire moved off 06:00Z (HG-t-5, applied), no
roster partition for today exists at 07:00Z, so the 07:00Z invocation raises `RegistryProducerError: BLOCKED` three times every day and
writes nothing (measured 2026-10-12: 07:00:15, 07:01:11, 07:03:16Z). Its work is done by the 13:15Z fire. This cell REMOVES the 07:00Z
rule, its target and its permission from the tf. Nothing is added; the stamp-gated rule, the function, the role and its policy stay.

**The estate, read at the base.** `infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf`:
- a comment block headed `THE SCHEDULE -- the entire reason this TO exists (T6AE-AC1/AC4)` (about lines 275-303) deriving 07:00Z;
- `resource "aws_cloudwatch_event_rule" "cot_satellites_registry_producer_daily"` (name `cot-satellites-registry-producer-daily`, `cron(0 7 * * ? *)`);
- `resource "aws_cloudwatch_event_target" "cot_satellites_registry_producer_daily"`;
- `resource "aws_lambda_permission" "events_cot_satellites_registry_producer"` (statement id `EventBridgeCotSatellitesRegistryProducerDaily`);
- then `module "stamp_gated_rule_name"` and the three `..._stamp_gated` resources, which STAY.

**Build (delete lines; do not rewrite the file):**
1. Remove the schedule comment block and the three resource blocks listed above, so that `module "stamp_gated_rule_name"` follows the function
   module directly.
2. In place of the removed block put ONE short ASCII comment (at most 8 lines) saying: the 07:00Z rule was retired by MDPF_HEALGAP.TO-HG-t15
   (CTO ADDENDUM 5); since HG-t-5 the runner's pull lands about 11:32Z, so only the stamp-gated 13:15Z rule can find today's roster partition;
   the daily rule failed 3 attempts a day (RegistryProducerError, writes nothing) from 2026-10-12; rollback of HG-t-5 must restore it.
3. Touch nothing else: no grant, no module call, no stamp-gated resource, no other comment block. The file carries non-ASCII characters in
   comments you are not editing; do not re-encode it.

### ACCEPTANCE

<criterion id="HG3-t15-AC1" cell_refs="HG-t-15"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_CHECKS/hg_t15_retire.py</invocation><expect>T15-OK</expect></criterion>
`HG3-t15-AC1` -- the 07:00Z rule, its target and its permission are gone; the stamp-gated rule (`cron(15 13 * * ? *)`, input `require_stamp`), its permission, the function module and the role policy are kept; against the base pin only lines were removed (nothing added or altered).

<expected_criteria>HG3-t15-AC1</expected_criteria>

Run the invocation from the worktree root. AC1 FAILS at the base (`T15-BAD GONE: ...`). No `terraform fmt` criterion (the sibling file
already fails fmt for unrelated lines; a removal of whole blocks cannot change alignment of what remains).
Known and accepted: the earlier order HG-t-9's check `hg_r3_rules.py --t9` asserts the 07:00Z rule exists and will read T9-BAD after this
cell. HG-t-9 is complete and is not re-graded; do not edit that check.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no Lambda invoke, no vendor call, no `terraform init`/`plan`/`apply`, no `safe-apply`.** The apply is the issuer's under its
  own never-widen pair. Read-only AWS reads are allowed where a criterion names them.
- **NEVER ADD** an alarm, SNS topic, SES send, freshness checker or monitor (standing moratorium).
- **Restore mechanisms (CTO round-1 analysis 2.2):** you arm no timer, background task or OS task. If you ever arm one, name it in your report.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_HEALGAP-D1-W12-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file
  below, and do not weaken a check. Rows are APPEND-ONLY: never edit an existing row. The investigation file is a Markdown file holding one
  fenced ```json array: append your row INSIDE the array before the closing bracket and fence. Keep LF line endings; check `git diff --stat`
  shows only your lines before committing (the Edit tool has rewritten LF files to CRLF on this box).

<paths>
infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 3, AMENDMENT 2), cell `HG-t-15`.
<owned_cells>HG-t-15</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: HG3-t15-AC1. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~12/MDPF_HEALGAP.TO-HG-t15.retire-the-0700z-registry-rule.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG3-t15-AC1 --governing-order org/missions/D8/MDPF/MDPF_HEALGAP/task-orders/MDPF_HEALGAP.TO-HG-t15.retire-the-0700z-registry-rule.md` BEFORE the flip (several ids would be comma-separated; space-separated ids print a usage error, rc 2).
Use the HG-t-14 worker's instance `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~11/MDPF_HEALGAP.TO-HG-t14.characteristics-retime-past-the-stamp-gated-fire.proof_of_spec.json` as the SHAPE reference only.
</proof_of_spec>

**REPORT:** the files, the criterion's output, a negative control (a copy in `.scratch/` with the daily rule left in place, run through `HG_T15_TF`,
printing T15-BAD), commits, and every row you filed.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this order removes a schedule and arms no gate; the 13:15Z stamp-gated fire stays as the registry producer's only schedule and serves registry.json and holdings.json daily (read 2026-10-12: 3300 ms, as_of 2026-10-12).
comp-iam: DECLARED-NOT-APPLICABLE no grant changes: the role, its inline policy and the function are untouched; only the rule, target and permission of the retired schedule go.
comp-adversary: RUN -- the check's GONE arm names the three resources and the cron literal, its KEPT arm names what must survive, and its ONLY arm refuses any added line; mutants (rule-only removal, stamp-gated removed, stamp-gated cron altered, 07:00Z cron relocated) each print T15-BAD, a good copy prints T15-OK.
risk: WORLD -- the removal of a scheduled invocation of a served-key writer; the apply is the issuer's under its own never-widen pair.
direct_act: false -- the class is WORLD.
</preflight>

Source: CTO ADDENDUM 5 (`1.0.0_SA_CTO~DELL1`, msg 3898, `NEVER_WIDEN_ROUND3_HG_T9_T11_CTO_HALF.md`): "The 07:00Z retirement is its own pair, cut the day
the first 12:45Z fire is read and applied within one trading day." The first exercised day was read 2026-10-12 (ledger `healgap-r3-act-ht5-runner-fire-1245z-20261011`
CLOSED `f3afa83d59`). The HG-t-5 half v2 `NEVER_WIDEN_HALF_REQUEST_HEALGAP_R3_ACT_HG_T5_20261011.md` @bdee8ed6e1 section 3.
