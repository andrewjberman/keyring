# MDLP_MONPUB W2 leg C witness: PASS both halves -- W2 FAILING-DIRECTION BATTERY COMPLETE

**archetype:** VERIFY

**Serial:** `3.0.0_SA_CVO`. Window: 2026-08-03T1650-1655Z.
**Executor:** 0.2.0_DS_PortfolioAnalytics on DT's scratch bucket
`opal-313476888478-yang-qa-scratch`, per the CTO-ratified scratch-only ruling.

## Witnessed evidence (CloudWatch + S3, independently read)

**C-CONTROL (older date, no flag) -- PASS.** Invocation 672537d4... at 16:47:58Z: event log
explicitly names the SCRATCH bucket (the binding that distinguishes this refusal from leg A's);
`PublishGuardError` raised in-window at deployed `:354 -> :649`, same verbatim guard message
(incoming 2026-07-27 OLDER than served 2026-07-31 -- on scratch, "served" = the seeded fake
object, deliberately equal to live's vintage). The guard governs the scratch route, so the bypass
half has a live control beside it -- the pair is a real experiment, not a demonstration.

**C-BYPASS (same event + force_publish=true) -- PASS.** Invocation b32c7fc2... : CloudWatch
verbatim `[WARNING] ... FORCE_PUBLISH: monotonic publish guard BYPASSED by explicit
force_publish=true (incoming data_as_of=2026-07-27). Deliberate-rollback path.` Scratch key
flipped seed `2ad52d9f...` (28 B) -> `b5221b71e5c11ed92a14db34be827273` (19,221 B real payload,
body `data_as_of=2026-07-27` -- read it myself). The 28B->19221B flip shape also corroborates
that the control wrote nothing (the bypass flipped FROM the untouched seed).

**LIVE SERVE UNTOUCHED -- verified by me, not the executor:** all three production ETags
byte-identical to the 16:23:50Z pins (`e94c4f12...` / `c09e3e21...` / `84c4fec3...`).

## W2 battery: COMPLETE

| Leg | Mode | Verdict |
|---|---|---|
| (a) older-date refuse | EXERCISED-LIVE (direct invoke) | PASS @ff496d7621 |
| (b) passing direction | CLOSED (W4 publish @b16913d35e + organic 16:21Z user pull) | PASS |
| (2b) mid-build-crash zero-write | EXERCISED-LIVE (historical killer input) | PASS @ff496d7621 |
| (c) force_publish bypass + control | EXERCISED-SCRATCH | PASS (this log) |

W2 is witnessed complete under the as-exercised acceptance form (live legs live, bypass scratch,
explicitly scoped -- no over-claim). **W8's end-to-end handle_rollback legs are NOT covered by
leg C** (different entry point, per the requirement now in W8's acceptance text) -- the same
scratch environment serves that session when DT's plumbing lands.

**Scratch disposition:** keep the seeded environment + fixtures until the W8 witnessing session
(imminent; 7-day self-expiry is fine as backstop). Do not clean sooner.
