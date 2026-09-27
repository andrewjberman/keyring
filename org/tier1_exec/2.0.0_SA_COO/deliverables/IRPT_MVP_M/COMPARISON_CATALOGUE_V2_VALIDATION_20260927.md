# Comparison catalogue v2: ~M's validation, the permitted firms, and one condition

2.0.0_SA_COO~M, 2026-09-27 ~21:5xZ, on 2.0.0_SA_COO~Y msg 102112 and CTO 102048 (Andrew-direct "call 1 yes", record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260927_195xZ_COMPARISON_PERMISSION_YES_AND_PURGE_S19_SCREENSHOTS.md`).

## 1. Identity: VALIDATED, 4 of 4 (re-graded from the raw reads, not from Y's grade)

Evidence: `IRPT_MVP_P/COMPARISON_IDENTITY_READS_W18_20260927.json`.
- The sha256 re-reads as `424eb3bf70d99752...`, which equals Y's `verification_ref`.
- 4 sent, 4 HTTP 200, stopped none, retrieved 2026-09-27T20:52:56Z.

| Id | Returned name (stripped) | Type | Catalogue label | Verdict |
|---|---|---|---|---|
| P:1728413 | Opal Long-Term | model_portfolio | Opal Long-Term | OK |
| P:1728415 | Opal Short-Term | model_portfolio | Opal Short-Term | OK |
| P:1728315 | Opal Intermediate-Term | model_portfolio | Opal Intermediate-Term | OK |
| P:1728420 | Opal Ultra Long-Term | model_portfolio | Opal Ultra Long-Term | OK |

The v2 patch (`IRPT_MVP_Y/P_COMPARISON_CATALOGUE_V2_20260927.patch`) changes only:
- `candidate_version` to `20260927.v2`;
- `admission`;
- per entry, `identity_status` VERIFIED, `entitlement_status` WORD_GRANTED_FIRMS_PENDING_M, `permission_scope` and the
  verification refs;
- `permitted_firm_ids` is still `[]`.

## 2. The permitted firms (FWD-11: "firms that already see these models in Opal's Model Portfolios view")

- **Instrument:** the served Model Portfolios per-firm artifact, `s3://opal-data-portal-v2/platinum/mdpf/<firm>/aggregate-aua-timeseries.json`
  (`by_model`), read 21:4xZ.
- **Name mapping:** the portal's canonical model map (`portal/src/lib/modelPortfolioColors.ts` :108-124, :245-263):
  - Long-Term Conservative is Long Term;
  - Long-Term Aggressive is Ultra-Long Term.
- **Denominator:** the Model Portfolios partner firms (`portal/src/pages/ModelPortfolios.tsx` ALL_MDPF_PARTNER_FIRMS):
  49financial, inflection, cottonwood. `global` is the Opal aggregate, and `demo` only views Global.

| Catalogue key (YCharts id) | MDPF model | 49financial (as of 09-24) | inflection (09-24) | cottonwood (09-22) |
|---|---|---|---|---|
| opal_long_term (P:1728413) | opal_long_term_conservative -> Long Term | 3,279 accts, $805.4M | 90, $13.9M | 123, $57.7M |
| opal_short_term (P:1728415) | opal_short_term -> Short Term | 704, $104.5M | 29, $6.7M | 126, $19.9M |
| opal_intermediate_term (P:1728315) | opal_intermediate -> Intermediate Term | 1,606, $296.2M | 202, $76.6M | 255, $80.3M |
| opal_ultra_long_term (P:1728420) | opal_long_term_aggressive -> Ultra-Long Term | 1,387, $203.8M | 32, $2.3M | 11, $1.1M |

**Resolved:** `permitted_firm_ids = ["49financial", "inflection", "cottonwood"]`. All 3 of 3 partner firms see all 4 of
4 models with accounts in each. The ids are the registry slugs the consumer's fixtures use (`test_maintained_sources.py`
:280).

## 3. One condition, found in the reads: the YCharts objects carry 49F-named benchmarks

- Every read returns a `benchmark` naming 49F: "49F Long Term Benchmark" (P:1728413), "49F Short Term Benchmark",
  "49F Intermediate Benchmark", and **"49F Long Term Benchmark" again for P:1728420 (Ultra Long-Term)**.
- If a Comparison or Multi-Comp page ever shows the model's `benchmark`, an INF or Cottonwood client reads another
  firm's name. That is a cross-firm reference on a client-facing report.
- The Ultra Long-Term object also carries the Long Term benchmark, which is a YCharts configuration fact, not ours.

**Condition proposed:**
- 49financial admits now.
- inflection and cottonwood admit once the rendering is shown never to print the YCharts `benchmark` field for a
  comparison model (2.0.0_SA_COO~Y's template), or once the benchmarks are renamed in YCharts.

## 4. The consumer

`_scope/maintained_sources.resolve_comparison_fields` (:514-600) still requires candidate v1 and refuses every
selection. The admitting consumer is ~M's to write. It must:
- accept v2 only;
- require `identity_status == "VERIFIED"`;
- require an entitlement that is granted, with the viewer's firm in `permitted_firm_ids`;
- never read `security_id` or `live_proven` as a fallback.
It follows the ruling on section 3.

## Addendum 1 (~21:5xZ): CTO ruling (a), then the proof, re-validated by ~M; all three firms admitted

- **CTO 102141, ruling (a):** 49financial admits now. inflection and cottonwood admit when ~Y proves the benchmark
  field never renders, and "M re-validates and admits ... with no new word needed".
- **The proof:** ~Y msg 102147, `IRPT_MVP_Y/COMPARISON_BENCHMARK_NEVER_RENDERS_20260927.md` @2e79ddb62d.
- **~M's own re-read** of both certified PDFs from `s3://opal-data-ycharts/research/20260911/variants/` (3 report.pdf
  under the prefix; the two matched by sha256):

| Report | sha256 | Pages | "49F" | "49 Financial" | "Benchmark" | lowercase "benchmark" | control: model name |
|---|---|---|---|---|---|---|---|
| Comparison 14141824 | f01cbd48a577.. | 31 | 0 | 0 | 0 | 2, both glossary prose (ETN definition; style-box "size-specific benchmarks") | Opal Long-Term x31 |
| Multi-Comp 14141847 | 0a67ecf76732.. | 35 | 0 | 0 | 0 | 2, both glossary prose (active-investing definition; style box) | Opal Short-Term x29, Intermediate-Term x28 |

- **Result:** the benchmark field does not render on these templates. **`permitted_firm_ids = ["49financial",
  "inflection", "cottonwood"]`** for all 4 entries.
- **Limit carried from ~Y's record:** a YCharts template change could start printing it. The certifier guard ("fail
  any non-49financial report carrying 49F") is not built; it waits on its own word.

## The values ~M's consumer will require (sent to ~Y to set in templates.json)

- `candidate_version` = `irpt-ycharts-comparison-candidate.20260927.v2`.
- Per entry:
  - `identity_status` = `VERIFIED`;
  - `entitlement_status` = `GRANTED`;
  - `permitted_firm_ids` = the 3 firms above;
  - `permitted_principal_classes` = `["FIRM_ADVISOR", "FIRM_OPERATIONS", "OPAL_GLOBAL"]`;
  - `verification_ref.evidence_sha256` = `424eb3bf70d9975250cc8351de025930f72715b76b8586cad936515e86250194`.
- The consumer also pins the validated (key, vendor_id, evidence sha, firms) set in code, so an edit to the catalogue
  alone widens nothing.
