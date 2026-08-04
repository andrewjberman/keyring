# Andrew-direct — DE portal-dataflow assessment dispatch (2026-08-04 ~02:3xZ, CVO terminal)

**Recorded per XXX.md record-verbatim law; relayed as a GO to `0.4.0_DE_ClientPlatform` same turn
(Andrew instantiated the seat; live at dispatch, PID 17772).**

## VERBATIM

> I'm bringing on 0.4.0_DE_ClientPlatform right now, and I want you to tell them all this and have
> them run comp-blast and comp-cluster to assess the data-flow that is actually displaying on the
> portal. for example, the opal-data-portal-v2/json/ buckets should not be displaying any model
> portfolio assets with regard to aua-aggregate-timeseries.json, account-distribution.json, and
> aum-metrics.json.

**Key-name note (mapping, not correction):** "aua-aggregate-timeseries.json" as spoken maps to the
live artifact family `aggregate-aua-timeseries.json` (hyphen family; the underscore twin
`aggregate_aua_timeseries.json` is the stopped legacy plane).

## CVO reading

DE assesses the AS-DISPLAYED dataflow (rendered portal -> fetch URLs -> resolved objects ->
writers), grounded on the deployed plane, using comp-cluster (page-rooted panel/data-source map)
+ comp-blast (kuzu universe). Acceptance example named by Andrew: NO Model Portfolios view may be
displaying content resolved from `opal-data-portal-v2/json/` for the three families
`aggregate-aua-timeseries.json` / `account-distribution.json` / `aum-metrics.json`. Any json/-
resolved display = a finding with the full bucket+key + the deployed fetch site. Briefing packet
= the corrected census @ MDPF_LEGACY_ROUTE_BLAST_CENSUS_20260804.md + its correction trail.

## ADJUDICATION ADDENDUM (CVO verdict on the F1 finding FORM — 2026-08-04 ~03:1xZ)

Two true observations, different layers, NOT a contradiction — ruled explicitly so this is never
re-litigated:

- **Andrew, eyewitness (~0305Z at the CTO terminal, CTO-recorded):** the 07-23
  `json/portfolios/aum-metrics.json` is NOT displayed on any view. **TRUE at the render layer** —
  no view renders the artifact AS an artifact; nothing on screen names it.
- **DE, measured (@b48634789a; CVO-validated on independent probes):** the Model Portfolios page's
  BASE metrics — model cards, quarterly totals, and the page-render GATE (`ModelPortfolios.tsx:519`
  + `:585`) — are COMPUTED FROM that file, live-exercised (6+ router rewrites 08-03), plus three
  indirect consumers via `getAUMMetrics()`. **TRUE at the read layer.**

**VERDICT ON FORM: F1 STANDS AS A READ-DEPENDENCY FINDING, not a render finding.** The values and
the gate users see derive from an artifact frozen 2026-07-23 16:57 ET (period 07-22 data; writer
flag-disabled that same day — the freeze is the half-decommission's own signature; the live edge
today is the READS, not production, per CTO's primitive check). The read-dependency form is the
SHARPER hazard precisely because it defeats eyewitness inspection: no rendered surface names the
source, the page's visible as-of stamp honestly reads the OTHER (timeseries) family, so 07-22
metrics wear a fresh page with zero on-screen tell.

**Left to Andrew (naming act, unchanged):** whether his verbatim criterion ("the json/ buckets
should not be displaying... aum-metrics.json") binds the json CHANNEL (CVO reading: yes — and
displaying-values-computed-from IS displaying assets with regard to that family) or `json/mdpf/*`
narrowly. Fix shape either way is already unconditionally in the wave remainder (canonical
aum-metrics emitter leg -> platinum, then repoint the four consumers); no dispatch waits on the
ruling.

— 3.0.0_SA_CVO
