# IRPT_ANLREQ -- decomposition, round 19 PORTAL READERS, round 6, workstream YR (issuer 2.0.0_SA_COO~Y2)

**Input:** release 5 of `irpt-status` was rolled back after 61 minutes because the portal's history reader refused an answer the service had begun to serve (rows `IRPT_ANLREQ-D2-S43`, `-S44`); its first pair named no portal reader. The reader's release (S33) adds four finding codes to the upload door's answers (`ACCOUNT_COLUMN_SEVERAL_VALUES`, `HEADER_ROW_REPEATED`, `SHEETS_NOT_READ`, `TOTAL_ROW_PRESENT`; the live reader emits none of them) and 23 correction-word codes to `uploads.py`. `AR-y-191` says in its own `not_read` that the words a portal shows for each code were not measured. The two-leg pair names the portal readers of the upload door's answer, or it repeats release 5's defect.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-202` | the portal readers of the upload door's answer at the PROD and DEV commits, each with its key policy; the door answers of the pinned and the moved pair passed through them | the worker's deliverables | LOCAL (git reads of the portal checkout, scratch copies outside the tree; no network write, nothing deployed) |

## Edges and chains

- None. M = 1 chain.

fanout: 1 of 1 chains, cap 8, reason: one independent read-and-run cell.
