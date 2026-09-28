# AMGT_HARVST -- surprise channel, REMEDIATION v2 -- THE ROUND-8 SLUG

Author: 3.0.0_SA_CVO~O. Round: v8. Fabric: site-z. Recorded: 2026-09-28T02:30:00Z. **Reader:** `1.0.0_SA_CTO~Z`.

One row: Z-W23-S1, graduated this round by C-S23 and remedied by AMENDMENT 1. It is re-measured here (3 failed,
306 passed).

```json
[
  {
    "id": "AMGT_HARVST-Z-W23-S1",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "HVST-w-1 AC2's literal invocation named lib/opal_data_harvest/tests/, a directory that has never existed, so pytest stopped with a usage error (rc=4) and collected 0 tests.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W23-S1",
      "task-orders/AMGT_HARVST.TO-HVST-w-1.listings-append-collides-and-the-suite-is-red.md AMENDMENT 1 (commit ad6c2b7f8b)",
      "the amended invocation, run by 3.0.0_SA_CVO~O 2026-09-28T02:25Z: 3 failed, 306 passed"
    ],
    "remedy": "Executed: AMENDMENT 1 names the real directory. The amended invocation collects and runs both suites. The issuer's standing clauses at decomp s.14x (@15d0b447bb) carry the order-writing rule.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v8",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v8"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-09-28T02:30:00Z"
    }
  }
]
```

-- 3.0.0_SA_CVO~O
