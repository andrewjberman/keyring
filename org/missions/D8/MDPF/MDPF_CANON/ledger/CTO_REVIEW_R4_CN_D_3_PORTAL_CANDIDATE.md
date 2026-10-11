# CTO review -- MDPF_CANON round 4, CN-d-3 portal candidate (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~06:5xZ)

**Candidate:** portal nested branch `wk-MDPF_CANON-12-portal` @133fb8af: 2 files, +52 -3 (`src/lib/pairedProvenanceRead.ts`,
`src/pages/ModelPortfolios.tsx`). Render: `deliverables/2.0.0_SA_COO~D1/round4/runs/cn_d_3_global_trend_candidate_133fb8af.png`.
Asked by `2.0.0_SA_COO~D1` msg 3571.

**Verdict: APPROVED for portal DEV, on one condition.** The CVO grades CN-d-3 AC3 MET first, including the tooltip read the packet
leaves open: on a sampled additive date, the tooltip rows add to the Total.

Read:
- Both series are FIELD READS of the artifact's own `sma_additive_aua` and `tax_additive_aua`. There is no arithmetic, and a null is
  "no band", never zero (`readGlobalEnterpriseSeries`; both dataPoint sites).
- The bands are Global only (`!timeSeriesData.isPerFirm`, and the legend is gated on `effectiveFirmId === 'global'`). Per-firm views do
  not change.
- In the render, the 2026-10-08 bar now reaches the aggregate (~$2.15B), with thin bands above Other AUA. That is round-3 item 3's
  intent: the stack meets the line.
- Note, not blocking: "Additive SMA sleeves" (#6366f1) sits close to "Opal Moderate Income Tax Efficient" in the legend, and
  "Tax-Managed SMA" (#ff4f1f) close to "Ultra Short-Term". The chart already carries same-colour pairs among the small cottonwood
  models, so this adds no new class of ambiguity. A palette pass belongs to the colour registry (3F-P3), not this cell.

Landing: a DEV fast-forward by the box manager under /govern once AC3 reads MET. The page is Opal-internal (Global partner selector),
so no word from Andrew is needed for DEV.

-- 1.0.0_SA_CTO~DELL1
