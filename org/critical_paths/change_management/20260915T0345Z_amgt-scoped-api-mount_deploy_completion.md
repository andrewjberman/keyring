# Deploy Completion Record
**Date opened:** 2026-09-15T03:45:34.477736+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-ri-4: THE MOUNT, DEPLOYED -- the scoped AMGT read API (function, IAM, integration, 11 CUSTOM-auth routes on shared portal api 7k3ed8px20) exists on the live plane
**Authored by:** 0.9.0_WK_AMGT_RESAPP~17
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | wk-amgt_resapp-10-2 branch commits (ri-2 builder a9cea42d5d already on branch; this ledger entry and its sentinel) | commit hash on the worker branch |  | OPEN |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip (the yang-lambda source_code_hash input, read at PLAN time) | head-object Meta.content-sha256 EQUAL to the locally computed sha256 b64, non-zero Size |  | OPEN |
| L3 | activation | terraform apply of .scratch/ri4.tfplan into harvest/tfstate (19 to add, 0 to change, 0 to destroy; the co-signed add-set) | Apply complete! line with 19 added, 0 changed, 0 destroyed |  | OPEN |
| L4 | verify | live route set of api 7k3ed8px20 and live config of function opal-amgt-scoped-api | before-subset-of-after True with lost [], after EQUAL to before plus 11, amgt-after 11, and function State Active python3.11 29 512 |  | OPEN |
| L5 | verify | direct invoke of the deployed adapter with a synthetic HTTP API v2 event, both firm-header branches | x-firm-id present -> statusCode 200 with row_count and a CROSSED resolution record; header absent -> statusCode 401 (boundary fails CLOSED), no FunctionError on either |  | OPEN |

## Log

- 20260915T034534Z OPENED by 0.9.0_WK_AMGT_RESAPP~17 with 5 leg(s)
