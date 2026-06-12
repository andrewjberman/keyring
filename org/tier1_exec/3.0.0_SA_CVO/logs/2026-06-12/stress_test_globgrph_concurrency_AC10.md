# CVO Stress Test — NFRA_GLOBGRPH §2b concurrency/freshness contract (Andrew-direct, 2026-06-12 ~14:45–15:35Z)

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE
**Verdict: AC10(a) PASS · AC10(c) mutex/atomic-swap PASS · AC10(b) end-to-end FAIL — one P0 (write/read HEAD divergence), two P1s (no public-API egress; Kuzu reader lock collisions), three P2s. The freshness *plumbing* works; the thing it serves is not yet the truth.**

Method: live injection probes (SNS topic create/delete; S3 bucket create/delete — all throwaway, all cleaned up), an 8-way concurrent comp-kuzu storm against a genuine BEHIND state, CloudWatch log traces of the 2b Lambda, and direct Iceberg metadata/table reads. No production resources touched; no manufactured gold runs.

## What PASSED (live, reproduced)

1. **AC10(a) provenance surface** — every comp-kuzu query prints DB identity / source / snapshot-id pins / built-at+age / Nessie HEAD distance; UNKNOWN-VINTAGE fires loud on a manifest-less DB (`kuzu_ac7.db`). BEHIND detection is *honest*: it correctly read "current" through two of my own tooling errors (I aged non-operative manifest fields — the check keys on `nodes_metadata_last_modified` vs S3 LastModified; and my first "HEAD ADVANCED" was a name-sort artifact — metadata files are `00000-<uuid>`, lexical order ≠ time order. Both owned, both corrected with time-sorted listings).
2. **AC10(c) mutex + auto-refresh under 8-way concurrency** — against a genuine BEHIND-by-1: exactly ONE worker detected staleness, acquired `kuzu_nessie_db.rebuild.lock` (observed live 15:30:12Z, released 15:30:26Z), rebuilt to temp, atomic-swapped, re-stamped the manifest with the new pin; 9 subsequent headers read current; waiters served the winner's build; no half-built reads, no duplicated rebuild.
3. **2b event pipeline + delete-propagation mechanics** — SNS CreateTopic arrived in ~2.5min, extracted + class-mapped; DeleteTopic hit the delete branch (`DELETE_PROPAGATE event=DeleteTopic` 15:17:05Z) and committed in one atomic Nessie commit with zero AWS API calls. The S3 object-grain resurrection class is correctly fenced (DeleteObject churn now drops instead of fabricating bucket writes — pre-deploy's constant `nodes_written=1` per batch WAS the resurrection bug writing; post-deploy it correctly stopped).

## FINDINGS

### P0 — write-path and read-path disagree on Nessie HEAD (data-integrity class)
The probe bucket create (15:21:48Z) produced `ICEBERG_COMMIT nodes_written=1` (15:27:09Z) and a new newest-by-mtime metadata file `00000-c454b6cd` (15:27:10Z). But:
- A direct `StaticTable` scan of that exact metadata returns **1157 rows, probe row ABSENT**;
- the file's own snapshot summary says `operation=append, added-records=1, total-records=2` — the commit lineage believes the entire table holds **2 records**;
- the auto-refreshed canonical (pinned to c454b6cd, built 15:29:45Z) serves 1157, probe absent — **the surface refreshed onto a "fresh" vintage that does not contain the change the writer reported committing.**
Mechanism hypothesis (for AE/CTO, not asserted): the Lambda's REST-catalog commits are landing on a different table lineage/branch than the one the nightly writes and the loader reads, with both lineages interleaving metadata files in the same S3 `metadata/` directory — so "newest metadata.json by mtime" (the HEAD definition shared by `kuzu_nessie_load` and `_provenance._nessie_commit_distance`) conflates them. The scan-vs-summary contradiction within one file needs a spec-level dig.
**Blast radius bounded:** the 02:00Z nightly (Item-2a) full-overwrite remains the source-of-truth reconciler, so the served graph self-heals daily. But until fixed, the incremental freshness contract — commit → HEAD-advance → rebuild serves the change — does not hold end-to-end for ANY class, and BEHIND-by-N counts are computed against an ambiguous HEAD. **For AE 0.7.0** (owner) + **CTO** (the §2b contract's HEAD definition may need to be "ask Nessie REST for the branch head," not "newest metadata by mtime" — which is also unreachable from dev boxes; design tension to rule on).

### P1 — 2b bounded-derive has no public-API egress: incremental coverage is S3-only
`vpc_endpoints.tf` provisions only s3+dynamodb (gateway) and cloudwatch-logs endpoints; the updater is VPC-attached (`item2b.tf:140-142`) with no NAT. Live-observed: lambda-class derive timeout 14:32Z (its own UpdateFunctionCode event), sns-class timeout 15:09:57Z (my probe: `BOUNDED_DERIVE_FAIL ... err=Connect timeout ... sns.us-east-1.amazonaws.com`). Every non-S3 create/update costs a 3s timeout then silently drops — HEAD never advances on the classes agents change most (lambda/iam/sns/sqs), hollowing rebuild-on-HEAD-advance precisely where it matters. Present since 2b shipped; NOT a regression from today's deploy. Options (AE/CTO cost call): 4 interface endpoints (~$30/mo), NAT, or extend the zero-API fabricate-from-event pattern beyond S3 (free, lower fidelity, matches the existing LIVE-INCREMENTAL drift-class contract where the nightly reconciles).

### P1 — concurrent readers collide on the Kuzu file lock
`kuzu_cli.py:55` opens `kuzu.Database(db_path)` without `read_only=True` → every query takes a writer-class lock. 4/4 storm runs killed 1-of-8 workers with `RuntimeError: Could not set lock on file`. Ten agents querying the canonical surface will hit this constantly. Fix: read_only connections for the query path (rebuilds keep the write-open under the mutex). **For AE.**

### P2s
- `ICEBERG_COMMIT nodes_deleted` counts match-KEYS not affected rows (`commit_batch` n_del = arn∪id set — logged "deleted=2" for one topic that deleted 0 actual rows). Log server-side affected rows.
- Unimplemented-class derives skip at DEBUG (`lambda_function.py:319`) — invisible at INFO; a coverage gap reads as silence. Promote to INFO with a per-batch skip census.
- `extract_arns_from_event` cannot extract logs/events/cloudfront/kms-class creates (e.g. CreateLogGroup carries only `logGroupName`) — even with egress fixed, those classes are 2b-blind. Census + extend, or document as nightly-only classes.

## Probe ledger (all cleaned up)
`/opal/cvo/concurrency-stress-20260612` log group (created 14:58Z, deleted 15:19Z) · `cvo-globgrph-stress-probe` SNS topic (15:07–15:14Z) · `opal-cvo-stress-probe-20260612` bucket (15:21–15:34Z; its create is the P0 reproduction — the divergent commit c454b6cd; its delete fired a final delete-propagation commit for AE's investigation trail).

## AC10 disposition
- **AC10(a): CERTIFIED PASS** (provenance header live on all invocation paths, UNKNOWN-VINTAGE loud).
- **AC10(c): mechanism CERTIFIED PASS** (single-rebuild mutex + atomic swap + honest BEHIND under 8-way concurrency) — but certified against a HEAD whose definition the P0 shows is ambiguous; re-affirm after the P0 fix.
- **AC10(b) (canonical serves the latest committed change): FAIL pending P0.** TO-F3 live demo remains deferred (Nessie REST unreachable from dev boxes — AE's own session log concurs; same constraint blocks an SSM-side exercise this session).

— 3.0.0_SA_CVO
