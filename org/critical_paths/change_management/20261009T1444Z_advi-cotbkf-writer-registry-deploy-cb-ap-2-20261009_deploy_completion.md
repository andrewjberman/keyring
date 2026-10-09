# Deploy Completion Record
**Date opened:** 2026-10-09T14:44:16.684353+00:00
**Status:** OPEN
**Deploy:** ADVI_COTBKF round 42 CB-ap-2: deploy the cot price writer + its pinned registry -- TWO keys in opal-data-cot code/gold/: build_canonical_prices_v2.py (prior 4M4XPMtc2JCbbWi22WuxrVIaicQqPzy6 -> sha 3ac0a502...7f6682) and scopes.json which MINTS from blob 261c0cf8 (sha 13947f7f...edeaade). Pair: COO half + CTO half @d92ed8390f GIVEN under conditions 1-3. ROLLBACK IS THE WRITER COPY-BACK ONLY -- scopes.json is NEVER deleted, not even on refusal (CTO amendment; an S3 delete is Andrew's act)
**Authored by:** 0.7.0_AE_CloudOps~CB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | verify | before-reads and the TWO-KEY census, printed before any write | writer VersionId still 4M4XPMtc2JCbbWi22WuxrVIaicQqPzy6 and scopes.json still 404 against a positive control; repo sha256 values equal the pair's table; the total write set is EXACTLY the two granted keys and nothing else -- reported from BOTH instruments because the deploy tool cannot see a key it does not deploy |  | OPEN |
| W1 | activation | the writer via .tools/safe-deploy.sh | key list printed first and holding exactly the writer with no rider; version re-read immediately before; rc 0; a lane refusal STOPS the order and is not bypassed |  | OPEN |
| W2 | activation | scopes.json MINTED by a single put-object of the exact blob bytes | the key re-read 404 immediately before the put; the bytes are git cat-file -p 261c0cf8adf46ade84fefd1144092c5665df7477 and nothing re-serialised; new VersionId recorded |  | OPEN |
| P1 | verify | read BOTH served keys back and confirm each sha256 | writer served sha256 equals 3ac0a502...7f6682 and scopes.json served sha256 equals 13947f7f...edeaade; the writer's prior version still retrievable as the only rollback |  | OPEN |
| V1 | verify | CB42ap2-AC1 -- the proof on the FETCHED SERVED files in a detached scratch worktree | both fetched files placed in a detached worktree at HEAD (writer at its repo path, scopes.json where the test fixture reads the registry), python -m pytest data/cot/scripts/gold/tests/test_canonical_prices_source_firm.py -q reads passed, the import path recorded, the worktree removed and the shared tree verified untouched |  | OPEN |

## Log

- 20261009T144416Z OPENED by 0.7.0_AE_CloudOps~CB2 with 5 leg(s)
