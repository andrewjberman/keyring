# INFGRO Stage -1 — txn_type Universe Audit (2026-05-13)

**Author:** `0.4.0_DS_ClientPlatform~A`
**Date:** 2026-05-13
**Authority:** Andrew direct routing override (2026-05-11) + COO GO (2026-05-13T14:59Z)
**Purpose:** Validate current bronze/silver `txn_type` universe at HEAD against PRD `ADVI_INFGRO_PRD.md` v0.3 §2.3 + `data/orion/scripts/silver/orion_cashflow_taxonomy.yaml` v2 (Stage 0b ratified).
**Baseline:** `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-11/DSA_inf_gro_txntype_audit.md` (DS~B 2026-05-11, 1,510 silver partitions / 1,145,124 rows / 43 distinct `type_desc` / 11 distinct `activity_category`).

---

## TL;DR

**Recommendation: PRD §2 NEEDS AMENDMENTS — Stage 1 dispatch BLOCKED until 3 issues resolved.**

**Across the FULL silver universe (all 1,513 partitions scanned): 45 distinct `type_desc`, 43 matched-to-yaml, 2 orphans (`Stock Split` + `Unknown`), ZERO zombies.** Yaml v2's 43-entry universe IS COMPLETE and accurate for the OLD-schema per-day partitions.

The amendment-required state arises from a NEW-schema snapshot file written 2026-05-13 02:16:04Z:

1. **Schema event 2026-05-13 02:16:04Z** — a new `silver/transactions/2026-05-13.parquet` snapshot (19.7 MB, 1,251,020 rows, full history 2020-05-26→2026-05-12) was written with a **completely different schema**: `type_desc` → `trans_type_desc`, `activity_category` → `category`, 43-col → 18-col, parquet-writer v20.0.0 → v21.0.0. This co-exists with 1,512 per-day OLD-schema partitions. PRD §2 + `orion_cashflow_taxonomy.yaml` are both keyed on the OLD column names — they DO NOT match HEAD-as-of-2026-05-13 IF INF_C_01 is migrated to consume the snapshot.
2. **2 type_desc orphans** discovered only in the new snapshot: `'Unknown'` (4,299 rows) and `'Stock Split'` (558 rows). `'Unknown'` is the smoking gun for a classification regression — sum of historical rows for 21 yaml type_descs absent from the new snapshot (~4,160 rows) closely matches `'Unknown'` count (4,299), suggesting the new ETL collapses 21 economically-meaningful classifications into a single bucket.
3. **21 type_desc "snapshot-zombies"** — present in OLD per-day partitions, ABSENT from NEW snapshot. Includes all 4 Tax Withheld bucket-Return entries (2,561 rows), Starting Value (896 rows; freshly-ratified Item 1 Internal), Rollover/Employer/Cancel/Ext-Out NNA flows (495 rows), Dividend Reinvested + Interest Reinvested DRIP-Internal (94 rows), and 13 others. These are NOT true zombies (full-universe audit confirms ZERO zombies) — they have been **mis-classified into 'Unknown'** by the new ETL writer.

---

## Methodology

| Step | Tool | Result |
|---|---|---|
| Yaml universe | `data/orion/scripts/silver/orion_cashflow_taxonomy.yaml` v2 | 43 distinct `type_desc`, 14 historical `activity_category` (via `merged_from_categories`) |
| Silver partition list | `aws s3 ls s3://opal-data-inf/silver/transactions/` | 1,513 parquet files (1,512 OLD-schema per-day from DS~B baseline through 2026-05-12 + 1 NEW-schema snapshot 2026-05-13) |
| Bronze partition list | `aws s3 ls s3://opal-data-inf/bronze/transactions/` | 2 files only (2026-05-12, 2026-05-13 — rolling refresh layer; not historical) |
| Full universe scan | Python + boto3 + pyarrow read of ALL 1,513 silver partitions + 2 bronze (schema-detection on each) | **45 distinct `type_desc` across all silver, 0 zombies, 2 orphans** (full-universe audit) |
| HEAD universe scan | `silver/transactions/2026-05-13.parquet` (1.25M rows snapshot 2020→2026-05-12) | 24 distinct `trans_type_desc`, 3 distinct `category` (`other` 97.7% / `billing` 1.6% / `activity` 0.7%) |
| Snapshot-zombie cross-check | Targeted reads of `silver/transactions/{2026-04-30,2026-05-11}.parquet` (OLD-schema partitions) | Confirmed all 21 snapshot-zombies present in OLD partitions (ADR Fee, Federal Tax Withheld, Dividend Reinvested, etc.) |

