# Session Log: Chain #22 (gold-d) + inf-pipeline-v1.7.52 Lambda Bundle Deploy

**Agent:** 0.6.1_AE_PartnerETL
**Date:** 2026-05-12
**Session window:** ~22:13Z – ~22:43Z (ongoing standby for chain #23)
**Branch:** CLOUD
**Continues:** `session_chain_dispatch_chains14_through_18.md` (chains #14-21 closed 19:54Z)

---

## Summary

Andrew direct GO + DS~D bump + COO GO converged on a single chain #22 gold-d fire at 22:14:26Z. Chain exit=0 in 13 minutes. RAVC2 scorecard: 7/8 PASS (sentinel exact), 1 FAIL (IWM $0 in leaderboard — root-caused by DS as INF_D_00c rep_bucket filter dropping account_team-attributed holdings). Followed by inf-portal-advisor-publisher Lambda bundle deploy (a186ffa9b + 796f5bbd6) — orphan drift on inf-unified-account-dim-daily forced COO Option C scoped `-target` apply. Tag inf-pipeline-v1.7.52 pushed.

---

## Chain #22 — gold-d (Andrew + DS~D + COO triple-GO)

| Field | Value |
|---|---|
| Mode | gold-d |
| Snapshot date | 2026-05-12 |
| Lambda invoke | `inf-gold-trigger` payload `{"mode":"gold-d","snapshot_date":"2026-05-12"}` StatusCode 200 |
| EC2 instance | i-0ed5afded2ebd4ed4 (started from stopped) |
| EC2 launch | 22:14:26Z |
| Chain start | 22:15:32Z (first platinum write) |
| Chain end | 22:27:39Z (CHAIN COMPLETE, exit=0) |
| Wall | ~13 min |
| Runner log | `s3://opal-data-inf/gold/logs/runner_20260512_222741.log` (1,079,256 B) |
| Artifacts | 25 fresh in platinum/firm/ |

### Spot-check scorecard

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | DS~D donut firm signed NNA | PASS | `views.nna.current.geo.donut.total = $562,384.65` (firm NNA, NOT $203M AUA) |
| 2 | DS~D WA.value signed state NNA | PASS | `WA.value = -$319,225.07` (signed NNA, not AUA) |
| 3 | DS~D WA.aua sidecar preserved | PASS | `WA.aua = $173,494,064.22` (informational) |
| 4 | DS~D WA.by_city populated | PASS | 16 cities incl. FERNDALE, Snohomish, Seattle, Everett, Lynnwood, Mill Creek, Mukilteo, ..., Other |
| 5 | DS~D sentinel sum(by_city)==WA.value | PASS exact | `-319,225.07 == -319,225.07` to the cent |
| 6 | DS~D Other catchall in by_city | PASS | `Other: {total: -$11,844.96, count: 22}` |
| 7 | DS~C item 1 bond funds in top-N | PASS | `firm_concentrations.securities` top-10 has HTRB / BAGIX / BSIIX (fixed_income) alongside VOO/JIJIX/CIVIX/AAAZX |
| 8 | DS~C item 2 IWM AUA $510K | **FAIL** | `leaderboard` IWM `total_aua = $0.00` across QTD/YTD/MAX (39 accounts / 11 clients carried but AUA=0) |

### Anomalies (advisory pass to DS)

- State key `"34"` in donut.segments: `{value=-$1,000, aua=$0, count=1}` — numeric-string state slipped state-normalization.
- State key `"Other"` at donut level: `{value=+$75,744.52, aua=$0, count=1}` — single-account residual; expected catchall, but flagged for DS~D confirm.

### IWM root cause (DS RAVC2)

Commit `75a29f9ae` — INF_D_00c.portal_leaderboard.py canonical account_team attribution. Root cause: INFLBIWMALIGN (`56c1082bc`) only removed IWM from the entry-enumeration `_placeholder` filter; underlying `aua_by_adv` source kept the `rep_bucket == 'individual'` filter at INF_D_00c:731. IWM's 89 firm-bucket holdings rows ($510K) were filtered out, 43 mis-tagged individual-bucket rows flowed to peter_lee/patrick_scanlan. Fix uses `account_team` join + sister fix on `nna_by_adv`. S3-deployed; chain #23 verifies.

---

## inf-pipeline-v1.7.52 Lambda Bundle Deploy

### Bundle scope

| Commit | Brief | LOC | Description |
|---|---|---|---|
| `a186ffa9b` | Brief A + Brief C addendum | +173 / -28 | book.json schema ext (composition + top_holdings + headline + historical_quarters + clients[].relationship_since); TIMESERIES_FLOOR_DATE=2020-04-01 (replaces TIMESERIES_MONTHS=36) |
| `796f5bbd6` | Brief B #4 | +57 / -4 | IWM Avg Fee Rate 0.0 bps fix — holdings-AUA fallback in `_aggregate_billing_per_advisor` when billing's ending_mv=0 |

### Build-and-upload

```bash
unset TMPDIR    # bun-only env per MEMORY.md
bash infra/aws/lambda/ci/build-and-upload.sh inf-pipeline inf-portal-advisor-publisher
```

- New SHA: `x2fw28YjNitQ8rvc/Oo7L8Id2qZRuKRY5L1LBjILaZk=`
- Old SHA: `S+YUKAfTNUNG/aAS6+oj9IU7++LKdxntapESlvAAXuM=`
- Upload exit 0
- Source map commit: `07d2855f5` (artifact upload)

### Orphan drift incident

`terraform plan` surfaced 19 in-place updates. Two source_code_hash diffs (real code) and 17 cosmetic s3_object_version drifts.

| Lambda | Hash diff | Authorized? |
|---|---|---|
| inf-portal-advisor-publisher | mine, expected | YES |
| **inf-unified-account-dim-daily** | un-attributed S3 upload at 16:47:00Z (no source map update, no recent commit) | **NO — orphan** |

MCP'd COO 22:38Z with Option A (apply with orphan) / B (back-out) / C (-target scoped apply). COO ruled Option C: scoped apply for advisor-publisher only; orphan investigation TO files tomorrow.

### Scoped apply

```bash
.tools/terraform.exe -chdir=infra/aws/terraform/inf-pipeline apply \
  -target=module.inf_portal_advisor_publisher.aws_lambda_function.this \
  -auto-approve
```

- Plan: 0 to add, 1 to change, 0 to destroy
- Apply exit 0, 1 changed in 6s
- Re-plan: advisor-publisher diff CLEARED. Orphan + 17 cosmetic diffs remain (expected, self-correct on next clean apply).

### Tag + push

- record-terraform-deploy.sh hit a bun bug on CHANGELOG.json write (`TypeError: cl.entries.unshift is not a function`) — source map stamps still landed but inline commit aborted because safe-commit.sh detected COO's concurrent staged session log (correct contamination guard).
- Manual recovery: re-ran safe-commit.sh with explicit pathspec → commit `c8bb6e605`.
- `git tag -a inf-pipeline-v1.7.52` + `git push origin CLOUD --follow-tags`: confirmed `16c337f66..c8bb6e605` + tag pushed.
- safe-deploy hook reported "no deploy-scope script files detected, nothing to do" (expected — Lambda zip already in S3 via build-and-upload).

---

## Communications

| # | Direction | Subject |
|---|---|---|
| 1 | AE→DS~D | RAVC1 chain #22 fired per Andrew + your bump |
| 2 | AE→COO | RAVC1 Andrew GO chain #22 fired |
| 3 | COO→AE | GO chain #22 retroactive scope (items 1+2) |
| 4 | COO→AE | ACK RAVC1 — multi-source GO convergence noted |
| 5 | COO→AE | Heads-up incoming Lambda deploy ask |
| 6 | AE→COO | ACK heads-up — Lambda sequenced post-chain #22 |
| 7 | DS→AE | RAVC2 Lambda commit `a186ffa9b` — ASK hold-and-bundle for Brief B |
| 8 | AE→DS | ACK + agree to HOLD-and-bundle |
| 9 | AE→COO | FYI Lambda deploy HELD per bundle ask |
| 10 | COO→AE | ACK HOLD-and-bundle; chain #23 sentinel-fire preferred |
| 11 | AE→COO | RAVC2 chain #22 EXIT=0 scorecard 7/8 PASS |
| 12 | AE→DS~D | RAVC2 chain #22 — NNA fix PASS all 5 paths |
| 13 | AE→DS | RAVC2 chain #22 — bond funds PASS; IWM $510K FAIL |
| 14 | DS→AE | RAVC2 Brief B `796f5bbd6` pushed — bundle ready |
| 15 | AE→DS | ACK bundle deploy starting build-and-upload |
| 16 | COO→AE | ACK chain #22 RAVC2 — IWM FAIL routed to DS~C |
| 17 | DT→AE | REQ — commit your AE-lane 2026-05-12 logs |
| 18 | AE→DT | ACK — folding into bundle deploy cycle |
| 19 | DS→AE | RAVC2 IWM regression fix `75a29f9ae` shipped |
| 20 | AE→DS | ACK IWM fix — chain #23 verify; bundle BLOCKED on orphan |
| 21 | AE→COO | BLOCKED pre-apply — orphan drift |
| 22 | COO→AE | DECISION: Option C -target apply |
| 23 | DS→AE | ACK orphan block + Brief #11 incoming |
| 24 | AE→DS | ACK Brief #11; -target apply done |
| 25 | AE→COO | RAVC2 deploy v1.7.52 LIVE |
| 26 | AE→DS | RAVC2 deploy ack — v1.7.52 LIVE |

---

## Commits This Session

| SHA | Author | Description |
|---|---|---|
| `07d2855f5` | 0.6.1_AE_PartnerETL | ci(inf-pipeline): upload inf-portal-advisor-publisher artifact for a186ffa9b + 796f5bbd6 bundle deploy |
| `c8bb6e605` | 0.6.1_AE_PartnerETL | ci: record deploy inf-pipeline @ 7f14ecfd3 (inf-pipeline-v1.7.52 — a186ffa9b + 796f5bbd6 bundle) [skip ci] |

Tag: `inf-pipeline-v1.7.52` pushed.

---

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| comp-pipescript deployed | not run | INF_D_04 S3 mtime 20:39:08Z verified via aws s3api head-object instead — comp-pipescript hardcoded for bd bucket per output, would need refactor for inf bucket |
| comp-iam | not run | No IAM changes in this deploy |
| comp-blast | not run | Single Lambda + scoped -target apply; no cross-component implication |

Append row to org/compiler-tools-log.md: skipped — comp-* tools have known inf-bucket gap (see Future Work).

---

## Open Items (carry forward to chain #23)

1. **Brief #11 mix_periods** — DS in progress (~30min ETA); chain #23 awaits commit
2. **inf-unified-account-dim-daily orphan investigation** — COO files TO tomorrow; AE 0.6.1 + DT 0.4 dual-owner
3. **Chain #23 fire** — gold-d, COO GO after Brief #11 lands; Lambda first-fires via D-stage sentinel
4. **State="34" + State="Other" donut anomalies** — DS~D advisory pass after chain #23
5. **comp-pipescript inf-bucket gap** — defer to comp-tools improvement TO

---

## Future Work

`comp-pipescript deployed` is hardcoded to `opal-data-bd` bucket. INF pipeline scripts can't be verified through it. Suggest comp-tools improvement TO to parameterize bucket prefix.

CHANGELOG.json bun-side `entries.unshift` bug in record-terraform-deploy.sh — file may have a stale schema where `cl.entries` is not an array. Source map stamping is unaffected (handled separately). Suggest CHANGELOG.json schema audit + script fix TO.
