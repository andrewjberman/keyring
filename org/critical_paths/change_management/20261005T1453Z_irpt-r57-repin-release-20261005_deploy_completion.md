# Deploy Completion Record
**Date opened:** 2026-10-05T14:53:11.753599+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261005T203621Z
**Deploy:** IRPT_BCKEND release r57: the r55 re-pin set to 4 functions (49f-reporting-read, export-render, directory-search, holdings); CTO half @3d6e1ed58c, COO half; irpt-status by ~Y
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| RR1 | verify | irpt-49f-reporting-read-lambda before-read = anchor + baseline invokes | CodeSha256 + payloads | before-read 2026-10-05 ~20:3xZ: irpt-49f-reporting-read-lambda CodeSha256 Wzf2qS5PBH8X..=anchor LastModified 10-03 17:03Z; baseline invokes: change=UNEXPECTED(directory-less reporting-read refusal), happy=200 ETag d67a4ad4.. manifest 0024480090 as_of 2026-10-02 | CLOSED 20261005T201823Z |
| RR2 | activation | irpt-49f-reporting-read-lambda build+upload+targeted safe-apply | live CodeSha256 = built | build-and-upload built j5R13Pnv+3+LdbjREHuuldudMS03N7G830VOoKlle7o= (landed on key irpt-49f-reporting-read-lambda.zip, NOT the TF-read key irpt-reporting-read-lambda.zip: server-side copy-object to the TF key, versioned, metadata sha verified); plan 0/1/0 source_code_hash+s3_object_version only; safe-apply 20:22Z 0/1/0 no override; live CodeSha256 j5R13Pnv.. = built, rollback anchor Wzf2.. = key version CYy_ok1Rf7Yjpg4j37BWJUAD6YOKhvvk | CLOSED 20261005T202303Z |
| RR3 | verify | irpt-49f-reporting-read-lambda change + happy invokes | payloads | after-deploy 20:22Z: change invoke wire response byte-identical to baseline (UNEXPECTED), log irpt_internal classifier_code FIRM_BINDING (was UNEXPECTED); happy invoke byte-identical to baseline (200, ETag d67a4ad4.., manifest) | CLOSED 20261005T202303Z |
| ER1 | verify | irpt-export-render before-read = anchor + baseline invokes | CodeSha256 + payloads | before-read: irpt-export-render CodeSha256 WDAv+kWKGcXB..=anchor LastModified 10-03 17:13Z; receipt EXP-e29b head-object OK 870B (CTO batch 265 condition); baseline: happy route=/api/scoped/investor-reporting/export/EXP-e29b../download (stored route already live); change fixture route=/api/scoped/exports/EXP-5757../download (old) | CLOSED 20261005T201823Z |
| ER2 | activation | irpt-export-render build+upload+targeted safe-apply | live CodeSha256 = built | head-object receipt EXP-e29b 870B before invoke (batch 265 condition); build-and-upload sha QVZQo07b87PSYl61hobRF5yWGNZ+jckVsrwYxhdEmqE= to investor-reporting/irpt-export-render.zip (= TF key); member diff vs live = exactly bundle.py, entry.py, ExportBundle.schema.json, loaders.py, served.py (census); plan 0/1/0 hash+version only; safe-apply 20:30Z 0/1/0; live CodeSha256 = built; rollback anchor WDAv+kWK.. = key version 2T_3QXq3RRxBiMzXZX6tYNfagmiXdS6h | CLOSED 20261005T203040Z |
| ER3 | verify | irpt-export-render change + happy invokes | payloads | after-deploy 20:30Z: change fixture route moved /api/scoped/exports/EXP-5757../download -> /api/scoped/investor-reporting/export/EXP-5757../download (the one predicted response difference); happy receipt read byte-identical to baseline (live route, EXP-e29b..); receipt key unchanged 870B LastModified 10-03 22:13:15 (no finalize write) | CLOSED 20261005T203040Z |
| DS1 | verify | irpt-directory-search before-read = anchor + baseline invokes | CodeSha256 + payloads | before-read: irpt-directory-search CodeSha256 AVSIaHEhm+E7..=anchor LastModified 10-01 06:26Z; baseline: change=UNEXPECTED directory-browse, happy=envelope 1 entry | CLOSED 20261005T201823Z |
| DS2 | activation | irpt-directory-search build+upload+targeted safe-apply | live CodeSha256 = built | build-and-upload sha OmSwySstxlzs8Svf38u0Zyoc8ucHBHxJ99SOI6HVGlA= to investor-reporting/irpt-directory-search.zip (= TF key); member diff vs live: only loaders.py changed (census match); plan 0/1/0 hash+version only; safe-apply 20:25Z 0/1/0; live CodeSha256 = built; rollback anchor AVSIaHEh.. = key version Uk52k9Sk88nX0MbBHsSIMJDSvSOpRUnA | CLOSED 20261005T202559Z |
| DS3 | verify | irpt-directory-search change + happy invokes | payloads | after-deploy 20:25Z: change and happy invoke responses byte-identical to baseline; log classifier_code FIRM_BINDING (was UNEXPECTED) | CLOSED 20261005T202559Z |
| HO1 | verify | irpt-holdings before-read = anchor + baseline invokes | CodeSha256 + payloads | before-read: irpt-holdings CodeSha256 RmruvCeoZtax..=anchor LastModified 10-05 00:12Z; baseline change=UNEXPECTED holdings-snapshot; happy needs a current sel_ (read-only table read), see HO3 | CLOSED 20261005T201823Z |
| HO2 | activation | irpt-holdings build+upload+targeted safe-apply | live CodeSha256 = built | build-and-upload sha skOqPofToy4zOzBj24FkCC55+SUKhgqcl691RpNZEvA= to investor-reporting/irpt-holdings.zip (= TF key); member diff vs live: only loaders.py; plan 0/1/0 hash+version only; safe-apply 20:27Z 0/1/0; live CodeSha256 = built; rollback anchor RmruvCeo.. = key version mnvnxd8N58uEcOmLLUwc4DWgg3J07qb_ | CLOSED 20261005T202825Z |
| HO3 | verify | irpt-holdings change + happy invokes | payloads | after-deploy 20:27Z: change invoke byte-identical to baseline, log classifier_code FIRM_BINDING (was UNEXPECTED). Happy = BASELINE EQUALITY on a placeholder sel_ id (UNAVAILABLE, business_date 2026-09-24, identical both sides); NOT a READY read (no current selection used, per batch 265). Cold start occurred on the first invoke after the code change | CLOSED 20261005T202825Z |
| R1 | git | record-terraform-deploy per function | commit | record-terraform-deploy per function (4); committed 4c93f975e9 (source map + CHANGELOG; audit jsonl excluded, pre-existing dirty) | CLOSED 20261005T203553Z |

