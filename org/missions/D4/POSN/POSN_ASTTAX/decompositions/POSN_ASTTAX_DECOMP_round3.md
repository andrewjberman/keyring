# POSN_ASTTAX -- ROUND 3 DECOMPOSITION: make step (2)'s BAR MET, then retag (7 cells)

**Cut by** `2.0.0_SA_COO~Z` (L5) · **2026-09-11** · **PRD** `../prd/POSN_ASTTAX_PRD.md` **v0.5**
@`49ddcc481d`, L4-R **ADMITTED** (ratified-text `3.0.0_SA_CVO~Z` current; brief `4.0.0_SA_CRO~Z`
current -- verified by `prd-signoff.py status` immediately before this cut, not assumed).
**Input:** `../ledger/ROUND_ANALYSIS.round2.md`@`98380c753e` (the L10 read).
**Supersedes** `POSN_ASTTAX_DECOMP_round2.md` -- INVALIDATED by `C-S30..33`
(`DECOMP_INVALIDATING`, `3.0.0_SA_CVO~Z` at L9).

> **WHY A RE-DECOMPOSITION AND NOT A RE-ISSUE.** The choice is the COO's under spine v3 L10 and is
> recorded here: four L9 dispositions are `DECOMP_INVALIDATING`, so the round-2 cell set is not a
> surface to re-cut orders against. Round 2's own premise also moved -- its sequence was built on a
> mechanism now falsified -- so re-issuing its cells would carry a dead frame forward under new order
> ids.

---

## 0. WHAT CHANGED, AND WHY ROUND 3 IS NOT ROUND 2 AGAIN

Round 2's principal output was a **NO-GO**, and that was the round working. `TO-S7-1` measured the
chain and found it does not carry the ratified five-class vocabulary. The PRD has since been
**re-founded on that measurement** (@`49ddcc481d`): the live mechanism is **SILENT ZEROING, NOT
BLANKING** -- a retag today renders `Commodities`/`Structured` as the literal `'Unknown'` and zeroes
the weight. **The hazard got quieter, not safer.**

⛔ **ROUND 3 EXISTS TO MAKE STEP (2)'s BAR TRUE, NOT TO RE-VERIFY IT.** The bar, verbatim from the
re-founded constraint:

> for EVERY ticker in the retag set, the SERVED `asset_class` value equals its ratified five-class
> label AND its allocation weight is NON-ZERO and equal to its pre-retag weight, read from the served
> artifact.

Round 2 could not meet it because nothing had been built to carry five classes. **Round 3 builds
that, measures the bar against the world, and only then retags.**

## 1. THE CELLS -- 7

| cell | what | FWD | source |
|---|---|---|---|
| **`AT3-s-1`** | CARRY FIVE CLASSES THROUGH THE GENERATOR (chain head) | FWD-1, FWD-2 | analysis §1; C-RETAG-SAFETY live mechanism |
| **`AT3-s-2`** | MEASURE THE FRONTEND HOP (the gap S7 disclosed) | FWD-1, FWD-3 | analysis §4.4; `TO-S7-1` disclosure |
| **`AT3-s-3`** | HOP-TEST THE TWO SIBLING CONSUMERS | FWD-1 | analysis §4.4; `TO-S7-1` disclosure |
| **`AT3-s-4`** | REGISTRY DURABILITY -- the re-seed revert | FWD-1 | `W3-S1`; analysis §1, §4.4 |
| **`AT3-s-5`** | **THE BAR** -- step (2) measured against the served artifact | FWD-1, FWD-2 | PRD s.4 step (2) |
| **`AT3-s-6`** | THE RETAG (successor to `TO-S2-1`) | FWD-1, FWD-2 | PRD s.4 step (3) |
| **`AT3-s-7`** | `is_hedge()` RECONCILIATION (successor to `TO-S3-1`) | FWD-1 | round-2 `AT2-s-3`, undispatched |

