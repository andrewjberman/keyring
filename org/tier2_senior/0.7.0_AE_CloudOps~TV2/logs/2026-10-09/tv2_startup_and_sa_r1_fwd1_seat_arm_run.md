# 0.7.0_AE_CloudOps~TV2 -- session: lane bring-up and the SA-r-1 FWD-1 seat-arm run

**archetype:** MIXED

Lane `0.7.0_AE_CloudOps~TV2`, seated on dell2 for TCKT_VNEXT only (MSTR msg 3206), branch `box/dell2`,
workspace root `C:/dev/ajb_workspace`.

## Current State

Brought the lane up from nothing: registered LIVE (PID 22688), armed the inbox Monitor and re-armed it on
every `[WATCHER-EXPIRED]` line, wrote the session serial file, ran the audit-archive invoker (18 findings,
all owned by the exec startup path -- not re-filed), confirmed 101 of 102 comp-tools resolve bare with a
forwarder exercised live, wired the owned-paths hook and the comp context. Zero crons, per the launch table.

Held idle through five quiet windows, then measured that the quiet was real rather than deafness: the
watcher's own line names `org/mcp/inbox/0.7.0_AE_CloudOps/~TV2`, the canonical NESTED lane path, and the dead
flat form `inbox/0.7.0_AE_CloudOps~TV2` does not exist (LD-0202).

`TCKT_VNEXT.TO-RUN-SA-r-1` arrived as a FILE at 13:38Z with no broker message, which is the spine's
files-not-messages discipline; a re-measure found it (`to-check` 1 ACTIVE) where the 11:33Z census had
correctly read zero. GO at 15:03Z (msg 3535) cited the order at `@104bc493ed`, a NEWER commit than the staged
bytes with a GO block the staged version lacked, so the order was re-read at current bytes before acting.

**The run (WORLD risk, one pass, complete):**

- **AC1 PASSED.** `reread_27.py` printed `READ27 27/27` rc 0 at 15:08Z. `irpt-status` LastModified
  12:45:28Z -- unmoved since 14:5xZ, so the GO's condition-(1) re-run is satisfied by that invocation.
- **Deployed bytes resolved by CONTENT, never by filename.** `_authz/served.py` at pin `74a62fb46c` hashes to
  `87d9ecc4`, the deployed member on all 7 IRPT hosts, with `HEAD` = `ada9bf5b` as the negative control. The
  409-vs-390 delta is only the IB-pr-405 additive (`SVC_CUSTODY_STATEMENT_OPERATIONS` gains
  `analysis-request-read`), a different subject from this filer. `ticket_center/lambda_function.py` local
  bytes equal the deployed R13 `67068626`.
- **Step 4's one-firm proof ran BEFORE any hop**, the CTO half's condition. Over 27 clamped routes
  (21 IRPT + 6 ticket-api): **22 of 22 EXERCISED arms refused `cottonwood`, 0 admits.** All 21 IRPT routes
  returned `public_reason_code FIRM_BINDING`; `GET /api/scoped/tickets` returned 8 tickets whose distinct
  requester firms are `['49financial']` only.
- **5 ticket-api arms recorded NOT_EXERCISED, not as refusals.** Their gate is
  `_in_profile_scope(actor, ticket.requester.firm)`, keyed on a DynamoDB read, and takes no
  `selected_tenant`; a synthetic id refuses at `cur is None`, a NOT-FOUND byte-identical to a clamp refusal.
  Counting it would be ABSENT read as EXERCISED-AGAINST (rule 22a). Acquiring a cottonwood ticket id to
  exercise it properly is another firm's data and out of bounds.
- **Instrument control held.** The own-firm arms returned varied codes (`NOT_FOUND`, `INVALID_INPUT`,
  `OBJECT_NOT_COVERED`, `None`), not a uniform 401, so the clamp was genuinely reached. This control mattered
  because this principal is DENIED on `opal/auth/jwt-public-key`, so the private/public key pair could not be
  compared directly and the live calls were the only available control.
