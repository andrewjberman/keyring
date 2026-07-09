# Deploy Completion Record
**Date opened:** 2026-06-26T14:12:36.142967+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260626T141757Z
**Deploy:** ADVI_COTETL.L4-GUARD v0.5.1 -- probe holdings + served-AUA data_as_of (Part-A.1 gap-close)
**Authored by:** 0.6.0_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit + tag cot-pipeline-v0.5.1 | hash + tag pushed | commit 952417807 (lambda+TF) + acbd28dc6 (artifact); tag cot-pipeline-v0.5.1 pushed (20e4efe10) | CLOSED 20260626T141756Z |
| L2 | s3-prefix | cot-pipeline/bd-cot-freshness-probe.zip re-uploaded | build-and-upload sha256 | bd-cot-freshness-probe.zip sha256=x+gw0tAmzXIFMFDrwUpi8D97roYYy0b17+zeca3HG/w= uploaded to opal-313476888478-lambda-artifacts/cot-pipeline/ | CLOSED 20260626T141756Z |
| L3 | activation | safe-apply: +holdings alarm + bd-cot-served-aua-stale + IAM GetObject platinum/firm/*; 0-diff | apply + 0-diff | safe-apply (HALT_ACK, HALTGT pass): 2 added (bd-cot-served-aua-stale + bd-cot-silver-stale-holdings) 2 changed (freshness IAM in-place + lambda) 0 destroyed; 0-diff replan = No changes | CLOSED 20260626T141756Z |
| L4 | verify | comp-iam gaps clean + Deny-bd belt still LIVE on freshness role | comp-iam output | comp-iam service: all ops GRANTED incl new s3:GetObject (served read); gaps=?? resource-precise tier only (no missing). DenyBdPlane survived in-place modify (get-role-policy confirms Deny + ReadServedAuaForFreshness both present) | CLOSED 20260626T141757Z |
| L5 | verify | EXERCISE: served-AUA alarm FIRES on live 06-22 freeze (lag>=2 from data_as_of CONTENT) + holdings-stale fires | alarm ALARM-state + probe return | EXERCISED LIVE: probe v0.5.1 emits holdings lag=3 + served_aua_lag=4 (data_as_of=06-22 read from CONTENT not mtime); bd-cot-served-aua-stale=ALARM + bd-cot-silver-stale-holdings=ALARM on the real freeze while the 4 gated tables=lag0 -> false-all-clear gap CLOSED | CLOSED 20260626T141757Z |

## Log

- 20260626T141236Z OPENED by 0.6.0_AE_PartnerETL with 5 leg(s)
- 20260626T141756Z LEG L1 closed: commit 952417807 (lambda+TF) + acbd28dc6 (artifact); tag cot-pipeline-v0.5.1 pushed (20e4efe10)
- 20260626T141756Z LEG L2 closed: bd-cot-freshness-probe.zip sha256=x+gw0tAmzXIFMFDrwUpi8D97roYYy0b17+zeca3HG/w= uploaded to opal-313476888478-lambda-arti
- 20260626T141756Z LEG L3 closed: safe-apply (HALT_ACK, HALTGT pass): 2 added (bd-cot-served-aua-stale + bd-cot-silver-stale-holdings) 2 changed (freshnes
- 20260626T141757Z LEG L4 closed: comp-iam service: all ops GRANTED incl new s3:GetObject (served read); gaps=?? resource-precise tier only (no missing). 
- 20260626T141757Z LEG L5 closed: EXERCISED LIVE: probe v0.5.1 emits holdings lag=3 + served_aua_lag=4 (data_as_of=06-22 read from CONTENT not mtime); bd-
- 20260626T141757Z CLOSED -- all 5 legs proven
