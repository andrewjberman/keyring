# IRPT_BCKEND~M -- Holdings with the snapshot model overlay -- status

Seat `2.0.0_SA_COO~M` (CLAUDE). Contract
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`. Reviewer `3.0.0_SA_CVO` (not seated
at this write). As of 2026-10-01T04:4xZ.

Mode: FAST. Lease `IRPT_BCKEND~M`, `org/mcp/drive-mode.log` line 30, until 2026-10-01T12:31Z, on Andrew-direct
2026-10-01 ~04:2xZ (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`
@c48af273cc; CTO 103440). FULL -> FAST boundary run at 04:3xZ: no worker was running; nothing was cut (a round-30
cut of three orders was drafted and dropped uncommitted); the five stale Holdings orders are flipped `superseded`.
The pre-FAST long-form status is this file's previous git version.

Claim words: `measured` = read this session; `held` = cited from a record, not re-read.

## Pins

| What | Value | Claim |
|---|---|---|
| Working branch / worktree | `coo-m-r30` at `../coo_m_r30` | measured |
| CLOUD (local) / origin/CLOUD | c48af273cc / 0abf99fcd4 (ls-remote read 04:07Z) | measured |
| Holdings class source on CLOUD | IB-mr-291 @9fef6a7e9c: canonical `etf-classifications` first, declared bd-securities fallback | measured (code read) |
| Served Holdings packages | re-minted 2026-09-30 15:18-15:33Z, 44 members (one-window leg H3) | held (session log @9f8fd81494) |
| Port source | branch `wk-IRPT_BCKEND-84` @00b88da890, 12 ahead of CLOUD, NOT merged; read with `git show` | measured |
| investor_reporting suite at the base | SUITE-WHOLE 319 passed; holdings Lambda suite 147 passed | measured 04:2xZ |

## Live thread

State: LIVE END TO END for the Holdings tab at three firms (goal criterion 1), held from the 09-27 walk HARs; not
re-walked this session. First unproven hop today: the 14:15Z scheduled publication carrying the narrowed classes
(next-list item 4).

## Acceptance IDs (goal record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md`)

| ID | State | Evidence |
|---|---|---|
| (1) signed-in journey 49F / INF / COT | MET | held: ~D HARs w8 + w9 (09-27) |
| (2) every active 49F/INF account resolvable or refused explicitly | MET on the then-current directories | held: census @f247a922a5 |
| (3) COT soundness, window disclosed | NOT RE-READ; last read BROKEN (COT `CASH -- CASH` served as equity) | re-verify at item 4's publication |
| W2-11 per-security aggregate, W2-15 per-class totals served | NOT STARTED on CLOUD | item 1 |

## Write claims

- `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py::compute_holdings_aggregates` and its call sites.
- `data/assets/scripts/gold/investor_reporting/tests/test_holdings_aggregates.py`.
- `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` (two optional top-level properties).

## Next proof

Item 1: on the 291 base, a built Holdings document carries `security_aggregates` and `class_totals`, validates
against the docs contract, and equals the base document once the two properties are removed. Shown by
`tests/test_holdings_aggregates.py`, the whole suite, and one real local build per firm
(`R30_CHECKS/r30_aggregates_census.py`).

## Next-list, in order

1. **Aggregates port** (was IB-mr-261; CTO DECISION 103025): the producer serves one aggregate per security identity
   and one total per asset class. LOCAL build; the served move is item 5.
2. **Unclassified-by-name tests** (was IB-mr-271). Measured at CLOUD: `classify_security` (`:922-956`) already serves a
   ticker neither source knows as `unclassified` / `NONE` with no refusal, and `canonical_lookup` (`:866-871`) returns
   before any table call on an empty ticker. What is missing is the tests.
3. **Holdings Lambda restage** (was IB-mr-272) with `infra/aws/lambda/investor-reporting/holdings/stage.py`, after
   item 1's contract is committed. Measured: `stage.py --check` reads 3 of 4 members drifted (`errors.py`,
   `handler.py`, the contract). See Dependencies before landing it on CLOUD.
4. **H5** at the 2026-10-01 14:15Z `irpt-holdings-snapshot` fire: PHYS reads commodities / Metals on the Holdings
   page, and each firm's served CATEGORY names; then close the IRPT legs of ledger
   `secclass-bd-thread-r2-and-irpt-narrowed-m-20260930`. Goal criterion 3 is re-read on the same publication.
5. **Release of items 1-3** under a new never-widen half pair: the holdings Lambda redeploy with the restaged
   members, then the Holdings package re-mint, then the served read.
6. Carried from the pre-freeze list, not re-measured this session: the S173 re-point, the BD C_06 sealed-date
   reprocess (W41-S2), the COT cash-line act, COT-new Part 2, the COT B_01b deploy. Each is re-measured before it
   is claimed.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| `infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json` gains item 1's two properties | `2.0.0_SA_COO~P` (issuer of open order IRPT_DASHBD.TO-DB-b-4, whose `<paths>` hold `_contracts/`; the lease refused that surface) | the docs contract at item 1's pin | AWAITED: asked when item 1 has a pin |
| Leg F5 of ledger `irpt-service-principal-boundary-served-20261001` (the `irpt_holdings` function, graded on a member census against the BEFORE zip) done before item 3's restage is on CLOUD | `2.0.0_SA_COO~P` | the ledger file | AWAITED: read from the file |
| Both halves for item 5 | `1.0.0_SA_CTO` + this seat | the half item 1 writes | NOT YET ASKED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| "FAST from 2026-10-01T04:31Z; pins graded after the fact" (the boundary's one line to the CVO) | `3.0.0_SA_CVO` | a CVO is seated; it reads this row |
| MDPF_SECCLASS BD_THREAD_R3: both halves signed (@8769ffe8d5); the window is three live-read invariants | `2.0.0_SA_COO~M` | the 04:00Z BD gold run ends and the runner stops (running at 04:33Z); it must close before the 22:10Z silver fire and the 23:00Z gold fire |
| The served industry half of W2-13 (the canonical table holds no industry field) | `1.0.0_SA_CTO` | the canonical-table project rules it |
| NOT_READY vs NOT_FOUND for a selected account with no custody row | `1.0.0_SA_CTO` | the CTO rules |

## Limits

Nothing in items 1-3 is deployed or served; each is a LOCAL build until item 5's halves are signed. No product ID is
PASS until the CVO grades a pinned candidate. HOLD 103137 on a table-only class source is unchanged. The census in
item 1 reads the firm buckets, the table and served snapshots; it writes nothing to AWS.
