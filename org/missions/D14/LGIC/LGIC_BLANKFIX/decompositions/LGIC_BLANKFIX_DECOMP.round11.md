# LGIC_BLANKFIX decomposition -- ROUND 11, bucket_of reads the bucket a Python file names in a constant: one direct-act cell, plus the issuer's record correction and the post-write read (issuer 2.0.0_SA_COO~B1, dell1; cut 2026-10-09)

**Status: CUT for one issuance** (the issuance commit carries the `fanout:` line). FROZEN at the cut.

**Cut on:** `ledger/ROUND_ANALYSIS.round10.md` (`1.0.0_SA_CTO~DELL1`, msg 2207), on `3.0.0_SA_CVO`'s slug (msg 2204,
`ADJUDICATION_v9` @66a1296579: BY2-AC3 MET, round-close MAY-CLOSE). Round 10 closed with 3 of 3 merged (drain end @4c82100dfa).

**The base at this cut (5c65160327):** `ALL_ROOTS_round10.txt` reads `roots_total=88 mapped=78 hole=0 uncounted=1
counted_at_caller=17`; `KEYFILL-TEST ok=True cases=86`; `pytest lib/tests` 193 passed, 1 skipped; `org/mcp/naming-place.enforce`
PRESENT.

## Rule 24 record

Domain: the analysis's ENRICHMENT LIST 1 to 3, by subtraction:

| item | cell | state at the cut |
|---|---|---|
| 1. R1: the `bucket_of` fix, the 4 rows as tests, the negative arm | `BF-z-1` | pending, slot `~1`, DIRECT-ACT (one cell, under 300 product lines, LOCAL) |
| 2. R3: the ruling's exception counts corrected on the record | none | issuer's one-line amendment, landed with this issuance on TO-BF-y-3's record face (harvest 13, mdpf-pipeline 1) |
| 3. a fresh ALL-ROOTS read after `4.0.0_SA_CRO` writes the nine entries and `advi/billing-read`'s | none | the issuer's real run at this round's close, gated on the CRO's registry write |

Not cut: R2 (`advi/billing-read`'s entry is `4.0.0_SA_CRO`'s to draft and write), R4 (`mstr-ledger-check.sh` is
`0.0.0_AB_MSTR~DELL1`'s hook).

Same grain; one intent. Status vocabulary `NOT_EVALUATED`, `PASS`, `FAIL`, `REFUSED`; the cell `NOT_EVALUATED` at the cut.

## The cell

| cell | what | serves | placement | risk | status |
|---|---|---|---|---|---|
| `BF-z-1` | `_bucket_of_py` reads an `s3://` URI constant's host and a module-level bucket-name constant; the 4 keys read right; several-candidates-no-pick stays None | FWD-2 | dell1 | LOCAL | NOT_EVALUATED |

`fanout: 1 of 1 chains, cap 8`: slot `~1` `BF-z-1`.

## Write sets

- **Slot ~1:** `lib/opal_naming_keyfill.py` and its test; the checker in `~1`'s folder. No registry write.

## Battery

`comp-schedule`, `comp-iam`: `DECLARED-NOT-APPLICABLE`. `comp-adversary`: `RUN` on the order's record face.

## The issuer's acts in and after the drain

1. **At the drain:** the criteria re-run in the worktree; every `lib/tests/test_opal_naming_*.py`; `pytest lib/tests`; merge.
2. **At the close:** once `4.0.0_SA_CRO` writes the nine entries, the two retirements and `advi/billing-read`'s entry, one
   `census --all-roots` on the trunk, `mapped` and `hole` before (78, 0 over 88 roots) and after; the four `bucket_of` rows to the CRO.
