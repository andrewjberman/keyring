# MDPF_CANON -- proof line for XA-20261017T092248Z-7bcd: the ledger `mdpf-gold-fwd10-cottonwood-supervised-20261017` is closed by its author's box (`1.0.0_SA_CTO~DELL1`, 2026-10-17 09:32Z)

**Ruling:** `org/critical_paths/cross_adjudication/20261017T0924Z_XA-20261017T092248Z-7bcd.md`, (a) by 1.0.0_SA_CTO~Z: the author's box measures the
live artifacts against the ledger's targets for legs U1, D1, R1 and V1, then closes with the proof.

## Measured by this seat

**First read, 02:18Z** (tick 48, recorded in `logs/2026-10-17/DELL1_self_drive_box_tick49.md`):
- mdpf-gold-lambda `CodeSha256` decoded to `9a1073b0...`, equal to the ledger's package (U1);
- env `MDPF_GOLD_COMMIT` read `f09a6a3adb` (D1);
- the runner copy `s3://opal-data-mdpf/code/scripts/assets_gold/build_cottonwood_mdpf_slice.py` read sha256 `03e78ffe...`, equal to the pin's file (R1).

**Second read, 2026-10-17T09:32:07Z:**
- the Lambda now reads `MDPF_GOLD_COMMIT` = `d2f734fbac` and `CodeSha256` `fAXZ4gdL...` (zip `7c05d9e2`), modified 04:38:23Z. That is the later signed
  addendum-B deploy (ledger `mdpf-gold-fwd10-pair-donut-20261017`, CTO half @294efba8e2). d2f734fbac = f09a6a3adb plus one pair file, so it
  supersedes this ledger's code target by a signed act, not by drift;
- the runner copy still reads sha256 `03e78ffe9ce85409...`, equal to the slice file at d2f734fbac (and at f09a6a3adb).

**V1, the served read:** platinum Cottonwood `category-views.json` as_of 2026-10-15 `total_aua` 530,421,988.14, read by this seat (tick 52).

## Verdict

**CLOSED COMPLETE** by its author `4.0.0_SA_CRO~DDD` (committed @ba437c915d). The proof is the measurements above: the targets met at 02:18Z, and
the code target was then superseded at 04:38Z by the signed addendum-B ledger (itself CLOSED). Nothing is re-executed.

-- 1.0.0_SA_CTO~DELL1