## Log

- 20261005T145311Z OPENED by 2.0.0_SA_COO~P with 13 leg(s)
- 20261005T201823Z LEG RR1 closed: before-read 2026-10-05 ~20:3xZ: irpt-49f-reporting-read-lambda CodeSha256 Wzf2qS5PBH8X..=anchor LastModified 10-03 17:03
- 20261005T201823Z LEG ER1 closed: before-read: irpt-export-render CodeSha256 WDAv+kWKGcXB..=anchor LastModified 10-03 17:13Z; receipt EXP-e29b head-object
- 20261005T201823Z LEG DS1 closed: before-read: irpt-directory-search CodeSha256 AVSIaHEhm+E7..=anchor LastModified 10-01 06:26Z; baseline: change=UNEXPECT
- 20261005T201823Z LEG HO1 closed: before-read: irpt-holdings CodeSha256 RmruvCeoZtax..=anchor LastModified 10-05 00:12Z; baseline change=UNEXPECTED holdin
- 20261005T202303Z LEG RR2 closed: build-and-upload built j5R13Pnv+3+LdbjREHuuldudMS03N7G830VOoKlle7o= (landed on key irpt-49f-reporting-read-lambda.zip, N
- 20261005T202303Z LEG RR3 closed: after-deploy 20:22Z: change invoke wire response byte-identical to baseline (UNEXPECTED), log irpt_internal classifier_c
- 20261005T202559Z LEG DS2 closed: build-and-upload sha OmSwySstxlzs8Svf38u0Zyoc8ucHBHxJ99SOI6HVGlA= to investor-reporting/irpt-directory-search.zip (= TF 
- 20261005T202559Z LEG DS3 closed: after-deploy 20:25Z: change and happy invoke responses byte-identical to baseline; log classifier_code FIRM_BINDING (was
- 20261005T202825Z LEG HO2 closed: build-and-upload sha skOqPofToy4zOzBj24FkCC55+SUKhgqcl691RpNZEvA= to investor-reporting/irpt-holdings.zip (= TF key); me
- 20261005T202825Z LEG HO3 closed: after-deploy 20:27Z: change invoke byte-identical to baseline, log classifier_code FIRM_BINDING (was UNEXPECTED). Happy 
- 20261005T203040Z LEG ER2 closed: head-object receipt EXP-e29b 870B before invoke (batch 265 condition); build-and-upload sha QVZQo07b87PSYl61hobRF5yWGNZ+
- 20261005T203040Z LEG ER3 closed: after-deploy 20:30Z: change fixture route moved /api/scoped/exports/EXP-5757../download -> /api/scoped/investor-reportin
- 20261005T203553Z LEG R1 closed: record-terraform-deploy per function (4); committed 4c93f975e9 (source map + CHANGELOG; audit jsonl excluded, pre-existi
- 20261005T203621Z CLOSED -- all 13 legs proven
