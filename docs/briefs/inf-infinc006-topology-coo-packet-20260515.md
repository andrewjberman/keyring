# INFINC.006 Pattern E TXN — COO Topology Resolution Packet

**Author:** 2.0.0_SA_COO
**Date:** 2026-05-15
**Trigger:** CTO validation brief `58777ee94` (`docs/briefs/inf-infinc006-cto-validation-20260515.md`) §7 agenda item #1 — "is the gold-chain REST TXN path or `inf-api-txn` Lambda the canonical daily producer? Resolve before green-lighting INFINC.006."
**Companion to:** CTO validation brief (validates DS~D's narrow technical claims; flags the unverified scope premise).
**Verdict:** Topology #1 **cannot be resolved to outcome A or B.** The `silver/transactions/{date}.parquet` end-state is not undecided — it is **contradictorily decided by two projects that never saw each other.** This is CTO outcome **(C)**, sharper than "dual by design." **Run the thread. INFINC.006 defers.**

---

## §1 — Question posed

Which is the canonical daily producer of `s3://opal-data-inf/silver/transactions/{date}.parquet` — the gold-chain REST path (`pull_inflection_transactions_rest.py` → `convert_transactions_to_silver.py`), or the `inf-api-txn` Lambda (`pull_inflection_transactions_v2.py` → `convert_orion_api_to_silver.build_transactions`)? If cleanly resolvable, INFINC.006 collapses to a TO amendment; if not, the thread fires.

It is not cleanly resolvable. Below is why.

---

## §2 — Verdict

Tracing the silver/transactions writer set end-to-end found **three** writers (not two), governed by **two projects with directly contradictory declared canonical end-states**, where **neither project's scope acknowledges the other's writer.** The most recent project (DWSPLT, 2026-05-13) even codified a false "exclusive writer" claim into a production decom docstring.

Outcome A ("gold-chain REST canonical, `inf-api-txn` is stale debt") and Outcome B ("`inf-api-txn` canonical, decom the chain steps") are each *half-supported by one project and half-contradicted by the other.* There is no single source of truth to read off. The thread must produce a **fresh superseding ruling.**

---

## §3 — The three writers of `silver/transactions/{date}.parquet`

| # | Writer | Source / mechanism | Windowed? | Invoked daily by | Status post-`f69461357` |
|---|--------|--------------------|-----------|------------------|--------------------------|
| 1 | `convert_orion_to_silver.py` `build_trn_silver()` | Orion CSV exports `bronze/orion/{date}/trn/*.csv` (43-col) | full history | (legacy orchestrator path) | **DECOMMISSIONED** by DWSPLT TO-2/3/5 `f69461357` — body retained for rollback only, not called in `main()` |
| 2 | `convert_transactions_to_silver.py` | Orion REST `/Portfolio/Accounts/{id}/Transactions` → `bronze/transactions/{date}.parquet` (31-col) → full-history snapshot | **No** — full history | **gold chain** `INF_API_SILVER_TXN` (`orion-gold-dispatch.sh:186`) | **LIVE daily** — in `CHAIN_FULL` (`:207`) AND `CHAIN_INCREMENTAL` (`:210`) |
| 3 | `convert_orion_api_to_silver.build_transactions` | Orion Custom Report 28198 → `bronze/orion-api/{date}/transactions.csv` | **Yes — already rolling-7-day** + `--start/--end-date` | **`inf-api-txn` Lambda**, EventBridge `cron(0 13 * * ? *)` (`inf-api-txn.tf:166-169`) | **LIVE daily 13:00 UTC** |

Empirical confirmation that #2 and #3 both target the identical S3 key:
- `convert_transactions_to_silver.py:48` — `Output: s3://opal-data-inf/silver/transactions/{date}.parquet`; `:85` `SILVER_PREFIX = "silver/transactions"`.
- `convert_orion_api_to_silver.py:12,84-86` — `silver/transactions/YYYY-MM-DD.parquet (Custom Report 28198)`; `_TXN_S3_PREFIX = 'silver/transactions/'`.
- `lambda-source-map.json:1669` — `inf-api-txn` Lambda bundles both `pull_inflection_transactions_v2.py` and `convert_orion_api_to_silver.py`.

Both #2 and #3 run **daily**. The gold `full`/`incremental` chain fires daily (INFETL JSON empirical: "chain #24 cron-fallback fire 06:00:58Z mode=full"); `inf-api-txn` fires daily at 13:00 UTC. **Last-writer-wins on the shared key.** Schemas AND semantics differ — #2 is a ~1.25M-row full-history snapshot (~19.7MB, DWSPLT §2.1); #3 is a rolling-7-day slice.

---

## §4 — The two conflicting projects

### ADVI_INFINGE.005b (CLOSED 2026-05-07) — declares writer #3 canonical

INFINGE.005b created the dedicated `inf-api-txn` Lambda, then **decommissioned transactions from the orchestrator + `inf-silver-chain`** and cut over to the Lambda. CHANGELOG commit messages, verbatim:
- `feat(ADVI_INFINGE.005b): inf-api-txn Lambda + TF cron 13:00 UTC + transactions decom plan (Phase 1)`
- `fix(ADVI_INFINGE.005b): decommission transactions DimSpec from orchestrator -- cutover to inf-api-txn Lambda cron 13:00 UTC`
- `fix(ADVI_INFINGE.005b): remove transactions from inf-silver-chain SILVER_BUILDERS -- **inf-api-txn Lambda owns TXN end-to-end**`
- `fix(ADVI_INFINGE.005b): build_transactions output silver/transactions/{date}.parquet (flat legacy path)`

COO session log 2026-05-07 corroborates: *"inf-bronze-runner EC2 stays only for inf-api-txn daily cron."* INFINGE Phase 2 absorbed into ADVI_INFETL.LAMBDA-DIMS — `inf-api-txn` is 1 of 9 daily-dim Lambdas in the live LAMBDA-DIMS architecture.

**INFINGE.005b's declared end-state: `inf-api-txn` Lambda (writer #3) owns TXN end-to-end.** It never mentions the gold-chain `INF_API_*_TXN` steps.

### ADVI_DWSPLT (PRD v0.2; TO-2/3/5 shipped `f69461357` 2026-05-13) — declares writer #2 canonical

DWSPLT §1 Scope, verbatim: *"Consolidate the two writers currently competing for `silver/transactions/{date}.parquet` into a **single REST-canonical writer (`convert_transactions_to_silver.py`)**... Retire the LEGACY CSV writer (`convert_orion_to_silver.py`)."*

DWSPLT's §2.2 writer-identity table names exactly **two** writers: LEGACY `convert_orion_to_silver.py` (#1) vs NEW `convert_transactions_to_silver.py` (#2). It decommissions #1 and crowns #2.

**DWSPLT's declared end-state: `convert_transactions_to_silver.py` (writer #2, the gold-chain path) is the single canonical writer.** It **never mentions `inf-api-txn` / `convert_orion_api_to_silver.py` (writer #3) anywhere** — not in §1 scope, not in the §2.2 writer table, not in §7 open questions (§7-Q4 flags a *future* audit for LEGACY `accounts_dim`/`aum_snapshot` but is silent on the TXN Lambda).

### The collision

INFINGE.005b (writer #3 canonical) and DWSPLT (writer #2 canonical) **cannot both be right.** They were authored 6 days apart, in the same artifact, by overlapping agents, and **neither acknowledges the other.** DWSPLT consolidated the LEGACY-vs-REST pair it could see and was blind to the third writer that INFINGE had already declared canonical.

---

## §5 — Smoking gun: the false-exclusivity docstring

DWSPLT's atomic bundle `f69461357` decommissioned writer #1 and wrote this into `convert_orion_to_silver.py:480-490` (`build_trn_silver` docstring), verbatim:

> *"DECOMMISSIONED 2026-05-13 (ADVI_DWSPLT TO-5 accelerated, Andrew ratify). ... Post-DWSPLT: `silver/transactions/` is **exclusively** written by the REST-driven `convert_transactions_to_silver.py` under CLAUDE.md Rule 17 strict semantics."*

The claim is false at the moment it was committed. `convert_orion_api_to_silver.build_transactions` (writer #3) was — and is — a live daily writer of the same prefix. DWSPLT codified an exclusivity it never verified. This is the same verify-don't-trust gap CTO's validation brief §4 names: no `comp-blast` / consumer-and-producer enumeration on the `silver/transactions/` artifact at PRD-authoring time.

---

## §6 — This is a live data hazard, not just tech debt

Writers #2 and #3 differ in **both schema and semantics** — #2 is a full-history snapshot, #3 is a rolling-7-day window. They overwrite the identical filename `silver/transactions/{date}.parquet`. A gold chain run is internally self-consistent (it writes via #2 then reads its own write within the sequential chain). The hazard is the **persisted artifact**: any consumer reading `silver/transactions/` *outside* a complete gold-chain run — the `txn_cache_reader.py` source-select path, ad-hoc analysis, a partial/group-stage chain (`gold-d` only) — gets whichever writer touched the key last. A full-history NNA consumer (e.g. `INF_C_01.canonical_nna`) reading a 7-day slice would produce drastically wrong numbers.

Same incident **class** as the DWSPLT-origin event ($6.64M SV-Internal misclassification risk, DWSPLT §2.1). Whether it is **currently** silently corrupting or failing loud (DWSPLT A.2 cache reader "fails loud on missing canonical cols" may be catching it, or the schemas may overlap enough to pass) is unknown from static analysis — **see §8, the thread's first empirical action.**

---

## §7 — DWSPLT has a real scope gap

DWSPLT is JSON-active but its TO-2/3/5 shipped (`f69461357`); JSON is stale (CTO already owns that correction). More substantively: **DWSPLT's project-level AC-7 ("LEGACY no longer writes `silver/transactions/`") and AC-9 ("cache reader source-selects exactly 1 file") do not protect against writer #3 overwriting that 1 file's *content*.** DWSPLT's stated goal — "a single writer for `silver/transactions/`" — is **not met**, because DWSPLT only ever counted to two. The thread must decide whether DWSPLT reopens with expanded scope or a successor project owns the #2-vs-#3 consolidation.

---

## §8 — Recommendation

**Fire the thread — `ADVI_INFINC-001`, CTO operating, COO co-owning, participants CTO + COO + DS~D + AE 0.6.1.** Do NOT collapse to a TO amendment; the end-state is genuinely unresolved at the architecture layer. AE 0.6.1 is non-optional (owns `inf-api-txn` / LAMBDA-DIMS). DS~D is the DWSPLT TO-2/3/5 atomic-bundle author and the INFINC.006 brief author — natural fit.

**Thread agenda — amended/sharpened vs CTO brief §7:**

1. **Empirical first move (do this before debating).** AE 0.6.1: pull `aws s3api list-objects` LastModified + size + a schema/row-count probe on the last ~5 days of `silver/transactions/*.parquet`. File size is a near-perfect discriminator — writer #2 ≈ 19.7MB full-history; writer #3 ≈ small 7-day slice. This tells us *which writer is winning today* and whether the hazard in §6 is active or latent. Five minutes; decides the tone of everything after.

2. **Reconcile INFINGE.005b vs DWSPLT (the blocking architectural call).** Produce ONE fresh canonical-writer ruling that supersedes both projects' contradictory statements. Three real end-states:
   - **(A) gold-chain REST (`convert_transactions_to_silver.py`) canonical** → decom `inf-api-txn` Lambda (AE 0.6.1 + INFETL-scope action); INFINC.006 proceeds on `_rest.py` as Pattern E.
   - **(B) `inf-api-txn` Lambda canonical** → INFINC.006's premise collapses: windowed-incremental pull *already exists* in `_v2.py` (rolling-7-day). INFINC.006 becomes a skip-gate/delete of the chain's `INF_API_PULL_TXN`/`INF_API_SILVER_TXN` steps, not a build.
   - **(C) both retained deliberately** → that is a consolidation project (DWSPLT reopen or successor); INFINC.006 defers behind it.
3. **INFINC.006 disposition** falls out of #2. If (A): ratify the CTO brief §5 AC revisions (AC1→client-level, AC5→~2min, AC7 7d-vs-90d with Q2's 65-day-max-backdate data, missing-prior-partition fallback). I author the amended TO; CTO ratifies.
4. **PERF:** per CTO brief — ratify defer-v1 (soft evidence) or take one clean windowed wall-time measurement.

**INFINC.006 status:** stays authored-not-started. DS~D HOLD already messaged direct (so they don't self-start off the /loop watchdog).

**One process note for the thread record:** the root cause here is two PRDs touching one S3 artifact with no producer-side blast check at authoring time. `comp-blast` on the *artifact* (not just the script) at PRD decomposition is the structural fix — flagging for the COO/CTO TO-authoring checklist regardless of how the topology resolves.

---

## §9 — Evidence index

| Claim | Source |
|-------|--------|
| Gold chain has `INF_API_PULL_TXN`/`INF_API_SILVER_TXN`, in `CHAIN_FULL`+`CHAIN_INCREMENTAL` | `data/orion/scripts/gold/orion-gold-dispatch.sh:185-186,207,210` |
| Writer #2 reads `bronze/transactions/`, writes `silver/transactions/{date}.parquet` | `convert_transactions_to_silver.py:48,85,204` |
| Writer #3 writes `silver/transactions/{date}.parquet` from Custom Report 28198 | `convert_orion_api_to_silver.py:12,84-88` |
| Writer #1 decommissioned by DWSPLT; false-exclusivity docstring | `convert_orion_to_silver.py:480-499` |
| `inf-api-txn` EventBridge `cron(0 13 * * ? *)` | `infra/aws/terraform/inf-pipeline/inf-api-txn.tf:166-169` |
| `inf-api-txn` bundles `_v2.py` + `convert_orion_api_to_silver.py` | `infra/aws/lambda/ci/lambda-source-map.json:1669-1690` |
| DWSPLT names only 2 writers; crowns #2; never mentions #3 | `docs/architecture/ADVI_DWSPLT.md` §1, §2.2, §7, AC-7/AC-9 |
| DWSPLT TO-2/3/5 atomic bundle shipped | commit `f69461357` |
| INFINGE.005b: "inf-api-txn Lambda owns TXN end-to-end" | `infra/aws/terraform/inf-pipeline/CHANGELOG.json` (INFINGE.005b commits); `org/projects/ADVI_INFINGE.json` phase; COO log 2026-05-07 `session62` |
| Gold `full`/`incremental` chain fires daily | `org/projects/ADVI_INFETL.json` phase ("chain #24 cron-fallback fire mode=full") |

— 2.0.0_SA_COO

---

## Addendum A — `INF_D_05` consumer finding + correction cycle (2026-05-15 ~14:0XZ)

Post-empirical (CTO ran §8.1's S3 discriminator directly — AE 0.6.1 offline): the dual-writer is **ACTIVE** and **schema-level**. Every `silver/transactions/` partition older than today is last-written ~13:00 UTC by the `inf-api-txn` Lambda in **snake_case** Custom-Report schema with **`trans_date` 100% NULL**; today's partition is the gold chain's **camelCase** DWSPLT Rule-17 schema. Day-by-day clobbering observed (DS~B saw `2026-05-14.parquet` camelCase on 05-14; CTO's probe found it snake_case post-05-15 13:00).

**Consumer enumeration** (grep `silver/transactions` across `data/orion/scripts/gold/`; `comp-blast` does not model the artifact):
- **Shielded:** the 6 DWSPLT §2.4 consumers (TO-3-migrated to bronze-name canonical) + the `txn_cache_reader` path. `txn_cache_reader` is *structurally* shielded — it mtime-sorts, takes latest-5, rejects partitions missing `REQUIRED_CANONICAL_COLS` (`:181-207`); the gold chain's daily camelCase write always lands in that window; worst case is fail-loud, not silent. `INF_D_02` shielded (newest-key source-select, `:1012`).
- **NOT migrated:** `INF_D_05.activity_scan.py` (chain step `INF_D_05a`; in `CHAIN_FULL` + `CHAIN_GOLD_D`). It does NOT use `txn_cache_reader`; `load_all_transactions()` (`:204-239`) paginate-concats ALL ~1,510 partitions. Not in DWSPLT §2.4's list — a **concrete second instance of the §7 DWSPLT TO-3 scope gap**.

**Correction cycle (recorded for discipline).** Static schema analysis of `_load_txn_partition` (`:168-201`) predicted `INF_D_05` produces empty output: camelCase partitions hit `return None` (no `account_id`), snake-Lambda partitions hit `dropna` (NULL `trans_date`). That prediction was **over-extrapolated** — the COO surfaced it to CTO as a severity upgrade, then **retracted it** on pulling the live artifact: `s3://opal-data-inf/platinum/firm/activity_scan_1y.json` is **non-empty** (`txn_count` 1447/1497/1743/2572…), `LastModified 2026-05-15T07:08:38Z`. The INFINC.005→.006 lesson — *do not extrapolate past the probe* — applied to the COO mid-investigation.

**Reconciled true state.** Code analysis (camelCase + snake-Lambda partitions both unreadable) AND the non-empty artifact reconcile via the **older partitions**: dates ≤ ~2026-05-05 retain the pre-Lambda old-NEW-REST snake schema (`account_id` / populated `trans_date` / `trans_id`) — readable by `INF_D_05`, and full-history snapshots. So `INF_D_05` is **silently recency-stale** — txn universe frozen at `max_date ≤ ~2026-05-05` (≥ ~10 days), output otherwise plausible — **NOT empty, NOT a visibly-broken panel.** `activity_scan_*` feeds `portal/src/.../inflection/InflectionInsightsPanel.tsx`. Exact `max_date` pending the `INF_D_05a` runner-log line (`:237-239`).

**Thread implication (unchanged by the correction):** migrate `INF_D_05` to the canonical camelCase Rule-17 schema **and complete the consumer re-enumeration TO-3 left half-done** — adopted into the ADVI_INFINC-001 agenda. The fix is correct regardless of the canonical-writer ruling; `INF_D_05` provably cannot read the canonical schema. Andrew-report severity word: **"silently ~10-day-stale,"** not "broken."

— 2.0.0_SA_COO
