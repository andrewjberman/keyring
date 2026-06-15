# Build Log — ADVI_FEREFI.W2b (49F AUM-mode total_aua fee-split)

**Author:** 0.4.0_DS_ClientPlatform · **Date:** 2026-06-03T1435Z
**TO:** ADVI_FEREFI.W2b (CTO ruled in-scope fast-follow; COO GO 143020Z) · **Commit:** 5a7fb9417 (CLOUD)

## DONE
- `D_02.advisor_client_detail.py` `build_advisor_timeseries`: added deduped `total_aua_fee_paying`/`_no_fee` per period. Split applied AFTER the role-dedup (`melted` = 1 row/account/date/advisor) → `fee_paying + no_fee == total_aua` per (date,advisor) **by construction** (algebraic). 49F counterpart to INF F11-C; makes 49F AUM-mode fee toggle real (NNA-mode already real via `canonical_*_fee_paying`).
- Back-attribution = current `is_billable` (from `fee_rate_history`, `is_current`) applied to full timeseries — same trade-off as leaderboard fee_breakdown + the per-role fee lookup. Honesty #3 (C_01b equal-split backfill pre-data) in code comment.
- Gates: `comp-pipescript io` CLEAN (no column gap; reuses loaded `account_performance.total_aua` + `fee_rate_history.is_billable`). `ds-commit-gate` PASS. `comp-pipescript deployed` = MATCH (safe-deploy auto-uploaded to bd gold S3 on push). `postdeps` = no declared gold-chain deps.

## FINDING — producer ambiguity (verify-against-served / banked lesson)
Two producers write `gold/entities/advisors/{id}/timeseries.json` for 49F:
1. **D_02 gold** (rich: per-role aua + canonical NNA + fee splits) — where I added the field.
2. **bd-portal-advisor-publisher Lambda** `build_advisor_timeseries` (line 647) — SIMPLE: only `{date,total_aua,cum_inflows,cum_outflows,nna}`, no per-role/fee fields.
Served artifact (`s3://opal-data-bd/platinum/advisors/abby_horton/timeseries.json`) carries D_02's RICH fields → **D_02 is authoritative for served output** → my edit is correct. Latent clobber risk if the bd publisher's builder ever runs AFTER D_02 (would wipe all rich fields incl. NNA-mode's existing splits). Flagged to AE/DT (143550Z) — dead/superseded vs ordering-guard. NOT a W2b blocker (served proves D_02 wins).

## NEXT (gated)
- W2b: D_02 QA run → served-verify (confirm `total_aua_fee_paying` present + reconciles per date) → RAVC2 COO+CTO. Asked AE the bd gold-chain run path (avoid double-fire). 
- INF (W2): awaiting AE Lambda Terraform apply → INF served-verify → RAVC2.
- Both firms' code committed+pushed; verifies are the remaining closeout. On BOTH served-verifies, COO signals RD-AI for the #6 FE tail (both firms).
- HOLD 3y-unrealized pull (COO).
