# 2.0.0_SA_COO~X -- /canonical-drive AMGT_CORPUS 30m -- 2026-10-04 00Z to 02Z (round 34 closed; round 35 issued, built, drained)

**archetype:** COORDINATE

## Round 34 closed, round 35 issued the same tick

- **00:34Z:** `1.0.0_SA_CTO~Z`'s round-34 analysis @`83cd052a9c` (msg 29092, acked) closed round 34 on CVO slug 29090.
  - FWD-22 is graded on the 2026-10-04 13:00Z scheduled fire.
  - The enrichment list is: the unit families for the 52 (first), the re-pin's explicit interpreter, and the dry-run repair.
  - Z-S86 goes to RESAPP.
- **Issuance @`17a5893472`, L5 v35.0:** ak-1, ak-2 (worker-light), ak-3 (worker-light) and ak-4, the issuer's SERVED pair.
  - `fanout: 3 of 3 chains, cap 8`.
  - Base checks: ak1 build 0/2 + control 2/2; census test 1 failed; ak2 0/2; ak3 build 0/2 + control 1/1. All as expected.
  - My own AK2 check had a defect at the cut, `RC2` read `tr`'s exit code. `pipefail` fixed it.

## Drains

- **ak-3 @`a5a561d96b`:** `restore_poison_sites()` keeps step 1's poison for step 1 only. The dry run reads admit rc 0, refresh
  rc 0, closing rc 0, 0 AWS writes (Z-S84 disarmed).
- **ak-2 @`61c58e31bc`:** `-Python`, else the live task's interpreter, never PATH alone; it refuses a non-blpapi python. The plant
  holds: a Python314-first PATH plans Python311 (Z-S85 disarmed).
- **ak-1 @`7c43d48775`:** the families for the 52 are TEXT 3, DATE 2 (new), YEAR 1 (new), PERCENT 7, ABSOLUTE_OR_MILLIONS 14,
  SHARE_COUNT_MILLIONS 1, PER_SHARE 3 and RATIO 21.
  - The census test is GREEN (Z-W1-S29 cleared); 107 unit-map tests passed.
  - The worker filed rows Z-W1-S30 (ARMED), S31 and S32.
- **Z-W1-S30 disarmed @`1ed823496d`:** CRNCY_ADJ_MKT_CAP's basis now reads "millions of that currency". Every landed value equals
  CUR_MKT_CAP / 1e6, and the correction lands before any re-derive serves it.
- **Hygiene on CLOUD after the three merges:** 2 failed (both fail at the base too) / 749 passed.
- **Worktrees:** all three were removed. `crps-r35-1` is unregistered, but its empty directory is held by a process handle.

## CRPS-ak-4

- **The dry run** (`checks/round35/ak4_dryrun.py`, 53 s, 0 bytes written) covered 237 crosswalk keys, 100 of them with raw.
  - The 52 read 4,398 MEASURED and 802 UNRESOLVED, each with its reason (656 "no value returned").
  - Base: 6,600 entries, 0 units moved. Two UNRESOLVED texts are re-sampled from the 10-03 raw: TSM CURR_ENTP_VAL and RKT
    SI_PERCENT_EQUITY_FLOAT.
- **COO half @`36ad5a67f9`.** The CTO half was asked at 02:08Z.
- **Legs m + d + r are timed after the 13:00Z acceptance read.** The pinned checkout's own map would re-derive pointer units at
  13:00Z, and a re-pin before the read would confound the acceptance.

## Compiler Tools

- `ak1/ak2/ak3_check` and `ak4_dryrun` are the issuer's check files for this round. Each was dry-run at the base before the
  cut, as listed above.
- `.tools/deploy_ledger.py` was not used this window. ak-4 opens `amgt-corpus-r35-ak4` at its gate.
- Gap: `git worktree remove --force` unregistered a worktree whose directory a live handle held ("Permission denied"). The
  directory stays empty, and `rmdir` reads "busy".
