# 0.4.0_DS_ClientPlatform — 3F-S4 cross-firm silver schema parity — COMPLETE (+ 3F-S3 AC-4 validated)

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, SCRIBE

**Window:** 2026-07-22 ~21:00Z → ~21:1xZ. **TO:** `MDPF_3FIRMS.3F-S4` (GO sequence 203250Z).
**Deliverable:** `deliverables/MDPF_3FIRMS_3F-S4_SILVER_SCHEMA_PARITY_CONTRACT_20260722.md`.

## Summary

Cross-firm silver schema parity contract built on EMPIRICAL parquet inspection of 10 tables at
stated partition vintages (the six census tables + fact_model_allocation_roster,
fact_allocation_valuation, fact_model_roster, fact_model_blend). **Column-level consumer map:
ZERO unmapped reads** across all six silver-consuming MDPF gold scripts (every read cites
file:line @ `61365878d`; two NAMED derivations: strategy_name→model_id join, partition-key date).
**Divergence register: 9 divergences, each with an explicit disposition** (D1 `_s{N}`-is-not-a-
contract law; D2 naming accept-with-reason; D3 money dtype; D4 provenance-sidecar canonicalize-
forward with rebalancer-family zero-provenance as priority; D5 coerce-vs-raise PINNED to
raise-on-drift, migration deferred to its own TO per COO 205514Z; D6 is_opal accept-with-reason;
D7 partition-date semantics table; D8 int64 booleans; D9 assignment no-date column).

The TO was amended mid-flight by COO (21:00Z correction block): its own §3.1 quote had transcribed
the PRD's `fact_holdings_s2` error — the correction consumed the 3F-S3 joint determination
(@`517bcb235`) and made LAW 1 the TO's headline ask, which the contract delivers.

## 3F-S3 AC-4 (joint with 0.7.0) — VALIDATED + CONFIRMED

