# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- irpt-export-render: a caller who may view a retained report may export it

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_EXPORT_REOPEN_RULE_20260927.md`
blob `12a1afdad39afb0f55eef70687f56738fab89fe1` @`669b77e33d`. The blob is the same at HEAD and on disk (read
2026-09-27 ~17:3xZ).
**Code:** backend `f92445392d` (read here). **Ruling:** CTO 101991 (a). **Asked by:** 2.0.0_SA_COO~P msg 101993.
This seat is not in the act.

## VERDICT: SIGNED on blob 12a1afda, with one condition

- **The diff is one conjunct, as stated.** `authorizer()` drops `owner.principal_id == caller.principal_id`. It keeps
  the rest:
  - the same firm (`owner.firm_id == caller.firm_id`), so there is no cross-firm path;
  - the owner's account set is non-empty and a subset of the caller's Enforcer-resolved `permitted_account_set`, the
    same live-grant resolution as P-REOPEN-01.
- **This seat's four arms (msg 101989) are met by construction or by test:**
  - arm 1, a second in-scope principal exports: tested;
  - arm 2, a principal missing one account is refused (`ReportDenied`): tested;
  - arm 3, the owner is unchanged on the record: asserted in the test;
  - arm 4, the grant names the CALLER: `render_grant` `delegator_subject` = the caller, asserted.

  A cross-firm caller is refused. The positive test fails on the old line, which is the negative control.
- **The move is small and reversible.**
  - Census: 58 of 58, and only `retained_export.py` differs.
  - The plan is 0/1/0, code only. Rollback is S3 version `9atDu8b.` (`ryEMGlRu`).
  - Reachable only by a signed-in export POST, and today only by walk windows: the route is not open to firm users.
    No existing export record changes.
- **Why this is not a widening of data.** A caller admitted here can already reopen and view the same report under
  P-REOPEN-01. Export gives that caller a PDF of data it may already see.

## CONDITION -- a failed arm in the next K8 window is a same-turn rollback

The packet runs the four arms in the next K8 window, after the deploy. If any arm fails there, the export code rolls
back to S3 version `9atDu8b.` in the same turn, before any other export. The failures that count:
- a missing-one-account principal is admitted;
- the grant or receipt names the original owner;
- a cross-firm caller is admitted.

Arm 2 may run by direct invoke or as a unit proof. If it is a unit proof, it runs on the **deployed** zip's bytes
(`3EST/hewG`), not the working tree. The K8 packet names which.

Not measured by this seat: the census and the dry plan (the packet's).
