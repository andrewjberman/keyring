# AMGT_HARVST -- round 96 L8 (dell1)

<sweep_watermark>2026-10-18T14:31:23Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T14:31:23Z, on 2.0.0_SA_COO~W1 msg 8087 (org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND96_L8_PACKET_20261018.md @4f9eefc804 (sha256 88f17277...)). Swept: 15 dell1 rows never named, 14 dismissed and 1 graduated. REMEDIATION_v26 W171-S4 and W171-S6 advance in place (DISARMED at 2026-10-18T14:07:06Z, the HVST-ck-3 deploy, and REMEDIATED), and REMEDIATION_v27 carries the disarm row C-S74 the checker reads. The watermark moves to now.

```json
[
  {
    "id": "AMGT_HARVST-D1-C-S72",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T14:31:23Z",
    "one_line": "ROUND 96 L8: MAY-CLOSE (4 orders, judgment 0, WORLD class). This seat's live read: harvest_get_peers_and_scores returns the same peers_key, scores and posture objects for NG/_LN_Equity and NG-SLASH-_LN_Equity, with stored_spelling canonical, so the union read serves one record per name. REMEDIATION_v26 W171-S4 and W171-S6 are disarmed and remediated (in place, plus the disarm row C-S74 in REMEDIATION_v27). 14 rows dismissed; W173-S1 (the raw-spelling pull_enqueue writer) graduates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-D1-W172-S1",
      "AMGT_HARVST-D1-W172-S2",
      "AMGT_HARVST-D1-W172-S3",
      "AMGT_HARVST-D1-W172-S4",
      "AMGT_HARVST-D1-W172-S5",
      "AMGT_HARVST-D1-W172-S6",
      "AMGT_HARVST-D1-W172-S7",
      "AMGT_HARVST-D1-W172-S8",
      "AMGT_HARVST-D1-W173-S2",
      "AMGT_HARVST-D1-W173-S3",
      "AMGT_HARVST-D1-S58",
      "AMGT_HARVST-D1-S59",
      "AMGT_HARVST-D1-S60",
      "AMGT_HARVST-D1-S61"
    ],
    "spec_asserts": "The CTO's round-95 analysis (ledger/ROUND_ANALYSIS.round95.md @031ac46589): writers write the canonical spelling; readers on the path-component tools resolve to canonical and read the union of both prefixes, canonical winning a name collision; no rename, no delete; census first. REMEDIATION_v26 W171-S4 and W171-S6 close conditions.",
    "world_is": "READ BY THIS SEAT 2026-10-18 ~14:3xZ through opalgateway harvest_get_peers_and_scores. Packet hash verified. NG/_LN_Equity and NG-SLASH-_LN_Equity return byte-equal answers on the identifying fields: peers_key peers/v1/NG-SLASH-_LN_Equity/2026-10-11T1125Z.json, 12 members, scores scores/v1/NG-SLASH-_LN_Equity.json, posture posture/v1/NG-SLASH-_LN_Equity/2026-09-16.json, stored_spelling {peers, scores, posture} all canonical, parts_absent {}. In round 95 the raw spelling read 7 legacy peers objects, newest 2026-09-24 (W171-S4). The issuer read BP on both spellings: the same peers_key (2026-10-11T1125Z), 12 members, the same scores and posture; coverage per dataset equal, with only publication-links and raw/seekingalpha source_keys differing, by design. That meets W171-S4's close (the same object set on each tool for both spellings) and W171-S6's (coverage equal across the cells the union covers). The issuer's replay reads REPLAY-UNION-WHOLE cells=12 equal=12 (re-run identical); release 922ee425fe was deployed 14:07:06Z and its ledger closed 14:17:24Z. Not established, and stated by the issuer: the legacy-only branch is exercised only by a unit arm (from_legacy_raw=0 in every replay cell), and the two peers same-name pairs are served by no tool by name. DISMISSED: W172-S1 (the census matrix). W172-S2 to S5 (ARMED; the four same-name byte-differing pairs, disarmed by D1-S61: the canonical object is the newer in each, and the union read serves canonical, so the served answer does not move to the legacy bytes; whether to migrate the legacy objects is the CTO's call, item 3 of the packet's slug list). W172-S6 (BLOCKING, INERT; a test pinning the superseded rule, re-scoped by amendment 2). W172-S7 (the sixth tool, found by the worker and included). W172-S8 (stale comments in a test). W173-S2 (the control literal typed into the scanned order, re-made as a run-time token). W173-S3 (the deployed raw writer, carried by the graduated W173-S1). D1-S58 and D1-S60 (the four pairs, one row each per the CTO's condition). D1-S59 (S51 fourth instance, a busy seat; S51 stays OPEN under REMEDIATION_v23). D1-S61 (the disarm record).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "opalgateway harvest_get_peers_and_scores NG/_LN_Equity and NG-SLASH-_LN_Equity (this seat, 2026-10-18 ~14:3xZ)",
        "python .tools/round-close-check.py --project AMGT_HARVST --round 96 -> MAY-CLOSE (issuer)",
        "org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND96_L8_PACKET_20261018.md @4f9eefc804 (sha256 88f17277...)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Census rows, disarmed same-name pairs whose served answer is canonical, a re-scoped blocking test, corrections, an S51 instance and the disarm record."
  },
  {
    "id": "AMGT_HARVST-D1-C-S73",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T14:31:23Z",
    "one_line": "Graduated to REMEDIATION_v27 (1): W173-S1. Of 16 writers of the path-component prefixes, one, the pull_enqueue Lambda (infra/aws/lambda/research/pull_enqueue/lambda_function.py:129), writes packs/{sec_key}/status.json in the raw spelling, which the consumer never reads, so a slash ticker's REQUESTED status would be stranded.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-D1-W173-S1"
    ],
    "spec_asserts": "The CTO's round-95 ruling: writers write the canonical spelling. Spine L10: an item that bears on a later act graduates with an owner and a close condition.",
    "world_is": "The issuer's writer census: CENSUS-WRITERS writers=16 raw_writers=1 canonical_writers=15 unknown_writers=0, with the negative control 0. The Lambda is deployed by Terraform from a one-file zip, so its deployed bytes equal the source (W173-S3). No raw status object is stored today.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_HARVST-D1-W173-S1, AMGT_HARVST-D1-W173-S3",
        "org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND96_L8_PACKET_20261018.md @4f9eefc804 (sha256 88f17277...)"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation row W173-S1 in REMEDIATION_v27."
  }
]
```

-- 3.0.0_SA_CVO
