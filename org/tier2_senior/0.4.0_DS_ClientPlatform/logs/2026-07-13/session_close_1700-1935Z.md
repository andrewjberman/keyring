# DS ClientPlatform — SESSION CLOSE 1700-1935Z: the observe run that stopped the serve, twice

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, IMPLEMENT

Prior log: `aor_stamp_aware_fold_and_change3_blocker_1503-1700Z.md` (85446ff61).

---

## THE HEADLINE

**Andrew ordered the time-lock served. It was stopped twice, and both stops were invisible from
where everyone else was standing.**

**STOP 1 — the chain could not run at all.** I executed the DEPLOYED BYTES instead of reasoning about
them. `INF_C_01` dies at `_normalize_silver_schema:512` -> `load_resolution()`: the AoR SSOT
`gold/dimensions/aor_resolution.parquet` **had never existed** — INF_A_0 had never run. It kills
`--dry-run` too (the read is in the DERIVATION, not the write). **The GO would have thrown a
RuntimeError, served nothing, and been read as THE TIME-LOCK FAILING** — after Door 5 and the hold had
been spent to get there. *A loadable file is not a runnable one.*

**STOP 2 — the first stamp would have frozen the DEFECT.** With the SSOT created (CTO-authorized) the
time-lock ran across **1,389 partitions**. Measured against current gold, **same denominator**:

```
peter_lee            104,318,087.60 -> 104,318,087.60    DELTA 0.00
patrick_scanlan       13,947,755.04 ->  13,947,755.04    DELTA 0.00
joe_brandenburg       12,564,418.50 ->  12,564,418.50    DELTA 0.00
inflection_wealth_mgmt 1,780,492.91 ->   1,780,492.91    DELTA 0.00
inflection_unmapped_rep   52,604.80 ->      52,604.80    DELTA 0.00
                                                     *** NOTHING MOVES ***
```
The lock restores nothing on run 1 (nothing was stamped before) and the AoR fold — which performs the
CORRECTION — is a NO-OP (0 movers; `advisor_of_record_raw` lands 07-14 13:22Z). **The stamp is IMMUTABLE
by my own design: the stamp-aware fold REFUSES to re-key a stamped row.**

> **SERVE TONIGHT -> TOMORROW'S FOLD CAN NEVER CORRECT HISTORY. MY OWN FIX WOULD CEMENT THE DEFECT IT
> WAS BUILT TO UNDO.** *FOLD, THEN LOCK. Tonight is LOCK-WITHOUT-FOLD — the one ordering never on the table.*

**FIRM TOTAL: PASS, to the cent.** And I nearly false-alarmed on it: the observed SUM is over the 1,389
REWRITTEN partitions; gold has 1,410. The 21 untouched hold **exactly $444,308.79**;
`132,663,358.85 + 444,308.79 = 133,107,667.64`. **A denominator, not a bug — established BEFORE escalating.**

---

## THE TRAP (COO retracted his own clearance on it)