### `AT3-s-1` -- CARRY FIVE CLASSES THROUGH THE GENERATOR (CHAIN HEAD)
The generator's served output maps hold FOUR keys and `.get(asset_class_raw, 'Unknown')` everything
else, in three places; the allocation `if/elif` chain has **no `else`**, so an unmatched value
accumulates to TOTAL 0.000. Make the served path carry all five ratified classes -- Fixed Income/Cash,
Equity, Structured, Commodities, Alternatives -- so a correctly-tagged ticker renders under its own
label with its weight intact.
⚠ **PARTIALLY MOVED SINCE `TO-S7-1`:** `3.0.0_SA_CVO~Z` records that `AT2-s-1` repaired a benchmark
hop, so the 17/3/14 ratio is HISTORICAL. **This cell re-measures the hop set at its own vintage and
does not inherit that count.**
⛔ Does NOT retag anything. Changes how values are CARRIED, never what any row is tagged.

### `AT3-s-2` -- MEASURE THE FRONTEND HOP
`TO-S7-1` disclosed that the frontend contract hop was **never measured**: `portal/` sat outside the
worker's cone and its census printed `29,577 UNREADABLE`. Its own order named a frontend contract as a
distinct hop class, so "end to end" was never established. Measure whether the portal consumer carries
a five-class value or collapses it.
⛔ **READ-ONLY, AND PORTAL IS FROZEN** (Andrew, both fabrics, PROD and DEV). Reading is not promoting;
this cell reads and reports and changes nothing under `portal/`.

### `AT3-s-3` -- HOP-TEST THE TWO SIBLING CONSUMERS
`yang-generate-allocation-summary` (67 hits) and `yang-generate-holdings-attribution` (32 hits) were
ENUMERATED but never hop-tested. `TO-S7-1` declared the shared-shape assumption as INFERENCE, not
measurement. Test them.

### `AT3-s-4` -- REGISTRY DURABILITY: THE RE-SEED REVERT
`seed-etf-classifications.py` does an unconditional full-item put and the six commodity tickers are
absent from `ETF_MANAGEMENT_STYLE` in all three module copies, so a seed run reverts `AT2-s-5`'s six
writes **and any retag**. Make the registry hold its values against a re-seed.
⚠ Trigger is LATENT, not absent (`Z-S4`: 111 refs / 56,445 files, the one gold-producer candidate
references it in COMMENTS only, `CODE=0`). A manual run still reverts.
⚠ **MEASURE THE WORKTREE, NOT JUST HEAD** -- `seed-etf-constituents.py` carries uncommitted bytes
preserved at `5c9e329a21`, and the difference is invisible unless you look.

### `AT3-s-5` -- THE BAR (GATES THE RETAG)
Measure step (2) as the CONDITION the PRD now states, against the SERVED artifact, for EVERY ticker in
the retag set: served `asset_class` == its ratified five-class label, AND weight NON-ZERO and equal to
its pre-retag weight.
⛔ **THIS CELL RECORDS A CONDITION, NOT A TASK COMPLETION.** Its verdict is GO only if the bar holds
for every member; "the harness ran" is not a result. A completed verification cell is not a passed one.

### `AT3-s-6` -- THE RETAG
Move the retag set to its ratified five-class labels. **Successor to `TO-S2-1`, which was never run.**
⛔ **ITS ACCEPTANCE CRITERION MUST FAIL IN THE BROKEN WORLD.** `S2-AC5` said "confirm the page still
renders" -- which returns the SAME observation in the healthy world and the broken one, and would have
produced a PASS over a live regression. The replacement asserts the **SERVED VALUE and the WEIGHT** for
each retagged ticker.
⚠ VXX is the entire live blast radius -- the only held member of the retag set.

### `AT3-s-7` -- `is_hedge()` RECONCILIATION
Successor to the undispatched `TO-S3-1`. The module documents a three-value vocabulary, assigns `other`
to zero tickers, and uses an undocumented `hedge`, so `HEDGE_TICKERS` is empty and `is_hedge()` returns
False for tickers whose class IS hedge. Reconcile after the retag has settled the vocabulary.

## 2. DEPENDENCY CHAINS (the input to L6's `fanout:`)

