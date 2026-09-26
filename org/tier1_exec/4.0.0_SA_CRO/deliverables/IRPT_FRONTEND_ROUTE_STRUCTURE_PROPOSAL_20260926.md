# Investor Reporting -- a frontend route structure for "search by client, Performance per account"

**Author:** 4.0.0_SA_CRO, 2026-09-26 ~15:4xZ, on Andrew-direct @`07c4b8b84e` (relayed by 1.0.0_SA_CTO msg 101269). The
CTO lands this as the DSGN_IRPTV1 PRD addendum; 2.0.0_SA_COO~D builds it in round 6.

**Built from three read-only traces** (this seat's `deliverables/`):
- `IRPT_PERFORMANCE_TAB_END_TO_END_GAP_BRIEF_20260926.md`
- `IRPT_HOLDINGS_TAB_END_TO_END_GAP_BRIEF_20260926.md`
- `IRPT_HEADER_IDENTITY_SEARCH_END_TO_END_GAP_BRIEF_20260926.md`

Evidence: `IRPT_FRONTEND_TRACE_EVIDENCE_20260926.json`, from 2.0.0_SA_COO~D's PROD walk HAR (sha256 `6b51023c...`) and
2.0.0_SA_COO~P's API walk log.

**Backend: taken as is (C4).** Every call below is already live on PROD and was measured answering. No new route,
field or contract is needed.

## 1. The facts the structure is built on (measured)

1. **Every directory entry is a client.** 436 of 436 sampled entries carry their own `client_id`, with none shared.
   Each entry's `ids.account_ids` equals the set its selection returns (3 of 3).
2. **The client's snapshot names its accounts.** `GET /holdings/{client set}` returns every account as a level-0
   `ACCOUNT` node, with a `display.label` and `drill_refs {ref_kind: ACCOUNT, ref_id}`: 5 of 5 accounts, 6 of 6
   snapshots. No other measured source names them: the directory account search named 0 of 5.
3. **Performance answers one account and refuses a set.**
   - Client-set requests: 4 of 4 `SELECTION_UNSUPPORTED`.
   - One-account requests (`POST /selections {ACCOUNT, [id]}` -> `accounts=1`, 5 of 5):
     - 49F: 2 computed and 2 `OBJECT_NOT_COVERED`;
     - INF: 1 `DEPENDENCY_UNAVAILABLE`.
4. **Holdings answers the client set.** 6 of 6 READY, with a deduplicated custody total.
5. **Narrowing today replaces the page's selection.** `index.tsx:145-188`: one `accepted` set feeds every tab, the
   identity card and Export.

## 2. The structure: one CLIENT context, and ACCOUNT focus that stays inside the tab

```
/investor-reporting
|
|-- R0  NO CLIENT       search + browse (clients only)            calls: resolve, search, browse
|
`-- R1  CLIENT          the page's unit of selection               calls: POST /selections {entry's own scope} ONCE
    |   (context)       identity card = the client, always          GET /holdings/{client set} ONCE -> accountList
    |
    |-- R2  HOLDINGS           client aggregate                     reads R1's snapshot (no second fetch)
    |   `-- R2a HOLDINGS/acct  one account, tab-local              POST /selections {ACCOUNT,[acct]} (cached)
    |                                                               GET /holdings/{account set}
    |
    |-- R3  PERFORMANCE        account chooser, always shown        no Performance request without an account
    |   `-- R3a PERFORMANCE/acct  one account                       POST /selections {ACCOUNT,[acct]} (cached)
    |                                                               GET /performance/{account set}?start&end
    |
    `-- R4  ANALYSIS           unchanged in this addendum           reads accountList for names (R1)
```

**Route state, not URL ids.** The route is a typed state object: `{ firm, client, tab, account? }`. It is not a URL
path, because the PRD rules that ids never print (a `client_id` or `acc_` id in the address bar would print one).
Deep links are parked (Call 2).

## 3. What each route does -- the frontend's paths

| Route | Holds | Calls (exact) | Never sends |
|---|---|---|---|
| R0 | firm, query text | `POST /directory/resolve`; `GET /directory/search?q`; `GET /directory/browse` | a selection |
| R1 | the client entry; `clientSetId`; `snapshot`; `accountList` = the snapshot's level-0 ACCOUNT nodes `{accountId via drill_refs, label, value}` | `POST /selections` with the ENTRY'S OWN `permitted_scope` (RELATIONSHIP / CLIENT / ACCOUNT, unchanged from today); ONE `GET /holdings/{clientSetId}` shared by the card and R2 | a directory account search (retired) |
| R2 | -- | none beyond R1 | -- |
| R2a | `accountId` | `POST /selections {scope_kind: ACCOUNT, scope_ids: [accountId]}` (idempotent: the same set gives the same `sel_` row); `GET /holdings/{accountSetId}` | a change to R1 |
| R3 | `accountId` or none | none until an account is chosen (Call 1 sets the default) | `clientSetId` to `/performance` |
| R3a | `accountId`, period | the same one-account `POST /selections` (cached per account and directory revision); `GET /performance/{accountSetId}?start&end` | `clientSetId` |
| R4 | -- | as today | -- |

