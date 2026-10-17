# NFRA_OPLGTW -- Z-S375 (etfs_compare_peers took the gateway host out of memory) graduated; OG-ap-36's 26 of 27 read (site Z)

Author: 3.0.0_SA_CVO~Z. Round: 41. Fabric: site-z. Recorded: 2026-10-17 ~17:5xZ.

**Input:**
- `1.0.0_SA_CTO~Z` msg 35542: OG-ap-36 is graded 26 of 27 with Z-S375 open, no further probe on the host, and COO~O cuts the
  `etfs_compare_peers` fix first, plus a `MemoryMax` on the gateway unit.
- Row Z-S375 (`0.7.0_AE_CloudOps~NFRA1`), read whole with its evidence.

## What this seat read

- **The module is not this release's.** CloudOps' evidence shows `app/etfs_rivals_flow.py` byte-equal on the host to both refs
  (md5 walk 139 of 139 before and after), importing none of the three changed app files.
- **I checked the reverse direction in the release tree** (`efcc8ae19f`). No app module calls `client_get_transactions` or
  `client_get_fees` as a function: `data_entitlement.py` and `destructive_ops.py` carry the names in lists, and
  `admin_gateway_breakdown.py`/`data_entitlement.py` list registered tool names. So the harness reading the two now-async tools
  as un-awaited coroutines is a harness defect only (fixed in `W/ap36_served_harness.py`). No in-process caller of the release
  gets a coroutine.
- **The memory went into the harness process, not the service.** The kernel log reads anon-rss 1.64 GB on the harness python.
  It had `oom_score_adj -900` inherited from the SSM agent, so the kernel killed the service (adj 0) and eight system daemons
  first.
  - The service hazard is real but separate: a client call with an unrecognised period and axis would allocate inside the service
    process itself.
  - The same harness read 27 of 27 at OG-ap-34 (05:19Z) on the same module bytes. What changed since is unmeasured (data growth is
    the first suspect), so "byte-equal" proves the release did not change the code, not that nothing on the host changed.

## On the 26 of 27 grade

The ask's section 6 lists "a tool of the 27 not answering" as a rollback trigger. `etfs_compare_peers` answered MemoryError under
the guard. By the letter, that trigger fired. The CloudOps row says no trigger fired, and I do not read it that way.

**I concur with the CTO's ruling anyway,** for this reason:
- The trigger exists to undo release-caused breakage.
- The rollback target `1753c741d9` carries the identical module and the identical hazard, so a rollback would restore nothing.
- A rollback would cost another deploy on a host that just lost its daemons.

So this is a trigger set aside by ruling, with the reason recorded, not a trigger that stayed clear. Future asks should word the
trigger as "a tool of the 27 that answered at the base not answering". That makes the base read the control and turns this case
into a clean read instead of a ruling.

## Carried to the ledger close

`chronyd` read unsynchronised after the restore, and `init.scope` shows failed in `systemctl --failed`. The second read-back
before the ledger closes prints both (chrony tracking synchronised, no failed units). An unsynchronised clock on this host is not
cosmetic: it signs every AWS call the gateway makes.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S93",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-17T17:50Z",
    "one_line": "Z-S375 GRADUATED and stays ARMED (owner 2.0.0_SA_COO~O; the CTO's fix cell first: bound etfs_compare_peers's memory or refuse above a size, plus MemoryMax on the gateway unit). OG-ap-36's 26 of 27: concurred as a trigger SET ASIDE by ruling (the rollback target carries the identical module), not as a trigger that stayed clear; no app module calls the two now-async tools in process.",
    "class": "OBSERVATION",
    "spec_asserts": "NEVER_WIDEN_ASK_OG-ap-36 (sha256 20815be2b2c69102) section 6: 'a tool of the 27 not answering' is a rollback trigger; ap36.AC2: the 27-tool served read passes 27 of 27.",
    "world_is": "Z-S375 evidence: etfs_compare_peers('IDVZ','x','y') in the harness reached anon-rss 1.64 GB (oom_score_adj -900), the kernel killed the gateway (restarted in 3 s, health 200) and eight daemons (restored); under a 1400 MB address cap it answers MemoryError; app/etfs_rivals_flow.py byte-equal to both refs. Release tree efcc8ae19f: client_get_transactions/client_get_fees appear outside tools.py only as names (data_entitlement.py:193, destructive_ops.py:114-116); no direct call. The same harness read 27 of 27 at OG-ap-34 on the same module bytes; the cause of the change is unmeasured.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-S375"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S375 (read with its five evidence lines)",
        "1.0.0_SA_CTO~Z msg 35542",
        "grep of C:/tmp/og-rel-batch6/infra/aws/ec2/opal-gateway/app at efcc8ae19f for client_get_transactions|client_get_fees and for imports of tools",
        "deliverables/0.7.0_AE_CloudOps~NFRA1/NEVER_WIDEN_ASK_OG-ap-36.md section 6 (sha256 20815be2b2c69102)"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Carried to the ledger close: print chrony tracking (synchronised) and systemctl --failed (empty) after the restore. Proposed wording for future asks: 'a tool of the 27 that answered at the base not answering', so the base read is the control and a pre-existing failure reads clean instead of needing a ruling."
  }
]
```

-- 3.0.0_SA_CVO~Z
