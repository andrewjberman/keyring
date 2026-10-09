# LGIC_BLANKFIX decomposition -- ROUND 9, the H8 rule, the S12 fixtures, the switch-on wiring and its override, counted at the caller, the newly mapped roots: six cells from the CTO's list E1 to E6 (issuer 2.0.0_SA_COO~B1, dell1; cut 2026-10-09)

**Status: CUT for one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `ledger/ROUND_ANALYSIS.round8.md` @2ba21c4271 (`1.0.0_SA_CTO`, laptop; relayed by `0.0.0_AB_MSTR~DELL1` msg 1674), on
`3.0.0_SA_CVO`'s slug (msg 107715): FWD-6 BUILT and graded (BW1-AC4 MET), switch absent; FWD-2 and FWD-7 NOT_REALIZED, advanced;
rulings on W1-S22 (fixed @b82324057e), H8, W4-S6, S12 and W1-S19/S20/S21; the list E1 to E6; no PRD addendum. E6's wait on
`4.0.0_SA_CRO` is lifted: the 15 round-8 entries landed @1e660e15be (msg 1679). Placement DELL1 @ca565d1871. Earlier rounds'
decompositions are frozen and unchanged.

**The base at this cut (9d55470156, measured by the issuer):** `ALL-ROOTS ok=True roots_total=87 mapped=78 unmapped=9 completed=78
stopped=0 items=2259 right=554 fix=1457 not_asked=174 pattern=23 carded=0 refused=0 hole=51 carded_class_holes=33
source_bucket_holes=0 event_rule_holes=0 unknown_word_holes=6 other_holes=12 stale_hints=0 uncounted=17` (the 17 all
`module-input`); `pytest lib/tests` 193 passed, 1 skipped; `ROOTCHECK-TEST ok=False cases=319` (case 5, row S12);
`FWD6-ARMS ok=False arms=7 held=5` (F: the HOLE the fixture relied on is closed; G: run without `NAMING_PLACE_PREVIEW=1`);
`SCOPE-TEST ok=True assertions=831`; `CADENCE-TEST ok=True cases=59`; `NAMING-GATE-SELF-TEST: PASS`;
`NAMING-APPLY-GATE-SELF-TEST: PASS`; `org/mcp/naming-place.enforce` absent.

## Rule 24 record

Domain: the six items of the analysis's ENRICHMENT LIST, by subtraction from that printed list. One cell each.

| item | cell | state at the cut |
|---|---|---|
| E1 H8 rule: NOT-GRADED -> NOT-ASKED | `BF-x-1` | pending after `BF-x-2`, slot `~1` |
| E2 S12 fixtures in the overlay | `BF-x-2` | pending, slot `~1` (first) |
| E3 switch-on wiring (W1-S19, W1-S20) | `BF-x-3` | pending, slot `~2` |
| E4 the override (W1-S21, arm H) (JUDGMENT) | `BF-x-4` | pending after `BF-x-3`, slot `~2` |
| E5 counted at the caller (W4-S6) | `BF-x-5` | pending after `BF-x-1`, slot `~1` |
| E6 holes on the newly mapped roots | `BF-x-6` | pending, slot `~3` |

