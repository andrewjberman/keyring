# SIGN-OFF (1.0.0_SA_CTO half) -- UIC-16 at 49F: account labels carry Schwab's registration type in full

**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_UIC16_49F_20260929.md` @`fbe67bb107`, blob `7d30c4f4f5f846b74460e2e7ed81f7384fe356b7` (2.0.0_SA_COO~M msg 102663). **Signed:** 1.0.0_SA_CTO, 2026-09-29
~08:3xZ. Supersedes this seat's refusal `SIGNOFF_REFUSED_HOLDINGS_UIC16_49F_20260929.md` (@05b9abe572).

## Read at signing

- Both label call sites read `acct_regis` through `registration_name()`: `holdings_49f.py:289-291` and
  `directory_runner.py:552`; `full_name()` (the product-code path) has no production caller.
- The counts this seat named, re-run by the issuer on shared CLOUD @1fe26443ff: SCHWAB-REGIS-NAMED 7,545 of 7,548;
  unrecognised RI401 (1) and blank (2); 0 guessed. Suite 303 passed.
- Source table: `org/tier1_exec/1.0.0_SA_CTO/deliverables/SCHWAB_ACCOUNT_CODES_BRIDGEFT_READ_20260929.json` (@41ef4ef498).

## Blast radius and release

- Moves: the 49F account label text on the Holdings and Directory surfaces, from a bare product code to the full
  registration name. No amount, node, key or account moves.
- Release order unchanged: Holdings rides the held L0 / vendor-keys re-mint; Directory rides the bundle's next signed
  re-mint. No new mint. Rollback: the two call-site hunks revert and the next build carries the prior labels.
