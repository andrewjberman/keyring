# ADVI_COTBKF decomposition -- ROUND 61 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11 ~06:0xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_CROSSBOX_XB-20261011T055236Z-0989_SHARED_INFRA_CRM_SCOPE_SELECTOR_20261011.md` @27ba4d3769 (msg 4216), answering cross-box call XB-20261011T055236Z-0989
from site Z. The ruling names this issuer the owner and says: one cell, cut now, ahead of anything else it issues.

**The defect is this project's (cell CB-d-4).** `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` line 197 selects the firm that holds the restricted Commonwealth CRM
prefix as "the ONE managed FIRM row that carries masters", through `one()`. On 2026-10-09 commit 5f962296ae (IRPT_DASHBD) gave the
inflection row a true `masters` value. Issuer read at HEAD: the managed set is 2 rows and both carry `masters`, so `one()` fails
and every `shared-infra` plan fails on every box (site Z measured the failed `init` and `plan`; this box has not run one).

**Ruled (sections 1 to 5 of the ruling):** the registry edit stands; the selector reads an EXPLICIT attribute on the firm's scope
row and keeps `one()`; the attribute's name and shape are proposed under rule 24; a new key on `scopes.json` is a change to the LGIC
canon's schema, whose owner is the laptop `1.0.0_SA_CTO`, and the proposal goes to that seat through the managers BEFORE it lands;
the proof is `init` and `plan` succeeding with 0 changes to the CRM restricted-prefix statements, the break-glass role and the firm
bucket policy. Verified DELTA=0 needs no hold and no apply. A moved resource is a STOP.

**Rule 24.** Domain: the ruling's items 2 to 5 -> two cells on one chain (the edit, then its plan proof).

## Measured constraints (issuer)

1. **Nothing lands on `box/dell2` before the laptop CTO accepts the attribute.** `box/dell2` is integrated to `CLOUD` by a schedule,
   so the worker's branch is NOT drained until (a) the proposal is accepted and (b) the plan proof reads 0. The plan runs against
   the worker's worktree.
2. **No apply.** Neither cell runs `terraform apply`. The proof is a plan.
3. **No firm token is typed in the `.tf`** (the naming gate refuses it); the firm is named only by the registry row that carries
   the attribute.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bi-1` | the rule-24 record for the attribute; the attribute on the one scope row that holds the CRM prefix; the selector reads it under `one()` | FWD-7 | WORLD | none | `0.9.0_WK_ADVI_COTBKF~88` |
| `CB-bi-2` | `init` and `plan` of `shared-infra` on the worker's worktree succeed; 0 changes to the CRM statements, the break-glass role and the firm bucket policies; no apply | FWD-7 | SERVED | `CB-bi-1` | `0.7.0_AE_CloudOps~CB2` |

**Risk class of `CB-bi-1`:** WORLD is the gate's floor for an order whose `<paths>` name an infrastructure path (spine v3.19 L6); the
cell itself runs no terraform and makes no AWS call.

**Fan-out:** `1 of 1 chains, cap 8` (two cells, in order). `CB-bi-2` is issued now and starts when `CB-bi-1` is complete on its
branch.
