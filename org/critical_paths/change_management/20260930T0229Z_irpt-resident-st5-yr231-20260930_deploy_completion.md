# Deploy Completion Record
**Date opened:** 2026-09-30T02:29:01.955622+00:00
**Status:** OPEN
**Deploy:** Resident st4 -> st5: resident_worker.py @7fc1a123f0 (IB-yr-231: the resident journals the matched eviction verdict and a job's ATTENTION code, no behaviour change); ~Y 103043/103059; CTO half pending on the st5 packet
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | resident package st5 upload | SUMS vs st4 (only resident_worker.py + bindings); tar sha; S3 VersionId; install script | build_resident_package.py --pin fe64236bbb with st4's 12 overrides, resident_worker.py re-pinned 0357fc7e08 -> 7fc1a123f0 (blob 583c12db = HEAD's). SHA256SUMS vs st4: 225/225 keys, exactly two differ: resident_worker.py (5288ff5a -> 8d1f5431) and resident_bindings.json (provenance). Tar 266 members = st4's names; sha256 71998920 (731,610 bytes) uploaded to a NEW key ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-st5.tar.gz, VersionId vJOIoCTh5mGuWbbLmMd43INv3t3FnEQ5 (HeadObject 404 before), read back by version: sha equal. Install script resident_host_install_st5_20260930.sh: 10 of 10 member pins equal the built package, bash -n OK. ~Y gates on the built st5 NOT yet run. | CLOSED 20260930T023420Z |
| D1 | activation | resident install st4 -> st5 | halves at HEAD on the packet blob; queue 0/0; install rc 0; running root + member shas; polls; 0 Tracebacks |  | OPEN |

## Log

- 20260930T022901Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260930T023420Z LEG U1 closed: build_resident_package.py --pin fe64236bbb with st4's 12 overrides, resident_worker.py re-pinned 0357fc7e08 -> 7fc1a123f
