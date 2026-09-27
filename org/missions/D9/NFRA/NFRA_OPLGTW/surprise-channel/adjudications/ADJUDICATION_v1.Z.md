# NFRA_OPLGTW -- adjudication (site Z), opened mid-round

Author: 3.0.0_SA_CVO~O, OPLGTW's CVO leg since the re-seat @6fba157e76. Fabric: site-z. Opened: 2026-09-27.

This file opens before the round is terminal. It carries a governance verdict the gate's owner needs now. The round's
L8 compile, which covers all rows of `investigations/INVESTIGATION_v1.md` including the rows inherited undispositioned
from 2026-09-15..20, appends here when the round goes terminal.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-27T15:05:00Z",
    "one_line": "Governance verdict on row Z-S1's fork: '# pipeline-override:' does NOT bypass LIMB 6. The L4-R sign-off limb runs even under an override; the override keeps its pipeline-shape effects. OG-e-1 stands, because the half is now SIGNED.",
    "class": "OBSERVATION",
    "spec_asserts": "CLAUDE.md 27 L4-R: LIMB 6 refuses a newly-added task order against a PRD with an unsigned half, and names no override.",
    "world_is": "to-pipeline-gate.py:2690-2711 returns ([], notes) for the whole file when the override line is present, before any limb runs. OG-e-1 carries the line, so LIMB 6 never ran on it. The gate's own texts (:511, :1994) document the override for pipeline shape only (coverage; an additional order into an open round).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_GOVERNANCE_VERDICT_PIPELINE_OVERRIDE_VS_LIMB6_20260927.md",
        ".tools/to-pipeline-gate.py:2690-2711, :511, :1994",
        "CLAUDE.md:44; org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md:283-290"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A verdict record. Z-S1 stays ARMED with its disarm_owner (1.0.0_SA_CTO~O) until the limb runs under an override; the disarm criterion is in the verdict."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-27T16:40:00Z",
    "one_line": "OG-e-2 never-widen SECOND (non-acting) half: SIGNED for the narrow release of 110d93fb73 + 06eff3b73f + 744e4468e1. DELTA = 0 at GO (EMAILDENY 0 of 162, measured by this seat). The 503-on-unreadable-store branch is a ruled, signed new dependency; no deny record is signed.",
    "class": "OBSERVATION",
    "spec_asserts": "CTO half @4f83d1a820: N = 4 writers, EMAILDENY 0 of 162, the 503 branch signed deliberately (R2-k call 2), and a condition to re-read EMAILDENY = 0 at GO.",
    "world_is": "Live = 110d93fb73 (S3 latest ETag 00356afd). The served files are app/{access_state,data_entitlement,server,token_broker}.py from 06eff3b73f only; the 2 other OPLGTW-worker gateway commits since the base touch tests/runbook only. The guard sits only in the /login+/sprint branch and the legacy /callback; /mcp is untouched. An empty email cannot reach the check (get_user_email fails closed first; the callback email comes from signed state). This seat's consistent scan at 16:40Z: 162 items, EMAILDENY 0, other POLICY# 10. The one reader of the record is data_entitlement.email_denial.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NFRA_OPLGTW_OG-e-2_NEVER_WIDEN_SECOND_HALF_20260927.md",
        "org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~O/RULING_OG-e-2_RELEASE_SIGNOFF_20260927.md@4f83d1a820",
        "infra/aws/ec2/opal-gateway/app/server.py and data_entitlement.py at 06eff3b73f"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A sign-off record carried onto the channel. It opens and adjudicates no investigation item."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-27T19:35:00Z",
    "one_line": "Post-act read of OG-e-2 against this seat's signed half (Z-C-S2): inside the signed radius. The code equals the signed change set, the host bytes equal fe94911257, and the tool list and ENABLED_INTEGRATIONS are unchanged. The CTO's GO re-read of EMAILDENY is absent from the ledger; this seat's own read shows it held.",
    "class": "OBSERVATION",
    "spec_asserts": "Z-C-S2 and the CTO half @4f83d1a820 signed a DELTA = 0 release of 110d93fb73 + 06eff3b73f + 744e4468e1, conditioned on EMAILDENY = 0 re-read at GO, the ENABLED_INTEGRATIONS literal, and mcportal a3bff71ffa.",
    "world_is": "S3 latest = opal-gateway-fe94911257 (ETag d67a7435, 18:43:41Z). 110d93fb73..fe94911257 over app/ + deploy-to-ec2.sh = the 4 signed files; 3 are byte-identical to 06eff3b73f, and server.py's change set equals OG-e-1's 41 lines exactly. SSM read by this seat: BEFORE 29bd1824 at 18:11Z (before the 18:43:43Z deploy) -- ENABLED_INTEGRATIONS literal, 46 tools; AFTER 822648a2 at 18:50Z -- the same 46 tool names, the same literal, host md5 of the 4 files = git show fe94911257. mcportal a3bff71ffa in ledger L1. Ledger closed @d3b0d04b4d. EMAILDENY: the completion record does not mention the GO re-read the CTO half made a condition. This seat's consistent scan at 19:33Z reads 167 items, EMAILDENY 0, and C6 gives no role policy DeleteItem, so it was 0 at GO. The condition held, but it was evidenced after the act and not by the deployer.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws ssm get-command-invocation 29bd1824-f1dd-43ad-8cd3-3e5a4ffd45e1 / 822648a2-5d61-47cd-be87-db2006ba1bba on i-07dccb1615503ac99",
        "org/critical_paths/change_management/20260927T1815Z_nfra-oplgtw-email-deny-release_deploy_completion.md (branch wk-NFRA_OPLGTW-8-e2 @d3b0d04b4d)",
        "git diff 110d93fb73 fe94911257 -- infra/aws/ec2/opal-gateway/app"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A post-act verification record. The missing GO re-read is noted for the round's L8 (a condition met but not evidenced by the act); it opens no hazard."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S4",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-27T21:35:00Z",
    "one_line": "OG-s-1 never-widen SECOND (non-acting) half: SIGNED. Release 6a98a0553a = live fe94911257 + deploy-to-ec2.sh (one .env key, SPRINT_VIEW_ALLOWED_EMAILS, one entry = the owner). The narrowing reaches /sprint* only, exactly Andrew's word.",
    "class": "OBSERVATION",
    "spec_asserts": "Andrew-direct @785fc4d71f: /sprint for Andrew only. COO ask 20260927T212047Z; order @95e499c916.",
    "world_is": "S3 latest = fe94911257 (d67a7435). The diff over the gateway is deploy-to-ec2.sh only (+2/-1). Parsed .env literal: 27 -> 28 entries, 9 -> 9 %s placeholders, one key added, no other value changed. The roster entry equals OTP_MAILBOX / MASTER_ADMIN_EMAILS / DASHBOARD_OWNER_EMAILS. Readers: config.py:103-104 (lower+strip) and sprint_view._allowed, called by sprint_page and sprint_archive only; /login and /mcp never read it. All identity providers lower-case the email, so the owner cannot be locked out by case. The GO step reads the host .env before the act (46 tools, the ENABLED literal, roster count 0).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NFRA_OPLGTW_OG-s-1_NEVER_WIDEN_SECOND_HALF_20260927.md",
        "infra/aws/ec2/opal-gateway/deploy-to-ec2.sh at fe94911257 and 6a98a0553a",
        "infra/aws/ec2/opal-gateway/app/sprint_view.py:173-182, :222; config.py:103-104; identity.py at fe94911257"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A sign-off record carried onto the channel. It opens and adjudicates no investigation item."
  }
]
```

-- 3.0.0_SA_CVO~O
