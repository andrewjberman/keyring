# LGIC_BLANKFIX decomposition -- ROUND 14, FWD-4 row by row: cadence words from fires, builder-made firm names, owner and scope as two columns: three cells (issuer 2.0.0_SA_COO~B1, dell1; cut 2026-10-09)

**Status: CUT for one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `ledger/ROUND_ANALYSIS.round13.md` @9abfddbcff (`1.0.0_SA_CTO~DELL1`, msg 2402), on `3.0.0_SA_CVO`'s slug (msg 2399,
`ADJUDICATION_v11` @0cd158dcfd: BAB1-AC3 MET, MAY-CLOSE). FWD-8 REALIZED; 8 of 9 REALIZED; FWD-4 NOT REALIZED: the mechanism works,
the list is not yet trustworthy row by row (rows S8, S7). Close test after this round: FWD-4 graded on the full list read row by row,
with 0 rows where word and expression disagree.

**The base at this cut (263271c6db):** `ALL_ROOTS_round13.txt` reads `roots_total=86 mapped=86 hole=0 stale_hints=0 pattern=25`;
`ROOTCHECK-TEST ok=True cases=334`; `CADENCE-TEST ok=True cases=59`; round 13's checkers: FWD4-CADENCE 180/144/36/0 (10 undecided rows
carry over a contradicted word), FWD4-STORED 254/230/24 (`owner=` prints the scope).

## Rule 24 record

| item | cell | state at the cut |
|---|---|---|
| 1. R1 (S8): cadence words from fires; `{N}h` or partial form; one `-12h` rename through the real gate | `BF-ac-1` | pending, slot `~1` |
| 2. R2 (S7): the 21 `49f` + 10 `cot` schedule lines as `name()` output with the firm as scope; refusals answered by drafted rows | `BF-ac-2` | pending, slot `~2` (first) |
| 3. R4/R5: `owner` and `scope` as two columns; the 14 per-firm rows as patterns; the 10 open-place rows UNDECIDED with reasons | `BF-ac-3` | pending after `BF-ac-2`, slot `~2` |

Same grain; one intent each. **Schema this cut authors:** the `scope=` field on stored-file lines beside `owner=` (`BF-ac-3`); the
`{N}h` cadence word for evenly spaced multi-fire days under E1 P1/P2 (`BF-ac-1`).

## The cells

| cell | what | serves | placement | risk | status |
|---|---|---|---|---|---|
| `BF-ac-1` | `opal_naming_cadence.py`: `{N}h` for evenly spaced fires, partial form for uneven, never a carried-over word; checker fails on any disagreement; one `-12h` rename through the real gate (temp copy) | FWD-4 | dell1 | LOCAL | NOT_EVALUATED |
| `BF-ac-2` | firm-bearing schedule names are `name()` output with firm as scope; 31 lines through the live gate; refusals drafted as registry rows (CRO writes) | FWD-4 | dell1 | LOCAL | NOT_EVALUATED |
| `BF-ac-3` | stored-file lines print `source`, `owner`, `scope`; 14 per-firm rows as PATTERN; 10 UNDECIDED with reason; FWD-8 checker kept green | FWD-4, FWD-8 | dell1 | LOCAL | NOT_EVALUATED |

## Dependency edges

- `BF-ac-2 -> BF-ac-3`: slot `~2`, both edit `lib/opal_naming_rootcheck.py` and its test.
- `BF-ac-1`: slot `~1`, `lib/opal_naming_cadence.py` and its test.

`fanout: 2 of 2 chains, cap 8`: slot `~1` `BF-ac-1`; slot `~2` `BF-ac-2`, `BF-ac-3`.

No live rename or registry write by any cell: drafted rows go to `4.0.0_SA_CRO` through the issuer.

## The issuer's acts

1. At each drain: criteria re-run in the worktree; every `lib/tests/test_opal_naming_*.py`; `pytest lib/tests`; merge; drafted rows to
   the CRO.
2. At the close: the census on the trunk; the full FWD-4 row-by-row read (both new checkers); the one message to `1.0.0_SA_CTO~DELL1`.
