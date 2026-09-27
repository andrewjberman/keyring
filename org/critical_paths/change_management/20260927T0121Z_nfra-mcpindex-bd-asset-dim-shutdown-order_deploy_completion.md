# Deploy Completion Record
**Date opened:** 2026-09-27T01:21:55.933779+00:00
**Status:** OPEN
**Deploy:** opal-bd-asset-dim-download arms its shutdown BEFORE the non-zero exit, so a failing run reports Failed and still stops its runner (NFRA_MCPINDEX MX-s-4 step 2, on 2.0.0_SA_COO~O's Z-S17 ruling)
**Authored by:** 0.7.0_AE_CloudOps~I
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 72.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD: the shutdown moved above the failure branch | commit hash |  | OPEN |
| L2 | activation | SSM document opal-bd-asset-dim-download, new DocumentVersion via update-document | describe-document LatestVersion advances past 2 and Hash changes from 5130ead6f5b0f201739af7a6fc65cb67574f7de2e6f89fee9e5f18a67d442129 |  | OPEN |
| L3 | verify | the LIVE content at the version the trigger Lambda pins | get-document at $LATEST shows shutdown -h ABOVE exit 1, exactly one of each |  | OPEN |
| L4 | verify | one failing run that records Failed AND ends with the instance stopped | the scheduled Monday 22:10Z fire: SSM Status Failed plus i-0e6f6dc014fdcf1cd State stopped afterwards |  | OPEN |
| L5 | git | the ledger state committed | commit hash |  | OPEN |

## Log

- 20260927T012155Z OPENED by 0.7.0_AE_CloudOps~I with 5 leg(s)

## Blast radius and rollback per key (NEVER-2)

**WRITE SET -- one object.** SSM document `opal-bd-asset-dim-download`.
PRE-ACT: DefaultVersion 2, LatestVersion 2, Hash
`5130ead6f5b0f201739af7a6fc65cb67574f7de2e6f89fee9e5f18a67d442129`. Versions 1 and 2 are retained.

**ROLLBACK, and it is the same non-obvious one as the prior entry:** the trigger Lambda calls
send_command with `DocumentVersion='$LATEST'`, NOT the default, so a default-version flip rolls back
NOTHING. Rollback = `update-document` again with the v2 content
(`git show 03e744ec3f^:infra/aws/ssm/opal-bd-asset-dim-download.json`), creating a v4 that restores it.
Read out of the producer's code, not predicted from the API.

**NO INSTANCE INTERACTION, which is the constraint the ruling placed on this act.** `update-document`
creates a document version. It does not start, stop, or send anything to `i-0e6f6dc014fdcf1cd`, which
is running and whose stop remains Andrew's. Nothing here touches it.

**NOT TOUCHED:** the EventBridge rule (Monday 22:10Z stays the acceptance and is L4's evidence
source); allocation, realized, transaction, unrealized -- all carrying the identical
exit-before-shutdown order, all routed as queued repair items by the ruling, none edited; fees.

**EXPECTED, BOTH BRANCHES.**
  - PASS: Monday's scheduled fire records SSM **Failed** (the login is still broken; that is expected
    and is not what this act repairs) AND `i-0e6f6dc014fdcf1cd` reads **stopped** afterwards. Both, or
    the reorder did not work.
  - STOP: if the run records Failed but the instance is still up, the reorder is wrong and this entry
    rolls back to v2 rather than being argued with.

**NO NEW VENDOR CALL.** L4's evidence comes from the schedule that fires anyway. Andrew's word covered
ONE ad-hoc run and that run is spent; this act does not seek a second.
