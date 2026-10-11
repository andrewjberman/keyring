# ADVI_COTBKF decomposition -- ROUND 56 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11 ~03:5xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` msg 4022 (ruling (c), answering this issuer's msg 4021), following round 55 (CB-bc-1, drained
@1f79a8182c) and row ADVI_COTBKF-D2-S83.
- With the device default gone, the silver suite reads 20 collection errors on any box without `COTBKF_SWEEPS_CONFIG`.
- The first ruling (a conftest fixture with a synthetic config, msg 4017) cannot pass: the module checks the file against ONE pinned
  sha256 at import. The CTO withdrew it and ruled (c): the module loads the config on FIRST USE, through one function, with the same
  single pin and the same named error. No test sha enters product code. Tests replace the loader's result with a synthetic dict.
- Round 55's order said the import-time load stays. This round reverses that one sentence, on the ruling.

**Rule 24.** Domain: the one module that loads the private config and the tests that import it -> one cell.

## Measured constraints (issuer)

1. **22 files import `commonwealth_sweeps` directly** (11 scripts, 11 tests, all under `data/assets/scripts/silver/`); more reach it
   through those. The module's public names stay importable so no importer needs an edit; an importer edit is a refusal, not a
   liberty.
2. **The chain output does not move.** The SWEEP-REGRADE line with the real config is the control.
3. **No S3 write, no deploy.** Row D2-S84: each hand-run invocation carries the variable; nothing is scheduled.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bd-1` | `commonwealth_sweeps` loads the private config on first use (single sha pin, same named error); the silver suite collects and passes with the variable unset; the SWEEP-REGRADE line is unchanged with the real config | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~83` |

**Fan-out:** `1 of 1 chains, cap 8`. DIRECT-ACT cell (one cell, under 300 product lines, LOCAL): its close is the one real run by
the issuer.
