# First-hop review handoff

Fresh user screenshot at localhost:5174/investor-reporting shows unresolved firm and scope refusal. Three sanitized real-browser requests had bearer presence, HTTP 200, UNAVAILABLE / UNEXPECTED and no data. This is a live failure, not a cache-only or cosmetic diagnosis. No private identity or token retained.

At 2026-09-23T17:07:42Z AWS get-function returned irpt-directory-search last modified 06:26:25Z, 149956 bytes. The downloaded 17-member ZIP independently hashes to iqLKa1RWk9hlcSlAheuoAMgIY4R3VrStPX1eG5Qwq/s=. Both entry.py and served.py lack Global handling, which is present in the prepared source. resolve.py bytes are unchanged. The earlier BucketUnmapped diagnosis is consistent with this unchanged artifact but the new sanitized response does not disclose its internal exception.

## Minimal frontend scope repair boundary

Served clean 3b15871b is fac3b6a0 plus local CloudFront launcher/trace. Missing scope commits, in order: 09d5d5ea (Global context and tenant propagation), f0e7e362 (header selector and accepted selection propagation), 910ebf36 (strict parser correction). e0531491 additionally regenerates custody RequestComposition; it is not needed solely for initial directory bootstrap. Do not wholesale replace the live tree. Preserve the committed local launcher and sanitized tracing.

The exact changed src paths through 910ebf36 follow. This is the bounded existing commit set, not a newly tested cherry-pick into the live tree. The first 12 paths include production code plus generated-wire helper; tests/controls accompany them.

- `src/api/endpoints/investor-reporting.ts`
- `src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts`
- `src/pages/InvestorReporting/contracts/adapt.ts`
- `src/pages/InvestorReporting/contracts/directory-context.ts`
- `src/pages/InvestorReporting/contracts/envelope.ts`
- `src/pages/InvestorReporting/contracts/index.ts`
- `src/pages/InvestorReporting/contracts/wire/DirectoryContext.ts`
- `src/pages/InvestorReporting/contracts/wire/ResolvedScope.ts`
- `src/pages/InvestorReporting/contracts/wire/index.ts`
- `src/pages/InvestorReporting/contracts/wire/responses.ts`
- `src/pages/InvestorReporting/header/ClientSearch.tsx`
- `src/pages/InvestorReporting/index.tsx`
- `src/pages/InvestorReporting/tests/opal-scope/README.md`
- `src/pages/InvestorReporting/tests/opal-scope/context.test.ts`
- `src/pages/InvestorReporting/tests/opal-scope/mounted.html`
- `src/pages/InvestorReporting/tests/opal-scope/mounted.mjs`
- `src/pages/InvestorReporting/tests/opal-scope/server-wire.json`

## Paired backend compatibility

The UI must receive the closed DirectoryContext Global arm with explicit per-firm READY/UNAVAILABLE outcomes. It must retain strict ResolvedScope validation, partner home-firm locking, session cache isolation, and per-firm selected_tenant on browse/search/selection. Browser classification expresses intent only; signed edge-injected identity controls server authorization. Global is never a union report grant. Changing frontend alone cannot provide this backend behavior.

Measured existing source-only directory candidate differs from live by exactly these six members (all other 14 candidate members match live bytes):

- `entry.py`: CHANGED from `infra/aws/lambda/investor-reporting/directory/entry.py` at `d7b885b74ec7fb35c28e68a4692e45a4ba762fe7`.
- `served.py`: CHANGED from `infra/aws/lambda/investor-reporting/_authz/served.py` at `bc3727b3a37de412c48d70e3ece13fd7ed27aa6c`.
- `contracts/ResolvedScope.schema.json`: CHANGED from `docs/contracts/investor-reporting/v1/ResolvedScope.schema.json` at `bc3727b3a37de412c48d70e3ece13fd7ed27aa6c`.
- `owner_reads.py`: ADDED from `infra/aws/lambda/investor-reporting/_scope/owner_reads.py` at `bc3727b3a37de412c48d70e3ece13fd7ed27aa6c`.
- `custody.py`: ADDED from `infra/aws/lambda/investor-reporting/_scope/custody.py` at `bc3727b3a37de412c48d70e3ece13fd7ed27aa6c`.
- `contracts/DirectoryContext.schema.json`: ADDED from `docs/contracts/investor-reporting/v1/DirectoryContext.schema.json` at `bc3727b3a37de412c48d70e3ece13fd7ed27aa6c`.

This six-member delta is the existing candidate package closure, not an assertion that each member is intrinsically required by the bootstrap operation: served.py carries later owner-read imports, accounting for owner_reads.py/custody.py. A narrower earlier source set would need separate extraction and verification. Existing candidate evidence is source-only, not a deployable artifact or live acceptance. No broader generation/M publication ZIP repair is required to establish that the currently served bootstrap code is old.

## Requested direct review / next boundary

CTO: review this exact paired delta and identify the permitted local-tree integration and runtime publication route under the current hold. Per 5edf991c06 and message 170428, no local-tree wholesale replacement, cloud write or promotion was performed. Current CLOUD hold is preserved (170739 law notice states unchanged for IRPT contract v1.3). Deeper custody package corrections remain parked. After a reviewed paired runtime change, repeat the actual authenticated first hop before claiming S1 or any later outcome.
