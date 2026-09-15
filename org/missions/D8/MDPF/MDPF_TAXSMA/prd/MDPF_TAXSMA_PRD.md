# MDPF_TAXSMA — complete traded-account membership and daily additive assets

```json
{
  "project": "MDPF_TAXSMA",
  "directive": "D8",
  "fabric": "laptop",
  "prd_version": "v0.1",
  "step": 4,
  "brief_ref": "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md@8e8afed454961bebb2a3d90a43522787e19ec9e4",
  "endpoint_outcomes": [
    "FWD-1",
    "FWD-2",
    "FWD-3",
    "FWD-4",
    "FWD-5",
    "FWD-6",
    "FWD-7",
    "FWD-8"
  ],
  "status": "DRAFT"
}
```

Author: `1.0.0_SA_CTO~A`. D8 / MDPF / laptop.

Brief: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md@8e8afed454961bebb2a3d90a43522787e19ec9e4`. Registration and Andrew's approval: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_MDPF_TAXSMA_ENDPOINT_APPROVED_20260915.md@e61a60b46f7babe37c050e0fca0a6ab543d6487e`.

The following endpoint carries the approved text from `org/tier1_exec/1.0.0_SA_CTO/deliverables/TAXSMA_D8_PIPELINE_20260915/ENDPOINT_PROPOSAL.md@8e8afed454961bebb2a3d90a43522787e19ec9e4`. Only the card heading layout is normalized to canonical FWD definition syntax; all DONE WHEN, ACCEPT and SOURCE text remains verbatim. Every bar requires EXERCISED completion; approval is not implementation evidence.

## ENDPOINT (step 2, /endpoint --forward)

FWD-1  — Live Tax SMA accounts are clearly separated from prospects and untraded accounts.

DONE WHEN: **EXERCISED** — a deliberate walkthrough demonstrates the membership distinction.

ACCEPT: An operator explains why each account belongs in the live group or stays outside it; a funded account that has not entered the strategy stays outside.

SOURCE: brief §I.O1, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md:28`.

FWD-2  — Workbook accounts can be reconciled to the intended Schwab accounts without guessing.

DONE WHEN: **EXERCISED** — a controlled comparison demonstrates both matches and disagreements.

ACCEPT: An operator can follow each live account to its custodian record, see missing or conflicting matches, and review additional candidates without calling them live automatically.

SOURCE: brief §I.O2, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md:32`.

FWD-3  — Newly traded accounts and later status changes reach the whole data path.

DONE WHEN: **EXERCISED** — a controlled activation and correction have been followed through to their results.

ACCEPT: An operator changes a controlled account case from pending to traded, then corrects it, and sees the right dated inclusion without manually patching the list of accounts being processed.

SOURCE: brief §I.O3, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md:36`.

FWD-4  — Daily Tax SMA assets have a consistent value and a traceable date.

DONE WHEN: **EXERCISED** — a deliberate comparison demonstrates the value and its stated basis.

ACCEPT: An operator traces the reported assets back to the dated account values and can explain the treatment of cash and borrowing; sales estimates and old quarterly figures do not stand in for daily assets.

SOURCE: brief §I.O4, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md:40`.

FWD-5  — Incomplete or outdated information cannot look like a complete current total.

DONE WHEN: **EXERCISED** — controlled missing and delayed information has demonstrated the visible limitation.

ACCEPT: A reader can tell when accounts or current values are missing, distinguish that from a true zero, and see the relevant date without mistaking a partial amount for the complete total.

SOURCE: brief §I.O5, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md:44`.

FWD-6  — Tax SMA assets add to 49 Financial and Global exactly once.

DONE WHEN: **EXERCISED** — a controlled before-and-after comparison demonstrates the intended totals.

ACCEPT: A reader sees the Tax SMA amount included in its category and in both intended totals exactly once, with the Client amount and other firms unchanged.

SOURCE: brief §I.O6, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md:48`.

FWD-7  — Authorized operators can explain the result while private account information stays protected.

DONE WHEN: **EXERCISED** — a deliberate review demonstrates traceability and the information boundary.

ACCEPT: An authorized operator can explain an inclusion, exclusion and exception from the supporting records, while the ordinary report reveals no client names or complete account numbers.

SOURCE: brief §I.O7, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md:52`.

FWD-8  — The pipeline runs reliably and can be recovered without duplicate contributions.

DONE WHEN: **EXERCISED** — controlled failures, repeated runs and recovery have demonstrated the behavior.

ACCEPT: An operator deliberately causes a failed run, sees what failed, recovers it and repeats it; the result is correctly dated, includes no duplicate contribution and preserves existing reports.

SOURCE: brief §I.O8, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_TAXSMA_D8_PIPELINE_BRIEF_20260915.md:56`.

## CONTRACTS

These are proposed engineering contracts at L4. The eight approved outcomes above retain their original completion bars. `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` v0.1.0 closes the project's enumerations, data meanings, response boundary, limits and error vocabulary; implementations consume that file rather than inventing a second enumeration. Its approval state follows this PRD's two independent L4-R halves. A source observation is not a grant or an implemented capability.