Not cut (the analysis's "Not in round 9"): the 9 held entries; W4-S7, W4-S8, W5-S2 (with `4.0.0_SA_CRO`). Row `LGIC_BLANKFIX-D1-S1`
(round-close-check reads a suffixed `complete` status as open) is an instrument row outside this decomposition. **No cell creates
`org/mcp/naming-place.enforce`**: the CTO rules the switch-on after E3 and E4 land and are graded.

Same grain; one intent each. Status vocabulary `NOT_EVALUATED`, `PASS`, `FAIL`, `REFUSED`; every cell `NOT_EVALUATED` at the cut.
**Schema this cut authors:** the census line kind `COUNTED-AT-CALLER` and the ALL-ROOTS field `counted_at_caller` (`BF-x-5`), and
the commit-message line `# naming-place-override: <reason>` with its audit log `org/naming-place-override-audit.log` (`BF-x-4`).

## The cells

| cell | what | serves | placement | risk | status |
|---|---|---|---|---|---|
| `BF-x-1` | `decide()` maps NOT-GRADED to NOT-ASKED; the 10 H8 names read NOT-ASKED | FWD-2 | dell1 | LOCAL | NOT_EVALUATED |
| `BF-x-2` | ROOTCHECK-TEST case 5 and arm F plant their HOLE in the overlay; arm G with `NAMING_PLACE_PREVIEW=1` | FWD-6 | dell1 | LOCAL | NOT_EVALUATED |
| `BF-x-3` | safe-commit and safe-apply act on the placement refusal under `naming-place.enforce`; plan gate gets its tree | FWD-6 | dell1 | WORLD (`.tools/` gates) | NOT_EVALUATED |
| `BF-x-4` | one audited override for the placement step; arms with/without; judgment for `3.0.0_SA_CVO` | FWD-6 | dell1 | WORLD (`.tools/` gates) | NOT_EVALUATED |
| `BF-x-5` | the 17 `module-input` names print COUNTED-AT-CALLER; `uncounted` reads the rest | FWD-2 | dell1 | LOCAL | NOT_EVALUATED |
| `BF-x-6` | holes on the 15 newly mapped roots, largest root first: rows drafted, the rest owned | FWD-2, FWD-7 | dell1 | LOCAL | NOT_EVALUATED |

## Dependency edges

- `BF-x-2 -> BF-x-1 -> BF-x-5`: slot `~1`, file contention on `lib/tests/test_opal_naming_rootcheck.py` (and `rootcheck.py` for
  x-1 and x-5), and a real one: x-1's and x-5's criterion is ROOTCHECK-TEST, red at the base until x-2 repairs case 5.
- `BF-x-3 -> BF-x-4`: slot `~2`, the CTO's chain; both edit `.tools/safe-commit.sh` and `.tools/naming-gate.py`.
- `BF-x-6`: slot `~3`, no edge. It does not wait on `BF-x-1`: a NOT-GRADED name is listed under that cell, never drafted a row.
- The analysis's "E6 waits on the CRO's write" is met @1e660e15be.

`fanout: 3 of 3 chains, cap 8`: slot `~1` `BF-x-2`, `BF-x-1`, `BF-x-5`; slot `~2` `BF-x-3`, `BF-x-4`; slot `~3` `BF-x-6`. Disk on
dell1 at the cut: 1.7 TB free; no concurrency hold.

## Write sets

- **Slot ~1 (x-2, x-1, x-5):** `lib/opal_naming_rootcheck.py`, `lib/tests/test_opal_naming_rootcheck.py`; the arms file and checkers in `~1`'s folder.
- **Slot ~2 (x-3, x-4):** `.tools/safe-commit.sh`, `.tools/safe-apply.sh`, `.tools/naming-gate.py`, `.tools/naming-apply-gate.py`,
  `org/naming-place-override-audit.log`; exercises in `~2`'s folder.
- **Slot ~3 (x-6):** `lib/opal_naming_cadence.py` and its test; rows, owned list and checker in `~3`'s folder.
- Disjoint across slots. No cell writes `infra/logic/registry/**` or creates `org/mcp/naming-place.enforce`. Every slot may append to
  the investigation file; the drain resolves its conflicts by row union.

## Battery

`comp-schedule`, `comp-iam`: `DECLARED-NOT-APPLICABLE` -- no cell creates a schedule or grants anything, and no cell calls AWS.
`comp-adversary`: `RUN` per cell, on each order's record face.

## The issuer's acts in and after the drain

1. **To `4.0.0_SA_CRO`:** at `BF-x-6`'s drain, the drafted rows as a path.
2. **At slot ~2's drain:** `org/mcp/naming-place.enforce` confirmed absent on the trunk; `org/naming-place-override-audit.log` holds no
   exercise row; both gates' self-tests; one ordinary `.tf`-free commit and one `.tf` commit through safe-commit with the switch absent
   (no new block, the PLACE-NOTICE line only).
3. **Hygiene at each merge:** `python -m pytest lib/tests -q`, every `lib/tests/test_opal_naming_*.py` script, each criterion re-run in
   the slot's worktree before the merge; `safe-merge.sh` only with no `MERGE_HEAD` and no staged entries in the shared index.
4. **The real run** at the close, by this seat: `census --all-roots`, `hole`, `uncounted` and `counted_at_caller` before and after
   with denominators, saved as `deliverables/2.0.0_SA_COO~B1/ALL_ROOTS_round9.txt`; `round-close-check.py`; the drain-end file; the
   L8 packet; the one message to `1.0.0_SA_CTO`.
