# Deploy Completion Record
**Date opened:** 2026-09-29T09:33:11.140294+00:00
**Status:** OPEN
**Deploy:** HoldingsSnapshot contract CATEGORY revision (a69fe8e33e, additive) served in irpt-holdings + irpt-ycharts-generate (TO-IB-pr-212 @dc1fc92e4e); step 1 of ~M's L0-categories release (102599); halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | two artifacts build + upload + gates | census vs live: ONLY contracts/HoldingsSnapshot.schema.json differs in each; cold start | Source map (TO-IB-pr-212 @dc1fc92e4e): both functions stage docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json at a69fe8e33e. irpt-ycharts-generate: recipe.py/resident_main.py/resident_worker.py PINNED to the LIVE blobs (03ea5980cc f18ab757 / 4ed7edaaa8 cfe19f8a / bb1eb7f92b 09bd7688) -- a first build from HEAD would have moved those resident-side modules too. build-and-upload rc 0 BAU_PARITY_SKIP=1; tracked sources restored (0 deleted left). irpt-holdings: S3 investor-reporting/irpt-holdings.zip VersionId vN9FiyknGePr9_jjYB3r0rr7cbG11awK sha U4/P5Bh3sfth..; census vs live kZygK57y: 33 -> 33, differ contracts/HoldingsSnapshot.schema.json ONLY. irpt-ycharts-generate: VersionId GP__8T1nIcOMpzQVh1saTMdBiYJQ5ovR sha wnt7hjABEc73..; census vs live AdE17rT6: 111 -> 111, differ contracts/HoldingsSnapshot.schema.json ONLY. Cold start /var/task mapped, live vs new, both functions: IMPORT OK, the same named envelope, rc 0. | CLOSED 20260929T095015Z |
| D1 | activation | apply both functions | halves at HEAD; before-read (a served snapshot validates); plan code-only; safe-apply; readback; cold start; after-read; re-plan 0 |  | OPEN |

## Log

- 20260929T093311Z OPENED by 2.0.0_SA_COO~P with 2 leg(s)
- 20260929T095015Z LEG U1 closed: Source map (TO-IB-pr-212 @dc1fc92e4e): both functions stage docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema
