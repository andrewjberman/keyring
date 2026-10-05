# /canonical-drive AMGT_RESAPP -- 2.0.0_SA_COO~Z -- 2026-10-04 20Z hour (opal_bloomberg)

Relaunch after the site-Z crash (18:58Z). Loop re-armed on Andrew's "2.) Yes" (MSTR~Z msg 29202, record @3166fec43e;
`org/ref/LIVE_ARMS.md` lines 33-71): cron `d0bb31b4`, 30m. Lease FULL.

| project | limb | round | TOs t/T | cells c/F | thread | act fired |
|---|---|---|---|---|---|---|
| AMGT_RESAPP | L7 drain -> WORLD leg | 67 | 4/5 | 4/4 drained | n (the real run is aq-5 on deployed) | DRIVE FORWARD (described below) |

## Acts

- **Drains**, all through `safe-merge.sh`, each carrying its issuer close. Every proof-of-spec instance is VALID.
  - aq-1 `fa22ce3149`: AC1-AC3 PASS.
  - aq-3 `e5ea575b16`: AC1-AC3 PASS.
  - aq-2 `aac5a586d1`: AC1 and AC3 PASS. AC2 FAILS on producer coverage: 21 of 95 covered names have no chatter_window row
    (row Z-W220-S1).
  - aq-4 `d8bafe6896`. The first worker had written its instance at ~03:20Z and stalled before committing. Slot ~222 was
    re-seated on that inherited state, and the new worker re-ran every criterion: build `2719915e9c`, AC1-AC3 PASS.
- **Drain hygiene on the merged tree.** py_compile and ruff are clean, and the api suite reads 535 passed. Local reads:
  r67 c23, c25 and c26 are YES; c24 is NO on the 21-name clause only. r64 c9-c14, r65 c17 and r66 c18/c19/c22 are all YES
  at the pin.
- **The `--build-only` at `d8bafe6896` found a STOP before any GO**, filed as row `AMGT_RESAPP-Z-S345`.
  - aq-4 reads the scanner sp500 universe, and the role reads it as implicitDeny.
  - So aq-5 was amended to put a one-statement grant leg ahead of the code leg.
  - COO half `round67/NEVER_WIDEN_HALF_COO_AQ5.md`, with the amendment, @0e415a64d9.
- **CTO half requested** from 1.0.0_SA_CTO~Z (one [DECISION] message).

## Next

Once the CTO half is signed: spawn `0.7.0_AE_CloudOps~A` (it is not registered) with the aq-5 GO. Then compile L8 on the
deployed reads and send the drain-end read.