| Contract | Direction / owner | Binding agreement and concrete treatment |
|---|---|---|
| Sovereign scope and additive basis | consumed; Andrew's L1 carrier at `8e8afed454` and L2 approval at `e61a60b46f` | D8 / MDPF / laptop. Traded accounts differ from sales prospects; full expected membership drives coverage. Tax contributes to 49 Financial and Global exactly once; Client is unchanged. All eight outcomes require EXERCISED proof. The separate D9 workflow supplies business evidence but is not a daily Black Diamond reporting dependency. |
| Workbook business claims | consumed; Shared/TAX workbook owner | One fixed site/item/Sheet1, all used rows, version-consistent reads, strict headers and exact account forms under the data contract. A workbook edit is data, not code or an account grant. `Traded=Yes` establishes an expected business claim; it does not independently prove historical activation or solve custodian disagreements. Blank, prospect, numbered-untraded and unresolved previously traded rows remain distinguishable. |
| Gateway delegated identity | consumed and narrowly extended; `NFRA_OPLMCP` | `docs/architecture/NFRA_OPLMCP_PRD.md@33c581d223e2e3bac5e44a37abb407b5f79f82de`, sections 1, 2 decision 1 and 6, keeps per-person delegated Graph access. CTO disposition 96946, recorded in `GOVERNING_CONTRACTS.md@d971e17752`, authorizes the architecture of one content-specific capability: `GET /ms/taxsma-workbook`, separate static bearer, server-held delegated token, one named person, one workbook, seven projected columns. Existing `ms_ingest.py` is a structure-only precedent, not permission to emit content there. The new route has its own guard before generic `/ms/*` handling. No app-only Graph permission, second token store, copied research credential, or generic caller identity. Andrew must name the person and authorize this unattended content use before activation; the PRD fixes every other design choice. |
| Custodian and canonical value | consumed; 0833 ingestion / ADVI canonical valuation | Use the full reporting-master identity and complete account key. `fact_acc`, `fact_rps`, `dim_balance` and `canonical_valuation` retain their own source dates and hashes. Reuse `data/assets/scripts/gold/runners_49f/b00_canonical_valuation.py`; authoritative capital is `dim_balance.net_mv_plus_cash`. Preserve cash/short/margin treatment and the existing accrual placeholder's PENDING-RULING limitation. This project neither changes b00's formula nor substitutes its similarly named holdings engine. |
| Provider reporting enrollment | relies on; `OPAL_TAXSMA_REGISTRY` and reporting-pull owner | Existing `active`, `pending_resolution`, `inactive`, missing and unavailable states are read and mapped to the separate technical axis. Preserve manually resolved BD identifiers. No roster rewrite, provider-pull enrollment, quarterly-report refresh or new BD egress is needed to produce daily Schwab assets. Missing BD identifiers never remove a traded account from the expected denominator. |
| Gold history and corrections | consumed and explicitly interpreted; `MDPF_CANON` / CTO | `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md@8d12b77adbcb871c6d267ce7ae501b260b2ae727`:178 and DEC-2:203-207; doctrine R11/R12/R18 at `6dab0d76a7425ee2448b872790c3364acdf87b2e`. CTO disposition 96944 at `GOVERNING_CONTRACTS.md@d971e17752` closes the interpretation: immutable daily **knowledge-date** partitions, independent **valuation_date**, new later observations with `supersedes_observation_id`. Once today's object exists, changed knowledge queues for the next daily partition. Readers consolidate the whole observation history per account/valuation date before summing; they cannot mistake a correction-only partition for the cohort. No same-date replacement leaf, overwrite, dual writer or shadow tree. The CANON owner carries this interpretation at its next contract bump. |
| Canonical naming and tenancy | consumed; `LGIC_ENFORCE` / `MDPF_CANON` | CTO owner disposition 96960 (2026-09-15T07:37:11Z) resolves the conflict under doctrine R7, Andrew's “These work i like it” at `3fd386598f`: firm-attributable Gold/state belongs in the firm bucket; Global composite Gold and MDPF pipeline code belong in the product bucket. `address(source,scope,tier,table,partition,object=None)` supplies every new address, without an override. CANON v2.3:177-179 is the stale carrier; its owner `1.0.0_SA_CTO` has explicitly amended the engineering contract by this disposition and will update its prose at the next bump. Publisher reads N+1 homes, firm buckets plus product Global. No worker chooses a bucket, weakens a fence or migrates an unrelated tree. |
| Artifact set and sole publisher | extended; `MDPF_CANON` and publisher owner | CANON v2.3:178-179 enumerates four artifacts and omits the already existing category view. This PRD explicitly adds the `category_views` Gold table / `category-views.json` served leaf to the TAXSMA contract, plus the protected `taxsma_assets` observation table. The owner must carry the category-view addition at its next bump. `opal-assets-mdpf-portal-publisher` remains the sole numerical parquet-to-JSON publisher. It may read the protected control state for **status only** (pending/auth/failure), never for account values or an alternate cohort total. It checks source coverage, destination existence/content and matching generation before reporting publication complete. |
| Consumer and migration boundary | extended; `D1_CATVIEWS`, coordinated through `2.0.0_SA_COO~D` | Counterparts `docs/architecture/D1_ASSET_CATEGORY_VIEWS_PRD.md@5d356cc426f6d3bdcaccfe192482ec2e04788270` and `docs/architecture/D1_CATVIEWS_SMA_LIVE_PRD.md@42fb68944bd244ba350bc4e2ee9a2065862c8633`. CTO disposition 96939 permits the narrow unknown/stale Tax presentation and affected totals; taxonomy stays unchanged. CANON DEC-5 preserves caller URLs during its migration; this PRD deliberately corrects the consumer's value/status contract. The actual calls remain `/api/general/mdpf/{firmId}/category-views.json`; the historical Global served key remains unchanged. Repointing/migrating storage stays with CANON. |
| Zero, unknown and incomplete display | consumed and specialized; D1_CATVIEWS | Andrew's L1-only amendment `ANDREW_DIRECT_20260915_024xZ_DSGN_REBRND_WHOLE_DOLLARS_AND_ZERO_L1_BUCKETS_SHOWN.md@fe76e3e036` displays zero/null L1 buckets as $0 once a sibling is valued, with whole-dollar presentation. It does not amend L2. Under CTO 96939, explicitly **unknown or stale Tax** is a visible dated exception, not a zero/null that may hide or become $0; affected complete totals remain unavailable. True zero retains ordinary presence rules. Unmapped taxonomy remains unmapped. |
| Execution, credentials and release | consumed; existing MDPF schedules, Gateway owner, deployment owners | Engineering is on this laptop fabric; production continues on registered AWS hosts/functions. Reuse the 13:30 UTC daily Gold floor and 13:50 daily publisher, including non-trading days. Add a bounded Tax prelude to the Gold invocation, not another standing monitor. Pipeline principals must receive only the exact read/write/capability grants their declared role needs and satisfy existing firm fences. Existing ambient worker credentials are a separately accepted current posture, not authority to widen runtime IAM. Normal deploy evidence, source-to-package parity and never-widen sign-offs apply. |
| Frontend freeze | consumed; Andrew | `ANDREW_DIRECT_20260914_052xZ_FRONTEND_DONE_IS_BUILT_BEHIND_THE_FREEZE_LIST_OWNER_FALLBACK.md@65a535f194` permits building and committing behind the freeze. Promotion, shared-branch push and gitlink movement remain held. Controlled local/staged exercises discharge the specified walkthroughs where their exact environment is stated; they do not claim live production delivery. |

## 1. The arc

Start with a complete, authenticated workbook snapshot and explain every row's business status. Preserve its version and effective membership evidence, reconcile full identities against the intended reporting master in both directions, and keep every unresolved traded claim in the coverage denominator. Join the proven dated population to the existing canonical account valuation, emit immutable observations, and carry the independent additive basis through firm and Global shaping. The sole publisher delivers the corresponding values, dates and completeness status to the existing category reader. Finish by deliberately changing, breaking and recovering controlled inputs and following those effects through the displayed Tax leaf and affected totals. No stage may turn a missing predecessor into an apparently complete successor.

## 2. Purpose and measured starting point

DONE means an operator can explain the full path from a business-status claim to a dated account value and its single contribution to 49 Financial and Global. A prospective or merely funded account is not live Tax membership. A traded account need not trade every day to remain a member. A missing traded account stays visible as missing, and successful processing of fewer accounts is not completion.

The documentary source run is `workflows/atom_decomposition/runs/mdpf-taxsma/20260915T0510Z`, finalized CERTIFIED at `717f49f6ea`. **Only `rectangle.final.certified.json@4ff8d9bdaa` is consumable**, SHA-256 `4a90496aa306b3c6edbf1ae589c67625e74ba8f1e2d093ed5bd93350c565a7a6`. CVO's passing terminal certificate was placed at `b79ced9360cae48123f50812a7515915c38254fb`, byte-equal to its signed verdict at `9af8072cd827e3d4871f6fcfeca845185f3a4162`. The certified patch set is empty. The planted historical `rectangle.final.json` and withdrawn patch are never PRD ground truth.

