# CTO ROUND-120 ANALYSIS -- IRPT_DASHBD workstream B-IN (Inflection) -- the missing account's reason class, measured on a second household (2026-10-15 ~05:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `2.0.0_SA_COO~I2` msg 8076, packet
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND119_BIN_DRAIN_END_20261015.md` @1721081b18: 1 of 1 PASS. The
missing account is active in Orion's roster, no exclusion flag differs, and its record has a null `accountStartDate` and
`accountStartValue` and no `modelName`. 40 of 863 roster accounts share the null start date. The CVO~IRPT slug closes the books behind this
round. Issuer: `~I2`, ONE issuance.

## Rulings

1. **The reason classes are adopted, with their claim carried:** `NO_START_DATE_AT_SOURCE` (null `accountStartDate`) and
   `NO_MODEL_AT_SOURCE` (a start date but no `modelName`).
   - The feed derives them by joining the roster the pull already lands (`accounts_v2`), with no extra vendor call.
   - The record's null field is MEASURED. That it CAUSES the missing Scope group is INFERRED from one account.
   - So the feed's reason row carries `claim: inferred` until ruling 2 measures it (CLAUDE.md, a value carries its claim).
2. **The second-household probe runs** (`~I2`, a WORLD read, cap 2 Scope calls, paced, no retry, inner-scope body). It covers one household
   that holds one account with a null start date and one with no model. Both are chosen by a rule the checker recomputes.
   - If both are missing from Scope and every other account is present, the claim becomes `measured (2 households)`.
   - If not, the classes stay inferred and the page keeps the neutral words.
3. **The page words state only what is measured.** Until ruling 2 measures the link, an account page says "Account-level returns are not
   available for this account yet." It does not name a cause it has not shown. Once measured, it may add "Orion has no start date recorded
   for this account."
4. **Fixing the 40 accounts at the source** is a request to Inflection's own operations: a partner firm, outside Opal. That is an
   outward-facing message on Opal's behalf, so it is an act for Andrew, filed with a draft. The draft names the 40 accounts' count and the two
   fields only, and no account ids in the repo. It is filed after ruling 2 lands, so the ask states a measured pattern. The 117 accounts not
   in the active roster are a separate class and are not in the ask.
5. **S60 stays ARMED** on `~P2`'s feed half, as the issuer states.

## Round-120 cell (ONE issuance by `~I2`)

1. The second-household probe (ruling 2).

-- 1.0.0_SA_CTO~DELL2
