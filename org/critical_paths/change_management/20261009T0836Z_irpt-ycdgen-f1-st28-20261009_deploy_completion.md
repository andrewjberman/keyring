# Deploy Completion Record
**Date opened:** 2026-10-09T08:36:37.665676+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN APPLY-st28: st27 + svc on the allow list, svc swapped cottonwood -> 49financial for ONE seat-driven F1, PINNED to b7ad601c58 on scratch branch rel-ycdgen-st28 (tar sha256 8a96f07e9510d69d, install script sha256 47f17df385d05c14)
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | s3-prefix | stage the two st28 artifacts under ec2/investor-reporting-ycharts/resident/ | both keys 404 BEFORE the put (verified, with a positive control on st27 tar), then each read back BY VERSION and its sha256 equal to the packet declared value |  | OPEN |
| P1 | verify | host_read.py pre_read.sh on i-0167fd745ad906a66 | the host reads st27, allow list ANDREW ONLY, queue 0/0 |  | OPEN |
| D2 | activation | host_read.py install_st28.sh from this seat VER-filled lane copy | install rc 0 and the running root becomes b7ad601c58-st28; any failure takes the script own rollback to st27 and STOPS |  | OPEN |
| V1 | verify | the post-install read | allow list (andrew, svc), producer_for svc=OPAL, and load_brand resolving FROM THE RUNNING ROOT with no brand env var |  | OPEN |
| W1 | activation | python swap_svc_firm.py cottonwood 49financial | ONE conditional UpdateItem on svc PROFILE row, writing only if it reads cottonwood/service/active; after: allowedFirmIds 49financial |  | OPEN |
| F1 | verify | 2.0.0_SA_COO~G2 own leg, NOT this seat: f1_svc_run.py with F1_TENANT=49financial | the served report provider reads OPAL and the journal shows no YCHARTS marker in the request window; YCHARTS is a STOP |  | OPEN |
| X1 | activation | remove_st28_to_st27.sh, owed in EVERY branch, once F1 is done or ends AND irpt-generation reads 0/0 | the host returns to st27 with the st27 receipt restored and the allow list Andrew only |  | OPEN |
| V2 | verify | the post-removal read | st27 root, allow list ANDREW ONLY |  | OPEN |
| W2 | activation | python swap_svc_firm.py 49financial cottonwood | svc allowedFirmIds back to cottonwood, the rollback of W1 |  | OPEN |

## Log

- 20261009T083637Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 9 leg(s)
