# MDPF_SECCLASS -- round 19 remediations

<sweep_watermark>2026-10-11T02:59Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T02:59:00Z. Graduated at ADJUDICATION_v15: 3 rows, all INERT. D1-S26 needs a build cell (the round-20 item); D1-S25 rides REMEDIATION_v9's D1-S23; D1-S27 is C_06's trace.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-S26",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "SC-e-79 changed the shared lib (classify_with_identity resolves a ticker-no-row position by its NAME:: row), but BD's three served classify sites (D_04 :160-167, C_06 :228-233, D_03 :135-140) call it only for a BLANK ticker. The branch is unreachable on the served path, so the 23 ticker-no-row securities ($966,285) still serve unclassified. The cell's AC1 graded the function, not the caller.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S26 @2ae7d56414",
      "ADJUDICATION_v15 D1-C-S1: call sites read at box/dell1 HEAD 1974b85f4e; served BD firm Unclassified 972,621.40 at data_as_of 2026-10-08 (VersionId 5Ws3Q6veR.qd3bueY48qALseVpW10kRl)"
    ],
    "remedy": "One build cell: the three BD classify sites route a non-blank ticker that classify() misses to classify_with_identity(ticker, name, cusip). Its acceptance must exercise D_04's SERVED classify path with a ticker-no-row position, not the lib function. Close when: a scheduled BD fire after the ship serves the 23 by their NAME:: rows and firm Unclassified falls by about $966K",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v19"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-S25",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "An addendum to D1-S23 (REMEDIATION_v9). safe-deploy's seat-gates matched 15 hits on the data/cot root, none contending for the three keys shipped. Three new limbs: (a) one unrelated crossbox call arms every root whose token its body document quotes; (b) the deploy's own open ledger entry, which the NEVER law requires be opened first, counts as contention against itself; (c) one slug is counted once per status it has held.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S25"
    ],
    "remedy": "The same fix as D1-S23: key the limbs on the deploy's own write set. Also exclude the actor's own ledger entry and count distinct slugs. Close when: D1-S23 closes, and a ship whose own entry is open reads 0 hits for that entry",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v19"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-S27",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "C_06's firm-daily snapshot total differs from the sum of its published class values by -4.71 / +128.06 / -128.57 on 2026-10-06 / 07 / 08 (about 6e-8 of $2.0B). D_04's Unclassified line is total minus the six classes by design, so it carries that gap.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S27 @4ee11df53c"
    ],
    "remedy": "Owner to route to C_06's lane: trace whether a position of about $128 counts in total on one day and in a class on the next. Close when: total equals the class sum on three consecutive firm-daily snapshots, or the gap is explained and ruled acceptable",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v19",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v19"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  }
]
```
