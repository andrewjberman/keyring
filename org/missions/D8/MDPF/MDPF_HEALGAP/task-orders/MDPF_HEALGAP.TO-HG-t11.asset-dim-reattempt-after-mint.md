# TO MDPF_HEALGAP.TO-HG-t11 -- round 3 HG-t-11: the BD asset-dim pull is re-attempted after the 22:20Z session mint, and a complete day no-ops
<to_id>MDPF_HEALGAP.TO-HG-t11</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.9.0_WK_MDPF_HEALGAP~8</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-11` (`decompositions/MDPF_HEALGAP_DECOMP.md`, ROUND 3) |
**outcome_ref:** FWD-6 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`HG-t-11`. FWD-6: a scheduled pull that leans on a session minted elsewhere recovers, or is shown not exposed. The asset-dim pull
(`bd-asset-dim-pipeline-trigger`, `cron(10 22 ? * MON-FRI *)`) mints its bearer from the 49F session secret that the 22:20Z session
chain refreshes, so a 22:10Z fire on a lapsed session fails and nothing re-runs it. This cell adds a re-attempt fire at 22:40Z on the
SAME trigger (after the mint) and a guard in the SSM document that makes a day whose bronze already landed a no-op (CTO ruling 3411,
option (d): the guard lives in the document, no new IAM, no new Lambda).

**The estate, read at the base.**
- `infra/aws/terraform/bd-pipeline/eventbridge.tf:146-170`: `bd_asset_dim_pipeline` rule, its target `module.asset_dim_trigger` and permission.
- `infra/aws/lambda/bd-pipeline/bd-asset-dim-trigger/lambda_function.py`: no guard; starts the instance if stopped, then
  `ssm.send_command(DocumentName='opal-bd-asset-dim-download')`. NOT edited by this cell. Its role `bd_daily_trigger` is shared by 7
  triggers and holds no S3 read; do not touch it.
- `infra/aws/ssm/opal-bd-asset-dim-download.json`: the REST pull (no Playwright): stages a producer tree, runs
  `pull_bd_asset_dim_rest.py pull ... --as-of`, which writes `bronze/assets_dim_rest/<UTC date>/assets_dim_rest.parquet` (the key
  comes from the generated pin `_asset_dim_rest_pin.py`: `key_prefix`, `object`, `bucket`), then rebuilds `silver/bd_assets_dim.parquet`.
- **The guard's key.** Ruling 3411 named `silver/assets/<D>.parquet`, the Playwright-era artifact. The REST path does not write it, so
  the guard keys on today's UTC bronze partition (decomposition ROUND 3, issuer ruling). A failed read (a missing key, a 403, any
  non-zero exit) is NEVER "exists": the download runs.

**Build -- the issuer prepared and pre-validated two reference patches against HEAD (they apply cleanly to a pristine checkout and both
criteria below read OK on them). Apply them, run the criteria, and fix minimally only if something differs in your tree:**
1. `git apply org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_PATCHES/t11_eventbridge_tf.patch` -- adds
   `module "asset_dim_reattempt_rule_name"` (system `blackdiamond`, scope `49financial`, function `asset-dim-reattempt`, kind `daily`,
   built name `blackdiamond-49f-asset-dim-reattempt-daily`), rule `bd_asset_dim_reattempt` at `cron(40 22 ? * MON-FRI *)`, its target
   (the SAME `module.asset_dim_trigger.function_arn`) and permission. The tag `Name` is the module's output, never typed.
2. `git apply org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_PATCHES/t11_ssm_document.patch` -- inserts 28 `runCommand`
   elements after the `chown -R ec2-user:ec2-user /opt/bd-exporter` line: a staged `hg_guard.py` (heredoc) that HEADs today's bronze
   key, run as `ec2-user`; on rc 0 it logs `SKIP-COMPLETE`, uploads the log, ARMS the shutdown (`shutdown -h +2 &`, so the instance is
   not stranded) and `exit 0`; otherwise the document continues unchanged into the pull.

Leave the document's JSON formatting as it is (2-space indent, one string per line); the patch is an insertion only.

### ACCEPTANCE

<criterion id="HG3-t11-AC1" cell_refs="HG-t-11"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_CHECKS/hg_r3_rules.py --t11</invocation><expect>T11-OK</expect></criterion>
`HG3-t11-AC1` -- the existing rule stays at `cron(10 22 ? * MON-FRI *)`; exactly one other rule targets the same trigger on MON-FRI after 22:20Z, with a permission.

<criterion id="HG3-t11-AC2" cell_refs="HG-t-11"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_CHECKS/hg_t11_assetdim.py --ssm</invocation><expect>SSMGUARD-OK</expect></criterion>
`HG3-t11-AC2` -- the document's own shell, run with the instance's tools stubbed: guard read OK -> the pull is not started, the shutdown is armed, rc 0; guard read failed (rc 1 and 2) -> the pull runs.

<expected_criteria>HG3-t11-AC1 HG3-t11-AC2</expected_criteria>

Run each invocation from the worktree root. Both FAIL at the base (`T11-BAD ...`, `SSMGUARD-BAD no 'runuser ... hg_guard.py' guard line`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no Lambda invoke, no `ssm send-command`, no `ssm update-document`, no vendor call, no `terraform init`/`plan`/`apply`,
  no `safe-apply`.** Every apply, and the first guarded fire, is the issuer's at the drain.
- **49F leg (CloudOps conditions, msg 1814, as carried by the round-3 draft):** a send that writes a firm data bucket, or assumes the 49F
  principal outside the runner's own job, is told to the laptop FIRST; every `mdpf-daily-runner` send is reported after; 49 Financial data
  never enters another firm's tree. This cell sends nothing and reads no firm data: the criteria run on stubs and static text.
- **NEVER ADD** an alarm, SNS topic, SES send, freshness checker or monitor. Do NOT edit the trigger Lambda or the `bd_daily_trigger` role.
- **Restore mechanisms (CTO round-1 analysis 2.2):** you arm no timer, background task or OS task. If you ever arm one, name it in your
  report with its state at your close.
- **Refusal clause.** If a criterion cannot be met as written (a patch does not apply, a gate refuses a name), stop, write the reason in
  your report and a surprise row (id `MDPF_HEALGAP-D1-W8-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or
  `BLOCKING`) in the investigation file below, and do not weaken a check. Rows are APPEND-ONLY: never edit an existing row. Write the
  file with LF line endings and check `git diff --stat` shows only your added lines before committing.

