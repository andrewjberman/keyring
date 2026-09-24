# Cottonwood authenticated Holdings proof

Prepared by 2.0.0_SA_COO~M after CTO publication verification9709e10c59.
State: PREPARED, NOT EXECUTED. Native publication is independently verified; this
document does not assert installed reader, authorized API, or rendered screen PASS.
Do not republish the accepted snapshot while the runtime cutover is pending.

## Inputs and runtime prerequisite

- Publication receipt: COT_NATIVE_PUBLICATION_RECEIPT_20260923.json@5e29e43c2c.
- Account: acc_d486fc9455d6b2aa18e13af1, firm cottonwood; same account as P's
  positive Reporting example. Select by canonical ID, not a guessed display name.
- Accepted revision: fe328763b5da690cc1a48ca4681444f167386578f3f0dfadb45f195459906a4e.
- P supplies actual installed Holdings package digest, retained-selection configuration,
  and least-scope native versioned-reader/selection IAM cutover receipt. Compare those
  installed bytes against COT_HOLDINGS_INSTALLED_RUNTIME_20260923.json before testing.
- Use the ordinary portal adapter and real authenticated login. No injected fixture,
  fabricated authorizer event, manually supplied X-Firm-Id, or copied credentials.
  Browser inventory returned no enabled surfaces at preparation time; browser proof
  must be recorded when a real authenticated surface becomes available.

## Exact wire sequence

Grounded in current local portal src/api/endpoints/investor-reporting.ts
(observed worktree HEAD c70855f30dd9679e57bca403405a8839942e9115), createSelection
and getHoldingsSnapshot, and M holdings/entry.py. Worktree bytes, not HEAD alone,
were inspected. Requests use the existing authenticated transport and route base.

```http
POST /api/scoped/investor-reporting/selections?selected_tenant=cottonwood
X-Contract-Version: v1
Content-Type: application/json

{"scope_kind":"ACCOUNT","scope_ids":["acc_d486fc9455d6b2aa18e13af1"]}
```

Require a valid v1 selection response with exactly that selected_account_ids set.
Retain returned account_set_id, selected_account_set_fingerprint and directory_revision.
Do not derive account_set_id from the account or hard-code a prior selection reference.
Then issue, substituting only the returned URL-encoded account_set_id:

```http
GET /api/scoped/investor-reporting/holdings/{account_set_id}?as_of=2026-09-22&selected_tenant=cottonwood
X-Contract-Version: v1
```

The ordinary Holdings tab also needs its default request without as_of to resolve the
same accepted snapshot. Capture both when exercising the screen. Client cache keys use
the returned selection fingerprint/revision through the existing adapter. A selector is
not authorization; current server grants must cover the retained selection.

## API and screen acceptance

1. Record actual URL, HTTP status, v1 operation/envelope, correlation ID if present,
   installed package digest, and response timestamp. Keep credentials out of evidence.
   Reject ENVELOPE_STATUS, malformed envelopes, and any error disguised as empty success.
2. Response scope contains only the selected account. source_set_revision includes
   source irpt-accepted-holdings with the accepted revision above; do not confuse this
   publication revision with the viewer's directory revision or envelope cache revision.
3. custody_totals: unique_account_count=1, unique_position_count=57,
   total_market_value={currency:USD,value:19705844.84}. The published raw node sum is
   19705844.8433; compare raw precision before cent formatting, never sum parent values
   together with leaves. Node census: one ACCOUNT, one SLEEVE, 57 SECURITY nodes.
4. Show current value USD 19,705,844.84 and one selected account. Preserve custody/business
   date 2026-09-22 and overlay date 2026-09-23 separately. The frozen as_of_timestamp is
   2026-09-23T21:26:56Z; it is observation time, not a replacement custody date.
5. Models, SMAs and Client remain the public taxonomy. All this snapshot's observed
   position value is Client, with truthful unestablished model/SMA membership. Coverage
   is 0 resolved of 57 attempted positions, not zero holdings. Account assignment exists
   but does not establish position allocation. Do not turn targets into observed dollars.
6. Expand account -> Client -> all 57 securities. Confirm unique IDs, amounts, signed
   values, and parent/selected percentages against the accepted JSON. Client is 100%
   of this selected account; no duplicated money under Models or SMAs. Spot check CUSIP
   46090E103: USD83,715.52, raw parent/total fraction 0.004248258355107436
   (about 0.4248258355%). Complete census remains required beyond this spot check.
7. Reload, leave/reopen Holdings, and recreate the same selection. New selection IDs are
   allowed; account membership, accepted source revision, totals, dates and drill must
   remain consistent. Record visible screenshots and corresponding response evidence.
8. Verify a controlled non-covered selection/refusal through the ordinary authorized test
   surface. Do not alter real client grants merely to test revocation. If no suitable
   restricted login exists, mark that live arm NOT_EVALUATED and retain prior source tests.

## Evidence and limits

M records each arm PASS/FAIL/NOT_EVALUATED with actual observations in its owned evidence
folder, then hands the pinned result to CTO. P's package status is a prerequisite, not
M's API/browser result. Missing browser access and missing cutover each remain explicit.
This one-account publication does not cover arbitrary Cottonwood accounts. Other accounts
must remain truthfully unavailable until accepted, without borrowing this account's data.
49F, INF, multi-account/mixed membership and complete all-firm acceptance remain open.
