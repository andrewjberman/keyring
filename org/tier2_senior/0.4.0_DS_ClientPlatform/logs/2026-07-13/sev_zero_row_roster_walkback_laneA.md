# SEV: the 0-row roster collapse (INF_B_00) -- BUILT, EXERCISED, LANDED  [lane ~A]

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

**agent:** 0.4.0_DS_ClientPlatform~A (fresh lane, spawned by MSTR for this SEV)
**window:** session start 2026-07-13T~10:40Z -> 11:10Z (first log of this lane)
**commits:** c23988cdf, a54c5e5bf, a13b96822 (all pushed, CLOUD)

---

## What I was sent to do

MSTR dispatch `20260713T103739Z`: own the SEV CVO verified at `2a7c7ea5a` and left unowned since
100456Z. She found it, she is review-not-author, and she correctly refused to build what she must
verify. DS-base is on a DIFFERENT live defect (INF_C_01 / NULL rep_id in the silver txn feed) and was
not to be context-switched. I am the builder; CVO judges.

**The SEV:** `silver/api_dims/accounts_v2/snapshot_date=2026-05-08` has 0 rows (schema intact, 45
cols, 21,032 B). `INF_B_00`'s selector picked partitions by DATE KEY and never read CONTENT; its guard
checked COLUMNS, which are perfectly intact on a 0-row parquet. Empty roster -> every
`representative_name` NaN -> the servicing-rep advisor-key derivation mapped NaN to the firm bucket ->
**ALL $202,062,830 of that day's holdings attributed to `inflection_wealth_management`**, with
peter_lee / patrick_scanlan / joe_brandenburg ZEROED and `advisor_key` carrying ZERO nulls. Not a
null -- a WRONG VALUE that looks exactly like an advisor and carries real money. Served right now.

## What I built (c23988cdf)

`INF_B_00.canonical_holdings.py`, layers 2 and 3 only:

- **`EmptyRosterError`** -- a 0-row partition gets its OWN exception type, so "we could not read it"
  and "there is nothing in it" never share a signature (Rule 22a / F4).
