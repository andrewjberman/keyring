# Session Log — STAUDT.INV1 historical NNA mechanism investigation

**Agent:** 0.6.0_AE_PartnerETL
**Date:** 2026-04-20
**TO:** ADVI_STAUDT.INV1
**Session purpose:** Pure-diagnostic S3 reconstruction to rule in / out three candidates for the $100M+ historical NNA vs <$100M AUA stock/flow apparent violation Andrew observed. FIX-TO 4 authoring blocked on the ruling.

---

## Phase Overview

| Phase | Action | Outcome |
|---|---|---|
| 1 | Startup: register + inbox catchup + prev-log read + TO read | GO received from CTO 20260420T141459Z; ACK to COO within 2 min |
| 2 | Phase 0 diligence: comp-pipescript io C_01 + nna_atomic partition span + Travis Penfield book timeline probe | 2296 partitions span 2020-01-02..2026-04-16 (Apr 14 gap = Bug 5); Penfield book grew 9→17→62→297 accts; pre-silver-start partitions are empty-schema placeholders |
| 3 | Pre-Q1 MCP gate to COO with Phase 0 findings + method-substitution ask (snapshot read vs daily sum) | COO approved snapshot method, local Q1, + cross-check advisor guidance 20260420T142211Z |
| 4 | Q1 per-advisor initial reading → discovered Bug 1 leaderboard 0.2012 identity (separate display defect) | Mid-flight MCP candidate (b) ruling — 3/3 advisors show leaderboard total_aua = 0.2012 × book.tagged_aua |
| 5 | COO pivot: Andrew clarified observation is FIRM-level, not per-advisor. Reshaped Q1. | Firm-level values reproduce observation EXACTLY: $118.20M NNA vs $27.65M AUA at 2020-12-31 |
| 6 | Q1 firm-level mechanism identified: NNA universe (669 accts at 2020-12-31) >> AUA universe (228 accts). 441 flow-only accts contributed $83.97M net NNA without corresponding AUA. | Candidate (c) ruled out — violation present in T3 production. Candidate (a) ruled in with nuance. |
| 7 | Q2 firm-level silver/transactions scan (732,843 rows across 699 partitions) | NO duplicates, NO null source, NO synthetic fills. Flow rows are legitimate; mechanism is universe asymmetry not silver-level inflation. |
| 8 | Q3 T3 portal artifact re-verification | Violation fully present at T3 (timeseries_chart 2026-04-17, firm_mix_views 2026-04-20) |
| 9 | Synthesis: historical_nna_mechanism.md with joint (a)+(b) ruling + FIX-TO 4 orthogonality + 4 fix-path options for CTO consideration | Decision doc + 3 query JSONs committed |

---

## Deliverables

| Path | Size | Purpose |
|---|---|---|
| `data/black_diamond/diagnostics/STAUDT/INV1/historical_nna_mechanism.md` | 14,485B | Decision document (primary deliverable) |
| `data/black_diamond/diagnostics/STAUDT/INV1/query1_nna_reconstruction.json` | 13,502B | Per-year firm + per-advisor NNA reconstruction; portal cross-ref |
| `data/black_diamond/diagnostics/STAUDT/INV1/query2_silver_tx_anomaly.json` | 18,559B | Firm-level + flow-only + Penfield per-month tx anomaly scan |
| `data/black_diamond/diagnostics/STAUDT/INV1/query3_t3_book_nna.json` | 7,403B | T3 portal artifact re-verification, per-advisor + firm |

---

## Key Numeric Findings

**Firm-level year-end NNA vs AUA (T3 production):**

| Year-end | Portal firm cum NNA | Portal firm total_aua | Ratio | Violation |
|---|---|---|---|---|
| 2020-12-31 | $118.20M | $27.65M | 4.28 | YES |
| 2021-12-31 | $226.26M | $59.16M | 3.82 | YES |
| 2022-12-30 | $347.57M | $122.00M | 2.85 | YES |
| 2024-12-31 | $864.47M | $953.00M | 0.91 | no |

**Account universe asymmetry:**

| Year-end | nna_atomic/ accts | canonical/nna/ accts | Flow-only |
|---|---|---|---|
| 2020-12-31 | 669 | 228 | 441 |
| 2022-12-30 | 2,844 | 1,027 | 1,817 |
| 2024-12-31 | 7,199 | 5,669 | 1,530 |

**Flow-only accts (at 2020-12-31):** 447 accts (updated from 441 after exact enumeration), $128.22M cum_inflow / $44.25M cum_outflow = $83.97M net NNA. Only 1.1-1.3% ever appear in canonical/nna/ at later dates. Default attribution: `architect='49F House'`, `relationship_id='0'`.

**Bug 1 leaderboard display identity (subsidiary):** Penfield/Kyle Sims/Hunter Lloyd all show leaderboard MAX `total_aua = 0.2012-0.2033 × book.tagged_aua`. Per-advisor Bug 1 manifestation; does NOT propagate to firm-level timeseries_chart.

---

## Ruling

