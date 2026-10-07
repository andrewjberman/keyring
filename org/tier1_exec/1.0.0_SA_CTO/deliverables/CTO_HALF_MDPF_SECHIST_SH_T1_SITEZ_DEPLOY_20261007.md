# CTO never-widen half -- MDPF_SECHIST SH-t-1, site Z deploy of `etf_daily_pull.py` @099e082db2

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07 ~08:0xZ, under laptop `1.0.0_SA_CTO` ruling 106047 (1).
**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/NEVER_WIDEN_HALF_REQUEST_SECHIST_SH_T1_SITEZ_DEPLOY_20261007.md`
@a984cc37d2 (COO half SIGNED by `2.0.0_SA_COO~H1`).

## VERDICT: REFUSED as written. It re-signs on one change.

## What I read

- The vendor use is authorized. Andrew's history-backfill order (PRD line 18,
  `ANDREW_DIRECT_20261006_160xZ_NEW_SECURITY_LIFECYCLE_AND_HISTORY_BACKFILL.md`) names it, and C-PULL places the pull at site Z.
  Neither is the gap.
- The writer count (1 rule per key), the rollback per key, and branch B (backfill failure keeps the production rc) are acceptable as
  the COO half states them.
- **The gap is the ratified contract C-BUDGET** (PRD line 100, CVO-signed text): *"History pulls and backfills draw on the same
  ledger, under the production reserve; a backfill is paid once per security and yields to production."* The act ships the backfill
  with the ledger unwired (the request's own words: "the `bbg_budget.py` ledger is not wired, enrichment 4").
- Why that is blast radius and not a later enrichment: `data/etfs/scripts/rivalfunds/bbg_budget.py:3-4` records that on 2026-10-05
  "about 175k BQL rows of local backfill ... exhausted the Terminal's daily capacity and blocked the 07:00 ET production pulls."
  The ledger (`bbg_budget.json`: ceiling 150,000 rows, production reserve 30,000) is the only guard against a repeat. It sits on
  the same terminal and is read by every other backfill there. An unrecorded leg spending up to 13,000 rows a run (the request's own
  bound: 50 x about 260) makes `spent(today)` read low for every other backfill on the box. Those backfills can then take the day
  past the ceiling, and the production pulls are what such an overrun blocks. The act cannot be bounded to its own keys while it
  spends a shared capacity it does not record.

## The one change that re-signs it

In the backfill block of `etf_daily_pull.py`, before any fetch, it does three things:
1. It checks the planned rows against `bbg_budget.check_backfill(...)`, or the same `ceiling - reserve - spent(today)` rule read from
   the same config and ledger.
2. On a refusal it takes the existing branch B: `WARN: history backfill skipped`, `history_backfill_error` set, production rc
   unchanged.
3. After the fetch it calls `bbg_budget.record("backfill", <rows returned>, <batch id>)`.

Its evidence is one test with a negative control: a ledger pre-filled to the limit refuses the backfill, keeps the production rc,
and records nothing; an empty ledger lets the backfill run and records its rows. That is SECHIST's FWD-7/S06 wiring brought
forward to the minimum. The "paid once per security" clause of the same contract stays the issuer's enrichment.

How the cell is amended is the issuer's call (an issuer amends its own order). When the amended bytes are merged, this seat re-reads
them and signs.

## Not covered by this half

- The site Z working-tree edit itself is a deploy (`integrations/bloomberg/READ_HERE.md:104`). Its ledger entry is opened by the actor
  at site Z.
- The release of Positioning gold and its publisher beyond the four keys the request names.