The ONLY reason nothing was stamped is `assert_no_residual_advisor` firing on the phantom
(`inflection_unmapped_rep`, $52,604.80 — Patrick's money).

```
DEPLOY THE SILVER RESCUE ALONE (phantom dies) WHILE THE FOLD IS STILL A NO-OP
   -> residual guard GREEN | coverage GREEN | firm total ties to the cent GREEN
   -> AND THE WRONG HISTORY IS STAMPED, PERMANENTLY, WITH EVERY CONTROL PASSING.
```
**The phantom is LOAD-BEARING. The defect is currently the only thing protecting us.** COO had cleared
Patrick's fix as "not blocked by the freeze" (collision axis) and retracted it: *a fix that removes the
symptom a guard is watching for is a guard deletion wearing a bug report.* Freeze is now TWO-AXIS.

## AND THE CURE MUST PASS THROUGH DOOR 5 — TWO LOCKS, TREATED AS ONE

`orion-gold-dispatch.sh:508` `sync_scripts()` flattens FOUR prefixes (`code/gold|manual_api|silver|bronze/`)
into one dir keyed by basename and FAILS LOUD on collision. `:292` `INF_API_SILVER_TXN |
convert_transactions_to_silver.py` — **Patrick's rescue is a DISPATCH STEP, in NO Lambda package.
`sync_scripts()` is the ONLY consumer of `code/silver/` — and it is the thing FATAL-ing.**

```
Patrick's money <- silver re-derived w/ rescue <- rescue in code/silver/ <- sync_scripts() SUCCEEDS
                <- basename collisions RESOLVED  <- *** DOOR 5 ***
```
> **THE COLLISION IS NOT THE HOLD.** CHOKEPOINT (`RELEASE=None`) = DELIBERATE, the real control.
> COLLISION (`sync_scripts()` FATAL) = ACCIDENTAL, a guard refusing a forked tree — which ALSO blocks the
> cure. **"Do not de-collide" was right while it was a TIDY-UP. It cannot be permanent policy: THE FIX
> MUST PASS THROUGH THAT DOOR.** De-collide as part of the GATED release, chokepoint still held. Never as
> a cleanup. *(Collision #2, `_orion_api_silver_lib.py`, is MINE — 12:48Z. I built half the wall in front
> of the fix I authored.)*

---

## WHAT I RAN (CTO-authorized OBSERVE path; both hard STOPs cleared at source first)

| gate | result |
|---|---|
| STOP 1: does INF_A_0 read the dead txn feed? | **CLEARED** — `transactions` = 0 hits in BOTH resolver modules (positive control: `accounts_v2` = 38 and 32). Reads `silver/api_dims/accounts_v2/` only. |
| STOP 2: does the SSOT write fire a serve? | **CLEARED** — enumerated EVERY trigger on the bucket; the resolver's 3 write-keys match NONE. (0.7.0 independently ran a 133-rule census; agreed.) |
| **INF_A_0 — FIRST RUN EVER** | 873 accounts, fold OFF, 0 movers/0 explicit, `unresolvable_rep=0 / unmapped_rep=0 / null=0`, 873 ledger events, `first_run=True`. Pre-write check: both keys ABSENT (a CREATE). Verified by `head-object`. |
| `INF_C_01 --out-prefix scratch/...` | SCRATCH banner fired; 1,389 partitions stamped; `0 OBSERVED / N BACKFILLED` on every one; **residual guard RAISED and refused the write**. |

`INF_AOR_ASOF=2026-07-13` / `INF_AOR_SRC_ETAG=f3cf244d...` pinned using **THE DISPATCH'S OWN DERIVATION
COMMANDS** (`:1390-1393`, `:1426-1428`), not mine — the resolver correctly REFUSED to fabricate a
wall-clock as-of (R1b).

**Numbers obtained WITHOUT weakening the guard:** wrapped `assert_no_residual_advisor` to print the
`advisor_amounts` it was handed, then called **THE REAL GUARD**, which still raised. *A number bought by
silencing the control that was right is worth less than no number.*

---

## COMMITS

| commit | what |
|---|---|
| `f99d67524` | `--out-prefix` — **"run the derive to a SCRATCH prefix" WAS NOT A THING THIS SCRIPT COULD DO.** Only modes were `--dry-run` (no artifact) and `--upload` (**PRODUCTION gold — the irreversible stamp**). The natural way to comply would have stamped 1,410 partitions. Default stays production (nightly DELTA-0); production ANNOUNCES ITSELF before every write. Deployed + verified on the runner. |
| `e3ec94f5b` | LEG-2 SPLIT-BRAIN GUARD (see below) |
| `c7009f308` | `.isdigit()` dropper in FOUR scripts, I had fixed ONE. One function, four callers, floor inside. |
| `5d948e352` | the 318 -> 0 universe-collapse floor, mutant-verified |
| `063101397` | COO's slug question answered by exercise |

## THE LEG-2 NEAR-MISS (holdings book, caught pre-apply)

Running 0.7.0's MIRROR PASS (he held his canary on my probe bug): deployed `inf-api-positions` **writes**
`bronze/positions/{d}.parquet` and **reads** `.parquet`; the REPO writes/reads `.jsonl.gz`. **Both worlds
self-consistent; LEG-2 landed in the repo and never shipped.** Put the canonical converter in a layer and
**the same lambda writes one format and reads the other, in one invocation** -> `NoSuchKey` -> positions_mv
dies -> `INF_B_00`'s served AUA goes stale. `.jsonl.gz` has not existed since 07-10; the 2,265-object
historical backfill is a **RED HERRING** (a spot-check on an OLD date PASSES; only TODAY's key is missing).
**A reach-set census cannot see it: `build_positions_mv` executes in BOTH worlds — it just reads a
different string.** Guard shipped (3 arms; diagnoses the split brain, says plain "bronze absent" when
NEITHER exists, still reads 33,760 rows on 07-10). **I did NOT revert the template** — that would un-land a
correct migration to make a symptom go away. LEG-2 is an ATOMIC PAIR.

---

## COMPILER TOOLS

| tool | use | result |
|---|---|---|
| `comp-grep` | callers of `canonicalize_advisor_of_record`; `sync_scripts`; `code/silver` consumers | **PASS** — and it remains the only searcher that can see `data/*/scripts/gold/lib/` |
| raw `rg` / native `Grep` | same | **FAIL** — false zero on the whole directory (root `.gitignore:47` `lib/` -> `**/lib`; git honours the `!` whitelist, ripgrep does not) |
| `safe-commit` / `safe-deploy` | 5 commits; INF_C_01 -> `code/gold/` | PASS (gate PASS, verified on the deployed bytes) |
| raw `aws s3 ls code/` | collision audit | **GATED by the rail** — no comp-tool models *same-basename-different-content ACROSS prefixes*; re-ran via boto3 |

**Gap found:** `comp-pipescript deployed` reports MATCH/STALE/MISSING per script — it does **not** model a
**basename collision across `code/` prefixes**, which is the exact condition `sync_scripts()` FATALs on and
the cause of a 3-day bronze outage + the gold hold. **That is a real coverage gap in the mandated tool.**

---

## MY OWN INSTRUMENTS THAT LIED (this window)

1. **A `$5,197,081.79` "_IWM misattribution" blocker — REPORTED TO THE COO, THEN RETRACTED.** I measured
   with `derive_advisor_key()`; the code calls `canonicalize_advisor_of_record()`. **Two paths to one fact,
   and I cited the one the code does not use** — verbatim the CTO's error from 8h earlier. The mapping was
   already closed: **0/837 unexpected.** Caught by EXERCISING the function to prove a *different* claim.
2. **"HARD RAISE, the chain stops" — read from a DOCSTRING.** The code alarms and serves. Fixed (`8fc930f21`).
3. **My "de-duplication" nearly switched two probes onto the WRONG DIM** (accounts_v2 295 households ->
   household_rep_mapping 318). **Ruff's `F841 unused variable 'df'` was the only thing that caught it — the
   orphaned read WAS the source I had bypassed. THE LINT WAS THE CONTROL.** *Share the floor, not the source.*
4. **A census-by-mention** (`grep -q canonical_nna_`) scored `INF_C_01` as exposed when it folds fresh txns —
   twenty minutes after I warned COO about mention-censuses.
5. **`AOR_FOLD_ACTIVE=1`** when the var is `INF_AOR_FOLD_ACTIVE` — my "ON" run was silently OFF.

**Every one self-caught. None by a reviewer. Not one by being careful — each by a control that could say NO.**

---

## CURRENT STATE (verified on live primitives, not recollection)

```
scratch/timelock_observe_20260713T1912Z/  -> 0 objects    NOTHING WRITTEN
gold/canonical/canonical_nna_2026-07-13   -> 0 objects    PRODUCTION UNTOUCHED
platinum/firm/advisor_nna_canonical.json  -> LastModified 2026-07-10T14:49:58Z   SERVED SPINE UNTOUCHED
gold/dimensions/aor_resolution.parquet    -> 12,006 B     THE SSOT (created tonight, CTO-authorized)
gold/dimensions/aor_ledger/events/20260713T191144705Z.parquet -> 873 events
```
- **Chain HELD** (chokepoint `RELEASE=None`). **Both basename collisions INTACT — I did not tidy mine.**
- **`code/gold/` + `code/silver/` FROZEN** (COO, two-axis: collisions AND "does this turn a RED guard GREEN?").
- `INF_C_01` on the runner has `--out-prefix` (deployed, 4 markers, safe-deploy gate PASS).
- Time-lock wired + verified on 1,389 partitions. `INF_AOR_FOLD_ACTIVE=0`.

## NEXT STEPS

1. **[1.0.0_SA_CTO + 2.0.0_SA_COO]** **STEP 4 IS THE ONLY THING NEEDING A DECISION:** resolve BOTH basename
   collisions as a **DELIBERATE, CO-SIGNED act with the chokepoint STILL HELD**. Never as a cleanup.
2. **[0.4.0_DS]** **07-14 after 13:22Z:** re-measure the **164-mover** prediction **AGAINST THE ROW**, not the
   roster (my pre-registration is off today's roster x today's accounts_v2 — right PATH, wrong BYTES).
3. **[0.4.0_DS]** Then: silver rescue -> fold ON -> **FOLD, THEN LOCK** -> stamp THE RIGHT ANSWER. One run.
4. **[0.7.0_AE_CloudOps]** LEG-2 is an ATOMIC PAIR (producer + converter). Layer canary stays HELD.
5. **[1.0.0_SA_CTO]** `.tools/deploy-import-lint.py` is PRESENT BUT NEVER INVOKED (0 refs in safe-deploy;
   positive control: `aws` x12 in the core). Blast radius spans firms — not mine to wire.

**Memory banked (survives the session):** `project_timelock_stamp_order_trap.md` (HARD STOP + the trap +
Door 5 dependency), `project_aor_golive_blocked_on_undeployed_change3.md` (07-14 trigger),
`project_leg2_split_brain_positions_bronze_format.md`.
