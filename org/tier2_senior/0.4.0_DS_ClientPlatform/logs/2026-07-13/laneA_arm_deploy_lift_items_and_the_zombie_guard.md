# Lane ~A, part 2: ARM + DEPLOY, the silver root, lift items 8/9/10, and a guard the sovereign deleted that was still killing the pipeline

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

**agent:** 0.4.0_DS_ClientPlatform~A · **window:** 2026-07-13T11:10Z -> 15:35Z
**commits:** d28f2d5b9 · ccabfb3de · d597edb76 · 92e654c52 · 8ac1d4cdd · ff0653ff3 · ff65624f1 · 49fe7b0e4 · dd65fc30d · 097924430

---

## What shipped

| # | thing | commit | state |
|---|---|---|---|
| 1 | **Silver ROOT chokepoint guard** -- `write_silver_api_dim_parquet` RAISES on a 0-row POPULATION dim | `d28f2d5b9` | landed |
| 2 | **Pre-registered 05-08 repair delta** (before any re-derive) | `ccabfb3de` | landed |
| 3 | **INF_B_00 walk-back ARMED + DEPLOYED**, verified on the deployed bytes | `d597edb76` | **LIVE ON THE RUNNER** |
| 4 | **Runtime oracle** `verify_deployed_silver_guard.py` (AST + reachability) | `92e654c52`, `69f3ffed7` | landed |
| 5 | **ITEM 10** -- the bypass census (data-flow, AST) | `8ac1d4cdd` | **ANSWERED: NO** |
| 6 | **ITEM 8** -- the collapse detector `assert_roster_usable()` | `ff0653ff3` | landed |
| 7 | **ITEM 9** -- removing the selector BREAKS THE BUILD | `ff65624f1` | landed |
| 8 | **Andrew-direct inline record** at the selector | `49fe7b0e4` | landed |
| 9 | **Zombie-guard assertion** -- "is a control we DELETED still running?" | `097924430` | landed, RED->GREEN |

## The one that mattered: my fix was committed, CVO-verified, and NEVER LIVE

CTO~B read the deployed bytes and found what nobody had checked: `resolve_accounts_v2_for_snap`
**DEFINED:0 CALLED:0** on the runner. My selector fix was committed, CVO-VERIFIED, and **serve-held** -- so a
re-derive would have **re-collapsed $202,062,830 onto one advisor**, and:

> **the coverage guard CANNOT catch that class. Its basis is `{account_id: net_nna}` -- `advisor_key` is not
> in it -- and in a COLLAPSE NOTHING VANISHES.** Deletion and collapse are **disjoint**, and we had a guard
> for one of them while calling the estate covered.

Armed under CTO~B's arch-gate + COO's NEVER#2 co-sign, and verified the way they demanded -- **download and
import from the bucket**, not a deploy log:

```
deployed INF_B_00   876 lines (was 760)
  resolve_accounts_v2_for_snap   DEFINED: 1  CALLED: 1   (was 0/0)
  accounts_v2_key_for_snap (OLD single-key) DEFINED: 0   <- the broken contract is GONE
  IMPORT on a clean path: OK    INF_AOR_FOLD_ACTIVE: unset (NOT a go-live)
  EXERCISED on real S3, 2026-05-08: walk-back ENGAGED -> 852 rows, 4 reps.  REPAIRED.
```

**Pre-registered the repair delta BEFORE arming** (`ccabfb3de`): firm $202,062,830.31 -> $252,714.37;
peter_lee +$164.6M; patrick_scanlan +$20.8M; joe_brandenburg +$16.4M. **Conserves to the cent**, rows
unchanged, and it lands **between the two healthy neighbours** -- a control it was not fitted to.
*A number registered before the run is evidence; the same number after it is a rationalisation.*

## The silver root, and the measurement that stopped it being an outage

`write_silver_api_dim_parquet` accepted the 0-row roster and wrote it. The guard for **this exact incident**
already existed -- in `main()` -- and **the daily producer is a Lambda that imports the builder and never
calls `main()`**. *The fix for the 05-08 collapse was put in the path that wasn't broken.*

**Per-dim disposition, MEASURED, not reasoned:**
```
billing      1,364 of 1,567 partitions are 0-row (87%)  -> LEGITIMATE (event dim)
accounts_v2      1 of    69                             -> THE DEFECT (population dim)
```
**A blanket `raise on empty` would have aborted the nightly on 1,364 legitimate billing partitions.**
That number is the only reason this is a guard and not an outage.

## ITEMS 8 / 9 / 10 -- all closed, all CTO~B-verified

- **10 (the bypass census): NO.** 71 scripts -> 27 touch the roster -> **69 attribution WRITE SITES** -> 5
  DERIVED. Only `INF_C_01` derives without a walk-back, and CTO~B grounded it further than I did: it
  references `accounts_v2` **once, in a comment**, reads the roster **zero times**, and is **structurally
  immune** -- not merely "owned by someone else." **Item 9 is sufficient; the ledger does not grow.**
- **8 (the collapse detector).** Threshold **measured across all 70 partitions**: legitimate catchall runs
  **1.53%-2.41%**; the poisoned 04-28 is **96.2%**. Both proven-RED dates fire on real S3; both healthy days
  pass.
- **9 (removal breaks the build).** AST-asserted, mutant-proven: I removed the selector **and inlined a
  bypass** (the C_07 evasion) -> the gate fails.

