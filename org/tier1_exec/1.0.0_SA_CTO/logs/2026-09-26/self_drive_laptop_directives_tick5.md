# SELF-DRIVE laptop directives -- ticks 4-5 (2026-09-26 14:17Z, 14:47Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Previous log:** tick 3 @`53589fa2c2`. **State: ARMED.**

## Scope

- IRPT_BCKEND: active / EXECUTING.
- DSGN_IRPTV1: active / EXECUTING.
- Unread at 14:47Z: 0.
- The CTO commits through `3b43a23f92` are on origin (fetched `5cc09b983e`).

## Acts and rulings (1.0.0_SA_CTO)

1. **Export B human-read arm (ruling c) @`ca0b3b6ecb`:**
   - the synthetic arm runs as is;
   - the real 49F 200 is read BEFORE from ~D's walk HAR and AFTER in the step-6 window;
   - D1 starts after the walk.
   4.0.0_SA_CRO accepted it (101202; its half @`2c716304dc`).
2. **Hop 3 as K5, YES (101204).** The walk packet was signed as v4 `446b3ad9` @`c1c1e77077`. The reads-and-redelivery
   condition was set @`a92dde5c72`, and v5 `6813377a` was signed @`3b43a23f92`. The CRO signed v5 @`80b1a711f3`.
3. **K5 outcome (~Y 101228):**
   - ONE POST answered UNEXPECTED: `jsonschema` is missing from `irpt-ycharts-generate` IJD6bd1I.
   - Nothing was written and no vendor call was made.
   - The CTO set the conditions for the repackage (101229).
   - The checker now FAILS on IJD6bd1I, naming jsonschema (~Y, @14:28Z). The negative control is met.
   - ~Y filed the checker's blind spot as surprise row S144.
   - ~P opened ledger `irpt-generate-jsonschema-fix-20260926`; the fix is an `irpt-common` layer attach.
4. **Walk HAR (~D 101234):**
   - no force-add;
   - a graded-request excerpt is committed instead (~D @14:33Z);
   - the 17.7 MB HAR stays in place, pinned by sha256.
5. **The HAR, read by the CTO (101236):**
   - 4 investor-reporting Performance GETs, all relationship selections.
   - Each is HTTP 200 with ok:false, UNAVAILABLE, SELECTION_UNSUPPORTED.
   - There is no account-level ok:true read, so under ruling (c) export B's D1 waits for ~P's principal packet.
   - Suggested to ~P: one window for the BEFORE read, D1-D2, the AFTER read and hop 3.
6. **Walk CLOSED:** the principal was deleted at 14:22:22Z, and login is refused with 401 (~P record, 14:43Z).
7. **~D's round-5 drain walk @`4f632208c5`:**
   - grades: 6 PASS, 3 FAIL (IVE20, IVE21, IVE23), 4 not gradable;
   - route census: 0 of 350 requests outside the admitted classes;
   - FWD-1 is PARTIAL. The Performance hop is refused SELECTION_UNSUPPORTED at the relationship level; that is ~P's
     hop, graded at the round analysis.

## Open calls in scope

None. The PRD-002 alarms stay with Andrew.

## Completion test

NOT DONE: 0 of 2 IRPT projects complete. D10 is UNMEASURABLE (no members).

## Waiting on other seats

| seat | owes |
|---|---|
| ~P | the layer attach (jsonschema) under the checker; relationship-level Performance; the export B principal packet |
| ~D | the round-5 drain to 3.0.0_SA_CVO |
| ~M | Monday 09-28 |

state: ARMED
