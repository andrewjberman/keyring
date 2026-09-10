# Andrew-direct: Holdings/model-overlay v1 brief

**Seat:** 4.0.0_SA_CRO. **Date:** September 10, 2026. **Parent:** Lightweight Investor Reporting, WS4; final Holdings tab.

## Direction, verbatim

> ok now we need to draft a brief for the final tab, the model overlay. this should basically be keyed off advisors, i think we have data to fulfill all of this from opal-data-assets for daily holdings. I dont even feel like dealing with time series views in v1 even though we should do it. The bigger concern and peak priority for that tab is figuring out how to overlay models, displaying model holdings percentages (good opportunity to use Asset Category/Taxonomy we developed e.g. Client SMAs Models, etc and drilldowns, all of which I think should be done in Pie Chart/Radial form. The work here is mostly backend and figuring out shapes and joins and movement for the various partners shapes. The frontend is just gonna be the same pattern as always, borrow same components, lay out some cards with various charts and summaries and so on. I think you can probably just comp-find around and see what you can get, maybe look into the D1 Model Overlay prior art in case there is anything useful in there. /brief-create

## Scope to carry

Create a child brief within the existing Investor Reporting umbrella for WS4. Prioritize advisor-scoped current holdings and partner-specific model attribution, taxonomy/category allocation percentages and drilldowns. Reuse portal components and chart/card patterns, preferring pie/radial presentation. Time-series views are deferred from v1. Research the named model-overlay prior art and verify which source, identity and model-join data are actually available in opal-data-assets. Earlier partner routing remains: 49F Schwab 0833 holdings with SmartX models, Inflection Orion holdings with Eclipse models, and Cottonwood Black Diamond holdings with Rebalancer models. The brief does not register a separate project or issue task orders.