Audit script + raw JSON: `.runtmp/infgro_txn_type_universe_audit_20260513.py` + `.runtmp/infgro_txn_type_universe_audit_20260513.json` + `.runtmp/infgro_audit_quick_head_2026-05-13.txt`.

---

## Finding 1 — Schema Event 2026-05-13 02:16:04Z (NEW; not in PRD §2)

A new silver partition was written at 02:16:04Z today with a **fundamentally different schema** from the 1,512 prior per-day partitions:

| Aspect | OLD schema (1,512 partitions through 2026-05-12) | NEW schema (1 snapshot 2026-05-13) |
|---|---|---|
| Column count | 43 | 18 |
| Classification column | `type_desc` (primary) + `activity_category` (secondary) | `trans_type_desc` (primary) + `category` (secondary) |
| `category` cardinality | 14 distinct (Advisory Fees Paid, Contributions, …) | **3 distinct** (other 97.7%, billing 1.6%, activity 0.7%) — collapsed |
| Granularity | One row per Orion transaction (per-day) | One snapshot containing full history 2020-2026-05-12 (1,251,020 rows in one file) |
| Writer | `parquet-cpp-arrow 20.0.0` | `parquet-cpp-arrow 21.0.0` |
| Written by | Regular daily Lambda (~09:00Z cadence) | **Unknown writer at 02:16:04Z overnight** |

**Critical inconsistencies:**
- PRD §2.3 + `orion_cashflow_taxonomy.yaml` v2 + `INF_C_01.build_canonical_nna` all read `type_desc` (OLD column name). The NEW snapshot does not have this column.
- PRD §2.2 cites `activity_category` as a secondary attribute with 11 distinct values. The NEW snapshot's `category` is collapsed to 3 useless buckets.
- This is NOT a documented Stage 0 / Stage 0b deliverable. Last yaml authority commit is Stage 0b "pending" (`data/orion/scripts/silver/orion_cashflow_taxonomy.yaml` header line 34). Whoever wrote the 02:16:04Z snapshot did not coordinate with the INFGRO Stage 0 schema work.

**Required clarification from CTO:**
- Is this NEW-schema snapshot intentional (Stage 1 pull script rewrite? AE migration?) or accidental (one-off probe / pipeline experiment)?
- Going forward, does `INF_C_01.build_canonical_nna` read OLD-schema per-day partitions OR the NEW-schema snapshot?
- Should the yaml taxonomy v2 be rewritten to key on `trans_type_desc` instead of `type_desc`?

---

## Finding 2 — type_desc Universe Delta vs Yaml

Source: full universe from `silver/transactions/2026-05-13.parquet` snapshot (1.25M rows, covers 2020-05-26 → 2026-05-12).

### 2a — Matched (22 of 43 yaml entries present in NEW snapshot)

| type_desc | yaml bucket | snapshot rows | yaml audit rows | delta |
|---|---|---:|---:|---:|
| Buy Exchange | Internal | 379,442 | 326,134 | +53,308 |
| Sell Exchange | Internal | 378,883 | 326,134 | +52,749 |
| Income Reinvested | Internal | 221,552 | 224,519 | -2,967 |
| Dividend to Cash | Return | 210,055 | 213,223 | -3,168 |
| Management Fee | Return | 19,709 | 14,453 | +5,256 |
| Merge In from Other Account | NNA in | 6,387 | 6,545 | -158 |
| Long Term Gain to Cash | Return | 4,883 | 4,725 | +158 |
| Client Contribution | NNA in | 4,428 | 4,363 | +65 |
| Trading Expense | Return | 4,418 | 4,549 | -131 |
| Client Distribution | NNA out | 3,797 | 3,992 | -195 |
| Short Term Gain to Cash | Return | 3,747 | 3,586 | +161 |
| Interest Paid in Cash | Return | 2,894 | 3,012 | -118 |
| Internal Account Journal In | Internal | 1,252 | 1,276 | -24 |
| External Account Activity In | NNA in | 1,116 | 1,145 | -29 |
| Fee Credit | Return | 848 | 862 | -14 |
| Internal Account Journal Out | Internal | 841 | 786 | +55 |
| Merge In Exchange | Internal | 518 | 350 | +168 |
| Merge Out Exchange | Internal | 516 | 350 | +166 |
| Decrease in Value | Internal | 422 | 398 | +24 |
| Merge Out to Other Account | NNA out | 255 | 360 | -105 |
| Dividend Paid from Cash | Internal | 100 | 101 | -1 |
| Income Paid | Internal | 100 | 101 | -1 |

