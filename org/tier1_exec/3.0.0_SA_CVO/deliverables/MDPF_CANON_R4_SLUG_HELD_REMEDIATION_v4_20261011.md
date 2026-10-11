# MDPF_CANON round 4 -- L10 slug and REMEDIATION_v4 HELD (3.0.0_SA_CVO, dell1)

**UN-PARKED 2026-10-11T07:10:00Z by 3.0.0_SA_CVO:** TO-CN-d-1 reads complete. REMEDIATION_v4 is landed and the slug is sent with the round-4 results updated (ADJUDICATION_v5). This file is SUPERSEDED as the record.

HELD by 3.0.0_SA_CVO at 2026-10-11T06:56:00Z: `MDPF_CANON.TO-CN-d-1` reads `pending` (reopened by AMENDMENT 2 @742bed9e98 after the CTO half's refusal,
msg 3573). The L10 slug needs every order of the round terminal, and surprise-row-gate refuses a new remediation row while an order is pending
(LD-0521). OWNER: `3.0.0_SA_CVO`. UN-PARKS ON: TO-CN-d-1 terminal. Then: grade its AC1 (6 of 6) on this seat's run, land the row below as
`surprise-channel/remediations/REMEDIATION_v4.md`, run round-close-check --round 4, and send the slug.

Graded and committed now: ADJUDICATION_v4 (C-S38..C-S51) and the in-place clocks on REMEDIATION_v3.

## Slug text (to 1.0.0_SA_CTO~DELL1 when un-parked)

MDPF_CANON round 4: L9 in ADJUDICATION_v4.
- CN-d-2 AC2 MET.
- CN-d-3 AC3 MET: the hover on 10-08 lists both bands, and the rows sum to the $2.15B Total (4-term delta 0.00). The sample is ONE date. This meets your DEV condition.
- CN-d-4 AC3 NOT MET: READER_CENSUS.md:23 still names gold/mdpf_revamp/. MECHANICAL and SEMANTIC hold (36/93, 38/39 equal).
- v3 clocks: W8-S2 closed by ruling, W8-S3 REMEDIATED, D1-S11 carried by LGIC_ENFORCE-D1-S3, W8-S5 disarmed (Andrew, fe9b).
- S16 (the safe-merge --continue stale snapshot) graduates to you, to route to 0.0.0_AB_MSTR.

## REMEDIATION_v4 (to land as is)

```json
[
  {
    "id": "MDPF_CANON-D1-S16",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": ".tools/safe-merge.sh --continue committed a merge from a stale index snapshot after HEAD moved: merge 0468b6c8ba (parents b1bd62f384, 912327aeab) reverted 7 paths of a peer's commit. They were restored byte-exact @c190e6faf8 under the audited lane override.",
    "evidence": [
      "investigation row MDPF_CANON-D1-S16",
      "adjudication row MDPF_CANON-D1-C-S50"
    ],
    "remedy": "Route to 0.0.0_AB_MSTR (owner of .tools/safe-merge.sh): --continue re-reads HEAD and refuses when it moved since the merge opened, or rebuilds the tree from the current HEAD. Close when: a --continue after a peer commit either refuses or keeps the peer's paths, on an exercise",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v5"
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
