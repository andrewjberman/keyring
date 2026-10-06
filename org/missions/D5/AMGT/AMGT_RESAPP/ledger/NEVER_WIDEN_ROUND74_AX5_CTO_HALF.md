# AMGT_RESAPP round 74 -- `AMGT-ax-5` never-widen pair, CTO half (font build fix + code + one greedy route on the portal proxy gateway)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-06 ~07:1xZ. **COO half:** `deliverables/2.0.0_SA_COO~Z/round74/NEVER_WIDEN_HALF_COO_AX5.md`
@ef57fb9fdc (66 lines, read in full; msg 29943). **Executor:** `0.7.0_AE_CloudOps~A`.

## Read live at signing

- **Function:** CodeSha256 `satkY3HXAhzfU7zYZ5fk+EmNHaqIRfj7bBtVlG4XfIY=`, MemorySize 1769. This equals the COO half's base.
- **Gateway `7k3ed8px20`:** 10 `GET /api/scoped/amgt/security/{security_key}/...` routes, all `CUSTOM`, 0 greedy. This equals the base.
- **Every route in `scoped-amgt-api.tf` is made by ONE `for_each` resource** (`:545`). It sets `authorization_type = "CUSTOM"` and the
  portal authorizer for each key (`:559-560`). So the added greedy key carries the same authorizer by construction.
- **The fonts:** Lato is the portal's own face (`portal/src/index.css:39,47`). Packaging it with its licence for the print uses the
  estate's existing brand asset, per round-73 ruling 2. No new styling is invented.

## Conditions

1. **Item 0 is committed alone,** and it is the build commit. The content diff is exactly CHANGED 4 and ADDED 3 (two Lato faces and the
   licence). Any other file is a STOP. Read back the new CodeSha256 with MemorySize 1769.
2. **The route leg's plan is exactly 1 to add, 0 to change, 0 to destroy.** After it:
   - the security GET routes read 11, with 1 greedy, and **all `CUSTOM`**;
   - **a negative control:** an UNAUTHENTICATED GET on a slash-key path through the greedy route answers 401, so the authorizer
     applies;
   - **a positive control:** an authenticated GET on `BP/_LN_Equity` and `NG/_LN_Equity` answers 200 on all 4 of Z-S276's routes.
3. **c55 is a PIN from this act on** (round-73 ruling 4). Every later redeploy of this function runs it.
4. **After the code leg:**
   - c53 shows a warm `/freshness` under about 2 s, with values EQUAL to the uncached read on all 292 rows;
   - c56 shows Lato in the rendered print;
   - the r71-r73 regression checks still read YES;
   - the cold read is reported with its phase table.
   Provisioned concurrency comes off Andrew's list only if the cold read falls under about 2 s.
5. **One NEVER-2 entry,** in the DEPLOY genre. Read every live worktree first. Rollback per key as the COO half's table.

**CTO HALF: SIGNED** for `AMGT-ax-5` under conditions 1-5.
