# Deploy Completion Record
**Date opened:** 2026-09-28T21:17:45.105450+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T002731Z
**Deploy:** irpt-performance-adapter F0bYtOfB -> hcZpXDDo (IB-pr-191): a linked engine day with r_net <= -1 refuses EngineReturnImplausible (DEPENDENCY_UNAVAILABLE) -- 26 YTD rows / 22 accounts move from served to refused. NOT CLOSED BY THIS ACT: 2 invested near-miss accounts (r_net -0.999631, -0.999959) keep serving about -100% (row S184; closed by row S181's producer fix or a class predicate). Code only; halves CTO b2239fa58f, CRO 3f953cb06b
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | artifact build + upload + gates | census vs live F0bYtOfB: ONLY entry.py + f49_engine.py differ; flat_zip_module_census + ~Y zip_module_census + built-zip cold-start smoke PASS | publish source map: irpt-performance-adapter staged entry.py c8ef8b7751 -> 57a58117fb (4d22ff2e) and f49_engine.py 8d7a8b10fe -> 57a58117fb (07ce5fff), commit 1af199f0f8; all 69 pinned blobs measured == live F0bYtOfB before the edit. build-and-upload rc 0 with BAU_PARITY_SKIP=1 (build tooling build_candidate/build_dependencies/cot_probe are not members, per the row's _build_note); the build's deletion of tracked performance/*.py restored in the worktree. S3 investor-reporting/irpt-performance-adapter.zip VersionId wVW7wVQw8BmW6rE3XzeVeYJhqQJHjoGO sha hcZpXDDofuUX2YImni0nsCDyLOxHl2Mxc1IvEBwG0+0= (417678 bytes, write verified). CENSUS vs live F0bYtOfB: 69 -> 69, differ entry.py + f49_engine.py ONLY. flat_zip_module_census: shared-package pin skew 0, rc 0. ~Y zip_module_census: with intents named (entry/handler/transport = performance/), FAIL set errors/maintained_sources/request_composition/resolve/routetable -- every one byte-equal to live (the live zip fails a superset). COLD START: ~Y zip_cold_start_smoke fails on BOTH zips at /var/task/firm_registry.json (a Linux path, Windows host: non-discriminating, stated); the same smoke with /var/task mapped to the extraction dir: new and live both import runtime and answer invoke {} with a named UNAVAILABLE envelope, rc 0. Dry plan (performance root, approved_performance_plan default null): 0/1/0, code only (s3_object_version G4UtfeeR -> wVW7wVQw, source_code_hash F0bYtOfB -> hcZpXDDo). | CLOSED 20260928T212657Z |
| D1 | activation | performance root safe-apply | both halves at HEAD naming the packet blob; LIVE before-read of the NEW-01 account YTD; plan 0/1/0 code only; readback CodeSha; cold start; the same read after; replan 0 | hcZpXDDo applied 22:02:49Z (halves CTO b2239fa58f, CRO 3f953cb06b; readback, real cold start Init 461.73 ms, replan clean). The CRO's first AFTER-read (@5f82151a2e) was NOT MET: the page reopens RETAINED reports (26 reopens, 0 engine runs). The served gap closed by the follow-on act irpt-adapter-reopen-guard-20260928 (qfxZ0DzB, 00:11:21Z); CRO 102505 @283d590379: NEW-01 YTD + 1Y read the named refusal, control 5.93 unchanged. | CLOSED 20260929T002708Z |
| A1 | verify | the Performance page | the NEW-01 account no longer shows -100% on the signed-in page (the next walk window) | CRO 102505 (@283d590379): the page shows the named refusal for NEW-01 YTD and 1Y ('temporarily unavailable ... upstream data source', pickers YTD/1Y unavailable) and the control's 5.93 unchanged, same shots as D1. Carried, not closed: S184's 2 near-miss invested accounts (close route: the consolidated holdings gold, PRD v0.19). | CLOSED 20260929T002708Z |

## Log

- 20260928T211745Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260928T212657Z LEG U1 closed: publish source map: irpt-performance-adapter staged entry.py c8ef8b7751 -> 57a58117fb (4d22ff2e) and f49_engine.py 8d7a8
- 20260929T002708Z LEG D1 closed: hcZpXDDo applied 22:02:49Z (halves CTO b2239fa58f, CRO 3f953cb06b; readback, real cold start Init 461.73 ms, replan clea
- 20260929T002708Z LEG A1 closed: CRO 102505 (@283d590379): the page shows the named refusal for NEW-01 YTD and 1Y ('temporarily unavailable ... upstream 
- 20260929T002731Z CLOSED -- all 3 legs proven
