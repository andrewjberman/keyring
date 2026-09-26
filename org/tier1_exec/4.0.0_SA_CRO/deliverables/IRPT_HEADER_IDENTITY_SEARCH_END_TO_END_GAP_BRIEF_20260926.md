# Investor Reporting -- header, identity panel and client search: end-to-end trace brief

Prepared by 4.0.0_SA_CRO on 2026-09-26. Read-only assessment plus proposed closure requirements; no application changes,
vendor calls, deployment or schedule activation. The route proposal is
`org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_FRONTEND_ROUTE_STRUCTURE_PROPOSAL_20260926.md`.

## Design finding

Every directory entry the backend returns is a CLIENT:
- 436 of 436 sampled entries carry their own `client_id`, with no two sharing one;
- no relationship holds more than one client entry;
- each entry's `ids.account_ids` equals the account set its selection returns (3 of 3 selections).

What varies is the entry's `permitted_scope`: RELATIONSHIP (317; the 49F and COT norm), CLIENT (100; INF) or ACCOUNT
(19; one-account clients with no relationship). The search and selection mechanics are sound, and the page sends the
entry's own scope back correctly. But:
- the header names each client by that scope kind ("Relationship");
- it fetches the client's account names from a search that cannot return them;
- it keeps the previous client's total when the search is cleared.

## Current measurement

- **Deployed behaviour:** 2.0.0_SA_COO~D's PROD walk, 2026-09-26 13:59-14:14Z, HAR
  `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/prod-uiwalk-20260926.har`.
  - 3 `POST /directory/resolve`, 13 `GET /directory/browse`, 5 `GET /directory/search` and 3 `POST /selections`, all
    200.
  - Screenshots `w02`, `w02a`, `w03`, `w12b`, `w13`.
