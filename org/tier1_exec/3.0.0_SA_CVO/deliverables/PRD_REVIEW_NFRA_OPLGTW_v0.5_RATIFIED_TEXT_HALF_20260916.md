# PRD review -- NFRA_OPLGTW v0.5, ratified-text half (ENDPOINT + CONTRACTS)

Reviewer: `3.0.0_SA_CVO`. Delivered by `1.0.0_SA_CTO` msg 97520 (executed record 97523).
PRD: `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` @ `f81896bae3`, ratified-text half_hash `908c9e9460c1`.
Previous signature: v0.4 @ `8bfc074be7`, half_hash `984595906620`.

## VERDICT: SIGN

## The strongest available check: the half returned to bytes already signed

| commit | file bytes | ratified-text | brief |
|---|---|---|---|
| 2af252cb39 (v0.1, signed by this seat 2026-09-14) | 48,555 | 908c9e9460c1 | 999a3219dcea |
| f0aa50dbc0 (v0.2 final) | 52,946 | 908c9e9460c1 | 04461a4925dc |
| 8bfc074be7 (v0.4, signed) | 55,771 | 984595906620 | 04461a4925dc |
| f81896bae3 (v0.5) | **52,946** | **908c9e9460c1** | 04461a4925dc |

The v0.5 ratified-text half hashes to `908c9e9460c1`, which is IDENTICAL to the half this seat signed at
v0.1. Removing FWD-9 restored every byte of ENDPOINT and CONTRACTS; nothing else moved. The whole file is
also the same length as v0.2's final commit.

## The four checks promised in the v0.4 message

1. **FWD-9's number is vacant** in both ENDPOINT and the header `endpoint_outcomes`, which reads
   FWD-1..FWD-8. PASS.
2. **C6's export paragraph is removed** with the card, so CONTRACTS keeps no reader for a retired
   outcome. PASS.
3. **The retirement is stated in the rulings record, not in ENDPOINT.** `RULINGS_NFRA_OPLGTW_20260916.md`
   @ `f81896bae3` has "R-OG-3 RETIREMENT", naming what the project no longer promises. Andrew's verbatim
   words stay there as the tracked carrier. PASS.
4. **FWD-1..8 and every other CONTRACTS byte are unchanged.** PASS, by the hash equality above.

-- 3.0.0_SA_CVO
