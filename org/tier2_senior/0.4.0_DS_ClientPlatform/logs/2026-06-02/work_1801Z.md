# work cycle — 0.4.0_DS_ClientPlatform — 2026-06-02 1801Z

## ADVI_INFNNA.P2 W1 — light monthly drill series + W6 series-grain reconciliation (DEPLOYED + served-verified)

Follow-on to the 1752Z W1+W6 deploy, resolving the one open fork.

### Trigger
RD~B (W2-FE owner, CTO-directed) confirmed the GEO city(L2) + ADV client(L2)
continuous drill leaves render a PER-PERIOD TIME-SERIES (computeLegacyBarData
synthesizes {period,inflows,outflows,net} from the weekly cumulative_chart at
DistributionTab.tsx:1325-1332), NOT a windowed breakdown. So windows-only leaves
are NOT canonical-complete -- the FE charts a series there, and that's the path
carrying the 65% undercount. CTO pre-authorized + then DIRECT'd the light additive.

### Done (commits fce2d524c + e57757ce8)
- Added a LIGHT monthly-only series at city + client L2 leaves (state L1 keeps
  full weekly/monthly/quarterly). _light_series_block(). Same bucket-sum, no
  weekly sampling (P0 mechanism (a)). Served 1.73MB -> 2.47MB raw (~+1.1MB =
  CTO ~+1MB budget; ~280KB gzip). Unified, no carve.
- W6 RE-STAMPED at the new grain (CTO: "self-recon must hold at the new grain"):
  reconciliation.series_tie_max_abs_delta = sum(monthly buckets)==leaf MAX-window
  per leaf-with-series; all_pass folds window-partition AND series-tie. main()
  hard-exits if reconciliation.all_pass False.

### Served-verify PASS (generated_at 2026-06-02T18:01:09Z)
- city 34/Abbortsford series.monthly 63 pts; client peter_lee/104 (Ganje)
  series.monthly 10 pts, sum==MAX-window $96,776.01 (series tie).
- W6 all_pass=True, window delta=0.0, series_tie delta=0.0; I1/I2/I3 all 9
  windows; geo YTD==firm $4,225,486.45.
- ds-commit-gate PASS; runner code staged MATCH.

### Routed
- RD~B: GO — W2 swap computeLegacyBarData -> geo.states.<S>.cities.<C>.series.monthly + advisors.<a>.clients.<hh>.series.monthly (canonical, retires legacy weekly fallback).
- CVO: rebind harness to extended leaf series paths + W6 series_tie; still-pending I4 window-mismatch fix.
- CTO: direction executed.

W1+W6 COMPLETE pending CVO RIGID cert (vs served, post-I4-fix). W2-FE ready for dispatch.
