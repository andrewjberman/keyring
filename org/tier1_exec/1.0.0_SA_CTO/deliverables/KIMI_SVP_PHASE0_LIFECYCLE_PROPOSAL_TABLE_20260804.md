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

**SITTING PROGRESS: 10 of 29 ratified** (advi-bd, advi-cot, advi-inf, canonical-schwab, causality, ceo-digest, cma, correlation, data-refresh -- 2026-08-05; **etf-reports -- 2026-08-06, PERMANENT with a standing review**)

> **CADENCE IS A DECLARED PROPERTY, AND IT WAS NOWHERE MACHINE-READABLE (row 7).** I proposed cma as
> "PERMANENT with NO declared cadence" and argued the age therefore could not be a finding. **Andrew
> corrected the premise, not the value: the cadence EXISTS and it is ANNUAL** -- *"this file gets
> uploaded once a year."* That is a better answer than mine in both directions: the artifacts are
> demonstrably HEALTHY (5 and 7 months, well inside a year), AND a freshness check here is
> LEGITIMATE rather than impossible -- it simply needs a one-YEAR window. My version would have
> banned a valid control; his supplies the parameter that makes it correct.
> **The cadence lived only in his head.** Nothing in the estate declared it, which is exactly why a
> survey reading artifacts alone cannot distinguish "annual product, on time" from "frozen." This is
> the lead NEVER-rule's shape at a 365-day scale. NO CHECK IS PROPOSED HERE (standing moratorium) --
> what is recorded is the DENOMINATOR that any future reasoning must use.

> **CLASS FINDING (row 6) - EMAIL-ONLY PRODUCTS ARE STRUCTURALLY INVISIBLE TO OUR REACHABILITY
> INSTRUMENTS.** `ceo-digest` records as `served: (no data artifact)` / `frontend: (none)` /
> `reachable: unreviewed`. All three are TRUE, and all three are the signals a roster survey leans
> on. Its only consumer is a human inbox, so it produces no artifact, has no frontend, and touches
> no queryable surface -- it does not look neglected, **it looks nonexistent.** This is the exact
> DANGEROUS direction the rule bank names: *"wrong in the DANGEROUS direction on TRANSIENT,
> EVENT_CREATED and DORMANT, where it reports a healthy system as dead and PROPOSES DELETING A LIVE
> ONE."* I was one ratification from proposing DORMANT on a system that had run four hours earlier.
> **Any product whose delivery is an email, a report to a person, or any other non-artifact channel
> shares this blindness.** Worth a deliberate sweep; NOT chased from this row.
>
> **AND THE PATTERN IN MY OWN `UNDECLARED` ROWS: two examined, two wrong, in OPPOSITE directions.**
> `causality` was RETIRED where I said unknown; `ceo-digest` is PERMANENT-and-firing where I flagged
> DORMANT. Those rows were not honest uncertainty -- they were UNEXAMINED rows wearing the enum's
> word for honest uncertainty. The remaining three (`insurance`, `security-scanner`, `ticketing`)
> get ground-read BEFORE they are put in front of Andrew, not after.

