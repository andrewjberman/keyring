# Owned request reader review

Reviewer: `3.0.0_SA_CVO~Y`, September 22, 2026 Eastern.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Exact candidate: `e93300e34b6d4e3fafacf57a658415c69648d16a`.

Bounded result: **29 supplied tests PASS; ten independent scenarios, 16 recorded
checks PASS**. No new candidate defect found in those controls. Integrated
acceptance remains **0 PASS / 0 FAIL / 14 NOT_EVALUATED**.

## Executed boundary

`probe_owned_requests.py` archives the exact investor-reporting source,
contracts and firm registry into the ignored seat runtime directory, records
source SHA-256 values, and runs actual OwnedRequestReader, DynamoAcceptance,
ArtifactRepository and RetentionService with the candidate's storage/clock
fixtures. The synthetic reporting policy is ACTIVE only inside those fixtures;
no canonical policy is activated. Socket calls are forbidden in the independent
process and supplied test subprocess.

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_owned_requests.py --pin e93300e34b --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/OWNED_REQUESTS_e93300e34b.json
```

The supplied suite combines `ops/tests/test_owned_requests.py` (18) and
`intake/tests/test_retained_uploads.py` (11): **29 PASS**. The paired
`owned_request_history.json` fixture is regenerated/compared by the supplied
actual-reader test. These 29 are one denominator, not additive to previously
reported retained-upload runs. Actual pytest output, hashes, public responses,
query arguments and every independent outcome are in the evidence JSON.

## Independent scenarios

| Scenario | Observed result |
|---|---|
| Three owned records | One consistent query with Limit3; three public identities/timestamps match individual reads; no private record fields |
| Wrong principal | REQUEST_UNAVAILABLE with zero artifact port calls |
| Accepted identity has foreign tenant | ACCEPTED_IDENTITY_BINDING before artifact access |
| Foreign-owner first row and untrusted seek hint | Empty first page preserves continuation; changing one's seek key skips rows but returns only validated owned records; replay under another owner refuses before any query |
| First accepted record changes after third artifact read | Entire page refuses ACCEPTED_RECORD_CHANGED; three artifact reads confirmed |
| Exact retention expiry after third artifact read | Entire page refuses RetentionExpired; three artifact reads confirmed |
| Retention service removed after third artifact read | Entire page refuses RETENTION_SERVICE_REQUIRED; three artifact reads confirmed |
| Owned record missing composition reference | RETAINED_COMPOSITION_REQUIRED before artifact access |
| Backend returns more rows than requested limit | HISTORY_PAGE_EXCEEDS_LIMIT before artifact access |
| Foreign tenant in LastEvaluatedKey | HISTORY_CURSOR_KEY_BINDING; no page released |

The ten scenarios generate 16 evidence checks because pre-I/O zero-call counts,
cursor query counts and the last-blob schedule are recorded separately. They are
not 16 independent scenarios. The first complete execution passed; no probe or
candidate repair was needed.

## Limits

This primitive returns accepted identity and timestamp, not job status,
composition bytes or a released report. The principal is assumed to come from
the verified server boundary. The current-authorize callback, retained artifact
read and final record checks were exercised using offline fixture services;
HTTP authentication and deployed route composition remain unproved.

History performs one bounded query and may return fewer items than the requested
limit, including an empty page with a continuation. The cursor is intentionally
an untrusted seek hint. Its owner digest is not a signature and does not grant
access; each fetched record still undergoes validation. Request-key order is
not accepted-time order, and this primitive does not promise newest-first history.

All candidates undergo artifact I/O before the final metadata/access/liveness
pass. That closes the tested earlier-row changes during later artifact I/O.
The final checks are sequential, not an atomic page snapshot; there is no proof
of simultaneous grants/expiry across arbitrary concurrent metadata changes.
Offline doubles do not establish real Dynamo expression/transaction semantics,
IAM, deployed retention, process loss, browser reload or worker/report retrieval.

No full Y6/S4/S7 grade follows. All 14 integrated criteria remain NOT_EVALUATED.
No implementation source changed, live calls, deployment, policy activation or
push occurred. Push state LOCAL.

-- 3.0.0_SA_CVO~Y
