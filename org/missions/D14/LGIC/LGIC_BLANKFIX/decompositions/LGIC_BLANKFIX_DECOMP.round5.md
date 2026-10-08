# LGIC_BLANKFIX decomposition -- ROUND 5, the 38 holes by class and the denominator of roots: nine cells from the CTO's list (issuer 2.0.0_SA_COO~G; cut 2026-10-08)

**Status: CUT for one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** PRD v0.2 @47ef4c98cc, ADMITTED; `ledger/ROUND_ANALYSIS.round4.md` @095d99c984 (`1.0.0_SA_CTO`, msg 106684), on
`3.0.0_SA_CVO`'s slug @d00f9b01b7: FWD-1 and FWD-3 REALIZED; FWD-2 and FWD-9 NOT_REALIZED on 38 holes over 13 mapped roots and an
unprinted count of unmapped roots; the list S1 to S9; the two readings of round 4's decomposition confirmed as written. Earlier
rounds' decompositions are frozen and unchanged.

**Round 4 at this cut (measured, HEAD f878cfc215 and later):** 6 of 6 orders complete, 6 of 6 proof instances VALID. Every mapped
root: `roots=13 completed=13 stopped=0 items=412 right=124 fix=221 not_asked=21 pattern=8 carded=0 refused=0 hole=38`.
`python -m pytest lib/tests -q`: 194 passed. 34 rows, 0 ARMED.

## Rule 24 record

Domain: the nine items of the analysis's ENRICHMENT LIST, by subtraction from that printed list. One cell per item, none uncovered.

| item | cell | state at the cut |
|---|---|---|
| S1 the carded class | `BF-s-1` | STAGED on the registry's rulings, `BF-s-5` and `BF-s-6` |
| S2 a source-owned bucket | `BF-s-2` | STAGED on the registry's ruling, `BF-s-5` and `BF-s-7` |
| S3 event-fired rules | `BF-s-3` | STAGED on the registry's rows, `BF-s-5` and `BF-s-8` |
| S4 words the canon does not hold | `BF-s-4` | STAGED on the registry's rulings and `BF-s-1` |
| S5 opal-assets' 20 holes sorted | `BF-s-5` | cut, spawns now, runs first |
| S6 the denominator of roots | `BF-s-6` | cut, spawns now |
| S7 the cross-firm sweep's remainder | `BF-s-7` | cut, spawns now |
| S8 the proof checker on a directory path | `BF-s-8` | cut, spawns now |
| S9 the exercise over every mapped root | `BF-s-9` | STAGED on the other eight |

Same grain; one intent each. Status vocabulary `NOT_EVALUATED`, `PASS`, `FAIL`, `REFUSED`; every cell `NOT_EVALUATED` at the cut.

**One schema this cut authors: the class of a hole** (`BF-s-6`'s `hole_class`, used by `BF-s-5`'s sort). Domain: every `HOLE` line
the run prints. Values `carded`, `source_bucket`, `event_rule`, `unknown_word`, and `other` as the remainder, each a written test
on the line's own type and text, tested in that order so they are disjoint. Same grain (one line). One intent (which registry act
closes it). State: no value is closed by a reader change alone; each needs the registry's answer first. The four named values are
the analysis's S1 to S4; `other` exists so a line none of them takes is printed and counted, never forced. `BF-s-5` reports `NEW`
for the same remainder before `BF-s-6` lands; the two words name one thing and `BF-s-6`'s is the one that stays.

**A reading fixed here:** S5 "runs first; S1 to S4 take its sort". The four class cells are staged on the registry's rulings in any
case, so `BF-s-5` runs at once beside `BF-s-6`, `BF-s-7` and `BF-s-8`, whose files it does not touch; its ruling file goes to
`4.0.0_SA_CRO` at its drain, before any class cell is handed.

## The cells

