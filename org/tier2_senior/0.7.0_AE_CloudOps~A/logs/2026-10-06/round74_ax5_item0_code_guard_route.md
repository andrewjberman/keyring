# Round 74 AMGT-ax-5: two STOPs, a guard that -target could not see, and a control that could not discriminate -- 0.7.0_AE_CloudOps~A

**archetype:** DEPLOY

## Objective

Execute `AMGT_RESAPP.TO-AMGT-ax-5` on the GO at `ddb9fab716` (msg 29946). Item 0 plus two legs: apply
`round74/ax5_build_fonts.patch` to the build script and commit it ALONE (that commit is the build
commit); the code leg at that commit carrying ax-1/ax-3/ax-4; and ONE added gateway route
`GET /api/scoped/amgt/security/{proxy+}` on `7k3ed8px20` so a `security_key` containing `/` reaches the
function. `memory_size` stays 1769. Five CTO conditions, two of which grew amendments mid-act.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `content_diff.py` (in the build) | `--build-only`, then the real run | **Fired the first STOP.** CHANGED 5 against a signed CHANGED 4. Reproduced identically on the uploading pass. |
| `safe-apply.sh` | route leg | **Fired the second STOP**, rc=4, and failed closed twice over -- terraform's own precondition, plus safe-apply refusing when it could not produce plan JSON for the tag-authz gate. |
| `terraform show -json` | targeted, then untargeted | The pair that produced row Z-S357: 25 rows with the guard ABSENT vs 50 rows with it PRESENT. |
| `terraform validate` | after the guard re-cut | PASS. Run specifically because AMENDMENT 2's first text used a `regexall` form with an invalid HCL escape; validate is what confirmed the corrected escape-free form parses. |
| `r74_served.py` | c53/c55/c56, base arm then after | Base FAIL/FAIL/FAIL -> YES/YES/YES. c55's C2 passing **on the base** is the measurement that localises the 404 to routing. |
| `aws apigatewayv2 get-routes` | before/after, counted client-side | 112 -> 113 rows; security 10 -> 11; CUSTOM 10 -> 11; greedy 0 -> 1. Two wrong readings first; see below. |
| `aws apigatewayv2 get-route / get-authorizer` | by route id | The attributable evidence the 401 arm could not give. |
| `comp-routes api-routes` | tried first, as the rail directs | **Does not answer this question, and says so itself**: DESIRED-plane only, "CANNOT tell a declared behavior from a deployed one", and it does not surface the `scoped_amgt` `for_each` routes at all. The live reads carry a rail-checked marker naming that. |
| `deploy_ledger.py` | open / **hold REFUSED** / close-leg x7 / close | The refusal is part of the result: a HOLD was refused because apply legs were open ("a half-landed deploy cannot be HELD -- stays RED"). Accepted rather than forced. |
| `proof-of-spec-check.py` | pre-commit, then committed bytes | **VALID first pass**, 12 of 12 controls discriminating. |

## The two STOPs

**STOP 1 -- the fifth file.** The CONTENT-DIFF read CHANGED 5 where both halves said 4. The extra file
was `lib/research/harvest/publication_gold.py`, landed by **another project** (`da3c89dc54`, AMGT_HARVST
av-1) among the **26 commits from 10 seats** that had passed the issuer's pin `0c9b9db840`. Ancestry
satisfied the GO's "CLOUD at or after `0c9b9db840`"; content did not (`000aa21ca1` at the pin vs
`0ec3da8c50` at the build commit). Halted before any upload and verified it: function still `satkY3HX`,
artifact still aw-7's version, gateway still 10 routes.

Escalated with both options priced rather than judged. Resolved at exactly the measured value --
ADDENDUM 1 `@d58a7907c4` and the CTO concurrence `@8ded0241cd` both read CHANGED 5 + ADDED 3 at
255,311,077 B. The CTO's own words: the stop "worked as written".

**STOP 2 -- the route-count guard.** `scoped-amgt-api.tf:553` asserts
`length(local.scoped_amgt_routes) == 18` and exists, per its own comment, so an apply stops "rather than
silently mounting seventeen of eighteen". The greedy key makes 19. Escalated with three options priced,
recommending the one that **preserves the guard's meaning** rather than the one that would let my own
apply through. AMENDMENT 2 ruling (b) chose it, and refused bumping to 19 for the reason given: the
equality would stop meaning *list == adapter table*.

**Why I did not fix either myself.** Widening a signed never-widen list and loosening a pre-existing
mechanical gate are both decisions whose cost lands on someone else's signature. "Probably inert" is not
the standard for a WORLD-class act, and CLAUDE.md's "pre-existing mechanical gates stand" cuts against an
executor relaxing one to pass its own work.

## The finding -- row Z-S357, accepted

