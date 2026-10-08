# Deploy Completion Record
**Date opened:** 2026-10-08T18:13:20.373801+00:00
**Status:** OPEN
**Deploy:** IRPT_YCDGEN F1 svc principal: resident st24 -> st25 (allow list adds svc-irpt-analysis), one seat-driven F1 run, then the removal release st25 -> st24
**Authored by:** 2.0.0_SA_COO~G2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | verify | st25 tar + install script staged in S3, read back by version | sha256 equal | tar irpt-resident-3cf5d52a7b-st25.tar.gz v Hwc58HnvsK34Ik4nWiLfUTPk4wj_blNO sha256 57e70cc96970f6c8...; install script v lrMO.Fq4usTTy.vsB67UKPvE4MU.Tlos sha256 86fe9deee41cbf88...; both keys 404 before, read back by version equal (staged ~18:1xZ before the ledger opened, as st24 did); gate PASS G1 267/267 G2 265/265 + added 1/1 G3 111/111 G4 0 unserved G5 vs st24 changed 2 (resident_worker.py, resident_bindings.json) identical 265 | CLOSED 20261008T181334Z |
| P1 | verify | host pre-read (root st24, allow list, queue 0/0) | recorded |  | OPEN |
| D2 | activation | install_st25.sh via SSM | root 3cf5d52a7b-st25 active, rc=0 |  | OPEN |
| V1 | verify | running allow list carries svc; producer_for svc=OPAL; queue 0/0; no traceback | read from the running root |  | OPEN |
| F1 | verify | one seat-driven F1 run as svc-irpt-analysis through the portal route (ruling d54e0b7515) | run record, zero YCharts calls measured |  | OPEN |
| X1 | activation | remove_st25_to_st24.sh via SSM (the removal release) | root 409e3066d1-st24 active, rc=0 |  | OPEN |
| V2 | verify | running allow list is andrew only; queue 0/0; no traceback | read from the running root |  | OPEN |

## Log

- 20261008T181320Z OPENED by 2.0.0_SA_COO~G2 with 7 leg(s)
- 20261008T181334Z LEG U2 closed: tar irpt-resident-3cf5d52a7b-st25.tar.gz v Hwc58HnvsK34Ik4nWiLfUTPk4wj_blNO sha256 57e70cc96970f6c8...; install script v
- 20261008T1816Z NOTE halves: COO half SIGNED (f1_svc_release/NEVER_WIDEN_PACKET_F1_SVC_PRINCIPAL.md @f04b0c498a); CTO half GIVEN by 1.0.0_SA_CTO~DELL2 @c5a94ae065 (msg 1384): X1 in the SAME session as D2 whatever F1's result (no install if X1 cannot follow); only F1 uses svc in the window; window times in this ledger.
- 20261008T1822Z NOTE HOLD before D2 (CTO~DELL2 msg 1391; MSTR~DELL2 msg 1389): dell2 SendCommand(AWS-RunShellScript) explicit deny (item 5, NFRA_CTLPLN cell 1) not applied, target ~20:0xZ; the laptop does not run host scripts. Nothing moved on the host. The tool refuses HELD while D2/X1 are open (nothing landed).
- 20261008T1824Z NOTE secret window (laptop 1.0.0_SA_CTO 107091 via MSTR 1394; CTO~DELL2 1398): cloudops-dell2-agent-user joins the Allow and the Deny exception on irpt/svc-irpt-analysis/password from D2 to X1 only. Conditions: (1) the restore read back by simulation and logged here before X1 closes; (2) the first read reported under rule 2; (3) the Dell cannot write that policy (simulate PutResourcePolicy implicitDeny, 18:2xZ), so 2.0.0_SA_COO~C cuts ADD (after V1) and REMOVE (at X1) to the laptop's 0.7.0_AE_CloudOps on this ledger's timing.
