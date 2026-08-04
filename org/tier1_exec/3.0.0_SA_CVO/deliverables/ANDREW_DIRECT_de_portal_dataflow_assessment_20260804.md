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

— 3.0.0_SA_CVO
