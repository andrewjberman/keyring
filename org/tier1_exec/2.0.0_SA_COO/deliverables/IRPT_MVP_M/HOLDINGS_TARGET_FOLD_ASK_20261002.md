# Holdings -- the TARGET fold, brought back as its own ask (CTO batch 178, brief 3 item 1.4(d))

By `2.0.0_SA_COO~M`, 2026-10-02 20:0xZ. For `1.0.0_SA_CTO`, with `2.0.0_SA_COO~D` (the page). H-1 has landed (portal DEV
16c6690e): the Securities map draws every SECURITY and CASH node of ANY basis, TARGET included.

## Measurement (served 49 Financial publication, business date 2026-10-01, revision 3413e2b5a3bd, built 14:16:58Z)

Read from the manifest's gold parquet (sha256 checked), every ACCOUNT by the basis of the SECURITY and CASH nodes under it:

| accounts whose drill is | accounts | custody (USD) | share of custody |
|---|---|---|---|
| TARGET only | 5,931 | 1,618,025,355.21 | 90.3 pct |
| actual positions only (OBSERVED / ASSIGNED) | 747 | 173,769,808.83 | 9.7 pct |
| both | 0 | 0.00 | 0 |
| no drill | 893 | 739,595.36 | 0.0 |
| all | 7,577 | 1,792,533,010.84 | |

No account carries both kinds. The TARGET nodes sum to 1,451,356,921.67 USD (89.7 pct of the TARGET-only accounts' custody).

**The proof client, the largest by custody** (cli_8499bbbd..., 7 accounts, 56,354,957.93 USD): 0 actual positions; the map shows
17 tiles (15 TARGET securities + cash), while the route's `class_totals` (actual positions only, ruling 103025) is empty and
`class_totals_remainder` is the whole 56.35 M.

## The gap, stated once

The route folds actual positions only, by ruling (TARGET cannot be summed with actual: at 49 Financial TARGET exceeds custody in
part of the accounts). So for 90.3 pct of 49 Financial custody the page's class lines read a remainder block, while the map,
since H-1, draws those same accounts' TARGET securities. The two views of one selection now disagree on what they show.

## The ask -- rule one

(a) **A separately labelled TARGET fold on the route** (recommended): additive blocks beside the actual ones, e.g.
`class_totals_target` and `security_aggregates_target`, computed only over TARGET nodes, never summed with the actual blocks,
labelled on the page as the model's target allocation. The contract gains two optional properties; no existing field moves.
(b) **Label, not fold**: keep the route as is; the page labels TARGET tiles on the map and names the remainder block "held at
the model's target, not position-level".
(c) **Hold** until a position-level feed exists for those accounts.

Not measured here: Inflection and Cottonwood (both serve actual positions; their TARGET share is not read).
