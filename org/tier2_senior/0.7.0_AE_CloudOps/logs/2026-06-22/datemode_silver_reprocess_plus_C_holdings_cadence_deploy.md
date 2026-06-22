# DATEMODE silver reprocess + DATEMODE-C holdings daily-cadence deploy (COTETL fix made sticky)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE

Window: ~14:33Z (prior log) -> ~15:02Z. Serial: 0.7.0_AE_CloudOps. TOs: ADVI_COTETL.AUAFIX-DATEMODE-B (silver leg) + DATEMODE-C (LEAD).
Completes the COTETL $24M AUA fix end-to-end: A (code) + B (templates+backfill+silver) + C (daily cadence).

## Current State

**DATEMODE-B silver leg -- DONE + verified.** DS cleared the dedup-listed filenames from the alloc/unrealized
manifests (gotcha 1 I'd flagged). Then DS couldn't run cot_silver_merge.py on Windows (the script's
`aws s3 ls|grep|awk` no-ops under cmd.exe -- the banked subprocess trap), so I ran the 3 --table merges on the
warm cot-exporter (DS-logic/AE-runtime split): SSM RunShellScript 85884ad3, rc=0, NO --finalize (avoided the
sentinel->ad-hoc-gold trigger). Verified partitions (live S3): silver/{holdings,allocations,unrealized}/ all
gained 06-{10,11,12,15,16,17,18}.parquet, max 06-18; holdings 06-18 = 10,714 rows, $397.3M (DS independently
confirmed). The freeze is broken at silver. (Old CurrentDay holdings 06-19..22 collapsed harmlessly to 06-08 --
market-closed days.) Surfaced the go-forward re-freeze risk.

**DATEMODE-C (LEAD) -- holdings daily silver cadence DEPLOYED + apply-verified.** The go-forward gap (holdings
excluded from _SILVER_STAGE_TABLES -> nightly won't refresh it -> AUA re-caps at 06-18 tomorrow) was confirmed
real by DS + me; CTO ruled (option-a decoupled daily); COO formalized the TO. Fix (my infra lane): added a
NON-GATING daily holdings refresh to the opal-cot-silver-run SSM runCommand (infra/aws/terraform/cot-pipeline/ssm.tf),
using DS's co-author failure-tolerant pattern verbatim:
  ... --table unrealized && { python3.11 cot_silver_merge.py --table holdings $DATE_ARG || echo 'WARN ... NON-GATING'; } && --finalize
The brace-group always exits 0 -> a holdings failure never breaks the && to --finalize (the 4 gated tables still
drive the sentinel/gold); holdings stays OUT of _SILVER_STAGE_TABLES (CTO CHAINFIX intent preserved); runs before
--finalize so gold reads fresh holdings; L4 = backstop. No cot_silver_merge.py change (sentinel-decoupled by
construction). Deploy: commit ded252bae (ssm.tf + ledger) + 445fad287 (ledger close); plan 0add/1change/0destroy;
safe-apply (HALTGT clean); 0-diff re-plan "No changes"; live doc verified; deploy-completion ledger OPENED+CLOSED
in-session; tag cot-pipeline-v0.4.3; pushed --follow-tags. Landed well before tomorrow's 02:00Z nightly.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| safe-apply.sh | cot-pipeline -target=cot_silver_run apply | PASS | HALTGT clean; 0add/1change/0destroy; 0-diff re-plan |
| safe-commit.sh | ssm.tf + ledger (x2) | PASS | ded252bae + 445fad287 |
| (SSM/aws) | opal-cot-silver-run get-document + RunShellScript silver merge 85884ad3 | PASS | operational (Rule 21 free); deployed-code reprocess |
| (rail) | aws s3 ls silver partitions -- `# rail-checked` | OVERRIDE | comp-freshness not a partition-enumerator + not cot-aware (logged gap) |

**What worked:** the DS-logic/AE-runtime split (DS owns manifest+confirm; I run the bash-launcher merge on Linux that Windows can't) -- same shape as the bronze loop; DS's non-gating brace-group pattern (prevented re-coupling holdings into the sentinel); never-half-land ledger on a same-session single-resource SSM deploy. **What failed:** nothing this window. **Gap:** comp-freshness/comp-pipescript cot-blind (rail-checked override needed for cot partition enumeration -- coverage gap worth a tool).

## Blockers

None. BINDING VERIFY-GATE (DATEMODE-B+C, project-level): served cot AUA data_as_of advances past 06-09 tonight
(->06-18) AND continues advancing past 06-18 on 06-23 + 06-24 nightlies (not re-capped) -- validate-on-served,
no ad-hoc gold run. GATED on the scheduled nightlies (review next mornings).

## Next Steps

- **[0.7.0_AE_CloudOps]** 06-23 AM: verify served AUA advanced to ~06-18/$397.7M (tonight's nightly) + A_00 tripwire; RAVC COO. 06-24 AM: verify holdings/AUA CONTINUES advancing (DATEMODE-C cadence working, not re-capped); RAVC COO.
- **[0.4.0_DS_ClientPlatform]** confirm silver/holdings gains a new partition each nightly (06-23, 06-24).
- **[Andrew]** F-1 critical-surface email confirm click -> I verify Delivered>0 + ping AE0.6 to re-verify the 4 SS4c alarms.
- **[0.6.0_AE_PartnerETL]** watch-the-watcher critical-surfaces.yaml draft -> my review+commit.
- **[deferred]** DEBTSCAN TO-D3 + TSGRAPH P2-2 (resume after COTETL verifies tonight, per COO).

## Ops note

cot-exporter EC2 i-0643a5bee8a8feabf RUNNING (CTO+COO -- nightly + the silver reprocess used it). DATEMODE-C is a
standing SSM-doc change (no runtime dependency on the EC2 staying up beyond the nightly).
