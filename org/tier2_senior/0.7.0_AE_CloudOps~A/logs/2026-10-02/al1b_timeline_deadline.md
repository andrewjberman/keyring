# AMGT_RESAPP round 62 -- AMGT-al-1 act (B), track B's 18 s silver-read deadline (session 352b911c, fifth act; URGENT, freeze 12:30Z)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

## Window

11:17Z (act (B) GO) -> 11:36Z. 2 commits by this lane, 1 inbound message acked (28417), 1 build +
upload, 1 code-only apply, 1 surprise row. Deployed 11:27Z, graded 11:32Z against a 12:30Z freeze
and a 13:00Z demo.

## What I did

Code-only redeploy of `opal-amgt-scoped-api` at `a2ff06d1a1`, carrying al-2: the timeline day
route's silver read now runs under an 18 s deadline from handler start, and on the deadline serves
the day's mentions with `headline: null` and one plain `headline_reason` **as a 200**, instead of
being killed by the sandbox.

**This act carried the never-widen pair and act (A) did not** -- ruling 5 classed track A
config-only, and track B as moving served output on the timeout path, "so it carries the never-widen
pair". Both classifications read at the ruling, not inherited from the order.

## Deployment Sequence (AE role section)

| # | act | result |
|---|---|---|
| 1 | order step 1: is the issuer's pre still the pre? | `AL2_CONTROLS_PRE.json` carries `E+FAZF0f...` **and MemorySize 10240**, so it postdates act (A) -- used as-is, no re-run |
| 2 | NEVER-2 entry opened, 4 legs, COMMITTED before the build | `29aac2ea64` |
| 3 | worktree at `a2ff06d1a1` | detached (removed at close) |
| 4 | pre-build guard: sha **+ MemorySize + artifact version**, live | all three matched -> build |
| 5 | `--build-only`, then independent diff grade | CHANGED 1, set `[scoped_amgt.py]` both ways, fabricated control discriminates |
| 6 | build + upload | `YSqlUTOW` -> `iDuPquXb`, content-sha256 `bZBmEtRr...`, 41,118,711 B |
| 7 | graded bytes vs uploaded bytes | **identical** |
| 8 | plan | 1 block, 3 attribute lines, **`memory_size` ABSENT** |
| 9 | `safe-apply` of the saved plan | `0 added, 1 changed, 0 destroyed` |
| 10 | live read | sha `bZBmEtRr`, **MemorySize 10240 preserved**, Timeout 29, CodeSize matches upload |
| 11 | `timeline_b.py --what post` | TRACK B SERVES THE DAY ROUTE INSIDE THE CEILING: YES |
| 12 | `pytest test_timeline_silver_deadline.py` | 3 passed |
| 13 | row `Z-S337`, 4 legs closed, entry CLOSED, instance extended | VALID rc=0, `9da65fe4b6` |

## Verification (ACTUAL output)

```
PASS C0 the deployed code moved E+FAZF0f...VcBY= -> bZBmEtRr...m9kW4=
   BA run 1: status 200 err None duration_ms 16532.87 init_ms 161.48 articles 5 headline_reason False
   BA run 2: status 200 err None duration_ms 15135.96 init_ms 146.07 articles 5 headline_reason False
   BA run 3: status 200 err None duration_ms 18006.03 init_ms 189.11 articles 5 headline_reason True
PASS C1 3 of 3 cold BA day invokes answer 200 3 of 3 status 200; cold 3 of 3
   control .../day/2026-09-30: sha 6c25fff80da9be93 vs pre 6c25fff80da9be93 equal True
   control .../day/2026-10-01: sha 69ecb7a884a83585 vs pre 69ecb7a884a83585 equal True
PASS C2 both control days' bodies are byte-equal to their pre values 2 of 2
TRACK B SERVES THE DAY ROUTE INSIDE THE CEILING: YES
exit=0
```

`3 passed in 3.53s` on the planted slow read.

## The two findings

**1. `memory_size` absent from the plan is the clause that mattered.** Act (A) set 10240 forty
minutes earlier under a *different* NEVER-2 entry. If act (B)'s plan had carried `memory_size`, one
act would have silently reverted another act's signed value -- the shape that makes a two-act
sequence unsafe. So I put MemorySize into the pre-build guard alongside the sha and the artifact
version, making the build *prove* it stood on act (A)'s state rather than assume it, and I read
MemorySize back after the apply. Absent in the plan, 10240 after.

**2. The new branch fired in production during its own acceptance run -- row `Z-S337`.** Run 3
returned 200 at **18006.03 ms carrying `headline_reason`**, 6 ms past
`TIMELINE_SILVER_DEADLINE_S = 18.0` (`scoped_amgt.py:4710`), while runs 1 and 2 at 16532.87 and
15135.96 ms took the normal path.

