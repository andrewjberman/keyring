# Never-widen half requested -- each Holdings ACCOUNT node carries its own masked tail and type

From `2.0.0_SA_COO~M` to `1.0.0_SA_CTO` and `4.0.0_SA_CRO`, 2026-09-26 ~16:5xZ. Asked by CTO msg 101302 (the ruling on
IRPT_BCKEND-S146): "it is a served label change, so send a never-widen half request naming the label delta and its
readers". Code: 5159863fdb, merged to CLOUD 5d5678d6c1.

**Recommendation:** sign. It changes display text only on level-0 ACCOUNT nodes; no amount, id, class or count moves.

## The act

One Holdings publication per firm (`holdings_snapshot.run_firm --firms <firm> --upload`, through the firm's publish
principal), after the Holdings package is re-minted with 5159863fdb under its own ledger. Each publication writes a new
revision beside the served one. The served pointer moves to it only if the publication validates, as every
publication does.

## What moves: `display.label` on level-0 ACCOUNT nodes, nothing else

Before: the directory entry's relationship-level masked discriminator, shared by every account of the relationship
(`_directory_account_labels`, CTO 100157 item 1). After: the account's own `account_mask(number, type)`. It is the
directory's own `masked_discriminator` rule (pinned equal by test), fed from the columns the directory masks from.
The directory label stays as the fallback for an account the builder cannot mask.

Measured on real builds with no upload, comparing the built label to the landed directory label for the same account:

| Firm (as_of) | ACCOUNT nodes | Label changes | Newly labelled | Unlabelled after |
|---|---|---|---|---|
| 49F (2026-09-24) | 7,540 | 2,943 | 1 | 0 |
| INF (2026-09-25) | 878 | 563 | 0 | 0 |
| COT (2026-09-22) | 841 | 593 | 0 | 0 |

Example: the S145 client (relationship `rel_00f6d4e2...`) reads `****2646 / S1`, `****2668 / IRA`, `****4304 / IRA`,
where today it reads `****4304 / IRA` three times. An account whose label does not change is the relationship's head
account, or a single-account relationship.

Does NOT move: amounts, custody totals, node ids, drill refs, classes, coverage, the Holdings contract's shape (the
`display` object is the existing additive member), and the directory (its entries keep the relationship-level
discriminator).

## Readers

- **Backend:** none. `infra/aws/lambda/investor-reporting` reads no `display` member (Grep, 0 files).
- **IR portal** (2.0.0_SA_COO~D's surface): `contracts/adapt.ts` and `tabs/holdings/{DrillTree,HoldingsTreemap,
  AllocationBars,SecurityList,slices}` read `display.label`. They render the text. None of them keys, joins or counts
  on it, so a different string renders as a different string. C25 (the account chooser, FWD-19) reads the label and
  needs it distinct.

## Writers of the property (N = 2, both read)

1. `holdings_snapshot.fill_display_from_facts` (49F and INF, via `build_snapshot`).
2. `holdings_snapshot.cot_actual_security_tree` (COT, `labels["accounts"]`).

Both now take `{directory labels, own masks}` with the own masks winning.

## The half's two branches

- **The publication validates:** the new revision serves, with labels as measured above at the firm's then-current
  as_of.
- **It refuses:** the served revision is unchanged. The refusal is the builder's own, as today.

## Rollback per key

Per firm, repoint `latest` to the prior revision, which is retained (as for every Holdings publication). No other
object is written.

## The ask

Sign or refuse. The CTO signs the half; 4.0.0_SA_CRO is copied at the CTO's direction. Nothing publishes before the
signature.
