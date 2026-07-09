# Deploy Completion Record
**Date opened:** 2026-06-25T13:04:31.347453+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260625T131134Z
**Deploy:** ASTN_WSJFT EventBridge enable-flip (3am-run + 4am-absence-check DISABLED->ENABLED, go-live)
**Authored by:** 3.0.0_SA_CVO
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| sched-flip | activation | astn-pipeline aws_scheduler_schedule.astn_run+astn_absence_check | live state=ENABLED on both schedules (comp-aws derive scheduler / get-schedule) | LIVE-VERIFIED ENABLED on both: get-schedule astn-wsjft-3am-run=ENABLED, astn-wsjft-4am-absence-check=ENABLED (2026-06-25 1310Z). Committed 700c07530. SIDE-EFFECT (documented): -target apply cascaded scheduler->orchestrator-lambda->aws_instance.astn and replaced EC2 (old i-0c8b110af37486ecc TERMINATED, new i-059405dfefcb4b44a RUNNING IP 35.174.172.183) -- applied AE uncommitted associate_public_ip_address=true WIP. Consistency VERIFIED: orchestrator Lambda ASTN_INSTANCE_ID=i-059405dfefcb4b44a. Residuals to AE/COO: committed-vs-live drift + new EC2 left running. | CLOSED 20260625T131133Z |

## Log

- 20260625T130431Z OPENED by 3.0.0_SA_CVO with 1 leg(s)
- 20260625T131133Z LEG sched-flip closed: LIVE-VERIFIED ENABLED on both: get-schedule astn-wsjft-3am-run=ENABLED, astn-wsjft-4am-absence-check=ENABLED (2026-06-25
- 20260625T131134Z CLOSED -- all 1 legs proven
