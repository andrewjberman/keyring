# Deploy Completion Record
**Date opened:** 2026-09-18T15:01:56.000398+00:00
**Status:** OPEN
**Deploy:** IB-rtd-5: targeted apply of aws_s3_object.mdpf_route_bindings to committed content (S68)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | targeted terraform apply of aws_s3_object.mdpf_route_bindings sourced from committed LF bytes sha256 98f5e9c5 | VersionId before iR4vgE0NJdkuQyNkO6AsYjlBmDaqBLBz after TBD |  | OPEN |
| L2 | verify | post-apply head-object content-sha256 + untargeted root plan 0/0/0 + 4 of 4 consumer reads | TBD |  | OPEN |

## Log

- 20260918T150156Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 2 leg(s)
