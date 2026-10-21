# NFRA_MCPORTAL -- the project slug (site Z): six undispositioned items adjudicated, with REMEDIATION_v6 in the same commit

Author: 3.0.0_SA_CVO~Z. Round: v14. Fabric: site-z. Recorded: 2026-10-21 ~00:5xZ.

**Input:**
- `2.0.0_SA_COO~MP` packet `deliverables/2.0.0_SA_COO~MP/ogw/OGW_R2_NINE_ROWS_PACKET_20261021.md` @04c43026dc, read whole, and
  its addendum on Z-S63 (ferry 00:38Z).
- The reason for this slug: Z-W3-S2's disarming remediation row (Z-C-S60, in REMEDIATION_v6.Z.md) is the project slug, and
  the row gate refuses it while any item is undispositioned or graduated without a remediation row.

**Checked by this seat:**
- `task-orders/NFRA_MCPORTAL.TO-MP-pe-1.breakdown-groups-by-source.md:128`: AC1's expect is now
  `named tests PASSED 10 of 10.*RESULT: PASS.*exit=0`, the order is `complete`, and W31-S4's unmatched literal is gone.
- **`DATA_CATALOG.yaml` at the live release `13917ef993`, `tool_index` block (lines 1349-3356, 2008 lines):**
  - `vendor:` 23 and `firm:` 23, for W31-S6;
  - `serves:` 7, `kind: store` 15 and `source_group:` 127, for W31-S7.
  - These are the packet's counts, re-measured.

**Verdicts:**
- W16-S1, W16-S3, W16-S4 and W31-S4 are DISMISSED as answered.
- Z-S63 is DISMISSED: the absent hash list is the intended state, by Andrew's word of 2026-10-09 and the dell2 CTO's msg
  4327 (COO~MP addendum 2).
- Z-S77 is GRADUATED to an OPEN remediation row that stays ARMED with its owner.
- In REMEDIATION_v6:
  - W31-S6 and W31-S7 are REMEDIATED, bounded;
  - W25-S2 is CLOSED_UNREMEDIATED with NOT_A_DEFECT;
  - Z-C-S60 disarms W3-S2.

## Rows

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S61",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-21T00:50Z",
    "one_line": "Z-W16-S1, Z-W16-S3, Z-W16-S4 (BLOCKING, INERT) DISMISSED as answered: each was the issuer's order defect on MP-z-6 (read paths missing from the sparse cone; a pick rule that chose a bucket channel; a store reader with only writers), fixed by AMENDMENT 1 (2e6385a297), after which AC1 passed 4 of 4 and drained 0aba910bd0e.",
    "class": "OBSERVATION",
    "spec_asserts": "A BLOCKING item is dispositioned before the project slug (spine L10).",
    "world_is": "2e6385a297 (2.0.0_SA_COO~MP): MP-z-6 AMENDMENT 1 after worker ~16's rows; issuer row Z-S75 records the cause and the 4 of 4 re-run; this seat graded MP-z-6 AC2 on the same drain (ADJUDICATION_v11.Z.md, Z-C-S49).",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W16-S1",
      "NFRA_MCPORTAL-Z-W16-S3",
      "NFRA_MCPORTAL-Z-W16-S4"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log -n1 2e6385a297 (read by this seat 2026-10-20)",
        "investigations row Z-S75; OGW_R2_NINE_ROWS_PACKET_20261021.md section A (read whole)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Answered: the order text was wrong, the amendment fixed it, and the criterion then passed on the drained run."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S62",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-21T00:50Z",
    "one_line": "Z-W31-S4 (BLOCKING, INERT) DISMISSED as answered: the AC1 expect that could not match pe1.AC1.sh's output was restated by AMENDMENT 2 as a regex the output does match, and MP-pe-1 is complete.",
    "class": "OBSERVATION",
    "spec_asserts": "W31-S4: AC1's expect 'named tests PASSED 10 of 10 -- RESULT: PASS -- exit=0' cannot match the check's three-line output.",
    "world_is": "task-orders/NFRA_MCPORTAL.TO-MP-pe-1.breakdown-groups-by-source.md:128 expect 'named tests PASSED 10 of 10.*RESULT: PASS.*exit=0'; :151 <status>complete</status> (read by this seat).",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W31-S4"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "task-orders/NFRA_MCPORTAL.TO-MP-pe-1.breakdown-groups-by-source.md:126-129, :151 (printed by this seat)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Answered by AMENDMENT 2; the expect now matches the check's own output."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S64",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-21T00:50Z",
    "one_line": "Z-S63 (ARMED) DISMISSED: site Z has no account_id_hashes.txt, and that is the intended state on every box -- Andrew-direct 2026-10-09 ~19:2xZ ('I don't care about the client data getting committed to Git... spending time messing around with that is I don't think is really worth it') stopped the containment sweep, and the dell2 CTO ruled the absence intended (msg 4327); the owner 0.0.0_AB_MSTR~Z withdrew its fabric-wide framing.",
    "class": "OBSERVATION",
    "spec_asserts": "The client-data commit check reads a hashed account-id list on every box that commits.",
    "world_is": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_192xZ_CLIENT_DATA_IN_PRIVATE_GIT_NOT_WORTH_TIME.md:5-6 (printed by this seat): the verbatim; item 2 stops the containment sweep. COO~MP addendum 2 (ferry 00:45Z): dell2 CTO msg 4327 rules the absent list intended; MSTR~Z withdrew (ferry 00:21Z).",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S63"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ANDREW_DIRECT_20261009_192xZ_CLIENT_DATA_IN_PRIVATE_GIT_NOT_WORTH_TIME.md:1-12 (printed by this seat)",
        "20261021T004500Z addendum 2 from 2.0.0_SA_COO~MP (read whole)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Not a hazard by Andrew's word: the list's absence is the intended state. Bound: where a never-widen half or a trace says to keep client figures out of a record, that half still binds; this disposition retires only the commit-check list."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S65",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-21T00:50Z",
    "one_line": "Z-S77 (ARMED) GRADUATED to an OPEN remediation row, owner 2.0.0_SA_COO~O, date 2026-10-21: it disarms on batch16's CLOSED report carrying the first measured halt-gate time under 60 s, and it is also the carrier of Z-W2-S8.",
    "class": "OBSERVATION",
    "spec_asserts": "A gateway release's rollback trigger is meetable by its named rollback command.",
    "world_is": "Z-S77: the 2026-09-25 disarm of W2-S8 rested on an unmeasured premise; halt-gate-check.sh L456-475 runs before the host step (ADJUDICATION_v13.Z.md, Z-C-S59).",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S77"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ADJUDICATION_v13.Z.md#NFRA_MCPORTAL-Z-C-S59 @a19cd08032",
        "OGW_R2_NINE_ROWS_PACKET_20261021.md section A (read whole)"
      ]
    },
    "disposition": "GRADUATED",
    "dismissal_reason": "Graduated: the hazard is live for every gateway rollback until a measured scan time says otherwise."
  }
]
```

-- 3.0.0_SA_CVO~Z
