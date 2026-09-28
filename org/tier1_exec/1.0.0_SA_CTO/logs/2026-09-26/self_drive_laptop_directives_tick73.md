# SELF-DRIVE laptop directives -- ticks 72-73 (2026-09-27 ~23:18Z to 2026-09-28 ~00:18Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the tick-71 log (@`89733a6564`). **State: ARMED.**

## The export chain -- window 19 closed (@`6d6e5984b2`)

- The decrypt fix held (0 AccessDenied), and the page's S26 poll is live.
- The render then failed at `selection.py:49-50`: every RENDER_DELEGATE was refused.
- **Ruled (102216):** an adapter-only rule, under which the delegate reads ONLY the grant-pinned selection, within the
  tenant and grant firm and the delegator-by-grant set; `_scope` untouched.
  - **CTO half @`30a4f2670f`** (diff `c8ef8b7751` read); CRO @`7f91727da1`.
  - Served as `F0bYtOfB` at 23:47:48Z; cold start answered.
- **S27** (the page stopped on a pending receipt that answered UNAVAILABLE/NOT_READY): ruled (b) (102222). The backend
  answers RUNNING while the export builds, and the page names any refusal (~D TO-IV-e-78).
  - That needed a contract change, so **R11 was written by this seat @`3c053cdf3f`**: export-receipt data is optional
    while QUEUED or RUNNING, mirroring R2. The schema was checked and both branches tested.
  - **The CVO signed the ratified-text half @`ab453f59ed`.** The wording it named was fixed @`25f7581ded`.
  - ~P's RUNNING receipt ledger is open @`f7e6b8b6cf` (apply after the freeze). ~D's TO-IV-e-78 amendment regenerates
    the portal wire copy against R11.

## irpt-status: a failed deploy, rolled back, and rebuilt

- HyEyoJ67 failed at cold start (stale `served.py`); it was rolled back at 23:15:47Z (tick-71 log).
- **Rebuild 2** (CTO half @`7ff22eace9`, CRO @`85593bc122`):
  - HEAD served.py, a 4-member census and an `_authz` census;
  - a built-zip cold-start smoke whose negative control reproduces the production AttributeError.
  - **Served `5fSyChId` at 00:02:49Z, read back by this seat.**
- The CRO's before/after read was taken after the apply (P's miss). The substitute (the old zip run on the same live
  reads) is EQUAL, and the CRO accepted it (@`da4b0bc76f`).
- ~Y verified live: window 15 reads **READY ANALYSIS_READY PER_SECTION, 51 dates** (@`f83d90684c`).
- ~Y built `zip_cold_start_smoke.py` (@`a2e417e865`), my standing smoke condition as a reusable tool.
- **Window 20** (K10 only, read-only; decides S25): CTO @`519ab8bb5c`, CRO @`802c8fb54d`. It closes before 02:30Z.

## Round 9

IV-e-68 and IV-e-69 are drained to local DEV `12aa026a`. TO-IV-e-79 re-goldens the tests the removed firm chip broke.

## Capacity

C: has 9.1 GB free. MSTR's S19 purge freeze runs ~03:00-05:00Z.

## Open calls at Andrew

1. BLOCKING: remove the ~5.7 GB Downloads scratch?
2. CARRIED: Schwab's registration-code list (UIC-16).

## Completion test

NOT DONE: 0 of 2 IRPT projects are complete (both `active`). D10 is UNMEASURABLE (no members).

state: ARMED
