# 0.4.0_DS_ClientPlatform~A — Session-Close Handoff (INFREF rebuild RIDING)

**archetype:** MIXED (IMPLEMENT / DIAGNOSE / COORDINATE)
**window:** 2026-06-30 ~2225Z → 2026-07-01 0210Z (since last log b84b7f81e)
**serial:** 0.4.0_DS_ClientPlatform~A | **branch:** CLOUD | **project:** ADVI_INFREF (P1 full-send)
**why this log:** Andrew reinstantiating me in a fresh context — Current State + Next Steps below are
written for ZERO prior context.

---

## Window summary

Pre-staged the entire post-rebuild cutover chain during the ~1h rebuild window (COO ask), built a
critical-path accelerator, caught+fixed a rebuild-blocking bug in my own de-convert, and answered
Andrew's path/ref-consistency question by building the tracking artifact the PRD lacked. The LEG-3
substrate rebuild is running now (0.6.1's SSM) on a working, verified path.

## Files Modified — see commit messages (12 commits, b84b7f81e..56c441d64)

Headlines:
- `761c21e9f` — **post-swap validation harness** `data/inf/scripts/verify/validate_post_swap.py`
  (L5 CVO cosign; 5 checks; semantic checks smoke-GREEN vs live served).
- `028553750` — added **check-5 served-extra** (CVO gap-1: dropped-view detection).
- `ef1fe997c` + `9b0d4a7d6` — **parallel reconvert accelerator** `reconvert_bronze_to_jsonl_parallel.py`
  (drained assets long-pole ~35→~7min; OOM'd harmlessly on tail; default lowered 32→16).
- `740aab11b` — **THE critical fix:** `run_silver_backfill_parallel.py:164` was `pd.read_parquet` on
  now-`.jsonl.gz` bronze → patched to gunzip+read_json; verified 24148→24148 both dims.
- `14a3a1679` `3cc941a4e` `c2e0ae06d` — **P3 decommission worklist** +
  **household-repoint spec** `docs/briefs/advi-infref-p3-decommission-worklist-20260630.md`.
- `ee964d4d2` `56c441d64` — **canonical PATH-MAP** `docs/briefs/advi-infref-pathmap-20260701.md`
  (as-built vs PRD-target; disposition RULED (a) by Andrew).
- `89e76dc7d` `c0aad6db1` — run_silver_backfill all-4-dims + assets→uniform-gzip.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| comp-grep | audit ALL `read_parquet` in silver+manual_api (de-convert reader bug class) | PASS — L164 the only bug; rest are silver/gold/reference reads |
| pipescript advi-inf | enumerate 9 pull-cron lambdas + producers for P3 worklist | PASS — all named exactly w/ crons |
| comp-glob / comp-which | locate household/txn builders, ADVI_INFREF PRD | PASS |
| comp-freshness/comp-blast | (not needed this window — verify was direct S3 + source read) | — |

**Worked:** comp-grep's dependency-context on hits sped the reader audit. **Failed/Gap:** none new;
Explore subagent hit session/rate limits twice → did the audit inline. **Rail:** several `aws s3 ls`
rail-checked (keyspace enumeration / phase-boundary / liveness — no comp-tool fits raw key inventory).

## MCP traffic (significant only)

- COO: 2 RAVCs (pre-stage #1+#2 done; L164 patched+audit=no-4th-bug).
- CVO: harness gap-1 closed + scope-locked (L3=pre-swap value-parity / my harness=L5 post-swap; both
  distinct, sequenced); CVO ACK'd + owns activity_scan/cash_drag L5 adjudication.
- 0.6.1: the accelerator hand-off, OOM triage, the 3 stacked de-convert-bug corrections (argparse /
  2-dim-only / L164 reader), the split-plan, "let it ride" (a).
- CTO: issued PRD §1/§4-R1 amend + path-map promote (Andrew ruled layout (a)).

## Blockers

NONE. The rebuild is legit-gated on COMPUTE (0.6.1's STEP2 silver-backfill riding ~80min, GIL-bound).
Not a stall — deterministic/idempotent/working, err=0.

---

## CURRENT STATE (zero-prior-context handoff)

**ADVI_INFREF = the durable re-architecture of the Inflection (inf) data pipeline. Tonight's full-send:
LAYER-1 categorical pull + LAYER-2 de-convert (parquet→.jsonl.gz raw bronze / typed silver) + a full
2020→2026 rebuild to lock the typed files. Perf-incremental is the FINALE (after rebuild lands).**

**Structure — DONE + deployed:**
- L1 categorical CHAIN_PULL: conditional-green (all bronze artifacts on the EC2 pull stage).
- L2 de-convert: all 4 dims (positions/assets/txn/perf) = `bronze/{dim}/{date}.jsonl.gz`, **uniform
  gzip** (CTO 235025Z). INF_D_00e dual-writer removed both halves.

**Rebuild — RIDING (0.6.1's SSM on i-0ed5afded2ebd4ed4):**
- STEP1 reconvert: DONE (positions 2259 + assets 2255 + txn 49 + perf 50 → .jsonl.gz; accelerator
  drained assets, sequential mopped tail). Integrity verified (4/4 sampled gunzip clean, rows==source).
- STEP2a silver-backfill: RUNNING via `run_silver_backfill_parallel.py --dims positions_mv assets_v2
  --start 2020-04-24 --end 2026-06-30 --workers 16` — leading edge ~2020-11 as of 0158Z, err=0,
  ~51 partitions/min GIL-bound, ETA ~03:20Z. **Then** STEP2b sequential `run_silver_backfill.py
  --dims transactions performance` (~4min). **Then** `--stage compute` → `platinum/_rebuild/{ts}/`
  staging → `_REBUILD_STAGED` sentinel.
- Silver is being OVERWRITTEN live but a pre-rebuild snapshot exists (rollback-safe); served untouched.

**Pre-staged + execute-ready (mine, all committed):**
- `validate_post_swap.py` — L5 post-swap harness, 5 checks (structural SHA256 staged≡served + AUA
  $202,125,678.08 to-the-cent + freshness + cross-consist + gap-1 served-extra). Semantic checks
  smoke-GREEN vs live served. Runs POST-swap (auto-discovers latest `_rebuild/{ts}/`).
- P3 decommission worklist — 9 pull-crons ordered leaf-first (A9/reps LAST), stub/orphan group,
  yahoo ground-truth-at-execution. Ledger-ready, reversible-first, Andrew-confirm-gated.
- Household repoint — near-clean accounts_v2 swap spec'd (5/7 geo fields direct; household_name
  redundant via aum_snapshot; execute post-cutover, gates A9).

**Andrew decisions this session:** (1) let the rebuild RIDE (~80min, no OOM gamble); (2) layout
disposition (a) — dim-prefixed bronze + mixed silver is OPERATIVE, orion-api/eclipse-api unification
DEFERRED downstream. Path-map `docs/briefs/advi-infref-pathmap-20260701.md` is the tracking artifact;
CTO issued the PRD amend + promote.

**Gate chain (locked w/ CVO):** CVO L3 (pre-swap VALUE-parity on `_REBUILD_STAGED`, byte-different-OK)
→ 0.6.1 L5 atomic swap → my `validate_post_swap` (5 checks) + CVO L5 cosign → cutover.

**Known drift (catalogued in path-map, NOT tonight-blocking):** silver layout split; LIVE orphan
`silver/api_dims/performance/` (gold reads `silver/performance/`); txn 49-bronze→1560-silver partial
rebuild; stale docstrings (convert_transactions:14 / convert_performance:4 say .parquet, read .jsonl.gz).

---

## NEXT STEPS

1. **[0.4.0_DS_ClientPlatform~A — fresh me]** Watch for `_REBUILD_STAGED` (0.6.1 + COO have sentinel-
   watches; I'm cc'd). On stage: stand ready for [3.0.0_SA_CVO] L3 verdicts; on L5 swap, RUN
   `validate_post_swap.py` (auto-discovers ts) → GREEN → CVO cosign → cutover.
2. **[3.0.0_SA_CVO]** owns L3 (pre-swap value-parity) + the activity_scan/cash_drag served-extra L5
   adjudication (ground portal consumers: deprecated→whitelist vs dropped→RED).
3. **[0.6.1_AE_PartnerETL]** owns the rebuild SSM → stage → L5 swap; watcher on `_REBUILD_STAGED`.
4. **Post-cutover (FINALE, Andrew-sequenced):** household repoint (spec'd) → perf-incremental
   watermark (the finale) → P3 decommission (checklist ready) → deploy-hygiene single-home sweep.
5. **Banked follow-ups (fix-later-downstream):** ProcessPool variant of run_silver_backfill_parallel +
   reconvert (real CPU parallelism, OOM-controlled — the GIL fix); fix stale docstrings post-rebuild;
   retire the `silver/api_dims/performance/` orphan writer; CTO PRD amend + path-map promote.
6. **[1.0.0_SA_CTO]** amend PRD §1/§4-R1 to operative layout (a) + promote the path-map doc.
