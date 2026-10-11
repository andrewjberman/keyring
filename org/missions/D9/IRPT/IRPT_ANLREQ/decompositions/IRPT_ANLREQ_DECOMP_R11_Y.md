# IRPT_ANLREQ -- decomposition, round 11, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's round-11 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_ROUND_11_Y_20261011.md`
@6385a12ed2 (msg 5546), section 3, ENRICHMENT LIST, three items. No PRD addendum; the endpoint is unchanged.

**Thread:** FWD-1 is not live. This round finishes the evidence for release 5's return and builds the portal change that return owes.

## How the three items map to cells

- Item 1 (the census's DEV column re-read; the ticket page's reader added to the after-reads): cell `AR-y-111`.
- Item 2 (the apply order, cut when the precondition reads true, with the fallback's removal the same day): the apply order is the
  issuer's and is NOT a cell (it is cut when portal PROD carries `cbd5cc66` and `a3f99d6e`). The fallback's removal is a build that
  can be made now and held unlanded: cell `AR-y-112`.
- Item 3 (row D2-S34 and the four unpinned members): the composition-read half was DONE in round 10 (cell `AR-y-102`, merged
  @908c44ed5e: `Y102-BUILD-OK`, 16 of 16 pinned, no skip). What row S34 still holds is its second function,
  `irpt-intake-poller`: cell `AR-y-113`. The CTO is told this reading with the issuance.

## Cells

| cell | source | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-y-111` | analysis item 1 | the return census's DEV column re-read at the DEV head of this hour, one row per served member, and the Ticket Center's report reader named on each trunk with its two after-reads | the worker's deliverables only | LOCAL (reads of git refs; no live call) |
| `AR-y-112` | analysis item 2, CTO msg 5487 | on a portal candidate branch, NOT landed: the Ticket Center's report read makes ONE read with the ticket id; the fallback, its predicate and its tests are removed; a refusal as invalid input is shown after one read | portal `src/pages/TicketCenter/` | LOCAL |
| `AR-y-113` | analysis item 3, row `IRPT_ANLREQ-D2-S34` | the map entry of `irpt-intake-poller` builds its recorded digest with NO parity skip | `infra/aws/lambda/ci/lambda-source-map.json` (that one entry) | WORLD (the path's floor; one live single-resource read; nothing uploaded or applied) |

## Not cells

- The apply order for release 5's return and the landing of `AR-y-112`'s candidate: the issuer's, after the precondition and after
  the release's after-reads pass, in that order.

## Edges and chains

- No edge. `AR-y-112`'s candidate is HELD by its order's text and by the pair (section 6); nothing lands it this round. M = 3.

fanout: 3 of 3 chains, cap 8, reason: three independent cells with disjoint write sets.
