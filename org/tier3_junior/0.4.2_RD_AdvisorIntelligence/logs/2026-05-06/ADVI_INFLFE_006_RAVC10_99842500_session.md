# Session Log — 0.4.2_RD_AdvisorIntelligence
**Date:** 2026-05-06
**Session:** INFLFE.006 RAVC10 — 4-check sweep on portal DEV 99842500
**GO:** COO SWEEP GO (DE bundle merged 960c289a → 99842500)

---

## Summary

Full 4-check sweep on portal DEV 99842500. CHECK 2 + CHECK 3 PASS cleanly. CHECK 1 has a defect (auaExistingClient mapping bug). CHECK 4 BLOCKED by genuine CDN staleness — the audit shape was correct all along; CloudFront serves an older 1931-byte hh226 body that lacks `total_household_mv`, while S3 has the correct 2338-byte body with the field populated.

---

## Check Results

| Check | Status | Details |
|---|---|---|
| 1. Clients/AUA panel | **FAIL** | New $19.7M ✓ + Total $200M ✓; Existing **$7.49M** vs spec $179.29M (FE bug at PartnerAnalytics.tsx:1612 maps `auaExistingClient = nmec` alone, missing `existing` segment) |
| 2. Mix legend Cash | **PASS** | All 4 classes (FI/EQ/ALT/Cash) present in legend |
| 3. B5 L4 account 177 | **PASS** | 12 quarters $27,446.95 → $46,238.51, no_data placeholder absent |
| 4. P3 hh226 QuarterlyMetricsBar | **BLOCKED** | CDN-stale (proof below); audit shape was correct — field genuinely missing in the bytes the FE receives |

---

## CHECK 1 — Clients/AUA Panel Defect

partner_analytics_quarterly.json segments returned by donut endpoint:

| key | label | aua | aua_pct | client_count |
|---|---|---|---|---|
| nmnc | New Money, New Client | $19,682,951.16 | 9.86% | 53 |
| nmec | New Money, Existing Client | $7,486,368.27 | 3.75% | 87 |
| existing | Existing | $172,479,866.88 | 86.39% | 167 |
| **sum** | — | **$199,649,186** | 100% | — |

PartnerAnalytics.tsx line 1610-1614:

```ts
const auaExistingClient = panelViewMode === 'aua'
  ? (isInflectionFirm && auaDonutSegments
      ? (auaDonutSegments.find(s => s.key === 'nmec')?.aua ?? 0)  // <-- BUG: missing 'existing' segment
      : (Number((src as Record<string, unknown>)['NMEC']) || ...))
  : 0
```

Visible UI shows `EXISTING CLIENTS $7.49M` (= nmec alone), not $179.97M (= nmec + existing).

Fix proposed: `auaExistingClient = (nmec.aua ?? 0) + (existing.aua ?? 0)` OR `auaTotal - auaNewClient`.

---

## CHECK 4 — P3 hh226 CDN Stale (PROOF)

vite.config.ts line 68 confirms `/api/scoped/advisor-intelligence/*` proxies to CloudFront `d2n2nzpeqf34ge.cloudfront.net`. Even from localhost dev portal, all platinum requests pass through CDN.

**Side-by-side body comparison for hh226 timeseries.json:**

| Source | Bytes | mix_periods len | periods WITH `total_household_mv` | first MV value |
|---|---|---|---|---|
| S3 direct (`s3://opal-data-inf/...`) | 2338 | 12 | **12/12** | $4,768,355.22 |
| Portal /api/scoped/.../226/timeseries.json (via CF) | **1931** | 12 | **0/12** | None (key absent) |

For comparison, hh79 portal-served body matches S3 exactly (1598 bytes both, total_household_mv populated 8/8). hh79 cache was successfully invalidated; hh226 was NOT.

**Audit shape verification** — my has_mv check is `any("total_household_mv" in p for p in mix_periods)`. For hh226, this returns `False` correctly because the field IS GENUINELY ABSENT in the response bytes. The dashes in the QuarterlyMetricsBar reflect what the FE receives, not what's in S3.

AE 0.6.1's CF invalidation `I7982VDTKUWNEBGKWP9CQXEWF1` Status=Completed claim notwithstanding, the CDN cache for `/api/scoped/advisor-intelligence/platinum/clients/226/timeseries.json` was NOT actually purged. Specific re-invalidation needed.

---

## Diagnostic Workflow

1. Pulled hh226 + hh79 from S3 via `aws s3 cp` — confirmed both have correct populated `total_household_mv`.
2. Built `inflfe006_p3_diag.py` to capture portal-served bytes via Playwright + JWT-authed `fetch()` to the `/api/scoped` proxy path.
3. Compared response bytes:
   - hh226 portal: 1931 bytes, no MV key (CDN stale).
   - hh79 portal: 1598 bytes, MV populated (CDN fresh).
4. Read vite.config.ts to confirm the proxy chain → CloudFront.
5. Concluded: the COO/CTO directive labeling this an "audit shape mismatch" was based on incomplete data (S3 alone, not CDN-served bytes). The audit was correct.

---

## Files

| File | Purpose |
|---|---|
| `inflfe006_sweep_99842500.py` | 4-check sweep script |
| `inflfe006_99842500_result.json` | Full per-check JSON output |
| `inflfe006_p3_diag.py` | P3-only diagnostic comparing S3 vs portal-served bytes |
| `inflfe006_p3_diag.json` | Captured response bodies + headers |

## Screenshots

| File | Content |
|---|---|
| `s10_01_mix_mode.png` | Books → Mix mode (4-tile stats row) |
| `s10_02_mix_legend_full.png` | Full-page Mix legend (all 4 classes visible) |
| `s10_03_clients_aua.png` | Books → Clients tab, AUA mode |
| `s10_04_clients_aua_full.png` | Full-page AUA panel showing $7.49M Existing bug |
| `s10_05_p3_hh226.png` | hh226 L3 Asset Mix panel with QuarterlyMetricsBar dashes |
| `s10_06_p3_hh226_full.png` | Full-page hh226 L3 |
| `s10_08_b5_l3_hh101.png` | L3 David Stuckle (hh101, Patrick Scanlan book) |
| `s10_09_b5_l4_modal.png` | L4 account 177 modal — chart renders |
| `s10_10_b5_l4_full.png` | Full-page L4 account 177 |

---

## RAVC Chain

| Msg | Direction | Subject | Timestamp |
|---|---|---|---|
| COO→RD | COO → RD | SWEEP GO — full re-sweep on 99842500 | ~20260506T214000Z |
| COO→RD | COO → RD | DIRECTIVE — Andrew confirms P3 = audit shape mismatch | 20260506T215036Z |
| RAVC10 | RD → COO | 4-check sweep + P3 root cause CONFIRMED CDN stale | 20260506T215428Z |

---

## Gate Status

- **GREEN**: Mix legend Cash (CHECK 2), B5 L4 acct 177 (CHECK 3)
- **DE FIX**: CHECK 1 PartnerAnalytics.tsx:1612 — auaExistingClient mapping (one-line)
- **AE FIX**: CHECK 4 path-specific CF invalidation re-issue for hh226
- Standing by for next bundle.
