# /ws-charter cycle 0009 — F6 branch-head-marker HEAD oracle (PRD v0.4.3, CVO stress-test P0)
**archetype:** SCRIBE
**secondary_archetypes:** VALIDATE

## Classification
- **Class:** REPAIR-AMENDMENT (CVO /verify-channel stress-test finding, trigger (a) mechanical-untruth-to-reality).
- **CVO finding:** stress-test verdict `dc06744c6` (Andrew-direct), MCP 153629Z. P0: F1's HEAD definition
  ("newest warehouse metadata.json by S3 mtime", shared by kuzu_nessie_load + _provenance commit-distance)
  empirically conflated two commit lineages — Lambda commit c454b6cd's row absent from the served state the scan
  selected; the canonical surface auto-refreshed onto the wrong lineage and reported current. The authoritative
  head lives in Nessie's catalog (DynamoDB), unreachable from dev boxes (private DNS — the same wall that
  deferred TO-F3's live demo). AC10(b) FAILS pending fix; AC10(a)+(c)-mechanism PASSED under 8-way storm.

## Ruling (the architecture half routed to me; AE owns the operational P0/P1s)
**HEAD oracle = writer-stamped branch-head marker** (PRD v0.4.3 F6):
- Every successful Nessie-commit writer (2a nightly Fargate / 2b Lambda / F3 opt-in — ALL in-VPC where Nessie
  REST is reachable) stamps `warehouse/_branch_head.main.json` post-commit: Nessie commit hash, commit ts,
  per-table current metadata locations/snapshot-ids, writer id. Atomic PUT; monotonicity-guarded overwrite.
- Readers key BOTH the commit-distance check AND kuzu_nessie_load's source selection off the marker — fixing
  the staleness oracle and the load-level lineage conflation with one mechanism. mtime-scan RETIRED as oracle;
  marker-absent ⇒ loud HEAD-ORACLE UNKNOWN, no churn.
- REJECTED: (a) Nessie-REST exposure for the query path — couples every dev-box query to tunnel/ALB
  reachability + security surface; the TO-F3 live-demo decision stays a SEPARATE call; (c) single-lineage
  enforcement — fights Iceberg's per-table metadata layout instead of fixing the oracle.
- **Default-flip disposition: STANDS, labeled.** Canonical remains strictly fresher than the retired tarball
  default; nightly 2a full-derive heals daily; F5 keeps verification off the graph. Mandatory interim label
  until F6 lands: `HEAD-ORACLE PROVISIONAL (mtime-scan; may under-detect incremental advances)` on the
  commit-distance line — known failure mode labeled, never silent.
- AC10(b) re-cert post-F6 on the c454b6cd-class scenario; NEW AC10(d) = marker-oracle demonstration
  (in-VPC 2b commit → dev-box query BEHIND via marker → refresh serves the state WITH the committed row).

## Inbox/sweep notes
Ground-truth at this cycle: default-flip committed (DEFAULT_DB_PATH = CANONICAL_DB_PATH, live); TO-F3 closed
(live-demo deferred in-VPC); NFRA_COT_TOOLING closed (6bc1f1ce3 + manifest 939b903fe); F-series wave complete
pending this F6 follow-on. AE 0.7.0 holds CVO's operational P0/P1s (lineage fix, no-egress coverage, kuzu
reader-lock collisions) — the F6 contract gives the P0 its architectural shape.

## Compiler Tools
| Tool | Run? | Why / result |
|---|---|---|
| comp-* (any) | NO | Doc-only PRD amendment; the empirical basis is CVO's stress-test (8-way storm + c454b6cd lineage evidence) + my prior same-day reads of _provenance/_canonical/kuzu_cli. Implementation mandates ride the F6 TO (COO decomposition; AE lane). |

## Follow-on
COO decomposes TO-F6 (marker writer-side in 2a/2b/F3 + reader-side _provenance/kuzu_nessie_load + interim
PROVISIONAL label lands FIRST as a micro-patch); CVO holds AC10(b) re-cert + AC10(d); TO-F3 live demo decision
(in-VPC vs SSM-tunnel) remains open and SEPARATE.
