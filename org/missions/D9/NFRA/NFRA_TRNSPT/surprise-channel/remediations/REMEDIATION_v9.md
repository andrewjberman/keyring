# NFRA_TRNSPT -- round 20 remediations

<sweep_watermark>2026-10-09T11:37Z</sweep_watermark>

Graduated at round 20's L8 (ADJUDICATION_v11.md), round label v21: 4 rows, OPEN.

```json
[
  {
    "id": "NFRA_TRNSPT-D2-S11",
    "project": "NFRA_TRNSPT",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The headless /hx/transcripts route refuses ALL 4 allowlisted meetings with 403 meeting_not_allowed for the stored bearer, so the pull TO-APPLY-p18 creates will see 4 and land 0 on its invoke and on every scheduled fire until the gateway HOST's own allowlist carries those 4 meeting ids.",
    "evidence": [
      "investigation row NFRA_TRNSPT-D2-S11",
      "GatewayTransport(secrets_reader=gateway_client.read_bearer).list_meeting_transcripts over all 4 rows of meeting_allowlist.load() (denominator printed, 4 of 4 probed): allowed=0 refused_403=4 other=0; every one status=403 error=meeting_not_allowed, for monday_meeting, ocio_ic, asset_management_ic and research_meeting"
    ],
    "remedy": "Site Z's env-only release puts the 4 meeting ids on the gateway host's allowlist (ruling @261e2c42a0); the pull then lands them (expect 3 of 4).",
    "owner": "0.0.0_AB_MSTR~DELL2 (cross-fabric to site Z, msg 3189)",
    "round": "v21",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "0.0.0_AB_MSTR~DELL2 (cross-fabric to site Z, msg 3189)",
      "round": "v21"
    },
    "closed": true
  },
  {
    "id": "NFRA_TRNSPT-D2-W2-S6",
    "project": "NFRA_TRNSPT",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The /hx/transcripts contract returns the transcript body only; the pull's fmt 'metadata' read (pull.py:98) has no route, so GatewayTransport raises GatewayFormatUnsupported for it and a live pull cannot yet land a meeting.",
    "evidence": [
      "investigation row NFRA_TRNSPT-D2-W2-S6",
      "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/HX_TRANSCRIPTS_ROUTE_CONTRACT_COPY_f67fbc2390.md: two GET paths only; the single-transcript answer is {meeting_id, transcript_id, createdDateTime, endDateTime, content, byte_count, sha256}"
    ],
    "remedy": "The /hx/transcripts metadata route at site Z (ruling @7f58eb8f77), or derive the metadata from the list row's start and end times; until then wallclock_basis reads 'absent'.",
    "owner": "0.0.0_AB_MSTR~DELL2 (site Z)",
    "round": "v21",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~DELL2 (site Z)",
      "round": "v21"
    },
    "closed": false
  },
  {
    "id": "NFRA_TRNSPT-D2-W2-S8",
    "project": "NFRA_TRNSPT",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "land_bronze.land cannot land a transcript with no metadata object, so pull.py carries its own content-only lander (_land_content_only); thread_trace.hop_land_probe will KeyError on such a sidecar (it reads sidecar['metadata_content']['object']).",
    "evidence": [
      "investigation row NFRA_TRNSPT-D2-W2-S8",
      "data/transcripts/scripts/teams/land_bronze.py:101,126 hashes metadata_bytes and always puts the .metadata.vtt key; land_bronze.py is outside <paths>"
    ],
    "remedy": "thread_trace.hop_land_probe reads a content-only sidecar without a metadata object (no KeyError), so the trace covers meetings landed by _land_content_only.",
    "owner": "2.0.0_SA_COO~T2",
    "round": "v21",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~T2",
      "round": "v21"
    },
    "closed": false
  },
  {
    "id": "NFRA_TRNSPT-D2-S12",
    "project": "NFRA_TRNSPT",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "NONE of the transcripts root's Lambdas carries a lambda-source-map.json entry (0 of 232 entries name one), and the root has never been tagged (0 transcripts-v* tags), so deployment rules 4 and 6 are unmet for the function TO-APPLY-p18 just created and for the three that predate it.",
    "evidence": [
      "investigation row NFRA_TRNSPT-D2-S12",
      "infra/aws/lambda/ci/lambda-source-map.json: functions enumerated, DENOMINATOR 232 entries, transcripts-bearing entries = 0 -- teams-global-transcripts-pull-lambda (created at this apply), outlook-global-transcripts-pull-lambda, the commentary Lambda and the chat-assist Lambda are all absent"
    ],
    "remedy": "Register the transcripts root's Lambdas in lambda-source-map.json and tag the root (transcripts-v*), per deployment rules 4 and 6.",
    "owner": "2.0.0_SA_COO~T2",
    "round": "v21",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~T2",
      "round": "v21"
    },
    "closed": true
  }
]
```
