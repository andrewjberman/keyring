# NFRA_REPORT.TO-RP-s-6 -- The ALERT-DELIVERY read -- alarm to topic to CONFIRMED subscriber

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP.md</decomp_doc>
<owned_cells>RP-s-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_REPORT~1</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-5; acceptance property 6)

```
RP-s-6 mirrors manifest row S6. ACT: for any alarm the estate relies on, make it readable whether a
message would actually ARRIVE AT A HUMAN BEING, before an incident tests it. One that would reach
nobody is shown as reaching nobody and is NEVER counted as protection.
MEASURED, LIVE, and already sufficient to satisfy FWD-5's bar in evidence terms the day this is built:
3 of 7 distinct alarm targets have ZERO confirmed subscribers -- opal-login-abuse-alerts,
astn-wsjft-alerts, etfs-reports-alerts -- POSITIVE-CONTROLLED by the 4 that do.
```

## DEPENDENCIES

This cell depends on: RP-s-1.
A dependency is keyed to OBSERVED COMPLETION -- a deliverable that exists and whose criteria passed -- never to a status word.

## BOUNDS -- what this cell may not cross

```
C-ALARM-ANCHORED: the check is anchored on the ALARM and reads CONFIRMED delivery. NEVER
"subscribed", and NEVER the alarm's own configuration. A PENDING subscription delivers nothing.
An alarm that cannot fire renders INERT on axis 1 -- ruling 12's own worked example is exactly
opal-login-abuse-alerts, which is INERT and never RED.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
THE STANDING ALERTING MORATORIUM IS ARMED (one of 12 NEVER clauses measured by comp-schedule).
This cell READS delivery state. It mints NO alarm, NO topic, NO subscription and NO notification.
Repairing an existing non-delivering topic is permitted; creating one is NOT.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_REPORT/deliverables/
org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP.md
org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md
org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-6.alert-delivery-read-alarm-anchored.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="RP-s-6"><invocation>grep -c -E 'opal-login-abuse-alerts|astn-wsjft-alerts|etfs-reports-alerts' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/ALERT_DELIVERY.md</invocation><expect>a count of 3 or greater</expect></criterion>
  <criterion id="AC2" cell_refs="RP-s-6"><invocation>grep -c -i 'confirmed' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/ALERT_DELIVERY.md</invocation><expect>a count of 1 or greater</expect></criterion>
  <criterion id="AC3" cell_refs="RP-s-6"><invocation>grep -c -i -E 'create-topic|subscribe --|put-metric-alarm' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/ALERT_DELIVERY.md</invocation><expect>a count of 0 -- any hit means an alarm or topic was minted and the moratorium was crossed</expect></criterion>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the deliverable names the three zero-subscriber targets
- **AC2** (mechanical): the read is anchored on confirmed delivery rather than subscription
- **AC3** (mechanical): no new alerting was minted -- the moratorium limb, proven by absence of a create verb

Every invocation runs under `timeout 120`. A timeout is recorded AS the output, so it does not fail loudly -- keep every invocation bounded.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>2</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

**Issuer:** `2.0.0_SA_COO~ZZ` (L6) · **Project:** NFRA_REPORT · **Directive:** D12 · **PRD:** v0.2 @1703e825d0
**Authority chain:** L1 `4.0.0_SA_CRO~Z` brief @37ff80867a -> L2/L3/L4 `1.0.0_SA_CTO~Z` -> L5 `2.0.0_SA_COO~ZZ` decomp @c34501140e -> L6 this issuance.
**Provenance:** the cell text mirrors PRD section 8 row S6; nothing in that manifest was re-measured at L4, so every `measured` claim carries the BRIEF's vintage @37ff80867a and this order's L5 battery re-grounds what it cites.
<preflight>
comp-schedule: RUN -- 5 of 5 carriers scanned; denominators C1=23 C2=7 C3=12 C4=20 C5=335; 2 gates ARMED, NEITHER this project's (G-3 CTO, G-7 POD4); C5's 137 non-null blocking fields are a READING LIST and are not counted as gates.
comp-iam: RUN -- 836 calls verdicted across 96 mapped roles over 31 services; 630 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED not CLEARED), 11 UNGRANTED, 266 calls in 26 role-UNMAPPED services NOT resource-checked; BLIND on wafv2 (coverage-unknown), the plane C-SENTINEL-STATE lives on.
comp-adversary: RUN -- 2 of 2 cited commits VERIFIED, 2 of 2 cited paths stable, 0 file:line cites; BLIND on the decomposition neighborhood (a DECOMP carries no decomp_ref) so it digested 12 of 13 filesystem siblings instead of the dependency chain, and its packet is therefore not evidence about these cells.
</preflight>

**Preflight disposition:** mandatory core RUN at L5 (comp-schedule C1=23/C2=7/C3=12/C4=20/C5=335; comp-iam 836 calls/96 roles/31 services; comp-adversary 2 of 2 commits VERIFIED with a declared neighborhood blindness). Non-core lenses DECLARED-NOT-APPLICABLE -- this cell touches no route, cache key, shared component or gold-pipeline I/O.
