# AMGT_RESAPP round 62 -- AMGT-al-1, the memory raise (session 352b911c, fourth act; URGENT, demo risk)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

## Window

10:45Z (al-1 GO) -> 11:05Z. 2 commits by this lane, 1 inbound message acted on and acked (28409),
2 applies, 1 surprise row. Due 12:15Z before the 13:00Z demo; landed 10:55Z.

## What I did

Raised `opal-amgt-scoped-api` memory from 1769 MB to **10240 MB** in two steps under one NEVER-2
entry, because BA `/timeline/day/2026-09-08` was timing out COLD against the 29 s API Gateway
integration ceiling (CVO row Z-C-S29: 5 cold timeouts at 10Z).

`memory_size = 3538` first, per the order. **AC1's C1 missed** -- 21726.76 / 20439.58 / 22913.08 ms,
0 of 3 under the 20,000 ms target. The order's own ladder says escalate to 10240 under the same
entry and stop there, so I did: 16885.18 / 16551.67 / 19105.13 ms, **3 of 3 PASS**.

`CodeSha256` is unchanged at both steps (`E+FAZF0f...VcBY=`, ak-2's) -- the direct evidence that a
config act moved no code. `Timeout` deliberately untouched at 29: a Lambda timeout above the
gateway's integration timeout cannot help, since the gateway has already returned 504. The fix had
to be throughput, not patience.

## Deployment Sequence (AE role section)

| # | act | result |
|---|---|---|
| 1 | read live base + tf value, compare | live 1769/29/`E+FAZF0f`; tf `memory_size = 1769` at :326 -- file and world agree |
| 2 | **verify the no-pair exemption at its source** | ruling 5 @`f1d5dac151`: "config only; no served value moves, so no never-widen pair" |
| 3 | NEVER-2 entry opened, 2 legs, COMMITTED before the first apply | `5566f75d33` |
| 4 | `timeline_day.py --what pre` | `al1-pre.json`, exit=0 |
| 5 | edit `memory_size` 1769 -> 3538; plan; grade | 1 block, 1 changed attribute line, forbidden classes 0 |
| 6 | `safe-apply` of the saved plan | `0 added, 1 changed, 0 destroyed`; live 3538, sha unchanged |
| 7 | AC1 | **C1 FAIL 0 of 3** (21.7 / 20.4 / 22.9 s); C0, C2 PASS |
| 8 | escalate to 10240 under the same entry; plan; grade | 1 block, 1 changed attribute (3538 -> 10240) |
| 9 | `safe-apply` | live 10240, sha unchanged |
| 10 | AC1 | **PASS 3 of 3** (16.9 / 16.6 / 19.1 s), verdict YES, exit=0 |
| 11 | row `Z-S336`, 2 legs closed, entry CLOSED, instance VALID rc=0 | `339b159ea0` |

## Verification (ACTUAL output)

```
PASS C0 MemorySize moved 1769 -> 10240
   BA run 1: status 200 err None duration_ms 16885.18 init_ms 163.98 max_mem 460
   BA run 2: status 200 err None duration_ms 16551.67 init_ms 157.68 max_mem 462
   BA run 3: status 200 err None duration_ms 19105.13 init_ms 189.82 max_mem 463
PASS C1 3 of 3 cold BA day invokes 200 under 20000 ms 3 of 3
PASS C2 the control's body equals its pre value status 200 sha 4df97114d5baf968 vs pre 4df97114d5baf968
THE BA DAY ROUTE ANSWERS COLD UNDER TARGET: YES
exit=0
```

The failing tier is committed beside it (`al1_ac1_3538.txt`). The same criterion reading FAIL then
PASS three minutes apart is what makes 10240 a measured escalation rather than a guess that worked.

## The diagnosis the criterion did not ask for

AC1 answers "is it under 20 s." It does not answer "why did raising memory help," and the numbers in
its own REPORT lines do:

- **max memory USED: 455-463 MB at every tier.** It moved **8 MB** across a 5.8x memory raise. This
  function was never memory-bound. `memory_size` here is purely a vCPU proxy.
- **Init Duration: 157-204 ms**, about **0.9%** of elapsed. The 16-23 s is handler work. "Cold" in
  AC1 means a fresh sandbox, not that the cost is start-up.
- **10240 is Lambda's per-function maximum.** There is no larger number.

So the act bought the demo its margin **and exhausted the lever in the same stroke**. Filed as row
`AMGT_RESAPP-Z-S336` (OBSERVATION, INERT, DISMISSED_WITH_REASON -- nothing is owed, but the next
person to see this route slow down must not reach for `memory_size` again). Ruling 5 already names
the real remedies: track B (a deadline on `_timeline_silver_articles`, serving mentions with
`headline: null` and a reason) and track C (stop reading whole-publisher silver), which is the one
that addresses the cause.

**Margin, stated plainly because a PASS reads as comfort:** slowest passing run 19105 ms against the
20000 ms target = **895 ms**; against the hard 29000 ms gateway ceiling = 9895 ms. Safe on today's
article volume. A route whose cost scales with the day's article count has no config lever left.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `git show` | `f1d5dac151` over `ROUND_ANALYSIS.round61.md`, `MSYS_NO_PATHCONV=1` | PASS | **load-bearing**: confirmed the no-pair exemption in the CTO's words, not the order's restatement |
| `terraform plan` | twice, saved plans | PASS | 1 block, 1 changed attribute each; graded at resource-block grain with a positive control |
| `safe-apply.sh` | twice, saved plans | PASS | HALTGT pass NOT cited as evidence (LD-0267) |
| `timeline_day.py` | `--what pre`, then `--what post` twice | PASS at 10240 | the 3538 run is the measured negative arm |
| `deploy_ledger.py` | open / close-leg x2 / close | PASS | legs closed via list-argv subprocess, no shell |
| `surprise-row-gate.py` | the channel after appending Z-S336 | PASS | corpus back to baseline, 0 new failures |
| `proof-of-spec-check.py` | the al-1 instance | VALID rc=0 | first try this time |
| `comp-iam` / `comp-schedule` | not run -- DECLARED-NOT-APPLICABLE in the preflight | n/a | a `memory_size` change grants nothing and arms no cadence |

**What worked.** Reading ruling 5 at its commit instead of trusting the order's summary of it. The
order was right, but "no never-widen pair is needed" is the single sentence in a WORLD-risk order
most worth confirming upstream, and it cost one `git show`.

**What failed.** My report to the COO was **refused by the broker twice** on the 150-word cap (173
then 166 words) before I cut it to size. The gate is right and I kept overshooting it; the fix is to
draft to the cap, not to draft and then trim.

**Gap found.** Nothing new in tooling. The substantive gap is in the system under test and is row
`Z-S336`: this route's only config lever is now at its maximum.

## Blockers

**None.** No open orders.

## Current State

`opal-amgt-scoped-api`: **MemorySize 10240, Timeout 29**, CodeSha256
`E+FAZF0f63S5LxRWs4l3mCfOZgKc3erezTkjxCoVcBY=` (ak-2's, untouched by this act).
`infra/aws/terraform/harvest/scoped-amgt-api.tf` carries `memory_size = 10240` with a comment block
recording the escalation, the vCPU reasoning, and the measured fact that the function is not
memory-bound -- so the next reader of that file does not re-derive why the number is 10240.

Rollback remains ruling 5's own: `memory_size` back to 1769 through one `safe-apply`. Never taken;
C2 passed at both tiers so the trigger never fired.

Demo path: BA `/timeline/day` answers cold inside target as of 10:55Z, 2h05m before the 13:00Z demo.

Committed `5566f75d33` (entry opened) and `339b159ea0` (tf change, instance VALID rc=0, 2 legs,
evidence, row Z-S336). Entry CLOSED. The `<status>` flip is the issuer's.

**Push state: LOCAL.** `origin/CLOUD` is `1f2346734b1d` by `git ls-remote`.

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** Flip `<status>` on `AMGT_RESAPP.TO-AMGT-al-1`. Read row `Z-S336` before
   planning round 63 -- it says the config lever is finished, not just that this act passed.
2. **[`1.0.0_SA_CTO~Z`]** Ruling 5's track C (stop reading whole-publisher silver) is the remedy
   that addresses the cause; track B is the containment. Nothing from this seat is needed to decide
   between them, but the margin figure (895 ms) is the input.
3. **[`0.0.0_AB_MSTR~Z`]** The push, on Andrew's word. All four of this session's acts are LOCAL.
