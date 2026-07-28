# ANDREW-DIRECT 2026-07-28 ~1741Z -- trace EVERY necessary channel: what feeds it, on what schedule, and is it reaching the Gold DDB

**Recorded by:** `2.0.0_SA_COO` - **Channel:** Andrew directly at the COO terminal
**Received:** 2026-07-28T174108Z (timestamp read from `date -u`, not inferred)
**Recorded + broadcast:** same turn, per `org/XXX.md` Andrew-direct protocol
**Sits under:** the ~1725Z priority ruling (canonical routes + schedules BEFORE monitoring, PRD s11 @`c60de93156`)

---

## VERBATIM

> "I agree with your framing, we need to trace every necessary channel, e.g. 0824 schwab and smartx buckets
> for 49F, and identify what feeds them on what schedule and make sure that they are getting to the Gold DDB
> table."

**NOT A PARAPHRASE. THE PHRASING IS THE RULING.**

---

## WHAT IT BINDS (surfaced, NOT adjudicated -- I am the receiving agent)

**1. IT RATIFIES THE BOUNDARY I PUT TO CTO AT 173813Z.** I had asked him to rule whether three items that
look observational under the ~1725Z monitoring-goes-behind test are in fact route PRECONDITIONS. Andrew's
*"I agree with your framing"* answers it directly: **establishing what a route IS, what feeds it, on what
schedule, and whether it ARRIVES is ROUTE WORK, not monitoring.** The gold-DDB stall is therefore not
sequenced behind the publisher -- **it is upstream of it.**

**2. THREE DELIVERABLE PARTS PER CHANNEL, and the third is the one nobody has done:**
   - **(a) WHAT FEEDS IT** -- the producer, named, source-confirmed.
   - **(b) ON WHAT SCHEDULE** -- and per NEVER#4, event-driven-with-no-schedule is a DEFECT, not a schedule.
   - **(c) IS IT REACHING THE GOLD DDB** (`opal-assets-daily-aua`) -- **arrival, not emission.** A producer
     that runs and a table that receives are two different claims.

**3. "EVERY NECESSARY CHANNEL." The 0824-Schwab + SmartX pair is an EXAMPLE, not the scope.** Do not narrow
to 49F. The channel set spans 49F (Schwab custody 0824, SmartX model + roster), Inflection (Eclipse model,
Orion custody), and Cottonwood (BlackDiamond allocations / holdings / unrealized / rebalancer models).

**4. IT TARGETS THE LARGEST OPEN ITEM FROM 07-28, WHICH CURRENTLY HAS NO OWNER.** Measured today by
`0.4.0_DS_ClientPlatform`: `opal-assets-daily-aua` carries **32 cohorts; a ROW census reports all 32 HEALTHY
at 2026-07-27; a VALUE census shows 13 stopped being fed on 07-21/07-22** -- **every AUA-bearing cohort,
including `_global__aua_total`.** The stall did **NOT** clear when the mdpf runner resumed 07-25/26/27, so
whatever feeds that table is **not** the mdpf runner and has been down ~4 trading days. **The emitter is
untraced and unowned.** Part (c) of this directive is exactly that gap.

---

## THE TRAP THIS DIRECTIVE WALKS INTO, STATED BEFORE THE WORK STARTS

**A ROW census on the gold DDB reports GREEN over a fully stalled table.** DS's first L2 pass did precisely
this and printed `HEALTHY` for all 32 cohorts; the rows exist at 07-27 and carry no values. **Part (c) must
be a VALUE census, per cohort, with the predicate printed** -- "is it reaching the DDB" answered on row
presence is the wrong question answered precisely, which is the ~1725Z ruling's own words one layer down.

**Second trap, measured twice today (once by me, once by DS): CONSTRUCTED PATHS RETURN A WELL-FORMED
EMPTY.** `opal-data-bd` vs the monolith, `blackdiamond/cot/` vs `blackdiamond/cottonwood/`, hyphen vs
underscore keys. **Enumerate prefixes from S3; never construct them.** A channel reported ABSENT on an
assumed prefix is not a finding.

**Third: a schedule read from Terraform is DESIRED, not APPLIED.** Row 13 today was a live gate reading a
deprecated bucket while the repo looked correct. **Ground schedules on the applied plane
(`aws events describe-rule` / `list-rules` paginated -- it caps at 100 and there are 141) and on the
producer's own run logs, not on the TF.**

---

## STATUS AT TIME OF RECORD

No work started. Broadcast to `1.0.0_SA_CTO` (arch gate + PRD owner) and `0.0.0_AB_MSTR` (record custody),
CC `3.0.0_SA_CVO`. This folds into the MDPF_DEBTCLEAN decomposition alongside D8 (per-channel bronze
schedule register across BOTH EventBridge surfaces) and the 171003Z deprecate-legacy directive -- **all
three point the same way and I am decomposing them as one pass, not three.**

-- `2.0.0_SA_COO`, 2026-07-28T174108Z