## 4. The rules (each is a test)

1. **C1: search by client.** Every option, the browse drawer and the identity card say "Client". The entry's scope
   kind is carried, never shown (header brief, hop 2).
2. **C2: the client is the page's unit.**
   - R1 is set only by a pick and cleared only by a clear or a firm switch.
   - No tab control changes it: the Holdings filter and the card's account entries move a TAB's account focus, never
     `clientSetId`.
   - Clearing the client clears the card in the same render (header brief, hop 6).
3. **C3: Performance is per account.**
   - Every `GET /performance/{id}` pairs with a one-account `POST /selections`.
   - The account chooser renders ABOVE the answer gate, in every state (Performance brief, hops 2-3).
   - A one-account client opens R3a directly.
4. **One account list.** R1's `accountList` feeds the card's "over what", the Holdings filter, the Performance chooser
   and Analysis's included accounts. `IdentityCard.fetchIdentityCardData`'s directory search is removed.
5. **Export follows the tab's scope.** On Performance, the page Export targets R3a's account set and its report
   revision, never `clientSetId` (a client-set Performance export would carry a refused report). On Holdings it has no
   kind today (`EXPORT_KIND_BY_TAB`), as now.
6. **A refusal reads in words.** A one-account refusal (`OBJECT_NOT_COVERED`, `DEPENDENCY_UNAVAILABLE`) renders in
   advisor words, with the code one click away. `SELECTION_UNSUPPORTED` cannot occur under rule 3.

## 5. What this retires or changes in the current code

- `ReportingTab.tsx:171-193`: requests with the tab's `accountSetId`, not the page's `scopeRef.accountSetId`.
- `ReportingTab.tsx:245-249`: the account chooser moves out of the `answer && report` branch.
- `AccountFilter.tsx` and `IdentityCard.tsx:234-277` (`narrowToOneAccount`, `restoreFullSelection`, chip click): these
  become tab-local account focus and stop calling the page's `select`.
- `IdentityCard.tsx:118-143`: the directory account-name search is removed, and names come from R1's snapshot. The
  card's snapshot fetch becomes R1's one shared fetch.
- `IdentityCard.tsx:145-156`, `BrowseDrawer.tsx:272`, `ScopeSummary.tsx:81-82`: the kind word becomes "Client".
- `index.tsx:145-188`: `select` sets R1 only. `selectedScopeRef` splits into the client ref (R1) and each tab's account
  ref.

## 6. Calls for the CTO (each with a recommendation)

**Call 1 -- what Performance shows at rest for a multi-account client.**
- (a) The account chooser, with no request until one is chosen.
- (b) The largest account by the snapshot's value, preselected, with the chooser visible.

REC: **(b).** The page's progressive-disclosure law gives a tab one main picture at rest, and (b) always has one. The
chooser says whose figure it is, and a second account is one click away. The cost is one request the advisor did not
ask for. On a tie, take the first in snapshot order.

**Call 2 -- deep links.**
- (a) Route state only, in-page.
- (b) URL routes carrying ids.

REC: **(a) now.** An id in the address bar prints one, against the PRD's "ids never print". If deep links are wanted
later, they need an opaque, server-owned reference: the `sel_` set id already is one, but a client or account id is
not.

**Call 3 -- a client-level summary of per-account figures on Performance** (every account's YTD in one list). This is
n one-account requests, largest entry 70 accounts at 49F. REC: **parked** as an enrichment item. C3 is met without it,
and it is the only item here whose cost grows with the client's size.

## 7. Acceptance (one reconciled trace per case, deployed stack)

- **FWD-1 thread:** a 49F 3-account client -> R1 -> R3a (account 1, YTD, a computed figure) -> account 2 -> R2 (the
  client total is unchanged) -> clear (the card is empty).
- COT 2-account client -> R3a: each account's answer renders, including a provider-side refusal in words.
- An INF CLIENT-scope client and an ACCOUNT-scope client -> R1 -> R3a directly.
- A HAR census for each: every `/performance` GET pairs with a one-account `/selections` POST, and 0 `/performance`
  GETs carry the client set.

## 8. What this does not claim

- The directory facts rest on the walk's sample (436 entries: 207 of 49F's 4,548, 129 of COT's 258, 100 of INF's 292).
  They are not a full census.
- `CLIENT`-kind selection was not exercised at 49F or COT, so the structure keeps sending each entry's own scope.
- The served bundle's digest was not compared. The deployed behaviour is the HAR's, and source equals PROD `36a37afc`
  by diff.
- The walked 49F client's Holdings reads $0.00 over 3 READY accounts. That is not investigated here and is filed as a
  surprise row for the Holdings backend owner.
- Analysis (R4) was not traced.
