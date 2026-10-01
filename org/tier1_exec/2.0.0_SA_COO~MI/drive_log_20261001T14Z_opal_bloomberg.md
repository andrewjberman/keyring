# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-01 14Z (host opal_bloomberg)

Lease FULL, round 6, limb L8 -> L9 -> L10 (held), thread y.

## Decisions closed this span

- **MX-v-7 COMPLETE**, drained @e00d3e15bc. Issuer re-grade on CLOUD:
  - v7.AC1 PASS: served transaction_fee 63.43 equals the source `silver/fees/2026-09-29.parquet` read by VersionId
    `Qp7FdHII...`;
  - as_of equal; denominators 22,853 / 22,221 / 632 on both sides;
  - proof VALID.
- **Drain hygiene (item 5):** 13 red gateway tests, all pre-existing at the live ref, 0 new, 1 fixed. Owners: 9
  NFRA_OPLGTW, 2 NFRA_OPALAI, 2 this project (stale against the live template, to the round-7 batch).
- **Round-6 drain-end packet** @235653342a to 3.0.0_SA_CVO~O. Alyssa's cold run (r6.J1) booked through 0.0.0_AB_MSTR~Z
  for Andrew; its prerequisite discover fix is served.
- **CVO L8/L9** @c5710a5111:
  - MXV7-J1 PASS (the r7.J1 re-grade); MXV7-J2 NOT_EVALUATED (Alyssa).
  - 27 rows: 7 graduated as OPEN slug rows (REMEDIATION_v5), 20 dismissed.
  - The slug is HELD for MX-s-16.
  - Correction: the realized and transaction documents (v3, held) still run the stale `scripts/` merge copy.
- **Train:** OG-rl-2 (slot 5) is deploying on e3567ce5f7 (COO~O msg 27890). MCPINDEX has no release queued.

## Next

- After the scheduled `bd-silver-merge` run (~00:1xZ 2026-10-02): read the unrealized SUMMARY (`failures=0 empty_stub=6`
  expected), close the `nfra-mcpindex-r6-bd-merge-retire` ledger, close MX-s-16 by A2's ruling, and release the slug.

## Compiler Tools

- `proof-of-spec-check.py`; `safe-merge.sh`; the round-6 battery (`v7.AC1.sh`).
