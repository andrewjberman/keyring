# Session log -- 0.7.0_AE_CloudOps~X -- 2026-09-04 04:30-06:00Z -- NFRA_OPSEC202609 Z-S127 sizing

**archetype:** DIAGNOSE

**Seat:** `0.7.0_AE_CloudOps~X` (site-z)
**Work:** not a task order -- the three measurements `2.0.0_SA_COO~Z` required (msgs 20224,
20248) before routing surprise row `Z-S127` to `1.0.0_SA_CTO~Z` and Andrew
**Commits:** `e8bab64257` (row Z-S140), `bda4dc6fa3` (row Z-S141), + this log
**Continues:** `session_0.7.0_AE_CloudOps~X_0230-0430Z_OPSEC_S9C_S9D_RESIDUAL_GRANT_AND_RETIREMENT.md`

---

## Current state

**The sizing packet is COMPLETE and CLOSED at the issuer's seat** (msg 20254). `Z-S127`,
`Z-S140` and `Z-S141` are sized, routed, and the retrospective window honestly declared
unclosable. **Nothing was remediated** -- no rotation, no secret moved, no endpoint
disabled, no function configuration edited, per the standing instruction in both rulings.

**The size: FORGEABLE AND REACHABLE**, the worst of the issuer's three branches.

## What was measured

**ONE -- does anything still validate?** It validates *and* mints, both read in the
**deployed bytes**: `trade-authorizer.validate_token` HMACs with `JWT_SECRET`,
`trade-auth-handler.generate_token` signs with the same one, and both carry an identical
hardcoded fallback so an absent env var fails **open** onto a committed string. The token
is **not a JWT** -- two parts, no header, no `alg`.

**REACHABLE, turned from configuration into fact.** `w8jnzvs21g` has a live `prod` stage,
`DisableExecuteApiEndpoint` FALSE, and six of seven routes bound to that authorizer. An
unauthenticated probe **woke the 129-day-dormant authorizer** and advanced its log stream
to now.

**TWO -- who can read it? 14 of 231**, by simulation across 224 roles + 7 users, both
controls in isolation. Three are human or interactive IAM users.

**THREE -- has anything ever successfully authenticated?** Yes: 2026-01-07 served 105
requests with zero 4xx and zero 5xx while the authorizer ran 18 times, so **all 18 returned
ALLOW** -- recorded as an *inference from two metrics*, because the log that would say it
directly is expired.

## Blockers

**None, and the lane's queue is empty by the issuer's own statement.** Placement is
`1.0.0_SA_CTO~Z`'s at L4; remediation needs its own face and its own consumer census.

## Next steps

- **[`1.0.0_SA_CTO~Z`]** L4 placement. The issuer added a branch the size did not originally
  carry: the traffic profile -- built and tested 05-11 Jan, one burst 26 Apr, nothing since
  -- is a pipeline **built, tested and never decommissioned**, so **retiring the API may be
  cheaper and safer than rotating its secret.**
- **[whoever takes remediation]** Access logging on the prod stage and a longer retention on
  the authorizer's log group would make the abuse question answerable *going forward*.
  Neither is retroactive.

## Errors and corrections at this seat

- **My first reachability probe was undiscriminating and I nearly read it as an all-clear.**
  I omitted the stage prefix and got **404 on the real route, the junk-token route AND the
  nonexistent control** -- three identical answers. A seat in a hurry reads that as
  "unreachable, stand down", which would have closed the finding at *inert*. The control is
  the only reason I knew. Re-probed with `/prod`: 401 / 403 / 404.
- **My first simulation sweep asked the wrong action set.** Only
  `lambda:GetFunctionConfiguration` -- and **five of eleven roles hold the capability solely
  via `lambda:GetFunction`**, which also returns the environment. They would have scored
  denied.
- **My script reported `0 IAM users` and it was a crash, not a count.**
  `bash .tools/aws iam list-users` from a python subprocess dies with a Windows
  **ACCESS_VIOLATION (rc 3221225477) returning EMPTY stdout AND EMPTY stderr** -- byte-identical
  to an account with no users. Caught **only** by a guard comparing the enumeration against
  the census `user_count`, which exited non-zero rather than sweeping a population it could
  not vouch for. Had it stood, all three human principals -- including both of Andrew's --
  would have fallen out of a security finding.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-iam refresh-census` | the 03:45:22Z artifact, re-used not re-run | Supplied the **224-role population** the simulation swept, and its `user_count = 7` is the cross-check that caught the ACCESS_VIOLATION masquerading as an empty user list. The census was the control on my own instrument, not the source of the answer. |
| `comp-routes auth-map` | run under S9C, cited here | Its own COVERAGE banner states `auth_api_gw` is derived from **origin TYPE, not from an authorizer's existence** -- a named topology-inferred residual. That disclosure is exactly why "which authorizer is bound to these routes" went to the live plane under a `# rail-checked:` marker instead of being answered from the tool. |
| `comp-read` | not required this segment | The questions were all live-plane -- API stage configuration, log retention, CloudWatch metrics, IAM simulation. No repo file was the subject, so no single-file read arose. Stated rather than left blank. |
| rail refusals | 2 this segment | Both correct: raw `aws` IAM inspection and raw API-GW inspection. Each was re-run with a `# rail-checked:` marker naming the grain the comp-tool structurally cannot answer -- verbatim per-principal simulate decisions, and which authorizer id is bound to which route. |

## Evidence discipline worth carrying

**"We found no evidence of misuse" would have been literally true and would have read as an
all-clear** -- when the instrument that would have shown misuse never existed. The answer
has two halves and reports usually pick one: a **finding**, not a demonstrated incident, and
**not a demonstrated non-incident either**.

**Three times in one night a silent instrument would have read as an all-clear** -- CloudTrail
data events, the 404 triad, and two of three abuse instruments. Asking *what the instrument
would show if the thing were true* caught all three, and it is the cheapest check available.
An instrument whose output is identical under a hypothesis and its negation is not an oracle.

**Subtracting my own probe explicitly** -- 3 authorizer and 2 mint-handler invocations -- is
what stops the investigation contaminating its own evidence.