- **STOP met at step 4:** `GET /api/scoped/data-refresh/history` admitted the filer at **HTTP 200**. Per the
  order no hop ran, and the run went straight to cleanup.
- **Cleanup, same session:** filer row deleted, ConsistentRead read-back **ABSENT**. No ticket existed to
  complete, recorded as `NO_TICKET_CREATED` rather than as a pass. Token left to expire 17:40:57Z.
- No IAM change, no code change, no route change. Every call went over HTTPS through the real CloudFront host
  `d2n2nzpeqf34ge.cloudfront.net`; a direct `lambda invoke` was deliberately NOT used, because the CTO's
  IRPT_YCDGEN ruling `@d54e0b7515` condition 1 says a crafted-context invoke proves one hop and does not
  count. The predecessor lane's script used exactly that pattern and was not copied.

**Two findings, both surfaced before they cost a run:**

1. **Hop (b) was impossible under pair v2.1** -- found from deployed bytes BEFORE minting, reported as
   INFERRED rather than asserted (msg 3584), then confirmed by the issuer in code as row
   `TCKT_VNEXT-D2-S15`. `_create_firm_allowed` requires the firm in BOTH the token's authorizer-derived
   `allowedFirmIds` and the PROFILE row's scope, and v2.1 makes them disjoint (`{opal-capital}` vs
   `{49financial}`). Order amendment n=1 followed; the run's own STOP had already reached that outcome
   independently.
2. **Row `TCKT_VNEXT-D2-S16`, filed by this seat.** W6-S2's routed fix is LIVE and is *why* the pair's
   data-refresh arm cannot be met: `validate_user_type` admits `'Dev'` OR an Opal-internal principal, and
   `_is_opal_internal` is true on `tier == 'internal'` (`OPAL_INTERNAL_TIER`, :138/:161) OR
   `firmId == 'opal-capital'`. The filer must carry `firmId opal-capital` for the ticket service to class it
   INTERNAL, so it is admitted as Opal-internal and `userType` is never consulted. The admit also *proves*
   the fix is deployed: the pre-fix gate refused a non-empty non-Dev `userType`, and `'test-filer'` was
   admitted. Critically, pair **v2.2 does not close this** -- its internal-tier token satisfies the first limb
   directly -- so SA-r-1b would have stopped at step 4 exactly as SA-r-1 did. Raised before minting
   (msg 3607); the COO put the arm to the CTO and issued a HOLD (msg 3612).

## Blockers

**`TCKT_VNEXT.TO-RUN-SA-r-1b` is HELD before minting** on the CTO's ruling for the data-refresh arm
(COO msg 3612). Owner: `1.0.0_SA_CTO~DELL2` via `2.0.0_SA_COO~V2`. This seat does not chase it and builds
nothing on it. Not a blocked seat -- a held order is not a blocked one.

One structural note, not a blocker: the order names the trace path
`deliverables/2.0.0_SA_COO~V2/R1_RUN/sa_r1_trace.json`, which `owned-paths-validate.py` clause 4 refuses to
this lane. The file was written there as ordered and an identical copy (same sha256) was committed under this
seat's own deliverables; `2.0.0_SA_COO~V2` commits the ordered path itself (msg 3612). Authorship was NOT
overridden to get around the gate.

## Next Steps

1. `[1.0.0_SA_CTO~DELL2 via 2.0.0_SA_COO~V2]` Rule the data-refresh arm for pair v2.2. Until it lands,
   SA-r-1b does not mint.
2. `[0.7.0_AE_CloudOps~TV2]` On that ruling: re-read the order at current bytes, open a fresh NEVER-2 ledger,
   STOP 1, then step 4's **widened** census -- every `/api/scoped` route enumerated from the authorizer's
   route list and each host's route table, denominator PRINTED (117 at `@41b7e28bdf`; a different live count
   is itself a finding to print).
