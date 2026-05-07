# Inflection Wealth Management — Portal Ground Truth

Canonical verified values for Inflection on PROD. Updated after each COO-confirmed sweep session.

---

## 2026-05-07 PROD State

**Portal tag:** portal-v2.1.81 (`52a6d84c`)
**CLOUD commit:** `7b96202b5`
**Verified by:** 0.4.2_RD_AdvisorIntelligence
**Verified date:** 2026-05-07
**Session:** INFLFE.006 visual verification track close-out

### AUA (Assets Under Advisement)

| Metric | Value | Source |
|---|---|---|
| Total AUA (canonical) | $199,649,186.31 | donut / dashboard.json |
| New Clients (nmnc) | $19.7M ($19,682,951.16) | partner_analytics_quarterly |
| Existing Clients (nmec) | $179.3M ($179,287,859.58) | partner_analytics_quarterly |
| Total AUA (UI display) | $199M | page header / tiles |

### QoQ Growth (Q2 '26 vs Q1 '26)

| Tile | Value | QoQ $ | QoQ % |
|---|---|---|---|
| NEW CLIENTS | $19.7M | +$4.18M | +27.0% |
| EXISTING CLIENTS | $179M | +$15.5M | +9.5% |
| TOTAL AUA | $199M | +$19.7M | +11.0% |

Data as of: Apr 28, 2026

### Stacked Bar Chart (Assets Overview)

| Field | Value |
|---|---|
| Data source | `platinum/firm/timeseries_chart.json?firm=inf` |
| Quarter count | 25 |
| Categories | `["nmnc", "nmec"]` |
| Series colors | nmnc = `#4caf50` (green), nmec = `#2196f3` (blue) |
| Last quarter raw (Q2 '26) | nmnc=$18,661,836 / nmec=$170,585,869 / total=$189.2M |
| Last quarter displayed | ~$199.6M (FE patches last bar to donut canonical) |
| 49F gate | `timeseries_chart.json` NOT fetched for non-inflection firms (isInflectionFirm guard) |

### Leaderboard

| Advisor | Value | Source |
|---|---|---|
| peter_lee YTD NNA | $1.2M confirmed | LDRBRD.002 AC1 PASS |

### Known Data Gaps (as of 2026-05-07)

| Gap | Description | Status |
|---|---|---|
| DG-3 | City drilldown labels use name fallback not canonical key | Pending DS~A fix |
| DG-4 | Bell curve not rendering (no histogram in distribution.total) | Future enhancement |
| hh226 Q-bar timeseries | CDN invalidation confirmed (has_mv=True); 12 quarters rendering | RESOLVED |

### Inflection Advisor Structure

| Advisors | Count |
|---|---|
| Total advisors | 4 |
| Structure | Firm-level + per-advisor only (no office/bucket hierarchy) |

### Auth Path (Portal)

Login as `michael@opalinvest.com` (or `andrew@opalinvest.com`) → Select Partner dropdown → Inflection Wealth Management → firmId=inflection.
Do NOT use devBypass — broken for data-presence gates.

---

## History

| Date | Portal Tag | Key Change | Session |
|---|---|---|---|
| 2026-05-07 | v2.1.81 (52a6d84c) | Stacked bars (nmnc+nmec) + QoQ growth tiles wired | INFLFE.006 close-out |
| 2026-05-06 | 99842500 | CHECK1 auaExistingClient fix + CHECK4 CDN hh226 fix | RAVC10 |
| 2026-05-06 | 3f043ccb | DG-1 + DG-dist-1 resolved ($200M Books/Distribution) | reg sweep v10 |
| 2026-05-06 | 43411a79 | B1 Distribution city crash + B2 Books tax crash fixed | INFLFE.006-rd |
