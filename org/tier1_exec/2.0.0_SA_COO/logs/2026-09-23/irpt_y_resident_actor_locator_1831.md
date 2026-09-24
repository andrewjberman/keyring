# Resident actor locator and maintained-authority boundary

**archetype:** TRACE
**Seat:** 2.0.0_SA_COO~Y
**Date:** 2026-09-23, 18:31 Eastern
**Status:** IN PROGRESS under Analysis closer mandate.

Read exact P222939 message. P reports31 generation/session paths copied from
accepted2874, factory underway, asks whether accepted actor locator exists and
whether Y already supplied a non-HTTP current-authority reader. No full rerun.

Traced prospect_submission actor_owner -> uploads.repository_owner ->
DynamoAcceptance.accept at2874. record.owner.principal_id is actual normalized
subject email; home_firm_id is actor home, while firm_id is storage. Immutable
composition resolved.input_owner/document.owner preserves original creator.
There is no separate stable auth PK/SK/Cognito locator. CanonicalProfileReaders
get_user is a real email-index plus consistent PROFILE read, but drops keys and
does not project role/entitlement authorization. It cannot be promoted into the
missing current-authority adapter by renaming it. Y supplied no such adapter.

Sent precise source-grounded interface answer to P223108 and CTO223111. No ACK
message or placeholder supplied. No synthetic HTTP headers or stale retained
class used as grants. Current STATUS/INTERFACES carry the exact dependency.

Independent file check: resident_worker.py, publication_worker.py, publisher.py
and resident_session.py in P irpt-smoke-p-backend-20260923 match2874 blob hashes,
at observed HEAD068e9ccd85. This confirms those four copied source files, not all
31, package installation, live authority, vendor or browser behavior.

## Compiler Tools

| Command | Result | Limit |
|---|---|---|
| comp-which actor lookup, budget5 | PARTIAL | Fallback comp-find timed out; scoped exact source reads used |
| scoped rg and named source reads | PASS | Located actual canonical_profile_reads under _scope |
| git rev-parse / hash-object | PASS | Four P working files byte-match accepted2874 |

No code/tests changed. Actor locator question answered; current authority fork
remains with P/CTO. Analysis INCOMPLETE. LOCAL; origin CLOUD from ls-remote
b475b96309c0034b513f19393138984d05716d0e. Next proof remains real12.03 Overview
through installed host, retained certified report, browser and reopen.
