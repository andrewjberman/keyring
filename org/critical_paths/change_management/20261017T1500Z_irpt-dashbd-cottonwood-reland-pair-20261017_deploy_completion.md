# Deploy Completion Record
**Date opened:** 2026-10-17T15:00:54.733989+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-332: the Cottonwood re-land pair - eight gold days rewritten through the function's own rewrite event (dry run first) and the series republished once; applier 0.7.0_AE_CloudOps~IB2; packet sha256 37ce1e48
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | before reads of the eight gold days, the totals, the series prefix and both functions | the printed before reads | before reads recorded: 8 gold days rows/versions/NOT_MEASURABLE equal the packet; 3391 gold parquet objects, 3457 versions, 1745057 rows, 939 series prefixes, 1878 series objects, 5640 versions; both code hashes and schedules as pinned | CLOSED 20261017T151911Z |
| L2 | verify | eight dry runs in their band, nothing written | dry run record with gold objects and versions equal before and after | eight dry runs ok, held 0, rows 894/879/897/881/896/881/901/888 (band 840-960), max memory 597 MB, longest 103 s; gold objects 3391 and versions 3457 equal before and after | CLOSED 20261017T151911Z |
| L3 | activation | eight gold day rewrites, each a new version, previous versions kept | rewrite record |  | OPEN |
| L4 | verify | pre-write diff of the republish inside its stop lines | the offline diff counts |  | OPEN |
| L5 | activation | one canary series, compared with its previous version | canary record |  | OPEN |
| L6 | activation | the full republish, 939 published | publish record |  | OPEN |
| L7 | verify | the after-read and the receipt | the after record |  | OPEN |

## Log

- 20261017T150054Z OPENED by 0.7.0_AE_CloudOps~IB2 with 7 leg(s)
- 20261017T151911Z LEG L1 closed: before reads recorded: 8 gold days rows/versions/NOT_MEASURABLE equal the packet; 3391 gold parquet objects, 3457 versio
- 20261017T151911Z LEG L2 closed: eight dry runs ok, held 0, rows 894/879/897/881/896/881/901/888 (band 840-960), max memory 597 MB, longest 103 s; gold o
