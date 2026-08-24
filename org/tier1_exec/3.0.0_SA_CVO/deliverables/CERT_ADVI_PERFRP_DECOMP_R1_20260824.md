# CERT — ADVI_PERFRP stage-3 decomp, round 1

**Certifier:** `3.0.0_SA_CVO` · **Requested:** COO 66452 · **Subject:**
`workflows/atom_decomposition/runs/advi-perfrp/20260824T201222Z/DECOMP.md` @`1ce9b2d6bc`
**Date:** 2026-08-24 ~20:25Z · **LOCAL at cert time** (rides integration; stated, not called landed).
**Bar:** the one I stated BEFORE COO authored (66357/66358), unchanged by the dispatch order.
**Alternate post-invalidation signer:** base `1.0.0_SA_CTO` only (CRO class excluded, Andrew-direct ~19:3xZ).

## VERDICT

**CERTIFIED on the ENUMERATION. 36 of 36, both symmetric differences EMPTY, every arithmetic claim
closes, s.11 mapped 14/14 in both directions. No P1. No correction owed.**

**This is the cleanest decomp I have certified this session, and the reason is mechanical, not
stylistic: COO ran my instrument against their own file before sending it** (`grep -o` control 36/36
pre-commit, stated on the face). The bar was published before authoring, so meeting it cost nothing —
which is the whole argument for pre-stating a bar.

## MECHANICAL — measured at this seat

| | measured by me | COO stated |
|---|---|---|
| cells declared (leading table cell, markup-stripped) | **36** | 36 |
| by surface | **inv 6 · a 6 · b 7 · c 3 · d 8 · e 1 · f 1 · g 4** | identical |
| declared duplicates | **EMPTY** | — |
| **mentioned-but-not-declared** | **EMPTY** (see the instrument note) | — |
| **declared-but-not-mentioned** | **EMPTY** | — |
| criterion-bearing | **32** (the four `g` boundary cells carry none by declaration) | 32 |
| s.11 FIXED entries | **14 rows parsed; numbers 1–14 covered; missing NONE** | 14, mapped both directions |
| criteria → cells | **0 criteria → NOT-YET-EVALUABLE** | stated as NOT-YET-EVALUABLE, not MISALIGNED |
| DARK cells | **0** — the UNMEASURED ones (`a-3`, `a-4`, `a-6`) measure themselves as their first act | 0 |

**Extractor controls:** `b-1` PRESENT ✓ · `inv-6` PRESENT ✓ · `z-9` ABSENT ✓ · `d-99` ABSENT ✓.

⛔ **INSTRUMENT NOTE — MY OWN, AND IT IS THE THIRD TIME MY EXTRACTOR HAS OVER-REACHED.** The raw run
reported four "mentioned-but-not-declared" ids: `a-49`, `b-0833`, `e-2`, `e-24`. **All four are my
regex eating substrings out of ordinary prose** — `a-49` from `opal-data-49financial`, `b-0833` from
`Schwab-0833`, `e-2`/`e-24` from `Rule-24`. **I inspected them rather than reporting them**, which is
the only reason this cert does not open with four fabricated findings against a clean file. *A
short-form cell grammar (`a-1`, `b-4`) is indistinguishable from a hyphenated number anywhere in the
document; the fully-qualified `PRF-` form is not. Recorded as a note to the grammar, not as a defect
in the decomp.*

## AGAINST MY PRE-STATED BAR, per-project items (66358), each measured

| my stated item | verdict |
|---|---|
| (a) five cards EXACTLY, no DEFERRED/GAP tiles | **MET** — `d-2` with a zero-tile oracle |
| (b) periods / groupings / export as declared enumerations with four-postulate records | **MET** — `R-p1`/`R-p2` + `d-1` |
| (c) Gain/Loss LAST + census-first on Schwab silver | **MET** — `a-4` → `b-4`, sequenced last in s.5 |
| (d) per-relationship PAGED Transactions refusing a firm-wide dump | **MET** — `b-5` |
| (e) ONE implementation, firm-pinned invocations; NO per-partner structure cells | **MET** — `inv-5` only; `g-3` declares the boundary |
| (f) NO new gate cells | **MET** — `d-8` rides the 49F switch promote; `e-1`'s report rides the DEV render |
| (g) #13 method extensions: DS drafts, CTO rules, CVO certifies; contract's author never briefed | **MET** — binds `a-2`/`b-1`/`b-6`/`b-7`; and the author's lane is off this subject by Andrew's word anyway |

## RULE 24 — six records, and two of them do real work

`R-p1`..`R-p6` present, (iv) applied as a test throughout. Two are worth naming:

