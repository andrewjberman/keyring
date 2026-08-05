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

**SITTING PROGRESS: 4 of 29 ratified** (advi-bd, advi-cot, advi-inf, canonical-schwab -- 2026-08-05). **CANONICAL MEDALLION FORM ratified same sitting:** bronze (raw vendor) -> silver (parquet queryable) -> gold (processed analytics) all under `s3://opal-data-assets/{vendor}/{firm}/`; serving = `s3://opal-data-portal-v2/platinum/`. TARGET, not current state -- deltas measured in the record below. Records:
`ANDREW_DIRECT_20260805_advi_bd_ratified_and_the_0833_0824_correction.md` (vertical 1 + the
full-account-string ruling + the grain convention) and
`ANDREW_DIRECT_20260805_canonical_medallion_form_and_advi_cot_ratified.md` (vertical 2 + the
four-tier canonical form, with the measured current-state deltas).

⚠ **GOLD-TIER ASYMMETRY ACROSS THE THREE ADVI SCOPES — surfaced by row 3's grounding, an
OBSERVATION not a challenge to any ratification.** Measured 2026-08-05:

| ADVI scope | source tree(s) | tiers present |
|---|---|---|
| 49F | `schwab/08335338/` | `bronze silver gold` |
| Cottonwood | `blackdiamond/cottonwood/` | `bronze silver gold` |
| **Inflection** | `orion/inflection/` **and** `eclipse/inflection/` | `bronze silver` — **NO `gold/` in EITHER** |

**RESOLVED SAME SITTING — Andrew-direct, and the cause is CONFIRMED, not inferred.** He read the
asymmetry as *"very quesitonable ... that points to migration not being completed there"* and named
two candidate causes. Ground-read confirms the first, **and it is LIVE TODAY, not a legacy remnant**:
`s3://opal-data-inf/gold/eclipse/2026-08-05/model_portfolio_{summary,households,accounts}.parquet`
written 2026-08-05 10:51:06Z. **The migration moved bronze and silver into `opal-data-assets` and
left gold behind in the superseded bucket, still producing.** His second candidate (producers writing
gold straight into a shared location such as a DDB) is **UNTESTED and not excluded** — the two are
not mutually exclusive.
My earlier guess — the top-level `opal-data-assets/gold/` prefix — was NOT the answer; it stays open
as a separate §4(a) item. *(Recording that my tidy two-items-become-one hypothesis was wrong: it was
plausible, it closed two open threads at once, and it was not what the measurement said.)*
**Full record + the medallion-intent ruling + the named consolidation fix:
`OPAL_CONSOLIDATION_INF_GOLD_GAP_AND_MEDALLION_INTENT_20260805.md`.**
Does NOT disturb row 3's PERMANENT: an incomplete migration is interior churn, which the ratified
grain convention explicitly excludes from being a lifecycle shift. It lands on the SHIFT-WATCH seed.

⚠ **ROW-4 FLAG raised by the vertical-1 correction, not yet ruled:** row 4 (`canonical-schwab`)
cites "Two daily scheduled Schwab CRS pulls ENABLED (08242234 + 08335338)". Those are now known to
be **two DIFFERENT PRODUCTS' masters** (MDPF and ADVI respectively), not two feeds of one vertical
— so `canonical-schwab`'s boundary versus `advi-bd`/`mdpf` needs Andrew's word at its row rather
than inheriting my original framing.


