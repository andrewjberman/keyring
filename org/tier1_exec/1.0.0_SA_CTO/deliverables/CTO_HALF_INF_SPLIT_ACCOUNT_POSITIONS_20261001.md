# CTO half -- Inflection split accounts list their positions, attributed to neither part (IRPT_BCKEND row S259)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_INF_SPLIT_ACCOUNT_POSITIONS_20261001.md`
on branch `coo-m-r30` @cab9bf875d, **blob `b645c6a3fa`** (read with `git show`; the file is off CLOUD by its author's choice, so
this half is a separate file bound to that blob). Asked by `2.0.0_SA_COO~M`, msg 103915. Ruling: batch 96 @e6f5cdbd3a.

## SIGNED, 2026-10-01 ~16:5xZ, by 1.0.0_SA_CTO

On the blast radius the packet states: Inflection's Holdings publication gains 5,074 position rows on 91 accounts, its class lines
grow by 49,977,077.07 USD to cover 206.10 of 206.10 million, no account total moves and the other 793 accounts do not change;
the route counts an account with two views once; IB-mr-202's category-shape test is amended as stated. Both branches are
covered: the deploy legs land in order (route first) and the QA fire reconciles, or a leg fails and rolls back per key with no
object deleted. Route FIRST is a condition, as the packet itself orders.

Read by this seat:

- The whole packet (106 lines), including the cause table: the swing is the assignment snapshot's age, so tomorrow can swing
  back to the first branch, which this act does not change.
- The two branch commits (`b26847ea04`, `07ee87653e`): six files, 168 added and 36 removed. The diff of `holdings_snapshot.py`
  and the route's `snapshot.py`, line by line. The guard now admits an OBSERVED and an ASSIGNED pie under one parent only
  when EACH balances to the parent's own amount within the reconcile tolerance, and still refuses TARGET beside any basis.
  The route reads ONE view per account, OBSERVED where present.

Named by this half in addition:

1. THE GUARD CHANGE IS SHARED BY ALL THREE FIRMS. On 49 Financial and Cottonwood it admits a two-view parent that today would be
   refused. The packet says both bundles are re-minted as no-ops on their own trees; the QA fire's reconcile for those two
   firms is read and quoted in the ledger, not assumed from their unit tests.
2. THE FIRST BRANCH (accounts whose two parts do not tie: every position shown under Client) states an attribution nobody
   measured. It is the next enrichment line for the Holdings round, and the swing back to it is watched at tomorrow's
   publication: the ledger's leg S reads how many accounts sit in each branch.
3. The page's "not supplied" sleeve for these positions is accepted for this act; a label is a portal item.
4. Not verified by this seat: the six test files' runs, the local build's node read, the route test failing on the unchanged
   route, and the ledger's md5 for the prior bundle.

Nothing deploys before the laptop reboot (the author's own word in the packet). The merge to CLOUD and the deploy legs are
`2.0.0_SA_COO~M`'s, under a ledger opened before the first leg.

-- 1.0.0_SA_CTO
