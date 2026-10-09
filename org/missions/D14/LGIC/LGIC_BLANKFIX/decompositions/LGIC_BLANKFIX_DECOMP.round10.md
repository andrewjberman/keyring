# LGIC_BLANKFIX decomposition -- ROUND 10, the override's audit row in its own commit, the override bound to the commit message, the nine held entries: three cells (issuer 2.0.0_SA_COO~B1, dell1; cut 2026-10-09)

**Status: CUT for one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `ledger/ROUND_ANALYSIS.round9.md` @1bd6fcf3dd (`1.0.0_SA_CTO~DELL1`) and its ADDENDUM 1 (msg 2088), on `3.0.0_SA_CVO`'s
grade BX4-AC3 MET @a73f37ba32. The laptop `1.0.0_SA_CTO` withdrew its own round-9 list (msg 2045, moved out of the ledger at
a0d1d52b5b) and ruled XA-...-3003 (a) @9f2ed0dc4f: the switch ON NOW, and round 10 cuts its two override fixes in place of the
analysis's R2 cells (msg 2050). The switch landed @4d2bfc6dfd; the FWD-6 live read is @8bff90628c (an unplaceable name refused with
its owed text, a placeable one passing, census hole=0).

**The base at this cut (9f252e010a):** the round-9 close `ALL_ROOTS_round9.txt` reads `mapped=78 hole=0 uncounted=1
counted_at_caller=17`; `pytest lib/tests` 193 passed, 1 skipped; every `lib/tests/test_opal_naming_*.py` ok;
`NAMING-GATE-SELF-TEST: PASS`; `ROOTMAP-TEST ok=True assertions=46`; `org/mcp/naming-place.enforce` PRESENT.

## Rule 24 record

Domain: the analysis's ENRICHMENT LIST E1 to E3 as amended by msg 2050 and ADDENDUM 1, by subtraction:

| item | cell | state at the cut |
|---|---|---|
| E1 (as ruled in msg 2050): the audit row committed with the commit it permits | `BF-y-1` | pending, slot `~1` |
| E2 (as ruled in msg 2050): the override bound to the commit message, forged-row negative arm (JUDGMENT) | `BF-y-2` | pending after `BF-y-1`, slot `~1` |
| E3: holes on the newly mapped roots after the CRO's entries | none | MET with no cell: the round-9 close and the switched trunk read hole=0 over 78 mapped roots |
| ADDENDUM 1 (3): the nine held entries per the CRO's round-10 rulings @acbc0d9aa6 | `BF-y-3` | pending; spawned once @acbc0d9aa6 is in the base (not on HEAD, CLOUD or box/laptop at the cut) |

Not cut: D1-W2-S1 (stands as designed, analysis R2); D1-S1 (to the tool's owner through `0.0.0_AB_MSTR~DELL1`).

Same grain; one intent each. Status vocabulary `NOT_EVALUATED`, `PASS`, `FAIL`, `REFUSED`; every cell `NOT_EVALUATED` at the cut.
**Schema this cut authors:** the tracked audit file `org/audit/naming-place-override-audit.jsonl`, one JSON line per override
(`utc`, `author`, `id`, `reason`, `names`, `msg_sha256`).

## The cells

| cell | what | serves | placement | risk | status |
|---|---|---|---|---|---|
| `BF-y-1` | safe-commit writes the audit row to the tracked JSONL and stages it into the commit it permits; the gate reads the staged row | FWD-6 | dell1 | WORLD (`.tools/` gates) | NOT_EVALUATED |
| `BF-y-2` | the row carries the message's sha256; the gate passes only a row bound to this commit's message; forged-row arm refused; age window retired | FWD-6 | dell1 | WORLD (`.tools/` gates) | NOT_EVALUATED |
| `BF-y-3` | the nine entries drafted per the CRO's tables; holes on the newly mapped roots filled or owned; mapped and hole before and after | FWD-2, FWD-7 | dell1 | LOCAL | NOT_EVALUATED |

## Dependency edges

- `BF-y-1 -> BF-y-2`: slot `~1`, same two scripts, and `msg_sha256` is the field y-1 creates.
- `BF-y-3 -> (4.0.0_SA_CRO's rulings @acbc0d9aa6 in the base)`: outside the cells; the slot is spawned when they arrive.

`fanout: 2 of 2 chains, cap 8`: slot `~1` `BF-y-1`, `BF-y-2`; slot `~2` `BF-y-3`.

## Write sets

- **Slot ~1:** `.tools/safe-commit.sh`, `.tools/naming-gate.py`, `org/audit/naming-place-override-audit.jsonl`; exercises in `~1`'s folder.
- **Slot ~2:** `~2`'s folder only (drafts; only `4.0.0_SA_CRO` writes the registry).
- Disjoint. No cell deletes or edits `org/mcp/naming-place.enforce`; every gate exercise runs in a temporary repository.

## Battery

`comp-schedule`, `comp-iam`: `DECLARED-NOT-APPLICABLE`. `comp-adversary`: `RUN` per cell, on each order's record face.

## The issuer's acts in and after the drain

1. **At slot ~1's drain:** the switch file unchanged on the trunk; no real audit row on the trunk; both gate self-tests; one `.tf`
   commit through safe-commit on the trunk's tree in a probe worktree, refused for an unplaceable name (the FWD-6 read again).
2. **At slot ~2's drain:** the entries and rows to `4.0.0_SA_CRO`, as paths.
3. **The real run** at the close: `census --all-roots`, mapped and hole before and after; `round-close-check.py`; the drain end; the
   L8 packet to `3.0.0_SA_CVO` for BY2-AC3; the one message to `1.0.0_SA_CTO~DELL1`.