**Joint (a)+(b); (c) out.**
- (a) silver/transactions inflation: RULED IN with nuance — flows are real but silver/transactions covers a wider account universe than holdings_lots in 2020-2022.
- (b) apples-to-oranges at firm grain: RULED IN — portal firm NNA (from nna_atomic/ which includes 447 flow-only accts) compared to portal firm AUA (from canonical/nna/ which excludes them).
- (c) already-resolved at T3: RULED OUT.

**FIX-TO 4 scoping:** role_aua/ refresh does NOT close the historical NNA explosion. Orthogonal concerns. CTO should consider a new FIX-TO for the universe-asymmetry display concern (recommended: Option 3+4 in decision doc — document + gate display).

---

## Compiler Tools

| Phase | Tool | Command | Result / rationale |
|---|---|---|---|
| 2 | comp-pipescript | `io C_01` | I/O manifest confirms `nna_atomic/` is WRITE via `canonical_nna_atomic_key` shadow writer; silver/transactions feeds via `load_flows_from_transactions()`. |
| 2 | aws s3 ls | nna_atomic/ head + tail | 2,296 partitions 2020-01-02 → 2026-04-16; Apr 14 gap confirmed (Bug 5). |
| 2-9 | pandas (manual) | 30+ parquet schema/value reads | Silver-scripts not in gold corpus (known blind spot from CP-AE1 session); direct inspection used. |
| 2 | aws s3api list | silver/transactions prefix | 1,774 partitions; 2020-03-06 is silver-start. |
| 4 | boto3 + pandas | employee_leaderboard.json + 3 book.json | Bug 1 0.2012 identity verified 3/3. |
| 6 | boto3 + pandas | timeseries_chart.json + firm_mix_views.json | Portal firm NNA + AUA cross-reference; matched my nna_atomic sum to penny. |
| 7 | boto3 + pandas | 699 silver/transactions partitions (2020-2022) parallel pull | 732,843 rows, no duplicates, no synthetics. |

**Role-minimum (AE):**
- `comp-pipescript deployed` — N/A (no gold run invoked).
- `comp-pipescript postdeps` — N/A (no gold script ad-hoc run).
- `comp-iam gaps` — N/A (no iam.tf change).
- `comp-blast` — attempted on `_emit_nna_atomic_shadow`; silver/shadow-writer subgraph not indexed.

Silver-layer corpus blind spot continues to be a gap. Flagged previously in CP-AE1 session 2026-04-17; not this session's scope to fix.

---

## Dispatches

No SSM / EC2 runs this session. Pure-read diagnostic per TO guardrails. All queries ran locally.

---

## MCP outbound

| To | Subject | Time (UTC) |
|---|---|---|
| 2.0.0_SA_COO | ACK STAUDT.INV1 | T141604Z |
| 2.0.0_SA_COO | Phase 0 findings — pre-Query 1 gate | T142127Z |
| 2.0.0_SA_COO | Q1 mid-flight — CANDIDATE (b) RULED IN (per-advisor initial) | T142634Z |
| 2.0.0_SA_COO | Q1 firm-level — OBSERVATION REPRODUCED; universe asymmetry mechanism | T143042Z |

---

## MCP inbound

| From | Subject | Time (UTC) |
|---|---|---|
| 1.0.0_SA_CTO | GO — ADVI_STAUDT.INV1 authorized | T141459Z |
| 2.0.0_SA_COO | Phase 0 GO — snapshot method + local Q1 approved | T142211Z |
| 2.0.0_SA_COO | INV1 SCOPE PIVOT — firm-level observation | T143000Z (approx) |

---

## Open / Followups

- **FIX-TO 4 (role_aua/ refresh)** — remains scoped as-authored for C_08 cum_* corruption. Does not close historical-NNA explosion.
- **New FIX-TO candidate** — CTO to decide whether to author a fix for the firm-level NNA/AUA universe asymmetry. Recommended: Option 3+4 in decision doc (document + display-gate).
- **Silver-layer compiler corpus** — persistent blind spot. Non-gating for INV1 but worth addressing before next silver-scoped investigation.
- **Bug 1 leaderboard 0.2012 identity** — SUBSIDIARY finding; confirms FIX-TO 1 (D_00c _compute_split_weight) will also fix leaderboard `total_aua` column. Report to CTO/COO for FIX-TO 1 acceptance criteria enrichment.

---

## Incidents / Lessons

- **Scope pivot lesson:** first reading of Q1 led me to the per-advisor Bug 1 leaderboard display defect (0.2012 identity). That defect IS real and DOES explain per-advisor "stock/flow violations" visible on the employee_leaderboard. But it does NOT explain Andrew's firm-level observation. COO's early pivot — pulling Andrew's clarification mid-flight — prevented me from synthesizing on the wrong grain. Lesson: when an observation's grain is ambiguous, always ask early. COO did this exactly right.
- **Snapshot-read method substitution** — `cum_inflow/cum_outflow` at year-end is inception-to-date per account. Summing them is mathematically equivalent to summing `daily_inflow - daily_outflow` across all daily partitions. 99.7% less I/O, same decision power. Rule-7 acceptance flex approved mid-flight.
- **Universe asymmetry pattern** — this is a non-obvious finding hiding in plain sight. nna_atomic/ is built by a separate shadow writer from silver/transactions; canonical/nna/ is built from account_gains which is built from holdings_lots. The two have different coverage characteristics in the historical window. Portal consumes both sides of this asymmetry without reconciling universes. Worth adding to docs/data as a known semantic limitation.

