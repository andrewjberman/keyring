# G3 V1 negative arm -- a render token for a Performance export, presented for an Analysis job

Carrier `2.0.0_SA_COO~P`, 2026-10-03 ~06:5xZ.
- **Ruled by:** CTO batch 212 (`CTO_HALF_IRPT_STATUS_G3_RENDER_PORTS_20261003.md` @4f1139744d).
- **Ledger:** `irpt-status-g3-20261003`, leg V1, arm 2.
- **After:** ~Y's D1, landed 06:28:49Z, msg 104567.

## The act

- **Mint:** ONE render token through the production path, exactly as `export/submit_installed.py` mints.
  - The input is `_render_identity/grant.py` `mint_input(record)` over an EXISTING frozen Performance export's grant:
    `firms/49financial/generations/exr_9f785460503746a6b486950e/render_grant.json` in the evidence bucket, one of the 3 grants
    there today, all Performance.
  - The signer is `_render_identity/mint.py` `mint_render_token(...)`, with the key read BY NAME from the secret
    `opal/auth/irpt-render-jwt-private-key` (slot `current`). The key was never printed or kept, and the token was never printed.
- **Token:** `jti = render-5447b60349cd45be967667823912bae5`;
  `sha256(token) = c496c0e116b259ee5ff5917490f9b3592d3a36350c6cf77df552e48c93adb9d3`. Its TTL is 300 s, so it has expired.
- **Presented:** to the portal origin (`https://opalinvest.dev`, the export function's `IRPT_PORTAL_ORIGIN`) as `Authorization:
  Bearer`, for the 49 Financial Analysis job `REQ-cf1d7894dd4b73a148b01a2d` from table `irpt-jobs`, the same firm as the grant.
  The probe script is in this seat's scratchpad and printed only the fields below.

## The answers

| request | HTTP | body | refused by |
|---|---|---|---|
| `GET .../analysis/<analysis job>/sections` | **403** | `{"message": "Forbidden"}` | the API Gateway custom authorizer (its Deny shape) |
| `GET .../status/<analysis job>` | **401** | `{"error": "Render token not admitted for this resource"}` | the edge (`auth-validator-edge`): the status path is not among the render-token paths |

## Reading

- The token for another report is REFUSED on both routes, and nothing is served: the arm's safety property holds.
- Both refusals happen UPSTREAM of `irpt-status`, so its own `OBJECT_NOT_COVERED` (the coverage check the G3 ports enable) is not
  reached by a mismatched token on this path.
  - The edge admits a render token only on its listed API paths.
  - The authorizer denies when the path id does not match the token's pinned `jobId`. That is V2's "each path id equals its claim",
    one layer earlier.
- So batch 212's expected answer, "must refuse OBJECT_NOT_COVERED", is not the answer measured. Measured is a refusal earlier in the
  chain. Whether that satisfies the arm, or whether the arm must also be driven past the authorizer (a direct invoke of
  `irpt-status` carrying the render identity headers the edge would inject), is asked of `1.0.0_SA_CTO`.
