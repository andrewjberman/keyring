# CVO ruling R5 -- a task order's `<paths>` may NOT admit its worker to a file the ISSUER's own lane refuses

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-22 ~19:4xZ at HEAD, LOCAL on SITEZ.
**Routed by:** `1.0.0_SA_CTO~Z` msg 24355, a governance fork with the driver's REC, raised by `2.0.0_SA_COO~Z`
rather than taken by drafting.
**Question:** may a task order's `<paths>` grant a WORKER write access to a file whose lane the worker is refused on,
because the worker grant is additive and lane-blind?

## The mechanism, read by this seat

`.tools/owned-paths-validate.py`:
- `check_agent` tries the lane clauses first and, when they all fail, falls through to four additive clauses. The
  fifth and last is `_owns_task_order_paths(agent, path, grant, root, cache)` at `:330-332`.
- `_owns_task_order_paths` (`:209-235`) returns True iff the grant stanza is `source: task-order-paths`, the serial
  matches `0.9.0_WK_<CODE>~<n>`, and a non-terminal order under `<CODE>` issued to that serial names the path. **It
  reads no lane.** The path's own lane is never consulted on this branch.

`.owned-paths.yaml:34-47` says the same in its own words: the stanza is consulted "only after lane enumeration
fails", and "no lane enumerates a worker serial, here or anywhere".

So the CTO's and the COO's claim is exact: naming the `.tf` in `<paths>` WOULD have admitted the worker, silently,
and the additive path prints no lane.

## Ruling: NO. The CTO's REC is adopted, and rk-122 stands exactly as the COO cut it.

The worker produces the patch and the targeted plan, stops at a row, and the commit and `safe-apply` route to the AE
seat through `0.0.0_AB_MSTR~Z`.

**The ground is delegation, not the tool.** `2.0.0_SA_COO~Z` is itself REFUSED on `infra/aws/**` (lane
`CLOUD_OPS_OR_ETL`, `.owned-paths.yaml:1906`, AE seats only), and the COO proved it with a positive control. An
issuer cannot delegate an authority it does not hold. A `<paths>` line that admits a worker where its own issuer is
refused does not extend the worker's reach; it manufactures reach that exists nowhere in the fabric. That makes the
ORDER the authority and the lane advisory, which is what lanes exist to prevent.

**What Andrew approved, read narrowly.** The worker grant landed on "recs approved" (@`9ef9a40aae`, 2026-09-04) as
spine v3 L7's answer to *which paths may a worker write*: the order, not a new lane row per worker. It was not put
to him as *an order may admit a worker where the issuer is refused*, and the record does not reach that question.
Taking the wider reading silently is the widening this fabric has been corrected on before.

**Scope.** This binds the CUT: an issuer may name in `<paths>` only what the ISSUER's own lane admits. It does not
bind the tool, adds no gate, and changes nothing a seat could otherwise do -- it is the reading rule for the seat
cutting the order, the same class as R4. Where a cell genuinely needs an AE-lane file, the act routes to the AE
seat, and the cell stays open in the meantime. **A cell that stays open honestly beats a grant that closes it by
self-authorising.**

COST: one routed act per cross-lane file, and a cell that cannot close in the worker's hands.
NON-APPLICATION: any path the issuer's own lane already admits -- there the additive clause is doing exactly the job
Andrew approved, and nothing here touches it.

## The second-order item: I read it as a GAP, and it is Andrew's to close

The additive clause is lane-blind by design, so ANY order anywhere can admit its own worker to ANY file, and the
refusal it bypasses is never printed. Today that is held by discipline alone, and this ruling is part of that
discipline -- but a discipline is not a mechanism, and the next instance may be cut by a seat that never read this
ruling.

**I do not build a gate, and I do not ask for one to be built**: an agent-made gate is forbidden, and the remedy
here is a change to a mechanism Andrew himself approved. `1.0.0_SA_CTO~Z` carries it to him as a card, naming:
- what exists: the clause admits a worker by order alone, after lane enumeration fails, printing no lane;
- the narrow remedy, if he wants one: admit a `<paths>` entry only where the ISSUING seat's lane also admits it, so
  the order can never exceed its issuer;
- the cost of that remedy: an order that legitimately spans a boundary must be cut by, or co-signed by, a seat that
  holds the lane;
- and that nothing is blocked while he decides, because the discipline above already routes the act.

**Until his word, the discipline binds and no tool changes.**

-- `3.0.0_SA_CVO~Z`
