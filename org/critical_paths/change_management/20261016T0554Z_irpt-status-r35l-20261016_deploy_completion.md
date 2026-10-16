# Deploy Completion Record
**Date opened:** 2026-10-16T05:54:23.480165+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T062808Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R35L (AR-g-117): irpt-status code CodeSha256 OOez8YSm... -> +TcZDWmwE7uv3sUwos2+jn1lbKyQikK+13nNBzD6q4A= (pin 90b69dcb12, 3 of 49 members: durable_job.py owned_status.py status.py; the closed failure code and its words): BUILD_ONLY digest check, one upload, scoped plan 0/1/0, safe-apply, V reads; COO half blob 3092cf2a13, CTO half msg 9106
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U | s3-prefix | investor-reporting/irpt-status.zip one new object version, sha256 f937190d... | the build digest +TcZDWmwE... equal then the object read-back and VersionId | BUILD_ONLY digest +TcZDWmwE7uv3sUwos2+jn1lbKyQikK+13nNBzD6q4A= equal; one upload, new latest VersionId vP3Bt0tM_n0qEa17Nf_VA0ZtXjwMt4GX (368309 bytes), read back sha256 f937190d69b013bbafdec530a2cdbe8e7d656cac908a42bed779cd0730faab80; prior latest LRVpkveSkjFQiKnK0XYAcutUlBEjSMuc kept as rollback source | CLOSED 20261016T062807Z |
| C | verify | scoped plan 0 add 1 change 0 destroy (last_modified, s3_object_version, source_code_hash only) then safe-apply | the plan line and the apply line | scoped plan Plan: 0 to add, 1 to change, 0 to destroy (last_modified, s3_object_version, source_code_hash only; s3_object_version LRVpkve... -> vP3Bt0t...); safe-apply rc=0 Apply complete! Resources: 0 added, 1 changed, 0 destroyed; targeted re-plan No changes | CLOSED 20261016T062807Z |
| V | verify | V: G1 CodeSha256, G2 delta exactly 3 of 49, G3 refusal envelope equal, G4 READY report read byte-identical, G5 census 0 | the printed reads | G1 live CodeSha256 +TcZDWmw... equal; G2 49 of 49 compared, exactly durable_job.py owned_status.py status.py differ; G3 credential-less refusal envelope status 401 body sha256 6b4f44c2... equal; G4 READY report REQ-5e4149d2863aea31cc87d660 read without ticket_id status 200 body sha256 a67e9f25... byte-identical; G5 release-census changed_members=0 | CLOSED 20261016T062807Z |
| irpt-status | tf-lambda | module.irpt_status.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | TF apply 0 added 1 changed 0 destroyed; targeted re-plan No changes; deployed CodeSha256 +TcZDWmwE7uv3sUwos2+jn1lbKyQikK+13nNBzD6q4A= equals uploaded zip sha256 f937190d... (CodeSha256 of the build); served reads G3 G4 equal; map record 126965dde2 and df16fbc28a on branch wk-aq2-r35l-map | CLOSED 20261016T062808Z |

## Log

- 20261016T055423Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 4 leg(s)
- 20261016T062807Z LEG U closed: BUILD_ONLY digest +TcZDWmwE7uv3sUwos2+jn1lbKyQikK+13nNBzD6q4A= equal; one upload, new latest VersionId vP3Bt0tM_n0qEa17N
- 20261016T062807Z LEG C closed: scoped plan Plan: 0 to add, 1 to change, 0 to destroy (last_modified, s3_object_version, source_code_hash only; s3_objec
- 20261016T062807Z LEG V closed: G1 live CodeSha256 +TcZDWmw... equal; G2 49 of 49 compared, exactly durable_job.py owned_status.py status.py differ; G3 
- 20261016T062808Z LEG irpt-status closed: TF apply 0 added 1 changed 0 destroyed; targeted re-plan No changes; deployed CodeSha256 +TcZDWmwE7uv3sUwos2+jn1lbKyQikK
- 20261016T062808Z CLOSED -- all 4 legs proven
