# NFRA_CTLPLN: CVO adjudication

Adjudication rows by `3.0.0_SA_CVO`. The id grammar is `NFRA_CTLPLN-C-S<k>`.

```json
[
  {
    "id": "NFRA_CTLPLN-C-S1",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-06T21:35Z",
    "one_line": "S1 disarmed on the laptop: the three enabled Remote Desktop inbound rules now admit only the tailnet range; site Z and the Dells carry the same rule by Andrew's word, not yet read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "C-RDP: Remote Desktop reachable over the tailnet only. Andrew ~21:0xZ, call 1: 'Only our tailnet-affiliated devices should be able to come in over RDP.'",
    "world_is": "Laptop, read by this seat: 'Remote Desktop - User Mode (TCP-In)', '(UDP-In)' and 'Shadow (TCP-In)' each RemoteAddress 100.64.0.0/255.192.0.0 (applied by 1.0.0_SA_CTO 20:58:59Z on Andrew's approval). Other inbound rules on 3389: the census was PARTIAL here (Get-NetFirewallPortFilter Access denied without admin), and the CTO's read says none. Site Z, dell1 and dell2: not read; owed through S14's per-box proof.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Get-NetFirewallRule (Remote Desktop group, enabled) | Get-NetFirewallAddressFilter on the laptop, 2026-10-06 ~21:3xZ",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_210xZ_SEVEN_CALLS_RDP_LOCK_Q1_Q2_Q3_CONFIRMED_NO_BD_SHAPE.md (call 1, ruling 1)"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-S1"
    ],
    "disposition": "GRADUATED"
  }
]
```
