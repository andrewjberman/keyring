# 2.0.0_SA_COO~H drive log -- 2026-10-01 05:3xZ-06:5xZ (host opal_bloomberg)

Arm: `/canonical-drive AMGT_HARVST 30m` (cron 079d5acb). Lease: FULL. Round 32 (issued @`a1eb58cd75`).

## Drains

| order | phase | drained | trunk suite after |
|---|---|---|---|
| `ae-4` driver | A | `4732ca8c57` | -- |
| `ae-2` one identity | complete | `594d7be519` | 386 passed (with the drain fixes below) |
| `ae-1` wrong-object | A + AMENDMENT 1 | `05198fa747` | 395 passed |
| `ae-5` challenge path | A | `021cf42819` | 414 passed (with both hookups) |

- **The shared index** carried peers' staged files twice (CVO ETFS_RIVALS, then CORPUS). The drains ran from a background
  loop at the first clear index. No peer state was touched.
- **Channel conflicts** (append-only, the expected case) were resolved by row union. The channel parsed at 202 and then
  205 rows, with 0 duplicate ids.

## Rulings and issuer acts

- **`ae-2` drain fixes** @`250c895b8e`:
  - `Z-W91-S1`: the base write-back test is inverted.
  - `contracts.json`: `body_format` is restored. The worker had overwritten ft's and wsj's body descriptors. The edit was
    made byte-level, so HEAD's mixed line endings are kept.
- **`ae-1` AMENDMENT 1** @`cec6fb0ba6`:
  - `Z-W90-S1` ACCEPTED: the `{"data": item}` bronze capture.
  - `Z-W90-S2` RULED: a stored listing item counts as fetched, and the sa arms of the base tests are updated.
  - The prior `~90` worker could not be resumed, so a fresh one did it.
- **`ae-5` AMENDMENT 1** @`bd29533457`:
  - Phase A was dispatched ahead of first light; it has no data edge on it.
  - Discovery goes in a new `discovery.py`.
- **Hookup** @`877e8ff5ac`:
  - `publishers.py` reaches every `"transport": "tab"` publisher through `TabSession`, seeded once from the bundle.
  - Request headers travel in-tab, minus User-Agent and Cookie.
  - `test_ae2_hookup.py` adds 7 tests. The negative control (pre-hookup `publishers.py`) reads 7 failed.
- **Hookup** @`a7dbc71874`:
  - `PacedSession.get` routes a tab leg's bot check to `route_bot_check` once, retrying the same request once.
  - `test_ae5_hookup.py` adds 5 tests. The negative control reads 3 failed, and the 2 base controls pass.
  - It sits one level below the worker's named site, because the worker handler cannot retry "the blocked request".
- **`ae-1` phase B signing** @`8b44d101ac` (AMENDMENT 2):
  - With the 33 quarantined keys, `build_mention` reproduces served gold exactly (379 rows, 0 moves).
  - Under NEVER-1 (a verified DELTA=0) phase B needs no pair. `build-daily` is dropped and a digest gate is added.
  - The CTO ACCEPTED (msg 27574) on one condition: daily WITH vs WITHOUT the keys must be equal. Measured EQUAL @`b86a5069b4`
    (52,334 rows, identical digest).
  - Phase B was handed to a fresh `~90` worker.
- **`ae-4` AMENDMENT 1** @`d45014a87e`:
  - Phase B carries no pair: it is vendor egress under R-21, which is scripted, and it moves no served gold.
  - It starts after `ae-1` B.
  - The worker proves stop/resume on 6 names. The issuer runs the full 89.

## Rows

`Z-W90-S1`/`S2`/`S3`, `Z-W91-S1`/`S2`/`S3`: all ruled or INERT.
- `Z-W91-S2`: the bbg/wsj date-ordered routes are UNMEASURED. First light and `ae-5` B measure them.
- `Z-W91-S3`: bbg has no in-profile sign-in, so wsj or barrons carries FWD-11's renewal half.