---

## Closeout

**Commit:** `ab1da7c8` (CLOUD, pushed 20260420T144505Z)
**7 files changed, 1407 insertions(+), 1 deletion(-)**
- data/black_diamond/diagnostics/STAUDT/INV1/historical_nna_mechanism.md (new, 14.5KB)
- data/black_diamond/diagnostics/STAUDT/INV1/query1_nna_reconstruction.json (new, 13.5KB)
- data/black_diamond/diagnostics/STAUDT/INV1/query2_silver_tx_anomaly.json (new, 18.6KB)
- data/black_diamond/diagnostics/STAUDT/INV1/query3_t3_book_nna.json (new, 7.4KB)
- org/tier2_senior/0.6.0_AE_PartnerETL/logs/2026-04-20/staudt_inv1_historical_nna_mechanism.md (new)
- org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_STAUDT.INV1.ae-historical-nna-mechanism-s3-reconstruction.md (M — status flip to complete)
- org/compiler-tools-log.md (M — auto-hook entries)

**MCP closeout trail:**
| Time (UTC) | Direction | Counterparty | Subject |
|---|---|---|---|
| T144506Z | OUT | 2.0.0_SA_COO | STAUDT.INV1 COMPLETE — (a)+(b) joint, (c) out; commit ab1da7c8 |
| T144514Z | OUT | 1.0.0_SA_CTO | STAUDT.INV1 COMPLETE — ruling + FIX-TO 4 scoping note |
| T144552Z | IN | 2.0.0_SA_COO | INV1 RAVC-CLOSED by COO — ab1da7c8 accepted; Option 3+4 recommendation being absorbed into FIX6 |

**COO RAVC-close acknowledgment (verbatim):** "ab1da7c8 accepted. Exemplary execution — two pivots handled cleanly... Your recommended Option 3 + 4 (document + gate portal display) aligns exactly with the FIX6 draft CTO authorized earlier. FIX6 (commit f1c685aa, awaiting CTO review) scopes a 3-year rolling NNA display gate at the platinum layer — essentially Option 4. Option 3 (document as known semantic limitation) will go into the ADVI_STAUDT project JSON + bug_attribution.md bridging note... Your enriched-FIX1-acceptance note — folding into the FIX1 TO revision I'm about to do in-place."

**RAVC state:** Step 4 CLOSED. TO marked complete in metadata.

---

## Current State (end of session snapshot)

- AE lane idle. Registered, heartbeat LIVE, inbox-watch running (task `bqfiyp61x`).
- Last heartbeat summary: "INV1 RAVC-closed by COO; standing by — next: Option B scoping (post-FIX1) or Option 3 doc pass"
- No pending task orders assigned to 0.6.0_AE_PartnerETL per broker status.

## Next Steps

- **[0.6.0_AE]** Standby. Next foreseen work: Option B scoping TO — AE+DS joint — covering C_01 shadow writer schema expansion (add aua_current + growth), 2,296 `nna_atomic/` re-backfill, and the 376-account shadow-writer asymmetry investigation. Gated on FIX1 landing + CTO authorization.
- **[0.6.0_AE]** Also foreseen: Option 3 documentation pass — add the universe-asymmetry note to `docs/data/` as a known semantic limitation of the historical NNA window. Will pick up as part of the ADVI_STAUDT project closeout sweep if COO tasks it to AE.
- **[2.0.0_SA_COO]** In-place revise FIX1 TO with the enriched acceptance criterion ("leaderboard `total_aua` restored to true `book.summary.tagged_aua` post-fix"); update ADVI_STAUDT project JSON + bug_attribution.md bridging note with Option 3 semantic-limitation documentation.
- **[1.0.0_SA_CTO]** Review FIX6 draft (commit f1c685aa) for the 3-year rolling NNA display gate — this is the Option 4 operationalization of my INV1 recommendation.

## Pending (carried from prior sessions, not this TO)

- **CP-DS1 Gate 1 signal** (from 2026-04-17 log) — still awaits COO re-authorization of `backfill --all` (2021-05-26 onward) + EC2 deploy of `merge-daily-incremental.py`.
- **SSM fc535736** (B_01 QA run 2026-04-15 from 2026-04-17 session) — three days old; presumed completed via natural DS workflow. Not re-polling unless asked.
- **SL-AE1 email draft** (commit 00760f48) — on COO hold pending review.
- **Schwab-bucket-access TF drift** — iam.tf import deferred pending CTO review.
- **silver/ULN converter commit** (from 2026-04-17 log) — pending; converter exists locally, not yet committed. Low urgency.
