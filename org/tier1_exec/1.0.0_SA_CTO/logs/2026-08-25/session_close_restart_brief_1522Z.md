# CTO SESSION CLOSE + RESTART BRIEF -- 2026-08-25 15:22Z

**Seat:** `1.0.0_SA_CTO`. **archetype:** MIXED. **secondary_archetypes:** DIAGNOSE, COORDINATE, VALIDATE.
**Window:** 2026-08-25 ~04:00Z -> 15:22Z (continuous). **50 commits this seat today.**

>> **WHY THIS FILE EXISTS: Andrew wound the entire fabric down ~14:3xZ, is rebooting the device,
>> and will instantiate a fresh CTO ON THIS LOG to restart all laptop-directive work.** Written for
>> a reader with ZERO prior context. Everything below is measured or cited; nothing is recalled.

---

# PART 1 -- DO THESE IN ORDER

## ACT 1. PUSH. BEFORE ANYTHING ELSE.

```
local HEAD    079b1b770e
origin/CLOUD  e291d38e4f
UNPUSHED      8 commits
```
`0.0.0_AB_MSTR` holds the integrator push (LD-0367). **Among the unpushed are the entire D8
directive, the `MDPF_COTREMEDIATION` registration, and the confirmed root cause of a live outage.**
A seat that pulls before the push sees none of it.

## ACT 2. RE-ARM THE LOOP -- FROM THE CARRIER CLAUSE ONLY

`/self-drive laptop directives` ran ticks 1-17 today (cron `f03462e0`, 30m) and **died with the
session.** Its durable carrier is the **`org/XXX.md` Step 1b-F row** for this serial, landed
@`4e754258fd`. **Re-arm from that row and nothing else -- never from memory, never from a log**
(skill s.0.4). Scope is now **6 directives / 13 projects**, completion **2 of 13**.

## ACT 3. THE LIVE OUTAGE -- see PART 3. It has a CONFIRMED root cause and a small remedy.

---

# PART 2 -- THE BOARD. ALL SIX LAPTOP DIRECTIVES.

```
directives-check: live=10 retired=1 malformed=0 rc=0
LAPTOP: 6 directives -> 13 projects | COMPLETION 2 of 13 | UNREACHABLE 0 | UNMEASURABLE D5
open TOs: D0=4  D1=3  D2=19  D3=7  D5=0  D8=0
```

| D | project | status / stage | THE NEXT STEP |
|---|---|---|---|
| **D0** | NFRA_COMPTOOLS | active EXECUTING | 2 TOs on disk at `0.8.0_AE_CloudComp`, both GO'd. Lane has no live session -- needs a seat. |
| **D0** | NFRA_DEPLOYLEDGER | active EXECUTING | `HELD-STATE` TO staged, GO'd 2026-08-18. **Its 5-specimen re-classification is NOT the 106 no-status ledger records** (disjoint; see PART 4). |
| **D0** | NFRA_DEPLOYCENSUS | **complete 08-18** | done |
| **D1** | D1_CATVIEWS | active EXECUTING | **DS lane certified 9/9 @`989a92e806`; the DE lane instance is UNCERTIFIED and sits with `3.0.0_SA_CVO`.** That cert is the open item. |
| **D2** | ADVI_PERFRP | active EXECUTING | 3 PASS / 10 UNCOMPUTABLE. **10 criteria need a leaf on the RENDER path. The publish gate STANDS -- zero perfrp leaves served is CORRECT.** |
| **D2** | ADVI_INSURE | active DECOMP | `~J` delivered TO-R1-DS 14/14, ACCEPTED. **Advisor spine leg NOT BUILDABLE -- BD dim 436 (PART 5).** 3 of 4 legs deliver. |
| **D2** | ADVI_STITCH | active EXECUTING | no open item at this seat |
| **D2** | ADVI_49FSRC | active PRD | no open item at this seat |
| **D2** | ADVI_COTKEY | active PRD | **BLOCKED on Andrew -- key of record. CVO refused it as sovereign: "I suspect" is not a ruling.** |
| **D2** | OPAL_ADVIPOINTERS | active (no dep_stage) | no open item at this seat |
| **D2** | ADVI_BDPLAT_RESTORE | **complete 08-19** | done |
| **D3** | D3_MODELOVERLAY | active PRD | `~K` delivered TO-R1-DS 16/16, ACCEPTED, at CVO for cert. **Advisor LEVEL not buildable -- same BD dim 436.** Deliver 3 of 4 levels. |
| **D5** | (none) | **UNMEASURABLE** | **Register has NO member projects. The loop cannot ever read DONE on D5.** Route to MSTR. |
| **D8** | **MDPF_COTREMEDIATION** | **active PRD** | **THE LIVE OUTAGE. PART 3.** |

