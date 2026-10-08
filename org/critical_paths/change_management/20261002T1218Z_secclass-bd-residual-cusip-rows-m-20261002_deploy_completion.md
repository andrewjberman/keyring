# Deploy Completion Record
**Date opened:** 2026-10-02T12:18:19.473422+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T185102Z
**Deploy:** MDPF_SECCLASS BD re-land residual first act: 36 CUSIP rows by peer (write_cusip_rows.py --write over R8_CHECKS/RESIDUAL_CUSIP_WRITE_SET_20261002.tsv); halves COO @d022796535 (blob 2a4428eb24) + CTO batch 162; inert until the r3 re-land
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 168.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| W | verify | stops (set blob 2e47dd1663; dry run named=36 plan=36 present=0 refused=0); the write; readback 36; table 2,841; second dry run plan=0 present=36 | writer output + get-item | Stops 12:1xZ: set file RESIDUAL_CUSIP_WRITE_SET_20261002.tsv blob 2e47dd1663 (HEAD = working copy, the CTO-read blob); pre-run dry run named=36 plan=36 already_present=0 refused=0 (table 2,805). Write 12:18:50Z --write rc 0: WRITTEN 36 of 36, no WARN. Readback (get-item, consistent): 36 of 36 equal the set's class and sub class, identifier_namespace CUSIP, classified_by scheduled. Second dry run: named=36 plan=0 already_present=36 refused=0 (table 2,841 = 2,805 + 36). The five same-security rows (VB, VO, VOE, VVIAX, BAC CUSIPs) are INFERRED identities (CTO batch 162). | CLOSED 20261002T121924Z |
| R | verify | read at the r3 re-land's leg R (49F unclassified 3.99 pct expected) | re-land ledger leg R | Read at re-land ledger secclass-bd-thread-r4-reland-m-20261002 leg R (CLOSED 20261002T193059Z): 49F mix_summary unclassified 4.14 pct <= 5.0, every class present; live re-read 2026-10-08 ~18:5xZ by 2.0.0_SA_COO~M1 (consistent get-item): 36 of 36 rows of RESIDUAL_CUSIP_WRITE_SET_20261002.tsv equal the set's class and sub class, 0 absent. World-done; closed, no act re-executed. | CLOSED 20261008T185053Z |

## Log

- 20261002T121819Z OPENED by 2.0.0_SA_COO~M with 2 leg(s)
- 20261002T121924Z LEG W closed: Stops 12:1xZ: set file RESIDUAL_CUSIP_WRITE_SET_20261002.tsv blob 2e47dd1663 (HEAD = working copy, the CTO-read blob); p
- 20261008T185053Z LEG R closed: Read at re-land ledger secclass-bd-thread-r4-reland-m-20261002 leg R (CLOSED 20261002T193059Z): 49F mix_summary unclassi
- 20261008T185102Z CLOSED -- all 2 legs proven
