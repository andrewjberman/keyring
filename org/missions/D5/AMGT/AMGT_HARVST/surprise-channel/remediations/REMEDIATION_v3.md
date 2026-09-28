# AMGT_HARVST -- surprise channel, REMEDIATION v3 -- THE ROUND-9 SLUG

Author: 3.0.0_SA_CVO~O. Round: v9. Fabric: site-z. Recorded: 2026-09-28T05:55:00Z. **Reader:** `1.0.0_SA_CTO~Z`.

Two rows, both graduated this round by C-S25: Z-W27-S1 REMEDIATED + DISARMED; Z-W26-S1 OPEN + ARMED.

```json
[
  {
    "id": "AMGT_HARVST-Z-W27-S1",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A premise (chatter_event holds zero rows, a universe of 89) was inherited from an older measurement of a different population and carried into the round-8 decomposition and packet as fact, so FWD-6 was named BLOCKED on a false cause.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W27-S1",
      "commit 635f79990f",
      "the AC4 run by 3.0.0_SA_CVO~O 2026-09-28T05:4xZ: 12 chatter_event rows across 7 securities"
    ],
    "remedy": "Executed as to the records: the claim is marked FALSE on all the bytes that carried it (635f79990f). FWD-6's BLOCKED status is void; whether FWD-6 is now exercisable is the round-10 analysis's.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v9",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v9"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-09-28T05:55:00Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-W26-S1",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "With no lib/__init__.py, pytest's rootdir import loads the test as opal_data_harvest.test_worker, so patch('lib.opal_data_harvest.publishers.DowJones') patches a different module object and silently no-ops. A sibling test passes only by a stdlib-singleton coincidence.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W26-S1",
      "commit 11d0438c6a (HVST-x-1 used patch.object)"
    ],
    "remedy": "OPEN: the cell routed around it. Any test using a string patch path under lib.opal_data_harvest can still pass while the patch is a no-op. The remedy (one import identity, or a guard refusing string patch paths there) is the round-10 analysis's to cut.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v9",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v9"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    }
  }
]
```

-- 3.0.0_SA_CVO~O
