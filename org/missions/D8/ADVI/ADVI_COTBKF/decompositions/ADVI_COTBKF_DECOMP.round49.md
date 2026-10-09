# ADVI_COTBKF decomposition -- ROUND 49 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~15:5xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** the issuer's own ruling inside its decomposition (canonical-drive obligation 7). Round 38's CB-al-2 (the mint of Cottonwood
`account_return_daily`) is now unblocked on content:
- round 47's rebuild (~74, drained @9c6b230812): 3,325 days, every manifest and row `method_version` 3;
- the three valuation fields present;
- IRPT_DASHBD's producer 106 and handler 86 tests passing;
- the issuer's re-run byte-identical.

But it has NO apply path. The adapter `data/assets/scripts/silver/commonwealth_account_return_daily.py` offers only `--out` (a local
build) and `--verify-served`. CB-al-2's order says the applier lands each day through the producer's own `emit_day(upload=True)`. No
entry point does that, and an applier never writes code.

**Rule 24.** Domain: one missing mechanism -> one LOCAL cell: add the apply mode.

## Measured constraints (issuer, ~15:5xZ)

1. The adapter calls `ard.emit_day(s3, frame, SCOPE, ds, upload=False, ..., src=entry)` (:336). The producer's `emit_day(upload=True)`
   writes `<address>/data.parquet` and `<address>/manifest.json` (`account_return_daily.py` :1714-1745).
2. The local build is under `.scratch/advi_cotbkf/ard_cottonwood_r47/`. Its manifest
   (`deliverables/0.9.0_WK_ADVI_COTBKF~74/ard_cottonwood_manifest.json`, sha256 `56eafe04...`) carries, per day: `sha256`,
   `content_sha256`, `manifest_sha256`, and the address.
3. The target prefix `s3://opal-data-cottonwood/irpt/cottonwood/gold/account_return_daily/` holds 0 keys. The positive control
   `irpt/` reads 3 keys on the first page (issuer read ~15:5xZ).

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-aw-1` | `--apply` mode: lands each locally built day through the producer's `emit_day(upload=True)`, guarded (manifest sha match, empty-prefix check, a pair-file argument required); `--verify-served` on content hashes; tests with S3 faked; no real write | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~76` |

**Fan-out:** `1 of 1 chains, cap 8`. CB-al-2's pair is written on this drain.
