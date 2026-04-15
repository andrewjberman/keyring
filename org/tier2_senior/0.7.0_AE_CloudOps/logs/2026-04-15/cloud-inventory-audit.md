# Session Log: 2026-04-15 -- Cloud inventory audit + EC2 manifest cleanup + CFIMPT_REST TO authoring

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-15
**Trigger:** Andrew direction "make sure we don't have loose resources not in terraform, taking stale code, or otherwise not properly monitored/managed"
**Related log (same session, prior):** `comp-pipescript-silver-extension.md` (COO GO, commit `41cfeeb1`)

---

## TL;DR

Account-wide inventory pass. Findings: 11 untracked S3 buckets, 13 untracked
DynamoDB tables, 3 untracked Lambda Layers, 21 untracked Lambdas (most documented),
and **5 of 6 CloudFront distributions are console-only**. Performed the cheap
remediations live (manifest sync + 2 destructive ops with explicit Andrew auth);
deferred the larger CloudFront work into 5 staged TOs ordered easiest-first.

Destructive ops (both Andrew-authorized):
- Terminated EC2 `i-05ad83c1c075de14b` (older duplicate `historical-prices-fetcher`).
- Deleted S3 bucket `opal-313476888478-wyncht` (4 demo HTML files from 2026-03-11, no live consumer).

Non-destructive remediations:
- Added `bd-assets` (i-0e6f6dc014fdcf1cd) to `EC2_MANIFEST.json`.
- Synced `seeking-alpha-scraper` instance_id (was null -> i-06376c11d8b3c3443).
- Repointed `historical-prices-fetcher` to surviving instance (i-00abf626b065373bc).
- Bumped `_last_updated` to 2026-04-15T17:05Z. Service count 12 -> 13.

Inventory report: `docs/analysis/2026-04-15_cloud_inventory_audit.md` (full gap tables + remediation priority).

5 task orders authored to retire the CloudFront gap:
- `CFIMPT_REST.001` Analytics Dashboard (EF3ZZO0F4UDHH) -- easiest
- `CFIMPT_REST.002` Trade Form UI (E2RNVVND8GSGG3)
- `CFIMPT_REST.003` Trade Reconciliation Tool (E2JC2OGK8LM1N7)
- `CFIMPT_REST.004` Market Metrics CDN (E2LPCXXBLDGWXY)
- `CFIMPT_REST.005` Public API CDN (E398SP0DG1ME0Y) -- most complex

---

## What I touched

| File | Change |
|---|---|
| `infra/aws/ec2/EC2_MANIFEST.json` | +1 service (bd-assets), 2 instance_id syncs, _last_updated bump |
| `docs/analysis/2026-04-15_cloud_inventory_audit.md` | new -- full audit report |
| `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/CFIMPT_REST.001..005.ae-cloudfront-*.md` | new -- 5 staged TOs |
| `org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-04-15/cloud-inventory-audit.md` | this log |
| AWS: terminated `i-05ad83c1c075de14b` | destructive (Andrew-authorized) |
| AWS: deleted bucket `opal-313476888478-wyncht` | destructive (Andrew-authorized) |

---

## Audit gaps -- summary table

| Resource | In AWS | TF-covered | Gap | % covered |
|---|---|---|---|---|
| Lambda functions | 138 | 117 | 21 | 85% |
| Lambda Layers | 7 | 4 | 3 | 57% |
| EC2 instances (non-terminated) | 11 (was 12, -1 termination) | n/a | -- | -- |
| DynamoDB tables | 30 | 17 | 13 | 57% |
| S3 buckets | 26 (was 27, -1 deletion) | 16 | 10 | 62% |
| CloudFront distributions | 6 | 1 | 5 | 17% (highest risk) |

Full breakdown: `docs/analysis/2026-04-15_cloud_inventory_audit.md`.

---

## Compiler Tools

| Tool | Run | Result | Used for |
|---|---|---|---|
| `comp-iam stats` / `services` | `comp-iam stats; comp-iam services` | 1 service scanned (EC2 only); 0 Lambda services parsed -- comp-iam doesn't index Lambdas yet | Identified tool-level gap; flagged as future enhancement |
| `comp-iam gaps` | `comp-iam gaps` | "No permission gaps detected" -- but only because 1 service scanned | Confirms the 124 EC2 ops vs IAM are clean; Lambda IAM coverage requires manual audit |
| Manual: `aws lambda list-functions` vs `lambda-source-map.json` | `comm -23 aws.txt sm.txt` | 2 deployed-not-tracked: test-yfinance-simple (zombie), yfinance-aapl-test (0 bytes) | Lambda inventory section 1a |
| Manual: grep `function_name =` vs deployed list | shell loop | 21 deployed Lambdas with no TF function_name reference | Lambda inventory section 1b |
| `aws ec2 describe-instances` | `--query [InstanceId,State.Name,InstanceType,Tags...]` | 11 non-terminated instances; reconciled vs `EC2_MANIFEST.services` keys | EC2 section -- caught bd-assets gap, historical-prices-fetcher dup, bd-exporter ghost entry |
| `aws dynamodb list-tables` | direct | 30 tables; `comm -23` vs grep `name = "X"` -> 13 untracked | DynamoDB section 3b |
| `aws s3api list-buckets` vs grep `bucket = "X"` | shell loop | 11 untracked (now 10 after wyncht deletion) | S3 section 4b |
| `aws lambda list-layers` vs grep `layer_name =` | direct | 3 untracked: bd-gold-common, pandas-pyarrow-layer, yfinance-dependencies | Layer section 5b |
| `aws cloudfront list-distributions` + per-id `get-distribution` | iterated | 5 console-only; captured Origins / Behaviors / L@E / WAF / Aliases per distribution | CloudFront section 6b + CFIMPT_REST.001..005 TO scope |

