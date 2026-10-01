# Never-widen half, IRPT_BCKEND row S259 -- an Inflection split account lists its positions, attributed to neither part

**Author:** `2.0.0_SA_COO~M`, 2026-10-01 (FAST lease `IRPT_BCKEND~M`). **For:** `1.0.0_SA_CTO` to sign the second half.
**Authority:** CTO rulings batch 96, INFLECTION-HOLDINGS-SPLIT-ACCOUNTS-20261001 items 2-6 (`RULINGS.md` @e6f5cdbd3a, msg 103859).
**Status of the act: NOT RUN.** Code on branch `coo-m-r30` @07ee87653e (`b26847ea04` + `07ee87653e`), not on CLOUD. Nothing is
deployed before the laptop reboot (Andrew-direct via msg 103892).

## The act, in three legs

1. **Merge** the two commits into CLOUD.
2. **Producer:** `safe-deploy --mint-bundle irpt_holdings_inf` from CLOUD (the bundle `irpt-holdings-refresh-lambda` runs at the
   14:15Z `irpt-holdings-snapshot` fire). Only Inflection's builder changes; the 49 Financial and Cottonwood bundles carry the
   shared guard change and are re-minted with it in the same act, each a no-op on its own trees (their tests pass unchanged).
3. **Route:** the `irpt-holdings` function (Terraform root `infra/aws/terraform/investor-reporting/holdings`, `main.tf:61`,
   by `safe-apply`; `lambda-source-map.json` already maps `snapshot.py` and is not edited), whose `project()` must count an account with two views
   once. **Order: the route goes FIRST.** A publication carrying split accounts read by today's route would count those
   accounts twice and fail its reconcile, so the page would refuse the selection (`SnapshotUnavailable`) -- a loud refusal,
   not a wrong number, but a refusal on a page advisors open.

## What the build holds (ruling item 3)

| item | how | evidence |
|---|---|---|
| (a) no position under the model line or the Client line | positions are emitted under the ACCOUNT; the Models line keeps only its MODEL_LEAF, the Client line has no child | `test_holdings_inf.py::test_split_account_keeps_membership_and_lists_its_positions_under_the_account` |
| (b) the account's dollars are not counted twice | THE TREE'S OWN SUM RULE, per (parent, basis): the ASSIGNED children (managed + excluded) and the OBSERVED children (the positions) each balance to the account on their own; `reconcile_before_after` already partitions by basis. The guard `assert_bases_not_spliced` admits two bases under one parent only in that case and still refuses a mix that balances only when added, and TARGET beside any basis. The route's `project()` counts one view per account (OBSERVED where present) | `test_split_account_is_two_views_and_the_dollars_are_counted_once`; `test_a_splice_is_still_refused` (four refusals); route `test_split_account_two_views_count_the_account_once`, which FAILS on the unchanged route (200 vs 100), and its control `test_a_spliced_split_account_does_not_reconcile` |
| (c) the firm's class lines cover these positions again | the positions are SECURITY nodes classified like any other; the route's `aggregate_selection` folds every OBSERVED/ASSIGNED SECURITY under the selection | route test above: class lines 70 + 30 = the account, remainder 0 |
| (d) the node says the feed does not state the part | each position carries the fact `part=NOT_STATED: ...`; both category lines carry "PART NOT STATED BY THE FEED" in place of "DRILL WITHHELD" | the first test above |

**An earlier ruling's test is amended, and named here for that reason.** IB-mr-202's shape test (CTO msg 102475) required every
account's direct children to be CATEGORY lines. Item 3(a) leaves no other place for the positions, so the test now admits exactly
one other direct child: an OBSERVED SECURITY carrying `part=NOT_STATED`, whose siblings of that kind sum to the account on their
own. Every other non-category child is still refused, and the category lines must still sum to the account.

**The page, read from its code (not walked):** the securities map shows these positions under "All" (no model chip names them,
since no model sits above them); the securities table lists them with sleeve "not supplied", an option the Sleeve picker
already offers; the category cards are unchanged (they read CATEGORY lines). A sleeve label for them is a portal item, not
part of this act.

## The cause, measured (ruling item 4)

The 89 accounts that turned split between the two publications, compared on the Eclipse values each publication read against
its own custody snapshot (2026-09-27 assignment vs 2026-09-30 custody; 2026-10-01 vs 2026-10-01):

| 2026-09-27 | 2026-10-01 | excluded value | managed value | accounts | custody USD |
|---|---|---|---|---|---|
| split, does NOT tie | split, ties | moved | moved | 51 | 30,263,786.86 |
| split, does NOT tie | split, ties | same | moved | 35 | 18,543,146.86 |
| excluded 0 | split, ties | moved | moved | 2 | 904,169.06 |
| split, does NOT tie | split, ties | moved | same | 1 | 11,962.86 |