### The trap in item 8's spec that would have been the worst thing I did today
The spec said to assert roster usability **in the loader**. `accounts_v2` **begins on 2026-04-28**, and
`INF_B_00`'s oldest-partition fallback resolves **all 2,271 historical dates back to 2020** onto it. A raising
catchall guard there **aborts six years of historical builds** -- a fail-closed fix firing on **97% of the
estate's history**. Scoped it to the time-lock backfill instead.
> **The 04-28 roster is not CORRUPT. It is PRE-ASSIGNMENT** -- structurally perfect, fully populated, and
> useless as a source of advisors. **Only the CALLER knows which of those it needs.**

## A guard the sovereign DELETED was still killing the pipeline

Chasing AE's `inf-api-txn` finding, I found the opposite of what was filed:
```
inf-api-positions   $150M-$300M (CANONICAL constants)  *** RAISES ***  3 reachable sites -> positions_mv  DAILY
inf-api-reps        $150M-$300M (CANONICAL constants)  *** RAISES ***  3 reachable sites -> the roster    DAILY
inf-api-txn         $ 50M-$400M (the "weakened" band)      raises      0 reachable       -> INERT
```
Andrew retired Guard B on **2026-05-08** -- *"vestigial guardrail not logical and we dont want it"*. The
retirement reached three copies and not the other three.

> **Firm AUA ~$202M against a $150M floor. A 26% DRAWDOWN -- AN ORDINARY BEAR MARKET -- MAKES BOTH LAMBDAS
> RAISE AND STOP WRITING. THE PIPELINE DIES EXACTLY WHEN THE MARKET CRASHES**, and its remedy is to stop
> producing data. *We were inside the band. That is luck, not a control.*

**COMPARE BEHAVIOUR, NOT VALUES.** The dangerous copies carry constants **identical** to the canonical; the
one that *looks* wrong never calls the guard. **A census comparing CONSTANTS calls the killers clean and the
corpse dirty.** `comp-constants` fired -- on the inert copy. *A NUMBER is the most convincing token of all,
and it is still just a token.*

Built the durable half (`097924430`): **"is a control we DELETED still running somewhere?"** -- the question
the estate had **no instrument for**. *We only check that controls we ADDED are present; nothing checked that
controls we REMOVED are gone. That asymmetry is how it survived two months.* AE deployed the retirement; I
re-verified on the deployed bytes (**RED -> GREEN across a real state change** -- better validation than any
mutant) and confirmed his same-file edit **did not regress the 0-row guard**.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-surface-check` (auto, safe-commit x10) | PASS | read the output, not the silence |
| `commit-gate.sh` (x10) | PASS | clean |
| `comp-pipescript io INF_B_00` | **GAP** (logged earlier) | omits the `accounts_v2` READ and the `gold/canonical/holdings` WRITE |

**GAP:** `comp-constants` compares **values**; it cannot see a **behaviour** divergence, and it pointed at the
inert copy while waving through two live zombies. **Filed to 0.7.0/COO; this is a real coverage gap in a
mandated gate, not a one-off.**

## What I got wrong, and how each was caught

**Nine self-caught failures. Not one caught by being careful.**
1. **Census-by-mention in a docstring** -> turned a real gate RED with a comment.
2. **"F7 has no builder"** -> it was built, 21/21, firing RED. I inferred from phrasing without opening the file.
3. **"The root layer is closed"** -> I censused `data/` and never opened `infra/`. **The live daily producer was in `infra/`.**
4. **A rigged fork detector** -> it globbed from `data/` and **PASSED while the runtime was 0-for-5**.
5. **A log line scored as a guard** -> `CALL_MARKERS` contained `'0-row'`; it matched `_log("...0-row CSV...")`.
6. **Over-condemned `inf-api-txn`** -> flagged EXPOSED off a call site the handler never reaches.
7. **The census missed `INF_B_00:424`** -- the derivation at the centre of the SEV -- because it is a **dict
   literal**. *One proven-RED case validates ONE SHAPE.*
8. **Falsely condemned `INF_D_08`** -> my guard-detector matched **function NAMES**; D_08 implements the
   walk-back inline. *The C_07 lesson with the sign flipped.*
9. **I executed my own commit message** -> backticks in a `-m` body were shell-evaluated and **a clause was
   deleted from the immutable record** (`49fe7b0e4`; annotated `dd65fc30d`; gate requested from CTO). I had
   used `-F` correctly four times that day and dropped it on the fifth -- **in the message about instruments
   that score prose as code.**

> **KNOWING A FAILURE MODE BY NAME DOES NOT IMMUNIZE YOU AGAINST WRITING IT.**
> **CARE IS NOT A CONTROL; CARE IS WHAT YOU HAVE INSTEAD OF ONE.**

## Current State

- **`INF_B_00` walk-back is LIVE on the runner.** The $202M collapse can no longer be re-derived.
- **All 5 silver Lambda writers COVERED**; **no zombie guards**; oracle exit 0.
- **Chain still HELD.** Nothing served. `AOR_FOLD_ACTIVE` OFF. `build_assets_dim.py` untouched by any verb.
- **The served 05-08 artifact is STILL COLLAPSED** -- correct-on-next-derive, and the re-derive is gated.

## Next Steps

1. **[1.0.0_SA_CTO~B]** the **Lambda-layer consolidation**. Case sent, unprompted: **the fork produced TWO
   production defects today in OPPOSITE directions** (a FIX and a REMOVAL that both never reached the
   runtime), and **the repo looked correct throughout both**. The argument is no longer tidiness.
2. **[0.7.0_AE_CloudOps]** `inf-api-txn` stays **filed, not fixed** -- inert; deliberate-or-drift unknown.
3. **[me]** available. Not touching `aor_resolution.py` -- DS-base owns P3 (and my "count it, don't reason
   about it" advice killed it: **the AoR field exists in 0 of 70 snapshots**; you cannot derive an
   effective-from date from a single observation).
