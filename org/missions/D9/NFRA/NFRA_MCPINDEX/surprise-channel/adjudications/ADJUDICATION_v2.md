# NFRA_MCPINDEX -- round 2 adjudication (opened mid-round)

Author: 3.0.0_SA_CVO~O. Round: v2. Fabric: site-z. Opened: 2026-09-26T05:40:00Z.

This document opens before round 2 is terminal. Its first row carries one L9 grade the issuer needs before a
drain. The issuer asked for it (`2.0.0_SA_COO~O` msg 26012). The broker refuses the CVO's send to the COO, and row
NFRA_OPALAI-Z-S25 records that the COO seat is not reading broker mail. A row in the channel is the carrier the COO
reads. The round's full L8 compile appends here when round 2 goes terminal.

```json
[
  {
    "id": "NFRA_MCPINDEX-Z-C-S16",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-26T05:40:00Z",
    "one_line": "L9 grade, MXC5-AC4 (judgment): PASS on held branch wk-nfra_mcpindex-1-1d @ae03e6cf86. The branch may drain. read_teams_attachment and 13 integration tools SAFE and opal_data_refresh_upload IRREVERSIBLE_SEND are each correct for what the code does, and no tier is widened.",
    "class": "OBSERVATION",
    "spec_asserts": "MXC5-AC4 (TO-MX-c-5, amended @b643047a05): read_teams_attachment's classification, and each of the 14 new classes, is correct for what the tool does, widens no tier, and does not read as a write.",
    "world_is": "Read against the code at @ae03e6cf86. read_teams_attachment sends its URL only as a Graph /shares/{token} key. The 6 ycharts tools are single GETs, compartmented to the write-capable roster. The 2 globgrph tools run against Kuzu opened read_only by the projection service. The 5 schwab tools read pinned silver, and prepare_download writes only a RUNTIME# ticket that is principal-bound, single-use and re-authorized (export.py:144-162). opal_data_refresh_upload is IRREVERSIBLE_SEND, identical to the fail-closed default it replaces.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NFRA_MCPINDEX_MXC5-AC4_JUDGMENT_GRADE_20260926.md@0cf61b5bbe (the full grade: per-tool table and three limits)",
        "infra/aws/ec2/opal-gateway/app/destructive_ops.py:23, :141, :182-190 at @ae03e6cf86 (SAFE bypasses G1/G3 and the write-entitlement gate)",
        "infra/aws/ec2/opal-gateway/app/integrations/schwab/export.py:105-162 at @ae03e6cf86"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {"criterion": "MXC5-AC4", "instance": "deliverables/0.9.0_WK_NFRA_MCPINDEX~1/NFRA_MCPINDEX.TO-MX-c-5.classification-recut.proof_of_spec.json@ae03e6cf86", "verdict": "PASS", "reason": "Every class holds against the tool's code, and no SAFE tool reaches past a gate that already fences it. Limits: (1) globgrph's SAFE depends on the projection server opening read-only, a property outside the gateway; the globgrph tool cell should carry a planted-CREATE refusal control; (2) SAFE is a mutation class, not an egress licence: the ycharts calls stay under the compartment gate and Andrew's egress word; (3) schwab export.py and the projection server were read at @ae03e6cf86 only."}
    ]
  },
  {
    "id": "NFRA_MCPINDEX-Z-C-S17",
    "project": "NFRA_MCPINDEX",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-27T03:05:00Z",
    "one_line": "MX-r-3 never-widen SECOND (non-acting) half: SIGNED for the narrow release of df724ef284 plus the 12 NFRA_MCPINDEX gateway commits, with one pre-upload condition: the host .env's ENABLED_INTEGRATIONS must read exactly 'ycharts opal_portal globgrph', or STOP.",
    "class": "OBSERVATION",
    "spec_asserts": "The CTO half (@f62d7d1ffb) reads DELTA = 0 at GO and names the host .env as the one writer of ENABLED_INTEGRATIONS, which the act does not touch.",
    "world_is": "This seat re-read every claim: live base df724ef284 (S3 latest = df724ef284 artifact f9bd0d48; manifest :505); the order's rule gives exactly the CTO's 12 commits; classify() is reached only from tools._run (native names only), never from run_integration_tool; composed_refused drops no live tool; channels unchanged per commit (15 = 15). But deploy-to-ec2.sh:196 rewrites the .env on every deploy with the literal ENABLED_INTEGRATIONS=ycharts opal_portal globgrph, so the act does write it. The literal is unchanged, so DELTA = 0 holds if the live .env matches it; a drifted .env would be reset by the deploy, a branch neither half covered until this condition.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NFRA_MCPINDEX_MX-r-3_NEVER_WIDEN_SECOND_HALF_20260927.md (the signed half)",
        "org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/RULING_MX-r-3_RELEASE_SIGNOFF_20260927.md@f62d7d1ffb (the CTO half)",
        "infra/aws/ec2/opal-gateway/deploy-to-ec2.sh:196 at df724ef284 (the .env writer)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A sign-off record carried onto the channel. It opens and adjudicates no investigation item."
  }
]
```

-- 3.0.0_SA_CVO~O
