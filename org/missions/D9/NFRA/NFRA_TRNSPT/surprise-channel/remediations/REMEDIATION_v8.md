# NFRA_TRNSPT -- rounds 17-19 remediations

<sweep_watermark>2026-10-09T09:40Z</sweep_watermark>

Graduated at the rounds-17-19 L8 (ADJUDICATION_v10.md), round label v20: 3 rows, OPEN, each a ruling for the CTO.

```json
[
  {
    "id": "NFRA_TRNSPT-D2-W1-S7",
    "project": "NFRA_TRNSPT",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "PRD C-TIERS says silver is PII-wiped and C-READERS lets a scoped role read the wiped silver, but the Teams silver writer states it applies no wipe, so no Teams silver partition is a wiped copy a narrower reader could be given.",
    "evidence": [
      "investigation row NFRA_TRNSPT-D2-W1-S7",
      "org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md:106 (C-TIERS: SILVER is typed, de-duplicated, PARQUET, with PII wiped) and :121 (C-READERS: a separate scoped role may read the wiped silver and gold prefixes only)"
    ],
    "remedy": "Wipe the Teams silver as C-TIERS requires (or rule Teams silver raw-tier and keep it out of C-READERS); no scoped reader is granted on it until one holds.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v20",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v20"
    },
    "closed": true
  },
  {
    "id": "NFRA_TRNSPT-D2-S10",
    "project": "NFRA_TRNSPT",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The Teams pull cannot land a meeting even if applied: its gateway transport is a STUB that raises GatewayToolsAbsent on every call, and pull.tf names a bearer secret (teams/global/gateway-token) that does not exist; TO-APPLY-p18 stopped at step 1 on the secret.",
    "evidence": [
      "investigation row NFRA_TRNSPT-D2-S10",
      "data/transcripts/scripts/teams/gateway_client.py:5 and :81 -- 'a GatewayTransport STUB that raises'; 'each method raises GatewayToolsAbsent naming the route it would call; no network call'"
    ],
    "remedy": "Rule the cell: a real Teams gateway transport and the owner-named bearer secret in pull.tf; then ~T2 cuts it and the pull lands one meeting.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v20",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v20"
    },
    "closed": true
  },
  {
    "id": "NFRA_TRNSPT-D2-S9",
    "project": "NFRA_TRNSPT",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The ONE 365-day backfill (TO-RUN-b17 @beef69ea0d) landed 24 messages on 6 dates, but all 6 silver rows are held_out by the wipe's residual check, so gold gained 0 rows: the precedent the backfill was ordered to supply (CTO msg 2205) is empty.",
    "evidence": [
      "investigation row NFRA_TRNSPT-D2-S9",
      "issuer read of the stored bytes 06:4xZ: silver 6 objects / 6 rows / held_out 6; gold 6 objects / 0 rows; pull_runs 19 (was 18)"
    ],
    "remedy": "Rule whether the wipe's residual allowlist widens for common capitalized words, or the backfill precedent stays empty (and FWD-10's precedent read is then stated as none).",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v20",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v20"
    },
    "closed": false
  }
]
```
