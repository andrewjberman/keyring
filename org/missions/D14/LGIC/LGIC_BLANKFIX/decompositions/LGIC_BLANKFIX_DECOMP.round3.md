# LGIC_BLANKFIX decomposition -- ROUND 3, every line acted on from the line alone: six cells from the CTO's list (issuer 2.0.0_SA_COO~G; cut 2026-10-07)

**Status: CUT for one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** PRD v0.2 @47ef4c98cc, ADMITTED; `ledger/ROUND_ANALYSIS.round2.md` @ef7133ec9a (`1.0.0_SA_CTO`, msg 106401), on
`3.0.0_SA_CVO`'s slug @ac8d39c4ac: FWD-1 NOT_REALIZED at 122 of 140 lines; the list R1 to R6; two calls ruled; round 1's ruling on
carded lines corrected. Rounds 1 and 2's decompositions are frozen and unchanged.

**Round 2 at this cut (measured, HEAD 1527383c06 and later):** 8 of 8 orders complete, 8 of 8 proof instances VALID. The thread:
`ROOTCHECK ok=True root=infra/aws/terraform/bd-pipeline items=140 right=9 fix=113 not_asked=9 pattern=1 carded=6 refused=2 hole=0`.
`python -m pytest lib/tests -q`: 194 passed. 22 rows, all dispositioned by `3.0.0_SA_CVO` (`adjudications/ADJUDICATION_v1.md`).

## Rule 24 record

Domain: the six items of the analysis's ENRICHMENT LIST, by subtraction from that printed list.

| item | cell | state at the cut |
|---|---|---|
| R1 the 18 lines | `BF-r-1` | cut, spawns now |
| R2 the match keys | `BF-r-2` | cut STAGED on the two registry shapes (`4.0.0_SA_CRO`) and on `BF-r-1`'s merge |
| R3 the folder map | `BF-r-3` | cut STAGED on the map's entries (`4.0.0_SA_CRO`) |
| R4 the worked case and the cadence restatement, "if cell E5 of round 2 did not land both" | `BF-r-4` | NO ORDER: the condition is false. Round 2's `BF-e-5` (reopened, AMENDMENT 1) landed both @1527383c06; `BE5-AC2` reads `GRADING-RULE ok=True worked_case=True cadence=True suite_failed=0 suite_passed=93`, re-run by the issuer at the merge |
| R5 the exercise again | `BF-r-5` | cut STAGED on `BF-r-1`, `BF-r-2` and the registry acts their holes name |
| R6 a second root | `BF-r-6` | cut STAGED on `BF-r-3` |

Six items, six cells, five orders, none uncovered. Same grain; one intent each. Status vocabulary `NOT_EVALUATED`, `PASS`, `FAIL`,
`REFUSED`; `BF-r-4` is `PASS` on round 2's proof; the others `NOT_EVALUATED`.

**No value is added to a schema by this cut.** The line kinds stay the seven of round 2. Three readings of the analysis are fixed
here so the cells are decidable, each from its own text:
- A carded name whose card gives neither a correct name nor a statement that none is owed prints `HOLE` (the analysis: such a
  card "is a defect of the card, and its owner fixes the card"). The cards are LGIC_ENFORCE's file; no cell edits it.
- Two different current names given one target both print `HOLE` (the analysis: "two resources never share a target"). Which
  resource keeps the name is a registry row, not a cell's choice.
- So after `BF-r-1` the run is EXPECTED to read holes again, where round 2 read 0. That is the count catching up with the grade.

**A citation in the analysis that does not resolve as written:** call 2 says the worked case "is cell R5 below"; the list's item
for it is R4.

## The cells

| cell | what | serves | placement | risk | status |
|---|---|---|---|---|---|
| `BF-r-1` | what the run prints for the 18 lines: a not-asked line says why and whether a rename is owed; a carded line per the corrected ruling; a refused line says what was measured and what to do; two names never share a target | FWD-1, FWD-3 | laptop | LOCAL | NOT_EVALUATED |
| `BF-r-2` | the match keys: a map exception may carry its role and overrides a role's system only then; a legacy row matches on bucket and key | FWD-1, FWD-4 | laptop | LOCAL | NOT_EVALUATED, STAGED |
| `BF-r-3` | the folder map read again: every unassigned name counted and given a reason | FWD-7, FWD-2 | laptop | LOCAL | NOT_EVALUATED, STAGED |
| `BF-r-4` | the worked case and the cadence restatement | FWD-3 | laptop | LOCAL | PASS (round 2, `BF-e-5` reopened) |
| `BF-r-5` | the exercise again: the root run live and saved, read to the end by a seat that built none of it (judgment, `3.0.0_SA_CVO`) | FWD-1, FWD-3 | laptop | LOCAL | NOT_EVALUATED, STAGED |
| `BF-r-6` | the same run on one second root the map newly covers, read the same way (judgment, `3.0.0_SA_CVO`) | FWD-2, FWD-9 | laptop | LOCAL | NOT_EVALUATED, STAGED |

## Dependency edges

- `BF-r-1 -> BF-r-2`: the role match is wired into the run `BF-r-1` rewrites.
- `BF-r-2 -> BF-r-5`: the exercise reads the run with both merged.
- `BF-r-3 -> BF-r-6`: the second root is one the rebuilt map covers.

Two chains. `fanout: 1 of 2 chains, cap 8`: slot `~1` takes `BF-r-1`, then `BF-r-2`, then `BF-r-5`; slot `~2` takes `BF-r-3`, then
`BF-r-6`, and spawns when the registry lane's map entries land.

## Write sets

- **BF-r-1:** `lib/opal_naming_rootcheck.py`, `lib/tests/test_opal_naming_rootcheck.py`.
- **BF-r-2** (after `BF-r-1` on the same chain and slot): those two, plus `lib/opal_naming_rootmap.py`, `lib/opal_naming_keyfill.py`
  and their tests.
- **BF-r-3:** `lib/opal_naming_scope.py`, `lib/tests/test_opal_naming_scope.py`.
- **BF-r-5**, **BF-r-6:** its deliverables folder only.
- Chains A and B share no file. No cell writes `infra/logic/**` or the card file.

## Battery

`comp-schedule`, `comp-iam`: `DECLARED-NOT-APPLICABLE` -- no cell creates a schedule or grants anything; `BF-r-2` reads which role a
policy attaches to from `.tf` text. `comp-adversary`: `RUN` per cell, on each order's record face.

## The issuer's acts in and after the drain

1. **To `4.0.0_SA_CRO`, as content, once `BF-r-1` drains:** the carded keys of the root with no correct name, and the EC2 pair with
   one target (each needs a registry answer or its card's owner). The three registry acts the analysis already asks of that seat
   are its own; each commit it names becomes an AMENDMENT 1 on the staged order it unblocks.
2. **Hygiene at each merge:** `python -m pytest lib/tests -q`, `.tools/commit-gate.sh` on the touched files; no test fails.
3. **The one real run** after `BF-r-5`, read to the end by this seat, committed under `deliverables/2.0.0_SA_COO~G/`. `BR5-AC2` and
   `BR6-AC2` are `3.0.0_SA_CVO`'s grades, each on a live run.
