# AE Brief — INFETL Phase-2-follow-on: txn-sentinel restore (silver-aggregator quorum + inf-api-txn runtime)

**Authored:** 0.7.0_AE_CloudOps, 2026-05-25
**Surface:** Pre-charter AE-domain mechanics + tradeoffs to inform ws CTO authoring of the Phase-2-follow-on charter post-DEMOV1 close. Not a charter; not a TO. Mechanics + sequencing options + open questions.
**Source MCPs:** ws COO close-confirm `eecc50c19` 2026-05-25T06:49Z §4 + ws COO ACK `3ccd9aa49` 2026-05-25T07:01Z §5 (pre-authoring optional).
**Anchor finding:** ADVI_INFETL.json verify-channel sweep MCP `~20260525T063626Z` §1 probe B: silver-aggregator quorum stuck since 2026-05-23 — `silver/_silver_complete/<date>/transactions.json` missing for snapshot dates 2026-05-23 + 2026-05-24; cron-fallback at 14:00 UTC catching the gap as defense-in-depth.

---

## §1 — Reframing the (i)/(ii) options after deeper probe

My verify-channel sweep MCP §4 framed two paths:
- **(i)** New sentinel-write hook on the post-TXNAMG canonical txn write path
- **(ii)** Quorum-reduction 10→9 to exclude txn from aggregator gating

**Additional probe after the sweep changes (i):** `inf-api-txn/lambda_function.py:101-113` ALREADY writes `silver/_silver_complete/{snap_date}/transactions.json` as STEP 2 of the Lambda's handler. The LAMBDA-DIMS Phase A authoring added the sentinel-write at the same time TXNAMG.004 removed the silver/transactions/ data write — the sentinel was deliberately kept so the aggregator quorum chain stays functional even after the silver-data writer migrated. The code is **deployed** (Lambda LastModified 2026-05-15T17:48:26Z; SHA `PvZReD75cPMA0tJGX81eU0Y0oLnvDFudmLHD+okNJfk=`) and matches local source (only commit since `aa7be4b5e` = the trim itself).

So the failure is **not "missing sentinel-write code"**; it's **runtime failure of the Lambda before the sentinel-write step executes**. The Lambda's STEP 1 (`pull_inflection_transactions_v2`) raises `RuntimeError` on non-zero exit (line 91), short-circuiting STEP 2 sentinel-write.

**Corroborating evidence:** `bronze/orion-api/<date>/transactions.csv` is ALSO missing for snapshot dates 2026-05-23 + 2026-05-24:

| Snapshot date | Bronze CSV LastModified + size | Sentinel landed |
|---|---|---|
| 2026-05-20 | 2026-05-21T13:00:38Z, 29,311 B | ✓ |
| 2026-05-21 | 2026-05-22T13:00:38Z, 3,347,557 B | ✓ |
| 2026-05-22 | 2026-05-23T13:00:37Z, 410,539 B | ✓ |
| **2026-05-23** | **MISSING** | **MISSING** |
| **2026-05-24** | **MISSING** | **MISSING** |

Bronze AND sentinel both missing → Lambda failed before STEP 2 OR didn't fire at all. CloudWatch log inspection (not run here — MSYS_NO_PATHCONV / aws CLI shim friction; punted to charter execution) will distinguish:
- (a) Lambda fired + JWT freshness check failed (line 59-63 raises before pull)
- (b) Lambda fired + Custom Reports/28198 API returned error → `pull_main()` exit non-zero → line 91 raises
- (c) EventBridge cron `inf-api-txn-daily` didn't fire (broken rule, IAM, or other)

Note: bronze size 2026-05-20 = 29 KB vs 2026-05-21 = 3.3 MB vs 2026-05-22 = 410 KB — high variance suggests Orion Custom Reports/28198 has variable per-day yield. A zero-row return wouldn't trigger the line-91 raise as long as exit_code is 0; a non-zero exit (API error, auth failure, etc.) would.

## §2 — Revised path options

**(ii) Quorum reduction 10→9 — PROXIMATE FIX (unchanged):**
- **Mechanism:** silver-aggregator Lambda reads dim list from env var `INF_DIM_LIST` (`lambda_function.py:36`). Default = `"tax,performance,billing,transactions,accounts_v2,unified_account_dim,representatives,assets_v2,positions_daily"` (9 dims).
- **Terraform attribute flip:** drop `transactions` from the env var in `infra/aws/terraform/inf-pipeline/` Lambda resource (need to confirm exact file holding `inf-silver-aggregator` resource block + whether env var is currently set explicitly or relying on default).
- **Effort:** ~0.1d AE — single Terraform attribute flip + plan + apply + 0-diff replan + tag + push.
- **Behavior post-flip:** aggregator fires on 8-dim quorum; txn excluded; aggregator-fire resumes from next cron snapshot. Gold runs sooner via event-chain primary; cron fallback at 14:00 UTC remains belt+suspenders.
- **Risk:** gold runs against snapshot that lacks confirmed-fresh txn-bronze. If `convert_transactions_to_silver.py` (the gold-chain amalgamating txn writer per TXNAMG.004) sources from the same bronze that inf-api-txn failed to write, gold txn-dependent emits (NMNC/NNA, account-level cohorts, leaderboard) may carry stale txn data without indication. **Need to confirm:** does `convert_transactions_to_silver.py` source from `bronze/orion-api/<date>/transactions.csv` (the file inf-api-txn writes), or from a different bronze artifact (e.g., a REST-pull bronze written by a different Lambda)?
- **Reversibility:** trivial (Terraform attribute flip back).

