# Deploy Completion Record
**Date opened:** 2026-09-29T08:00:28.432331+00:00
**Status:** OPEN
**Deploy:** Resident st3 -> st4: recipe.py + resident_worker.py @14c961af32 (IB-yr-201 S194: a Comparison sends its models and refuses a PDF printing none; IB-yr-211 S193: a resolve RETRY is logged and re-offered in 60 s); ~Y 102630/102647; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | resident package st4 upload | SUMS vs st3: only recipe.py, resident_worker.py + bindings; tar sha; S3 VersionId; install script | build_resident_package.py --pin fe64236bbb with st3's 12 overrides, recipe.py + resident_worker.py re-pinned ec8f69f718 -> 14c961af32 (IB-yr-201 @f287444013 + IB-yr-211, drained by ~Y; ~Y 102647). SHA256SUMS vs st3: 225/225, differ recipe.py (4fde9ac9 -> b2fbd720), resident_worker.py (95f79dad -> 0b67be2a) and resident_bindings.json ONLY; tar 266 members = st3's; tar sha 7d10152c.. uploaded ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-st4.tar.gz VersionId jK0FFkzC_Oc8m3mZMiatYrPCpuyOc9ZE, read back by version sha equal. Install script resident_host_install_st4_20260929.sh = st3's with NEW/OLD/KEY/tar/recipe/worker shas and receipt ledger changed only; bash -n OK. | CLOSED 20260929T081244Z |
| D1 | activation | resident install st3 -> st4 | halves at HEAD; ~Y gates on built st4; queue 0/0; install rc 0; polls; running root + member shas |  | OPEN |

## Log

- 20260929T080028Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260929T081244Z LEG U1 closed: build_resident_package.py --pin fe64236bbb with st3's 12 overrides, recipe.py + resident_worker.py re-pinned ec8f69f718 