- **Firm ids:** `fir_0fe2a063..` = cottonwood and `fir_c9fc0465..` = 49financial (selection responses);
  `fir_b6b200b4..` = inflection (P's API log).
- **Source:** portal `1e02be40`, the same as PROD `36a37afc` for these files.

Machine-readable evidence: `org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_FRONTEND_TRACE_EVIDENCE_20260926.json`
(`directory_search`, `directory_entries_sampled`, `selections`).

## Adapter map

| Part | Endpoint | Measured | Gap |
|---|---|---|---|
| firm context | `POST /directory/resolve` | 3 of 3 200; GLOBAL context with 3 firms | firm tokens print on the body (IVE23) |
| search / browse | `GET /directory/search?q`, `GET /directory/browse` | client entries, 100 per browse page | kind word shown is the scope kind |
| pick | `POST /selections` (entry's own scope) | 3 of 3 200, account sets equal to the entries' | none |
| identity "how much" | `GET /holdings/{client set}` (the card's own fetch) | COT $287,274.21, equal to Holdings | stale after clear |
| identity "over what" | `GET /directory/search?q=<client label>&limit=<firm account count>` (the card's name fetch; its `kinds: ['account']` is not on the wire) | 0 of 2, 0 of 3 accounts named | wrong source |

## Start-to-finish walk

### 1. Page load -> firm context -- WORKS

What exists: `index.tsx:78-99` (two `resolve-scope` queries). Measured: 3 of 3 200 (`completeness: COMPLETE`).

Close: none. The firm-token print is hop 7.

### 2. Typed text -> client options -- MISMATCHED (label only)

What exists: `header/search.ts:111-130` (`toOptionRow`) sets `kind` from `permitted_scope.scope_kind`
(`contracts/adapt.ts:625`). `IdentityCard.tsx:145-156` and `BrowseDrawer.tsx:272` print it: "cottonwood --
Relationship", "49financial -- Relationship" (`w02`, `w03`, `w13`).

The exact mismatch: the entry is a client (its own `client_id`), and the label says "Relationship" or "Account" according
to the scope kind. C1 says the search asks for a client, never an account.

Close: every option and the identity card read "Client". The scope kind stays an internal carrier that is never shown.
Proof: no "Relationship" or "Account" kind word on the search list, the browse drawer or the card.

### 3. Pick -> client selection -- WORKS

What exists: `header/selectionRequest.ts:12-17` sends the entry's own scope (`RELATIONSHIP` + `relationship_id`, or
`CLIENT` + `client_id`, or `ACCOUNT` + the one id). `_scope/selection.py:87-103` resolves each kind to the union of the
entry's accounts.

Measured: 3 of 3 200, each account set equal to the entry's `ids.account_ids`.

Close: keep sending the entry's OWN scope. Do not switch everything to `CLIENT`: `CLIENT` is accepted by the backend for
any `client_id`, but it was not exercised live at 49F or COT.

### 4. Client set -> identity "how much" -- WORKS

What exists: `IdentityCard.tsx:118-125` fetches `getHoldingsSnapshot` for the page's client set. Measured: COT
$287,274.21 on the card equals the Holdings summary (`w03`).

Close: none. One snapshot should serve both the card and the Holdings tab. Today each fetches its own copy (HAR
entries 98 and 99, the card at the pick and the tab two minutes later).

### 5. Client -> identity "over what" (account names) -- MISMATCHED

What exists: `IdentityCard.tsx:126-140` searches `GET /directory/search` with `q` = the client's label and `limit` = the
firm's whole permitted-account count.

Measured: `limit` 843 (COT) and 7,576 (49F); 0 of 2 and 0 of 3 selected accounts named. The chips fall back to
unnamed, so they are not clickable (`IdentityCard.tsx:270-277`). The Analysis tab's nameless included accounts
(IVE20-5) are consistent with the same missing names; that was not traced here.

Close: the account list is the client snapshot's level-0 `ACCOUNT` nodes (5 of 5 labelled, with ids by `drill_refs`;
correction 16:4xZ: the labels repeat within a client until ~M's own-mask labels are served, so the value disambiguates), shared
with the tabs. The directory account search is retired. Proof: the card lists every account by name, and each entry
opens that account's Performance.

### 6. Search cleared -> identity -- MISMATCHED

What exists: the card's fetch runs only while `scopeRef` is set (`IdentityCard.tsx:322-335`), and nothing clears
`fetchedSnapshot` when the client is cleared.

Measured: "No client selected" beside the previous client's $287,274.21 (IVE20-3).

Close: clearing the client clears the card to its empty state in the same render. Proof: after a clear, the card shows
no total.

### 7. Firm context -> firm names on the body -- MISMATCHED

What exists: the card prints `scope.verifiedRequestFirm.displayName`, and the Holdings chip, the picker suffixes and the
firm menu print the same.

Measured: the firm TOKEN (`cottonwood`, `49financial`, `inflection`) prints on the body (IVE23-AC4, FAIL; `w02`, `w03`).

Close: firm display names from the firm catalogue, never the token. This is FWD-15 work already cut as IVE23; it is
listed here because it sits on this surface.

## Recommended completion sequence

1. **The live thread** is the Performance tab's. This surface contributes hop 5 (the account list) and hop 3 (unchanged).
2. Hops 2 and 6: the client label and the clear.
3. Hops 4 and 7: one shared snapshot and the firm names.

## Acceptance

One reconciled trace per case: typed text -> options -> pick -> client set -> card (who, how much, over what). Cases:
- a RELATIONSHIP-scope client (COT, 49F);
- a CLIENT-scope client (INF);
- an ACCOUNT-scope client;
- a clear;
- a firm switch.

## Evidence anchors and limits

- The directory statements rest on the entries the walk loaded: 436 unique entries, meaning 207 of 49F's 4,548, 129
  of COT's 258 and 100 of INF's 292. They are not a full census. "No relationship holds more than one client" holds in
  that sample only.
- `CLIENT`-kind selection was not exercised live at 49F or COT.

- `portal/src/pages/InvestorReporting/header/search.ts`, `selectionRequest.ts`, `IdentityCard.tsx`, `BrowseDrawer.tsx`
- `portal/src/pages/InvestorReporting/contracts/adapt.ts`
- `infra/aws/lambda/investor-reporting/_scope/selection.py`

## Andrew-direct request -- verbatim record

Channel: the 1.0.0_SA_CTO terminal, relayed by msg 101269; record @`07c4b8b84e`, 2026-09-26 ~15:1xZ.

> "... balancing this by the case that "client" is the aggregation of "accounts", and peoplewould only ever search by
> client, not by account."
