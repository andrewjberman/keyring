<task_order>
<metadata>
  <to_id>ADVI_FEREFI.W2</to_id>
  <project>ADVI_FEREFI</project>
  <title>DS: emit real per-period *_fee_paying/*_no_fee canonical sub-streams (Inflection since-inception back-attribution + 49F surface) — kills the FE synthetic "approx"</title>
  <assigned_to>0.4.0_DS_ClientPlatform</assigned_to>
  <issued_by>2.0.0_SA_COO</issued_by>
  <issued_date>2026-06-03</issued_date>
  <status>dispatched — GO (feasibility accepted as build plan)</status>
  <dispatch_held>false</dispatch_held>
  <priority>HIGH — gates the ADVI_FEREFI #6 FE tail (W1); Andrew-direct directive.</priority>
  <references>
    <ref type="prd">docs/architecture/ADVI_FEREFI_PRD.md item 6 (Andrew-direct since-inception back-attribution)</ref>
    <ref type="feasibility">org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-06-03/work_1406Z.md (DS feasibility — accepted as the build plan)</ref>
    <ref type="rule">CLAUDE.md Rule 17 (fee classification = business logic = GOLD tier, not silver) + Rule 14/14a/15 (gates, future-import) + comp-validate before signal</ref>
  </references>
</metadata>

<scope>
Emit REAL per-period canonical fee-split sub-streams so the FE `hasFeeSplitSeries` (AdvisorAnalytics.tsx:235-239) fires on `total_aua_fee_paying` / `nna_canonical_fee_paying` / `inflows_canonical_fee_paying != null`, killing the synthetic `computeSyntheticFeeRatio` (feeBucket.ts:209) + dropping the "approx" label.

## INFLECTION (back-attribution build — gold-tier):
- No per-period fee history exists upstream (Orion Billing Dim = one current row/account, earliest Period End 9/30/2025). Back-attribution is the ONLY path = exactly Andrew's directive.
- Path: current per-account `is_fee_earning` (HAVE) x AUA-timeseries periods (HAVE) -> classify each period's AUA as fee-paying iff acct currently fee-earning -> roll account->household -> emit `total_aua_fee_paying`/`_no_fee` (+ nna_canonical_fee_paying / inflows_canonical_fee_paying variants) per period.
- Gold-tier (classification = business logic, Rule 17). No historical billing pull (none exists).

## 49F (surface existing infra):
- Substream infra already exists (black_diamond C_01b/D_00c emit aua_fee_paying/aua_no_fee at role_aua grain + leaderboard fee_breakdown). Likely small: confirm the Lifetime Activity per-period timeseries surfaces `total_aua_fee_paying` so hasFeeSplitSeries fires (verify SERVED artifact). Note C_01b backfill periods use equal-split (aua_fee_paying=0) for pre-data — carry that honesty.

## HONESTY (carry into the emit + flag for FE label, per DS work_1406Z):
1. Inflection pre-Q3-2025 fee-paying is INFERRED (back-attributed current status), NOT measured — emit must not imply measured history.
2. Back-attribution can't detect fee-status CHANGES before Q3-2025 (no data) — accepted per directive; label honestly.
3. "No approx" is true for current/recent window; older periods inferred (INF) / equal-split-backfilled (49F) — don't over-claim full-history "no approx". (FE label decision = Andrew/RD at FE-#6 time.)
</scope>

<acceptance>
- [ ] Gold script emits per-period total_aua_fee_paying/_no_fee (+ nna/inflows canonical variants) for Inflection (back-attributed) + 49F (surfaced); future-import + ds-commit-gate + comp-validate all-pass.
- [ ] SERVED artifact verify: the Lifetime Activity timeseries the FE reads carries the substreams -> hasFeeSplitSeries fires (confirm against the actual consumed artifact, not a partial proxy).
- [ ] DS commit+push+deploy per Rule 13 cycle; RAVC2 to COO (CC CTO) with the served-artifact confirmation + the 3 honesty flags restated for the FE-label decision.
- [ ] On W2 served-verify -> COO signals RD-AI to do the #6 FE tail (drop the approx span).
</acceptance>
</task_order>
