# Performance tab: end-to-end trace brief (the deployed stack, 2026-09-24)

Prepared by 4.0.0_SA_CRO on 2026-09-24 (~05:00-05:35 UTC). Read-only assessment plus proposed closure requirements; no
application changes, vendor calls, deployment or schedule activation. Two things beyond a pure read happened and are
named: the deployed package was downloaded and its retained-performance service was DRY-RUN locally under this seat's own
credentials (reads only; it raised before its first AWS call); and Andrew's own 04:32Z browser session (HAR) was read in
place. `/closer trace` form; the 2026-09-22 brief (`PERFORMANCE_END_TO_END_GAP_BRIEF_20260922.md`) is the baseline and
is not repeated -- this brief measures what is deployed TONIGHT and where the journey stops.

**Conclusion first.** The Performance tab does not work for any user tonight. Every performance request in Andrew's
04:32Z session (three selections, six calls) answered `UNAVAILABLE`, and the screen showed "Failed / Retry". The
deployed path is no longer the 09-22 "recorded capture" adapter: since 00:07:10Z it is P's RETAINED, ONE-USE,
SERVER-APPROVED Cottonwood calculation (one account, one window, one vendor call per operator-installed plan, reopened
from immutable storage afterwards). That path stops at its FIRST gate for every single-account request -- the
registered reporting policy (`X10`) is `PENDING_ENFORCEMENT` and the gate demands `ACTIVE` -- and the refusal is
classified `UNEXPECTED` because the gate's exception class is not in the boundary's reason map. Behind that gate two
more things are missing before a number can reach the screen: no one-use plan is installed (the vendor call is refused
by design until one is), and the deployed success status still carries a member the portal refuses. A relationship
(household) selection is refused earlier, by design ("exact single selected owner required"). 49 Financial and
Inflection have no performance path at all in the deployed bytes (Cottonwood-only calculation).

## Design finding

The 09-22 design stands: performance is the provider's calculated return (Black Diamond for Cottonwood and, as
verification only, 49 Financial; Orion for Inflection; SmartX is 49F's PRIMARY per `tenants.py`), requested for the
exact authorized account set and period, retained with its request/response digests, normalized, rendered and exported.
Opal computes no return.

What changed since 09-22 is the MECHANISM P built for it under the closer contract (RULINGS.md
`IRPT-PERFORMANCE-INSTALL-GO-20260923`, install VERIFIED LIVE 00:07:10Z): `runtime.lambda_handler` ->
`installed.build_runtime` -> `retained.RetainedPerformance.compute`. It is a mechanism for ONE PROVEN TRACE: an operator
installs a plan naming one firm, one account, one window, an expiry and the exact request digests (two env keys on the
function); the service claims it once in DynamoDB (conditional put, no TTL), makes the two Black Diamond calls with the
firm's session cookie, persists the evidence and the report under finite retention, publishes an accepted pointer, and
every later request for the same owner/window REOPENS the stored report without a vendor call. It is deliberately not
an on-demand path: a second account, or the same account next week, is a new plan, i.e. a Lambda configuration change
per report. That is Andrew's per-use vendor word made mechanical, and it is the right shape for the first live thread;
it is not the shape of the product journey the DSGN_IRPTV1 PRD names (FWD-5: periods across, portfolio / benchmark /
spread rows, the area chart), which needs standard periods, a benchmark and a standing authorization for the product's
own firm data. Both facts are stated here so the completion sequence can be chosen rather than inherited.

The work worth keeping: the exact-identity parser and window/series alignment (`bd_selected.py`), the bounded
session->token->period->series transport with receipts (`bd_live.py`), the dated account mapping port
(`cot_account_mapping.py`), the finite-retention repositories, and the one-use claim. The unfinished connections are
the four gates below (hops 4, 6, 10, 11) and the multi-period/benchmark request (hop 8).

## Current measurement

Read from DEPLOYED bytes at 05:01:26 UTC: `irpt-performance-adapter`, CodeSha256 `JwJEEQGTENJJukTvrNQt3dq6VIAI8xqioIYA1atL+hk=`
(the downloaded zip's own sha256 equals the configuration's), 358,117 bytes, 61 members, last modified 2026-09-24T00:07:10Z,
handler `runtime.lambda_handler`, 1536 MB, 120 s, layers `irpt-common:5` and `irpt-performance-native-layer:1`
(69.9 MB pandas/numpy/pyarrow, created 00:07:00Z), six environment keys. NOT present in the environment:
`IRPT_PERF_TRANSPORT_MODE`, `IRPT_PERFORMANCE_APPROVED_PLAN`, `IRPT_PERF_VENDOR_EGRESS_AUTHORIZED`.

