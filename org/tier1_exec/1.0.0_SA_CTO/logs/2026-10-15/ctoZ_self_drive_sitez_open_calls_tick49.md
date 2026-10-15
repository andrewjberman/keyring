# /self-drive sitez open calls -- tick 49 (22:52Z 2026-10-15), `1.0.0_SA_CTO~Z`

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md`
@ce0ba39d90. Covers the span since tick 48 (@ebc54d3a08). **state: ARMED.**

## Measured

- `open-calls.py list`: rows 46, open 7, all person acts.

**Gateway finish, planned vs cut:**
- **OPLGTW:** cl-1 to cl-4 complete (cl-1, the client core and Schwab, merged @01345bac7c); cl-5, cl-6, cl-7, gf-1 and
  ap-22..24 pending.
- **MCPINDEX:** MX-c-22 complete (@22a906d22e); RESEARCH issued @dfabd4baff (MX-c-30, MX-c-34..37).
- **MCPORTAL:** MP-pf-1 complete; MP-pf-3 issued to read `serves` (@068ea1969f).
- **No planned cell with met gates lacks an order.**

## Rulings and acts since tick 48

1. **C-GROUP item 2 amended @5ba12d1de5** (COO~MP msg 34589).
   - Each assets or bd `tool_index` entry carries `serves`, a LIST of (vendor, firm) pairs derived from its rows.
   - A single pair would read `unresolved` for the multi-vendor `client_*` tools.
   - COO~MI carries it as MX-c-23 A1, check c23.AC4 @81a60d64e7 (msg 34596).
2. **COO~MI2 RESEARCH issuance read** (msg 34594). Bucket is already present on 165 of 180 RESEARCH rows; the other 15
   are normalised by MX-c-21's emitter.
3. **Dell1 COO~R1's read after the 10-16 ~09:00 ET price-leg fire** (relay msg 34597): site Z carries bn-5 byte-equal.
   I take the read myself (one-shot cron e42419d8, 09:23 local) and report through MSTR~Z.
4. **OG-ap-21, CTO never-widen half SIGNED @378438988e** at release d577e0e729 on live c4c106aea1 (ask msg 34600).
   - Z-S153: keep the base guard. Z-W67-S1 stays open as its own cell after the finish.
   - Z-S154: drop the MP-pd-3 test.
   - The CVO half @bee4c81023 was relayed to COO~O (msg 34604). The COO half is the last one owed.

## Acts only Andrew can do (each with its citation)

1. One MC Portal sitting, including one sign-in as Opal Bloomberg (21d9; covers 21c5, 8ed7, f0d2). Citation: his login and
   a human read.
2. One sitting with Alyssa (def4; 3b41 is a duplicate). Citation: his person act.
3. One Teams message from his account to Opal Bloomberg (a519). Citation: his own account.

## Completion test

NOT DONE: 7 open calls, every one a person act.
