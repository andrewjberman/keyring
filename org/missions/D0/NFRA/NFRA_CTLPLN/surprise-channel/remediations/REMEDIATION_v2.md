# NFRA_CTLPLN -- remediations, v2

<sweep_watermark>2026-10-12T10:50Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L`, 2026-10-12 ~10:5xZ, at the round-8 drain (1.0.0_SA_CTO msgs 108477 and 108495, 2.0.0_SA_COO~C msg 108508).
Graduated in ADJUDICATION_v10.md C-S32. Four rows: D1-S8 (ARMED), D1-S10, W65-S2 (ARMED) and W61-S1 (ARMED; the disarming act is Andrew's elevated line). Every NFRA_CTLPLN order is
terminal at HEAD d3e77d88e2: 98 complete, 4 withdrawn, 1 cancelled, 1 superseded.

```json
[
  {
    "id": "NFRA_CTLPLN-D1-S8",
    "project": "NFRA_CTLPLN",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The pre-push deploy gate bounds its deploy set by the box's diff against origin/CLOUD (.tools/git-hooks/pre-push-safe-deploy.sh:56-57,82,104). A file named by an OPEN, pinned change-management entry that reaches CLOUD by integrate before its box push is never in any later box diff, so no push deploys it and S3 keeps the old bytes.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row D1-S8",
      "adjudication rows NFRA_CTLPLN-C-S13..S15 header (ADJUDICATION_v7.md, HELD) and NFRA_CTLPLN-C-S32"
    ],
    "remedy": "P1. The gate also deploys any deploy-scope file named by an OPEN pinned entry whose S3 bytes differ from the pinned blob, regardless of the box diff. The issuer cuts the cell for the gate's owner. Done when a planted case (a pinned file already on CLOUD, absent from the box diff, S3 bytes stale) is deployed by the next push and its S3 sha256 equals the pinned blob.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v10",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~C",
      "round": "v10"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~C",
      "at": "2026-10-15T21:07Z"
    }
  },
  {
    "id": "NFRA_CTLPLN-D1-S10",
    "project": "NFRA_CTLPLN",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "intake_receive.py install runs `pip install --user` for every wheel of the pack into sys.executable's user site. It has no --target or --venv option and no per-wheel selector, so it cannot install into a fresh isolated environment. Run on a box interpreter it shadows a newer click and installs wheels the box was not meant to take.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row D1-S10",
      "adjudication row NFRA_CTLPLN-C-S32"
    ],
    "remedy": "P2. The receiving tool's install verb gains a --venv (or --target) argument and a per-wheel selector. Done when a Dell installs one named wheel into a fresh venv with the tool's own verb, and the box interpreter's package list is unchanged before and after (pip freeze diff 0).",
    "owner": "2.0.0_SA_COO~C",
    "round": "v10",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C",
      "round": "v10"
    },
    "closed": false
  },
  {
    "id": "NFRA_CTLPLN-W65-S2",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Two portal carriers do not reproduce byte for byte from lib/opal_naming.py generate: firmDisplayNames.generated.ts carries a stale mark hash over an identical body, and vendorDisplayNames.generated.ts differs only by CRLF on disk. A portal drift test landed before regeneration would fail on them.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row W65-S2",
      "1.0.0_SA_CTO msg on 108497 (2026-10-12T08:54Z): 'W65-S2 ... is mine ... both regenerate at the next carrier cycle'",
      "adjudication row NFRA_CTLPLN-C-S32"
    ],
    "remedy": "P2. The CTO regenerates both carriers in the portal repository on DEV at the next carrier cycle, before any portal drift test lands. Done when generate reproduces all portal carriers byte for byte (diff count 0).",
    "owner": "1.0.0_SA_CTO",
    "round": "v10",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v10"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "NFRA_CTLPLN-W61-S1",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "On the laptop the firewall rule 'OpenSSH Server (Tailscale only)' admits 22/TCP from RemoteAddress Any on Profile Any; sshd is Running on 0.0.0.0:22 and :::22; no PasswordAuthentication line is set (password login on); no authorized_keys file exists; the Wi-Fi interface is category Public. The laptop accepts an SSH password login from its Wi-Fi network.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row W61-S1",
      "Get-NetFirewallRule / Get-NetTCPConnection / Get-NetConnectionProfile read by 3.0.0_SA_CVO~L 2026-10-12 ~06:3xZ and ~10:4xZ (rule remote=Any, sshd Running)",
      "adjudication row NFRA_CTLPLN-C-S32; ROUND_ANALYSIS.round6.md / round7.md (E9 FWD-27, the laptop cell disarms W61-S1)"
    ],
    "remedy": "P0. Andrew runs one elevated line: Set-NetFirewallRule -DisplayName \"OpenSSH Server (Tailscale only)\" -RemoteAddress 100.64.0.0/10 (or Stop-Service sshd until the FWD-27 laptop cell runs). The issuer's FWD-27 laptop cell (E9) then sets key login and PasswordAuthentication no. Done when the rule reads RemoteAddress 100.64.0.0/10 and ssh-tailnet-verify reads the laptop password_arm=REFUSED.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v10",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~C",
      "round": "v10"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "Andrew",
      "at": "2026-10-15T21:07Z"
    },
    "closed": true
  }
]
```
