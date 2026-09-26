# Investor Reporting -- Performance tab: end-to-end trace brief

Prepared by 4.0.0_SA_CRO on 2026-09-26. Read-only assessment plus proposed closure requirements; no application changes,
vendor calls, deployment or schedule activation. The proposed route structure for all three surfaces is
`org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_FRONTEND_ROUTE_STRUCTURE_PROPOSAL_20260926.md`.

## Design finding

Performance is an ACCOUNT fact (Andrew-direct, recorded @`07c4b8b84e`). The backend computes exactly one account per
request and refuses a set: `infra/aws/lambda/investor-reporting/performance/retained.py:77-80`, "performance computes
exactly one selected account". The frontend sends the CLIENT's whole account set, the same set Holdings uses. So every
client with more than one account gets a refusal. 43% of 49F entries, 68% of COT's and 70% of INF's are multi-account
(`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/RELATIONSHIP_PERFORMANCE_CARD_20260926.md` section 1).

The one-account path works end to end on PROD. The one account-choice control on this tab cannot render in the state
where it is needed, and the account names it would show are fetched from a place that does not hold them.

Worth keeping unchanged:
- the period controls and the availability gate;
- the request key binding (`ReportingTab.tsx:159-193`);
- the report body (headline, chart, heatmap, accounts table);
- the server-accepted narrowing path (`selectionRequest.ts:8-11`).

## Current measurement

- **Deployed behaviour:** 2.0.0_SA_COO~D's signed-in admin + Dev walk on PROD `36a37afc` (portal-v2.1.188),
  2026-09-26 13:59-14:14Z. HAR `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/prod-uiwalk-20260926.har`,
  sha256 `6b51023c...`, 350 entries.
- **Source:** portal source at HEAD `1e02be40` differs from `36a37afc` under `src/pages/InvestorReporting` and
  `src/api/endpoints/investor-reporting.ts` by one test file only (`git diff --stat`). The bundle digest was NOT
  compared.
- **One-account arm:** 2.0.0_SA_COO~P's API walk on the bounded Opal-class principal
  (`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/WALK_API_LOG_20260926.jsonl`, 03:20-03:28Z).
- **Not invoked by this seat:** no request, no login, no vendor call.

Machine-readable evidence: `org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_FRONTEND_TRACE_EVIDENCE_20260926.json`.

## Adapter map

| Firm | What Performance needs | Measured | Gap |
|---|---|---|---|
| 49F | a one-account set id | 4 one-account requests: 2 computed (`PERFORMANCE_PARTIAL`), 2 `OBJECT_NOT_COVERED` (an account the engine does not cover); 2 of 2 client-set requests (3 accounts) refused | the frontend never sends a one-account set for a multi-account client |
| COT | the same | 2 of 2 client-set requests (2 accounts) refused `SELECTION_UNSUPPORTED` | the same, plus the provider plan gate per account (backend, as is) |
| INF | the same | 1 one-account request answered `DEPENDENCY_UNAVAILABLE` (Orion; backend, as is) | the frontend part is the same |

One firm's success does not certify another's. INF and COT answers depend on provider plans that the frontend does not
change.

## Start-to-finish walk

### 1. Client pick -> page selection (`POST /selections`) -- WORKS

What exists: `index.tsx:145-168` (`select`), `header/selectionRequest.ts:12-17`. The page sends the picked entry's own
scope: `RELATIONSHIP` + `relationship_id` for 49F and COT entries.

Measured: 3 of 3 answered 200 with 2, 2 and 3 accounts, each equal to the entry's own `ids.account_ids`.

Close: none needed for this hop. The label is a header defect (header brief, hop 2).

### 2. Page selection -> Performance request -- MISMATCHED

What exists: `ReportingTab.tsx:171-193` requests `getPerformanceReport(performanceReportRequest(scopeRef, ...))`.
`scopeRef.accountSetId` is the PAGE's accepted selection (`index.tsx:169-175`), which is the client's whole set.

The exact mismatch: the frontend sends `GET /performance/{client set id}` with 2 or 3 accounts; the backend accepts
exactly one. Measured: 4 of 4 answered 200 `ok:false`, `UNAVAILABLE`, `SELECTION_UNSUPPORTED`.

Close: Performance never sends the page's client set id. It sends a one-account set id that the tab creates itself
(hop 3). Proof: in a new walk, every `GET /performance/{id}` pairs with a `POST /selections` of `scope_kind: ACCOUNT`,
one id.

### 3. Account choice on the Performance tab -- MISSING

What exists: `ReportingTab.tsx:245-249` mounts `AccountFilter` INSIDE the `answer && report` branch (`:224`). A refused
report takes the `StatusPanel` branch (`:267-268`), so the filter cannot render in the only state where it is needed.
Even when mounted, `AccountFilter.tsx:94-95` returns `null` when no account is NAMED (hop 4).

