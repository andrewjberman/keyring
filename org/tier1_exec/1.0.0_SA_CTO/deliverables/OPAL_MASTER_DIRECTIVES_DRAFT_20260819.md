# OPAL MASTER DIRECTIVES -- v0 DRAFT (CTO scribe, 2026-08-19 ~15:35Z)

**What this is:** the persistent home for Andrew's standing project directives -- the Teams-thread
item list + his transcript series (1 of 3 ingested) + the ratified sub-programs -- drafted per his
word: *"start drafting a master 'Opal Master Directives' document which will persist all of this
(later we can figure out how to incorporate this into a more 'compiled' state via the /missions
folder/function)."* Every directive carries its authority (transcript/verbatim/record). DRAFT
status until transcripts 2-3 land and the ambiguity questions (S9) are answered.

## S1. THE ITEM LIST (Andrew's Teams-thread frame, grounded 08-19)

| # | product | stand (grounded) | timeline (Andrew) | device |
|---|---|---|---|---|
| 0 | Infrastructure | healthy; tightening set executing (T1-T4) | ongoing | laptop |
| 1 | Model Portfolios -- OPAL ASSET-CATEGORY VIEWS (S3 below; NOT security naming) | new directive, needs taxonomy ratification then portal build | ~2 wks | laptop |
| 2 | Advisor Intelligence -- 49F E2E template | FRIDAY COMPRESSION live (push plan SS6); parity program SS7 | E2E Fri PM; parity census next wk | laptop |
| 3 | Account-Level Model Overlay (S4 below) | scope CONFIRMED; PRD to write now; pends 1+2 | ~6-7 wks | laptop |
| 4 | ETFS fold-in to Positioning | ETFS_CANON phase-0; CTO design-gate this week unsticks it | 3-8 wks, behind 1 | laptop |
| 5 | Alt Research Pipeline | phase 1 complete (28/28 ingested); interim = ingest | ongoing | laptop |
| 6 | Opal Analyst (+ partner GraphQL, S5) | runtime legs done (autologin, fallback); SharePoint+BBG builds + GraphQL = v0 gap | v0 in ~2 wks | SITEZ box legs + laptop cloud |
| 7 | Opal Ticketing (S8b) | P0 shipped; intake workflow DIRECTED -- **HIGH PRIORITY THIS WEEK** | this week (intake leg) | SITEZ intake + laptop portal/API |
| 8 | Philosophy Dashboard -- LIVE EDIT (S6) | B-1 ruled; edit-surface directive new | this week | laptop |

## S2. RATIFIED SUB-PROGRAMS OF RECORD (pointers, not restatements)

- **49F Friday spine + BD parity:** `ADVI_49F_END_TO_END_PUSH_PLAN_20260818.md` SS6+SS7 @762b06ca84
  (fam declared-stale decouple w/ CRO~A's measured cost basis; Wed/Thu/Fri to E2E-complete;
  account-level EXACT parity program vs Black Diamond's calculated outputs -- standing template
  feature inherited by INF/COT).
- **Tightening set:** `TIGHTENING_INCORPORATION_BRIEF_20260819.md` @094df1d132 (T1 broker
  primitives / T2 stamps-then-assertion / T3 vendor-clock DONE / T4 two-homes declarations).
- **Infra-graph program (CRO terminal, being interviewed):** verbatim
  @3033712139 -- definitions-first ladder, cost-ordered autonomy hierarchy
  (deterministic -> NLP -> AI -> user), endpoint = "spin up our entire Opal infrastructure for a
  new partner." Overlaps the held W-06/S0-S5 spine; CRO carries; fold on its plan record.

## S3. DIRECTIVE: THE OPAL ASSET-CATEGORY VIEW TAXONOMY (transcript 1; Item 1's true content)