Expected rectangle IDs are exactly `S1-workbook`, `S2-identities`, `S3-enrollment`, `S4-valuation`, `S5-category`, `S6-publication`, `S7-operations`, `S8-onboarding`; every entity has `source_contract`, `recorded_observation`, `unverified_boundary`: **8 x 3 = 24 cells**. The canonical validator returned zero violations and the terminal check zero violations/deviations. CVO certified documentary coherence, not deployed behavior, and did not independently rederive every identity helper or onboarding document. A MEASURED boundary proves a documented gap with an owner/probe; it is not a runtime expected value.

| Source-grounding row | What the measured vintage establishes | What it does not establish |
|---|---|---|
| S1-workbook | September 14 workbook, read through live Gateway MCP before the brief: 20 account slots, 10 numbered, 3 unopened prospects, 7 blank; eight numbered Yes/Yes and two No/No. Used rows = 22 including header and Total. | Eight is a snapshot, not a fixed list; displayed 33.33 million includes prospects and is not daily assets. The masked August workbook cannot support an exact additions diff. |
| S2-identities | September 11 0833 ACC has 7,469 rows and 11 Tax strategy candidates; six of eight workbook-traded claims match the dated account/position/balance sources. Two workbook/custodian strategy labels conflict. Ten numbered workbook identities have no match in same-date 0824 ACC. | Missing claims have no proven cause; candidates are not automatically traded. Same-date non-overlap is not a permanent additive proof. |
| S3-enrollment | Existing roster has five entries: three active and two pending BD resolution; three of the eight traded claims are absent. | Technical BD enrollment is not the expected traded population; quarterly reporting is not a complete current daily feed. |
| S4-valuation | The same six claims have existing canonical values; the 7,468-row dated canonical object ties the inspected values to balance to the cent. Basis is net market value plus cash. | Six values are not an eight-account total. A zero accrual placeholder is not proof of no accrued income. |
| S5-category | Existing key `tax` already maps to Tax-Managed SMA / SMA / ALT Strategies and ADDITIVE. Current Global fixed-key and reconstruction paths can drop new members/basis. | Registry membership alone proves neither a produced daily contribution nor correct Global inclusion. |
| S6-publication | Existing publisher, accessor and renderer are identified. Missing/empty inputs, hidden null Tax leaves and source-hash-only publication skipping require explicit correction. | Source inspection, a successful upload or a declared route is not a successful authorized page read. |
| S7-operations | Source and deployment declarations name the daily Gold floor, publisher and canonical calendar binding. | A schedule being enabled does not prove complete inputs, correct dates, or an exercised recovery. |
| S8-onboarding | SharePoint SOP distinguishes onboarding money-manager and reporting-master roles. Converter uses Ready/existing files rather than a full traded denominator. | This D8 project does not run or alter the D9 converter, open accounts, change strategy or grant access. |

The workbook and named relevant source tables were read completely; broader SharePoint searches had continuation links and were not a tenant census. September 11 was the latest present when measured before the next delivery; that alone is not lateness. Public evidence uses aggregate counts and masked display labels only. Raw full IDs, balances and OAuth receipts remain in protected/private data, not this PRD or ordinary repository files.

## 3. Territory and detailed design

### 3.1 Owned engines and dependencies

This project owns the engineering changes represented by S01-S18 in the surface manifest: workbook capability, snapshot acquisition, effective membership, reconciliation, dated Tax observation production, firm/Global contribution, category shaping, publication/status delivery, accessor behavior, leaf presentation, page date/total presentation, Gold packaging, scoped runtime access, controlled proof harness, operator recovery contract, activation disposition, publisher packaging and Gateway packaging. Ownership here is responsibility for delivering this extension; it does not replace the standing Gateway, CANON or D1 owners. Each shared surface is coordinated before edits.

Relies-on references D01-D08 are named in `component_manifest.yaml` beside this PRD and appear as dependency IDs only in the manifest: D01 workbook business evidence; D02 0833/0824 dated sources; D03 b00 canonical valuation; D04 existing BD roster/xref; D05 LGIC builders and resolved CANON contract; D06 existing Gold/publisher schedules; D07 Gateway token broker/audit; D08 D1 consumer rules and freeze. These are not authoring rows. The certified run's original 24-component inventory remains its historical grounding scope. The PRD's separate normative inventory declares this extension's whole target set, including proposed units; neither count is presented as an estate census.

### 3.2 Workbook capability and stable snapshots — S01/S02

Implement one route at the registered Gateway, with the content-specific guard and output projection in the data contract. It accepts no caller-selected site, item, sheet, range, URL, identity or Graph query; every other method or selector is refused. The server reads exactly the configured workbook's named Sheet1 used range, checks the whole response and stable before/after ETag, then emits only the seven named business fields and minimal row/snapshot metadata. Do not freeze A1:N22: new rows must be discovered without a code edit. Unique expected headers and a recognized Total row are structural conditions; ambiguous headers, unknown nonempty row structure, partial pages, extent overflow or an ETag race invalidate the snapshot. Blank indexed slots remain blank when all business cells are empty. A Total row is a unique explicit Total marker, without an account identity or traded status; other nonempty summary-looking rows are UNRECOGNIZED, never silently dropped.

Do not return client names, adviser contacts, AUM estimates or free-text instructions/comments. `other_business_cells_present` is a boolean allowing a nameless unopened prospect to differ from an empty template row. Reading the worksheet internally still accesses client-financial content; Andrew's activation approval must cover that bounded read, not just the projection. No existing structure-only route is widened.

Acquire the snapshot at the beginning of the existing scheduled Gold invocation. Persist the minimized response as protected versioned source/control evidence, bound to source ETag, acquisition time and SHA-256. A read failure produces AUTH_REQUIRED or SOURCE_UNAVAILABLE with the last successful snapshot's date; it never manufactures an empty workbook. Retain the prior expected cohort with unavailable-current-source status. First-run failure yields unknown denominator, not zero. Snapshot records are inputs to the membership engine, never a second served value path.

### 3.3 Business membership and effective history — S03

Parse status explicitly under the data contract. Ready=Yes alone, an account number, a funded balance, custodian open status or a Tax strategy label does not activate membership. Traded=Yes is an expected business claim; contradictory Ready/trading/identity fields become a conflict attached to that claim. Traded=No remains excluded from values even when funded. A prospect without an account remains a prospect and an empty slot remains blank. Count all four populations plus conflicts on each complete snapshot.

The first full snapshot establishes the currently claimed population. It does **not** backdate every member to the oldest available valuation. For a valuation date, inclusion requires evidence of membership effective on that date: source-proven activation evidence or an authorized operator's dated disposition. `Inception Date` and `Last Trade Date` are evidence fields, not silently interchangeable with first strategy activation. Unknown effective dates remain an explicit unresolved part of coverage. A correction disposition records actor, full account key privately, effective date, evidence, reason, snapshot and superseded disposition. It cannot grant access, open an account or place a trade.

Each subsequent complete snapshot is compared by validated full identity, not by row number or last four digits. New Traded claims are automatically discovered and enter the expected denominator; a missing BD identifier does not hold that discovery back. A removed or rekeyed previously traded row remains REMOVED_UNCONFIRMED or TRANSFER_UNRESOLVED until a dated disposition proves deactivation or transfer. Confirmed deactivation ends membership on its effective date; an account remains in historical dates where it was active. A later correction cannot erase the earlier observation. No monthly/manual hardcoded roster update is required for normal activation.

