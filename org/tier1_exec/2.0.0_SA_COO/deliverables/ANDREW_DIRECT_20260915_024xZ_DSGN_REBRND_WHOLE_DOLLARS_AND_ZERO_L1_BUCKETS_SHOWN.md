# ANDREW-DIRECT 2026-09-15 ~02:4xZ -- DSGN_REBRND: AMOUNTS TO THE NEAREST DOLLAR; A ZERO L1 BUCKET (ALT STRATEGIES) IS SHOWN AS $0

**Terminal:** `2.0.0_SA_COO~D`, page-by-page mode. **Recorded by:** `2.0.0_SA_COO~D`, in the same turn. It arrived
while the ~02:2xZ changes (record @e71821c1df, portal 23f07d74) were being committed. It is about the Asset Category
Views figures on live data:
- the Client breakdown shows a near-zero "Opal-Unsupervised" amount with cents;
- the SMA breakdown hides "ALT Strategies" altogether, because it is zero.

## VERBATIM AND ENTIRE

> also client side make it round to the nearest dollar. we can also round to nearest dollar to 0 for ALTS Strategies,
> might as well show that as well if we're going to show $0 for Unsupervised Client when its 100% supervised client.

## WHAT IT SETTLES

1. **Amounts in Asset Category Views are rounded to the nearest dollar.**
   - A sub-dollar amount reads "$0", not "$0.47".
   - Amounts at and above $1,000 keep their scaled form (for example "$21.68M").
2. **A zero L1 bucket is SHOWN, as $0.**
   - ALT Strategies with nothing in it now appears, like Opal-Unsupervised does for a firm that is 100% supervised.
   - An L1 bucket is a fixed part of its category's split (ETF / ALT, Supervised / Unsupervised), so all of the split
     is drawn.
   - **This amends the L1 half of his 2026-08-28 presence rule** (D1_CATVIEWS TO-S1-DE, "named constituents at L1 and L2
     only appear if there is AUM associated"). Its null-is-zero reading stands, but a zero L1 bucket is now drawn as
     "$0" instead of hidden.
   - **L2 is not amended.** He named only L1 buckets. An L2 member the firm does not hold is still not listed (his Opal
     Fixed Income example).

## HOW 2.0.0_SA_COO~D APPLIES IT, AND SAYS SO

- **Rounding applies to every amount in this view** (both halves of his message name different categories), below
  $1,000 only.
- **The L1 rule:** once any sibling bucket carries a value, a null or zero bucket shows "$0". Where no sibling carries a
  value, the level is unmapped and every bucket keeps "--". That is the existing systemic-absence guard, unchanged.
- **Under a $0 bucket,** an L2 member with no amount is not listed, since nothing is held.
- **A $0 bucket has no width in a bar.** A bar still needs two positive parts to be drawn.

## WHAT IT DOES NOT SETTLE

It rules none of the seven open calls (@31f728cea4), does not close DSGN_REBRND and does not promote. The portal
freeze and the feature branch stand.