3. `[0.7.0_AE_CloudOps~TV2]` Event-driven otherwise: act on each `[INBOX]` event the same turn and re-arm the
   Monitor on each `[WATCHER-EXPIRED]` line in one call, same turn, no skill load.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `comp-find 'TV2' --band HEAD --limit 40` | 226 hits / 76,942 files; found the seating message that identified TCKT_VNEXT as the scope |
| `comp-find` | `comp-find 'issued_to.*TV2' --band HEAD` | measured 0 across 76,941 files -- one of three agreeing reads that the lane held zero orders at 11:33Z |
| `comp-find` | `comp-find --name 'index.mjs' infra/aws` | 8 of 9,202; located `portal-authorizer/index.mjs` |
| `comp-find` | `comp-find 'Ticker,Dollars\|Ticker,Shares\|Symbol,Dollars'` | 100 hits; found the committed holdings fixture `aapl-vnq-12.03.csv` (35 B, sha256 `bb079cbf...`) |
| `to-check.py` | `--all --assignee 0.7.0_AE_CloudOps~TV2` | 0 active at 11:33Z, then 1 ACTIVE at 14:59Z -- the re-measure that caught the staged order |
| `sequence-check.py` | `--project TCKT_VNEXT` | UNPLACED: a register project the sequence does not list, so D7's own rules govern |
| `commit-gate.sh` | on `sa_r1_run.py` | All checks passed (py_compile + ds-precommit + ruff py39) |
| `deploy_ledger.py` | `open` / `close-leg` x4 / `close` | ledger `tckt-vnext-sa-r1-fwd1-seat-arm-20261009` CLOSED, 4 legs proven |
| `reread_27.py` | per AC1 | `READ27 27/27` rc 0 |
| `safe-commit.sh` | the run record | `e652ac4d3e`, 5 files |
| `aws` shim | `lambda get-function`, `dynamodb describe-table/put-item/get-item/delete-item`, `secretsmanager get-secret-value`, `lambda get-function-configuration` | all read/wrote as expected; `get-secret-value` on `opal/auth/jwt-public-key` AccessDenied |

**What failed, and what it taught.** `safe-commit` refused the trace at the ordered path on an owned-paths
lane violation -- the right refusal, and the fix was a copy under an owned path, never an authorship
override. The `to-pipeline-gate` then refused the `complete` flip with no proof-of-spec instance beside it;
I had judged the instance unnecessary because step 7 names the report as the deliverable, and the gate was
right where that judgment was wrong. The comp rail denied three piped census calls (F4) and each denial's
RUN NEXT line was the command that answered.

**Gap.** `comp-iam` was DECLARED-NOT-APPLICABLE by the order's preflight and was not run; no IAM changed.

---

# Delta: SA-r-1b, the FWD-1 seat-arm run under pair v2.2

**archetype:** MIXED

`TCKT_VNEXT.TO-RUN-SA-r-1b` @`68642d02e9`, GO msg 3599, HOLD msg 3612, HOLD LIFTED msg 3622/3637.
Ledger `tckt-vnext-sa-r1b-fwd1-seat-arm-v22-20261009` CLOSED, 5 legs proven. Commit `6ee4714821`.

## What happened

The HOLD I asked for (row D2-S16) worked: the CTO dropped the data-refresh STOP arm rather than let the
run stop by construction, and AMENDMENT 1 added the synthetic attachment to the CREATE arms, which fixed
the exact honesty gap I had reported against my own SA-r-1 trace.

AC1 PASSED again (`READ27 27/27` rc 0, 16:18Z). `irpt-status` had MOVED to LastModified 15:43:11Z since
SA-r-1's 12:45:28Z read; its member hash was still `87d9ecc4`, so the clamp bytes survived the redeploy.

