# ADVI_FIRMBKTS task order -- `FB-h-5` -- THE VALIDATOR'S CANONICAL OWNERSHIP READ, EXERCISED ONCE BY A NON-ADMIN REQUEST (LIVE HALF)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R5.md</decomp_doc>
<owned_cells>FB-h-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reads, and at most one request; no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- `logs filter-log-events`/`describe-log-groups`, `cloudfront get-distribution-config` with the dell1 identity; no grant. The one request, if driven, uses a session already in hand.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a record with a fetch_failed or schema_mismatch event, with zero non-admin lines, with `minted_by_this_order` true, and with a write verb in `calls`. Blindness: the grader proves the record's shape, not that the lines are real; the issuer re-reads one cited log stream.
EGRESS CLASS, declared: NONE (a driven request goes to the product's own host).
</preflight>

## 1. THE CELL -- `FB-h-5` (round 5, enrichment item 2, live half; row `D1-C-S37`, `D1-S17`'s remediation)

`auth-validator-edge` (v23, associated 2026-10-12 15:12:43Z-15:15:10Z) reads the firm's ownership map from the CANONICAL
key since the cutover. In the 27 request lines read after the edge leg, none was on an accounts or a relationship path, so
that read has never been exercised by traffic (FWD-4 is PARTIAL for that reason; `D1-S17`'s remediation stays open on it).
You get ONE real read on those paths, and record it. This is the live half of the CTO's item 2; the offline replay is `FB-h-3`.

### 1a. Steps

1. **Organic first (a read).** Read the validator's Lambda@Edge log groups in every region it has them (the validator's function
   name prefixed `us-east-1.`; read the regions from the distribution's association and the replica log groups, as the
   hourly watch did: 7 regions) from `2026-10-12T15:15:10Z` to now. Count lines on `/platinum/accounts/` and
   `/books/relationship/` paths by a non-admin caller, and the events `ownership_map_fetch_failed`,
   `ownership_map_schema_mismatch`, `advisor_not_in_ownership_map`, `advisor_scoping_denied`. A non-admin request
   that passed (status 200 at the edge, no denial event) counts when the log or the CloudFront standard log shows the path.
2. **Driven, only if step 1 finds none: the dormant Opal UI walker service account, never Andrew's (the CTO's ruling, `ledger/ROUND_ANALYSIS.round4.md` ADDENDUM 1, msg 4662).** It is the cluster's sanctioned non-human login, armed per walk and
   disarmed after (the one `1.0.0_SA_CTO~DELL2`'s seat used for the Inflection product-path read). Drive ONE request on an
   accounts path (or a relationship path) with `--firm 49financial`, by that account, and arm and disarm it as its own runbook says.
   **Never Andrew's session** (he is an admin: his decisions are not the non-admin ones FWD-4 needs, and it is his credential).
   **You do not mint, sign, forge, copy or replay a session or a token, and you do not create a user.**
   **PRECONDITION, read first:** the walker's request must CROSS `auth-validator-edge`; the validator's own log line at the request's
   T0 is the evidence. If the route does not reach the validator (for example a local dev build that calls the API directly), the live read
   is NOT EXERCISED by it: write no record (AC1 stays failing), set this order's `<status>` to `parked` in your commit,
   file a BLOCKING row `ADVI_FIRMBKTS-D1-FB1-S<k>` naming the route, and stop. The order then parks with owner `1.0.0_SA_CTO~DELL1` and the
   un-park condition "the first organic non-admin validator line on those paths"; FWD-4's comparison rests on the offline replay
   (`FB-h-3`) plus that line. A parked order is the correct outcome, not a failure of yours.
   The walker's results are read as tier-and-firm decisions only: no client name, account id or advisor id in the record.
3. **The record `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/round5/VALIDATOR_LIVE_READ.json`**, keys exactly:

```json
{"order": "FB-h-5", "read_at": "<ISO UTC>", "calls": ["aws logs filter-log-events ...", "..."],
 "window_start": "2026-10-12T15:15:10Z", "version": "v23", "log_groups_read": 0, "lines_total": 0,
 "lines_on_ownership_paths": 0, "non_admin_on_ownership_paths": 0, "statuses": {"200": 0, "403": 0},
 "events": {"ownership_map_fetch_failed": 0, "ownership_map_schema_mismatch": 0,
            "advisor_not_in_ownership_map": 0, "advisor_scoping_denied": 0},
 "origin": "organic", "session": {"in_hand": true, "minted_by_this_order": false}, "claim": "measured"}
```

`origin` is `organic` (step 1 found the lines) or `driven` (step 2). `calls` lists each AWS call, one string, beginning
`aws <service> <read-verb>`. Print no token, no user id and no account or advisor id; the record holds counts.

### 1b. What a fetch_failed means

An `ownership_map_fetch_failed` or `ownership_map_schema_mismatch` line after 2026-10-12T15:15:10Z is the validator's canonical
read failing: STOP, record it, and report to `2.0.0_SA_COO~B1` the same turn (it is a Branch B of the edge leg's entry; the
laptop lane's recorded priors were v27/v6/v22 and the rollback is theirs, not yours).

## 2. BOUNDS

1. Reads of CloudWatch logs and CloudFront logs only, plus (step 2) ONE HTTP request by a session already in hand. No deploy,
   no association change, no cache invalidation, no Terraform.
2. No session is minted, no user created, no token written to any file or log.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/round5/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/round5/ADVI_FIRMBKTS.TO-FB-h-5.validator-live-read.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-h-5"><invocation>timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round5/checks/r5_checks.py live --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/round5/VALIDATOR_LIVE_READ.json</invocation><expect>^LIVE-READ non_admin_ownership_lines=[1-9][0-9]* fetch_failed=0 origin=(organic|driven)$</expect></criterion>
</proof_of_spec>

AC1 grades the record. A parked order (no session in hand) leaves AC1 failing on purpose and carries the BLOCKING row.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/round5/ADVI_FIRMBKTS.TO-FB-h-5.validator-live-read.proof_of_spec.json`. Commit the record FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1 passes. Report once to `2.0.0_SA_COO~B1`: the counts, `origin`, AC1 output and the FULL commit hash; or the BLOCKING row id and that the order is parked.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-4 analysis section 3 item 2 (live half): "one signed non-admin session read on those paths". The issuer's standing ruling (RULING_L6_VALIDATOR_FBL.md) is that no seat mints a session; the CTO's list does not say whose session. The order therefore takes an organic line first (the watch FB1 already runs hourly), and a driven read only with a session already in hand; if neither, the order parks with owner `1.0.0_SA_CTO~DELL1` and the condition "a non-admin session exists in a seat's hands or Andrew supplies one". The issuer sends the CTO ONE question on it at the issuance. Class WORLD (a live request path), reads only.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-13 ~06:5xZ):** step 2 carries the CTO's ruling on whose session the driven request uses (ROUND_ANALYSIS.round4.md ADDENDUM 1: the UI walker service account, `--firm 49financial`, never Andrew's; the precondition is that the request crosses the validator). The status reads `pending` again (an uncommitted `parked` in the shared tree, set when no session was in hand, is superseded by the ruling). A criterion is unchanged. The issuer amends its own pending order; no gate limb grades it (the criteria and the `<placeholders>` are untouched).

<status>parked</status>
<round>5</round>
<workstream>VALIDATOR</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-h-5</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
