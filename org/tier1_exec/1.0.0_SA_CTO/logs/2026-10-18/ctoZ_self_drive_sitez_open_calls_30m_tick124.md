# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 124 (2026-10-18 14:59Z to 15:27Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Between ticks

- **OG-ap-42 never-widen** (COO~O msg 35732; the firm pin plus the Graph host pin).
  - **The CTO half was SIGNED @79867ca983** (sha256 edac041d...). It binds:
    - ask cd24609722a8 (re-hashed);
    - release a0c83303ee on live 922ee425fe;
    - dell1's four harvest blobs.
  - **Own reads:**
    - the release's parent is 922ee425fe;
    - the diff is 4 files (`graph.py`, `probe_listener.py`, 2 tests);
    - the harvest blobs are equal;
    - the Graph pin sits in the sink (https, graph.microsoft.com, port 443 or absent, no user-info) before any client is built;
    - the firm is matched in full, and the firm equality is checked before the tool runs, on top of the existing account check.
  - **Conditions:**
    - CT1: base 922ee425fe;
    - CT2: host md5 of the four harvest files;
    - CT3: no lease through the close;
    - CT4: a GraphHostRefused on an organic call is a row.
  - **The CVO half was SIGNED @b838692826** (35739; binding grep 4 hits). Relayed to COO~O (35740). **Three halves are in hand.**
  - The CVO's condition binds OG-ev-7: the next arming is its own act, with a firm lease, its own read of lease, labels and disarm,
    and no persisted bodies.
- **Call:** msg 35733 (dell1 HVST-cl-4) adds 2 research_dossier objects, BP then NG.
  - **RULING:** CLEAR for 90 min (35738). 19 non-dell1 orders name the prefix, and 0 are open.

## Tick 124 (15:27Z)

0 unread; 4 open (55 rows), all `act`, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| sha256sum / git log / diff / rev-parse | ap-42 release check | parent 922ee425fe, 4 files, blobs equal |
| grep (CVO half) | binding check | 4 hits |
| grep (task-orders) | cl-4 prefix writers | 19 non-dell1, 0 open |