**Also for MSTR:** `D9.PFMG_TAXSMA` reads `no-json` -- the last instance of the class Andrew's
Fix 1 closed this morning. And **D8 now appears in BOTH the live register and
`DIRECTIVES_RETIRED.yaml`** (the cut Philosophy row). `malformed=0`, so not a violation -- but a
reader searching `D8` finds two rows with different titles. **The retired row is the historical
record of the 08-20 cut and must NOT be deleted.**

---

# PART 3 -- D8 / MDPF_COTREMEDIATION: A LIVE CLIENT-FACING OUTAGE, ROOT CAUSE CONFIRMED

**Andrew-direct ~14:20Z re-minted D8 as "Model Portfolios Pipeline Fortification"** (the prior D8,
"Philosophy + benchmark modal live-edit", was CUT 2026-08-20T20:32:35Z and carries nothing forward).

## THE SYMPTOM

```
platinum/mdpf/{partner}/aggregate-aua-timeseries.json   field as_of_last
  49financial 2026-08-24 OK      inflection 2026-08-24 OK
  cottonwood  2026-08-19 FROZEN  global     2026-08-19 FROZEN
NEVER#1 discharged FIRST: expected_last_trading_day(2026-08-25) = 2026-08-25.
FOUR TRADING DAYS. Not a weekend.
```

## THE CONFIRMED ROOT CAUSE

```
[ERROR] RuntimeError: event run 20260825T114559Z had 1 failure(s):
  blackdiamond/cottonwood/bronze/holdings/HOLDINGS_DAILY_2026-08-24.xlsx:
  VendorDriftError("blackdiamond/holdings: xlsx header DRIFT.
    observed = [... 'Account Supervised' ... 'Holding Supervised']   21 columns
    declared = [...      neither one      ...]                       19 columns")
mirror_conversion.py:899 run_event -> RuntimeError
```

**BLACK DIAMOND ADDED TWO COLUMNS TO THE HOLDINGS EXPORT: `Account Supervised` and
`Holding Supervised`.** The silver converter's declared header contract detected the drift and
**refused to convert.** It has refused every holdings file since.

## THE CHAIN, EVERY HOP MEASURED

```
vendor .xlsx     ALL FIVE bronze tables delivered TODAY 11:45:53-54Z (holdings 08-24)   HEALTHY
S3 trigger       ObjectCreated | Prefix=blackdiamond/cottonwood/bronze/ | Suffix=.xlsx  FIRING
lambda           opal-assets-silver-blackdiamond, Active, code LastModified 2026-07-23
invocations      10/day, steady, never stopped
ERRORS           0,0,0 then 3,3,3,3,3 per day BEGINNING 2026-08-21
last silver write 2026-08-20T11:46:11Z  <- the error onset matches it EXACTLY
silver partitions blackdiamond/cottonwood/silver/fact_holdings/ LAST = date=2026-08-19
  -> build_cottonwood_mdpf_slice.py (data/assets/scripts/gold/) reads that prefix :339/:393/:400
  -> gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json: OBJECT FRESH (13:30:46Z today),
     CONTENT FROZEN (dates LAST 08-19, covered_dates LAST 08-19 n=17, provenance measured LAST 08-19)
  -> dim_mdpf_aggregate_aua_timeseries.py:1915 load_cottonwood_slice() folds it
  -> platinum/mdpf/cottonwood + global, as_of_last 2026-08-19
```

**THE LAMBDA CODE DID NOT CHANGE. THE VENDOR DID.** Andrew's guess -- *"on august 20 or so I'd
guess"* -- was exact.

## !! WHY IT RAN FOUR DAYS UNSEEN -- THE PART THAT GENERALISES

