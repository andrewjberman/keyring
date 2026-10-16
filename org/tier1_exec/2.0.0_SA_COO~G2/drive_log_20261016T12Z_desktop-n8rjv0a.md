# Drive log 2026-10-16 12Z -- 2.0.0_SA_COO~G2 (IRPT_YCDGEN and IRPT_ANLREQ workstream G)

Lease: FULL on both. Keep-driving empty_tick=on. Cadence 30m (:23 and :53).

| project | limb | round | TOs t/T | cells c/F | thread | act fired |
|---|---|---|---|---|---|---|
| IRPT_ANLREQ ~G | the release leg for the door checker (r34d rolled back; r34e in build) | 37 (AR-g-122/123), 38 (AR-g-124), 39 (AR-g-125), 40 (AR-g-126 issued) | R37 build merged, apply rolled back; R38 read done; R39 fix merged; R40 build running | each round covered | n (run 3 on HOLD until a ledger CLOSES with V2S OK) | DRIVE FORWARD |
| IRPT_YCDGEN | engine release train (see ANLREQ ~G) | -- | -- | -- | n | none own |

Acts this window (12Z), in order:
1. 12:02-12:08Z: CTO signed the r34d pair on COO blob 60cf9b70bc (commit b8554e2112); GO to AQ2 for TO-APPLY-R34D (every script as root).
2. 12:20Z: AQ2 applied r34d and ROLLED IT BACK the same session (msg 9343): V1 green, but V2 in the service's own environment read SPY KEPT and ZQXWVK CHECK_FAILED EXCEPTION. Host back on r34c, r34d root and 3 S3 objects kept. CTO (msg 9345): read the real exception class before any r34e; no guess-fix.
3. Round 38 (AR-g-124): ordered the read-only probe TO-READ-EXCCLASS (script probe_exc_class_r34d.sh, sha256 5962d92a...e8c5, offline test 11 cases). AQ2's record EXCCLASS_READ.txt (6395c4000d), MEASURED in the service: ZQXWVK raises curl_cffi.requests.exceptions.HTTPError "HTTP Error 404: " from yfinance's info fetch (quote.py:612 _fetch_info, models.py:167 raise_for_status; code 0, status and URL on exc.response); the r34d checker answered not-missing, EXCEPTION. SPY: no exception, 22 rows. My r34d miss: the fix matched only yfinance's own classes.
4. CTO msg 9354 approved the r34e rule with one tightening: no rows ONLY for YFTickerMissingError by name, or a curl_cffi HTTPError whose exc.response.status_code is 404 and whose URL is Yahoo's quoteSummary endpoint naming THIS symbol; everything else CHECK_FAILED.
5. Round 39 (AR-g-125): the issuer's checks (build, guard, regress, scope) with curl_cffi 0.13.0's real exception classes (fixture: exceptions.py and const.py byte-exact from the approved wheel, packaged as .pyfix because the lint gate rewrites third-party .py); reference fix passes, five mutants each fail. Worker 260 built it; I re-verified and merged 5e7fe11fc8.
6. r34e tooling forked from r34d (names r34e, over the running r34c root); trial build at pin f9f851d215: 314 members, 3 changed, tar a96fbfb7...9227, AR-G126-OK. The V2 script (v2_service_env_r34e.sh) prints the exception's class, MRO, status and URL without its query on any CHECK_FAILED, and runs four no-Yahoo in-service controls (one NOT_KEPT, three stay CHECK_FAILED) on ~Y2's ask (msg 9365); offline test 14 cases. Round 40 issued (d0608d1254): AR-g-126 build, worker 261 running.

Waiting on: worker 261's build. Next: verify and merge, packet, CTO half, then AQ2's TO-APPLY-R34E (AR-g-127) with the V2 in the service environment.
Messages acked: 9336, 9343, 9345, 9352, 9354, 9365.
Push state: origin box/dell2 read 2e2fe17b25 at 13:08Z; this seat's 12Z-13Z commits are LOCAL.
