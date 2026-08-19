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
| 7 | Opal Ticketing | P0 shipped; MS-integration half remains | queued; dated TO post-Wave-1 | laptop |
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

## S9. OPEN -- AMBIGUITY QUESTIONS TO ANDREW (block only their own items)

- **Q1: ANSWERED** (folded into S3 -- hierarchy pinned, MDPF-only home for now, advisory_scope
  prior art composes, Cottonwood tie-in + Client Advised/Residual split).
- **Q2: ANSWERED** (folded into S6 -- all-viewers persistence, server-side store).
- **SLOTS:** transcript 2 -- (pending) · transcript 3 -- (pending) · partner GraphQL spec file --
  (pending) · Mike-call outputs -- (pending) · BD householding-template sample (egress word) --
  (pending Andrew).

## S10. COMPILATION PATH (deferred by design)

Later act per Andrew: fold this document into the /missions compiled state (comp-missions /
org/tier0/missions.yaml). NOT done in v0 -- missions surgery is a taxonomy act with its own gate;
this file is the persistence home until then.
