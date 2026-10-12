# MDPF_SECCLASS -- re-filed rows (dell1)

<sweep_watermark>2026-10-12T02:35Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-12T02:35:00Z. On 1.0.0_SA_CTO ruling 4d96 @b91d51e6a4 (relay msg 4217): two rows written on 2026-10-07 in the
worktree C:/dev/cvo_secclass_r9 never landed and their ids were reused on the trunk. They are re-filed here under fresh dell1 ids
(MDPF_SECCLASS-S60 -> D1-S29 in INVESTIGATION_v1.md; MDPF_SECCLASS-C-S78 -> D1-C-S4 below), content unchanged, so the worktree can go.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-C-S4",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-12T02:35:00Z",
    "one_line": "D1-S29, re-filed S60 (OBSERVATION/INERT, the advisor Book view 403) dismissed: explained as the local dev proxy bypassing CloudFront's origin check; not the walker, not the product.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-D1-S29"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The 403 is the laptop's local dev server, not the walker and not the product: vite.config.ts at fc18e50b proxies /api/scoped/partners to the API Gateway (7k3ed8px20.execute-api, :142-143) instead of CloudFront, and opal-portal-authorizer logs 'Origin verification FAILED - request did not come through CloudFront' for exactly those requests, before reading the token. The walker's token verifies as role admin, allowedFirmIds ALL. Real users on the deployed site go through CloudFront, so this refusal is not a FWD-1 break. FWD-1's live read moves to the deployed DEV site (Andrew's act). The local-proxy defect belongs to the portal's dev tooling and is routed to 1.0.0_SA_CTO~DELL1 for its owner.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_S60_WALKER_403_CAUSE_20261007.md @f77d1c8d7e (laptop 3.0.0_SA_CVO): authorizer log lines 16:05:31-41Z (Token verified role admin / Dev superadmin ALL; then Origin verification FAILED for the two platinum-summary probes); 5 such FAILED lines all day, all the walker's",
        "vite.config.ts at fc18e50b: /api/scoped/advisor-intelligence -> CloudFront d2n2nzpeqf34ge (:102-104); /api/scoped/partners -> execute-api 7k3ed8px20 (:142-143)",
        "this seat's read of opal-users-v2 USER#usr_opal_ui_walker: role admin, firmId opal-capital, userType Dev",
        "investigation row MDPF_SECCLASS-S60 (3.0.0_SA_CVO)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The 403 is the laptop's local dev server, not the walker and not the product: vite.config.ts at fc18e50b proxies /api/scoped/partners to the API Gateway (7k3ed8px20.execute-api, :142-143) instead of CloudFront, and opal-portal-authorizer logs 'Origin verification FAILED - request did not come through CloudFront' for exactly those requests, before reading the token. The walker's token verifies as role admin, allowedFirmIds ALL. Real users on the deployed site go through CloudFront, so this refusal is not a FWD-1 break. FWD-1's live read moves to the deployed DEV site (Andrew's act). The local-proxy defect belongs to the portal's dev tooling and is routed to 1.0.0_SA_CTO~DELL1 for its owner.",
    "notes": "RE-FILED under a fresh id on ruling 4d96 (@b91d51e6a4). Original: MDPF_SECCLASS-C-S78 in ADJUDICATION_v10, commit ad06fb5487 (laptop, 2026-10-07T18:06Z), never landed; the trunk reuses MDPF_SECCLASS-C-S78 for the S55 dismissal. It adjudicates the re-filed observation MDPF_SECCLASS-D1-S29 (was S60). Content otherwise unchanged."
  }
]
```
