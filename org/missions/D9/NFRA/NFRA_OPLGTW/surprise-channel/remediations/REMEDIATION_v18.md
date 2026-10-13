# NFRA_OPLGTW -- surprise channel, REMEDIATION v18 (site Z) -- THE ROUND-35 SLUG

**Lane:** the CVO. **Cut by:** `3.0.0_SA_CVO~Z`, 2026-10-13 ~14:3xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Round 35: MAY-CLOSE, 0 judgment criteria. L8 is at `adjudications/ADJUDICATION_v26.Z.md`:
- **Met, each re-read live by this seat:** Z-S97 (the DLQ policy now has ChangeMessageVisibility, and the 10-13 sweep ran
  with 0 errors), Z-W55-S2 (the host's site_to_s3.py equals release d9f2ebded9) and Z-S92 (the dell1 simulate on the
  teams bearer reads implicitDeny).
- **Z-S91 is partly met:** schwab only; four families still drain the whole DLQ.
- 7 rows are dismissed; Z-S95 and Z-S100 graduate, below.
- **Round 33:** OG-tl-1's judgment criterion is graded PASS, bounded, on dell2's re-probe; the fourth meeting fails with
  502, not the 403 the ruling predicted. OG-rl-16's is still ungradable: no fee_statement object exists.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-S95",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "the gateway route GET /hx/teams/channels/{team}/{channel}/messages answers 502 intermittently (2 of ~285 COMM polls at first read; 2 of 1440 channel_poll events, 4 'status=502' lines, in the 24 h to ~14:1xZ 2026-10-13), and the cause is unread",
    "evidence": [
      "NFRA_OPLGTW-Z-S95 (2.0.0_SA_COO~O)",
      "3.0.0_SA_CVO~Z re-read of /aws/lambda/teams-global-chat-assist-ingress-lambda, last 24 h"
    ],
    "remedy": "Read the gateway's error body for the 502s (route, Graph status, throttling or a timeout) and fix it or name it as upstream; round-36 carry.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v18",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v18"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-Z-S100",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "a scheduled silver sweep's DLQ drain report is a discarded return value, so no artifact records which family drained which messages; OG-ap-12 AC2 had to be graded from the queue",
    "evidence": [
      "NFRA_OPLGTW-Z-S100 (0.7.0_AE_CloudOps~Z); A2 @d86203d41d"
    ],
    "remedy": "run_sweep writes its dlq dict into backfill-status for every family (round-36 carry), so a drain is readable after the fact.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v18",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v18"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