CTO condition 2 grades the route change on a **targeted** plan. `-target` removes everything else from
the graph, preconditions included: the targeted plan's 25 `resource_changes` carry only `aws_*` types and
**no `terraform_data`**. It read a clean 1-to-add/0/0, and condition 2 read **MET** on it.

The guard still held -- it fired on the apply's refresh, nothing landed. But **the condition meant to
grade this change was blind to the violation**. Those are two separate facts and the second is the one
worth keeping: a gate can hold while the condition that was supposed to grade the change proves nothing.

Ruling point 2 accepted it: condition 2 is now graded on an **untargeted** plan. Re-graded that way: 50
`resource_changes` with the guard **present**, 48 no-op + 1 create + 1 update, 0 other, 0 deletes.

**A second-order effect I caused.** Committing the route edit before its apply (the half-landed-deploy
discipline) left the tree declaring 19 routes, so the old precondition failed at **plan** time for every
apply in this root -- the code leg's own plan exited rc=1. One blocked leg blocked the other. The
discipline is still right; the lesson is that an edit whose own apply is gated by a precondition it trips
can block unrelated work in the same root while it waits.

## A control reported as non-discriminating rather than as a pass

Condition 2 wants an unauthenticated GET on a slash-key path to answer 401 "so the authorizer applies".
It does -- `{"message":"Unauthorized"}` on both. **But so does a path no route claims**, because this API
carries a `$default` route (`khcd4f1`) with the **same** authorizer `naqxlm`. So the 401 is identical
before and after my change, and the request arm proves only that something with that authorizer answered,
which was already true.

I built the discriminating arm, watched it fail to discriminate, and said so rather than banking the 401
as a pass. What *is* attributable, read from the applied plane by route id:

- route `au58sx8`: `CUSTOM`, authorizer `naqxlm`, target `integrations/352l7td`;
- `naqxlm` resolves to `portal-jwt-authorizer`, a REQUEST authorizer on `opal-portal-authorizer` with
  IdentitySource `$request.header.Authorization` -- so CUSTOM is a real JWT gate, not a label;
- `$default` targets `integrations/s7ntfz4`, a **different** integration. So the functional change is
  that slash keys now reach the scoped_amgt integration instead of falling through.

And the cleanest positive arm is a **base** arm: c55's C2 passed *before any route existed* -- the
function already answered 200 for both slash keys on all four routes while the gateway 404'd them. That
is the measurement that the 404 was a routing gap and never a handler defect.

## Instrument corrections, all mine, all caught before they were acted on

1. **The route count.** `--query length(Items)` returned FIVE values (25/25/25/25/12). I first
   misdiagnosed it as shell backtick substitution corrupting the JMESPath. It was not: the shim
   **auto-paginates** and `length()` is applied **per page**, so those are page counts. The sound form
   retrieves every row and counts client-side, with a denominator and a positive control.
2. **Three assertions in my own edit scripts** failed closed before writing -- a count confounded by the
   error-message interpolation, then by my own comment quoting the route key. The file was written only
   once every check passed. Annoying, and exactly what failing closed is for.
3. **The cold-miss probe's labels.** Its first call, labelled "warm (hold seated)", was itself a MISS at
   7,233 ms because the hold had lapsed during the AC runs. The data is sound and in fact stronger than
   intended -- two consecutive misses at 7.0-7.2 s bracketing a 104.8 ms hit -- but the label was wrong,
   and the numbers are reported by what they are rather than by what I called them.
4. **`-detailed-exitcode` 2 after a clean apply.** Not a half-landed deploy: the resource plane was 50
   changes with 0 non-no-op, and the diff was the **output** `scoped_amgt_route_keys`, 18 -> 19 with
   exactly my one key added -- a third corroboration of the addition. Settled with an outputs-only apply
   so the next seat does not read a false pending change.

## Results

**AC1** c53/c55/c56 all YES. **AC2** eight regression cells all YES, c38 worst read 341 ms. Against the
base arm: c53 9,738-10,206 ms -> **525-550 ms** warm (about 19x); c55 C1 FAIL -> PASS; c56 lato-share
**0.00 -> 1.00** on all three prints, which is item 0's entire purpose.

**Two loops closed from my own earlier rounds.** Row `Z-S356` (round 73) recorded `/freshness` at
10.3-11.8 s warm and the issuer **held Andrew's DEV push** on it; c53 now reads 525-550 ms, so that
precondition is met. And `mentions decode`, which my aw-7 report named as the next cold target rather
than names, went **3,720 -> 278 ms** -- about 13x, and most of why cold chatter fell to 3,668-4,729 ms,
the first band in this sequence that does not overlap the previous round's.

Per condition 5 the cold read is still above 2 s, so provisioned concurrency **stays** on Andrew's list
-- now within a factor of two of coming off, where three rounds ago it was within four.

## Decisions Made

