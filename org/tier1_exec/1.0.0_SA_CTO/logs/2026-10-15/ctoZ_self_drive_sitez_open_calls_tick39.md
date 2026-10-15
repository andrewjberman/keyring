# /self-drive sitez open calls -- tick 39 (10:50Z 2026-10-15), `1.0.0_SA_CTO~Z`

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md`
@ce0ba39d90. Covers the span since tick 38 (@966cb94af1). **state: ARMED.**

## Measured

- `open-calls.py list`: rows 45, open 7, boxes 1 read 1, absent none. The 7 open rows are the same as at tick 38, and every
  one is a person act (listed below).
- Inbox: 1 broker message (34383, MSTR~Z's re-send that OG-ng-1 @bf9198273e landed; already acted on), acked.

## Rulings and acts since tick 38

1. **OG-ap-20, CTO half condition 2 (row Z-S144, CloudOps~Z msg 34410): satisfied.** Grounds: the cone fix; the trunk
   ENFORCE PASS at `f12b5d39bd`; the grant blob `1efa01e5fd` is equal at release `06cfb6db64` and at `f12b5d39bd`, which
   I read myself. Ruling record @8c2ab4855e. Sent to CloudOps~Z and COO~O.
2. **OG-ap-20, condition 1 (row Z-S141, COO~O msg 34414): done.** COO~O repaired `ap20.AC1.sh` @4ffb7a40c0. I re-ran it at
   the release: RESULT PASS, rc=0 (12 files changed, 0 outside the allowed set, 6 of 6 tools registered, grant has 1
   policy with no wildcard and no Put or Delete).
3. **OG-ap-20, CVO half SIGNED (CVO~Z msg 34415, @d463859c97).** I relayed it to COO~O, because the CVO cannot send
   there. All three halves are signed at `06cfb6db64`. The CVO's conditions: the six tools are read through
   `mcp.opalinvest.dev` against the 60 s ALB, and `etfs_get_ownership_rollup` exercises the single-object ARN.
   CloudOps~Z opened the deploy ledger `nfra-oplgtw-gateway-release-g5a` @cc6f8e8bbc.

## Moving without a call

- OG-rv-3 (batch hookup of the ten rival-fund tools): cut @bcff0f9889, amended A1 @92af867a7d.
- MX-c-18 (MCPINDEX tags) is complete; the MX-c-19 slot is re-seated for the stale test @bf89afe102.

## Acts only Andrew can do (each with its citation)

1. One MC Portal sitting, including one sign-in as Opal Bloomberg (21d9; covers 21c5, 8ed7, f0d2). Citation: his login
   and a human read (TO-MP-z-6).
2. One sitting with Alyssa (def4; 3b41 is a duplicate). Citation: his person act (TO-MP-c-2).
3. One Teams message from his account to Opal Bloomberg (a519). Citation: his own account; he answered "later".

## Completion test

NOT DONE: 7 open calls, every one an act only Andrew can perform. No call is open for a decision.
