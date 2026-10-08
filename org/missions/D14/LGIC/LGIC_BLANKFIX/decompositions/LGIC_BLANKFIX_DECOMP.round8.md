# LGIC_BLANKFIX decomposition -- ROUND 8, FWD-6 built, uncounted to 0, holes largest root first, the held entries, the README residual: five cells from the CTO's list E1 to E5 (issuer 2.0.0_SA_COO~G; cut 2026-10-08)

**Status: CUT for one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** PRD v0.2 @47ef4c98cc, ADMITTED; `ledger/ROUND_ANALYSIS.round7.md` @ec6f56562b (`1.0.0_SA_CTO`, msg 107458), on
`3.0.0_SA_CVO`'s slug (msg 107456): FWD-5 REALIZED; FWD-6 design accepted (build is round 8's); FWD-2 and FWD-7 NOT_REALIZED,
advanced; FWD-2's order ruled (uncounted to 0, then holes largest root first, then the held entries; no ceiling); the list E1 to E5;
no PRD addendum. Earlier rounds' decompositions are frozen and unchanged.

**Round 7 at this cut (measured by the issuer at the cut):** `ALL-ROOTS ok=True roots_total=87 mapped=63 unmapped=24 ... items=1600
... hole=285 carded_class_holes=205 source_bucket_holes=14 event_rule_holes=7 unknown_word_holes=0 other_holes=59 stale_hints=0
uncounted=301`; `pytest lib/tests` 194 passed; `ROOTCHECK-TEST ok=True cases=213`; `SCOPE-TEST ok=True assertions=728`;
`CADENCE-TEST ok=True cases=53`; `NAMING-GATE-SELF-TEST: PASS`; `NAMING-APPLY-GATE-SELF-TEST: PASS`; the switch file
`org/mcp/naming-place.enforce` absent; the round-7 entries file holds 24 entries with UNDECIDED fields; the root `README.md` names
`infra/logic` 0 times.

## Rule 24 record

Domain: the five items of the analysis's ENRICHMENT LIST, by subtraction from that printed list. One cell each.

| item | cell | state at the cut |
|---|---|---|
| E1 build FWD-6 (JUDGMENT) | `BF-w-1` | pending, slot `~1` |
| E2 uncounted to 0 | `BF-w-2` | pending, slot `~4` |
| E3 holes, largest root first | `BF-w-3` | pending after `BF-w-2`, slot `~4` |
| E4 land the 24 held entries | `BF-w-4` | pending, slot `~3` |
| E5 README residual | `BF-w-5` | pending, slot `~5` |

Not cut: row `S11` (the declares checker reads newly mapped roots as missing) and W1-S15 (Andrew's act); W4-S3 is the CTO's to
disposition and is read by `BF-w-3`. **The switch file `org/mcp/naming-place.enforce` is not created by any cell**: `BF-w-1` lands
the refusal with it absent; turning it on changes every seat's commits and is the CTO's to order.

Same grain; one intent each. Status vocabulary `NOT_EVALUATED`, `PASS`, `FAIL`, `REFUSED`; every cell `NOT_EVALUATED` at the cut.
**Schema this cut authors:** the residual UNCOUNTED reasons (`BF-w-2`: a closed set the cell writes into the module, each "the
repository cannot decide it" for a stated cause; the round-7 values `local`, `var`, `module`, `interpolation` are retired as residual
reasons, `bare_reasons=0`).

## The cells

| cell | what | serves | placement | risk | status |
|---|---|---|---|---|---|
| `BF-w-1` | `place()` extracted; commit and apply gates call it under `naming-place.enforce` (landed absent); arms A to G exercised (judgment, `3.0.0_SA_CVO`) | FWD-6 | laptop | WORLD (`.tools/` gates) | NOT_EVALUATED |
| `BF-w-2` | modules, vars, locals, references resolved; residual UNCOUNTED with a closed reason | FWD-2 | laptop | LOCAL | NOT_EVALUATED |
| `BF-w-3` | holes by root, largest first: registry rows drafted, cadence reader fixed, the rest owned | FWD-2 | laptop | LOCAL | NOT_EVALUATED |
| `BF-w-4` | the 24 held entries landed or named, on the current map | FWD-7 | laptop | LOCAL | NOT_EVALUATED |
| `BF-w-5` | the README types no counts or timings; linked from the root README and STEP 13 | FWD-5 (hold) | laptop | WORLD (writes under `infra/`, root `README.md`) | NOT_EVALUATED |

## Dependency edges

- `BF-w-2 -> BF-w-3`: same slot `~4`; the CTO's order (uncounted first), and newly counted names may add holes.
- `BF-w-1` and `BF-w-2`/`BF-w-3` write disjoint files (`rootcheck` and the gates; `scope`; `cadence`), no wait.
- `BF-w-3 -> (4.0.0_SA_CRO writes the rows)`, `BF-w-4 -> (4.0.0_SA_CRO writes the entries)`: outside the cells.

`fanout: 4 of 4 chains, cap 8`: slot `~4` `BF-w-2`, then `BF-w-3`; slot `~1` `BF-w-1`; slot `~3` `BF-w-4`; slot `~5` `BF-w-5`.
**Concurrency is held below the fan-out by the disk rule** (`1.0.0_SA_CTO` msg 106860: at most 3 worker worktrees across all COO
lanes until 20 GB is free; none under 10 GB). At the cut C: read 15 GB free and other COO lanes held 2 worker worktrees, so slots are
handed as worktrees free, in the order `~4`, `~1`, `~3`, `~5`.

## Write sets

- **BF-w-1:** `lib/opal_naming_rootcheck.py` and its test, `.tools/naming-gate.py`, `.tools/naming-apply-gate.py`; its exercise in `~1`'s folder.
- **BF-w-2:** `lib/opal_naming_scope.py` and its test; its checker in `~4`'s folder.
- **BF-w-3:** `lib/opal_naming_cadence.py` and its test; its rows, owned-holes list and checker in `~4`'s folder.
- **BF-w-4:** `~3`'s folder only.
- **BF-w-5:** `infra/logic/README.md`, `README.md`, `infra/logic/10_ONBOARDING_CHECKLIST.md`; its checker in `~5`'s folder.
- Disjoint across live cells. No cell writes `infra/logic/registry/**` or creates `org/mcp/naming-place.enforce`.

## Battery

`comp-schedule`, `comp-iam`: `DECLARED-NOT-APPLICABLE` -- no cell creates a schedule or grants anything, and no cell calls AWS.
`comp-adversary`: `RUN` per cell, on each order's record face.

## The issuer's acts in and after the drain

1. **To `4.0.0_SA_CRO`:** at `BF-w-3`'s drain the drafted rows, at `BF-w-4`'s the entries, as paths.
2. **At `BF-w-1`'s drain:** `org/mcp/naming-place.enforce` confirmed absent on the trunk; the repeat check and the `all` command
   re-run against the base (outputs unchanged by the extraction); both gates' self-tests.
3. **Hygiene at each merge:** `python -m pytest lib/tests -q`, every `lib/tests/test_opal_naming_*.py` script, each criterion re-run in
   the slot's worktree before the merge; the shared index checked for a `MERGE_HEAD` or staged entries before every merge.
4. **The real run** at the close, by this seat: `census --all-roots`, `hole` and `uncounted` before and after with denominators,
   committed under `deliverables/2.0.0_SA_COO~G/`.