> **FINDING (row 4) - ONE EC2 CARRIES TWO IDENTITIES, AND THE LIVE ONE IS NAMED "SPIKE".**
> Andrew asked me to confirm which box is canonical because he recalled "another quartz spike EC2".
> Ground-read: **there are not two boxes doing this. `i-0f3d57a97f14727af` IS both names.**
>
> | | value |
> |---|---|
> | `EC2_MANIFEST.json` (Rule 8 source of truth) | `canonical-schwab-si2` |
> | LIVE AWS `Name` tag | **`quartz-si2-spike`** |
> | IAM role / inline policies | `quartz-si2-spike-role`, `quartz-si2-monolith-write`, `quartz-si2-spike-inline` |
> | other tags | `project=SCHWAB_SSOT.DERISK-1`, **`reversible=true`** |
> | state | **RUNNING** (t3.large) - one of only 3 running instances in the estate |
> | all 3 Schwab EventBridge rules target | `quartz-si2-spike (i-0f3d57a97f14727af)` |
>
> **IT IS THE CANONICAL ONE, on Andrew's own discriminator (the REST backend):**
> `sdd-daily-pull.ps1` hits **`https://si2.schwabinstitutional.com/fileservices/SDDServices/`**
> (SDD = Schwab Data Delivery), header: *"ADVI OPAL_ASSETS -- CANONICAL DAILY SDD PULL
> (Andrew-direct 2026-07-13). Replaces the SI2 GUI auto-download channel."*
>
> **THE OTHER BOX IS REAL BUT IS NOT THIS PATH:** `canonical-schwab-runner`
> (`i-0ed92ce2e72f505dc`, STOPPED) - manifest purpose *"build_canonical_daily.py (17 silver + G1-G14
> gold) on production 01_raw/, **parallel/NOT-served**"*. A parallel non-served compute path is worth
> its own look against the standing no-shadow-channel veto; NOT chased here.
>
> **WHY THE NAMING IS A RISK AND NOT A COSMETIC GRIPE:** a box tagged `spike` + `reversible=true` +
> `DERISK-1` is asserting *disposable*, while actually being the sole live ingest for BOTH 49F Portal
> products. Any cleanup sweep keyed on "spikes" or "reversible" would terminate production for ADVI
> and MDPF simultaneously. That is exactly the failure the lifecycle rule bank names as primary -
> *"a false-positive (decommission a deliberate belt) is THE named failure mode"* - except here the
> misleading label is on a LIVE PRODUCER, not a dormant belt. **The spike graduated to production and
> its name never did.**
>
> Incidental, from the same file and worth preserving - the incident that created this path:
> the SI2 GUI channel *"exited rc=0 on ~22 consecutive cycles over 11 days while landing NOTHING
> (delivery folder frozen at 2026-07-02 ... the vendor HAD posted). **A pipeline that grades its own
> homework cannot report its own death.**"*
>
> **CLOSED OUT 2026-08-05 -- EDICT ISSUED, DISPATCHED, ACKED.** Andrew ratified the recommendation
> VERBATIM: *"I agree with your rec, issue the edict, let's close out any necessary updates for
> canonical-schwab item and then proceed to item 5."* Seat `0.7.0_AE_CloudOps~C` was instantiated by
> him for this express purpose; briefed and acked (RAVC-2, watcher exercised).
> - **STAGE 1 GO:** set the live Name tag to **`canonical-schwab-si2`** -- the name EC2_MANIFEST
>   already carries. **Do not invent a third name: the manifest was RIGHT and the live tag was
>   WRONG, so the fix is to make reality match the record, not to change the record.** Correct the
>   false `reversible=true`; align manifest and tag.
> - **STAGE 2 HELD (IAM role / profile / SG / key rename):** delivered as a JUDGEMENT to Andrew, not
>   as work -- what risk actually remains after Stage 1, what create-new-and-migrate costs on the
>   sole live producer for two products, and a do/don't recommendation. Not authorized on this pass.
> - **TASK A (decommission `canonical-schwab-runner` if dead) ordered FIRST** -- read-only, zero
>   blast radius, removes real debt; a tag edit can wait an hour.
> - I corrected one of my own briefing defects to `~C` before they acted: I asserted "no pipeline
>   resolves this box by Name tag" and attached a verify-it instruction, i.e. handed over a
>   load-bearing assumption dressed as a footnote. It is Stage 1's whole safety argument and is now
>   an explicit exercised check on their side.


| # | Vertical | Proposed | Evidence (one line) | Conf | Shift-watch note (R2 seed) |
|---|---|---|---|---|---|
| 1 | advi-bd | **PERMANENT — RATIFIED 2026-08-05** | **`s3://opal-data-assets/schwab/08335338/`** — the 49F Black Diamond master. ADVI = "Advisor Intelligence", an Opal data product served by the Portal, scoped PER ADVISOR (49 Financial here). Layout `_ops/ bronze/ gold/ meta/ silver/`; daily scheduled ingest live. ⚠ MY ORIGINAL ROW CITED `08242234` = **`s3://opal-data-assets/schwab/08242234/`, which is MDPF "Model Portfolios"** (`_ops/ bronze/ meta/ silver/` — no `gold/`). Corrected on Andrew-direct, verified by `aws s3 ls` | HIGH | — |
| 2 | advi-cot | **PERMANENT — RATIFIED 2026-08-05** | **`s3://opal-data-assets/blackdiamond/cottonwood/`** (`bronze/ gold/ meta/ silver/`) — the BLACK DIAMOND vendor tree, NOT a Schwab account; 49F's sibling is `.../blackdiamond/49f/`. Cottonwood BD feed live (cot-bd-session-daily ENABLED); relationship-grain ruling 08-04 active | HIGH | **Interior route consolidating legacy→canonical (Andrew's own R2 exemplar)** — State watches; under the ratified grain convention this is NOT a lifecycle shift |
| 3 | advi-inf | **PERMANENT — RATIFIED 2026-08-05** ("your understanding is correct on advi-inf, no notes") | **TWO-VENDOR SOURCE, unlike the other two advisors:** `s3://opal-data-assets/orion/inflection/` + `s3://opal-data-assets/eclipse/inflection/`. There is **NO `blackdiamond/inflection/`** — `blackdiamond/` holds only `49f/` and `cottonwood/` (ground-read). INF partner serving live; MDPF_CANRTE covers its direct-silver leg | HIGH | **INF GOLD NOT MIGRATED** — gold still LIVE-writing to `s3://opal-data-inf/gold/` (2026-08-05 10:51Z) while its assets trees carry no `gold/`. Named OPAL_CONSOLIDATION fix. Plus canonical-route redesign in flight. Both interior — NOT lifecycle shifts |
| 4 | canonical-schwab | **PERMANENT - RATIFIED 2026-08-05** | THE PRODUCT-AGNOSTIC INGEST SPINE for the Schwab custodial source. Two ENABLED twice-daily pulls (`canonical-schwab-si2-08335338-daily-pull` cron(45 9,21), `...-08242234-daily-pull` cron(15 10,22)) + an event-driven start accelerator (`canonical-schwab-xref-success`, legitimate - both pulls carry real crons). **20 silver tables (08335338) / 19 (08242234), 18 IDENTICAL** - divergence is 3 tables at the edge. **CORRECTION: my original row said 'six silver tables' - that was the CONVERTER count from the runbook, reported as a table count.** | HIGH | **DUAL-IDENTITY BOX - see finding below.** 08242234 has NO `gold/` (2nd instance of the INF class, different product) |
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
