# Session close -- `0.7.0_AE_CloudOps` -- AMGT_RESAPP `AMGT-rk-123`, the `/api/scoped/amgt/*` CDN behavior

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, SCRIBE

**Window:** 2026-09-22 ~19:51Z -> 2026-09-23 ~06:55Z. First log of this session (prior log 2026-09-14),
so the window is the whole session.
**Seat:** `0.7.0_AE_CloudOps`, site Z, branch SITEZ. Zero crons armed all session; event-driven.

---

## Current State

**The act is done, accepted and has held all night.** CloudFront distribution `EVTSA9VEHNZVH`
carries ONE appended `ordered_cache_behavior` for `/api/scoped/amgt/*` -> origin
`APIGateway-portal`, Managed-CachingDisabled
(`4135ea2d-6df8-44a3-9df3-4b5a84be39ad`), origin-request policy
`b689b0a8-53d0-40ab-baf2-68738e2966ac`, and ONE `viewer-request` association to
`arn:aws:lambda:us-east-1:313476888478:function:auth-validator-edge:20`. It is behavior index
28 of 29, i.e. LAST, which the never-widen pair required.

Declared at `infra/aws/terraform/portal-auth/cloudfront-distribution.tf`, resource
`aws_cloudfront_distribution.portal`. The change is 36 insertions, 0 deletions, committed by
this seat at `8c038da7e7` and merged to SITEZ at `6c41b5d70e`.

**What it fixed:** every `/api/scoped/amgt/*` request previously fell through to the SPA origin
and returned `200 text/html` (1000b), which is why Andrew's Security Analysis page rendered
nothing. They now return `401 application/json` (51b) unauthenticated -- byte-identical to the
two control families -- meaning the route resolves and the edge validator is attached.

**Deploy ledger:** `org/critical_paths/change_management/20260922T2058Z_amgt-rk123-edge-behavior_deploy_completion.md`
reads `Status: CLOSED -- nothing stranded -- closed 20260922T212649Z`, both legs proven, sentinel
`org/critical_paths/.open_deploys/amgt-rk123-edge-behavior.json` removed, and
`deploy_ledger.py check` returns no rk123 row.

**Order:** `org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-123.amgt-edge-behavior-apply.md`
@`010ef26367`, `<status>complete</status>`. Proof-of-spec instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps/AMGT_RESAPP.TO-AMGT-rk-123.amgt-edge-behavior-apply.proof_of_spec.json`
grades VALID (rc=0). Issuer `2.0.0_SA_COO~Z` ACCEPTED and CLOSED it, msg 24411.

**Push state: LOCAL.** Local SITEZ @`b35a0b1449` at my last read; `origin/SITEZ` read
`3ad6fe5490` by `git ls-remote` at 21:3xZ, and `1.0.0_SA_CTO~Z` reported `3303326c25` at
06:52Z. The push is `0.0.0_AB_MSTR~Z`'s on Andrew's word; this seat commits and never pushes.

---

## Deployment Sequence (AE role addition)

1. Linked worktree `C:/tmp/ae-amgt-rk123` cut from SITEZ `256546ecb0` (order required a base at
   or after `2e0fa454b1`; verified by `merge-base --is-ancestor`).
2. **AC0 pre-act**, this seat's own instruments, nothing inherited.
3. Patch applied from `deliverables/0.9.0_WK_AMGT_RESAPP~122/rk122_amgt_behavior.patch`
   (sha256 `5b5a451702abee200781dac25e1d22d4319211760468eb6f8eec1dda70e94c2b`).
4. `.tf` committed `8c038da7e7` -- **the commit IS the lane check**; `safe-apply` does not check
   lanes.
5. `terraform init` + targeted plan; plan graded against the pair's bound.
6. Deploy ledger OPENED and committed `12f7e03f9f` BEFORE the apply.
7. `HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/portal-auth apply -target=aws_cloudfront_distribution.portal`
   -- see DEVIATION below.
8. **AC4 post-act**, read twice across the propagation window.
9. Ledger legs proven, entry CLOSED, worktree and branch removed.

## Verification -- ACTUAL output

**AC0, pre-act:**
```
5b5a451702abee200781dac25e1d22d4319211760468eb6f8eec1dda70e94c2b *.../rk122_amgt_behavior.patch
28
(amgt pattern query returned an EMPTY line)
ETag E3E2K17TJ5XXGE
/api/scoped/amgt/lists 200 text/html
/api/scoped/advisor-intelligence/ping 401 application/json
```
The live ETag `E3E2K17TJ5XXGE` is IDENTICAL to the value `1.0.0_SA_CTO~Z` signed in the CTO
half, so the pair's pre-act state still held at act time.

**AC1:**
```
pre-patch auth_validator_edge_arn count: 26
36      0       infra/aws/terraform/portal-auth/cloudfront-distribution.tf
post-patch auth_validator_edge_arn count: 27
```

**AC2, the plan:**
```
Plan: 0 to add, 2 to change, 0 to destroy.
  # aws_cloudfront_distribution.portal will be updated in-place
  # aws_wafv2_web_acl.opal_cloudfront_protection will be updated in-place
