# Never-widen sign-off packet -- irpt-status: the whole bundle at CLOUD b1db201025 (E7: the request read names the chosen comparisons)

**For:** `1.0.0_SA_CTO` (CTO half; the contract text of `OwnedAnalysisRequest.schema.json` is ratified here too).
**Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-02 ~02:4xZ. **Authority:** CTO rulings batch 98 items 1-3 @29a6581479
(msg 103913: serve the chosen comparisons' names from the request's frozen keys and the catalogue's labels, never read
back from the PDF) and batch 100 (msg 103946: cut the irpt-status packet for E7, then st10).
**Ledger:** `irpt-status-e7-20261001` (legs U1, D1, V1), opened 2026-10-01T18:56Z; U1 proven here; D1 and V1 HELD on
row IRPT_BCKEND-S261 (section 4). One Lambda function's code. No IAM policy, queue, table, route or schema file moves. No
vendor call.

## 1. What ships

Every member of `irpt-status` at ONE commit, `b1db201025`, no member override (`build_irpt-status.txt`).

| | value |
|---|---|
| built zip | sha256 `iYgp83014ZjXiXxdgcBnvme/QooX4aIlUh8C5C7LTVI=`, 327,801 bytes, 45 members |
| S3 | `opal-313476888478-lambda-artifacts/investor-reporting/irpt-status.zip`, version `gqIQUc_Z0srcda_A1CGybmGZSXzTowjW` (uploaded 2026-10-01T18:58:17Z) |
| U1 read-back (2026-10-02 ~02:3xZ) | downloaded BY VERSION, sha256 equal, 45 members; `owned_requests.py` and `durable_job.py` byte-equal to `git show b1db201025:<source>` |
| live now | `2V7xV1+zII4+g6tV722Tk5M9LWJFMzLShyjq6Q+v/J4=`, LastModified 2026-10-01T06:59:55Z (read 2026-10-02 ~02:2xZ) |

Member census against the LIVE function (`census_irpt-status.json`): **45 members; added 0, removed 0, changed 2,
identical 43**; the 15-member served closure is identical to live.

| changed member | what it carries | numstat against the live-equal commit |
|---|---|---|
| `owned_requests.py` (item 17, `8c4398e32a`) | `read()` takes the composition through the ONE retained GET the old read already made (`head()` is `get()["ref"]`, `reports/repository.py:402-406`), checks the reference as before, and returns `comparisons: [{key, label}]` from the frozen `browser.comparison_keys` and `resolved.comparison_catalog[key].name`; a composition that does not derive refuses `COMPOSITION_COMPARISON_BINDING` | 29 added, 2 removed (against `03de809d50`) |
| `durable_job.py` (item 16, `7122afefc1`) | `append_vendor_requests` and one constant. INERT in this function: its one call site is `ycharts/generate/resident_worker.py:184`, which is not a member of this bundle | 25 added, 0 removed (against `b3fc529601`) |

Targeted plan (`plan_ops_targeted.txt`): `module.irpt_status.aws_lambda_function.this` update in place, only
`source_code_hash`, `s3_object_version`, `last_modified`. 0 add, 0 destroy.

