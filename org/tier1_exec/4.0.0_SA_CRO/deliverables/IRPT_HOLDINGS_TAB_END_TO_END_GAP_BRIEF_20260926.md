# Investor Reporting -- Holdings tab: end-to-end trace brief

Prepared by 4.0.0_SA_CRO on 2026-09-26. Read-only assessment plus proposed closure requirements; no application changes,
vendor calls, deployment or schedule activation. The route proposal is
`org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_FRONTEND_ROUTE_STRUCTURE_PROPOSAL_20260926.md`.

## Design finding

Holdings is the CLIENT's aggregate: the backend answers one snapshot for the client's whole account set, with a
deduplicated custody total and a drill whose level 0 is the client's accounts. That is exactly C2 ("a client IS the
aggregation of its accounts"), and it works on PROD.

Two frontend defects sit on top of it:
- its account filter never renders, because it takes its names from the same failed directory search as the
  Performance tab;
- narrowing to an account from any control replaces the PAGE's client selection, so the client stops being the unit of
  selection for every tab and the identity card.

The snapshot is also the only measured source that names the client's accounts. It should become the page's account
list.

## Current measurement

- **Deployed behaviour:** 2.0.0_SA_COO~D's PROD walk, 2026-09-26 13:59-14:14Z, HAR
  `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/prod-uiwalk-20260926.har` (sha256 `6b51023c...`).
- **Screenshots:** `prod-uiwalk-20260926.shots/w03-holdings.png`, `w04a`-`w06`, `w12a`/`w12b`.
- **Source:** portal `1e02be40`, the same as PROD `36a37afc` for these files.

Machine-readable evidence: `org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_FRONTEND_TRACE_EVIDENCE_20260926.json`
(`holdings`).

## Adapter map

| Firm | Endpoint | Measured | Gap |
|---|---|---|---|
| COT | `GET /holdings/{client set}` | 4 of 4 READY; 2 accounts, 2 of 2 account nodes named | account filter absent; narrowing is page-wide |
| 49F | the same | 2 of 2 READY; 3 accounts, 3 of 3 account nodes named; custody total and all 3 account values read 0.0 | the same, plus an unexplained zero total (see limits) |
| INF | the same | not walked | -- |

## Start-to-finish walk

### 1. Client set -> `GET /holdings/{id}` -- WORKS

What exists: `HoldingsTab.tsx:146-180` requests `getHoldingsSnapshot(scopeRef)` with the page's accepted client set.

Measured: 6 of 6 answered 200 READY. `custody_totals.unique_account_count` equals the selection's accounts (2 and 3),
`deduplicated: true`, and coverage 45/45 and 9/9.

Close: none.

### 2. Snapshot -> screen (summary and drill) -- WORKS, with one label defect

What exists: `HoldingsSummary`, `DrillTree`. The walk graded the drill total -> account -> sleeve -> model -> securities
as PASS (IVE13-AC4), and the asset-class colours as PASS (IVE12).

The defect: the level-1 pie labels both slices "Unknown" (IVE20-1, `w03`), while the table beside it names both
accounts from the same snapshot (`****8749 / ROTHIRA`).

Close: the pie reads the same `display.label` the table reads. Proof: `w03`'s pie and table agree.

### 3. Account list -> Holdings account filter -- MISSING at render

What exists: `HoldingsTab.tsx:226` mounts `AccountFilter`. `AccountFilter.tsx:94-95` renders `null` when
`overWhatFor(...)` has no NAMED account. Its names come from `IdentityCard.tsx:118-143`, the directory account search,
which returned 0 of 2 and 0 of 3 selected accounts in the walk (Performance brief, hop 4).

Measured: no account filter above the drill in `w03`.

Close: the account list comes from this snapshot's level-0 `ACCOUNT` nodes. Each carries a `display.label` and a
`drill_refs` entry `{ref_kind: ACCOUNT, ref_id: <account id>}`: 5 of 5 accounts, 6 of 6 snapshots. Proof: the filter
lists every account of a 2- and a 3-account client.

### 4. Account filter -> what it narrows -- MISMATCHED with C2

What exists: choosing an account calls `onNarrow(narrowToOneAccount(...))` (`AccountFilter.tsx:59-76`). That is the
page's `select` (`index.tsx:145-168`). It POSTs a new `ACCOUNT` selection and REPLACES the page's accepted set, which
every tab and the identity card read (`index.tsx:169-188`). `IdentityCard.tsx:234-251` narrows the same way from its
chips.

The exact mismatch: narrowing Holdings to one account makes the whole page one account: the identity card, the
Performance tab and the export target. The client is no longer the page's unit of selection.

Close: an account focus on Holdings is TAB-LOCAL. It creates its own one-account set (`POST /selections {ACCOUNT, [id]}`,
proven: Performance brief, hop 5) and reads `GET /holdings/{account set}`. The page's client set and the identity card
never change. Proof: after focusing an account on Holdings, the identity card still reads the client's total and
account count.

## Recommended completion sequence

1. **The live thread** is the Performance tab's: this tab's hop 3 supplies its account list.
2. A tab-local account focus (hop 4).
3. The pie labels (hop 2).

## Acceptance

One reconciled trace per case: client pick -> client set -> snapshot -> drill; account focus -> one-account set ->
snapshot -> drill; identity card unchanged. Cases: COT 2-account, 49F 3-account, a 1-account client, an account focus
then clear.

## Evidence anchors and limits

- **Not investigated:** the walked 49F client's snapshot is READY with custody total 0.0 and all three account nodes
  0.0 (HAR entries 256-257; `w13` shows "$0.00"). The frontend renders it faithfully, so it is not a frontend defect.
  Whether those accounts are empty or the value is missing is the Holdings backend owner's read; it is filed as a
  surprise row, not chased here.
- INF Holdings was not walked.

- `portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx`
- `portal/src/pages/InvestorReporting/tabs/holdings/AccountFilter.tsx`
- `portal/src/pages/InvestorReporting/header/IdentityCard.tsx`
- `portal/src/pages/InvestorReporting/index.tsx`

## Andrew-direct request -- verbatim record

Channel: the 1.0.0_SA_CTO terminal, relayed by msg 101269; record @`07c4b8b84e`, 2026-09-26 ~15:1xZ.

> "In essence what I'm telling you is that this is a design/presentation issue with regard to how frontend is trying to
> shape the results and the paths its using to do so, we need to adjust that design to be proper based on the facts of
> how performance reporting works at the account level, balancing this by the case that "client" is the aggregation of
> "accounts", and peoplewould only ever search by client, not by account."