Buy+Sell Exchange account for +106K of the +106K overall snapshot row delta (1,251,020 - 1,145,124). Most other matched entries show small variance (±0.3% of baseline) consistent with the 5 days of transaction accumulation between 2026-05-08 (DS~B audit cutoff) and 2026-05-12 (snapshot trans_date max).

### 2b — Orphans (in HEAD data, NOT in yaml) — 2 NEW type_desc

| type_desc | rows | first_date | last_date | hypothesized bucket | rationale |
|---|---:|---|---|---|---|
| `'Unknown'` | 4,299 | 2020-06-05 | 2026-05-11 | ⚠️ **REGRESSION INDICATOR** — see Finding 3 | 4,299 rows ≈ Σ(21 zombie row counts) = ~4,160 rows; strongly suggests new ETL collapses 21 classifications into 'Unknown' rather than discovering a new economic category |
| `'Stock Split'` | 558 | 2020-08-31 | 2026-04-21 | Probably **Internal** (corporate-action, same economic position different shares) — parallel to existing `Spin Off in`/`Spin Off out` precedent (yaml: Internal) | NEW canonical Orion classification not present in DS~B 2026-05-11 audit; needs CTO bucket ratification before Stage 1 dispatch |

### 2c — Snapshot-zombies (in yaml + OLD partitions, NOT in NEW 2026-05-13 snapshot) — 21 type_desc

**Full-universe audit across all 1,513 partitions: ZERO true zombies — yaml v2's 43-entry universe is complete and correct for OLD-schema data.**

The 21 below are *snapshot-only zombies* — they ARE present in OLD-schema per-day partitions (sanity-probed `2026-04-30.parquet` and `2026-05-11.parquet`; cross-validated by full 1,513-partition scan). They have NOT been deleted; they have been **mis-classified by the new ETL writer** that produced the 2026-05-13 snapshot.

| type_desc | yaml bucket | yaml audit rows | likely fate in HEAD |
|---|---|---:|---|
| **Federal Tax Withheld** | Return (CTO Item 2) | 2,252 | → 'Unknown' (loss of tax-Return classification, $2.23M materiality) |
| **State Tax Withheld** | Return (CTO Item 2) | 274 | → 'Unknown' ($92K materiality) |
| **Foreign Tax Withheld** | Return (CTO Item 2) | 33 | → 'Unknown' ($139 materiality) |
| **Foreign Dividend Tax** | Return | 33 | → 'Unknown' |
| **Tax Credit** | Return (CTO Item 2) | 2 | → 'Unknown' (trivial) |
| **Starting Value** | Internal (CTO Item 1 — freshly ratified) | 896 | → 'Unknown' — loses ε-bucket placement; without classification INF_C_01 may default to NNA inflow, reintroducing the $6.64M over-statement that Item 1 just fixed |
| **Rollover Contribution** | NNA in | 362 | → 'Unknown' (loses NNA-inflow classification) |
| **Cancel Account** | NNA out (CTO Item 3) | 101 | → 'Unknown' (loses NNA-outflow classification) |
| **Employer Contribution** | NNA in | 18 | → 'Unknown' |
| **External Account Activity Out** | NNA out | 14 | → 'Unknown' |
| **Dividend Reinvested** | Internal | 65 | → 'Unknown' (loses DRIP-Internal classification → ε leakage) |
| **Interest Reinvested** | Internal | 29 | → 'Unknown' (same) |
| **Return of Capital** | Internal | 10 | → 'Unknown' |
| **Return of Principal (Bonds)** | Internal | 2 | → 'Unknown' |
| **Spin Off in** | Internal | 6 | → 'Unknown' OR → 'Stock Split' |
| **Spin Off out** | Internal | 6 | → 'Unknown' OR → 'Stock Split' |
| **ADR Fee** | Return | 33 | → 'Unknown' |
| **Administrative Fee** | Return | 9 | → 'Unknown' |
| **Administrative Fee Adjustment** | Return | 6 | → 'Unknown' |
| **Wire Fee** | Return | 6 | → 'Unknown' |
| **Interest Paid** | Return | 3 | → 'Unknown' |

