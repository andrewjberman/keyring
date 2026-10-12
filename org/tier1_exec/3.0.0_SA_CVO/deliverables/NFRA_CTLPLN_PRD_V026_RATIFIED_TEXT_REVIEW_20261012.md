# NFRA_CTLPLN PRD v0.26 -- ratified-text half (ENDPOINT + CONTRACTS) review

**Reviewer:** `3.0.0_SA_CVO~L` (laptop), on the L4-R delivery 1.0.0_SA_CTO msg 108582. 2026-10-12 ~14:3xZ.
**Verdict:** SIGNED.

## What was read

- PRD at dfec0d8ab6 (v0.26), unchanged at HEAD; previous signature at 579b691872 (v0.25).
- ratified-text half_hash `f58c33b1d1cbc9b1ffb98fc217f6a4fc14dea0eed86630612d12416d2a1dc26f`; endpoint_hash `7f30cdd39afe...`.
- `git diff 579b691872 dfec0d8ab6`: inside the ENDPOINT section, one line of FWD-28's ACCEPT is replaced by two. Class (ii)
  now refuses a caller "whose authorizer `tier` is not `internal` and whose `userType` is not `Dev`". FWD-1 to FWD-27, the rest
  of FWD-28 and CONTRACTS are unchanged.

## Checks

1. **Scope.** One clause widens class (ii) by exactly one admit path. Nothing else moves.
2. **The widening adds no new privilege class.**
   - `infra/aws/users/lambda/portal-authorizer/index.mjs:285,294-296` already grants a `userType Dev` login ALL access, and the
     portal shows it every page. Class (ii) now matches the authorizer instead of refusing a login the authorizer admits.
   - Where the value comes from: `auth-handler/src/db.ts:145` reads `userType` from the user's PROFILE row, and `jwt.ts:170-178`
     signs it into the token. The authorizer reads the signed claim (`index.mjs:390,406`). No handler in
     `infra/aws/opalinvest_dev/lambda/auth-handler/src` writes `userType`, so it is set only by a direct users-table edit.
   - The addendum's measurement (14:1xZ): 6 PROFILE rows carry Dev, and the 3 with a tier other than internal are all
     `firmId opal-capital`.
3. **Exact match on both values** is stated ("exact match on both"). It matches the authorizer's `=== 'Dev'`.
4. **Annotation:** "(the authorizer's own Dev-is-all rule; v0.26)" puts a version tag inside the ratified text. Not blocking;
   cut it at the next ENDPOINT bump, together with the earlier notes.

## Note for CT-aa-3 (not the text)

Defense in depth: the helper could also require `firmId == opal-capital` for the Dev path. Every Dev row is opal-capital
today, so the conjunct changes no answer. It would stop a mistaken Dev flag on a partner user's row from opening the 39
internal-only routes. The ENDPOINT does not require it; the CTO or the cell may choose it.
