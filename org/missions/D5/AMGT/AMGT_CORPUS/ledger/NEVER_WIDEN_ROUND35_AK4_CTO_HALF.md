# AMGT_CORPUS round 35 -- CRPS-ak-4 never-widen pair, CTO half (unit-map rebuild for the 52, 96 re-derives, re-pin)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-04 ~02:2xZ. **COO half:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND35_AK4_SERVED_ACT.md`
@36ad5a67f9 (msg 29121). **Authority:** round-34 analysis @83cd052a9c, ruling 2 and section 3 item 1, under Andrew's card 3
(@9fe6e6f111).

## What I read

- **The dry run, `evidence/r35_ak4_dryrun.txt`:** over 100 names with raw landed, the 52 read 4,398 MEASURED and 802 UNRESOLVED.
  Every UNRESOLVED carries its reason (656 "no value returned", the rest zero-dominated or a named magnitude non-discrimination).
  The base comparison covers 6,600 entries. The 2 it flags are UNRESOLVED-to-UNRESOLVED re-samples (TSM `CURR_ENTP_VAL`,
  RKT `SI_PERCENT_EQUITY_FLOAT`), with no unit moved. The would-be map has 118 fields and 100 securities.
- **Writers:** 1 for the served block (`stage_derive`, reached by 4 callers), and 2 rules for a figure's unit (`_resolved_unit` on
  `field_map.json`, plus the per-security exception path). Both are named in the half.
- **Timing:** the legs run after the 13:00Z fire is read. A map write before then would be undone by the old pin's own map, and a
  re-pin before then would put new code under the acceptance fire. Both reasons hold.
- **Rollback:** revert the map commit; re-derive forward for the blocks (exact restore by delete stays Andrew's word); re-register
  the old pin. Each one is per key.

## Conditions

1. **The interpreter check runs BEFORE (m) as well**, with `-Plan -Commit HEAD` (the interpreter does not depend on the commit),
   and again before (r) with `<m>`. Branch C then stops before any write. As ordered, the gate names a `<m>` that does not exist yet.
2. **The legs run only if the 13:00Z fire closed clean** (its closing line and refresh line read success). If it did not, STOP:
   nothing is written, and the fire goes to the CVO's FWD-22 read first.
3. **(v) also prints the base-field VALUES moved** against each name's 13:00Z block, and the count must read 0. The same raw is
   re-derived, so any moved value is a defect: roll forward under the reverted map.
4. Branch B names every name that failed to derive, and the pointer-unit count in (v) excludes only those names.
5. One act, once. The NEVER-2 entry `amgt-corpus-r35-ak4` is opened at the start and closed at the end.

**CTO HALF: SIGNED** for CRPS-ak-4 (legs 0, m, d, r, v; branches A, B and C), under conditions 1-5.
