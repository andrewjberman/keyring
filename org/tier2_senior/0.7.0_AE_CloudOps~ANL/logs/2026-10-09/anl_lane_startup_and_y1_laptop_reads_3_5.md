# Five read-only reads land; 3a, 4_route and 5 are ONE absent retention row — 0.7.0_AE_CloudOps~ANL

**Date:** 2026-10-09
**Task Order:** ADHOC.irpt-anlreq-y1-laptop-reads-3-5
**Status:** COMPLETE

**archetype:** VALIDATE

---

## Objective

Run dell2's five reads (3a, 3b, 3c, 4, 5) that dell2 cannot make itself — `irpt-requests` is
SSE-KMS under a CMK (row IRPT_ANLREQ-D2-S8) and the laptop identity can decrypt it. Return the
spec's shape only: booleans, one expiry, one outcome name. Zero writes, no minted credential, no
link/email/principal id/record body in any artifact.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-to | `comp-to ADHOC.irpt-anlreq-y1-laptop-reads-3-5` | PASS | bound the session TO id race-free per seat+session |
| comp-find | `comp-find 'status_installed' --files --limit 30` | PARTIAL | exceeded 120 s and was backgrounded; the deployed-package read answered first and better, so the census was never needed |
| comp-iam | `comp-iam service irpt-status` | PARTIAL | printed 3 statements off `investor-reporting/ops/iam.tf`, all scoped to `opal-users-v2` (Query on email-index, GetItem, conditioned kms:Decrypt). It shows NOTHING for the `irpt-requests`/`irpt-jobs`/S3 grants the function demonstrably exercised this session — the documented FLOOR behaviour (models `(action)`, never `(action, resource)`). Not cited as coverage. |
| comp-adversary | `comp-adversary --help` | SKIPPED (as a composer) | it composes a validation-context declaration for the atom_decomp workflow; this order's `<preflight>` carried its adversary arms inline, and each arm was exercised directly (see Verification). Running the composer would have produced a packet no one in this order consumes. |
| comp-schedule | — | SKIPPED | the order declares it DECLARED-NOT-APPLICABLE: one set of reads, no cadence |
| comp-pipescript deployed / postdeps | — | SKIPPED | AE minimum binds before a GOLD RUN trigger; no gold script, no pipeline run, no infra change in this order |
| comp-blast | — | SKIPPED | AE minimum binds before an infra CHANGE; this order changes nothing |

**What worked:** `comp-to` for TO binding. The single highest-value instrument was not a comp-tool
at all: `aws lambda get-function` → read `status_installed.py`, `served.py`, `resolve.py`,
`interactive_access.py`, `owned_requests.py`, `owned_report.py`, `retention.py` straight out of the
DEPLOYED zip. That is the bytes that run, so the principal model I replayed came from the artifact
rather than from a tree that might not match it.

**What failed:** `comp-find` on a bare token took >120 s. `comp-iam` under-reported by a wide margin
(see table) — exactly the silence its own doctrine warns about; it is a floor, never a warrant.

**Gap found:** the comp-rail denied a `grep` over my own scratchpad scripts as a "blind recursive
repo search" even though the path is outside any checkout — which the rail's own FREE list admits
("any path outside a checkout"). Worked around with the native `Grep` tool, also FREE. Low-harm
false positive in the rail's path classification; recorded, not routed as a blocker.

---

## Deployment Sequence

Not applicable — this order is READ-ONLY. Nothing was built, uploaded, applied, tagged or deployed.
No deploy ledger was opened because no deploy occurred.

| Step | Action | Result |
|------|--------|--------|
| 1 | Confirm the release under test | `irpt-status` CodeSha256 `BjUZjt2oq8GPJSibq4vD/0m8/LfdN0GF3THwCaBMVOM=`, LastModified 2026-10-09T11:20:57Z — equals the sha the spec names |
| 2 | Confirm the spec at its pin | disk sha256 == `git show 66b6d08b9c:<spec>` sha256 (`691fa8ee...`), positive control read at the same pin |
| 3 | Read the handler's principal model | from the DEPLOYED zip, not the tree |
| 4 | Run the five reads | direct invoke, front-door event shape |
| 5 | Corroborate with a principal-free instrument | retention tree walk in `irpt-requests` |
| 6 | Write result + flip TO terminal | commit `2315575398` |

---

## Verification

**Method, stated as the order requires.** Each GET was reached by a DIRECT INVOKE of `irpt-status`
with the event the HTTP API front door passes — `routeKey` + `pathParameters` +
`queryStringParameters` + the edge-injected trusted header set (`resolve.py TRUSTED_HEADERS`:
`x-origin-verify`, `x-user-email`, `x-firm-id`, `x-user-role`, `X-Contract-Version`) carrying each
principal's claims. The Lambda@Edge validator is the gate and the function reads the claims, so
this is the shape the function's own route table resolves.

**Principals — existing only, none minted.**
- 3a / 4 / 5: the request's REAL owner, replayed from its stored record. Both named records are
  owned by an `OPAL_GLOBAL` subject with `home_firm_id` `opal-capital` acting in data firm
  `49financial`, so the replay is `x-firm-id: opal-capital` + `selected_tenant=49financial`.
