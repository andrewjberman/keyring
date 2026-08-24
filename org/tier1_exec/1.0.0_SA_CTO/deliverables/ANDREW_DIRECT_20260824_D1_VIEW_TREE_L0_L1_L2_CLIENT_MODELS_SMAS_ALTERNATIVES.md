# ANDREW-DIRECT 2026-08-24 ~18:5xZ (base CTO terminal) -- D1 MDPF category views: the FRONTEND VIEW TREE -- L0 "Client, Models, SMAs, Alternatives" (Insurance NOT included for MDPF: no fees taken); L1 drilldowns per L0 value; L2 where further derivations exist

**Recorded by:** `1.0.0_SA_CTO` (addressed seat) - **archetype:** SCRIBE / COORDINATE
**Context:** his comment on the laptop-directive state + dependency order ("This all looks good"), delivered as
"my only comment on this group". Quoted exactly as typed. Binds `D1_CATVIEWS` (directive D1) -- the frontend
view tree and the category vocabulary it renders.

## VERBATIM

> "This all looks good, my only comment on this group is that there is going to need to be some front-end work,
> whereby firms have a new L0 View based on what is present, and an L1 drilldown view based on what they click
> on, with potentially an L2 view if there are further derivations. L0 view is "Client, Models, SMAs,
> Alternatives". I don't believe there were any other categories (There was "Insurance" but I don't really care
> about including that in here, we don't take fees on it so not really relevant for MDPF purposes). L1 view for
> Clients is "Client Supervised" and "Client Unsupervised", where this is solely a function of assets the
> advisors take fees on or don't take fees on. L1 view for Models is "Primary Models" and "Custom Models", where
> Primary models are UST ST INT LT ULT, the current main 5, and custom models are any opal models that are not
> those (e.g. Opal Fixed Income) which are displayed upon L2 Drill. L1 view for SMAs is just "Tax" "Muni" "DIVZ"
> "PFOE" so far, maybe others will eventually be added. "Alternatives" we will not get into just yet. If you need
> clarity on the ruleset for how these are comprised per Partner, I can cover off on those as well/"

## WHAT IT BINDS (surfaced, unwidened; the phrasing is the ruling)

1. **A new frontend surface on the MDPF global view: a three-level drilldown.** **L0** = what is PRESENT for the
   firm, from the set **{Client, Models, SMAs, Alternatives}**; **L1** = the drilldown of the clicked L0 value;
   **L2** where further derivations exist.
2. **L0 vocabulary, and one exclusion:** Client, Models, SMAs, Alternatives. **Insurance is NOT in the MDPF view
   tree** -- *"we don't take fees on it so not really relevant for MDPF purposes."* (It stays a top-level value in
   the D1 taxonomy RULING of 08-19 and in the ADVI plane per finding 1 -- it is excluded from THIS product's view
   tree, not from the registry. Rule 24: the view axis and the registry axis are two axes; the exclusion is
   recorded on the view axis.)
3. **Client L1 = "Client Supervised" / "Client Unsupervised"** -- *"solely a function of assets the advisors take
   fees on or don't take fees on."* (Relation to the 08-19 ruling's `Client = Advised + Residual`: same split,
   his vocabulary now names the DISCRIMINATOR -- fee-taking -- rather than advisory scope; the decomp records
   whether `advisory_scope=advised` == fee-taking on every firm's data or whether a fee predicate must replace
   it. Prior art: the COT_SUPERVISED filter already ships a fee-based supervised/unsupervised split for
   Cottonwood -- Build Ladder rung 2.)
4. **Models L1 = "Primary Models" / "Custom Models"** -- Primary = **UST, ST, INT, LT, ULT** (the current main
   five); Custom = **any Opal model that is not those** (e.g. Opal Fixed Income), **enumerated at L2 drill**.
   (Matches the 08-19 ruling `Models = Primary + Custom` MECE; the five Primary names are now RULED verbatim.)
5. **SMAs L1 = "Tax", "Muni", "DIVZ", "PFOE" so far** -- *"maybe others will eventually be added"* (an OPEN
   enumeration; the registry must admit additions without a code change -- the D1 producer-resolution surface).
6. **Alternatives: no L1 yet** -- *"we will not get into just yet."* L0 value present; drilldown deferred.
7. **Per-Partner composition rulesets are his to give** -- he offered; the D1 producer-resolution surface (e) is
   exactly those hand maps resolving through the ONE registry. CTO asks for them (below).

## CONSEQUENCES (this seat)
- `D1_CATVIEWS`: PRD s.8 gains this as a stage-2 AMENDMENT (the view tree + vocabulary); the D1 run gains a row
  (AMENDED-PRD-GAINS-A-RUN-ROW); the stage-3 decomp COO landed at 13:28Z (14 cells) PRE-DATES this word and must
  absorb it before the CVO cert (a view-tree cell set: L0/L1/L2 renderers + the vocabulary in the registry);
  TO-D1d (DE global view) is the cell family this lands on.
- Rule 24 (enumeration): L0 {Client, Models, SMAs, Alternatives}; Client L1 {Supervised, Unsupervised}; Models L1
  {Primary, Custom} with Primary = {UST, ST, INT, LT, ULT}; SMAs L1 {Tax, Muni, DIVZ, PFOE, ...open}. Each axis
  gets its four-postulate record at decomp; the fee-taking discriminator is the state axis to name.
- Broadcast: MSTR + the D1 seats (COO, CVO, DS, DE) -- same turn. Not a 49F subject; CRO not needed.
