# AMGT Peers B04/P1 -- PRE-BUILD BASELINE, captured before any candidate exists

**`3.0.0_SA_CVO~Z`, 2026-09-24 ~02:3xZ.** Mandate `CVO_Z_PEERS.md` @`7b26e2ac1c`.
**This is NOT a grade.** No pinned candidate exists yet. This is the **before-state** every later grade
will be measured against.

## WHY THIS EXISTS, AND WHY IT COULD NOT WAIT

Three of the mandate's five selections are specified by **TODAY's** state -- `ASML_US_Equity` *"today
UNRESOLVED at the route with an object in the pool"*, `CAT_US_Equity` *"resolved, no object today"*, and
the two `after step N` clauses that depend on them. ⛔ **Once the build lands, today's state is
unrecoverable.** A before-state not measured before the change can only be taken on the builder's word
afterward, and the builder is the party the grade is about.

**INSTRUMENT:** direct `lambda invoke` against the deployed `opal-amgt-scoped-api`
(`CodeSha256 DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=`), synthetic API Gateway v2 event, firm header
present -- the deployed bytes on the real S3 data plane -- plus a live `s3api` read of the pool.

## THE FIVE SELECTIONS, MEASURED

| selection | route `identity_status` | `basis` | members | `peer_read.status` | pool objects |
|---|---|---|---|---|---|
| `BA_US_Equity` | MEASURED | derived | **12** | SERVED | 5 |
| `992_HK_Equity` | MEASURED | derived | **12** | SERVED | 5 |
| `ASML_US_Equity` | **UNRESOLVED** | absent | 0 | **`{}`** | **4** |
| `CAT_US_Equity` | MEASURED | absent | 0 | ABSENT (+reason) | **0** |
| `NOSUCHKEY_ZZ_Equity` | UNRESOLVED | absent | 0 | `{}` | 0 |

**EVERY ONE MATCHES THE MANDATE'S STATED TODAY-EXPECTATION.** The selection table is confirmed, not
assumed, on the deployed plane.

**`ASML_US_Equity` IS CONFIRMED STRANDED** -- the route answers UNRESOLVED while **4 objects for that
exact key sit in the pool**. That is the defect the build exists to close, and it is now measured rather
than asserted.

**Served object keys, for reconciliation:**
`peers/v1/BA_US_Equity/2026-09-17T0240Z.json` and `peers/v1/992_HK_Equity/2026-09-17T0240Z.json`,
both `source: pool`, `store: s3://opal-data-harvest`, `as_of 2026-09-17T0240Z`.

## THE POOL DENOMINATOR -- 191, INDEPENDENTLY CORROBORATED

`peers/v1/` holds **797 objects across 191 distinct security keys**. ⭐ **The mandate's proof obligation 2
names "the 191 newest pool keys" and that number is reproduced here from the live bucket by a seat that
did not author it.** The obligation's denominator is sound before the step runs.

## ⭐ A STRUCTURAL FINDING THAT BEARS DIRECTLY ON HOW STRANDED SETS HIDE

The route records **two different things** for two different failures, and only one of them leaves a trace:

- **UNRESOLVED identity** -> `peer_read` is `{}` **-- EMPTY. No read was attempted and NO RECORD OF A
  FAILED READ EXISTS.** (`ASML_US_Equity`, `NOSUCHKEY_ZZ_Equity`)
- **RESOLVED identity, no object** -> `peer_read` is **populated**: `status: ABSENT`, `read_completed:
  true`, `object_key: null`, `reason: "no obj..."`. (`CAT_US_Equity`)

⛔ **So a stranded set -- an object that EXISTS but whose key the crosswalk cannot resolve -- produces the
SAME empty `peer_read` as a security that does not exist at all.** The one case where data is being lost
is indistinguishable, from the response, from the case where there was never anything to lose. **That is
why 111 stranded sets could sit unnoticed: the route does not record a failure it never attempted.**

This is offered as a grading note, not a defect claim on top of the ruled work -- the ruled remedy
(converge the route UP to the producer) addresses the cause. It matters for **acceptance**: a future
"`peer_read` empty" reading must not be graded as ABSENT-and-fine.

## WHAT THIS BASELINE DOES **NOT** ESTABLISH

- ⛔ **Nothing is rendered here.** **Route-proof is not render-proof** -- no tab, no column state, no
  count, no FX caveat, no `P/E 2026` label has been observed. All of that is the render half and is
  **NOT_EVALUATED**.
- **Consumer 2 is untouched.** `PostureTab.tsx:339-347` calls `usePeerSet` twice; nothing here exercises
  the Posture comparable read, so every case above is **HALF-GRADED by construction** and is recorded as
  a baseline rather than a case result.
- **No failure case is exercised** -- not the expired session, not `READ_FAILED`, not the literal-`/`
  `BP/_LN_Equity` shape.
- **The edge is not exercised.** Direct `lambda invoke` bypasses the CloudFront behavior and the
  `auth-validator-edge` header injection. A `/market` redirect, which the mandate makes a FAIL, **cannot
  be detected by this instrument at all.**
- **`ASML_US_Equity`'s 4 pool objects were not opened.** Their existence is measured; their contents,
  and whether they would yield 12 valid members after the crosswalk widens, are not.

## STANDING LIMITS CARRIED FROM THE MANDATE, NOT SILENTLY DROPPED

`AMGT_MODEL_BLOCK_ROOT` / `AMGT_POOL_ROOT` unset on the deployed function, so the second identity surface
cannot fire and every pool read goes to `s3://opal-data-harvest` -- **consistent with `store` in every
payload above**. Universe vintage `2026-08-06`; a stale-universe result is not a Peers defect. The
string-order "latest" hazard is noted and is not a defect today.
