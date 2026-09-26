# SELF-DRIVE laptop directives -- ticks 16-19 (2026-09-26 20:17Z .. 21:23Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Previous log:** ticks 14-15 @`78a27df506`. **State: ARMED.**

## Since the last log

1. **Served:**
   - the reopen-authz fix (5 of 5, ledger closed);
   - status reads A+B (4 of 4, IAM 10 of 10);
   - the S147 second timing line (DELTA=0).
2. **S147 root cause measured:**
   - a fresh 49F read makes 64 authorize calls, each rebuilding the Enforcer: 20.5 s of 25.8 s;
   - the engine read is 4.4 s, so R9's B is HELD (@`c7a4c2e085`);
   - **fix M** (a per-request memo, the final release fresh) is RULED (101490);
   - the CTO half is SIGNED on `20c3533c` @`15bc769335`, and the CRO signed @`4eacc1283f`;
   - ~P opened ledger `irpt-authz-memo-20260926`.
3. **Andrew-direct UI review** (CRO brief @`fd463341e3`, 49 findings):
   - **DSGN_IRPTV1 PRD v0.13** @`6ce514ca80`: FWD-21, FWD-22 and FWD-23 added, plus the UI REVIEW FINDINGS table (the
     coverage check reads 49 of 49, exit 0);
   - UIR-07 ranking is server-side (~P, 101506);
   - backlog items 25-31 and C27-C33 added;
   - the CVO re-sign is asked (101504) and reads STALE.
4. **Andrew-direct: ETF Classifier tags take precedence** (@`714ba46408`: VXX Structured, GLD/PHYS Commodities).
   - ~M is asked to measure and bring a half (101502).
   - The CRO is asked to add it as UIR-50 (101503).
5. **Andrew question:** the last portal promote was 09-25 19:12 ET, PROD `36a37afc`. DEV is 6 ahead, none of it IRPT
   page work.

## Completion test

NOT DONE: 0 of 2 IRPT projects complete. D10 is UNMEASURABLE.

## Open calls

None at this seat.

state: ARMED
