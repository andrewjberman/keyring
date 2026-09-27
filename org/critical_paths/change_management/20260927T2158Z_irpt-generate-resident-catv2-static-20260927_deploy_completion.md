# Deploy Completion Record
**Date opened:** 2026-09-27T21:58:18.516427+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T224727Z
**Deploy:** Comparison catalogue v2 in generate AND resident together (backend 4b563c98a0; ~Y 102113) + the resident Static-only level tolerance (backend 12a67ed5ee; CTO 101971 item 2); generate code only; resident fe64236bbb-lt -> fe64236bbb-st; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | generate artifact build + upload | census vs live G/TqLPdL: ONLY templates.json differs; flat import | publish 5e266c02cd (cherry-picks a27d119759 = backend 4b563c98a0 templates.json v2; 5e266c02cd = backend 65957b8afc = ~M 5dede2f029 maintained_sources.py); source map: generate's staged maintained_sources.py re-pinned 19d8f3038c -> 5e266c02cd; build-and-upload rc 0; s3 investor-reporting/irpt-ycharts-generate.zip VersionId Iu3nADjaXTWGM3ubzZHPSEr1.DX6nkkj sha ykJltfTdA8tU..; census vs live G/TqLPdL: 111 -> 111, differ maintained_sources.py + templates.json ONLY. Dry plan (ycharts root, backend worktree after terraform init): 0/1/0 code only (s3_object_version 84.Msfap -> Iu3nADja, source_code_hash G/TqLPdL -> ykJltfTd). Suites on the backend: generate 287/30s, _scope 205. | CLOSED 20260927T221656Z |
| U2 | verify | resident package st upload | SUMS vs lt: ONLY extract.py, recipe.py, resident_worker.py, templates.json + bindings; tar sha recorded | build_resident_package.py --pin fe64236bbb (lt's 7 overrides, recipe.py/resident_worker.py/extract.py -> 12a67ed5ee, + templates.json=4b563c98a0, _scope/maintained_sources.py=65957b8afc); SHA256SUMS vs lt: 225/225, differ _scope/maintained_sources.py, extract.py, recipe.py, resident_worker.py, templates.json + resident_bindings.json ONLY, 0 added/removed; tar ./-layout 266 entries sha256 75e672b121a68767c07017965a66b03c9eef4e32c245591fbdd1494aad366bfc uploaded ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-st.tar.gz VersionId 7Ry2IczLye_Br0221ro35cKUNTK8tTLp; member shas recipe 982d8171, worker 9b2dbd18, extract 719369d5, templates 831fe1f2, maintained_sources 0c710edc; main/broker/capture unchanged (0e5c17e7/3d490d6d/5170522c). Install script resident_host_install_st_20260927.sh (bash -n OK). Suites separately: test_calculation_settings 5; test_resident_worker 37/8s; extract 23; generate 287/30s. NOT in this release (naming gate refused at commit): ~Y CATALOGUE_GRANT and FOREIGN_FIRM_NAME_CHECK. | CLOSED 20260927T221657Z |
| D1 | activation | generate safe-apply | both halves at HEAD; plan 0/1/0 code only; readback CodeSha; replan 0 | Both halves at HEAD naming blob f70c9530 (@1da407f0b7): CRO @035b0ab386 102167, CTO @a4ed7d7933 102169 (named: live generate CodeSha + resident running root read back). Live before G/TqLPdL. safe-apply catv2_gen.tfplan (ycharts root): 0 added / 1 changed / 0 destroyed at 22:33:55Z. Readback: irpt-ycharts-generate CodeSha256 ykJltfTdA8tU8/KPafkO5MDxotwagVgiIXSZN0/e3+U= Active/Successful. Re-plan: no changes (detailed-exitcode 0). Rollback: S3 version 84.Msfap (G/TqLPdL). | CLOSED 20260927T224726Z |
| D2 | activation | resident install lt -> st | both halves at HEAD; queue 0/0; controlled stop; install rc 0; polls; host shas == the package; rollback root lt kept | Attempt 1 (SSM 14b49d39) BLOCKED safely at the factory pre-check, unit untouched (log line 2240Z). Script delta 3f4d12ed -> 638addc8 re-signed: CTO @0f4ea3c451 102179, CRO @0844092f92 102180. Attempt 2 SSM 412388ad-355f-44c9-a4f1-38e2e2be16f2: tar + SHA256SUMS OK (225), all 8 member shas checked, factory OK (enrolled 1276035), queue 0/0, controlled stop, install fe64236bbb-st rc 0, active=active polls_30s=2 tracebacks_30s=0, MainPID 208299 since 22:46:12Z, NRestarts 0. RUNNING ROOT READ BACK (systemctl ExecStart): /opt/irpt-resident/fe64236bbb-st; host recipe 982d8171.. worker 9b2dbd18.. (= 12a67ed5ee blobs), broker 3d490d6d.. capture 5170522c.. main 0e5c17e7.. (unchanged). Rollback root fe64236bbb-lt kept. The live Static-branch proof is the next Analysis window's K5. | CLOSED 20260927T224727Z |

## Log

- 20260927T215818Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260927T221656Z LEG U1 closed: publish 5e266c02cd (cherry-picks a27d119759 = backend 4b563c98a0 templates.json v2; 5e266c02cd = backend 65957b8afc = ~M
- 20260927T221657Z LEG U2 closed: build_resident_package.py --pin fe64236bbb (lt's 7 overrides, recipe.py/resident_worker.py/extract.py -> 12a67ed5ee, + t
- 20260927T224726Z LEG D1 closed: Both halves at HEAD naming blob f70c9530 (@1da407f0b7): CRO @035b0ab386 102167, CTO @a4ed7d7933 102169 (named: live gene
- 20260927T224727Z LEG D2 closed: Attempt 1 (SSM 14b49d39) BLOCKED safely at the factory pre-check, unit untouched (log line 2240Z). Script delta 3f4d12ed
- 20260927T224727Z CLOSED -- all 4 legs proven
