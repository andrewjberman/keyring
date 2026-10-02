# Deploy Completion Record
**Date opened:** 2026-10-02T10:25:26.852664+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T180238Z
**Deploy:** MDPF_SECCLASS BD forward fix 2: 67 rows mapped from bd-securities (28 direct, 32 fixed_income class kept, 7 EM renamed) by R8_CHECKS/write_bd_mapped_rows.py --write over BD_MAPPED_WRITE_SET_20261002.tsv; conditional put only; halves COO @f227938dfd (blob 4b00c949d8) + CTO CTO_HALF_SECCLASS_BD_MAPPED_AND_COT_THREE_ROWS_20261002.md (batch 140); rollback a corrected row, no delete
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 30.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| W | verify | stops (writer f057c77a7a, set 09acc7aff9, shared put 3e6e081e3b at CLOUD; dry run named=67 plan=67 present=0 refused=0); the write; readback 67; second dry run plan=0 present=67 | writer output + get-item | Stops 10:25Z at CLOUD: writer R8_CHECKS/write_bd_mapped_rows.py f057c77a7a, set BD_MAPPED_WRITE_SET_20261002.tsv 09acc7aff9, shared put etf_classification_scheduled.py 3e6e081e3b (HEAD = working copy each); pre-run dry run named=67 plan=67 already_present=0 refused=0 (table 2,719). Write 10:26:13Z-10:26:18Z --write rc 0: WRITTEN 67 of 67, no WARN. Readback (get-item, consistent): 67 of 67 equal the set file's class, sub class and name, classified_by scheduled, updated_by mdpf-secclass-bd-mapped. Second dry run: named=67 plan=0 already_present=67 refused=0 (table 2,786 = 2,719 + 67). | CLOSED 20261002T102653Z |
| S | verify | next irpt-holdings-snapshot publication: the 39 sub class moves read at one firm per holder | served-slice read | R8_CHECKS/holdings_publication_row_read.py -> HOLDINGS_PUBLICATION_ROW_READ_20261002.json (sets derived from the writing commits / set file; live table 2,841 rows scanned; each firm's newest served publication read through its manifest's gold parquet, sha256 checked: 49financial 2026-10-01 rev 3413e2b5a3bd as_of 14:16:58Z, inflection rev 100a0dc22f12 14:17:10Z, cottonwood rev a3751a6acff2 14:17:13Z): of the 67 written tickers, 25 are held in a publication (49financial 16, inflection 12, cottonwood 5 holder-firm instances) and 25 of 25 are served with exactly the row's class and sub class (basis TABLE), 0 otherwise; 42 have no position in any firm's 10-01 publication (named in the JSON: ABB, AEO, ANF, CADUX ... WMG), so no holder reads them. The sub class moves among held tickers read as written. | CLOSED 20261002T180132Z |

## Log

- 20261002T102526Z OPENED by 2.0.0_SA_COO~M with 2 leg(s)
- 20261002T102653Z LEG W closed: Stops 10:25Z at CLOUD: writer R8_CHECKS/write_bd_mapped_rows.py f057c77a7a, set BD_MAPPED_WRITE_SET_20261002.tsv 09acc7a
- 20261002T180132Z LEG S closed: R8_CHECKS/holdings_publication_row_read.py -> HOLDINGS_PUBLICATION_ROW_READ_20261002.json (sets derived from the writing
- 20261002T180238Z CLOSED -- all 2 legs proven
