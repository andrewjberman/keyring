# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 1730Z (Schwab re-derive serving-verify pre-build alignment)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

## Context
No new pings (AE on BMKAUD, will pick up my A+ diff; CTO+DS~B actively PRD'ing the Schwab re-derive). Rather than idle, aligned my gated serving-verify thread (leg 2) to the now-published CTO PRD (mdpf-49f-schwab-canonical-full-history-rederivation-prd-20260601.md) which NAMES me (§7 DE serving-continuity verify, AC3 estimate-labeling, AC4 continuity, AC6 trading-calendar). Andrew ruled re-derive-not-flag (interpolated 1c + Schwab-canonical 3-cohort: 1a=SmartX model, 1c=interpolated SMA, 1b=Schwab plug).

## Work — pre-build serving-verify CONTRACT to DS~B (CC CTO+COO)
KEY forward move: AC3/§6 require my harness to verify "estimated regions FLAGGED, not silently continuous" — only machine-verifiable if DS~B EMITS an estimate flag. Defined the contract BEFORE DS~B builds (avoids post-emit rework):
- Proposed meta.basis_provenance {schwab_exact_range, interpolated_1c, pre_1_16 disposition} AND/OR per-date estimated bool / basis enum.
- My PRD-aligned checklist: AC4 (5/15 seam gone, 1/16-fwd continuous), AC2 (total=1a+1b+1c DIFF~0/date), AC3 (estimate-flag present), AC6 (trading-calendar).

## AC6 concrete recon (current 49F series — saves DS~B the scan)
- SPURIOUS WEEKEND: 1 = 2025-12-27 (Sat) -> drop.
- NON-HOLIDAY BUSINESS DAYS MISSING (add): 2025-12-30, 12-31, 2026-01-02, 02-02, 03-02.
- Correctly ABSENT (real holidays, leave): 2025-12-25, 2026-01-01 (12/24 half-day = DS call).
- => AC6 re-emit = drop 12/27 + add 5 business days; XNYS trading-calendar disambiguates.

## Commits
- CLOUD `<pending>` — this log (harness update deferred until DS~B confirms the flag shape + re-derived artifact lands)

## Comms
- SERVING-VERIFY CONTRACT -> DS~B (0.4.0_DS_ClientPlatform~B); CC CTO + COO.

## Next
- [DS~B] confirm estimate-flag shape + build re-derive to the checklist; ping me w/ re-derived/sample artifact.
- [me] update verify_continuity.py to the confirmed flag shape + PRD ACs; serving-verify post-emit; CVO independent verify pairs (AC5).
- [AE] A+ Positioning diff deploy (separate thread). Held: RD~B fold(103f623a) verify. /work cron live.
