# Deploy Completion Record
**Date opened:** 2026-09-29T09:33:11.140294+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T122815Z
**Deploy:** HoldingsSnapshot contract CATEGORY revision (a69fe8e33e, additive) served in irpt-holdings + irpt-ycharts-generate (TO-IB-pr-212 @dc1fc92e4e); step 1 of ~M's L0-categories release (102599); halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | two artifacts build + upload + gates | census vs live: ONLY contracts/HoldingsSnapshot.schema.json differs in each; cold start | Source map (TO-IB-pr-212 @dc1fc92e4e): both functions stage docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json at a69fe8e33e. irpt-ycharts-generate: recipe.py/resident_main.py/resident_worker.py PINNED to the LIVE blobs (03ea5980cc f18ab757 / 4ed7edaaa8 cfe19f8a / bb1eb7f92b 09bd7688) -- a first build from HEAD would have moved those resident-side modules too. build-and-upload rc 0 BAU_PARITY_SKIP=1; tracked sources restored (0 deleted left). irpt-holdings: S3 investor-reporting/irpt-holdings.zip VersionId vN9FiyknGePr9_jjYB3r0rr7cbG11awK sha U4/P5Bh3sfth..; census vs live kZygK57y: 33 -> 33, differ contracts/HoldingsSnapshot.schema.json ONLY. irpt-ycharts-generate: VersionId GP__8T1nIcOMpzQVh1saTMdBiYJQ5ovR sha wnt7hjABEc73..; census vs live AdE17rT6: 111 -> 111, differ contracts/HoldingsSnapshot.schema.json ONLY. Cold start /var/task mapped, live vs new, both functions: IMPORT OK, the same named envelope, rc 0. | CLOSED 20260929T095015Z |
| D1 | activation | apply both functions | halves at HEAD; before-read (a served snapshot validates); plan code-only; safe-apply; readback; cold start; after-read; re-plan 0 | Halves: CTO 102755 (condition replaced by (a)+(b), 102767), CRO 102759 + addendum 1 (102770), packet blob 9f638d70. S3 latest = vN9Fiykn / GP__8T1n at each apply. safe-apply holdings 12:05Z, ycharts 12:07Z (0 STOP, HALT_ACK=1), each 0/1/0. Readback: irpt-holdings U4/P5Bh3, irpt-ycharts-generate wnt7hjAB, deployed zips member-equal to the artifacts (33, 111; only contracts/HoldingsSnapshot.schema.json vs prior live). BEFORE/AFTER three-firm assembled validation (served publication.capture, Draft 2020-12) 49F 151,697 / COT 16,749 / INF 33,328 nodes VALID under the new copy. Fresh-container invokes: holdings GET + generate POST refused CONTRACT_VERSION, Init present, 0 errors; generate import census 59/0 failed; Registry build on the deployed bytes offline OK (revision schemas-4780eaf85be2). Re-plan both: No changes. Holdings card through the page on 49F + INF at 12:22-12:24Z (4.0.0_SA_CRO walk, 102790). Record: org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/HOLDINGS_CONTRACT_CATEGORY_APPLY_READS_20260929.md @6bec26c0a7. Rollback keys: ZbLWvaO1 / BIEsyaNn. | CLOSED 20260929T122815Z |

## Log

- 20260929T093311Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260929T095015Z LEG U1 closed: Source map (TO-IB-pr-212 @dc1fc92e4e): both functions stage docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema
- 20260929T122815Z LEG D1 closed: Halves: CTO 102755 (condition replaced by (a)+(b), 102767), CRO 102759 + addendum 1 (102770), packet blob 9f638d70. S3 l
- 20260929T122815Z CLOSED -- all 2 legs proven
