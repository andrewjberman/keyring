# Deploy Completion Record
**Date opened:** 2026-09-26T21:17:38.479213+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T212345Z
**Deploy:** IRPT hop 7: ~Y's chart-date certify fix into the resident (fe64236bbb + ycharts/extract/certify.py @ad817b55ea); ~Y 101492
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | activation | resident package on i-0167fd745ad906a66 | SUMS vs fe64236bbb: exactly certify.py + bindings; controlled stop on an empty queue; install rc 0; unit polls; host sha of certify.py = ad817b55ea blob; rollback root fe64236bbb kept | package = fe64236bbb + ycharts/extract/certify.py @ad817b55ea via build_resident_package.py --override (715386c211); SUMS vs rebuilt fe64236bbb: exactly certify.py (f1516e24.. -> 33e54ac0..) + resident_bindings.json differ; tar cf4326c6ef84285f.. at s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-h7.tar.gz version jdWKCBKU2YfmHjMSag2Kr6q8jpIQ042O; SSM caa4f434 (resident_host_install_hop7_20260926.sh): tar sha verified, SUMS OK 225, certify sha verified, host manifest 325cee0b.. (3652 with pydeps), factory dry run OK (enrolled 1276035), queue 0/0, controlled stop 21:20:43Z, install rc 0, unit active MainPID 155920 NRestarts 0 since 21:20:44Z on /opt/irpt-resident/fe64236bbb-h7, IRPT_RESIDENT_POLL x2, 0 tracebacks; running root certify.py sha 33e54ac0.. = ad817b55ea blob. Rollback root fe64236bbb (and f624e8a72f) retained; prior receipt kept as cutover_receipt.fe64236bbb.json. | CLOSED 20260926T212344Z |

## Log

- 20260926T211738Z OPENED by 2.0.0_SA_COO~P with 1 leg(s)
- 20260926T212344Z LEG R1 closed: package = fe64236bbb + ycharts/extract/certify.py @ad817b55ea via build_resident_package.py --override (715386c211); SUM
- 20260926T212345Z CLOSED -- all 1 legs proven
