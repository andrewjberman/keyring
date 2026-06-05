# /spot-check cycle 20 — MDLP_DISTFIX I3 RAVC2 independent verify: PASS

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO · 2026-06-05 ~1950Z · checkpoint c69bc94c5 -> post-startup
**Trigger:** COO dispatch 192952Z — independent I3 RAVC2 verify for MDLP_DISTFIX (DS filed 192336Z)

---

## Startup state

- Respawn from cycle 19 (prior session ended ~1827Z)
- MSTR correction received (194647Z): /spot-check still my standing loop (LD-0157 did NOT retire CVO loop)
- Crons armed: /spot-check 20m (72c6b4d8) + /verify-channel 2h (ac251b3d)
- Monitor armed: task ba5zr06nb (persistent)

---

## MDLP_DISTFIX I3 — CVO Independent Verify

### RAVC2 claims (DS 192336Z via COO)

- Commit: `25154e161` (DS orion-gold lane, adv-view bypass fix)
- S3 byte-verified deploy: 19:09:27Z
- AE republish: 191506Z (inf-gold-layer-runner --single INF_D_04)
- CF flush: EVTSA9VEHNZVH /api/scoped/advisor-intelligence/*
- Served adv.current p10 = $11,729.60 / min = $1,052.42 (all >= $1K)
- Sum invariant: adv.total_dist.sum = geo.total.sum = $206,082,063.00

### CVO independent actions

1. **S3 artifact pull** — `s3://opal-data-inf/platinum/firm/partner_analytics_monthly.json`
   downloaded directly (484.5 KiB); not relying on DS/AE reads.

2. **Deployed code pull** — `s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py`
   downloaded directly (200.5 KiB); not relying on pre-checkout repo state.

### Verify results

**Served artifact (adv.current.total_dist) — independently read:**

| field | value | gate |
|---|---|---|
| min | $1,052.42 | >= $1K: PASS |
| percentiles.p10 | $11,729.60 | >= $1K: PASS (was $8.42) |
| p50 | $106,531.29 | monotonic: PASS |
| sum | $206,082,062.65 | preserved: PASS |
| count | 875 accounts | full population: PASS |

Note: p10 is nested at `total_dist.percentiles.p10` (not top-level). DS's $11,729.60 matches to the cent ($11,729.6 in JSON, rounding to $11,729.60). Sum is $206,082,062.65 vs DS-reported $206,082,063.00 — penny rounding, consistent.

**Sum invariant (cross-view, independently computed):**

| window | adv.total_dist.sum | geo.total_dist.sum | match |
|---|---|---|---|
| current | $206,082,062.65 | $206,082,062.65 | PASS |
| m1 | $206,237,585.70 | $206,237,585.70 | PASS |
| m2 | $198,163,102.03 | $198,163,102.03 | PASS |
| m3 | $188,320,423.56 | $188,320,423.56 | PASS |

All 4 windows: adv sum = geo sum. Invariant confirmed.

**Code consistency — deployed S3 script:**

- `_calc_distribution_stats_adv`: confirmed `return floored_distribution_stats(aua_values, _ADV_SUMMARY_NUM_BINS)` with MDLP_DISTFIX I3 inline comment. This function gates ALL per-advisor donut `distribution` entries.
- `_build_adv_view` `by_segment` loop: confirmed `_seg_stats = floored_distribution_stats(aua_series.tolist(), _ADV_SUMMARY_NUM_BINS)` with MDLP_DISTFIX I3 adv-view bypass fix comment. `sum` and `count` preserved on full series (no reassignment).
- `_build_adv_view` `total_dist` block: confirmed MDLP_DISTFIX I3 comment + `aua_series_total = acct_aua['aua']` (no filter reassignment = sum stays full).
- `floored_distribution_stats` occurrences in deployed file: 6 (consistent with geo + adv block coverage + shared helper uses).

Fix is structurally present and consistent with DS's description. No discrepancy between committed code and S3-deployed code.

**AE f0b9fe8f3 corroboration:** AE 0.7.0 independently confirmed all 4 surfaces GREEN in work-cycle:0015. Consistent with CVO served read. No cross-agent contradiction.

### CVO observations (not gate-blocking)

1. **P2 — dual-loop architecture:** `_build_adv_view` iterates `adv_agg` twice — once for donut `segments` (calls `_calc_distribution_stats_adv`) and once for `by_segment` histograms (calls `floored_distribution_stats` directly). Both paths are now floored, but the dual-loop pattern creates a dual maintenance surface: a future dev adding a third percentile block would need to know to use `floored_distribution_stats` or `_calc_distribution_stats_adv`. Not a regression; P2 refactor candidate.

2. **Scoped open item (DS-flagged, CVO-noted, not blocking):** DS noted "aua has no percentiles block (flagged)" — the AUA view does not have an equivalent floor. Outside I3 scope; DS-flagged correctly. Not a CVO gate.

3. **Snohomish/SNOHOMISH duplicate key:** The served artifact contains duplicate keys `'Snohomish'` / `'SNOHOMISH'` in a geo sub-object. PowerShell ConvertFrom-Json rejects the file; Python json.load is lenient (last-key wins). This is a pre-existing issue from the INFNNA W1 CVO W4-CONDITIONAL finding (city-key case normalization). Not related to I3; not a regression from 25154e161.

### VERDICT

**RAVC2 PASS — I3 adv-view fix independently verified.**

- adv.current.min = $1,052.42 >= $1K: PASS (was $8.42 dust)
- adv.current.percentiles.p10 = $11,729.60 >= $1K: PASS
- Sum invariant: adv = geo = $206,082,062.65 all 4 windows: PASS
- Deployed code contains MDLP_DISTFIX I3 fix in both by_segment and total_dist paths: PASS
- No DS-missed gaps (1 P2 structural note, 1 scoped open item both non-blocking)

**Remaining gate (not CVO's):** Andrew-visual on ADV panel. COO to loop Andrew / /frontend-dev per DS's own filing.

COO acceptance follows this PASS (or Andrew-visual if that gate is required first).

---

## Other delta (quick scan — not primary focus this cycle)

- MDPF_COUNTS Parts 2+3: validate nightly + DE FE re-point pending from cycle 19; no new commit observed. Will pick up at next spot-check cycle.
- FIND_DUALBIZ registration still pending (cycle 19 recurring watch). Will pick up.
- DS work_1946Z.md present — will read next cycle if new work landed.

---

## Compiler Tools

| Tool | Result |
|---|---|
| S3 pull: platinum/firm/partner_analytics_monthly.json | 484.5 KiB DOWNLOAD_OK |
| S3 pull: code/gold/INF_D_04.client_portal_summary.py | 200.5 KiB DOWNLOAD_OK |
| Manual parse: adv.current.total_dist | min=$1,052.42 p10=$11,729.60 sum=$206,082,062.65 — all gates PASS |
| Manual parse: cross-window sum invariant | All 4 windows adv==geo — PASS |
| Code grep: floored_distribution_stats | 6 occurrences in deployed script — consistent |
| Code read: _build_adv_view body | by_segment + total_dist both use floored helper — PASS |

No standard comp-* tools required (this is a post-deploy served-artifact CVO verify, not a gold-edit or portal-change cycle).

— 3.0.0_SA_CVO
