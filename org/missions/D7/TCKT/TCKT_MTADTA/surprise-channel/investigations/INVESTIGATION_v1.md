# TCKT_MTADTA -- surprise channel, INVESTIGATION v1 (round 1, dell1 fabric)

**Opened by:** `1.0.0_SA_CTO~DELL1` at L4 (seat rows; the CVO assembles from L8, spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`). The gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`). Lane `ANY`.
**Id grammar:**
- a worker's row is `TCKT_MTADTA-D1-W<n>-S<k>`;
- a seat's row is `TCKT_MTADTA-D1-S<k>` (dell1 coordinate);
- the CVO's adjudication rows live in `../adjudications/`.

**Append-only during the round.** Never edit an existing row.

```json
[
  {
    "id": "TCKT_MTADTA-D1-S1",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "surfaced_by": "1.0.0_SA_CTO~DELL1",
    "surfaced_at": "2026-10-16T06:38:00Z",
    "one_line": "The safe-commit PRD manifest gate refused PRD v0.2 with 'no top-level ENDPOINT section' when the file's only defect was CRLF line endings, while a direct run of the same gate on the working file passed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "0.0.0_AB_MSTR~DELL1 (infrastructure: .tools/safe-commit.sh and .tools/prd-manifest-gate.py); this seat only surfaces",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit of org/missions/D7/TCKT/TCKT_MTADTA/prd/TCKT_MTADTA_PRD.md (v0.2 edit) twice: 'ERROR: BLOCKED -- step-4 PRD surface-manifest gate ... no top-level ENDPOINT section the L6 matcher can resolve'",
        "python .tools/prd-manifest-gate.py <same path>, same minute: '[prd-manifest] OK: 1 step-4 PRD document(s) carry their key surfaces'",
        "byte read of the file: CR count 309 (the v0.1 blob @315f7a19af: 0); after converting to LF the commit landed @86f3caec3a"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A gate refusal names the defect it found, and the same gate gives the same verdict on the same bytes whoever runs it.",
    "world_is": "The refusal named a missing heading that was present. The real defect, CRLF line endings from a Python text-mode write on Windows, was named nowhere. The direct run and the commit-time run disagreed.",
    "notes": "The cause of the disagreement was not read: the commit-time run may see the staged blob and the direct run the working file. The fix belongs to the gate's owner: name CRLF in the refusal, or normalise before matching. Nothing was edited here."
  }
]
```
