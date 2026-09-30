# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 28, `HVST-aa-3` (the served bbg silver `article` rebuild on `q-2`'s parse) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~10:2xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round28/NEVER_WIDEN_HALF_COO_AA3.md` @`bdbae7c371` (msg 27082, READ-acked; read to EOF,
3,348 B).
**Ruling it serves:** `ROUND_ANALYSIS.round27.md` ruling 4, as superseded @`803ea38a9e`.

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT (S3 read in process, independent of `aa3_common`)

| what | COO half | this seat |
|---|---|---|
| bbg silver `article` parts | 30 | **30** |
| bbg bronze `article` objects | 30 | **30** |
| served rows / distinct `article_key` | 30 | **30 / 30** |
| empty (`text` blank) | 11, keyed `bbg:<hash>` | **11** (for example `bbg:0685726bc294db72f8354585`) |
| bbg pairs in the served mention snapshot (`part-20260930T062354Z`) | 32 | **32** |
| of which on an empty row | 0 | **0** |
| of which with no silver row | -- | **0** |

- **The predecessor-code question (this seat's y-4 AMENDMENT 1 discipline) is answered by the COO's own instrument.** The signing
  dry run applies TODAY's `silver_from_bronze` code to every bronze object and filters the output against the SERVED rows the way
  `silver_append` does. So any drift since the 19 non-empty rows were built would show up as extra rows. It reads exactly 11.
  Accepted as the write-path trace.
- **Read path:** `/timeline/day` reads silver only for keys in the mention snapshot, and the snapshot carries none of the 11 empty
  keys. This act does not rebuild the snapshot, so no served page moves.

## 2. CONDITIONS

1. **The act-start gate** (`aa-3.signing.py` without `--signing`) reads equal on parts, bronze, the latest hashes and the expected
   write (11 rows, 1 put), or STOP.
2. **After the act:** `aa-3.AC1.py` and `aa-3.AC2.py` pass.
   - served keys read 41, and the 30 pre-existing keys are byte-unchanged;
   - the 11 NEW rows are non-empty;
   - 0 mention pairs sit on an empty row.
   - **Any served list reaching an empty row is a STOP** (ruling 4).
3. **Ordering with cell 2 (the fresh-day run):** the two WORLD acts do not overlap. Whichever pair signs first runs first; the
   other's act-start gate then re-reads its before-state.

## 3. ROLLBACK

Forward only. Every put is never-overwrite. A delete is Andrew's act.

## 4. NOT COVERED

- the mention rebuild (the NEW rows add bbg pairs only when it runs, under its own pair);
- any other publisher's silver;
- any gold table.
