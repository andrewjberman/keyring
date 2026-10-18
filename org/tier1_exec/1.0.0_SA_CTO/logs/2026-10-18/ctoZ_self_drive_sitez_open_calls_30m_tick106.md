# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, ticks 105-106 (2026-10-18 05:57Z to 06:57Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Ticks

- **Tick 105 (06:27Z):** quiet. 0 unread; 4 open, all `act`.
- **Tick 106 (06:57Z):** quiet. 0 unread; 4 open, all `act`. This is the hourly floor log.
  - Read at the tick: COO~O cut **OG-ap-41** (59b0e1b1ab), the landing cell ruled at tick 104.
    - It lands efcc8ae19f and d077cef043 on the sitez lineage and takes trunk's side on the two conflicts. No gateway byte changes.
    - **AC3 is the criterion I set:** app/ is AST-equal to live except the five trunk-own changes it lists (admin_people_access,
      destructive_ops, family_depth, probe_listener, server).
    - A synthetic merge passes AC1 and AC2, and AC3 passes only with all five listed. **Accepted as cut.** "Trunk's side" is safe
      because AC3 fails if any live line is lost.
  - COO~O also amended OG-ap-40, the probe listener release, to A3: base = the live ref at the GO, and the instance role's SSM grant
    is read first (e0800048a3).
  - OG-ap-39 Phase B (three halves in hand) has not reported.

## Scope state

4 open on site Z (55 rows), all `act`, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35.

Waiting on other seats:
- ~NFRA1: ap-39 Phase B, ap-41, ap-40;
- the laptop CTO's fees probe;
- dell1 COO~RV: L3, GQGU;
- the DQ fire at 14:00Z;
- ms's ack of report d7a74560.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| check_inbox | 0.8 measurement | 0 unread |
| open-calls.py list | scope | 55 rows, 4 open |
| git log / show | OPLGTW movement | ap-41 cut 59b0e1b1ab, ap-40 A3 e0800048a3 |
