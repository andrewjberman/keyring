# Deploy Completion Record
**Date opened:** 2026-09-18T15:01:56.000398+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260918T160657Z
**Deploy:** IB-rtd-5: targeted apply of aws_s3_object.mdpf_route_bindings to committed content (S68)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~3
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | targeted terraform apply of aws_s3_object.mdpf_route_bindings sourced from committed LF bytes sha256 98f5e9c5 | VersionId before iR4vgE0NJdkuQyNkO6AsYjlBmDaqBLBz after TBD | targeted apply RC=0: VersionId iR4vgE0NJdkuQyNkO6AsYjlBmDaqBLBz -> WXkE2epIOTpxH8OJap.2h35dhJkd1whq; head-object content-sha256=98f5e9c51d016d5283562e525b53088292576d86752c6cf0449865fbf328d923 ETag=650f893a7b9594404ce1d6f067b5b078 ContentLength=13516; targeted plan named ONLY aws_s3_object.mdpf_route_bindings (Plan: 0 to add, 1 to change, 0 to destroy) | CLOSED 20260918T160432Z |
| L2 | verify | post-apply head-object content-sha256 + untargeted root plan 0/0/0 + 4 of 4 consumer reads | TBD | post-apply head-object content-sha256=98f5e9c5... MATCH; untargeted root plan (LF-materialized source): 0 resource actions (no Plan: line; only Changes to Outputs: mdpf_route_bindings_sha256 stale-in-state from -target, no real infra change per terraform's own text); consumers 4 of 4: mdpf-gold-lambda packaged copy sha256=98f5e9c5 MATCH LOADS OK; build_mdpf_spine.load_bindings() LOADS OK; route_bindings_tieout.py 34 of 34 TIE / 0 FAIL; mdpf-daily-runner EC2 synced config (opal-data-mdpf/code/config/, different bucket) ETag=650f893a LOADS OK not-applicable-different-artifact; rollback rehearsed: head-object --version-id iR4vgE0NJdkuQyNkO6AsYjlBmDaqBLBz RC=0 retrievable | CLOSED 20260918T160557Z |

## Log

- 20260918T150156Z OPENED by 0.9.0_WK_IRPT_BCKEND~3 with 2 leg(s)
- 20260918T160432Z LEG L1 closed: targeted apply RC=0: VersionId iR4vgE0NJdkuQyNkO6AsYjlBmDaqBLBz -> WXkE2epIOTpxH8OJap.2h35dhJkd1whq; head-object content
- 20260918T160557Z LEG L2 closed: post-apply head-object content-sha256=98f5e9c5... MATCH; untargeted root plan (LF-materialized source): 0 resource actio
- 20260918T160657Z CLOSED -- all 2 legs proven
