# NFRA_OPLGTW -- OG-ap-23 served read graded against the CVO's conditions (site Z)

Author: 3.0.0_SA_CVO~Z. Round: v28. Fabric: site-z. Recorded: 2026-10-16 ~09:4xZ.
**Input:** `2.0.0_SA_COO~O` msg 34884 (acked); `deliverables/0.7.0_AE_CloudOps~Z/CODE_SERVED.json` @2d97278481.
**Live:** `EC2_MANIFEST.json` `deployed_commit` `3d5c9c8bf1dea0854c9b59d58b83fdf9dcb480e4`, `deployed_at` 2026-10-16T09:14:19Z. The
release worktree's HEAD `ed5d4541a8` is only the deploy record on it: `git diff --stat 3d5c9c8bf1 ed5d4541a8` over
`client_adapter_smartx.py`, `client_core.py` and `data_entitlement.py` is empty.
**Instrument:** a harness run on the host over SSM (`849da95a`, Success, rc 0) that imports the INSTALLED app.
- The harness's md5 on the host, `d07e2f9c4d79...`, equals the committed `ap23_served_harness.py` (this seat's md5sum).
- The tool calls run through the real `decide()`, adapters and env. Principals are built stand-ins, not a login through the ALB.
- The audit sink is stubbed, with 80 rows captured.

## The grade

| condition (where set) | reading | grade |
|---|---|---|
| `client_admission` (my OG-ap-23 re-cut half) | all three values hold. The unprofiled non-admin stand-in is refused with code `entitlement_denied` on **5 of 5** client tools, `reads_on_refusal_after_all_five` 0. The master_admin stand-in is served (`master_code` null). `master_roster_entries` 1 | **MET** |
| C1, one real AssumeRole (OG-ap-24 half) | `assume_role_real` true. `c1_detail`: caller before `opal-gateway-role`, assumed `gateway-smartx-read-role`, ARN from the installed env | **MET** |
| C2, SmartX two-firm negative arm (OG-ap-24 half) | `smartx_two_firm_arm` true, read through the installed tools as master_admin. Firm A (`49financial`) resolves 3 SmartX candidates and reads 12 holdings rows (enveloped). The other canonical firm, naming the **same** account ref, reads 0 rows (not firm A's). The same last4 resolves 0 SmartX candidates under the other firm | **MET, bounded** (below) |
| `via_internal_reader` (my OG-ap-26 half) | `classification_identity`: configured, client used, session role `gateway-global-internal-reader-role`, instance role `opal-gateway-role` | **MET** |
| release triggers (read, not my conditions) | registry 76 to 103 (delta 27, 0 missing), per tool 27 of 27 good, non-Opal refused with 0 reads per tool, `.env` 64 keys with 6 of 6 reader keys present, `/health` 200 | consistent |

**C2's bound, stated:**
- **What it tests:** the served arm tests the fence by the firm INPUT. SmartX serves only `49financial` (`client_adapter_smartx.py:72`,
  `FIRMS = (49financial,)`), so the other-firm call is refused or emptied by routing before the row filter runs.
- **What it does not test:** that a `49financial` resolve or holdings read excludes the other firms' advisors who share the SmartX
  objects on real data. That filter (`_firm_allocations` `:127-146`: advisor_ids whose rows all name the firm, keyed on
  advisor_id, never advisor_crd) is proven by the build cell's planted two-firm arm. The served read adds that the 3
  candidates and 12 rows came back through that filter.
- **What closes it:** a served count of firm A's candidates whose advisor maps to a different firm (expected 0). I carry this as
  an enrichment and do not hold the grade on it.

## Rows

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S75",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-16T09:45Z",
    "one_line": "OG-ap-23 served read graded: client_admission MET (unprofiled non-admin refused on 5 of 5 client tools, 0 reads; master_admin served), C1 MET (real AssumeRole of gateway-smartx-read-role from opal-gateway-role), C2 MET bounded (the other firm reads 0 rows on firm A's ref; the real-data row filter is proven by the build cell's planted arm), via_internal_reader MET. Z-S162 is closed on the served side.",
    "class": "OBSERVATION",
    "spec_asserts": "CVO halves: OG-ap-23 re-cut (client_admission all three values before close), OG-ap-24 (C1 one real AssumeRole; C2 SmartX two-firm negative arm), OG-ap-26 (via_internal_reader in the served read).",
    "world_is": "CODE_SERVED.json @2d97278481, SSM 849da95a Success on the host running the installed 3d5c9c8bf1 (manifest deployed_at 09:14:19Z; harness md5 equal to the committed file). client_admission_detail: nonadmin_code entitlement_denied, nonadmin_refused_per_tool 5 of 5, reads_on_refusal_after_all_five 0, master served. c1_detail: caller_before opal-gateway-role, assumed gateway-smartx-read-role, succeeded. smartx_two_firm_detail: firm A 3 SmartX candidates, 12 rows; other firm on the same ref 0 rows, not firm A's; other-firm resolve 0 SmartX candidates. classification_identity: session_role gateway-global-internal-reader-role. Bounds: stand-in principals (not an ALB login), audit sink stubbed, C2's other-firm call fenced by routing (SmartX serves 49financial only), so the real-data row filter rests on the build cell's planted arm.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-S162",
      "NFRA_OPLGTW-Z-S163"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.7.0_AE_CloudOps~Z/CODE_SERVED.json @2d97278481 (body and _ssm read by this seat)",
        "deliverables/0.7.0_AE_CloudOps~Z/ap23_served_harness.py:407-456 (the C2 arm), md5 d07e2f9c4d79 equal to the host's",
        "EC2_MANIFEST.json at HEAD: deployed_commit 3d5c9c8bf1, deployed_at 2026-10-16T09:14:19Z",
        "C:/tmp/og-rel-code @3d5c9c8bf1 app/client_adapter_smartx.py:61-80, :127-146"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a defect: every CVO condition on OG-ap-23/24/26 reads met on the live release. Z-S162 closes on the served side (Z-S163 carried the code side). Enrichment carried: a served count of firm A SmartX candidates whose advisor maps to another firm (expected 0)."
  }
]
```

-- 3.0.0_SA_CVO~Z
