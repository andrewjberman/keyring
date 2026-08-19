# W-24 — THE 29-VERTICAL PLACEMENT PASS (Subject x Function grid)

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Date:** 2026-08-19
**Mandate:** the 2026-08-12 walk-list item W-24 (`org/tier1_exec/4.0.0_SA_CRO/logs/2026-08-12/post_reboot_ontology_rulings_fanout_and_cto_brief.md` §E), queued at this seat through three successive handoffs, terminal carry in the 08-19 wind-down log. Grid authority: `org/modules/graph/NFRA_ONTOLOGY_C2C3_CANONICAL.yaml` `c4_subject_function_grid` (RATIFIED Andrew-direct 2026-08-12); term entries `Subject`/`Function` in `infra/system/ontology/SYSTEM_DEFINITIONS.yaml` v3.0.
**What this settles:** W-02 (`build` fifth Function value — EMPIRICAL settlement, ruling stays Andrew's) · W-26 (ops-internal adjudication) · W-27 (model-portfolios ROW x ROW) · W-28 (portfolio-management suspect flag). Plus four NEW findings the structural read could not see.

---

## 0. DENOMINATORS AND INSTRUMENT VINTAGE (read first)

- **Roster placed: the RATIFIED 28** — the 2026-08-07 Andrew merge of `model-portfolios` INTO `mdpf` binds (`org/tier1_exec/4.0.0_SA_CRO/deliverables/C3II_COMPREHENSIVE_SEMANTIC_COVERAGE_SCAN_20260811.md` §5: ratified roster = 28). The canonical YAML, the resolver, and `comp-estate --matrix` still MATERIALIZE 29 (W-15 propagation open, not this pass's act). This pass places 29 materialized names into **28 placements** — the merged pair appears as ONE row carrying both name-halves.
- **Ground set: 138 chains** per `org/modules/graph/estate-coverage-resolver.json` (FILE, vintage `last_review: 2026-07-30` — 20 days old, past the declared 14-day staleness bar). C3.ii membership is DECLARED (legislated), so the membership itself does not decay the way a measurement does; chain `status` labels (in-scope / explicit-out / unreviewed) and descriptions are census-vintage and are quoted as such. Per CLAUDE.md Rule 21, comp-estate topology claims are priors under test; every load-bearing placement below cites the chain-level record, not a segment summary.
- **Status mix across the 138:** in-scope 98 · explicit-out 26 · unreviewed 14 (script-counted from the resolver FILE this session).
- **Segment cross-check base:** the canonical's `measured_2026_08_12` (38 assignment slots / 29 distinct verticals / 8 multi-segment: 6 row x column, 2 row x row) — **re-derived this session from the five `verticals_served` lists: 9+13+4+6+6 = 38, 29 distinct, 8 multi. Confirmed.**

## 0b. PLACEMENT GRAIN LAW (stated so the table is falsifiable)

1. **Subject is SINGLE-VALUED per vertical** (MECE rows — the overlap law's own rule: a two-row vertical has an unresolved subject).
2. **Function is a SPAN** (coarse by design, Andrew-direct verbatim in the `Function` registry entry; a vertical's chains legitimately play several roles).
3. **PROPOSED ATTRIBUTION RULE — terminal store-writes do not confer `serving`.** Every pipeline chain ends in a store; if that conferred `serving`, every vertical would span it and the column would stop discriminating. `serving` is attributed only where the vertical carries a REQUEST-PATH or DELIVERY surface (API, proxy, edge route, auth, email delivery). Applied uniformly below; flagged as PROPOSED, not ratified.
4. **Subject follows the DECLARED vertical grain, not the consumption graph.** A shared analytics engine's own verticals (cma, correlation, ...) stay `market` even though client products consume them; chains DECLARED into a product's vertical take the product's subject. This is what keeps the mdpf ruling (§3) from dragging the whole yang engine into `client`.

---

## 1. THE PLACEMENT TABLE (28 rows, ratified roster)

Chains column = n (status mix at resolver vintage). Segment check = the grid position the five `c4_segments` `verticals_served` lists imply, and whether this pass agrees.

| # | Vertical | Subject | Function span | Chains | Evidence anchor | Segment cross-check |
|---|---|---|---|---|---|---|
| 1 | advi-bd | client | acquisition, analysis, serving | 19 (15 in / 3 out / 1 unrev) | BD medallion ingest→gold (acq); gold analytics A_00..D_00 class (ana); `bd-client-detail-api`, `bd-portal-publisher`, `bd-time-machine` (serv) | partner-data ROW(client) — AGREE |
| 2 | advi-inf | client | acquisition, analysis, serving | 14 | INF medallion bronze→silver quorum→gold (acq, ana); publishers + PPI-08/09 shared-advisor routers (serv) | partner-data + access-delivery = row x col — AGREE |
| 3 | advi-cot | client | acquisition | 1 | `cot-pipeline` (Cottonwood medallion) | partner-data ROW — AGREE |
| 4 | canonical-schwab | client | acquisition | 1 | Schwab CRS/RPS canonical feed | partner-data ROW — AGREE |
| 5 | smartx | client | acquisition, serving | 3 | `smartx-rest-daily-ingest` (acq); `smartx-ec2-csv-exporter` census family api-serve (serv); monthly benchmarks (ana leg, minor) | partner-data ROW — AGREE |
| 6 | partners | client | serving | 2 | `PPI-02-opal-portal-authorizer`, `PPI-04-opal-partners-data` — identity + access is `serving`'s own definition | access-delivery COL — subject assigned here: client |
| 7 | portal-infra | client | serving | 6 | Auth edge validators/handlers, public-data-router, cache-control, time-machine, session-analytics — the spine every CLIENT request crosses | access-delivery COL — subject assigned here: client |
| 8 | **mdpf (merged, incl. model-portfolios)** | **client** | acquisition, analysis, serving | 10 (2 mdpf + 8 model-portfolios; 6 in / 4 out) | §3 (W-27). `mdpf-global-view` per-partner model-AUA aggregation (acq/ana); `PPI-05-opal-portal-data-proxy` (serv); yang model-construction chains (ana) | WAS the row x row defect — RESOLVED to client, §3 |
| 9 | ticketing | client | serving, experience | 1 | `ticket-center-api` — portal ticket intake/track (user-operated product surface + its API) | interactive-products COL — subject assigned here: client |
| 10 | etf-reports | client | acquisition, analysis, serving | 1 | Per-firm ETF-ownership dailies → canon fanin → netassets → month-end SES reports + dashboard (partner-rebate basis = partner-level data) | partner-data ROW — AGREE |
| 11 | trade-submission | **client** | serving, experience | 12 (7 in / 2 out / 3 unrev) | §5 F-1. TS-1..TS-7 ticket intake/auth/workflow on client accounts; pm-tool bridge chains (`portfolio-excel-generator` export-and-submit) | segments imply ROW(market) x COL(experience) — **DISAGREE: subject flip finding, §5 F-1** |
| 12 | portfolio-management | **client** | serving, experience | 9 (8 in / 1 out) | §4 (W-28). Eight pm-tool product chains (autosave, loader, snapshot, upload-urls, export, funds-list, pickle-parser); the estate flag came from ONE explicit-out observation chain | WAS the semantic-suspect COL x ROW — RESOLVED to client, §4 |
| 13 | market-overview | market | analysis, serving, experience | 11 (8 in / 3 unrev) | MA-01..07 analytics + regime classifier (ana); tiered publishes (serv); interactive version panel (exp). ⚠ carries 2 pm-tool chains — §5 F-4 | market-intelligence + interactive-products = row x col — AGREE |
| 14 | news | market | acquisition, analysis, serving | 13 (10 in / 2 out / 1 unrev) | Ingestion + scrapes (acq); FinBERT, keyword GPT, layer3 curation (ana); trending publisher + `sentiment_query_api` (serv) | market-intelligence ROW — AGREE |
| 15 | macroeconomics | market | acquisition, analysis, serving | 9 (6 in / 2 unrev / 1 out) | FRED ingests (acq); yang macro + generated artifacts (ana); exec-summary/deck/agenda delivery (serv) | market-intelligence ROW — AGREE |
| 16 | cma | market | analysis | 1 | `yang-cma` | market-intelligence ROW — AGREE |
| 17 | correlation | market | analysis | 1 | `yang-correlation` | market-intelligence ROW — AGREE |
| 18 | factor-tilts | market | analysis | 1 | `yang-factor-tilts` | market-intelligence ROW — AGREE |
| 19 | positioning | market | analysis | 1 | `yang-positioning-attribution-allocation` (attribution content lives here per the 07-30 retirement of `attribution`) | market-intelligence ROW — AGREE |
| 20 | valuation | market | analysis | 1 | `yang-valuation-risk-premium` | market-intelligence ROW — AGREE |
| 21 | causality | market | analysis | 5 (2 out / 3 unrev) | Generative market analysis; **lifecycle flag carried: sys-causality-engine ADJUDICATED RETIREMENT-PENDING 2026-07-30** — placement records where it SITS, not that it is well | market-intelligence ROW — AGREE |
| 22 | ceo-digest | market | acquisition, analysis, serving | 1 | Bright Data pull (acq) + LLM cited-bullet summary (ana) + SES delivery (serv) | market-intelligence ROW — AGREE |
| 23 | data-refresh | market | serving | 1 | `PPI-10` — refresh/trigger surface over the Yang analytics Step Functions + factor-scanner backend; the world it operates on is market-analytics machinery. Thin call; alternative (client, as product-operations) named and not chosen | access-delivery COL — subject assigned here: market |
| 24 | security-scanner | **market** (split pending) | analysis, serving | 2 (1 in / 1 out) | §5 F-2. The IN-SCOPE chain is an EQUITIES FACTOR scanner ("NOT a security/ops scanner" — its own description) serving the portal SecurityScanner page = market. The explicit-out `ops-anomaly-scanners` (IAM/cost/security posture) = estate. Name-collision bucket | estate-infrastructure ROW — **DISAGREE for the live chain: subject flip finding, §5 F-2** |
| 25 | insurance | **market (boundary-flagged)** | analysis | 2 (both out) | §5 F-3. Insurance case-find / prospecting (dualbiz) — external non-client firms. Neither world holds it cleanly; `market` ("the environment we operate in") is the nearest honest row; alternative reading (client = "the business we run", growth arm) named for the ruling | estate-infrastructure ROW — DISAGREE (subject is external firms, not our machinery), §5 F-3 |
| 26 | graph-platform | estate | acquisition, serving, experience | 4 | Derive runners ingest the estate's own state into Nessie/Iceberg (acq — of estate data); Nessie catalog service (serv); Kuzu local build/query surface (exp — agent-operated) | estate-infrastructure ROW — AGREE |
| 27 | m365-mcp | estate | serving | 1 | Delegated-token access layer fronting M365 for agents: identity + access + audit | estate-infrastructure ROW — AGREE |
| 28 | **ops-internal** | **— DISSOLVE (rec)** | — | 5 (ALL explicit-out) | §2 (W-26). Five chains, THREE subjects, zero in-scope members — a residue bucket wearing a vertical's name | WAS the ROW x ROW x COL defect — RESOLVED by decomposition, §2 |

**Grid after placement (3 x 4, counts of verticals whose span touches the cell; subject single-valued):**

| | acquisition | analysis | serving | experience | row total (verticals) |
|---|---|---|---|---|---|
| **client** | 7 | 4 | 10 | 3 | **12** |
| **market** | 3 | 12 | 6 | 1 | **13** |
| **estate** | 1 | 0 | 2 | 1 | **2** |

(12 + 13 + 2 = 27 placed + ops-internal dissolving = 28. Cell counts are span-touches and deliberately do NOT sum to 28 — the non-summable rule one level down; the ROW total is the MECE denominator.)

---

## 2. W-26 — ops-internal: DECOMPOSITION CONFIRMED, DISSOLUTION RECOMMENDED

The 08-12 hypothesis ("behaves as a catch-all; likely needs decomposition rather than a subject ruling") is **confirmed at chain grain**. The five chains (ALL `explicit-out` at resolver vintage):

| Chain | Actual subject | Disposition proposal |
|---|---|---|
| `PPI-13-schwab-anonymizer` | client (PII tooling over Schwab RPS/CRS files) | Re-home → `canonical-schwab` (it processes exactly that feed's files) |
| `ops-ec2-governance-lambdas` | estate (auto-shutdown-enforcer KILLS idle instances; runtime-monitor flags) | Re-home → estate row (see §6 note: this is the roster's ONE actuation-shaped chain) |
| `semantic-pipeline-parallel-set` | market (abandoned parallel news pipeline, "appears superseded") | Re-home → `news` WITH a retirement adjudication (it is a superseded parallel path — the standing no-shadow-channels class; already explicit-out) |
| `test-yfinance-simple` / `yfinance-aapl-test` | none (test scaffolds, empty descriptions) | NOT vertical members — route to residue/retirement; a test scaffold does not earn C3.ii membership |

`ops-internal` fails the estate row's own residue-bucket test: its contents are NOT statable positively — they are statable only as "things nobody else claimed." Dissolving it clears the roster's only ROW x ROW x COL defect **and** removes a catch-all that would otherwise keep attracting unplaceable chains. **Dissolution + re-homes are NAMING ACTS — Andrew/CVO legislation; this pass proposes, it does not execute.**

## 3. W-27 — model-portfolios ROW x ROW: RESOLVED TO `client`, AND NOT MOOT

The 08-07 merge did not make the adjudication moot — it **relocated** the ambiguity onto the merged `mdpf` vertical (client half: per-partner model-AUA aggregation, portal proxy; market half: yang model-construction chains). The resolution is grounded in **Andrew's own ratified Subject definition, verbatim** (canonical `c4_subject_function_grid.subject.values.client`): *"advisor-level data and systems, e.g. the advisor intelligence and **model portfolio portal products and what they consume**."* The ratified text ALREADY names this product AND its consumption as `client`. The market reading came from C3.i SYSTEM membership (sys-yang-analytics-engine / sys-market-intelligence-engine span the vertical) leaking into the vertical's subject — the exact segment-vs-grid confusion the grid was ratified to remove. Per placement rule 4, the SHARED analytics verticals (cma, correlation, factor-tilts, positioning, valuation) stay `market`; only the chains DECLARED into the product vertical take `client`.

**Rec: merged mdpf subject = client.** The market-intelligence segment may KEEP listing it for recall (a segment is a routing index, deliberately overlapping); the GRID classification is client. Executes with W-15 propagation, not before.

## 4. W-28 — portfolio-management suspect flag: RESOLVED TO `client`; the flag was one chain's shadow

Chain-grain read: **8 of 9 chains are the client-facing PM product backend** (in-scope). The ENTIRE `subject:estate` signal came from `ops-infrastructure-monitors` (explicit-out; daily estate snapshot + health monitor) — an observation chain that the estate-infrastructure segment's own note already explains: *"observation chains route here even when the observed thing lives in another segment — the observed belongs to its segment, the observing belongs here."* That note is a rule about SEGMENT routing; it was never a subject claim about the PM product.

**Rec: portfolio-management subject = client, span {serving, experience}. `ops-infrastructure-monitors` re-homes to the estate row.** With ops-internal dissolving (§2), the estate row has no ops-observability vertical to receive it or `ops-ec2-governance-lambdas`/`ops-anomaly-scanners` — **candidate naming act for the legislature: an estate ops-observability vertical** (or a ruled fold into graph-platform). All affected chains are explicit-out, so nothing live is misplaced while that ruling waits.

## 5. NEW FINDINGS (the structural read could not see any of these)

- **F-1 — trade-submission subject flips to `client`.** The 08-12 measured grid implicitly carried it at `market` (its only ROW membership is market-intelligence, via causality/market engine spans), and because its other segment is a COLUMN, no row x row defect fired. Semantically: trade tickets, order intake, submission tracking on client accounts — advisor action on the business we run. The market row was engine-span leakage, same mechanism as §3. **Third subject correction of the pass.**
- **F-2 — security-scanner is a name-collision bucket.** Its live chain is an EQUITIES FACTOR scanner (market product surface, says so in its own description); its explicit-out chain is estate security posture. One name, two worlds — the "one word, two things" class. **Rec: split** — live chain re-homes/places as market; `ops-anomaly-scanners` joins the estate ops-observability question (§4). Naming act; proposed, not executed.
- **F-3 — insurance exposes a genuine boundary gap.** Prospect/business-development data (external firms we might do business with) sits cleanly in NEITHER `client` (not yet partners) NOR `market` (not financial-environment data) NOR `estate`. Placed at `market` as nearest-honest with the alternative reading named. **This is a Subject-axis boundary note for Andrew, not a new-value proposal** — 2 explicit-out chains do not earn an axis value.
- **F-4 — market-overview carries two pm-tool chains** (`portfolio-version-get`, `portfolio-versions-list` — portfolio version history). Declared membership is a naming act, so this is flagged-not-chased: review at W-15 propagation whether they belong in portfolio-management.
- **(Standing, not new)** W-15: the ratified 28 has still not propagated to the canonical YAML / resolver / matrix; this pass had to carry the 29→28 reconciliation in-band. The canonical grid block's own `measured_2026_08_12` and `non_summable_rule` cite "29 distinct verticals" and will need the same touch.

## 6. W-02 — `build` AS A FIFTH FUNCTION VALUE: EMPIRICAL RESULT = ZERO MEMBERS. REC: COLLAPSE TO THE CLEAN 3 x 4.

**The empirical settlement the canonical asked for:** across all 138 chains in the ground set, **zero chains are deploy/CI machinery**. Every estate-row chain placed cleanly in the four ratified values — graph derive/ingest = acquisition, Nessie/M365 gateways = serving, Kuzu/agent-operated surfaces = experience — exactly the collapse Andrew hypothesized when he left the question open (*"'the tools I use to build the estate' is already fully described by subject:estate spanning the four functions"*).

**The one near-member, examined so the zero is honest:** `ops-ec2-governance-lambdas` (explicit-out) ACTS on the estate (kills idle instances) rather than describing it. But its shape is OPERATIONS-ACTUATION, not deploy/CI — it does not match `build`'s own definition ("deploy/CI machinery") — and 1 explicit-out chain of 138 (0.7%) does not earn an axis value under Rule 24 discipline.

**The domain caveat, stated so the collapse is not over-read (Rule 22 — name the instrument's domain):** the ground set is the lambda-census chain roster. The estate's ACTUAL deploy/CI machinery — Terraform + `.tools/safe-apply.sh`, `.tools/safe-commit.sh` + gates, `infra/aws/lambda/ci/` tooling, provisioning scripts — is **not in the C2/C3 chain ground set at all**, so part of the zero is by construction. Two things keep the collapse recommendation sound anyway: (a) C4 classifies chain-carrying verticals, and in THAT population `build` is empty — the grid needs no empty column; (b) even in a hypothetically expanded ground set, the agent/human-operated deploy tools land in `experience` ("portal tools, agents, CLIs" — verbatim) under `subject:estate`, and the estate BY STANDING LAW has no autonomous deploy machinery for a `build` column to hold (every apply is gated and operator-driven). If Andrew ever wants deploy tooling COVERED by C4, that is a ground-set expansion question, not a fifth Function value.

**REC to Andrew (the W-02 card): collapse `build`; ratify the 3 x 4 grid.** Edits on ratification: strike the provisional block at canonical `c4_subject_function_grid.function.values.build`; strike the provisional sentence in the `Function` registry entry (SYSTEM_DEFINITIONS v3.0). Sequence WITH the W-15 propagation touch so the canonical is opened once.

---

## 7. ROUTING

- **→ Andrew (via /open-calls at this seat, + relayed to CTO/MSTR for terminal carry):** the W-02 collapse rec (§6) — the ruling that was explicitly held for this pass — plus ratification of the three resolutions (§2 dissolve, §3 client, §4 client) and the F-1/F-2 subject corrections. F-3 is a boundary NOTE, no decision forced.
- **→ CVO (legislature mechanics):** on Andrew's words, the row adjudications + re-homes are CVO-verified naming-act executions (C3.ii invariant: legislation admits). Nothing in this pass edits the canonical YAML or the resolver.
- **→ CTO:** sequencing — the canonical edits (build strike + measured-block refresh) ride the W-15 propagation touch; W-17 (the c3-walk-agenda first-match enum hazard) still lands before any enum insertion.
- **Compiler tools this pass:** comp-find (x3, denominators quoted in-line), resolver FILE read via python (138-chain census, status mix counted), canonical YAML + SYSTEM_DEFINITIONS read direct, segment cross-check re-derived from the five `verticals_served` lists (38/29/8 confirmed against `measured_2026_08_12`).
