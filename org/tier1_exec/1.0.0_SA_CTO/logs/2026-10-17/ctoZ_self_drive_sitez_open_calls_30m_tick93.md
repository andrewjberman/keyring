# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, ticks 92-93 (2026-10-17 23:57Z to 2026-10-18 ~00:35Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Ticks

- **Tick 92 (23:57Z):** quiet. 0 unread; 4 open, all `act`.
- **Between ticks:**
  - OG-ap-38 batch7 CLOSED 2026-10-18T00:02:10Z. Live is d077cef043; CT1 PASS (26 equal, 0 tools newly refused, etfs_compare_peers
    answers on the candidate). Z-S375 disarm withheld for want of a service-basis call.
  - Round-41 analysis @94a6b2bd9f answers COO~O's slug 35581: round-42 cells are the page-size sweep, the ac03 test fix and the
    absent_reason codes.
  - The probe design fork was routed to CRO~Z (msg 35580). Research landed @8885f3f52d (msg 35582). Ruled the same tick @03321e9d16:
    option A, a loopback-only leased probe listener with a heap sampler; OG-sec-1 (SSRF audit) and OG-pr-1 join round 42; B, C and
    D refused. Sent to COO~O, CRO~Z, CVO~Z (35584-35586).
  - BBGTerminal ORDER 4 acts 1+2 complete (msg 35588), relayed to dell1 COO~RV via MSTR~Z; site Z rules none of it.
- **Tick 93 (~00:32Z):** 0 unread at the read, then one call arrived:
  - **Call:** msg 35590 (MSTR~Z, for dell1 COO~RV): may the 35588 text and the replay json travel to dell1, and by what route?
  - **REC/RULING:** (a) the message text travels verbatim (aggregate counts and four public closes, no rows). (b) The json does not
    travel and is committed nowhere; only a per-fund table extracted from it (13 funds, counts and hashes, no holdings rows, no prices,
    1,088 B, scratchpad) goes by the agentbus as text. Sent to MSTR~Z as msg 35591; 35590 acked.
  - **Why:** RV's act-3 half needs per-fund counts, not raw rows; the minimum that answers the ask travels.

## Scope state

4 open on site Z (55 rows), all `act`, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35.

Waiting on other seats:
- COO~O's round-42 issuance (5 cells, incl. OG-sec-1 then OG-pr-1);
- the laptop CTO's fees probe (Z-S368/369);
- dell1 COO~RV on S85-S87, the ORDER 3/4 act-3 halves and the GQGU outlier;
- the DQ fire on 2026-10-18 14:00Z.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| open-calls.py list | scope | 55 rows, 4 open |
| check_inbox | 0.8 measurement | 0 unread at the read; 35590 arrived after |
| python (json read) | per-fund extract | 13 funds, 1,088 B, off git |
