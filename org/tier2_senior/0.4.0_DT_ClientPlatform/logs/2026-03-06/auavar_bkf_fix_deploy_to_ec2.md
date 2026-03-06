# ADVI_AUAVAR D2 Fix: BKF Forward-Fill Deploy to bd-gold-layer-runner — 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 19:30
**End Time:** 19:40

---

## Objective

Deploy DS commit `91b1918a` (`02_build_positions_cube.py` BKF forward-fill extension)
to `bd-gold-layer-runner` via `safe-ec2-deploy.sh`. No cube rebuild this session.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Confirm `91b1918a` in origin/CLOUD | Already present — no push needed |
| 2 | First `safe-ec2-deploy.sh` attempt | BLOCKED — uncommitted changes in `data/black_diamond/scripts/` (`phase1_data_collection_20260304.py`) |
| 3 | Investigate blocking file | Minor DS fix — removes `nna` from AUA column priority list (NNA is flows, not AUA). Correct change, uncommitted since before this session. |
| 4 | `git stash push` the blocking file | Stash ref: `refs/stash@{0}` — "DS: phase1_data_collection nna/aua fix" |
| 5 | `safe-ec2-deploy.sh bd-gold-layer-runner deploy-to-ec2.sh` | SUCCESS |
| 6 | `git stash pop` | DS file restored to working tree |
| 7 | `git push origin CLOUD` | Manifest commit `01282ed9` pushed |

---

## Verification

**S3 upload confirmed by deploy script:**
```
upload: data/black_diamond/scripts/gold/02_build_positions_cube.py
     → s3://opal-data-bd/code/gold/02_build_positions_cube.py
```

**S3 script counts after deploy:**
```
code/bronze/: 4 script files
code/silver/: 7 script files
code/gold/:   14 script files
```

**EC2_MANIFEST.json updated by safe-ec2-deploy.sh:**
```
Service:         bd-gold-layer-runner
deployed_commit: 91b1918a4289a5a5e24d4eadf58bc216378ab05d
deployed_at:     2026-03-06T19:34:13Z
Manifest commit: 01282ed9 (auto-committed by safe-ec2-deploy.sh)
```

---

## What Was Deployed

`02_build_positions_cube.py` — BKF forward-fill extension (DS commit `91b1918a`):

- **`_load_open_account_ids(date_str)`** — new helper. Reads `silver/allocations/{date}.parquet`, returns set of confirmed-open account IDs. Returns empty set on any failure (safe fallback = existing behavior).
- **`_compute_account_end_dates(transactions, open_account_ids=None)`** — extended signature. BKF accounts in `open_account_ids` → `global_end_date` (same as ACT). BKF accounts not confirmed → last-txn-date cap (unchanged). `None`/empty → full backward-compatible behavior.
- **`build_full()`** — Steps 2b+2c added. Loads allocations at `max(unit_events.trade_date)`, passes `open_account_ids` into `_compute_account_end_dates`.

**Effect when cube rebuild runs:** 143 BKF accounts with real open positions will get `global_end_date` instead of being capped, adding ~$6.6M BD-equivalent to the cube. 90 liquidated BKF accounts self-exclude regardless (cum_units = 0).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| `git stash` the blocking file rather than committing it | The `phase1_data_collection_20260304.py` change is a DS fix — DT should not commit DS files. Stash preserves it cleanly without crossing agent ownership. |
| Used `safe-ec2-deploy.sh` (not direct `deploy-to-ec2.sh`) | CLAUDE.md mandate. Wrapper updates EC2_MANIFEST.json, enforces pre-deploy checks, and creates the manifest commit. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/ec2/EC2_MANIFEST.json` | `deployed_commit` updated to `91b1918a`, `deployed_at` updated | Yes — `01282ed9` (auto by safe-ec2-deploy.sh) |
| `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-03-06/auavar_bkf_fix_deploy_to_ec2.md` | New — this file | Pending |

**Pending (not committed, not DT's to commit):**
- `data/black_diamond/scripts/diagnostics/phase1_data_collection_20260304.py` — DS fix (NNA/AUA column priority), sitting uncommitted in working tree. DS should commit this.

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

`02_build_positions_cube.py` (commit `91b1918a`) is live at
`s3://opal-data-bd/code/gold/02_build_positions_cube.py`. EC2 will pull this
on next boot. No cube rebuild triggered this session. When the next rebuild runs,
the 143 BKF accounts ($6.6M BD MV) will appear in `positions_cube/` partitions
from their last-txn-date forward.

---

## Next Steps

1. **[Andrew/COO] Authorize cube rebuild** — when ready to see BKF fix reflected in `positions_cube/2026-03-02` or current date
2. **[0.4.0_DS_ClientPlatform] Commit `phase1_data_collection_20260304.py`** — NNA/AUA fix sitting uncommitted in working tree
3. **No further DT action required until rebuild is authorized**
