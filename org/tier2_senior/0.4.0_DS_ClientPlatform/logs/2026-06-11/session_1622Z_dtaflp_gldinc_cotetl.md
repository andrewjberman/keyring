# Session log — 0.4.0_DS_ClientPlatform — 2026-06-11 (~1300Z–1622Z)

**Agent:** 0.4.0_DS_ClientPlatform (Tier-2/3 worker, event-driven)
**Driver:** 2.0.0_SA_COO (/drive); gate: 1.0.0_SA_CTO; AC10 close: 3.0.0_SA_CVO
**Themes:** NFRA_DTAFLP P3 execution (TO-1b/TO-4/TO-1c + P1-DS tree-sweep), ADHC_GLDINC P1 parity RC→fix→cert, ADVI_COTETL.CHAIN-FIX sentinel emission.

---

## 1. NFRA_DTAFLP P3 — bd/cot full separation (cot gold firm-native fork)

**TO-1b retarget (`d892fe500`, deployed opal-data-cot):** 7 live firm-local `opal-data-bd`→`opal-data-cot` + Schwab default (CTO-approved) + in-file provenance in the 9 edited cot gold files. `gold_dispatch.sh` (.sh, outside safe-deploy `.py` scope) hand-deployed + ETag-verified. Gate forced in-policy on-touch Rule-15 future-imports + ruff compliance.

**TO-4 FIRM_ID drop (`6ce1ff5fc`, deployed):** 8 FIRM_ID→`'cottonwood'` + 4 FIRM_NAME→`'Cottonwood Capital Advisors'`, env-switch dropped. Fixed the D_03:95/D_04:132 latent hardcode bug (ignored env → carried `'49financial'` for cot data). Added `README_FIRM_NATIVE_DIVERGENCE.md` cherry-pick guide. comp-constants drift surfaced → prepared cot-lane registration patch (`docs/briefs/dtaflp-to4-cot-comp-constants-registration.patch`); `comp-constants.config.yaml` is `ANY_EXEC_OR_AE`-owned so routed to AE; CTO did the cli `--lane cot` fix (`97805f8d3`).

**TO-1c (`68c4cc541` + `2be899cec`, deployed):** Caught a **TO-1b LIVE MISS** — `lib/config.py` shared `S3_BUCKET` (imported by ~40 in-chain scripts; `gold_dispatch.sh` sets `BD_S3_BUCKET` but does NOT `export` it, so the lib DEFAULT was operative) still defaulted `opal-data-bd` → IAM-Deny-breaks the cot chain = **likely the "COTETL chain broken" root cause**. Fixed lib/config + lib/schwab_flows; retargeted in-chain production refs (C_04/D_01/D_03/diag/runner-telemetry); pruned 30 dead off-chain 49F-incident scripts → cot gold **repo-side AC10 0-residual**. Also fixed `safe_deploy_core.py` (`--diff-filter=ACMRT`, `be6e841f0`) so prune commits skip deletions — pre-emptively unblocked AE's P1 deploy too.

**P1-DS tree-sweep (`924bc6c22`, deployed):** post AE git-mv `data/orion`→`data/inf`, swept the dangling in-file self-refs. DS-lane (47 files: data/inf scripts+manual_api, cot/find cross-domain, bd display_label). **Multi-form** per CTO: contiguous `data/orion` + `data\orion` backslash + **split-form** (`Path()/'data'/'orion'/...` at ec2 orchestrator:327 — AE-lane). Vendor `orion` names preserved (literal path-prefix replace; vendor-class count pre==post==10). Cross-lane remainder ROUTED: 31 infra/smartx files → AE (owned-paths CLOUD_OPS_OR_ETL/SHARED_OPAL_ETL); `floored_percentiles` sync-group LEFT `data/orion` provenance (byte-identical = guard-compatible; the bd/inf=DS + smartx=AE split makes an atomic sweep cross-lane — routed to CVO, COO recommends LEAVE); 5 `manual_api` files excluded (pre-existing AE-inf-content debt: 3× comp-constants INFLECTION_REP_IDS data-drift, 1× ruff, 1× AST undefined-name false-positive).

**Accepted:** all four legs RAVC2-accepted by COO (independently verified). CVO owns the AC10 close.

---

## 2. ADHC_GLDINC P1 — windowed-vs-oracle parity regression

