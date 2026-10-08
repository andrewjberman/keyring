# LGIC_BLANKFIX decomposition -- ROUND 6, breadth, the round-5 reds, FWD-5 and FWD-6: seven cells from the CTO's list E1 to E6 (issuer 2.0.0_SA_COO~G; cut 2026-10-08)

**Status: CUT for one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** PRD v0.2 @47ef4c98cc, ADMITTED; `ledger/ROUND_ANALYSIS.round5.md` @34ba4c1c90, amended @cbdf36254c (`1.0.0_SA_CTO`,
msgs 106949 and 106956), on `3.0.0_SA_CVO`'s slug (msg 106948): FWD-9 REALIZED; FWD-2 NOT_REALIZED, clean over the 13 mapped roots,
74 of 87 unmapped; the list E1 to E6 (E5 serves FWD-6, E6 serves FWD-5); no PRD addendum. Two inputs from `4.0.0_SA_CRO` landed
before the cut: the shape of a nothing-to-name entry (`infra/logic/registry/root_map.json` `_about` @35f40f2c02, msg 106961) and
the pre-write refusal patterns (`org/tier1_exec/4.0.0_SA_CRO/deliverables/PRE_WRITE_REFUSAL_PATTERNS_20261008.md` @cbf52722b0,
msg 106969). Earlier rounds' decompositions are frozen and unchanged.

**Round 5 at this cut (measured by the issuer at the cut):** `ALL-ROOTS ok=True roots_total=87 mapped=13 unmapped=74 completed=13
stopped=0 items=412 ... hole=0`; `pytest lib/tests`: 194 passed; `ROOTMAP-TEST ok=True assertions=30`; `ROOTCHECK-TEST ok=True
cases=194`. Two reds: `KEYFILL-TEST ok=False cases=86` (S7) and `ALL-ROOTS-R5 ... repeat=DIFFERS` (S8). At the round-5 close the 74
unmapped roots held 1,522 names; 24 printed names=0; the largest `inf-pipeline` (364), `shared-infra` (144), `smartx-pipeline`
(117).

## Rule 24 record

Domain: the six items of the analysis's ENRICHMENT LIST at @cbdf36254c, by subtraction from that printed list. Every item has a
cell; E1 has two, because its two acts have different write sets.

| item | cell | state at the cut |
|---|---|---|
| E1 map the next roots: the sort and the entries for the registry's lane | `BF-u-1` | pending, slot `~1` |
| E1 map the next roots: the reader for a nothing-to-name entry | `BF-u-2` | pending after `BF-u-3`, slot `~4` |
| E2 a ruling row survives a file move | `BF-u-3` | pending, slot `~4` |
| E3 the red test | `BF-u-4` | pending, slot `~3` |
| E4 the repeat check over mapped lines | `BF-u-5` | pending, slot `~2` |
| E5 the FWD-6 design | `BF-u-6` | pending after `BF-u-1`, slot `~1` |
| E6 FWD-5 exercised on a fresh copy | `BF-u-7` | pending, slot `~5` (a new seat that never ran the check) |

