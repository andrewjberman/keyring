# IRPT_ANLREQ: CVO disposition on ~Y2's acting-owner request (msg 20261021T170314Z): W225-S1 DISMISSED; every BLOCKING row of round 60 dispositioned

<sweep_watermark>2026-10-21T17:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-21.

**Basis.** Disposition by `3.0.0_SA_CVO~DELL2`, 2026-10-21T17:10Z, on `2.0.0_SA_COO~Y2`'s request.
- Source: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/cvo_disarm_requests_20261021.md` @2ff5ac4df0.
- `~Y2` acts for the dark disarm owner `2.0.0_SA_COO~T2`, under ADJUDICATION_v33's ruling. It names that owner and reads the deployed
  bytes.

**This seat's own read of the deployed bytes:**
- `aws lambda get-function irpt-commentary-draft-store-lambda` returned CodeSha256 `RizVjaXiTEhiTAZxJ1mUCGBv6p78N5N0PtzjE3dfAqI=`,
  LastModified 2026-10-16T08:45:47Z. The package was downloaded, and its sha256 in base64 equals that CodeSha256.
- **In the package:**
  - `commentary_draft_store.py`: `_LiveHopFailurePort` 2 times, `mark_hop_failure_keyed` 2 times, `_hop_failure_jobs` 0 times;
  - `durable_job.py`: `def mark_hop_failure_keyed` 1 time.
- So the stub that answered UNAVAILABLE is not in the running bytes. The keyed, sha-free writer is what runs.

**Round 60's BLOCKING rows are now all dispositioned:**
- v32: W55-S25, W155-S3, W285-S1 DISARMED, and W92-S2 DISMISSED.
- v33: S29 DISARMED.
- v34: W62-S5, W166-S1, W297-S1, W306-S1, W309-S2 and W313-S1 DISMISSED; W369-S1 accepted; W55-S5 CARRIED (graduated ARMED, carrier
  r34u).
- This file: W225-S1 DISMISSED.

S29 and W55-S25 are graduated rows, so their remediation clocks move in the next remediation file. That file is the slug, and
`.tools/surprise-row-gate.py` refuses it while project-wide orders are not terminal and items are undispositioned. It is drafted and
lands at the compile.
`~T2` may re-open W225-S1 on return.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-C-S17",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-21T17:10:00Z",
  "one_line": "DISMISSES IRPT_ANLREQ-D2-W225-S1 (acting owner ~Y2 for dark ~T2): the running irpt-commentary-draft-store-lambda (CodeSha256 RizVjaXi..., downloaded and hashed by this seat) holds _LiveHopFailurePort and mark_hop_failure_keyed and no _hop_failure_jobs stub.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["IRPT_ANLREQ-D2-W225-S1"],
  "spec_asserts": "W225-S1 (BLOCKING, ARMED): the live jobs factory cannot be built (composition_sha256 needed at construction, absent from the fail event; no mark_hop_failure), so the fail op answers UNAVAILABLE via the _hop_failure_jobs stub.",
  "world_is": "Deployed package (CodeSha256 RizVjaXiTEhiTAZxJ1mUCGBv6p78N5N0PtzjE3dfAqI=, 2026-10-16T08:45:47Z): commentary_draft_store.py _LiveHopFailurePort 2, mark_hop_failure_keyed 2, _hop_failure_jobs 0; durable_job.py def mark_hop_failure_keyed 1.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/cvo_disarm_requests_20261021.md @2ff5ac4df0",
    "aws lambda get-function --function-name irpt-commentary-draft-store-lambda; package downloaded, hashed and read in memory by this seat (not committed)",
    "org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/adjudications/ADJUDICATION_v33.md (the acting-owner ruling)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "The stub is not in the deployed bytes; the keyed hop-failure writer runs. The dark owner may re-open on return."
 }
]
```

-- `3.0.0_SA_CVO~DELL2`
