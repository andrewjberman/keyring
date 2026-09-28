# AMGT_HARVST ROUND 8 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~O`. Routed by `1.0.0_SA_CTO~Z` (20260928T021824Z), which also ruled round 8 terminal on its
issued half (20260928T022141Z). **Written:** 2026-09-28 ~02:30Z. **Terminality:** 2 of 2 issued orders are complete
(`HVST-w-1`, `HVST-w-3`; issuer `2.0.0_SA_COO~Y`). The cards `w-2`, `w-4` and `w-5` carry to round 9.

Input: `investigations/INVESTIGATION_v1.md`, 66 rows; 1 was undispositioned (Z-W23-S1). L9 is vacuous, with its
cause named in C-S24.

Read at HEAD by this seat and not re-run: the listings half of Z-W9-S1 (`uploads.py:265`, `:302` route through
`_silver_append_retrying_object_name`), Z-S27 (`__main__.py:70`: "writes nothing to S3 by itself"), and Z-W11-S1
(`454fc37e30`, 1.0.0_SA_CTO~Z). Their REMEDIATION_v1 rows are append-only and still read OPEN; the flip is carried
to the round-9 analysis.

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S23",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T02:30:00Z",
    "one_line": "Round 8 L8: Z-W23-S1 is GRADUATED. It was a real issuer defect (AC2 named a directory that never existed, so it collected 0 tests), and it is remedied by the order's AMENDMENT 1.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Z-W23-S1 was the only undispositioned row on _latest_dispositions at 02:23Z (66 items, 17 files). AMENDMENT 1 @ad6c2b7f8b replaced lib/opal_data_harvest/tests/ with lib/opal_data_harvest/. This seat ran the amended invocation at 02:25Z: 3 failed, 306 passed. The same 3 known failures (Z-W21-S2) remain; the COO's 292 was read earlier and the suite has grown since.",
    "adjudicates": [
      "AMGT_HARVST-Z-W23-S1"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "task-orders/AMGT_HARVST.TO-HVST-w-1.listings-append-collides-and-the-suite-is-red.md AMENDMENT 1 (commit ad6c2b7f8b)",
        "python -m pytest lib/research/harvest/tests/ lib/opal_data_harvest/ -rA, run by this seat 2026-09-28T02:25Z: 3 failed, 306 passed",
        "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W23-S1"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "AMGT_HARVST-Z-C-S24",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-28T02:30:00Z",
    "one_line": "Round 8 L9 is VACUOUS, with its cause named: the round's only judgment criterion sits on the carded cell w-2, which never issued. Nothing issued this round carries a judgment criterion.",
    "class": "OBSERVATION",
    "spec_asserts": "Round 8 carries a judgment criterion, graded by the CVO at L9 (decomp :1306-1311).",
    "world_is": "The criterion sits on w-2 (decomp :1308), and w-2 is CARDED at Andrew under the vendor rule (:1209). The issued cells w-1 and w-3 are mechanical only (w-1 order point 4, and the COO~Y drain-end packet @3d74fc0ade). 1.0.0_SA_CTO~Z ruled at 20260928T022141Z that round 8 is terminal on its issued half and L9 is reported vacuous. The CTO names the miss as its analysis's: the rule required a judgment criterion without requiring it on a cell that could issue. The cards w-2, w-4 and w-5 carry to round 9 unchanged.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "decompositions/AMGT_HARVST_DECOMP.md:1206-1213 and :1306-1311 @4801bee438",
        "deliverables/2.0.0_SA_COO_Y/ROUND8_DRAIN_END_PACKET.md@3d74fc0ade",
        "org/mcp/inbox/3.0.0_SA_CVO/~O/read/20260928T022141Z_1.0.0_SA_CTO_Z_Ruling_round_8_terminal_on_the_issued_half.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item. No grade is recorded, because no issued cell carries a judgment criterion."
  }
]
```

-- 3.0.0_SA_CVO~O
