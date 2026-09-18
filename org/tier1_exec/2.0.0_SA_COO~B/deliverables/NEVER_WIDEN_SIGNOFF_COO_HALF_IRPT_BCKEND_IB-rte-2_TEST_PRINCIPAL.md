# NEVER-WIDEN SIGN-OFF, COO HALF -- IRPT_BCKEND IB-rte-2: the bounded test principal (Andrew-direct "Approved", ~17:3xZ, record @af794c77e3)

**Signer:** `2.0.0_SA_COO~B` (the COO half; CLAUDE.md NEVER-1 -- CTO+COO). **Signed:** 2026-09-18 ~22:0xZ. **The act signed:** the
creation, exercise and deletion IB-rte-2 performs, exactly as
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/NEVER_WIDEN_SIGNOFF_PACKET_IB-rte-1.md` describes it, read at HEAD
`f08295cc8f` (blob `3d9f57335b9893753973132ba5c4958b2622e24f`). A packet whose bytes differ from that blob is NOT what this half signs;
IB-rte-2 re-reads the blob hash before any write. The CTO half is asked the same tick.

This half signs the ACT'S BLAST RADIUS and rollback per key, both branches, never the producer's intention. Writers of the named property
are counted (the packet's identity-plane census, re-read here).

## The keys, as the packet names them

| key | what the act touches | blast radius this half signs | rollback |
|---|---|---|---|
| K1 | ONE DynamoDB item in `opal-users-v2` (`PK = USER#usr_irptrte_<epoch>`, `firmId = 49financial`, `advisorKey`/`advisorId = abby_horton`, a `.test`-TLD e-mail, no phone, no MFA) | a bearer of a token minted against this row receives EXACTLY `abby_horton`'s existing, already-live entitlement in 49financial -- no new grant is minted (K3/K4 NOT NEEDED, named so a half cannot assume them); the row is readable/writable only by the 6 of 263 identity-plane writers the census names (3 human/terminal, `opalinvest-auth-lambda-role` the estate's own mint path, and two lambda roles with account-wide access noted as a finding) | `DeleteItem` on the same PK, VERIFIED by a consistent-read `GetItem` returning no `Item`; a token already issued before deletion lives only to its own TTL (named) |
| K2 | the session access token minted by `generateAccessToken()` on a normal login through the real portal auth route | while it exists it is indistinguishable from a real `abby_horton` session to every downstream control -- which is exactly why it is NEVER persisted, logged, or committed (bound 6); the private key is read by NAME only | ephemeral; expires on its own TTL; nothing to roll back |

**Writers of the named property, counted:** `dynamodb:PutItem`/`UpdateItem` on `opal-users-v2` -- **6 of 263** principals, `0` UNKNOWN,
resource plane none. BLIND SPOT the packet names and this half carries: an identity provider's own admin surface is not IAM; a signup flow
inside the auth Lambda is a writer the IAM census cannot see. One property, six writers, six rules read by the packet; this half signs
none of those six moves.

## Both branches covered

- The producer creates and exercises: K1 exists inside IB-rte-2's ledger interval only; every arm is a real signed request bound by
  artifact hash; the four outcomes read whatever they read (PASS or a truthful FAIL -- **W1-S22 says the served path refuses every advisor
  today, so rte-2 is gated on IB-rte-6 and this half does not predict the arms**); the deletion is the cell's LAST arm, verified by a
  failing read, whatever the arms read.
- The producer STOPS (packet hash differs; a half names fewer keys; the row cannot be created as shaped): nothing is written, or the
  row written so far is deleted the same turn.
- The row leaks a capability (a route reachable that the packet's fence says is not): the negative controls run BEFORE the outcome arms;
  a failed negative control is a STOP and a same-turn deletion, and a BLOCKING row.

## What this half does NOT sign

- Any standing account, any second identity for FWD-11 (the packet costs it; a second identity is a second packet), any ownership-map
  or directory write, any change to the auth Lambda, the authorizer or the JWT key.
- The two account-wide DynamoDB writers the census surfaced (`opal-news-lambda-role`, `trade-submission-lambda-role`) -- an IAM
  finding for the IAM owner, not absorbed here.

**Push state at signing:** `f08295cc8f` LOCAL; origin/CLOUD `ec5a7afd2b` (the CTO's 18:49Z ls-remote; not re-read here).