**1. The served objects are REWRITTEN EVERY DAY.** All four partners within two seconds of each
other. The publisher runs, emits, succeeds. **The staleness is INSIDE THE PAYLOAD.** Every
object-mtime freshness instrument (`comp-freshness`, `s3 ls` age, `head-object` LastModified)
reports these HEALTHY **and each is CORRECT ABOUT THE FILE.**

**2. The downstream loader is aggressively FAIL-CLOSED and every gate PASSED.**
`load_cottonwood_slice()` has FOUR `SystemExit` paths: absent/unreadable, lacks dates/by_model,
un-composed (`meta.composed_backfill` missing), scope-consistency (`covered_dates` != provenance
measured). **ALL FOUR WERE MEASURED AND ALL FOUR PASS.** Its docstring says *"the refusal IS the
outage signal"* -- **and the only outage it can signal is STRUCTURAL, never TEMPORAL.**

**3. THE GUARD WORKED.** This is not a broken converter. It detected a real vendor schema change
and refused rather than silently absorbing two new columns -- exactly what Rule 17 asks of silver.
>> **THE DEFECT IS NOT THE REFUSAL. IT IS THAT A LOUD, CORRECT, DAILY-REPEATING REFUSAL REACHED
>> NOBODY FOR FOUR TRADING DAYS.**

## !! THE CONVERGENCE WORTH NAMING

The two columns Black Diamond added are **`Account Supervised`** and **`Holding Supervised`** -- the
exact supervised-status fields `0.4.0_DS_ClientPlatform~F`'s `SPEC_COT_OPAL_SUPERVISION_PREDICATE`
was written about THIS MORNING, and that Andrew ruled on at ~14:05Z.
**The vendor shipped the field the business was asking for, and our drift guard turned it into a
four-day outage.**

## THE REMEDY -- SHAPE ONLY. NOT AUTHORIZED BY THIS LOG. NOT DONE BY THIS SEAT.

1. **Declare the two columns** in the `blackdiamond/holdings` silver header contract.
   **Rule 17: ADD as passthrough. NEVER slim, filter, fillna, or drop.**
2. **Re-run 2026-08-20 .. 2026-08-24.** Bronze `.xlsx` for all five tables is ON DISK -- nothing lost.
3. **DS lane owns silver per Rule 13. `2.0.0_SA_COO` seats it from the atom-decomp (Rule 27 stage 3,
   BEFORE any TO exists).**

>> **!! THE RE-RUN TRAP, RECORDED BEFORE ANY SEAT EXISTS: a backfill WILL produce correct-looking
>> data. If anyone re-runs WITHOUT declaring the columns, the next holdings file drifts again and
>> the freeze returns silently.** A re-run that produces correct data does not establish the cause.

## AC STATUS
AC1 (root cause at source, as a mechanism) is **discharge-ready**. AC5's null-filled `dates` array
and the forward-fill signature are **downstream artefacts of a silver layer stopped at 08-19** --
questions against a known cause now, not open leads.

---

# PART 4 -- SETTLED TODAY. DO NOT RE-LITIGATE.

- **Andrew ~14:05Z: WHOLE BOOK IS THE DEFAULT.** 49F unsupervised **$138,839,619.90 IN**.
  Cottonwood's supervised-only view is a **PARTNER REQUEST, not a semantic ruling.**
  **The Cottonwood $30.3M exclusion and the 49F inclusion are BOTH CORRECT AND NOT IN TENSION.**
  !! **An estate-wide "make the firms consistent" fix would be a DEFECT.**
- **Andrew ~14:12Z: ALL WORK SITS UNDER A DIRECTIVE; a project minted mid-task is TAGGED TO THAT
  DIRECTIVE AT CREATION, by the seat minting it.** Measured basis: 332 project JSONs, 103 active,
  **91 members of nothing** -- 49 with open TOs (live, untracked), 42 with zero (close-out backlog).
  **OPPOSITE REMEDIES; must not be worked as one item. DIRECTION RATIFIED, MIGRATION NOT AUTHORIZED.**
- **12:45Z ADVI chain PASSED all four pinned expectations.** `REFUSED-NO-BMV` 7,335 -> **0** over the
  7,334 both-day accounts, positive control fires at 7,334. Three seats, three instruments, same numbers.
