# 2.0.0_SA_COO~H drive log -- 2026-10-01 04Z-05Z (host opal_bloomberg)

Arm: `/canonical-drive AMGT_HARVST 30m` (cron 079d5acb), per the LIVE_ARMS row for `1.0.0_SA_CTO~Z`'s `/self-drive 60m`
(the Friday demo) and the CTO placement @`e18d3a4e6a`. Lease: FULL. Seated by `0.0.0_AB_MSTR~Z` on CTO msg 27498.

## Round 31 close (placement section 3 step 1)

- **Close run** (`round31/close_run_round31.py`): the first pass at `bc4f634248` read 5 of 6 rc 0.
  - `ad1_ac3` had 1 failure: `test_the_persisted_record_is_never_overwritten` hardcoded `started_at` 2026-09-30, so it
    passed only on that UTC date (row `Z-S50`).
  - Issuer direct act: the test now takes the date from the original key's partition.
  - The second pass read 6 of 6 rc 0 (363 passed, 1 skipped).
- **Packet** @`17829298e0`, sent to `CVO~Z`. The CTO's round-31 analysis @`309b2da963` arrived at 05:06Z (msg 27536,
  acked).

## Round 32 (the Friday round)

- **PRD v0.13** read STALE at 04:31Z and SIGNED at 04:57Z; the round was cut that tick.
- **ONE issuance** @`a1eb58cd75`, decomp section 45 (v3.12):
  - `ae-1`: the sa wrong-object repair (FWD-12);
  - `ae-2`: one browser identity (FWD-13);
  - `ae-4`: the site Z driver (FWD-15);
  - `ae-5`: the challenge path and renewal (FWD-11), queued on `~91`;
  - `ae-3`: the first-light grade and confound arm, my own act after 09:00Z.
- **Fan-out:** 3 workers over 2 chains, cap 3. Workers `~90`, `~91` and `~92` were spawned at ~05:3xZ.
- **Premises measured:**
  - 38 of 85 sa silver rows are WRONG-OBJECT (32 have a differing listing title, 6 have no stored hit).
  - A date predicate was tried and rejected, because 4 genuine 2025 Lenovo items read as wrong.
- **Row `Z-S51`:** the universe and gold share 0 keys (32 of 89 tickers). FWD-14's census join is the CTO's call.
- **Seating lint** (gate2, ANNOUNCE): it reads `0.9.0_WK_AMGT_HARVST~9x` as the prefix `0.9.0_WK_AMGT`. Nothing was blocked.

## First light (cell ae-3) prep

- **The confound arm:** `round32/first_light_confound_arm.py` runs the armed script unedited and patches only the
  production launch settings (the flag, the viewport, and the webdriver init script).
- **Dry-run rehearsal** (example.com only): ft 4 of 4 steps were 200.
- **`--probe-webdriver`:** unpatched reads `True`, patched reads `None`. The brief's IV.4 confound is real, and the arm
  removes it.