Source pin: 6 of the 7 performance modules are byte-identical to P's branch head `irpt-smoke-p-backend-20260923`
@9f360e8f3b (runtime, handler, transport, bd_live, bd_selected, tenants); `entry.py` differs from that head (it still
emits `internal_correlation_id`, see hop 10). CLOUD HEAD c3508c07df carries NONE of `runtime.py`, `bd_live.py`,
`bd_selected.py` or the 31 non-performance members (the boundary, scope, ids, custody, retained repositories) -- the
deployed source lives on P's branch, not on the shared branch. The Terraform root on CLOUD
(`infra/aws/terraform/investor-reporting/performance/lambda.tf`) still declares `entry.lambda_handler`, 512 MB, 60 s,
one layer and `IRPT_PERF_TRANSPORT_MODE = "recorded"`; the live function is P's `build_candidate.py` flat shape. The CTO
has the same finding and a GO to reconcile the source map to the live 61-member shape (CTO 100268, "0/1/0"); note that
GO says "NOT in this GO: wiring installed.py / the retained runtime into the handler" -- measured, the live handler
ALREADY IS `runtime.lambda_handler`, which wires it. That sentence and the live configuration disagree; the CTO owns
the reconciliation of the two.

Live trace read: Andrew's HAR `aaaaaa.har`, 358 entries, 04:32:00-04:33:10Z, local portal on the DEV consolidation
candidate 7975c3bb against the deployed API. Three selections, each with the same READY holdings answer and the same
UNAVAILABLE performance answer:

