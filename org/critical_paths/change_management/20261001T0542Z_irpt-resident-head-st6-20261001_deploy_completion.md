# Deploy Completion Record
**Date opened:** 2026-10-01T05:42:02.735040+00:00
**Status:** OPEN
**Deploy:** Resident st5 to st6: the whole tree at CLOUD HEAD (IB-yr-293, the terminal authority refusal, IB-yr-291, certification handed the comparisons) and the host capture library at the same pin; CTO rulings batch 61 item 2c; row S244
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | resident package st6 built, gated and uploaded | gate G1-G5 PASS on the built package; tar sha256; S3 VersionId read back by version; install script sha256 | Built by build_resident_package.py at pin 36dfa80058 with no member override (243 members). Gate resident_package_gate.py PASS: G1 243 of 243 members hash to SHA256SUMS; G2 241 of 241 equal git show 36dfa80058:path; G3 98 of 98 .py compile; G4 2 operation constants, 0 unserved; G5 against running st5: added 18, removed 0, changed 39, identical 186. Tar sha256 3eb86dd967db4b672c5243267f3142d53ee227d506f6a12e086e9d69755864b2, 753160 bytes, NEW key ec2/investor-reporting-ycharts/resident/irpt-resident-36dfa80058-st6.tar.gz (HeadObject 404 before; st5 key 731610 as positive control), VersionId G6ZEskNLZl_v7QG_aZ9IfxOPrFVmDd3J, read back by version: sha equal. Install script sha256 830682df93d1a05cc2618a16305783e0019636dc538d924e696832289b9af9a6, VersionId Xxgbj.B9Yw4XiUUuDrKG4PGYmKIXtTm6, read back by version: sha equal; bash -n clean. Suites at the pin: generate 314 passed, session 100, extract 33, resident_installed with the resident suite 50 passed. Nothing installed. | CLOSED 20261001T055203Z |
| D1 | activation | resident install st5 to st6 with the host capture library | both halves at HEAD on the packet blob; queue 0/0; install rc 0; running root; polls; 0 Tracebacks |  | OPEN |
| V1 | verify | running bytes read back on the host (row S244) | current_authority.py digest equals the package and names allowedFirmIds; resident_worker.py names PERMANENT_AUTHORITY_REFUSALS; host library sha equals the bindings |  | OPEN |
| R1 | verify | dead-letter redrive of REQ-86f1ce70 and REQ-3a1b73a8 | each job terminal by name in irpt-jobs with its journal line; dead-letter queue 0 |  | OPEN |

## Log

- 20261001T054202Z OPENED by 2.0.0_SA_COO~Y with 4 leg(s)
- 20261001T055203Z LEG U1 closed: Built by build_resident_package.py at pin 36dfa80058 with no member override (243 members). Gate resident_package_gate.p
