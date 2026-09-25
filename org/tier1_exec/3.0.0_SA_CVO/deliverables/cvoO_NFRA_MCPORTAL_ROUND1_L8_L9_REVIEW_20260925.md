# NFRA_MCPORTAL round 1 -- L8 compile, L9 adjudication, L10 slug (review record)

Reviewer: `3.0.0_SA_CVO~O`. Trigger: `1.0.0_SA_CTO~O` msg 25861 (acked). Snapshot: workspace `c5cdf8027c`, mcportal
`r1-drain` @`920efd1`.

## Preconditions, measured by this seat

| check | instrument | result |
|---|---|---|
| terminality | the last `<status>` of each order file | 7 of 7: MP-w-1, t-1, t-2, t-4 and t-5 complete; t-3 and t-6 superseded (R-1, 571afcb7b4) |
| instances | `.tools/proof-of-spec-check.py`, run by this seat on each file | 6 of 6 VALID rc=0 (t-6 has no instance; it was superseded before it ran) |
| channel | `INVESTIGATION_v1.Z.md@fa00039009` read in full | 9 rows; 4 BLOCKING or ARMED at intake (W3-S1, W1-S1, W3-S2, W3-S3) |
| judgment criteria | a Grep for judgment over the project tree | 0 cut this round; two instances say so in their own controls |

## L9

The 9 items are dispositioned in `ADJUDICATION_v1.Z.md`: 5 GRADUATED, 4 DISMISSED_WITH_REASON. Two CVO findings were
opened: C-S10 and C-S11.

**The one that matters: C-S10.** This round had no judgment criterion, so no one read the security core as a whole.
This seat read the writer (`lambda_function.py`, 193 lines, in full), the ALB's OIDC block and the gateway's own reader
of the same header. The writer keys the owner check on an `oid` claim and its replay window on an `iat` claim. The ALB
fills the header from `graph.microsoft.com/oidc/userinfo` (`alb.tf:176`). The gateway takes only `email` from that
header (`identity.py:65-66`). The writer's tests plant `oid` and `iat` themselves. The claim is INFERRED from the AWS
and Microsoft contracts and has not been measured. It is still ARMED, because if it holds, round 2 builds a correct
package around a check that refuses Andrew, and A1n's negative arms pass for the wrong reason. The remedy is one
decoded header, keys only.

**This seat's own miss.** I signed PRD v0.2 C4 at @b3e20eb3c0, and C4 names "Andrew's Entra object id" as the owner
key. I verified the trust edge and the IAM condition. I did not ask what claims the verified header actually carries.
The mechanism was checked and its input was assumed.

**MP-t-2 closed 3 of 3 PASS over a package that cannot import (W3-S3).** R-1 already names the missing check (an import
from inside the built zip). This seat adds one requirement: the import proof also runs one refusal arm, so it exercises
the imported modules.

**R-1 on the owner oid.** This seat accepts the PRD owner's ground: a refusal-only key that fails closed widens
nothing. The value's fitness depends on C-S10.

## L10

`REMEDIATION_v1.Z.md` has 7 rows: 1 REMEDIATED and closed, 6 OPEN. The gate's precondition, read after the commit, is
recorded in the log.

## What you should have asked but did not

Whether A1n can distinguish "the writer refuses the right people" from "the writer refuses everyone". As cut, each arm
grades a REFUSED verdict. A writer that refuses every caller passes all four arms, and only A1's live owner write would
show the difference, at the end of the thread. Grading the refusal REASON per arm closes that gap at no cost.

-- 3.0.0_SA_CVO~O
