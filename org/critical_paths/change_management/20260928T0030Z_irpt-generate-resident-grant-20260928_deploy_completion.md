# Deploy Completion Record
**Date opened:** 2026-09-28T00:30:46.682190+00:00
**Status:** OPEN
**Deploy:** Comparison GRANT release: generate ykJltfTd + resident st -> catalogue GRANTED (6096ee740b) + ~M consumer re-pin (15b9f85eb3 = d7c97910d9) + get_catalogue wiring (2e3d50caac) + foreign-firm name check (c1fd6c5e52); ~Y 102177/102194, ~M 102184, CTO 102169; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | generate build + upload + smoke | census vs live ykJltfTd: only templates.json, maintained_sources.py, generate_installed.py, publication.py, publisher.py; zip_cold_start_smoke PASS | publish cherry-picks 3f80724d2e/3b10bc336c/3523706d32/987689c242 (= backend 2e3d50caac, 6096ee740b, c1fd6c5e52, 15b9f85eb3); generate staged re-pins generate_installed.py -> 2e3d50caac (b4f33b37), publication.py -> c1fd6c5e52 (6aa82b3a), maintained_sources.py -> 15b9f85eb3 (774eca9b); each parent == the live pin; templates.json 54656584 + publisher.py 68900af6 from the checkout (== backend). build-and-upload rc 0; S3 investor-reporting/irpt-ycharts-generate.zip VersionId BIEsyaNnhqvviJymsOOJfc73Oyh5xgp0 sha AdE17rT6f3IZ..; census vs live ykJltfTd: 111 -> 111, differ generate_installed.py, maintained_sources.py, publication.py, publisher.py, templates.json ONLY. Built-zip smoke (~Y zip_cold_start_smoke, POST /analysis): PASS. ~Y zip_module_census with intents named (errors=_authz, entry=ycharts/generate, publication=ycharts/extract, resolve=_scope, transport=ycharts/generate): every collision winner intended; the 6 STALE modules (broker, certify, extract, recipe, resident_main, resident_worker) are byte-equal to live ykJltfTd (resident-side, not moved here). flat_zip_module_census pin skew: _scope maintained_sources @15b9f85eb3 vs the rest @19d8f3038c -- the same one-member skew live ykJltfTd already serves (@5e266c02cd), covered by ~Y's composition arms. | CLOSED 20260928T005024Z |
| U2 | verify | resident package st2 upload | SUMS vs st: only templates.json, maintained_sources.py, publication.py, publisher.py + bindings | build_resident_package.py (st's overrides + templates.json=6096ee740b, maintained_sources.py=15b9f85eb3, publication.py=c1fd6c5e52, publisher.py=c1fd6c5e52); SHA256SUMS vs st: 225/225, differ _scope/maintained_sources.py, ycharts/extract/publication.py, ycharts/generate/publisher.py, ycharts/generate/templates.json + resident_bindings.json ONLY; tar sha256 f681024b7fbe78fe0c8906bbf148ba3f17be1e78bad9fd7b78f26d42e5a22c91 uploaded ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-st2.tar.gz VersionId 2ZLL.I5jJuTCFrlqji.fQM18znQJft4F; install script resident_host_install_st2_20260928.sh (st's, 10 member shas checked, factory pre-check on resident_main.py's own sys.path, rollback to st; bash -n OK). | CLOSED 20260928T005024Z |
| D1 | activation | generate safe-apply | halves at HEAD; live before-read; plan 0/1/0; readback; cold start; after-read; replan 0 |  | OPEN |
| D2 | activation | resident install st -> st2 | halves at HEAD; queue 0/0; install rc 0; polls; running root read back |  | OPEN |

## Log

- 20260928T003046Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260928T005024Z LEG U1 closed: publish cherry-picks 3f80724d2e/3b10bc336c/3523706d32/987689c242 (= backend 2e3d50caac, 6096ee740b, c1fd6c5e52, 15b9f85e
- 20260928T005024Z LEG U2 closed: build_resident_package.py (st's overrides + templates.json=6096ee740b, maintained_sources.py=15b9f85eb3, publication.py=
