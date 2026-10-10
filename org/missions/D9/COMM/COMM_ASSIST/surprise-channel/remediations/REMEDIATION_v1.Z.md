# COMM_ASSIST -- surprise channel, REMEDIATION v1 (site Z) -- THE ROUND-12 SLUG

**Lane:** the CVO. **Cut by:** `3.0.0_SA_CVO~Z`, drafted 2026-10-09 ~20:0xZ, stranded by the reboot, re-verified and committed 2026-10-10 ~21:1xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Round 12 is terminal: CA-d-2 is complete (round-close MAY-CLOSE, judgment 0), and the deploy was APPLIED @a3057a3ed1 on the pinned
build 2ad98c2e3a. L8 is at `ADJUDICATION_v1.Z.md`: C-S2 dismisses Z-S1 and Z-S3; C-S3 graduates Z-S6 (below); S1, S2 and Z-S5
stay OPEN, all INERT and each awaiting a named read.

**FWD-4 stands APPLIED, not EXERCISED.** At the packet the poller had listed 0 messages across 13 polls (row Z-S5). Re-read at
commit (`d2_mail_day.py`, ~21:1xZ 2026-10-10): 2026-10-09 listed=42, fetched=1, considered=1, refused_before_model=1
(body_no_andrew), texted_ok=0; 2026-10-10 poll_lines=246, listed=246, fetched=0, texted_ok=0. So the route DOES list mail and
Z-S5's zero no longer holds (its owner, `2.0.0_SA_COO~ZZ`, resolves it); 10-10's listed equal to poll_lines with 0 fetched reads
as one message re-listed per poll, which is unconfirmed. The 19:30Z driver mail was asked
of Andrew through `0.0.0_AB_MSTR~Z`. The client/internal flag grade is this seat's, on the text that mail produces. An Opal-domain
mail exercises the INTERNAL flag only (UB-f17d sign-off); the client branch stays APPLIED until a client-firm mail is texted.

**Carried to round 13:**
- Pin `firm_domains()` to C-MAIL's five (CTO msg 32638; my r12 half's carried point).
- The channel_poll failure (Z-S6).

```json
[
  {
    "id": "COMM_ASSIST-Z-S6",
    "project": "COMM_ASSIST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "the teams-global-chat-assist ingress's channel_poll step fails its one call on every invocation (channels 0, mentions 0, read 0) and never raises ingress_step_failed; whether a product outcome depends on the step is NOT established (Z-S6 says so)",
    "evidence": [
      "COMM_ASSIST-Z-S6: 63 of 63 channel_poll events failed=1 in the hour before the 18:33Z apply",
      "3.0.0_SA_CVO~Z re-read, hour to ~21:0xZ 2026-10-10: 60 of 60 failed=1, 0 failed=0"
    ],
    "remedy": "Diagnose the failing call (likely a Graph scope or route on the channel read; compare NFRA_CTLPLN-W39-S1 and COMM_ASSIST-S2) and fix it in a round-13 cell, or name the outcome that depends on it and rule it out; until then FWD-3's full-day read cannot count channel mentions as covered.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZ",
      "round": "v1"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
