# BMKAUD — Exhaustive Writer Census: `s3://opal-data-portal-v2/json/benchmarks/*`

**Andrew-direct (via CTO 153649Z):** *"make sure there is no other writer that will come in and fuck this up from SmartX."* Census FIRST (proof we found them all), then neutralize non-canonical + structural Deny backstop. **Method:** TF grep of every `s3:PutObject` grant to `opal-data-portal-v2` across `infra/aws/terraform/` (authoritative for TF-managed IAM) + code-path confirmation.

## VERDICT: 1 canonical writer + 4 non-canonical principals that CAN write the benchmark surface
The structural bucket-policy Deny on `json/benchmarks/*` (except the canonical yang role) is justified: 4 distinct non-canonical principals can reach the prefix (1 active orphan + 3 over-broad latent grants). IAM-tightening each is whack-a-mole; the Deny neutralizes all at once.

## CENSUS TABLE
| # | Principal / resource | TF grant (Resource) | Reaches json/benchmarks/*? | Writes today | Disposition |
|---|---|---|---|---|---|
| **A (CANONICAL)** | `yang-pipeline-lambda-role` → **yang-model-portfolio-benchmarks** | `opal-data-portal-v2/*` (bucket-wide) — yang-pipeline/iam.tf:44-45,64-65 | YES | YES — the 3 benchmark JSONs (canonical) | **KEEP** (sole legit writer; whitelist in the Deny). Grant is over-broad (`/*`) but it's the canonical writer. |
| **B** | `smartx-model-monthly-pull-role` → **smartx-model-monthly-pull** | `json/benchmarks/*` — model-perf-pull.tf:102 | YES | was daily (now DISABLED f38353b0f) | **RETIRE** (Finding #1 orphan). Writes BOTH `_smartx_model_monthly.json` (OUT_KEY) AND `_smartx_model_daily.json` (OUT_KEY_DAILY, L98/422/462) — **resolves the "B3 daily producer" question: NO separate daily lambda; one lambda writes both sidecars.** Full-retirement plan = 056fb2855. |
| **C** | `smartx ec2_exporter` role → **smartx-exporter EC2** | `opal-data-portal-v2/*` (bucket-wide) — smartx-pipeline/iam.tf:178 (ec2_s3_access) | YES (bucket-wide) | DORMANT — runs `generate_benchmark_performance.py` writing `json/benchmarks/benchmark_returns.json` (own period math), but NO cron/autostart invokes it | **NEUTRALIZE** (Finding #3). Latent manual-run clobber/desync. Remove/repoint the script off the live key; the Deny backstops the role's bucket-wide grant. |
| **D** | `smartx ingestion_lambda` role → **opal-smartx-ingestion-pipeline** | `opal-data-portal-v2/*` (bucket-wide) — smartx-pipeline/iam.tf:95-115 (ingestion_s3) | YES (bucket-wide) | writes its own ingestion artifacts; CAN write json/benchmarks (over-broad grant), no evidence it does | **LATENT** — over-broad grant. Recommend tighten to its actual prefix; the Deny backstops it regardless. |
| **E** | `news-pipeline` lambda role | `opal-data-portal-v2/json/*` — news-pipeline/iam.tf:110 | YES (`json/*` ⊇ json/benchmarks) | writes json/semantic-trending, json/sentiment; CAN write json/benchmarks, no evidence it does | **LATENT** — over-broad `json/*` grant. Deny backstops. |
| — | portfolio-management | `/portfolio-management/*` only (main.tf:305) | NO | — | EXCLUDED (prefix-scoped away) |
| — | market-overview | `/market,/sentiment,/macro,/trending` (+ bucket-level List) | NO | — | EXCLUDED (prefix-scoped away from benchmarks) |
| — | data-refresh | `/security_scanner/*` only (main.tf:69) | NO | — | EXCLUDED |

## COMPLETENESS NOTES
- Census is over TF-managed grants (source of truth for IaC). Non-TF/manual IAM grants or root/admin creds are NOT enumerable here — **which is exactly why the bucket-policy Deny (a resource-policy backstop) is required**: it denies non-canonical writes regardless of any identity-policy Allow (TF-managed or not, including the un-attributable 5/29-class dev cred).
- The 2 SmartX sidecars (`_smartx_model_monthly.json` + `_smartx_model_daily.json`) are FE-unconsumed post-revert (CVO Component-3 PASS + repo grep zero consumers).

## LOCK-DOWN PLAN (3 layers — folds into the held TF batch 056fb2855, applies HELD for Andrew-ratify)
1. **RETIRE** smartx-model-monthly-pull (B) — full destroy (lambda+TF+scheduler+source-map), neutralizes both sidecars. Plan captured (8 resources).
2. **NEUTRALIZE** the EC2 dual-writer (C) — remove/repoint `generate_benchmark_performance.py` off `json/benchmarks/benchmark_returns.json`; record disposition in EC2_MANIFEST.json (DT CC).
3. **STRUCTURAL DENY (the durable guarantee):** import the unmanaged `opal-data-portal-v2` policy (2 OAC GetObject statements, exact replication + 0-diff proof) → add write-only Deny:
   `Deny {s3:PutObject,s3:DeleteObject}` on `arn:aws:s3:::opal-data-portal-v2/json/benchmarks/*` with `Condition ArnNotLike aws:PrincipalArn = [assumed-role/yang-pipeline-lambda-role/*, <narrow break-glass>]`. NEVER GetObject (OAC reads untouched). After apply, ONLY the canonical yang lambda role can write the benchmark serving keys — every other principal (B/C/D/E + any rogue/manual/dev-cred) is structurally DENIED.
   - (Companion MDPF Deny on `platinum/mdpf/aggregate_aua/*` excepting mdpf_runner rides the same import pass — both serving surfaces locked.)
**Optional grant-tightening (defense-in-depth, non-blocking):** narrow the bucket-wide `/*` grants (A yang, C ec2_exporter, D ingestion) + `json/*` (E news) to their actual prefixes — the Deny makes this non-urgent but it's good hygiene.
