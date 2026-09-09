# INVESTOR REPORTING & DATA UNIFICATION — STEP-1 BRIEF (L1) — the D14 directive brief

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Recon ID:** RCN-0008 — registered in RECON_REGISTER.md
**Mode:** `/brief-create` DEFAULT (NEW). No Investor Reporting project or directive row exists. See §0 for how the
in-flight siblings were handled.
**Commissioned:** Andrew-direct 2026-09-09 ~17:1xZ + ~17:2xZ at this terminal, VERBATIM in
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260909_171xZ_INVESTOR_REPORTING_BRIEF_CREATE_WRAPS_D1_D2_D3_ESTABLISHES_D14.md`:
*"We are about to sort out the biggest project on this box. I want you to /brief-create from this document"* and
*"...wraps a lot of work we've been doing on D1 D2 D3 as well as establishes a dedicated D14, "Investor Reporting", as
this product needs to be its own segment."*
**Source:** Andrew's proposal `Opal_Capital_Investor_Reporting_Unification_Proposal_Clean.docx` (80,251 B, sha256
`db4168a6…f0e8`), cited below as **§NN** = the proposal's own numbered sections 01–17 + Appendix A. Citable text:
`docs/briefs/sources/INVESTOR_REPORTING_UNIFICATION_PROPOSAL_20260909_extracted.txt`.
**Consumer:** `1.0.0_SA_CTO`, `/endpoint --forward` (L2). Cut outcomes from PART I only. PART VI is NOT outcome-bearing.
**Measured at:** 2026-09-09 17:00Z–17:30Z, working tree HEAD `98e8771068` (origin/CLOUD `7e35640ec8`, ls-remote read).

---

## 0. HOW THE SIBLINGS WERE HANDLED, AND WHERE IT BENT

This brief is NEW by the skill's default, but the territory is not empty: Andrew's word is that it *wraps* D1, D2 and
D3. So I applied the midstream blindness rule to those three anyway, because a brief written while looking at the open
task-order set ratifies the branch instead of describing the base.

**Honoured:** I did not open a single task order under D1, D2 or D3, nor any project JSON's `phase`/`blocking`
field. I did not open `ADVI_PERFRP_PRD.md` past its header (see §VII.1 — a standing restriction names this seat).

**Where it bent, named:** (a) I read the directives board (`directives-check`) and the registry dashboard
(`registry-check -all`), which print each project's one-line *Where* — that is branch-adjacent prose and I read it;
(b) I read §1 (Scope) and §2 (Existing State) of the D1, D2, D3, D6, D8 and D10 PRDs, which describe intent and
measured state, not open work; (c) the D2 board stance's TO count (19 open) is in Part VI. None of the twelve outcomes
below was derived from an open task order; every one is cited to the proposal.

**"Unchanged" verdict, in part:** the proposal's engineering direction (§08–§09, §14) does not move the estate's
already-ruled direction — the D10 canonical pattern, the 2026-07-24 channel-independence rulings, and the
"four names, one fact" convergence are the same direction restated. What IS new is the PRODUCT decision (§06 D01): the
client workflow leaves Advisor Intelligence. That is the one thing the estate has not already ruled, and it is the
reason a D14 exists.

---

# PART I — THE OUTCOME TERRITORY

Twelve outcomes, each one thing a named kind of person can do. Numbered for L2 citation. The proposal's own
acceptance-test boxes (§04, §07, §11, §12, §14) are folded in where they fit; none is a number.

### O1 — An advisor finds a client by name or account and lands in the right scope, without walking the tree
An advisor in an authorized firm context types a client or account and arrives at that relationship or account
directly, still seeing where it sits under its book and firm. Top-down navigation (firm → book → relationship →
account) and direct search resolve to the same entity and the same permitted population. **SOURCE:** §07 "Entry,
search, and persistent context"; §11 "Navigation and direct search".

### O2 — An advisor answers "what does this client own, and which Opal models are involved" in one place, at every level
At account, relationship, advisor/book and firm, the advisor sees the underlying securities AND the Opal model
allocations that account for them, and the two reconcile to the same population. Assets whose model attribution is
unknown or unassigned stay visible as an exception, never summed silently into "all assets". The view links to
Positioning for a model's characteristics and does not re-implement it. **SOURCE:** §04 "Capability 3"; §04 capability
table (holdings + model views required at all four levels); §05 "Keep the page boundary".

### O3 — An advisor produces a client-ready performance report for an account or relationship, and the PDF says what it is
For a selected account or relationship and a selected period, the advisor previews the performance presentation and
exports a PDF that reproduces the same scope and values with the approved disclosures, and states its method basis,
data snapshot and as-of. If the figure is a normalized vendor result under the transitional method, the PDF says so;
it never implies an Opal-computed result that was not. **SOURCE:** §04 "Capability 1", "Define calculation ownership
before replacing a vendor", "Client-ready output is part of the product", ACCEPTANCE TEST box.

### O4 — From the same client context, an advisor runs an approved stress scenario and takes the result out as a PDF
At account or relationship level the advisor picks a preset scenario, sees the modeled response with its coverage
and limitations in context, and exports a PDF naming the scenario, scope, data date, method and limitations. Missing
betas or durations are shown as coverage gaps, never as a zero response. A modeled result is labelled as modeled.
**SOURCE:** §04 "Capability 2"; §16 row "Stress method and event definitions".

### O5 — A firm principal slices everything by supervision and by billing, independently, from the top down, and the slice survives
From the firm level the principal chooses supervised / unsupervised / all and, separately, billable / non-billable
/ all; the intersection applies to holdings, model views, reports and stress outputs; it persists across every
navigation step; a PDF shows the population it actually evaluated. Unknown classifications are visible in "all", not
coerced to false. **SOURCE:** §12 entire; COHORT ACCEPTANCE box (the nine combinations at each level).

### O6 — A partner sees only its own data, and a book-restricted user cannot widen their view by any route
Firm context and the user's permitted books govern every read, calculation, export and later agent query. A user
restricted to a book gains no firm-wide visibility by editing an account id in a URL, requesting a PDF, or asking an
agent for an aggregate; an authorized parent total reconciles with the visible child population under the same
filters. **SOURCE:** §11 "Foundation 1", "Reuse mechanics", FOUNDATION ACCEPTANCE box.

### O7 — Every partner gets the same product regardless of custodian or vendor; a new partner is a mapping, not a product
49 Financial (Schwab custodian-first + SmartX models), Inflection (Orion/Eclipse) and Cottonwood (Black Diamond)
produce the same Investor Reporting gold datasets and field meanings; the front end does not know which path produced a
tenant's data; switching a provider changes a mapping implementation, not the client's identity or the product's shape.
**SOURCE:** §08 principle 3; §09 "Common rules every adapter must satisfy", "Quality gates before serving"; §10 "Two
migration tracks into one gold contract".

### O8 — An engineer can draw the Investor Reporting dependency boundary and show that a change to a legacy page's gold does not reach it
Before build approval and at every release, someone can point at the boundary and demonstrate which changes to
Advisor Intelligence or Model Portfolios gold pipelines no longer affect Investor Reporting. Investor Reporting reads
shared bronze/silver and shared versioned libraries; it reads no other page's gold or serving output. **SOURCE:** §06
"What must not happen", DECISION D01 and its practical test; §08 principle 3; §14 "The minimum manifest" last
paragraph.

### O9 — It is there each morning at 9 Eastern, and late data is visible as late, never relabelled current
An advisor opening the workspace at the morning target finds a coherent published release for their firm; when a
provider is late, the affected scope shows its true age and the functions that no longer meet completeness are
withheld, while other partners' releases proceed. Source arrival, source business date, processing completion and
publication time are four visible facts, not one. The wall-clock intent survives daylight-saving without a manual
edit. **SOURCE:** §14 "Preserve the business requirement: 9:00 a.m. Eastern", "Clarification: no daylight-saving
hassle", "Late data must be visible, not relabeled".

### O10 — An engineer or an agent reads one manifest and knows, for every path, what it is and whether it may be used
For each pipeline and dataset touching Investor Reporting, one manifest states its inputs, outputs, owner, schedule,
consumers, layer and relationship to legacy paths, classified as retained shared source / active legacy / retirement
candidate / new Investor Reporting. An agent handed the manifest uses only declared active inputs. A path is retired
only when its consumers are resolved, its schedule disabled, its replacement validated and its retention addressed.
**SOURCE:** §14 "Establish the path map before the new build", PATH GATE box, RETIREMENT ACCEPTANCE box; §17 task
envelope.

### O11 — Opal can retire a vendor at a partner only when a named checklist says the replacement covers what the vendor supplied
For each partner, someone can read the replacement checklist — holdings, history depth, calculation basis, model
attribution continuity, partner acceptance, other workflows still on the vendor — and see which items are covered
before Orion, Black Diamond or a model source is discontinued. 49 Financial's custodian-first path is the reference the
others are measured against. **SOURCE:** §01 "The one-year ambition"; §10 "Model continuity is a separate replacement
gate"; §16 rows "Vendor retirement scope", "Model assignment continuity".

### O12 — An analyst or an agent later works over the same governed gold without re-deriving it (horizon-bearing)
Because gold stays in typed Parquet with recorded lineage and platinum JSON is the serving format only, a later
Opal analyst or an agent service answers BI and investor-analysis questions over the same committed data, identifying
scope, filters, snapshot, method and limitations. This outcome bounds the horizon (§13 Version 2); it is not a Version 1
deliverable and should be cut as a constraint on O7/O8, not as a build. **SOURCE:** §08 principle 6; §13 "Version 2";
§13 "GraphQL is a possible interface, not the analytical engine".

---

# PART II — WHERE THE BOUNDARY SITS

**Investor Reporting (D14, Andrew's number) OWNS:**
- the advisor client-service workflow as a distinct product surface inside the portal — search, the four-level
  navigation, holdings + model views, the two client actions, PDF export (§05 table row "Investor Reporting — new", §07);
- its own gold and platinum namespaces, schedules and publication path (§06 D01; §09 "Platinum"; §14 illustrative
  locations — illustrative, not existing paths);
- the Investor Reporting path manifest and the retirement acceptance for paths it replaces (§14);
- the two cohort axes as DATA contracts at their authoritative grain (§12);
- the per-partner vendor-replacement checklist (§10, §16).

**It RELIES ON, and does not own:**
| Relied-on thing | Owner / where it lives today | Note |
|---|---|---|
| Bronze + silver source foundation ("Opal Data assets" = `opal-data-assets`) | **D10 Partner Implementations** (the taxonomy directive; `D10_GLOBAL_PIPELINE_STRUCTURE_PRD.md`) | D10 already rules BRONZE raw / SILVER typed Parquet event-triggered / GOLD Parquet per-product-or-per-firm / PLATINUM JSON publisher to `opal-data-portal-v2`. §08–§09 restate it. Investor Reporting conforms; it does not re-rule. |
| Tenant identity + enforcement (edge JWT, `X-Firm-Id` injection, ownership-map scoping, role tiers) | `PORTAL_AUTHHARD_PRD.md` (CTO~B), `ADVI_ROLGAT_PRD.md`, `ADVI_FIRMSEP` (inactive) | Foundation 1 (§11) is a REUSE. See Part IV F-D. |
| The firm enumeration | `data/firm_registry.json` (NFRA_PSTMRT) | 3 client firms; buckets `opal-data-bd/inf/cot`. |
| Account → client/relationship → advisor → firm spine | Advisor Intelligence, **D2** | Foundation 2 (§11). |
| Account-grain model membership + SmartX↔Schwab exact join | **D3 Portfolio Analytics** (`D3_MODELOVERLAY`, `a06_dim_identity_crosswalk.py`) | O2's substrate at account grain. |
| Model / SMA / Alternatives / Insurance / Client view taxonomy + category registry | **D1 Model Portfolios** (`D1_CATVIEWS`, `mdpf_revamp_model_crosswalk.py`); `ASSETCLASS_TAXONOMY` | O2 consumes the registry; does not mint categories. |
| Performance method contract + parity oracle | RCN-0001/RCN-0002 (this seat), `fact_account_return` spec (HELD), `ADVI_49F` TWR engine, `ADVI_BDPARITY`, `ADVI_PERFRP` (D2) | See F-F and §VII.1. |
| Trading calendar | `lib/trading_calendar.py` (lane POD4) | Binds O9's "late" (CLAUDE.md NEVER: count trading days). |
| Channel-independence + manifest-only failure surface | Andrew rulings 2026-07-24, `MDPF_CHANNEL_INDEPENDENCE_PRD.md`; alarm moratorium (`GLOBALALARM`) | Binds O9. No SES/alarm build. |
| Agent query layer | **D6 Opal AI** (`D6_OPAL_ANALYST_GRAPHQL_PRD.md`) | O12's interface is D6's; Investor Reporting supplies governed gold. |

**It DOES NOT TOUCH:** Positioning (§05: "no redesign requested"); Advisor Intelligence's BI job (§05: stays
BI-focused; D2 continues); Model Portfolios' global/firm summaries (D1, D8/MDPF remediation); tax workflows (D9);
platform ops (D12); trading, account maintenance or unrestricted edits (§07 "Read functions first").

**Sibling projects, named (register state 2026-09-09 17:17Z):** `ADVI_PERFRP` (active, D2 — performance
attribution + reporting per client inside the ADVI Books tab; **direct overlap with O3 on HOME, the decision the CTO
must make at L2/L4**); `ADVI_BDPARITY` (active, D2 — the check-our-work harness = O3's oracle); `ADVI_STITCH`
(active, D2 — BD history we hold = O11's history item for 49F); `ADVI_49F` (active, D2 — TWR engine c-series);
`ADVI_INSURE` (active, D2 — insurance beside, never inside, performance); `ADVI_ROSTERCOLS`, `ADVI_COTKEY` (D2);
`D3_MODELOVERLAY` (active, D3); `D1_CATVIEWS`, `D1_NAMEDISCOVERY` (D1); `OPAL_ADVIPOINTERS` (active, D2 — the
ADVI/MDPF canonical repointing, "one traceable path from vendor bytes to the portal"); `MDPF_COTREMEDIATION`,
`WSE_COTMDL`, `MDPF_GLOBAL` (Model Portfolios); `NFRA_PPL49F` / `NFRA_PPLINF` / `NFRA_PPLCOT` (dormant since 07-10 —
the prior attempt at O10's resource-SSOT + debt decommission, Phase 0 only); `ADVI_FIRMSEP` (inactive — multi-firm
compartmentalization); `SXPL_RESTIN` (inactive — SmartX REST replacement of the Playwright exporter).

**What "wraps D1 D2 D3" means here, as this brief reads Andrew's word:** D1 supplies the classification registry O2
reads; D2 supplies the spine, the 49F reference path and the parity oracle O1/O3/O7 stand on; D3 IS O2 at account
grain. D14 is where those three converge into one advisor-facing product, and §06 D01 is the decision that moves the
client workflow's HOME out of Advisor Intelligence. Whether any member project re-homes to D14 is a register act
(MSTR as register owner, CTO at L3) — this brief names the relationship and moves nothing.

---

# PART III — THE QUALITATIVE BAR

Disputable statements. No number in any of them.

1. An advisor preparing for a client meeting produces that client's performance PDF here and does not open Black
   Diamond or Orion for it. (O3)
2. The same advisor, in the same session and scope, produces the stress PDF here and does not open YCharts for it. (O4)
3. A compliance reviewer reads the method basis, the as-of, the population filter and the disclosure version off the
   PDF itself, without asking engineering what produced it. (O3, O4, O5)
4. An advisor who checks a served figure against the vendor finds nothing they cannot have explained from the
   method contract and the parity record. (O3 — the ADVI_BDPARITY bar, carried unchanged)
5. A firm principal filtering supervised + billable at firm level reads the same total the sum of the visible books
   shows, and the same total their PDF carries. (O5)
6. When Black Diamond is unreachable for Cottonwood, 49 Financial's and Inflection's morning releases land anyway,
   and Cottonwood's screen says how old its data is. (O9)
7. A partner-operations person onboarding a fourth firm edits a mapping and a manifest row and touches no page code. (O7, O10)
8. An engineer asked "if we deleted Advisor Intelligence's gold tomorrow, what breaks in Investor Reporting?" answers
   "nothing" and can show the graph. (O8)
9. An agent handed the manifest and a question uses only declared active inputs and names them in its answer. (O10, O12)
10. Nobody at Opal discovers a frozen payload from a partner's complaint; the release surface says it first. (O9 — the
    D8 incident class, inverted)

---

# PART IV — THE SUBSTRATE: IS THIS IN A CANONICAL PATTERN?

Findings, each with what was measured, the instrument, and the vintage. Denominators printed.

### F-A — The three legacy pages exist as three routes; there is no Investor Reporting route
`portal/src/App.tsx` declares `/portfolios` (Model Portfolios), `/advisor-intelligence`, `/positioning` at lines
90/91/102; `portal/src/pages/` holds 18 entries (17 page dirs + `ModelPortfolios.tsx`), none named for reporting.
Instrument: directory listing + single-file grep on the working tree, 17:1xZ. **Finding:** §05's three-page map is
accurate; §06 D01 is greenfield on the portal surface.

### F-B — Gold is SIX per-firm-or-per-domain trees, not one contract; THREE bucket generations are live
`data/{assets,black_diamond,cot,inf,mdpf,etfs}/scripts/gold/*.py` = **10 / 69 / 43 / 54 / 23 / 9 = 208 gold scripts
across 6 trees** (listing, 17:1xZ). `data/firm_registry.json` binds the 3 client firms to `opal-data-bd`,
`opal-data-inf`, `opal-data-cot`; D10's canonical pattern puts bronze/silver in `opal-data-assets` and platinum in
`opal-data-portal-v2`; the D3 PRD names a third gold home `opal-data-49financial/gold/advi/` (8 dims + 8 canonical
tables, its run #1). CLAUDE.md's cross-firm NEVER rule states both bucket shapes are live. **Finding:** §08
principle 3 ("same gold contract across partners") is NOT the estate's current shape — it is the D10 direction, with
49 Financial the only partner measured on it (D2/D3 PRD reads). The proposal's own §09 sentence "gold is the
principal engineering lift" is corroborated by the 208-script census.

### F-C — Supervision and billing exist as per-firm gold FIELDS, at account grain with a current-flags caveat, not as a two-axis cohort dimension
`comp-find -i supervis`: 12,243 hits across 152,378 files (HEAD 576 / DEF 10 / DOC 2,581); the one gold producer is
`data/cot/scripts/gold/D_05.supervised_split.py`. `comp-read` on it: classification is at ACCOUNT grain
(`account_supervised` from the accounts dim, line 126), with an in-file "TODAY'S-FLAGS CAVEAT" (current flags applied
to history, CTO ruling 63310 cited at line 79) and a partition assert (buckets must sum to total, line 150). `comp-find
-i billable`: 1,078 hits across 152,380 files (DEF 6: `A_02.fee_rate_history.py`, `D_00c.portal_leaderboard.py`,
`D_02.advisor_client_detail.py` in BOTH `black_diamond/` and `cot/`). **Finding:** the estate has already answered
§12's open grain question for Cottonwood — account grain, current flags — and billing lives in the fee-rate lineage,
not as a cohort axis. Inflection's semantics for either token were NOT measured. Foundation 3 is a re-shaping of
existing fields into a contract, not a from-scratch build.

### F-D — Tenant isolation is measured SOUND and is a reuse
`PORTAL_AUTHHARD_PRD.md` (CTO~B, grounded at HEAD 2026-07-20): the trust boundary closes at the edge —
`auth-validator-edge` verifies the RS256 JWT and injects server-derived `X-Firm-Id`/`X-User-Role` over client headers;
advisor-id (004a) + ownership-map account/relationship (004c) + tier-role (`ADVI_ROLGAT`) scoping; explicit cross-firm
secret Deny. That PRD's own thesis: "this project is NOT re-architect tenant isolation." **Finding:** §11 Foundation 1
is a carry-over with an exercise obligation (O6's URL/PDF/agent widening tests), not a design. Vintage 07-20; not
re-exercised by this seat.

### F-E — The spine and the account→model join exist; account-grain membership is D3's live deliverable
The spine (account → client/relationship → advisor → firm) is the organizing structure of Advisor Intelligence and the
title object of `ADVI_PERFRP_PRD.md`; drill rights per role are enumerated in `ADVI_ROLGAT_PRD.md` §2. The D3 PRD
§2 (run 08-19) measures `a06_dim_identity_crosswalk.py` landing daily: smartx_allocation_uuid → smartx_account_uuid →
schwab_account_number → account_id at 99.86% feed→map / 99.65% end-to-end, with Andrew's bar quoted as "know it's
perfect rather than an estimate." **Finding:** O2 at account grain is D3's deliverable, in the pipeline (4 open TOs on
the board). Investor Reporting should consume it, not re-derive it.

### F-F — The performance method is further along than §04 says: a pinned method, a written contract, two teardowns, a held build, a live engine, a parity harness
- RCN-0001 (BD teardown, 8 HARs, 229 endpoints / 52 schemas): BD's `firm/globalsettings` method contract
  (`NetOfFees / Accrued / Account365 / ClassSpecific / QuarterToDate / FIFO`) and its transaction affect vector as the
  cash-flow taxonomy; Andrew pinned **Account365** 2026-07-21 (*"I like the BD approach because its defensible to
  refer to"*) — the standing METHOD-vs-NUMBERS split.
- RCN-0002 (Orion, 150 endpoints + Eclipse OpenAPI 493 paths): performance as a request-time calculation graph;
  method options firm-level AND account-level (32 + 5); the `1:69ANNUAL` days-with-value setting = our own `c01`
  defect class, named.
- `FACT_ACCOUNT_RETURN_BUILD_SPEC_20260721.md` — the CTO's "four names, one fact" convergence — **HELD at CTO
  registration since 2026-07-22**, register reads unchanged.
- `ADVI_49F` (active): the canonical runner chain with a TWR engine (c-series). `ADVI_BDPARITY` (active): P1 probe
  5 of 5. `ADVI_PERFRP` (active, D2 purpose project, PRD v0.2 from two BD HARs + 13 screenshots): distribution-restricted
  to this seat (§VII.1).
**Finding:** §04's "the conversation did not select a performance methodology" is true of the conversation and
false of the estate: method PINNED (Account365, TWR net-of-fee default), contract WRITTEN, build HELD, engine LIVE
for 49F, oracle LIVE. The open items are the ones the proposal lists after that sentence (gross/net presentation,
periods, corrections, incomplete history) plus the HOME question (Books tab in ADVI vs Investor Reporting).

### F-G — Sensitivity / stress analysis is GREENFIELD in the estate; the only YCharts assets are a session-capture path and gateway read tools
`comp-find -i 'stress_test|stress test|scenario_id|drawdown scenario|yen carry' --band DEF`: **0 DEF hits** of 103
total across 152,383 files (the 103 are DOC/SURFACED/CONFIG mentions). No `integrations/ycharts/`. YCharts presence:
`infra/aws/lambda/ycharts-session-capture/` + `infra/aws/terraform/ycharts-pipeline/` (a DISABLED 72-hour capture
schedule and an ENABLED 6-hourly probe, per `comp-trigger --list`), and six read-only `opal-gateway` MCP tools
(`ycharts_search / time_series / fund_series / snapshot_metrics / risk_return_scatter / freshness`). **Finding:**
O4 has no producer, no scenario contract and no method in the estate; the proposal's beta/duration description is a
hypothesis about a vendor (§04 says so itself). Any programmatic YCharts pull is vendor egress — Andrew's per-use word,
every time (README §3).

### F-H — PDF generation as a client artifact does not exist; headless-browser tooling does
`comp-find -i 'reportlab|weasyprint|pdfkit|fpdf|jspdf|react-pdf|pdf-lib|puppeteer'`: 143 hits across 152,383 files,
**DEF = 13, all `.mjs` puppeteer runners** (portal `.runtmp`/`.frontend-dev` screenshot runners, `valgate`, the
YCharts session-capture Dockerfile). **Finding:** the estate can drive a headless browser; nothing produces a
versioned, disclosure-bearing client artifact. §04 "Client-ready output is part of the product" is a build, and its
template/disclosure owner (compliance) is unnamed in the estate.

### F-I — Scheduling is two mechanisms and mostly UTC; event-driven silver→gold already exists for two partners; the 9 a.m. ET problem is a ruled direction, not a new idea
`comp-trigger --list` (live, us-east-1, 17:3xZ): **142 EventBridge rules + 19 Scheduler schedules.** Rules are
UTC cron expressions (e.g. `bd-*-pipeline-trigger` at 21:38–22:30Z MON–FRI; `inf-api-*` 11:02–11:32Z; `opal-assets-
silver-*-sweep-daily` 12:15–23:30Z); schedules include ET-named ones (`cot-bd-session-daily-et`, `estate-report-
0900et`, `opal-assets-ingest-mirror-cot-daily-et`) and `mdpf-scheduled-floor`, `advi-49f-gold-floor`. Event patterns
exist for `cot-bronze-complete`, `cot-silver-complete`, `inf-silver-chain-bronze-complete`, `inf-gold-dispatch-
release-changed`, `mdpf-feeder-accelerator`, three `*-served-guard-on-write`. Andrew's 2026-07-24 rulings
(`MDPF_CHANNEL_INDEPENDENCE_PRD.md` §0) already require event-driven bronze→silver→gold, per-partner channels that
never hold each other, carry-forward on a break, a manifest as the ONLY failure surface, and no SES alarms. The D8
re-mint records the measured failure this exists to end: served `as_of_last` frozen four trading days while the
publisher emitted daily (frozen INSIDE the payload). `comp-schedule` shows the trading-calendar guard in
`gold_dispatch.sh:59` INERT with 5 files named `trading_calendar.py` (drift candidate G-7). **Finding:** §14's
"one morning release, correctly sequenced inputs" is the estate's ruled direction restated, with the mechanism
half-built and two timing semantics live at once. The DST clarification (§14, Scheduler + `America/New_York`) is
correct and is what the `-et` schedules already do.

### F-J — The path manifest has been attempted before and is dormant; D10 is its owner
`NFRA_PPL49F`, `NFRA_PPLINF`, `NFRA_PPLCOT` (resource-SSOT + debt decommission, one per partner) — registered
2026-07-02, **dormant, Phase 0 only, last commits 07-10**. `OPAL_ADVIPOINTERS` (active) is the canonical-repointing
program ("one traceable path from vendor bytes to the portal"), stale-dates disclosed 08-29. `MDPF_PIPELINE_RESOURCE_
INVENTORY.md` and `MDPF_PIPELINE_TRUTH.md` exist for one page. **Finding:** §14's manifest is a re-buy unless it lands
as D10's instrument over the D10 taxonomy; the prior per-partner attempt stalled at Phase 0 and the brief cannot say why
(not chased).

### F-K — The directive register has no D13 and no D14
`comp-read --enumerate 'D1[34]\b'`: 0 hits / 481 lines in `org/missions/DIRECTIVES.yaml`; 0 hits / 44 lines in
`DIRECTIVES_RETIRED.yaml`. Live: D0–D12 (13 live, 1 retired; `directives-check` 17:17Z). **Finding:** D14 is
Andrew's number and is unminted; D13 is unexplained by anything read here. The register row is `0.0.0_AB_MSTR`'s cell.

### F-L — The proposal's terminology map already has an estate object: one firm enumeration, and ADVI_ROLGAT's role tiers
`data/firm_registry.json` is "THE ONE FIRM ENUMERATION" by its own law block (3 client firms; `kind` enum
client|test|demo). §03's "partner/advisory firm vs advisor/book" split maps to `firm_id` vs the ROLGAT/ADVI advisor
object. **Finding:** §03's ambiguity fix is a naming discipline over existing keys, not a schema.

---

# PART V — WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Named, not sequenced. Sequencing is L5.

1. **D14 exists on the register** with its member set stated (MSTR, on Andrew's word; §F-K).
2. **The HOME of client-level performance reporting is decided** — inside Advisor Intelligence's Books tab
   (ADVI_PERFRP as written) or inside Investor Reporting (§06 D01) — and ADVI_PERFRP is amended, re-homed or
   superseded WITH its pointer (XXX.md terminal-status rule). CTO.
3. **The 08-24 distribution restriction on ADVI_PERFRP toward this seat is confirmed, lifted or scoped** (§VII.1). Andrew.
4. **The performance presentation decisions the proposal lists are owned:** gross vs net presentation, supported
   periods, fee and flow treatment, combined histories, corrections, incomplete history — on top of the pinned
   Account365 / TWR net-of-fee method (§04, F-F). Investment owner + compliance.
5. **The `fact_account_return` HOLD is lifted, superseded or re-homed** — it has been HELD at CTO registration since
   2026-07-22 (F-F). CTO.
6. **The stress method and scenario definitions are owned:** approach (historical replay vs factor vs prescribed
   shock), the three named episodes incl. the unresolved "2016 issue", coverage rules for missing beta/duration, cash,
   funds, look-through (§04 Cap 2). Investment owner + compliance. **Data rights / vendor egress for any YCharts pull:
   Andrew, per use.**
7. **Cohort grain and history policy per partner:** account-grain current-flags is Cottonwood's measured choice
   (F-C); 49 Financial's and Inflection's are unmeasured; the historical-flags policy (§12 "recorded under an approved
   historical policy") is undecided. Product + partner ops.
8. **Authoritative model-assignment source per partner, post-migration:** SmartX (49F), Eclipse (INF), Black Diamond
   (COT) today; what replaces each is unnamed (§10). Investment + data engineering.
9. **The D10 gold-bucket case for Investor Reporting** (per-product vs per-firm — "Andrew defines which case") and the
   namespace under it. Andrew via D10.
10. **Custodian access inventory per partner, verified not estimated:** Inflection Fidelity (no direct access per the
    proposal), Cottonwood Schwab (no portal access per the proposal), 49F Fidelity coverage (§10). Partner ops.
11. **Publication policy:** what blocks a whole release vs a tenant vs a capability; retention of the last coherent
    snapshot; correction/reissue (§14). Platform + product. Under the standing alarm moratorium.
12. **PDF template, disclosure text and review process owner** (§04, §16). Compliance. No wording invented anywhere in
    the chain until then.
13. **Naming:** "Investor Reporting" is provisional (§06). Andrew.
14. **The trading calendar is one file in one lane** (F-I: 5 basenames, guard inert). POD4 / whoever D10 names.

---

# PART VI — STATUS SCOPING — NOT OUTCOME-BEARING

Measured 2026-09-09 17:00Z–17:35Z. Ages; do not cut outcomes from it.

1. **Register:** 355 project JSONs; 48 open; 86 open TOs estate-wide; 13 live directives D0–D12, 1 retired; 34 of 48
   open projects are directive members (14 unaffiliated). D2 holds 19 open TOs, D3 4, D1 1 (`directives-check`).
2. **Siblings' last commits (calendar):** `ADVI_PERFRP` 09-02 (CVO); `ADVI_49F` 09-03 (CTO); `ADVI_BDPARITY`,
   `ADVI_STITCH`, `ADVI_COTKEY` 09-01 (CRO~A); `D3_MODELOVERLAY` 09-02; `D1_CATVIEWS` 09-03; `OPAL_ADVIPOINTERS` 09-04;
   `NFRA_PPL49F/INF/COT` 07-10 (dormant) (`registry-check -all`).
3. **Held/unchanged since July:** `fact_account_return` build spec HELD at CTO registration since 2026-07-22
   (RECON_REGISTER RCN-0001 downstream; no BDX/total-return project JSON then or now).
4. **Live triggers:** 142 EventBridge rules + 19 Scheduler schedules, us-east-1 (`comp-trigger --list`, budget 60 s,
   used 1 s). Among them: `ycharts-session-capture-schedule` DISABLED; `advi-49f-publisher` schedule DISABLED;
   `advi-49f-gold-floor` ENABLED.
5. **Gates armed (`comp-schedule`):** 26, of which 7 open deploy-ledger entries (two ADVI_INSURE, one freshguard, two
   D12 SMS, two OPSEC) and 12 standing NEVER clauses; 137 project `blocking` fields carry prose (a reading list, not gates).
6. **Portal:** three legacy routes live (F-A). Portal submodule is a work-site, not a base; not entered.
7. **This seat:** HEAD `98e8771068`; origin/CLOUD `7e35640ec8` (ls-remote read 17:0xZ). Push state of this brief: LOCAL
   until an integrator runs.

---

# PART VII — WHAT THIS BRIEF DOES NOT CLAIM

1. **ADVI_PERFRP was read to its header only.** Its header carries *"DISTRIBUTION RESTRICTION (Andrew ~16:1xZ):
   nothing on this subject to `4.0.0_SA_CRO`"* (2026-08-24). I stopped there. Nothing in this brief about the
   performance-reporting shape comes from that PRD; O3 is cut from the proposal and F-F from this seat's own RCN-0001/
   RCN-0002 record and the registry. Today's instruction is Andrew's word to this seat on a document covering the same
   subject; whether the 08-24 restriction stands is surfaced in the Andrew-direct record and NOT adjudicated here.
2. **No task order under D1, D2 or D3 was opened** (§0). If an open TO already delivers one of O1–O12, L2 will find
   it; that is the designed check.
3. **Silver "all columns retained" (§09) was not measured.** `mirror_schemas.py` exists in four `opal-assets-silver-*`
   lambdas, which suggests typed passthrough; UNVERIFIED.
4. **Tenant enforcement was not exercised** — F-D cites the AUTHHARD PRD's grounding at its 07-20 vintage.
5. **Custodian access, holdings percentages ("approximately 4% at Fidelity", "roughly 60% may be [at Schwab]") and
   vendor arrangements are the proposal's account of Andrew's account** (§10 says so). Carried as direction to verify
   (Part V.10), never as facts. No percentage from the proposal is repeated as a measurement anywhere above.
6. **The proposal itself is an LLM rendering of a planning conversation** (its own front matter). Its "Established
   direction" rows are treated as Andrew's direction; its "Recommendation" rows as recommendations; its illustrative
   S3 paths (§14 table) are not paths and were not searched for.
7. **Inflection's supervision/billing semantics were not measured** (F-C covers Cottonwood and 49F/BD trees only).
8. **Why `NFRA_PPL*` stalled at Phase 0 was not chased** (F-J).
9. **No bucket or live S3 object was read.** Bucket names come from the firm registry, the D3 and D10 PRDs and CLAUDE.md.
10. **The `1:69ANNUAL`/`c01` defect's current state in `ADVI_49F` was not re-measured**; F-F carries RCN-0002's naming only.
11. **"2016 issue" and "Pershing Square"** remain exactly as unresolved as the proposal leaves them.
12. **D13** — its absence is reported, not explained.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/investor-reporting-unification-brief-20260909.md
  SOURCE            docs/briefs/sources/INVESTOR_REPORTING_UNIFICATION_PROPOSAL_20260909_extracted.txt
                    (docx sha256 db4168a65ef0afe2c7e8436ca9be8e2ee5776d35e6d5ae2cf4df769ff61ef0e8, 80,251 B, Andrew's Desktop)
  ANDREW-DIRECT     org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260909_171xZ_INVESTOR_REPORTING_BRIEF_CREATE_WRAPS_D1_D2_D3_ESTABLISHES_D14.md
  DIRECTIVE         D14 "Investor Reporting" -- Andrew's number, UNMINTED (F-K); register owner 0.0.0_AB_MSTR
  PROJECT           NONE-YET
  EXISTING PRD      NONE for Investor Reporting. Touching PRDs: ADVI_PERFRP_PRD.md (D2; header-only read, restricted),
                    D1_ASSET_CATEGORY_VIEWS_PRD.md, D2_ADVI_49F_E2E_PRD.md, D3_ACCOUNT_MODEL_OVERLAY_PRD.md,
                    D10_GLOBAL_PIPELINE_STRUCTURE_PRD.md, D6_OPAL_ANALYST_GRAPHQL_PRD.md, MDPF_CHANNEL_INDEPENDENCE_PRD.md,
                    PORTAL_AUTHHARD_PRD.md, ADVI_ROLGAT_PRD.md
  SIBLING PROJECTS  ADVI_PERFRP, ADVI_BDPARITY, ADVI_STITCH, ADVI_49F, ADVI_INSURE, ADVI_ROSTERCOLS, ADVI_COTKEY,
                    D3_MODELOVERLAY, D1_CATVIEWS, D1_NAMEDISCOVERY, OPAL_ADVIPOINTERS, MDPF_COTREMEDIATION, WSE_COTMDL,
                    MDPF_GLOBAL, NFRA_PPL49F, NFRA_PPLINF, NFRA_PPLCOT (dormant), ADVI_FIRMSEP, SXPL_RESTIN (inactive)
  PRIOR ART         RCN-0001 BD teardown + FACT_ACCOUNT_RETURN_BUILD_SPEC_20260721.md (HELD 07-22);
                    RCN-0002 Orion teardown + PLATFORM_STRUCTURE_COMPARISON_20260722.md;
                    Account365 pin + METHOD-vs-NUMBERS split (Andrew 2026-07-21);
                    channel-independence rulings (Andrew 2026-07-24); D10 canonical pattern (Andrew 2026-08-25);
                    a06_dim_identity_crosswalk.py (D3); mdpf_revamp_model_crosswalk.py (D1);
                    D_05.supervised_split.py (cot cohort at account grain); data/firm_registry.json; lib/trading_calendar.py
  MEASURED AT       2026-09-09 17:00Z-17:35Z; HEAD 98e8771068; origin/CLOUD 7e35640ec8 (ls-remote)
```
