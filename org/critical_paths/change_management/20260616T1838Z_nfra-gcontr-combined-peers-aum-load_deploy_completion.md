# Deploy-completion ledger -- NFRA_GCONTR combined peers+aum SEV2 contract-row load (in-VPC)

**class:** deploy_completion
**status:** CLOSED COMPLETE (peers+aum LIVE+ratified, benchmark UNCHANGED, 3 rows, independently StaticTable-verified)
**opened:** 20260616T1838Z
**closed:** 20260616T1846Z
**owner:** 0.7.0_AE_CloudOps
**project / TO:** NFRA_GCONTR / TO-3 SEV2 wave (combined peers+aum)
**authorization:** COMBINED LOAD-GO (COO 183719Z). Both SEV2 rows joint-ratified: peers (CTO 182757Z + COO) + aum (CTO 183430Z + COO). SEV2 v1 ceiling COMPLETE.
**code commit:** fe645e103 (prefix-aware PENDING gate -- recognizes PENDING-CTO-COO-SIGNOFF)

## What
Rebuild the derive image (carries fe645e103) and load the two CTO+COO-ratified SEV2 contract
rows -- peers-model-portfolios + aum-model-portfolios -- into globgrph.graph_contracts in-VPC,
single combined pass (1 deploy, not 2). benchmark-model-portfolios = SKIP (already-present guard;
its live Nessie ratified_at MUST stay unchanged). Append-only; --stamp-ratified both SEV2 ids;
NO --overwrite.

## Legs -- ALL LANDED
- [x] L1: staged CVO YAML (3 rows verified on S3: benchmark/peers/aum) -> s3://.../contracts/graph_contracts.yaml
- [x] L2: CodeBuild rebuild -- **CAUGHT A STALE-SOURCE MISS**: the CodeBuild source is an S3 zip (build-source/derive-runner-source.zip), NOT git. First `start-build` (6b4eda41) rebuilt the STALE zip (pre-fe645e103). The plain dry-run (L3) discriminator caught it: write=2 instead of 0. Re-zipped source from working tree (verified _is_pending_ratified x3 IN the zip), uploaded, rebuilt (9d0e9261 SUCCEEDED).
- [x] L3: in-VPC plain --dry-run (task 3641be33) on the FRESH image -> benchmark SKIP (already-present); peers+aum SKIP (PENDING -- needs --stamp-ratified); PLAN write=0. CONFIRMS fe645e103 live (gate recognizes PENDING-CTO-COO-SIGNOFF).
- [x] L4: in-VPC real --stamp-ratified peers-model-portfolios,aum-model-portfolios (NO --overwrite; task 0210f291) exit 0 -> CONTRACTS_APPENDED count=2, ratified_at_pin=a7bc0aed07a0313f... (real Nessie hash). benchmark SKIP (already-present).
- [x] L5: WRITE_VERIFY peers period_defs=9 + aum period_defs=4; table_row_count=3. INDEPENDENT contract_engine StaticTable read (status ok, 3 rows): benchmark ratified_at=6f21c75ca78040ee... period_defs=11 UNCHANGED; peers ratified_at=a7bc0aed... pd=9 writer=yang-pipeline-lambda-role; aum ratified_at=a7bc0aed... pd=4 writer=smartx-ingestion-lambda-role.
- [x] L6: CVO byte-verify ping (loaded period_defs keys) + RAVC2 COO + CC CTO.

## Closure evidence
- LOADED period_defs keys (StaticTable-confirmed, match CVO YAML byte-for-byte):
  - peers(9): ['1M','QTD','1Q','YTD','1Y','Since Inception','_return_basis','_per_period_fields','_percentile_source']; forbidden_writers=[]; models=[UST,ST,INT,LTC,LTA]
  - aum(4): ['as_of','aum_basis','timeseries','_per_firm']; forbidden_writers=['smartx-exporter-role']; models=[UST,ST,INT,LTC,LTA,Opal Blend 5050 Int Ltc,Opal Blend 5050 St Int]
- benchmark row PROVABLY untouched (already-present guard; ratified_at + period_defs unchanged). SERVED/StaticTable-verified, not rc=0.
- LESSON banked: globgrph derive CodeBuild builds from an S3 SOURCE ZIP, not git HEAD -- a code fix needs the zip re-built+uploaded BEFORE start-build, else it rebuilds stale. The plain-dry-run discriminator (write=0 expected) is the image-content verification.

## Close criteria
peers + aum rows LIVE + ratified (ratified_at = real Nessie hash) on Nessie main, StaticTable-verified;
benchmark row UNCHANGED; 3 rows total. Then status -> CLOSED COMPLETE + RAVC2.

## Rollback
Append-only on a 2-row table (benchmark + ... wait, 1-row pre-load); a mis-loaded SEV2 row's
contract_id can be overwritten/retired via a Nessie commit (active=false). Recoverable, no data
path touched. Finish-in-session or roll back -- no stranded leg.

## Note
Post-06-17: aum's smartx-exporter EC2 forbidden_writers tripwire + NNA policy-limb go Q2-ENFORCED
when the EC2-WRITES derive fix lands (CVO re-verifies on the 06-17 nightly). Today aum's EC2
dual-writer containment = EC2-stopped + IAM + value-limb (declarative tripwire).
