# FILED (post-NFRA) -- market-update feature is DARK / largely broken

**STATUS:** FILED, tracked, NOT worked now (non-NFRA; NFRA-first mandate holds). Assign the market-update feature owner + route the fixes when the NFRA wave clears.
**Source:** 0.5.0_AE_OpalETL, surfaced during the WRITE-root least-privilege behaviour-exercise (2026-07-09, 104629Z). Routing-not-repairing (a security change never silently absorbs these).
**Andrew:** the fabrication (#1) is a SEV2 CTO is flagging to Andrew (latent + discipline-win framing). The rest are operational.

## The whole feature is dark -- which plausibly explains why the secretsmanager:* on Resource:* exposure sat unnoticed across 3 firms.

1. **market-update-data-aggregator -- SEV2 latent data-integrity (fabricate-on-exception).** Route `/macro` (`fetch_economic_calendar`): on ANY exception (AccessDenied, network blip, FRED outage) it returns `get_mock_economic_calendar()` -- INVENTED CPI/FOMC/jobs events at HTTP 200 (`lambda_function.py:168-170` no-key path + `:244-246` bare-except), indistinguishable from real FRED releases. **FIX = fail-closed: ERROR / clear no-data state on any dependency failure, NEVER invent.** See [[feedback_fail_silent_fabricate_on_dependency_denial]].
   - **AMPLIFIER (why it's invisible):** the `print("Warning: ... returning mock data")` goes to NO log group -- `market-update-lambda-role` is implicitDeny on `logs:PutLogEvents` in us-east-1, its only logs grant is us-east-2 (wrong region), and the functions have no log group anywhere. Invisible by construction. **Fix the region/log-group too, else the fail-closed error is also unlogged.**
   - **PERVERSE PROPERTY:** failure makes the output look RICHER (healthy `/macro` = `{"events":[]}`; broken = populated fabricated calendar) -> a human reviewer concludes the system IMPROVED. Defeats human review.
   - LATENT: the read succeeds today (real empty-events), so no live fabrication -- but any denial fires it.

2. **market-update-generator -- DOWN (500).** `Client.__init__() got an unexpected keyword argument 'proxies'` -- the `openai`/`httpx` version incompatibility. Content generation returns 500. FIX = pin/repair the openai+httpx versions.

3. **market-update-exporter -- writes to a NONEXISTENT bucket.** Writes its PowerPoint to `opal-data-portal-s3`, which does not exist (HeadBucket 404, absent from `list-buckets`). CTO asked 0.5.0 to route this specifically. FIX = point at the correct bucket (do NOT create `opal-data-portal-s3` on the strength of a broken writer -- confirm the intended target first). Relevant to WRITE-root B2 (DDB/S3 scoping): B2 must NOT grant to a bucket that doesn't exist.

## Disposition
Post-NFRA: assign the market-update feature owner, route #1 (fail-closed + log-region fix), #2 (openai/httpx pin), #3 (correct export bucket). Until then: tracked here + CTO's SEV2 Andrew-flag on #1.