So the 18 s line sits **inside** the observed cold spread rather than above it -- act (A)'s AC1 read
16.6 / 16.9 / 19.1 s at the same memory an hour earlier. On today's data the degraded branch is
roughly a coin-flip per cold load, which means Andrew's 13:00Z demo will show bracketed
`[no headline]` placeholders on some cold BA day views. That is the **specified** outcome, not a
failure: the route no longer dies, and PROD renders the placeholder safely (CTO half:
`TimelinePanel.tsx:354` renders `row.headline ?? '[no headline]'`). Reported to the issuer in the
close message rather than left to the channel, because it changes what the demo looks like.

**I did not quote a rate.** Three concurrent runs sharing one post-deploy moment cannot establish
one, and the row says so rather than printing "33%".

**Why both grades are needed, not one:** the pytest proves the branch *behaves* when forced; the
live grade proves it *fires* on real data but cannot make a read slow on demand. Neither alone
establishes the other, which is why the CTO condition names both.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `timeline_b.py` | `--what post --pre round62/AL2_CONTROLS_PRE.json` | PASS | also fired the new branch once -- the unasked-for finding |
| `pytest` | `test_timeline_silver_deadline.py -q` | 3 passed | the only arm that proves the branch is correct |
| `ak2_content_diff_grade.py` | `--expect-changed lib/research/api/scoped_amgt.py` | PASS | **generalized, not copied** -- one reviewed grader now serves a 3-file and a 1-file set |
| `terraform plan` / `safe-apply.sh` | saved plan, applied from it | PASS | `memory_size` absence graded explicitly |
| `deploy_ledger.py` | open / close-leg x4 / close | PASS | list-argv subprocess, no shell |
| `surprise-row-gate.py` | after appending Z-S337 | PASS | corpus at baseline |
| `proof-of-spec-check.py` | the extended al-1 instance | VALID rc=0 | first try |

**What worked.** Putting MemorySize in the build guard. It wasn't asked for, and it's the one check
that distinguishes "building on act (A)" from "assuming act (A)". Also: generalizing the diff grader
with a flag instead of copying it, so the same reviewed implementation covered ak-2's three files
and this act's one.

**What failed.** My close report to the COO was **refused by the broker a third time** this session
on the 150-word cap (181 words). Three refusals in one session is a pattern, not a slip: I was
drafting the full account and then trimming, when the cap requires drafting to it. The gate was
right all three times.

**Gap found.** None new in tooling. The substantive one is row `Z-S337`: the deadline constant sits
inside the cold distribution, so the containment fires routinely. Moving the distribution is ruling
5's track C.

## Blockers

**None.** No open orders. **FREEZE IN EFFECT** -- nothing deploys to this function between 12:30Z
and the end of Andrew's demo read (ruling 5a).

## Current State

`opal-amgt-scoped-api`: CodeSha256 `bZBmEtRrAagqpRJCa4JLvyZmNaM0EvkOp6K6Gcm9kW4=`, **MemorySize
10240**, Timeout 29, CodeSize 41,118,711, LastModified 2026-10-02T11:26:56Z. Artifact VersionId
`iDuPquXbC0ZpmHbnZREUzQd7CVYh15vi`.

Rollback: artifact `YSqlUTOWHwV6H7LePjd1pr9DKomiDo5U` through one code-only `safe-apply`, restoring
`E+FAZF0f...`. Never taken; C1 and C2 both passed.

Served behaviour now: BA `/timeline/day` answers cold inside the 29 s gateway ceiling in all
measured cases. A day whose silver read passes 18 s serves mentions with `headline: null` and
`headline_reason` as a 200. Every non-deadline body is byte-equal to its pre value (2 of 2 controls).

Committed `29aac2ea64` (entry opened) and `9da65fe4b6` (instance extended VALID rc=0, 4 legs,
evidence, row Z-S337). Entry CLOSED. The `<status>` flip is the issuer's.

**Push state: LOCAL.** `origin/CLOUD` is `1f2346734b1d`; local HEAD `9da65fe4b6`.

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** Flip `<status>` on `AMGT_RESAPP.TO-AMGT-al-1` -- acts (A) and (B) are both
   closed. Row `Z-S337` is the pre-demo read.
2. **[`1.0.0_SA_CTO~Z`]** Ruling 5's track C is the fix that moves the cold distribution rather than
   capping it; the carried post-demo DSGN item (print `headline_reason` in place of
   `[no headline]`) becomes more valuable now that the branch is known to fire routinely.
3. **[`0.0.0_AB_MSTR~Z`]** The push, on Andrew's word. All five of this session's acts are LOCAL.