**(i') Diagnose + fix inf-api-txn runtime — ARCHITECTURAL RESTORE (replaces original (i) framing):**
- **Diagnose phase (~0.5d AE):**
  - CloudWatch logs for inf-api-txn for `eventbridge` cron fires 2026-05-24T13:00Z + 2026-05-25T13:00Z — identify failure class (a/b/c above)
  - If (a) JWT-stale — investigate inf-jwt-trigger 12:00 UTC fire health on the same dates; possible upstream JWT failure
  - If (b) Orion API failure — investigate Custom Reports/28198 vendor-side state + retry pattern + permanent vs transient
  - If (c) EventBridge cron not firing — check `aws_cloudwatch_event_rule` state + `aws_lambda_permission` + recent Terraform changes
- **Fix phase (~0.5-2d AE depending on diagnose):** scoped per failure class. JWT path probably has existing remediation tooling; API failure may need retry logic or vendor-side coordination; cron path is Terraform-only.
- **Restore sequencing once fixed:** revert (ii) quorum flip → restore 10-dim aggregator quorum → confirm aggregator fires cleanly against next full quorum snapshot.

**(iii) NEW — Lambda-source-map drift (NOT in original framing, surfaced during probe):**
- `infra/aws/lambda/ci/lambda-source-map.json` does NOT have an `inf-api-txn` entry (`jq '.["inf-api-txn"]' = null`).
- Per CLAUDE.md Rule 4: "Every Lambda must have an entry in `infra/aws/lambda/ci/lambda-source-map.json`. CI drift detection depends on this."
- This is a separate hygiene finding from the txn-sentinel chain itself. Probably easier to bundle into the Phase-2-follow-on charter than route separately. Effort: ~0.05d AE — single JSON entry add.

## §3 — Recommended sequencing for charter

**Option A — proximate-first (recommended; minimizes silent-degradation window):**
1. Ship (ii) quorum flip immediately — single Terraform attribute → restores aggregator firing
2. In parallel: (i') diagnose CloudWatch logs → identify failure class
3. Per failure class: author + ship (i') fix
4. Once fix verified empirically (≥3 consecutive cron-snapshot sentinels landing clean), revert (ii) → restore 10-dim quorum
5. Bundle (iii) source-map drift fix into one of (i')/(ii) commits

**Option B — root-cause-first (acceptable if (i') diagnose is fast and cron-fallback covering production):**
1. (i') diagnose first → fix → verify ≥3 consecutive sentinels land
2. Skip (ii) entirely — aggregator quorum self-restores
3. Bundle (iii) source-map drift into (i') fix commit

**Tradeoff:** Option A preserves architectural intent (event-chain primary) sooner — silent-degradation window is ≤1 cycle. Option B avoids the temporary quorum-misconfiguration window but holds event-chain degraded until (i') ships. Cron-fallback in either case keeps production-side gold + platinum healthy.

**Lean:** Option A. The (ii) flip is reversible + 0.1d effort + doesn't depend on diagnose outcome; (i') can take its time without production pressure. The temporary 9-dim quorum is auditable + obviously-temporary in Terraform commit history.

## §4 — Open questions for ws CTO ruling

1. **convert_transactions_to_silver.py source-binding (load-bearing for (ii) risk):** does the gold-chain amalgamating txn writer read from `bronze/orion-api/<date>/transactions.csv` (same file inf-api-txn writes), or from a different bronze artifact? If same, (ii) gold-runs-during-quorum-flip carry stale txn risk and need a guard. If different, (ii) is genuinely safe to ship immediately.
2. **(i') diagnose: who runs it?** AE 0.7 has standing capacity now; AE 0.6.1 may have more context on inf-api-txn historically; either-or DS~A may have context on the convert_transactions_to_silver.py source-binding question above. Suggest AE 0.7 takes (i') diagnose with DS~A as consultant on §4.1.
3. **Bundle scope:** is this Phase-2-follow-on ONE charter covering (i')+(ii)+(iii), or three separate charters? Recommend one bundled charter — the three are tightly coupled in operational terms (all three serve the silver-aggregator chain restoration).
4. **Cron retime context:** ADVI_INFDRF.002 retimed fallback cron 06:00 → 14:00 UTC. The fallback at 14:00 UTC is ~1h AFTER the inf-api-txn 13:00 UTC cron. If inf-api-txn fails at 13:00 UTC and cron fallback fires at 14:00 UTC against stale txn bronze, the same gold-dependent-on-stale-txn issue from §4.1 applies symmetrically. Worth verifying as part of (i') diagnose.

## §5 — Effort + cap

- **Total AE effort (all 3 paths):** ~1-3d AE depending on (i') diagnose outcome
- **Cap-arithmetic impact:** zero — AE 0.7 base session in place; no spawn needed
- **DEMOV1 dependency:** charter routes post-DEMOV1 Phase 5 RAVC2 (ETA ~13-16Z UTC); pre-DEMOV1 routing fine if ws COO/CTO bandwidth allows

## §6 — Non-goals / explicit out-of-scope

- New Lambda authoring — sentinel-write already exists in inf-api-txn; (i') is diagnose + fix, not greenfield
- TXNAMG.004 reversal — the silver-data-writer migration to gold-chain is correct architectural choice per Andrew sovereign + CTO ruling; sentinel-write divergence is the cleanly-separable concern
- Gold-chain code changes — convert_transactions_to_silver.py source-binding question (§4.1) may need DS-side input but is read-only investigation, not gold-chain modification
- Cron fallback removal — fallback is now part of v0.2 §3 defense-in-depth pattern explicitly recorded in INFETL close-out narrative; remains structurally necessary

---

*AE 0.7 standing for ws CTO architectural ruling + charter routing. tier0_commit_hash: 3cca313d8.*
