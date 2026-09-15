# POSN_AGGFIX -- L1 BRIEF: the Positioning aggregate ("AGG") book, restored for Opal users only

**Author:** 4.0.0_SA_CRO~Z (site Z CRO lane) - **Step:** L1 of the canonical flow (Rule 27; CRO only)
**Date:** 2026-09-15 - **Mode:** NEW (greenfield project; nothing is built under this code)
**Consumer:** 1.0.0_SA_CTO~Z. L2 was cut on the plan itself (FWD-1..FWD-8 @d5e068cde4) before this brief landed,
so this brief now serves as the PRD header's admitted-shape `brief_ref` at L4 and carries its measurements there.
**Substance from:** 4.0.0_SA_CRO's draft plan
`org/tier1_exec/4.0.0_SA_CRO/deliverables/POSITIONING_AGG_OPAL_ONLY_RESTORE_PLAN_20260915.md`
(committed on CLOUD @2033ff3ea6; carried byte-identical onto SITEZ in this brief's commit, blob `0765b9af1f`).
Section references below written "plan s.N" point into that file.

---

## WHY THIS BRIEF EXISTS, AND WHAT IT DOES NOT CHANGE

**Andrew-direct ~16:2xZ 2026-09-15, at the 0.0.0_AB_MSTR terminal, relayed over the bus (id d7aa0f67) to
0.0.0_AB_MSTR~Z, relayed to this seat as msg 23157 and to 1.0.0_SA_CTO~Z as msg 23156. VERBATIM AND ENTIRE:**

> "Send this to sitez, it is a "Positioning" D4 project that their CTO~Z needs to /endpoint --forward
> org/tier1_exec/4.0.0_SA_CRO/deliverables/POSITIONING_AGG_OPAL_ONLY_RESTORE_PLAN_20260915.md. Currently CTO~Z is
> down so send this to MSTR~Z, tell them to spawn ~Z fabric to address this new project. I would call it
> POSN_AGGFIX"

1. **Andrew named the plan as the L2 input.** The plan calls itself "not a task order and not a brief" (its
   header). Rule 27 gives L1 to the CRO, and `/endpoint --forward` cuts outcomes only from citable,
   outcome-shaped sections. This brief is the plan re-cut into that shape. It adds no direction.
2. **It is not a gate, and it does not re-open L2.** 1.0.0_SA_CTO~Z forwarded on the plan, as Andrew named, and
   landed FWD-1..FWD-8 @d5e068cde4 while this brief was being measured. The map below shows the two agree.
3. **What it adds over the plan, all measured on site Z today:**
   - the plan's producer line numbers were taken at the CLOUD vintage and land on other code at SITEZ HEAD, so
     every citation is re-located here (Part IV, F3 and F6);
   - the canonical AUM file's $8.3M gap is present in the GOLD source too, and the legacy file tied to the cent
     (F4);
   - the claim that the AGG producer is the last reader of the legacy AUM key is checked with a denominator (F8);
   - Andrew's 2026-09-09 ruling is located and quoted, with its scope (F9).
4. **The plan's s.6 process question stays OPEN and stays Andrew's.** It asks whether he wants the 2026-08-24
   "just clean it up" exemption again. His ~16:2xZ word names the canonical route (L2) without answering it in
   those words, and 0.0.0_AB_MSTR~Z records that 0.0.0_AB_MSTR is asking him (msg 23165). If he grants the
   exemption, this brief is simply unused.
5. **The four decisions D1-D4 stay Andrew's** (plan s.6). The plan's recommendations are carried in Part V as
   recommendations, never as outcomes.

### How the outcomes below map onto the landed endpoint

| This brief | Endpoint @d5e068cde4 |
|---|---|
| O1 whole book on Positioning | FWD-1 |
| O2 per-model split | FWD-3 |
| O3 hidden from non-Opal viewers on screen | FWD-2 |
| O4 current mix, dated | FWD-4 and FWD-5 |
| O5 which models are covered; O6 total reconciles | FWD-6 |
| O7 data withheld (conditional on D3) | FWD-7 |
| Part III item 4, nothing else moves | FWD-8 |

Every endpoint outcome has a home here, and every outcome here has a FWD. **Three measured points bear on the
endpoint's wording at L4.** They are findings for 1.0.0_SA_CTO~Z to weigh, not gates:

1. **FWD-2 and FWD-7 exercise a CLIENT only, while their claim is "nobody outside Opal".** The portal names three
   viewer tiers, internal, advisor and client (the `model.json` docstring at origin/PROD: "Internal + Advisor tiers
   only", "blocks client tier", `portal-proxy.ts:1421`). So the non-Opal population is advisors plus clients, and
   an advisor arm is one more page open. It matters most for FWD-7: the precedent route plan s.5 Phase 3 follows
   refuses the client tier only, so an aggregate moved behind that pattern would still reach advisors. Advisors
   reading Opal's mix as their own is the exact 2026-08-24 concern (F9).
2. **FWD-6's "explained" branch depends on a seat outside this project.** The gap is already in the gold source
   (F4), whose producer this project relies on and does not own (II.2 item 1). Its "disclosed" branch does not.
3. **FWD-4's "Phase 1 alone" branch also re-opens the premise of Andrew's 2026-09-09 ruling 5** (F9; Part V
   item 4), not only the staleness the endpoint names.

---

## PART I -- THE OUTCOME TERRITORY

Each outcome is one thing a named kind of person can do. "Opal user" means a viewer the portal already treats
as internal (F6: the page's one predicate). "Non-Opal viewer" means every other signed-in viewer, advisors and
clients alike.

### O1 -- An Opal user can look at the whole Opal model book as one book on Positioning
On the Positioning page in Models mode, an Opal user selects an aggregate book and reads its **Portfolio
Composition** and **Holdings Breakdown** panels exactly as they read any single model's.
SOURCE: plan s.1 (the data path), plan s.5 Phase 1 steps 1-3.

### O2 -- An Opal user can see which models drive each aggregate position
For every holding in the aggregate, the Opal user reads how much each model contributes, in columns that are as
legible as the rest of the page on today's light canvas.
SOURCE: plan s.1 (the Model Breakdown column group), plan s.3 item 5, plan s.5 Phase 1 step 4.

### O3 -- A non-Opal viewer never sees the aggregate book on screen
An advisor or a client never finds the aggregate in the book selector, and cannot land on it through a
remembered or hand-edited selection.
SOURCE: plan s.5 Phase 1 steps 2 and 5; the 2026-08-24 concern (F9).

### O4 -- An Opal user reads aggregate weights that describe the current model book, and can see their date
The weight each model carries in the aggregate reflects Opal's model AUM as of a recent trading day, and the
Opal user can read that as-of date on the page rather than infer freshness.
SOURCE: plan s.3 item 1, plan s.4, plan s.5 Phase 2 steps 1 and 3; decision D1.

### O5 -- An Opal user can tell which models the aggregate covers
The Opal user can tell whether the two Opal Blend 5050 models are inside the aggregate and how, and nothing on
screen implies full coverage when a model is left out.
SOURCE: plan s.3 item 2, plan s.4; decision D2.

### O6 -- An Opal user can reconcile the aggregate's total to Opal's own AUM figure
An Opal user comparing the aggregate's total model AUM with the Opal-wide model AUM shown elsewhere either finds
them in agreement or can see why they differ.
SOURCE: plan s.4 ("Reconcile before relying"); Part IV F4.

### O7 -- (CONDITIONAL on D3) A non-Opal viewer cannot obtain the aggregate data at all
If Andrew takes D3 as recommended, a non-Opal viewer cannot retrieve the aggregate through any data route, not
merely through the screen.
SOURCE: plan s.3 item 4, plan s.5 Phase 3; decision D3. **If D3 is declined, O7 is cut, not deferred.**

---

## PART II -- WHERE THE BOUNDARY SITS

### II.1 This project OWNS
1. The aggregate book in **Models mode** of the Positioning page: its selector entry, its two panels, its
   per-model columns, its viewer gate and its remembered-selection handling (`portal`, Positioning `HoldingsTab`
   and its parent page).
2. The **`current_holdings.AGG` block** the Positioning producer writes, and **where that block's model weights
   come from** (`yang-generate-positioning`).
3. **Only if D3 is taken:** the route that carries the aggregate to Opal users alone.

### II.2 This project RELIES ON, and does not own
1. **The canonical Opal-wide AUM-by-model file** `platinum/mdpf/global/aum-metrics.json`, written by
   `opal-assets-mdpf-portal-publisher` from the MDPF gold producer `data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py`
   (F4). Its $8.3M gap belongs to that producer's owner. The owning project is not resolved here (Part VII).
2. **The portal's one internal-viewer predicate** (F6) and the **JWT edge** in front of
   `/api/general/positioning/*` (F7).
3. **The portal colour law** for the light canvas (portal `CLAUDE.md`, `DESIGN.md`).

### II.3 Siblings, named
1. **POSN_ASTTAX** (D4, CLOSED @e223c78ed5, 7 of 7 REALIZED). Same page, same producer. Its five-class asset
   taxonomy and labelled-zero benchmark rows ship in the same served file, so this project must leave the five
   model books exactly as that project left them.
2. **ETFS** macro (D4). The Positioning page's Satellites mode is ETFS territory. The aggregate is a Models-mode
   book only, and Satellites is untouched.
3. **The MDPF AUM family** (gold `dim_mdpf_aum_metrics.py`, the publisher, and the legacy
   `json/portfolios/aum-metrics.json` writer that stopped on 2026-07-23). Relied on, never modified here.

### II.4 NOT in scope (carried from plan s.7, plus two found here)
1. The aggregate on **Attribution** and **Factor Tilts**. Andrew's 2026-09-09 ruling 5 took both pages off
   `json/portfolios/` (F9), and his current word names only the Positioning panels.
2. The **AGG ETF ticker** (iShares Core U.S. Aggregate Bond). It shares the string and appears in the producer's
   benchmark and characteristics code (F3); any change must discriminate per call site.
3. A **per-advisor aggregate**. That needs an advisor-scoped AUM source that does not exist.
4. The **toggle-persistence pattern** from the 2026-08-24 record. It already exists and is reused, not rebuilt.
5. **Found here:** the portal's two dead legacy-AUM fetch functions (F8). They are surfaced, not removed.
6. **Found here:** retiring the legacy `json/portfolios/aum-metrics.json` object or its writer. The re-point
   stops this project's read of it; the object's fate is the MDPF family's.

---

## PART III -- THE QUALITATIVE BAR

No numbers are set here. Each line names who, what, and what it displaces, so each can be disputed.

1. **Answering the aggregate question.** An Opal user answers "what does Opal's model book hold in aggregate, and
   which models drive each position" on the Positioning page. Today they would assemble it by hand from five
   model books.
2. **Never mistaken for the reader's own positioning.** No advisor or client can come away reading Opal's
   firm-wide model mix as their own. This is the exact concern that removed the view on 2026-08-24 (F9), and
   restoring the view must not reopen it.
3. **Never a stale mix presented as current.** An Opal user never reads today's holdings weighted by a months-old
   model mix without the page saying so.
4. **Nothing else moves.** Every viewer, Opal or not, sees the five model books, the Satellites mode and the other
   Positioning panels exactly as before.
5. **Legible in the house style.** The restored per-model columns read as clearly as the neighbouring columns on
   the light canvas. A reviewer holding them to the portal colour law finds nothing to flag.

---

## PART IV -- THE SUBSTRATE: what exists, measured

All reads on site Z, 2026-09-15 16:36-16:55Z, by 4.0.0_SA_CRO~Z. The instrument is named on each finding.

### F1 -- The served aggregate block is present and refreshed daily
- Instrument: `.tools/aws s3api head-object` + `s3 cp`, then a gzip-aware parse. The object is gzip-encoded and
  decodes to 80,704 bytes.
- `s3://opal-data-portal-v2/json/positioning/positioning_data.json`, VersionId `aJ7nhwRKko3H_AMRzsNvvwkf1NiO9aou`,
  LastModified 2026-09-15T11:06:20Z, `generated_at` 2026-09-15T11:06:19Z, `data_as_of` 2026-09-14.
- `current_holdings` keys: UST, ST, INT, LT, ULT, AGG.

| Measure | Value |
|---|---|
| AGG holdings | 30 |
| AGG weights summed | 1.0001 over 30 of 30 |
| AGG holdings carrying `model_breakdown` | 30 of 30 |
| Model codes appearing in any `model_breakdown` | INT, LT, ST, ULT, UST (5) |
| AGG `total_aum` | 1,637,144,180.01 |

### F2 -- The aggregate's weights are July's
- Instrument: the same parse against `s3://opal-data-portal-v2/json/portfolios/aum-metrics.json`, VersionId
  `2xsIhWJmoBR96Qy5NzsEpT8ZG5daawKe`, LastModified 2026-07-23T20:57:17Z, `period` 2026-07-22.
- The AGG `total_aum` equals the legacy file's five mapped model rows summed (1,637,144,180.01). Each of the five
  served per-book `aum` fields equals its legacy row exactly (5 of 5).
- The legacy file's two Opal Blend 5050 rows (32,065,435.25 and 7,284,199.86) carry no model code, so they are
  outside the aggregate.

### F3 -- The producer at SITEZ HEAD
- Instrument: source read of `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py`
  at SITEZ @ec29ae6fae, 2,643 lines. The last commit to touch it is dbe34de7b0 (2026-09-14, POSN_ASTTAX TO-V1-1).

| Piece | Line @ec29ae6fae |
|---|---|
| `load_aum_data` | `:1421` |
| name-to-code map, 13 names over 5 codes, no blend entry | `:1437-1451` |
| S3 read of `json/portfolios/aum-metrics.json` | `:1461` |
| a failed read returns an empty dict | `:1474-1476` |
| `calculate_aggregated_holdings`; zero total AUM returns an empty aggregate | `:1525`, `:1538-1541` |
| `current_holdings['AGG'] = {holdings, total_aum}` | `:1811` |

- **The plan's citations for the same pieces (`:1395`, `:1411`, `:1435`, `:1499`, `:1785`) are at the CLOUD
  vintage.** At SITEZ HEAD they land on other code (printed: `:1395` is a fixed-income yield branch), consistent
  with the 26 lines POSN_ASTTAX added above them on this fabric. Cite the lines above on SITEZ.
- Failure mode worth naming: if the weight read fails, the aggregate is served as an EMPTY list and the file still
  publishes (`:1474-1476` then `:1538-1541`).

### F4 -- The current canonical weight source, and where its gap comes from
- Instrument: `.tools/aws` head + parse of `s3://opal-data-portal-v2/platinum/mdpf/global/aum-metrics.json`,
  VersionId `OVcFBOpgjFywfYJGYjowX2VSVwLdiyez`, LastModified 2026-09-15T13:50:50Z, `period` 2026-09-14,
  `scope` global.
- Its `_provenance`: written by `opal-assets-mdpf-portal-publisher` at 13:50:49Z from
  `s3://opal-data-assets/portal/gold/mdpf/global/aum-metrics/2026-09-14.json`.
- Seven `by_model` rows, with names as served. LT and ULT still carry the pre-rename labels, which the producer's
  map already covers (F3):

| `model_name` | Code | AUM |
|---|---|---|
| Ultra Short-Term | UST | 65,550,660.50 |
| Short-Term | ST | 133,205,460.44 |
| Intermediate | INT | 456,971,348.29 |
| Long-Term Conservative | LT | 883,977,496.68 |
| Long-Term Aggressive | ULT | 209,446,529.75 |
| Opal Blend 5050 Int Ltc | none | 35,744,571.59 |
| Opal Blend 5050 St Int | none | 7,217,454.65 |

| Reconciliation | Value |
|---|---|
| seven rows summed | 1,792,113,521.90 |
| the file's own `total.model_aum` | 1,800,437,987.06 |
| gap | 8,324,465.16 |
| the same three figures in the GOLD source it was published from | identical |
| the legacy July file: seven rows summed vs its own `total.model_aum` | 1,676,493,815.12 vs 1,676,493,815.11 |

- **So the gap is produced at or before gold, not by the publisher, and it did not exist in the legacy file.**
- The file's `meta.current_source` says its totals are "the global spine's own frontier row ... by construction",
  which indicates the totals and the rows come from different derivations. That is a lead, not an explanation.

### F5 -- What switching sources does to the weights
- Instrument: the same parse, weights = model AUM / sum over the models included.

| Weights | UST | ST | INT | LT | ULT |
|---|---|---|---|---|---|
| Served aggregate today (legacy July file) | 3.20% | 7.89% | 27.14% | 49.15% | 12.62% |
| Canonical file, 5 coded models, blends excluded | 3.75% | 7.62% | 26.13% | 50.54% | 11.97% |
| Canonical file, each blend folded 50/50 into its two models | 3.66% | 7.63% | 26.70% | 50.32% | 11.69% |

The third row is new here. It reads the two blend names as their constituents: "Int Ltc" as INT + LT and
"St Int" as ST + INT. That reading follows plan s.4 and is not confirmed against a definition (Part VII).

### F6 -- The portal, at what users see
- Instrument: `git -C portal grep` / `git show` at `origin/PROD` @edf85ce503, promoted 2026-09-15. It carries
  POSN_ASTTAX.
- The removal commit `d53049a0` is an ancestor of origin/PROD and of the local portal checkout. The local checkout
  is **detached at e85f6eb84f (2026-09-10), older than PROD**, and its line numbers differ, so cite PROD.
- At origin/PROD there is **no AGG entry** in the book selector (0 matches for the old selector constant or id).

| Anchor | File @origin/PROD | Line |
|---|---|---|
| removal note for the AGG selector entry | `src/pages/Positioning/tabs/HoldingsTab.tsx` | `:39` |
| FIRST-RENDER LANDING block | same | `:841` |
| "Portfolio Composition" panel | same | `:1105` |
| "Holdings Breakdown" panel | same | `:1197` |
| "THERE IS NO `aggregate` CAPABILITY" rationale | `src/pages/Positioning/shared/bookSet.ts` (plan cited a path without `shared/`) | `:238` |
| "a THIRD coupling ... the AGG AUM denominator" note | same | `:39` |
| `const internal = isInternal() \|\| isDev()` | `src/pages/Positioning/Positioning.tsx` | `:267` |
| `<HoldingsTab` mount (does not receive `internal`) | same | `:642` |
| `getPositioningData()` | `src/api/portal-proxy.ts` | `:1177` |
| "Auth: REQUIRES A VALID JWT BEARER" | same | `:1131` |
| `model.json` route, "blocks client tier" | same | `:1421`, `:1430` |

### F7 -- The aggregate data already reaches every signed-in viewer
- Instrument: the proxy docstring at `:1131` records a served-plane measurement by 0.0.0_AB_MSTR~Z on 2026-08-27
  (401 without a bearer, 200 with one, a distinct 401 on a bogus one). **Not re-measured here.**
- Every signed-in viewer receives the same `positioning_data.json`, and the AGG block is inside it. A screen gate
  makes the aggregate Opal-only on screen, not in the data (plan s.3 item 4). This is why O7 exists and is
  conditional.

### F8 -- Who else reads the legacy AUM key
- Instrument 1: unscoped `comp-find -i "portfolios/aum-metrics" --files --all`. DENOMINATOR: 536 hits across
  61,813 files (bands HEAD 29, SURFACED 168, CONFIG 127, TEST 9, DOC 203).
- The first-party code hits, classified by reading each hit in place:

| Class | Where |
|---|---|
| **Reads values from it** | **1: the AGG producer, `:1461`** |
| Writes it (writer flag-disabled per the note at `infra/aws/terraform/smartx-pipeline/lambdas.tf:44-46`) | `infra/aws/lambda/smartx_ingestion_pipeline/lambda_function.py` |
| Grants a write | `infra/aws/terraform/mdpf-pipeline/iam.tf:287`, `infra/aws/terraform/opal-assets/monolith.tf:269` |
| Lists it for freshness, monitoring or head checks | `infrastructure_monitor` lambda `:97`, `ai-supervisor.py:132`, `ai-supervisor-v2.py:296`, two `infra/aws/scripts/validate_portal_data_*.sh` |
| Snapshot exception | `yang-time-machine` lambda `:56` |
| Archived access-control example | `infra/aws/users/_archive_pre_2026-04-15/access_control/access_matrix.py` |
| Portal: fetch functions that request the legacy route | `portal-proxy.ts` `getAUMSummary` `:281` and `getAUMMetricsWithCalculations` `:364`, wrapped by `src/api/endpoints/aum.ts` `:184` and `:389` |

- Instrument 2 (different): word-bounded `git -C portal grep` at origin/PROD for callers of those two wrappers
  outside their defining files. **0 callers.** Positive control: `getAUMMetricsByFirm` found 2 times in
  `ModelPortfolios.tsx`. Instrument 3, native search over the local checkout, also found 0 files outside the two
  defining files.
- **So the plan's claim holds at the grain of code that reads values: the AGG producer is the only live reader.**
  The two portal functions are dead code that still names the legacy route. That is the II.4 item 5 finding.

### F9 -- The standing rulings this project touches
- **2026-08-24**, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260824_PULL_AGG_VIEW_THREE_PAGES_AND_TOGGLE_PERSISTENCE_PATTERN.md`.
  The concern, verbatim: *"my concern here is that the "Agg" view is somehow tied to Opal's aggregate models
  somehow as opposed to the Advisor's aggregate Opal Model exposure, which would be a problem."* The decision,
  verbatim: *"simply just pulling "Agg" toggle view from those three pages ("Positioning" "Attribution" and
  "Factor Tilts") nobody cares about this view and its more trouble than its worth."*
- **2026-09-09 ruling 5**, record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260909_1458Z_INFRA_REPORT_FIVE_RULINGS.md`
  `:29-31`, verbatim: *"We've excised the need for this already via not displaying an "AGG" view, which is what
  required aum-metrics. Neither /attribution nor /factor-tilts should have any reliance on /json/portfolios/."*
  **Its letter names only Attribution and Factor Tilts. Its stated premise is that AGG is gone.** Restoring AGG on
  the legacy source would contradict that premise even though it breaks no letter of the ruling (Part V item 4).

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Named, not sequenced. Sequencing is L5.

1. **Andrew answers plan s.6:** canonical flow, or the 2026-08-24 exemption again. Reserved to him.
2. **Andrew decides D1-D4** (plan s.6). The plan's recommendations, carried as recommendations only:
   - D1: Phases 1 and 2 together;
   - D2: fold the blends in;
   - D3: move the aggregate to an Opal-only file;
   - D4: his preference.
3. **The $8.3M gap is explained by the gold producer's owner, or disclosed to the Opal user** before the aggregate
   total is read as authoritative (O6, F4).
4. **The aggregate stops depending on `json/portfolios/`** if the view returns. Otherwise the view that ruling 5
   treated as gone comes back on the exact dependency that ruling reasoned away (F9). This bears on D1: Phase 1
   alone keeps that dependency.
5. **Any change to `current_holdings.AGG` or its delivery changes served output.** It needs the never-widen
   sign-off (CTO + COO) naming the blast radius. **The writers of `current_holdings.AGG` must be counted first.**
   One writer was found here (F3), but this brief did not run a writer census over the estate.
6. **The five model books stay byte-identical** in the served file across any producer change (Part III item 4;
   II.3 item 1).
7. **The screen gate uses the page's existing internal predicate** (F6), not a new one. It reaches the
   aggregate's selector entry, its columns and the remembered selection alike (O3). The predicate includes
   `isDev()`, whose meaning is not read here (Part VII).
8. **The restored columns are verified by rendering the page as both viewer classes.** The portal verification
   law applies (`/frontend-dev`) and its colour law binds (Part III item 5).
9. **The producer deploys through its normal Terraform path** (plan s.5 Phase 2 step 5). The deployed producer
   bytes have not been read against source.

---

## PART VI -- STATUS  [NOT OUTCOME-BEARING -- do not cut outcomes from this part]

Measured 2026-09-15 on site Z. Status ages; the outcomes in Part I do not.

| Fact | Value | Clock (UTC) |
|---|---|---|
| Project code | POSN_AGGFIX, named by Andrew. Unregistered at 16:36Z; **REGISTERED by 1.0.0_SA_CTO~Z @d5e068cde4** (`org/missions/D4/POSN/POSN_AGGFIX/project.json`, dep_stage REGISTERED) | 16:36Z, re-read 17:01Z |
| Directive / macro | D4 "Positioning"; macro POSN is ratified for D4 in `MACROS.yaml` | 16:39Z |
| Sequencing | not listed in `org/missions/SEQUENCE.yaml` (`sequence-check --project POSN_AGGFIX` places nothing) | 16:36Z |
| Served aggregate | present, 30 holdings, July weights | object 11:06:20Z, read 16:41Z |
| Canonical AUM file | current (period 2026-09-14), gap 8,324,465.16 | object 13:50:50Z, read 16:41Z |
| Portal PROD | edf85ce503, no aggregate on screen | read 16:5xZ |
| Open task orders for this lane | 0 (`to-check --all --assignee 4.0.0_SA_CRO~Z`, 2648 faces) | 16:38Z |
| 1.0.0_SA_CTO~Z | L2 endpoint FWD-1..FWD-8 and L3 landed @d5e068cde4 (its log f61a880243); L4 waits on Andrew's DONE WHEN word and D1-D4 | 17:01Z |
| Site Z push hold | standing (Andrew's word); this brief's commit is LOCAL | -- |

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

1. **No build, render, typecheck or deploy.** Nothing was changed outside the brief and the carried plan.
2. **The deployed producer bytes were not read.** F3 is source at SITEZ HEAD, not the running Lambda.
3. **The JWT edge was not re-measured** (F7 rests on a docstring's cited 2026-08-27 measurement).
4. **The $8.3M gap is unexplained.** F4 locates it at or before gold. It does not say why.
5. **The folded-weights row (F5) assumes** the blend names mean INT + LT and ST + INT. It is not read against a
   model definition.
6. **The per-holding aggregate values were not re-derived by hand.** Only totals, counts and weight sums were
   checked.
7. **No writer census of `current_holdings.AGG`** beyond the one producer found (Part V item 5).
8. **The owning project of the gold AUM producer was not resolved.** comp-estate returns
   `SUBJECT_ABSENT_FROM_CORPUS` for the platinum key across 135 chains. It maps the legacy key to one D2
   positioning chain.
9. **The meaning of `isDev()` in the internal predicate was not read.**
10. **The removal diff was not re-read.** Plan s.1's account of `d53049a0` rests on 4.0.0_SA_CRO's reading of it
    (740 lines, read in full per plan s.8). This brief confirms only the commit's ancestry and today's absence of
    the selector entry.
11. **The Andrew-direct record for the ~16:2xZ word** is cited by 0.0.0_AB_MSTR~Z at
    `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260915_162xZ_POSN_AGGFIX_TO_SITEZ_SPAWN_Z_FABRIC_CTO_Z_ENDPOINT_FORWARD.md`
    "on CLOUD". **It is ABSENT from origin/CLOUD @2033ff3ea6** (fetched 16:3xZ; `git cat-file -e` rc=128, with the
    plan beside it as the positive control). It may be local on the CLOUD device. On SITEZ the word is recorded by
    1.0.0_SA_CTO~Z at `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_162xZ_POSN_AGGFIX_CTO_Z_ENDPOINT_FORWARD_ON_CRO_RESTORE_PLAN.md`
    (@d5e068cde4), and this brief quotes it verbatim again.
12. **The D4 directive PRD** (`docs/architecture/D4_ETF_POSITIONING_VARIANT_PRD.md`) was not read for how it
    relates to this project.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/posn-aggfix-opal-only-agg-view-brief-20260915.md
  PROJECT           POSN_AGGFIX, org/missions/D4/POSN/POSN_AGGFIX/project.json (REGISTERED @d5e068cde4)
  ENDPOINT          org/tier1_exec/1.0.0_SA_CTO/deliverables/POSN_AGGFIX_ENDPOINT_FORWARD_20260915_Z.md (FWD-1..FWD-8)
  DIRECTIVE/MACRO   D4 Positioning / POSN
  EXISTING PRD      NONE
  SOURCE PLAN       org/tier1_exec/4.0.0_SA_CRO/deliverables/POSITIONING_AGG_OPAL_ONLY_RESTORE_PLAN_20260915.md
                    (CLOUD @2033ff3ea6; SITEZ copy byte-identical, blob 0765b9af1f)
  SIBLING PROJECTS  POSN_ASTTAX (CLOSED @e223c78ed5); ETFS macro (Satellites mode); MDPF AUM family (gold
                    dim_mdpf_aum_metrics.py + opal-assets-mdpf-portal-publisher)
  PRIOR ART         served current_holdings.AGG (F1); producer AGG path @ec29ae6fae (F3); canonical AUM file (F4);
                    internal predicate + model.json client-tier refusal @portal origin/PROD edf85ce503 (F6)
  RULINGS           2026-08-24 AGG removal (1.0.0_SA_CTO deliverables); 2026-09-09 ruling 5 (4.0.0_SA_CRO
                    deliverables :29-31)
  MEASURED AT       2026-09-15 16:36Z-16:55Z, site Z, 4.0.0_SA_CRO~Z (per-fact clocks in Part VI)
```
