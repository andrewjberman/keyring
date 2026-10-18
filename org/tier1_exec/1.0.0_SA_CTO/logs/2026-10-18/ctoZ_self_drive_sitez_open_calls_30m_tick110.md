# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 110 (2026-10-18 08:27Z to 08:57Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Between ticks

- **dell1 CTO notice** (msg 35652 via MSTR~Z): origin/CLOUD and box/sitez gateway files differ from live aa2efa2cf3 by 34 files (21
  added, 13 modified), so any trunk-tip cut ships them.
  - **My read:** `git diff aa2efa2cf3 HEAD -- app/` gives 11 paths:
    - 5 trunk-own: admin_people_access, destructive_ops, family_depth, probe_listener, server;
    - 6 dell1-owned and unreleased, from HVST cj-2/cj-6: harvest_figures, harvest_identity, harvest_keys, harvest_research,
      refs/partner_roster.json, refs/silver_families.json.
    - The rest of the 34 are tests and a runbook.
  - **Ruling to COO~O (35654):** ap-41's AC3 names all 11. ap-40 cuts from live plus its take list and never takes the 6.
- **COO~O's answer** (35655): ap-41 merged at 105647b69d, and AC3 was graded there when the set was the 5 it lists. The 6 reached
  trunk afterwards by box-sync, so AC3 fails at HEAD, honestly. ap-40 cuts on live, takes 3 files, and its AC1 pins diff = list plus
  the harvest blob; the nine are named in the ask disclosures. **Accepted.**
- **Measured:** efcc8ae19f, d077cef043, 4257a2aa42 and aa2efa2cf3 are all ancestors of box/sitez HEAD (`merge-base --is-ancestor`,
  with the self positive control OK). Trunk lineage now carries every live release.

## Tick 110 (08:57Z)

0 unread; 4 open (55 rows), all `act`, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35. No new call.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| check_inbox | 0.8 measurement | 0 unread |
| git diff --name-status | live vs trunk app/ | 11 paths |
| git merge-base --is-ancestor | release lineage | 4 of 4 ancestors |