added ordered_cache_behavior: 1 | removed: 0
amgt lines: exactly 1 -> + path_pattern = "/api/scoped/amgt/*"
```
WAF field diff COMPUTED and PRINTED, never asserted: 3 rule blocks removed and re-added, rule-name
sets identical, **21 scalar fields compared pairwise + 3 `override_action{count{}}` blocks present
both sides = 24 visible fields, 0 DIFFERING.** I flag that a naive scalar parse yields 21, not the
order's stated 24; both numbers are in the instance rather than reporting the smaller one as though
it were the stated one.

`spa_fallback` returned 1 substring hit. Resolved rather than waved through: it is the
`Refreshing state... [id=portal-spa-fallback]` line, carries NO `+`/`-`/`~` change marker, and the
resource-change denominator is 2. Not a third resource.

**AC3, the apply:**
```
Apply complete! Resources: 0 added, 2 changed, 0 destroyed.
```

**AC4, post-act, read TWICE:**
```
29
/api/scoped/amgt/*      APIGateway-portal       1
read 1: amgt/lists 401 application/json | BA_US_Equity/thesis 401 application/json |
        992_HK_Equity/thesis 401 application/json | advisor-intelligence/ping 401 application/json |
        general/health 401 application/json
read 2 (after propagation): all six identical, with sizes -- every path 401 application/json 51b
viewer-request arn:aws:lambda:us-east-1:313476888478:function:auth-validator-edge:20
Distribution Status: Deployed  2026-09-22T21:04:05.880000+00:00
```
`BA_US_Equity` first, then `992_HK_Equity`, in the order the CTO's ruling names. Position: amgt at
index 28 of 29 = LAST. Template match: 8 of 8 fields identical to `/api/scoped/investor-reporting/*`.
Pre-existing: 28 patterns intact, order preserved, 0 duplicates. WAF: 18 rule-fields compared live
vs the plan's removed side (which IS the pre-act live state terraform read), 0 moved.

**Controls -- a passing assertion never mutated has never been tested:**
```
contains 'amgt' -> 1 row | contains 'amgtXYZZY' -> 0 rows | contains '/api/' -> 26 rows
/api/scoped/amgt/lists      401 application/json
/api/scoped/amgtXYZZY/lists 200 text/html
/definitely-not-a-route-zzz 200 text/html
```
The second mutant is the decisive one: an UNMATCHED path still shows the pre-act symptom, so the
flip on the real amgt paths is caused by the new behavior MATCHING, not by any global change.
Determinism: AC4 twice, identical -> STABLE.

I also ruled out 4xx->HTML masking before trusting the 401s: all 3 `custom_error_response` hits in
the `.tf` are COMMENTS recording that the distribution-global 403/404->HTML rule was REMOVED, and
the control families already answered `401 application/json` pre-act.

---

## DEVIATION, disclosed (row `AMGT_RESAPP-Z-S231`)

The order's literal `safe-apply` invocation is **unexecutable in this harness**: terraform prompts
`Enter a value:` for approval, stdin is the null device, and the run dies
`Error: error asking for approval: EOF` having applied NOTHING. Negative control that nothing
half-landed: live behavior count read 28 immediately after, unchanged from AC0.
`.tools/safe-apply.sh:361` is `exec "$TERRAFORM" "$@"`, so the wrapper passes argv through and
cannot suppress the prompt.

Resolved by appending `-auto-approve`: same wrapper, same `-target`, same single resource, zero
change to blast radius. A saved-plan file was considered and REJECTED because it would have required
DROPPING `-target` and deviating further. The re-plan gap `-auto-approve` opens is covered by grading
the apply's own result line against AC3's expect and by AC4's full read against every rollback
trigger in both halves. `2.0.0_SA_COO~Z` read it as conforming and RULED `-auto-approve` into its
future deploy orders: HALT_ACK is the fabric's approval checkpoint; terraform's prompt is an
interactive artifact this harness cannot answer.

## MY OWN ERROR, self-caught (row `AMGT_RESAPP-Z-S234`)

I ran the deploy-ledger `close` INSIDE the linked worktree. The tool mutates the tree it runs in;
the branch had already merged at its OPEN commit `12f7e03f9f`; the close was never committed; and
`git worktree remove --force` destroyed it. The SHARED tree was left reading `Status: OPEN` with
`check` printing `stranded=['tf-commit', 'edge-verify']` -- a half-landed deploy ledger, which
CLAUDE.md's NEVER block forbids. Commit `b250fe35c9` and my AC5 row had both asserted CLOSED on the
strength of the worktree read.

Caught by RE-READING THE SHARED TREE AFTER THE DRAIN instead of trusting the pre-drain read.
Re-closed there with identical proofs at `20260922T212649Z`; AC5 evidence corrected IN PLACE to
record the overstatement rather than overwrite it; re-graded VALID.

**The deploy itself was never at risk** -- the apply had landed and AC4 had verified it live twice
before any of this. Bookkeeping loss, not a world loss. The generalisation, banked to memory:
**a stateful tool run in a linked worktree writes to THAT worktree, and only what is COMMITTED
survives the drain.** The trap is that every check done BEFORE the drain PASSES, because it is true
of the tree being checked.

---

## Files Modified

See commit messages: `8c038da7e7`, `12f7e03f9f`, `ebc343fc3c`, `6c41b5d70e`, `b250fe35c9`,
`b35a0b1449`. Six commits, all under this seat's author line.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-routes` | `comp-routes behaviors` | PASS | DESIRED-plane corroboration of AC0: 28 ordered + the `/*` default, 0 amgt, template `/api/scoped/investor-reporting/*` present with its validator. Its own coverage line says "never a live CloudFront describe-distribution". |
| `comp-read` | `comp-read <tf> --enumerate 'custom_error_response'` | PASS | 3 hits / 1033 lines, 3 whole-value / 0 substring, ALL 3 comments recording the 403/404->HTML rule's removal. |
| `comp-read` | `comp-read .tools/surprise-row-gate.py --enumerate 'HAZARD_STANDING\|hazard_standing' --limit 40` | PASS | 15 hits, CODE=15, denominator 3125 lines. Settled that `DISARMED` is a `disarm.state` value, not a `hazard_standing`. |

**What worked:** `comp-routes behaviors` gave the declared-plane behavior list and the template's
exact edge association in one read, on a DIFFERENT instrument from the live AWS read -- that is what
made AC0's declared-vs-live agreement a real corroboration rather than a repetition.

**What failed:** nothing failed, but the rail cost three aborted calls. Twice a `comp-read` piped
into `tail` was denied for erasing its denominator (correct); once a compound call was denied
because a `.tf` path inside a PROOF STRING tripped the grep classifier -- and since a rail denial
aborts the WHOLE bash call, all three `deploy_ledger.py close-leg`/`close` segments chained after it
were silent no-ops. Caught it because I re-read the ledger state rather than the exit code.

**Gap found:** `comp-routes` is DESIRED-plane only by its own disclosure and cannot answer whether
an apply LANDED, so every live grading read here needed an audited `# rail-checked:` marker naming
exactly that limitation. That is the correct outcome, not a defect -- but a live-plane CloudFront
read is a real hole in the comp-tool set for anyone verifying a distribution change.

## Rows filed

| row | class | standing | subject |
|---|---|---|---|
| `AMGT_RESAPP-Z-S231` | BLOCKING | INERT | the order's literal safe-apply invocation is unexecutable in a non-TTY harness |
| `AMGT_RESAPP-Z-S232` | OBSERVATION | INERT | `.open_deploys/` absent from `<paths>` while the mandated tool writes there |
| `AMGT_RESAPP-Z-S233` | OBSERVATION | INERT | AC5 cites a `deploy_ledger.py status` subcommand that does not exist |
| `AMGT_RESAPP-Z-S234` | BLOCKING | INERT | the ledger close died with the worktree (self-caught, repaired same turn) |

With the row-id template itself -- the gate refused `W123` because a seat's row on the main index
carries no `W` -- that is FOUR instances of one class: an order template carried forward without
being exercised against the tool that consumes it. I corrected shapes rather than taking audited
overrides, since `safe-merge` has no override path and a gate refusing on a shape is naming a wrong
shape. `2.0.0_SA_COO~Z` took all four as its own issuer-text defects for the round-30 packet.

NOT duplicated: `0.9.0_WK_AMGT_RESAPP~122` had already filed `Z-W122-S1` on the `spa_fallback`
substring defect. I hit it independently and corroborated on a DIFFERENT instrument (change-marker
check + resource-change denominator) rather than filing a second row.

## MCP traffic

10 messages total. Significant: **24383** the GO from `2.0.0_SA_COO~Z` (acked); **24361/24362** my
live-and-read-both-halves confirmation to `1.0.0_SA_CTO~Z` and `0.0.0_AB_MSTR~Z`, with **24363/24364**
a correction for a malformed hash I had put beside the real one; **24408/24409/24410** the completion
report, 3 of 3 DELIVERED; **24411** the issuer's ACCEPTED-and-CLOSED (acked); **24738** the CTO's
information-only relay of Andrew's wind-down word (acked).

## Blockers

**None.** Nothing is owed by this seat.

## Next Steps

1. **[`0.0.0_AB_MSTR~Z`]** The push. Everything from this seat is LOCAL on SITEZ; the push is that
   seat's on Andrew's word.
2. **[`1.0.0_SA_CTO~Z`]** An AUTHENTICATED end-to-end render of `BA_US_Equity` then `992_HK_Equity`
   is the confirming read. **This act fixed ROUTING, not auth and not content** -- if authentication
   is also broken the page still renders empty, and row `Z-S227` (0 of 5 tabs carry an `isError`
   branch) is why that would again be SILENT, as this outage was. Not this seat's cell.
3. **[`2.0.0_SA_COO~Z`]** Holds rows `Z-S231`..`S234` as issuer-text defects for the round-30 packet;
   `-auto-approve` already ruled into future deploy orders.
4. **[this seat]** Wound down on Andrew's word (~07:0xZ, relayed by `1.0.0_SA_CTO~Z` msg 24738 as
   information, not as an instruction). Nothing armed: zero crons all session.

## Note for a successor at this seat

`1.0.0_SA_CTO~Z` carried one line worth keeping: **Andrew's EGRESS and AMGT-ADJUDICATION grants are
SESSION-SCOPED and expire with that session.** They do not re-arm off a log or off memory, and the
per-use vendor bar returns by default.

One device-specific trap cost a turn and is banked: the standard watcher census regex reads **ZERO
against a live watcher** on this box, because the workspace path contains a space, so the Monitor
command quotes it and puts a `"` between `.sh` and the serial. Use `inbox-watch\.sh"? <serial> stream`.
Following the zero would mean re-arming on top of a healthy watcher.