<paths>
infra/aws/terraform/bd-pipeline/eventbridge.tf
infra/aws/ssm/opal-bd-asset-dim-download.json
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 3, the enrichment), cell `HG-t-11`.
<owned_cells>HG-t-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG3-t11-AC1, HG3-t11-AC2. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~8/MDPF_HEALGAP.TO-HG-t11.asset-dim-reattempt-after-mint.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG3-t11-AC1 HG3-t11-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits, and every row you filed.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE comp-schedule is the gate ledger and this order arms no gate; the new weekday fire at 22:40Z on the existing trigger sits after the 22:20Z session mint (bd-49f-fees-session-daily) and the 22:10Z fire is unchanged. The re-attempt starts the instance once more on a weekday (a start/stop cost, no new vendor act on a complete day).
comp-iam: DECLARED-NOT-APPLICABLE no new grant: the guard HEADs a key the instance role already reads (it writes and reads the firm bucket for the pull itself); the shared trigger role is untouched (CTO ruling 3411).
comp-adversary: RUN -- `comp-adversary compose` over this order 2026-10-11 03:39Z: 1 cited commit verified, 10 cited paths (1 GONE: this order's own proof instance, not yet written), neighborhood 2 members (decomposition, PRD), 0 proof instances; it has no view of the instance's runtime. The guard's failure direction is toward running the download; its skip path arms the shutdown so the instance is not stranded. Residual named: bronze present with a failed dim rebuild reads "complete" until the next day's run.
risk: WORLD -- an infrastructure path and an SSM document on a 49F leg; the applies are the issuer's at the drain under their own never-widen pair; rollback = the prior document version and the rule's removal.
direct_act: false -- the class is WORLD.
</preflight>

Source: PRD v0.3 FWD-6; CTO round-2 analysis @1974b85f4e section 3 item 3; rulings E and 3411; decomposition round 3.
