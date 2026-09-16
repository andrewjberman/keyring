# Local publication harvest commissioning

Seat `4.0.0_SA_CRO~W`; AMGT_RESAPP / D5. Evidence through 2026-09-15 05:12 UTC.

**Status: not fully commissioned. Barron's independent slider recovery remains
unproven. No readiness ping or recurring collection authorization is inferred.**

## What passed

The latest three distinct-security qualification jobs for each publisher contain
five distinct, structurally complete article candidates for BA, COST and HD.
All accepted bodies were obtained by the tested harvest/HTTP scripts; existing
bucket contents were not used as evidence of script success.

| Publisher | BA | COST | HD | Stored bodies reused in this latest three-job round |
|---|---:|---:|---:|---:|
| Seeking Alpha | 5 | 5 | 5 | 0 |
| Financial Times | 5 | 5 | 5 | 0 |
| WSJ | 5 | 5 | 5 | 0 |
| Bloomberg | 5 | 5 | 5 | 3 |
| Barron's | 5 | 5 | 5 | 13 |

These are result counts, not a claim that every latest job refetched five bodies.
Earlier HTTP receipts establish the provenance of cached bodies. The worker now
avoids duplicate body requests and records `retrieval: stored_body` explicitly.
The automatic quality test checks metadata, clean blocks, relevance, minimum
length, unlocked flags and publisher word counts where available. It does not
constitute editorial review or exhaustive historical coverage.

Proof: `.runtime/opal-data-harvest/qualification.json`; the exact job receipts and
body hashes are listed there. Canonical migration corrected four SA block-array
whitespace inconsistencies without changing their stored body text or hash.

All **83 canonical article objects and 84 security links** pass the versioned
schemas and body/hash consistency checks. Proof: `schema-validation.json`.

**25 local tests pass**, including auth replay, verification replay, throttling,
partial results, shared body lookup before article HTTP, lost S3 acknowledgement,
small upload budgets, rejected-body reporting, publisher pacing, and broken
article routes, and rejection of HTTP-200 challenge/preview responses.
`ruff check lib/opal_data_harvest` passes.

## Storage and scheduling

Canonical source: `lib/opal_data_harvest/`.

- Stable identity: `publisher:article_id`, with a canonical URL hash fallback.
- Body: `publications/v1/{publisher}/{sha256(identity)}.json`.
- Security association: `publication-links/v1/{security_key}/{publisher}/{sha256(identity)}.json`.
- Token values: current-user DPAPI vault; secret references and API contracts in
  `contracts.json`. Credential/session values are excluded from the code archive
  and publication objects.
- Conditional S3 writes, durable upload outbox, schema/hash GET readback, and
  retries that recognize a completed write after a lost acknowledgement.
- Links follow their parent bodies even with a one-object upload budget.

Live S3 validation: one body/link pair from each publisher (10 objects), then
new Bloomberg/HD and Barron's/HD pairs (4 objects) using one-object batches.
All 14 readbacks passed. Normal reruns wrote nothing; simulated lost local
acknowledgements recovered without another PUT.

Proof: `upload-validation/validation-proof.json` and
`upload-small-batches-20260915T050106Z/proof.json` under the runtime root.

The on-demand Windows task completed a bounded SA/BA `--new-only` job with five
new articles, zero credential refreshes and `LastTaskResult=0`. It is now
**disabled, with zero triggers and no next run**. Proof:
`scheduler-validation.json` and `scheduler-final-state.json`.

The current 38-file code/contract archive and its manifest were uploaded and verified by
readback at `s3://opal-data-harvest/lib/local-publications/0.1.0/6aef3ceee43976dc/`.
Archive SHA-256: `6aef3ceee43976dce29bb304d9b670800c9cc4a911e3096dbffb3d50dfb88904`.
This is commissioning code, not a certification of Barron's autonomous recovery.

## Remediation findings

1. Bloomberg's signed-in search page hid an API robot challenge. Recovery now
   opens the challenged route with saved cookies and retries REST after the
   browser verification. A live BA job recovered this way without entering
   credentials; the same original login then served COST and HD.
2. Invalid empty-domain/expired cookies from the HTTP jar are excluded before
   transferring cookies into Playwright. Original login time is preserved;
   HTTP cookie rotation has a separate update time.
3. Publisher pacing now survives client replacement and job/process boundaries.
4. Bloomberg search can match unrelated stems, including BoE for Boeing.
   Accepted article relevance is checked independently. Quoted searches and
   bounded pagination improved the result set; false matches remain possible.
5. A Barron's short-update URL returned HTTP 500 from the full-article API.
   Discovery now restricts that API to its measured native article slug shape.
   One unavailable article can be skipped; repeated server failures defer.
6. Rejected new bodies are not reported as an empty feed. Accepted partial work
   survives failures, and recovery replays do not duplicate stored bodies.
7. Recovery no longer treats HTTP 200 alone as restored access. It requires the
   expected structured search/article response and, for Barron's, a subscriber
   account check. Real captured-response replay passed four cases, including a
   rejection of the challenge JSON. A bounded live check at 05:10 UTC verified
   subscriber access and unlocked article JSON with the saved session. It saw
   no slider, so it is not an independent captcha pass. Evidence:
   `verification-contract-validation.json` and
   `verification/20260915T051028Z-barrons-contract-check/verification-proof.json`.

## Remaining validation: Barron's slider

Andrew's earlier manual drag remains **human-assisted**, unchanged. Autonomous
Barron's verification is still disabled. The candidate handler is experimental.

Three isolated checks used the recorded earlier session, then omitted its
verification cookie, then opened the homepage. Each returned usable publisher
access without presenting the slider; none counts as a captcha pass. The working
vault was untouched. A recorded challenge URL subsequently returned a restriction
page with no slider. It is not a usable independent challenge test.

Proof folders: `verification/20260915T044906Z-barrons-independent`,
`20260915T045002Z-barrons-independent`, `20260915T045404Z-barrons-independent`, and
`20260915T045956Z-barrons-recorded-challenge`. The current test measures Windows
operator-input activity across the whole browser run and records script actions.
An absent challenge or detected operator input cannot certify an independent pass.

Next qualifying evidence must show a genuine slider, script-driven completion
without operator input, a verified paid session, and a complete native REST
article afterward. Then validate the recovery path in the worker before enabling
automatic Barron's recovery. Do not repeat completed broad collection batches
merely to provoke a challenge, or use a credential login as a generic 403 remedy.

## Decisions reserved to Andrew

Production mechanism, gradual backfill budget, recurrence and incremental-update
policy remain open. Five articles is a validation target, not a daily quota.
The pilot's bounded discovery window is not a persistent exhaustive backfill
cursor. Refreshing known articles after publisher corrections also needs an
explicit policy. No downstream consumer integration or production daily
ingestion schedule is claimed by this commissioning result.

Implementation commits: `7aaf58f0c1`, `edbea6bf93`, `c2d48b64d4`, `77d2b46284`.
Andrew-direct records: `cdc3576436`. Push state: LOCAL; no push performed.
Observed origin/SITEZ at 05:03 UTC:
`6f09a06dc919bf21ef96b52aff5cd7e9608ccf85` (`git ls-remote`).
The repository risk reflex remained PARTIAL_OR_BLIND because its danger map was
stale; its output is not cited as a clean risk check.