Andrew (voice memo, 08-19): the Model Portfolios GLOBAL VIEW gains an Opal-specific breakdown of
"what kind of asset we're looking over." **Top-level views: INSURANCE / CLIENT / ALTERNATIVES /
MODELS / SMAs.**
- **MODELS** is a CATEGORY larger than the five archetypal models: **primary** (ultra short /
  short / intermediate / long / ultra long term) + **custom** (e.g. Opal fixed income; the
  Cottonwood constituent models sitting under Black Diamond's rebalancing-page "strategies").
- **SMAs** = the strategies: Muni SMA, Tax SMA, the ETF strategies (PFOE SMA + DIVZ SMA -- both on
  49 Financial through SmartX).
- **CLIENT** = client advisory assets (advised / fee-earning) vs e.g. client residual.
**ANSWERED (Andrew, 08-19 ~15:5xZ):** hierarchy PINNED -- top level = Models / SMA / Alternatives /
Insurance / Client (peers); under Models: Primary + Custom (peers). **Client splits into Advised +
Residual, where Client->Residual is effectively today's "Non-Model."** Home: ENTIRELY in Model
Portfolios for now; the eventual ADVI home is downstream of the Item-3 overlay work. **Indelibly
tied to displaying Model Portfolios for COTTONWOOD correctly: ~$7M of Custom models + ~$30M of
Client assets we advise.**
**PRIOR ART (Andrew's pointer, located):** CRO's
`MDPF_PORTFOLIO_ONTOLOGY_AND_SLEEVE_ATTRIBUTION_SPEC_20260805.md` -- the three independent axes
`selection_origin` (opal/client/external_manager/unknown) / `advisory_scope` (advised/excluded/
null) / `fee_basis`. The view taxonomy COMPOSES from these ratified axes rather than minting a
parallel vocabulary: Client->Advised = advisory_scope=advised; Client->Residual = the
excluded/residual class; Models Primary/Custom rides selection_origin + model identity. Rule-24
declaration + the composition mapping are the CTO taxonomy gate's content; then category registry
-> MDPF global-view portal components. Owner-classes: CTO gate + DE build; COO decomposes;
Cottonwood display acceptance is part of DONE.

## S4. DIRECTIVE: ACCOUNT-LEVEL MODEL OVERLAY (Item 3, scope CONFIRMED)

Show clients in Advisor Intelligence WHAT MODELS THEY ARE INVESTED IN, at the **account** grain --
because account-grain resolution gives relationship / advisor / firm slices for free. "Very
important that we get it to the account level... that is what's going to allow us to create those
slices of various granularity." Pends Items 1+2; **PRD written NOW** (ground-truth-at-outset) so it
launches the day dependencies clear.

## S5. DIRECTIVE: PARTNER GRAPHQL -> FOLDS INTO OPAL_ANALYST

Confirmed: the Teams-based queryable-agent layer for clients folds into OPAL_ANALYST as its query
access layer. Andrew holds a spec file to be dropped -- slot open.

## S6. DIRECTIVE: LIVE-EDITABLE MODALS (Item 8 widened)

BOTH the Philosophy-page modal pop-ups AND the model modal pop-ups in the Benchmark tab of Model
Portfolios become **editable live by Opal employees**. **ANSWERED (Andrew, 08-19 ~15:5xZ):**
edits persist FOR ALL VIEWERS -> server-side store required. Audience: Opal employees (editor-set
granularity = implementation detail at the auth surface). Owner-class: DE + a small storage/auth
leg (AE); CTO gates the auth surface.

## S7. VENDOR/CONTACT FRAME (transcript 1)

Mike = the 49 Financial DATA contact (more info coming from him) -- **NOT the Schwab channel**.
FAM stoppage: urgency LOWERED on Andrew's stable-fields read; CRO~A tasked (his word) with the
field-semantics assessment; the SS6 decouple keeps the schedule independent; the contact-ready
Schwab line stays available, not clock-bearing.

## S8. DEVICE SPLIT + COORDINATION (standing)

Laptop fabric = all AWS/data/portal work (Items 0-5, 7, 8, parity, tightening). SITEZ fabric = the
Bloomberg-terminal box-resident legs of Item 6 (BBG pipe, box SharePoint) + its own velocity work.
**MSTR = sole sitez coordinator (standing law); MSTR seat currently DOWN -- respawn required
before any sitez issuance.** Cross-fabric kickoff is never implicit.

## S8b. DIRECTIVE: THE OPAL TICKETING SYSTEM -- INTAKE WORKFLOW (transcript 2; HIGH PRIORITY THIS WEEK)

**Andrew's workflow (voice memo 08-19):** client partners (49 Financial / Inflection WM /
Cottonwood CA) email their Outlook DISTRIBUTION GROUPS with requests (sensitivity analyses, ad-hoc
account questions). As emails hit the groups: pull deterministically via **Graph API** -> the
**Opal Analyst agent (the Bloomberg-box Teams concierge) manages the ticketing center** as a named
responsibility -- analyzes content, keeps LOGS/persistent memory, tracks
receipt -> acceptance -> execution timing -- and **"buzzes" a ticketing-center Teams thread** with
a structured, concise summary + a LINK -> the link opens the **portal ticket page, where the Opal
user ACCEPTS, moves in-progress, and marks COMPLETE**. Smooth + frictionless is the bar; "largely
deterministic"; "start putting water through the pipes."

**PRIOR ART (assessed, grounded):** the transcript RATIFIES-AND-SHARPENS the existing OPAL_TICKET
plan rather than replacing it. P0 SHIPPED 07-14: backend LIVE (opal-tickets + opal-ticket-api,
e2e lifecycle green incl. claim-race), portal /ticket-center LIVE on DEV (board/create/claim/
complete/metrics), CF auth chain independently exercise-verified. The prior plan's P1 (Teams claim
links -- ruled TEAMS-ONLY 07-14) and P2 (AI intake via a Teams shared channel, "pending
Andrew/team channel setup") are exactly what this directive now specifies concretely: intake
source = the client DLs; intake agent = Opal Analyst; the Teams channel = the ticketing-center
thread. The m365 gateway (NFRA_OPLMCP, build-complete) already carries the Graph surface
(read/search email, channel messages). Prior open human items resurface in S9.
**Device split:** intake watcher + analysis + Teams buzz = SITEZ (the Analyst's box -- newly
hardened by autologin + remote fallback); ticket API/portal/storage = laptop-cloud (live).
**Sequencing vs Friday:** disjoint seats from the 49F flip (no DE/DT/CVO dependency) -- the
intake leg can carry water this week without touching the critical path. MSTR respawn is the
sitez-coordination precondition (second reason now).

## S8c. DIRECTIVE: TAX SMA OPS -- CLOSE IT OUT, ASSESS-FIRST (transcript 3)

**Andrew (voice memo 08-19, archived at partner_calls/):** the Tax SMA process needs "a lot better
job... a lot of prior art in the repo... we need to close it out." Requirements: (1) sync with the
existing SHAREPOINT documentation from Yang + Alyssa; (2) TRACK THE ASSETS DAILY; (3) PARTITION
the assets somewhere CONSISTENT as it grows -- per his cover note, designed **within
opal-data-assets** and threaded into the whole pipeline process; (4) TAXONOMY: Tax SMA slots into
the **SMA category** of the S3 view taxonomy (and Client=Advised/Residual gets some semantic/
ad-hoc input from Andrew); (5) the assets ultimately roll into the **Model Portfolios page**;
(6) **ASSESS-FIRST, his exact sequencing:** "we need to know what we've done thus far in order to
have that meeting" -- a state assessment (workflow-as-designed, holes, remaining work) BEFORE
setting the Yang/Alyssa meeting.
**PRIOR ART (known):** OPAL_TAXSMA + OPAL_TAXSMA_PT2 + OPAL_TAXSMA_REGISTRY projects; the
/taxsma-step1 skill (PFMG_TAXSMA Short Sale intake) + tax-newacc/tax-pt1/2/3 skills; ⚠ the 08-04
memory row: a TAXSMA TO sat PENDING ~3wks at a DEAD seat (0.5.0_AE_OpalETL~A) -- the stall Andrew
is naming is real and already flagged; the assessment supersedes-or-seats it.
**Shape for the delegation pass:** one recon-class assessment deliverable (repo census + workflow
map + SharePoint-doc sync review + hole list) -> Andrew reviews -> Yang/Alyssa meeting -> then
the pipeline build TOs (opal-data-assets home, daily tracking, SMA-category wiring, MDPF page
roll-in). Laptop fabric; SharePoint leg may ride the m365 gateway.
**Adjacent recordings spotted in Downloads (NOT yet ingested, Andrew's call):** "Dashboard Update
and Tax SMA Reporting" .docx+.vtt pair -- looks like the ops-detail call for exactly this
assessment; plus two SMARTX_ADVISORY activity-ledger CSVs (WILLIAM_CHAN...) that look like Tax
SMA working files.

## S9. OPEN -- AMBIGUITY QUESTIONS TO ANDREW (block only their own items)

- **Q1: ANSWERED** (folded into S3 -- hierarchy pinned, MDPF-only home for now, advisory_scope
  prior art composes, Cottonwood tie-in + Client Advised/Residual split).
- **Q2: ANSWERED** (folded into S6 -- all-viewers persistence, server-side store).
- **Q3 (S8b ticketing):** the v1 distribution-group SET -- exact DL addresses (49F / Inflection WM /
  Cottonwood CA; others? internal groups?), and does a monitorable mailbox already sit in each
  group or do we add one for the Graph subscription?
- **Q4 (S8b):** v1 = INTERNAL-ONLY confirmed (clients keep emailing as today; client-facing
  visibility stays P3 per the prior ruling)?
- **Q5 (S8b, prior plan's open human items):** the 2PM-ET interim cutoff config (07-14) -- stands,
  or replaced by the AJ-agreement number? And the bobby@ address confirm (parked ~08) -- still
  relevant to the notification set?
- **Q6 (S8b):** Opal Analyst on the Bloomberg box as the intake manager = CONFIRMED as the decided
  placement (your transcript reasons to yes; binding ticketing intake to that box's uptime, which
  the autologin+fallback work just hardened)?
- **SLOTS:** transcript 2 -- INGESTED (S8b) · transcript 3 -- INGESTED (S8c Tax SMA) · partner GraphQL spec file --
  (pending) · Mike-call outputs -- (pending) · BD householding-template sample (egress word) --
  (pending Andrew).

## S10. THE DELEGATION BREAKOUT (Andrew ~17:35Z: "break out each item based on the original list
with tax added on as Item 9") -- the decomposition source for COO's unified wave

**ITEM 0 -- INFRASTRUCTURE (ongoing, laptop).** Workstreams: (a) T1 broker primitives -- CTO design
note -> 0.8.0-class build; (b) T2a stamps generalization + T2b stamp-assertion (stamps-first,
worded); (c) T4 two-homes declarations (0.8.0 respawn); (d) REG-SCAN-ATOMCHECK w/ REG-0 founding
fixture + J3 comp-atomcheck (08-20, REQUIRED before INF binds); (e) LD-0424 kill-instrument
self-exclusion fix; (f) GLDRNS wrapper disambiguation (08-25); (g) infra-graph program (CRO-led,
absorbs S0-S5; CTO S0-sequencing law binds).
**ITEM 1 -- MDPF ASSET-CATEGORY VIEWS (~2wks, laptop).** (a) CTO taxonomy gate: Rule-24 declaration
+ composition mapping onto advisory_scope/selection_origin (prior art S3); (b) category registry
artifact; (c) DE-class portal build on the MDPF global view; (d) Cottonwood display acceptance
(~$7M Custom + ~$30M Client Advised/Residual) = part of DONE. Independent of R and of Friday.
**ITEM 2 -- ADVI 49F E2E (Fri PM, laptop).** (a) DONE TODAY: floor ENABLED on the 107.1s pin
(@647c432a7d), corrected chain proven, IAM complete; (b) THU: first green 12:45Z (AE reads),
DS~B emit 15 twins + shell activation (CTO-gated), CVO pins + oracle table; (c) FRI: second green,
DE repoint -> DT PROD promote, rendered+behavioral acceptance = E2E COMPLETE; (d) parity program:
probe THU-FRI (DS-class + CRO), full census MON-TUE, drive-to-EXACT loop after (conventions
pre-registered rev-2: calendar-vs-trading-day basis, quarterly non-amortized fees, IDC pricing,
BD-vs-Schwab source deltas -- Mitch Johnson case); (e) then INF binds (after J3 + A3-green), COT
third. FAM heal = R-WATCH + the BD-sample probe (fires at AE's convenience, no clock).
**ITEM 3 -- ACCOUNT-LEVEL MODEL OVERLAY (pends 1+2; ~6-7wks, laptop).** (a) CTO writes the PRD NOW
(user story from the Mike call verbatim: "what models a given account is in... without having to
dig"); (b) precondition workstream startable EARLY: the SmartX<->BD/Schwab EXACT-JOIN spec (models
live in SmartX, not BD -- rev-2 fact); (c) build launches the day 1+2 clear.
**ITEM 4 -- ETFS FOLD-IN TO POSITIONING (3-8wks, behind Item 1, laptop).** (a) CTO rules the
ETFS_CANON design gate THIS WEEK (5 open items, DE-defaulted); (b) build sequences behind Item 1's
lane; ETFS strategies also appear as SMA-category members in Item 1's taxonomy -- one registry
serves both.
**ITEM 5 -- ALT RESEARCH (ongoing, laptop).** Continue ingest (CRO lane); build queue activates on
Andrew's prioritization word. No change.
**ITEM 6 -- OPAL ANALYST + PARTNER GRAPHQL (v0 ~2wks; SITEZ box legs + laptop cloud).** (a) SITEZ:
SharePoint access build + BBG pipe build (off the proven W7/W8 investigations) -- MSTR coordinates;
(b) laptop: the GraphQL query layer (SPEC FILE STILL PENDING from Andrew -- the one open input);
(c) the Analyst's ticketing duty (Item 7) lands as a named responsibility.
**ITEM 7 -- TICKETING INTAKE (THIS WEEK; SITEZ intake + laptop serve).** (a) Graph DL discovery ->
one-liner confirm with Andrew (addresses = the open input); (b) Graph subscription/poll leg
(m365 gateway, laptop); (c) Analyst-agent intake + analysis + Teams-thread buzz w/ portal link
(SITEZ); (d) portal accept/in-progress/complete already LIVE (P0); (e) SLA log
(receipt->acceptance->execution) in the agent's persistent memory; (f) cutoff 2PM-ET stands;
bobby@ later per Andrew.
**ITEM 8 -- PHILOSOPHY + BENCHMARK MODAL LIVE-EDIT (this week, laptop).** (a) server-side content
store (small AE leg); (b) edit surface on both modal families (DE-class); (c) CTO gates the auth
surface (Opal-employee scope). Days of work.
**ITEM 9 -- TAX SMA OPS (NEW; assess-first, laptop + m365).** (a) STATE ASSESSMENT deliverable
(recon-class): repo prior-art census (OPAL_TAXSMA/_PT2/_REGISTRY + skills + the stalled 08-04 TO
seat-or-supersede), workflow-as-designed map, SharePoint doc sync review (Yang+Alyssa), hole list;
(b) -> Andrew review -> Yang/Alyssa meeting; (c) -> pipeline build TOs: opal-data-assets home,
daily asset tracking, consistent partition scheme, SMA-category taxonomy wiring, MDPF-page
roll-in. Extra recordings pair + SMARTX CSVs pend Andrew's ingest word.

**RESPAWN/SEAT NEEDS (COO cuts, MSTR spawns):** THU AM latest -- DS~B (emit), CVO (pins), DE + DT
(Fri flip), 0.8.0 (REG/J3 + tightening), DS base (R-WATCH + dated items). SITEZ issuance (Items
6/7 legs) via MSTR now that they are ready-and-waiting. The BD-sample probe + parity P1 ride
existing live seats.
**WEEK SHAPE:** THU = first green + emit + pins + ticketing intake water + parity probe; FRI =
flip (E2E) + Item-8 edit surface + Item-4 design gate ruled; MON-TUE = parity census + Item-1
taxonomy gate + Item-9 assessment; behind = Item-3 PRD (now) + exact-join spec.

## S11. COMPILATION PATH (deferred by design)

Later act per Andrew: fold this document into the /missions compiled state (comp-missions /
org/tier0/missions.yaml). NOT done in v0 -- missions surgery is a taxonomy act with its own gate;
this file is the persistence home until then.
