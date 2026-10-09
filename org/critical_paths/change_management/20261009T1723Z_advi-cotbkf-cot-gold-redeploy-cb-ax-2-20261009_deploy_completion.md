# Deploy Completion Record
**Date opened:** 2026-10-09T17:23:30.166896+00:00
**Status:** OPEN
**Deploy:** ADVI_COTBKF round 50 CB-ax-2: cot gold redeploy -- FOUR keys in opal-data-cot code/gold/ as the UNION of every tool's printed list (ADDENDUM 18), in write order: ticker_overrides.py MINTS, legacy_addresses.json MINTS, then build_canonical_prices_v2.py and B_00.canonical_holdings.py by safe-deploy. Pair: COO half @ea3b5ad9f8 (blob 2186cd1adc) + CTO half @fe56ae564e GIVEN under conditions 1-4. scopes.json NOT written. Rollback is copy-object of the two prior script VersionIds; minted files are never deleted by this seat
**Authored by:** 0.7.0_AE_CloudOps~CB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | verify | before-reads and the diff census, printed before any write | ticker_overrides.py and legacy_addresses.json both still 404 against a positive control; writer VersionId still GAOI7tORcF7V7F0fW9NMH35bonjXEwzj and B_00 still hU7ZrZTD5NDlVvuSo9aBMUd1hKUg_lAe; all four repo-side sha256 equal the pair's table; the served-vs-repo diff for each script confined to the pair's NAMED changes, any line outside meaning STOP |  | OPEN |
| M1 | activation | MINT code/gold/ticker_overrides.py first, by one put-object of the exact repo blob bytes | the key re-read 404 immediately before the put; bytes taken from the blob with no re-serialisation; served sha256 equals 4d407c3acf2c3fd4106050af98010541646571b88148115549b0997ccc817015 |  | OPEN |
| M2 | activation | MINT code/gold/legacy_addresses.json second, by one put-object of the exact repo blob bytes | the key re-read 404 immediately before the put; served sha256 equals 34dfcb376088328686d1c9a3fabae279e1316373f8470a969b5d513d7eedfe17 |  | OPEN |
| D1 | activation | deploy the writer third, by .tools/safe-deploy.sh | prior VersionId re-read immediately before and still GAOI7tORcF7V7F0fW9NMH35bonjXEwzj; the tool's key list printed and holding only this script; rc 0; a lane refusal STOPS the order and is not bypassed |  | OPEN |
| D2 | activation | deploy B_00 fourth, by .tools/safe-deploy.sh | prior VersionId re-read immediately before and still hU7ZrZTD5NDlVvuSo9aBMUd1hKUg_lAe; rc 0; no key written outside the pair's union list |  | OPEN |
| P1 | verify | read all FOUR served keys back and confirm each sha256 | 4d407c3a... / 34dfcb37... / 8b733bb1... / 2b38b142...; both prior script VersionIds still retrievable as the only rollback |  | OPEN |
| V1 | verify | CB50ax2-AC1 plus the two reads the amendments add, all on the FETCHED SERVED bytes | in a detached scratch worktree with NO lib/opal_naming on the path: pytest test_cot_gold_failclosed.py reads passed (scopes-absent, overrides-absent and legacy-absent each STOP with 0 rows; a synthetic rps day with no ImportError; 757 overrides and 104 corrections); the written-key census equals the pre-change writer's with no new key class; and IMPORT-CLOSURE b00_modules=<n> writer_modules=<m> missing=0 against a paginated listing of the mirror with its denominator printed |  | OPEN |

## Log

- 20261009T172330Z OPENED by 0.7.0_AE_CloudOps~CB2 with 7 leg(s)