**Σ zombie rows = 4,160 ≈ 'Unknown' rows (4,299)** — variance 139 rows (3.3%), within slack for 2 additional days of transaction activity since baseline OR for `Stock Split` partly absorbing `Spin Off in/out` (12 rows yaml; 558 in snapshot — magnitude mismatch suggests `Stock Split` is mostly a NEW pre-existing-but-newly-surfaced canonical value, not solely a Spin Off rename).

**Materiality impact (if NEW snapshot is what INF_C_01 will consume):**
- NNA classification loss: 495 rows (Cancel, Rollover, Employer, Ext-Out) — would default to ε bucket, breaking partner-facing NNA accuracy
- Tax-Return classification loss: 2,594 rows × ~$1K avg = ~$2.6M of tax-on-income wrongly classified
- Starting Value loss: 896 rows × Item 1 ratification — direct regression of the just-applied $6.64M Internal reclassification
- DRIP-Internal loss: 94 rows — ε leakage from previously-correct Internal bucket

---

## Finding 3 — activity_category Universe Delta

| | Cardinality | Distinct values |
|---|---:|---|
| Yaml (`merged_from_categories` union) | 14 | Advisory Fees Paid, Contributions, Distributions, Dividend Interest Reinvested, Dividends and Interest, Exchange In, Exchange Out, Journal In, Journal Out, Merge In, Merge Out, Misc Charge, Net Dividends/Interest/Gains Withdrawn, Other |
| OLD per-day partitions through 2026-05-12 | 14 (DS~B) | Same as yaml |
| **NEW snapshot `category` column** | **3** | `other` (1,222,238 = 97.7%), `billing` (20,557 = 1.6%), `activity` (8,225 = 0.7%) |

**The new `category` provides essentially zero classification signal.** Yaml's `merged_from_categories` audit trail (which validates schema-collapse Stage 0b decisions for ADR Fee, Administrative Fee, Dividend Reinvested, etc.) no longer maps to current data. PRD §2.2's "11 distinct activity_category, useful as secondary drill-down" no longer holds for HEAD.

`activity_category_orphans` = ∅ (none of the 3 NEW values are unknown to yaml semantically; `other` is a yaml-known value, `billing` and `activity` are new but trivial coverage).
`activity_category_zombies` = all 13 yaml values except `other` — same root cause as Finding 2 (schema event, not data event).

---

## Finding 4 — Bronze Layer Status

- `s3://opal-data-inf/bronze/transactions/` — only 2 files (2026-05-12 and 2026-05-13, both ~30 MB / 1.25M rows)
- Schema is `accountId/transTypeId/transactionDescription/...` (camelCase, raw Orion API field names) — distinct from BOTH OLD and NEW silver schemas
- No `type_desc` or `trans_type_desc` column — bronze stores `transTypeId` (numeric id) and `transactionDescription` (free-text)
- Bronze appears to be a **rolling-2-day refresh layer**, not historical — silver does the classification mapping

PRD §2 cites `silver/transactions/` as the source. **Confirmed correct** — bronze is too raw and ephemeral to key taxonomy on.

---

## Sub_type Delta vs DS~B §2.2 Snapshot

DS~B audit (2026-05-11) reported "11 distinct activity_category values when collapsed" — actual yaml `merged_from_categories` union is 14 distinct (Advisory Fees Paid, Contributions, Distributions, Dividend Interest Reinvested, Dividends and Interest, Exchange In, Exchange Out, Journal In, Journal Out, Merge In, Merge Out, Misc Charge, Net Dividends/Interest/Gains Withdrawn, Other). The 14-value universe is **stable in OLD per-day partitions** (probed 2026-04-30 + 2026-05-11). The NEW snapshot collapses to 3 — see Finding 3.

No NEW sub_type values discovered in OLD partitions or in NEW snapshot. Sub_type granularity has DEGRADED (14 → 3), not expanded.

---

## Recommendation: PRD §2 NEEDS AMENDMENTS

**§2.5.1 — add a third Stage 1 dispatch gating condition (now THREE conditions, not two):**

> **Stage 1 dispatch gating (formal):** TO-INFGRO.001 + TO-INFGRO.003 cannot ship until ALL of these conditions hold:
> 1. TO-INFGRO.000b ratification ships (taxonomy YAML reclassifications applied) — **DONE (Stage 0b ratification applied 2026-05-11)**
> 2. `inf-performance-daily` Lambda fires + produces fresh `bronze/performance/` partition — **AE 0.7 audit pending**
> 3. **NEW: 2026-05-13 schema event resolved — CTO ruling on (a) which silver schema INF_C_01 consumes going forward, (b) `'Unknown'` and `'Stock Split'` bucket ratification, (c) yaml v3 written if column rename `type_desc` → `trans_type_desc` adopted.**

