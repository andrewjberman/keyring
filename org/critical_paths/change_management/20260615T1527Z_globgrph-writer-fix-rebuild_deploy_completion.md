# Deploy Completion Record
**Date opened:** 2026-06-15T15:27:11.623194+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260615T171403Z
**Deploy:** NFRA_GLOBGRPH P0: incremental_updater parent=None writer-fix + full rebuild-from-source (silent 2.7d freeze since marker 2026-06-12T16:15:51Z)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 10.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | writer parent-linkage fix committed+pushed to CLOUD | hash pushed | writer fix + linear-ancestry guard committed 90ebf40e6, pushed to origin/CLOUD (5a014dfea..90ebf40e6); ds-commit-gate clean; VALIDATION-PENDING (deploy gates on 4-case real-Nessie proof) | CLOSED 20260615T154552Z |
| L2 | activation | incremental_updater Lambda redeployed via Terraform with the fix | 0-diff apply + CodeSha256 | A1 fix + fix(a) deployed to opal-globgrph-incremental-updater via Terraform/safe-apply; 0-diff verified; CodeSha256 pkXq/5K4oFqMsCHBoSOPawejwJmgj3qbn1jpVDPNmMs= (A1+fix-a). Mapping kept enabled=false (paused). | CLOSED 20260615T165829Z |
| L3 | verify | writer produces parent-correct snapshot: FRESH marker stamp advances PAST 2026-06-12T16:15:51Z (NOT rc=0) | served marker readback | VALIDATION (i) PASSED on real Nessie: served marker advanced 2026-06-12T16:15:51Z -> 2026-06-15T16:41:25Z, writer_id=incremental_updater, multiple clean commits (ICEBERG_COMMIT nodes_written=1 -> MARKER_STAMPED), 0 orphan/error. CTO sign-off CLOSED (i)+(ii). | CLOSED 20260615T165829Z |
| L4 | verify | full rebuild-from-source lands a fresh parent-correct main HEAD + served HEAD advances | served _branch_head.main.json + graph HEAD | DEFERRED to NFRA_GLOBGRPH.json forward-tracker (COO 5a433df13) per COO decision (b) 171315Z: incident CLOSED on unfreeze; L4 derive-rebuild -> current-state marker is NON-URGENT forward-work (graph unfrozen + serving advancing marker; needs the TF-managed globgrph-derive CodeBuild project), NOT a stranded deploy. | CLOSED 20260615T171402Z |
| L5 | verify | stale SQS+DLQ sample-verified re-derivable THEN purged | sample + queue depth readback | DEFERRED to NFRA_GLOBGRPH.json forward-tracker (COO 5a433df13): L5 purge stale SQS/DLQ is GATED on the ingest-filter going LIVE (CTO architecture lane; Andrew pinned INCLUDE-S3-code carve-in) -> sequenced forward-work, not stranded. | CLOSED 20260615T171402Z |

## Log

- 20260615T152711Z OPENED by 0.7.0_AE_CloudOps with 5 leg(s)
- 20260615T154552Z LEG L1 closed: writer fix + linear-ancestry guard committed 90ebf40e6, pushed to origin/CLOUD (5a014dfea..90ebf40e6); ds-commit-gate cl
- 20260615T165829Z LEG L2 closed: A1 fix + fix(a) deployed to opal-globgrph-incremental-updater via Terraform/safe-apply; 0-diff verified; CodeSha256 pkXq
- 20260615T165829Z LEG L3 closed: VALIDATION (i) PASSED on real Nessie: served marker advanced 2026-06-12T16:15:51Z -> 2026-06-15T16:41:25Z, writer_id=inc
- 20260615T171402Z LEG L4 closed: DEFERRED to NFRA_GLOBGRPH.json forward-tracker (COO 5a433df13) per COO decision (b) 171315Z: incident CLOSED on unfreeze
- 20260615T171402Z LEG L5 closed: DEFERRED to NFRA_GLOBGRPH.json forward-tracker (COO 5a433df13): L5 purge stale SQS/DLQ is GATED on the ingest-filter goi
- 20260615T171403Z CLOSED -- all 5 legs proven

---

## CLOSE NOTE (0.7.0_AE_CloudOps, per COO decision (b) 171315Z; CTO doctrine-concur 170051Z)

**Root cause (H4, CTO-confirmed):** the orphan-detector a613084cb (shipped ~06-12 16:32Z) asserted `produced.snapshot.parent_snapshot_id == prior HEAD` -- an Iceberg-Hadoop invariant that is **null BY DESIGN** on this Nessie-REST-backed table (every commit writes a fresh single-snapshot metadata; lineage lives in Nessie's commit graph). Master diagnostic: EVERY pre-detector HEAD-advancing commit (06-09 onward) + the served 06-12 good HEAD all had parent=null. So the detector false-rejected EVERY valid commit from both writers since deploy = the 2.7-day silent freeze. **NOT corruption** -- the writers never broke; valid writes were blocked from stamping, never lost. ~ZERO data impact (consumers read the valid 06-12 HEAD throughout).

**Fix (A1, CTO ruling 162100Z):** dropped the false parent-assertion in BOTH writers (incremental_updater commit c4e1a072f + derive_runner), rely on Nessie branch-ref CAS (the months-proven off-branch guarantee; a successful main commit IS chained, a stale-base 409s+retries). Reverted the two wrong-premise interim fixes (txn writer / linear-ancestry guard). Kept commit-failure LOUD. + fix(a) 850183bfa (short-timeout the in-VPC SNS clients).

**Validation:** (i) PASSED on real Nessie -- marker advanced 06-12T16:15:51Z -> 06-15T16:41:25Z, multiple clean commits, 0 orphan. (ii) accepted via code-inspection (handler stamps only after commit_batch returns; a 409-exhaust raises -> no stamp) + the freeze-itself-is-the-empirical-reject-proof + re-raise confirm. CTO re-enable SIGN-OFF fully closed.

**Loud-channel reframe (corrected hardening B2, CTO f4c047a09):** the VPC reaches only S3/DDB (gateway) + CloudWatch-LOGS (interface) -- no SNS/monitoring endpoint, no NAT. So the in-VPC LOUD channel = CloudWatch-LOGS metric-filter on the ERROR log line -> metric -> alarm -> SNS, + an out-of-VPC marker-S3-age checker (observe the served artifact) -- NOT SNS/PutMetricData from the writer.

**Incident closed on the UNFREEZE** (half-landed-deploy NEVER-law satisfied: A1 deploy landed + validated + signed off + served-state restored). FORWARD-WORK tracked in `org/projects/NFRA_GLOBGRPH.json` (COO 5a433df13), NOT held as an open RED incident:
- L4 derive-rebuild -> full current-state marker (non-urgent; needs the TF-managed standing globgrph-derive CodeBuild project -- closes a reproducible-build debt). AE lane.
- L5 purge stale SQS/DLQ (gated on the ingest-filter going LIVE).
- RE-ENABLE the incremental SQS ESM: gate = sign-off DONE + ingest-filter LIVE + backlog PURGED. (Ingest charter: Andrew pinned INCLUDE S3-artifact code carve-in; CTO finalizing the filter spec.)
