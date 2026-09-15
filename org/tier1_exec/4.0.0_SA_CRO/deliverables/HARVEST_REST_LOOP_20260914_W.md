# Local session-harvester to HTTP-consumer loop

**2026-09-15 implementation update:** the canonical five-publication local worker
now lives in `lib/opal_data_harvest/` (README, contracts, encrypted session vault,
worker and Windows schedule). This document preserves the earlier four-publisher
test record; its counts and WSJ route are historical. New live results are in
`.runtime/opal-data-harvest/runs/`. No all-publisher completion is implied by this pointer.

Author: 4.0.0_SA_CRO~W
Authority: ANDREW_DIRECT_20260914_HARVEST_METHOD_CORRECTION_W.md
Status: testing; three-ticker requirement NOT yet measured.

## Method

`harvest_local_session.py` runs a byte-identical runtime copy of each canonical headed harvester with its existing shared handlers. It requires network-auth corroboration and hands the local bundle to the matching existing REST consumer. No cloud parking, bucket writes, broad backfill, or scheduler. Browser content extraction is disabled as an execution path.

| Publisher | Canonical harvester | Canonical consumer | HTTP content contract |
|---|---|---|---|
| SA | sa_harvest_session.py | sa_rest_fetch.py | Residential proxy; account check and per-symbol news JSON. HTML body fragments normalized into text. |
| FT | ft_harvest_session.py | ft_rest_fetch.py | Residential proxy; authenticated GET returns server HTML. Inner article-content-body normalized into text. No JSON article endpoint established in its brief. |
| WSJ | None in established mechanism | wsj_rest_fetch.py | Bright Data Web Unlocker, zone one_shotter. Public HTML; full subscriber bodies not guaranteed. |
| Bloomberg | bloomberg_harvest_session.py | bloomberg_rest_fetch.py | Native HTTP. Quote API established; full news request parameters and article-body API still missing. |

The three consumer session constructors now accept an optional local bundle; omitted bundles preserve the existing Secrets Manager behavior. FT's flat cookie shape remains unchanged, with auth provenance in a separate sidecar. Failed sessions are archived locally and refreshed in the next publisher round.

## Run and review

```powershell
python org/tier1_exec/4.0.0_SA_CRO/scripts/harvest_rest_loop.py --rounds 1 --tickers VLO HAL BA COST HD INTU KMB --candidates 20 --trace-hold
python org/tier1_exec/4.0.0_SA_CRO/scripts/harvest_rest_loop.py --review-only
```

Each round attempts SA, FT, WSJ, Bloomberg for one ticker, then uses a different ticker. The driver inspects failures and changes the failed strategy between rounds. Completed publisher results persist, allowing an unfinished round to resume. A round limit bounds an invocation, not the overall goal.

Local artifacts: `.runtime/codex-seats/4.0.0_SA_CRO~W/harvest-rest-iteration/`. Session bundles, auth logs, raw content and reviews remain local. Separate state prevents browser experiments from qualifying this method. Every accepted set needs five unique URLs and five distinct body hashes, with explicit complete/relevant reviews checked against the current saved body bytes. Each publisher must pass three consecutive different tickers; publisher windows need not coincide.

## Corrected live evidence

- SA fresh canonical login: exit 0; three identity-cookie events from `/api/v3/login_tokens`. Its local bundle passed the REST account check. VLO news returned 20 records, 14 candidates and five reviewed complete bodies. The same session subsequently returned 13 HAL candidates through REST.
- FT fresh canonical login: exit 0; NopeCHA callback followed by network `FTSession_s` issuance. Its local bundle returned eight VLO article candidates via HTTP. Five complete bodies reviewed; standalone Recommended inserts removed, with originals retained locally.
- WSJ audited through its exact Unlocker function: an INTU response returned about 90 words against its embedded 955-word article metadata. That is incomplete content. Initial VLO loop failed before candidates; following runs retain sanitized status and response evidence for diagnosis.
- Bloomberg first canonical attempt: exit 1, no session bundle. Repeated early pixel-spike releases did not clear the challenge. Andrew observed draining and directed release, allow partial fall, then re-press. The next strategy disables early pixel-peak releases, records widget frames, and measures a partial fall while released before re-pressing. Authentication still requires its network/session oracle.

## Consumer repairs and validation

FT's former nested-div regex stopped at a byline; its fallback could return a subscription shell. The parser now scopes the inner content body and reports missing bodies for session/entitlement verification. WSJ's former all-paragraph regex included CSS; it now scopes returned article content and uses publisher word-count metadata to flag clearly partial responses. Parsing cannot recover text absent from the response.

Six REST regressions pass: local bundle without parked-session reads, FT nested content, FT subscription-shell rejection, WSJ CSS exclusion, SA related-footer exclusion, and stale review rejection. Eight existing hold/experimental-gate regressions also pass. Live complete content remains the acceptance evidence; these tests do not establish publisher reliability.
