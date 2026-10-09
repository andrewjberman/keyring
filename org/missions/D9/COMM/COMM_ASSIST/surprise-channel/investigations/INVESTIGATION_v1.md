# COMM_ASSIST -- surprise channel, INVESTIGATION v1 (laptop fabric)

**Opened by:** `2.0.0_SA_COO~R`, 2026-10-08, on `1.0.0_SA_CTO` msg 107481. **Home:** the project tree's channel; the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`). Lane
`ANY`. A seat's row is `COMM_ASSIST-S<k>`; a worker's is `COMM_ASSIST-W<n>-S<k>`. **Append-only during the round.** Never edit an
existing row.

**Carried by reference from NFRA_CTLPLN's channel** (`org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`;
the rows stay there): `NFRA_CTLPLN-S33`, `NFRA_CTLPLN-S34` (ARMED, disarmed in code by CT-i-13, closing on the FWD-3 full-day read),
`NFRA_CTLPLN-W36-S2` (handed to NFRA_TRNSPT in round 8's issuance).

## COMM_ASSIST-S1 -- carry record: S33 and S34 move here by reference, closing on FWD-3's full-day read

```json
{
  "id": "COMM_ASSIST-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~R",
  "surfaced_at": "2026-10-09T00:04:35Z",
  "one_line": "Carry record: NFRA_CTLPLN-S33 (a refused End of Day redraft failed silently) and NFRA_CTLPLN-S34 (a chat's later drafts within a week were never texted) move to COMM_ASSIST by reference; both are disarmed in code (CT-i-13, live 2026-10-08 22:32Z) and close on FWD-3's full-day read.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md rows NFRA_CTLPLN-S33, NFRA_CTLPLN-S34",
      "NFRA_CTLPLN.TO-CT-i-13 merged 75420934c2; TO-APPLY-20 live 22:31:55Z/22:32:01Z, CodeSha256 xWURpe/nRkiZAc8Uui+arsJpSeVnUErNEHBWqtvrM5Q= (read by the issuer)",
      "1.0.0_SA_CTO msg 107481: 'run round 8 under COMM_ASSIST, carrying S33/S34/W36-S2 by reference'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-3: no refusal fails silently, and every texted outcome is a text he got.",
  "world_is": "Fixed in code and applied; not yet exercised on a day with traffic (2026-10-08 22:31Z-23:22Z: 0 handler invocations).",
  "notes": "W36-S2 is handed to NFRA_TRNSPT (row file in that channel) and disarmed at NFRA_CTLPLN by S35."
}
```

## COMM_ASSIST-S2 -- W39-S1 does not bind: the gateway's Teams identity is unscoped (site Z code read); r29's read-back confirms

```json
{
  "id": "COMM_ASSIST-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~R",
  "surfaced_at": "2026-10-09T02:12:50Z",
  "one_line": "Disarm read for NFRA_CTLPLN-W39-S1 (the gateway's caller map omits two Graph scopes the channel routes need): site Z reads MS_INGEST_IDENTITY as UNSCOPED, so its consent is the full GRAPH_SCOPES envelope and the omission does not bind; to confirm at r29's ENV read-back.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "site Z 1.0.0_SA_CTO~O msg 32269 (relay 0.0.0_AB_MSTR 107632): identity_scope.py:54-77 and identity_tool_allowlist.txt:19,25 scope exactly one identity, opalbloomberg@opalinvest.com; config.py:224; consent_scopes() returns None for an unscoped identity (:135-137)",
      "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~39/CHANNEL_READ_SCOPES_MEASURED.md (both scope lists carry Team.ReadBasic.All, Channel.ReadBasic.All, ChannelMessage.Read.All)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The channel routes shipping in NFRA_OPLGTW r29 get the Graph scopes they need.",
  "world_is": "True by code read on site Z; the host .env value of MS_INGEST_IDENTITY is not read (site Z's limit, stated).",
  "notes": "Closes when r29's ENV read-back shows MS_INGEST_IDENTITY is not the one scoped identity; then the first channel_poll line reads failed=0."
}
```
