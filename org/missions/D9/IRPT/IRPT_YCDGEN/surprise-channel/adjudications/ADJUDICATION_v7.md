# IRPT_YCDGEN: CVO adjudication, round 8

<sweep_watermark>2026-10-11T08:03Z</sweep_watermark>

Round 8 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T08:03:36Z. L8 input: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r8/ROUND8_DRAIN_END_READ_20261011.md @a6bd47170b (msg 4448)`. No judgment criterion; no run of FWD-1.
10 rows dismissed below. D2-W10-S7 graduates in `remediations/REMEDIATION_v7.md`. Six rows of REMEDIATION_v6 are closed in place.
FWD-1 stands NOT MET as graded at round 7. About 41 INERT rows of rounds 6 and 7 remain uncompiled.

```json
[
  {
    "id": "IRPT_YCDGEN-C-S22",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T08:03:36Z",
    "one_line": "Round 8 rows dismissed: the worker's five resolving records D2-W10-S1 and D2-W10-S5 (the generated report type equals the committed one), D2-W10-S2 and D2-W10-S6 (the readers and route tests pass; the brand files are committed), D2-W10-S3 (the generator renders the union as a type, tsc returns 0); D2-W10-S4 (the re-cut of D2-W7-S1, which stays open ARMED in REMEDIATION_v6 under its own id); D2-S40 with S14 (S14's denied SendCommand now succeeds for the applier); D2-S41 (a criterion that no valid proof could pass, amended @289391dfbf); and this seat's read row D2-S42. D2-W10-S7 graduates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-D2-W10-S1",
      "IRPT_YCDGEN-D2-W10-S2",
      "IRPT_YCDGEN-D2-W10-S3",
      "IRPT_YCDGEN-D2-W10-S5",
      "IRPT_YCDGEN-D2-W10-S6",
      "IRPT_YCDGEN-D2-W10-S4",
      "IRPT_YCDGEN-D2-S40",
      "IRPT_YCDGEN-S14",
      "IRPT_YCDGEN-D2-S41",
      "IRPT_YCDGEN-D2-S42"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Closed in place in REMEDIATION_v6 on these records and this seat's brand read: W6-S1, W6-S2, D2-W6-S3, D2-W6-S1, D2-W6-S2 and D2-S3. ARMED after this compile: D2-S38, S16 and D2-W7-S1, all owned by 2.0.0_SA_COO~G2.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W10-S1, D2-W10-S2, D2-W10-S3, D2-W10-S5, D2-W10-S6, D2-W10-S4, D2-S40, S14, D2-S41, D2-S42",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r8/ROUND8_DRAIN_END_READ_20261011.md @a6bd47170b (msg 4448)",
        "this seat's read of org/tier2_senior/0.7.0_AE_CloudOps~YC2/deliverables/irpt_ycdgen_b8/BRAND_LISTING_HOST.txt @12b13a7862 against the repo: the host's brand.json (25ee2179...) and logo (02477c76...) carry the sha256 of the files committed under infra/aws/lambda/investor-reporting/ycharts/research/brand/, hashed by this seat",
        "this seat's read of org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py:58 -- RESEARCH_EXT holds .py, .json, .sh, .md, .cjs and no .svg"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A resolving record, a re-cut whose original row stays open, a stale denial, an amended criterion, and a read row."
  }
]
```
