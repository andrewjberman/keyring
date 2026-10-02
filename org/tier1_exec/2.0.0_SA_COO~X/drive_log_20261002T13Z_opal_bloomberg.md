# 2.0.0_SA_COO~X -- /canonical-drive AMGT_CORPUS 30m -- 2026-10-02 06Z to 13Z

**archetype:** VALIDATE

## Ticks 2-17 (05:16Z to 12:46Z): NO-OP by round-31 ruling 1

- No CORPUS-tree commit landed in that window other than this seat's own, and no walk-through finding was filed.
- At every tick, `tabs/ModelTab.tsx` (c6aacc68) and `modelSheet.ts` (c8119301) were unchanged on local DEV, origin DEV and
  origin PROD b3a1d8a6. So the demo's Model tab was CORPUS's own face at 13:00Z.

## 13:2xZ: ARMED census (Andrew's GO on this seat's /next-steps option 1)

- Instrument: `surprise-row-gate._latest_dispositions`, the fold the L10 limb reads. The rows' `hazard_standing` field
  was not used.
- Of 45 rows filed ARMED, 36 resolve GRADUATED and 9 resolve open:
  - Z-S3 is the fabric's (CTO~Z).
  - Seven carry an owner's disarm awaiting the CVO's clock: Z-S12 and Z-S48 (both re-verified at HEAD), Z-S77 and Z-S78
    (new).
  - Z-W4-S6 is LIVE, narrowed by Z-S79. For BP and NG, the Peers raw-key lookup (`engine.py:165`) reads the 09-25
    blocks. Their values are equal to the 09-30 blocks; their unit, sign and currency labels are stale.
- Rows Z-S77..Z-S80 landed at 00a7083e85 and the row gate passed them.
- One ask went to `3.0.0_SA_CVO~Z` (msg 28482), READ 13:30:23Z.

## Tick 18 (13:31Z)

NO-OP: the lease is FULL and there is no new CORPUS commit. PROD is still b3a1d8a6, and both Model-tab files are
unchanged.

**Carried for round 32, behind the round-31 analysis's after-Friday hold:**
- Z-S74 (unit-claim predicates);
- the BEST_DIV_YLD label (needs the pair);
- Z-W4-S6's one-line Peers lookup fix (Z-S79);
- FWD-20 and FWD-22, on Andrew's word.
