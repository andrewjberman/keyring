# Deploy Completion Record
**Date opened:** 2026-10-09T00:50:56.791191+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN F1 st26: resident st24 -> st26 (Opal brand asset + svc on the allow list) on i-0167fd745ad906a66, one seat-driven F1 run by 2.0.0_SA_COO~G2, then the removal back to st24
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | verify | st26 tar + install script staged in S3, read back by version | sha256 equal to the declared values; both keys 404 before | staged ~00:4xZ before the ledger opened, as st24 and st25 did. BOTH KEYS 404 BEFORE (head-object, explicit). tar ec2/investor-reporting-ycharts/resident/irpt-resident-26df2c7622-st26.tar.gz v lUA.lKoWK3_LggXVlPr5KZ_V0oHCN9bM, read back BY VERSION and hashed = 06328304b64962dec04568c853e7b0cf9ff3b319ecfdeeca731c8df4d05c00b0 = declared; install script .../resident_host_install_26df2c7622-st26.sh v B2M6FErdxpFs1a6YmwqR.nXy6lKoziRn, read back BY VERSION and hashed = d2abe0e831656a6657262f66bc558cbeab47473ffdab49e1baa33d748531a0ad = declared. Census 26df2c7622-st26.census.json: old_root 409e3066d1-st24, new_root 26df2c7622-st26, members 269, added 2 (ycharts/research/brand/Opal-Capital-Logo-Full-Color.svg, brand.json) + changed 3 (reports/resident_bindings.json, ycharts/generate/resident_worker.py, ycharts/research/layout_overview.py) + removed 0 => identical 264, matching the order; gates G1-G4 true. VER=B2M6FErdxpFs1a6YmwqR.nXy6lKoziRn written into install_st26.sh; the FETCH IS BY KEY because the host role lacks s3:GetObjectVersion (st25 attempt 1, SSM 56fe806f, exit 30) | CLOSED 20261009T005116Z |
| P1 | verify | host pre-read (root st24, allow list Andrew only, queue 0/0) | host_read.py pre_read.sh via SSM, rc 0, recorded | SSM ca8da4c1-1b00-496e-a8ea-de513fef93ed 2026-10-09T01:07:24Z Success rc 0, AWS-RunShellScript on i-0167fd745ad906a66: active, root /opt/irpt-resident/409e3066d1-st24 since 2026-10-08 22:27:20 UTC, restarts 0; OPAL_PRODUCER_PRINCIPALS = ("andrew@opalinvest.com",) i.e. ANDREW ONLY; worker sha256 9317219a (st24); rollback root st24 present yes, st26 root present NO; receipt 89a7d531632352a1; library 857d90b8 + wrapper 55ddb8f7 (the wrapper equals the census wrapper_sha256, which is the ON-HOST wrapper and not the install script); pyarrow + renderer drop-in present; queue visible/in-flight 0 0; journal 60s polls 3 tracebacks 0. Capture pulled from AWS via get-command-invocation: deliverables/irpt_ycdgen_st26/P1_PRE_READ_20261009.txt | CLOSED 20261009T010945Z |
| D2 | activation | install_st26.sh via SSM | root 26df2c7622-st26 active, NRestarts 0, rc=0 | SSM 7f6d5a0a-6d9c-4713-91d8-719b04e5b307 01:07:52-01:08:32Z Success rc 0, run from this seat VER-filled copy deliverables/irpt_ycdgen_st26/install_st26.sh: install script sha256 verified ON THE HOST; package SHA256SUMS OK 269 members (= the census members count); factory OK enrolled 1276035; queue 0 0 before the library swap and after; install 26df2c7622-st26 rc=0; final active, MainPID 754728, NRestarts 0, ActiveEnterTimestamp 2026-10-09 01:08:07 UTC; ExecStart points at /opt/irpt-resident/26df2c7622-st26/ycharts/generate/resident_main.py; polls_30s 2 tracebacks_30s 0. Capture: deliverables/irpt_ycdgen_st26/D2_V1_INSTALL_20261009.txt | CLOSED 20261009T010945Z |
| V1 | verify | running root carries the allow list (andrew, svc), producer_for svc=OPAL other=YCHARTS, and load_brand resolving ycharts/research/brand/ in the RUNNING root with NO brand env var | read from the running root; a fall-back resolution is a STOP (CTO half condition) | same SSM 7f6d5a0a: running root /opt/irpt-resident/26df2c7622-st26, active, restarts 0; allow list OPAL_PRODUCER_PRINCIPALS = ("andrew@opalinvest.com", "svc-irpt-analysis@opalinvest.com"); worker sha256 c0bbea55fc9b069e = built; producer import OK family YCHARTS_OPAL_REPORT with that allow list; producer_for svc -> OPAL, andrew -> OPAL, other -> YCHARTS; proof process exit code 0; queue 0 0; journal 60s polls 3 tracebacks 0. THE CTO HALF CONDITION IS MET AND NOT A FALL-BACK: brand resolved FROM THE RUNNING ROOT -- spec /opt/irpt-resident/26df2c7622-st26/ycharts/research/brand/brand.json and logo .../brand/Opal-Capital-Logo-Full-Color.svg, logo bytes 3853, spec keys [colors, extended_palette, logo, typography], and "env brand vars []" i.e. NO brand environment variable was involved, so no fall-back path was taken | CLOSED 20261009T010945Z |
| F1 | verify | one seat-driven F1 run -- 2.0.0_SA_COO~G2's leg, NOT this seat's | the issuer's run record |  | OPEN |
| X1 | activation | remove_st26_to_st24.sh via SSM, only after F1 is done AND irpt-generation reads 0/0 | root 409e3066d1-st24 active, rc=0 |  | OPEN |
| V2 | verify | running allow list is Andrew only; queue 0/0; no traceback | read from the running root |  | OPEN |

## Log

- 20261009T005056Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 7 leg(s)
- 20261009T005116Z LEG U2 closed: staged ~00:4xZ before the ledger opened, as st24 and st25 did. BOTH KEYS 404 BEFORE (head-object, explicit). tar ec2/inv
- 20261009T010945Z LEG P1 closed: SSM ca8da4c1-1b00-496e-a8ea-de513fef93ed 2026-10-09T01:07:24Z Success rc 0, AWS-RunShellScript on i-0167fd745ad906a66: a
- 20261009T010945Z LEG D2 closed: SSM 7f6d5a0a-6d9c-4713-91d8-719b04e5b307 01:07:52-01:08:32Z Success rc 0, run from this seat VER-filled copy deliverable
- 20261009T010945Z LEG V1 closed: same SSM 7f6d5a0a: running root /opt/irpt-resident/26df2c7622-st26, active, restarts 0; allow list OPAL_PRODUCER_PRINCIP
