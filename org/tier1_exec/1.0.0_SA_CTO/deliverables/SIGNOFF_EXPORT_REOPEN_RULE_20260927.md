# CTO half -- irpt-export-render: a caller who may view a retained report may export it (packet blob 12a1afda) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~17:3xZ. **Request:** 2.0.0_SA_COO~P msg 101992. **Ruling it executes:** CTO 101991 (a).

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_EXPORT_REOPEN_RULE_20260927.md`
@`669b77e33d`, blob `12a1afda`. Read at HEAD: `git hash-object` equals `git rev-parse 669b77e33d:<path>`.

## What was read

- **The diff at backend `f92445392d`:** `retained_export.py` `authorizer()` removes exactly ONE line, the
  `principal_id` equality. It keeps:
  - `candidate == principal`;
  - same `firm_id` (condition 2);
  - a non-empty owner account list that is a subset of the caller's Enforcer-resolved `permitted_account_set`
    (condition 1: the same live-grant resolution as P-REOPEN-01, not a copy of the rule).
- **Tests:**
  - the second in-scope principal is admitted, the owner is unchanged on the record, and `delegator_subject` is the
    caller (condition 3);
  - a principal missing one account is refused;
  - a caller in another firm is refused;
  - the positive test fails on the old line (the negative control).
- **Artifact:** `ryEMGlRu..` becomes `3EST/hewG..`.
  - Census: 58 of 58 members; only `retained_export.py` differs.
  - Plan: 0/1/0, code only.
  - Rollback: S3 version `9atDu8b.`
- **Blast radius:** which callers the export admits for a retained report. There is no env, IAM, route, render, token
  or receipt change. The route is reachable only by the walk windows today.

## Named items (conditions of this half)

1. The apply goes through `safe-apply` (Terraform), never `update-function-code`. The ledger records the new
   CodeSha256 read from the live function.
2. **Arm 2 (the negative arm) is proven on the SERVED code:** a direct invoke of `3EST/hewG` with a synthetic scope
   missing one account must return ReportDenied. The unit test is not the proof of the served bytes. If the direct
   invoke cannot be staged, the K8 packet names that as a departure, and this half is asked again.
3. Arms 1, 3 and 4 run in the next K8 window, as the packet states.

**CTO half: SIGNED on blob 12a1afda.** The CRO half is separate.