| selection (from) | accounts | performance calls | server wait | state / public_reason_code |
|---|---|---|---|---|
| `sel_85779d75...` (RELATIONSHIP `rel_724131fb...`) | 2 | 2 (F7 double call) | 5.26 s cold, 1.04 s | UNAVAILABLE / DEPENDENCY_UNAVAILABLE |
| `sel_3169a90a...` (ACCOUNT `acc_0698a3de842dbe7b3d48c787`) | 1 | 2 | 1.59 s, 1.74 s | UNAVAILABLE / UNEXPECTED |
| `sel_2f4d0701...` (ACCOUNT `acc_d486fc9455d6b2aa18e13af1`, the PRD's FWD-1 account) | 1 | 2 | 1.58 s, 1.58 s | UNAVAILABLE / UNEXPECTED |

Every refusal states `business_date 2026-09-17` (the Cottonwood directory artifact's date -- five trading days old; the
shared bootstrap hop, not this surface's, but the thread crosses it). CloudWatch for the function over that window: 19
events, ALL lifecycle lines (INIT/START/END/REPORT; durations 3736 / 767 / 1418 / 1543 / 1399 / 1370 ms, init 437 ms,
228 MB) -- not one line naming a cause (hop 12).

Dry run (the discriminating instrument): `RetainedPerformance.compute` from the deployed bytes, own credentials, the
FWD-1 account, 2026-01-01..2026-09-24, an authorize stub returning True: raised
`retention.RetentionRefused: registered enforced policy required` at `retained.py:49 -> retention.py:57 _policy` after
0.01 s and ZERO AWS calls. The packaged registry row `infra/logic/registry/reporting_policies.json` reads
`policy_id irpt-private-reporting, register X10, state PENDING_ENFORCEMENT, enforcement_ref null`; the gate requires
`state == "ACTIVE"`, a 40-hex `enforcement_ref` and a `policy_sha256` equal to the row's digest. `RetentionRefused`
subclasses `ReportRefused` (mapped to DEPENDENCY_UNAVAILABLE), but `served.public_reason_for` looks the code up by the
EXACT class name, so it falls to UNEXPECTED -- exactly what both single-account calls returned. The relationship
selection never reaches that gate: `compute` refuses a two-account owner first (`ReportRefused`, mapped ->
DEPENDENCY_UNAVAILABLE). Both observed codes are therefore explained by the deployed code, and the timing agrees (the
1.4-1.7 s is the boundary's own loads; the compute fails instantly).

Also measured: the mapping loader succeeds for BOTH accounts outside the function role (54 partitions, picks
`date=2026-09-23`, 973 rows, 0 identity-shape mismatches, 0 duplicates; 1.06 s / 0.31 s; positive control on the
mapping's first row MAPPED); `irpt-requests` holds 0 one-use claims and 0 accepted performance pointers (17 items
scanned); the Cottonwood session secret `blackdiamond/cot/session` exists (created 2026-06-08, last changed 2026-09-16,
last accessed 2026-09-24; value not read; validity NOT measured -- a Black Diamond cookie expires, and the 09-22
capture's two 401s were an expired one on the 49F route). IAM on the applied plane could not be proven by simulation
(every probe ALLOWED including the intended negative control, "NO CONTROL DERIVABLE"); the CTO's record says the two
extra policies from P's `retained.tf` are on the role.

Not invoked: the Lambda (no synthesized verified header), any vendor endpoint, the export chain.

Machine-readable evidence: `.runtime/codex-seats/4.0.0_SA_CRO/performance_trace_20260924/evidence.json` (private, gitignored).

## Adapter map

| Surface / firm | Provider and intended endpoints | Existing work (deployed) | Gap |
|---|---|---|---|
| Cottonwood | Black Diamond ClientView: cookie `.bd.identity` from Secrets Manager `blackdiamond/cot/session`; GET `/session/token`; POST `/portfolioreporting/api/performance/performancePeriod` and `/performanceSeries` | `bd_live.CottonwoodTransport` (one two-request sequence, receipts with sha256, 16 MB cap, no redirects); `bd_selected` (exact account identity, exact window, series aligned to the period return); `cot_account_mapping` (dated mapping from `fact_model_assignment`, both accounts map); `retained` persist/reopen; `authorization.OneUseTransportFactory` | X10 policy enforcement (hop 4); an installed plan (hop 6); the first live exercise (hop 7); one custom period only, no benchmark, PARTIAL always (hop 8); reopen pointer v1 and the success status member (hops 9-10, both fixed at P's head, not deployed); refusal rendering (hop 11) |
| 49 Financial | SmartX PRIMARY (policy, `tenants.py`); Black Diamond as independent verification only | `handler.run` policy stub answers `SMARTX_ACCOUNT_CAPABILITY_UNPROVEN`; the retained service refuses non-Cottonwood ("Cottonwood calculation only") | No adapter. The SmartX feed is not being received (this seat's 09-23 note); UNAVAILABLE by construction |
| Inflection | Orion: POST `/api/v1/Reporting/Scope`; token `/api/v1/Security/Token`; secret `orion/credentials` | Capture-proven parser (`orion_adapter`), research request graph | Refused by the retained service before any Orion code runs; no production request builder (unchanged from 09-22) |

One firm's success does not certify another's; tonight no firm has a success to generalize from.

## Start-to-finish walk

### 1. Account pick -> retained selection -- WORKS

What exists: `portal/src/api/endpoints/investor-reporting.ts` `selection-create` (POST `/selection`, body
`{scope_kind, scope_ids}`, query `selected_tenant`); the server mints `sel_<sha256>` (`selected-accounts-v1`, firm
`cottonwood`). Measured: three selections minted in the HAR, holdings READY on each.

Close: nothing on this hop. Note that a RELATIONSHIP selection is ACCEPTED here and refused at hop 3 -- the two ends
disagree about what a selection may hold.

### 2. Tab -> GET `/api/scoped/investor-reporting/performance/{sel}?start&end&selected_tenant` -> boundary -- WORKS

What exists: `ReportingTab.tsx` requests the period window (`period.ts`; the HAR carries `start=2026-01-01&end=2026-09-24`)
through `getPerformanceReport` with `X-Contract-Version: v1`; the authorizer verifies the user; `served.py`'s boundary
binds the firm, loads the directory and ownership map, resolves scope; `entry.performance_report` validates the
`sel_` reference and the dates and resolves the retained selection (`selection.py`, `selection_store.py`, both packaged).
Measured: six calls reached the compute (the envelopes carry the firm and a business date). Cost: 0.8-1.7 s warm,
3.7 s cold -- this function has none of the B1/B3/B7 levers the listing got tonight (the CTO says the reconcile carries
them), and F7 calls it twice.

Close: none for the hop; the double call and the loaders are P's in-flight items (100206 item 1, 100268).

### 3. Boundary -> retained service: one account only -- INCOMPLETE

What exists: `retained.py:30-32` -- `compute` refuses unless the resolved scope is exactly ONE account and the owner's
account list equals it (`ReportRefused("exact single selected owner required")` -> DEPENDENCY_UNAVAILABLE);
`bd_selected.calculate` repeats the one-account rule. Measured: the RELATIONSHIP selection (two accounts, USD 46.0M)
got exactly this.

The exact mismatch: the header offers relationships and multi-account sets (hop 1 accepts them; the 09-22 brief hop 1
and DSGN_IRPTV1 FWD-3/4 want them); the calculation admits one account.

Close: decide the aggregate rule ONCE -- either the vendor-calculated aggregate for the exact set (a different BD
request shape, certified like the single-account one) or per-account reports with an explicitly unavailable aggregate --
and until it lands, answer a multi-account selection with a named code (`OBJECT_NOT_COVERED`-class, "one account at a
time") rather than DEPENDENCY_UNAVAILABLE. Proof: the same relationship selection returns the named code and the screen
says so.

### 4. Retention policy gate -> X10 enforcement -- MISSING

What exists: `retention.py:50-73` `_policy`, called by `compute` before any read (`retained.py:48-49`) for the families
`PERFORMANCE_SOURCE_EVIDENCE` and `PERFORMANCE`; the packaged `infra/logic/registry/reporting_policies.json` row
(register X10, `infra/logic/06_CONFORMANCE_LEDGER.md:144`, GRANTED CONDITIONAL); `entry.build_entry` reason map
(`ReportRefused`, `ReportDenied`, `SelectedPerformanceRefused` added to the module's own).

The exact mismatch, two halves: (a) the row says `state: PENDING_ENFORCEMENT, enforcement_ref: null` and carries no
`policy_sha256`; the gate demands `ACTIVE`, a 40-hex enforcement commit and the digest -- so every single-account
request stops here, before the mapping, the plan or the vendor; (b) the exception class `RetentionRefused` (and
`RetentionExpired`) is not a key in the reason map, and `public_reason_for` matches the exact class name, so a
policy-gate refusal surfaces as `UNEXPECTED` -- the code a viewer and an operator can do least with.

Close: (a) land X10's enforcement in the registry row (`state ACTIVE`, `enforcement_ref` = the enforcing commit,
`policy_sha256`) through its owner (the LGIC register / the CTO; `installed.py`'s own docstring calls this "the
prerequisite for every write and read"), and repackage; (b) add `RetentionRefused` / `RetentionExpired` to
`build_entry`'s reasons (DEPENDENCY_UNAVAILABLE / OBJECT_NOT_COVERED) -- or make the lookup walk the class's MRO so a
mapped parent is honoured. Proof: the FWD-1 account's request returns `DEPENDENCY_UNAVAILABLE` (hop 6 still unarmed)
instead of `UNEXPECTED`, in the same HAR shape as tonight's.

### 5. Canonical account -> vendor account (dated mapping) -- WORKS (measured outside the role)

What exists: `cot_account_mapping.make_cot_mapping_loader(s3, as_of=IRPT_PERFORMANCE_MAPPING_AS_OF)` lists
`s3://opal-data-assets/blackdiamond/cottonwood/silver/fact_model_assignment/date=*/`, takes the newest partition on or
before the cutoff, reads the parquet (pandas from the native layer), projects every `external_id` (`z09` + 8 digits)
through the id space and requires exactly one match; `retained.tf` (P's branch) grants the role ListBucket on that
prefix and GetObject/GetObjectVersion on the parquet. Measured: 54 partitions (2026-07-21..2026-09-23), the 09-23
partition has 973 rows, zero shape violations, both HAR accounts MAPPED, positive control MAPPED.

The exact mismatch: none in the loader. Two limits: the cutoff is a DATE TYPED INTO THE FUNCTION CONFIGURATION
(`2026-09-23`), so tomorrow's mapping is invisible until someone changes the environment; and the mapping is the
rebalancer's model-assignment table, so a Cottonwood account without a model assignment cannot map (0 of 2 tonight;
the fraction of the 858 Cottonwood portfolios that carry one is not measured here).

Close: derive the cutoff from the trading calendar (`lib/trading_calendar.py`, T-1) at request time, or make the
configuration bump an explicit daily act with an owner; and name the "no model assignment" case with its own code
rather than a mapping failure. Proof: a request on the day after a new partition lands maps without a deploy.

### 6. Server-approved one-use plan -> credential-bearing transport -- MISSING (nothing armed)

What exists: `authorization.OneUseTransportFactory` -- reads `IRPT_PERFORMANCE_APPROVED_PLAN` (schema
`irpt-performance-one-use-v1`: approval_ref, firm, account, vendor ids, mapping revision, start, end, expires_at,
requests_sha256) and requires `IRPT_PERF_VENDOR_EGRESS_AUTHORIZED` to equal the plan's digest; checks the request and the
mapping against the plan; claims `PERFORMANCE_USE#<sha>` in `irpt-requests` with a conditional put and no TTL ("a failed
or lost provider request consumes the use"); only then builds `CottonwoodTransport`. Measured: neither key is in the
deployed environment; 0 claim rows have ever been written.

The exact mismatch: the transport cannot exist without a plan, and a plan is one account, one window, one use. The
FWD-1 thread needs exactly one; the product journey needs one per account per window, each a Lambda configuration
change.

Close: for the thread, the CTO installs one plan for `acc_d486fc9455d6b2aa18e13af1` and the YTD window on Andrew's
per-use word (the plan IS the word, recorded by `approval_ref`); for the journey, a standing authorization class for the
product's own firm data -- Andrew's word once, recorded -- with the claim table kept as the per-request audit (one row
per calculation, still no TTL). Proof: one claim row, one accepted pointer, one READY answer.

### 7. Transport -> Black Diamond (cookie -> token -> period -> series) -- INCOMPLETE (built, never exercised)

What exists: `bd_live.CottonwoodTransport.request` -- loads the cookie through the private session-helper instance
(`load_bd_session` with `SECRET_ID = blackdiamond/cot/session`), GET `/session/token` for the ClientView bearer, POST
the period then the series body, sha256 receipts, raw bytes retained privately; the period body comes from the 49F
helper `bd_helpers.py` at `/opt/python` (layer `irpt-common:5`) with the 49F benchmarks emptied. Measured: never run
(no claim row exists); the secret exists and was last changed 2026-09-16.

The exact mismatch: an eight-day-old session cookie of unmeasured validity is the credential; the secret's own
description says it rotates "on each successful OIDC login", which nothing in this path performs.

Close: exercise the sequence once under the hop-6 plan; the proof is the two receipt digests inside the persisted
`PERFORMANCE_SOURCE_EVIDENCE` artifact and a 200 on `/session/token`. Name the cookie's owner and its refresh act
(who logs in, how often) in the CONTROL for the thread; an expired cookie must surface as a named provider refusal,
not `UNEXPECTED`.

### 8. Provider response -> one certified period, aligned series -- INCOMPLETE

What exists: `bd_selected.calculate` -- exact account identity in `levels[0]` (level, key, accountId, externalId), the
first `dateRangePoints` entry must equal the requested window, finite non-annualized TWR, series `dataStartDate` /
`dataEndDate` equal the window, series last point equals the period return within 1e-9; publishes ONLY the Custom range
and drops the helper's YTD/trailing/inception ranges; absence `historical_periods UNSUPPORTED`; no benchmark sent.

The exact mismatch: the report the screen wants (FWD-5: periods across; portfolio / benchmark / spread rows; the spread
server-stated per CTO 100194) needs the standard ranges and a benchmark the firm assigns. Today's path yields one
period, no benchmark, and is PARTIAL by construction; `adapt.ts:826-828` sets `benchmarks: []` unconditionally, so the
period table's benchmark section never renders whatever the wire carries.

Close: extend the certified request shape -- the standard ranges the helper already builds, kept and certified by
their echoed dates (not dropped), plus the firm's assigned benchmark in `parameters.benchmarks` -- as a NEW pinned
request hash, and carry `optional_facts.benchmark` as a typed member the adapter maps. Proof: one reconciled trace whose
period table shows YTD / 1Y / inception with the vendor's own dates and one benchmark row.

### 9. Retained persist -> reopen -- INCOMPLETE (built, unexercised; storage prerequisite = X10)

What exists: `composition.build_retained_repositories` (S3 blobs at `reporting_destination(firm, family, ...)` in the
X10 product bucket, DynamoDB report/retention index in `irpt-requests`, finite retention reserve/promote), the accepted
pointer `PERFORMANCE_ACCEPTED#<digest>`, `reopen` re-checking access and retention. Deployed pointer is v1 (owner-bound:
`digest({"owner": owner, "request": request})`), the shape P-REOPEN-01 replaced at 9074dba320 (v2: firm + sorted accounts
+ window); the deployed `retained.py` is one of the seven members the CTO's reconcile replaces.

The exact mismatch: under v1 a second user opening the same account and window cannot reopen the first user's report
and would need another plan (or fail); under v2 they reopen. Neither has been exercised: 0 rows.

Close: the reconcile (CTO 100268) lands `retained.py` at P's head; proof after the thread: the same window opened by a
second principal returns READY with `retained_ref` and writes no claim row.

### 10. Success status -> portal envelope -- MISMATCHED (fixed at P's head, not deployed)

What exists: deployed `entry.py:141-151` builds the READY/PARTIAL status WITH `internal_correlation_id`; the portal's
`PublicStatusEnvelope` closed-key rule refuses that member (`EnvelopeMismatch('status')`); P removed it at 786f767796
(accepted, "deploys with the next Performance package"); measured, the deployed `entry.py` differs from P's head.

The exact mismatch: once hops 4-7 pass, today's bytes would return a READY answer the browser refuses, and the tab
would show "Failed / Retry" for a report that exists.

Close: the reconcile carries `entry.py` @P head; proof = the READY envelope parses in the browser exactly as
`HOLDINGS_READY` did at 02:45Z tonight.

### 11. Refusal -> screen -- MISMATCHED

What exists: `served.refuse` returns `ok:false` with a public code and a business date; the client raises
`IrRequestError` carrying the code (`investor-reporting.ts:982-983`); `state/status.ts:274` `envelopeFromRefusal`
turns that into `Unavailable` + the code + "Contact support". `ReportingTab.tsx:166-170` does not call it: its catch
sets `REQUEST_FAILED_ENVELOPE` unconditionally -- state `Failed`, reason `IR-REQUEST-FAILED`, a Retry button.
`HoldingsTab.tsx:157-162` does call it.

The exact mismatch: what Andrew saw on all three selections was "Failed / Retry", and a retry cannot change a policy
gate or an absent plan; the producer's code (`DEPENDENCY_UNAVAILABLE`, `UNEXPECTED`) never reached the panel.

Close: `ReportingTab.tsx` catch -> `envelopeFromRefusal(error)` (one line, P's surface); proof = the relationship
selection shows "Unavailable -- DEPENDENCY_UNAVAILABLE -- Contact support".

### 12. Refusal -> operator (correlation id -> nowhere) -- MISSING

What exists: `served.py:912,933` call `_errors.record_internal(None, cid, operation, exc)` -- the sink argument is
`None`, and `record_internal` writes only to an injected sink by design ("never to a return value, never to
public_line"); the public envelope omits the correlation id (by design). Measured: 19 CloudWatch events in the HAR
window, none naming a class; this brief had to reproduce the compute locally to learn which gate refused.

Close: inject a sink at Entry construction -- one structured log line per refusal (`event`, `cid`, `operation`, the
class name, no vendor bytes) -- and return nothing more to the browser. Proof: the next `UNEXPECTED` carries a class
name in the function's own log group.

### 13. Report -> rendered screen -- INCOMPLETE against the design word

What exists: `Summary`, `CumulativeReturnChart` (renders when `dailyCumulative` is non-empty), `PeriodResults`,
`AccountDetail`, `MethodAndSources`; `AnswerStatus` prints the producer's state and business date; the renderer names
`PERFORMANCE_READY` / `PERFORMANCE_PARTIAL` (dc47f5bd). Andrew's approved layout (CRO~F 100220, recorded in CTO 100230):
a full-width time series in the AUA-Trend area-chart style and a heatmap with periods across and portfolio / benchmark /
spread rows.

The exact mismatch: the deployed report supplies one custom period, a daily cumulative series and no benchmark; the
adapter drops benchmarks; account names are opaque ids (the `display` member is accepted for Holdings only). The area
chart can be drawn from today's series once one exists; the heatmap cannot be filled until hop 8.

Close: DSGN_IRPTV1 cells for the area chart and the heatmap consume the hop-8 request shape and the `spread` member; the
render-only write surface stands. Proof: one reconciled trace from the BD response bytes to the two visuals.

## Recommended completion sequence

1. **The live thread.** One Opal user (Andrew's own sign-in on the DEV candidate), Cottonwood, account
   `acc_d486fc9455d6b2aa18e13af1` (the PRD's FWD-1 subject), the YTD window, no export: selection-create -> performance
   -> READY -> Summary + area chart, recorded as ONE HAR plus the function's own log line plus the accepted pointer row.
   It crosses hops 1-2 (work), 4 (X10 enforcement + the reason map), 5 (works), 6 (one installed plan), 7 (the first
   live Black Diamond exercise), 9-10 (the reconcile's `retained.py` and `entry.py`), and lands on 13. Owners: the shared
   first hop (boundary, scope, directory business date) is P's; the X10 row is the LGIC register's / CTO's; the plan is
   the CTO's install on Andrew's per-use word; the two portal lines (hops 11, 12) ride with it so the FIRST refusal on the
   way reads true.
2. Refusals read true everywhere (hops 3, 11, 12): three one-line changes, no design decision.
3. The relationship/subset rule (hop 3) and the standard periods + benchmark + spread request shape (hop 8) -- the
   DSGN_IRPTV1 rounds' enrichment, each a newly certified request hash.
4. A standing authorization class for the product's own firm data (hop 6, Andrew's word) so a second account does not
   need a deploy; the claim table stays as the audit.
5. 49 Financial (SmartX feed not received) and Inflection (Orion request builder): separate acceptance matrices, as
   09-22 said; nothing tonight changes them.
6. Export: the 09-22 brief's hops 11-12 stand un-remeasured.

## Acceptance

One reconciled trace per case, each following one request from the selection through the plan claim, the two Black
Diamond requests and their receipt digests, the persisted evidence and report, the accepted pointer, the READY envelope
and the rendered Summary / chart / period table. Cases: Cottonwood x {one account, a relationship} x {YTD, custom window}
x {policy pending, plan absent, plan spent, expired cookie, account without a model assignment, reopen by a second
principal}. The surface is complete when these traces reconcile, not when the parsers pass their fixtures (tonight:
`performance/tests` 131 passed at the source pin, and the deployed path answers nothing).

## Evidence anchors and limits

Source inspected at workspace `c3508c07dff82e4850f1a991ed3acb33b1c79515` and portal `7975c3bbf3f224a98a2a57554c74f54ddfb7b267`;
the deployed source at P's branch `irpt-smoke-p-backend-20260923` @9f360e8f3b; shared work advances concurrently (P's
holdings repackage, the option-B apply and the performance reconcile are queued in that order per CTO 100268).
Verified fresh: the deployed package and configuration, the HAR, CloudWatch, the mapping partitions and parquet, the
requests table, the secret's metadata, the local dry run. NOT verified: the applied IAM on the function role (simulation
returned ALLOWED on every probe including the intended negative control -- unproven); the session cookie's validity;
any vendor response; the export chain; which of the two single accounts is the person the PRD names (the PRD says
`acc_d486...`; both behave identically here).

- `infra/aws/lambda/investor-reporting/performance/{entry,handler,tenants,transport,bd_adapter,orion_adapter,normalize,units}.py` (CLOUD) and the deployed `runtime.py`, `installed.py`, `authorization.py`, `bd_live.py`, `bd_selected.py`, `retained.py`, `retention.py`, `repository.py`, `composition.py`, `served.py`, `errors.py`, `data/assets/scripts/gold/investor_reporting/cot_account_mapping.py`, `infra/logic/registry/reporting_policies.json` (from the downloaded zip)
- `infra/aws/terraform/investor-reporting/performance/{lambda.tf,iam.tf}` (CLOUD); `retained.tf` at 9f360e8f3b
- `infra/logic/06_CONFORMANCE_LEDGER.md:144` (X10)
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/{RULINGS.md,CONTROL.md}` (install GO, VERIFIED LIVE :904-909, P-REOPEN-01, success-status acceptance)
- `portal/src/api/endpoints/investor-reporting.ts:950-1016,1108-1113`; `portal/src/pages/InvestorReporting/{tabs/reporting/ReportingTab.tsx,tabs/holdings/HoldingsTab.tsx,state/status.ts,contracts/adapt.ts:758-830}`
- `C:\Users\AndrewBerman\Downloads\aaaaaa.har` (read in place; no copy made)
- `.runtime/codex-seats/4.0.0_SA_CRO/performance_trace_20260924/evidence.json`

## Andrew-direct request -- verbatim record

Channel: the 4.0.0_SA_CRO terminal, 2026-09-24 ~05:0xZ.

> /closer trace IRPT "Performance Tab". Release your findings to COO~P afterward.
