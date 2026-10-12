# CTO ruling (self-drive tick 3) -- dell1-20261011T053810Z-fe9b: MDPF_CANON X2 global view folds every per-model line held at fewer than 2 firms -- option (A)

From 1.0.0_SA_CTO (laptop, cluster lead; `/self-drive` cluster open calls, arming record @4698a8f59d), 2026-10-12 ~14:0xZ.

## The fork

Row MDPF_CANON-D1-W8-S5 (ARMED). The round-3 basis `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~11/X2_GLOBAL_BASIS.md`
(as-of 2026-10-08) reads: `by_model` entries 41 (20 aggregate-aua-timeseries, 14 account-distribution, 7 aum-metrics); single-firm
entries 21 (10 + 9 + 2), each held at ONE firm (Cottonwood for 17, Inflection for 4), and for most of them the Global value
EQUALS that firm's own value; two carries (`opal_growth_sma`, `opal_div_sma`) held at no firm at the as-of. Headline sums
(`opal_aggregate_aua`, `model_aua`) read 3 firms. X2 (the Global view) was GRANTED 2026-09-15 on the round-2 basis "aggregate
counts only".

(A) fold every `by_model` entry held at fewer than 2 firms into one "other models" line (count and value summed) and keep the two
one-firm non-model series out of Global; headline sums unchanged; a served change under never-widen with every Global leaf read
before and after. (B) keep every line and re-sign the ENDPOINT to say Global shows per-model lines down to one firm.

## Ruling: (A)

1. The grant's own basis decides: X2 was granted as "aggregate counts only". A per-model line held at one firm whose value equals
   that firm's value is not an aggregate; it is that firm's book under a Global label. (A) restores the basis the grant was given
   on; (B) widens the grant, which is an ENDPOINT change and a new sign-off. Between restoring a basis and widening it, the
   restore wins by default (the never-widen principle applied to what a reader may see).
2. The headline sums are untouched by (A): the fold moves lines, not totals; the portal page's contract (the served JSON shape)
   keeps every key -- the folded entries become one entry -- so the Model Portfolios page keeps working, which was Andrew's
   stated concern on 2026-10-11.
3. The threshold is `min_firms = 2`, read per as-of from the firm scopes' own objects exactly as the basis file computes it,
   never a static list; an entry that gains a second firm un-folds on its own at the next emit; a carry (held at no firm) folds.
4. Design-fork procedure: the CRO's past-pattern research was asked 13:04Z and the seat is dark (re-seat asked 13:58Z). A dark
   seat does not hold a call; this ruling stands, and the CRO's research, when it lands, may AMEND it only by naming a
   pattern this reasoning misses (the driver would then re-rule in the same loop).

## Acts (dell1's)

- `2.0.0_SA_COO~D1` cuts the fold cell in MDPF_CANON's next issuance (the FWD-3 "global fold" cell the row gates): emitter
  change + the before/after read of every Global leaf under a never-widen pair signed by `1.0.0_SA_CTO~DELL1` and the COO; the
  three served documents (aggregate-aua-timeseries, account-distribution, aum-metrics) each read back with the folded line
  present and the headline sums byte-equal to before.
- `1.0.0_SA_CTO~DELL1` closes dell1-fe9b on this file (`--ruled-by cluster-lead`) and disarms D1-W8-S5 on the cell's read-back.
- No Andrew act: (A) spends nothing the law reserves; the PROD page shows one more line and loses none of its totals.

## Addendum 1 (14:1xZ) -- the CRO's pattern read AMENDS the shape, not the option (msg 108577, record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/CRO_PATTERN_READ_DELL1_FE9B_X2_GLOBAL_FOLD_20261012.md` @afdb738704)

Patterns found: R7 (`infra/logic/02_DOCTRINE.md:415-422`, attributability decides tenancy at ANY grain) makes a one-firm
`by_model` line under `global/` non-conformant independently of the X2 grant, so (B) would also be an R20 departure. The
missed pattern: the fold line is itself a slice -- in aum-metrics both folded entries are Inflection (X2_GLOBAL_BASIS.md:48-50),
so the "other models" line would be one firm's book under another label. RULING AMENDED: primary plus secondary suppression,
applied per date index -- the fold line is emitted only when the entries it holds come from >= 2 firms; otherwise it is
suppressed for that document and date (the headline sums still carry the value, so nothing is lost from the totals), and the
suppression is said in the document's basis note. The cell's read-back asserts, per document and date, that every emitted
`by_model` line (folded or not) is held at >= 2 firms. Option (A) stands.
