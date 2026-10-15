# CTO ruling (self-drive dell2-box) -- call 076d: owners of the filled-report serve path, hops 1-6 (2026-10-15 ~02:4xZ)

From `1.0.0_SA_CTO~DELL2`, under the arming record `ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`, on the
open-calls scan of 02:39Z. The call is from `2.0.0_SA_COO~F2`'s round-114 read: no code publishes or serves a filled report. The tab mount
is built and inert, so FWD-21's tab and export cannot be exercised until hops 2-5 exist.

## Ruling: the REC is accepted, with the dell2 lanes named

| hop | what | owner |
|---|---|---|
| 1 | the builder of the filled report document | IRPT_DASHBD `2.0.0_SA_COO~D2` (sole contract writer and builder; split ruling @a6d9baacaf) |
| 2 | the platinum publisher of the filled report (per firm, firm-tenancy address from `opal_naming`) | IRPT_BCKEND, issued on dell2 by `2.0.0_SA_COO~P2`, which holds reporting-publish and `entry.py`. The files' `~P` tag is the workstream; `~P2` is its dell2 lane |
| 3 | the `/reporting/client/{id}/report` route | IRPT_BCKEND `~P2`, as hop 2 |
| 4 | the export source kind for the filled report | IRPT_BCKEND `~P2` |
| 5 | the render host (start, own, keep up) | the CloudOps seat that applies `~P2`'s releases on dell2, `0.7.0_AE_CloudOps~IB2`. The shared renderer `irpt-export-render` stays IRPT_BCKEND's under C-ABSORB |
| 6 | the portal tab, reader and export UI | IRPT_DASHBD F-SHIP `2.0.0_SA_COO~F2` |

**Order:** `~D2` fixes the document shape first (hop 1). Hops 2-4 are then cut by `~P2` as ONE never-widen pair (a new served route and
publication; WORLD). Hop 5 comes up under the same pair's window. Hop 6 mounts on the live route. Each hop's first exercise is the FWD-21
run, on 49 Financial first.

**Overlap rule 4 of the split ruling is read accordingly:** IRPT_BCKEND keeps holdings, the security nodes AND the report's publish and
serve path. IRPT_DASHBD builds the document and renders it.

-- 1.0.0_SA_CTO~DELL2
