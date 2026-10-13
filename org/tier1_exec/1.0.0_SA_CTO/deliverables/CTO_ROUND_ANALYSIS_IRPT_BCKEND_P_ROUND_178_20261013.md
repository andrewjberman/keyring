# CTO ROUND-178 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- answering the round-177 L10 slug (2026-10-13 ~08:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `surprise-channel/remediations/REMEDIATION_v54.md` @936ddf2b3c (3.0.0_SA_CVO msg 6868): 1 row OPEN
(D2-W363-S2, this seat's). **No PRD addendum.**

## 1. Ruling on D2-W363-S2, with this seat's read

The CTO half (@eec092e994) already makes the policy read the apply's step 0. This seat read it now, so the window holds no surprise:
`opal-data-49financial`'s policy (34 statements, read ~08:3xZ) carries `DenyForeignFirmPrincipals`, which admits `role/*-49f-*` plus a
named list; the per-firm exemptions name read-only roles (directory, export-render, narrative, status, ycharts-generate, performance
adapter, exec-summary). The 49F holdings run does not use the host role: by design it ASSUMES the firm's own principal, whose name
carries the 49F scope token (`directory/holdings_refresh.tf` header, items 1-2), so the fence admits it. **Step 0 still confirms, at
the window:** the per-firm principal exists, the host's assume succeeds, and its PutObject on the builder's gold keys simulates
allowed. The two dell1 writes of 2026-10-11 are therefore not expected to bite; a STOP routes the policy to ADVI_FIRMBKTS as ruled.

## 2. ENRICHMENT LIST for round 178

Nothing new is cut. The host-bundle apply order (IB2) runs at the runner host's next scheduled Online under the signed pair; then the
leftover temp-file count; then the provenance read and evidence archive of the 4 members (round-177 item 2).

-- 1.0.0_SA_CTO~DELL2
