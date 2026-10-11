# TO NFRA_OPSWKF.TO-OW-s2 -- the trade dashboard service refuses every caller whose tier is not internal

<to_id>NFRA_OPSWKF.TO-OW-s2</to_id>
<project>NFRA_OPSWKF</project>
<issued_to>0.9.0_WK_NFRA_OPSWKF~8</issued_to>
<issued_by>2.0.0_SA_COO~O2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>S</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (path floor: a Lambda handler; you apply nothing) | **Decomp cell:** `OW-s-2` |
**outcome_ref:** FWD-8 | **depends_on:** none.

---

## WORKER FACE

You are `0.9.0_WK_NFRA_OPSWKF~8`. Your worktree is `C:/tmp/opswkf-s-8` (branch `wk-NFRA_OPSWKF-8`, cut from box/dell2 at the
issuance commit). Work and commit ONLY there with `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_OPSWKF~8
<0.9.0_WK_NFRA_OPSWKF~8@opal.agent>" -F <msgfile> -- <paths>`; write the message file with the Write tool.

### THE CELL

`OW-s-2`. `infra/aws/lambda/trade-pipeline/trade-dashboard-api/src/dashboard_api.py` (527 lines; read it whole first). Its
router `lambda_handler` (lines 38-85) hands every handler only the query string or a path id, except `get_users_me`, which
gets the event. So eight routed reads return Opal's trade submissions, a download link, or the whole trade-users list to ANY
caller the portal authorizer verified. The owner's ruling: **the router passes the event to every handler; each requires
tier `internal`; the caller's own-record route stays exactly as it is.**

Build this, and nothing else:

1. Add `_require_internal(event)`. It reads the authorizer context the way `get_users_me` already does (lines 387-388:
   `event.requestContext.authorizer`, then `.get('lambda', ctx)`), takes `tier`, and returns `None` when
   `str(tier or '').strip() == 'internal'` (EXACT match). Otherwise it returns
   `cors_response(403, {'message': 'Forbidden: this route answers Opal staff only'})`. Fail closed: no context, no `tier`,
   an empty string, the string `null`, `client`, `service`, or anything else is refused. It reads no table.
