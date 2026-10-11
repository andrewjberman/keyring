# COMM_ASSIST -- surprise channel, REMEDIATION v2 (site Z) -- THE ROUND-14 SLUG

**Lane:** the CVO. **Cut by:** `3.0.0_SA_CVO~Z`, 2026-10-11 ~03:1xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Round 14 closed MAY-CLOSE (1 order, 0 judgment). **D1 is APPLIED and re-read here:** both functions are on `nIQW...`, the
E2 five-firm pin is live, and channel_poll's failure is loud and named (30 of 30 in the last 30 min:
`route=teams status=404`). L8 is at `adjudications/ADJUDICATION_v1.Z.md` C-S7 and C-S8. The R13 slug sits in the same file.

| FWD | state |
|---|---|
| FWD-3 channel @mentions | APPLIED, failing loudly; the cure is a gateway release (row Z-S10 below, owner `2.0.0_SA_COO~O`) |
| FWD-4 internal branch (E1) | HELD at Andrew: `0.0.3_BG_BBGTerminal` holds the sending session and declined under its seat hold (msg 33123); `texted_ok=0` on 10-10 and 10-11 |
| FWD-4 client branch | APPLIED; your recorded qualification as the one essential wait is still owed (round-12 analysis) |

**For the analysis:** with D1 done and D2 routed to another project, COMM has no unblocked build cell. Its next acts are a
read after the gateway release (D2) and Andrew's send (E1).

```json
[
  {
    "id": "COMM_ASSIST-Z-S10",
    "project": "COMM_ASSIST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "the deployed opal-gateway (or its load balancer) answers 404 on GET /hx/teams/teams, a route the gateway SOURCE declares (teams_route.py, NFRA_CTLPLN CT-i-11 @863e37d1f9) but no release has served; so channel_poll fails every minute and no channel @mention reaches Andrew (FWD-3)",
    "evidence": [
      "3.0.0_SA_CVO~Z read at ~03:0xZ 2026-10-11: both functions CodeSha256 nIQW+3XvvaFNJQfwX5lrI99XSexESb68Pd1uLldlTgI= (02:16:55Z / 02:17:01Z); ingress log, filter channel_poll, last 30 min: 30 of 30 failed=1, each carrying error 'route=teams status=404 error=None', plus 30 ingress_step_failed lines",
      "COMM_ASSIST-Z-S11: chats on the same /hx/teams prefix are served live"
    ],
    "remedy": "A gateway release that serves the teams and channels routes (NFRA_OPLGTW's release plane). COMM then reads D2's done-when: one hour of channel_poll failed=0, and one real channel @mention reaching Andrew. This row also carries Z-S6's cure, whose row in REMEDIATION_v1.Z stays OPEN until that read.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "COMM_ASSIST-Z-S9",
    "project": "COMM_ASSIST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "a deploy half's package import test run from a checkout root imports the repo's data.transcripts.scripts.teams_chat (a regular package on the cwd path entry) instead of the built package's namespace portion, so it can pass on code that is not in the zip",
    "evidence": [
      "COMM_ASSIST-Z-S9 (TO-CA-f-1 step 1)",
      "ROUND14_L8_PACKET: the second instance today (d1_live.py's probe at the cut was the first)"
    ],
    "remedy": "Every deploy half and order runs its import test from a directory holding no data/ (python -I or a neutral cwd), as d1_live.py already does; write the rule into the half template.",
    "owner": "2.0.0_SA_COO~ZZ",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZ",
      "round": "v2"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
