# Deploy Completion Record
**Date opened:** 2026-10-09T02:22:40.738735+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN st27: resident st24 -> st27 (the Opal brand asset, no svc) on i-0167fd745ad906a66 -- the st26 shape minus svc and the F1/X1 legs
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | verify | st27 tar + install script staged in S3, read back by version | sha256 equal to the declared values; both keys 404 before | BOTH KEYS 404 BEFORE (explicit head-object). tar ec2/investor-reporting-ycharts/resident/irpt-resident-e606008994-st27.tar.gz v S51IxQHe6DZBgq9EQLNhc3UTrEbXqi_V, read back BY VERSION and hashed = 20916261074c356ab31497b338a6957e3d72cb252b8a3f54432db98610da39e4 = declared; install script .../resident_host_install_e606008994-st27.sh v 1Nr9jWADLtJSLU9x0piz7DT2Dnu9qeEk, read back BY VERSION and hashed = 64a817c58c66ebd181cd00e4663c6fdfc0592f49e29dcc506c38686853bc0eab = declared. Census e606008994-st27.census.json cross-checked and DERIVED not restated: old_root 409e3066d1-st24, new_root e606008994-st27, members 269, added 2 (ycharts/research/brand/Opal-Capital-Logo-Full-Color.svg, brand.json) + changed 2 (reports/resident_bindings.json, ycharts/research/layout_overview.py) + removed 0 => identical 265, exactly the order figures; gates G1-G4 true; tar_sha256 in the census equals the measured tar. VER=1Nr9jWADLtJSLU9x0piz7DT2Dnu9qeEk written into THIS SEAT lane copy at deliverables/irpt_ycdgen_st27/install_st27.sh (the COO lane file is untouched, per owned-paths). PRE-FLIGHT READ OF THE SCRIPT: its header comment says it fetches BY KEY AND VERSION, but line 13 is a plain aws s3 cp by KEY and VER is never used in the fetch -- so the st25 exit-30 class (host role lacks s3:GetObjectVersion) does NOT apply here; the sha256 check at line 14 binds the bytes | CLOSED 20261009T022259Z |
| P1 | verify | host pre-read (root st24, allow list Andrew only, queue 0/0) | host_read.py pre_read.sh via SSM, rc 0, recorded |  | OPEN |
| D2 | activation | install_st27.sh via SSM from this seat VER-filled lane copy | root e606008994-st27 active, NRestarts 0, rc=0 |  | OPEN |
| V1 | verify | load_brand resolves ycharts/research/brand/ from the RUNNING root with no brand env var | read from the running root; a fall-back is a STOP plus rollback (CTO half); the shell window closes after V1 |  | OPEN |

## Log

- 20261009T022240Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 4 leg(s)
- 20261009T022259Z LEG U2 closed: BOTH KEYS 404 BEFORE (explicit head-object). tar ec2/investor-reporting-ycharts/resident/irpt-resident-e606008994-st27.t
