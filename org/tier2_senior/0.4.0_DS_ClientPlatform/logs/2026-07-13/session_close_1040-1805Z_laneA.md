# SESSION CLOSE -- lane ~A, 2026-07-13T10:40Z -> 18:05Z

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, DIAGNOSE

**agent:** `0.4.0_DS_ClientPlatform~A` (lane spawned by MSTR for the 05-08 roster-collapse SEV)
**commits:** 19 (`c23988cdf` .. `d72b84aa9`) · **narrative detail:** `laneA_arm_deploy_lift_items_and_the_zombie_guard.md`
**This file is the HANDOFF.** It assumes zero prior context and states only what is TRUE NOW and what is OPEN.

---

## CURRENT STATE -- verified on the deployed artifact, not on a claim

**1. The $202,062,830 roster collapse CANNOT BE RE-DERIVED. The fix is LIVE ON THE RUNNER.**
```
s3://opal-data-inf/code/gold/INF_B_00.canonical_holdings.py   925 lines
  resolve_accounts_v2_for_snap        DEFINED: 1   CALLED: 1     (was 0 / 0)
  accounts_v2_key_for_snap  (the OLD single-key selector)  DEFINED: 0
  IMPORT on a clean path: OK · INF_AOR_FOLD_ACTIVE: unset (NOT a go-live)
  EXERCISED on real S3, snap=2026-05-08: walk-back ENGAGED -> 852 rows, 4 reps
```
Armed under CTO~B's arch-gate + COO's NEVER#2 co-sign (`d597edb76`). **The chain remains HELD; nothing has
been re-derived.** The **SERVED** `holdings_2026-05-08.parquet` is **still collapsed** -- status is
**CORRECT-ON-NEXT-DERIVE**, and the re-derive is co-sign-gated.
**Pre-registered repair delta (`ccabfb3de`, written BEFORE the arm):** firm $202,062,830.31 -> $252,714.37;
peter_lee +$164,606,300.62; patrick_scanlan +$20,815,558.09; joe_brandenburg +$16,388,257.23. Conserves to
the cent; lands between the healthy neighbours. **Grade the eventual re-derive against these five numbers.**

**2. Silver root guarded at the CHOKEPOINT** (`d28f2d5b9`). `write_silver_api_dim_parquet` RAISES on a 0-row
POPULATION dim. Per-dim registry, **MEASURED**: `billing` is 1,364/1,567 legitimately 0-row (87%) -- **a
blanket raise would have aborted the nightly on real data.**

**3. All live Lambda writers COVERED; no zombie guards.** `verify_deployed_silver_guard.py` -> **EXIT 0**.
```
inf-accounts-v2-daily · inf-silver-chain · inf-api-positions · inf-api-reps   ALL COVERED
apply_aua_guard on all four: "correctly retired (no-op)"
inf-api-txn: NO-LIVE-WRITE (bundles a writer its handler never calls) -- filed, NOT fixed, deliberately
```

**4. Guard B is finally dead in all three copies it hid in.** Andrew retired it 2026-05-08; it was still
RAISING in two daily writers (a 26% drawdown would have stopped `positions_mv` and the roster) and in
`shape_check.py` **under an alias**. All retired. **Test suite: 324 pass + 1 INTENTIONAL RED** (the fork
detector on `inf-api-txn` -- that RED is TRUE and must not be scoped green).

## OPEN -- with owners. NONE are mine.

