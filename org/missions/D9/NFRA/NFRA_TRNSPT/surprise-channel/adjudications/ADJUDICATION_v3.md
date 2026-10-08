# NFRA_TRNSPT -- round 5 L8/L9 adjudication

<sweep_watermark>2026-10-08T19:08Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-08 ~19:1xZ. L8 input: `deliverables/2.0.0_SA_COO~T2/R5_CLOSE.md @5ff7717f66`
(addressed to `1.0.0_SA_CTO~DELL2` as msg 1376; relayed to this seat by msg 1451). Round 5 (issuance 904370fa25): TO-TR-a5 and TO-TR-c5
complete, 0 judgment criteria, `round-close-check --round 5` MAY-CLOSE. 1 row dismissed below; undispositioned after this compile:
0 of 39. ARMED: 0.

FWD-1 hop 2 stays open on a person act outside this fabric: loading `TRANSCRIPT_MEETING_ALLOWLIST` on the gateway (msg 1356 to
`0.0.0_AB_MSTR~DELL2` for the NFRA_OPLGTW owner); until then `/hx/transcripts` answers 403 `meeting_not_allowed`.

```json
[
  {
    "id": "NFRA_TRNSPT-C-S8",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T19:08:21Z",
    "one_line": "D2-W2-S1 (the gateway manifest's deployed_commit aa75078e1b is not an object in the repo, so deployed-vs-HEAD could not be compared by git show) is dismissed: amendment 14289f79b2 resolved it by content from the release artifact, SAME-AS-HEAD, with a positive control.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-D2-W2-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "R5_DEPLOYED_ARTIFACT_READ.md: the artifact's app/mail_route.py and HEAD's both hash c7bf6ad9...c3444; 03a23664b4~1's copy differs by 19 lines (the positive control). The live counts-only listing (R5_E2_LIVE_CENSUS.json, 18:06:07Z) shows every span paged to its end: sender#1 13 (2 spans, 1 page each, no token), sender#2 87 (2 spans, 2 pages each, token on page 1, none on the last). The artifact is not the running process's bytes, but the live listing's own paging settles D2-S2's truncation question either way: NOT truncation. D2-S2 stays OPEN (REMEDIATION_v3) and moves to classification: was the 2026-08-11 message outside the has-attachment listing for the table senders, or listed and classed out?",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row NFRA_TRNSPT-D2-W2-S1",
        "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R5_CLOSE.md @5ff7717f66",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R5_DEPLOYED_ARTIFACT_READ.md lines 12-17 and R5_E2_LIVE_CENSUS.json (this seat's read)",
        "426f5751e9, f1e2990e05, 14289f79b2 ancestors of dell2 CLOUD HEAD; round-close-check --round 5 MAY-CLOSE (this compile)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved by content inside the round; the verdict it blocked is written."
  }
]
```
