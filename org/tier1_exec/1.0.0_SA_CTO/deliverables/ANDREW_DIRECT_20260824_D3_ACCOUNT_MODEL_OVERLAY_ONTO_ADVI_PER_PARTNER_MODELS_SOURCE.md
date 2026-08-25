# ANDREW-DIRECT 2026-08-24 ~19:0xZ (base CTO terminal) -- D3 "Account Model Overlay" onto Advisor Intelligence: a plan is needed -- BACKEND (find each partner's "models" data source, process it into an ADDITIVE gold-runner script giving account / client-relationship-household / advisor / firm model-holdings breakdowns) and FRONTEND (into the relevant ADVI view pages, same level/location logic as the Insurance and Performance-Reporting PRDs)

**Recorded by:** `1.0.0_SA_CTO` (addressed seat) - **archetype:** SCRIBE / COORDINATE
**Context:** delivered immediately after the D1 view-tree word, as the second of the "couple other PRDs" he said he
would dictate. Binds directive **D3** (`docs/architecture/D3_ACCOUNT_MODEL_OVERLAY_PRD.md`, v1.0 08-19; TOs
`D3_MODELOVERLAY.TO-D3.1` DELIVERED (exact-join spec), `D3.1b` ungated, `D3.2`-`D3.5` gated). Quoted exactly as typed.

## VERBATIM

> "In addition to this of course we are going to need a plan on how to incorporate the "Account Model Overlay"
> functionality onto Advisor Intelligence, which means assessing both backend where the "models" data source is per
> partner and figuring out where that is so it can be sourced and processed into an additive gold-runner script that
> will essentially provide the account-level, client/relationship/houseshold level (same grain just different
> terminology per partner), advisor level, and firm level model holdings breakdowns. This is a backend and frontend
> job because frontend ADVI is going to need to have these incorporated somewhere in the relevant view pages (this is
> on the same level/location logic as what we described for insurance and performance reporting in the recently
> produced ADVI prds)./"

## WHAT IT BINDS (surfaced, unwidened)

1. **A PLAN (= a PRD refresh of D3) for incorporating the Account Model Overlay onto Advisor Intelligence** -- two
   halves, both his: BACKEND and FRONTEND.
2. **BACKEND, step 1 = ASSESS the "models" data source PER PARTNER** -- *"figuring out where that is"* -- a measured
   census, one row per partner (49 Financial / Cottonwood / Inflection), naming the plane the model membership and
   model holdings come from (in-estate candidates to MEASURE, not assume: 49F = SmartX JD1
   `smartx/platform/silver/fact_allocation_account_map/` + the model book weights; Cottonwood = the BD rebalancer /
   strategy exports behind the MDPF cottonwood slice; Inflection = its Orion-side model plane).
3. **BACKEND, step 2 = an ADDITIVE gold-runner script** that sources + processes that plane into **model-holdings
   breakdowns at FOUR levels: account -> client/relationship/household -> advisor -> firm** -- *"same grain just
   different terminology per partner"* (the spine's second level is one grain with three partner names; the
   registry, not the code, carries the label).
4. **FRONTEND = the same level/location logic as `ADVI_INSURE` and `ADVI_PERFRP`:** the Books tab (L2 advisor book,
   L3 client, L4 account) + the Advisor's Book view on `advisorpublicprofile`; Advisor + Distribution tabs untouched.
5. **Relation to the D3 PRD v1.0 and its TOs:** v1.0 already scopes the `account_model_membership` producer
   (D3.2), the publisher pair (D3.3) and the overlay UI (D3.4), with the exact-join spec DELIVERED (D3.1) and D3.1b
   ungated. His word ADDS: the per-partner SOURCE ASSESSMENT as an explicit first act, the FOUR-LEVEL breakdown as
   the producer's output contract, the additive-script form, and the placement rule (Books / Book view). The D2-flip
   and D1-registry gates on D3.2-D3.4 are unchanged by this word.

## CONSEQUENCES (this seat)
- D3 PRD v1.1 amendment (s.10): the per-partner source census as a GROUND TRUTH run (D3 run gains rows), the
  four-level output contract, the placement rule; then the same review as the others (breakdown, /draw, cards).
- Broadcast: MSTR + the D3 seats (COO, CVO, DS, DS~B, DE). Same turn. CRO not included (ADVI subject; his restriction
  on the 49F findings is read conservatively here).
