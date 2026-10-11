# NFRA_MCPINDEX -- surprise channel, REMEDIATION v7 -- THE ROUND-9 SLUG

Author: 3.0.0_SA_CVO~Z. Round: v7 (round 9). Fabric: site-z. Recorded: 2026-10-11 ~15:3xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Round 9: 5 of 5 complete, MAY-CLOSE, all-mechanical. L8 is at `adjudications/ADJUDICATION_v8.md`:
- **FWD-18 REALIZED** at 3 of 14, from the served catalog (C-S45).
- **FWD-19's two GAPs stand** (C-S46). The trade-rec OWNER is the analysis's question: the blocker is the Opal side's fund
  grain (the engine bridge, NFRA_OPSWKF), not a missing custodian status.
- Five round-8 remediation rows are met (file header). Z-S97 graduates, below.

**For the analysis:**
1. FWD-19 needs producers, not readers. Billing goes to ADVI_BILLING; trade rec is the owner question above.
2. The Z-S100 battery lesson: exercise a dry-run-excused check's PASS arm once on a planted input before the cut.
3. The deploy wrapper's sparse-tree imports (Z-S92) recurred on MX-r-10.
4. The thread criterion stays HELD at Andrew.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-S97",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~C",
      "at": "2026-10-10T23:30Z"
    },
    "mechanism": ".tools/tests/test_round_close_and_research.py reads CLOSE-GATES-TEST 19 of 24 at HEAD: four cases call read_orders with the retired 3-argument signature and one ENFORCE case reads rc=0 where a refusal is expected, so a new regression in round-close-check hides among standing failures",
    "evidence": [
      "3.0.0_SA_CVO~Z re-run ~15:2xZ 2026-10-11: cases=19/24 ok=False; Z-S97 (0.0.0_AB_MSTR~Z)"
    ],
    "remedy": "Repair the four cases to read_orders(src, proj_dir, rnd, ws), and make the ENFORCE case refuse again, or re-scope each with a reason; land it with the Z-C-S42 J-id scoping fix, under a test that plants a stale CVO row. Disarms at 24 of 24.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C",
      "round": "v7"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
