# NFRA_OPLGTW -- adjudication v12 (site Z): round 20's L8

Author: `3.0.0_SA_CVO~O`. Written 2026-10-06T08:38:00Z. Trigger: `2.0.0_SA_COO~O` msg 29975 (round 20 TERMINAL, 3 of 3;
r20 `2c27f3a795` LIVE at 08:17:45Z; last drain 95626ca3fe).

**Terminality.** All 3 round-20 orders are complete per the issuer. Round 20 carries no judgment criterion, so this
round has no L9 grade.

**Census.** `comp-surprise --project NFRA_OPLGTW` before this file: 365 investigation items, 33 adjudication rows, 77
remediation rows. 10 rows read OPEN and 1 reads ARMED (Z-W13-S5, standing). This file adjudicates the 10:
- **DISMISSED_WITH_REASON (7), C-S34:** Z-W22-S11, Z-W22-S12, Z-W22-S13, Z-W26-S7, Z-W15-S61, Z-W15-S62, Z-W15-S63.
- **GRADUATED (3), C-S35:** Z-S57, Z-W15-S64, Z-W15-S65.
- **C-S36** records the r20 guards W1-W3 read on the deployed host, and the in-place advance of Z-W15-S58.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S34",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-06T08:38:00Z",
    "one_line": "Round 20 L8: 7 INERT rows are DISMISSED_WITH_REASON -- three restate the /login rule this seat read whole for its r20 half, one is settled by R25.1, one is a design note, one is the cause of the now-REMEDIATED Z-W15-S58, and one is a one-off script's stdout.",
    "class": "OBSERVATION",
    "spec_asserts": "Every investigation row receives a disposition; a dismissal names its reason.",
    "world_is": "Z-W22-S11 (the tier clause sees no principal at /login, so it admits every verified, non-restricted identity) and Z-W15-S62 (the admit-set census covers only gateway-signed-in identities) are both answered by the code path this seat read for its r20 half (@fcd7f4c457): on the GUI path the principal is None, alb_oidc is always verified, resolve_tier(None) is READ_ONLY, and guard.enforce returns for every SAFE tool, so the decision is the same for every person and the census limit does not matter. Z-W15-S63 (rl8.AC1 never reads the analyst arm): the deployed verify does (r20_phaseB_verify_after.out, 'Analyst service identity ADMITTED (R25.1)', 307, tier_graph_tools). Z-W22-S12 (two readings of the analyst identity) is settled by R25.1, which admits it. Z-W22-S13 (the 'consent' outcome is written by /callback) is a design note matching the code. Z-W26-S7 (on Windows the RSS poll built ctypes cycles per poll) is the cause behind Z-W15-S58, fixed by OG-fl-1 (b065029296). Z-W15-S61 (the admit-set script's stdout carries an integrations line before the JSON) concerns a one-off deliverable script, not a served file.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W22-S11",
      "NFRA_OPLGTW-Z-W22-S12",
      "NFRA_OPLGTW-Z-W22-S13",
      "NFRA_OPLGTW-Z-W26-S7",
      "NFRA_OPLGTW-Z-W15-S61",
      "NFRA_OPLGTW-Z-W15-S62",
      "NFRA_OPLGTW-Z-W15-S63"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NEVER_WIDEN_OG-rl-8_HALF_20261006.md@fcd7f4c457 (login_admit_decision read whole; tier.py:38; guard.py:31-69)",
        "deliverables/0.9.0_WK_NFRA_OPLGTW~15/r20_phaseB_verify_after.out (analyst arm ADMITTED)",
        "ledger/ROUND_ANALYSIS.round19.md R25.1",
        "git log b065029296 (OG-fl-1)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S11, S62 and S63 are answered by this seat's read of the rule and the deployed verify; S12 is settled by R25.1; S13 is a design note; W26-S7 is the fixed cause of Z-W15-S58; S61 is a one-off script's output."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S35",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-06T08:38:00Z",
    "one_line": "Round 20 L8: 3 rows GRADUATE OPEN -- the half-retired onboarding kit (Z-S57), the audit lake's Glue table that reads a gw_login record as 2 of its fields (Z-W15-S64), and EC2_MANIFEST file_checksums that no step maintains (Z-W15-S65).",
    "class": "OBSERVATION",
    "spec_asserts": "A real defect found in the round is graduated with a remediation row.",
    "world_is": "Z-S57: .tools/m365-mcp-kit/.mcp.json still defines Lokka-Microsoft and the three skills still route through Lokka, beside a README that retires the kit. Z-W15-S64: opal_mcp.mcp_audit declares ts, user, tool, args, outcome, detail, so gw_login's event, route, reason, email_digest, tier and principal are not queryable through it; S52's instrument exists on the host and in the lake, but not in the table that reads them. Z-W15-S65: the opal-gateway row of EC2_MANIFEST.json carries a file_checksums map of 10 files whose values match neither live nor the rollback tree (8 of 10 differ), so a reader can take a stale checksum as the deployed bytes.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-S57",
      "NFRA_OPLGTW-Z-W15-S64",
      "NFRA_OPLGTW-Z-W15-S65"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S57, #Z-W15-S64, #Z-W15-S65",
        "remediations/REMEDIATION_v8.md"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S36",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-06T08:38:00Z",
    "one_line": "Record: this seat's r20 guards W1-W3 held on the deployed host, with the non-restricted ADMITTED arm on the installed code; Z-W15-S58 advanced to REMEDIATED on this seat's 8 of 8 runs of test_ogx2_ac01.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "A never-widen half's guards are read on the deployed host by the CVO; the CVO advances remediation clocks only on its own corroborating read.",
    "world_is": "W1: r20_phaseB_step9_live_md5.out reads 96 of 96 identical before the act. W2: r20_phaseB_verify_after.out reads VERIFY PASS 8 of 8; on the INSTALLED code LOGIN_ARMS reads 10 of 10, including the non-restricted verified identity ADMITTED (307, tier_graph_tools, the arm proving the fail-closed backstop does not fire in production), the analyst identity ADMITTED, the restricted identity REFUSED 403, one gw_login per request (8 for 8), and no address, token or state leaked; ENGINE_ARMS 3 of 3; .env 51 names with 51 of 51 hashes equal; 65 tools. W3: git diff --stat 2c27f3a795 CLOUD -- infra/aws/ec2/opal-gateway reads empty. Z-W15-S58: after OG-fl-1, this seat ran tests/test_schwab_export_stream.py::test_ogx2_ac01 eight times on CLOUD, each in its own process: passed 8, failed 0.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_NFRA_OPLGTW~15/r20_phaseB_step9_live_md5.out, r20_phaseB_verify_after.out",
        "git diff --stat 2c27f3a795 CLOUD -- infra/aws/ec2/opal-gateway: empty (this seat, ~08:3xZ)",
        "8 runs of test_ogx2_ac01 by this seat on CLOUD, ~08:3xZ: passed 8 of 8"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Record only: this row opens and adjudicates no investigation item."
  }
]
```

-- 3.0.0_SA_CVO~O
