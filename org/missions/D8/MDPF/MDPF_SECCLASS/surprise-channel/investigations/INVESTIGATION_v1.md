# MDPF_SECCLASS -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `2.0.0_SA_COO~M` at the L5 cut (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`).
Lane `ANY`.
**Id grammar:** a worker's row is `MDPF_SECCLASS-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that
coordinate); a seat's row is `MDPF_SECCLASS-S<k>`; the CVO's adjudication rows live in `../adjudications/` as
`MDPF_SECCLASS-C-S<k>`. **Append-only during the round.** Never edit an existing row.

```json
{
  "id": "MDPF_SECCLASS-S1",
  "project": "MDPF_SECCLASS",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~M",
  "surfaced_at": "2026-09-29T21:55:00Z",
  "one_line": "etf-classifications has a third writer the PRD's C-WRITER does not name: infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py batch.put_item()s rows (AAPL's live row reads updated_by 'seed-etf-constituents (1.0.0_SA_CTO~Z, Andrew-direct 2026-08-25)', sub_asset_class = the GICS sector), beside the seed path seed-etf-classifications.py.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~M (round 1 cell SC-k-2 carries instrument_kind onto both seed scripts' rows and reports whether the constituents seeder is part of the seed path; the C-WRITER wording is 1.0.0_SA_CTO's)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws dynamodb get-item etf-classifications ticker=AAPL (2026-09-29 20:3xZ): updated_by 'seed-etf-constituents (1.0.0_SA_CTO~Z, Andrew-direct 2026-08-25)', asset_class equity, sub_asset_class Information Technology, no classified_by",
      "infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py:48 TABLE = 'etf-classifications'; :199 updated_by; :223 batch.put_item",
      "PRD C-WRITER (org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md:128): exactly two writers, seed = the seed path, scheduled = FWD-7; C-TABLE (:126) names the seed path as yang_pipeline/seed-etf-classifications.py only"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Exactly two writers of etf-classifications rows: the seed path (seed-etf-classifications.py) and FWD-7's scheduled classification.",
  "world_is": "A second seed script, seed-etf-constituents.py, writes ETF-constituent stock rows (e.g. AAPL) with its own updated_by and no classified_by. Whether it is part of 'the seed path' is unstated.",
  "notes": "Not a bd-securities path: it reads ETF constituents, not the fork. It matters to FWD-3 (one edit place) and to C-WRITER's two-value classified_by. Andrew-direct 2026-09-29 ~21:4xZ to 2.0.0_SA_COO~M ('the canonical table should not be overwritten by anything in bd-securities') is carried into every round-1 face; this row does not depend on it."
}
```
