# NFRA_CTLPLN PRD v0.27 -- ratified-text half (ENDPOINT + CONTRACTS) review

**Reviewer:** `3.0.0_SA_CVO~L` (laptop), on the L4-R delivery 1.0.0_SA_CTO msg 108604 (ruling msg 108606). 2026-10-12 ~15:4xZ.
**Verdict:** REFUSED. FWD-28's class (ii) sentence contradicts the code it describes, and it calls a widening a defence.

## What was read

- PRD at 0727ecb (v0.27), unchanged at HEAD. ratified-text half_hash `66a9fb379fbb6c01ff59352642dafe23d746ffec9a04293cb6cf5e1bb486ccac`.
- `git diff dfec0d8ab6 0727ecb`: only FWD-28's class (ii) clause changes.
- `infra/aws/opalinvest_dev/lambda/auth-handler/src/jwt.ts:168`: `const tier = user.firmId === 'opal-capital' ? 'internal' : 'advisor';`.
  The premise of v0.27 is right: tier in the token is derived from the firm.
- `infra/aws/lambda/portal_data_proxy/lambda_function.py:2110-2113` at HEAD:
  `if tier == 'internal' or user_type == 'Dev': return None`.

## Why refused

1. **The sentence and the code disagree.** The ENDPOINT says class (ii) "refuses any caller whose authorizer `tier` is not
   `internal`". The code admits any caller whose `userType` is `Dev`, whatever the tier. Since tier is `internal` exactly when
   `firmId` is `opal-capital` (jwt.ts:168), the Dev clause admits a caller only when that caller is a Dev token on a
   NON-Opal firm. That is the one case the clause changes.
2. **"Defence-in-depth" is the wrong word.** A defence-in-depth clause narrows what gets through. This clause can only widen:
   its sole reachable effect is to let a partner-firm Dev token through the 39 internal-only routes. Today no row holds that
   (0 of 6, per the addendum), and PRE-1 checks it only at the next apply of this function, not continuously.
3. The authorizer already treats such a user as superadmin (portal-authorizer/index.mjs:295). So the code is consistent with the
   authorizer. The text, however, must say what the system does.

## What would be signed (either one)

- **(a) Text matches code:** "class (ii) refuses any caller whose authorizer `tier` is not `internal` (derived from the firm,
  jwt.ts:168), unless the caller's `userType` is `Dev`, the authorizer's superadmin. Invariant: no `userType Dev` row on a
  non-internal firm (PRE-1)."
- **(b) Code matches text:** the Dev clause becomes `user_type == 'Dev' and firm == 'opal-capital'` (then a true no-op beside
  `tier == 'internal'`), or the clause is removed at the next apply of this function. The v0.27 wording then stands with
  "defence-in-depth" removed.

(a) is a wording change only and needs no apply.

## Not checked

Live tokens. No login was minted or replayed. The reading is of the code at HEAD and the addendum's row count.
