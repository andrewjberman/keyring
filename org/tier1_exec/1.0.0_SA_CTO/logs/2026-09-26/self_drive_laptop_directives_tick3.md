# SELF-DRIVE laptop directives -- tick 3 (2026-09-26 ~13:5xZ)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since tick 2 (@`b754e6df4f`, 13:22Z). **State: ARMED.**

## Scope

9 laptop directives. IRPT first:
- IRPT_BCKEND: active / EXECUTING (~P, ~M, ~Y on /closer-drive);
- DSGN_IRPTV1: active / EXECUTING (~D on /canonical-drive, round 5 issued).

Unread at the tick: 0.

## Acts (1.0.0_SA_CTO lane)

1. **UI walk, admin+Dev principal (packet `NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_ADMIN_DEV_PRINCIPAL_20260926.md`):**
   - v2 `4ae2693b` re-signed @`43d0a9d48d`.
   - K4 correction @`bdfd81063e`, on ~Y 101179: v2 omitted K4's one YCharts `securities_info` GET.
   - v3 `07b7a000` re-signed @`b70ede1756`: the diff is K4 only.
   - 4.0.0_SA_CRO signed v3 (message at 13:48:24Z). **Both halves are at HEAD, so ~P may create the principal.**
2. **Export deploy (B), packet blob `3c916b9c`:** CTO half SIGNED @`b70ede1756`, in
   `deliverables/SIGNOFF_IRPT_EXPORT_DEPLOY_B_20260926.md`. It adds two checks: the INF unarmed-plan negative arm,
   and rollback in reverse order (D3, D2, D1). The CRO half is owed.
3. **FAST leases** IRPT_BCKEND~M, ~P and ~Y re-armed for 12h, until 2026-09-27T01:52Z. The surfaces are unchanged.
4. **Watcher:** the inbox watcher re-armed on expiry.
5. **Messages:** acked 101173, 101179, 101181 and 101184. Sent 101176-101177 and 101187-101189.

## Open calls in scope

None at this seat. The PRD-002 alarms stay with Andrew ("alarms need further consideration"); that is not a call to
decide.

## Completion test

NOT DONE:
- IRPT_BCKEND and DSGN_IRPTV1 are both `active`;
- D10 has no members, so it is UNMEASURABLE (routed to 0.0.0_AB_MSTR at arm).

## Waiting on other seats

| seat | owes |
|---|---|
| ~P | principal create, then the walk; export B once the CRO half lands |
| ~D | the round-5 drain and the walk grades |
| ~M | Monday 09-28 runs |
| ~Y | K4, one POST in the walk window |

state: ARMED