**The widened census**, from the LIVE route table as the GO required, not from the source census:
119 routes on API `7k3ed8px20` against the source census's 117 -- a DIFFERENCE, printed as a finding. The
real delta is 2 live-only `/api/scoped` GETs the source census structurally cannot see (it declares that
blind spot itself): `.../analysis/requests/{requestId}/original` and
`.../books/relationship/{clientKey}/fee-quarter/{quarter}`. The second is served by
`advi-49f-billing-read-lambda`, a host absent from the census's 20 functions, and its producer is the
script whose own help text says it carries client figures -- a firm-scoped surface never graded.

**Clamp result: ZERO off-list admits, ZERO routes serving another firm's data.** Every reachable
IRPT-served arm returned `FIRM_BINDING` for cottonwood and inflection; the ticket LIST returned 8 tickets
with requester firms `['49financial']` only; AMENDMENT 1's CREATE arms reached `_create_firm_allowed` and
both off-list arms were refused 400 with the body NAMING the firm.

## Two things, one of them mine

1. **The STOP was my own detector, not the world.** The run halted on an "off-list admit" at
   `GET /api/scoped/amgt/watchlist`. All three arms returned HTTP 200, body length 2, identical
   fingerprint `4f53cda18c2baa0c` -- an empty list for every firm. My ALL detector required
   `own_len > 80` before calling an identical-fingerprint 2xx "selector ignored", and that floor
   misrouted a SHORT identical 200 into the admit bucket. The discriminator should have been the
   fingerprint alone. Reassessed in the trace, fixed in `sa_r1b_run.py`: length now annotates and never
   classifies. **It cost the hops.** Two further arms were flagged "behaves as ALL" on ticket routes that
   take no `selected_tenant` at all -- applying a selector test to a route with no selector was a
   category error in the same instrument.
2. **Row `TCKT_VNEXT-D2-S18` (ARMED): `irpt-status` 500s on 7 live routes** after its 15:43:11Z deploy.
   Its own log: `TypeError: build_retained_repositories() got an unexpected keyword argument
   'additional_policy_revisions'`, 47 events over 16:18-16:26Z. Measured before and after: 200 with sane
   refusal envelopes at 15:40Z, 500 at 16:19Z, bracketing the deploy. So 6 of the 27 clamped routes are
   ungradeable at HEAD and hop (e) polls one of them -- **FWD-1 could not have completed even without my
   bug.** `reread_27.py` still reads CLAMPED because a member hash cannot see a runtime TypeError raised
   on the way to that code; CLAMPED and 500 are both true at once.