The current cases requiring operational reconciliation are the two uncorroborated traded claims and two strategy conflicts. Resolve their actual cause from authorized evidence during implementation; do not invent corrected numbers or presume a late feed. This is acquisition of case evidence under a closed rule, not an open architecture choice passed to L5.

### 3.4 Complete-identity reconciliation — S04

Normalize only the approved full forms. Reject suffix padding, masked values, malformed separators, Unicode digit coercion, fractional/numeric precision loss and scientific-notation strings. Duplicate full account keys are a conflict even if rows appear equal; do not select the first. Preserve source row identities privately so an operator can find the issue without a consumer-visible account number.

For every expected claim at each valuation date, join full account identity to 0833 `fact_acc`, canonical value and balance, with position data as corroboration. Record the reporting-master identity, custodian status and strategy, source partition and version/hash. Report each disagreement as a reason; a matching account number does not override a master or strategy conflict. Never alias money-manager master 0804-4932 to reporting 08335338 or base 08242234. Discover additional Tax-labeled custodian candidates by the complete dated source population and classify them UNCONFIRMED; no automatic workbook edit or membership promotion follows.

Compare the expected Tax set to the full dated base population before adding its value. A full-ID overlap blocks the affected additive total pending explicit basis resolution; it does not subtract from Client, net an arbitrary number or reuse the historical zero-overlap observation as perpetual permission. An unavailable base/control source is an unverified overlap check and cannot pass by absence. Read BD enrollment independently and preserve ACTIVE/PENDING_RESOLUTION/ABSENT/INACTIVE/UNAVAILABLE as a technical axis. No new provider egress or roster mutation is in this project.

### 3.5 Dated account observations and correction ledger — S05

Join reconciled membership to the existing b00 `canonical_valuation` record for exactly the relevant valuation date. Require uniqueness, full identity, boundary version, source provenance and a finite canonical `net_mv_plus_cash` value. Preserve cents with decimal arithmetic. Retain the canonical basis for cash, short positions and margin; the result is capital, not gross holdings, tax lots, leverage-multiplied AUM or the workbook's sales estimate. Carry the accrual limitation explicitly. A legitimate zero is KNOWN_ZERO only when the matching source actually reports it and all completeness conditions hold.

Emit protected `taxsma_assets` parquet with the data contract's history fields, including explicit unavailable rows for unresolved expected claims. The producer derives its source basis independently as ADDITIVE and validates it against the category registry. A mismatch refuses the contribution. `covered_accounts` counts only rows satisfying identity, effective membership, source date and value validation; the expected count is computed before those filters. A confirmed subtotal may exist for explanation but cannot populate `complete_value` while any expected claim remains unresolved. Unknown denominator is a separate state, never `0 of 0` success.

UTC **knowledge_date** keys the immutable daily object; **valuation_date** is a row field. Stable observation IDs depend on source versions, full key, effective-membership evidence and basis, not a run UUID. Conditional object creation makes retry/replay idempotent. If the object already exists, identical knowledge is NO_CHANGE; changed knowledge enters protected pending control state for the next daily partition. The normal production writer uses the daily slot; on-demand tests use isolated local artifacts, and operator retries cannot mint an extra same-date production leaf. Missed scheduling is recorded as delay, never concealed by a false date.

Corrections carry `supersedes_observation_id`. Readers resolve an acyclic chain per account/valuation date across the complete retained history and select the latest knowledge. Reject competing corrections, duplicate IDs with different payloads and missing superseded observations. An empty correction partition is not an empty cohort. Past values can be restated as newly known history without overwriting any old object; the view carries both dates. Pending corrections are visible before the next partition through status control, without supplying alternate numerical values.

### 3.6 Firm, Global and category contribution — S06/S07

The existing key is `tax`; preserve Tax-Managed SMA beneath SMA / ALT Strategies. Add an explicit Tax contribution to the existing firm aggregation and carry `source_basis` through every reconstructed entry, including the Global fixed-key/reconstruction path. The base amount must be declared to exclude Tax; the result is `firm_total = base_excluding_tax + complete_tax` once. Existing Client residual is unchanged. Do not subtract Tax from Client and then add it back. Apply the same no-double-count discipline at each parent. Global sums completed firm totals once and presents its Tax leaf as the sum of firm Tax leaves; it does not add Tax again on top of those totals.

The S06-to-S07 interface closes the current double-add hazard explicitly: for changed 49financial/Global series, add `aggregate_basis=INCLUDES_ADDITIVE`, `base_excluding_tax_aua`, `tax_additive_aua` and `tax_coverage`, each aligned to `dates`. `opal_aggregate_aua` is then the complete base-plus-Tax figure (or null with coverage); `by_model.tax.model_value` supplies the Tax breakdown with `source_basis=ADDITIVE`. S07 consumes the declared inclusive aggregate and **does not add `sma_additive_aum` again**. `non_model_aua` and Client carve-out inputs are unchanged. Global's base is the sum of each firm's base (unaffected firms use their original complete total) and its Tax is the sum of firm Tax; derive its inclusive aggregate once from those two. Absence of the new aggregate-basis declaration on an expected TAXSMA path is a schema failure, not fallback to the old addition rule. This changes the existing shaping contract deliberately and owes same-vintage before/after arithmetic controls.

Unknown/stale Tax propagates to the completeness status of SMA, ALT Strategies, 49 Financial and the dependent Global totals. Preserve unaffected Client and other-firm figures with their own correct dates. If some contributions are known, a separately labelled confirmed subtotal is permissible; it is not the complete total and must not populate a field the existing reader treats as complete. A last complete historical value may be shown with its original valuation date and stale status. Never use a missing scalar's current default zero or a positive parent to hide the unknown Tax leaf. Source code at consolidator `1465fd3f7dba7dedbb2e566ffd13917b55778ec9` locates `_last` at 621-643 and the withhold logic at 646-660; these exact behaviors, not their names, are the regression targets.

Store the aggregate count/date/status fields defined in the contract alongside numerical results and preserve them through category shaping. All aggregate families changed by this contribution must agree on the same generation and basis. The producer/publisher artifact-type-scope declaration is the denominator; validation cannot scope itself to whichever files happened to appear. No new taxonomy, performance series or trading UI is introduced.

### 3.7 Sole publication and truthful consumer — S08-S11

Keep publication in `opal-assets-mdpf-portal-publisher`. Numerical values come only from the canonical Gold parquet; the publisher may use the protected status/control record to mark an outstanding correction, expired source identity or failed run. That status record never supplies a value or reduces membership. A status-only change must update the existing served document even when numerical source bytes are unchanged. Include the control-state version in publication idempotency. Before skipping an unchanged source, verify the destination exists, matches the expected content/generation and has the required metadata. Missing/corrupt destination is repaired through the same publisher and key. Source-pair presence alone does not establish cohort completeness.

The existing category URL remains `/api/general/mdpf/{firmId}/category-views.json`. Gold migration and firm-bucket route work remain CANON-owned; the historical Global path is preserved. Validate both 49financial and Global through the actual authorized consumer route and check an unauthorized control. No direct object URL is offered as a substitute for route authorization. The ordinary JSON contains dates, aggregate counts and reasons, with no full account numbers, names or protected evidence links.

