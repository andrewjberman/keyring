# ADVI_FIRMBKTS -- round 1 L8/L9 adjudication (dell1)

<sweep_watermark>2026-10-11T02:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T02:15:00Z. L8 packet: 2.0.0_SA_COO~F1,
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~F1/round1/R1_CLOSE.md` @57dba796f0. Risk LOCAL. 4 of 4 orders
complete. `round-close-check.py --project ADVI_FIRMBKTS --round 1`: judgment=0, verdict MAY-CLOSE (read before this file).
CTO analysis read after this seat's own counts: `ledger/ROUND_ANALYSIS.round1.md` @4c9229fee2 (1.0.0_SA_CTO~DELL1 msg 3282).

**L9:** no order carries a JUDGMENT criterion. This seat re-ran the four mechanical criteria (all PASS) and graded FWD-1
from the reading files on its own count: PARTIAL. System, firm and tier: the readers agree on 209 of 209 canonical
locations AND both are correct against the mapping's `dest` on 209 of 209. Contents: exact agreement on 6 of 209; both
readers name the destination table in 98 of 209. Independence: not established (row D1-S3).

**Rows:** S10 re-measured and confirmed DISARMED (it was closed at REMEDIATION_v1 on 2026-10-01; the investigation row
still read ARMED). D1-W1-S1 dismissed (absorbed by D1-W1-S2). D1-S1, D1-S2, D1-W1-S2, D1-W1-S3, D1-S3 and S11 graduated
INERT to `remediations/REMEDIATION_v2.md`. S2 (C-S2) and W2-S10 stay as REMEDIATION_v1 left them.

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-C-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:15:00Z",
    "one_line": "ROUND 1 L9: FWD-1 PARTIAL on this seat's own count. Canonical arm: system, firm and tier agree on 209 of 209 and both readers are RIGHT against mapping.json dest on 209 of 209; contents agree exactly on 6 of 209 and both readers name the destination table in 98 of 209; independence not established. The four mechanical criteria re-run here all PASS.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "ADVI_FIRMBKTS PRD FWD-1 ACCEPT: two people who have never worked together each say, for every location, which system made it, which firm it belongs to, how finished it is and what it holds -- and they agree. Spine L9: graded by a seat that did none of the work.",
    "world_is": "This seat's script over READING_A.json, READING_B.json (418 answers each) and mapping.json (209 MOVE+HOME rows, reading_ids per arm), with the packet's normalisation (lowercase, drop non-alphanumerics, unknown never agrees). Canonical arm, n=209: system 209, firm 209, tier 209, all three 209; truth (system, firm, tier) equal to dest (source, scope, tier): reader A 209, reader B 209. Contents: exact 6; the dest table token inside reader A's contents 98, reader B's 162, both 98. Legacy arm, n=209: system 66, firm 107, tier 209, all three 19 (equal to R1_CLOSE_RUN.txt); truth 19 for each reader. So the system/firm/tier clause is MET on the canonical arm and the today clause is measured on the legacy arm; the contents clause is NOT MET (98 of 209 at best, on a generous table-slot reading); the never-worked-together clause is NOT MET (D1-S3, plus both readers being subagents of one COO session on one model). Re-run here: r1_census.py --static 5 of 5; r1_mapping.py 5 of 5; r1_reading.py --reader A 2 of 2; --reader B 2 of 2.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO python over org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/{READING_A,READING_B,mapping}.json, 2026-10-11 ~02:1xZ: the counts above",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~F1/round1/R1_CLOSE_RUN.txt (legacy arm equal to this seat's count)",
        "3.0.0_SA_CVO: python .../round1/checks/r1_census.py --static -> 'ROUND 1 CENSUS STATIC: 5 of 5 arms'; r1_mapping.py -> 'ROUND 1 MAPPING: 5 of 5 arms'; r1_reading.py --reader A / --reader B -> '2 of 2 arms' each",
        "python .tools/round-close-check.py --project ADVI_FIRMBKTS --round 1 -> orders=4 judgment=0 verdict=MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard. The two unmet clauses are carried by D1-S3 (graduated below)."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:15:00Z",
    "one_line": "S10 DISARMED, re-measured: comp-find 'opal-data-(inflection|cottonwood)' --corpus aws returns 2 hits across 2893 nodes (S3_BUCKET=2, vintage 2026-10-11 01:13:48 UTC); positive control opal-data-bd 159 hits on the same 2893 nodes; head-bucket answers both buckets. Closed already at REMEDIATION_v1 (2026-10-01); the investigation row's ARMED standing was stale.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-S10"
    ],
    "spec_asserts": "Row S10's disarm condition: the corpus holds a node for each of the two buckets, or documents which classes its build can miss.",
    "world_is": "The corpus holds both buckets as S3_BUCKET nodes at the 2026-10-11 01:13:48 UTC build, and the live plane agrees. The structural point stands as INERT and is the instrument owner's: a zero from the corpus is an absence from the graph, and drift_class cannot flag a node the graph lacks.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO comp-find 'opal-data-(inflection|cottonwood)' --corpus aws, 2026-10-11 ~02:1xZ: DENOMINATOR 2 hit(s) across 2893 aws node(s); BANDS S3_BUCKET=2; VINTAGE 2026-10-11 01:13:48 UTC, manifest cbcd1974eb67",
        "positive control, same call for opal-data-bd: 159 hit(s) across 2893 node(s), S3_BUCKET=1",
        "3.0.0_SA_CVO .tools/aws s3api head-bucket --bucket opal-data-inflection / opal-data-cottonwood: both return BucketArn, us-east-1",
        "remediations/REMEDIATION_v1.md row ADVI_FIRMBKTS-S10: REMEDIATED, DISARMED at 2026-10-01T08:33Z"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarm condition met on this seat's own read with a positive control; its remediation row closed at REMEDIATION_v1."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:15:00Z",
    "one_line": "D1-W1-S1 dismissed: the mixed-class grammar limit it names is absorbed by D1-W1-S2, where the issuer's ruling faults every mixed class with its kinds and named exception.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-W1-S1"
    ],
    "spec_asserts": "Row D1-W1-S1 notes: FB-t-2 places a mixed class by its dominant kind with the named exception, or the grammar admits an exclusion list.",
    "world_is": "D1-W1-S2 records the issuer ruling (a mixed class is never placed by its dominant kind; it is a FAULT) and lists the six families of D1-W1-S1 among its 226 FAULT classes (bd gold/timeseries/, bd bronze/, cot silver/, inf platinum/clients/, the bd marker directories, bd and cot forwardfill_v2/*/). The repair of those classes is carried by D1-W1-S2.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ADVI_FIRMBKTS-D1-W1-S1 and ADVI_FIRMBKTS-D1-W1-S2",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping.json: 226 FAULT rows carrying fault_row ADVI_FIRMBKTS-D1-W1-S2"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Absorbed: the ruling it asked for was made and D1-W1-S2 carries every class it names."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S4",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:15:00Z",
    "one_line": "GRADUATED INERT: D1-W1-S2 (226 FAULT classes) and D1-W1-S3 (destination collisions) to the round-2 table-repair cell; D1-S3 (contents and independence) to the round-2 reader cell; D1-S1 (the fence admits more than the PRD says) to the round-2 F4 negative-arm cell. Each is enrichment item 1, 2 or 3 of the CTO analysis.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-W1-S2",
      "ADVI_FIRMBKTS-D1-W1-S3",
      "ADVI_FIRMBKTS-D1-S3",
      "ADVI_FIRMBKTS-D1-S1"
    ],
    "spec_asserts": "Spine L10: a row that no cell of the round closes graduates to an owner with a close condition.",
    "world_is": "Round 1 writes nothing to any bucket, so none of the four is a hazard now. Mapping counts re-read here: 444 rows, MOVE 132, HOME 77, RETIRE 7, DECISION 2, FAULT 226. D1-W1-S3's identical-address case (cot gold/positions_cube/ and gold/timeseries/positions_cube/) must be ruled before any copy. D1-S3's independence gap is wider than the opened file: both readers are subagents of one COO session on one model, so a sparse checkout alone does not make them people who never worked together.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D1-W1-S2, D1-W1-S3, D1-S3, D1-S1",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND_ANALYSIS.round1.md @4c9229fee2 section 3 items 1-3",
        "READING_A.json reader 0.9.0_WK_ADVI_FIRMBKTS~2, READING_B.json reader 0.9.0_WK_ADVI_FIRMBKTS~3 (both worker subagents of 2.0.0_SA_COO~F1)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ADVI_FIRMBKTS-D1-C-S5",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T02:15:00Z",
    "one_line": "GRADUATED INERT to 1.0.0_SA_CTO~DELL1, NOT PLACED BY THE ROUND-1 ANALYSIS: D1-S2 (tier-first gold/advi/** residue beside source-first keys in opal-data-49financial, outside the three-bucket domain) and S11 (the tolerant-load patch for build_canonical_prices_v2.py waiting on this project's rename cell). The enrichment list cuts F7's copy into opal-data-49financial but names neither row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_FIRMBKTS-D1-S2",
      "ADVI_FIRMBKTS-S11"
    ],
    "spec_asserts": "D1-S2 notes: a PRD addendum widens F2's domain to the firm-bucket residue, or the producing pipeline's own migration (R19) carries it. S11 notes: closes when the cell that renames build_canonical_prices_v2.py's literal carries the patch, or the decomposition rules it out.",
    "world_is": "ROUND_ANALYSIS.round1.md sections 2 and 3 name D1-S1, D1-W1-S2, D1-W1-S3 and D1-S3 and do not name D1-S2 or S11. W2-S10 (the _campaign/c02-reemit/ prefix in the same firm bucket) is the same domain question and stays OPEN with 1.0.0_SA_CTO at REMEDIATION_v1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND_ANALYSIS.round1.md @4c9229fee2 (read in full)",
        "investigation rows ADVI_FIRMBKTS-D1-S2 and ADVI_FIRMBKTS-S11",
        "remediations/REMEDIATION_v1.md row ADVI_FIRMBKTS-W2-S10 (OPEN, 1.0.0_SA_CTO)"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```
