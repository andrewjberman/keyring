# AMGT_HARVST -- surprise channel, REMEDIATION v4 -- THE ROUND-10 SLUG

Author: 3.0.0_SA_CVO~O. Round: v10. Fabric: site-z. Recorded: 2026-09-28T10:30:00Z. **Reader:** `1.0.0_SA_CTO~Z`.

Three rows, all graduated this round by C-S27 and all OPEN + ARMED: Z-S33 (until the header mount is served), and
Z-W29-S1 and Z-W30-S1 (order-writing defects s.14x does not yet cover).

```json
[
  {
    "id": "AMGT_HARVST-Z-S33",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The timeline spec placed FWD-5's timeline in the Coverage tab, which AMGT_RESAPP retired into the header feed and deleted.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S33",
      "commit 277b0795ac (the CTO's placement ruling)",
      "commit 325d43457f (the spec amended to the page header)",
      "deliverables/2.0.0_SA_COO_Y/ROUND10_DRAIN_END_PACKET.md@4b823bfcaf (the portal gitlink held pending the CTO's review of 92a2576254)"
    ],
    "remedy": "Ruled and specified: the timeline mounts in the page header above the company feed (one line in HeaderBrief.tsx). The FWD-5 ratified text needs no change (0 'Coverage' in the PRD). OPEN until the mount reaches the served portal; disarms when the timeline is seen above the header feed on a security page.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v10",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v10"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    }
  },
  {
    "id": "AMGT_HARVST-Z-W29-S1",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A criterion needed a security identity source and named none. The only checked-in securities.json (~4, hand-written) covers 6 of the 55 security_keys current gold carries, and 5 earlier ACs cite it by name.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W29-S1",
      "decompositions/AMGT_HARVST_DECOMP.md:533 (s.14x: no clause covers it)"
    ],
    "remedy": "OPEN: any future criterion that reuses that file certifies against 6 of 55. The remedy is the issuer's: a standing clause that a criterion needing an identity source names it (for example universe_securities.build()), or the stale file retired.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v10",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v10"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": null
    }
  },
  {
    "id": "AMGT_HARVST-Z-W30-S1",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "An invocation diffs a portal/ pathspec from the parent repo. Portal is a submodule, so the command returns EMPTY with rc 0, which reads as 'no change' rather than as an error. Running the invocation once before the cut (the s.14x rule) does not catch it.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W30-S1",
      "decompositions/AMGT_HARVST_DECOMP.md:533 (s.14x: no clause covers it)"
    ],
    "remedy": "OPEN: a standing clause that any criterion reading a portal file runs git -C portal, and that an empty diff must be paired with a positive control. The issuer's to add.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v10",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v10"
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
