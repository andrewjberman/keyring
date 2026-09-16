# Andrew-direct: WSJ and Barron's subscriber harvesters

Seat: `4.0.0_SA_CRO~W`. Channel: direct Codex user message, 2026-09-14 Eastern; exact message timestamp unavailable.

## Verbatim nonsecret instruction

> I just set up a credential for WSJ and Barron's. Let's get scraper method set up for them in same fashion as we have done for the other harvesters. Credential should be saved in AWS Secrets Manager,

The remainder supplied the username and password. Credential values are intentionally redacted from this durable record and broadcasts.

## Execution

Created `dowjones/credentials` in AWS Secrets Manager, `us-east-1`; version `667be973-f297-400b-b4d1-5162b3c919db`. Readback equality verified without printing the value. Shared account; publisher-specific session bundles. This supersedes the previous subscriber-credential-pending state.

Prior direct instruction continues to govern collection: headful browser for session harvesting and API discovery, then HTTP/API article collection. Login, subscriber entitlement, complete article retrieval, and multi-ticker reliability are separate checks.

## Additional direct instruction: local canonical scheduler

Channel: direct Codex user message, 2026-09-14 Eastern; exact message timestamp unavailable.

> yes also make sure there is a lib or something in canonicl form inside opal-data-harvest that has the various tokens for each of these platforms as well as their api contracts + relevant code. The architecture should be the same self-healing cookie secural run from a stable server and then lambda rest api pulls, the only difference is that the stable server is this box, and the lambda api calls are also this box. i think this whole operation needs to be handled local on this device with some kind of local cron job that cycles through the various platforms for the various securities in a polite manner so no rate limiting. Then if there is a reauth needed that occurs during a scheduled run, the reauth is triggered for new bundle and immediately follwed by the relevant rest api pull, just like how our cloud process does it. I want you to design this process in pattern as I describe, once its done and implemented and functional across all harvest publications (the original 4 + Barron's), ping me.

Implementation scope: canonical `opal-data-harvest` library, five publisher contracts and session references, local scheduler and REST worker, paced collection, bounded reauthentication followed by immediate retry, durable progress and evidence. Credential/token values remain outside tracked code. Report completion only after live verification across all five publishers.

## JSON-first, with measured last-resort fallback

Direct Codex reply, 2026-09-14 Eastern; exact message timestamp unavailable:

> Try to get proper JSON. If there really is no clean JSON field available, then we can allow HTTP extraction, but it is a last resort.

Prefer native JSON APIs, then a complete structured JSON article field in an authenticated HTTP response. HTML body extraction requires a recorded JSON-route investigation and an explicit transport label; no browser DOM article collection.