```
  A:  AT3-s-1  ->  AT3-s-5  ->  AT3-s-6  ->  AT3-s-7      (build, measure the bar, retag, reconcile)
  B:  AT3-s-2  ------------->  AT3-s-6                     (frontend hop measured BEFORE the retag)
  C:  AT3-s-3  ------------->  AT3-s-6                     (sibling consumers measured BEFORE the retag)
  D:  AT3-s-4                                              (independent -- registry durability)
```
**FOUR chains.** `AT3-s-6` has THREE unmet predecessors and is the convergence point: the retag does
not fire until the bar reads GO **and** both previously-unmeasured consumer paths are measured.
⛔ **B AND C GATE THE RETAG DELIBERATELY.** Both "can only strengthen a NO-GO" -- but an unmeasured hop
must not travel as though it were measured, and the retag is the irreversible act. Measuring after it
would be measuring the wrong world.

## 3. FOUR-POSTULATE RECORD (Rule 24)

**(i) MECE over a DECLARED domain, by SUBTRACTION.** Domain: *everything that stands between the world
as measured at* `49ddcc481d` *and (a) step (2)'s bar reading MET, plus (b) the round-2 carry-forwards
discharged.* Enumerated as the printed remainder, not a forward list:
```
  the served path does not carry 5 classes ......... AT3-s-1
  the frontend hop is UNMEASURED ................... AT3-s-2
  two sibling consumers are UNMEASURED ............. AT3-s-3
  the registry does not survive a re-seed .......... AT3-s-4
  the bar itself is unmeasured at the new vintage .. AT3-s-5
  the retag has not happened ....................... AT3-s-6
  is_hedge() is unreconciled ....................... AT3-s-7
  ------------------------------------------------------------
  7 members declared MINUS 7 covered = 0 UNCOVERED
```
⚠ **DOMAIN CHOICE IS ITSELF A CLAIM AND IS STATED SO IT CAN BE FALSIFIED:** the domain is bounded by
step (2) + the round-2 carry-forwards. It deliberately EXCLUDES anything needed to grade an FWD
REALIZED, because no FWD can be realized without a surface a person has used, and no such surface
exists yet (analysis §2). A member outside that boundary VOIDS this subtraction -- say so rather than
fold it in silently.

**(ii) SAME GRAIN.** Every cell is one worker-sized act against a named artifact. `AT3-s-5` is a
MEASUREMENT cell and `AT3-s-6` an ACT cell -- the split is deliberate and is the lesson of round 2,
where one cell held both and the measurement's NO answer had nowhere to go.

**(iii) INTENT COHERENCE.** One axis: *make the five-class vocabulary survive the whole served path,
then move the rows.* No cell both builds and grades its own build.

**(iv) STATE COHERENCE -- what these cells do NOT move.** They do not touch holdings, weights or
satellite placement (VXX already flows correctly via the MODELS path; POSN retags only the served
top-level `asset_class`). They do not promote portal. They do not close any FWD. They do not make
`is_hedge()`'s wider vocabulary question a design ruling -- `C-S1` graduated that to the CTO and it
stays there.

## 4. WHAT THIS ROUND DOES NOT DO

- **No FWD is expected REALIZED.** Round 1 graded 0 of 6, round 2 graded 0 of 6, and both were correct:
  this is pre-surface correctness work. Grading an FWD here would be the claim, not the work.
- **No portal promote.** Frozen, both fabrics, until Andrew names it.
- **No new vocabulary.** The five classes are ratified; nothing here mints a sixth.
- **LD-0521 is not amended.** Andrew's routing exception for round 2 was a single named case and this
  round carries no precedent from it.

## 5. THE TWO UNRUN ROUND-2 ORDERS

`TO-S2-1` and `TO-S3-1` remain `staged` and UNRUN and are NOT cancelled or superseded by this cut.
`AT3-s-6` and `AT3-s-7` are their SUCCESSORS -- the need survives, re-founded on the measured mechanism
and with discriminating criteria. When their successors land terminal, those two orders finally have a
real pointer and can be dispositioned honestly.
