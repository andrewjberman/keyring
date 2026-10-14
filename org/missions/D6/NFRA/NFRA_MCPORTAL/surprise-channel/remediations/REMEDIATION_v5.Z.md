# NFRA_MCPORTAL -- surprise channel, REMEDIATION v5 (site Z) -- THE PC ROUND-1 SLUG

**Lane:** the CVO. **Cut by:** `3.0.0_SA_CVO~Z`, 2026-10-14 ~17:4xZ. **Reader:** `1.0.0_SA_CTO~Z`.

Workstream PC round 1 has 6 of 6 orders terminal and is served at bacec95ccd. Its one judgment criterion is graded:
**MP-pc-4 AC2 PASS, bounded** (Z-C-S35). L8 is at `adjudications/ADJUDICATION_v5.Z.md`.
- **The People view (FWD-21's read half) and the three-state refusal reading are served.** The close run read them
  against the stores. Not exercised: a recorded refusal (rc != 0), and an owner's browser look (call 21d9).
- **Z-C-S31 and Z-S47 are met and flipped REMEDIATED in place** (REMEDIATION_v4.Z):
  - Z-C-S31: laptop reads "refused: false" and sitez "not recorded".
  - Z-S47: FWD-22 now exists, and its first cell has run.
- **Two procedure rows dismissed; Z-W24-S2 graduates** (below).

**For the analysis:**
1. **FWD-22 (account and usage) has a credential-free source for the account only.** The 5-hour and weekly remaining
   need a build act: a status-line command configured on every box, writing `rate_limits` to a local file. That changes
   each box's Claude Code settings, which is every seat's harness, so the cell names that blast radius. Its first act is
   to see one live `rate_limits` payload, since the field names are inferred from the binary.
2. **U1 measured 1 of 4 boxes.** The account source on laptop, dell1 and dell2 is read by the build cell, not assumed.
3. **The People view is untested under the operator role** (Z-W24-S2).

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-W24-S2",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "the People view's close run compared the grant store and the page module both under the host instance role, so it never read the owner-gated route through its own gate, or the operator role's read",
    "evidence": [
      "NFRA_MCPORTAL-Z-W24-S2 (0.9.0_WK_NFRA_MCPORTAL~24); PC_R1_DRAIN_PACKET.md @b53cc655ee"
    ],
    "remedy": "One read of /api/admin/people through the served route under a real owner identity (Andrew's sitting, call 21d9) or the operator role, compared with the grant store for the same person. Closes when that read equals the store for each data-grant tool, with the denominator printed.",
    "owner": "2.0.0_SA_COO~MP",
    "round": "v5",
    "remediation": {"state": "OPEN", "owner": "2.0.0_SA_COO~MP", "round": "v5"},
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~Z
