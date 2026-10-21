# L4-R review, NFRA_OPLGTW PRD v3.16 (FWD-23 reshaped: an AWS CLI over MCP), ratified-text half -- REFUSE, one cure (3.0.0_SA_CVO~Z, 2026-10-21 ~14:2xZ)

**Asked by** `1.0.0_SA_CTO~Z` msg 36283, read. It is not acked: this seat's broker tools are disconnected.

**Supersedes:** this seat's v3.15 review @30e41b770c. v3.16 withdraws v3.15's field classes, so V1 there is moot as written.
Its substance carries into the cure below.

**Bytes reviewed:** `git diff 866ccad604 1ae82e6749` on the PRD, read whole: the FWD-23 block replaced and the v3.16
addendum. The PRD at HEAD equals the pin.

## Sources read

- **Andrew's words in the addendum:** "give menachem an aws cli over mcp ... query these folders as i do via aws cli", and
  "I agree with your rec" (keep tax ids, addresses, email and phone out). The scope he set for Menachem
  (opal-data-assets, opal-data-etfs, opal-data-portal-v2) is in the 10-21 record, read earlier.
- **`data/assets/scripts/silver/schwab_schemas.py:8`:** `opal-data-assets/schwab/08335338/bronze` holds the raw vendor
  extracts that the silver is parsed from.
- **The same module's pinned silver columns:**
  - `ssn_tin_number` (`:144`);
  - `mailing_address_line_1..3` (`:91-93`);
  - `email_address` (`:98`);
  - `phone_nbr` (`:99`) and `mobile_phone_number` (`:161`);
  - `date_of_birth` (`:155`).

## What is right

- **It is his shape:** list and read over three buckets, reusing `harvest_read.py` and the Schwab engine, with no typed
  contract.
- The allowed prefixes are a list in code, built by the builder (rule 30).
- The proof has teeth: 19 tables listed per master, a `fact_trn` row-count equality on a trade-date range, a `fact_acc` name
  search, and a 0-read negative arm.
- The reader IAM is its own never-widen act.

## Verdict: REFUSE

There is one cure, text-only.

### V1 (blocking): the forbidden fields are dropped only "by column name", but the tool reads ANY object, so raw files carry them out

**The leak.**
- ACCEPT says: "Dropped at read, by column name ... tax identifiers, mailing addresses, email addresses, phone numbers."
- DONE WHEN says: read "any object there: Parquet as rows ...; JSON parsed; text as text".
- A column drop works on Parquet rows. It does nothing to a text read of `opal-data-assets/schwab/<master>/bronze/...`,
  the raw vendor extracts the silver is parsed from, which carry the same identifiers in fixed-width text.
- It also does nothing to a JSON object that carries them under other keys.
- As written, the exclusion Andrew agreed to ("I agree with your rec") holds for silver and leaks through bronze.

**The cure.**
1. **The forbidden fields are dropped on EVERY read path:**
   - Parquet by column;
   - JSON by key;
   - delimited text by header column.
2. **An object whose format the tool cannot filter is refused on any prefix that can hold them,** or those prefixes (the
   vendor `bronze` and raw folders) are left out of the allowed prefix list. The simpler of the two is the issuer's
   choice. Excluding raw prefixes keeps "as i do via aws cli" for every curated layer.
3. **The drop list is matched against the source's actual names, not typed words:** `ssn_tin_number`, any `tax_id`
   form, `mailing_address_line_*`, `email_address`, `phone_nbr` and `mobile_phone_number`. It is generated from the
   converter's pinned schemas and the other vendors' schemas.
4. **Add a negative arm to the proof:**
   - a planted column of each forbidden kind is dropped on a Parquet read and on a JSON read;
   - a read of a raw text extract on an allowed prefix is refused, or that prefix is not listable.

## Noted, not grounds

- **`date_of_birth` is not in the four.** With CLI parity as his word, it is served. That is consistent with "as i do via
  aws cli", and it is a client personal-data field.
- If the CTO thinks he would want it out with the other four, one line to him settles it. It is not this seat's call, and
  it does not block.

## Not graded here

- The reader IAM over the prefixes.
- The per-firm client grant shape.
- Round 48's decomposition.

-- 3.0.0_SA_CVO~Z
