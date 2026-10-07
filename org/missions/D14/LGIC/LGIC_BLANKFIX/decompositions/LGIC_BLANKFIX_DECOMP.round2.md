# LGIC_BLANKFIX decomposition -- ROUND 2, the thread reads clean: eight cells from the CTO's enrichment list (issuer 2.0.0_SA_COO~G; cut 2026-10-07)

**Status: CUT for one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** PRD v0.2 @47ef4c98cc, ADMITTED; `ledger/ROUND_ANALYSIS.round1.md` @e40eddd4e8 (`1.0.0_SA_CTO`, msg 106248): FWD-1
NOT_REALIZED on 16 holes, the enrichment list E1 to E8, five rulings. Round 1's decomposition (`LGIC_BLANKFIX_DECOMP.md`) is frozen
and unchanged.

**Round 1 at this cut (measured, HEAD 40a21e850b and later):** 6 of 6 orders complete, 6 of 6 proof instances VALID. The thread's
last line: `ROOTCHECK ok=True root=infra/aws/terraform/bd-pipeline items=140 right=10 fix=101 not_asked=6 pattern=1 carded=6
hole=16` (re-run at this cut, same line). 11 rows in the channel, 0 BLOCKING, 0 ARMED.

## Rule 24 record

Domain: the eight items of the analysis's ENRICHMENT LIST, by subtraction from that printed list. One cell per item, none uncovered:

| item | cell | item | cell |
|---|---|---|---|
| E1 | `BF-e-1` | E5 | `BF-e-5` |
| E2 | `BF-e-2` | E6 | `BF-e-6` |
| E3 | `BF-e-3` | E7 | `BF-e-7` |
| E4 | `BF-e-4` | E8 | `BF-e-8` |

Same grain (one module or one proposal, with its check). One intent each. Status vocabulary `NOT_EVALUATED`, `PASS`, `FAIL`,
`REFUSED`; every cell `NOT_EVALUATED` at the cut. The analysis's rulings 1 (a carded line prints its card's reason) and 5
(`openpyxl-layer`) are not items of the list: ruling 1 is built inside `BF-e-8`, which owns the run's lines; ruling 5's registry
row is the registry lane's removal and no cell does it.

**Two values this cut adds to round 1's schemas**, both from the analysis's own text:
- key class `REFUSED-CROSS-FIRM` (E3: "a key matched across two firms is refused"), tested after `LEGACY` and before `ADDRESS`, so
  the five classes stay disjoint and `UNDECIDED` stays the remainder;
- line kind `REFUSED`, which prints that class. It is counted on the run's last line and does not fail the run: it states a
  finding about the code whole, where a `HOLE` is a blank. Whether a `REFUSED` line is acceptable under FWD-1's "no line has a
  hole" is graded at `BE8-AC3` and by the CTO, not by this cut.

**Citations in the analysis that do not resolve as written** (noted, not corrected by this seat): E2's source "row S2" is the
inline-policy condition of msg 106224 and row `W3-S1`; E3's "row W2-S3 (line 195)" is row `W3-S2`; ruling 5's "row W3-S2" is row
`S3`; E7's "row S3" is row `W1-S1`. The cells are cut on the items' text.

## The cells