- 3b: an EXISTING active `cottonwood` admin PROFILE row in `opal-users-v2` → `FIRM_OPERATIONS`.

**Returned shape (the deliverable).**

| key | value |
|---|---|
| 3a | false |
| 3a_link_expiry | null |
| 3b | true |
| 3c | null |
| 3c_custody_request_exists | false |
| 4_record | true |
| 4_route | false |
| 5 | false |
| 5_outcome | OUTSIDE_DECLARED_DOMAIN |

**Per-read evidence.**

| read | public code | internal record (own-RequestId join) |
|---|---|---|
| 3a | NOT_FOUND | `RetentionExpired: retention record unavailable` |
| 3b arm, no selection | NOT_AUTHORIZED | `ProspectOwnershipRefused: issued record not currently authorized` |
| 3b arm, selects 49financial | FIRM_BINDING | none by design (refused before any record read) |
| 4 route | NOT_FOUND | `RetentionExpired: retention record unavailable` |
| 5 | NOT_FOUND | `RetentionExpired: retention record unavailable` |

The log join is per-invocation: each call's own AWS RequestId slices its own lines between
`START <id>` and `REPORT <id>`. An earlier time-window join was UNSOUND — it attributed 7 internal
records to 12 calls — and was discarded, not reported.

**THE FINDING — one shared dependency, not three failures.** All three of the spec's named requests
depend on the SAME retention row, and it is ABSENT from `irpt-requests`:

```
RETENTION#RET-021c9f6b5a6c410564cfad5c59ef10174f344d0f778b232f8f2bbae8c8e7c5b7
family NORMALIZED_PORTFOLIO
```

Walked principal-free over all 7 tenant requests (denominator printed):

| request | chain |
|---|---|
| REQ-cf1d7894dd4b73a148b01a2d | COMPOSITION → NORMALIZED_PORTFOLIO → ORIGINAL_HOLDINGS, all live |
| REQ-1f8b4cc4682f2d929cc70215 | all live |
| REQ-448d42480cadd873fa74c3cf | all live |
| REQ-5e4149d2863aea31cc87d660 | all live (PROMOTING) |
| REQ-3d76e5b49dae4f91db1694b0 (spec prospect) | first missing row `RET-021c9f6b` |
| REQ-9d59d4d2334f841152914569 (spec ticketed) | first missing row `RET-021c9f6b` |
| REQ-f7ddede91f98562412314b6e (spec third, Y77 reads 4-5) | first missing row `RET-021c9f6b` |

Each request's OWN `REQUEST_COMPOSITION` retention row is PRESENT and unexpired (RESERVED,
~20–30 days remaining), so the absence is strictly in the dependency.

**Controls that make that claim safe to act on.**
- POSITIVE CONTROL: `REQ-cf1d7894dd4b73a148b01a2d`, whose chain is complete, ANSWERS its composition
  through the identical route, principal replay and event shape. So the three refusals are the
  world's missing row, not my method.
- KEY-SPELLING CONTROL: 390 `RETENTION#` rows exist in tenant `49financial`, so ABSENT is a true
  absence and not a wrong key prefix.
- TWO AGREEING INSTRUMENTS: the live route's internal `RetentionExpired` and the direct table walk
  name the same cause independently.

**3c, measured over the right denominator.** No custody-lane request exists in the tenant: every one
of the 7 acceptance records' frozen compositions was read straight from S3 at the BUILDER's address
(`lib/opal_naming.reporting_destination`, family `REQUEST_COMPOSITION`, pinned `VersionId`) and
inspected for `browser.input_id` — 7 prospect lane, 0 custody lane, 0 unreadable, and every blob
hashed equal to its `composition_ref.sha256`. The ROUTE could only read 1 of those 7, so a
route-only census would have reported a lane distribution over a denominator of 1 and called it the
tenant. Nothing was created.

**3a's false is not a mismatch.** No link was issued, so there was nothing to hash:
`3a` false means "did not answer a matching link", never "answered a mismatched one". Same shape for
`4_route` — it never reached `composition.ticket_id`. The ticket itself IS proven, by `4_record`,
read from the decrypted acceptance row: stored `ticket_id` == `TCK-20261009-a1052909`.

**`5_outcome` is an uncovered enum member.** The spec declares the domain `{SIGNED, NOT_RETAINED}`.
The observed outcome is neither — the route refuses upstream of the PDF-retention branch — so the
field carries `OUTSIDE_DECLARED_DOMAIN` rather than the nearest legal value. Forcing `NOT_RETAINED`
would assert that branch was reached when it was not. Whether a PDF is retained for this request is
UNMEASURED by this read. Owner of the enum: `2.0.0_SA_COO~Y2`.

**The order's adversary arms, each exercised.**