- **CVO found 15 of 6,412 returns breaching the ruled 0.05 threshold** (one at +69,056%; body sane,
  p50 -0.21%). **`c04` check 7's deferral is OVER** -- its premise (nothing to evaluate) expired at
  12:47:31Z. COO to seat. **Nobody is calling those 15 defects.**
- **a06 weekend guard:** the 49F gold chain is **dead every Sunday and Monday** (`map_dates[-1]`, no
  non-empty check; map writes 13:15Z, chain runs 12:45Z, so `[-1]` is always D-1). **NOTHING TO
  BACKFILL** -- both aborted runs targeted an already-existing partition. **Fix forward. The
  mechanism is undiminished.** !! The obvious fix (read today's map / move the chain) INVERTS the
  ordering and breaks the four working days.
- **Portal CI is GREEN on `fce757cb`**; the provenance-read backstop is live after six dark runs.
  `ci.yml:56`'s zero-file `tsc --noEmit` under a step named "Type Check" is a **LOG-HONESTY defect,
  NOT a coverage gap** (step 5's `bun run build` is `tsc -b && vite build` and type-checks for real).
- **`TO-D3.3` SUPERSEDED BY VINTAGE** (its `<authority>` names a vintage predating PRD s4c ruling 9).
  Surface (c) publisher key = `0.7.0_AE_CloudOps`.
- **The promote ledger closes** as CLOSED-WITH-PROOF / third-party measured, limitation written in.
  !! **Its manifest drift is the MECHANISM of the PERFRP-on-PROD finding:** the manifest pinned DEV
  @`d43b88c5`; the merge executed 17h later against `063ff4d7` -- **28 commits later, 11 of them
  ADVI_PERFRP.** A manifest that pins a source sha at deploy-START and a merge that resolves the
  branch NAME at deploy-TIME are two different deploys wearing one ticket.
- **The 106 no-status ledger records are NOT in `NFRA_DEPLOYLEDGER.HELD-STATE`'s scope** (that TO
  covers 5 named specimens). **BLOCKED-ON-SEQUENCE with the predecessor named** -- they would be
  classified against a lifecycle axis HELD-STATE is about to create.

---

# PART 5 -- OPEN AT ANDREW: 4 CARDS

1. **`ADVI_COTKEY` key of record.** CVO refused as sovereign.
2. **BD dim 436 -- a VENDOR ASK.** One Black Diamond template field (`dim 436` not selected by
   `template 390224`) blocks **D3's advisor level AND ADVI_INSURE's advisor spine leg**. Source-
   confirmed; the runner declares its own gap with its own positive control. Record @`a6c76382b1`.
   !! **The prohibition is the load-bearing half: NEVER sum to advisor level without `is_primary`.**
   90.6% of accounts sit in 2+ portfolio groups (mean 4.86) -- an advisor sum counts each ~5 times
   and **produces a NUMBER, not an error.** **The absent level is the SAFE state.**
3. **CVO's condition-4 no-gates test** as a clarification of his own rule.
4. **Retro-tagging volume** -- all 49 orphans-with-TOs now, or as-touched?

---

# PART 6 -- MCP + RULINGS THIS WINDOW

~60 dispatches. **Significant:** 5 Andrew-direct records (06:1xZ recs-approved, 08:5xZ PROD/data,
12:0xZ fixes+reorient, 14:12Z directive-tagging, 14:20Z D8+outage). **Rulings issued:** the DS~F
spec fold (4 homes), global-has-no-Client-L1, PERFRP accept, ROSTER UNION CLOSURE, `criterion_verbatim`
as MECHANISM, the 922+5 reason-string call, `ci.yml:56` build-mode + its sequencing, the promote-ledger
close, TO-D3.3 superseded-by-vintage, the 106 scope call, c04 deferral over. **Verdicts received:**
CVO 3 (D1 claim SPLIT, label supersession CONDITIONAL, COTKEY REFUSED-AS-SOVEREIGN), CVO tick-15
adjudication (s.11 SIBLING SECTION, my label corrected).

# PART 7 -- Compiler Tools

| tool | invocation | result |
|---|---|---|
| `lib/trading_calendar` | before EVERY staleness claim | NEVER#1 discharged twice (twr, MDPF) -- 4 trading days both times |
| `aws s3api` list/head (UTC) | served frontiers, 4 partners x 2 products | **objects FRESH over frozen payloads -- the session's biggest finding** |
| `aws logs filter-log-events` | opal-assets-silver-blackdiamond | **the VendorDriftError -- the confirmed root cause** |
| `aws cloudwatch get-metric-statistics` | Invocations + Errors, 6d | **10/day invoked, 3/day failing since 08-21 -- the onset date** |
| `pandas.read_parquet` + positive control | twr D and D-1 | REFUSED-NO-BMV 7,335 -> 0; control fires at 7,334 |
| `comp-find -i` | ~10 sweeps | the cot MDPF code home (falsified my own claim); BD dim 436; the silver writer |
| `git show <vintage>:<path>` + 2 controls | TO-D3.3 vs ruling 9 | superseded-by-vintage |
| `bash -x safe-commit.sh` | an invisible refusal | **owned-paths, not the risk-reflex I had blamed** |
| `directives-check.py` | 17 ticks + the D8 mint | live 9 -> 10, malformed=0, rc=0 |
| `safe-commit -F` (msg-verify) | 50 commits | all MATCH, path-scoped |

**What worked:** measuring the payload rather than the object; running the positive control on every
zero; reading the file instead of the summary (found the third dead CI step, and the VendorDriftError).

**What failed, mine:** (1) a **category error** -- cited `data/cot/scripts/gold/` (Cottonwood's ADVI
tree) as evidence about its MDPF layout; **Andrew corrected it**, and the false version FLATTERED a
hypothesis he had already voiced, which is the class of claim that gets least scrutiny. (2) A
**sequencing ruling built on a false premise** -- I enumerated "steps 3-5" without reading what step 5
does, in a file I had open; DE~C falsified it by reading four lines further. (3) **"the transition has
already happened"** -- read past a correctly-stated push state. (4) A **press sent four minutes stale**
that carried a sovereign rebuke at a seat which had already delivered. (5) **Misdiagnosed a commit
refusal** as a risk-reflex block. (6) A **completion predicate** (`== "complete"` vs the register's
`"complete 08-18"`) that was correct-by-luck for nine ticks. (7) An **incident-check** that matched
`CTO` inside `deteCTOr`, run in the same tool call as the commit it gated.

**Gap found:** **object-mtime freshness is structurally blind to a payload freeze.** A served key
rewritten daily with frozen contents passes every instrument this estate owns. **That is the condition
D8 exists to end** -- and it is why a four-trading-day client-facing outage was found by Andrew and
not by us.

# PART 8 -- BLOCKERS

**None at this seat.** Nothing is held, nothing is staged, the working tree carries no CTO-owned
dirt. The 61 dirty paths in the tree belong to seats that went down mid-work and are untouched.

# PART 9 -- NEXT STEPS BY OWNER

- **[0.0.0_AB_MSTR]** (1) **PUSH -- 8 commits, ACT 1.** (2) Confirm the D8 register row I wrote in
  your lane under an audited `GIT_COMMIT_AUTHOR_OVERRIDE=TIER0_MSTR` (@`a0394e34f4`) -- the
  owned-paths gate refused correctly and I overrode on Andrew's explicit instruction with you down.
  (3) `D9.PFMG_TAXSMA` no-json. (4) D5's empty member set. (5) The D8-in-two-files question.
- **[2.0.0_SA_COO]** (1) **`MDPF_COTREMEDIATION` atom-decomp -- Rule 27 stage 3, ahead of all D8
  fortification work.** (2) The promote-ledger close (text supplied 13:09Z; two evidence cells need
  fixing first). (3) a06 weekend guard seat. (4) c04 check 7. (5) The twr status-vocabulary owner.
  (6) `ci.yml:56` cell (non-urgent).
- **[3.0.0_SA_CVO]** `D1_CATVIEWS.TO-R1-DE` cert; `D3_MODELOVERLAY.TO-R1-DS` cert.
- **[0.8.0_AE_CloudComp]** 2 GO'd TOs on disk, no live session -- needs seating.
- **[Andrew]** the 4 cards in PART 5.
- **[1.0.0_SA_CTO, next instance]** ACT 1 -> ACT 2 -> then drive the board in PART 2. **The D8
  outage is the priority and it no longer needs diagnosis -- it needs a decomp and a seat.**
