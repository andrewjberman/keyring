# BRIEF — Inflection served AUA frozen at $202,711,894 since Fri 06-26 (investigation handoff)

**To:** 0.6.1_AE_PartnerETL (drive to root-cause + fix)
**From:** 1.0.0_SA_CTO
**Date:** 2026-06-29
**Priority:** Andrew-direct, P1 (served partner AUA wrong + falsely labeled fresh)
**Status:** symptom + producer-chain GROUNDED; final root-cause NARROWED to 2-3 specific tests (below). Stop guessing — run the named tests.

---

## 1. The symptom (Andrew-flagged)

- Portal (ADVI ClientsTab) shows Inflection AUA **$202.71M**, labeled "updated today."
- Orion UI shows **$200.99M** today.
- Gap ~$1.72M (~0.85%), and we falsely claim freshness.

## 2. What it actually is (GROUNDED, S3 version history of `platinum/firm/header_metrics.json`)

The served `total_aua` per refresh:

| Refresh | total_aua | data_as_of stamped | note |
|---|---|---|---|
| Wed 06-24 | 202,321,763.24 | 06-24 | advancing normally |
| Thu 06-25 | 202,379,189.47 | 06-25 | advancing normally |
| Fri 06-26 | 202,379,189.47 | **06-25** | **STALLED — re-served Thursday's value + Thursday's as_of** |
| Sat 06-27 | **202,711,894.29** | 06-27 | jumped to a new value on a non-trading day (likely Fri data processed late, mislabeled as_of) |
| Mon 06-29 | **202,711,894.29** | 06-29 | **frozen — penny-identical to Sat, re-stamped "today"** |

