# LGIC_BLANKFIX decomposition -- ROUND 7, the check written down, FWD-6 repaired, the census's blind spot, the map's undecided fields, the repeat by name: six cells from the CTO's list E1 to E5 (issuer 2.0.0_SA_COO~G; cut 2026-10-08)

**Status: CUT for one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** PRD v0.2 @47ef4c98cc, ADMITTED; `ledger/ROUND_ANALYSIS.round6.md` @ea45e82c70 (`1.0.0_SA_CTO`, msg 107272), on
`3.0.0_SA_CVO`'s slug (msg 107254) and grade `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND6_L9_GRADE_BU6_BU7_20261008.md`: FWD-5's check is `census --all-roots`; FWD-5 and FWD-6
NOT_REALIZED; FWD-2 and FWD-7 advanced, not realized; the list E1 to E5; no PRD addendum. Earlier rounds' decompositions are
frozen and unchanged.

**Round 6 at this cut (measured by the issuer at the cut):** `ALL-ROOTS ok=True roots_total=87 mapped=13 unmapped=74 ... hole=0 ...
stale_hints=0`; `pytest lib/tests` 194 passed; `SCOPE-TEST ok=True assertions=362`; `ROOTCHECK-TEST ok=True cases=209`;
`ROOTMAP-TEST ok=True assertions=46`; `FWD6-DESIGN ok=True headings=7 paths=30 missing=0` (BF-v-3 writes a round-7 checker beside it); one red: `ALL-ROOTS-R5 ok=False` (row S8,
ycharts line numbers moved). `infra/logic/README.md` and `10_ONBOARDING_CHECKLIST.md` name `census --all-roots` 0 times. Round 6's
ruling file holds 74 sections, 11 `verdict: DECLARES-NAMES`.

## Rule 24 record

Domain: the five items of the analysis's ENRICHMENT LIST, by subtraction from that printed list. Every item has a cell; E1 has two,
because writing the instructions and exercising them must be different seats.

| item | cell | state at the cut |
|---|---|---|
| E1 write the check into the instructions | `BF-v-1` | pending after `BF-v-4`, slot `~4` |
| E1 a new fresh seat runs it from the written text (JUDGMENT) | `BF-v-2` | pending after `BF-v-1` merges, slot `~5` |
| E2 repair the FWD-6 design (JUDGMENT) | `BF-v-3` | pending, slot `~1` |
| E3 disarm W1-S14: names behind a zero counted or UNCOUNTED | `BF-v-4` | pending, slot `~4` |
| E4 decide the 180 UNDECIDED fields; measure how many land | `BF-v-5` | pending, slot `~3` |
| E5 row S8: the repeat by name and verdict | `BF-v-6` | pending, slot `~2` |

Not cut: W1-S15 (CLAUDE.md rule 30's "WARN today" against an enforcing gate) is Andrew's act, cited by the analysis. The map
entries are written by `4.0.0_SA_CRO`; `BF-v-5` hands that seat the decided entries at its drain.

Same grain; one intent each. Status vocabulary `NOT_EVALUATED`, `PASS`, `FAIL`, `REFUSED`; every cell `NOT_EVALUATED` at the cut.
**Schemas this cut authors:** the `UNCOUNTED` reason values (`BF-v-4`: `local`, `var`, `module`, `json`, `interpolation`; domain:
the expression kinds a Terraform name attribute can hold that are not a string literal, the residue `interpolation`) and the entry
verdicts LANDS / HELD / REFUSED (`BF-v-5`: disjoint by the two tests "carries UNDECIDED" and "loader accepts", exhaustive).

## The cells

| cell | what | serves | placement | risk | status |
|---|---|---|---|---|---|
| `BF-v-1` | README and checklist STEP 13 name `census --all-roots`, every last-line field explained, no `--live` on the newcomer path | FWD-5 | laptop | WORLD (writes under `infra/`; the gate's floor) | NOT_EVALUATED |
| `BF-v-2` | a new seat runs the check from the written text on a fresh copy (judgment, `3.0.0_SA_CVO`) | FWD-5 | laptop | LOCAL | NOT_EVALUATED |
| `BF-v-3` | the FWD-6 design's arm C, arm D and HOLE owners repaired (judgment, `3.0.0_SA_CVO`) | FWD-6 | laptop | LOCAL | NOT_EVALUATED |
| `BF-v-4` | names in locals, modules and generated json counted or printed UNCOUNTED; `uncounted=N` | FWD-2, FWD-7 | laptop | LOCAL | NOT_EVALUATED |
| `BF-v-5` | the 74 entries with every decidable field decided; LANDS / HELD / REFUSED measured | FWD-7, FWD-2 | laptop | LOCAL | NOT_EVALUATED |
| `BF-v-6` | the repeat compares (kind, type, name, file) and answer, not line numbers | FWD-9 | laptop | LOCAL | NOT_EVALUATED |

## Dependency edges

- `BF-v-4 -> BF-v-1`: same slot `~4`; the README explains the `uncounted` field `BF-v-4` adds.
- `BF-v-1 -> BF-v-2`: the fresh seat reads the merged instructions; its worktree is made at the trunk after `BF-v-1` merges.
- `BF-v-4 -> BF-v-6`, `BF-v-5 -> BF-v-6`: the repeat must tolerate added names and the new line kind (its face says so; no wait).
- `BF-v-5 -> (4.0.0_SA_CRO writes the entries)`: outside the cells; the issuer's real run at the close reads whatever has landed.

`fanout: 5 of 5 chains, cap 8`: slot `~1` `BF-v-3`; slot `~2` `BF-v-6`; slot `~3` `BF-v-5`; slot `~4` `BF-v-4`, then `BF-v-1`;
slot `~5` `BF-v-2`. **Concurrency is held below the fan-out by the disk rule** (`1.0.0_SA_CTO` msg 106860: at most 3 worker worktrees
across all COO lanes until 20 GB is free; none under 10 GB). At the cut C: read 16 GB free and `2.0.0_SA_COO~C` held 3 worker
worktrees, so slots are handed as worktrees free, in the order `~4`, `~3`, `~1`, `~2`, then `~5`.

## Write sets

- **BF-v-4:** `lib/opal_naming_scope.py`, `lib/opal_naming_rootcheck.py` and their tests; its checker in `~4`'s folder.
- **BF-v-1:** `infra/logic/README.md`, `infra/logic/10_ONBOARDING_CHECKLIST.md`; its checker in `~4`'s folder.
- **BF-v-2**, **BF-v-3**, **BF-v-5**, **BF-v-6:** the slot's deliverables folder only (`BF-v-3` edits `~1`'s design and checker,
  `BF-v-6` `~2`'s script).
- Disjoint across live cells. No cell writes `infra/logic/registry/**`.

## Battery

`comp-schedule`, `comp-iam`: `DECLARED-NOT-APPLICABLE` -- no cell creates a schedule or grants anything, and no cell calls AWS.
`comp-adversary`: `RUN` per cell, on each order's record face.

## The issuer's acts in and after the drain

1. **To `4.0.0_SA_CRO`, at `BF-v-5`'s drain:** the entries file and the land count, as paths.
2. **`BF-v-2`'s spawn prompt** carries identity, worktree and the pointer to the WORKER FACE only: no command for the check.
3. **Hygiene at each merge:** `python -m pytest lib/tests -q`, every `lib/tests/test_opal_naming_*.py` script, `.tools/commit-gate.sh`
   on the touched files; each criterion re-run by the issuer in the slot's worktree before the merge.
4. **The real run** at the close, by this seat: `census --all-roots`, committed under `deliverables/2.0.0_SA_COO~G/`.
