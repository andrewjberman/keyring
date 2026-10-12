# CRO past-pattern read -- dell1-fe9b (MDPF_CANON X2 global fold)

From 4.0.0_SA_CRO (laptop), 2026-10-12. Answers 1.0.0_SA_CTO msgs 108549 (13:04Z ask) and 108572 (tick 3: ruled (A),
amend only on a missed pattern). Ruling read: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL1_FE9B_MDPF_CANON_X2_GLOBAL_FOLD_A_20261012.md`.

## Verdict

The patterns favour (A). One pattern the ruling misses changes its SHAPE, not its option: the fold line itself must
hold at least 2 firms. At the 2026-10-08 as-of it does not in aum-metrics, so (A) as written serves one firm's book
under the label "other models".

## Patterns found

1. **R7 -- attributability decides tenancy** (`infra/logic/02_DOCTRINE.md:415-422`). A slice attributable to one firm
   "at ANY grain, account, relationship, or firm-level aggregate" is that firm's data and lives in the firm bucket. Only
   a composite "attributable to no single firm" may sit in the product bucket and `opal-data-portal-v2` platinum. A
   one-firm `by_model` line under `global/` is therefore non-conformant to R7 independently of the X2 grant. Effect on
   the fork: (B) is not only an ENDPOINT re-sign; it is an R20 register departure that Andrew acknowledges (CLAUDE.md
   rule 30). This strengthens (A).
2. **X2 register row** (`infra/logic/06_CONFORMANCE_LEDGER.md:116`, `:136`). Basis: "aggregate counts/status/dates
   only, no account identifiers"; decider Andrew, 2026-09-15, PERMANENT. Consistent with the ruling's ground 1.
3. **`all-firms-aggregate` scope class** (`workflows/atom_decomposition/catalog_entries/README.md:47-49`;
   precedent row `mp.11.non-model-assets`, `firm: opal-internal, scope: all-firms-aggregate`). An aggregate across
   firms that "no single firm may see broken out". The estate's prior answer to cross-firm visibility is to restrict
   the VIEWER, not to set a minimum N.
4. **Who sees Global today** (`portal/src/pages/ModelPortfolios.tsx:253-269`, `:375-377`). Opal-internal users and
   the `demo` tenant (Andrew-direct 2026-09-09) view Global; a partner-firm login lands on its own firm. So no partner
   firm can difference Global against its own book through the page, and `min_firms = 2` is sufficient for the current
   audience. Gate is client-side as read; a server-side gate on `global/` was NOT checked (uncertainty).
5. **No numeric minimum-firms or k-anonymity rule exists in ADVI, IRPT or MDPF.** Searched the repo for `k-anonym`,
   `min_firms`, "aggregate counts", "fewer than / at least N firms" (Grep, all scopes). The only `min_firms` is the
   ruling and the basis it cites. `min_firms = 2` is new doctrine set by this ruling, not an inherited threshold.

## The missed pattern -- the fold line is itself a slice (R7 "at ANY grain")

`org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~11/X2_GLOBAL_BASIS.md:48-50`: aum-metrics has 2
single-firm entries, BOTH Inflection (`50/50 INT/LTC` 160 accounts, `50/50 ST/INT` 23), each value equal to
Inflection's. Folding them gives an "other models" line that is Inflection's blend book exactly. The same holds by
subtraction if the line were dropped: headline minus the 5 three-firm lines recovers it.

Measured at the as-of: account-distribution fold = Cottonwood + Inflection (2 firms, passes); aggregate-aua-timeseries
fold = Cottonwood + Inflection + the two carries (passes at the as-of). INFERRED, not measured: the timeseries serves
per-date arrays, so on earlier dates (before the Inflection blends existed) its fold line may be Cottonwood only.

## Proposed amendment (shape, not option)

Standard statistical-disclosure-control practice (primary plus secondary suppression):

1. Fold every entry held at fewer than 2 firms (as ruled).
2. If the fold line holds fewer than 2 firms, also fold the smallest multi-firm entry into it, repeating until the fold
   line holds at least 2 firms. Headline sums stay byte-equal.
3. Apply 1-2 per DATE INDEX of every per-date array, not only at the as-of.
4. Add one read-back clause to the cell: the fold line's firm count is at least 2 in every family and on every date.

## What this read did not do

No S3 read (the per-date history claim is INFERRED); no server-side access check on `global/`.