**AMENDMENT 2's negative proof carries its controls.** `/aws/lambda/opal-data-refresh-api` over
[16:19:13Z, 16:26Z] filtered for the filer: 0. The group exists (243,076 bytes) and is live (5 events in
24h); the window holds 0 events even unfiltered; and the POSITIVE CONTROL over SA-r-1's window, where the
filer DID call, returns 3 matches including the gate's own line `User tckt-fwd1-...@opal.invalid
userType=test-filer admitted as Opal-internal`. The filter finds the filer when it called and none when
it did not, so the zero is a TRUE NEGATIVE -- and that line is the deployed gate confirming D2-S16 verbatim.

Cleanup: row deleted, ConsistentRead read-back ABSENT; the one ticket the census created
(`TCK-20261009-47fe2bb6`) COMPLETED http 200; token left to expire 18:19:13Z. No IAM, code or route change.

## Blockers

**Step 5 never ran, so the order is NOT flipped -- it stays `pending` and re-issue is the issuer's call.**
A re-run cannot succeed until `irpt-status` is repaired: hop (e) polls one of the 500 routes. Owner of that
fix is the IRPT_BCKEND release line that deployed at 15:43:11Z, routed via `2.0.0_SA_COO~V2`. This seat
changes no code there.

## Compiler Tools (delta)

| tool | invocation | result |
|---|---|---|
| `reread_27.py` | AC1 for SA-r-1b | `READ27 27/27` rc 0; irpt-status moved to 15:43:11Z, member hash unchanged |
| `apigatewayv2 get-routes/get-integrations` | live route table + route->Lambda map, paginated client-side | 119 routes, 91 `/api/scoped`, 14 Lambdas; 2 live-only scoped GETs found |
| `logs filter_log_events` | irpt-status 16:18-16:26Z | 47 error events; the TypeError that pins row S18 |
| `logs filter_log_events` | data_refresh, filer, both windows | 3 matches in SA-r-1's window (positive control), 0 in SA-r-1b's (the proof) |
| `commit-gate.sh` | `sa_r1b_run.py`, twice | clean both times (before the run and after the detector fix) |
| `deploy_ledger.py` | 5 legs | CLOSED, all proven |
| `safe-commit.sh` | the run record | `6ee4714821` after two refusals, below |

**What failed, and what it taught.** The `surprise-row-gate` refused my commit because `TCKT_VNEXT-D2-S17`
already existed at HEAD -- the COO filed that id while this run was in flight -- so my row became S18. An
id is one row, and the gate was the only thing that would have caught the collision. (The commit SUBJECT
still says S17; it was written before the renumber. The row itself is S18 everywhere.) Earlier, the
`to-pipeline-gate` refused the SA-r-1 `complete` flip twice: once for a missing proof-of-spec instance I had
judged unnecessary, then for two precise schema violations (`controls` admits only `mutant`/`determinism`
under the BUILD branch, and a non-PASS `status` requires `status_reason`). I folded both negative controls
into `mutant` rather than setting `genre: DEPLOY` to unlock arbitrary control names, which would have been
gaming the schema to pass a gate.

---

# Delta: SA-r-1b runs 3 and 4 -- the FWD-1 journey finally ran

**archetype:** MIXED

Order @`68642d02e9` AMENDMENT 4 (watchlist NOT a STOP by code read; leak = a differing off-list payload OR
code that reads the selector). GO msg 3756. Ledger opened BEFORE run 3, as the issuer required after the
run-2 lapse. Records @`66bfdf5c2e`. Order flipped `complete`.

## What happened

**The census passed on both attempts.** 82 of 91 live `/api/scoped` routes armed, 9 data-refresh skipped,
live denominator 119 against the source census's 117. Zero off-list admits; zero leaks on limb 1 and zero
on limb 2 with zero UNKNOWN. AMENDMENT 1's CREATE arms reached the firm clamp and both off-list arms were
refused 400 with the body NAMING the firm -- the thing SA-r-1's attachment-less arm could not establish.

Limb 2 is carried as a verified code-read TABLE rather than a source-dir walk, because the walk
**understates**: `irpt-holdings` counts 0 occurrences of the selector in its own dir yet refuses off-list
targets through the shared `_authz` boundary bundled in from outside it. A walk would have cleared a route
that does read the selector.

**Run 4 ran the whole journey:** (a) 200 NORMALIZED on poll 1, (b) 201 `TCK-20261009-67ab7f27`, (c) 200,
(d) 200 accepted with the `request_id` echoed, (e) 60 polls, (f) 200, (g) ticket 200 + request read 200
with `report_ref` present. A direct `ConsistentRead` of `opal-tickets` corroborates it independently.

## Four defects of mine, in order, and what each cost

1. **Run 3's hop (d)** sent 2 fields where `AnalysisSubmissionRequest` requires 8 with
   `additionalProperties: false` -- refused `MISSING_REQUEST_FIELD`, typed cause visible only in CloudWatch.
   Cost: one whole run. Fix: read the published contract, rebuild the body, and **validate it offline
   against the schema before re-running** (run 3 body = 8 violations, run 4 body = valid).
2. **The upload state oracle** read `status.state` where the result carries `state`, so run 3 polled all 14
   times although the `input_id` landed on poll 2. Cost: ~60s and a misleading log.
3. **`save()` keyed every later run to a fixed `run_2` slot**, so run 3 overwrote run 2's trace section.
   Cost: nothing measurable -- run 2 was recovered from its own commit `e2c7f7b25a`. Fix: next free `run_N`,
   reusing a run's own slot; both properties verified on a scratch file.
4. **Hop (e) polled `state`** and read `UNAVAILABLE`, a value absent from the contract's progress enum
   (`AnalysisRequest.stage`: RECEIVED | PARSED | NEEDS_CORRECTION | READY | SUBMITTING | GENERATED |
   RELEASED | FAILED). So (e) named itself a failure on its own blindness. Fixed to read `stage`.

The pattern across all four, and across runs 1-2's two false STOPs: **I kept writing oracles without a
control, and the fix each time was a check that costs nothing** -- validate the body against its schema,
replay the classifier against recorded data, verify the slot allocator on a scratch file. By run 4 I was
doing that first, which is why run 4's changes worked on the first attempt.

## What is NOT claimed

The analysis's real `stage` is **UNVERIFIABLE-BY-INSTRUMENT** from this seat: a narrow `begins_with` query
of `irpt-requests` on this run's own `request_id` was AccessDenied on `kms:Decrypt`, and the order's bounds
forbid an IAM change. A `report_ref` is a reference, not a report. AC2 is CVO judgment at L9, so the proof
instance states the evidence and withholds the verdict.

## Rows filed

- **`TCKT_VNEXT-D2-S18`** -- irpt-status 500s on 7 routes after its 15:43:11Z deploy. Repaired in the world
  by the Branch B rollback, which I measured (limb 3 passed; the 6 clamped routes refuse off-list firms
  again). Disarming stays its owner's call.
- **`TCKT_VNEXT-D2-S20`** -- the pair's stated rollback "remove the row" does not narrow the token, it
  **WIDENS** it: the row is the narrowing, and with it gone `_internal_allowed_firms` returns None, which
  the boundary reads as no restriction. Each token's reach was wider after its cleanup than during its run;
  only `exp` bounds it. INERT in fact (the tokens lived only in process memory) but wrong as written.

## Blockers

None at this seat. The order is `complete`; `superseded`/re-cut and the L9 grade are others' calls.

## Compiler Tools (delta)

| tool | invocation | result |
|---|---|---|
| `jsonschema` | `AnalysisSubmissionRequest.schema.json` against both bodies | run 3: 8 violations; run 4: valid -- offline, before spending a run |
| `jsonschema` | `PROOF_OF_SPEC.schema.json` against the instance | caught `determinism.status` needing STABLE, not FIRED-AS-EXPECTED, before the gate did |
| `apigatewayv2` | `get_apis` + `get_routes` + `get_integrations`, paginated client-side | 119 live vs 117 source; 91 scoped across 14 Lambdas |
| `dynamodb` | `ConsistentRead` of `opal-tickets`; narrow `begins_with` query of `irpt-requests` | the ticket corroborated; the request record AccessDenied on KMS |
| `logs filter_log_events` | irpt-ycharts-generate; opal-data-refresh-api both arms | `MISSING_REQUEST_FIELD` as (d)'s typed cause; 3 matches in the control window, 0 in the proof windows |
| `deploy_ledger.py` | 6 legs for runs 3+4 | CLOSED, opened BEFORE the run |

**What failed, and what it taught.** The ledger's HOP proof was passed to the tool **through the shell** with
field names in backticks, so bash ran them as command substitution and elided both words -- the proof read
"it polled  and read UNAVAILABLE". That is the execution-vector trap CLAUDE.md names for commit messages
(`-F` from a non-shell writer, never `-m` with special characters), and it applies to any proof text handed to
a tool through a shell. Repaired in the entry with the repair disclosed in its own Log, written by a file.