- **`R-p5` declares advisor→firm NON-ADDITIVE, and therefore refuses to apply `inv-3` there.** A
  four-level rollup whose top level is not a sum of the level below is exactly where a decomp
  silently ships a double-count by assuming symmetry. **Declaring the non-additivity and scoping the
  invariant off it is the postulate preventing a defect, not documenting one.**
- **`R-p6` records the PRD's own HAVE / BUILD / GAP / DEFERRED axis as a 24(iii) INTENT MIX** —
  it fuses *what exists* with *what we will do about it* — **and resolves it by TABLE rather than by
  renaming Andrew's word.** That is the right call twice over: the axis is genuinely two axes, and
  the fix does not touch sovereign vocabulary. **A decomp catching a taxonomy defect in the PRD it is
  decomposing, without re-opening the PRD's language, is the pattern I want cited.**

## THE PREMISE CORRECTION (Q-p1) — I RE-DERIVED IT INDEPENDENTLY, BECAUSE IT IS A BUILD INPUT

COO reported the PRD's assumed `fact_account_return_daily` does not exist. **A claim about to become
a build input gets the control, whoever wrote it** (MSTR's rule, recorded against my own miss on
2026-08-21). Measured at this seat, live, rail-checked:

| probe | result |
|---|---|
| `gold/advi/canonical/` table prefixes | **8** — `accrual_materiality`, `canonical_positions`, `canonical_valuation`, `flow_ledger`, `nna_atomic`, `nna_canonical`, `twr_daily`, `valuation_integrity` |
| `fact_account_return_daily` / `twr_periods` | **ABSENT from that set** |
| `gold/advi/` top level | **4** — `_logs`, `canonical`, `dimensions`, `reference` (no home for the gains trio) |
| negative control | a fabricated table prefix returns null, a real one returns a count — **the listing discriminates** |

**CONFIRMED, and the denominator is named: 8 of 8 prefixes enumerated in ONE tree.** This is an
existence claim about `opal-data-49financial` only — per the firm-partition rule, it is not a claim
about any other tree, and PERFRP does not need one.

**CTO ruled Q-p1/p2/p3 CONFIRMED (66461) while I was measuring, on the same reading.** The decomp's
s.2.0 decision (consume the live canonical tables, import the existing pure cores, DECLARE absent
plan columns in the contract) therefore stands with both an author ruling and an independent read
under it. **CTO's added reason is the one I would have given: landing the plan's ~50-column table
first would build ADVI_PERFORMANCE's unbuilt Phase-2 table inside PERFRP** — Build Ladder rung 1, and
it would brief the contract's author, which s.11 #13 forbids.

## WHAT I DID NOT VERIFY (declared)

- **I re-derived ONE instrument** (the canonical-table existence read behind Q-p1). I5–I11-class
  instruments in s.1 stand as **COO's** measurements with their printed denominators, not mine.
- **`twr_daily` = 9 columns vs the plan's ~50** is COO's read; I confirmed the table's EXISTENCE and
  the absent siblings, **not the column count**. A cert that implies otherwise would be the
  authorship-is-not-evidence class.
- **No exercise.** Every oracle here is exercise-shaped and fires at TO time. `e-1`'s parity harness
  and `inv-2`'s control are MINE to run on first emission — they are commitments in this cert, not
  discharged by it.

## WHAT COO SHOULD HAVE ASKED BUT DID NOT

**Who owns the moment `b-1`'s contract skeleton and `d-1`'s consumption of it disagree — and how
would anyone find out?** s.5 sequences `d-1` to start on `b-1`'s *contract skeleton*, before the
leaves land. That is correct for velocity and it creates a window where the DE lane is building
against a **declared** shape and the DS lane is still discovering what the live canonical tables can
actually fill — precisely the case `R-p6`'s HAVE/BUILD split exists to track. **The contract is the
only artifact in both lanes' hands, and no cell owns its VERSIONING.** If `b-1` declares a column
absent (per the Q-p1 ruling: absent plan columns are declared, never silently filled) *after* `d-1`
has rendered a tile for it, the disagreement surfaces as an empty tile on DEV — indistinguishable
from a data gap, on a client-facing performance card. **Cheap form: `b-1`'s contract carries a
version and `d-1`'s oracle asserts the version it built against.** Not a gate, not a monitor — a
field and an assert. *This is the same shape as the D1 unknown-unknown I filed an hour ago (two cells
sharing a trigger neither one owns), which is itself worth noticing: two decomps, same session, same
seam class.*

— `3.0.0_SA_CVO`
