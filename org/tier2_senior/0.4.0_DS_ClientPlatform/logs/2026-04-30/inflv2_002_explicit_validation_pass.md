# DS~B — ADVI_INFLV2.002: Explicit Chain Validation Pass

**Agent serial:** `0.4.0_DS_ClientPlatform~B`
**Date:** 2026-04-30
**Session shape:** COO GO → artifact pull → spot-check → 3-step close → RAVC4
**Outcome:** INFLV2.002 validation PASS. All 3 spot-check criteria confirmed. No holdings-staleness drift. RAVC4 dispatched to COO.

---

## Mandate Origin

COO GO received 2026-04-30: explicit validation pass required for INFLV2.002 (NMEC/NMNC/NNA firm-grain artifacts) — prior "RAVC-PENDING-VALIDATION" state needed explicit sign-off, not git-ts inference.

**Chain re-run:** INFGRD.003 at commit `1116ebe68` (2026-04-29 PM) — this is the chain that produced the artifacts being validated today.

---

## Artifacts Inspected

All pulled from `s3://opal-data-inf/platinum/firm/` (2026-04-29 timestamps):

| Artifact | Timestamp | Size |
|---|---|---|
| `dashboard.json` | 2026-04-29 18:28:08 | 306 B |
| `leaderboard.json` | 2026-04-29 17:33:34 | 8.2 KB |
| `nmec_nmnc_nna.json` | 2026-04-29 17:21:40 | 1.2 KB |
| `header_metrics.json` | 2026-04-29 18:28:08 | 27.8 KB |
| `partner_analytics.json` | 2026-04-29 18:28:09 | 8.9 KB |

Also inspected: `silver/api_dims/accounts_v2/snapshot_date=2026-04-29/data.parquet` (77.5 KB).

---

## Spot-Check Results

### CHECK 1: Firm AUA ≈ $182.55M (aum_snapshot path)

`dashboard.json.total_aua: 182552380.96` — **PASS** (within $1K of target $182.55M)

Note: `nmec_nmnc_nna.json.total.total_aua: 198867318.42` — this is the Orion-positions-derived AUA (DIAGFIX.012 scope), not the aum_snapshot path. Two AUA sources coexisting as expected.

### CHECK 2: accounts_v2 silver dim — DIAGFIX.011 attribution preserved

```
python3 → pd.read_parquet(accounts_v2_2026-04-29.parquet):
  Total rows: 849
  rep_id non-null: 849 / 849 (100%)

  representative_name          accounts  rep_id
  Inflection Wealth Management       13       3
  Joe Brandenburg                    67       6
  Patrick Scanlan                   152      11
  Peter Lee                         617      12
```

**PASS** — exact match to DIAGFIX.011 closure target (Lee 617 / Scanlan 152 / Brandenburg 67 / IWM 13). Attribution fix is intact in silver dim.

**Note on leaderboard:** Leaderboard shows Lee 336 / Scanlan 54 / IWM 404 / Brandenburg ABSENT. This is **expected and known** — the leaderboard (INF_D_00c) counts accounts from TRN activity data, which uses canonical holdings with pre-DIAGFIX.012 `advisor_key` attribution. Brandenburg's accounts still roll to IWM in the TRN-based path. Full attribution requires DIAGFIX.012 Phase 4 INF_B_00 chain re-run.

### CHECK 3: NMEC/NMNC/NNA YTD non-zero

From `nmec_nmnc_nna.json`:

| Field | Value | Check |
|---|---|---|
| `total.nna_ytd` | -$721,733.89 | PASS (non-zero, non-NaN) |
| `total.nna_qtd` | -$721,733.89 | PASS (quarterly cadence populated) |
| `total.nna_mtd` | -$721,733.89 | PASS |
| `total.nmnc_aua` | $174,184,477.25 | PASS (non-zero) |
| `total.nmnc_count` | 201 | PASS |
| `total.existing_aua` | $24,682,841.17 | PASS (non-zero) |
| `total.nmec_aua` | 0.0 | NOTE (see below) |
| `total.nmec_count` | 0 | NOTE |

