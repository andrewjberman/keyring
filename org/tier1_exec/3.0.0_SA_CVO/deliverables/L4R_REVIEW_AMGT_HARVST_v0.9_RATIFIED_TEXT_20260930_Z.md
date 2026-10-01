# L4-R ratified-text review -- AMGT_HARVST v0.9 @e1b5fd6d8c (CONTRACTS only: `C-HV-TRUST-TOKEN`)

**Reviewer:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~13:1xZ - **Asked by:** CTO~Z msg 27158
**Span:** from this seat's own signed bytes (v0.8 @`b56263c6a5`) to `e1b5fd6d8c`. The ENDPOINT hash is `974dada544a2` at both, so there
is **no ENDPOINT change**. One addition: `C-HV-TRUST-TOKEN`.

## CHECKS

1. **Faithful to Andrew's words.** Record
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_125xZ_OPEN_CALLS_RECS_APPROVED_TRUST_TOKENS_BACKOFF.md`, read
   in full. Each of the contract's four bullets maps to a quoted clause of his:
   - "credentials for everything in AWS Secrets" -> read from Secrets Manager, never asked of him, typed or harvested;
   - "use existing trust tokens secured from past runs" / "Crawling is only necessary if existing trust tokens are not working" ->
     token first, crawl last;
   - "Important to not confuse rate limit for trust token expiry" -> 429/throttle backs off and keeps the token; only a persistent
     401, or a 403 whose kept body says the session is invalid, marks it expired;
   - "recommend a retry backoff for the REST API hits" -> bounded exponential backoff with jitter, each attempt written to the run
     record.

   No clause is added beyond them. **One modal shift, recorded not refused:** Andrew wrote "recommend" for the backoff, and the
   contract makes it a requirement. That is the PRD owner adopting a recommendation, which is within the CTO's authority, and the
   record says so ("lands as PRD CONTRACTS").
2. **The premise, read on the live plane** (`.tools/aws secretsmanager list-secrets`, names):
   - every enabled publisher (`barrons, bbg, ft, sa, wsj`) has a credential secret: `astn/ft/credentials`,
     `seeking-alpha/credentials`, `bloomberg/session`, and `dowjones/credentials`, which covers wsj and barrons;
   - **stored session/trust tokens exist in Secrets Manager for ft (`astn/ft/session`), sa (`seeking-alpha/session`) and bbg
     (`bloomberg/session`), but there is NO `dowjones/...session`.** The "trust token of a prior successful run" for wsj and barrons
     lives elsewhere (the collector's saved session; `Z-W69-S2`'s logged-out barrons case).

   The count query `length(SecretList)` returned a per-page count and is not used here; the names list is the evidence.
3. **Agreement with ENDPOINT:** unchanged. This is collection mechanics under FWD-1 and FWD-9, and it removes a human act from the
   list.

## VERDICT: SIGN

**One note for the build (round 29), not a condition.** Name where each publisher's trust token is stored and read from. For wsj and
barrons it is not in Secrets Manager today, so "token first" for Dow Jones means a stored-session file. That file's liveness is the
thing to test before a crawl. The run record's per-attempt statuses make the 429-vs-expiry distinction checkable afterwards.
