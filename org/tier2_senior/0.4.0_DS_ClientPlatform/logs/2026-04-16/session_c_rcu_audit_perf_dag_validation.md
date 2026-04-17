# Session Log — RCU Advisor Audit + GOLD_PERF_PRD D1 + DAG Validation
**Agent:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-04-16
**Session Scope:** (1) RCU data team advisor role cross-reference + canonical taxonomy fix; (2) GOLD_PERF_PRD D1 — gold_prof.py process-tree fix + Group A/D bottleneck audits; (3) DAG validation — Group D + cross-group boundary edges

---

## Task Orders Executed

| TO | Scope | Commit | Status |
|----|-------|--------|--------|
| Ad hoc (Andrew) | RCU 141-person advisor list cross-reference vs leaderboard Primary Type | — | COMPLETE |
| Ad hoc (Andrew) | Canonical advisor role taxonomy — S3 memorialize + CTO frontend fix | — | COMPLETE |
| GOLD_PERF_PRD.D1 | gold_prof.py process-tree CPU monitor fix + S3 upload | 99d80dbd | COMPLETE |
| GOLD_PERF_PRD.D1 | Group A bottleneck audit (5 scripts) | 99d80dbd | COMPLETE |
| GOLD_PERF_PRD.D1 | Group D bottleneck audit (7 scripts) | 83dae334 | COMPLETE |
| COO dispatch (DAG validation) | Group D + cross-group edge validation; merge with ~B's A/B/C | f94c8629 | COMPLETE |

---

## Work Narrative

### 1. RCU Advisor Role Cross-Reference

Andrew provided `report1776352673541.xls` — a 141-person data team advisor list with role classifications from the RCU.

**Parsing issue:** File is HTML disguised as XLS (common web-report export). `pd.read_excel()` and `xlrd` both failed. Resolved with `pd.read_html()`.

**Finding:** 35 mismatches between RCU "Primary Type" and portal leaderboard "Primary Type". Primary disagreement: 14 cases were Consultant vs Implementor. RCU ranks Consultant above Implementor; our system had the reverse.

**Root cause:** `ADVISOR_ROLES` array order in `AdvisorsTab.tsx` governed `derivePrimaryRole()`. Prior order: `['architect','implementor','consultant',...]` — giving Implementor higher priority than Consultant. RCU order (and business intent) is the opposite.

---

### 2. Canonical Advisor Role Taxonomy

**Andrew directive:** Establish canonical order `architect > consultant > implementor > additional_advisor > local_ops`. Preserve color sequence (blue > green > purple > orange > red) but reassign to new priority order. Memorialize in S3. CTO implements frontend.

**S3 artifact created:**
`s3://opal-data-bd/gold/config/advisor_role_taxonomy.json`

```json
{
  "canonical_priority_order": ["architect","consultant","implementor","additional_advisor","local_ops"],
  "roles": {
    "architect":         {"priority":1,"color_name":"blue",  "color_hex":"#60a5fa","color_token":"advisor-blue"},
    "consultant":        {"priority":2,"color_name":"green", "color_hex":"#34d399","color_token":"advisor-green"},
    "implementor":       {"priority":3,"color_name":"purple","color_hex":"#a78bfa","color_token":"advisor-purple"},
    "additional_advisor":{"priority":4,"color_name":"orange","color_hex":"#fb923c","color_token":"advisor-orange"},
    "local_ops":         {"priority":5,"color_name":"red",   "color_hex":"#f87171","color_token":"advisor-red"}
  }
}
```

**CTO implementation (commit 4672e8d):**
- `portal/src/lib/chartColors.ts` — `ADVISOR_ROLE_COLORS` reassigned to new color mapping
- `portal/src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx` — `ADVISOR_ROLES` reordered; `derivePrimaryRole()` + filter checkboxes auto-update via array
- `portal/src/pages/AdvisorIntelligence/AdvisorPublicProfile.tsx` — `ROLE_KEYS` reordered
- `portal/src/pages/AdvisorIntelligence/FeeEfficiencyPanel.tsx` — `B8_ROLE_KEYS` reordered

---

### 3. gold_prof.py Process-Tree Bug Fix (GOLD_PERF_PRD D1)

