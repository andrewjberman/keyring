# Never-widen half, MDPF_SECCLASS FWD-9 -- the Rival Funds universe rows (CTO rulings batch 257 Q1, Q3, Q4, item 6)

**Author:** `0.9.0_WK_MDPF_SECCLASS~14` for `2.0.0_SA_COO~M`, 2026-10-05 (cell `SC-e-17`). **For:** `1.0.0_SA_CTO`, second half.
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
| writer | `R7_CHECKS/r7_fwd9_write.py`: dry run by default; `--write` through `etf_classification_scheduled.write()` (`attribute_not_exists(ticker)`); no overwrite path, no delete path; `classified_by: scheduled`, `updated_by: rivalfunds-backfill` |
| the rule | Q4: `provider_security_type == Equity` and non-cash. Q1: a US listing keeps the bare ticker; any other listing is `BBG:<ticker>:<exch>` with `identifier_namespace: BLOOMBERG` and the verbatim `security_bloomberg`. Q3: GICS sector where RESOLVED and one of the table's existing sector values; else the exchange country mapped to `Developed` or `EM` by the MSCI split (a table in the module); else no sub-class and `low_confidence: true` |

## The write set (the set file and its counts)

Row-set line: `FWD9-ROW-SET securities=1051 write=664 present_same=11 present_differs=106 out=270`.

- **WRITE 664** (a key with no row today): 626 `BBG:` rows and 38 US bare-ticker rows (listed in the set file).
  - Sub-class source: GICS 233 (225 `BBG:`, 8 US); country 400 (`Developed` 350, `EM` 50); none 31 (30 US and 1 `BBG:SBER:RM`, written
    with no sub-class and `low_confidence: true`).
  - The 38 US keys: AAGIY ADYEY AGPXX ATI AUGO BAP BG BKD BZ CACI CMQXX DGCXX DGVXX ETOR FTIXX GENI GRFS GVMXX GXYYY HDB HTHT IJGXX JAN
    KB NBIS RARE RYAAY SPHR STLA STVN SUNB TCOM THC TISI VG XTSLA YMM ZIM.
- **PRESENT-SAME 11:** a row with the same class and sub-class. Not touched.
- **PRESENT-DIFFERS 106:** a row with another sub-class (the asset class is `equity` in all 106). **NEVER overwritten; listed
  in the set file for the CTO.** 96 are a planned row with no sub-class (US, GICS unresolved) against an existing size-split
  sub-class (`US Large Cap` and its kind); 10 have a sub-class on both sides and they differ.
- **OUT 270:** not in the domain. `provider_security_type` None 218 (see row `MDPF_SECCLASS-W14-S1`), Curncy 32, Index futures 17,
  cash lines 3.

Open points the CTO reads before signing (surprise channel, `INVESTIGATION_v1.md`):
- `MDPF_SECCLASS-W14-S1`: Q4 read literally leaves out 218 real-stock securities whose type is empty; 8 stocks among them have no
  table row (BRK/B, CRWV, EPAM, FPS, MDLN, NBIS, ORI, SLDE).
- `MDPF_SECCLASS-W14-S2`: the shared writer's attribute list lacks `security_bloomberg`; the writer adds it on the same put.
- `MDPF_SECCLASS-W14-S3`: 7 money-market funds (AGPXX CMQXX DGCXX DGVXX FTIXX GVMXX IJGXX) are in the WRITE set as `single_security`.
- 24 of the `BBG:` keys hold `/`, `-` or `*` (for example `BBG:BP/:LN`, `BBG:AC*:MM`, `BBG:TTB-R:TB`); none holds whitespace.

## Blast radius

- **What the act may touch:** the `etf-classifications` table, 664 new keys, each put on absence. No existing row is read for
  update; none changes. The table counts 2,866 today; it would count 3,530.
- **Who reads the new rows:**
  - the 38 US keys are bare tickers, so a firm that holds one reads a row where it read the fallback before. Holdings served
    effect is NOT measured for them;
  - the 626 `BBG:` keys match no firm's holding ticker, so no holdings tab moves;
  - the reader census for the `BBG:` namespace (cell `SC-e-16`, `R7_BBG_READER_CENSUS_20261005.json`) is a precondition of the
    write, not a claim of this half.
- **Blast-radius limit:** a key a firm already holds as a different class cannot be changed by this act (put on absence).

## Writers counted, both branches

**N = 1 writer of these keys in the act's window:** `r7_fwd9_write.py` through `write()`. The table's other writers, read:
the seed script (writes seed-source tickers only; none of the 664 is a seed-source key, because the row set read each key from
the live table first), the E_18 detector (writes only new securities of a firm's holdings and is not run in this window), the
CUSIP, model and multi-asset writers (their own keys).

- **Branch A, every put lands:** 664 of 664 `written`; a second run reads `plan=0`.
- **Branch B, a put meets an existing row** (a key appeared between the read and the put): that put raises
  `ConditionalCheckFailedException`, `write()` reports it `refused` and leaves the row exactly as it was; the run continues and
  prints each refused key. Nothing is overwritten on either branch.

## The three refusal preconditions (`--write` refuses unless all hold)

(a) `R7_BBG_READER_CENSUS_20261005.json` (cell `SC-e-16`) reads crashes, refuses, miskeys and fails_contract all 0.
(b) `org/standards/MDPF_SECCLASS_CONTRACT.json` lists `BLOOMBERG` in the `identifier_namespace` values (contract 0.4.0, the CTO's
carrier). Until it lands, `--write` refuses.
(c) `--half <path>` names a half whose `## CTO half` heading reads SIGNED.

The dry run, 2026-10-05, prints all three as NOT MET and writes nothing.

## Rollback per key

A key this act wrote is deleted only on Andrew's word, because that is a delete (`delete-item` of `ticker = <key>`; the keys
are the `ticker` column of the set file's WRITE lines). Otherwise a written row stays and a corrected row goes by the same
absent-only path after its delete. The act has no other effect to roll back.

## The local candidate diff

The candidate is the set file itself, `R7_CHECKS/FWD9_ROW_SET_20261005.tsv`: its WRITE lines are the diff against the table
(664 new items, 0 changed, 0 removed), and its PRESENT-DIFFERS lines are the 106 rows this act leaves as they are.

## Acceptance

1. Right after the run: 664 of 664 keys read back `classified_by: scheduled`, `updated_by: rivalfunds-backfill`, the line's
   class and sub-class; the `BBG:` rows read `identifier_namespace: BLOOMBERG` and the verbatim `security_bloomberg`; the table
   counts 3,530.
2. A second dry run reads `plan=0` WRITE lines.

**Ledger:** `secclass-fwd9-rows-m-<date>`, opened before the write.

## COO half -- [PENDING SIGNATURE]

For `2.0.0_SA_COO~M`, left unsigned by the worker. Sign after reading the set file, the three open points and the preconditions.

## CTO half -- [PENDING SIGNATURE]

For `1.0.0_SA_CTO`, left unsigned by the worker. Precondition (c) reads this heading; it must read SIGNED to unlock `--write`.
