# Deploy Completion Record
**Date opened:** 2026-09-12T08:56:20.424832+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260912T090453Z
**Deploy:** IRPT_BCKEND IB-rt-6: re-mint the investor-reporting bundle with the trading-calendar member, and re-drive the fire so the host's import check can be read
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the member declaration in .tools/safe_deploy_core.py committed | commit hash | 6e9ad7851e -- .tools/safe_deploy_core.py declares trading_calendar.py with repo_path lib/trading_calendar.py and sha_metadata_key trading-calendar-sha256 | CLOSED 20260912T090452Z |
| L2 | s3-prefix | opal-data-mdpf code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz | safe-deploy --mint-bundle rc=0, new ETag/VersionId, four per-member sha metadata keys each equal to the repo file | bash .tools/safe-deploy.sh --mint-bundle investor_reporting rc=0 (the guard's own path, never a bare aws s3 cp): ETag c596538e9494b640e27de50720a14b52, 41844 bytes, VersionId DU0ppTu2Y1K_0GSNE2VTJXLCzUBnBnUG. FOUR OF FOUR per-member sha metadata keys re-derived from the repo files by a DIFFERENT instrument than the mint (hashlib over the four repo paths) and EQUAL: directory-runner, holdings-snapshot, ids, trading-calendar. source-repo-paths now names lib/trading_calendar.py | CLOSED 20260912T090453Z |
| L3 | verify | the host unpacks the re-minted bundle and the runner IMPORTS -- arm (d)'s import check printed in the command's own stdout | the SSM command id and its IMPORT-OK line | SSM command a83c5d88-2392-43f2-be55-c9845a0b1384 on i-02448edb624a7a7cf, dispatched by the DEPLOYED function, stdout verbatim: 'member trading_calendar.py' now present in the tar listing, then 'IMPORT-OK first-party modules resolved: trading_calendar, ids, contract' and "SOURCE_SETS ['49financial', 'cottonwood', 'inflection']" on python3 3.9.25 with boto3 1.42.97 / pandas 2.3.3 / pyarrow 21.0.0 / jsonschema 3.2.0. THE IMPORT CHECK PASSES ON THE HOST. The build then stops at the NEXT named missing repo file -- FileNotFoundError infra/aws/lambda-edge/_shared/firm-config.mjs -- which is recorded as a BLOCKING row, not chased further | CLOSED 20260912T090453Z |

## Log

- 20260912T085620Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 3 leg(s)
- 20260912T090452Z LEG L1 closed: 6e9ad7851e -- .tools/safe_deploy_core.py declares trading_calendar.py with repo_path lib/trading_calendar.py and sha_met
- 20260912T090453Z LEG L2 closed: bash .tools/safe-deploy.sh --mint-bundle investor_reporting rc=0 (the guard's own path, never a bare aws s3 cp): ETag c5
- 20260912T090453Z LEG L3 closed: SSM command a83c5d88-2392-43f2-be55-c9845a0b1384 on i-02448edb624a7a7cf, dispatched by the DEPLOYED function, stdout ver
- 20260912T090453Z CLOSED -- all 3 legs proven
