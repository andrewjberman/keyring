# CVO Live-Exercise-Cert — SCTY PREMCP P1 C1/C2 (rate-limit + request-size cap): PASS

**Date:** 2026-07-07T08:22Z
**Agent:** 3.0.0_SA_CVO
**Deployed:** 0.7.0~A (commit 495b2b213, CTO-gate 080241Z) on the live gateway (box i-07dccb1615503ac99). L1-L3 closed; this = L4.
**Method:** LIVE on-box curl to 127.0.0.1:8080 -- exercised the actual middleware, not config-read. 6th SCTY control this session.
**Verdict:** PASS -- rate-limit + size-cap BITE live; the un-spoofable right-most-XFF keying is the load-bearing detail, exercised.

## Config defaults (sanity -- match the arch-gate)
RATE_LIMIT_ENABLED=True; MAX_REQUEST_BYTES=1048576 (1 MiB); RL_IP_AUTH=20/60s; RL_IP_GLOBAL=300/60s; RL_MCP_IDENTITY=120/60s. All env-tunable (no redeploy), kill-switch present.

## Exercises (live on-box)
- EX-A per-IP-AUTH 429 + UN-SPOOFABLE right-most keying (the load-bearing one): POST /token 23x with a VARYING left-most XFF (10.0.$i.$i) but a FIXED right-most (9.9.9.9). Codes: 400 x20 (endpoint), then **429 429 429**. The limit (20/60s) fires at the 21st -- AND a varying/spoofed LEFT did NOT create new keys (all 21 accumulated to the same 9.9.9.9 key). => right-most-XFF keying is UN-SPOOFABLE + the auth-limit bites. This is the security-load-bearing detail (a spoofed XFF-left cannot dodge the per-IP limit; the ALB appends the real client as the right-most).
- EX-B right-most DIFFERENTIATES: FIXED left (1.1.1.1), VARYING right (7.7.7.21-25) -> all 400 (non-429). A different right-most = a fresh key = fresh count. Correct keying (no false-accumulation across genuinely-different clients).
- EX-C 413-on-oversize: POST /mcp with a 1.3 MiB body -> **413** (the size cap bites at >1 MiB, deterministic Content-Length path).
- EX-D no false-throttle: /health -> 200; single legit requests pass.

## Honest scope
Live-exercised: per-IP-AUTH 429, un-spoofable right-most keying, size-413, no-false-throttle (the load-bearing behaviors). Covered by AE's lock-test tests/test_ratelimit.py 6/6 (not separately live-exercised by me): the per-identity /mcp 429 (needs a valid bearer -- mintable like P0, but the coarser IP-auth limit + keying + size are the load-bearing proofs) + the FAIL-MODES (auth FAIL-CLOSED, global+identity FAIL-OPEN on an induced limiter error -- a deliberate availability-vs-security split: an auth-endpoint limiter error denies (fail-closed), a general-traffic limiter error allows (fail-open, don't self-DoS)). Deploy-proof: on-box md5 == local (ratelimit.py/server.py/config.py); service active + /health 200 proves the middleware loaded (an import error would down it).

## Verdict
C1/C2 = PASS. The rate-limiter bites (per-IP-auth 429 at the limit), the keying is un-spoofable (right-most XFF -- a spoofed left can't dodge), the size cap bites (413 >1 MiB), and legit traffic is not false-throttled. L4 closes. 6th SCTY control (G1 + P0 + VA-sig + write-scope-L1 certified; L2-mechanism-certified/live-403-pending-human-login; C1/C2 now).
