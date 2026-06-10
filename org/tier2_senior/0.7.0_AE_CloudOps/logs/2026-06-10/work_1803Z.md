# work_1803Z — 0.7.0_AE_CloudOps (fresh session; LD-0177 queue pull)

## Session start
- /watcher: re-registered (PID 25920), persistent inbox Monitor armed (bokcpqh0x; exit-143 SIGTERM quirk fired once, lossless re-arm as bswjt7l3p per LD-0146 protocol).
- Launch-prompt LD-0082 "/work 20m cron" NOT re-armed — superseded by LD-0157/LD-0175 + Andrew-direct cron kill earlier today (prior session 3e03fb17). Single ad-hoc /work pass instead.
- 26 inbox messages triaged: all handled by prior ~B session (scope-confirm RAVC2 1539Z, keyword-intelligence deploy 09f361593, COSTAWS closures).

## LD-0177 queue (COO 1744Z)
- 12 TOs verified on disk; ACK + R1 status sent 1746Z (R1 was already 100% per COO's own 1449Z ACCEPT; AC2 lag-bound only).

## NFRA_GLOBGRPH.ICEBERG-409 — COMPLETE
- e574a0c7c (globgrph-v0.1.6): _overwrite_with_retry (reload-per-attempt, 2s/30s/jitter/5 attempts env-tunable, CommitStateUnknown retried, _ensure_table create-race guard). Gate clean; 4-case mock smoke PASS.
- CodeBuild 052acccf SUCCEEDED (replicated ~B's morning source-override config recovered via batch-get-builds) -> ECR :latest 20260610-175421.
- ECS verify task 0a9119b0 exit 0: 1176 nodes / 2539 edges through the retry path, NESSIE_COMMIT ok, snapshot archived. Landed pre-Item-2b per sequencing constraint; 02:00Z nightly uses this image.

## NFRA_COSTAWS.W1 — 2/3 legs
- (a) R1 tags all 5 VERIFIED Active in CE (already landed with R1).
- (b) CUR SHIPPED 554c424e5 + 0-diff apply (shared-infra-v1.22.0): opal-cur-313476888478 + hourly Parquet CUR w/ RESOURCES+SPLIT_COST_ALLOCATION_DATA+ATHENA. Served-artifact verify tomorrow (~24h AWS delivery).
- (c) CE resource-granularity: console-only payer opt-in (API AccessDenied; no API exists) — routed to COO as sovereign 1-click Andrew ask.
- RAVC2-COMPLETE sent 1802Z.

## Footguns hit/avoided
- MSYS leading-/ log-group arg mangled by Git Bash -> PowerShell per banked memory.
- tag tail -5 lexicographic trap: shared-infra latest was v1.21.0 not v1.9.0 — use --sort=-v:refname.

## NFRA_GLOBGRPH.ITEM-2B — COMPLETE (added ~1835Z)
- DISCOVERY: 2b already LIVE since Wave-1 and in a 409 storm: ~8k errors, 298,351 DLQ. Root cause: per-ARN delete loop (N+1 commits/batch) x uncapped ESM concurrency -> executions raced EACH OTHER -> whole-batch SQS retry amplification.
- FIX 2ce19eaee (globgrph-v0.1.7, 0-diff, live sha verified): single-commit overwrite(In-filter) upsert + reload-per-attempt retry (1s/15s/5) + ESM max_concurrency=2 + source_code_hash (Rule 1). Local zip artifact was STALE (pre-42eeb9761) — rebuilt from repo source.
- VERIFIED: live batches clean post-deploy; smoke invoke (real-shape S3 event) DERIVED -> ICEBERG_UPSERT nodes_written=1 failed=0. Queue drained. DLQ: recommend natural 24h expiry (nightly 2a re-bases; no replay/purge).
- ICEBERG-409 RAVC2-ACCEPTED by COO 1803Z (sequencing constraint was already moot — flagged in RAVC2).

## Next
- Tomorrow AM: GLOBGRPH 02:00Z artifact review (LD-0176) — now ALSO check 2a-vs-2b conflict/retry log lines (first real concurrent-409 exercise, both writers retry-capable) + CUR first delivery (s3://opal-cur-313476888478/cur/) + W3/W4/W5 + COMPAWS x3 + DTAFLP TO-3.
- DTAFLP P1: HELD awaiting COO PROCEED (scope: orion->inf only).