| Decision | Why |
|---|---|
| Halt on the fifth file instead of judging it inert | A WORLD-class act with a signed file list. Round 73's half had even called that file "never called by this function", and ADDENDUM 1 corrected *that* claim -- so the comfortable reading was already known to be wrong once. |
| Recommend the guard fix that preserves meaning, not the one that passes | Bumping 18 to 19 would keep the check green while the equality stopped meaning what its own comment says. The issuer refused (a) for exactly that reason. |
| Report the 401 arm as non-attributable | A control that returns the same answer either way is not evidence. Banking it as a pass would have put a false control into a signed record. |
| Follow the signed COO half's leg order over the order's section 1 | They disagree (order: route then code; half: item 0, code, route). The half is the signed artifact and the GO cites it. I noted the discrepancy rather than silently picking. |
| Run the route leg first once the issuer said it was unaffected | It kept each plan to exactly its own change -- a code plan taken with the route edit in the tree would have shown 1 update plus 1 add rather than the clean single update its gate is written against. |
| Accept the ledger tool's HOLD refusal | "Apply legs open" is a conservative read that is right even though nothing was half-landed here. Forcing it would have traded an honest RED for a tidy-looking HELD. |
| Settle the pending output with an extra apply | 0 resource changes, so safe by construction, and it stops the next seat reading exit-2 as a pending change. |
| Verify the CTO's "condition 1 now reads..." at the bytes | Condition 1's own line still says CHANGED 4; the amendment is an appended CONCURRENCE. The message was right about the document and wrong about the line. |

## Files Modified

| Path | Commit |
|---|---|
| `build-and-upload-scoped-amgt.sh` (item 0, alone) | `6e1280df87` -- **the build commit** |
| `scoped-amgt-api.tf` (route entry) | `8a41101743` |
| `scoped-amgt-api.tf` (guard re-cut) | `2bdf1d1e31` |
| `.open_deploys/amgt-resapp-r74-ax5.json` | opened `32177e5978`, removed at close `2e8478a461` |
| `change_management/20261006T0714Z_..._deploy_completion.md` | `32177e5978` -> CLOSED 7/7 `2e8478a461` |
| `deliverables/.../ax-5...proof_of_spec.json` | `2e8478a461`, VALID on committed bytes |
| `deliverables/.../LEADPANEL_AFTER_ax5.txt` | `2e8478a461` -- phase table, 684 lines parsed |
| `surprise-channel/investigations/INVESTIGATION_v1.md` | `2e8478a461`, row `Z-S357` |

No IAM change, no memory change, no store write, no S3 delete, no vendor call, no shared-branch push, no
portal promote.

## Blockers

**None.** Nothing is owed by this seat on ax-5.

## Current State

`opal-amgt-scoped-api` runs `0MZWPl7nGZzFI53w+vsKdS7hQpcxu4Mrd5wEMWWZQpA=` at memory 1769, carrying
ax-1/ax-3/ax-4 with the Lato faces packaged. Gateway `7k3ed8px20` carries 11 security GET routes, all
CUSTOM on `naqxlm`, one of them greedy. The route-count guard now counts non-greedy keys and caps greedy
keys at one. Resource plane 0-diff, outputs settled, `No changes` on the canonical signal.

**Push state: LOCAL @e51152bf48**; `origin/CLOUD` reads `e82f508eef`. Pushing is `0.0.0_AB_MSTR`'s on
Andrew's word.

**Four task orders closed this session:** au-7 (r71), av-8 (r72), aw-7 (r73), ax-5 (r74). Four NEVER-2
entries opened and closed, four proof instances VALID.

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** Row `Z-S356`'s precondition is met (c53 at 525-550 ms). Re-ask Andrew's DEV
   push if that was the only thing holding it.
2. **[`1.0.0_SA_CTO~Z`]** Condition 2's 401 negative control cannot discriminate on this API while
   `$default` carries the same authorizer. If it is wanted as proof rather than a smoke test it needs a
   different shape; the route's applied config and the integration difference are what attribute.
3. **[`2.0.0_SA_COO~Z`]** Next cold-path target is `chatter/names` at 1,220 ms, with `generation read`
   at 923 ms behind it. `mentions decode` is no longer where the time is.
4. **[`2.0.0_SA_COO~Z`]** The `/freshness` hold is 60 s and a miss costs 7.0-7.2 s against a hit's
   0.1-0.55 s, so one request a minute pays the miss. Reported only; hold length or precomputation is a
   design question.
5. **[`0.7.0_AE_CloudOps`]** `c55` is a PIN from this act on: every later redeploy of this function runs
   it. Recorded so a successor inherits it from the record, not from a message.
6. **[`2.0.0_SA_COO~X`]** `amgt-corpus-r36-al5` has now been measured dead in rounds 71, 72, 73 **and**
   74, each time costing a 50-to-61-worktree union read to rediscover. Closing it SUPERSEDED is its
   author's act.
