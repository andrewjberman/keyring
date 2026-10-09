# ADVI_COTBKF decomposition -- ROUND 41 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~14:1xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s ADDENDUM 13 @9326a48990 (msg 3423). Rounds 36 and 39 are MET, and D2-S52 is CLOSED. This issuance
is ONE SERVED cell, which deploys the round-39 `_ff_worker` carry-forward stamp under its own pair.
- Its census shows only the carry-forward members.
- Its proof drives the carry-forward on a synthetic day and reads the stamp. The path is unreachable for cot today, so the proof is
  not read from a live fire.
- Round 38 stays held, only on IRPT_DASHBD 13.1's sources-fields cell.
- Round 40 (`source_firm`) is running.

**Rule 24.** Domain: one item -> one cell.

## Measured constraints (issuer, ~14:1xZ)

1. **The deployed key** is `s3://opal-data-cot/code/gold/B_00.canonical_holdings.py`:
   - VersionId `BMqu7SNCbx2f3bQ_Tr56xMBCvtMe3van`, LastModified 2026-10-02T17:43:29Z, 65,249 bytes;
   - sha256 `6dbf6a86e734f514c92421e8e6ca9a9168bd8b6b90f742857f0f86d83c0d69a8`.
   It is BYTE-IDENTICAL to the repo file before round 39's change (`git show 88e7452955^1:...`). The deploy therefore moves exactly
   round 39's diff (+25/-1 lines in `_ff_worker`) and nothing else.
2. **The file to deploy** is `data/cot/scripts/gold/B_00.canonical_holdings.py` at HEAD, sha256
   `45fbbd921f026f9d4e30785e632c8f8e0feeb02730f033b96fd03b23da74c08d`.
3. **Deploy tool:** `.tools/safe-deploy.sh` (CLAUDE.md rule 13; `data/cot/scripts/{gold,...}` maps to `opal-data-cot`). It does
   S3 cp, SHA verify and the comp-pipescript confirm.
4. **Readers of the key:** the cot gold run's `aws s3 sync s3://$BD_S3_BUCKET/code/gold/` (`gold_dispatch.sh`:497-498). `_ff_worker`
   is reached only when `schwab/silver/rps/` holds data (empty today; CTO-measured).

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ao-1` | deploy `B_00.canonical_holdings.py` (the `_ff_worker` stamp) to the cot code mirror under a never-widen pair; read back the bytes; the stamp proven on a synthetic day against those bytes | FWD-3 | SERVED | both pair halves | `0.7.0_AE_CloudOps~CB2` |

**Fan-out:** `1 of 1 chains, cap 8`.