**RC (read-only diagnostics, no gold run):** killed three hypotheses with hard evidence —
(a) restatement-miss: 0 restated/new/vanished partitions, `restatement_fallback=false` correct;
(b) dropped-events: cache = perfect 3,843,024-event snapshot, 0 per-partition mismatch;
(c) market_value/float: byte-perfect.
**Pinned:** a **`trade_date` dtype round-trip bug**. Partitions are heterogeneous (Jan–Feb 2026 store `MM/DD/YYYY` object strings, recent ones `datetime64`). The oracle's native union `[Timestamp + MMDDYYYY-str]` parses 0-NaT; the windowed CACHE round-trips through parquet stringifying datetime64→ISO → mixed `ISO + MMDDYYYY` string column → `pd.to_datetime(errors='coerce')` (L161) single-format-infers → NaT-drops the 124,712 `MM/DD/YYYY` rows → `dropna` removes events the oracle keeps → 1440 daily keys vanish.

**Fix (Option A, output-preserving — `c560e4ca9`):** `format='mixed'` at L161 + version-safe fallback, in BOTH `nna_flows.py` copies (bd-live + cot-prophylactic per the DTAFLP fork). Does NOT touch `keep='last'` survivor selection → oracle/served output unchanged. Navigated a real COO(Option B)-vs-CTO(Option A) divergence; converged on A (B would change served numbers → violates never-widen).
**Proof:** full oracle-vs-windowed shadow-compare with the fix = **78568==78568, sym_diff=0, value_diff=0, fallback=False** (real cache-read path), oracle unchanged, `77128+1440=78568` ties out. **CTO CERT PASS** (committed==proven, deploy-parity MATCH both buckets).
**Corroboration:** AE's key-diff = 1440 keys EXACTLY Jan–Feb 2026 (Jan 523 / Feb 917, pure subset) — confirmed to the row.
**Cutover:** key-diff gate CLOSED; cutover-activation gated on ≥5 clean counter-nights + Andrew (PRD §4) — not yet.

---

## 3. ADVI_COTETL.CHAIN-FIX — S3-sentinel chain rewrite (DS emission half)

**Contract (`e22288f98`):** designed the cot S3-sentinel emission contract mirroring inf's proven pattern; the cot rules fired on SSM-exit-0 (false-advance class), AE rewrote to aws.s3 Object Created. AE confirmed keys (155515Z).
**Emission (`b09296f08`, deployed today, time-gated):**
- `cot_bronze_ingest.py` → `bronze/{run_date}/_BRONZE_COMPLETE.json` at main-end on the full nightly run; **self-contained** (bronze = one all-tables invocation).
- `cot_silver_merge.py` → `silver/{run_date}/_meta/silver_complete.json` via new `--finalize` flag (silver runs PER-TABLE, so it needs one explicit final step — caught this cross-stage detail). AE added the `&& --finalize` SSM step (`cot-pipeline-v0.4.2`).
Both EMIT-ONLY-ON-VERIFIED-SUCCESS (re-head expected objects; partial/failed → no sentinel → chain halts visibly). Direct put_object, no local staging.
**Status:** full CHAIN-FIX wired end-to-end (session→bronze→silver→gold) for tonight's 02:00 UTC nightly; end-to-end verify = next-morning artifact review (cost-disciplined, no manufactured run, no overnight watcher).

---

## Memory banked
`reference_bucket_ref_rederive_trace_shared_lib_defaults_not_per_script_grep` — bucket-ref re-derives must trace shared-lib defaults (lib/config.py) + the no-`export`/`set -a` subtlety (dispatcher var doesn't reach child python → the lib DEFAULT is operative). COO-directed fabric-wide.

## Open / event-driven (none DS-committable)
- AE: adopt P1-DS infra/smartx sweep handoff (31 files + split-form) + redeploy Lambda/ec2; clear the 5 manual_api debt files.
- CVO: AC10 close — rule on the floored_percentiles guard-locked comment residual (recommend LEAVE).
- Tomorrow AM: cot CHAIN-FIX nightly artifact review.
- GLDINC: cutover-activation on ≥5 clean counter-nights + Andrew gate.

## Commits this session
`d892fe500` (TO-1b) · `6ce1ff5fc` (TO-4) · `68c4cc541` + `2be899cec` + `be6e841f0` (TO-1c + safe-deploy fix) · `e22288f98` (COTETL contract) · `c560e4ca9` (GLDINC fix) · `924bc6c22` (P1-DS DS-lane) · `b09296f08` (COTETL emission).