| # | item | owner | note |
|---|---|---|---|
| 1 | **Lambda-layer consolidation** | CTO~B (scoped, no clock) | The fork produced **two production defects in one day, in opposite directions** (a FIX and a REMOVAL that both never reached the runtime) and **the repo looked correct throughout both**. |
| 2 | **The lib-parity CI covers 0 of 6 live copies** | CTO~B / COO / 0.7.0 | It compares against a path `safe-deploy` never writes, guarding a DEAD artifact no gold script imports, and `aws s3 cp` **cannot see inside a Lambda zip**. **Do NOT fix by adding PAIRS -- the model is wrong; it would go green while blind.** |
| 3 | **`as_of_date`/`snapshot_date` assert a vintage the content does not have** | 0.5.0 (pull = his lane) | **ORION fabricates it** -- every layer of ours is a faithful reporter. **The honest vintage DOES NOT EXIST in the source: no data-layer fix, only a serving-layer detector on value-movement.** Do not "correct" the stamp -- that invents a vintage the vendor never gave us. |
| 4 | **`AUAFIX-L6(b)`** -- automate snapshot-zeroed, retire `aua_overrides.json` | base DS (`0.4.0_DS_ClientPlatform`) | (a) is **DONE and LIVE** (~$3M correction served). **TRAP: the TO's expected `~$365.7M` is a STALE ORACLE** -- served cot AUA is **$435.8M** (the book grew); verifying (a) against it falsely condemns a correct fix. **Strike or re-base it.** |
| 5 | `inf-api-txn` vendored lib | 0.7.0 | Inert (0 live writes). **Filed, not fixed** -- deliberate-or-drift unknown; do not "tidy" it. |

## Blockers

**NONE.** Nothing is waiting on me and I am waiting on nothing.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-surface-check` (auto via safe-commit x19) | PASS | read the output, never the silence |
| `commit-gate.sh` (x10) | PASS | clean on every `.py` touch |
| `comp-pipescript io INF_B_00` | **GAP** | omits the `accounts_v2` READ and the `gold/canonical/holdings` WRITE -- **the roster input at the heart of the SEV is invisible to the tool a DS is mandated to run before editing that script** |
| `comp-constants` (via 0.7.0) | **GAP** | compares **VALUES**, cannot see a **BEHAVIOUR** divergence -- it flagged the inert copy and waved through two live zombies carrying **identical canonical constants** |

**Both gaps are real coverage holes in mandated gates, not one-offs. Filed to 0.7.0 + COO.**

## THE LESSON -- and it is the only thing here I would fight for

**Roughly a dozen of my own instruments failed today. Every one was self-caught. NOT ONE was caught by being
careful.**
```
a docstring   scored as an enforcement      a repo      scored as a runtime
a log line    scored as a guard             a CONSTANT  scored as a behaviour
a comment     scored as a roster read       a NAME      scored as a control
a hash        scored as the columns         "landed"    scored as "reachable"
```
Each was caught by **a control failing**, by **running the arm I had skipped**, or by asking **"why is the
thing I KNOW is broken not in my own output?"** The registry I shipped to hunt zombie guards was itself blind
to a zombie guard **within four hours**.

> **KNOWING A FAILURE MODE BY NAME DOES NOT IMMUNIZE YOU AGAINST WRITING IT.**
> **CARE IS NOT A CONTROL; CARE IS WHAT YOU HAVE INSTEAD OF ONE.**

**And two that cost other people, not me:**
- I **overstated a premise** ("the ONLY columns that differ are the date stamps") **that my own output had
  already falsified.** 0.5.0 nearly reported a false contradiction off my sentence. *A right conclusion on an
  overstated premise is as dangerous as a wrong one -- the next person reasons from the PREMISE.*
- I **refused credit for two findings I did not make.** *A finding misattributed to an agent who does not have
  it is an UNOWNED finding wearing an owner's name* -- and only the person being credited can see it, while
  every incentive says stay quiet.

## Next Steps

1. **[2.0.0_SA_COO]** allocate items 1-4 above; **strike/re-base the `~$365.7M` in `AUAFIX-L6`** before anyone
   reads it as an acceptance criterion.
2. **[1.0.0_SA_CTO~B]** the layer decision, now re-based on two production defects rather than tidiness.
3. **[1.0.0_SA_CTO]** the `-m`-with-backtick PreToolUse gate is **LIVE and it blocked me** -- one refinement
   sent: its match unit is the **compound** command, not the **simple** command (my `-m` body was clean; a `$(`
   in a trailing `echo` tripped it). Fails closed, so ship as-is if the fix is not cheap.
4. **[me]** IDLE, reachable, queue empty. Not touching `aor_resolution.py` (base DS owns P3) or `infra/` (AE).
