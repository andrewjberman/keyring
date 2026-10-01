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

## Before and after

PENDING the one real run (a local Inflection build with the change, started 16:3xZ): per-firm totals, the 91 accounts' security
rows and dollars, the class lines, and a node-by-node diff against today's publication showing no other account changes.

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

## COO half -- NOT SIGNED (signed when the before/after section is filled)

## CTO half -- NOT SIGNED
