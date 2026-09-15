# Lusha v3 reference review: position-only request remains unestablished

**Seat:** `4.0.0_SA_CRO~W`. **Date:** 2026-09-15.
**Trigger:** exact inbox message 23238 from CTO~W, self-drive tick 1, ruling 2.
**Related findings:** `AMGT_RESAPP_TAB_SCORE_DATA_FINDINGS_20260915_W.md` @ `7bad309f20`.
**Status:** reference review complete; authorized one-call enrich UNUSED. No credential access or vendor API call.

## Endpoint reference findings

Read the official [Enrich Contacts reference](https://docs.lusha.com/apis/openapi/enrich/enrichcontacts),
including its [Markdown representation](https://docs.lusha.com/apis/openapi/enrich/enrichcontacts.md).
The official [Data Waterfall page](https://docs.lusha.com/user-guide/lushas-api/data-waterfall) links to the Enrich API section,
which links to this exact endpoint. Both HTML and Markdown returned HTTP 200; the Markdown exposes the actual request/response schema.

- Endpoint: `POST /v3/contacts/enrich`, required `ids` array.
- The documented `reveal` selectors are `emails` and `phones`. The reference says: **“Omit reveal to get both by default.”**
- It does not document a positions selector or guarantee that an explicit empty list excludes both contact channels while returning employment data.
- The response documents `previousEmployment` with company and job-title data. It does not document employment start/end dates or the fixture's `currentPosition.startDate` / `previousPositions` paths.
- Response `updateDate` is not documented as a company-join or role-start date and cannot be used as one.
- `waterfallEnabled: false` controls third-party fallback; it is not a contact-field exclusion switch.

The documented schema is narrower than an assertion about everything the vendor might supply. Undocumented fields or behavior remain
unverified; lack of documentation is not proof that the vendor has no employment dates.

## Local consequence and disposition

The local client `data/find/imo/scripts/_util/lusha_client.py:contacts_enrich` drops an empty reveal list, as reproduced in the earlier
review. The exact endpoint reference now confirms the omitted-selector default for the endpoint itself; the earlier finding relied
on a combined-endpoint tutorial as a warning.

Even changing the client to preserve `[]` would not establish the required behavior from this reference. No speculative request was
made. The condition in CTO ruling 2 remains unsatisfied, so the one bounded enrich stays authorized and unused. The process flag was
not enabled. Employment-date coverage and per-officer cost therefore remain unmeasured.

The specific unresolved vendor contract is whether `reveal: []` is a supported request that returns job history without any email or
phone fields, and whether that history includes dated positions. A vendor clarification or updated reference could resolve this;
no external message to Lusha has been sent or authorized by this act.

## Other content of 23238

Read the 12 CTO adjudications and two Andrew-reserved decisions. CTO confirms it used our @7bad309f20 findings, despite the failed
canonical sends. My role remains research/brief review. Production promotion and recurring harvest remain reserved to Andrew;
round-11 orders remain unchanged. Heartbeat restoration is now explicitly routed to MSTR~Z, with no alternate helper.

Canonical readiness was rechecked during this turn: heartbeat missing and liveness absent; app-server, bridge and detector remain
alive. The assigned reference research is complete independently of that delivery defect. Push state: LOCAL.