On 2026-09-27 the gap |managed + excluded - custody| had a median of 2,642.82 USD and a maximum of 53,558.45, under 1 percent of
custody on 79 of the 89. **So the swing is the snapshot's age, and tomorrow can swing back:** a stale assignment snapshot sends
these accounts to the FIRST branch (`client_values_do_not_tie`: every position shown under Client, the model membership stated
only in the facts), a fresh one to the split branch. **The first branch has the same defect in the other direction** (it states
an attribution -- all of it Client -- that nobody measured) and is NOT changed in this act (item 4).

## Before and after (the one real run)

A local Inflection build of `holdings_snapshot.py` from branch `coo-m-r30` @07ee87653e (`--firms inflection --dry-run
--local-out`, no upload), 16:35Z-16:42Z, business date 2026-09-30, rc 0, against today's SERVED publication of the same business
date (revision b29682b06ab6, written 14:18:50Z), every node read:

| | served today | built with the change |
|---|---|---|
| accounts | 884, 206,098,981.92 USD | 884, 206,098,981.92 USD |
| security rows | 29,328, 156,121,904.85 USD | 34,402, 206,098,981.92 USD |
| accounts whose security rows do not sum to the account | 91 (49,977,077.07 USD) | 0 |
| category lines / model lines | 975 / 642 | 975 / 642 |
| class lines: equity | 101,697,547.62 | 131,674,679.27 |
| fixed_income | 48,834,761.15 | 67,022,764.18 |
| alternatives | 2,104,537.24 | 2,918,646.50 |
| cash | 1,823,401.19 | 2,389,630.83 |
| structured | 1,657,770.18 | 2,089,373.67 |
| commodities | 3,887.47 | 3,887.47 |
| unclassified | 0.00 | 0.00 |

- The 91 accounts: 91 of 91 carry their positions directly under the account (5,074 positions, 49,977,077.07 USD), every one
  carrying `part=NOT_STATED`; 0 "DRILL WITHHELD" notes remain.
- The other 793 accounts: 0 changed in amount, position count or position dollars.
- Category lines sum to their account on 884 of 884. The build's own reconcile: 206,098,981.92 before and after, accepted.
- After the change the firm's class lines cover 206.10 of 206.10 million USD (item 3(c)); today they cover 156.12.

## Rollback

Per leg: the route function to its prior version (Terraform, previous package); the producer bundle to the prior mint (its md5
is in ledger `secclass-bd-thread-r2-and-irpt-narrowed-m-20260930` leg H3); the publication is immutable per revision and the index
moves back with the next fire of the old bundle. No object is deleted.

## Acceptance

1. Route deployed: a QA projection of today's publication reads exactly as before (no account has two views yet).
2. The QA fire with the new bundle (`irpt-holdings-refresh-lambda {qa:true}`): the QA publication's 91 split accounts carry their
   positions; the firm's security rows sum to its account total; reconcile accepted.
3. Served: the next 14:15Z publication, and one walked Inflection account that is split reads its positions and its class lines tie.

**Ledger:** `irpt-inf-split-positions-m-<date>`, opened before the first deploy; legs R (route), P (bundle), Q (QA fire), S (served).

## COO half -- SIGNED (2.0.0_SA_COO~M, 2026-10-01 16:5xZ)

Signed on the blast radius above: Inflection's Holdings publication gains 5,074 position rows on 91 accounts and its class lines
grow by 49,977,077.07 USD with no change to any account total and no change to the other 793 accounts; the route counts a
two-view account once; IB-mr-202's shape test is amended as stated. Read at signing: the local build node by node against the
served publication, the four item-3 tests, the route test failing on the unchanged route, the cause table. I deploy only after the
second signature and after the reboot, route first, under a ledger opened before the first leg.

## CTO half -- NOT SIGNED
(Signed in a separate file: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_INF_SPLIT_ACCOUNT_POSITIONS_20261001.md` @07e4769540.)

## Addendum 1 (2.0.0_SA_COO~M, 2026-10-01 ~20:0xZ, at the deploy) -- one rider on the route, named as its own commit asked

The live `irpt-holdings` carries `snapshot.py` at pin 21eca74f40 (sha256 270b57c4.., read from the deployed zip). Between that
pin and this act's commit `b26847ea04`, the file gained `38b72bf469` (this seat, 06:46Z): the class remainder clamp
`max(residual, 0.0)` becomes `residual if residual > 0 else 0.0`, because `max(-0.0, 0.0)` returns -0.0 and a page would
print the minus sign. Its own message says it "rides the next move of irpt-holdings and needs to be named in that move's
half". Named here. VALUE DELTA = 0 on both branches: residual < -0.01 still returns None; on every other input the two
expressions return equal floats (-0.0 == 0.0), so only the sign of a zero changes, where the old one served -0.0
(`class_totals_remainder.amount.value` at Inflection and Cottonwood). No amount, weight or count moves. The source-map row
is re-pinned to `b26847ea04` (sha256 9f07f1b4..), which carries both commits.
