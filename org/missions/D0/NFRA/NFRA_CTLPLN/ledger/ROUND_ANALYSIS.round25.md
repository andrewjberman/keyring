# NFRA_CTLPLN -- ROUND-25 ANALYSIS (1.0.0_SA_CTO, 2026-10-16 ~04:1xZ)

**On:**
- the issuer's L8 packet `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND25.md` @a14976a438;
- `round-close-check`: MAY-CLOSE (judgment 2 graded, 0 self-graded).

**PRD:** v0.31 (ADMITTED).

## 1. FWD coverage

This seat grades nothing; the CVO grades at L9. The table enters as round 24's: REALIZED 5 (1, 3, 5, 24, 28); ADVANCED 19;
PARKED 1 (9); MOVED 3 (13, 20, 26).

**The package journey ran end to end, on a package that was NOT approved.** In order:
- `requirements.txt` did not name tabulate, and the status verb read UNKNOWN.
- The status verb then read REQUESTED, then APPROVED; polars reads REFUSED.
- Checks 1-7 passed, and this seat signed check 8.
- The wheel was released, packed and sent to dell1 by Taildrop, each send exit 0.
- dell1 verified, proved and installed it with `--no-index --no-deps` into a scratch target, then committed its receipts on
  `box/dell1` (`c25860a18b`). The received SHA-256 equals the laptop's wheel, and both pip logs hash to their receipts.
- `requirements.txt` is unchanged.

What each owed outcome now has, for the CVO to grade:

| FWD | evidence this round | the gap in round 23 it closes |
|---|---|---|
| 15 | dell1's own receipts, with pip logs whose hashes the issuer re-read, and a received SHA-256 equal to the sent file | round 23's receipt was MSTR's relay with no hash |
| 16 | the arm exercised on an absent package: UNKNOWN, REQUESTED, APPROVED, delivered; polars REFUSED | round 23 used duckdb, which was already approved |
| 17 | Andrew heard the tabulate check-8 record and approved it, verbatim (@ba2e7f6545) | `318f` |

**What the evidence does not show, stated for the grade:**
- The stand-in lane's table was never rendered. The drive asked only for the route.
- The organic arm is the negative case: dell1, dell2 and site Z each answered NONE, which the round-24 analysis made the
  expected organic result.

## 2. Rulings

1. **dell1's scratch folders (`SCRATCH2`, `SCRATCH_TARGET` under `C:\dev\_intake_tabulate_20261016\`): put to Andrew now.**
   - A recursive delete needs a human's confirmation (CLAUDE.md Agent Autonomy), so the delete is his act.
   - REC: delete. They hold one pure-Python test package, outside any git tree, and nothing reads them.
   - If he declines, the leftover is accepted as harmless and recorded. No grade depends on it.
2. **`XB-20261016T034630Z-a0a3`:** the issuer closes it from its side after the CVO's read, as the packet says.
3. **`W128-S1`:** INERT and accepted. Re-running the check with the signature is the batch's normal step.

## 3. ENRICHMENT LIST for round 26 (one issuance)

1. Wait on the CVO's L9 grade of FWD-15, FWD-16 and FWD-17. Any FWD graded short of REALIZED gets ONE cell naming the missing
   act.
2. The scratch delete on dell1, if Andrew says yes (ruling 1). It is one act by dell1's seats, not a cell.
3. FWD-14 after Andrew's sitting (`c9a4`, `b87f`). Nothing else is reachable by a seat this round.

## ADDENDUM 1 (~04:3xZ): on the CVO's L10 slug, `ADJUDICATION_v29.md` @6b85624313 (msg 109593)

- **Grades:** FWD-16 REALIZED (C-S82). FWD-17 REALIZED (C-S83). FWD-15 stays ADVANCED, one act short (C-S81).
- **Tally:** REALIZED 7 (1, 3, 5, 16, 17, 24, 28); ADVANCED 17; PARKED 1 (9); MOVED 3 (13, 20, 26); denominator 28.
- **FWD-15's missing act is accepted as the CVO states it.** The DONE WHEN names ONE package taken the whole way AND the lane's
  work then runs. Tabulate reached dell1 with receipts, but no dell1 work ran on it beyond `prove`'s import.
- **Section 3 (round-26 enrichment list) is REPLACED by:**
  1. **ONE cell, dell1.** A dell1 lane (`1.0.0_SA_CTO~DELL1` names it) imports tabulate ONLY from
     `C:\dev\_intake_tabulate_20261016\SCRATCH_TARGET` (`PYTHONPATH` set to it, otherwise isolated), renders the one read-only
     table and commits the output plus `tabulate.__file__` on `box/dell1`.
     - Pass: the table prints, and `__file__` sits under `SCRATCH_TARGET`.
     - Cross-box act, asked through `0.0.0_AB_MSTR` as a crossbox call; dell1 is asked no outside site.
  2. **Ruling 1 is RE-ORDERED.** The scratch delete is put to Andrew only AFTER cell 1's output is committed. Deleting first
     would force the install to be repeated.
  3. FWD-14 after Andrew's sitting (`c9a4`, `b87f`).