Extend the existing document rather than invent another endpoint: add `taxsma_contract_version`, document-level `taxsma_coverage`, and `coverage` on each affected existing node/child. The registry's node IDs remain the keys. The existing `sums.gold_plane`, `sums.view_plane`, `sums.total_aua` and affected node/child `aum` fields become nullable where the corresponding complete value is unknown; preserve known unaffected amounts. No null is meaningful without its coverage record. The accessor validates the version and fields before returning a usable block. A stale last-complete amount is carried only as an explicitly labelled historical display value, never as a current complete sum. At rollout the new payload cannot be enabled on served production keys until the compatible consumer is available under the applicable promotion authorization; staged/local paired producer-consumer exercises proceed behind the freeze. Merely building the consumer does not make an old deployed reader safe for new nulls.

`portal/src/api/endpoints/aum.ts` gains the typed value/status/date contract, a category cache TTL no greater than five minutes, failure non-caching and an explicit refresh that bypasses both accessor and query caches. `CategoryViewTree.tsx` renders unknown/stale Tax visibly and distinguishes true zero, unknown denominator and known incomplete coverage. `ModelPortfolios.tsx` carries the same status to affected totals and displays actual valuation/knowledge/acquisition dates; do not fabricate a 5 p.m. timestamp from a date-only field. Missing transport or schema fields yield an explicit unavailable display. Preserve unrelated presence rules and the L1 zero amendment. Build and exercise these changes in the consumer owner's coordinated branch behind the freeze; no production promotion is implied.

### 3.8 Execution, packaging, access and recovery — S12-S15

Add the bounded Tax acquisition/reconciliation/valuation prelude to the existing Gold handler before its 49financial/Global shaping. The 13:30 UTC floor runs every calendar day. Use observed success/failure records to gate the subsequent stage; a 13:50 publisher tick is not proof that the predecessor finished. On a Tax failure, retain honest Tax/dependent-total status while preserving unrelated firms' eligible outputs; do not abort their whole pipeline merely because Tax authentication failed. Use the canonical exchange calendar to choose the expected completed session. Weekend/holiday knowledge updates still process corrections; they do not create a new trading date. Missing calendar support fails closed, never silently uses weekday subtraction.

Use the existing package builders with exact source pins and per-member hashes. Include every new module and the contract data as declared package inputs; validate both Gold and publisher import closure with their deployed Python/layer combination. Register any Gateway bundle change through `EC2_MANIFEST.json` and its canonical S3-to-SSM deployment path. Gateway source existence is checked on the instance before a build is cut: the 07:31:52Z token census read 43 deployed Python files and found no literal `taxsma-workbook`; it is a bounded existence check, not proof that no dynamically generated capability exists. The next worker reads the actual route registration before adding one. If the intended capability already exists in usable form, the row becomes verification/reuse rather than duplicate authoring.

Runtime access is explicit: the Gateway's existing token broker remains the only delegated-token holder; the job receives only its content-specific capability bearer and the declared data permissions. Generate new resource/address names through LGIC builders, satisfy the firm deny fence without a catch-all exemption, and permit only the required source reads, conditional output writes and status operations. Compiler IAM uncertainty is carried to exact-ARN applied simulation and exercised allowed/denied controls; it is not permission to guess a grant. No console credential is copied into a Lambda, config file or evidence artifact.

Recovery uses the same producer and publisher, with source/output hashes, last good snapshot, pending-correction queue and exact run receipt. `S15` documents the operator commands and decision path: inspect the latest receipt and dates; fix the source/auth/disposition through its owner; run the bounded controlled/retry mode; check output identity, cohort and served readback; stop when the measured failure recurs rather than creating a new path. No new alarm, watcher, email or standing comparator is commissioned. Readers and moments are specified in the contract: Tax prelude and publisher on every run, the existing daily MDPF operator/COO check, the page on load/refresh, and Gateway access/incident review. Failure records have these consumers, not an unnamed audience.

Reversal disables the Tax prelude/capability and restores the pinned prior packages and consumer code through their normal paths. Preserve immutable observations and audit history. While reversed, show Tax/dependent totals as unavailable or clearly dated historical values; never silently return to a complete-looking zero. Verify unchanged non-Tax outputs and no additional writer. Source-code rollback alone is not proof that the current served data was repaired.

### 3.9 Concrete unattended-content activation prerequisite — S16

Before activation, Andrew names one Opal person who already has access to this workbook and explicitly authorizes the Gateway to use that person's delegated token for the unattended read described in §3.2. The configuration has no default person. The permission covers internally reading the one named Sheet1 used range and emitting only Index, Account Number, Strategy, Ready, Inception Date, Last Trade Date and minimal row/version metadata. It does not cover other workbooks, mail, Teams, writes or delegated-token export. Revocation disables the capability and yields AUTH_REQUIRED/stale; it does not replace the identity with another person's token. The capability secret is separately revocable and accepted on this route only.

This is an activation input, not an unresolved design selection for COO. The endpoint bars and this PRD's development/review can proceed without establishing a production credential. Use synthetic Gateway responses for the controlled harness until the named authorization exists. Record the exact approval reference in protected configuration/deploy evidence when supplied. The reusable pattern is “Gateway-held delegated identity behind one content-specific capability”; later IRPT_BCKEND mailbox intake is a separate authorization and project.

## 4. Acceptance properties and deliberate exercises

Every property below is judged against the approved FWD bar, with proof at the actual tested source/package/consumer vintage. A mechanism reaching a function is insufficient: when a condition gates a result, the same harness must show what differs with that condition engaged and disengaged. Census properties state their expected ID set and count. No exercise waits for a real outage or future market event. A local test is labelled local; it cannot certify a live deployment.

| Property | Outcome | Controlled exercise and required observable result |
|---|---|---|
| A01 business membership | FWD-1 | Full-sheet fixture contains traded, funded-but-untraded, unopened prospect, blank and conflicting rows. Operator explains every row. Flipping only Traded from No to Yes changes the expected claim, not merely a label; funding alone does not. Reordering/inserting rows does not lose an account. |
| A02 exact reconciliation | FWD-2 | Full identities match in both directions; suffix-only/masked/duplicate/malformed/master/strategy/transfer cases remain unresolved. Additional custodian candidates stay outside live membership. Same fixture with the mismatch corrected changes the corresponding coverage result. No private IDs appear in consumer/log outputs. |
| A03 activation and dated correction | FWD-3 | New traded row outside the original used extent enters expected membership automatically, acquires exact source/effective-date evidence and contributes once. A later status/identity/transfer correction preserves both old and corrected observations and changes only the appropriate dated contribution. Missing effective evidence remains visible until supplied. |
| A04 canonical value | FWD-4 | Synthetic and authorized dated-source cases include cash, long/short exposure, margin and actual zero. Result equals the existing canonical net-value basis to the cent, with source/date/boundary trace. Gross exposure, sales estimate, quarterly data and unverified accrual cannot replace it. |
| A05 honest incompleteness | FWD-5 | Remove one expected account, deny workbook access, stale a source, omit overlap evidence and break the calendar in separate controlled arms. Each has its own reason/status and prevents a complete Tax/dependent total. Unknown denominator, partial, stale, unavailable and true zero remain distinguishable through the rendered page. Restoring the exact input restores completeness. |
| A06 additive arithmetic | FWD-6 | Fixed synthetic baseline and known Tax cents yield exactly one addition in Tax, SMA, ALT Strategies, 49financial and Global; Client and other firms stay unchanged. A deliberate overlapping full ID or basis disagreement blocks the total. Replaying and reconstructing Global retains `tax`/`source_basis` without a second addition. |
| A07 protected traceability | FWD-7 | Authorized operator follows a result via protected snapshot, membership/disposition, full-key source join, observation and publisher receipt. Ordinary JSON/page/logs contain no names, full IDs, row values or tokens. Wrong route, wrong method, wrong bearer, other workbook and revoked identity controls fail; the authorized exact-route control succeeds and is audited. |
| A08 repeat/recovery | FWD-8 | Duplicate invocation cannot duplicate an observation or total. Corrupt/delete a local served artifact with unchanged source hash: the same publisher repairs it. Inject a mid-run failure and pending same-day correction; recovery preserves immutable history, dates and one writer. Disable/restore the extension and verify the affected display plus unchanged non-Tax results. |

