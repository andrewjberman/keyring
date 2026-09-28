# Deploy Completion Record
**Date opened:** 2026-09-28T20:32:56.553266+00:00
**Status:** OPEN
**Deploy:** MX-s-10 PHASE B (TO MX-s-12): publish infra/aws/ssm/opal-bd-asset-dim-download.json @0ff972bc38 as DEFAULT of SSM doc opal-bd-asset-dim-download; retire the fees schedule leg (bd-fees-pipeline-trigger, bd-fees-trigger) + two Playwright scripts through Terraform; acceptance = the 22:10Z scheduled weekday fire (G2 disclosure). Halves: CTO RULING_MX-s-10_NEVER_WIDEN_CTO_HALF_20260928.md, CVO cvoO_NFRA_MCPINDEX_MX-s-10_NEVER_WIDEN_SECOND_HALF_20260928.md
**Authored by:** 0.9.0_WK_NFRA_MCPINDEX~8
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | G1 rollback targets read live: prior SSM DefaultVersion, served dim VersionId, id count, non-null cusip count, id-set sha256 | values printed from live aws describe-document and list-object-versions, never typed |  | OPEN |
| L2 | activation | SSM doc opal-bd-asset-dim-download published from repo file byte-equal to 0ff972bc38 and set DEFAULT | get-document DEFAULT content equals file as parsed JSON; carries rc 92 refusal and --union-bronze; AC1 PASS |  | OPEN |
| L3 | activation | Terraform retire fees leg (bd-fees-pipeline-trigger rule+target+permission, bd-fees-trigger lambda) via safe-apply; delete two ts scripts and EC2_MANIFEST _ts_source entry | G3 plan graded (only fees-leg destroys); apply result; plan -detailed-exitcode 0; AC2 PASS |  | OPEN |
| L4 | verify | G2 at the scheduled 22:10Z fire: builder DELTA block, ids before/after/added/removed, cusip non-null before/after, per-column changed counts | AC3 PASS + run log excerpt; rollback to the G1 VersionId if ids fall or any cusip non-null->null |  | OPEN |
| L5 | git | retirement and ledger committed on the worker branch (LOCAL, not pushed) | commit hashes |  | OPEN |

## Log

- 20260928T203256Z OPENED by 0.9.0_WK_NFRA_MCPINDEX~8 with 5 leg(s)