Suites at CLOUD HEAD `485c7f37dd` (the ops, reports and `durable_job.py` trees equal the pin's): `ops/tests` 187 passed,
22 skipped (2026-10-02 ~02:3xZ). The generate suite at the branch tip: 333 passed, 30 skipped (reboot brief).

## 2. Blast radius, by branch (the producer's own rule, read at the pin)

Only the single-request read (`GET .../analysis/requests/{requestId}`, operation `analysis-request-read`) changes.
History, status, sections, report and dates routes run byte-identical members (the durable_job addition is never called).

| the request's retained composition | BEFORE (live) | AFTER |
|---|---|---|
| derives (schema `irpt-analysis-composition.v1`, every chosen key in the frozen catalogue with a non-blank name) | `{identity, accepted_at}` | `{identity, accepted_at, comparisons}`; `[]` for an Overview |
| does not derive | `{identity, accepted_at}` | refused `COMPOSITION_COMPARISON_BINDING` (a NEW refusal) |
| reference changed or retention expired | refused as today | refused as today (same checks, same order, `_final` unchanged) |

**Both branches against every accepted request (census, `composition_census_20261002.txt`, script
`composition_census.py` running the pin's own `_chosen_comparisons`, 2026-10-02 ~02:3xZ):** 20 of 20 accepted
requests in `irpt-requests` (cottonwood 18, inflection 1, 49financial 1; all revision 1) DERIVE: 16 read `[]`, 2 read
one comparison, 2 read two; **0 refuse.** Labels seen: Opal Short-Term 2, Opal Intermediate-Term 2, Opal Long-Term 2.
The only writer of a composition (`ycharts/generate/submission.py:183`) writes `irpt-analysis-composition.v1`, so the
refusal branch is reachable only by a composition whose catalogue lacks a chosen key -- none exists.

IAM: no new permission. The GET is the one the live read already makes; sid
`ReadRetainedAnalysisFamiliesUnderThePolicyPrefixesOnly` on `irpt-status-policy` grants `s3:GetObject` and
`s3:GetObjectVersion` on `irpt/{inflection,cottonwood,49financial}/state/request_compositions/*` (applied policy read
2026-10-02 ~02:3xZ).

## 3. The consumer -- the reason D1 is HELD (row IRPT_BCKEND-S261)

The page parses this response with `readOwnedRequest`
(`portal/src/pages/InvestorReporting/contracts/owned-requests.ts:23`), which requires EXACTLY the keys `identity` and
`accepted_at` (`exact()`, `:6-8`) and throws `Invalid owned request projection` on a third. Same bytes on portal HEAD
`24646bca`, origin/DEV `24646bca` and origin/PROD `f2731ad3`. **Applied today, the AFTER row of section 2 breaks every
request the page opens, the live Overview `REQ-a69e5751` included.** The schema's "optional" holds for the contract file,
not for the deployed consumer.

So the order is: (1) `2.0.0_SA_COO~D` makes the parser accept an optional `comparisons` array (validated: at most 5,
each `{key, label}` non-empty strings, nothing else) and that build is deployed wherever the page calls this route; (2)
this apply; (3) the page shows the names and re-walks the Multi-Comp; the CTO calls the arm live.

## 4. Apply protocol, in this order

1. Both halves at HEAD naming this file's blob. Row S261's precondition met: the deployed page build(s) parse a
   response with `comparisons` (named by `2.0.0_SA_COO~D` with the build's commit).
2. Before-read: live CodeSha256 `2V7xV1..`; the artifact key's latest version still `gqIQUc_Z..` with sha `iYgp8301..`
   (re-read; if anything replaced it, stop and rebuild).
3. ONE `safe-apply` of `-target=module.irpt_status.aws_lambda_function.this` in `infra/aws/terraform/investor-reporting/ops`
   from a fresh plan whose only changes are section 1's three attributes.
4. D1: CodeSha256 equals `iYgp8301..`; a re-plan of the same target reads no changes.
5. V1: the request read of `REQ-a1d9abc0bc037ea3d9e4a7ed` as the service principal returns `comparisons` naming Opal
   Short-Term and Opal Intermediate-Term in the request's key order; `REQ-a69e5751d42c374f1d2354f9` returns `[]`; one
   status and one sections read answer as before; the page opens both requests.
6. The ledger closes at V1.

## 5. Rollback, per key

`aws_lambda_function.irpt_status` back to S3 version `m1LolBKFxtfUUbodMML8ZuM.Wfo6Op.C` (code `2V7xV1..`), the version the
function runs now, by one targeted apply pinned to it. The function holds no state; nothing else moves.

## 6. Not claimed

- That a future composition always derives: the census covers the 20 that exist.
- That the page shows the names: that is `2.0.0_SA_COO~D`'s change, after this apply.
- Which deployed page builds call this route: DEV and PROD carry the same parser; `2.0.0_SA_COO~D` names them.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-02 ~02:4xZ, on this packet's bytes at the commit that carries it, CONDITIONAL on section 4 step 1's
precondition (row S261). The write set is one Lambda function's code (`irpt-status`). The blast radius is section 2, both
branches read against all 20 accepted requests; the consumer's break is section 3; the rollback is section 5.

## CTO half -- 1.0.0_SA_CTO

(not signed)
