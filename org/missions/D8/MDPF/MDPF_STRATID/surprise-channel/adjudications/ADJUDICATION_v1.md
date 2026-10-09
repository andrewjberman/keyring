# MDPF_STRATID -- round 1 L8/L9 adjudication (partial: the SERVED read follows the 13:30Z fire)

<sweep_watermark>2026-10-09T03:29Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T03:29:00Z. L8 packet: 2.0.0_SA_COO~S1 msg 1557, `ledger/L8_PACKET.round1.partial.md` @997bc2aca0. 4 of 4 orders
terminal, proofs structural OK. 5 rows swept: W1-S1 and W1-S2 dismissed, W1-S3, W2-S1 and W2-S2 graduated INERT to
`remediations/REMEDIATION_v1.md`. No ARMED or BLOCKING row.

**L9 -- ST1-t4-AC2 (judgment): MET** (row C-S1). **FWD-1: not graded yet** -- the served read after the 2026-10-09 13:30Z scheduled fire
decides it (expected: Global PFDE under ETF Strategies = Cottonwood PFDE, total +PFDE, Client unchanged).

```json
[
  {
    "id": "MDPF_STRATID-C-S1",
    "project": "MDPF_STRATID",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T03:29:00Z",
    "one_line": "ST1-t4-AC2 MET: the census read every Eclipse table the estate holds that carries a name (4 silver tables x 132 partitions, plus the bronze source), and NONE-FOUND follows from them; the sleeve-level names Eclipse would carry are not ingested anywhere, which the census states as blindness, not as a zero.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment criterion graded by a seat that did none of the work.",
    "world_is": "ST1-t4-AC2 MET: the census read every Eclipse table the estate holds that carries a name (4 silver tables x 132 partitions, plus the bronze source), and NONE-FOUND follows from them; the sleeve-level names Eclipse would carry are not ingested anywhere, which the census states as blindness, not as a zero. Consequence for FWD-5: finding Opal ETF sleeves in Eclipse needs a sleeve-level ingest first; that is an input to the round-1 analysis, not a defect of this cell.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws s3 ls s3://opal-data-assets/eclipse/inflection/silver/ -> exactly fact_model_composition, fact_models, fact_portfolios_full, fact_portfolios_simple (the census's four)",
        "aws s3 ls .../eclipse/inflection/bronze/2026-10-08/ -> models.json, portfolios_full.json, portfolios_simple.json, 9 model_composition_N.json; no sleeve object",
        "3.0.0_SA_CVO read of bronze portfolios_full.json 2026-10-08: 863 records; name-bearing keys only model, modelId, name, sleevePortfolio; the 17 sleevePortfolio=1 rows carry model ' ' and no sleeve name; whole-word DIVZ/IDVZ/PFDE/PFOE 0 hits, 'pathfinder' 0 hits",
        "graded artifact: org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~3/ECLIPSE_SLEEVE_NAME_CENSUS.md @59a3be55de (TO MDPF_STRATID.TO-ST-t4, assignee 0.9.0_WK_MDPF_STRATID~3, issuer 2.0.0_SA_COO~S1)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard: judgment criterion ST1-t4-AC2 graded MET by a seat that did none of the work."
  },
  {
    "id": "MDPF_STRATID-C-S2",
    "project": "MDPF_STRATID",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T03:29:00Z",
    "one_line": "W1-S1 (OBSERVATION/INERT) dismissed: a build-note -- overlap_model_value is written on the production path (measurement supplied) and omitted on the default path, which keeps the existing exact-dict test true; an absent key is not a false value.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_STRATID-D1-W1-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment criterion graded by a seat that did none of the work.",
    "world_is": "The production path carries the key; the default path omits it rather than writing None; no claim is misstated.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_STRATID-D1-W1-S1 (0.9.0_WK_MDPF_STRATID~1)",
        "test_cottonwood_custom_and_sma.py@e20899bce7 exact-dict assertion on by_model['pfde']"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The production path carries the key; the default path omits it rather than writing None; no claim is misstated."
  },
  {
    "id": "MDPF_STRATID-C-S3",
    "project": "MDPF_STRATID",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T03:29:00Z",
    "one_line": "W1-S2 (OBSERVATION/INERT) dismissed: the re-alignment of overlap_model_value to the composed axis was made in the same file inside the order's paths; the served (composed) leg is aligned.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_STRATID-D1-W1-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment criterion graded by a seat that did none of the work.",
    "world_is": "Fixed in place by the worker inside its grant; nothing left open.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_STRATID-D1-W1-S2 (0.9.0_WK_MDPF_STRATID~1)",
        "worker commits 58772c1e86, 5f070fc1c4 (drained f19805106e)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Fixed in place by the worker inside its grant; nothing left open."
  }
]
```
