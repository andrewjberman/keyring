# NFRA_OPALAI -- round 1 adjudication (site Z), opened mid-round

Author: 3.0.0_SA_CVO~O. Round: v1. Fabric: site-z. Opened: 2026-09-26T18:25:00Z.

This document opens before round 1 is terminal. Its first two rows carry two decisions the issuer needs now. MCP send
is down fabric-wide (0.0.0_AB_MSTR~Z, 17:15Z), and the CVO's send gate reaches only the CTO. The issuer reads this
channel. The round's full L8 compile appends here when round 1 goes terminal. These rows adjudicate no investigation
item.

```json
[
  {
    "id": "NFRA_OPALAI-Z-C-S1",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-26T18:25:00Z",
    "one_line": "OA-g-2 never-widen SECOND (non-acting) half: SIGNED for the narrow release df724ef284 on the live base c5f8099440. DELTA = 0 at GO, re-measured at ~18:1xZ: 0 of 141 grant-table items carry portal_channels.",
    "class": "OBSERVATION",
    "spec_asserts": "Andrew's arming term: served output moves only under a never-widen sign-off with a CTO half plus a second, non-acting half. The CTO half is @321a726fc6. The GO job at 21:07Z deploys only if the CVO half reads SIGNED at HEAD.",
    "world_is": "This seat re-read the blast radius itself: 5 gateway files and nothing else in the tree; the base is the live release (artifact ETag fc23bd5d, manifest c5f8099440, /mcp 401); v1.1 records parse unchanged (data_entitlement.py:233-237); 0 portal_channels records and 0 data_entitlement records in a full read-only scan; the order's guards read /health on the host and compare the tool list before and after.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NFRA_OPALAI_OA-g-2_NEVER_WIDEN_SECOND_HALF_20260926.md (@073447e387; the signed half)",
        "org/missions/D6/NFRA/NFRA_OPALAI/deliverables/1.0.0_SA_CTO~O/RULING_OA-g-2_RELEASE_SIGNOFF_20260926.md@321a726fc6 (the CTO half)",
        "task-orders/NFRA_OPALAI.TO-OA-g-2.portal-grant-release.md@2ae3e0a96d :59, :66-68, :70"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A decision record carried onto the channel. It opens and adjudicates no investigation item."
  },
  {
    "id": "NFRA_OPALAI-Z-C-S2",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-26T18:25:00Z",
    "one_line": "Governance verdict on NFRA_OPLGTW contract v1.2: KEEP. It is additive and optional and moves nothing served (0 portal_channels records). Ratification stays with OPLGTW's contract owner. Carried rule: a verdict that parks a class of acts also withdraws the open authorizations of that class.",
    "class": "OBSERVATION",
    "spec_asserts": "Fork msg 26105: OA-g-1 amended the OPLGTW contract v1.1 -> v1.2 at 07:01Z on a 03:33Z authorization, after this seat's 04:01Z verdict parked CTO acts on OPLGTW (row Z-S30). Keep or revert?",
    "world_is": "The contract reads v1.2 with portal_grant at HEAD. A missing portal_grant means v1.1. The running gateway hard-codes the dimension and does not read the file per request. The first served use is OA-g-3, which already needs its own two-half sign-off. The laptop CTO's 17:19Z no-objection covers the OA-g-2 diff, not the contract.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_GOVERNANCE_VERDICT_OPLGTW_CONTRACT_V1_2_20260926.md (@073447e387)",
        "INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-S30",
        "org/standards/NFRA_OPLGTW_CONTRACT.json at HEAD (version 1.2)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A verdict record. Z-S30 is dispositioned at the round's L8, not here."
  },
  {
    "id": "NFRA_OPALAI-Z-C-S3",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-27T01:35:00Z",
    "one_line": "Post-act reads of the two served moves this seat's records covered. OA-g-2: live release is df724ef284 as signed. OA-g-3: one portal-only query grant is ACTIVE, and it needed no two-half sign-off. C-S2's sentence saying it did is corrected on its own bytes.",
    "class": "OBSERVATION",
    "spec_asserts": "C-S1 signed OA-g-2 for df724ef284 on the live base c5f8099440 only. C-S2's record said OA-g-3 'already needs its own two-half never-widen sign-off'.",
    "world_is": "OA-g-2: S3 opal-gateway-latest ETag f9bd0d48 equals the df724ef284 artifact; the c5f8099440 artifact (fc23bd5d) is kept; EC2_MANIFEST.json:505 deployed_commit df724ef284; /mcp 401; the deploy entry is closed. OA-g-3: this seat ran g3.AC1.sh and g3.AC2.sh at ~01:30Z, both PASS: items=159 policy=10 active_profiles=1 portal_only_active=1 operations=[['query']]. OA-g-3's write set is one named principal's POLICY record, written through the operator command on Andrew's word naming person and scope. CLAUDE.md section 5 exempts 'an act whose write set is a literal key list the actor controls', so C-S2's sentence was wider than the law.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "task-orders/NFRA_OPALAI.TO-OA-g-2.portal-grant-release.md closed @20bf1189bd",
        "task-orders/NFRA_OPALAI.TO-OA-g-3.alyssa-portal-grant.md closed @2d3317fd02",
        "deliverables/2.0.0_SA_COO~O/round1/checks/g3.AC1.sh and g3.AC2.sh (read-only scan, counts only)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_GOVERNANCE_VERDICT_OPLGTW_CONTRACT_V1_2_20260926.md (correction on the superseded sentence)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A verification and correction record. It opens and adjudicates no investigation item."
  }
]
```

-- 3.0.0_SA_CVO~O
