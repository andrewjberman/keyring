# Deploy-Completion Ledger -- ETFS_CANON Dynamo lane (table + fan-in)

**Opened:** 2026-06-25T20:16Z | **Agent:** 0.5.0_AE_OpalETL | **Authority:** COO GO 193400Z (resume 201426Z; CTO design-bless 193246Z; inf-fix gate cleared)
**Status:** OPEN -> (in progress)
**Change:** Deploy the ETFS_CANON AE Dynamo lane (new etfs-canon TF root): opal-etfs-ownership-daily DynamoDB table (PK client_etf/SK date + GSI-etf + GSI-client) + etfs-canon-fanin Lambda (daily-slice -> Dynamo upsert, internal reader-IAM read-etfs-daily + write-table only, zero firm-bucket) + daily schedule. The daily slices are now ALL canonical (inf P0 re-backfill) -> the fan-in reads correct data.

## Plan
1. [x] Finalize skeleton: main.tf (provider+backend etfs-canon/tfstate) + status tags active + source-map entry + artifact_key aligned (etfs-canon/).
2. [x] OPEN this ledger.
3. [ ] Commit; build-and-upload fanin (pipeline=etfs-canon); init new root.
4. [ ] plan (ADD-only) -> safe-apply HALTGT -> apply.
5. [ ] 0-diff; LIVE-verify: real fan-in invoke writes Dynamo rows from the canonical slices; comp-iam firm-sep (read etfs/daily + write table, zero firm-bucket).
6. [ ] CLOSE; tag etfs-canon-v1.0.0 + push. Signal DE (rows live for the monthly producer) + CVO (firm-sep cert).

## Rollback
New root, net-new resources (table + role + lambda + schedule). terraform destroy the root; no existing dependency. Dynamo table empty until the fan-in runs.

## Log
- 20:16Z opened. Skeleton finalized (main.tf/backend/source-map/artifact_key). Committing + building.
