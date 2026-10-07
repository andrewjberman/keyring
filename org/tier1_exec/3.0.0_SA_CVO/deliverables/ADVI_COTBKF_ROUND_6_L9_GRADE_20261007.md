# ADVI_COTBKF -- L9 grades owed at round 6 (CB4d5-AC3, and the CB4d1-AC3 re-grade)

**archetype:** VALIDATE

Grader: `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~10:3xZ-10:5xZ. Input: the drain-end packet
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_6_DRAIN_END_20261007.md` @f6d26131f1 (msg 340).
The round-4 grades are in `ADVI_COTBKF_ROUND_4_L9_GRADE_20261007.md` @2114a2a7a2.

| criterion | grade | one line |
|---|---|---|
| CB4d5-AC3 | MET | One statement and one tax form found by account and date in the applied documents table, fetched, hash-equal to the table, and opened: each is the document its row says it is |
| CB4d1-AC3 (re-grade) | NOT MET | The two buckets are now listed, but only two prefix levels deep; one of them holds the investor-reporting tree, where a per-security daily store lives at other firms |

## CB4d5-AC3 -- MET

The criterion: "one statement and one tax form found by account and date in the documents table and opened (FWD-5's DONE WHEN)".

- **The table:** `s3://opal-data-assets/commonwealth/cottonwood/silver/documents/date=2026-06-23/documents.parquet` (LastModified
  10:18:55Z), 11,119 rows, all `status=VERIFIED`; doc types STMT 7,736, NCSD 1,239, TXRP 1,034, CLNT 932, ADVS 165, REPR 13.
- **This seat chose its own two, not the issuer's**, by sorting each doc type by account and date and taking a fixed position:
  - STMT, account B3S-623111, date 2025-09-30: fetched from its `written_key`, 49,845 bytes, sha256 `1f1c8871..` equal to the row's.
    Opened (text extracted from its streams with the standard library; no PDF tool exists on dell2): "STATEMENT FOR THE PERIOD
    SEPTEMBER 1, 2025 TO SEPTEMBER 30, 2025 ... Account Number: B3S-623111", 14 pages, an account overview with beginning and ending
    values. The account and the date match the row.
  - TXRP, account B3S-706612, date 2026-03-09: fetched, 71,412 bytes, sha256 `63b1fb88..` equal to the row's. Opened: "Form 1099-DIV
    2025 Dividends and Distributions Copy B for Recipient", "Recipient ID No. B3S-706612", 18 pages. The account matches; the date
    is the 2025 tax year's issue date.
- Client names in the two documents are not copied into this record.
- The issuer's own two (STMT B3S-605713 2025-06-30, TXRP B3S-605598 2025-02-09) were not re-opened; two independent picks are the grade.

## CB4d1-AC3 -- re-grade, NOT MET

The criterion: "the census is complete (no unnamed store that holds a per-security daily price in a USABLE bucket) and every BARRED
grade is the registry's".

- **What changed:** row S15. The laptop listed both buckets dell2 cannot list, to two prefix levels: `opal-data-cottonwood` holds
  `irpt/cottonwood/` and `mdpf/cottonwood/`; `opalinvest-portal` holds `assets/`, `fonts/`, `logos/` with no sub-prefix. The census was
  also re-run on the covering calendar (S17): the needed security-days equal round 2's 9,388,961.
- **`opalinvest-portal` is cleared:** static web assets, no price store at any depth (no sub-prefixes).
- **`opal-data-cottonwood` is not cleared.** `irpt/cottonwood/` is the investor-reporting tree. At another firm, the same tree holds
  a per-security daily store: `s3://opal-data-inflection/irpt/inflection/gold/holdings_performance_daily/date=<d>/data.parquet`, landed
  daily (IRPT_BCKEND rows S336 and S338). A listing that stops at `irpt/cottonwood/` can neither name nor exclude the Cottonwood twin,
  and the census does not name it. `mdpf/cottonwood/` (model portfolios) is likewise unread below its second level.
- **The BARRED half still holds** (unchanged from round 4: the 5 BARRED buckets are exactly the registry's non-Cottonwood firm buckets).
- **What clears it:** a permitted principal lists `opal-data-cottonwood/irpt/cottonwood/` and `mdpf/cottonwood/` to the table level and
  says whether a per-security daily price or value store is there. If one is, the census names it (USABLE: it is Cottonwood's own
  bucket) or states why it is not a price source.

-- 3.0.0_SA_CVO
