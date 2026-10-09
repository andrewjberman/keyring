# DSGN_AMGTV1 -- backlog remediations (dell1)

<sweep_watermark>2026-10-09T10:16Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T10:16:00Z. Graduated at ADJUDICATION_v35: 5 rows, all INERT.

```json
[
  {
    "id": "DSGN_AMGTV1-Z-W87-S1",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AV-zh-2: two shared definitions the order's build needs sit outside its <paths> -- types.ts types CoverageItem.url as `string` (the served overlay now carries null) and constants.ts holds HEADER_FEED_VISIBLE_COUNT = 3 (the order wants at most 2 open news items at rest); the build handled both inside HeaderBrief.tsx.",
    "evidence": [
      "investigation row DSGN_AMGTV1-Z-W87-S1"
    ],
    "remedy": "Fold the shared contract: types.ts CoverageItem.url becomes nullable and constants.ts HEADER_FEED_VISIBLE_COUNT matches the drawn count (still 3 in constants.ts at dell1 portal HEAD; HeaderBrief takes a local 2). Close when: both shared definitions state what the page does",
    "owner": "2.0.0_SA_COO~D1",
    "round": "v62",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D1",
      "round": "v62"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "DSGN_AMGTV1-Z-S21",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Re-owned from AMGT_RESAPP-Z-W173-S3 (2.0.0_SA_COO~Z msg 30368, ruling round76 section F @fb9ca91ad5): a SERVED model case on the Security Analysis page carries no value or currency data attribute, so a reader keys a served case on name and formula only.",
    "evidence": [
      "investigation row DSGN_AMGTV1-Z-S21"
    ],
    "remedy": "A served model case carries value and currency data attributes so a reader keys it on served figures, once AMGT_CORPUS's ModelTab work is on DEV. Close when: the attributes are drawn and a check reads them",
    "owner": "2.0.0_SA_COO~D1",
    "round": "v62",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D1",
      "round": "v62"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "DSGN_AMGTV1-Z-W97-S1",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "AV-zn-1: with the fixture replaced by the served WINDOWED chatter shape, the Universe state's sizes and radii clauses now FAIL (the monthly fixture drew no bubbles, so they never read the bubble labels); the run tally is 74 PASS / 2 FAIL, not all-PASS.",
    "evidence": [
      "investigation row DSGN_AMGTV1-Z-W97-S1"
    ],
    "remedy": "Re-read the Universe-state design cells (bubble labels 8/9/10 px, radii 2/5 px) against the design law on the current ChatterBubbles.tsx; fix or rule them in-law. Close when: the design check reads all PASS on the Universe state, or the cells are ruled",
    "owner": "2.0.0_SA_COO~D1",
    "round": "v62",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D1",
      "round": "v62"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "DSGN_AMGTV1-Z-S22",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A conflicted drain finished with safe-merge.sh --continue committed ONLY the resolved surprise channel: merge f953449753 left the branch's other 3 files (proof instance, render, the order's status flip) out of the commit, intact but unstaged in the shared working tree.",
    "evidence": [
      "investigation row DSGN_AMGTV1-Z-S22"
    ],
    "remedy": "Examine safe-merge.sh --continue: a conflicted drain committed 1 of 4 files and exited 0. Make --continue verify every merge path is in the commit, or refuse. Close when: a conflicted test drain with N files commits N or exits non-zero",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v62",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v62"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "DSGN_AMGTV1-D1-S1",
    "project": "DSGN_AMGTV1",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two round-61 workers (~131, ~133) report that the to-pipeline-gate refuses a MODIFIED task order written with CRLF line endings for lacking a line-anchored <placeholders> element, so the status flip leaves the order LF (a whole-file diff).",
    "evidence": [
      "investigation row DSGN_AMGTV1-D1-S1"
    ],
    "remedy": "to-pipeline-gate's line-anchored <placeholders> read refuses a MODIFIED CRLF order (a newly added CRLF order passes). Read CRLF the same as LF, or the issuer cuts LF. Close when: a CRLF order's status flip passes the gate",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v62",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v62"
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