> **RETIREMENT RULING ON RECORD (row 5).** `RETIRED` carries `requires: [retirement_ruling]` --
> *"a retirement with NO RULING is an outage with paperwork."* A teardown had occurred (June 2026)
> and no authorizing ruling was found. **Andrew's word at this sitting IS that ruling**, VERBATIM:
> ***"Retired completely."*** (2026-08-05, `1.0.0_SA_CTO~B` terminal, Phase-0 sitting.) The
> requirement is therefore satisfied by this record, not by an inherited one.
>
> **DENOMINATOR NOTE:** the roster remains 29 verticals; **28 are live and 1 is terminal.** RETIRED
> is a legitimate member of the ratified enum, so the row STAYS on the c3.ii matrix carrying its
> terminal value rather than being deleted from it -- deleting it would destroy the record that a
> decommission happened, which is the same class of loss as an un-ruled retirement. *(Stated as my
> reading of "completely" = the retirement is total, NOT that the row is erased. Cheap to correct
> if he meant otherwise.)*. **CANONICAL MEDALLION FORM ratified same sitting:** bronze (raw vendor) -> silver (parquet queryable) -> gold (processed analytics) all under `s3://opal-data-assets/{vendor}/{firm}/`; serving = `s3://opal-data-portal-v2/platinum/`. TARGET, not current state -- deltas measured in the record below. Records:
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
>
> **NAMING CONFLICT RESOLVED 2026-08-05 -- and HOW it resolved is the part to preserve.**
> `0.7.0_AE_CloudOps~C` stopped Stage 1 on finding a PRIOR Andrew-direct naming law
> (`data/assets/docs/SCHWAB_BOX_ARCHETYPE.md:6`, 2026-07-17): *"this device is the 'Schwab Box.'
> Drop 'quartz' / 'SI2 spike' entirely... A name that implies 'throwaway' for load-bearing infra is
> a real defect."* The edict's `canonical-schwab-si2` still contains **SI2**. They refused to
> adjudicate between two Andrew-directs -- correct, and the class he ruled against 2026-08-04.
> Surfaced with both candidates + the 07-17 text quoted. **RULED VERBATIM: *"canonical-schwab-si2 is
> fine, let's get that sorted out and proceed to the next."***
> >> **A sovereign ruling made WITHOUT sight of a conflicting prior is an OVERSIGHT TO SURFACE; one
> made WITH sight of it is a DECISION TO EXECUTE.** When he first said *"I agree with your rec"* the
> 07-17 law was not in front of him -- my recommendation never mentioned it. The second time it was.
> `~C` converted the first into the second at the cost of one message.
>
> **TASK A CLOSED @772ff82f5, re-derived by this seat:** instance terminated - rule
> `ResourceNotFoundException` - **484 objects PRESERVED** under `canonical/schwab/` - dry-fit pinned
> key intact (228,605 B). The box had **NEVER RUN ONCE**.
> **THE GENERALISING FINDING: A TARGETED DESTROY ARMS A RESURRECTION.** After 11 verified-absent
> resources, the `.tf` still DECLARED them -- `Plan: 11 to add`. The next apply by any agent, for any
> unrelated change, would have recreated a terminated box with no ruling and nobody looking.
> **terraform destroy removes INFRASTRUCTURE; only deleting the DECLARATION removes the INTENT.**
> Applies to EVERY `-target` destroy in this estate; invisible to "is it gone from AWS?". Sibling:
> `apply -target` WITHOUT `-destroy` printed *"Apply complete!"* at rc=0 having destroyed nothing.
>
> **THREE DEFECTS OF MINE IN ONE BRIEF, all caught by `~C` before they cost anything:** (1) "no rule
> targets the stopped box" -- FALSE, bound via `InstanceId` inside the Input JSON payload, invisible
> to a target-ARN scan *(and I had put that rule in a `/draw` Andrew ratified, as an accelerator on
> the LIVE box -- corrected with him directly)*; (2) candidate S3 prefixes in the WRONG BUCKET; (3) a
> "Terraform only" non-negotiable applied to a box TF does not lifecycle-manage (`managed_by`:
> *"Terraform (IAM only -- the instance is a persistent Andrew-direct box, not TF
> lifecycle-managed)"*) -- narrowed to sanction `aws ec2` tag mutation, since there is no TF state to
> drift from and a `terraform import` would have put the sole live 49F ingest one careless apply from
> replacement. **The common shape is not sloppy facts -- it is CONFIDENT CONSTRAINTS WHOSE
> PRECONDITIONS I NEVER GROUNDED, stated in the register of a rule rather than a claim, which is the
> register that discourages checking.**



