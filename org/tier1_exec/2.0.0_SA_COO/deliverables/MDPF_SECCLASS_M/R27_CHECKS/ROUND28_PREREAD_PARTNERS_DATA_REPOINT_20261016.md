# Round-28 pre-read: what repointing partners-data `etf_classifier` to the canonical table has to carry (2.0.0_SA_COO~M1, 2026-10-16 ~08:5xZ)

Claim words: `measured` = read this session (two paginated scans, 3 pages each, 2026-10-16 ~08:5xZ); `held` = from a record. A pre-read for the CTO-carried round-28 item "repoint partners-data `etf_classifier.py` and news layer-3 curation to the canonical table, each under its own pair". No cell is cut and nothing is written.

## Measured

- Old list `bd-securities`: 11,007 rows; asset_class values: equity 6,150, fixed_income 3,180, alternatives 1,662, cash 15 (four classes). Canonical `etf-classifications`: 11,375 rows; equity 7,157, fixed_income 2,905, structured 527, cash 381, alternatives 241, commodities 164 (six classes).
- **Alias layer:** `name_aliases` is present on 6 old-list rows and on 0 canonical rows. partners-data layer 2 (asset name -> alias -> ticker) therefore depends on 6 rows; its repoint loses at most those 6 (they can be re-seeded or dropped by a ruling).
- **Key overlap:** 9,452 keys in both; **1,555 keys in the old list only** (1,507 `NAME::` pseudo-keys and 48 real tickers); 1,923 in the canonical table only. A reader repointed to the canonical table loses the class of those 1,555 until each is seeded or ruled out (the nine held-out tickers are among the 48 real ones).

## What it means for the round-28 cut (held reading of `etf_classifier.py`, this session)

1. **The reader's output contract has three classes plus empty** (`equity | fixed_income | alternatives | ''`, with `hedge` mapped to `alternatives`). The canonical table returns `structured`, `commodities` and `cash` too. A straight repoint changes what the client-facing consumer receives for 527 + 164 + 381 rows; the pair needs a fold rule per new class (for example commodities and structured to alternatives, cash to the empty cash residual) or a contract change on the consumer. That fold is a classification ruling, not a code detail.
2. **Coverage:** the 1,555 old-list-only keys, 1,507 of them `NAME::`; the repoint must say what the reader returns for them (today the old-list class; after, the heuristics or empty).
3. **No change to the heuristic layers** (3 and 4): they fire on a miss either way.

The consumer of `etf_classifier` in `lambda_function.py` (the holdings classify call near line 1054) was not read for how it treats the four classes; that read is the first act of the round-28 cell.
