---
name: Inflection mix classification approach
description: Andrew's directive on asset-class mix data source for Inflection — prefer Orion-native over BD ETFClassifier; Opal securities are V2 concern
type: project
---

For Inflection asset-class mix (DIAGFIX.008), investigate Orion manual_api first for native classification/security-master data before building BD ETFClassifier solution.

**Why:** Orion may expose asset_class or category fields via their API (positions, securities master) that are cleaner and more authoritative than classification via ETFClassifier regex. Using Orion-native data keeps INF pipeline clean of BD dependencies.

**Opal model portfolio securities:** Opal has its own internal classification for securities in Opal model portfolios. For Inflection V1, any Opal securities in their portfolio are purely coincidental (new client, no managed Opal portfolios yet) and likely negligible AUA. Do NOT build Opal-classification override logic for V1. Revisit in a later phase when Inflection may deliberately allocate to Opal model portfolios.

**Priority of data sources for mix classification (V1):**
1. Orion API native classification (if available via manual_api) — preferred
2. ETFClassifier regex-fallback (BD lib, no DDB access) — fallback
3. Opal securities classification — V2/future only

**How to apply:** When DS reports DIAGFIX.008 Step 0 findings, COO routes build using Orion-native if available, regex-fallback if not. If Opal-branded tickers appear in Inflection holdings, flag count but do not special-case them for V1.
