# FIND_INSURE wealth_management_axis design substrate (v0.2.0 candidate)

**Authored:** 2026-05-27T~21:10Z by 0.1.0_DS_MarketIntelligence~B
**Anchor:** Andrew sovereign directive 2026-05-27T~19:50Z (routed via CVO MCP `20260527T193706Z` → ~B); COO carry-forward green-light in RAVC2-ACCEPT-FINAL `20260527T2010Z`; LD-0025 additive-materializes-immediately
**Scope class:** design substrate (not PRD; CTO ratify-into-PRD path expected)
**Class:** Phase 1.5 v0.2.0 candidate (non-blocking on Phase 1 RAVC2-Accept items: 99-IMO fan-out + AC-T1/T2 telemetry)
**Companion artifacts:** `docs/briefs/find-insure-score-web-design-20260527.md` v1; `data/find/imo/config/term-taxonomy-v1.json`; `data/find/imo/scripts/gold/score_web_gold.py`

---

## 1. Andrew directive (verbatim)

> "ANY MENTION OF WEALTH MANAGEMENT IS A KEY INDICATOR. WE SHOULD NOT IGNORE COMPANIES ON THAT LIST THAT DO NOT EXPLICITLY MANAGE WEALTH/ASSET MANAGEMENT, BUT THE ONES THAT DO MENTION IT SHOULD BE RANKED FAVORABLY ON A DESIGNATED FEATURE/AXIS RELIANT ON THAT FLAG IN THE GOLD LAYER."

**Two structural binds extracted:**
1. **Not exclusion filter.** IMOs without wealth-management mentions STAY in the universe; they just don't get the additive boost.
2. **Designated feature/axis in gold layer.** Separate from the global `rollup_score`. Ranking-favorability via a NEW gold-output column.

## 2. Why a separate axis (not just a re-weighted term)

The taxonomy v1 already includes `wealth management` (business-model class, weight 0.85). Raising the weight further would inflate `rollup_score` for IMOs that mention it — but the global score commingles regulatory-license + certification + product + org-structure signal too. Andrew's directive is sharper: **wealth-management mention deserves a discrete ranking dimension**, separable from the global discrimination axis.

A separate `wealth_management_axis` lets the consumer (Phase 3 IR-team UI / Andrew strategic review) rank by EITHER:
- `rollup_score` (global asset-mgmt-transition signal, all classes)
- `wealth_management_axis` (specifically: does this IMO use wealth-management vocabulary at all)
- joint sort (`rollup_score DESC, wealth_management_axis DESC`) — the operationally interesting query

Single-score commingling forces the consumer to detect the wealth-mgmt component post-hoc by re-parsing per_term_matches. The axis surfaces it as a first-class field.

## 3. Proposed gold-output schema extension

Current `score_web_gold.py` output (per `data/find/imo/scripts/gold/score_web_gold.py:lambda_handler` + per-IMO gold partition):

```json
{
  "slug": "avantax-wealth-management",
  "rollup_score": 100,
  "rollup_raw": 38.42,
  "class_diversity_multiplier": 1.4,
  "matches": 171,
  "per_term_matches": [...],
  "per_class_summary": {...},
  ...
}
```

**v0.2.0 addition:**

```json
{
  "slug": "avantax-wealth-management",
  "rollup_score": 100,
  "rollup_raw": 38.42,
  "wealth_management_axis": {
    "score": 100,
    "raw": 12.7,
    "matches": 47,
    "term_breakdown": {
      "wealth management": {"matches": 31, "weighted_contribution": 9.2},
      "wealth management division": {"matches": 4, "weighted_contribution": 2.1},
      "wealth advisor": {"matches": 12, "weighted_contribution": 1.4}
    },
    "axis_term_scope": ["wealth management", "wealth management division", "wealth advisor"]
  },
  ...
}
```

## 4. Axis-term scope question (CTO-DECISION)

Andrew's directive says "ANY MENTION OF WEALTH MANAGEMENT" — exact phrase is unambiguous. The DESIGN-DECISION ask to CTO: which OF the following sets is the canonical scope for `wealth_management_axis`?

| Option | Scope | Tradeoff |
|---|---|---|
| **A. Literal-strict** | Only `wealth management` (case-insensitive) | Sharpest signal; misses "wealth advisor" / "wealth-mgmt division" prose variants |
| **B. Wealth-cluster (RECOMMENDED)** | `wealth management`, `wealth management division`, `wealth advisor` | Captures the prose-variation Andrew probably means; bounded enough not to dilute |
| **C. Wealth+asset-mgmt cluster** | Option B + `asset management`, `asset management division` | Andrew said "wealth/asset management" so asset-mgmt is in directive; but conflates wealth-mgmt-specific signal |
| **D. Full business-model class** | All 16 business-model terms | Equivalent to recomputing rollup over one class — defeats the "designated axis" framing |

**My lean: Option B.** Andrew said "wealth/asset management" in the directive, but framed it as "ANY MENTION OF **wealth management**" — the wealth-management vocabulary cluster, with asset-management as a sibling cluster (future `asset_management_axis` v0.3.0).

