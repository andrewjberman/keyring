# Deploy Completion Record
**Date opened:** 2026-09-27T20:25:20.418123+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T204017Z
**Deploy:** S157 COT use AGAIN on the refreshed session (AWSCURRENT 9da4e781): plan 4 b20d69b2 (acc_81d92b2b.., 01-01..09-21, stated departure), direct IAM invoke as V1; arm 1/1/0 (no code move), ONE read (= 2 BD requests), reopen, disarm to null same tick; halves pending
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | arm plan 4 | both halves at HEAD naming the packet blob; live re-plan 1/1/0 equal to the dry plan; safe-apply; readback env plan sha b20d69b2 + egress digest; code sha unchanged bOefL9nx | Both halves at HEAD naming blob 049ea241 (@95f271b30a): CTO @c07a035190 102083 (live re-plan = dry key for key; AWSCURRENT printed at arm; a second BDRequestFailed is a finding, not a refresh), CRO @342bf8baca 102084. AWSCURRENT at arm (20:32:14Z read): 9da4e781-7f11-4cf0-b2dd-2980e56db1db, created 1790534547.771 = 2026-09-27T18:42:27.771Z. Live re-plan (plan4 tfvars) vs dry s157r_arm.tfplan: KEY-FOR-KEY EQUAL (addresses, actions, env map, policy) = 1 add performance_approved_session[0] / 1 change adapter env. safe-apply 20:33:45Z -> 20:35:04Z: 1 added, 1 changed, 0 destroyed. Readback: CodeSha bOefL9nx (unchanged; no code move), env plan sha b20d69b2f3e3, egress digest b20d69b2f3e3. | CLOSED 20260927T204017Z |
| R1 | verify | ONE read + ONE reopen | READY/PARTIAL with a retained report whose actual_start is the first series point, or a named refusal; exactly 2 BD requests in the claim's provider evidence; COT REPORT# +1 at most; reopen = same report, 0 vendor calls | ONE read 20:35:28Z (COT_S157R_READ_20260927.json): PARTIAL/PERFORMANCE_PARTIAL, retained RPT-12b885b84f7badf270d3969c106f7542 rev 65fc347a.., requested 01-01..09-21, ACTUAL 2026-07-21..2026-09-21, 44 series points, series first 07-21 = actual_start (S157-4 PASS on real data; not 01-02). Claim PERFORMANCE_USE#b20d69b2.. claimed_at 1790541333 (20:35:33Z). Provider evidence ART-448c25af.. (sha 3e465fa8, version myVzOncF): requests = performancePeriod + performanceSeries = EXACTLY 2 BD requests. cottonwood REPORT# 2 -> 3 (+1). Owner = V1 (reopen-arm-1@opal.test). ONE reopen 20:36:14Z (COT_S157R_REOPEN_20260927.json): the same report (sha 65fc347a), PARTIAL, no new claim. FINDING: the claim row's approval_ref reads the plan builder's DEFAULT ("Andrew-direct 02:5xZ yes to all three -- call 3"), a spent word, not this use's authority (both halves on 049ea241 under CTO 102044 / MSTR 101850 as scoped by CTO 101854); the row is immutable, the builder was run without --approval-ref; recorded as a surprise row. | CLOSED 20260927T204017Z |
| D1 | activation | disarm to null | approved_performance_plan = null; re-plan 0/1/1; readback env null; policy gone; replan 0 | Disarm plan (null-plan tfvars) 0 add / 1 change / 1 destroy (performance_approved_session[0] destroyed, env keys removed); safe-apply done 20:38:19Z (0 added, 1 changed, 1 destroyed). Readback: CodeSha bOefL9nx, IRPT_PERFORMANCE_APPROVED_PLAN null, IRPT_PERF_VENDOR_EGRESS_AUTHORIZED null; role inline policies matching approved-session: 0. Re-plan with null: detailed-exitcode 0 (no changes). Armed interval 20:35:04Z -> 20:38:19Z. | CLOSED 20260927T204017Z |

## Log

- 20260927T202520Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260927T204017Z LEG A1 closed: Both halves at HEAD naming blob 049ea241 (@95f271b30a): CTO @c07a035190 102083 (live re-plan = dry key for key; AWSCURRE
- 20260927T204017Z LEG R1 closed: ONE read 20:35:28Z (COT_S157R_READ_20260927.json): PARTIAL/PERFORMANCE_PARTIAL, retained RPT-12b885b84f7badf270d3969c106
- 20260927T204017Z LEG D1 closed: Disarm plan (null-plan tfvars) 0 add / 1 change / 1 destroy (performance_approved_session[0] destroyed, env keys removed
- 20260927T204017Z CLOSED -- all 3 legs proven
