# CVO Assessment — Graph Platform Live-State Status Brief (week kickoff 2026-06-15)

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, DIAGNOSE
**Requested by:** 1.0.0_SA_CTO (Andrew-direct). **Method:** ground-truthed against
live AWS/S3 (SQS, Lambda, CloudWatch, S3 marker), not the graph's self-report (F5).

## Headline (one line)

**The global-graph committed HEAD has been FROZEN at 2026-06-12T16:15:51Z for ~2.7
days and is failing SILENTLY** — the incremental writer produces `parent=None`
orphan snapshots that the (correctly-working) CAS guard rejects, so no increment
can land; ~37.5k events are queued + ~15.2k dead-lettered; and NOTHING alarms on
it. The 06-12 "orphan fix" added *detection*, not a *writer* fix.

## Per-subsystem verdict

| Subsystem | Verdict | Live evidence |
|---|---|---|
| Incremental write path (Item-2b updater → Nessie) | **RED** | HEAD frozen since 06-12T16:15:51Z; `ICEBERG_COMMIT_ORPHAN` on every invocation |
| Critical-surfaces monitoring (D8) | **RED (gap)** | freeze is fully silent — no alarm, 0 SNS subs, Lambda Errors=0 |
| comp-kuzu reader / marker oracle | **AMBER** | reader healthy + auto-refresh works, but "current" is current-vs-a-FROZEN-marker (false comfort) |
| F6 branch-head marker (S3) | **GREEN** | live, snapshot-IDs match pin exactly — consistent anchor (just frozen) |
| Kuzu canonical DB (kuzu_nessie_db) | **GREEN** | 1157 nodes/2150 edges, pin==marker, auto-refreshed clean |
| Stitch surface (kuzu_stitch_db) | **AMBER** | 3088 nodes == baseline (no regression) but 73.2h stale-by-age |
| AC10 a/b/c/d certs | **HELD-BUT-STALE** | certified 06-12 on the 16:15:52Z first-stamp; do NOT reflect post-18:52Z freeze |
| NFRA_GRAPHS D7/D8 | **AMBER** | D8 SNS+IAM live but metric-alarms absent / 0 subs = monitoring half-landed |

## The RED, mechanism-specific

**What's happening (live):** `opal-globgrph-incremental-updater` (ESM Enabled,
batch 100, deployed 2026-06-12T18:52:05Z, CodeSha `nzkYaTwK...`) is consuming the
`opal-globgrph-incremental-events` SQS queue (invocations 37→99/30min, ramping;
Errors 0; Throttles 0). It DERIVES graph deltas correctly (CloudWatch logs:
`DERIVED arn=...positions_cube/*.parquet`), then the Iceberg→Nessie commit fails
every time: `ICEBERG_COMMIT_ORPHAN attempt=1..3/5 ... produced snapshot parent=None
!= expected_parent=<id> (off-branch / concurrent-fork; increment not on main HEAD)`
(two distinct request-ids confirm it is systematic, not isolated).

**Why HEAD is frozen:** `lambda_function.py:484-506` (TO-P1 `a613084cb`) is a
fast-forward-only CAS + orphan self-detection: it requires the produced snapshot to
build on the current HEAD; a `parent=None` produced snapshot == off-branch orphan,
so it LOUD-fails rather than stamp a marker onto orphaned state. **The guard is
working as designed — it is preventing corruption.** The unfixed half is the
*writer*: the pyiceberg overwrite is emitting snapshots with no parent linkage. The
06-12 P1-B work (`a613084cb`/`2c7d1dd98`, deployed 18:52Z) shipped the DETECTOR;
the writer-residual it was meant to catch is still live. Net: committed HEAD has not
moved past 16:15:51Z since that deploy.

**Backlog/data state (live):** main queue `ApproximateNumberOfMessages` = 37,530
(+669 in-flight), oldest-message age growing (~1,000s → ~3,452s across the 2h
window = consumer cannot drain what it cannot commit). DLQ
`opal-globgrph-incremental-events-dlq` = 15,262 (24h retention → these dead-lettered
in the LAST 24h; maxReceiveCount=3 = each failed 3×). Every event since
16:15:51Z is either queued or dead-lettered — none is in the committed graph.