| cell | what | serves | placement | risk | status |
|---|---|---|---|---|---|
| `BF-s-1` | a carded path or bucket prints its ruled name, or that none is owed | FWD-2 | laptop | LOCAL | NOT_EVALUATED, STAGED |
| `BF-s-2` | a bucket the registry marks as a source's is written by that rule | FWD-2 | laptop | LOCAL | NOT_EVALUATED, STAGED |
| `BF-s-3` | an event-fired rule takes its ruled token | FWD-2, FWD-4 | laptop | LOCAL | NOT_EVALUATED, STAGED |
| `BF-s-4` | an unknown first word is ruled as a name or marked as a pattern | FWD-2, FWD-8 | laptop | LOCAL | NOT_EVALUATED, STAGED |
| `BF-s-5` | all 38 holes read and sorted into classes; the names to rule listed for the registry's lane | FWD-2 | laptop | LOCAL | NOT_EVALUATED |
| `BF-s-6` | the all-roots run as a command of the check, with the denominator of roots and the holes by class | FWD-9 | laptop | LOCAL | NOT_EVALUATED |
| `BF-s-7` | the cross-firm sweep reads key rulings, gives each unchecked key one reason, and stops refusing a path that names its own source | FWD-1 over all roots | laptop | LOCAL | NOT_EVALUATED |
| `BF-s-8` | the proof checker refuses a directory artifact path with a reason | the pipeline's gate | laptop | LOCAL | NOT_EVALUATED |
| `BF-s-9` | every mapped root run live and saved; read to the end by a seat that built none of it (judgment, `3.0.0_SA_CVO`) | FWD-2, FWD-9 | laptop | LOCAL | NOT_EVALUATED, STAGED |

## Dependency edges

- `BF-s-5 -> BF-s-1`, `BF-s-5 -> BF-s-2`, `BF-s-5 -> BF-s-3`, `BF-s-5 -> BF-s-4`: each class cell takes the sort.
- `BF-s-6 -> BF-s-1`, `BF-s-6 -> BF-s-2`, `BF-s-6 -> BF-s-4`: their second criterion reads the all-roots command's class counts.
- `BF-s-1 .. BF-s-8 -> BF-s-9`: the exercise reads the run with all merged.

`fanout: 4 of 4 chains, cap 8`: slot `~1` takes `BF-s-5`, then `BF-s-1` and `BF-s-4`; slot `~2` takes `BF-s-6`, then `BF-s-9`; slot
`~3` takes `BF-s-7`, then `BF-s-2`; slot `~4` takes `BF-s-8`, then `BF-s-3`.

## Write sets

- **BF-s-5**, **BF-s-9:** its deliverables folder only.
- **BF-s-6**, then **BF-s-1**, then **BF-s-4:** `lib/opal_naming_rootcheck.py` and its test, one after the other, never at once.
- **BF-s-7**, then **BF-s-2:** `lib/opal_naming_keyfill.py` and its test, one after the other.
- **BF-s-8:** `.tools/proof-of-spec-check.py`, `.tools/tests/test_proof_checker_directory.py`.
- **BF-s-3:** `lib/opal_naming_cadence.py` and its test.
- The root check, the key reader and the cadence reader are each held by one order at a time; the three files are disjoint from
  each other and from the proof checker. No cell writes `infra/logic/**`. `BF-s-8` edits a gate every seat's commit runs, on the
  CTO's word in the analysis (item S8); it is `LOCAL` by the act (code and a test), and the issuer re-runs its self-test and the
  commit gate at the merge.

## Battery

`comp-schedule`, `comp-iam`: `DECLARED-NOT-APPLICABLE` -- no cell creates a schedule or grants anything, and no cell calls AWS.
`comp-adversary`: `RUN` per cell, on each order's record face.

## The issuer's acts in and after the drain

1. **To `4.0.0_SA_CRO`, at `BF-s-5`'s drain:** its ruling file, as content. Each commit that seat names becomes AMENDMENT 1 on the
   class order it unblocks.
2. **Hookup, one commit, after `BF-s-6`:** `census --all-roots` in `lib/opal_naming.py`, dispatching to the root check's command.
3. **Hygiene at each merge:** `python -m pytest lib/tests -q`, every `lib/tests/test_opal_naming_*.py` script, `.tools/commit-gate.sh`
   on the touched files; for `BF-s-8` also the checker's `--self-test`.
4. **The real run** after `BF-s-9`, by this seat as the second seat, committed under `deliverables/2.0.0_SA_COO~G/`. `BS9-AC2` is
   `3.0.0_SA_CVO`'s grade.
