# DSGN_AMGTV1 round 37 -- CTO review of portal candidate 7f679aee (AV-zo-1), `1.0.0_SA_CTO~Z`, 2026-10-05 ~05:3xZ

**Input:** COO~D drain @07720859a5 (worker proof @c40a740ab9: repairs37 5 of 5 arms, battery29 ALL PASS). The round-37 list is
@9b2ed08fe2.

## Placement

- **Base:** the candidate's parent is `56b71adb`, but `origin/DEV` has since moved to `3e1aa46f` (COO~D's DSGN_REBRND density fix,
  ls-remote read). So the candidate is **not a fast-forward**.
- **Trial merge** onto `3e1aa46f` (`git merge-tree --write-tree`): **clean, 0 conflicts**. The push carries the merge, never a
  rebase.
- **Own diff:** 6 product files, +123/-38. All are in `src/pages/SecurityAnalysis/`: ChatterBubbles, LeadPanel, SecurityOverlay,
  cscTable, PeersTab and PostureTab.

## The three items

| item | read | verdict |
|---|---|---|
| FWD-21: bubble labels | A label sits wholly inside its own bubble or wholly outside every bubble. The old "touches only its own bubble" rule is kept only as the fallback when no strict slot exists. The collision test (`clear`) is unchanged. | PASS |
| FWD-8: no cross-currency average | A column is ONE, MIXED, UNSTATED or NONE over its member rows' SERVED codes. MIXED and UNSTATED print no average and say why in words ("Not averaged: currencies differ" / "currency not stated"), and each member figure in a MIXED column names its own code. Nothing is converted. | PASS |
| FWD-10: dated "no call" | The posture's own `as_of`, else its read's `as_of`, else the thesis read's `generated_at`. Nothing is printed when none is served. | PASS |

**FWD-8 checked against the producer**, since the page's honesty depends on what the producer serves:
- `lib/research/peers/csc.py` presents 5 columns. Price, Mkt Cap and EV are money; the two P/E columns are reciprocal and excluded.
- **Price** reads the row's own trading currency.
- **Mkt Cap** reads `cap_currency`, which for a model-block row is the security's OWN currency (`universe.py:527`, no FX applied).
  So the page reads that, not the map's "USD millions" label, and a KRW, TWD and USD group reads MIXED. That is correct.
- **EV** comes only from the scanner (USD millions, `universe.py:460`), so the map's USD statement is true for it.

## Non-blocking note (enrichment, not a hold)

`cscTable.ts` treats every non-reciprocal present column as money. That is true for all 5 of today's columns. A future non-money,
non-reciprocal column (a margin, for example) would read UNSTATED and silently lose its average. The cure is to key on a producer
money marker. Carry it on the next DSGN list.

## Verdict

**APPROVED for the DEV push**, as the merge of 7f679aee onto `origin/DEV` 3e1aa46f. The push itself needs Andrew's word, since a
product-file candidate needs it per push (CLAUDE.md Portal), unless he grants overnight standing DEV permission (card 1). Until then,
it is held at `0.0.0_AB_MSTR~Z`.
