# Deploy-Completion Ledger — ADVI_BREAKS TO-3 49F: B_01 non-empty-unrealized gate

**Status:** CLOSED -- closed 2026-06-30T14:40Z (deployed 6b903ab8e + verified MATCH + regression-free)
**Opened:** 2026-06-30T14:24Z by 0.4.0_DS_ClientPlatform~B
**Deploy:** B_01.holdings_lots.py `_resolve_unrealized_key` — skip 0-row/degenerate unrealized partitions, fall back to last NON-EMPTY within the existing 2-day window (restores 49F served frozen since 06-26T05:00).
**Gates cleared:** CTO apply-co-sign (135551Z) + COO GO (142324Z) + Andrew GO (135xxx direct).
**Scope:** single gold script, `code/gold/` S3 prefix. DS commit->QA-deploy (Rule 13).

| Leg | Type | Step | Status |
|---|---|---|---|
| L1 | git | CLOUD commit B_01 source (ds-commit-gate PASS) under DS~B author | CLOSED 9d5642cc3 |
| L2 | s3-prefix | B_01.holdings_lots.py -> s3://opal-data-bd/code/gold/ (safe-deploy pre-push hook auto-deployed; comp-pipescript deployed = MATCH) | CLOSED |
| L3 | effect-verify | the gate's EFFECT given the 4-day drift -- see CORRECTION below | RE-SCOPED |

**CORRECTION (20260630T1430Z, post-deploy ground-truth):** The gate ships CORRECT but its EFFECT is NOT a same-day restore. The last HEALTHY silver/unrealized partition is 06-24; 06-26..06-29 are empty stubs, 06-30 missing. For a 06-30+ run the 2-day window (the deliberately-NOT-widened cap, per the 2026-03-29 stale-false-close incident) holds NO non-empty partition -> the gate FAILS LOUD (no mass-close corruption, alarm fires) but does NOT restore the served value. The healthy partition AGED OUT of the 2-day window during the 4-day freeze. So the B_01 gate = corruption-prevention + fail-loud guard (durable; restores same-day IF caught within 2d, and once the feed is fresh again). The SERVED RESTORE now depends on the INGESTION fix (template-431167 -> fresh non-empty unrealized within the window). Restore tracked on the ingestion-fix follow-on, NOT this deploy.

**Closure:** DEPLOY COMPLETE -- L1+L2 closed (code shipped + verified MATCH). L3 re-scoped: served-restore moved to the template-431167 ingestion follow-on (this gate alone does not un-freeze given the drift). RAVC'd COO+CTO+CVO with the correction.

## Log
- 20260630T1424Z OPENED at deploy-start.
- 20260630T1428Z L1 CLOSED commit 9d5642cc3 (ds-commit-gate PASS); L2 CLOSED safe-deploy hook deployed + comp-pipescript deployed MATCH.
- 20260630T1430Z CORRECTION: gate is corruption-prevention+fail-loud, NOT same-day restore (healthy 06-24 aged out of the 2-day cap). Served-restore -> template-431167 ingestion fix.
- 20260630T1438Z REGRESSION CAUGHT (pre-next-run): the deployed raise-on-all-empty version would set-e/wait_phase ABORT the gold chain at PHASE_B (gold_dispatch.sh:57 set -e, :360 FATAL-abort; B_01 call site :604 not try-wrapped) -> starve ALL downstream surfaces (worse than the localized D_03/D_04 freeze in prod).
- 20260630T1440Z FOLLOW-UP DEPLOY: changed raise -> never-raise graceful fallback to nearest-existing partition (= prior prod behavior when all-empty, chain stays alive) + loud CONTRACT warn. Commit 6b903ab8e (ds-gate PASS), safe-deploy hook deployed, comp-pipescript deployed = MATCH.

**STATUS: CLOSED 20260630T1440Z.** B_01 gate DEPLOYED + verified MATCH + REGRESSION-FREE (never aborts the chain). EFFECT = durable corruption-resistance + loud alarm; it does NOT restore the served value (healthy unrealized aged out of the 2-day cap). The 49F SERVED RESTORE is the template-431167 ingestion fix + unrealized backfill (separate P0, COO-elevated 143000Z) -- tracked there, not on this deploy ledger.
