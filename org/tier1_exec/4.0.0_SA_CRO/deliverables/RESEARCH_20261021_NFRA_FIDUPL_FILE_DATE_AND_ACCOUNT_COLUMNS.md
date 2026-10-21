# RESEARCH 2026-10-21 -- NFRA_FIDUPL: the as-of date column and account-number column, per custom file (0-based)

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1). **Answers:** 2.0.0_SA_COO~P1 msg 8890.
**Verified locally** on Andrew's own custom exports held on dell1 (`account.txt`, `prices.txt`); the other four custom files
(`position.txt`, `balance.txt`, `transact.txt`, `security.txt`) I do NOT have -- those lines ENDORSE the COO's box measurement with the
discriminating reasoning. Values are not printed.

## As-of / content date column (0-based)

| File | date field | source |
|---|---|---|
| `position.txt` | **0** | COO box measure; matches the date-first shape of prices/security |
| `prices.txt` | **0** | **verified local** (field 0 is the business date; every row) |
| `security.txt` | **0** | COO box measure |
| `account.txt` | **16** | **verified local**: field 16 is a SINGLE value across all 5,007 rows (the file's as-of). **field 3 is a DIFFERENT, per-account date** (1,352 distinct) -- do not use field 3. |
| `balance.txt` | **3** | COO box measure (constant over rows); endorsed -- a balances file's as-of is the constant date field |
| `transact.txt` | **17** | COO box measure (2 distinct); **endorsed, and a warning:** fields 52 and 57 are per-ROW dates (trade/settle, many distinct) -- they are NOT the file as-of. Field 17 (low-distinct = the run's business date) is the correct content date. |

**Rule the lander can apply:** the file's as-of/content date is the date field that is **constant (or lowest-distinct) across the file**,
not a per-row date. That picks field 0 / 16 / 3 / 17 correctly and rejects transact's 52/57.

## Account-number column (0-based)

| File | grain | account column |
|---|---|---|
| `account.txt` | account | **0** -- **verified local**: field 0 matches 5,007 of 5,007 accounts in the book |
| `position.txt` | account x security | account-grain; **confirm on the box** as the field whose values match the account set (~4,900 distinct). I lack the file. |
| `balance.txt` | account | same -- confirm by account-set match on the box |
| `transact.txt` | account x txn | same -- confirm by account-set match on the box |
| `prices.txt` | security | **none** -- **verified local**: no account column (date, security type, symbol, cusip...) |
| `security.txt` | security | **none** -- security-grain, no account |

For the three I cannot see, the sound method is the one the COO already used for the date: **the account-number column is the field whose
distinct values match the book's account set** (the ~4,900-5,000 numbers in `account.txt` field 0 / the `.naa` set). That is
deterministic and needs no vendor spec.

## Firm attribution (the gap already tracked)

None of the six custom files carries a G number or firm code (measured earlier,
`RESEARCH_20261019_NFRA_FIDUPL_ACCOUNT_TXT_AND_FIRM_SPLIT.md`). Firm split comes from the per-G `accountList.json` map built by switching
the G Number in the session, not from a column in these files.

## Not measured

- The exact account-column index in `position.txt`, `balance.txt`, `transact.txt` (files not on dell1; confirm by account-set match on
  the box).
