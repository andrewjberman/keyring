# 2.0.0_SA_COO~H drive log -- 2026-09-30 17Z-18Z (host opal_bloomberg)

Arm: `/canonical-drive AMGT_HARVST 30m` (cron bf9d159b). Lease: FULL. Round 29 L8/L10, then round 30 L6/L7.

## The round-29 analysis and the round-30 cut

- **~17:14Z -- the round-29 analysis** @`d0bc0a79f0` (PRD v0.10: `bot_check`). `prd-signoff` reads ADMITTED.
- **~17:3xZ -- ONE issuance** @`92ac03f4c8`, decomp section 43:
  - `ac-1`: the `bot_check` class;
  - `ac-2`: the sa probe on resolved securities;
  - `ac-3`: the paired daily rebuild.
- **Premise corrected at the cut:** the analysis names 4 kept bodies; 2 exist (wsj, ft). bbg and barrons raised through
  `verification.py` with no body.
- **The cut was delayed:** a peer's `index.lock` refused it once; the retry landed.

## Andrew-direct via the CTO

- **~17:23Z:** a cloud headed route, NopeCHA, and REST on long-lived tokens go to `CRO~Z`. Round-30 cells stand.
- **~17:47Z, ~18:00Z, ~18:38Z -- round-31 input:** the CTO's cloud ruling section 0. Cells 1 and 4 stand; cell 3 is withdrawn
  (`CRO~Z` ran the trial); cell 2 waits on the CRO's trial 2.

## ac-1

- **AMENDMENT 1, before dispatch** (PRD v0.11): a body-less refusal is `unclassified`, never expiry.
- **Reported:** 333 passed. wsj is `bot_check/datadome`, and ft is `bot_check/ft_security_verification`.
- **Row `Z-W84-S1`:** accepted as built.
- **Row `Z-W84-S2`** (a `check_auth` re-check after a bot check could reach a sign-in): ruled in as AMENDMENT 2
  @`b5143abdf8`, now running.

## ac-3

- **COO half** @`f406a6106b`. The expected rows are DERIVED from `ab-2`'s in-window new pairs: 992_HK 08-13 and 09-01, plus
  AAPL, C and MU on 08-13. That widens the analysis's "992_HK only" by measurement.
- **The count:** 539 moves, 0 OTHER.
- **CTO signed** @`1f2edc7733`, and added the positive arm: AC1 and AC2 PASS on the captured part (@`c3f2f1cd1d`).
- **The act** (18:17Z): `part-20260930T181745Z` equals the dry run. Drained @`8d25ddbdc3`; on the trunk AC1 and AC2 PASS.
  Complete @`1dc2ffb4a5`.
- **Result:** the 2 in-window bbg articles are on the page.

## ac-2

- **AMENDMENT 1:** the probe runs OUTSIDE the Worker, because inside it an sa `AuthExpired` or a 402 would trigger a sign-in.
  COO half @`0ee2667f36`.
- **CTO signed** @`e5171bf838`, with two conditions:
  - a refusing sign-in, since `TokenFirstSessions.get` signs in when no token is stored;
  - direct `check` and `news` calls capped at 3 requests, since `seeking_alpha` fetches one article per hit.
- **Dispatched** to `~85` after `ac-3`'s act.
