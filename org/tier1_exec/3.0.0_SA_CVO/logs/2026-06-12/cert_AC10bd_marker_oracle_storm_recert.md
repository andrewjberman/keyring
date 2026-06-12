# CVO Re-Certification — NFRA_GLOBGRPH AC10(b) + AC10(d) post-F6, integrated storm final

**archetype:** VALIDATE
**Certifier:** 3.0.0_SA_CVO · **Date:** 2026-06-12 ~16:20Z · **Verdict: AC10(b) RE-CERTIFIED PASS · AC10(d) CERTIFIED PASS (one labeled simulation caveat) · integrated 8-way storm CLEAN — the §2b freshness/concurrency contract is now verified end-to-end on the marker oracle. AC10 a/b/c/d ALL CERTIFIED.**

## The live marker chain (real, in-VPC, first stamp)

CVO fired the AE-staged probe-bucket delete (`opal-ae-tof6-probe-20260612`, empty, creator-intended, Andrew-confirmed) at 16:15:17Z:
- 16:15:41Z `DELETE_PROPAGATE event=DeleteBucket` (24s event latency)
- 16:15:51Z `ICEBERG_COMMIT` (one atomic Nessie commit)
- 16:15:52Z **`MARKER_STAMPED hash=59b0a6a9… nodes_snap=2373504567134934158`** — first live writer stamp (v0.1.11)

Marker content verified: Nessie commit hash, committed_at ISO, writer_id=incremental_updater, both tables' metadata_locations + snapshot_ids.

## AC10(d) — marker-oracle demonstration: PASS

1. **Current leg:** comp-kuzu header reads `Nessie HEAD: current (pin == marker HEAD)` — reader keyed off the marker, mtime retired.
2. **BEHIND leg:** aged the local manifest pin against the REAL marker → `BEHIND Nessie HEAD (pin X != HEAD 2373504567134934158 (writer=incremental_updater, committed_at=…))` — staleness named with writer attribution at the moment it matters.
3. **Refresh leg:** auto-refresh rebuilt from the **marker's** metadata_location, restamped, post-refresh header current.
4. **Loud-absent leg:** pre-stamp, header read `HEAD-ORACLE UNKNOWN (no branch-head marker)` — never silent.

*Labeled caveat:* the BEHIND state was induced by aging the local pin against the real marker (no snapshot-advancing organic commit landed in-window; the delete commit stamped an unchanged snapshot). The chain components are each live-real; the composite with a real advancing commit self-demonstrates on tonight's 02:00Z nightly (2a stamps post-rebuild per CTO's container-rebuild order 984773e0e) — recommend a one-line morning confirm, not a held cert.

## AC10(b) — committed state served: RE-CERTIFIED PASS (with a correction to the original repro)

The served canonical contains the latest committed incremental row — `arn:aws:s3:::opal-data-bd` with `snapshot_ts=1781278026414` (= the 15:27:06Z commit's batch_ts) — confirming commit → HEAD → serve holds for rows that are actually written.

**Correction to the record (CVO owns):** the original P0 repro's "committed row absent" conflated two defects. The probe bucket's row was never written at all — `CreateBucket` is not ARN-extractable (the create-coverage P2), so `nodes_written=1` at 15:27 was an organic opal-data-bd upsert, which IS served. The real and now-fixed defect was mtime-not-HEAD (orphan parent=None metadata conflation — AE's root-cause). The P0 stands as filed (the oracle was structurally wrong); the "write path loses rows" implication is RETRACTED — no evidence any committed row was ever lost.

## Integrated final storm — "manages storms with ease": VERIFIED

Aged pin + 8 simultaneous comp-kuzu agents in one shot (marker-BEHIND + mutex + atomic swap + read_only readers all exercised together):
- **Rebuilds: exactly 1** (marker-keyed) · **Errors: 0** · **Lock collisions: 0** (was 1-of-8 pre-fix `35c9d4f14`, 4/4 repro) · **8/8 workers: one distinct count** (1157) · post-swap restamp clean.

Combined with the 15:30Z storm (real BEHIND-by-1, mutex observed live) and the standalone 8/8 read_only re-verify: three storm exercises, zero inconsistent reads across 24 concurrent worker invocations.

## Standing residuals (owned, none contract-blocking)

- derive_runner ECR container rebuild TODAY pre-nightly (CTO 984773e0e order; AE owns) — 2a then stamps the marker nightly.
- Writer-hardening P1 TO (orphan parent=None snapshot production on the Lambda overwrite path) — CTO spec.
- P1-A egress option-c (fabricate-from-event extension) — COO GO'd, deferred.
- P2s: create-event extract coverage (the CreateBucket class above), nodes_deleted keys-vs-rows, line-319 DEBUG skip.
- graph_changes materialization — roadmap item 4 (binding reqs attached, v0.4.2).

Probe ledger: opal-ae-tof6-probe bucket deleted (AE's artifact, handed off); my globgrph probes/cvo-ac10d-event-probe.txt object put+removed (bucket not in trail data-event selectors — noted: globgrph bucket changes only reach the graph via the nightly).

— 3.0.0_SA_CVO
