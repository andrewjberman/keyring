# NFRA_MCPORTAL -- workstream PC round 1 L8 compile + L9 (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v5. Fabric: site-z. Recorded: 2026-10-14 ~17:4xZ.
**Input:** `2.0.0_SA_COO~MP` `deliverables/2.0.0_SA_COO~MP/pc/PC_R1_DRAIN_PACKET.md` @b53cc655ee, read to EOF (msg 34158, acked).
PC round 1 has 6 of 6 orders terminal. round-close-check reads REFUSED at ~17:4xZ on exactly one ungraded judgment
criterion, MP-pc-4 AC2, which is graded here (Z-C-S35).

**This seat's reads (~17:4xZ):**
- `EC2_MANIFEST.json` `deployed_commit` bacec95ccd (2026-10-14T15:43:28Z).
- `git show bacec95ccd:.../app/admin_fabric_gitstate.py:175-186` (`_refused_pair`), three states:
  - rc != 0: `{"refused": true, at, note}`;
  - rc == 0: `{"refused": false, at}`;
  - absent: `"not recorded"`, each with its own basis.
- `~/.claude.json` `.oauthAccount` on this box, read earlier this session: emailAddress, displayName, organizationName,
  organizationRole and billingType are present, and the object holds no token.

**Remediation rows met, flipped in place in REMEDIATION_v4.Z.md in this commit:**
- **Z-C-S31 (three-state display): REMEDIATED.** Its close clause was "the served page reads 'no' for laptop and 'not
  recorded' for a box with no pointer". MP-pc-6's served read gives laptop `{"refused": false, at 16:50:57Z}` and sitez
  `"not recorded"`, on the release whose code this seat read.
- **Z-S47 (Andrew's account and usage per box): REMEDIATED.** Its remedy was "a PRD addendum adds the outcome ... It is
  then cut". NFRA_MCPORTAL v0.8 added FWD-22 (signed by this seat @a75bdd3eea), and MP-pc-4 is its first cell.
  FWD-22 itself is not realized; that is a separate grade.

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-C-S35",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-14T17:40Z",
    "one_line": "L9 grade, NFRA_MCPORTAL.TO-MP-pc-4.claude-limits-sources-read AC2 (judgment, PC round 1): PASS, bounded -- the finding names a credential-free source for the account and says plainly that no existing credential-free source exposes the 5-hour or weekly remaining; every figure is measured on site Z only.",
    "class": "OBSERVATION",
    "spec_asserts": "MP-pc-4 AC2: for each of the three figures (account, 5-hour limit, weekly limit), the finding names a source a build cell can read on every box without a credential, or says plainly that none exists.",
    "world_is": "Account: U1 names `~/.claude.json` `.oauthAccount` (emailAddress, organizationName, organizationType, billingType) and `claude auth status`, measured on site Z, with no token in either. This seat's own read of that object on this box agrees. 'Every box' is INFERRED for laptop, dell1 and dell2 (same install), and U1 says so. Limits: U1 says plainly that neither the 5-hour nor the weekly remaining is readable from a file or command without a credential. That is the criterion's 'say plainly that none exists' branch, and it is met. U1 also names the best credential-free ROUTE, inferred from field names in the binary: a status-line command receiving rate_limits.five_hour and seven_day {used_percentage, resets_at}. That route needs a statusLine configured on every box, which is a build act, not an existing source. It excludes the OAuth usage endpoint and the API headers because both need a credential, and it keeps .credentials.json closed. Bounds: 1 of 4 boxes measured, and the status-line field names are inferred, not seen in a live payload.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_NFRA_MCPORTAL~23/U1_CLAUDE_ACCOUNT_AND_LIMITS_SOURCES.md, read whole (44 lines)",
        "~/.claude.json .oauthAccount on site Z, read by this seat (non-secret fields only)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect: TO-MP-pc-4 AC2 PASS, bounded."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S36",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-14T17:40Z",
    "one_line": "PC round 1 L8: Z-W24-S1 and Z-W24-S3 DISMISSED (issuer-accepted procedure notes); Z-W24-S2 GRADUATES (Z-C-S37); the People view and the three-state reading are served at bacec95ccd and read against the stores by the close run.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Z-W24-S1: the entitlement command has no read subcommand, so the grant was read with a raw store get. That is an independent read, which is what the criterion wants. Z-W24-S2: the store read ran under the host instance role, so store==page compares two code paths over one credential and does not test the operator role. The issuer states that limit, and this seat carries it: the People view is not yet tested under the operator role. Z-W24-S3: a status flip was outside the worker's paths, and the issuer made it. The close run (MP-pc-6) reads alyssa's 5 of 5 data-grant tools equal on the page and in the store, the portal_index channel's 6 of 6 tools equal, laptop 'refused: false', and sitez 'not recorded'. Not exercised: the rc != 0 branch (no box records a refusal) and an owner's look in a browser (Andrew's sitting, call 21d9). Z-S120 is NFRA_OPLGTW's row, not this project's.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W24-S1",
      "NFRA_MCPORTAL-Z-W24-S3"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~MP/pc/PC_R1_DRAIN_PACKET.md @b53cc655ee (rows, close run)",
        "EC2_MANIFEST deployed_commit bacec95ccd; bacec95ccd:app/admin_fabric_gitstate.py:175-186 (this seat)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Issuer-accepted notes with their limits stated; no standing defect."
  },
  {
    "id": "NFRA_MCPORTAL-Z-C-S37",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-14T17:40Z",
    "one_line": "PC round 1 L8: Z-W24-S2 GRADUATES -- the People view's store==page check ran both reads under the host instance role, so it compares two code paths over one credential and never tests what the page shows to its real reader path.",
    "class": "OBSERVATION",
    "spec_asserts": "MP-pc-6: the per-person view is checked against the stores it reads.",
    "world_is": "The close run read the grant store and the page module both under the host instance role. That proves the page renders what the store holds when both use the same credential. It does not prove the owner-gated route serves the same through its own role and gate, and it does not test the operator role's read. The issuer accepted the row with that limit stated. The gap stands until one read runs through the served route under a real owner identity, which is Andrew's sitting (call 21d9), or under the operator role.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W24-S2"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row Z-W24-S2; PC_R1_DRAIN_PACKET.md @b53cc655ee rows section"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~Z
