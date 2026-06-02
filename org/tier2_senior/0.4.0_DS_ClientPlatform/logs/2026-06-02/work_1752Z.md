# work cycle — 0.4.0_DS_ClientPlatform — 2026-06-02 1752Z

## ADVI_INFNNA.P2 W1 + W6 — unified canonical GEO/client emit + self-reconciliation (DEPLOYED + served-verified)

DS-led, GEO/client analog of F5. P0 (mechanism (a) weekly-sampling) gated this;
CTO ruled unified-additive; my emit-cost confirmed tiered-series keeps it unified.

### W1 — canonical GEO (state/city) + per-client leaves (commit fc6974fcf)
Additive extension of INF_D_00f.advisor_nna_canonical.py (the F5 spine), dims
{adv[existing], geo, client}. Straight re-aggregation of the SAME
canonical_nna.net_nna over all dates (P0: NO _weekly_sample) — eliminates the
65% continuous-GEO undercount.
- load_account_geo() (accounts_v2 state/city) + load_client_names() (accounts_dimension).
- geo: state L1 (full weekly/monthly/quarterly series) + city L2 (windows-only); per-advisor clients[] (household-grain, windows-only). Tiered series per emit-cost (full-everywhere +21MB vs tiered: served 1.73MB / ~400KB gzip).
- Partition-complete catch-alls: Other (state join-miss, 2 accts) / no_city / unassigned.

### W6 — self-reconciliation + granularity_coverage (commit 820561227, CTO-critical Andrew-direct e5b28ee4f)
Stamped into the artifact (reuses the W1/W4 partition sums): reconciliation
{method, tolerance_usd, all_pass, max_abs_delta, per_window[...]} +
granularity_coverage {n_advisors,n_states,n_cities,n_client_leaves,dimensions,series_policy}.
AE daily checker + CVO W4 harness bind to all_pass / max_abs_delta.

### In-build self-check (W4 invariants I1/I2/I3) — hard-exit on mismatch
sum(states)==firm; sum(cities)==state; sum(clients)==advisor — to-the-cent ALL 9 windows.

### Deploy (Rule 13 DS cycle)
ds-commit-gate PASS (caught a window_order scope bug pre-deploy). commit -> push CLOUD -> stage to s3://opal-data-inf/code/gold/ (MATCH) -> run --upload (light boto3 emit, same served key the runner writes).

### Served-verify PASS (platinum/firm/advisor_nna_canonical.json, generated_at 2026-06-02T17:51:31Z)
- geo 18 states / 92 cities / 297 client leaves; keys geo + reconciliation + granularity_coverage present
- W6 all_pass=True, max_abs_delta=0.0
- geo YTD sum == firm YTD == $4,225,486.45 (was $1,456,681 / 34.5% via the lossy weekly path)
- peter_lee clients sum == peter_lee YTD == $1,665,551.07 (matches CVO reference exactly)
- existing firm/advisor keys untouched (F5 consumers unaffected — additive)

### CVO W4 harness (pre-published, ran pre-RAVC2): 632 PASS, 1 I4 fail = HARNESS window-mismatch
I4 compared my geo-YTD ($4.23M) vs snapshot partner_analytics single-quarter ($1.62M q_current). My data ties same-window (geo q_current==snapshot $1,619,579.03; geo YTD==header_metrics YTD $4,225,486.45). Flagged CVO to fix I4 (+ exit-code-on-BLOCKED bug) + rebind to served artifact incl W6.

### Notes / downstream
- W5(b): state key '34' (malformed) passes through faithfully from accounts_v2 into canonical geo (partition still ties); W5(b) cleans upstream — NOT a W1 blocker.
- Drill-render-type (city/client = chart vs windowed) routed by CTO to RD~B (W2-FE). Emitted windows-only (default); light monthly-only series held as a ready additive if W2 confirms continuous drill.
- Gates W2 (FE repoint + weekly-fallback removal) + W4 (CVO RIGID) + W6.2 (AE daily checker).

### RAVC2 -> CTO + COO + CVO. Probe/build scripts gitignored (.runtmp/).