Measured: `[data-slot*=account-filter]` is absent on Performance for a 2-account and a 3-account client (walk IVE21,
FAIL), and screenshot `w13-49f-performance.png` shows only the refusal and a "Contact support" button.

Close: the tab owns an account chooser that renders ABOVE the answer gate, from the client's account list (hop 4), in
every state. A one-account client goes straight to that account. Proof: the chooser is present on a refused, a
partial and a complete report.

### 4. Account names -> chooser -- MISMATCHED

What exists: the chooser's names come from `IdentityCard.tsx:118-143` (`fetchIdentityCardData`). That searches
`GET /directory/search` with the CLIENT's label as `q`, and `limit` = every account the viewer's firm permits.

The exact mismatch:
- the directory holds ACCOUNT entries only for single-account clients: 19 of 436 sampled entries, 0 covering a
  multi-account client's accounts;
- the walk's name searches asked for `limit` 843 (COT) and 7,576 (49F) and returned 0 of 2 and 0 of 3 of the
  selected accounts;
- the holdings snapshot the page already fetches for the same client carries every account as a level-0 `ACCOUNT`
  node, with a non-generic `display.label` and a `drill_refs` entry of `ref_kind: ACCOUNT` naming the account id:
  5 of 5 accounts across both clients walked, 6 of 6 snapshots.

Close: the client's account list (id, label, value) is read from the holdings snapshot's level-0 `ACCOUNT` nodes, the
only measured source that names them; the directory account search is retired. Proof: the chooser lists n named
accounts for an n-account client.

### 5. One-account set -> Performance -- WORKS (backend, as is)

What exists: `_scope/selection.py:77-104` accepts `scope_kind: ACCOUNT` with the exact ids ("The caller can explicitly
choose a subset by submitting ACCOUNT IDs instead").

Measured: 5 of 5 `POST /selections {ACCOUNT, [one id]}` returned `accounts=1`. Performance on them: 49F 2 computed
(`PERFORMANCE_PARTIAL`) and 2 `OBJECT_NOT_COVERED`; INF 1 `DEPENDENCY_UNAVAILABLE`. The non-computed answers are the
backend's per-account coverage and provider facts, which stay as they are and must render in words (hop 6).

Close: none on the backend. The frontend reuses this exact call.

### 6. Refusal -> screen -- INCOMPLETE

What exists: `StatusPanel` prints the public reason code. Screenshot `w13` shows `SELECTION_UNSUPPORTED` on the body
(walk IVE20-2, FAIL).

Close: once hops 2-4 land, the client-set refusal cannot occur. Any remaining refusal (for example, provider coverage)
reads in advisor words, with the code one click away as on the other tabs.

## Recommended completion sequence

1. **The live thread.** One 49F multi-account client, admin + Dev login, PROD:
   - pick the client;
   - open Performance and choose one account;
   - read the YTD figure;
   - switch to the second account.

   It is one trace artifact. It crosses hops 1-5. The shared first hop (auth, scope, selection) is already WORKS. The
   frontend owner is 2.0.0_SA_COO~D (DSGN_IRPTV1 round 6).
2. The same journey at COT, where the provider plan gate answers per account.
3. The advisor-words refusal (hop 6) and the account chooser at 390 px.

## Acceptance

One reconciled trace per case: client pick -> client set -> account chosen -> one-account set -> Performance response
-> rendered figure. Cases:
- 49F x {1-account client, 3-account client} x YTD;
- COT x 2-account client x YTD;
- INF x 1 client (expecting a provider-side refusal, rendered in words);
- switching accounts;
- clearing the client.

## Evidence anchors and limits

Workspace CLOUD at this commit's parent; portal `1e02be40` (IR sources equal to PROD `36a37afc` bar one test). Verified
fresh: the HAR census and the source lines above. Not verified: the served bundle's digest; any walk after 14:14Z; the
INF and COT per-account plan behaviour beyond P's API log.

- `portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx`
- `portal/src/pages/InvestorReporting/tabs/holdings/AccountFilter.tsx`
- `portal/src/pages/InvestorReporting/header/IdentityCard.tsx`
- `portal/src/pages/InvestorReporting/index.tsx`
- `infra/aws/lambda/investor-reporting/performance/retained.py`
- `infra/aws/lambda/investor-reporting/_scope/selection.py`

## Andrew-direct request -- verbatim record

Channel: the 1.0.0_SA_CTO terminal, relayed by 1.0.0_SA_CTO msg 101269; record @`07c4b8b84e`, 2026-09-26 ~15:1xZ.

> "Performance is always going to be account-level, not client level. To me, this is just a frontend code issue rather
> than a backend data issue. I think we need to have a 4.0.0_SA_CRO agent run a /closer trace on several surfaces: 1.)
> The Performance tab, 2.) The Holdings tab, 3.) The header/identity panel and the adjacent search function. We need to
> take that data and come up with a refined route structure to manage this, on the frontend specifically."
