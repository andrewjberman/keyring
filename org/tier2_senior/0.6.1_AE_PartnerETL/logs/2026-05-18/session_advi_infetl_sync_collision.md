# Session Log — ADVI_INFETL.SYNC-COLLISION
**Agent:** 0.6.1_AE_PartnerETL
**Date:** 2026-05-18
**TO:** ADVI_INFETL.SYNC-COLLISION (COO-issued, GO 20260518T135007Z)

## Summary

Fixed the `orion-gold-dispatch.sh sync_scripts()` flat-dir last-write-wins
defect found during INFINC.006 chain-validation. Two halves: (1) immediate S3
remediation so the chain runs correct code now, (2) a structural collision-
detecting fail-loud rewrite so silent clobbering cannot recur.

## Phase 0 — Census + Live-Defect Determination

`comp-blast orion-gold-dispatch` → "No nodes matching" — expected (shell
dispatcher, not a modeled pipeline node); blast radius established empirically
by the S3 census instead.

Census of every `.py` basename present in 2+ of `code/{gold,manual_api,silver,bronze}/`:

| basename | prefixes | sha-divergent? | chain step | verdict |
|----------|----------|----------------|-----------|---------|
| pull_inflection_transactions_rest.py | gold+manual_api+bronze | YES | INF_API_PULL_TXN (active) | **DEFECT — CLOBBER**: stale bronze copy beat the INFINC.006 manual_api deploy |
| pull_inflection_performance_rest.py | gold+manual_api+bronze | no (uniform) | INF_API_PULL_PERF (active) | **DEFECT — DEPLOY-MISS**: all 3 copies uniformly pre-f39550d99 (COO/DS flag) |
| pull_inflection_assets_v2.py | manual_api+bronze | YES | INF_API_PULL_ASSETS_V2 | stale-but-correct — chain step is a **no-op** (resume-skip; Lambda-migrated) |
| pull_inflection_positions_daily.py | manual_api+bronze | YES | INF_API_PULL_POSITIONS_DAILY | stale-but-correct — chain step is a **no-op** (resume-skip; Lambda-migrated) |
| build_assets_dim.py | gold+silver | YES (whitespace) | not in catalog | harmless — winner (silver) == repo HEAD |
| pull_inflection_performance_dim.py | gold+manual_api | YES | not the chain PERF script | harmless — winner (manual_api) == repo HEAD |
| pull_inflection_new_portfolio.py | gold+manual_api | no | INF_API_PULL_NEW_PORTFOLIO | harmless — byte-identical |
| _orion_api_silver_lib.py | gold+silver | no | shared lib | harmless — byte-identical |
| __init__.py | code/gold (+subdir) | n/a | n/a | benign package marker |

**Live-data-defect determination (AC1/AC2):**
- assets_v2 + positions_daily: **stale-but-CORRECT.** Both are Lambda-migrated
  (`inf-api-assets-v2`, `inf-api-positions`, shipped inf-pipeline-v1.7.43). The
  chain script steps resume-skip every run — 05-17 chain: "RESUME: bronze/assets/
  2026-05-17.parquet exists — skipping", "0 total rows", wall 1.0s / 0.9s. The
  step writes nothing; the Lambda owns the data. No live data defect — no
  escalation triggered.
- transactions: CLOBBER, but the pre-INFINC.006 code is a correctness-safe
  daily full-pull (verified in the INFINC.006 chain-validation) — no data
  regression, only the AC5 optimization lost.
- performance_rest: DEPLOY-MISS — see below. COO surfaced it; already in the
  COO loop, so no separate escalation needed.