2. The router passes `event` to every handler it calls. Each of these checks FIRST, before any `dynamodb` or `s3` use, and
   returns the 403 when the check returns one: `get_pending_submissions`, `get_by_initiator`, `get_by_approver`,
   `get_by_status`, `get_by_date`, `get_excel_download`, `get_submission`, `get_users`, `get_recent_submissions` (this last is
   also the router's default branch, so an unknown path is refused too). The `/excel` branch's own 400 for a path with no
   `TRADE-` part must also come AFTER the check.
3. `get_users_me` is not changed: a client-tier caller still gets its own row from it.
4. The three aggregate functions at lines 413-513 (`get_initiator_dashboard`, `get_approver_dashboard`,
   `get_executor_dashboard`) are called by nothing. Give each the same first-line check and an `event` first parameter, so no
   function in the file returns submissions without it. Change nothing else: no response body, no query, no CORS header,
   no logging of a caller's claims.

How you thread `event` (a first parameter on each handler, keeping `params` or the id after it) is yours; the checks below
call only `lambda_handler`.

**Tests:** `infra/aws/lambda/trade-pipeline/trade-dashboard-api/tests/test_internal_only.py` (new; the `tests/` folder does
not exist yet). Stub `dashboard_api.dynamodb` and `dashboard_api.s3` the way
`infra/aws/lambda/trade-pipeline/trade-submission-handler/tests/test_initiator_from_token.py` stubs its table (read it), set
`AWS_DEFAULT_REGION` before the import, and build events with `rawPath`, `queryStringParameters`, and
`requestContext = {"http": {"method": "GET"}, "authorizer": {"lambda": {...claims...}}}`. Exact test names:

- `test_internal_caller_served_on_every_route`: tier `internal` gets 200 or 404, never 403, on each of the eight routes and `by-date`.
- `test_client_tier_refused_on_every_route`: tier `client` gets 403 on each.
- `test_service_tier_refused_on_every_route`: tier `service` gets 403 on each.
- `test_no_authorizer_context_refused_on_every_route`: no `authorizer` key gets 403 on each.
- `test_refusal_touches_no_table_and_no_s3`: with stubs that raise on any use, a refused call still returns 403.
- `test_users_me_unchanged_for_client_tier`: `/api/general/trades/users/me` as tier `client` returns 200 with the caller's own email.

The route paths: `/api/general/trades/submissions`, `.../submissions/pending`, `.../submissions/by-status`,
`.../submissions/by-initiator`, `.../submissions/by-approver`, `.../submissions/TRADE-<id>`, `.../submissions/TRADE-<id>/excel`,
`.../users`, and the branch `.../submissions/by-date`.

### AMENDMENT 1 (2026-10-11 ~18:4xZ, the issuer) -- OPAL-INTERNAL is tier exactly `internal` OR firmId exactly `opal-capital`

**This amendment overrides every "tier internal" sentence above.** PRD v0.6 @ca5f93a729 (ruled by `1.0.0_SA_CTO~DELL2`, msg 5574,
on row NFRA_OPSWKF-D2-S6): 7 of the 9 real trade users carry tier `advisor` with firmId `opal-capital`, so a tier-only check
locks Opal staff out of their own blotter. Your first build (commit c02c0aa8e7 on this branch) is inherited state: keep it and
change only this.

1. Rename nothing. `_require_internal(event)` now admits a caller when `str(tier or '').strip() == 'internal'` OR
   `str(firmId or '').strip() == 'opal-capital'`. Both are EXACT string matches, never truthiness: the authorizer sends the
   STRING `null` for an absent firmId, and `if firm_id` would be True for it. Anything else is refused with the same 403.
   This is the estate's existing rule; read `infra/aws/lambda/data_refresh/lambda_function.py:142-165` (`is_opal_internal`)
   and write the same two comparisons with two module constants (`OPAL_INTERNAL_TIER = 'internal'`,
   `OPAL_INTERNAL_FIRM_ID = 'opal-capital'`). `userType` is NOT read: a `Dev` user of another firm is refused.
2. Change the 403 message to `Forbidden: this route answers Opal staff only` (unchanged) and the helper's docstring to state
   the two comparisons. Nothing else in the handler changes.
3. Add two tests to `test_internal_only.py`, exact names:
   - `test_opal_capital_firm_served_whatever_the_tier`: tier `advisor`, firmId `opal-capital` gets 200 or 404 on every route.
   - `test_advisor_tier_of_another_firm_refused`: tier `advisor`, firmId `49financial` gets 403 on every route; so does the
     same caller with `userType` `Dev`.
   Give the callers in your existing refusal tests a `firmId` that is not `opal-capital` (the service caller: the string `null`).
4. The check file `ow_s_checks.py` on this branch is already the amended one (the issuer placed it; do not edit it). Both
   criteria below keep their ids and invocations. Re-run both, rewrite the proof-of-spec instance for the new outputs,
   re-validate, flip `<status>` back to `complete`, and commit handler + tests + instance + flip together.

### ACCEPTANCE

<criterion id="OW-s2-AC1" cell_refs="OW-s-2"><invocation>python org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/S_CHECKS/ow_s_checks.py s2-tests</invocation><expect>OW-S2-TESTS-OK</expect></criterion>
`OW-s2-AC1`: the eight named tests exist and pass (six from the first cut, two from AMENDMENT 1).

<criterion id="OW-s2-AC2" cell_refs="OW-s-2"><invocation>python org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/S_CHECKS/ow_s_checks.py s2-probe</invocation><expect>OW-S2-PROBE-OK</expect></criterion>
`OW-s2-AC2`: the issuer's own probe of `lambda_handler` -- eight outsiders (a client, a service token with firmId `null`, an
advisor of another firm, a `Dev` of another firm, an empty tier, tier and firm both the string `null`, a near-miss spelling,
no context) on ten paths (the eight routes, `by-date`, an unknown path) are each answered 403 with no table or S3 touched;
three insiders (tier internal; tier internal with no firm; tier advisor with firmId `opal-capital`) are answered 200 or 404 on
all ten; `users/me` still answers a client-tier caller. The handler's own `print` of a traceback may appear above the check
line when a path is wrong; the last line is the verdict.

<expected_criteria>OW-s2-AC1,OW-s2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block, your deliverables folder `org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~8/`,
  and this order's file (status flip only). `config.py`, `excel_generator.py` and every other handler are READ only.
- Never call AWS. Deploy nothing. Touch no Terraform and no portal file.
- No non-ASCII in anything you write (the handler file is ASCII today; keep it so). If you need a row, append it in BINARY
  mode as `NFRA_OPSWKF-D2-W8-S<k>`, keeping the file's line endings; `surfaced_at` = `date -u +%FT%TZ` at filing.

<paths>
infra/aws/lambda/trade-pipeline/trade-dashboard-api/src/dashboard_api.py
infra/aws/lambda/trade-pipeline/trade-dashboard-api/tests/test_internal_only.py
org/missions/D9/NFRA/NFRA_OPSWKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPSWKF/decompositions/NFRA_OPSWKF_DECOMP.md</decomp_doc> (workstream S), cell `OW-s-2`.
<owned_cells>OW-s-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: OW-s2-AC1, OW-s2-AC2. The instance is at
`org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~8/NFRA_OPSWKF.TO-OW-s2.dashboard-internal-only.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> OW-s2-AC1,OW-s2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (once):** both check lines verbatim, the commits, the names of every function you changed, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, hold or gate is created or consumed by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the handler reads no new resource
comp-adversary: DECLARED-NOT-APPLICABLE at the cut (nothing built yet); the adversarial read of this authorization change runs at the drain on the merged handler, and criterion OW-s2-AC2 is the issuer's own probe of it
lane: trade-pipeline dashboard service; TRSB_LEDGER (inactive) wrote it last; no open order on it.
</preflight>

Release: `1.0.0_SA_CTO~DELL2` msg 5533 on `3.0.0_SA_CVO`'s verdict @287ea37a51. Remedy shape: the laptop CTO's ruling @8e9ca364d7.
The release (cell `OW-s-d-1`) is the issuer's, under its pair; this order applies nothing.
