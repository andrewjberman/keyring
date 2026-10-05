# Deploy Completion Record
**Date opened:** 2026-10-05T12:53:36.536410+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261005T131506Z
**Deploy:** MDPF_SECCLASS FWD-9 rows BRANCH 1: 626 BBG rows into etf-classifications, put on absence (half @79452258c9, batch 261 condition met @c3fc274af4)
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P | verify | preconditions (a)(b)(c) MET for --namespace BLOOMBERG and the 24 literal keys tolerated | dry-run lines + R7_FWD9_LITERAL_KEY_CENSUS_20261005.json | 12:5xZ dry run --namespace BLOOMBERG --half: plan=626, (a) MET census clean 45 readers (READ-ONLY 11, TOLERATES 34), (b) MET, (c) MET (COO + CTO headings sign BLOOMBERG); negative controls --namespace TICKER and all-rows both REFUSED at (c); batch 261 FWD9-LITERAL-KEYS keys=24 tolerated=24 held=0 @c3fc274af4; table COUNT 2866 (consistent scan) | CLOSED 20261005T125636Z |
| W | activation | r7_fwd9_write.py --write --namespace BLOOMBERG | WRITTEN n of 626 line | r7_fwd9_write.py --write --namespace BLOOMBERG --half <half>, 12:57:15Z-13:07:39Z, rc 0: WRITTEN 625 of 626; WARN 1 left alone: BBG:8354:JP -- read back: its row carries last_updated 2026-10-05T12:57:16Z (this act's first second), classified_by scheduled, updated_by rivalfunds-backfill and the planned fields, so the put landed and a retried put met its own row (the half's branch B, nothing overwritten) | CLOSED 20261005T131357Z |
| V | verify | 626 keys read back (consistent get): classified_by scheduled, updated_by rivalfunds-backfill, BLOOMBERG, security_bloomberg verbatim, no name; table count; second dry run plan=0 | read-back census output | r7_fwd9_readback.py --namespace BLOOMBERG (consistent gets + consistent COUNT scan, 13:1xZ): FWD9-READBACK namespace=BLOOMBERG keys=626 match=626 differs=0 absent=0 table_count=3492 (= 2866 + 626). The half's 'second dry run plan=0' does not apply as written: the writer plans from the set file, not from the live table, so it still prints plan=626; the read-back's 626 present keys are the equivalent (any re-put is refused on absence). | CLOSED 20261005T131358Z |

## Log

- 20261005T125336Z OPENED by 2.0.0_SA_COO~M with 3 leg(s)
- 20261005T125636Z LEG P closed: 12:5xZ dry run --namespace BLOOMBERG --half: plan=626, (a) MET census clean 45 readers (READ-ONLY 11, TOLERATES 34), (b)
- 20261005T131357Z LEG W closed: r7_fwd9_write.py --write --namespace BLOOMBERG --half <half>, 12:57:15Z-13:07:39Z, rc 0: WRITTEN 625 of 626; WARN 1 left
- 20261005T131358Z LEG V closed: r7_fwd9_readback.py --namespace BLOOMBERG (consistent gets + consistent COUNT scan, 13:1xZ): FWD9-READBACK namespace=BLO
- 20261005T131506Z CLOSED -- all 3 legs proven
