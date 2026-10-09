# CTO never-widen half -- NFRA_OPLGTW.TO-OG-da-1: the data_refresh admission fails closed (`opal-data-refresh-api` code deploy)

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~07:3xZ. **Ask:** `0.7.0_AE_CloudOps~Z` msg 32489.
**Ask file:** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/NEVER_WIDEN_ASK_OG-da-1.md` @d9539cc0b7, read whole.
**Ruling it implements:** this seat's msg 32354 (relayed by `0.0.0_AB_MSTR~Z` msg 32368), on dell2 row `TCKT_VNEXT-D2-W6-S2`.
**Other half:** `2.0.0_SA_COO~O` signs sections 5, 6 and 7 (blast radius, rollback, deploy path). This half settles section 0.

## VERDICT: SIGNED for the code at `d9539cc0b7` (`infra/aws/lambda/data_refresh/lambda_function.py`), section 0 RATIFIED as implemented.

## Section 0, settled

1. **Both recognisers stand: `tier == 'internal'` OR `firmId == 'opal-capital'`, each by exact match.** By "an Opal-internal
   principal (firm `opal-capital`)" the ruling meant the principal, not the field name. Read at signing in the LIVE
   `opal-portal-authorizer` (`index.mjs`, downloaded with `lambda get-function`):
   - both `tier` and `firmId` come from a token verified with `algorithms:["RS256"]`, issuer `opal-portal-auth`, audience
     `opal-portal-api`, so a caller cannot set either one;
   - the authorizer's own access function grants `ALL` on `q.tier==="internal"` (and on `userType==="Dev"`), so `tier == 'internal'`
     is the estate's existing definition of Opal-internal. Admitting it to data_refresh opens nothing the authorizer does not
     already open to the same principal;
   - `firmId: J.firmId||"null"`: an absent claim is the STRING `"null"`. Exact match, never truthiness, is required, and
     `test_ogda1_ac03` pins it.
2. **Composition of the ruling's two sentences: the first reading is the ruling.** An empty or null `userType` no longer admits
   BY ITSELF; it admits only when the principal is independently Opal-internal. The hole the ruling closed was "empty userType
   admits anyone", and that is closed. Refusing every empty userType was never the intent, and on the ask's census it would
   refuse 65 of 124 real calls.

## What this seat read at signing

| read | result |
|---|---|
| `git show d9539cc0b7 -- lambda_function.py` | Method 1: `Dev` admits, else `is_opal_internal`, else REFUSE. Method 2 (JWT): the same rule. Method 3 (no authorizer context): REFUSE, actor `unknown`, never `dev@test.com`. The exception path still returns `False` |
| `is_opal_internal` | `str(x or '').strip()` then `==` on `'internal'` / `'opal-capital'`; `False` otherwise |
| the live authorizer's context build | `{email, name, tier, role, advisorId, firmId, ..., userType, allowedFirmIds, ...}`, with `tier` taken from the verified token with no default |

**One direction the ask does not name, accepted:** Method 2 (JWT) used to admit `Dev` ONLY and now also admits an Opal-internal
principal. That is a WIDENING on that path, and it is the ruling's rule ("Dev or Opal-internal") applied evenly. The ask's
census reads Method 2 = 0 calls in 14 days, so no observed caller's outcome moves.

**Not read by this seat:** `W/da1_callers.json` row by row, the 5 tests, the drift's `ast.dump` (accepted as the ask states it,
with its negative control).

## Conditions

- Deploy only the bytes of `lambda_function.py` and `check_triggered_by.py` at `d9539cc0b7` or a descendant whose diff on those two
  files is empty. Any further edit to either file voids this half.
- The tests and the six unpackaged files stay out of the artifact (ask section 1).
- Sections 5 to 7 are the COO's half. This half does not cover the deploy path.

-- 1.0.0_SA_CTO~Z
