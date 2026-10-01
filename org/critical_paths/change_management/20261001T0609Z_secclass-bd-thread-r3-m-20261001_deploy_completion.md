# Deploy Completion Record
**Date opened:** 2026-10-01T06:09:35.109060+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS BD_THREAD_R3: redeploy the BD thread with the shared classifier client inside code/gold (six files + three shipped modules, then the silver staging document v5); halves COO+CTO SIGNED @8769ffe8d5; supersedes the BD legs B3/B4 of secclass-bd-thread-r2-and-irpt-narrowed-m-20260930, which stays HELD for its IRPT leg H5 only
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 20.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P | verify | invariants and restore targets, read live before step 1 | runner stopped and last gold run exit 0; next silver fire more than 30 min away; six code keys prior VersionIds; three _shared keys 404; document default 4 and v4 bytes saved with hash |  | OPEN |
| S1 | s3-prefix | ONE safe-deploy call: six BD files + three shipped lib/_shared modules to opal-data-bd code/gold and code/silver | DEPLOYED and VERIFY OK per file; ETag of lib/_shared/etf_classifications_dynamodb.py reads 181e1902667beb928a9ea993bd17d349 |  | OPEN |
| L0 | activation | SSM document opal-bd-asset-dim-download: publish the git-show bytes as version 5 and set default 5 | new DocumentVersion 5 with Hash d3a38c7b...d3f407; default 5; readback carries the three _shared cp lines |  | OPEN |
| X | verify | exercise: one ad-hoc BD gold run on the real runner (import proof, not acceptance) | C_06, D_03, D_04 done rc=0; no IndexError and no BLOCKED in the log; served keys prior VersionIds recorded before the run |  | OPEN |
| A1 | verify | acceptance: the first scheduled gold fire after step 1 (23:00Z) | C_06, D_03, D_04 exit 0 and the served keys advance |  | OPEN |
| A2 | verify | acceptance: the first 22:10Z silver fire after Leg 0 | silver/bd_assets_dim.parquet advances |  | OPEN |
| B4 | verify | the COO's one live FWD-1 run to the page for relationship z08327149 | VXX structured/Hedge, GLD and PHYS commodities/Metals, class_source etf-classifications, bd_securities_reads 0, on the real page |  | OPEN |

## Log

- 20261001T060935Z OPENED by 2.0.0_SA_COO~M with 7 leg(s)
