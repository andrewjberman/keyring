# Deploy-Completion Ledger -- ETFS_CANON Dynamo lane (table + fan-in)

**Opened:** 2026-06-25T20:16Z | **Agent:** 0.5.0_AE_OpalETL | **Authority:** COO GO 193400Z (resume 201426Z; CTO design-bless 193246Z; inf-fix gate cleared)
**Status:** CLOSED -- LIVE + verified 2026-06-25T20:21Z (tag etfs-canon-v1.0.0).
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
- 20:18Z committed + build (sha lpv7nDc) + init. plan 11-add/0-change/0-destroy -> safe-apply HALTGT -> Apply complete 11 added -> 0-diff "No changes".
- 20:21Z LIVE-verify: fan-in {"full":true} wrote 356 rows / 3 partners; dynamo scan=356; spot inflection#DIVZ@06-24=$15.23M (canonical). Firm-sep: role grants opal-data-etfs/daily/* read + list + table write ONLY, ZERO firm-bucket (comp-iam GRANTED + live get-role-policy). tag etfs-canon-v1.0.0 + push. CLOSED. Signaled DE (rows live) + CVO (cert).
