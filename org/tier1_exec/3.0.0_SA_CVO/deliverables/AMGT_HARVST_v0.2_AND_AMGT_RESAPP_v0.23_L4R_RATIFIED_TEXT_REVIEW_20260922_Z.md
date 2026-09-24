# L4-R review -- AMGT_HARVST v0.2 and AMGT_RESAPP v0.23, ratified-text halves (`3.0.0_SA_CVO~Z`)

**One commit carries both bumps:** @`9102ccfe81`. **Delivery:** `1.0.0_SA_CTO~Z` msgs 24286, 24287 and 24288.

| PRD | ratified-text hash at HEAD | verdict |
|---|---|---|
| `org/missions/D5/AMGT/AMGT_HARVST/prd/AMGT_HARVST_PRD.md` v0.2 | `ae9dc6e891db` | **SIGN** |
| `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` v0.23 | `8d23896506dc` | **SIGN** |

Both halves were read in full at the commit. Carry items are at the end; none blocks.

## AMGT_HARVST v0.2 -- the four refusal items, each closed

- **R1, closed.** C-HV-AXIS-PROJECTION now names AMGT_RESAPP's C-ONE-STORE as the contract whose read path it
  replaces:
  - The trigger: H4 (`article_security_mention`) and H5 (`chatter_daily`) land, and both readers move to those tables
    through the SAME single adapter.
  - The old keys retire under C-FORMAT-SEQUENCE in one window, with a pair.
  - "Until then C-ONE-STORE binds as written."
  - The counterpart amendment is in AMGT_RESAPP v0.23, below, and its trigger names the same two tables.
- **R2, closed.** The hash is `sha256("<publisher_code>:<article_id>")`, with the five codes listed. It cites
  `harvest_grammar.py` `SOURCE_FOR_PUBLISHER` as the one implementation and gives the `sa:4635742` example, and it says
  "a held article is never re-fetched under a new hash".
- **R3, closed.** The tier rule is now a partition, evaluated A -> B -> C -> D with the first match winning.
  Title-without-lead is B, and D is the remainder. Walking the space of (title, lead, count, share), every point lands
  in exactly one tier.
- **R4, closed.** C-SILVER-PARQUET binds unchanged: `date=` is the FETCH date, `published_date_utc` is a column, and the
  lineage columns are carried. C-DEDUPE-BY-KEY binds, and names the fetch key and record key for both `article` and
  `listing`.

## Andrew's two new words, as they land in this half

- **Absolute only:**
  - C-HV-DAILY-DENSE lists absolute columns only. `baseline_30d_sum` and `baseline_30d_days` replace a stored mean and
    SD.
  - Breakout, z-score and normalisation are computed at serve time, and the contract quotes his words.
  - The new C-HV-ABSOLUTE-ONLY makes this bind every gold table.
  - My density question was answered on the stricter reading, and not silently: `blocks_hit` and `blocks_total` are
    stored, and the share is computed only where the tier is assigned. If Andrew reads a within-article share as
    absolute, the change note names the one-line contract change.
- **The 2026 backfill:**
  - Dense from 2026-01-01 for every security.
  - The retrieval floor is the later of the FLOOR and the WATERMARK.
  - `retrieval_mode` and `run_stamp` are on every silver row.
  - FWD-9's DONE WHEN includes the page counts printed BEFORE the run, and idempotence ("running it again adds
    nothing").
  - C-HV-EGRESS puts the backfill under his per-use word, per security.

**Rule 30:** the new and changed text types no new address. The v0.1 addresses (10 of 10 builder output) are
unchanged.

## AMGT_RESAPP v0.23 -- one hunk in this half

C-ONE-STORE gains the supersession sentence. The read path is superseded, at a stated point, by AMGT_HARVST's
C-HV-AXIS-PROJECTION:
- the trigger is the same two gold tables;
- the adapter stays the same single adapter;
- the retirement follows C-FORMAT-SEQUENCE with a pair;
- "Until then this contract binds as written".

It agrees with the HARVST text clause for clause. No other ratified line moved. The brief-half changes (stage 9's
dependency, and the 18 count) are the CRO's.

## Carry items (for the next bump; none blocks)

1. **AMGT_RESAPP C-ONE-STORE cites "AMGT_HARVST_PRD.md v0.2".** Under the provenance ruling (@`8420ba2ddc`), a pointer
   in the ratified text is `path@commit`. Pin it: `...AMGT_HARVST_PRD.md@9102ccfe81`.
2. **FWD-9 depends on Andrew's list and his per-use word.** Both are inputs he controls, so FWD-9 is not provable on
   demand until they arrive. The rule for FWD waits (Rule 27, "expressly qualified on the outcome with its reason and
   Andrew's word") wants that qualification ON the outcome itself. Add one line: "Runs on Andrew's starting list and
   his per-use word for each run (C-HV-EGRESS)."
3. **C-HV-MENTION-GRADE tier D** reads "exactly one mention". Retrieval's mention floor means zero cannot occur, so this
   is only wording: "at most one mention" makes the partition self-evidently complete.

-- `3.0.0_SA_CVO~Z`
