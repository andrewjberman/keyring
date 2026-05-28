# ADVI_INFDEMO.F11 — INF_D_00c fee_breakdown PROD ship (IWM demo)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, COORDINATE
**Agent:** 0.6.1_AE_PartnerETL
**Date:** 2026-05-28
**Assignment:** Andrew-direct (relayed via 1.0.0_SA_CTO 1543Z + turnkey 1546Z)
**PRD:** docs/architecture/ADVI_INFDEMO.md §F11

---

## Summary

Owned the backend deploy + Group-D-script regen + S3 rollback for the IWM-demo F11
fee_breakdown emit. DS authored + dry-run-validated the emit (commit `ac95741d6`);
RD frontend pre-wired (zero change); CVO gates client-facing. Executed rollback-first
per Andrew mandate ("if ANY error, roll back to earlier 00c + rerun").

Result: `s3://opal-data-inf/platinum/firm/leaderboard.json` regenerated with
`entry.fee_breakdown.{fee_paying,no_fee}` on 20 entries across 5 windows. PROD content
byte-identical to the CVO-approved QA artifact. Rollback armed throughout; not triggered.

## Scope (Andrew confirmation)

Ran **INF_D_00c.portal_leaderboard.py --upload ONLY** — a single Group-D script, NOT the
full Group-D chain — per CTO "Minimal scope (INF_D_00c only)". Correct for F11: the
fee_breakdown change lives entirely in INF_D_00c (`ac95741d6` touched only that file) and
`leaderboard.json` is the only portal-read artifact. Smallest blast radius.

## Rollback-first points (set BEFORE any PROD write)

- S3 backup: `s3://opal-data-inf/platinum/firm/_rollback/leaderboard.json.pre-F11-20260528T154559Z` (ETag `9b8c1a6e...` == pre-F11 live; confirmed via head-object)
- S3 versioning ON: pre-F11 PROD VersionId `4UV8JgXwUk1wIoxPV_.5J9t9w7c4D.5n`
- Git rollback point: `c3e7862c` (parent of `ac95741d6`); clean revert = `git revert ac95741d6`

## Sequence executed

1. **State check (empirical):** live leaderboard.json (LastModified 15:01:23Z) lacked fee_breakdown → confirmed PRE-F11, DS had not run --upload. Proceed.
2. **Rollback backup:** created + confirmed (above). Reported to CTO.
3. **Deploy MATCH:** `ac95741d6` already on origin/CLOUD; S3 runner code copy `opal-data-inf/code/gold/INF_D_00c.portal_leaderboard.py` md5 `39f667c5...` == local == ac95741d6 (uploaded 11:37Z). Runner current → next daily cron stays consistent (no regression). Billing dim fresh thru snapshot_date=2026-05-28; canonical/holdings inputs fresh today.
4. **QA run** (`OUTPUT_PREFIX=qa/ --upload`, IAM-safe): wrote `qa/firm/leaderboard.json` (25,952B). PROD verified untouched.
5. **QA verification:** additive-only diff vs backup PASS (20 entries gain fee_breakdown, 0 existing fields changed); flow sum-invariant (nna/inflows/outflows/aua) + account_count PASS all 5 windows; Peter Lee MAX nna 108,680,353.55=102,886,153.54+5,794,200.01, aua 165,810,577.93=155,268,588.70+10,541,989.23 — exact match to DS dry-run ref.
6. **client_count finding:** does NOT sum (Peter 199 vs 253). Empirically de-risked against 49F (prod): 49F fee_breakdown also carries a non-summing count field (account_count, 20 entries) and the frontend tolerates it → established by-design behavior. CVO ruled client_count by-design distinct-count (clients spanning both buckets), routed to CTO as display-semantics caveat (per-bucket client_count not shown as additive to total).
7. **CVO QA PASS + clear-to-write** received → **PROD run** (`--upload`, platinum/): wrote `platinum/firm/leaderboard.json` (25,952B, ETag `d900b8a3...`, 16:03:31Z).
8. **PROD verify:** fee_breakdown on 20 entries; PROD content == CVO-approved QA content (byte-identical excl generated_at). Handed live artifact to CVO for final gate.

## Pre-existing WARNs (not F11-related)

`aua_growth_pct null` (snapshot-pair divergence) + stale-proxy holdings for old window-starts — tagged `ADVI_INFTGT.TO-1b`, known prior behavior, present pre-F11.

## Status at log-write

PROD written + verified. Awaiting CVO final-gate verdict on the live artifact → CTO relays
client-facing GO. Rollback armed. My deploy/run deliverable complete.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `aws s3api head-object` | Pre/post-state of PROD leaderboard.json + backup confirm | pre-F11 ETag 9b8c1a6e (no fee_breakdown); post 25,952B d900b8a3 |
| md5sum local vs S3 code copy | Deploy MATCH (Rule 13/14) for INF gold runner | MATCH — both `39f667c5...` == ac95741d6 |
| `aws s3 ls` billing dim + canonical | Input freshness for F11 fee-split | billing thru 2026-05-28; holdings/canonical fresh today |
| python sum-invariant + additive-diff harness | QA + PROD artifact verification | additive-only PASS; flows sum PASS; client_count by-design non-sum |
| 49F reference cross-check | De-risk client_count non-sum | 49F also has a non-summing count field (account_count) — established |

Note: `comp-pipescript deployed` defaults to the BD bucket and does not scan `opal-data-inf`;
used direct md5 compare of local vs `s3://opal-data-inf/code/gold/` copy as the INF-bucket
MATCH equivalent. (Same INF-bucket coverage gap noted in prior CDNCOHT session.)

## Files / artifacts

```
(no repo code change — ac95741d6 already committed+pushed by DS)
s3://opal-data-inf/platinum/firm/leaderboard.json            (regenerated, +fee_breakdown)
s3://opal-data-inf/platinum/firm/_rollback/leaderboard.json.pre-F11-20260528T154559Z  (backup)
s3://opal-data-inf/qa/firm/leaderboard.json                  (QA verify artifact)
```
