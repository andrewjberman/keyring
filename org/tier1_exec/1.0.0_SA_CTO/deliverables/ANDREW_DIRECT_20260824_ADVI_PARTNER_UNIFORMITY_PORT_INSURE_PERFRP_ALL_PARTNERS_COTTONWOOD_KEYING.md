# ANDREW-DIRECT 2026-08-24 ~19:1xZ (base CTO terminal) -- ADVI PARTNER UNIFORMITY: ADVI_INSURE ports to Cottonwood's ADVI when complete + validated; ADVI_PERFRP logic applies across ALL partners (49 Financial, Inflection Wealth Management, Cottonwood Capital Advisors); Cottonwood needs a DEEP ANALYSIS of its current ADVI keying ("portfolio_group" suspected); NO per-partner data/frontend structures except 49F (large advisor group -> leaderboard); Cottonwood's view = Inflection's, exactly, plus the Insurance views

**Recorded by:** `1.0.0_SA_CTO` (addressed seat) - **archetype:** SCRIBE / COORDINATE
**Context:** delivered after the D3 breakdown, as an addition "to the forefront" of the ADVI program. Quoted exactly as
typed. Binds `ADVI_INSURE`, `ADVI_PERFRP`, `D2`, and the Cottonwood ADVI tree (`cot`). **Distribution restriction
(his ~16:1xZ word) read conservatively: not to `4.0.0_SA_CRO`.**

## VERBATIM

> "Additionally I also want to bring the schema to the forefront that the whole ADVI_INSURE function we build out is
> going to have to be ported and applied to Cottonwood's ADVI instance when complete and validated. BY the same token,
> the same logic for ADVI_PERFRP is also going to have to be applied across all partners, 49 Financial and Inflection
> Wealth Management and Cottonwood Capital Advisors. Lastly, Cottonwood is going to need some deep analysis on their
> current ADVI process and setup because currently we are not keying them in the right way. I suspect that the place
> that they actually use to assign advisor relationships is the "portfolio_group" key or some derivation of "portfolio
> group", so that will need to be investigated. I do not like the idea of having all these advisors have their own data
> structure and frontend structure aside from 49F which has a very large-scale advisor group, therefore they need the
> leaderboard and all that. In the case of Cottonwood however, their view should essentially be the same as
> Inflection's; it should look exactly the same, with one notable differnece. Inflection has no insurance business, but
> Cottonwood does, so those Insurance views and schemas we design for 49 Financial are going to have to be incorporated
> into their design."

## WHAT IT BINDS (surfaced, unwidened; the phrasing is the ruling)

1. **`ADVI_INSURE` is a PORT OBLIGATION, not a pattern note.** The whole function built for 49F -- backend pattern,
   gold table shape, platinum key, the three surfaces + the Total Assets element -- is **ported and applied to
   Cottonwood's ADVI instance when complete and validated.** Same schema and UI; separate tree and keys (bd<->cot law
   unchanged). The INSURE PRD's s.11 #9 ("pattern note only") is SUPERSEDED-BY-WIDENING: the note stays as the port
   spec, and the port is a scheduled act on completion.
2. **`ADVI_PERFRP` logic applies to ALL THREE partners** -- 49 Financial, Inflection Wealth Management, Cottonwood
   Capital Advisors -- as bindings of ONE runner / publisher / interface (the D2 pattern: build once on 49F, bind INF and
   COT at their gates), never three implementations.
3. **Cottonwood: a DEEP ANALYSIS of its current ADVI process and setup** -- *"currently we are not keying them in the
   right way"*; hypothesis to test: advisor relationships are assigned via **`portfolio_group` or a derivation of it.**
   A measured investigation (atom-decomp over the Cottonwood ADVI identity/keying surfaces) with a remedy plan --
   prior art: the 49F Portfolio-Group keying scan (BD `qt6` "BI Billing", Primary Portfolio Group as the partition key,
   groups OVERLAP) -- reusable as an ARTIFACT (its author's lane is off the restricted subject; the artifact is not).
4. **THE UNIFORMITY LAW, his:** no per-partner data structure and frontend structure -- **EXCEPT 49F**, whose
   large-scale advisor group needs the leaderboard "and all that". **Two UI tiers, then:** **Tier A = 49F** (full ADVI:
   leaderboard, advisors, distribution, Books, Book view); **Tier B = Inflection = Cottonwood** (the SAME view, exactly),
   **plus the Insurance views/schemas for any Tier-B partner with an insurance book** (Cottonwood yes; Inflection no).
   The insurance module is an OPTION on the tier keyed on a partner FACT (has an insurance book), not a per-partner
   design.
5. **Consequence for every ADVI PRD in this round:** each names its partner-binding plan (49F first; INF + COT as
   bindings) and its UI tier; the partner-uniformity law is recorded once (D2 PRD s.11) and referenced, never restated.

## CONSEQUENCES (this seat)
- `ADVI_INSURE_PRD.md` s.12: the Cottonwood PORT obligation (trigger: 49F complete + validated; scope: same schema/UI
  on the cot tree; the `DATA_BDINSURANCE` Phase-0 work is the Cottonwood ingest half already in motion -- rung 2).
- `ADVI_PERFRP_PRD.md` s.12: partner bindings (49F build; INF + COT bind; Tier-B view = Inflection's, exactly).
- `D2_ADVI_49F_E2E_PRD.md` s.11: THE ADVI PARTNER UNIFORMITY LAW (Tier A / Tier B; insurance option by partner fact).
- Cottonwood keying investigation: registration PROPOSED as its own bounded project (code candidate `ADVI_COTKEY`),
  atom-decomp over the cot ADVI identity surfaces; one question to Andrew below.
- Broadcast: MSTR + COO/CVO/DS/DE (queued). Same turn.
