# NFRA_MCPORTAL task order -- `MP-pc-2` -- WORKSTREAM PC ROUND 1: the owner-gated per-person view handler (FWD-21 read, F1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pc-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pc-2</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~21</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a request handler; read when opened (PRD C8).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the grant-store Scan it reuses is MP-z-4's grant, already applied.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (a candidate holding nothing, a tool with no tool_index row, kill switch, unreadable store, non-owner, the seam to the breakdown with its difference control).
EGRESS CLASS, declared: none. Every store read in a test is a fake client.
</preflight>

## 1. THE CELL -- `MP-pc-2` (workstream PC round 1, decomposition sections PC.1 and PC.3)

Your worktree is `C:/tmp/mp-pc-21` (branch `wk-NFRA_MCPORTAL-pc-21`). Work and commit only there.

Andrew wants to pick a person and see what that person reaches through the gateway: the channels, the tools on each,
the tier, and each tool's history depth and poll cadence (PRD v0.8 FWD-21). This cell is the READ half. Nothing here
writes. The gateway already answers the channel-first view, `GET /api/admin/gateway/breakdown`, in
`infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py` (read it whole first). This cell inverts it per person
WITHOUT editing that file. A parallel cell builds the page against the response below, so do not rename or drop a field.

Build, in the gateway app at `infra/aws/ec2/opal-gateway/`:

1. **`app/admin_people.py` (new).** It has ONE handler, `people`, decorated with `owner_gate.owner_only`, and a module
   function `_compute(scan_client=None, store=None)` that returns the body (a release check calls `_compute()` on the
   host). Run `_compute` in `run_in_threadpool`, as `admin_gateway_breakdown.breakdown` does. The body, exactly:
   ```
   { "read_at": "<ISO Z>",
     "kill_switch": true | false,
     "people": [
       { "who": "<email or display>",
         "kind": "person" | "population",
         "how": "<basis, as the breakdown's holder rows phrase it; '; '-joined when several>",
         "tier": "<tier.resolve_tier value>" | "unresolved",
         "channels": [
           { "id": "<channel id>", "name": "<channel name>",
             "tools": [ { "name": "<tool>",
                          "history_depth": {"claim": "measured" | "inferred" | "absent", "value": <as catalogued> | null, "reason": "<text>" | null},
                          "freshness":     {"claim": "measured" | "inferred" | "absent", "value": <as catalogued> | null, "reason": "<text>" | null},
                          "cadence":       {"claim": "absent", "value": null, "reason": "no poll-cadence source is served yet (NFRA_OPLGTW FWD-20)"} } ] } ] } ],
     "people_basis": "<one line: the candidate sources, and any gap>",
     "grant_store": {"status": "read" | "unreadable", "principals": <int> | null, "reason": "<text>" | null} }
   ```
   - **People** = EVERY candidate the breakdown evaluates in `_compute`'s inner `evaluate()` (about `:265-336`):
     `MASTER_ADMIN_EMAILS`, `WRITE_CAPABLE_EMAILS`, `MASTER_ADMIN_PRINCIPALS`, `WRITE_CAPABLE_PRINCIPALS`, every scoped
     identity `identity_scope` knows, every principal with a `principal_profile` in the grant store (the breakdown's
     `_scan_principals`, about `:174`), and the population row (`_POPULATION_EMAIL`, about `:43`). Build the same
     candidates the same way. Import and call the breakdown module's own helpers (`_admits`, `_scan_principals`, its
     candidate type, its channel construction) rather than copying their bodies. Where a helper you need exists only
     inline inside `evaluate()`, re-derive the CANDIDATE LIST from the same config and store sources it reads (that is
     enumeration, not an access rule), and call `_admits` for every access decision. Never re-type an access rule.
   - A person appears whether or not it holds any tool. A person holding nothing has `channels: []`.
     `opalbloomberg@opalinvest.com` is listed like any other person whenever a source names it. `kind` is "population"
     for the population row only (`who` "every signed-in Opal Microsoft user", as the breakdown words it), else
     "person". Order: `MASTER_ADMIN_EMAILS` first (that is Andrew), then by `who`, the population row last. One row per
     person: a person in several sources gets one row, with the bases joined by "; " in `how`.
   - **What a person holds:** a tool is listed under a person iff `_admits(candidate, tool)` is True. Use the same channel
     placement as the breakdown (a channel appears under a person only when the person holds at least one of its tools,
     and lists only those tools). Channel `id` and `name` are exactly the breakdown's.
   - **`tier`:** the value `tier.resolve_tier` gives for the candidate, built the way the breakdown builds the candidate's
     request identity; "unresolved" when it cannot be resolved for that candidate, never a guessed tier.
   - **Depth and freshness:** load `app/refs/DATA_CATALOG.yaml` once per `_compute`. Its top-level `tool_index:` list
     (about `:1359`) has one row per tool, keyed by `tool:`. A row's `history_depth:` and `freshness:` are mappings with
     a `claim` (measured / inferred / absent) and a `value` or a `reason` (a `freshness` may also carry `row`). Carry
     `claim`, `value` (or null) and `reason` (or null) through. A tool with no `tool_index` row, or a row with no such
     key (member b or c rows carry none), reads `{"claim": "absent", "value": null, "reason": "no tool_index row"}`.
     Never blank, and never a default value.
   - **Cadence:** exactly `{"claim": "absent", "value": null, "reason": "no poll-cadence source is served yet
     (NFRA_OPLGTW FWD-20)"}` for every tool.
   - **Kill switch on:** every person's `channels` is `[]`, and `people_basis` says "kill switch on: no one may call".
   - **`grant_store`:** exactly as the breakdown reports it. A Scan that fails gives "unreadable" with the reason. The
     profiled principals are then missing, `people_basis` names that gap, and the handler still answers 200.
   - **Writes:** none. This module calls no write API of any store.