The exercised runner-role read ran under CTO GO (SSM adc0f11f… on i-02448edb624a7a7cf; box
re-stopped, found-state restored — lifecycle was 0.7.0's, routed to CTO/Andrew rather than
self-cleared by either of us). My independent validation: identity ARN = runner role on the runner
box; 16,762×24 == my own read of the partition; ETag a6ea4428… + 388,478 B verified by my own
head-object at confirmation time; staged-script ETag matched my staging receipt. CONFIRMED sent
211xZ; 0.7.0 records AC-4 CLOSED jointly; 3F-S3 → COMPLETE (dim_model_portfolio exercise
sequenced to first G8/G3 population).

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-pipescript io` | 6 gold consumers | PARTIAL — 5/6 resolve; ALL silver reads dynamic-key-invisible | build_dim_model_portfolio UNREGISTERED (data/assets gold registry gap); io's own WARN mandates manual review — column map built from source, per the TO's if_mismatch |
| empirical parquet inspection | 10 tables, stated partitions | PASS | pyarrow schema dumps; the evidence base for §2/§3 |
| `comp-blast` | ×6 silver tables | NOT-FOUND ×6, denominator 2,218 nodes printed | monolith silver artifacts are not graph nodes — honest NOT-FOUND, not a clear; consumer set grounded on comp-grep sweep + source. Graph-coverage gap routed |
| `comp-grep` | fact-table names over data/ | PASS | 6 gold consumers surfaced (the blast substitute) |
| `comp-to` | 3F-S4 | PASS | session TO context |
| `s3api head-object` | AC-4 ETag cross-check | PASS | independent validation limb for the CONFIRMED |

Phase-3 io re-run: doc-only commit, no script changed — no new COLUMN GAPS possible; re-run of the
5 registered consumers unchanged.

## MCP traffic

0.7.0 joint thread (AC-6 concur 205701Z, lane split + CTO routing 210008Z, AC-4 evidence 210554Z,
my CONFIRMED) · COO S2 acceptance + S4 TO amendment · DE 3F-P1 locus table ACK (4 rows banked for
G-lane).

## Next

3F-G8 on its narrowed gate (3F-B5 + 3F-B6-liveness + 3F-S3): **S3 leg goes COMPLETE with AC-4** —
remaining gate legs are 0.6.2's B5 (tonight's 03:30Z landing) + B6-liveness. Circulate contract to
0.6.2~A/0.7.0 (done in-window); G8 prep (read CRO join spec + dim slices) can start now.

## G8 PREP STATE (banked ~21:12Z — build session picks up here)

- **CRO handoff RECEIVED COMPLETE** (211136Z, inbox read/): join = `externalId == account_id`,
  string equality, both z09 (NO int coercion); Opal filter = strategyName contains "opal" → 296/14;
  edges (Income falls through rollup → non-model; sleeves visible `is_opal=false`; closed accounts
  = zero-value shells, denominator filters value>0); identities (i) strategy-sum == LIVE dim sum,
  (ii) model+non_model == firm total, (iii) bridge 296/296 LOUD. ⚠ **CRO's dollars are a CROSS-DATE
  fixture (assignment 07-22 × holdings 07-20)** — identities reproduce, dollars do not. ACKed 211217Z.
- **49F/INF reference schemas captured** (gold/mdpf_revamp staged artifacts): distribution =
  {firm_id, firm_name, generated_at, period, source, basis, total{count/aum/mean/median/percentiles
  p10-p90/min/max/std_dev/histogram{bins,counts,bin_labels}/active_accounts_count/
  excluded_unfunded_count}, by_model{...same block per model}}; aum-metrics = {period, last_updated,
  dates{q0..q3}, total{aum, model_aum, non_model_aum, account_count, q0..q3{change,growth,
  priorLevel}}, by_model[...]}.
- ~~⚠ DESIGN QUESTION FOR BUILD~~ **RESOLVED — CTO RULING 213636Z (pre-raised 213524Z, banked
  pre-B5): OPTION 1, per-entity `series_start`, three bindings.** Mechanism grounded first:
  `dim_mdpf_aum_metrics.py:126-132 @ 19d3a606d` already emits an honest all-None triple when
  prior=None (get_value_at_date :116-123 forward-fills only real values), so a ~2-day Cottonwood
  series yields all-None at every q0–q3 — mechanically fine but byte-identical across
  feed-gap vs series-too-short (DE's dual-null G1 class). Ruling bindings:
  (1) **series_start DERIVED at build time from the facts** (first fact date per entity), NEVER a
  hardcoded constant — ruling-9 self-extending: back-delivered history moves the field with zero
  code change. Consumer semantics: `quarter_end < series_start` ⇒ STRUCTURALLY ABSENT;
  `quarter_end >= series_start` with None ⇒ feed-gap class, worth a look.
  (2) It is the **S5 PREDATES-CONTRACT shape at the artifact level** — contract-fact boundaries
  publish constants, data-fact boundaries derive per run; never freeze as a constant what the data
  can tell you.
  (3) **FEEDS G1, does not settle it** — if G1's general null-composition rule lands on a different
  shape, G1 WINS and this migrates; the build must carry a note so the two never read as competing
  standards. (Options 2/3 rejected: 2 ratifies a cheaply-resolvable ambiguity; 3 fails Andrew's
  ruling-11 lightweight standard.) Ruling verbatim: inbox read/ 20260722T213636Z.
- Phase-1 io/blast run (io dynamic-key-blind, blast no-extracted-edges lower bound — both recorded);
  producer family mapped (`dim_mdpf_account_distribution.py` = revamp copy of the served smartx
  producer; build adds a `_units_cottonwood()` leg + the aum-metrics artifact).

## G8b PREP STATE (banked ~2245Z — staged TO @d8570d2f3, same B5 gate)

**3F-G8b = Cottonwood appended daily model-snapshot series.** Andrew-direct via CRO (~2210Z, spec
@26f218a75), CTO-ruled 222856Z, COO GO(staged) 224026Z. **APPENDER, NOT BACKFILL** — consumes G8's
OUTPUT with zero re-derivation (io must show: reads G8 output only, never rebalancer/fact_holdings/
crosswalk).

- **Sequencing (COO, hard):** G8 CORE first → S5 provenance → G8b. G8b NEVER delays G8; on any
  contention G8 wins.
- **Four CTO bindings:** (1) G8-core-first; (2) gold → NO fact_ prefix — spec's own
  `fact_model_portfolio_daily` name SUPERSEDED, DS finalizes; working candidate
  `dim_model_portfolio_daily`, comp-blast collision check at build; (3) FORWARD-APPEND ONLY,
  Phase-3 proves both sides (day-2 adds row, day-1 byte-identical ETag); (4) CRO source-keying
  carried so a future CTO-gated backfill is non-conflicting — appender never writes a past date;
  if keying ever appears to require one: STOP + escalate (ruling 10).
- **Spec digest (@26f218a75):** grain (model_id, snapshot_date); snapshot_date=assignment_date
  partition key; source ∈ {daily-snapshot, datamining-backfill}; feed_live + basis from 0.6.2's B6
  ~05:01Z heartbeat (unchanged snapshot still appends, dead-feed day labelled); row_appended_at;
  __FIRM__/companion rows (firm_total_aua, model_aua_total, non_model_aua, counts) so G3 identity
  needs no side-join; §4 five FAIL-LOUD per-append checks (penny identity, 17/17 roster
  cross-validation, bridge exact, trading-day continuity via lib/trading_calendar.py, vintage lag
  flag); idempotent within a date (re-run overwrites own partition only); NO hardcoded series
  start; §3b query surface = one consolidated parquet + MDPF JSON slice regenerated per append
  (serve wiring stays a CTO/COO call); producer under data/assets/scripts/ (deploy-map hazard).
- **Requested from CRO 224306Z (TO Phase-1 step 1):** confirm §3a is the complete source-keying
  design + the proof notebook. Awaiting reply; do-not-re-derive stands.
