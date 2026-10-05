# Never-widen half, MDPF_SECCLASS FWD-9 -- the Rival Funds universe rows (CTO rulings batch 257 Q1, Q3, Q4, item 6; batch 259 section 2)

**Author:** `0.9.0_WK_MDPF_SECCLASS~14` for `2.0.0_SA_COO~M`, 2026-10-05 (cell `SC-e-17`, amendments 1 and 2 applied). **For:** `1.0.0_SA_CTO`, second half.
**Status: DRAFT. Both halves UNSIGNED. The act is NOT RUN, and its writer REFUSES `--write` until three preconditions hold
(below).** Ruling: batch 257 item 6 ("the FWD-9 row write is served output, under its own never-widen half (CTO+COO), with the
dry run first").

## The act

`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_fwd9_write.py --write --half
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD9_ROWS_20261005.md`, once, by the
issuer, after both halves are signed.

| | value |
|---|---|
| input (read only) | `s3://opal-data-etfs/rivalfunds/etfs/gold/canonical_shape/date=<d>/`, the newest revision of each of 504 days (2024-09-30 to 2026-10-02), 10 columns read |
| mapping | `infra/aws/lambda/v2_portal/_shared/rivalfunds_classification.py` `classify_canonical_row`, pure; tests `_shared/tests/test_rivalfunds_classification.py` |
| set file | `R7_CHECKS/FWD9_ROW_SET_20261005.tsv`, one line per security, built by `R7_CHECKS/r7_fwd9_row_set.py` with a consistent get of each key on `etf-classifications` |
| writer | `R7_CHECKS/r7_fwd9_write.py`: dry run by default; `--write` through `etf_classification_scheduled.write()` (`attribute_not_exists(ticker)`), whose attribute list now carries `security_bloomberg` and `listing_country` (no table wrapper); no overwrite path, no delete path; `classified_by: scheduled`, `updated_by: rivalfunds-backfill` |
| the rule | Q4 (batch 259): non-cash, the final token of `security_bloomberg` (the yellow key) is `Equity`, and `provider_security_type` is `Equity` or empty; a US five-letter ticker ending `XX` is a money-market fund and OUT. A `BLOOMBERG` item carries no `name`. Q1: a US listing keeps the bare ticker; any other listing is `BBG:<ticker>:<exch>` with `identifier_namespace: BLOOMBERG` and the verbatim `security_bloomberg` (and `listing_country`, ISO 3166-1 alpha-2). Q3: GICS sector where RESOLVED and one of the table's existing sector values; else the exchange country mapped to `Developed` or `EM` by the MSCI split (a table in the module); else no sub-class and `low_confidence: true` |

## The write set (the set file and its counts)

Row-set line: `FWD9-ROW-SET securities=1051 write=657 present_same=16 present_differs=122 out=256` (live read of the 504 days and of
each key with a consistent get, 2026-10-05).

- **WRITE 657** (a key with no row today): 626 `BBG:` rows and 31 US bare-ticker rows (listed in the set file).
  - Sub-class source: GICS 233 (225 `BBG:`, 8 US); country 400 (`Developed` 350, `EM` 50); none 24 (23 US and 1 `BBG:SBER:RM`,
    written with no sub-class and `low_confidence: true`).
  - The 31 US keys: AAGIY ADYEY ATI AUGO BAP BG BKD BZ CACI ETOR GENI GRFS GXYYY HDB HTHT JAN KB NBIS RARE RYAAY SPHR STLA STVN
    SUNB TCOM THC TISI VG XTSLA YMM ZIM.
  - No `BBG:` item carries a `name` (0 of 626); each carries `security_bloomberg` verbatim and `listing_country` where the exchange
    code is known.
- **PRESENT-SAME 16:** a row with the same class and sub-class. Not touched.
- **PRESENT-DIFFERS 122:** a row with another class or sub-class (the asset class is `equity` in all 122). **NEVER overwritten;
  listed in the set file for the CTO.** 100 are a planned row with no sub-class (US, GICS unresolved) against an existing sub-class;
  22 have a sub-class on both sides and they differ. A present row keeps its `instrument_kind` (34 read `single_security`, 88 hold none);
  none of the 122 is written.
- **OUT 256**, by reason (the row set prints one `FWD9-OUT` line each):
  - cash line 38;
  - money-market fund (US five-letter ticker ending `XX`) 7: AGPXX CMQXX DGCXX DGVXX FTIXX GVMXX IJGXX;
  - no parseable Bloomberg identifier 192 (records keyed only by `security_ticker`; see `MDPF_SECCLASS-W14-S5`);
  - yellow key `Index` 17 (futures);
  - yellow key `US` 2 (HAL US, VLO US).

Open points the CTO reads before signing (surprise channel, `INVESTIGATION_v1.md`):
- `MDPF_SECCLASS-W14-S1`: answered by batch 259 section 2 and applied (an empty provider type with the Equity yellow key is IN).
- `MDPF_SECCLASS-W14-S2`: closed by amendment 1 (`write()` carries `security_bloomberg` and `listing_country`).
- `MDPF_SECCLASS-W14-S3`: closed by amendment 1 (the 7 money-market funds are OUT).
- `MDPF_SECCLASS-W14-S4`: precondition (a) fails closed because the committed SC-e-16 census holds no crashes, refuses, miskeys
  or fails_contract counters.
- `MDPF_SECCLASS-W14-S5`: 7 real stocks with no Bloomberg id and no table row (BRK/B CRWV EPAM FPS MDLN ORI SLDE) cannot be written
  under the ruled rule; HAL US and VLO US carry the exchange code where the yellow key belongs.
- 24 of the `BBG:` keys hold `/`, `-` or `*` (for example `BBG:BP/:LN`, `BBG:AC*:MM`, `BBG:TTB-R:TB`); none holds whitespace.

## Blast radius

- **What the act may touch:** the `etf-classifications` table, 657 new keys, each put on absence. No existing row is read for
  update; none changes. The table counts 2,866 today (scan COUNT, consistent read, 2026-10-05); it would count 3,523.
- **Who reads the new rows:**
  - the 31 US keys are bare tickers, so a firm that holds one reads a row where it read the fallback before. Holdings served
    effect is NOT measured for them;
  - the 626 `BBG:` keys match no firm's holding ticker, so no holdings tab moves;
  - the reader census for the `BBG:` namespace (cell `SC-e-16`, `R7_BBG_READER_CENSUS_20261005.json`) is a precondition of the
    write, not a claim of this half.
- **Blast-radius limit:** a key a firm already holds as a different class cannot be changed by this act (put on absence).

## Writers counted, both branches

**N = 1 writer of these keys in the act's window:** `r7_fwd9_write.py` through `write()`. The table's other writers, read:
the seed script (writes seed-source tickers only; none of the 657 is a seed-source key, because the row set read each key from
the live table first), the E_18 detector (writes only new securities of a firm's holdings and is not run in this window), the
CUSIP, model and multi-asset writers (their own keys).

- **Branch A, every put lands:** 657 of 657 `written`; a second run reads `plan=0`.
- **Branch B, a put meets an existing row** (a key appeared between the read and the put): that put raises
  `ConditionalCheckFailedException`, `write()` reports it `refused` and leaves the row exactly as it was; the run continues and
  prints each refused key. Nothing is overwritten on either branch.

## The three refusal preconditions (`--write` refuses unless all hold)

(a) `R7_BBG_READER_CENSUS_20261005.json` (cell `SC-e-16`) reads crashes, refuses, miskeys and fails_contract all 0.
(b) `org/standards/MDPF_SECCLASS_CONTRACT.json` lists `BLOOMBERG` in the `identifier_namespace` values (contract 0.4.0, the CTO's
carrier). Until it lands, `--write` refuses.
(c) `--half <path>` names a half whose `## CTO half` heading reads SIGNED.

The dry run, 2026-10-05 (no `--half`), prints (a) NOT MET (the census holds none of the four counters, `MDPF_SECCLASS-W14-S4`), (b) MET
(contract 0.4.0 lists `BLOOMBERG`), (c) NOT MET (no half named), and writes nothing; its line reads `FWD9-WRITE plan=657 (BLOOMBERG=626, TICKER=31)`.

## Rollback per key

A key this act wrote is deleted only on Andrew's word, because that is a delete (`delete-item` of `ticker = <key>`; the keys
are the `ticker` column of the set file's WRITE lines). Otherwise a written row stays and a corrected row goes by the same
absent-only path after its delete. The act has no other effect to roll back.

## The local candidate diff

The candidate is the set file itself, `R7_CHECKS/FWD9_ROW_SET_20261005.tsv`: its WRITE lines are the diff against the table
(657 new items, 0 changed, 0 removed), and its PRESENT-DIFFERS lines are the 122 rows this act leaves as they are.

## Acceptance

1. Right after the run: 657 of 657 keys read back `classified_by: scheduled`, `updated_by: rivalfunds-backfill`, the line's
   class and sub-class; the `BBG:` rows read `identifier_namespace: BLOOMBERG` and the verbatim `security_bloomberg` and `listing_country`, and no `name`; the table
   counts 3,523.
2. A second dry run reads `plan=0` WRITE lines.

**Ledger:** `secclass-fwd9-rows-m-<date>`, opened before the write.

## COO half -- [PENDING SIGNATURE]

For `2.0.0_SA_COO~M`, left unsigned by the worker. Sign after reading the set file, the three open points and the preconditions.

## CTO half -- [PENDING SIGNATURE]

For `1.0.0_SA_CTO`, left unsigned by the worker. Precondition (c) reads this heading; it must read SIGNED to unlock `--write`.
