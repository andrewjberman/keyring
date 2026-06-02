# work cycle — 0.4.0_DS_ClientPlatform — 2026-06-02 1725Z

## TO ADVI_INFNNA.P2.P0 — continuous-GEO NNA flow-loss mechanism (COMPLETE, READ-ONLY)

3rd Inflection PRD (Andrew-direct), GEO analog of F5. P0 = the investigation pass
gating W1 canonical-GEO emit correctness.

### VERDICT: mechanism (a) weekly-snapshot-SAMPLING loss — NOT definitional
Both producers read the SAME `gold/canonical/canonical_nna_*.parquet` and the SAME
`net_nna` (= daily_inflow − daily_outflow). Zero definitional difference in source.
The only transform divergence is `INF_D_00d.cumulative_chart.py` `_weekly_sample`
(L458-459): it sub-samples the DAILY flow series to ~1 date/7, dropping ~6/7 of the
flow. F5 (`INF_D_00f`) sums net_nna over ALL dates; its own docstring (L340-343)
already names the contrast: "INF_D_00d.build_nna_adv_view which weekly-SAMPLES".

### Reproduced to-the-cent (live S3, 2026-06-02)
| method | firm YTD net_nna | vs canonical |
|---|---|---|
| FULL daily sum (F5 canonical) | $4,225,486.45 | = canonical firm YTD to-the-cent |
| served cumulative_chart.nna_geo YTD (weekly) | $1,456,681.11 | 34.5% (65.5% loss) |
| served nna_adv YTD | $1,456,681.11 | byte-identical (same weekly producer) |

Weekly grid keeps 22 of 102 active YTD days. FE strips 'Other' → top-8 display
$1,211,999.57. Probes: .runtmp/infnna_p0_flowloss_probe.py + _faithful_repro.py (gitignored).

### W1 emit-spec determination (gates released)
- STRAIGHT re-aggregation of canonical_nna by state/city — full daily sum, no _weekly_sample, no definitional reconcile.
- state/city NOT in canonical_nna (cols: account_id, advisor_key, custodian, daily_inflow/outflow, date, n_*_events, net_nna, rep_bucket) → join account_id→state/city via accounts_v2/household_dim (the SAME join INF_D_00d already uses L437-446; data exists + joins cleanly today).
- per-client leaves: groupby(advisor_key, account/household) sum net_nna; window-explicit (F5 vocab QTD/YTD/MAX/1Y/3Y/q-strip).
- W5(c) "8 vs 14 states" auto-resolves (top-N artifact of INF_D_00d, gone with complete canonical emit).

### Routing
RAVC2 mechanism finding → CTO + COO + CVO (evidence-base author). On receipt, COO+CTO co-author W1 correct-by-construction.

### Also this session
- W2D CVO RAVC2-VERIFY: CLOSED-PASS (independent, 7/7 both firms, 0 mismatch) — no action.

### Finding doc
docs/briefs/infnna-p0-geo-nna-flowloss-mechanism-20260602.md