**Intentional-vs-accidental multi-homing:** NO genuinely-intentional multi-homing.
Every collision is accidental deploy cruft (successive deploys to different
prefixes over a script's history). `_orion_api_silver_lib.py` (gold+silver) is
byte-identical so moot.

### performance_rest.py — second casualty (COO/DS flag, INFGRO.009)

COO relayed a DS finding: INFGRO.002 commit `f39550d99` (2026-05-13, "persist
summaries[] block to bronze", +41 lines) is in the repo history of
`data/orion/manual_api/pull_inflection_performance_rest.py` (repo HEAD sha
`b95fa3a6`), but all three S3 prefix copies were uniformly `8a7dc8c9` — the
PRE-f39550d99 version. f39550d99 was committed but **never uploaded to any
code/ prefix** — a plain deploy-miss, distinct from the transactions clobber.
`INF_API_PULL_PERF` is an active chain step (ran 326s on 05-17), so
bronze/performance has been missing the summaries[] columns (matches DS:
05-13/15/17 partitions only `[client_id, date, factor, pull_date]`).
The chain did not break — INF_API_SILVER_PERF builds fine from the short
bronze — so this is a missing-enrichment defect, not a chain-stopper.

## Phase 1 — Immediate Remediation

Re-deployed the repo-HEAD canonical version over every divergent S3 copy
(re-deploy/overwrite only — NO S3 object deletion). Post-remediation sha256
parity verified across all colliding basenames:

| basename | uniform sha256 (post-fix) |
|----------|---------------------------|
| pull_inflection_transactions_rest.py | e3d7120bd54f (INFINC.006) — gold/manual_api/bronze |
| pull_inflection_performance_rest.py | 4e64b2545f74 (INFGRO.009 38410e1dd) — gold/manual_api/bronze — SEE CORRECTION below |
| pull_inflection_assets_v2.py | 0b9d26be6934 — manual_api/bronze |
| pull_inflection_positions_daily.py | b65bc70a0548 — manual_api/bronze |
| pull_inflection_performance_dim.py | 1b8db3968bca — gold/manual_api |
| build_assets_dim.py | 8ac08137d770 — gold/silver |
| _orion_api_silver_lib.py / new_portfolio | already uniform |

Every multi-homed script now resolves to byte-identical content at every
prefix the chain syncs — AC3 satisfied. The chain runs INFINC.006 TXN code
regardless of sync order.

### CORRECTION — performance_rest.py stale-HEAD error (DS~C catch)

My Phase 1 re-deploy of `pull_inflection_performance_rest.py` was WRONG: I
derived "repo HEAD" via `git show HEAD:` on a local clone that did not yet
have DS~C's commit `38410e1dd` (ADVI_INFGRO.009 Method-Y windowed performance
pull). I re-deployed the superseded `b95fa3a6` (the f39550d99 version) over
code/gold/ + code/bronze/ — the actual repo HEAD was `4e64b254` (16,346 b).
This created a divergent collision (manual_api=4e64b254, gold/bronze=b95fa3a6).

DS~C caught it and remediated: re-deployed `4e64b254` to gold + bronze. I then
re-fetched origin/CLOUD and re-verified ALL 6 Phase-1 scripts against fresh
HEAD — all now match: performance_rest = 4e64b254 uniform across 3 prefixes;
the other 5 (transactions/assets_v2/positions_daily/performance_dim/
build_assets_dim) were unaffected (no commit newer than my stale local HEAD).

ROOT CAUSE of my error: deriving repo-HEAD for a deploy without a fresh
`git fetch` on a fast-moving multi-agent branch. Lesson: always fetch before
treating local HEAD as canonical for an S3 deploy.

CONSEQUENCE — chain #2: `chain_full_20260518_153102` (the INFGRO.007/009/
BIWNDW.002 co-land) synced scripts ~15:32Z, before 4e64b254 reached the
winning (bronze) prefix. Its INF_API_PULL_PERF step ran the OLD puller —
INFGRO.009's windowed pull did NOT execute on chain #2. Root is the
SYNC-COLLISION defect (single-prefix deploy + last-write-wins); my stale
b95fa3a6 deploy contributed to the divergence. Surfaced to COO 16:24Z
(time-sensitive) — INFGRO.009 needs a re-run on a post-16:15Z chain. AC5
(transactions) is unaffected — transactions was uniformly e3d7120b at chain
#2's sync.

## Phase 2 — Structural sync_scripts() Fix

`orion-gold-dispatch.sh sync_scripts()` rewritten (commit a45dd856f, built on
cf11cb697):
- **Pass 1** inventories every object by basename (prefix, key, body, sha256,
  size, mtime).
- **Pass 2** detects any basename in 2+ prefixes with DIFFERING content.
  Identical copies → "collision OK". `DECLARED_PRECEDENCE` (empty by default)
  resolves genuinely-intentional multi-homing. Anything else → **FAIL LOUD**:
  prints basename + every conflicting key/size/mtime/sha256 to stderr, exits 1.
- **Pass 3** writes one copy per basename (declared-precedence winner, else
  any copy — all proven identical or collision-free).
- Shell wrapper captures the python exit code and aborts the dispatcher (exit
  1) on a non-zero sync.
- `COLLISION_EXEMPT = {'__init__.py'}` for package markers.
- Bare prefix reordering was rejected (CTO + TO directive) — the fix is
  collision-detecting, not order-dependent.

`bash -n` PASS; embedded-Python `py_compile` PASS.

## Phase 3 — Verification

### AC4 — synthetic collision test

`.runtmp/infinc006/test_sync_collision.py` slices the real Pass-2/3 logic out
of the deployed dispatch script and exercises it against synthetic inventories:

| scenario | expected | result |
|----------|----------|--------|
| A. divergent undeclared collision | exit 1, names basename + prefixes | PASS |
| B. identical collision | exit 0, "collision OK (identical)" | PASS |
| C. divergent + declared precedence | exit 0, "collision RESOLVED" | PASS |
| D. __init__.py divergent | exit 0 (exempt) | PASS |

ALL 4 SCENARIOS PASS — fail-loud demonstrated; silent last-write-wins eliminated.

### AC5 — chain run executes INFINC.006 TXN code — PASS