| # | Vertical | Proposed | Evidence (one line) | Conf | Shift-watch note (R2 seed) |
|---|---|---|---|---|---|
| 1 | advi-bd | **PERMANENT — RATIFIED 2026-08-05** | **`s3://opal-data-assets/schwab/08335338/`** — the 49F Black Diamond master. ADVI = "Advisor Intelligence", an Opal data product served by the Portal, scoped PER ADVISOR (49 Financial here). Layout `_ops/ bronze/ gold/ meta/ silver/`; daily scheduled ingest live. ⚠ MY ORIGINAL ROW CITED `08242234` = **`s3://opal-data-assets/schwab/08242234/`, which is MDPF "Model Portfolios"** (`_ops/ bronze/ meta/ silver/` — no `gold/`). Corrected on Andrew-direct, verified by `aws s3 ls` | HIGH | — |
| 2 | advi-cot | **PERMANENT — RATIFIED 2026-08-05** | **`s3://opal-data-assets/blackdiamond/cottonwood/`** (`bronze/ gold/ meta/ silver/`) — the BLACK DIAMOND vendor tree, NOT a Schwab account; 49F's sibling is `.../blackdiamond/49f/`. Cottonwood BD feed live (cot-bd-session-daily ENABLED); relationship-grain ruling 08-04 active | HIGH | **Interior route consolidating legacy→canonical (Andrew's own R2 exemplar)** — State watches; under the ratified grain convention this is NOT a lifecycle shift |
| 3 | advi-inf | **PERMANENT — RATIFIED 2026-08-05** ("your understanding is correct on advi-inf, no notes") | **TWO-VENDOR SOURCE, unlike the other two advisors:** `s3://opal-data-assets/orion/inflection/` + `s3://opal-data-assets/eclipse/inflection/`. There is **NO `blackdiamond/inflection/`** — `blackdiamond/` holds only `49f/` and `cottonwood/` (ground-read). INF partner serving live; MDPF_CANRTE covers its direct-silver leg | HIGH | **INF GOLD NOT MIGRATED** — gold still LIVE-writing to `s3://opal-data-inf/gold/` (2026-08-05 10:51Z) while its assets trees carry no `gold/`. Named OPAL_CONSOLIDATION fix. Plus canonical-route redesign in flight. Both interior — NOT lifecycle shifts |
| 4 | canonical-schwab | **PERMANENT - RATIFIED 2026-08-05** | THE PRODUCT-AGNOSTIC INGEST SPINE for the Schwab custodial source. Two ENABLED twice-daily pulls (`canonical-schwab-si2-08335338-daily-pull` cron(45 9,21), `...-08242234-daily-pull` cron(15 10,22)) + an event-driven start accelerator (`canonical-schwab-xref-success`, legitimate - both pulls carry real crons). **20 silver tables (08335338) / 19 (08242234), 18 IDENTICAL** - divergence is 3 tables at the edge. **CORRECTION: my original row said 'six silver tables' - that was the CONVERTER count from the runbook, reported as a table count.** | HIGH | **DUAL-IDENTITY BOX - see finding below.** 08242234 has NO `gold/` (2nd instance of the INF class, different product) |
| 5 | causality | **RETIRED - RATIFIED 2026-08-05** (Andrew VERBATIM: *"Retired completely."*) | **APPLIED PLANE IS EMPTY, measured:** 0 live Lambdas, 0 DynamoDB tables (was causality-generations + causality-saved-analyses), 0 refs in portal/src (comp-grep 405 of 405 files - complete scope, cross-checked `find portal/src -type f` = 405), and `causality-endpoints.ts` DOES NOT EXIST though the estate model cites it. Teardown on the record: `0.5.0_AE_OpalETL` 2026-06-11 + 2026-06-16; `safe-destroy.sh:10` exists partly because of it. **MY ORIGINAL ROW CLAIMED 'no evidence either way' - the evidence was abundant, I had simply never looked.** | HIGH | **ONTOLOGY LAG:** `comp-estate causality` still returns 5 chains with producers/API-GW/frontend prose, all flagged `producers-dead-applied-plane-20260730`. The model outlived the system by ~6 weeks |
| 6 | ceo-digest | **PERMANENT - RATIFIED 2026-08-05** | **IT RAN THIS MORNING.** `astn-wsjft-3am-run` schedule ENABLED; EC2 `astn-wsjft-scraper` LaunchTime 2026-08-05T07:00:35Z = 3:00 AM ET today, stopped after (healthy transient signature). Chain `ceo-daily-wsjft-digest`: 3am-ET one-shot, Bright Data pull + LLM cited-bullet summary, **SES email to Austin**. **MY ORIGINAL ROW PROPOSED IT AS A DORMANT CANDIDATE ON 'no schedule/consumer evidence at hand' - it had fired 4 hours earlier.** | HIGH | **HUMAN-INBOX CONSUMER = INVISIBLE TO EVERY ARTIFACT-BASED INSTRUMENT** (no data artifact, no frontend, no queryable surface). See class note below |
| 7 | cma | **PERMANENT - RATIFIED 2026-08-05**, **CADENCE = ANNUAL** (Andrew VERBATIM: *"this file gets uploaded once a year"*) | Chain `yang-cma` / `sys-yang-analytics-engine`, motif generative-publish. Producers `yang-generate-cma` (cma_excel branch) + `data/yang_pkl/scripts`. SERVED, verified LIVE: `json/capital-markets/assumptions.json` 4,146 B LastMod **2026-03-11**; `views.json` 5,992 B LastMod **2026-01-09**. Frontend REAL + mounted: `portal/src/api/portal-proxy.ts:1363 getCMAAssumptions()` (views at :1399), CVO `mounted-reachable` | HIGH (was MED - I had rated it on a FAMILY NAME, not on this chain's evidence) | **5- and 7-month-old artifacts are HEALTHY against an annual cadence.** A daily/weekly freshness check here would false-alarm forever with a real-looking number |
| 8 | correlation | **PERMANENT - RATIFIED 2026-08-05** | Chain `yang-correlation` / `sys-yang-analytics-engine`, producer `yang-generate-correlation` (ProcessDataPKLOnly). SERVED verified LIVE: `json/correlations/correlation_data.json` 152,639 B **LastMod 2026-08-05 07:30:29Z (today)** - the census claimed 2026-06-15, **stale by 7 weeks**. Frontend real + mounted: `portal-proxy.ts:1633 getCorrelationData()`, exported :2168 | HIGH (was MED - rated off a family name) | ACTIVELY PRODUCING - unlike `cma`, an old artifact here WOULD be a finding. Two chains I had lumped as one MED family read OPPOSITE on cadence |
| 9 | data-refresh | **PERMANENT - RATIFIED 2026-08-05** | Chain `PPI-10-opal-data-refresh-api` / `sys-partner-serving-platform`, motif edge-route. Lambda `opal-data-refresh-api` LIVE (python3.11/256MB, **LastMod 2026-08-03**). Frontend MOUNTED: `App.tsx:30,32` lazy -> rendered `:466` (DataRefresh) + `:434` (SecurityScanner). Census said `reachable: unreviewed`; **resolved to mounted by this check**. Dev-only (JWT userType=Dev) - internal operator tool | HIGH | **COUPLES TO ROW 25:** the SAME Lambda serves `/security-scanner/*` and the SAME App.tsx mounts both pages - row 25's 'LEGACY candidate' note is likely inverted. **ALSO: this Lambda is the named specimen in CLAUDE.md Rule 22a** - it executes 5 real DynamoDB ops and comp-iam reports 'dynamodb' ZERO times |
| 10 | etf-reports | **PERMANENT — RATIFIED 2026-08-06**, **WITH A STANDING REVIEW** (Andrew VERBATIM: *"This is Permanent, but we need to make sure that all of these are properly grouped together, that nothing is redundant, that what is actually supposed to be canonical here is, I'd say essentially that it is subject for review."*) | **NINE live schedules, all ENABLED**, spanning all three advisor firms — the row's original single-line evidence understated this by 8. Chain (UTC): `wsd-49f-partner-held-etf-daily` 03:30 **TUE-SAT** · `cot-etf-ownership-daily` 10:30 · `bd-49f-etf-ownership-daily` 10:45 · `inf-etf-ownership-daily` 15:00 · `etfs-canon-fanin` 15:45 · `etf-ownership-dashboard` 16:00 · `etfs-netassets-daily` 22:00 · `opal-assets-silver-etf` 23:30 · `etfs-reports-monthly-run` cron(0 10 1 * ? *) America/New_York -> Sep-1 14:00Z -> `etfs-reports-orchestrator`. Rule->Lambda mapping is **1:1, zero duplicate targets**. Original cited evidence VERIFIED correct | HIGH | **REVIEW OWNED, scope below the table.** ETFS CANON question still open — and a Lambda named `etfs-canon-fanin` fires DAILY while "which location is canonical" is an unresolved P0 |
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

---

## ROW 10 STANDING REVIEW — ETFS grouping / redundancy / canonicality

**Opened 2026-08-06 on Andrew-direct at the CTO~B terminal, VERBATIM:**
> *"This is Permanent, but we need to make sure that all of these are properly grouped together,
> that nothing is redundant, that what is actually supposed to be canonical here is, I'd say
> essentially that it is subject for review."*

Ratification of PERMANENT is NOT contingent on this review. The review is a separate owned item.

### What the ground-read already settled

**No literal redundancy.** All nine schedules map 1:1 to distinct Lambdas; no two fire the same
target. Whatever duplication exists is SEMANTIC (two jobs computing the same thing under different
names), not mechanical, and names cannot settle it.

**The core group is coherently ordered.** Three per-firm ownership producers complete
(cot 10:30 / bd 10:45 / inf 15:00) before the fan-in (15:45), which completes before the dashboard
(16:00). That IS a proper group and the sequence is sound.

### The four open questions, and why each is real

**1. THE CHAIN IS TIME-ORDERED, NOT DEPENDENCY-ENFORCED.** `etfs-canon-fanin` fires 45 minutes after
`inf-etf-ownership-daily` on a clock, not on its completion. If INF runs long or fails, the fan-in
fires anyway and the dashboard publishes 15 minutes later. **The fan-in cannot distinguish "INF wrote
nothing today" from "INF failed."** That is the presence-vs-health class (`degraded_sources: []`)
sitting in a live partner-facing chain. *Note the CLAUDE.md ad-hoc/schedule rule cuts the OTHER way
here — these correctly have real schedules; the gap is that nothing verifies upstream completion.
The remedy is a precondition check, NOT converting them to event-only triggers, which would
reintroduce the freeze-silently defect that rule exists to prevent.*

**2. TWO 49F ETF JOBS ON DIFFERENT CALENDARS.** `bd-49f-etf-ownership-daily` runs 7 days/week;
`wsd-49f-partner-held-etf-daily` runs **TUE-SAT only** (a T-1 weekday pattern). Same firm, both ETF.
Either they are different datasets — in which case the naming makes them look redundant when they
are not — or they overlap, and one calendar is wrong. **Not resolvable from schedules; needs the
two Lambdas' outputs compared.**

**3. TWO JOBS RUN AFTER THE DASHBOARD PUBLISHES.** `etfs-netassets-daily` (22:00) and
`opal-assets-silver-etf` (23:30) land 6 and 7.5 hours AFTER `etf-ownership-dashboard` (16:00), so
neither is in the dashboard a reader sees that day. Either they feed the NEXT day's run — legitimate,
but it makes the dashboard T-1 on those inputs and nothing says so — or they belong to a different
vertical that merely shares the `etf` name. **This is the grouping question Andrew asked, in its
sharpest form.**

**4. THE CANONICALITY QUESTION IS LIVE WHILE A JOB NAMED `canon` RUNS DAILY.** The open ETFS CANON
question is *which DynamoDB table / S3 location is canonical for ETFS* (Andrew P0, gating the
`ETFS_AVGCAP` `partial`-flag defect and the INF gold-floor figure as ONE cluster). Meanwhile
`etfs-canon-fanin` has been firing every day at 15:45. **Either it has already settled canon de
facto — which is the "it is deployed and it works" answer CLAUDE.md 17a explicitly rejects as an
architecture — or it is fanning in to a location that is not the canonical one.** Both readings are
findings; they are not the same finding, and no schedule read can tell them apart.

### Method note

Everything above is grounded on LIVE schedule + target state. **Questions 2, 3 and 4 are
deliberately left as QUESTIONS**: each requires reading what these Lambdas actually WRITE, which I
have not done. Naming a suspicion as a finding would be the ungrounded-causal-claim class
(CLAUDE.md 22) — the schedules are evidence of WHEN, never of WHAT.

**Instrument gap found while grounding this row, and it is wider than ETFS:** `aws events
list-rules` **cannot see EventBridge Scheduler schedules at all** — a different API. **16 live
schedules** sit there, including `etfs-reports-monthly-run` (this row's own cited evidence),
`astn-wsjft-3am-run` (row 6's evidence) and `estate-report-0900et`. A `list-rules`-based census of
"what is scheduled in this estate" silently omits all 16 and reads as complete. I nearly filed the
month-end email as MISSING on a `ResourceNotFoundException` before checking the second API.
**Separately: `--query 'length(Rules)'` reported 100; the token-walked truth is 139** — the
documented paginated-count trap, which genuinely hid `opal-assets-silver-etf-sweep-daily` from the
first read of this very row.
