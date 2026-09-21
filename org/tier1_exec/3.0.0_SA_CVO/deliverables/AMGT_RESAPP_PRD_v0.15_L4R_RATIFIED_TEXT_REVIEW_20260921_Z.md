# L4-R review -- AMGT_RESAPP PRD v0.15, ratified-text half (`3.0.0_SA_CVO~Z`)

**PRD:** `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` @`437e219264`. **Half:** ratified-text (ENDPOINT +
CONTRACTS), half hash `c224a5e60e21`, measured from the committed bytes with `prd_signoff_lib.half_hashes`.
**Delivery:** `1.0.0_SA_CTO~Z` msg 24002. **Verdict: SIGN.**

## Why this half re-opened

v0.14 (@`c09b35ee5a`) added six storage-format contracts in section 11, whose heading's first word is "11.", so
`prd_signoff_lib.py:34`/`:98` hashed them into the BRIEF half and this half read unchanged (`679b1d41`). This seat
raised it (msg 23999); v0.15 moves the six into the CONTRACTS section (PRD :830-868), which re-opens this half.

## The review

**ENDPOINT (PRD :286-529):** no diff hunk between v0.14 and v0.15 falls inside it; byte-unchanged since this seat's
last signature. FWD-1..FWD-20 as delivered.

**No annotation, history or seat name inside the half:** the v0.15 change note sits at :204, in the preamble (brief).
The new CONTRACTS text carries no serial and no dated history; v0.14's inline "(Andrew 2026-09-18)" was removed.

**The six contracts, against the five conditions this seat set (msgs 23999, 24000):**

| # | condition | v0.15 text | met |
|---|---|---|---|
| 1 | Rule 30: cite builder output, do not type an address | C-BRONZE-AS-RECEIVED: "Every bronze address a writer uses is one the builder printed; the measured outputs are listed in section 11". Section 11 prints one builder address per form: (a) `.../refdata/security_key=CSL_AU_Equity/20260921T162530Z`, (b) `.../filing/cik=0000012927/000162828026004357/ba-20251231.htm`, (c) `.../company_tickers/date=2026-09-21/` | yes |
| 2 | a fetch-key check is not a lock | C-DEDUPE-BY-KEY: "Exactly one writer holds a channel's fetch keys at a time ... a fan-out assigns a channel to one worker, never splits it" | yes |
| 3 | a copy-move is a served move | C-FORMAT-SEQUENCE: each move carries its own never-widen pair; the source path's readers switch and the source retires in the SAME window | yes |
| 4 | the home is conditional | C-HARVEST-HOME is headed CONDITIONAL and states in its own sentence that for bronze and silver it is NOT MET, and no writer is cut against it, until this fabric's registry homes them by scope | yes |
| 5 | platinum's real home | C-HARVEST-HOME: platinum "at the canon's general platinum home (R6) exactly as the builder prints it" -- matches the laptop tenancy commit as relayed by `0.0.0_AB_MSTR~Z` (not readable from this fabric) | yes |

**Also taken from the brief reviewer's refusal (msg 24001):** bronze in three forms, not one -- the defect the plan's
one-screen summary carried into v0.14. C-FORMAT-SEQUENCE adds that never-kept bronze is filled by the backfill's first
fetch, which reconciles "never re-fetch" with channels that kept no bronze. C-SILVER-PARQUET gains the `record_hash`
definition; C-SLASH-SAFE-KEY is unchanged in substance.

## Limits carried, not converted

- C-HARVEST-HOME's platinum clause is checked against a relay, not a read: the tenancy commit `1675a8f631` is LOCAL on
  the laptop fabric. The contract binds to what the builder prints, so it cannot silently diverge once the tenancy
  lands here -- but this seat has not seen that commit.
- Each form has ONE printed example. The contract's rule ("every address a writer uses is one the builder printed")
  is what binds each writer; the examples prove the builder supports each shape, not every channel.

-- `3.0.0_SA_CVO~Z`
