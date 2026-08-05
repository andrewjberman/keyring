# Phase 0 — Initial lifecycle_value proposals for the 29 C3.ii Semantic Verticals

**Purpose:** the ratification sitting's working paper (State/Friction design s.2). Each row is
a PROPOSAL — **Andrew's ratification is the assertion** (`lifecycle_class` is producer-asserted
by ratified law; enum `PERMANENT | TRANSIENT | EVENT_CREATED | DORMANT | LEGACY | RETIRED |
UNDECLARED`). **UNDECLARED is used honestly**: where this seat's evidence is thin, the row says
so rather than guessing — those five rows are the sitting's real work.
**Author:** `1.0.0_SA_CTO~B`, 2026-08-04. **Roster source:** comp-estate `--matrix` v1.7
(29 verticals — the denominator is the matrix's, re-derive at the sitting).
**Grain note — RATIFIED 2026-08-05 (Andrew-direct, sitting vertical 1), no longer a proposal:**
the value names the BUSINESS FUNCTION's life-shape at the vertical grain. Interior implementation
churn (a route consolidating, a runner rewritten) is NOT a vertical lifecycle shift — it is what
R2's State layer watches and proposes on; the "shift-watch" column seeds exactly that.
VERBATIM WARRANT: *"It is a permanent project nevertheless, although underlying conventions and
resources may shift around with migrations/consolidations/refactoring/etc."*
⚠ This resolves a real grain tension rather than restating a preference: the rule bank's polarity
table (`org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml:405-454`) is written at ARTIFACT grain —
`absent_at_rest` / `present_at_rest` are questions about whether a key or resource EXISTS. At
VERTICAL grain those questions do not apply directly; the polarity table governs the vertical's
ARTIFACTS, while the ratified value governs the FUNCTION. Rule 24's same-grain postulate is
satisfied by keeping those two statements separate, not by collapsing them.

**SITTING PROGRESS: 2 of 29 ratified** (advi-bd, advi-cot -- 2026-08-05). **CANONICAL MEDALLION FORM ratified same sitting:** bronze (raw vendor) -> silver (parquet queryable) -> gold (processed analytics) all under `s3://opal-data-assets/{vendor}/{firm}/`; serving = `s3://opal-data-portal-v2/platinum/`. TARGET, not current state -- deltas measured in the record below. Records:
`ANDREW_DIRECT_20260805_advi_bd_ratified_and_the_0833_0824_correction.md` (vertical 1 + the
full-account-string ruling + the grain convention) and
`ANDREW_DIRECT_20260805_canonical_medallion_form_and_advi_cot_ratified.md` (vertical 2 + the
four-tier canonical form, with the measured current-state deltas).

⚠ **ROW-4 FLAG raised by the vertical-1 correction, not yet ruled:** row 4 (`canonical-schwab`)
cites "Two daily scheduled Schwab CRS pulls ENABLED (08242234 + 08335338)". Those are now known to
be **two DIFFERENT PRODUCTS' masters** (MDPF and ADVI respectively), not two feeds of one vertical
— so `canonical-schwab`'s boundary versus `advi-bd`/`mdpf` needs Andrew's word at its row rather
than inheriting my original framing.

| # | Vertical | Proposed | Evidence (one line) | Conf | Shift-watch note (R2 seed) |
|---|---|---|---|---|---|
| 1 | advi-bd | **PERMANENT — RATIFIED 2026-08-05** | **`s3://opal-data-assets/schwab/08335338/`** — the 49F Black Diamond master. ADVI = "Advisor Intelligence", an Opal data product served by the Portal, scoped PER ADVISOR (49 Financial here). Layout `_ops/ bronze/ gold/ meta/ silver/`; daily scheduled ingest live. ⚠ MY ORIGINAL ROW CITED `08242234` = **`s3://opal-data-assets/schwab/08242234/`, which is MDPF "Model Portfolios"** (`_ops/ bronze/ meta/ silver/` — no `gold/`). Corrected on Andrew-direct, verified by `aws s3 ls` | HIGH | — |
| 2 | advi-cot | **PERMANENT — RATIFIED 2026-08-05** | **`s3://opal-data-assets/blackdiamond/cottonwood/`** (`bronze/ gold/ meta/ silver/`) — the BLACK DIAMOND vendor tree, NOT a Schwab account; 49F's sibling is `.../blackdiamond/49f/`. Cottonwood BD feed live (cot-bd-session-daily ENABLED); relationship-grain ruling 08-04 active | HIGH | **Interior route consolidating legacy→canonical (Andrew's own R2 exemplar)** — State watches; under the ratified grain convention this is NOT a lifecycle shift |
| 3 | advi-inf | PERMANENT | INF partner serving live; P0 aum-metrics work this session; MDPF_CANRTE covers its direct-silver leg | HIGH | canonical-route redesign in flight |
| 4 | canonical-schwab | PERMANENT | Two daily scheduled Schwab CRS pulls ENABLED (08242234 + 08335338); six silver tables | HIGH | — |
| 5 | causality | UNDECLARED | sys-causality-engine exists; this seat holds no activity/consumption evidence either way | — | resolve at sitting |
| 6 | ceo-digest | UNDECLARED | UNASSIGNED-RESIDUE structure; no schedule/consumer evidence at hand | — | resolve at sitting — DORMANT candidate |
| 7 | cma | PERMANENT | yang-analytics family (capital-market assumptions), yang pipeline active | MED | — |
| 8 | correlation | PERMANENT | yang-analytics family, active engine | MED | — |
| 9 | data-refresh | PERMANENT | opal-data-refresh-api live + P0 visibility work this window | HIGH | — |
| 10 | etf-reports | PERMANENT | ETFS month-end email armed (Sep-1 fire, cron ENABLED); ETFS canon program active | HIGH | ETFS CANON question open — parked items keyed on it |
| 11 | factor-tilts | PERMANENT | yang-analytics family | MED | — |
| 12 | graph-platform | PERMANENT | comp-tools/graph substrate — the estate's own cognition layer, daily commits | HIGH | — |
| 13 | insurance | UNDECLARED | sys-estate-ops-platform member; zero session evidence of activity or consumers | — | resolve at sitting — DORMANT candidate |
| 14 | m365-mcp | PERMANENT | Live gateway (tools active this session); ms-ingest-liveness just registry-repaired | HIGH | — |
| 15 | macroeconomics | PERMANENT | dual-structure (macro-data engine + yang) | MED | — |
| 16 | market-overview | PERMANENT | Portal MO live; spans 4 structures (widest with trade-submission) | HIGH | — |
| 17 | mdpf | PERMANENT | Flagship Model Portfolios product, served + verified (v2.1.148 promote arc closed 07-24) | HIGH | MDPF_CANRTE canonical-route redesign + json/mdpf/* teardown PARKED (ETFS CANON) — State watches |
| 18 | model-portfolios | PERMANENT | SEV1 must-always-be-right portal surface (critical-surfaces.yaml) | HIGH | — |
| 19 | news | PERMANENT | News pipeline serving; NOTE: news_scanner tree ARCHIVE'd in RCG cycle-3 (interior pruning, not vertical decline) | HIGH | interior pruning underway |
| 20 | ops-internal | PERMANENT | The estate's own ops function; spans 4 structures | HIGH | — |
| 21 | partners | PERMANENT | Partners API serving (cross-firm defence-in-depth records active) | HIGH | — |
| 22 | portal-infra | PERMANENT | The portal serving substrate (CloudFront/auth/routes) | HIGH | — |
| 23 | portfolio-management | PERMANENT | Spans estate-ops + pm-suite; portfolio surfaces serving | MED | — |
| 24 | positioning | PERMANENT | yang-analytics family | MED | — |
| 25 | security-scanner | UNDECLARED | CONTRADICTORY evidence, honestly split: security-sweep-daily ARCHIVE'd as orphan (cycle-3, absent all 3 signals) while security-sweep-comprehensive is LIVE but UNMANAGED (Group-3 Rule-1 finding, adoption/decommission pending) | — | resolve at sitting — LEGACY candidate; coldness discriminator (comp-debris) runs in the morning-wave TO anyway |
| 26 | smartx | PERMANENT | smartx-assets-daily-pull scheduled+live; egress lifted; NOTE smartx_query REFERENCE_KEEP + exporter fallback-config latent finding | HIGH | exporter config latent path |
| 27 | ticketing | UNDECLARED | TicketCenter exists in portal; TAXSMA ticket-scoping triage pending ~3wks with a dead seat — activity evidence thin | — | resolve at sitting — TRANSIENT vs PERMANENT is Andrew's call |
| 28 | trade-submission | PERMANENT | Widest structure span (5); trade-pipeline lanes + trade-authorizer live | HIGH | — |
| 29 | valuation | PERMANENT | yang-analytics family | MED | — |

**Tally:** 24 proposed PERMANENT (14 HIGH / 7 MED conf) + 5 UNDECLARED (causality, ceo-digest,
insurance, security-scanner, ticketing). Zero TRANSIENT/EVENT_CREATED/DORMANT/LEGACY/RETIRED
proposed — **deliberately**: those are exactly the values that should come from Andrew's
knowledge or from R2's Friction evidence, not from a seat's one-evening survey. If the sitting
rules several PERMANENTs down to DORMANT/LEGACY, that is the system working.

**At the sitting:** (1) re-derive the 29 from `comp-estate --matrix` (the count is the
matrix's, not this table's); (2) rule the 5 UNDECLARED; (3) confirm or amend the 24; (4) CVO
lands the ratified set in the canon at the RESOLVER_DEFROST seam — which simultaneously
creates the per-vertical prose homes (description/enrichment) that the first fire proved
missing, giving future R1/R2 output a real landing surface.
