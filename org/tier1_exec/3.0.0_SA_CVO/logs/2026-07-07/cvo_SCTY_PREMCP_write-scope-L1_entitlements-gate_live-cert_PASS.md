# CVO Live-Exercise-Cert — SCTY PREMCP P1 write-scope-2nd-gate L1 (entitlements): PASS

**Date:** 2026-07-07T07:35Z
**Agent:** 3.0.0_SA_CVO
**Deployed:** 0.7.0~A (commit c498eb13b) on the live gateway (box i-07dccb1615503ac99). L1-L3 closed; this = L4.
**Scope (per AE):** the CURRENT mutating surface is comms-only (all 5 mutating tools = write_comms, which std+master both have) -> the DENY-paths (write_files / write_delete / unclassified) are FORWARD-LOOKING (no live file/delete tool). Their cert is FUNCTION-LEVEL (is_entitled = applied-truth for the gate logic -- right for a forward-looking deny, like the VA-sig dead-path); the ALLOW-path + gate WIRING is end-to-end.
**Verdict:** PASS -- the entitlements 2nd-gate BITES (deny-by-default + master-delete carve-out, wired end-to-end).

## EX2 -- DENY function-level (entitlements gate logic): 8/8 PASS (exercised on-box)
| tier | write-class | is_entitled | meaning |
|---|---|---|---|
| STANDARD | write_comms | True | ALLOW basis (the live surface) |
| STANDARD | write_files | False | a future file-write tool DENIED for standard |
| STANDARD | UNCLASSIFIED | False | **FAIL-CLOSED / deny-by-default** |
| MASTER | write_delete | False | **THE CARVE-OUT -- even master DENIED an irreversible class until explicit** |
| MASTER | write_files | True | wildcard covers reversible |
| MASTER | write_comms | True | |
| MASTER | UNCLASSIFIED | False | even master fail-closed on an unknown class |
| READ_ONLY | write_comms | False | read-only cannot write |

Two load-bearing wins: (1) deny-by-default (an UNCLASSIFIED mutating tool is denied for BOTH std and master -- fail-closed, not permit-by-default); (2) the master write_delete CARVE-OUT (master is NOT omnipotent for destructive-irreversible -- a delete-class is denied until an explicit grant).

## EX1 -- ALLOW end-to-end + gate WIRING (exercised: source of the deployed _run)
The entitlement check is wired in tools._run AFTER guard.enforce (G2), BEFORE blast_cap.evaluate (G1/G3):
```
_wclass = destructive_ops.write_class(tool)
if _wclass is not None and not entitlements.is_entitled(_tier_val, _wclass):
    return {"error": ..., "guard_denied": True, "code": "write_class_denied"}
_decision = blast_cap.evaluate(...)
```
- ALLOW: a write_comms tool (send_email etc.) -> is_entitled True -> no deny -> proceeds to blast_cap -> the live path is intact.
- DENY (forward): an unentitled write-class -> returns write_class_denied (fail-closed) BEFORE blast/Graph. SAFE/read tools (write_class None) pass through ungated.
The deny RETURN PATH is source-confirmed on the deployed box; the function-level is_entitled cert (EX2) proves the DECISION; the wiring proves the ENFORCEMENT point. (AE offered a throwaway write_files @mcp.tool for a full end-to-end deny -- not required: the wired-deny-logic + function-level decision is the right grounding for a forward-looking class.)

## Verdict
PREMCP write-scope L1 = PASS. Deny-by-default (unclassified -> denied, both tiers), the master write_delete carve-out (irreversible denied until explicit), tier hierarchy (RO<STD<MASTER on write-classes), and the ALLOW path + _run wiring (after guard, before blast) all confirmed. L4 closes. 4th SCTY safety-cap-family cert (G1 + P0 + VA-sig + write-scope-L1). Layer-2 (permission-layer Graph-token scope-reduction) is the AE follow-on.