2. **DO NOT edit `app/admin_gateway_breakdown.py` or `app/admin_api.py`.** The release cell adds
   `Route("/people", admin_people.people, methods=["GET"])` and its import. Name that line in your report.
3. **`tests/test_admin_people.py` (new).** Mount the handler on a `Starlette` test app, as
   `tests/test_admin_gateway_breakdown.py` does (reuse its stubbing approach). These eight tests, by these exact names:
   - `test_people_lists_every_candidate_even_holding_nothing`: a planted candidate admitted to no tool is listed with
     `channels: []`.
   - `test_depth_and_freshness_carry_their_claims`: a planted `tool_index` row with `history_depth` claim measured and a
     value is carried through; a tool with no row reads claim "absent" with reason "no tool_index row".
   - `test_cadence_reads_absent_with_reason`: every tool's `cadence` is exactly the PC.3 object.
   - `test_kill_switch_empties_every_person`: kill switch on; every `channels` is [] and the basis says so.
   - `test_people_grant_store_unreadable_is_labelled`: a fake Scan raising botocore `ClientError` AccessDenied gives 200,
     `grant_store.status` "unreadable" with the reason, and the basis names the gap.
   - `test_people_non_owner_is_refused`: a non-owner gets 403, and the fake clients record zero calls.
   - `test_person_holdings_equal_breakdown_holders`: THE SEAM. In one planted world, call BOTH `admin_gateway_breakdown`
     `_compute` and this `_compute`. For every person, the set of (channel id, tool) pairs this view lists EQUALS the
     set the breakdown's holder rows list for that `who`. Difference control in the same test: blocklist one planted
     person, and BOTH sides become empty for it.
   - `test_real_server_people_inventory`: with the real `app.tools.mcp` registered list, as the test environment leaves
     the registry, every tool any person is listed holding is a tool the server registers, and no channel id is
     invented.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not change any other `app/` module or test, Terraform, the
   manifest, or anything in `mcportal/`. Make no deploy and no AWS call.
2. If a chain or helper cannot be reused without editing the breakdown module, REFUSE that criterion with what you
   measured and file a BLOCKING row. Never re-type the rule to make the test pass.
3. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md
   14a). If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_people.py
infra/aws/ec2/opal-gateway/tests/test_admin_people.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~21/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `app/admin_gateway_breakdown.py`, `tests/test_admin_gateway_breakdown.py`, every other
`infra/aws/ec2/opal-gateway/app/` module, `app/refs/DATA_CATALOG.yaml`, and
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pc/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W21-S<k>` (the next free k for W21). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an
ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pc-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pc/checks/pc2.AC1.sh; echo "exit=$?"</invocation><expect>people tests: 0 failed; named tests PASSED 6 of 6 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pc-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pc/checks/pc2.AC2.sh; echo "exit=$?"</invocation><expect>people seam: 0 failed; named tests PASSED 2 of 2 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~21/NFRA_MCPORTAL.TO-MP-pc-2.people-handler.proof_of_spec.json`.
Report once, with:
- the two check outputs;
- the commit hash;
- the route line for the issuer;
- from `test_real_server_people_inventory`: the person count and the tools each holds in the test environment;
- every breakdown helper you imported, and anything you had to re-derive and from which source;
- any field of the response you could not fill as written, and why;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PC issuance (decomposition v9) from PRD v0.8 FWD-21 and C15 @7da54894cf, and the C17
round-2 analysis @d0dd3f0964 (F1). Checks dry-run at base 9be88c9134: AC1 FAIL (test file absent), AC2 FAIL (test file
absent). The research read for the cut (per-call chain, depth fields, breakdown internals) is in decomposition PC.0. NFRA_MCPINDEX MX-c-9 edits
`admin_gateway_breakdown.py:108` (msg 33864); this cell only imports from that file. Lives through MP-pc-5.

<status>complete</status>
<round>1</round>
<workstream>PC</workstream>
<slot>~21</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