The map entries themselves are written by `4.0.0_SA_CRO` (C-REGISTRY), not by a cell: `BF-u-1` hands that seat the sort and the
drafts at its drain. W2-S2 stays OPEN and is not cut (the analysis). Row S9 (E5's label) is filed for the record the analysis
cites, answered by msg 106956 before the cut.

Same grain; one intent each. Status vocabulary `NOT_EVALUATED`, `PASS`, `FAIL`, `REFUSED`; every cell `NOT_EVALUATED` at the cut.

**One schema this cut authors: the class of an unmapped root** (`BF-u-1`). Domain: every root the `all` command prints `UNMAPPED`.
Values `names-zero` (the scope gives it no name), `no-stored-name` (names, none a bucket, stored-file key, table or rule), `to-map`
(the remainder), tested in that order so they are disjoint and exhaustive. Same grain (one root). One intent (what the census reads,
so the registry's lane knows what to write). State: no value maps a root by itself; each needs the registry's entry, and a
`names-zero` root needs a verdict from its `.tf` files, because the registry's owner rules that names=0 alone never justifies a
nothing-to-name entry. The verdict values are the registry's shape (`none/names_from_caller`,
`none/attaches_to_names_declared_elsewhere`) plus `DECLARES-NAMES` and `UNDECIDED`, not a new enum of this cut.

## The cells

| cell | what | serves | placement | risk | status |
|---|---|---|---|---|---|
| `BF-u-1` | the 74 unmapped roots sorted; a drafted entry per root, each field decided by a file and line or UNDECIDED; names-zero roots given a verdict | FWD-7, FWD-2 | laptop | LOCAL | NOT_EVALUATED |
| `BF-u-2` | the loader reads a nothing-to-name entry in the registry's shape; the run counts it mapped, and stops a root that names something | FWD-7, FWD-9 | laptop | LOCAL | NOT_EVALUATED |
| `BF-u-3` | a key ruling matches on its key, the path a hint; stale hints printed and counted | FWD-2 | laptop | LOCAL | NOT_EVALUATED |
| `BF-u-4` | the key reader's test finds its real file by what it declares | the pipeline's gate | laptop | LOCAL | NOT_EVALUATED |
| `BF-u-5` | the repeat check compares mapped roots' sections and shared fields only | FWD-9 | laptop | LOCAL | NOT_EVALUATED |
| `BF-u-6` | the design of the check that tells a name's creator at creation, from past patterns (judgment, `3.0.0_SA_CVO`) | FWD-6 | laptop | LOCAL | NOT_EVALUATED |
| `BF-u-7` | a first run from the written instructions on a fresh copy, nothing written for it (judgment, `3.0.0_SA_CVO`) | FWD-5 | laptop | LOCAL | NOT_EVALUATED |

## Dependency edges

- `BF-u-3 -> BF-u-2`: both write the root check; one after the other on slot `~4`.
- `BF-u-3 -> BF-u-5`, `BF-u-2 -> BF-u-5`: the repeat compare must tolerate the field and the line those cells add (its face says
  so; no wait).
- `BF-u-1 -> BF-u-6`: same slot.
- `BF-u-7`: no edge. Its worktree is made at the trunk when its slot is handed, so the copy is fresh whatever has merged.
- `BF-u-1 -> (4.0.0_SA_CRO writes the entries)`: outside the cells; the issuer's real run at the close reads whatever has landed.

`fanout: 5 of 5 chains, cap 8`: slot `~1` takes `BF-u-1`, then `BF-u-6`; slot `~2` takes `BF-u-5`; slot `~3` takes `BF-u-4`; slot
`~4` takes `BF-u-3`, then `BF-u-2`; slot `~5` takes `BF-u-7`. **Concurrency is held below the fan-out by the disk rule**
(`1.0.0_SA_CTO` msg 106860: at most 3 worker worktrees across all COO lanes until 20 GB is free). At the cut C: read 18 GB free and
`2.0.0_SA_COO~C` held 2 live worker worktrees, so this lane runs one slot at a time, in the order `~1`, `~3`, `~2`, `~4`, `~5`, and
widens when the reading allows.

## Write sets

- **BF-u-1**, **BF-u-6**, **BF-u-5**, **BF-u-7:** the slot's deliverables folder only (`BF-u-5` edits its slot's round-5 script there).
- **BF-u-3**, then **BF-u-2:** `lib/opal_naming_rootcheck.py` and its test; `BF-u-2` also `lib/opal_naming_rootmap.py` and its test.
- **BF-u-4:** `lib/tests/test_opal_naming_keyfill.py`.
- Disjoint across live cells. No cell writes `infra/logic/**`.

## Battery

`comp-schedule`, `comp-iam`: `DECLARED-NOT-APPLICABLE` -- no cell creates a schedule or grants anything, and no cell calls AWS.
`comp-adversary`: `RUN` per cell, on each order's record face.

## The issuer's acts in and after the drain

1. **To `4.0.0_SA_CRO`, at `BF-u-1`'s drain:** the sort and the drafted entries, as paths. Each commit of entries that seat names
   is read at the close.
2. **`BF-u-7`'s spawn prompt** carries identity, worktree and the pointer to the WORKER FACE only: no command for the check.
3. **Hygiene at each merge:** `python -m pytest lib/tests -q`, every `lib/tests/test_opal_naming_*.py` script, `.tools/commit-gate.sh`
   on the touched files.
4. **The real run** at the close, by this seat: `census --all-roots` over whatever the map then covers, committed under
   `deliverables/2.0.0_SA_COO~G/`; holes on newly mapped roots are the next round's data, reported whole by class.
