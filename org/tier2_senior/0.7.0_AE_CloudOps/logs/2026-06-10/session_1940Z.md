# 0.7.0_AE_CloudOps — Session Log 2026-06-10 ~16:38Z -> ~19:40Z

## Session summary

Fresh session (Andrew-launched). /watcher self-heal + LD-0177 queue pull.
Shipped 3 NFRA_GLOBGRPH TOs (all RAVC2-ACCEPTED same evening) + 2/3 of
NFRA_COSTAWS W1 + the Andrew-direct 409-storm cost-banking dispatch.
Caught and fixed TWO latent production bugs, both landed before tonight's
02:00Z nightly. Stand-down ordered by COO ~19:35Z (LD-0176).

## Startup

- Re-registered (PID 25920); persistent inbox Monitor armed (one benign
  exit-143 mid-session, lossless re-arm: task bswjt7l3p).
- Launch-prompt LD-0082 `/work 20m` cron deliberately NOT re-armed —
  superseded by LD-0157/LD-0175 + Andrew-direct cron kill earlier today.
  Single ad-hoc /work pass instead; flagged the stale launch template.
- 26 inbox messages triaged: all pre-handled by prior ~B session.
- LD-0177 queue (12 NFRA TOs) received 1744Z; ACK'd with R1 ground-truth
  (R1 was already 100% per COO's own 1449Z ACCEPT; AC2 lag-bound only).

## Shipped (chronological)

### NFRA_GLOBGRPH.ICEBERG-409 — COMPLETE, ACCEPTED 1803Z
- `e574a0c7c` (tag globgrph-v0.1.6): `_overwrite_with_retry` in
  derive_runner — table RE-LOADED per attempt (stale in-memory metadata
  409s forever), exp backoff 2s/30s cap/50% jitter/5 attempts
  (env-tunable), CommitStateUnknown retried (overwrite idempotent),
  `_ensure_table` create-race guard. 4-case mock smoke PASS.
- Deployed via CodeBuild 052acccf -> ECR :latest (20260610-175421);
  ECS verify task 0a9119b0 exit 0 (1176 nodes / 2539 edges clean cycle).

### NFRA_COSTAWS.W1 — 2/3 legs, ACCEPTED as partial 1803Z
- (a) R1 tags (Project/Pipeline/Macro/Owner/Environment) verified Active.
- (b) CUR shipped `554c424e5` + 0-diff apply (shared-infra-v1.22.0):
  opal-cur-313476888478 + hourly Parquet CUR w/ RESOURCES +
  SPLIT_COST_ALLOCATION_DATA + ATHENA. First-delivery verify tomorrow.
- (c) CE resource-granularity = console-only payer opt-in (no API;
  AccessDenied probe) -> routed sovereign via COO (1-click Andrew ask).

### NFRA_GLOBGRPH.ITEM-2B — COMPLETE, ACCEPTED 1832Z  **[production fire #1]**
- DISCOVERY: 2b already LIVE since Wave-1 and silently melting down ~21h:
  ~8k errors ("Requirement failed: snapshot id changed"), 298,351-deep DLQ.
- ROOT CAUSE: per-ARN `table.delete()` loop = N+1 Nessie commits/batch x
  UNCAPPED ESM concurrency -> executions raced each other -> whole-batch
  SQS retry amplification.
- FIX `2ce19eaee` (tag globgrph-v0.1.7, 0-diff, live sha verified):
  single-commit `overwrite(filter)` upsert + reload-per-attempt retry
  (1s/15s/5) + ESM `maximum_concurrency=2` + `source_code_hash` wired
  (Rule 1). On-disk zip was STALE (pre-42eeb9761) — rebuilt from repo src.
- VERIFIED: post-deploy batches clean; controlled smoke invoke ran the full
  path (DERIVED S3_BUCKET -> ICEBERG_UPSERT nodes_written=1, failed=0).
- DLQ disposition: natural 24h expiry, COO-ratified (no replay/purge).

### NFRA_GLOBGRPH.ITEM-3 — load-layer COMPLETE, ACCEPTED 1851Z  **[production fire #2]**
- DISCOVERY: graph_edges committed with EMPTY src/dst since Item-2a shipped
  (derive_runner read `src`/`dst`; comp_aws_cli edges are
  `{source,target}`). Found ONLY because the Kuzu load tried to USE the
  data (2539/2539 unusable).
- FIX `fd62befc1` (tag globgrph-v0.1.8): image rebuilt (390500b3), ECS
  verify f3881f4a exit 0 — landed PRE-02:00Z so tonight commits real edges.
- SHIPPED `0a24bebe7` + `935a90874`:
  - `kuzu_nessie_load.py` — latest-Nessie-commit loader (pyiceberg
    StaticTable, pin evidence printed; includes 2b incremental commits),
    ARN-canonical node keys, hard-fail --force wipe.
  - `kuzu_ac_traversals.py` — AC5/8/9 done-gate harness, fail-honest
    substrate preflight (SUBSTRATE-MISSING exit 2, never PASS; §10.1).
- VERIFIED on fresh commit (nodes_snapshot=6022571177485028345): 1180
  nodes / 2199 of 2541 edges / 0 untyped / 0 collisions; 341 of 342 skips
  = wildcard `*:logs_to` pseudo-endpoints (by design) + 1 ECS ARN (P4).
  Sanity 3-hop LAMBDA-ASSUMES->IAM_ROLE-HAS_POLICY->IAM_POLICY = 826 paths.
- AC5/AC8/AC9 honestly UNVALIDATED (substrate-gated on P2 stitch / P3-A /
  P3-C). CVO pairing note sent (commit-pin caveat + wildcard allowance +
  PASS bar flagged for their acceptance lens).

### NFRA_COSTAWS 409-storm cost-banking — Andrew-direct via MSTR, done 1934Z
- Brief `6f3b74e06`: ~$14-16 incident (766,680 GB-s, ~$0.61/hr x ~21h
  silent; 7-day-unnoticed projection ~$100+), MSTR's CloudWatch figures
  verbatim; LD-0177 same-day-ROI framing.
- Burn-stop early evidence: post-fix ~1.9s avg vs ~135s -> ~$0.0006/hr
  (~1000x). Formal billing/CE confirm rides tomorrow's review.
- DLQ metric reconciled: 298,351 = queue DEPTH (get-queue-attributes), not
  NumberOfMessagesSent (redrive moves aren't producer sends; Sent=0 OK).
- COO folded INC-1 into the scorecard 1935Z.

## Footguns hit / lessons banked

- MSYS leading-/ aws args (log-group names) -> PowerShell per banked memory.
- `git tag -l | tail` is lexicographic — use `--sort=-v:refname`
  (shared-infra latest was v1.21.0, not v1.9.0).
- `rmtree(ignore_errors=True)` on Windows survived a file lock -> stale +
  fresh node union in Kuzu (1967 from 1180 rows) -> hard-fail wipe shipped.
- Edge id-space is ARN; node `id` is short name — Kuzu PK must be
  arn-if-present else node_id (first pass matched 15/2541 edges).
- New memory: `reference_iceberg_nessie_multiwriter_one_commit_per_batch_reload_retry`
  (one-commit-per-batch / cap concurrency / reload-per-attempt retry / DLQ
  natural-expiry pattern).

## Tag chain today (mine)

| Tag | Commit | What |
|-----|--------|------|
| globgrph-v0.1.6 | e574a0c7c | derive_runner 409 commit-retry/backoff |
| shared-infra-v1.22.0 | 554c424e5 | CUR per-resource cost attribution |
| globgrph-v0.1.7 | 2ce19eaee | 2b single-commit upsert + retry + ESM cap |
| globgrph-v0.1.8 | fd62befc1 | derive_runner edge endpoints (source/target) |

## Open / tomorrow (COO-ruled sequence)

1. Burn-stop formal billing/CE confirm (RAVC2 to COO).
2. 02:00Z TRIPLE-FIX artifact review (LD-0176): 2a-vs-2b conflict/retry log
   lines (first real race, both writers retry-capable), edge endpoint
   integrity in the new commit, run/perf normal.
3. CUR first delivery: s3://opal-cur-313476888478/cur/.
4. P2-STITCH (TO filed; CTO schema 82f766166 ready; AC5 flips on it).
5. COSTAWS W3/W4/W5 -> COMPAWS SFN-FIX/LAMBDAMAP-P2/PHASE-0 -> DTAFLP TO-3.
- HELD (do not start): DTAFLP P1 orion->inf (~190 files), TO-2, TO-4 —
  await Andrew explicit go + COO PROCEED.
- Andrew 1-click pending: CE resource-level granularity (console,
  Billing > Cost Explorer Settings).