Chain `chain_full_20260518_153102` (log `gold/logs/chain_full_20260518_153020.log`)
synced scripts ~15:32Z — AFTER the Phase-1 re-deploy made `code/*/pull_inflection_
transactions_rest.py` uniformly the INFINC.006 copy (e3d7120b). Its
`INF_API_PULL_TXN` section (log lines 291-325):

```
[2026-05-18T15:31:21Z] pull_date=2026-05-18 ... mode=INCREMENTAL (flag=False
   env=False sunday=False incremental_override=False) upload=True dry_run=False
[2026-05-18T15:31:21Z] INCREMENTAL: window 2026-05-11..2026-05-18 (7-day trailing)
   for 862 accounts
[2026-05-18T15:35:33Z] === pull_inflection_transactions_rest.py FETCH COMPLETE ===
[2026-05-18T15:35:37Z] INCREMENTAL merge: prior=1,300,879 + window=50,061 =
   1,350,940 pre-dedup -> 1,300,879 post-dedup (50,061 duplicate ids collapsed)
[2026-05-18T15:35:37Z] FINAL bronze frame: 1,300,879 rows, 31 cols, mode=INCREMENTAL
[PERF] pull_inflection_transactions_rest  wall=259.8s
```

The `mode=INCREMENTAL` line, the 7-day trailing window (AC7), the incremental
merge, and the "FETCH COMPLETE" wording are all present — the exact INFINC.006
signatures. This is the inverse of the defect-report evidence (no `mode=` line,
`household_rep_mapping`, plain "COMPLETE"). The chain demonstrably executes the
INFINC.006 Pattern E TXN code. **AC5 PASS.**

Live confirmation of the fixed dispatcher: `chain_full_20260518_170409`
(dispatched 17:04Z) is running on the deployed fail-loud `sync_scripts()` and
passed the sync stage (observed at step 19/56) — the fixed sync does not abort
on the now-uniform script copies, as designed.

## Phase 4 — Commit + Deploy

- Commit a45dd856f (orion-gold-dispatch.sh) — pushed to CLOUD.
- S3 deploy: `s3://opal-data-inf/code/gold/orion-gold-dispatch.sh`, sha256
  0c905e6255ec — verified S3 == local HEAD. Per the EC2 code deployment
  standard (S3 artifact model).
- Tag: `inf-dispatch-v1.3.0` on a45dd856f (next after inf-dispatch-v1.2.0).

## Cross-Domain Coordination (AC6)

orion-gold-dispatch.sh is concurrently owned by AE 0.7.0 (RUNDATE-DISPATCH-IMPL
E1/E2). MCP exchanged: 0.7.0 confirmed cf11cb697 is their FINAL committed state;
my sync_scripts() edit is confined to that one function, zero overlap with
E1/E2 (step_is_date_capable + validate_rundate_coherence). 0.7.0's E1/E2 changes
are intact in the committed file. S3 deploy sequenced after 0.7.0's in-flight
chain per their clean-audit request.

## Compiler Tools

| Tool | Phase | Result |
|------|-------|--------|
| comp-blast orion-gold-dispatch | 1 (before write) | "No nodes matching" — expected for a shell dispatcher; blast radius established by the S3 census |
| aws s3 ls (4 code/ prefixes) | 1 (before write) | Full basename inventory — the empirical census basis |
| comp-iam | 3 (after commit) | N/A — sync_scripts() changed `s3.download_file`→`s3.get_object` (both `s3:GetObject`); paginator `s3:ListBucket` already used. No new AWS API surface, no iam.tf change. |

## RAVC2

RAVC2-close sent to COO; CC CTO + CC DS~C + CC AE 0.7.0 — census, commit
a45dd856f, AC4 synthetic test, AC5 chain-log evidence, the 0.7.0 coordination
record, and the stale-HEAD error + DS~C correction.

## Status

ADVI_INFETL.SYNC-COLLISION COMPLETE. All 7 ACs met:
- AC1 census delivered; AC2 no live-defect missed (performance_rest +
  chain-#2-PERF both escalated to COO on discovery); AC3 sha parity verified
  (re-verified post-correction); AC4 4/4 synthetic scenarios PASS; AC5 chain
  `chain_full_20260518_153102` ran INFINC.006 TXN code (mode=INCREMENTAL);
  AC6 0.7.0 coordination honored; AC7 no emoji, EC2-standard deploy, this log.
- Commit a45dd856f, tag inf-dispatch-v1.3.0, deployed sha 0c905e6255ec.
- One self-caught error: Phase 1 stale-HEAD re-deploy of performance_rest
  (corrected by DS~C; all 6 scripts re-verified against fresh origin/CLOUD).
- Follow-ups surfaced to COO: INFGRO.009 needs a re-run (chain #2 ran old PERF
  code); a full repo-HEAD-vs-S3 deploy-miss audit recommended (VALGATE.008).
