# The $696K: why Patrick Scanlan's non-fee AUM still displays wrong — mechanism, grounded

**Author:** 4.0.0_SA_CRO~A · 2026-08-11 ~0750Z · **archetype:** DIAGNOSE
**Andrew's live observation:** the Inflection portal still shows ~$696K non-fee for Patrick when
the reviewed truth is $127,961.76 classified non-fee.

## THE ANSWER IN ONE PARAGRAPH
The figure on his screen is `platinum/advisors/patrick_scanlan/book.json` →
`book.non_fee_earning_aua = 695,956.41` (republished 07:39Z by run-2), produced NOT by the fixed
D_04 but by a SECOND implementation of the fee split:
`INF_D_02.advisor_client_detail.py:1941-1951` — a per-account loop whose `else` bucket books
EVERY account lacking a fee-earning billing MATCH into non-fee. That else conflates two
populations: genuinely-classified non-fee accounts (the reviewed $127,961.76) AND accounts with
no billing match in the join (the no-billing-row + book-definition-drift class, ~$568K of AUA at
current values). The number GREW from ~$606K to ~$696K precisely BECAUSE the unstick refreshed
AUA — the misclassified component moves with current holdings, which is diagnostic of
artifact-absorbing arithmetic. CPR-4's fix was scoped to D_04 (firm level) and its succession is
PROVEN there (DS 074932Z: served firm non-fee = $3,623,738.50 where the retired residual would
print $71,944,750.24). The advisor-grain surface Patrick views was never in CPR-4's scope.

## THE STRUCTURAL FINDING: ONE QUANTITY, FOUR IMPLEMENTATIONS
| site | form | state |
|---|---|---|
| `INF_D_04:763-836` (firm header_metrics) | classified sum + unreconciled bucket | **FIXED + succession PROVEN** (unreconciled projection gap found by DS, fixed @fac59e6e15, serve-release #2 pre-13:47Z) |
| `INF_D_02:1941-1951` (advisor book block → book.json) | per-account else-bucket (match-fail → non-fee) | **THE $696K PRODUCER — unfixed** |
| `INF_C_08:251` (fee_efficiency gold → D_04 pass-through) | own computation, 0.0-defaults under fee_data_available:false | unfixed, pre-existing defaulting (DS-discriminated) |
| advisor-publisher Lambda (`summary`/`headline` back-compat blocks → summary.json) | its own split — serves **$15,471,205.77** for the SAME field name | unfixed; disagrees with book.json by 22× SIDE-BY-SIDE |
Two served artifacts carry the same field with values differing by 22×. **The retirement vehicle
must retire the CLASS, not one site — the archetype's one-producer-per-quantity atom, measured in
the wild.**

## FIX SHAPE (routed to DS via COO; the ratified succession bar extends)
D_02's else splits three-way mirroring the ratified D_04 form (classified non-fee = billing row
present + not fee-earning / unreconciled = no billing match, SEGREGATED and named); C_08's
defaulting made loud; the Lambda's redundant blocks superseded by the gold value (one producer);
acceptance = Patrick's served book shows $127,961.76-class non-fee + a named unreconciled line,
and summary.json/book.json AGREE.