**Sibling axes future-staged:** per `work_1955Z` standing-forward — `iar_axis` (Series 65/66 + IAR), `aum_axis` (AUM + assets under management + AUS + AUA), `regulatory_filing_axis` (Form ADV + ADV Part 2). Each follows the same pattern: cluster of close-synonym terms → discrete gold-output axis.

## 5. Implementation sketch (no new code this brief; PRD-ratification first per CTO authoring lane)

When CTO ratifies axis-term scope (§4) into a PRD addendum:

1. **Taxonomy v1 → v2 amendment:** add `axis_membership` array per term:
   ```json
   {"term": "wealth management", "class": "business-model", "weight": 0.85,
    "axes": ["wealth_management_axis"], "match_type": "case_insensitive"}
   ```
2. **`score_web_gold.py` extension:** new helper `compute_axis(term_matches, axis_id)`:
   - Filter `term_matches` to terms with `axis_id` in their `axes`
   - Apply same per-match-contribution formula (location_multiplier × log(1+n)) as `rollup_raw`
   - Apply axis-specific normalization scale (TBD — likely scale-factor calibrated against full-100-IMO empirical distribution)
   - Emit axis-score in gold output
3. **Multi-axis loop:** iterate `axes_to_compute = ["wealth_management_axis", "iar_axis", "aum_axis", "regulatory_filing_axis"]` and emit each as a gold-output field
4. **No new Lambda; same `find-insure-score-web` re-invoke produces v0.2.0 gold partition**
5. **Gold-partition versioning:** new `run-date` writes to `s3://opal-data-imo/corp/{slug}/gold/web-scrape/{run-date}/score-web-v0.2.json` (gold-output co-version with taxonomy v1.1)

## 6. Acceptance criteria sketch (for CTO PRD-addendum authoring)

- **AC-WMA1.** Taxonomy v1.1 amendment with `axes` field on all in-scope terms per §4 CTO disposition
- **AC-WMA2.** `score_web_gold.py` emits `wealth_management_axis` block per §3 schema; bit-identical `rollup_score` preservation (no regression on Phase 1 AC8 spot-IMO baseline)
- **AC-WMA3.** Empirical run on 3-IMO local fixture (1st-atlantic / Avantax / Carl-Ostenson) — Avantax wealth_management_axis > 0 (probably max); 1st-atlantic = 0; Carl-Ostenson = 0 (unless body_text has wealth-mgmt prose) — confirms axis isolation works
- **AC-WMA4.** Deployed Lambda invocation 3-IMO bit-identical to local preview-fire (Phase 1 AC10 sister-pattern)
- **AC-WMA5.** Phase 3 IR-team UI/feedback-form consumes axis-score for ranking dimension (~E sister-coordinate)
- **AC-WMA6.** (Optional / future) Sibling axes `iar_axis` + `aum_axis` + `regulatory_filing_axis` follow same pattern in v0.3.0+

## 7. Defer-to-arsenal (per LD-0113 throughput-phase doctrine)

Formal lift measurement of "does the axis improve IR-team ranking-accuracy" requires comparative empirical regime against rollup-score-only baseline. **Defer §5 PRD lift-measurement to v0.2.x arsenal phase per Andrew sovereign 2026-05-27 light-fast-local-benchmarking doctrine.** v0.2.0 acceptance = mechanical-PASS on 3-IMO local fixture + Avantax-axis > 0 + 1st-atlantic-axis = 0 (isolation test).

CVO assigns expected_lift_grade at PRD-ratify + delivered_lift_grade at /verify-channel PASS-mechanical per `feedback_lift_grading_framework_cvo_judgment`.

## 8. Sibling-coordinate: Phase 3 ~E

Per `work_1955Z` standing-forward + COO RAVC2-ACCEPT-FINAL carry-forward item 3: **Phase 3 ~E sister-coordinate on axis-as-Phase-3-ranking-dimension integration.** IR-team feedback-form UI should expose `wealth_management_axis` as a sort-dimension alongside `rollup_score`. ~E's Phase 3 Lambda skeleton (anchor Brief #3 ship `b67ad03ec`) can consume the axis field once gold v0.2.0 ships. **No coordination blocker today** — substrate this brief; ratify into PRD addendum; ship gold v0.2.0; then ~E consumes.

## 9. Standing forward

- This brief = pre-PRD substrate. **Ask CTO** (via COO routing per LD-0116) to ratify §4 axis-term scope (recommend Option B) + author PRD addendum §3.4.1 wealth_management_axis spec
- On PRD-addendum ratification + GO: implement per §5 sketch (~3-4h wall — taxonomy v1.1 amend + score_web_gold.py axis-helper + 3-IMO empirical pass + deploy)
- Future sibling axes (`iar_axis`, `aum_axis`, `regulatory_filing_axis`) follow same substrate→PRD-addendum→impl pattern

— 0.1.0_DS_MarketIntelligence~B 2026-05-27T~21:10Z work-cycle:11 archetype DESIGN-SUBSTRATE