**Bug:** `_monitor()` in `gold_prof.py` sampled only `proc.pid`. Scripts A_03, B_00, and C_06 fork `ProcessPoolExecutor` workers (~60 cores). Single-PID monitoring reported near-0% CPU for their heaviest computation phases — perf_report.json would have been structurally misleading from first nightly run.

**Fix:** Replaced single-pid sample loop with `psutil.children(recursive=True)` process-tree approach. Primes `cpu_percent()` on main process and all children at startup (first call always returns 0.0). Aggregates CPU across full process tree; divides by `ncpus` for system-relative %.

**Validation:** `python -m py_compile gold_prof.py` — EXIT 0. Committed 99d80dbd. Uploaded to `s3://opal-data-bd/code/gold/gold_prof.py` before nightly.

---

### 4. Group A Bottleneck Audit (GOLD_PERF_PRD D1)

Deliverable: `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/group_a_bottleneck_audit_2026-04-16.md`

**Summary:**

| Script | Lines | Class | Critical Issues | Est. Wall Time |
|--------|-------|-------|-----------------|----------------|
| A_00 | 735 | Already-parallelized | None | 3–6 min |
| A_01 | 548 | Pandas-CPU bound | L316–343 `.at[]` SCD loop | 4–8 min |
| A_02 | 456 | Already-parallelized | None | 2–4 min |
| A_03 | 1,739 | Already-parallelized | None — ProcessPool + TPE | 8–20 min |
| A_04 | 477 | Already-parallelized | None | 2–4 min |

**Primary finding:** Dispatch serialization is the A-group bottleneck, not intra-script compute. A_01–A_04 are all independent post-A_00. Running them concurrently (Wave A2) cuts A-group wall time from `A_00+A_01+A_02+A_03+A_04` to `A_00+A_03` (~3x).

**Only intra-script fix needed:** A_01 L316–343 `.at[]` loop → vectorized `loc[]` bulk assign (2–4 min → <1 min).

---

### 5. Group D Bottleneck Audit (GOLD_PERF_PRD D1)

Deliverable: `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/group_d_bottleneck_audit_2026-04-16.md`

