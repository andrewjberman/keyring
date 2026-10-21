# L4-R review, NFRA_OPLGTW PRD v3.18 (FWD-23 the AWS-CLI shim, FWD-24 folder entitlement), ratified-text half -- REFUSE, one cure (3.0.0_SA_CVO~Z, 2026-10-21 ~15:1xZ)

**Asked by** `1.0.0_SA_CTO~Z` msgs 36292 and 36295 (files 145443Z and 145501Z), read. They are not acked: this seat's
broker tools are disconnected.

**Bytes reviewed:** `git diff 0723d15aa8 1b5bf86827` on the PRD, read whole: FWD-23, FWD-24 and the v3.18 addendum. The PRD
at HEAD equals the pin.

## Sources read

- **The CTO's endpoint draft,** `ENDPOINT_DRAFT_MCP_CLI_SHIM_20261021_Z.md` @08c62c6f21, `:44-51`. Andrew's call 1 put the
  REC "keep the four classes plus date of birth out, by column name in Parquet, and keep bronze out of every grant".
  - His answer, "sure, keep the Tax IDs and so on", reads with the REC: the five classes stay OUT, and bronze is in no
    grant.
  - That is the reading the addendum records, and it answers both of this seat's v3.15 and v3.16 points.
- **The SOURCE quotations** in FWD-23 and FWD-24 are as recorded.

## What is right

- **It is his shape:** list, describe, query; one page or a total, never a dump; a cursor; the engine's memory and time
  ceilings; no caller string as SQL outside the engine's closed grammar.
- **The proof is exercised and has teeth:**
  - a row-count equality against a direct read;
  - the 1.53M-row Orion file never loaded whole;
  - Cottonwood dates parsed;
  - refusal by folder name with 0 reads.
- The first cut is Schwab, Orion and Cottonwood Black Diamond, and the rest are deferred by name.
- The typed tools retire only after FWD-23 is proven. That is his "Sure".
- FWD-24 is the entitlement he described, a bucket or a folder per person, with the superseded clauses named.

## Verdict: REFUSE

There is one cure, text-only.

### V1 (blocking): FWD-24's proof grants the whole `opal-data-assets/` bucket, which contains bronze, while FWD-23 says "bronze is in no grant"

- FWD-23 ACCEPT says "bronze is in no grant".
- FWD-24 DONE WHEN says "the owner grants Menachem `opal-data-assets/`, `opal-data-etfs/` and `opal-data-portal-v2/` in one
  act; he reads under them".
- `opal-data-assets/schwab/<master>/bronze/` holds the raw vendor extracts (`schwab_schemas.py:8`). Those carry the tax ids,
  addresses, email, phone and date of birth that the column drop removes only from Parquet.
- As written, a whole-bucket grant reaches bronze, and FWD-24's own proof writes exactly that grant. The two outcomes
  contradict each other, and the exclusion Andrew agreed to depends on which one the builder reads.

**The cure.**
1. **State the mechanism in FWD-24:** a bucket or folder grant NEVER reaches a `bronze/` or raw prefix. The shim's prefix
   check excludes them for every principal, and the reader IAM grants no bronze prefix, so granting `opal-data-assets/`
   means "the bucket minus bronze".
2. **Add the negative arm to FWD-24's proof:** under Menachem's whole-bucket grant, a `list` or `query` under
   `opal-data-assets/schwab/<master>/bronze/` is refused by folder name with 0 reads.

## Noted, not grounds

- **"Dropped by column name" must match the sources' actual names, generated rather than typed:**
  - Schwab's `ssn_tin_number`, `mailing_address_line_1..3`, `email_address`, `phone_nbr`, `mobile_phone_number` and
    `date_of_birth` (`schwab_schemas.py:91-161`);
  - Orion's and Black Diamond's equivalents.
- One planted column of each class per vendor, dropped on a query and on a describe, is the cheap test. That is for the
  decomposition.

## Not graded here

- The reader IAM (its own never-widen act).
- NFRA_MCPINDEX FWD-26.
- The MCPORTAL folder switch.

-- 3.0.0_SA_CVO~Z
