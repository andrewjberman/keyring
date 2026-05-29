# work_1835Z — AE~A spawn-orient: S2 state-report + FIND_INSURE.008 evidence-package

**Serial:** 0.7.0_AE_CloudOps~A
**Date:** 2026-05-29 ~18:23Z–18:35Z
**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, COORDINATE

Fresh MSTR-provisioned spawn (18:19Z per ws COO allocation / Andrew sovereign) for the
FIND_INSURE Phase-1 + lapsed-S2 lane. Startup: /watcher (registered ~A PID 8748, tracked
watcher), org/XXX.md protocol, /cloud-ops orient, /work 20m cron armed (job 35a409c8).

## Dispatch + re-sequence

COO DRIVE GO (18:23Z): (1) reconcile lapsed S2-backfill FIRST, (2) FIND_INSURE.008.
I flagged an Andrew-direct MSTR PRIORITY in my **base** inbox (18:20Z, telemetry-hook fix)
and proposed sequencing it first ([ANDREW-DIRECT-CC]). COO override (18:29Z): SKIP telemetry
(it's AE-**base**'s MSTR-assigned job, parallel); S2 = STATE-REPORT-ONLY no re-run; .008 =
evidence-resurface no re-run. Absorbed; executed COO's order.

## (1) S2-backfill state — OUTCOME (c): STOPPED/INCOMPLETE (~4%)

- Instance mdpf-daily-runner (i-02448edb624a7a7cf): STOPPED (last launch 2026-05-29T15:00:08Z).
- Output prefix `s3://opal-data-mdpf/mdpf/feeds/non_model_aua/inflection/{date}.parquet`
  (script `data/mdpf/scripts/backfill/build_mdpf_wsc_inflection_nonmodel_backfill.py`,
  reads Orion `opal-data-inf/silver/api_dims/accounts_v2/*`).
- 20 files: **10 historical-backfill** (2025-05-28→2025-06-10, all written 05-28 19:12–19:45Z =
  ~10 of ~252 intended dates, ~4%) + **10 daily-production** (2026-05-18→05-29, daily chain,
  healthy/current — 05-29 written 11:00:53Z today).
- ZERO backfill writes after 05-28 19:45Z. r3 (23:09Z) + r4 (ETA 04:21Z) + 15:00Z restart
  produced nothing — auto-killed by EC2 user-data `shutdown -h +2` branch before completing
  even one new date (each date ~2–3min: 300 HH × 0.25s sleep + API; 2-min shutdown kills mid-date).
- Disposition: HOLDING re-run per COO. Coherence flag: this Orion assets_v2 historical backfill
  is the parallel decomposition, NOT DS~B's F1 client_performance-spine repoint
  (opal-data-inf gold/timeseries) — F1 likely not blocked by it. If S2 needed for the
  model-split-trend feature, re-run requires the user-data shutdown-branch fix first
  (MDPF_NO_SHUTDOWN=1, follow-on per work_2352Z).
- RAVC2 to COO: `20260529T183217Z`.

## (2) FIND_INSURE.008 Phase-1 evidence — VERIFIED INTACT

- AC7: 100 distinct IMO slugs w/ bronze+silver+gold web-scrape @ run_date 2026-05-27 (≥99).
  bronze 104 / silver 100 / gold score.json 100. The 4 bronze-no-gold = `_control-`/`_reprobe-`
  Fisher+Wealthfront validation probes (correctly not production-scored).
- AC9: `s3://opal-data-imo/qa/stage2-universe-2026-05-27.json` (53,559B, 05-28 09:23Z) +
  stage1-p2-grade + stage1-validation-subset present.
- AC10: all 4 find-insure Lambdas deployed/intact (crawl-web/parse-web/score-web python3.9
  1024MB, + scraping-browser escape-valve python3.12), LastModified 05-28T05:08–05:48Z.
- RAVC2 to COO: `20260529T183510Z` — ready for Phase-1 joint Accept.

