# ADVI_FIRMBKTS -- DECOMPOSITION (L5) -- WORKSTREAM TRADEFORM, ROUND 8: THE TICKET API'S TRADE-FORM ACCESS TO THREE FIRM BUCKETS (the fence owner's one apply)

```json
{
 "project": "ADVI_FIRMBKTS",
 "directive": "D8",
 "macro": "ADVI",
 "fabric": "dell1",
 "decomp_version": "v8-tradeform",
 "step": 5,
 "prd_ref": "org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md",
 "order_ref": "laptop 1.0.0_SA_CTO msg 109703 (relayed by 0.0.0_AB_MSTR~DELL1 msg 6786): cut ONE ADVI_FIRMBKTS task order for 0.7.0_AE_CloudOps~TF; pair ledger/NEVER_WIDEN_TCKT_TRADE_FORM_FIRM_BUCKET_ACCESS_COO_HALF.md @5c3504c184 and the CTO half @1c8af1a3fc",
 "author": "2.0.0_SA_COO~B1",
 "round": 8,
 "workstream": "TRADEFORM",
 "rectangle": "The ticket API role opal-ticket-api-role may Get and Put objects under portal/<firm>/state/ticket_attachments/trade-form/ in the three firm buckets, through the fence's own registry rows; the browser origins that upload the form are admitted by one CORS rule per bucket; the two lgic buckets render the Allow beside every scoped Deny. ONE targeted apply by a laptop CloudOps lane, read back on all three buckets. Serves TCKT_VNEXT FWD-10 (Andrew P2, due 2026-10-24; this apply targeted for 2026-10-20).",
 "cells": 1,
 "chains": 1,
 "join_cells": 0,
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~B1` (dell1). A workstream is a SCOPE, not a round (CLAUDE.md rule 27): round 8's decomposition (`ADVI_FIRMBKTS_DECOMP_R8.md`) and the READYHALT workstream stay frozen; this workstream has a disjoint write surface (one lgic Terraform file, one new CORS file, one record).

## Workstream TRADEFORM -- the cell

| cell | serves | owned files | depends on | slot, class | risk | at the cut |
|---|---|---|---|---|---|---|
| `FB-n-1` the one scoped apply of the trade-form pair (lookup edit, three CORS rules, three regenerated policies), read back | no FWD of this PRD: the fence owner's act for TCKT_VNEXT FWD-10 (ruling @ee287446e1, step 4) | `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` (one line), a new CORS file in the same root, `deliverables/0.7.0_AE_CloudOps~TF/TRADEFORM_FENCE_RECORD.json` | the signed pair (both halves at the current bytes), the laptop CTO's GO, M02 sequencing on `opal-data-inflection` | `0.7.0_AE_CloudOps~TF` seat order (laptop) | WORLD | staged |

Chain: {`FB-n-1`}. No worker cell: the act is a Terraform apply by a seat, and a Dell writes no bucket policy.
