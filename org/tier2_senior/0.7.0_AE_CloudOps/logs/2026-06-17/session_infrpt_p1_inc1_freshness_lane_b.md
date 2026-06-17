# NFRA_INFRPT.P1 increment-1 -- DATA FRESHNESS section + sec-F dogfood fix + cot non-advancement gate (0.7.0_AE_CloudOps~B)

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, IMPLEMENT, DIAGNOSE, COORDINATE

Lane: 0.7.0_AE_CloudOps~B (distinct cold-start session 2026-06-17; folder = base 0.7.0_AE_CloudOps). Window: session start -> inc-1 close.

## Current State

NFRA_INFRPT.P1 increment-1 is **DEPLOYED + in-Lambda-verified + tagged + pushed**. The daily infra report (`opal-infrastructure-monitor`) now carries a real per-pipeline DATA FRESHNESS section.

- **Lambda:** `opal-infrastructure-monitor` (TF `infra/aws/terraform/shared-infra/infra-monitor.tf`, resource `aws_lambda_function.infra_monitor`; source `infra/aws/lambda/infrastructure_monitor/lambda_function.py` + `openai_cost_tracker.py`). Deployed sha256 `Ev6MHc0LgyaJ++hFZFZkzbM7+Tleg7QLja1OgcdGIjI=`, 24K 2-file zip at `s3://opal-313476888478-lambda-artifacts/shared-infra/opal-infrastructure-monitor.zip`. py3.12/512MB/120s, layer anthropic-sdk-deps. Tag `shared-infra-v1.23.0` (commit `014ed80aa`, pushed origin/CLOUD).
- **New section B (DATA FRESHNESS):** `check_data_freshness()` reads the DS-generated manifest `s3://opal-data-portal-v2/infrastructure/freshness_manifest.json` (no hardcoded paths), head-objects / lists each served artifact, grades age vs per-artifact warn/fail thresholds. Severity-gated (ERROR past-fail -> RED; WARN past-fail -> WATCH advisory). `manifest_age` meta-freshness line (missing manifest -> RED; >7d -> WATCH = absence-coverage). Action-first render (one summary line per pipeline + detail only on WATCH/RED); alert (email subject) trips only on overall RED. Emits a P3-consumable structured shape (report["sections"]["data_freshness"]).
- **cot non-advancement gate (CTO ruling):** artifacts with `as_of_source="silver-partition-key"` are graded on the MAX date-partition key under the silver prefix (BD's stamped as-of), NOT artifact mtime -- the snapshot artifact is rewritten each run with frozen-date data so mtime false-cleans a frozen feed. Emits as_of + advanced-vs-baseline (the non-advancement metric); WARN severity keeps the snapshot tables ADVISORY (never RED) pending Andrew's interval-N. Helpers `_extract_date` / `_max_date_partition_key` (list keys only). `cadence="deprecated"` -> advisory WATCH (yang_volatility_data stub).
- **sec-F dogfood fix:** `fetch_error_logs` was sending pseudo-regex `INIT_REPORT.*error` as a CloudWatch FilterLogEvents `filterPattern` -> `InvalidParameterException: Invalid character(s) in term '*'` (confirmed against the DEPLOYED Lambda + CloudWatch logs: fired on trade-parquet-batch-export / infrastructure-daily-snapshot / inf-tax-daily). Replaced the per-pattern loop with one valid OR-pattern `?ERROR ?Error ?Exception ?Traceback ?"Task timed out" ?ImportModuleError ?Timeout`.
- **IAM:** new inline policy `MonitorDataFreshnessRead` on `opal-portal-lambda-role` (the shared role): `opal-data-inf` GetObject + ListBucket (inf mtime freshness; the shared role already covered bd/portal-v2/news/market-data); `opal-data-cot` ListBucket-ONLY (cot partition-key signal lists key names, never reads cot contents -> firm-separation-respectful cross-firm ops monitor). comp-iam gaps = 0 missing.
- **OPLMCP (P1 queue item #1):** ground-truthed COMPLETE -- `.01`/`.03` live (curl https://mcp.opalinvest.dev = 503 over valid wildcard TLS = CLOSED-503 invariant; tag m365-mcp-gateway-v1.0.0). `.02` IT-gated (Andrew Entra app-regs). `.04` is CTO-led. Nothing to rebuild.

**In-Lambda verification (deployed IAM, archive `infrastructure/reports/2026-06-17/15-08-07.json`):** OVERALL RED; bd-gold 25 OK/6 WATCH/1 RED, inf 25 OK/4 WATCH/2 RED, cot 1 OK/6 WATCH/1 RED, mdpf OK, model-portfolios WATCH, news OK, nna OK. MATCHES local verify exactly -> deployed IAM sufficient, zero AccessDenied false-REDs. cot live: holdings as-of 6/9 WATCH (advanced 0d vs baseline), realized 6/17 OK, transactions 6/9 RED.

**4 ERROR-tier RED findings (the section's first real catches, all live-S3-confirmed TRUE):**
1. `bd_silver_unrealized` -- last write 06-11 (5.7d), bd otherwise fresh ~10h.
2. `inf_silver_accounts_dim` -- latest.parquet frozen 2026-04-29 (48d); inf gold fresh -> likely superseded-path config-debt.
3. `inf_silver_aum_snapshot` -- prefix EMPTY (missing).
4. `cot_silver_transactions` -- partitions stuck 06-09 while realized advances to 06-17 = real silent silver-merge freeze (CTO steer: STAYS ERROR/RED, must alarm). Routed to 0.4.0_DS for root-cause under ADVI_COTETL.

## Deployment Sequence (AE)

code -> ds-commit-gate (clean) -> safe-commit (1591d9ef8 + 011822ac9) -> build-and-upload.sh shared-infra (sha Ev6MHc0...) -> source-map commit (23e54a189) -> terraform plan (1 add / 1 change / 0 destroy) -> RAVC1 to COO+CTO -> safe-apply (HALT-gate passed; 1 added, 1 changed, 0 destroyed) -> terraform plan 0-diff ("No changes") -> record-terraform-deploy.sh shared-infra --version shared-infra-v1.23.0 (014ed80aa) -> git tag -a shared-infra-v1.23.0 -> push --follow-tags (GCM workaround; b83adde29..014ed80aa + tag).

## Verification (paste)

```
terraform plan (post-apply): No changes. Your infrastructure matches the configuration.
in-Lambda archive 15-08-07.json: OVERALL RED, manifest_present True, age_h 0.3
  cot_silver_holdings: BD as-of 2026-06-09 (207.1h) > warn 72h -> WATCH (advanced 0d vs baseline 2026-06-09)
  cot_silver_realized:  BD as-of 2026-06-17 (15.1h fresh) -> OK
  cot_silver_transactions: BD as-of 2026-06-09 (207.1h) > fail 72h -> RED
curl https://mcp.opalinvest.dev = HTTP 503 / TLS verify 0 (OPLMCP .03 CLOSED-503 invariant holds)
```

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| pipescript | `--list` | PASS | 25 named threads / 134 sub; grounded the freshness coverage set |
| comp-freshness | `--list` | PASS | cadence config = bd(32)+inf(31)+DDB(2) ONLY -> cot/mdpf/yang/news/NNA-served = coverage GAP (the P1 finding driving the manifest design) |
| comp-iam | `service opal-infrastructure-monitor` | PASS | located TF (shared-infra/infra-monitor.tf), picked up the new manifest get_object |
| comp-iam | `gaps` | PASS | 0 missing after the inf+cot grant; deny-present items = unrelated bd->cot firm-separation guardrails |
| ds-commit-gate.sh | lambda_function.py (x3) | PASS | py_compile + AST + ruff clean each edit |
| build-and-upload.sh | `shared-infra opal-infrastructure-monitor` | PASS (2nd) | 1st blocked on ADHC_DRIFTD.002 parity (typing_extensions.py); removed the unused cruft, rebuilt |
| safe-apply.sh | `-chdir=shared-infra apply` | PASS | HALT-gate passed; 1 add / 1 change / 0 destroy |
| record-terraform-deploy.sh | `shared-infra --version shared-infra-v1.23.0` | PASS | CHANGELOG + source-map recorded |

**What worked:** comp-freshness --list immediately exposed the bd/inf-only coverage (the central manifest-design finding); comp-iam service+gaps cleanly scoped the inf/cot grant. The Phase-3 local-then-in-Lambda verify caught a real severity-gating bug (WARN feeds were false-REDing) BEFORE deploy. **What failed:** none blocking. The aws CLI invoke timed out (60s read-timeout < ~70s Lambda) and botocore retried ~4x -> ~4 report emails to Andrew; verified off the S3 archive instead (no re-invoke). Lesson: use `--invocation-type Event` (async) + read the archive. **Gap:** comp-freshness covers only bd/inf -> cot/mdpf/yang/news need real configs (DS authored them in 1b). Monitor source_dir carries pre-layer vendored cruft (subdir packages) -- harmless to the artifact, noted hygiene follow-up.

## MCP traffic

~20 messages. Significant: MSTR first-message (priority queue) -> CTO correction (OPLMCP done, first-move = INFRPT P1) -> COO exact-serial GO for P1 -> contract negotiation with 0.4.0_DS (proposed shape -> 4 deltas -> LOCKED) -> DS 1a + 1b LANDED (manifest live) -> CTO non-advancement RULING (via COO) + 0.6.0_AE cot cheap-signal spec -> RAVC1 (plan) -> COO CONCUR -> CTO transactions-reconcile + RED-steer -> RAVC2 (inc-1 close, joint with DS). 4 RED findings routed to DS.

## Blockers

None. Increment-2 (DRIFT section E) is COO-sequenced (awaiting GO) -- a planned dependency, not a blocker.

## Next Steps

- **[2.0.0_SA_COO]** Confirm the inc-1 RAVC2 + sequence increment-2 (DRIFT section E). Caveat: must NOT flag the 2 now-in-TF Lambdas (snapshot + monitor) as drift; surface NEW drift since last report (state-change).
- **[0.4.0_DS_ClientPlatform]** Root-cause the cot `silver/transactions` merge-freeze (stuck 06-09 vs realized 06-17), under ADVI_COTETL. Triage #2/#3 (inf superseded-path config-debt) + #1 (bd_silver_unrealized).
- **[0.7.0_AE_CloudOps~B]** Increment-2 (DRIFT) on COO GO. Hygiene follow-up: monitor source_dir vendored-cruft cleanup (subdir packages). Banked lesson: async Lambda invoke for verification.
- **[0.7.0_AE_CloudOps~B / Andrew]** OPLMCP .02 stays IT-gated (Entra app-regs); execute the go-live leg when the 5 values land.

## Files Modified

See commit messages: `1591d9ef8` (freshness section B + sec-F + inf IAM + TO flip), `de2e361e8` (remove typing_extensions.py), `c6b9ad73a` (source-map), `011822ac9` (cot non-advancement branch + cot IAM + deprecated), `23e54a189` (source-map re-upload), `014ed80aa` (record deploy + CHANGELOG).