S14 produces an expected-case manifest containing every A01-A08 arm and its fixture/input/output hashes, along with proof receipts and `comp-adversary` context. A reviewer independently compares expected case IDs to actual results before reading any overall PASS. Controls bind to the current aggregation code; changing that code makes old control results stale until rerun. Receipts enumerate every acted-on bundle member, data family and served family, including failure limbs; receipt domain must cover gate domain. A claimed complete user journey includes authorized route and rendered consumer readback in the stated environment.

## 5. Compiler Evidence

### 5.1 Required union and limits

Surfaces: Gold script, Portal component, Lambda, EC2 service, new artifact and cross-firm Portal. The corresponding protocol union was run during research/certification and the supplemental L4 pass. `compiler-evidence.md` and context declarations in the certified run retain the original commands, denominators and blind spots. The supplemental evidence is in `AUTHORING_CHECKS.md` beside this PRD; it is not retroactively added to the certified 18-file packet. Supplemental source/declaration findings do not become runtime expected values. The retired global compiler log is not appended.

### 5.2 Evidence and design effect

| Tool / exact subject | Key result and scope | Disposition |
|---|---|---|
| `comp-build` | Research build: 2,364 nodes / 3,053 edges; 1,992/1,992 source SHAs. | Source graph vintage recorded; later implementation rebuilds if its inputs change. |
| `comp-dataflow b00_canonical_valuation.py`; `comp-pipescript io b00_canonical_valuation.py` | Zero extracted reads / not in graph; similarly named B_00 holdings suggestion is a different engine. | Changed §3.5: exact source and live canonical object identify the reused engine; no absence claim. |
| `comp-pipescript io mdpf_gold_consolidator.py`; aggregate spine I/O | Dynamic prefixes and writes are partially unextracted; manual source reads name real emit/reconstruction paths. | Changed §3.6: separate firm/Global propagation and producer declaration coverage. |
| `comp-blast _shape_category_views` | Function absent from extracted graph. | Boundary, not zero impact; source callsites identify firm and Global shaping. |
| `comp-platinum reverse aum-metrics.json`; `comp-platinum reverse taxsma_assets` | First resolves an unrelated advisor route; second matches 0/57 indexed payload fields and no known producer. | New observation producer S05 is explicit; neither result proves estate absence or MDPF lineage. |
| `comp-routes trace /api/general/mdpf/49financial/category-views.json` and corresponding `global` path | DESIRED: `/api/general/*`, S3 portal-v2 origin, auth-validator-edge/public-data-router/cache-control-injector, rewrite to `platinum/mdpf/<scope>/category-views.json`. | Confirms actual `.json` route subjects for §3.7; applied edge pin and authorization remain required at exercise. |
| `comp-cache collisions` | 634/634 files, 119/119 useQuery calls, 0 unparseable, 17 shared keys, 0 type mismatches. Other hook families/TTL behavior not covered. | Accessor and query cache interaction gets its own S09/S14 proof. |
| `comp-transform schema-check ModelPortfolios` | Category type resolution warning. | Not a schema PASS; explicit contract/type/render tests required. |
| `comp-iam service opal-gateway` | DESIRED: 3 operations all UNRESOLVABLE-RESOURCE. Parser scans 473 TF files/3 trees; 27 unattached policies and 2 unparsed deny overlays limit the answer. | S13 requires actual scoped grants and exercised boundaries; no assumed permission. |
| `comp-iam service mdpf-gold-lambda` | Resolved the role view with 11 statements, not a complete handler-operation census. Existing paths include legacy Gold and 0824 reads. | New 0833/canonical/contract/control accesses require explicit role review, not a claim that existing grant is sufficient. |
| `comp-iam service opal-assets-mdpf-portal-publisher` | 7 calls: 6 unresolvable, 1 GetObject granted-action/ungranted-resource for portal-v2 latest pointer in desired source. | S08/S13 include exact source and destination readback permissions; no unrelated broad IAM cleanup. |
| `python .tools/check-lambda-layer-deps --function mdpf-gold-lambda` and publisher equivalent | Each audited 1 function: 0 FAIL, 1 OK. | Existing declared layer closure only; new package import closure still required at its pin. |
| `EC2_MANIFEST.json` exact Gateway row + read-only SSM command `c8fbe036-1c5a-4073-947c-b8fb5eeb7740` | Manifest maps Gateway to `i-07dccb1615503ac99` / `/opt/opal-gateway`; live Name/state matched. On-box source token census succeeded over 43 Python files, no literal workbook-specific route; general workbook reader found. | §6 deployed-app existence form satisfied within stated token-census boundary. S01 confirms actual registrations before new code. |
| `comp-estate taxsma` / MDPF Lambda | No matching chain in the historical 135-chain view. | No claim of AWS absence; live primitives and exact source pins supply the actual referents. |
| strict-identity source probes and crossreview | 6 original / 7 crossreview synthetic cases; existing normalizer accepts short numeric suffixes contrary to whole-ID intent. | New identity contract refuses them at S04 without rewriting unrelated BD enrollment. |
| `comp-adversary compose` declarations; canonical `ssot_validate` | Two bounded validation contexts; 24 expected cells; certified consumable validates. | PRD ground truth is documentary and exclusions remain explicit; future implementation validation gets its own context. |

### 5.3 Findings that changed the design

The workbook denominator replaces the stale five-account technical roster. Six-of-eight source coverage prevents a complete total. The independent source-basis and fixed Global reconstruction gaps require S06/S07 rather than registry-only work. Hidden null leaves, accessor caching and publisher source-hash skipping require S08-S11 rather than upload-only completion. The Gateway content permission and naming-contract disagreement are explicit owner interfaces; neither is silently inferred from an existing service name.

## 6. Rulings, limits and worker mandate

