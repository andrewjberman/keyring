# Deploy Completion Record
**Date opened:** 2026-09-21T23:22:02.803177+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260921T232454Z
**Deploy:** IRPT_BCKEND IB-rti-1: publish repaired capture-session.cjs/.sh to render host artifact prefix (host stopped, no on-host verify)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~9
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/investor-reporting-export/ capture-session.cjs + capture-session.sh | S3 readback sha256 == packet blobs (cjs 5b26be91, sh 17ae44f0) | S3 readback sha256 cjs 5b26be9133ae468ddb55af4e34be860f7f2d7338dea496bfd71f0c43f5a01d23 (VersionId JN6.A7WDgUx_I.__uUTu_FIRi8vUemPs), sh 17ae44f0d6ee0a2f30225a99446f74c33fb82ce893026bb9852d211581ef89e0 (VersionId Z3NJuuiIxczhtYxGEsXW8ZqBpqYi1gs7) == packet blobs; host stopped, NO on-host verification | CLOSED 20260921T232454Z |

## Log

- 20260921T232202Z OPENED by 0.9.0_WK_IRPT_BCKEND~9 with 1 leg(s)
- 20260921T232454Z LEG L1 closed: S3 readback sha256 cjs 5b26be9133ae468ddb55af4e34be860f7f2d7338dea496bfd71f0c43f5a01d23 (VersionId JN6.A7WDgUx_I.__uUTu_
- 20260921T232454Z CLOSED -- all 1 legs proven