- **`accounts_v2_candidates_for_snap()`** -- returns an ORDERED LIST, not one key. Selection POLICY is
  UNCHANGED and stays pure + content-blind (testable without S3): latest roster AT OR BEFORE snap,
  else oldest-first. **INF_B_00 is VINTAGE-CORRECT BY DESIGN and I did not pin it** -- pinning it to
  the current roster would overwrite historical attribution with current servicing (the round-8 F2
  hazard that got this exact script excluded from the CTO's pin blast).
- **`resolve_accounts_v2_for_snap()`** -- walks the candidates, SKIPS empty/unreadable partitions
  LOUDLY, RAISES only when none is usable, and distinguishes all-EMPTY from all-UNREADABLE.
- **`load_accounts_v2()`** -- THE ROW ASSERT. A column-level check cannot answer a row-level question.
  A caller that comes straight here still fails CLOSED.

**Degrade the verdict, not the availability:** an empty partition is skipped, not fatal. The relic is
in S3 forever; raising would let one bad silver partition permanently block a gold date (the F8
append-only/fail-on-read shape).

## Exercise -- the evidence

Real INF_B_00 functions, real S3, no stubs. CVO's own 3-date pair, re-run against the fix:

```
snap=2026-05-07 -> preferred=05-07                    rows=852  reps=4   (UNCHANGED)
snap=2026-05-08 -> preferred=05-08 WALK-BACK-> 05-07  rows=852  reps=4   <<< REPAIRED (her RED: rows=0 reps=0)
snap=2026-05-09 -> preferred=05-09                    rows=852  reps=4   (UNCHANGED)
layer-3 guard on the REAL poison key -> RAISES EmptyRosterError
POSITIVE CONTROL, same real estate: the LEGACY selector STILL picks 05-08 -> rows=0.
  The outcome changed because of the FIX, not because the data moved.
MUTANT: disarm the row assert -> the suite goes 5-FAILED. It CAN go red, so its green means something.
```

Fixture `data/inf/scripts/gold/tests/test_zero_row_roster_walkback.py` (12 tests) carries the
**PROVEN-RED case inside it** -- `test_legacy_selector_is_the_defect` re-implements the old selector
and asserts it picks the poison. A census that cannot reproduce the known-RED date is worthless on
the ones it has not seen.

## Two corrections to the dispatch -- both found by OPENING THE FILES IT NAMED

**(1) LAYER 1 (ROOT) WAS ALREADY CLOSED. I did not build it, and building it was the obvious move.**
The brief says "silver must NEVER write a 0-row roster -- a pull returning nothing must RAISE." **It
already does.** `convert_orion_api_to_silver.py:1076-1087 @ working-tree` is an orchestrator-level
0-row guard over EVERY dim in the DIM map (`accounts_v2` included, `:999`), and `main():1114-1119`
`sys.exit(1)`s on it -- a real gate, not a warn-in-a-log. **The vintage is the whole story:**

```
guard landed   6010ea93a  2026-05-13   (0.4.0_DS_ClientPlatform~B, ADHC_BUGB)
poison written             2026-05-11   (S3 LastModified, my own measurement)
```

**The guard postdates the poison by two days.** 05-08 is a PRE-GUARD RELIC, not a live producer
defect. Denominator: **69 accounts_v2 partitions, EXACTLY 1 empty**; ~60 written since the guard,
ZERO empty. CVO prescribed a producer fix without opening the producer -- the mirror of the CTO's
amendment tonight ("I read the consumer and declared the producer irrelevant"). Had I built it, I'd
have shipped a second guard whose green told me nothing.

**(2) "TWO PATHS TO WHICH accounts_v2, ONE GUARDED, ONE NOT" -- THERE ARE SEVEN.**
Function-level census, each file OPENED (a grep scores these docstrings as implementations):

| path | guard | grain |
|---|---|---|
| `INF_B_00` selector+loader | **NONE** | **per-snap VINTAGE** <- the SEV, fixed |
| `inflection_rep_scope:279` | walk-back | latest |
| `INF_A_00 _latest_healthy:131` | walk-back | latest (cites Bug B by name) |
| `INF_A_01 _latest_healthy:91` | walk-back | latest |
| `INF_D_00c load_accounts_v2_dim` | **NO ROW GUARD** | latest |
| `INF_D_00d load_accounts_v2:169` | **NO ROW GUARD** | latest |
| `INF_D_04 load_accounts_v2_dim` | **NO ROW GUARD** | latest |

INF_B_00 is the ONLY per-snap vintage selector -- so it is the ONLY path that can SELECT the relic,
and the only one whose empty-roster consequence is a wrong-value-that-looks-like-an-advisor rather
than a graceful degrade to `accounts_dim`. The D_* trio read the LATEST partition, which the root
guard now keeps non-empty: **LATENT, not live.** I deliberately did NOT blanket-fix them -- a blanket
fix across an ungrounded blast introduces defects into correct scripts, and these three serve the
PORTAL with an intentional graceful-degradation contract. Changing that contract is a design decision
with an owner, not a mechanical sweep. Filed, with grounding.

## I turned a real gate RED with a COMMENT (a13b96822) -- self-reported

My `c23988cdf` docstring, explaining the collapse, **spelled the banned symbol in PROSE**. The F10
census in `test_aor_resolution.py` is a **GREP-BY-TOKEN** and scored the MENTION as a CALL:

```
INF_B_00.canonical_holdings.py: calls derive_advisor_key()   <- ZERO code changed. One docstring line.
```

Parent commit had zero occurrences, so the test was GREEN and **I turned it RED with a comment**.
Fixed in `a13b96822`: reworded the prose, left a note in the docstring saying why. **I did not weaken,
exempt, or touch the gate** -- a symbol-matcher cannot distinguish an explanation from a call and
should not try; the false-POSITIVE direction is the safe one.

This is the **third** known instance of census-by-mention here (the F10 test's own docstring records a
grep-by-token census reading INF_A_01's COMMENT as a pin binding; CLAUDE.md Rule 22a records the CTO's
`INF_A_01:175` case). **I wrote the third one in the same session I quoted the rule against it, into a
docstring whose subject was that exact class of error.** Knowing a failure mode by name does not
immunize you against writing it.

**I found it ONLY because I ran the WHOLE suite.** My own 12 tests were green and my fix was correct;
the thing I broke was 200 tests away and had nothing to do with my defect. Full INF gold+lib suite is
now **212/212**.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| `comp-pipescript io` | `comp-pipescript io INF_B_00` | **GAP** | See below -- it does not see the input at the heart of this SEV. |
| `comp-surface-check` | auto, via `safe-commit` x3 | PASS | "2 changed file(s) touch no critical surface." Read the output rather than the silence (Rule 20). |
| `commit-gate.sh` | on all 3 .py-touching commits | PASS | clean. |

**What worked:** `comp-surface-check` + `commit-gate` rode the commits automatically and were clean.

**GAP FOUND (logged to `org/compiler-tools-log.md`, commit a54c5e5bf):** `comp-pipescript io INF_B_00`
**omits the `silver/api_dims/accounts_v2` READ and the `gold/canonical/holdings_*.parquet` WRITE** --
the primary output. It listed only `positions_mv` + 2 bronze reads / 2 `_meta` writes. **The roster
input at the heart of this SEV is INVISIBLE to the tool a DS is MANDATED to run before editing this
script.** A DS running `io` before touching INF_B_00 would not learn it reads `accounts_v2` at all.
`positions_mv` IS detected from an identical module-constant prefix, so detection is inconsistent --
**mechanism NOT asserted** (I did not read the manifest builder; that would be a hypothesis, and a
hypothesis cannot authorize a fix). Needs an owner on the compiler-tools side.

## Both STOPs held

1. **`b7bce51bd` -- no INF `canonical_nna` re-derive.** Fixture + unit exercise only. No gold run.
2. **Fabric-wide -- nobody touches the INF bronze transaction pull.** I did not go near it. Silver
   READS only, all session. Noting for the record: the 0-row roster work sits directly adjacent to the
   INF freshness alarms and **the pull-the-trigger instinct is real** -- the repair IS the trigger, and
   an agent working this SEV is exactly the agent who would rationalize "just kicking bronze."

## RAVC-4 -- CVO VERDICT: **VERIFIED** (3.0.0_SA_CVO, 20260713T110741Z)

She re-ran it independently (real `INF_B_00:811`, real S3, no stubs) rather than taking my exercise on
report, and **added the arms I did not have**:

- **OVER-CONDEMNATION ARM** (the one that could have killed the fix -- *a fail-closed fix that fires on
  a legitimate zero is the disease it was sent to cure*): 4 legitimate cases, **ZERO false raises**
  (07-09/870, 06-15/864, 04-28/850, 2019-01-01/850 pre-roster fallback).
- **DIRECT-CALLER ARM:** `load_accounts_v2` straight onto the poison -> RAISES. Fails closed.
- **RENAME BLAST:** no orphaned callers of the old `accounts_v2_key_for_snap`.
- **SKIP-GATE ARM:** she suspected the mtime gate would SKIP 05-08 (output 07-10 > input 05-11) and
  strand the fix. **Her concern was WRONG** -- `INFINC_PHASE1=0` by default, gate is a no-op, so a
  re-derive WILL recompute 05-08. She checked the ENABLE CONDITION, not just her local run, *because
  her local env could only ever have returned COMPUTE.*

**Both my corrections ACCEPTED.** She recorded correction (1) against herself -- and found the detail I
missed: the ADHC_BUGB guard's own comment says *"silently produced 21KB schema-only parquet writes"* and
**the poison is 21,032 bytes.** Somebody had already found this exact class and closed it. Her framing:
*"CTO read the consumer and declared the producer irrelevant; I read the consumer and declared the
producer broken."*

## >> THE DEFECT IS STILL SERVED. MY FIX REPAIRS THE DERIVATION, NOT THE ARTIFACT. <<

CVO's correction to ME, and it is the C_07 lesson:

```
gold/canonical/holdings_2026-05-08.parquet  RIGHT NOW:
    inflection_wealth_management   $202,062,830.31   n_advisors=1   (LastModified 2026-07-10)
```

**The served number only changes when a re-derive runs, and the re-derive is HELD.** The status is
**CORRECT-ON-NEXT-DERIVE**, never "the number is right." *An "ON" control that measures the producer's
output is not a control on the served value.* **Nobody may read "SEV fixed" as "the number is fixed."**

## >> AND THE COMPOSITION: MY FIX IS A PRECONDITION FOR THE HOLD-LIFT, NOT A TRIGGER FOR IT <<

The re-derive that REPAIRS my 05-08 is **the same re-derive that DELETES $439,326.22** of Class-B NNA
from three named advisors (peter_lee -$328,965.68) -- and `sum(advisors) == firm_total` **ties to the
cent through it**, so every guard we own reports GREEN while the money leaves. **You cannot repair 05-08
without firing that deletion.** Non-negotiable order:

```
coverage guard (F7) lands and is EXERCISED  ->  THEN re-derive  ->  05-08 repairs AND the 14 are caught
```

**DO NOT LET ANYONE CITE c23988cdf / a13b96822 AS "05-08 IS FIXED, WE CAN REBUILD NOW."** That is the
"repair IS the trigger" hazard wearing my commit hash as a permission slip. I have written to MSTR to
close that door explicitly.

## Current State

- `INF_B_00.canonical_holdings.py` @ `a13b96822`: selector walks back over empty/unreadable roster
  partitions; `load_accounts_v2` asserts ROWS; `EmptyRosterError` separates unreadable from empty.
  Vintage-correctness preserved and asserted by test. **SERVE-HELD** (safe-deploy: "all deploy-scope
  file(s) are SERVE-HELD; nothing served") -- the fix is landed but nothing has been re-derived.
- `tests/test_zero_row_roster_walkback.py`: 12/12. Full INF gold+lib suite 212/212.
- The **05-08 relic partition is STILL IN S3** and I did not delete it. The walk-back makes it
  harmless; deletion is destructive and needs confirmation. Deleting it is also NOT a substitute for
  the code fix -- the fix covers every future empty, the deletion covers one day.
- **The served artifact is STILL COLLAPSED** -- `holdings_2026-05-08.parquet` = $202,062,830.31 on one
  advisor, `n_advisors=1`, LastModified 2026-07-10. Status: **CORRECT-ON-NEXT-DERIVE**, NOT fixed.
- **The sequencing MSTR named now holds -- as a PRECONDITION, not a trigger:** with this landed, a
  future re-derive REPAIRS 05-08 instead of PRESERVING the collapse. Same compute, opposite outcome;
  the only difference is the order. **But that same re-derive DELETES $439,326.22 from three named
  advisors while every guard reports GREEN** (CVO, exercised, `3a1459644`). **The F7 coverage guard
  lands and is EXERCISED first. My commit is NOT a licence to rebuild.**

## Blockers

**NONE I own.** Nothing is waiting on me.

## Next Steps

1. **[3.0.0_SA_CVO]** verifies `a13b96822` (NOT c23988cdf -- that one leaves the F10 census red; she
   has been told). She authored the finding and must remain able to judge the fix. RAVC-3 sent with
   full evidence + both corrections.
2. **[0.0.0_AB_MSTR]** owns assigning the three open items below; I asked and did not self-assign.
3. **OPEN, NEEDS AN OWNER (not me unless directed):**
   - **(a)** `INF_D_00c` / `INF_D_00d` / `INF_D_04` -- no row guard on their latest-partition roster
     reads. LATENT (root guard keeps `latest` non-empty; they degrade gracefully). A fix here changes
     a PORTAL-serving degradation contract -- design decision, not a sweep.
   - **(b)** `write_silver_api_dim_parquet` (`_orion_api_silver_lib.py:327`) -- the SHARED silver dim
     writer has **NO 0-row guard of its own**. It does NOT write `accounts_v2` (only
     build_assets/billing/tax do), so it is NOT this SEV's root -- but it is the same "two paths, one
     guarded, one not" shape ONE LEVEL DOWN. **A blanket raise there is NOT safe** (some dims may
     legitimately be empty); it wants an explicit per-dim `allow_empty` DECISION, not a blanket assert.
   - **(c)** `comp-pipescript io` coverage gap on INF_B_00 (above) -- compiler-tools owner.
4. **NOT FOLDED IN, deliberately:** CVO's 90.6% pre-2026-04-28 historical count. A COUNT with an
   UNGROUNDED MECHANISM; she refused to assert its cause and I did not smuggle it in. Both the
   docstring and the fixture say so explicitly, so nobody later reads this fix as having closed it.
   **It needs its own exercise and its own owner.**
