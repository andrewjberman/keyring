# NFRA_OPLGTW -- surprise channel, REMEDIATION v17 (site Z) -- THE ROUND-34 SLUG

**Lane:** the CVO. **Cut by:** `3.0.0_SA_CVO~Z`, 2026-10-11 ~22:5xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Round 34: MAY-CLOSE, 0 judgment criteria; 9 of 10 complete, OG-bd-1 held on Andrew. L8 is at `adjudications/ADJUDICATION_v25.Z.md`:
- **Z-S85 is disarmed.** This seat read the trunk deploy script: 5 allowlist references, up from 0.
- **/hx/teams 200 is corroborated on a second plane:** COMM's channel_poll reads 29 of 29 `failed: 0`.
- C-S68 dismisses 9 rows; C-S69 graduates the 4 below.

**Still owed by this seat from round 33:** the OG-tl-1 and OG-rl-16 judgment criteria (dell2's re-probe; dell2's first E2 put).
Since the CT-i-11 release, the meeting re-probe can be read on the live route.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-S91",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "each declared 16:00Z silver sweep drains the WHOLE shared DLQ opal-assets-silver-dlq and reports other families' failures as its own, so a family's failures leave the queue under another family's name",
    "evidence": [
      "NFRA_OPLGTW-Z-S91 (2.0.0_SA_COO~O, OG-dq-1 @94ddb37165); names the actor of Z-S77 and Z-W57-S1"
    ],
    "remedy": "Round-35 code cell: drain per family (receive, keep only this family's messages, release the rest), each family reporting only its own.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v17"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W55-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "the .pptx market_update key is intake's content-addressed form because the gateway host carries no lib/opal_naming; the quarter argument the order named is not in the key",
    "evidence": [
      "NFRA_OPLGTW-Z-W55-S2 (0.9.0_WK_NFRA_OPLGTW~55)"
    ],
    "remedy": "Round-35 .pptx release pair: state the key form and how a reader finds a quarter's deck.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v17"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-W57-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "blackdiamond_list_fees has 2 unprofiled callers (one master_admin; 5 calls 2026-10-01 to 10-08), so denying it to unprofiled principals would cut a live caller; OG-bd-1 stopped and built no deny",
    "evidence": [
      "NFRA_OPLGTW-Z-W57-S2 (OG-bd-1 step 2 census)",
      "continues NFRA_OPLGTW-Z-W45-S2 (REMEDIATION_v16)"
    ],
    "remedy": "Andrew's admission call (MSTR~Z msg 33359): admit the two callers by profile, then deny unprofiled access; OG-bd-1 re-cuts in round 35.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v17"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-10-11T17:36Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-Z-S92",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "the Teams bearer secret gateway/teams/bearer is readable by the gateway, COMM_ASSIST's Lambda and the cloudops-dell-agent group; the dell group's consumer is unnamed",
    "evidence": [
      "NFRA_OPLGTW-Z-S92 (2.0.0_SA_COO~O, a CTO observation)"
    ],
    "remedy": "Round 35: name the dell group's consumer or remove its read, and record each holder's reason.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v17",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v17"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
