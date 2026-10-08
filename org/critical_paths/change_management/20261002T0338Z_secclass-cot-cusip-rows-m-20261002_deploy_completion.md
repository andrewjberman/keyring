# Deploy Completion Record
**Date opened:** 2026-10-02T03:38:46.636313+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / its leg R reads with secclass-cot-repoint-m-20261002 leg S (own gate text); 29 of 29 rows measured matching 2026-10-08, deployed etf_classifier.py ETag 2fef39d1 equals HEAD md5 (held since 2026-10-02T03:41:55.046127+00:00)
**Deploy:** MDPF_SECCLASS Cottonwood CUSIP rows (batch 93 item 2): 29 bank-CD CUSIP: rows in etf-classifications by R7_CHECKS/write_cusip_rows.py --write over COT_CUSIP_ROWS_WRITE_SET_20261002.txt, conditional put only; halves COO @ffe6235c2a (blob 56a1db3d3e) + CTO CTO_HALF_SECCLASS_COT_CUSIP_ROWS_20261002.md (batch 108); rollback a corrected row, no delete
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 72.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| W | verify | stops: writer blob 6dfcd7fc75, set blob 85f1bff9a4, shared put blob 3e6e081e3b at CLOUD; dry run named=29 plan=29 already_present=0 refused=0; the write; get-item readback of 29; table count 2,719; second dry run plan=0 already_present=29 | script output + get-item | Stops read 03:39Z at CLOUD: writer R7_CHECKS/write_cusip_rows.py blob 6dfcd7fc75, set COT_CUSIP_ROWS_WRITE_SET_20261002.txt blob 85f1bff9a4, shared put etf_classification_scheduled.py blob 3e6e081e3b (HEAD = working copy, each). Pre-run dry run 03:39:35Z: named=29 plan=29 already_present=0 refused=0 (table rows 2,690). Write 03:40:18Z-03:40:23Z, --write, rc 0: WRITTEN 29 of 29, no WARN line. Readback (get-item, consistent read): 29 of 29 equal -- fixed_income, no sub_asset_class, identifier_namespace CUSIP, classified_by scheduled, updated_by mdpf-secclass-cusip-rows, name equal to the set file; last_updated 2026-10-02T03:40:20Z. Second dry run: named=29 plan=0 already_present=29 refused=0 (table rows 2,719 = 2,690 + 29). | CLOSED 20261002T034154Z |
| R | verify | read with the Cottonwood re-point's served leg (no reader keys these rows before it ships) | the re-point ledger's leg S |  | OPEN |

## Log

- 20261002T033846Z OPENED by 2.0.0_SA_COO~M with 2 leg(s)
- 20261002T034154Z LEG W closed: Stops read 03:39Z at CLOUD: writer R7_CHECKS/write_cusip_rows.py blob 6dfcd7fc75, set COT_CUSIP_ROWS_WRITE_SET_20261002.
- 20261002T034155Z HELD-SOVEREIGN-GATED gate=external/No reader keys a CUSIP: row for Cottonwood until the re-point (NEVER_WIDEN_HALF_
- 20261008T185130Z HELD-SOVEREIGN-GATED gate=external/its leg R reads with secclass-cot-repoint-m-20261002 leg S (own gate text); 29 o
