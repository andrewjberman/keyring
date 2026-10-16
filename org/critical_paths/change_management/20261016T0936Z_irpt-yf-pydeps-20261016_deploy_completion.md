# Deploy Completion Record
**Date opened:** 2026-10-16T09:36:49.038784+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T094316Z
**Deploy:** IRPT_ANLREQ TO-APPLY-YFDEPS (AR-g-119): the yfinance 1.2.0 closure (17 wheels) into the resident host's pydeps: R0 pre-read (PRE OK), D1 upload of 17 wheels to 17 new keys under ec2/investor-reporting-ycharts/resident/pydeps-wheels/yfinance-1.2.0/ in opal-313476888478-lambda-artifacts, D2 install_yf.sh by Systems Manager (17 dist-info added 0 removed, 22 existing unchanged, 18 imports), V checks; no restart; COO half blob 5c6da65b0b, CTO half df1fd7869b (msg 9156), receipts ruling msg 9253
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | resident host pydeps folder (pre_read_yf.sh) and the host role GetObject simulation | PRE OK and the simulator decision allowed with the matched statement | pre_read_yf.sh (sha256 6f2924f2... equal) by Systems Manager as ec2-user: PRE OK (x86_64, python 3.12.14, pydeps writable by ec2-user, 2532984 KB free, 22 distributions equal the inventory, names already importable none, 17 wheels expected); simulator s3:GetObject on a key of the new prefix for irpt-ycharts-runner-role: allowed, matched role inline policy irpt-ycharts-runner Sid PullRunnerArtifact (ec2/investor-reporting-ycharts/*); negative control (an unrelated bucket) implicitDeny | CLOSED 20261016T094053Z |
| D1 | s3-prefix | ec2/investor-reporting-ycharts/resident/pydeps-wheels/yfinance-1.2.0/ 17 new keys | 17 keys read 404 first, uploaded, read back sha256 equal, 17 VersionIds | 17 of 17 collected wheels equal the approved list; 17 of 17 keys read 404 before any write; 17 put_object from the named list, each read back by VersionId with sha256 and size equal to the table; the 17 VersionIds are in D1_UPLOAD_OUT.txt (deliverables/irpt_anlreq_yfdeps) | CLOSED 20261016T094123Z |
| D2 | verify | /opt/investor-reporting-ycharts/pydeps on the resident host (install_yf.sh) | INSTALL OK with rc, 17 dist-info added 0 removed, 22 existing unchanged, 18 imports | install_yf.sh (sha256 f1324cd4... equal) by Systems Manager as ec2-user: all 17 wheels sha256 and size verified on the host, pip rc=0, INSTALL OK 09:41:47Z; V1 37 entries added 0 removed, dist-info added 17 (want 17), none outside the wheels' own names, the 22 pre-existing distributions unchanged; V2 18 imports ok from pydeps (the 17 libraries and pyarrow 18.1.0), 0 failed; pip stderr warning that pydeps/bin already exists (skipped, nothing replaced) | CLOSED 20261016T094316Z |
| V | verify | the record A_AFTER_YFDEPS.txt and the collected wheels untouched | the seven lines and the 17 VersionIds | A_AFTER_YFDEPS.txt holds the seven lines as written and the 17 VersionIds; the collected wheels re-hashed after the act 17 of 17 equal; host staging removed by name (17 files and rmdir); nothing else deleted | CLOSED 20261016T094316Z |

## Log

- 20261016T093649Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 4 leg(s)
- 20261016T094053Z LEG R0 closed: pre_read_yf.sh (sha256 6f2924f2... equal) by Systems Manager as ec2-user: PRE OK (x86_64, python 3.12.14, pydeps writabl
- 20261016T094123Z LEG D1 closed: 17 of 17 collected wheels equal the approved list; 17 of 17 keys read 404 before any write; 17 put_object from the named
- 20261016T094316Z LEG D2 closed: install_yf.sh (sha256 f1324cd4... equal) by Systems Manager as ec2-user: all 17 wheels sha256 and size verified on the h
- 20261016T094316Z LEG V closed: A_AFTER_YFDEPS.txt holds the seven lines as written and the 17 VersionIds; the collected wheels re-hashed after the act 
- 20261016T094316Z CLOSED -- all 4 legs proven
