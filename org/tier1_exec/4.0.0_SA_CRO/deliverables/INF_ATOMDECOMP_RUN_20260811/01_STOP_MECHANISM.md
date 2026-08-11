# INF pipeline stop — the mechanism, grounded end to end, and the repair executed

**Run:** INF_ATOMDECOMP_RUN_20260811 (charter in 00_CHARTER.md) · **Author:** `4.0.0_SA_CRO~A`
**Window:** 2026-08-11 ~0445–0515Z · **archetype:** DIAGNOSE + IMPLEMENT
**Statuses per the method:** every claim below is PROVEN unless marked otherwise; evidence classes
SOURCE (file:line@vintage) / DEPLOYED (S3 bytes) / RUNTIME (chain logs) / DATA (live S3 + parquet
reads) / ABSENCE (measured-zero with denominator).

---

## THE STOP IN ONE PARAGRAPH

The INF gold chain has failed at `INF_C_01.canonical_nna` every run since 2026-08-02 (RUNTIME:
per-day chain-log census; last `pipeline-complete.json` 2026-07-31T14:56Z). The F7 coverage guard
(`lib/nna_coverage_guard.py:320`) correctly refuses to erase served NNA history that the daily
FULL re-derive would silently drop: first 5 accounts (+$514,487.47, byte-stable 08-02→08-08), then
a disjoint 16 accounts (net $−1,268,687.56, 08-09→) — because **the transaction snapshot the
re-derive reads is rebuilt every Sunday from per-account inception-to-date pulls over the CURRENT
account universe, so any account that leaves the universe loses its entire history on the next
Sunday rebuild.** The universe is `accounts_v2` (custodian + rep-allowlist filtered from Orion
/NewPortfolio). Event A: a 07-31 Orion rep reassignment (12→10) dropped 5 accounts (rep 10 was not
in `INFLECTION_REP_IDS`; Andrew ruled it in 08-05 @93c898445, and Sunday 08-09's rebuild restored
their history — the event self-cured exactly as the timeline shows). Event B: 16 accounts under
rep 12 (Peter Lee), **cancelled at Orion effective 2026-07-01**, left /NewPortfolio during the
08-02..08-08 week and Sunday 08-09's rebuild erased their 6-year histories (26,371 rows, DATA:
membership diff 850→834, exactly the 16, zero additions). No pipeline code changed (DEPLOYED: the
pull unmodified since 07-02). Downstream: no sentinel → publisher frozen → platinum at 07-31 →
mdpf's completion-marker trigger starved. Two masked co-failures: 08-01 crashed at `INF_D_00:328`
(`int('unknown')` — the event-A accounts' unresolved households; its writer sits after C_01, so it
self-heals on the first passing run) and 08-06 had NO run at all (the estate-wide orion bronze gap
day starved the silver-aggregator quorum).

## THE CAUSAL CHAIN (each link with its evidence)

1. **Universe definition:** `pull_inflection_transactions_rest.py:152-172` (DEPLOYED, S3
   `code/gold/`, LastModified 2026-07-02 — ⚠ NO REPO COUNTERPART, see findings) — account_ids from
   accounts_v2 silver; accounts_v2 is rep-allowlist + custodian filtered
   (`convert_orion_api_to_silver.py:632`, `INFLECTION_REP_IDS = {3, 6, 10, 11, 12}`).
2. **Sunday full-pull replaces the snapshot:** `:360-361` Sunday auto-detect; `:380`
   inception-to-date per CURRENT account; merge base = single latest partition (`:175-199`).
   08-02 and 08-09 were Sundays; the two guard-set transitions land exactly on them (RUNTIME).
3. **Mon–Sat incrementals** merge 7-day windows into the prior snapshot (`:11-12`) — which is why
   event-A accounts reappeared as PRESENT on 08-08 while the guard still fired for their
   2026-03/07 partitions: presence returned with the 7-day window; HISTORY only returned with the
   next Sunday full (DATA: membership + guard-set timeline).