The L1/L2 commission, eight accepted bars and contract-owner dispositions bind this PRD. No second endpoint approval is required. D9 account opening, margin approval, money-manager changes, trading, Yang converter changes, strategy changes and access grants remain out of scope. No new provider egress, taxonomy, return calculation, competing valuation formula, shadow publisher, new monitor, shared-branch push or portal promotion is authorized by this PRD.

Worker subagents hold **no cloud identity of their own**; they inherit the box's ambient credentials. Andrew accepted that posture for now with “recs approved,” recorded in `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260905_133xZ_RECS_APPROVED_BRIEF_TO_CUT_BRIEF_COMMISSIONED_WORKER_AMBIENT_CREDS_ACCEPTED.md@8e89f1127f`. This project expects canonical COO-seated workers and therefore carries the ruling. It opens no IAM act and does not widen a worker's authorized cloud surface. Runtime service grants remain separately scoped and tested.

The following mandate travels with each corresponding surface when COO cuts work. It is not a task order or permission for this author to issue one.

<compiler_tools_mandate>
Phase 1 — BEFORE WRITING: run bare comp-which for the surface question, then its routed bare compiler. Reuse the pinned §5 evidence when unchanged; rebuild when graph inputs changed. For every proposed file inspect exact path/history; for Gateway code inspect the deployed app through read-only SSM and actual route registration. Existing usable capability collapses authoring to verify/reuse. Gold: comp-pipescript io of the exact producer, comp-blast of each changed function and comp-platinum reverse of the exact artifact; manually reconcile printed dynamic gaps. Portal: both actual .json route traces, comp-cache collisions and comp-transform schema-check; check consumer-owner branch coordination. Lambda/EC2: comp-iam service, manifest, package/layer and actual access surfaces. Stop on a conflicting current owner contract; never invent a bucket, source value or grant.
Phase 2 — BEFORE COMMITTING: rerun only lenses affected by the delta; validate contract shape, expected surface/case IDs and source/consumer fields. Run same-input control-on/control-off outcome tests for gates, full-key cohort and overlap tests, decimal/basis/Global arithmetic, history/replay, status propagation and privacy tests. Check exact package-member/import closure, allowed/denied IAM/capability cases and actual target referents. Receipts cover the complete acted-on union. No cloud mutation or external send is part of a compiler read.
Phase 3 — AFTER COMMITTING: bind every proof to commit/package/input hashes and rerun controls made stale by that commit. For an authorized deploy, verify applied package/config identity, run the prescribed controlled path, follow any changed converter through its complete output-to-consumer chain, and read the final artifact/page. Deploy time is not data freshness. Compose comp-adversary context for returned-work validation; independently compare the expected case set before interpreting PASS. Report blind spots, current holds and LOCAL push state. Do not broaden a failed criterion to rescue it; return a pinned refusal to COO.
</compiler_tools_mandate>

## 7. SURFACE MANIFEST (step 4 -> step 5)

`claim` describes the address/capability evidence, not completion. Proposed homes are **unmeasured**, never “absent” on a graph miss. D01-D08 are the relies-on IDs defined in §3.1/component manifest; all S dependencies below are keyed to observed completion, not merely a calendar. Engineering rows are served by workers on the laptop fabric under COO issuance; lane names below identify the standing surface owner. S16 is the distinct sovereign actor required before activation, with its exact act already specified in §3.9.

| id | outcome_ref | surface | claim | MEASURED-BY / evidence | lane | verb | depends_on | accept | bound |
|---|---|---|---|---|---|---|---|---|---|
| S01 | FWD-7 | NEW -> `infra/aws/ec2/opal-gateway/app/taxsma_workbook.py` | unmeasured | CTO ~A: bounded on-box census 43 Python files, no literal route; D07 pattern | Gateway | wire | D01,D07 | A07 | One exact content capability; existing structure-only/MCP/OTP routes preserved; no production activation before S16 |
| S02 | FWD-1,FWD-3,FWD-5 | NEW -> `data/mdpf/scripts/gold/taxsma_snapshot.py` | unmeasured | certified S1/S7 identifies source and gap; new producer declared | MDPF data | wire | S01,D01 | A01,A03,A05 | Whole Sheet1, no hardcoded population, no copied delegated token; source failure never empty membership |
| S03 | FWD-1,FWD-3 | NEW -> `data/mdpf/scripts/gold/taxsma_membership.py` | unmeasured | certified S1/S3/S8 plus normative data contract | MDPF data | classify | S02,D04 | A01,A03 | Preserve effective history; no workbook/trading/BD-roster mutation |
| S04 | FWD-2,FWD-6 | NEW -> `data/mdpf/scripts/gold/taxsma_reconcile.py` | unmeasured | certified S2 source joins and identity probe; 8 claims/6 dated matches | MDPF data | classify | S03,D02,D04 | A02,A06 | Full IDs only; master roles separate; unresolved denominator and two-sided candidates preserved |
| S05 | FWD-4,FWD-5 | NEW -> `data/mdpf/scripts/gold/taxsma_assets.py` | unmeasured | certified S4 existing canonical basis; reverse query 0/57 is not absence | MDPF data | wire | S04,D03,D05 | A04,A05,A08 | Reuse b00; immutable knowledge-date parquet; no partial-as-complete or alternate value basis |
| S06 | FWD-6 | `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` | measured | certified S5 and source pin `73c2dea263aa31a5b8906e2685902061d1a34d78` | MDPF data | align | S05,D05 | A06 | Preserve Client/other firms; independent source_basis; Global exactly once |
| S07 | FWD-5,FWD-6 | `data/mdpf/scripts/gold/mdpf_gold_consolidator.py` | measured | certified S5/S7; dynamic I/O limits in §5 | MDPF Gold | align | S06,D06 | A05,A06 | Prelude failure/status explicit; registry vocabulary preserved; unrelated outputs preserved |
| S08 | FWD-5,FWD-8 | `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/lambda_function.py` | measured | certified S6; supplemental IAM 7-call floor | MDPF publisher | align | S07,D05,D06 | A05,A08 | Sole publisher; numerical values only from Gold; status-only control allowed; destination readback |
| S09 | FWD-5 | `portal/src/api/endpoints/aum.ts` | measured | certified S6; actual .json routes and cache-collision bounds | D1_CATVIEWS | align | S08,D08 | A05 | Typed dates/counts/status; explicit refresh crosses both caches; caller URLs unchanged |
| S10 | FWD-5,FWD-7 | `portal/src/components/CategoryViewTree.tsx` | measured | certified S6 pinned consumer read | D1_CATVIEWS | align | S09,D08 | A05,A07 | Visible unknown/stale Tax; preserve taxonomy, L1 amendment and true-zero rules; no PII |
| S11 | FWD-5,FWD-6 | `portal/src/pages/ModelPortfolios.tsx` | measured | certified S6; schema-check limitation disclosed | D1_CATVIEWS | align | S10,D08 | A05,A06 | Honest affected totals/dates; no invented time; build behind freeze |
| S12 | FWD-8 | `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/build_package.py` | measured | certified S7 package declarations; current Gold layer check OK | CloudOps Gold packaging | align | S07,D06 | A08 | Exact member hashes and contract bundle; existing Gold schedule only |
| S13 | FWD-7 | `infra/aws/terraform/mdpf-pipeline/iam.tf` | measured | §5 desired IAM findings, never applied grant proof | CloudOps access | align | S12,S17,S18,D05,D07 | A07 | Exact declared runtime access matrix, firm fence and never-widen proofs; no broad exemption or delegated-token export |
| S14 | FWD-1,FWD-2,FWD-3,FWD-4,FWD-5,FWD-6,FWD-7,FWD-8 | NEW -> `data/mdpf/tests/taxsma/test_taxsma_journey.py` | unmeasured | normative A01-A08 expected arm set; source run not runtime proof | MDPF verification | verify | S05,S08,S11,S12,S13,S17,S18 | A01-A08 | Local controlled data unless separately authorized; no live trade, send or production write; current-vintage paired controls |
| S15 | FWD-8 | NEW -> `org/missions/D8/MDPF/MDPF_TAXSMA/operations/RECOVERY.md` | unmeasured | normative contract readers/moments; certified S7 gap | MDPF operations | wire | S14,D06 | A08 | Existing daily operator check, explicit retry/reversal; no new monitor; preserve historical data |
| S16 | FWD-7 | NEW -> protected `TAXSMA_WORKBOOK_IDENTITY` activation record | held | CTO 96946 requires named-person word; none supplied for this capability | Andrew | classify | S01,S14 | A07 | Exact one-person content authorization before activation only; no default or substitution; engineering/review proceeds |
| S17 | FWD-8 | `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/build_package.py` | measured | exact build source named in compiler search; publisher layer check 1/1 OK | CloudOps publisher packaging | align | S08,D06 | A08 | Exact publisher members/declaration; no extra publisher or changed Global path |
| S18 | FWD-7 | `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` | measured | manifest exact registered deploy script and live instance source census | Gateway packaging | align | S01,D07 | A07 | Canonical S3-to-SSM package and manifest; capability remains disabled pending S16 |

