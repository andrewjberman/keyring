# Deploy Completion Record
**Date opened:** 2026-10-09T22:16:09.865799+00:00
**Status:** OPEN
**Deploy:** MDPF_CANON CN-b-3 + CN-b-4: the publisher to python3.11 + pandas-pyarrow-requests-layer with one DELTA=0 ad-hoc run, and the composite grant re-pointed to builder output (no-op plan)
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | CN-b-4: the targeted plan on aws_iam_role_policy.mdpf_gold_writers in infra/aws/terraform/mdpf-pipeline, which must show the rendered policy UNCHANGED and is never applied otherwise | C2: 'No changes', or a change whose rendered policy JSON is byte-identical before and after -- compared as parsed JSON, not as a diff of the HCL |  | OPEN |
| L3 | verify | the publisher's live configuration after the apply | C3: Runtime python3.11, Layers naming pandas-pyarrow-requests-layer, and GOLD_BUCKET / GOLD_ROOT / SERVE_BUCKET / SERVE_ROOT each byte-equal to its pre-apply value |  | OPEN |
| L4 | activation | the ONE ad-hoc invocation of opal-assets-mdpf-portal-publisher, in the event shape its own scheduler sends | C4: StatusCode 200, no FunctionError, a response naming the leaves it served |  | OPEN |
| L5 | verify | the BEFORE/AFTER comparison of every served leaf under opal-data-portal-v2 platinum/mdpf/{scope}/ | C5: DELTA=0 on every data-bearing value with the leaf denominator printed (only _provenance.written_at and _manifests/ may differ), or the same-session rollback recorded and its re-read matching BEFORE |  | OPEN |
| opal-assets-mdpf-portal-publisher | tf-lambda | opal-assets-mdpf-portal-publisher | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T221609Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 5 leg(s)