**Wave structure validated:**
- Wave D1: D_00 || D_00c || D_03 (all independent, read A+B+C outputs only)
- Wave D2: D_00b || D_01 (after D_00's aua_certification_count + portal_leaderboard)
- Wave D3: D_02 (after D_01's canonical_role_aua)
- Wave D4: D_04 (terminal, after all complete)

**Prioritized TO list:**

| Priority | Target | Change | Est. Speedup |
|----------|--------|--------|--------------|
| P1 | Dispatcher | Wave D1/D2/D3/D4 concurrent structure | 3–4x D-group wall time |
| P2 | D_03 | Add TPE for S3 reads (currently serial) | 4–5x D_03 alone |
| P3 | D_02 | L1808–2095 timeseries builders — vectorize/TPE | 2–3x |
| P4 | D_01 | L984 role_lookup precompute + L2404 export TPE | 1.5–2x |
| P5 | D_00b | L233/259 merge alignment fix (correctness risk) | Minor |
| P6 | D_00c | L505 champion_streak loop vectorize | <1 min |

---

### 6. DAG Validation — Group D + Cross-Group Edges

Deliverable: `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/gold_dag_validation_2026-04-16.md` (merged with ~B's A/B/C sections)

**D-group apparent circulars — all resolved as prior-run reads:**

| Pair | Apparent Circular | Resolution |
|------|-------------------|------------|
| D_00 ↔ D_01 | D_01 reads aua_certification_count (D_00 writes) | True dep: D_01 waits on D_00. D_00 reads D_01's partner_analytics rolling window — prior-run only. Gate: D2 after D1. |
| D_01 ↔ D_02 | D_02 reads canonical_role_aua (D_01 writes) | True dep: D_02 waits on D_01. D_01 reads D_02's timeseries for trend context — prior-run only. Gate: D3 after D2. |
| D_01 ↔ D_04 | D_04 reads partner_analytics (D_01 writes) | True dep: D_04 waits on all. D_01 reads D_04 model_scores rolling window — prior-run only. Gate: D4 after D3. |

**Zero race conditions in D-group proposed wave map.**

**Cross-group boundary edges confirmed:**
- A_00 → B_00, B_01, B_02: `accounts_dimension_latest.parquet` (blocking; B scripts wait for A to complete)
- B_00 → C_05, B_02 → C_05: `canonical_lots_*` (implicit — comp tool FUNC-key gap; validated by ~B via code inspection)
- C_02 → D_01, D_00, D_00b, D_00c: `aua_certification_count.parquet` (D-group waits on all C)
- C_01b → D_01, D_02, D_00b: `canonical_role_aua/{date}.parquet`

**~B race condition caught (B_02 || B_03):** comp-pipescript io missed B_02's FUNC-key `put_object` writes to `canonical_lots_unrealized` and `canonical_lots_realized`. B_03 reads both. Running B_02 and B_03 concurrently would have caused a live race condition. Fixed in validated map: B_03 moved to Wave B3 gated on B_02.

**Comp tool gaps documented:**
1. FUNC-key write detection (put_object via helper — call graph not traversed one level)
2. PREFIX-read vs FUNC-write cross-referencing (detected separately but not flagged as dependency)

**Combined 13-phase validated map (final):**
```
PHASE_A1: A_00 || A_02 || A_03
PHASE_A2: A_01 || A_04
PHASE_B1: B_00 || B_01
PHASE_B2: B_01b || B_02
PHASE_B3: B_03 || C_05
PHASE_C1: C_00 || C_01
PHASE_C2: C_02
PHASE_C3: C_03
PHASE_C4: C_04 || C_07
PHASE_C5: C_06 || C_08
PHASE_D1: D_00 || D_00c || D_03
PHASE_D2: D_00b || D_01
PHASE_D3: D_02
PHASE_D4: D_04
```

---

## Files Modified / Created

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/gold_prof.py` | Process-tree CPU monitor fix (_monitor uses psutil.children recursive=True) |
| `org/.../deliverables/group_a_bottleneck_audit_2026-04-16.md` | New — Group A per-script bottleneck audit |
| `org/.../deliverables/group_d_bottleneck_audit_2026-04-16.md` | New — Group D per-script bottleneck audit + wave structure |
| `org/.../deliverables/gold_dag_validation_2026-04-16.md` | ~C appended D-group + cross-group sections to ~B's A/B/C base |
| `s3://opal-data-bd/gold/config/advisor_role_taxonomy.json` | New — canonical role priority + color mapping source of truth |
| `s3://opal-data-bd/code/gold/gold_prof.py` | Uploaded fixed profiler before nightly |

---

## Commits

| Commit | Author | Description |
|--------|--------|-------------|
| 83dae334 | 0.4.0_DS_ClientPlatform~C | Group D bottleneck audit deliverable |
| 99d80dbd | 0.4.0_DS_ClientPlatform~C | gold_prof.py process-tree fix + Group A audit |
| f94c8629 | 0.4.0_DS_ClientPlatform~C | DAG validation — D-group + cross-group edges |
| 4672e8d | 1.0.0_SA_CTO | Portal: ADVISOR_ROLES reorder + color reassign (canonical taxonomy) |

---

## MCP Messages Sent

| To | Subject | Time (ET) |
|----|---------|-----------|
| 1.0.0_SA_CTO | Canonical advisor role taxonomy — frontend shift required | 2026-04-16 session |
| 2.0.0_SA_COO | DAG VALIDATION COMPLETE — f94c8629 — before nightly | 2026-04-16 ~8:04 PM ET |
| 1.0.0_SA_CTO | DAG validation complete — comp tool gaps need remediation | 2026-04-16 ~8:04 PM ET |

---

## Deferred

| Item | Condition | Owner |
|------|-----------|-------|
| AC#2 6-site Travis reconciliation | Post gold-run with D_00b + C_08 on qa-runner | ~C validates when AE queues |
| GOLD_PERF_PRD D2/D3 (S3 read/write counts) | Per-script boto3 instrumentation or CloudTrail delta | Scope: D2 (instrumentation TO), D3 (CloudTrail analysis) |
| Comp tool gaps (FUNC-key write detection + PREFIX/FUNC cross-ref) | comp-tools.yaml remediation | CTO |
| Bottleneck TO dispatch (D_03 TPE, D_02 vectorize, A_01 SCD loop) | After DAG validation accepted; COO issues dispatch order | COO / next ~C session |
