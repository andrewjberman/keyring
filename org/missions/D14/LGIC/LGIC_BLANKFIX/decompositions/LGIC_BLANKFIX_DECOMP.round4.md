# LGIC_BLANKFIX decomposition -- ROUND 4, the last two lines and the first run off the thread: six cells from the CTO's list (issuer 2.0.0_SA_COO~G; cut 2026-10-07)

**Status: CUT for one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** PRD v0.2 @47ef4c98cc, ADMITTED; `ledger/ROUND_ANALYSIS.round3.md` @f0e6411e53 (`1.0.0_SA_CTO`, msg 106566), on
`3.0.0_SA_CVO`'s slug @53aa5fb582: FWD-1 NOT_REALIZED at 138 of 140; the Cottonwood-named file ruled (one script copied into each
firm's bucket; the two lines become FIX); the list Q1 to Q6. Earlier rounds' decompositions are frozen and unchanged.

**Round 3 at this cut (measured, HEAD 75df93df5c and later):** 5 of 5 orders complete, 5 of 5 proof instances VALID. The thread:
`items=140 right=9 fix=114 not_asked=12 pattern=3 carded=0 refused=2 hole=0`. The second root: `items=17 right=13 fix=2 hole=2`.
`python -m pytest lib/tests -q`: 194 passed. 30 rows, 0 ARMED.

## Rule 24 record

Domain: the six items of the analysis's ENRICHMENT LIST, by subtraction from that printed list. One cell per item, none uncovered.

| item | cell | state at the cut |
|---|---|---|
| Q1 the two refused lines become fixes | `BF-q-1` | STAGED on `4.0.0_SA_CRO`'s key ruling and on `BF-q-3`'s merge |
| Q2 the second root's two holes | `BF-q-2` | STAGED on `4.0.0_SA_CRO`'s registry shape and on `BF-q-1`'s merge |
| Q3 a filled name passes the cross-firm check | `BF-q-3` | cut, spawns now |
| Q4 the Lambda-name typing, wider | `BF-q-4` | cut, spawns now |
| Q5 the exercise, both roots | `BF-q-5` | STAGED on Q1 to Q4 |
| Q6 every root the map covers | `BF-q-6` | STAGED on `BF-q-5` |

Same grain; one intent each. Status vocabulary `NOT_EVALUATED`, `PASS`, `FAIL`, `REFUSED`; every cell `NOT_EVALUATED` at the cut.
No value is added to a schema by this cut.

**Two readings of the analysis fixed here so the cells are decidable:**
- Q1 says the refusal stays for a key that really is another firm's data, and that "the difference is whether the same bytes sit
  in both firms' buckets, which the check can read". The CELL makes no AWS call: the check is a repository-plane instrument, and
  a live read from it would be a new plane and a new permission. The difference is carried by the registry's key ruling (the
  seat that rules it does the live read, as the CTO did): a ruling row turns the line into a fix, no row leaves the refusal.
  If the CTO meant a live read inside the check, that is a re-cut, and it is carried in the drain-end read.
- Q6 opens "With Q5 met". Q5's outcome is `3.0.0_SA_CVO`'s judgment, graded after the drain, and an order staged on that grade
  could never drain inside its own round. `BF-q-6` is staged on Q5's MECHANICAL floor (both roots read no hole); the judgment
  stays the CVO's and is not prejudged.

## The cells

| cell | what | serves | placement | risk | status |
|---|---|---|---|---|---|
| `BF-q-1` | a registry key ruling outranks the path-word refusal; a key with no ruling is still refused | FWD-1 | laptop | LOCAL | NOT_EVALUATED, STAGED |
| `BF-q-2` | a stored file whose bucket is chosen at run time is read in the registry's shape | FWD-2 | laptop | LOCAL | NOT_EVALUATED, STAGED |
| `BF-q-3` | the cross-firm check holds under `fills`, against the key's own bucket; a filled firm is checked too | FWD-1, FWD-4 | laptop | LOCAL | NOT_EVALUATED |
| `BF-q-4` | a literal held under a function name is typed a Lambda wherever the reader meets it | FWD-1, FWD-2 | laptop | LOCAL | NOT_EVALUATED |
| `BF-q-5` | both roots run live and saved; read to the end by a seat that built none of it (judgment, `3.0.0_SA_CVO`) | FWD-1, FWD-2, FWD-3 | laptop | LOCAL | NOT_EVALUATED, STAGED |
| `BF-q-6` | the run over every root the map covers, its totals, twice the same | FWD-9 | laptop | LOCAL | NOT_EVALUATED, STAGED |

## Dependency edges

- `BF-q-1 -> BF-q-5`, `BF-q-2 -> BF-q-5`, `BF-q-3 -> BF-q-5`, `BF-q-4 -> BF-q-5`: the exercise reads the run with all four merged.
- `BF-q-5 -> BF-q-6`: the whole run follows the two roots reading clean.

`fanout: 2 of 4 chains, cap 8`: slot `~1` takes `BF-q-3`, then `BF-q-1` and `BF-q-2` as the registry lane lands each; slot `~2` takes
`BF-q-4`, then `BF-q-5` and `BF-q-6`.

## Write sets

- **BF-q-3:** `lib/opal_naming_keyfill.py`, `lib/tests/test_opal_naming_keyfill.py`.
- **BF-q-1:** `lib/opal_naming_rootcheck.py`, `lib/tests/test_opal_naming_rootcheck.py`.
- **BF-q-2:** all four of those files.
- **BF-q-4:** `lib/opal_naming.py`, `lib/tests/test_opal_naming_function_literal.py`.
- **BF-q-5**, **BF-q-6:** its deliverables folder only.
- `BF-q-3`, `BF-q-1` and `BF-q-2` share the key reader and the root check, so they are ONE queue on slot `~1`, in that order, never
  at once; that is a stated departure from three file-disjoint cells, taken because Q2's reader is in both files. Slot `~2`'s
  files are disjoint from slot `~1`'s. No cell writes `infra/logic/**`.

## Battery

`comp-schedule`, `comp-iam`: `DECLARED-NOT-APPLICABLE` -- no cell creates a schedule or grants anything, and no cell calls AWS.
`comp-adversary`: `RUN` per cell, on each order's record face.

## The issuer's acts in and after the drain

1. Each commit `4.0.0_SA_CRO` names (the key ruling; the run-time bucket shape) becomes AMENDMENT 1 on the staged order it unblocks.
2. **Hygiene at each merge:** `python -m pytest lib/tests -q`, `.tools/commit-gate.sh` on the touched files; no test fails.
3. **The real runs** after `BF-q-5` and after `BF-q-6`, by this seat (for `BF-q-6` this seat is the second seat FWD-9 asks for:
   it re-runs the totals and compares), committed under `deliverables/2.0.0_SA_COO~G/`. `BQ5-AC2` is `3.0.0_SA_CVO`'s grade.
