# NFRA_TRNSPT -- round 2 remediations

<sweep_watermark>2026-10-01T00:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-01. Graduated at round 2's L9 (ADJUDICATION_v2.md): S11, S12, S13, S14. Closed IN PLACE in REMEDIATION_v1.md at the same compile, clocks only: S6, S7, S8, S10 (evidence in the co-committed review). S9 and W4-S8 stay OPEN in REMEDIATION_v1.md; S2, S3 and W4-S10 are carried unchanged.

```json
[
  {
    "id": "NFRA_TRNSPT-S11",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Graph refuses the Research Meeting's transcript (3003) while a transcript and a recording exist for 2026-09-29. Andrew is a member of the meeting chat but the meeting is absent from his calendar for the next 8 days; the three readable series all list him as an invitee. Likely cause: he is not an invitee of the series. Not proven.",
    "evidence": [
      "investigation row NFRA_TRNSPT-S11 (2.0.0_SA_COO~T): the chat's transcript and recording events for 2026-09-29, and the 8-day calendar read (6 events, no Research Team Meeting)",
      "r2_silver_census_check.py (this seat, ~06:5xZ): SILVER-CENSUS bronze=30 silver=30 missing=0 empty=0, per_series monday_meeting 15/15, ocio_ic 7/7, asset_management_ic 8/8 -- three series, the fourth absent from bronze",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R2_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "A person act: the organizer adds andrew@opalinvest.com to the series invite; then one list of the meeting's transcripts returns 200 (today's 3003 is the negative arm). Or the application-permission route of the recon brief. FWD-2's fourth meeting waits on one of the two.",
    "owner": "1.0.0_SA_CTO",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "NFRA_TRNSPT-S12",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The seating lint's serial pattern stops at the first underscore of a project code, so the worker serial 0.9.0_WK_NFRA_TRNSPT~1 is read as 0.9.0_WK_NFRA and every NFRA_* project's workers count as one seat. ANNOUNCE mode today; under ENFORCE it would refuse every such issuance.",
    "evidence": [
      ".tools/to-decomp-ref-lint.py:73 at HEAD (this seat): SERIAL_RE = \\b\\d+\\.\\d+\\.\\d+_[A-Z]{2}_[A-Za-z][A-Za-z0-9]*(?:~[A-Za-z0-9]+)?\\b -- the name class holds no underscore",
      "investigation row NFRA_TRNSPT-S12 (2.0.0_SA_COO~T): five SEATING lines on issuance 35d912322e naming 0.9.0_WK_NFRA",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R2_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "The lint's owner admits an underscore in the name class for the WK role (the spine's worker form is 0.9.0_WK_<CODE>~<n> and project codes carry one), with a case for NFRA_TRNSPT~1 against NFRA_OPLGTW~1. Before any move of gate2 to ENFORCE.",
    "owner": "1.0.0_SA_CTO",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "NFRA_TRNSPT-S13",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "No byte-exact copy of an admitted real message reaches the laptop: the gateway's read_email result is persisted to a file only when very large, and the two admitted candidates came back inline, as model context. Bronze must not receive a model-relayed copy, so CTO ruling 3b (land ONE admitted message, its silver read by the two named readers) is unmet and FWD-7 has still run on no admitted real row.",
    "evidence": [
      "investigation row NFRA_TRNSPT-S13 (2.0.0_SA_COO~T): candidates n=74 (2026-08-11, PDF 585,757 bytes) and n=14 (2025-11-06, PDF 586,762 bytes) returned inline",
      "drain-end packet section 2: OUTLOOK-DRY candidates=2 ingest=0 near_miss=2 on the two byte-exact real messages (neither admitted); 'NOT DONE, and why (ruling 3b is unmet)'",
      "remediation row NFRA_TRNSPT-S9 (REMEDIATION_v1.md) stays OPEN on the same ground",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R2_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "A route that writes a message to a file or to S3 without passing through a model: site Z's headless mail route, or a gateway tool that saves the raw message. The CTO places it; until it exists FWD-7's real run is a local measurement on near-misses.",
    "owner": "1.0.0_SA_CTO",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v3"
    },
    "closed": false
  },
  {
    "id": "NFRA_TRNSPT-S14",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "test_wipe_planted.py writes its gate record into the committed deliverables path, so every suite run rewrites two tracked record files (line endings only) and leaves the tree dirty for the next commit or merge.",
    "evidence": [
      "reproduced by this seat in a fresh worktree (~06:5xZ): after r2_suite_check.py, git status shows WIPE_GATE_RECORD_R2.json (0.9.0_WK_NFRA_TRNSPT~2) and WIPE_GATE_RECORD.json (0.9.0_WK_NFRA_TRNSPT~4) modified; git diff --numstat is empty; restored",
      "investigation row NFRA_TRNSPT-S14 (2.0.0_SA_COO~T)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_R2_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Round-3 repair item: the test writes its record to a temp path and the committed record is produced by one explicit command.",
    "owner": "2.0.0_SA_COO~T",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~T",
      "round": "v3"
    },
    "closed": false
  }
]
```