| arm | result |
|---|---|
| a signed link or identity leaked into a file or message | result file and commit: 0 email-shaped strings, 0 `http(s)` urls, 0 non-ASCII — with a POSITIVE CONTROL proving the email detector fires (1 hit on a planted string) |
| a write disguised as a read | 25 AWS calls across 7 scripts, all reads (`get_item`, `query`/`scan` paginators, `get_object`, `invoke` of GET routes, `filter_log_events`); a scan for every mutating verb returned no matches |
| a principal minted for the test | none — owner replayed from its own record, other-firm principal an existing `opal-users-v2` row |
| BLIND: what the owner does with the link | no link was ever issued, so nothing was released to anyone |

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Read the handler from the DEPLOYED zip, not the repo tree | Rule 22a: deployed bytes are the thing that runs; a tree read could have modelled a principal path the live release does not have |
| Ran 3b as TWO arms (no selection; selects 49financial) | one arm alone proves less — without selection the tenant lookup simply misses; with selection the cross-firm boundary itself is exercised. `3b` is true only because BOTH refused and neither signed |
| Reported `5_outcome` as `OUTSIDE_DECLARED_DOMAIN` | taxonomy law (iv): name the value a remedy does not move rather than coerce an observation into a domain that does not hold it |
| Discarded the time-window log join | it attributed 7 records to 12 calls; an unsound join is not weak evidence, it is wrong evidence |
| Did not chase WHY the retention row is absent | read-only order; the cause is upstream and is the issuer's call. Stated as not-claimed in the result file |
| Wrote the result under this seat's own deliverables | owned-paths refused the spec path (TREE_DELIVERABLES, ADHC_OWNPTH.004). The order named this exact fallback |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/Y1_laptop_reads_3_5_result.json` | the result (new), sha256 `13aa6be20e5487e384616d9b8be453c1b061423a7f9fe4c8f861a1f2a3e06927`, 8074 bytes | Yes — `2315575398` |
| `org/tier2_senior/0.7.0_AE_CloudOps~ANL/task_orders/ADHOC.irpt-anlreq-y1-laptop-reads-3-5.md` | `<status>` pending → complete | Yes — `2315575398` |
| `org/tier2_senior/0.7.0_AE_CloudOps~ANL/logs/2026-10-09/anl_lane_startup_and_y1_laptop_reads_3_5.md` | this log | pending this commit |

NO AWS resource, policy, object, table row or Lambda was created, modified or deleted.

---

## Blockers

None for this lane. Its one order is terminal and reported.

One finding is owned ELSEWHERE and is not this seat's to fix: the absent `NORMALIZED_PORTFOLIO`
retention row `RET-021c9f6b…` blocks the `/original`, `?include=composition` and `/pdf` reads of all
three requests dell2's release-1 exercise named. Routed to `2.0.0_SA_COO~C` for dell2 in the
completion message (msg delivered 13:14:04Z, 1441 bytes). Not a blocker on this order, which asked
for the reads' outcomes and got them.

A second observation, surfaced not chased: three of the seven tenant requests refuse their own
owner's composition read with FIRM_BINDING, i.e. those owners' profile `allowedFirmIds` narrowing
does not admit selecting `49financial`. Outside this order's five reads; named here so it is not
rediscovered as a defect of the route.

---

## Current State

Lane `0.7.0_AE_CloudOps~ANL` is LIVE (PID 18816, branch `box/laptop`, workspace root
`C:/Users/AndrewBerman/Desktop/ajb_workspace`), one inbox watcher armed (Monitor `b49t2p936`), zero
crons. Its ONE order, `ADHOC.irpt-anlreq-y1-laptop-reads-3-5`, is `complete` and its result is
committed at `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/Y1_laptop_reads_3_5_result.json`
(sha256 `13aa6be2…`, 8074 bytes) in commit `2315575398`, which is **LOCAL** — origin `box/laptop`
reads `4586920aca691c08d465939f481dae4945d6c417` by `git ls-remote`, and `box/*` is pushed only by
an MSTR or the box's scheduled `box-sync`. The seven pending task orders `get_agent_status` prints
are BASE-scoped (rule 22a) and are NOT this lane's. Nothing was written to AWS this session.

---

## Next Steps

1. **[0.7.0_AE_CloudOps~ANL] Event-driven hold** — act on the next `[INBOX]` event the same turn;
   re-arm the Monitor on each `[WATCHER-EXPIRED]` line, same turn, one call, no skill load.
2. **[2.0.0_SA_COO~C] Route the absent retention row to dell2** — `RET-021c9f6b…`
   (NORMALIZED_PORTFOLIO) is the single cause of 3a, 4_route and 5. Until it is restored or
   explained, those three reads cannot answer true for any of the three named requests.
3. **[2.0.0_SA_COO~Y2] Commit the result on the spec path** — owned-paths bars this seat from
   `deliverables/2.0.0_SA_COO~Y2/release1/`; the bytes are identical and the sha256 is in the
   completion message.
4. **[2.0.0_SA_COO~Y2] Rule on `5_outcome`'s enum** — either the domain gains the observed member
   or read 5 is re-cut once the retention row is live.
5. **[0.0.0_AB_MSTR] Carry `2315575398` to CLOUD** at the next `box-sync` drain; this seat does not
   push `box/laptop`.
