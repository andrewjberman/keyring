# NFRA_OPSWKF PRD v0.9 -- ratified-text review (ENDPOINT: FWD-9's admitted arm is read by a direct invoke)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/NFRA/NFRA_OPSWKF/prd/NFRA_OPSWKF_PRD.md` @d7de5b9217.
**Asked by:** `1.0.0_SA_CTO~DELL2`, msg 5944. **Prior:** v0.8 SIGNED; this seat's grade of workstream S @25857907be found its third
read never made.
**Verdict: SIGNED. One suggestion that costs one more invoke.**

## What changed

v0.8 asked for a read by an Opal-internal caller after the release. The CTO's half of the pair then declined to mint that caller,
for a stated reason: for its token's minutes it would be Opal-internal on every surface that reads the firm claim. That left a
DONE WHEN nobody could meet. v0.9 replaces the read with one a seat can take on demand:

- one direct invoke of the deployed function with a constructed event: authorizer context carrying the Opal firm id and an email,
  the same unstorable body; answered 400;
- the same invoke with a context that fails both comparisons; answered the new 403.

No token is minted and no identity exists for either.

## Why this is the right read

- It exercises the admitted branch of the DEPLOYED bytes, which is what was missing. This seat read those bytes live today:
  3 of 3 members equal to the tree at the release pin.
- The second invoke is what makes the first mean something. Without it a 400 shows only that the function answers 400.
- The unstorable body returns before any table or mail on both paths, by the handler's own order, printed by this seat at the v0.7
  review. Nothing is stored by either invoke provided the body is that body; the pair's amendment names both events.
- It buys the proof without the cost the CTO refused, and the refusal of that cost was right.

## What it does not show, and the text says so

That the authorizer hands this function the context a real staff session carries. The text names that gap, names the evidence
beside it (FWD-8's live read of an Opal-firm caller through the same authorizer), and says the first real staff submission closes
it by-session. That is an honest statement of a residual, not a hidden one.

The mail side is now stated for what it is: no read of the mail service, a claim resting on the handler's order.

## One suggestion

The check has two comparisons and the admitted invoke exercises one, the firm id. A third invoke, with tier `internal` and a firm
id that is not Opal's, exercises the other on the deployed bytes at the cost of one more call and no identity. FWD-8 left that
branch unexercised live for want of a token; here no token is needed. Not a condition.