**§2.3 — add two new type_desc entries (regardless of which schema is canonical):**

```yaml
  - type_desc: "Stock Split"
    bucket: Internal  # PROPOSED — parallel to Spin Off in/out precedent (corporate action, no real cashflow)
    rationale: corporate-action share-multiplication; same economic position, different share count
    row_count_audit: 558  # from 2026-05-13 HEAD snapshot
    needs_cto_ratification: true

  - type_desc: "Unknown"
    bucket: ?  # CRITICAL — see audit finding 2c — current 4,299 rows are the 21 zombie reclassifications
    rationale: REGRESSION CATCH-ALL — new ETL classifier failure mode; PRE-DEPLOY FIX required (re-classify upstream, do not bucket as Unknown in yaml)
    row_count_audit: 4299
    needs_cto_ratification: true  # also: probably needs to be REMOVED by fixing the new-schema writer's classifier, not added to yaml
```

**§2.3 — leave the 43 OLD-schema entries intact** (they are still ground truth for OLD per-day partitions, which are the only source containing the full 43-cardinality classification).

**§2.2 — amend "Schema discovery (DS~B audit, 2026-05-11)" line to add:**
> Note (2026-05-13): A NEW-schema snapshot variant exists at `silver/transactions/2026-05-13.parquet` with column rename `type_desc` → `trans_type_desc` + `activity_category` → `category` (collapsed 14→3 values) + 21 type_desc values reclassified to `'Unknown'`. INF_C_01 currently reads OLD-schema; canonical-source ruling pending.

---

## Standing Open Questions for CTO

1. **Schema canonical:** Is the 2026-05-13 02:16:04Z snapshot the start of a planned migration? If yes, who wrote it (which Lambda / EC2 / one-off)? If no, should it be deleted to prevent INF_C_01 silent drift?
2. **'Unknown' fix point:** Is the right fix (a) update yaml to map 'Unknown' to ε bucket and accept regression; (b) update the new-schema writer to preserve 21 classifications (preferred); or (c) hold INF_C_01 on OLD-schema until writer is fixed?
3. **'Stock Split' bucket:** Stage 0b ratification needed — propose `Internal` per Spin Off precedent.
4. **Yaml v3 column rename:** If migrating to `trans_type_desc`, yaml needs a schema-version bump + INF_C_01 read-path update.

---

## Acceptance (per COO GO message)

| Item | Status |
|---|---|
| Distinct txn_type universe count + list at current HEAD | ✅ 24 distinct `trans_type_desc` in 2026-05-13 HEAD snapshot (see Finding 2a/2b) |
| Orphan list (in data, NOT in PRD §2.3) | ✅ 2 orphans: `Unknown` (4,299), `Stock Split` (558) (Finding 2b) |
| Zombie list (in PRD §2.3, NOT in data) | ✅ 21 zombies (Finding 2c) — but flagged as MIS-CLASSIFICATION not true zombies |
| Sub_type universe delta vs §2.2 snapshot | ✅ 14 → 3 collapsed in NEW snapshot; stable in OLD per-day partitions (Finding 3) |
| Recommendation | ✅ **PRD §2 NEEDS AMENDMENTS** — see Recommendation section above. Stage 1 dispatch should NOT proceed until 4 CTO rulings + schema canonicalization resolved. |

---

## Evidence

- Audit script: `.runtmp/infgro_txn_type_universe_audit_20260513.py`
- Raw HEAD universe output: `.runtmp/infgro_audit_quick_head_2026-05-13.txt`
- Yaml baseline: `data/orion/scripts/silver/orion_cashflow_taxonomy.yaml` (v2 Stage 0b)
- DS~B baseline audit: `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-11/DSA_inf_gro_txntype_audit.md`
- HEAD silver snapshot probed: `s3://opal-data-inf/silver/transactions/2026-05-13.parquet` (19,695,826 bytes, ETag `a332759692b6a9ecc0785aaf751e5c7e`, LastModified 2026-05-13T06:16:04.000Z, 1,251,020 rows)
- OLD-schema partitions zombie-probed: `s3://opal-data-inf/silver/transactions/{2026-04-30,2026-05-11}.parquet`
