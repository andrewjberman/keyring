# Deploy Completion Record
**Date opened:** 2026-09-28T23:32:14.018761+00:00
**Status:** OPEN
**Deploy:** irpt-performance-adapter hcZpXDDo -> IB-pr-194: a RETAINED 49F report whose series reaches <= -1 is refused at reopen (EngineReturnImplausible, DEPENDENCY_UNAVAILABLE); closes irpt-adapter-implausible-guard-20260928 D1's served gap; moves exactly 2 of 23 retained 49F reports (790fe675, 74fb35a4); no store mutation; code only; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | artifact build + upload + gates | census vs live hcZpXDDo: ONLY retained.py differs; flat_zip_module_census + ~Y zip_module_census byte-equal flags + cold start with /var/task mapped | publish source map: irpt-performance-adapter staged retained.py b18cb77c7d -> 90c4b596f3 (880cf928), commit 40b755719d; all 69 pinned blobs measured == live hcZpXDDo before the edit. build-and-upload rc 0 with BAU_PARITY_SKIP=1 (build tooling not members, per _build_note); the build's deletion of tracked performance/*.py restored in the worktree. S3 investor-reporting/irpt-performance-adapter.zip VersionId 5bmwADQsNWxADpJYfNXeLlUPoeKPDb8G sha qfxZ0DzBGcSrD2B0ownwGZtSLskLGuw4vnqyASd0AMA= (418269 bytes, write verified). CENSUS vs live hcZpXDDo: 69 -> 69, differ retained.py ONLY. flat_zip_module_census: pin skew 0, rc 0. ~Y zip_module_census (entry/handler/transport intents named): FAIL set errors/maintained_sources/request_composition/resolve/routetable, all byte-equal to live; the live zip fails the same set plus retained.py (STALE vs the tree -- the move resolves it). COLD START with /var/task mapped: new and live both import runtime and answer invoke {} with a named envelope, rc 0. Dry plan (performance root, plan var default null): 0/1/0 code only (s3_object_version wVW7wVQw -> 5bmwADQs, source_code_hash hcZpXDDo -> qfxZ0DzB). | CLOSED 20260928T233613Z |
| D1 | activation | performance root safe-apply | both halves at HEAD; before-read of the NEW-01 retained 1Y + YTD and a control via the CRO walk (discriminating: the reopen path); plan 0/1/0 code only; readback CodeSha; real cold-start invoke; the same reads after; replan 0 |  | OPEN |
| A1 | verify | the Performance page | NEW-01 1Y and YTD show a named refusal on the page; the control shows its figure |  | OPEN |

## Log

- 20260928T233214Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260928T233613Z LEG U1 closed: publish source map: irpt-performance-adapter staged retained.py b18cb77c7d -> 90c4b596f3 (880cf928), commit 40b755719d; 
