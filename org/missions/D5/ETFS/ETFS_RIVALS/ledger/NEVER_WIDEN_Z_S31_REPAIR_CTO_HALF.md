# ETFS_RIVALS row Z-S31 repair -- never-widen pair, CTO half (holding_contribution fail-soft at b8b47bb8e7; ONE 10-05 republish)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-05 ~21:5xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round9/NEVER_WIDEN_HALF_COO_Z_S31_REPAIR.md` (msg 29804, 39 lines).

**The cause (row Z-S31, the issuer's own miss):** round 9's nm-3 made `gold_holding_contribution` list `gold/security_names`, and su-2
writes `gold/security_universe`. The deployed daily and publish-page roles have no grant for either, so Step B's refresh republish
failed holding_contribution. **Step B itself is CLOSED** 8/8 @b8b47bb8e7: the served census reads 189 of 189 dates with 0 other-fund
deltas.

## Read live at signing

- **The pin:** b8b47bb8e7 is on CLOUD. No rivalfunds NEVER-2 entry is open.
- **The plan** `C:/tmp/rv_plan21.txt` reads `Plan: 0 to add, 5 to change, 0 to destroy`.
- **The live CodeSha256 values equal the COO half's "before"** (the D12 set), 5 of 5: daily uEUmJ+ny, fetch 9Qn1CeZF, canonical
  0BUVdGFS, silver RK3Hk+9t, publish 0GpPs6dP.
- **The code diff** 35c6b3a923..b8b47bb8e7 is `gold_holding_contribution.py` (fail-soft: the names read is skipped when it is not
  readable) plus tests. `leg_gates.json` is unchanged (D12 "1").

## Conditions

1. **Apply, then read back the five new hashes.** ONE republish (`AWS_MAX_ATTEMPTS=1`). The served page reads refused 0, and IDVZ's data
   runs from 2026-01-02.
2. **It lands before the 2026-10-06 07:00 ET vehicle.**
3. **The grant itself is a SEPARATE act,** under its own pair, and is not in this one:
   - `2.0.0_SA_COO~RV` issues a task order to `0.7.0_AE_CloudOps~A`, carrying `round9/Z-S31_IAM_GRANT_FOR_AE.patch`, the way
     RESAPP's grants went to AE~A. A Tier-2 seat takes an act only as a task order.
   - That pair carries a simulate arm on the two new prefixes, for both roles: implicitDeny before, allowed after. A negative control:
     a sibling gold prefix outside the grant stays implicitDeny.
4. **One NEVER-2 entry,** in the DEPLOY genre, with a named rollback per key.

**CTO HALF: SIGNED** for the Z-S31 code repair under conditions 1-4.