**Conclusion:** the AUA has been **frozen at $202,711,894.29 (Friday 06-26's value) since Sat 06-27**, while the artifact regenerates twice daily and re-stamps `data_as_of` to today. Penny-identical across 3 days is impossible on a live recompute (prices move) → it's a **frozen value re-served with a fresh label**. mtime-fresh / value-frozen.

## 3. The producer chain (GROUNDED)

```
served header_metrics.total_aua  (platinum/firm/header_metrics.json -> getHeaderMetrics -> ClientsTab)
  <- INF_D_00.portal_aggregates.py
  <- INF_B_00.canonical_holdings.py  (gold/canonical/holdings_{date}.parquet)  [holdings_2026-06-29 sums to EXACTLY 202,711,894]
  <- silver/api_dims/positions_mv     (built by convert_orion_api_to_silver.py -> build_positions_mv; market_value = positions_mv.current_value DIRECT from Orion)
  <- bronze Orion positions pull       (pull_inflection_positions_daily.py, BASE=api.cloud.orionadvisor.com)
  <- Orion positions API
```
`positions_mv` for `snapshot_date=2026-06-29` exists, stamped `as_of_date=06-29`, but every row's `edited_date` is frozen at **2026-06-26 15:50 (Friday)**. The Monday partition carries Friday's positions.

## 4. What we have ELIMINATED (do not re-chase)

- **NOT a code change.** No inf gold/silver commit since 06-11 (`git log` on the inf scripts).
- **NOT the legacy `aum_snapshot`.** `silver/aum_snapshot/` is empty — but it's been dead since the Orion CSV->REST migration (~April; bronze/orion CSV ingestion stopped 04-29). It's a red herring, not the cause.
- **NOT a current auth / JWT / IAM failure.** LIVE Orion API call just now (cid=18/19/20, `/api/v1/Portfolio/Clients/{cid}/Assets/{date}`) returned **HTTP 200**. The JWT at `s3://opal-data-inf/orion/jwt/current.json` is **fresh — issued 2026-06-29T12:13Z, expires 22:14Z**. Auth works right now.

## 5. The DECISIVE live evidence (Orion API, run 2026-06-29 ~20:30Z)

| client | date asked | HTTP | currentValue | maxEditedDate |
|---|---|---|---|---|
| 18 | 06-29 | 200 | $1,939,774 | 2026-06-03 |
| 18 | 06-26 | 200 | $1,939,774 | 2026-06-03 |
| 20 | 06-29 | 200 | $460,942 | 2026-06-03 |
| 20 | 06-26 | 200 | $460,942 | 2026-06-03 |

**Orion returns the IDENTICAL `currentValue` for Friday and Monday**, and the max `editedDate` across all Inflection positions is **Friday 06-26 15:50**. So **Orion itself has not updated position valuations since Friday afternoon** — our pipeline is *faithfully* pulling Orion's Friday-frozen positions. Our code is doing the right thing with non-advancing source data.

So the real anomaly reframes to: **Orion's UI ($200.99M, "current") differs from Orion's positions API ($202.71M, Friday-last-edit).** Two different Orion numbers.

## 6. The strongest LEAD (chase this first)

`INF_D_00e.fresh_header_supplement.py` references a **DIFFERENT, fresher Orion endpoint**: `bronze/orion-api/{date}/assets.csv` — described in-code as "CSV daily-AUM export; **fresher endpoint**." Hypothesis: **Orion's UI $200.99M comes from this fresher daily-AUM export**, while our served header is computed from the positions-derived path that lags at Friday's last-edit. If so, the header should source AUA from the fresher endpoint (or reconcile to it), and the positions-derived value is structurally a step behind.

## 7. The named tests to settle it (run these — stop guessing)

1. **Positions endpoint live test (the actual AUA driver — I tested /Assets, not /Positions).** Run `pull_inflection_positions_daily.py` for `--date 06-29` vs `06-26`, full universe, and compare the summed `current_value` + the max `edited_date`. Does the positions endpoint advance past Friday on a Monday call, or not?
2. **Reconcile the fresher daily-AUM endpoint.** Pull `bronze/orion-api/{date}/assets.csv` (the INF_D_00e "fresher" endpoint) for 06-29 and sum it. **Does it equal Orion UI's $200.99M?** If yes -> the header should use it; the freeze is "we sourced the lagging endpoint," not a break.
3. **Pull-success audit over the freeze window (Fri 06-26 -> Mon 06-29).** Check the daily Orion pull's CloudWatch/runner logs: did the positions pull SUCCEED each day, or fail (401 / `assert_fresh_or_exit` exit / rate-limit) — i.e., was the JWT actually fresh each day over the weekend, or did it lapse Fri-Sun and only get refreshed today 12:13? A weekend JWT lapse would explain "stalled Friday, caught up late." Check `orion/jwt/` refresh history + the pull logs.
4. **IAM check (rule it in/out cleanly):** `comp-iam` on the inf positions pull's role — confirm S3 read/write + Secrets/JWT access is intact (no recent policy change around 06-26). Live-ground it, don't trust TF-desired.

## 8. The fixes that follow (regardless of which test wins)

- **Honesty fix (do immediately, independent of root-cause):** `data_as_of` / "updated today" MUST reflect the true DATA date, never the gold-run time. A Friday value must never be served stamped "06-29." This is the false-freshness defect that made it invisible. (INF_D_00 header build.)
- **Source the right endpoint:** if test #2 confirms the fresher daily-AUM endpoint = Orion UI, wire the header to it.
- **Producer-source parity alarm (comp-drift seam-7):** an automatic served-AUA vs Orion-source check would have caught "served stopped matching Orion" on Sat 06-27 instead of Andrew catching it Monday. This is the WS3 case in miniature.

## 9. Ground rule (CLAUDE.md Rule 22)

Every causal claim in the fix must cite its grounding (the live read it rests on). I over-stated "Orion's source froze" earlier from our *stored* edited_date before hitting Orion live — corrected here by the §5 live call. Hold the same bar: ground the mechanism on a live Orion read + the pull logs, not on our own stored copy.

---

*Issued 1.0.0_SA_CTO 2026-06-29 to 0.6.1_AE_PartnerETL. RAVC CTO + Andrew with: the test #1/#2 results (does positions advance? does the fresher endpoint = $200.99M?), the pull-log audit over Fri-Mon, and the fix. This is P1 — a wrong, falsely-fresh partner AUA on the live Portal.*
