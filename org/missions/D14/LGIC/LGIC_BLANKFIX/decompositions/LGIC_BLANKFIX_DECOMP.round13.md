# LGIC_BLANKFIX decomposition -- ROUND 13, the two never-served outcomes: FWD-4 (schedules, stored files) and FWD-8 (patterns, whole list): three cells (issuer 2.0.0_SA_COO~B1, dell1; cut 2026-10-09)

**Status: CUT for one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `ledger/ROUND_ANALYSIS.round12.md` @b45108c324 (`1.0.0_SA_CTO~DELL1`, msg 2324), on `3.0.0_SA_CVO`'s slug (msg 2323,
`ADJUDICATION_v10` @4573027c4e). The coverage read: FWD-1, 2, 3, 5, 6, 7, 9 REALIZED; **FWD-4 and FWD-8 NOT REALIZED -- never served**;
LGIC_BLANKFIX does not close. PRD `prd/LGIC_BLANKFIX_PRD.md` FWD-4 (lines 51-57), FWD-8 (lines 85-90), C-CADENCE (line 118).

**The base at this cut (b89f2f09c4):** `ALL_ROOTS_round12.txt` reads `roots_total=86 mapped=86 unmapped=0 hole=0 stale_hints=0
uncounted=1 pattern=25`; `ROOTCHECK-TEST ok=True cases=324`; the list already prints a schedule's new name with a cadence word
(`FIX EVENT_RULE bd-49f-keepalive-sched -> blackdiamond-49f-keepalive-sched-15min`) and a stored file's new location
(`FIX S3Key code/silver/... -> blackdiamond/49financial/code/silver/...`), but no stored-file line states its source and owner in
words, and no cell has ever EXERCISED either outcome.

## Rule 24 record

| item | cell | state at the cut |
|---|---|---|
| 1. FWD-4 group C: the schedules (cadence word against the expression; one renamed from the list alone) (JUDGMENT) | `BF-ab-1` | pending, slot `~1` |
| 2. FWD-4 group D: the stored files (source and owner; one move read from the list alone) | `BF-ab-2` | pending, slot `~2` (first) |
| 3. FWD-8: the whole list read, every pattern shown as a pattern, negative arm | `BF-ab-3` | pending after `BF-ab-2`, slot `~2` |

Not cut: R2's rows (with the CVO, the round-close-check owner via `0.0.0_AB_MSTR~DELL1`, and their named owners).

Same grain; one intent each. **Schema this cut authors:** the `source=<system> owner=<firm or system>` fields on stored-file lines
(`BF-ab-2`), with `UNDECIDED` as the value a ruling does not decide.

## The cells

| cell | what | serves | placement | risk | status |
|---|---|---|---|---|---|
| `BF-ab-1` | every schedule's cadence word read against its own expression (undecided listed); one schedule renamed from its list line alone in a temporary copy, graded CONFORMANT by the real gate; CVO judgment | FWD-4 | dell1 | LOCAL | NOT_EVALUATED |
| `BF-ab-2` | stored-file lines state source and owner from the ruling or key class (UNDECIDED otherwise); one move read from the list alone, none applied | FWD-4 | dell1 | LOCAL | NOT_EVALUATED |
| `BF-ab-3` | the whole list read: every code pattern shown as PATTERN, none as a name; negative arm | FWD-8 | dell1 | LOCAL | NOT_EVALUATED |

## Dependency edges

- `BF-ab-2 -> BF-ab-3`: slot `~2`, both may edit `lib/opal_naming_rootcheck.py` and its test.
- `BF-ab-1`: slot `~1`, `lib/opal_naming_cadence.py` and its test; no edge.

`fanout: 2 of 2 chains, cap 8`: slot `~1` `BF-ab-1`; slot `~2` `BF-ab-2`, `BF-ab-3`.

No live rename and no S3 move is any cell's act: a live schedule rename is a deploy, and a stored file's move is a data act, each with
its own pair. FWD-4's DONE WHEN ("renamed from the list alone") is exercised on a temporary copy through the real gate (C) and as a read
of the list line (D).

## The issuer's acts

1. At each drain: criteria re-run in the worktree; every `lib/tests/test_opal_naming_*.py`; `pytest lib/tests`; merge.
2. At the close: the census on the trunk (hole stays 0); the L8 packet to `3.0.0_SA_CVO` for BAB1-AC3; the one message to
   `1.0.0_SA_CTO~DELL1`.