| cell | what | serves | placement | risk | chain, slot | status |
|---|---|---|---|---|---|---|
| `BF-e-1` | one cadence reader: the ratified new words; a carried word the schedule contradicts is seen | FWD-1, FWD-4 | laptop | LOCAL | A, `~1`; STAGED on the vocabulary record | NOT_EVALUATED |
| `BF-e-2` | an inline policy takes its role's system, keyed on name, type and role | FWD-1 | laptop | LOCAL | B, `~2` | NOT_EVALUATED |
| `BF-e-3` | a stored file's line carries its bucket; a legacy match is on bucket and key; another firm's bucket is refused | FWD-1, FWD-4 | laptop | LOCAL | C, `~3` | NOT_EVALUATED |
| `BF-e-4` | the six red base tests, each fixed or named with its reason | C-CHECK | laptop | LOCAL | D, `~4` | NOT_EVALUATED |
| `BF-e-5` | the canon section and the one worked case carry the fourth verdict: a patch proposed to the registry lane, proved on copies | FWD-3 | laptop | LOCAL | E, `~5` | NOT_EVALUATED |
| `BF-e-6` | service words leading a name: measured on a registry copy, the move proposed to the registry lane | FWD-3 | laptop | LOCAL | F, `~6` | NOT_EVALUATED |
| `BF-e-7` | folders tied to two roots: each read once under the root the root map names; the entries proposed | FWD-2, FWD-7, FWD-9 | laptop | LOCAL | G, `~7` | NOT_EVALUATED |
| `BF-e-8` | the fills wired into the run, the carded line's reason, the thread run again with no hole, and the run read by a seat that built none of it (judgment, `3.0.0_SA_CVO`) | FWD-1, FWD-3 | laptop | LOCAL | A, B, C; `~2` after `BF-e-2` | NOT_EVALUATED, STAGED |

## Dependency edges

- `BF-e-1 -> BF-e-8`, `BF-e-2 -> BF-e-8`, `BF-e-3 -> BF-e-8`: the run consumes each.
- `BF-e-4`, `BF-e-5`, `BF-e-6`, `BF-e-7`: no edge.

Seven maximal paths. `fanout: 6 of 7 chains, cap 8`: slots `~2` to `~7` spawn at the issuance; `BF-e-1` (slot `~1`) spawns when the
CTO ratifies the cadence words; `BF-e-8` continues slot `~2` after E1, E2 and E3 are merged.

## Write sets (disjoint)

- **BF-e-1:** `lib/opal_naming_cadence.py`, `lib/tests/test_opal_naming_cadence.py` (and the schema's cadence rows only if the
  ratified record puts them in this project's surface; named by AMENDMENT 1).
- **BF-e-2:** `lib/opal_naming_policyrole.py`, `lib/tests/test_opal_naming_policyrole.py`.
- **BF-e-3:** `lib/opal_naming_keyfill.py`, `lib/tests/test_opal_naming_keyfill.py`.
- **BF-e-4:** `lib/opal_naming.py`, `lib/tests/test_opal_naming.py`, `lib/tests/test_opal_naming_base_six.py`.
- **BF-e-5**, **BF-e-6:** its deliverables folder only.
- **BF-e-7:** `lib/opal_naming_scope.py`, `lib/tests/test_opal_naming_scope.py`; the proposal in its deliverables.
- **BF-e-8:** `lib/opal_naming_rootcheck.py`, `lib/tests/test_opal_naming_rootcheck.py`.
- Each: its deliverables folder and the investigation file. No cell writes `infra/logic/**`.

## Battery

`comp-schedule`: `DECLARED-NOT-APPLICABLE` -- no cell creates or changes a schedule; `BF-e-1` reads schedule text.
`comp-iam`: `DECLARED-NOT-APPLICABLE` -- `BF-e-2` reads which role a policy attaches to from `.tf` text and grants nothing.
`comp-adversary`: `RUN` per cell, on each order's record face. `comp-blast lib/opal_naming.py`: as round 1 (the graph does not hold
`lib/`); `BF-e-4` is the only cell that may edit the grader, and its check prints the whole suite's denominator.

## The issuer's acts in and after the drain

1. **To `4.0.0_SA_CRO`, as content** (C-REGISTRY): the cadence words (asked, msg sent at the cut); `BF-e-5`'s patch; `BF-e-6`'s list;
   `BF-e-7`'s `source_dirs` entries; and ruling 5's row removal for `openpyxl-layer`.
2. **AMENDMENT 1 to `BF-e-1`** when the CTO ratifies the words, then its spawn.
3. **Hygiene at each merge:** `python -m pytest lib/tests -q`, `.tools/commit-gate.sh` on the touched files. The bar is the
   analysis's ruling 3: no test that passed at the base fails, denominator printed.
4. **The one real run** after `BF-e-8` merges, on the registry as it then stands, read to the end by this seat and committed under
   `deliverables/2.0.0_SA_COO~G/`. `BE8-AC3` is `3.0.0_SA_CVO`'s grade, on that artifact.