**Why it is SILENT (the monitoring RED):** (1) Lambda `Errors` metric = 0 because
the orphan path uses SQS partial-batch-failure (function returns 200, reports the
record as failed) — structurally invisible to the Errors metric. (2) The orphan
path does NOT `sns:Publish`; only the SUCCESS path calls `_publish_marker_advance`
(`lambda_function.py:695`). (3) The `opal-critical-surface-alerts` SNS topic has
**0 subscriptions**. (4) Live CloudWatch alarms on the globgrph namespace = only 2
(S3-request *volume*, both OK) — **no DLQ-depth, no SQS-oldest-age, no
marker-staleness alarm.** (5) comp-kuzu's provenance header reads `current
(pin == marker HEAD)` — true, but the marker is the frozen one, so the header
conveys false comfort. A reviewer trusting any single self-report would never see
this. This is the half-deploy / silent-FATAL class the no-half-deploy NEVER-law
was written against.

## Debtscan-P1 relevance (flagged per ask)

The isolated-node + stitch-coverage pass would run against a graph frozen at 06-12;
the stitch DB (73.2h stale) is built off that frozen state. Any "isolated node" or
"coverage gap" finding produced now is against stale HEAD, not live estate —
**defer the debtscan-P1 graph pass, or caveat it explicitly, until HEAD unfreezes.**

## Forward-look (parked, no work)

FalkorDB registered as a future research spike on my radar per CTO: evaluate vs the
Nessie/Kuzu surface for agent-concurrency + speed; built-in MCP server is the draw.
Andrew-flagged not-immediate; CTO will PRD when it surfaces. No action now.

## Recommendations (per driver, priority-ranked)

**For AE (owner — infra/Lambda; the RED):**
- **P0** — Root-cause the `parent=None` writer in `incremental_updater`: why the
  pyiceberg overwrite emits off-branch snapshots (concurrent-fork / table-load HEAD
  not being read as the append base). The guard is correct; the fix is the writer
  linking each produced snapshot to current main HEAD. Verify the fix against the
  SERVED state — a *new marker stamp* advancing past 16:15:51Z — not rc=0 (banked
  stale-deploy / served-artifact class).
- **P0** — Decide the 15,262-DLQ redrive: are these unique graph mutations (must
  redrive after the writer fix) or idempotent/duplicate (drainable)? 24h DLQ
  retention means they age out — decide before loss is moot.

**For AE + CTO (monitoring gap — the silent-failure RED):**
- **P0/P1** — Add absence-alarms, not activity-signals: CloudWatch alarms on DLQ
  `ApproximateNumberOfMessages` > 0, main-queue `ApproximateAgeOfOldestMessage`,
  and marker staleness (HEAD-not-advanced-in-N-hours). Subscribe a real endpoint to
  `opal-critical-surface-alerts` (currently 0 subs). The current "marker-advance
  SNS publish on success" cannot detect a frozen writer — silence ≡ idle today.

**For CTO / CVO:**
- **P1** — AC10 a/b/c/d cert currency: the 06-12 cert rests on the 16:15:52Z
  first-stamp; the marker-watch armed for "re-cert on first stamp" never refired.
  Re-validate AC10(d) marker-oracle storm AFTER the writer fix produces a fresh
  stamp. Not a broken cert — lapsed currency.

**For CTO / COO:**
- **P2** — Stitch staleness (73.2h) self-clears on the next derive→Nessie→kuzu
  nightly *only if* HEAD unfreezes; otherwise the nightly stitches a frozen graph.
  Sequence the writer fix before relying on the next nightly.

## What you should have asked but did not

Whether the graph platform's alerting is structurally capable of detecting a
*frozen* HEAD at all. The D8 design alerts on marker-ADVANCE (a positive,
success-only SNS publish) and on the nightly scan — both are activity signals. A
writer that fails every commit produces NO advance, NO Lambda error (partial-batch
semantics), and NO alarm; it looks identical to a quiet/idle fabric. The entire
2.7-day freeze + 15k-DLQ accumulation was invisible until live ground-truthing. The
gap is not a missing threshold — it is that the platform has no *negative* health
signal (staleness/absence), only positive ones. Until an absence-alarm exists, the
graph can silently freeze again the moment a writer regression ships, and the next
discovery will again be by accident. That structural inversion (alert-on-presence
vs alert-on-absence) is the highest-value thing to fix, above the specific orphan
bug.

— 3.0.0_SA_CVO, 2026-06-15 graph-platform live-state assessment