4. **C_01 re-derives ~1,400 historical partitions from the current snapshot every run**
   (`INF_C_01.canonical_nna.py:880-935` @f72495f387); the guard raises when any rewritten
   partition would lose an account (`nna_coverage_guard.py:320`); its own comment names the
   architectural exit: exposure "closes only when attribution stops being re-derived off a
   CURRENT-STATE roster."
5. **The 16 are terminal, not remapped** (DATA: roster 08-10 — all rep 12, all
   `cancelDate: 2026-07-01`, histories ending 2026-07-10; absent from /NewPortfolio on both 08-08
   and 08-10 — 3,005 accounts, zero churn between those days).
6. **Vendor-side processing, not our deploy** (DEPLOYED: pull bytes unchanged since 07-02;
   ABSENCE: no code/gold deploys 08-07+ touching the pull).

## THE REPAIR EXECUTED (F2 — history restoration, additive, reversible)

Under Andrew's fix mandate + his standing point-in-time ruling ("history does not restate"),
closed accounts keep their served history. Excusals would ACCEPT erasure — rejected. The repair
restores the histories to the snapshot so the re-derive stops attempting the erasure:

- Extracted the 16's 26,371 verbatim lines from `bronze/transactions/2026-08-08.jsonl.gz`;
  verified `2026-08-10.jsonl.gz` carried ZERO of their rows (control); wrote the union.
- Local verification: 1,434,111 lines (= 1,407,740 + 26,371 exact), 850 distinct accounts
  (= 834 + 16 exact), all 16 present.
- Uploaded over `bronze/transactions/2026-08-10.jsonl.gz` at 05:13:28Z — new VersionId
  `Ls9G3ZVFmemPfO21GRXrR8XXhkku.wCa`; prior `n3eptV8dceuEJm2x7WRUTX.yJk1FGpAm` retained
  (versioned bucket — one-call rollback).
- QA chain run dispatched 05:14:35Z via `inf-gold-trigger {mode:full}` (SSM `6a92d696`, lock
  `lock-full-f08460c2ece7`) — outcome watcher armed on the terminal sentinels. The 13:47Z
  scheduled cycle remains the production proof (ad-hoc is QA, never production evidence).

## WHAT REMAINS (the durable legs — routed, not silently held)

- **F1 (durable, DS lane via COO):** the Sunday full-pull must UNION-preserve prior-snapshot rows
  for accounts absent from the current universe — one function in the pull; without it, Sunday
  08-16 re-erases the 16 and the guard re-fires. ALSO: the pull script is DEPLOYED-ONLY (no repo
  home) — it must be homed in `data/inf/scripts/gold/` under version control.
- **F4 (scope-add):** the `INF_D_04` non-fee-AUA residual fix — separate record.
- **F5 (program):** the refactor spec per instruction 2 + the north star (raw endpoints,
  point-in-time daily shape, allowlist→predicate). The allowlist is hand-copied across ~28
  definition sites with measurable drift between them — a drift factory the refactor retires.
- **Decision surfaced to Andrew (not blocking):** whether cancelled accounts should EVER leave the
  served spine. Point-in-time says no; if he ever wants pruning, that is the guard's excusal path
  with a named decision — never a side effect of a vendor flag.

## FINDINGS BESIDE THE PATH (surprise-channel items, one line each)

- `pull_inflection_transactions_rest.py` deployed-without-repo-home (MISSING_IN_REPO class).
- `CHAIN_INCREMENTAL` contains NO B/C scripts while the disabled rule's description promises
  "current-day B+C" — description-vs-implementation drift on the two-flow design.
- The predecessor brief's stop mechanism ("rules disabled under the hold") was a stale-frame read:
  the hold was CURED+LIFTED 07-16 (trigger env provenance); the live dispatch is the aggregator's
  direct invoke. Corrected here with the evidence, not silently.
- `MDPF_PIPELINE_TRUTH.json` pipelines/6 (INF) rows asserting the freeze cause can now be updated
  from INFERRED to MEASURED — routed to the truth-JSON owner (CTO), not edited by me.