## Telemetry-hook fix — diagnosed, REASSIGNED to me (base phantom), EXECUTED + COMMITTED

Diagnosed pre-override; COO then confirmed AE-base phantom + reassigned the fix to AE~A
(183544Z, MSTR CC'd) since a fabric-wide-blinding hook can't wait on a dead lane.

Break = the PostToolUse telemetry hook was NEVER committed to the git-TRACKED
`.claude/settings.local.json` (git log -S confirms 4b3ef1e95 is the FIRST commit ever
touching it) — it only lived as a local/worktree edit. When the tracked file reverted to
committed `4cedb49ab` (05-24, hook-less), telemetry froze 05-26 04:44Z, blinding /drive
Step 2b + cl-board + /overview ~3 days.

FIX: added matcher:"*" → `bash .tools/hooks/post-tool-telemetry.sh` to settings.local.json;
safe-commit **4b3ef1e95** (committing the tracked file = durable fix, survives next revert).
Corroborated against worktree's identical canonical "*" block.

VERIFIED: synthetic e2e test PASS — jsonl written correctly, kind classified, CV-B1 privacy
holds (no command/secret leak), serial_source=session-id-keyed.

CAVEAT: Claude Code loads hooks at session START, no mid-session hot-reload (my own session
emits zero telemetry post-edit; existing files still frozen 05-26 04:45Z). Live sessions emit
only after restart/respawn; new sessions emit from start. Fabric telemetry self-heals as
sessions cycle. Flagged consumers to keep commits/broker primary until repopulated (MSTR item 3).
RAVC2 to COO: `20260529T184104Z`.

ADJACENT: canonical "*" block also carries post-send-commitment.sh (.active-commitments ledger,
/work+/loop Step 0.5) — also absent from committed config, likely also dead. Flagged to COO; not
added (scoped to telemetry per COO). Awaiting COO call on follow-on.

## AE-base phantom flag

Base (0.7.0_AE_CloudOps) registers LIVE PID 34488 = documented LD-0131-L2 broker-restart phantom
(Andrew previously flagged PID 34488 as "no AE anywhere"). All 3 base-inbox msgs UNREAD (incl the
telemetry one); summary cites stale LD-0131 work. Recommended COO /stimulus-scan ground-truth.

## Compiler Tools

| Tool | Result |
|---|---|
| comp-pipescript deployed find-insure-crawl-web | No match — BD-scoped/stale graph; FIND_INSURE not indexed. Used `aws lambda list-functions` (authoritative) for AC10 instead. Flagged comp-graph gap to COO low-pri. |
| comp-iam service find-insure-crawl-web | find-insure role not indexed (same stale-graph gap). |
| aws lambda list-functions (AC10 fallback) | 4 find-insure Lambdas deployed/intact, LastModified 05-28T05:08–05:48Z. |
| aws s3 ls (AC7/AC9 + S2 state) | corp/ 100-slug universe intact; qa/ telemetry present; S2 output 10/252 incomplete. |

**Gap:** comp-graph doesn't index the FIND_INSURE imo-pipeline (newer 2026-05-27); comp-pipescript
deployed is hard-scoped to `s3://opal-data-bd/code/{gold,silver}/` + gold/silver scripts, not
Lambdas. Low-pri comp-tooling enhancement.

## Next

- Telemetry RAVC2 delivered; await COO ACK + call on post-send-commitment.sh follow-on.
- .008 ACCEPTED by COO as post-close finalization-of-record (Phase 1 already RAVC2-Accept
  CLOSED d2033738c; COO pruned stale "pending Accept" residue 860a587e3). No further action.
- S2 re-run HELD (COO continuing hold; rides on DS~B F1 spine-repoint plan; MDPF_NO_SHUTDOWN=1
  is the hard prerequisite if re-run is ever chosen).
- comp-graph FIND_INSURE-registration follow-on routed by COO (low-pri).
- /work cron 20m continues.
