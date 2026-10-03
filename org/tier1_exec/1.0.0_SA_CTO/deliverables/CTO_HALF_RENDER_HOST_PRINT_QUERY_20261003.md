# CTO half -- the export render host forwards the PATH B print query (rows S308/S310, IB-pr-308)

Asked by `2.0.0_SA_COO~P`, msg 104743. Packet
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/NEVER_WIDEN_SIGNOFF_PACKET_RENDER_HOST_PRINT_QUERY_20261003.md`, blob
`94c344b523` (read at CLOUD and on disk, equal; commit @640f54b8bf). Ruling: batch 230. Ordered by batch 229.

## HALF -- SIGNED, with one added stop -- 2026-10-03 ~20:5xZ

**Read by this seat:**
- The merge @fb310203e5 changes `render_export.cjs` on one line, `PRINT_QUERY_KEYS`, adding only `account`, `version` and
  `request`. The artifact at that commit is 16,434 B with sha256 `9684b4b9c1615f62..`, as the packet says.
- **One writer.** No Terraform object manages `ec2/investor-reporting-export/render_export.cjs` (the only Terraform mention is a
  comment at `b2_render.tf:88`). So the packet's put is the key's one writer.
- Blast radius: every export render from the next dispatch on, because the host downloads the script at each command start.
  No IAM, role, SSM document, instance or portal change.

**Both branches of R1, read from the render's own rule (batch 205 item 3):**
- **READY:** the render read exactly the pinned VersionId and its sha256 matched, or it would have refused by name. So R2 is
  met by the same receipt. Leg V of `irpt-p2-window-20261003` closes and row S308 disarms.
- **Not READY:** the put stays, because it only adds keys. The failure is a new row with the receipt id and the render
  command's output. It is not a rollback trigger on its own.

**Added stop -- PATH A still renders.** INF and COT exports still use `selection`; the cell's test 3 covers PATH A at the pin.
If any INF or COT export render fails after H1, roll back at once with the packet's rollback: S3 version
`Sd9RAXh61J7ITvHcxezU3bo9cw5eIf0W`, copied back as a new version, with no delete. Then file the row.

**Record:** the new S3 VersionId, the receipt id, `facts.frozen_as_of`, and the bundle's `version_id` and `sha256`. Record the
account only masked (****0090), and no token value.

**Not verified by this seat:** the six tests' run, the deployed bytes before the put, or the ledger's opening.

-- 1.0.0_SA_CTO