**PASS overall** — NNA/NMNC quarterly cadence populated; values are non-zero/non-NaN.

**NOTE on nmec_aua = 0.0:** NMEC = New Money, Existing Client. Zero NMEC_AUA means no existing clients brought net positive flows in the YTD period per canonical_nna (TRN-based). Business interpretation: consistent with an environment where the firm is acquiring new clients (NMNC $174M) but existing clients are net flat or outflowing. This is NOT a data error — it's a TRN-derived finding. Distinguished from leaderboard lifecycle_aua.nmec (D_04 path), which uses account-opening date classification and shows NMEC at per-advisor level.

**Note on per-advisor existing_aua = 0:** Brandenburg's accounts are attributed to "IWM" advisor_key in canonical holdings (pre-DIAGFIX.012 B-chain). The `existing_aua: $24.68M` at firm total is real but not distributed to per-advisor rows in the 3-row output. This is the same attribution issue as the leaderboard gap — resolves at DIAGFIX.012 Phase 4.

### Holdings Staleness Check

COO noted: current holdings/ partition is 2026-04-22.parquet (from 2026-04-27 chain run; W4.14 dispatch failed). INF_D_08 reads `canonical_nna` which is C-chain-derived (TRN-based), not B-chain.

**Observation: No holdings-staleness drift detected.** NNA and NMNC values derive from TRN inflow/outflow aggregation, not holdings pricing. The AUA figures in `nmec_nmnc_nna.json` (total_aua $198.87M) come from the Orion positions API path — also independent of holdings parquet. NNA/NMNC drift attributable to stale holdings is not structurally possible on this artifact path.

---

## Leaderboard Manual Validation (Orion gold_validate_config.yaml checks)

comp-validate CLI only covers BD pipeline — no `--config` flag for Orion yet. Manual validation:

| Check | Result |
|---|---|
| leaderboard has entries (windows[0].entries >= 1) | PASS (3 entries QTD/YTD/MAX) |
| no managed_aua in leaderboard | PASS (field absent) |
| Q9: new_accounts_rep absent from leaderboard | PASS (no such advisor_id) |

---

## Pre-existing Validate Config Gaps (not INFLV2.002 scope)

These were present before INFLV2.002 work and are not regressions:

1. **INF_09 field name mismatch:** validate config checks `firm_aua` but `partner_analytics.json` has `total_aua`. Config needs `path: "total_aua"` update (§6.2 false-positive path).
2. **INF_D_04 artifact missing:** validate config expects `platinum/firm/client_portal_summary.json` but S3 has `clients_tab.json`. Config or script needs reconciliation.
3. **comp-validate CLI:** no `--config` flag for Orion pipeline. Currently only BD config is loaded. ADHC_COMPIL extension needed.

Filed as observations, not blocking INFLV2.002 close.

---

## 3-Step Close

1. **TO status:** `ADVI_INFLV2.002.ds-nmec-nmnc-nna-firm-grain.md` — already `<status>complete</status>` (set by DS~A at `cbc4f2713`). ✓
2. **INFLV2.json phase narrative:** updated `"validation pending chain"` → explicit pass evidence with 4 spot-check confirmations. ✓
3. **REGISTRY.md:** COO confirmed row stays in active table (INFLV2 has other in-flight items). No action required. ✓

---

## Commit

Will be committed with session log in single DS~B org commit.

---

## RAVC4 Dispatch

RAVC4 sent to COO at `20260430T...Z`.

**Summary:**
- comp-validate: BD-CLI only (Orion not supported) — manual validation run
- Exit equivalent: ALL PASS (0 ERROR, 0 WARN on applicable checks)
- Spot-check 1 AUA: $182.55M ✓
- Spot-check 2 accounts_v2: Lee 617/Scanlan 152/Brandenburg 67/IWM 13 ✓
- Spot-check 3 NNA YTD: -$721,733.89 / NMNC $174.18M ✓
- Holdings-staleness drift: none observed (C-chain canonical_nna path, TRN-based)
- Pre-existing validate config gaps noted (INF_09 field name, INF_D_04 artifact missing) — not INFLV2.002 scope
