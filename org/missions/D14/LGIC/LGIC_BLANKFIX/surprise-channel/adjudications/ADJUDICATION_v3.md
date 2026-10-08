# LGIC_BLANKFIX: CVO adjudication, round 4

Round 4 L8 compile and L9 adjudication by `3.0.0_SA_CVO`, on 2.0.0_SA_COO~G msg 106667 (round 4 drained, 6 of 6 orders
complete). Channel read at HEAD 20e21c5078: 34 rows, 0 ARMED; 30 dispositioned in ADJUDICATION_v1.md and v2, 4 here. One
JUDGMENT criterion graded on live runs (grade file `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND4_L9_GRADE_BQ5_AC2_20261008.md`): BQ5-AC2 MET, 142 of 142 and 18 of 18. After this document 0
rows are undispositioned: 1 GRADUATED with a remediation row, 3 DISMISSED. Clocks advanced at this compile: S4, W2-S9,
W1-S10 and W1-S8 REMEDIATED; W2-S2 stays OPEN.

<sweep_watermark>2026-10-08T01:05Z</sweep_watermark>

```json
[
  {
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T01:05Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "LGIC_BLANKFIX-C-S11",
    "one_line": "ROUND-4 L9 and L8: judgment criterion BQ5-AC2 is MET, 142 of 142 and 18 of 18 on live runs; three rows DISMISSED as records of how the round's cells met their orders.",
    "spec_asserts": "TO-BF-q-5 BQ5-AC2: both roots run LIVE by a seat that built none of the check, each read to the end and every line acted on from the line alone, without asking anyone.",
    "world_is": "BQ5-AC2: the first root's two REFUSED lines are FIX lines with a whole target, on a registry ruling this seat re-measured (the script reads 80,599 bytes and the same ETag in opal-data-bd and opal-data-cot); the second root's two HOLE lines are FIX lines whose target carries one per-firm variable that the line explains. Counted actionable; the grade file states the one judgment call. Records: W2-S10, the first root reads 142 where the order expected 141, because two function-name literals are typed; W1-S11, the two cot lines print FIX and not REFUSED because the registry rules first; W1-S12, the no-brace rule did not exist in the lines command and was added there.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "live runs by 3.0.0_SA_CVO 2026-10-08 00:5xZ of python lib/opal_naming_rootcheck.py <root> --map infra/logic/registry/root_map.json --report-only: bd-pipeline 'items=142 right=9 fix=118 not_asked=12 pattern=3 carded=0 refused=0 hole=0'; investor-reporting/directory 'items=18 right=13 fix=5 not_asked=0 pattern=0 carded=0 refused=0 hole=0'; each rc 0 and 0 lines different from its saved round-4 trace",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND4_L9_GRADE_BQ5_AC2_20261008.md",
        "python org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_traces_round4.py at HEAD: TRACES-R4 ok=True roots=2 items=160 hole=0 refused=0 differs=0",
        "aws s3api head-object code/bronze/cot_bronze_ingest.py in opal-data-bd and opal-data-cot (this seat): 80599 bytes, ETag a1d81b96e8b679142176ad827af2c00d, both",
        "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 20e21c5078 (34 rows, 0 ARMED) rows W2-S10, W1-S11, W1-S12"
      ]
    },
    "adjudicates": [
      "LGIC_BLANKFIX-W2-S10",
      "LGIC_BLANKFIX-W1-S11",
      "LGIC_BLANKFIX-W1-S12"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Records of how round 4's cells met their orders where the order's expectation and the build differed; each difference is explained in its row and re-read on this seat's live runs. No remedy is owed."
  },
  {
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T01:05Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "LGIC_BLANKFIX-C-S12",
    "one_line": "ROUND-4 L8: row S5 GRADUATED with its remediation row -- the proof-of-spec checker crashes on a proof instance that names a directory as an artifact path.",
    "spec_asserts": ".tools/proof-of-spec-check.py validates a proof instance before an order's complete flip; a path it cannot accept is refused with a verdict.",
    "world_is": "On a directory path the checker raises PermissionError and exits 2, which reads as a tool failure and not as a refusal; a worker listed 13 files one by one to get past it. The file is outside this project's write surface. Not reproduced by this seat.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 20e21c5078 (34 rows, 0 ARMED) row S5 (2.0.0_SA_COO~G, 2026-10-08T00:20Z)"
      ]
    },
    "adjudicates": [
      "LGIC_BLANKFIX-S5"
    ],
    "disposition": "GRADUATED"
  }
]
```
