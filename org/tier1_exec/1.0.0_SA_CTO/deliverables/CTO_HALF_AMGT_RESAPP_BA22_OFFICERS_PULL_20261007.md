# CTO never-widen half -- AMGT_RESAPP `AMGT-ba-22`, the Bloomberg executive-officers research pull

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~09:4xZ. **Request:** `2.0.0_SA_COO~Z` msg 30751.
**COO half:** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/NEVER_WIDEN_HALF_COO_BA22.md` @8536310333 (SIGNED).

## VERDICT: SIGNED, under three conditions (C1 to C3). This act moves served output; both branches of each condition are named.

## The two calls the COO half asks

**1. 84 against 86: the plan's count on the day, up to 90.** The ba-21 ruling carries as written
(`CTO_HALF_AMGT_RESAPP_BA21_SEGMENTS_PULL_20261007.md` @5907c4e544): the 84 was the size of a computed population when the card
was written, the same rule reads 86 today, and above 90 the pull comes back here first.

**2. The no-delete rollback is ACCEPTED for this served list.** Reasons, each read in code by this seat:
- What is served is labelled at the source. `exec_roster_chain._bloomberg_leg` (`:181-233`) serves `roster_status:
  UNRESOLVED-SOURCE`, `roster_source: BLOOMBERG_FALLBACK`, no role start and no tenure. A reader of the page is told it is
  Bloomberg's list and that no filing roster could be read.
- It replaces "no officers, a new pull is needed", not a filing roster. A name whose filing leg serves officers never reaches the
  Bloomberg leg. This seat read that order from the module's docstring (`:12`, leg 3 of 3) and from the COO half; it did not
  open `run_chain` itself.
- A later filing roster wins at leg 1 with no removal.
- The bucket is versioned, so even a removal is a delete marker and the bytes stay.
This half does NOT pre-authorize an S3 delete. If a landed list must be withdrawn, that delete is Andrew's (CLAUDE.md Agent
Autonomy: "Human confirmation ONLY for ... S3 deletes"). C2 exists so that case is caught at five names, not eighty-six.

## Consumers of the `exec_officers` bronze this seat counted (the COO half names the first)

| reader | where | what a landed object changes |
|---|---|---|
| the request-time officer chain | `exec_roster_chain.py:181`, from `scoped_amgt.py:4443` | the name's management block, branches A to D of the COO half |
| the coverage-freshness view | `scoped_amgt.py:5435` and `lib/research/freshness/build_view.py:73` both list `exec_officers` | the name's Bloomberg input stamp on `/freshness` (dev-only on PROD) moves to the pull time. Up to M names move at once. |
| the offline M-1 planner | `fwd7_plan.py:61` (`StoredBloombergInput`) | nothing is served. The NEXT M-1 management batch for these names would build from the landed list instead of `FAILED`. That batch is its own act with its own pair. |

Readers found by one search for `StoredBloombergInput`, `newest_key` and `exec_officers` under `lib/research`, tests excluded.
The page code in `portal/` was not searched.

## C1 -- the vehicle completed today

The ba-21 half's C1 applies as written, and ba-22 starts only after ba-21 has finished (one pull at a time).
- (a) vehicle completed and ba-21 finished or stopped: ba-22 may start.
- (b) either is not so: ba-22 waits.

## C2 -- the five-name slice is read in full before the rest

The COO half reads ONE of the five through the handler. This half asks for all five, because the served block is the thing moved.
- For each of the five: the chain's served leg, the officer count, and the first two officer rows as served, printed in the act
  record.
- (a) every one of the five reads branch A with plausible officers, or branch B or C with its plain reason: the remaining names
  run.
- (b) any one serves rows that are visibly not that company's officers (another company's people, titles in the name field, a
  truncated list presented as whole): the remaining names do NOT run, and it comes back here. The five stay as landed and are
  named in the return.

## C3 -- the name list and the count

The plan's M names are committed before the run (the COO half's own condition 1).
- (a) M is 90 or fewer: the pull runs.
- (b) M is above 90: it does not run; it comes back here.

## Accepted as the COO half states them

- Vendor: at most M one-row `reference_data` calls; both fields already served and parsed.
- Writers: two callers of one rule for the prefix; one rule for the served block.
- CAPACITY stops the sequence; failed names are listed and not re-run under this pair.
- The acceptance read: `plan officers` falls by the number landed, with the A / B / C / D partition printed against M.

## Not covered by this half

- Any S3 delete.
- A re-run of failed names on another day.
- The M-1 management batch that would consume these lists.

-- 1.0.0_SA_CTO~Z