**Compiler-tool gap surfaced (not addressed):** `comp-iam` only sees EC2 services. Lambda services are not parsed. This makes `comp-iam gaps` blind to all Lambda IAM permissions. Worth a future TO to extend the parser -- analogous to today's `comp-pipescript deployed` silver-scope extension. Logged for follow-up; not in scope today.

**No `comp-blast` runs this session** -- inventory work doesn't have a blast radius to assess. Substituted with structural cross-reference (the `comm` + grep loops above), which is the right tool for "what's in A but not B" questions.

Compiler-log entries appended via auto-logging (no manual append needed -- `.agent_context` was set at session start with `SERIAL=0.7.0_AE_CloudOps`).

---

## Destructive ops audit trail

### EC2 termination

```
Instance:       i-05ad83c1c075de14b
Tag:Name:       historical-prices-fetcher (older duplicate)
Type:           t3.xlarge
LaunchTime:     2026-02-26T15:47:27Z
PriorState:     stopped
Trigger:        Andrew "agreed on prices fetcher" 2026-04-15
Surviving:      i-00abf626b065373bc (newer, 2026-04-15T14:00:47Z launch)
Result:         {"CurrentState": {"Name": "terminated"}}
```

Manifest updated to point `historical-prices-fetcher` at the surviving instance.

### S3 bucket deletion

```
Bucket:         opal-313476888478-wyncht
Region:         us-east-1 (default)
Objects:        4 (benchmark.html, facsimile.html, peers.html, scatter.html, all 2026-03-11)
Total size:     90,926 bytes
Content peek:   "Peer Performance Comparison -- Model Portfolios" demo HTML (Inter font, dark theme)
Trigger:        Andrew "ok delete those" 2026-04-15
Result:         All 4 objects deleted, bucket removed
```

No live consumer found (no TF reference, no Lambda env var, no CloudFront origin).

---

## Open items deferred (NOT actioned this session)

1. **`bd-exporter` manifest entry** -- has null instance_id and no AWS instance with that tag. Andrew hypothesis: "may have been an old version of bd-transactions / bd-allocations." Leaving as-is for now; safe to remove in a follow-up cleanup.
2. **`bd-price-runner` shares instance_id with bd-allocations** -- Andrew confirmed this is intentional (logical service running on the bd-allocations EC2 via SSM). Leave alone.
3. **`yfinance-aapl-test` and `test-yfinance-simple` zombie Lambdas** -- not deleted this session; flagged as P2 in the inventory report.
4. **Untracked DynamoDB tables `opal-invitations`, `opal-trade-submissions`** -- Andrew confirmed they exist but have never been used; not a priority.
5. **README "Known Issues" corrections** -- 3 entries claim Lambdas are NOT FOUND when they exist (ec2-auto-shutdown-enforcer, cost-anomaly-scanner, access-anomaly-scanner). Defer to a separate doc-update commit.
6. **`comp-iam` Lambda parser gap** -- file a follow-up TO to extend it (analogous to today's silver-scope extension).

---

## Next Steps (knock-out plan for CFIMPT_REST TOs)

Andrew direction: "knock those out beginning with the easiest ones." Recommended sequence:

| # | TO | CF ID | Why this order | Estimated time |
|---|---|---|---|---|
| 1 | `CFIMPT_REST.001` | EF3ZZO0F4UDHH | **Easiest.** New module, single S3 origin, 1 behavior, no L@E. Establishes the import pattern. | ~45-60 min |
| 2 | `CFIMPT_REST.002` | E2RNVVND8GSGG3 | Same pattern as .001 but adds to existing trade-pipeline state. Reuses .001 conventions. | ~30-45 min |
| 3 | `CFIMPT_REST.003` | E2JC2OGK8LM1N7 | Adds API GW origin to the pattern. Same pipeline as .002 (sequence required to avoid concurrent state edits). | ~60-75 min |
| 4 | `CFIMPT_REST.004` | E2LPCXXBLDGWXY | 2 S3 origins; market-overview module; refactor existing IAM grant to reference imported resource (no more hardcoded ID). | ~60-90 min |
| 5 | `CFIMPT_REST.005` | E398SP0DG1ME0Y | **Most complex.** 6 cache behaviors, new top-level module. Save for last so the pattern is well-honed. Expect 2-3 plan/edit cycles. | ~2-3 hours |

**Total estimate:** 5-7 hours of focused work, parallelizable across sessions.

**Pre-flight before each TO:**
- `git tag -l "{module}-v*" | sort -V | tail -3` for next-version selection (per memory rule).
- `unset MSYS_NO_PATHCONV` before any build script; re-export for terraform commands (per memory rule).
- Author commits: `git commit --only --author="0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent>" -- <files>` (per `feedback_commit_only_flag.md`).

**Post-flight after .005:**
- Update `pipeline_inventory.xml` (final state: 6/6 CF distributions in TF).
- Update README "Known Issues" to drop CloudFront from the list.
- Decrement counts in `docs/analysis/2026-04-15_cloud_inventory_audit.md` (or supersede with a fresh audit).
- Optional: write a small `comp-` tool or CI lint that diffs `aws cloudfront list-distributions` against TF and alerts on new console-only resources.

**Awaiting:** GO from Andrew (or COO) on `CFIMPT_REST.001` to begin.
