# NFRA_CTLPLN -- remediations, v3

<sweep_watermark>2026-10-12T12:35Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L`, 2026-10-12 ~12:3xZ, at the round-9 drain (2.0.0_SA_COO~C msg 108534). Graduated in ADJUDICATION_v11.md
C-S34. One row: S9112 (ARMED). Every NFRA_CTLPLN order is terminal at HEAD e08f8332a9: 103 complete, 4 withdrawn, 1 cancelled,
1 superseded.

```json
[
  {
    "id": "NFRA_CTLPLN-S9112",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The log group /aws/lambda/opal-portal-data-proxy holds logged request events that carry long-lived credential cookies: refresh_token (38 lines, 16 inside the 7-day refresh expiry when read) and device_trust (29 lines, all inside the 30-day trust window). CT-w-10 (@e08f8332a9) stops new lines; it does not remove these. The group's retention is 14 days (describe-log-groups read by 3.0.0_SA_CVO~L ~12:3xZ: retentionInDays 14, storedBytes 212029), so the events age out by about 2026-10-26. Until then, any principal holding logs:FilterLogEvents or GetLogEvents on the group can read tokens that may still be accepted.",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row S9112",
      ".tools/aws logs describe-log-groups --log-group-name-prefix /aws/lambda/opal-portal-data-proxy (no event read): retentionInDays 14",
      "2.0.0_SA_COO~C msg 108534: 27 post-apply events read Bearer 0, JWT 0, cookie 0",
      "adjudication row NFRA_CTLPLN-C-S34"
    ],
    "remedy": "P0. Andrew's two acts, as the CTO asked: (1) purge the credential-bearing events (delete the group's log streams written before the CT-w-10 apply, or the group, letting it re-create); (2) invalidate the refresh tokens and device-trust tokens issued before the apply, by rotating the signing secret or revoking sessions. Done when a filter for the two cookie names over the group returns 0 events and an old refresh token is refused. If neither act lands, the hazard self-expires when the last pre-apply event passes the 14-day retention (about 2026-10-26); the row closes on that read.",
    "owner": "2.0.0_SA_COO~C",
    "round": "v11",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~C",
      "round": "v11"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "Andrew",
      "at": "2026-10-14T01:25Z"
    },
    "closed": true
  }
]
```
