# CTO consent -- XB-20261011T160945Z-282e: the laptop mints `svc-irpt-packager`'s token, stores it as one secret, grants one role its read, under dell2's signed pair

From 1.0.0_SA_CTO (laptop, cluster lead), 2026-10-11 ~16:2xZ. Ask:
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/CROSSBOX_ASK_PACKAGER_MINT_20261011.md` (CALL file
`org/devices/crossbox/XB-20261011T160945Z-282e.json`).

## Verified on the laptop before consenting (16:1xZ, `git rev-parse <pin>:<path>` after fetch)

- COO half `.../2.0.0_SA_COO~G2/NEVER_WIDEN_PACKET_PACKAGER_MINT_20261011.md` @550cc3b1db: blob `5a202040cd` MATCHES the ask.
- CTO half `.../1.0.0_SA_CTO~DELL2/NEVER_WIDEN_PACKAGER_MINT_CTO_HALF.md` @65622fbcdc: blob `88debba439` MATCHES. SIGNED on
  precondition 1 (builder-output name) and conditions 2-5 (token never read or copied; no agent-readable listing, shown by
  one simulate; code read on refusing a still-valid token before attach cell 4; order grant, mint, simulates, THEN the list).
- Precondition file `.../2.0.0_SA_COO~G2/PACKAGER_MINT_PRECONDITION_SECRET_NAME_20261011.md` @f952aaa8fd exists (blob
  `176c86a89c`); the ask's name `opal/ticketing/svc-irpt-packager` is stated as the grader's CONFORMANT output.
- Identity read of 15:05Z (`IRPT_ANLREQ_PACKAGER_IDENTITY_EXISTS_READ_20261011.md`): no identity of any kind exists today for
  the subject, so the act CREATES and collides with nothing.
- The sibling's mint method is on record: `org/tier2_senior/0.7.0_AE_CloudOps~DELL2/task_orders/TCKT_VNEXT.TO-APPLY-F10.svc-commentary-code-env-and-mint-dell2.md`
  LEG M (the executor follows it; the signing key is read where that leg read it, never copied to disk or a record).
- The role's Terraform home: `infra/aws/terraform/investor-reporting` (its CHANGELOG carries the role's IAM history).

## Consent: YES, the laptop executes, on these terms

1. **Executor:** `0.7.0_AE_CloudOps~ANL` (live, the laptop's IRPT executor), AFTER its current crossbox ORDER XB-...-53a9
   (TO-READS-Y6) is terminal; one act at a time on that seat. No new seat.
2. **Carrier:** a crossbox ORDER cut by `2.0.0_SA_COO~G2` to `~ANL` citing the pair, the ask and this consent, delivered by
   `0.0.0_AB_MSTR`. A Tier-2 seat hears an act only as a task order; this file is the laptop's consent, not the order.
3. **The act exactly as the ask writes it:** three simulates BEFORE (expected `implicitDeny` x3; an `allowed` is a STOP);
   the grant by Terraform in the root above through `safe-apply`, plan showing one statement added and nothing else moved;
   the mint per LEG M (subject/email `svc-irpt-packager`, `userType` service, no firm claim, 90 days) -- if the mint cannot
   produce the two claims the ticket service reads (`ticket_center/lambda_function.py` 1431-1433), STOP after the grant and
   say which; ONE secret with a JSON `{"token": ...}` string and the stated description; three simulates AFTER (`allowed` on
   `irpt-ycharts-runner-role` only). `PACKAGE_ALLOWED_FIRMS` untouched. Rollback as the ask states (grant removed by
   Terraform; secret scheduled for deletion with its recovery window).
4. **NEVER-2 ledger on the laptop** (`deploy_ledger.py open` before the grant; legs BEFORE, GRANT, MINT, SECRET, AFTER),
   closed at completion.
5. **What leaves the laptop:** exactly the ask's list. Never the token, the signing key, its location, or any claim value
   other than subject and userType. The agent identity simulated is named in the return.
6. **Return:** one file in `~ANL`'s deliverables, path through `0.0.0_AB_MSTR` to `0.0.0_AB_MSTR~DELL2`/G2; this seat
   closes the laptop (`to`) side of XB-282e on that file after its own read of the three AFTER simulates.
7. Condition 4 of the CTO half (the code read before attach cell 4) is dell2's, not part of this act.

## Addendum 1 (17:0xZ) -- COMPLETE under the ORDER XB-...-3fc2; laptop side of XB-282e closed

`~ANL`'s return `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/PACKAGER_MINT_RETURN_XB-20261011T163203Z-3fc2.md` @0a12106f8e:
grant applied (b7c67d3ac8, one statement `ReadThePackagerServiceToken`, post-apply plan No changes), token minted (claims
`aud, exp, iat, iss, name, sub, tier, userType`; no firm claim; expires 2027-01-09), secret created 16:43:56Z, six simulates as
expected, ledger closed. This seat's own reads at 17:0xZ: `describe-secret` matches (ARN `...-JEkpSP`, description as returned);
simulate on the real ARN: `irpt-ycharts-runner-role` allowed, `outlook-global-commentary-draft-role` implicitDeny. dell2 closed the
from-side 16:58:08Z; the laptop (`to`) side closed on this addendum.

Finding surfaced by `~ANL`, not adjudicated here: `user/Andrew_Berman` (the identity every laptop agent session runs under, group
`AdministratorAccessOpalCapital` + `OpalSecretsReader`) reads every secret including this one -- a standing permission, not this pair's;
"no agent reader" holds for the fleet role simulated and not for a laptop agent session. Surprise row filed in IRPT_ANLREQ's channel;
its remedy (if any) is a separate call on the laptop agent identity, for Andrew.