MECE authoring check: forward **18/18** OWNS IDs have a row; reverse **16/16** non-verify/non-sovereign engineering work rows map to OWNS (S01-S13,S15,S17,S18), with S14 verification and S16 activation separately counted; outcomes **8/8** have at least one owned surface. The component manifest expands package/config companions without treating each file as another independent engine. COO decomposes multi-file access effects to one actor/act per cell and preserves the existing owner boundaries; it cannot use S13 as a grant for unnamed files.

## 8. Brief coverage — content carried, not just cited

The pinned brief has **9 top-level headings** and **8 nested outcome headings**. All 17 are enumerated here, including explicitly non-outcome status context. This map's denominator is the brief at `8e8afed454961bebb2a3d90a43522787e19ec9e4`, not a reconstructed outline.

| Brief heading | Carried content | Consuming sections / cells |
|---|---|---|
| Commission and precedence | Direct D8/laptop placement, real workbook research before writing, traded-versus-prospect correction, additive authority, D9 separation and historical-input precedence | CONTRACTS; §1-3; S01-S18 |
| I. Outcome territory | Entire eight-outcome movement from business status to defensible final assets and repeatable recovery | approved ENDPOINT; §1; A01-A08 |
| I.O1 | Expected traded population distinct from prospect/open/funded/Ready/strategy labels; no daily-trade requirement; accountable exclusions/conflicts | §3.2-3.3; S02/S03; A01 |
| I.O2 | Full-ID two-sided workbook/0833 join; malformed/masked/duplicate/master/strategy/transfer exceptions; onboarding/reporting masters distinct | §3.4; S04; A02 |
| I.O3 | Automatic new activation, effective dates, correction/deactivation/transfer history, expected denominator and technical-resolution separation | §3.3-3.5; S02-S05; A03 |
| I.O4 | Existing canonical net value, cents, cash/short/margin and accrual limitation; no sales/gross/lot/leverage/quarterly substitutes | §3.5; S05; A04 |
| I.O5 | Complete/partial/unknown/stale/zero distinction, no source-failure denominator shrink, original historical dates, exchange calendar and expected daily arrival | §3.5-3.8; S05/S07-S11; A05 |
| I.O6 | Existing tax/SMA/ALT hierarchy, exact-once firm and Global addition, unchanged Client/other firms, independent source_basis and live dated overlap guard | §3.4/3.6; S04/S06/S07; A06 |
| I.O7 | Authorized full provenance, exclusions and exceptions; aggregate consumer dates/counts without names/full IDs/private onboarding data | §3.2/3.7/3.9; S01/S08-S11/S13; A07 |
| I.O8 | Supported daily owner/receipt, controlled activation/correction/failure/delay, replay without duplicates, deliberate recovery and reversal | §3.8; S12-S15; A08 |
| II. Boundaries | D8 ingestion/identity/date/value/coverage/Gold/operation; D9 opening/margin/master/trades/converter/access excluded; BD not mandatory daily dependency; taxonomy reused; no automatic workbook edit | §3.1/3.4; CONTRACTS; §6; every row's bound |
| III. Qualitative completion bar | Operator follows one controlled case to full result, explains all others; funded-untraded excluded; missing traded visible; repeatable bad-to-good difference without collateral change | §1-2; §4; S14/S15 |
| IV. Measured prior art and gaps | Current 20-slot/8-traded versus technical five-entry roster, 6/8 dated source coverage, untraded funded counterexample, strategy disagreements, canonical basis, SOP/converter/old-mask limits | §2 certified eight surfaces; §3.3-3.6; S02-S07 |
| V. Dependencies, without sequencing instructions | Workbook owners/access, dated feeds/canonical boundary, registry/consolidator, supported execution; missing cases need actual evidence rather than invented repairs | CONTRACTS; D01-D08; §3.1/3.3/3.8 |
| VI. Status context — NOT OUTCOME-BEARING | Historical no-implementation state and then-proposed registration retained as vintage; current project is registered and evidence certified; no delivery inferred | §2; §9; no added FWD |
| VII. Limitations and closure required in the PRD | Bounded tenant search, masked-history limit, latest-at-read not lateness, unknown missing causes, all schema/lifecycle/identity/basis/calendar/privacy/delivery/recovery choices concretized | §2; CONTRACTS; data contract; §3.2-3.9; A01-A08 |
| References | Original additive input/ruling, committed research/manifest, forward/flow/spine provenance preserved | preamble; CONTRACTS; §2/5/9 |

## 9. Handoff and completion boundary

Package for L4-R: this PRD, the normative data contract, this PRD's `component_manifest.yaml`, `AUTHORING_CHECKS.md`, the pinned L1/L2 carriers, `GOVERNING_CONTRACTS.md` including final naming disposition, and the certified run/consumable/certificate identified in §2. CVO signs ENDPOINT + CONTRACTS; CRO (or a permitted independent COO substitute) signs the brief half. The author never signs either half. `python .tools/prd-signoff.py status MDPF_TAXSMA` must read ADMITTED before the notifier releases the package to the project's COO for L5 decomposition.

No project runtime has been implemented or deployed by this PRD. The eight approved bars remain to be exercised. The unattended named-person activation record is explicit and separate from engineering approval. Frontend changes can be built and committed behind the freeze; promotion/push/gitlink holds remain. The contemporaneous Cottonwood cents hotfix and its future scheduled readback belong to their existing ledger, not to completion of this project.
