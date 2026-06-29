# Session Log (delta) — 0.4.0_DS_ClientPlatform~B — Andrew no-normalize: G13 raw-credit + recon tracker

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE
**serial:** 0.4.0_DS_ClientPlatform~B · **date:** 2026-06-29 · **window:** since g13_parity_mirror log (1616Z) -> 1748Z

## Summary

Two Andrew rulings (via COO) landed + executed; one removed work, one added it. Commit `e01b54ec9`.
1. RAW-PASSTHROUGH ruling: stand down split curation (override dormant no-op, worksheet dropped). Confirmed (grounded) dim already passes BD raw splits through + G13 normalization was downstream-only -> nothing to change.
2. NO-NORMALIZE ruling (GO): G13 -> raw-credit + a dedicated unattributed-$ reconciliation tracker.

## Interim: CVO loop closed + base-DS co-own closed (carried from prior window)

- CVO SIGNED the G13 mirror Wave-2 substrate (82f6726e4); implementor residual grounded as override-overlay (no bridge error). base-DS co-own on TO-7 dim CLOSED (live-artifact verified).
- PFMG_TAXSMA S0.2 found already CLOSED (06-26) -> not an open pick.

## Andrew no-normalize GO (IMPLEMENT)

- G13 partner_analytics (schema 2.0 -> 3.0): credited_aua = account_aua * RAW split_pct per role (dropped 3-case normalization). Conservation intentionally OFF. Kept total_aua = RAW full per-role (BD headline mirror, CVO TO-4). 157 advisors; credited $1.367B; role_breakdown ties total_aua $0.00.
- NEW build_gold_advisor_split_reconciliation.py -> the tracked "money not accounted for" surface:
  - per-account (5894): account_aua, raw_split_sum_pct, credited_aua_total, SIGNED unattributed_aua, gap_direction, role_detail. 5846 under / 1 over / 47 exact.
  - firm rollup (_firm, 1-row, time-tracked): HEADLINE net unattributed $224.2M = 14.1% of the $1.591B book; gross $224.2M.
  - reconciles with G13 by construction; identity sharp-check PASS (credited+unattributed==account_aua).

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-pipescript io | build_gold_advisor_split_reconciliation | N/A (expected) | NOT-FOUND -- canonical uncovered (documented); mandate attempted |
| ds-commit-gate / ruff | G13 + recon (several passes) | PASS | caught unused billable/_weights after dropping the fee gate -> removed |
| (read-only boto3) | raw-passthrough confirm (acct 0026881039 dim vs BD-alloc), served firm-rollup verify | PASS | F5 grounding |

- **What worked:** the recon firm-net ($224.2M) ties G13's credited-gap exactly (by construction) -- the two surfaces are self-consistent.
- **What failed:** identity assert tripped on a $0.01 2-decimal-rounding hair -> tolerance 0.02.
- **Gap found:** none new.

## Blockers

None.

## Current State

Andrew no-normalize ruling COMPLETE. Served (date=2026-06-24, AES256): partner_analytics (schema 3.0 raw-credit), advisor_split_reconciliation + _firm (the $224.2M/14.1% tracker). 08_GOLD_SCOPE updated (G13 + new G14 recon row). Override layer left dormant (Andrew stood down curation). Commits this window: e01b54ec9. Registered LIVE, IDLE.

## Next Steps

- **[0.4.0_DS_ClientPlatform]** (base) fold build_gold_advisor_split_reconciliation.py + G13 into the gold orchestrator / build_canonical_daily.py when wiring G11-G13 (D4) -- so the $224.2M tracker regenerates each run for the time-series.
- **[3.0.0_SA_CVO]** noted the G13 credit-method change (raw vs normalized) for the TO-4 harness; total_aua mirror unchanged, recon is a canonical-only gap surface.
- **[2.0.0_SA_COO]** next dispatch; the headline ($224.2M / 14.1% unattributed) is in the RAVC for Andrew.
