# NFRA_MCPORTAL -- surprise channel, INVESTIGATION v1 (site-Z fabric)

**Home:** the project tree's channel. Lane `ANY`; `.tools/surprise-row-gate.py` validates every NEW row
(schema, identity, coordinate, folder == project). **Append-only.**

**Id grammar on this fabric:** a seat's row is `NFRA_MCPORTAL-Z-S<k>`; a worker's row is
`NFRA_MCPORTAL-Z-W<n>-S<k>` with `<n>` its slot; `<k>` restarts at 1 per coordinate. `"project":
"NFRA_MCPORTAL"` and `"fabric": "site-z"` on every new row. The CVO's adjudication rows live in
`adjudications/`, never here.

---

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-W3-S1",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~3",
    "surfaced_at": "2026-09-24T23:55Z",
    "one_line": "_root.sh's mp_writer_entry() (shared by t2.AC1.sh, t2.AC2.sh and t2.AC3.sh) is a SyntaxError inside a redirected python -c one-liner, so all three MP-t-2 checks read an empty source-map lookup and FAIL regardless of whether the cell's registry row, source, tests and Terraform are conforming.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/_root.sh mp_writer_entry(): `print(len(hits)); [print(k); print(v.get('source_dir','')); print(v.get('tf_file','')) for k,v in hits[:1]]` -- a list comprehension cannot contain semicolon-separated statements.",
        "Running that exact string through `python -c` (no redirect) raises `SyntaxError: invalid syntax` at the second `print(...)` inside the brackets; t2.AC1.sh's own invocation of mp_writer_entry() carries `2>/dev/null` inside the function, so the error is swallowed and $e is empty.",
        "The underlying data is conforming: python -c \"import json; d=json.load(open('infra/aws/lambda/ci/lambda-source-map.json',encoding='utf-8'))['functions']; hits=[(k,v) for k,v in d.items() if 'mcportal' in (v.get('source_dir') or '') and 'grant-writer' in k]; print(len(hits))\" prints 1, with source_dir=infra/aws/lambda/mcportal/mcportal-grant-writer-lambda and tf_file=infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf, both real paths in this worktree.",
        "t2.AC1.sh: `name()=mcportal-grant-writer-lambda; source-map entries= key=; source_dir exists=no; tf_file exists=no` / `RESULT: FAIL` / exit=1. t2.AC2.sh: `writer tests absent (/tests/test_grant_writer.py)` / `RESULT: FAIL` / exit=1 (src is empty, so the path is a bare `/tests/...`, even though `.../mcportal-grant-writer-lambda/tests/test_grant_writer.py` exists and its 4 named tests pass 4/4 under plain pytest). t2.AC3.sh: `tf_file absent` / `RESULT: FAIL` / exit=1, even though `infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf` exists and is terraform-fmt-clean. All three measured at CLOUD HEAD 054bad6cc7 + this worker's own commit."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Each of MP-t-2's three literal invocations (`bash .../checks/t2.AC{1,2,3}.sh`) is expected to print `RESULT: PASS` / exit=0 once the builder name resolves, the source-map carries exactly one conforming entry, the tests pass and the Terraform is present and fmt-clean.",
    "world_is": "The shared mp_writer_entry() helper cannot report a non-empty result for ANY conforming entry, ever, because its embedded python fails to parse before it prints anything -- so all three checks FAIL from that one empty lookup regardless of the cell's own state. The defect is in the check, not in this cell's registry row, source directory, tests or Terraform file (all four are present and independently verified correct above and in this worker's proof-of-spec instance).",
    "notes": "Not in this worker's <paths> (org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/** is the issuer's own), so not repaired here -- recorded and the literal AC1 invocation's output kept verbatim in this worker's proof-of-spec instance as FAIL, per the worker rule against repairing a criterion. ARMED because every future re-run of t2.AC1.sh (by MP-t-3, by a re-check, by a fresh worktree) hits the same SyntaxError regardless of what any worker builds."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S1",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-24T23:55Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_MCPORTAL-Z-W3-S1 (owner this seat): the checker defect is fixed at CLOUD @259e1cf375 and carried onto this branch; the fixed _root.sh reads the writer entry here (entries=1) and none at the base (entries=0), so t2.AC1-AC3 now grade the cell.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Issuer dry-run of the fixed checker, both arms, 2026-09-24 ~23:5xZ: main tree t2.AC1 'source-map entries=0' FAIL, t2.AC2 FAIL, t2.AC3 FAIL; wk-NFRA_MCPORTAL-3 @b1cd5fca01 t2.AC1 'entries=1 key=mcportal-grant-writer-lambda' PASS, t2.AC2 'named tests passed 4 of 4' PASS, t2.AC3 'fmt rc=0 ... sts:AssumeRole outside a Lambda trust policy=0' PASS.",
        "The defect was the issuer's: mp_writer_entry's python -c held statements in a list comprehension (SyntaxError) and its 2>/dev/null silenced it; the issuer's own base dry-run read the empty lookup as the expected FAIL."
      ]
    },
    "spec_asserts": "NFRA_MCPORTAL-Z-W3-S1 is ARMED with this seat as disarm_owner.",
    "world_is": "The criteria now discriminate; the cell's recorded FAILs were the instrument's, and the order is re-run by a fresh worker on this slot to rewrite its instance against the fixed checker.",
    "notes": "The mistake the assignee caught is the one the refusal clause exists for: the author cannot be the control on its own criteria. No gate is built here."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W1-S1",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~1",
    "surfaced_at": "2026-09-24T20:05Z",
    "one_line": ".tools/owned-paths-validate.py's --check-agent CLI resolves `resolve_lane(path, paths_config)` BEFORE ever consulting the ADHC_OWNPTH.005 task-order-paths worker grant, so a worker task-ordered to create a genuinely NEW top-level path (never enumerated as a pattern in .owned-paths.yaml) is refused UNDEFINED and can never reach the grant clause that names it in its own <paths> block.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/owned-paths-validate.py `_cmd_check_agent` (worktree wk-NFRA_MCPORTAL-1): `lane_name = resolve_lane(path, paths_config); if lane_name is None: violations.append(f\"VIOLATION: {path} -- UNDEFINED (no matching path rule; agent={agent})\"); continue` -- `check_agent` (which holds the `_owns_task_order_paths` ADHC_OWNPTH.005 clause) is never called on this branch.",
        "`check_agent()` itself also gates on the same condition first: `lane_name = resolve_lane(path, paths_config); if lane_name is None: return False  # unmapped path` -- the ADHC_OWNPTH.005 clause is unreachable code for any path absent from `paths_config`.",
        "Reproduced live: `printf '.gitmodules\\nmcportal\\n' | python .tools/owned-paths-validate.py --check-agent \"0.9.0_WK_NFRA_MCPORTAL~1\" .owned-paths.yaml` -- `.gitmodules` (which HAS a `.owned-paths.yaml` entry, lane BASE_EXEC) passes via the ADHC_OWNPTH.005 grant naming it in my task order's `<paths>`; `mcportal` (which has NO entry in `.owned-paths.yaml` -- it is the brand-new top-level path my task order MP-w-1 <paths> names verbatim) is refused `UNDEFINED (no matching path rule)`, exit 1.",
        "My task order `org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-w-1.repo-and-shell.md` @HEAD (this worktree, based b99ab96fdf) section 3 `<paths>` names `mcportal` and `mcportal/` verbatim -- a legitimate worker grant the gate cannot see."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md rule 14a and ADHC_OWNPTH.005's own doc comment: 'a worker serial 0.9.0_WK_<CODE>~<n> is admitted to exactly the paths that a NON-TERMINAL task order under <CODE>, issued_to that serial, names in its <paths> block AT HEAD -- and to nothing else', resolved 'from the order itself, never from a lane'.",
    "world_is": "In practice the grant only resolves for a path that ALSO already carries an entry in `.owned-paths.yaml`'s `paths_config` (any lane, any permitted_agents) -- a task-ordered path with zero prior YAML footprint (the common case for a worker's first cell standing up a brand-new top-level directory or submodule) is refused before the grant clause runs at all, regardless of what the order's <paths> block says.",
    "notes": "Disarm = have `_cmd_check_agent`'s UNDEFINED branch (and/or `check_agent`'s early `return False`) fall through to `_owns_task_order_paths(agent, path, grant, root, cache)` before concluding UNDEFINED, so an unmapped path can still be granted by a worker's own task order. Worked around THIS COMMIT via the documented audited escape hatch (`GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_MCPORTAL~1`, CLAUDE.md 14a) rather than by editing `.tools/owned-paths-validate.py` or `.owned-paths.yaml`, neither of which are in this task order's `<paths>` grant. Not scoped to mcportal: any worker's first commit of a genuinely new top-level path hits this same gap."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W2-S1",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~2",
    "surfaced_at": "2026-09-24T22:00Z",
    "one_line": "GET /api/admin/changes as the TO names it (no tid/oid) has no unscoped read path in the existing store; implemented tid/oid-scoped instead.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "NFRA_MCPORTAL.TO-MP-t-4.grant-handlers.md s.1: 'GET /api/admin/changes: the writer's audit records, newest first, each with before and after' -- no tid/oid named on this route, unlike the two grant routes above it.",
        "infra/aws/ec2/opal-gateway/app/access_state.py@a2b89be579: operator_audit records are stored at POLICY#<tid>#<oid> (policy_key), and AccessState.query(pk, sk_prefix) reads ONE partition -- there is no cross-tenant scan or index this module's existing read path exposes.",
        "app/admin_grants.py@17b7e01c0f: get_changes() requires tid and oid as query parameters and 400s without them, citing this gap in its own error message."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "GET /api/admin/changes lists the writer's audit records, newest first, each with before and after -- stated with no tid/oid, unlike the narrow/widen/grant routes' explicit {tid}/{oid} path segments.",
    "world_is": "The only read this box can make against the existing store (access_state.query) takes one partition key; operator_audit records are partitioned per principal (POLICY#<tid>#<oid>). No global/cross-tenant audit feed exists without a new index, which is outside this cell's <paths> (app/access_state.py is read-only here). Implemented as a tid/oid-scoped GET with required query parameters; AC1's test_changes_newest_first exercises this scoped shape.",
    "notes": "No repair attempted per BOUNDS #2 (never widen a criterion or meet it by a route the face does not name); the mechanical criterion (AC1) is unaffected since it grades this cell's own test file, which exercises the scoped design. A true global feed is a build decision for whichever cell owns access_state.py's read surface."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W1-S2",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~1",
    "surfaced_at": "2026-09-25T00:40Z",
    "one_line": "MP-t-5 names `src/pages/recent-changes/` with no sidebar slot, and `src/shell/pages.ts` (the ONE place the sidebar order lives, verbatim from Andrew's brief word) enumerates exactly the brief's eight entries with no 'Recent Changes' member, so the router hookup the issuer owes cannot land it as a nav item without amending PAGES -- a change outside this cell's face.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Task face section 1 item 2 says entitlements is built 'under the sidebar's MCP Server entry'; item 3, for recent-changes, names only the page directory and its content, with no sidebar placement.",
        "mcportal/src/shell/pages.ts:1-20 (read-only surface per this order's Bounds) -- the file's own header comment: 'This is the ONE place that order lives; the sidebar and its test both read it from here,' and its `PAGES` array holds exactly the brief's eight ids (home, operations-report, user-management, user-analytics, mcp-server, health-check, cost-management, infosec); no `recent-changes` id exists.",
        "mcportal/src/pages/recent-changes/index.ts (this commit, 1eb686a) exports `RecentChanges` with no route wired -- reachable only once the issuer's hookup adds a `<Route>` for it, and pages.ts is not in this order's write surface (`<paths>` names only `src/api/admin.ts`, `.../entitlements/` and `.../recent-changes/`)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The two pages this cell builds both reach the shell through the same mechanism -- a router hookup the issuer adds -- and the brief's sidebar order (pages.ts) is the one place that order lives.",
    "world_is": "Only the entitlements page has a named sidebar home (MCP Server); recent-changes has none in the brief's eight-item order, so the issuer's hookup must choose one of: add a ninth PAGES entry (widening the brief's enumerated order), nest it as a sub-route reachable only from within MCP Server/entitlements, or leave it route-only with no sidebar link -- none of which this worker's face names or this worker's `<paths>` (pages.ts excluded) permits deciding.",
    "notes": "Not a defect in this cell's own build (RecentChanges renders and tests pass standalone); flagged so the issuer's hookup commit states which of the three it picked rather than silently defaulting to one."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S2",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T02:48Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_MCPORTAL-Z-W3-S3 (owner this seat): no apply ran, so the grant writer whose parents[5] cannot resolve inside its own zip is not deployed; the packaging defect goes to the CTO as a recut decision. Also CORRECTS W3-S2's premise: Andrew's Entra oid is on record, and that row's disarm stays Andrew's.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "wk-NFRA_MCPORTAL-3 instance c2619fa81c, AC1: 'entry files at HEAD=0; sentinel at HEAD=no' -- no NEVER-2 entry was opened and safe-apply never ran.",
        "Read by this seat: infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py:42 '_REPO_ROOT = Path(__file__).resolve().parents[5]' and :47-48 import app.access_state and ops.schwab_entitlement_admin from the gateway tree; infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf:25-28 archive_file zips ONLY that function's source_dir, :85 handler lambda_function.lambda_handler. At /var/task/lambda_function.py, parents[5] raises IndexError, and the gateway modules are not in the zip.",
        "Live read by this seat, dynamodb scan of gateway-access-state-table (118 items, Count 118, no LastEvaluatedKey): 6 of 6 rows carrying email andrew@opalinvest.com (sk oauth_refresh_family, written by the gateway from a verified Entra sign-in) carry one oid, 2e21f8e5-55ca-45c1-91b9-a4607bf28d4f, and one tid, 6810043e-d171-4adc-9975-068b35e179da."
      ]
    },
    "spec_asserts": "W3-S2: no existing record names Andrew's Entra object id. W3-S3: ARMED, with this seat as disarm_owner.",
    "world_is": "The oid is on record in the gateway's own access-state store, as the verified-token claim, consistent across 6 refresh families. MP-t-3 still cannot pass: its AC3 live invoke needs a writer package that carries the gateway modules and resolves them without parents[5]. That is a change to MP-t-2's built product, outside every open face.",
    "notes": "Andrew confirms the oid (W3-S2 is his). The packaging fix, a staged build that carries app/ and ops/ plus a root resolved from the package, is a product change to a closed cell, and it is asked of 1.0.0_SA_CTO~O as a recut decision. MP-t-3 and MP-t-6 stay open."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W3-S2",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~3",
    "surfaced_at": "2026-09-25T02:03Z",
    "one_line": "No existing record anywhere in the repo or the checked live AWS stores names Andrew's Entra object id (`G-OWNER-OID`) -- MP-t-3 cannot supply `var.mcportal_owner_oid` and STOPS before the ledger/apply per the task order's own step 1.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "Andrew",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The decomposition itself already flags this as unresolved: `org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md:91` '(b) Andrew's Entra oid source is NOT-EVALUATED (MP-t-3).' and `:186` 'G-OWNER-OID (only if MP-t-3 cannot find it): Andrew's Entra object id for the writer's owner config. Holder: Andrew.'",
        "Repo-wide identity for Andrew is carried ONLY by email, never by oid: `infra/aws/ec2/opal-gateway/app/config.py:253` `MASTER_ADMIN_EMAILS` defaults to `andrew@opalinvest.com`; no analogous `MASTER_ADMIN_OID`/`ANDREW_OID` constant exists anywhere (comp-find -i 'andrew' across `infra/aws/ec2/opal-gateway`, `org/missions/D6/NFRA/NFRA_MCPORTAL`, `users/configs/opal-capital.json` -- 86 hits across 37 files, none an Entra object id for him).",
        "The gateway's own POLICY# access-state partition (the example the task order names, 'a principal record the gateway's audit or policy store already holds') carries no live record at all in this tree: comp-find 'POLICY#' under `infra/aws/ec2/opal-gateway` returns only the schema definition (`app/access_state.py:55` `POLICY_PREFIX`) and synthetic test fixtures (`tests/test_access_state.py`, `tests/test_entitlement_admin.py` -- literal placeholders like `tid-a#oid-b`, `_TID`/`_OID`), never a committed real oid.",
        "Live AWS check (read-only, no gateway authentication triggered): `.tools/aws ssm describe-parameters` and `.tools/aws secretsmanager list-secrets`, names filtered for andrew|oid|mcportal|owner -- SSM: 0 hits; Secrets Manager: 2 hits (`opal/openai/andrew-fideles`, `google/andrew-goldengate/credentials`), neither an Entra object id.",
        "Per the task order text verbatim: 'If no existing record names it, STOP: file a BLOCKING row (G-OWNER-OID, owner Andrew) and do not apply. Never guess or derive it from an email.' -- this row is that stop; the ledger was never opened and no apply was attempted."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "MP-t-3 step 1: 'Find it in an EXISTING record, never by asking the gateway to authenticate anyone... If no existing record names it, STOP: file a BLOCKING row (G-OWNER-OID, owner Andrew) and do not apply.'",
    "world_is": "No existing record (repo-committed or live-AWS, read-only) names Andrew's Entra object id anywhere this worker can reach; the decomposition had already scoped this as NOT-EVALUATED and pre-named the gate. Ledger open, safe-apply, and AC1/AC2/AC3 are all downstream of `var.mcportal_owner_oid` and are not attempted.",
    "notes": "AC1/AC2/AC3 were still run literally per the worker rule (unapplied state): AC1 'entry files at HEAD=0; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR: 8 of 8 sentinel(s) scanned' FAIL exit=1; AC2 'function ... state=... gateway invoke=Invalid length for parameter ResourceArns[0] ...' FAIL exit=1 (function does not exist); AC3 'no header -> NONE NONE; forged header -> NONE NONE' FAIL exit=1 (function does not exist). All three recorded verbatim in this worker's proof-of-spec instance as FAIL, not repaired. Disarm = Andrew supplies the oid (e.g. via an Entra/Graph lookup he runs, or a committed operator artifact he authors naming it) for a future MP-t-3 re-attempt."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W3-S3",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~3",
    "surfaced_at": "2026-09-25T02:03Z",
    "one_line": "Even once G-OWNER-OID clears, `lambda_function.py`'s own `_REPO_ROOT = Path(__file__).resolve().parents[5]` (line 42) cannot resolve at runtime: the frozen `.tf`'s `handler = \"lambda_function.lambda_handler\"` (mcportal_grant_writer.tf:85) requires the file to sit at the deployed package's ROOT (only 3 `.parents` levels exist there), so the module-level import crashes before any refusal branch runs -- AC3's live invoke cannot pass regardless of how the app/ops trees or PyJWT/cryptography are packaged.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "`infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py:42-45` (HEAD 0c303246e4, this worktree): `_REPO_ROOT = Path(__file__).resolve().parents[5]` then `_GATEWAY_ROOT = _REPO_ROOT / \"infra\" / \"aws\" / \"ec2\" / \"opal-gateway\"`, run unconditionally at module import time, before `from app import access_state as acs` / `from ops import schwab_entitlement_admin as admin` and before any handler code.",
        "`infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf:27` `source_dir = \"${path.module}/../../lambda/mcportal/mcportal-grant-writer-lambda\"` (the function's OWN directory, flattened -- `archive_file` zips its contents relative to that root) and `:85` `handler = \"lambda_function.lambda_handler\"`. AWS Lambda's Python handler resolution requires the named module importable from `sys.path` (only `/var/task` by default), which for a bare `lambda_function.lambda_handler` string means `lambda_function.py` must sit at the zip's root (`/var/task/lambda_function.py`) -- a dotted path through `infra.aws.lambda.mcportal.mcportal-grant-writer-lambda...` is impossible in any case because `mcportal-grant-writer-lambda` contains a hyphen, not a valid Python identifier.",
        "Empirically verified: `python3 -c \"from pathlib import PurePosixPath; p=PurePosixPath('/var/task/lambda_function.py'); print(list(p.parents)); p.parents[5]\"` -> parents = [`/var/task`, `/var`, `/`] (3 entries, indices 0-2); `p.parents[5]` raises `IndexError: 5`. This is a deterministic property of the path depth, independent of AWS account state, so no packaging arrangement inside `infra/aws/lambda/mcportal/` (this worker's only writable surface for the artifact) can supply a 6th parent for a file whose deployed path is fixed at `/var/task/lambda_function.py`.",
        "The comment at `lambda_function.py:33` ('This file lives 5 parents below the repo root ... the same depth ops/schwab_entitlement_admin.py computes for itself') and the source-map note at `infra/aws/lambda/ci/lambda-source-map.json` (`mcportal-grant-writer-lambda._note`, 'the deploy package must also carry infra/aws/ec2/opal-gateway's app/ and ops/ trees ... MP-t-3's packaging concern') both assume packaging alone resolves this; it does not, because the FILE THAT EXECUTES (root of the zip, per the frozen handler) is not the file 5 levels deep the comment describes."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "MP-t-3 step 3: 'Packaging the function's code follows the map's tf_resource / build convention ... A zero-diff apply with no artifact built is a failed leg, not a pass' -- implying a correctly packaged artifact lets the function run for real (PRD C4, AC3's live refusal arms).",
    "world_is": "No packaging choice within this worker's granted paths (`infra/aws/lambda/mcportal/`, `infra/aws/lambda/ci/lambda-source-map.json`, no `.tf`/source logic changes permitted) can make the module import succeed once deployed, because `lambda_function.py`'s own repo-root computation is incompatible with the depth AWS Lambda's handler resolution forces on it. AC3 would FAIL on a live invoke (Runtime.ImportModuleError) even after G-OWNER-OID clears and a full apply lands.",
    "notes": "Not fixed here: fixing requires a logic change to `lambda_function.py` (e.g. reading the gateway root from an env var/layer path instead of `parents[5]`, or a different handler/source_dir shape) or to the `.tf`'s `handler`/`source_dir`, both explicitly out of bounds for this cell ('Change no logic in them; a needed logic change is a BLOCKING row'). Surfaced now, before a wasted apply, so a re-issued packaging cell can carry the fix alongside G-OWNER-OID's resolution."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S3",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T03:30Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "Relays the CTO's ruling R-1 onto NFRA_MCPORTAL-Z-W3-S2 (disarm_owner Andrew): the measured owner oid 2e21f8e5-55ca-45c1-91b9-a4607bf28d4f is ACCEPTED as the writer's owner configuration because the setting fails closed. MP-t-3 and MP-t-6 are superseded as cut (571afcb7b4), so no apply waits on the oid this round.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/1.0.0_SA_CTO~O/ROUND1_RULINGS.md R-1 @aed83d11fe: 'the measured oid ... is ACCEPTED as the writer's owner configuration. Andrew's separate confirmation is not needed, because the setting fails CLOSED'.",
        "Row NFRA_MCPORTAL-Z-S2: the oid is one value across 6 of 6 of Andrew's refresh-family rows in gateway-access-state-table (118 of 118 items scanned)."
      ]
    },
    "spec_asserts": "NFRA_MCPORTAL-Z-W3-S2: no existing record names Andrew's Entra object id, so MP-t-3 cannot configure the writer's owner.",
    "world_is": "The oid is on record, and the PRD owner has accepted it as the configuration. Round 2's re-cut of MP-t-3 carries it.",
    "notes": "This is a relay of R-1. It adds no rule and does not speak for Andrew."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S4",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~O",
    "surfaced_at": "2026-09-25T05:09Z",
    "one_line": "DISARMS NFRA_MCPORTAL-Z-W1-S1 (disarm owner 1.0.0_SA_CTO; this lane holds it, ruling R-6 @667f442b8a): owned-paths-validate now consults the worker's task-order grant on an UNMAPPED path in both check_agent and the --check-agent loop, so a worker's order-granted brand-new top-level path is admitted without the author override. Fixed @6bc980ad5d.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/owned-paths-validate.py @6bc980ad5d: check_agent's unresolved-lane branch returns _owns_task_order_paths(...); the CLI loop calls it before appending UNDEFINED.",
        "python .tools/owned-paths-validate.py --self-test .owned-paths.yaml: 16 arms, 0 failed; new arms 'UNMAPPED path ... -> admitted' and 'UNMAPPED path MUTANT ... -> both refused'.",
        "Negative control: the same admit arm run against `git show HEAD:.tools/owned-paths-validate.py` (pre-fix) returns False."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NFRA_MCPORTAL-Z-W1-S1 is ARMED with 1.0.0_SA_CTO as disarm_owner.",
    "world_is": "The gap is closed at the tool: an unmapped path is admitted ONLY for a worker whose own non-terminal order names it; every other committer on an unmapped path is still refused UNDEFINED. The same fix serves NFRA_OPALAI-Z-W1-S1.",
    "notes": "No lane rule was added and no gate was widened beyond the registry's own worker_grant stanza (ADHC_OWNPTH.005)."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S5",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T15:20Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_MCPORTAL-Z-W2-S3 (owner this seat): tests/test_owner_gate.py appends one line per run to the TRACKED infra/aws/ec2/opal-gateway/audit.jsonl, because the audit path defaults to ./audit.jsonl (app/config.py:307). Contained: MP-g-1's worker restored the file and committed none of it; this seat restored the same side effect in /c/tmp/mx-1 after a dry run. The fixture fix goes to the round-2 drain-end read as an enrichment.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Worker report 0.9.0_WK_NFRA_MCPORTAL~2 (resume): 'The existing tests/test_owner_gate.py does: it adds one line per run, because the audit path defaults to ./audit.jsonl (app/config.py:307)'; audit.jsonl restored to HEAD, not committed.",
        "This seat's MX-c-5 dry run in /c/tmp/mx-1 appended to the same file (git status ' M infra/aws/ec2/opal-gateway/audit.jsonl'); restored with git restore before any commit."
      ]
    },
    "spec_asserts": "NFRA_MCPORTAL-Z-W2-S3 is ARMED with this seat as disarm_owner.",
    "world_is": "No commit carries a test-run audit line. The hazard stands for any seat that commits the whole gateway tree after running its suite.",
    "notes": "Enrichment: a conftest fixture pointing the audit path at a tmp file. It is the gateway suite's owner's to cut. No gate is built here."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W2-S2",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~2",
    "surfaced_at": "2026-09-25T00:00Z",
    "one_line": "Building MP-g-1's literal whoami schema {email, claim_keys, oid, sub} unconditionally BROKE test_owner_gate.py::test_owner_page_served's exact-equality {\"email\":...} assertion; resolved by adding the three fields ONLY when the request's x-amzn-oidc-data header decodes to a non-empty claims dict (always true on a real ALB-OIDC request; false only for that test's header-less identity stub).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "NFRA_MCPORTAL.TO-MP-g-1.claims-capture-and-history.md s.1: 'GET /api/admin/whoami returns, to the owner only, {\"email\", \"claim_keys\", \"oid\", \"sub\"}' -- no conditional named.",
        "First build (unconditional): `python -m pytest tests/test_owner_gate.py tests/test_admin_grants.py -v` -> `test_owner_page_served FAILED: assert {'email': 'andrew@opalinvest.com', 'claim_keys': [], 'oid': 'ABSENT', 'sub': 'ABSENT'} == {'email': 'andrew@opalinvest.com'}` (this worktree, pre-fix commit not landed).",
        "tests/test_owner_gate.py::test_owner_page_served's `as_identity(ANDREW)` stubs `owner_gate._alb_oidc_identity` directly and sends `client.get(\\\"/\\\")`/`client.get(\\\"/api/admin/whoami\\\")` with NO `x-amzn-oidc-data` header at all -- `owner_gate.owner_claims(request)` on that request returns `{}` (empty header).",
        "After making the three fields conditional on `if claims:` in app/admin_api.py's whoami: `python -m pytest tests/test_owner_gate.py tests/test_admin_grants.py tests/test_admin_round2.py -v` -> 14 passed, 0 failed (this worker's own 4 named tests, which DO send a crafted header, still assert claim_keys/oid/sub present)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "BOUNDS #1: 'the existing tests/test_owner_gate.py and tests/test_admin_grants.py stay green' -- alongside section 1 item 1's whoami schema naming exactly {email, claim_keys, oid, sub} with no conditional.",
    "world_is": "The two are structurally incompatible for a header-less verified-owner request: any non-empty addition to whoami's response dict fails test_owner_gate.py's `== {\\\"email\\\": ANDREW}` exact equality, regardless of the added fields' values. No route in this cell's <paths> can edit the read-only test file. Resolved by gating the three added fields on the header actually carrying claims -- a real alb_oidc request always does, so this is additive in production and narrows nothing this order's own test file (test_admin_round2.py) exercises.",
    "notes": "Not a repair of AC1/AC2 (both still measured verbatim against this worker's own test_admin_round2.py, which supplies a real crafted header and asserts the four-key shape); this only decides the header-ABSENT edge case the task-order text did not address. INERT: both suites are green at this worker's commit."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W2-S3",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~2",
    "surfaced_at": "2026-09-25T07:10Z",
    "one_line": "Running BOUNDS #1's regression suite tests/test_owner_gate.py appends one line per run to the TRACKED file infra/aws/ec2/opal-gateway/audit.jsonl (outside this order's <paths>); the two proof invocations g1.AC1.sh/g1.AC2.sh do not write it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/app/config.py@d0ba96d27c:307: AUDIT_PATH defaults to os.environ.get(\"AUDIT_PATH\", \"./audit.jsonl\") -- the gateway dir's tracked file when pytest runs from there; the line is unchanged by build d0ba96d27c (git diff af11e91097 d0ba96d27c touches no audit writer).",
        "This worktree, restored to HEAD bytes first each time: `python -m pytest -q tests/test_owner_gate.py` rc=0 -> git diff --numstat audit.jsonl added=1; `python -m pytest -q tests/test_admin_grants.py` rc=0 -> added=0; g1.AC1.sh and g1.AC2.sh -> file clean.",
        "The earlier run of this slot left 3 such lines (user someone.else@opalinvest.com, tool sprint_view, 2026-09-25T06:42-06:51Z); restored to HEAD, never committed."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "BOUNDS #1: 'the existing tests/test_owner_gate.py ... stay green' (they must be run) and BOUNDS #2: 'The gateway writes nothing.'",
    "world_is": "Each run of test_owner_gate.py writes a real audit line into a tracked repo file, so every worktree that runs the regression suite is left with a dirty tracked file that a wide commit or drain could carry. The test file and config are read-only to this order; the file was restored to HEAD and not committed.",
    "notes": "ARMED because it recurs on every future regression run in any worktree; disarm (e.g. AUDIT_PATH to tmp in the test fixture) is outside this worker's paths."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S6",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T16:30Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_MCPORTAL-Z-W1-S3 and -Z-W1-S4 (owner this seat). The face and checks were amended at 051240c792 (CLOUD) / b7281eb222 (branch): the package mirrors the repo layout so ops' parents[5] lands on the package root, and the checks extract the zip at Lambda's /var/task depth and import through a script file. The rebuild passes 3 of 3 (db3bae76ba).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The amended b1.AC1 dry-run on the earlier gateway-relative build f6ce4d1ca3 read 'IMPORT-FAILED IndexError: 5': the Lambda failure made visible.",
        "Rebuild db3bae76ba: AC1 'extracted at Lambda depth; lambda_handler callable=yes; app and ops resolved inside the package 2 of 2'; AC2 'verdict=REFUSED NO-OWNER-HEADER'; AC3 '8 of 8 byte-equal to their repo path'. Worker control: with the sys.path guard disabled, AC1 fails 'No module named app'."
      ]
    },
    "spec_asserts": "Z-W1-S3 (ops parents[5] at /var/task) and Z-W1-S4 (the stdin probe trips dotenv) are ARMED with this seat as disarm_owner.",
    "world_is": "The package imports and refuses at Lambda depth. ops/ is unedited. Nothing is applied until MP-a-1.",
    "notes": "Checker lesson for the round: a proof that imports from a deep temp path cannot see a parents[N] defect. Reproduce the runtime's depth."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W1-S3",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~1",
    "surfaced_at": "2026-09-25T15:00Z",
    "one_line": "The staged grant-writer zip still cannot import at /var/task: ops/schwab_entitlement_admin.py:49 (read-only for MP-b-1) computes Path(__file__).resolve().parents[5] at IMPORT time, and /var/task/ops/schwab_entitlement_admin.py has only 4 parents, so the import raises IndexError. The MP-b-1 checks run the zip from a deep temp path where parents[5] exists, so they PASS and cannot see it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py@af11e91097 (last touched 7a5554face) :49 `_REPO_ROOT = Path(__file__).resolve().parents[5]` and :50 `_CONTRACT_PATH = _REPO_ROOT / \"org\" / \"standards\" / \"NFRA_OPLGTW_CONTRACT.json\"`, both module-level, so they run on `from ops import schwab_entitlement_admin`.",
        "python -c \"from pathlib import PurePosixPath as P; P('/var/task/ops/schwab_entitlement_admin.py').parents[5]\" -> IndexError 5 (measured 2026-09-25 on this worktree's interpreter).",
        "build_package.py --out .scratch/mcpw.zip (this cell) -> members app/__init__.py, app/access_state.py, app/config.py, app/context.py, app/data_entitlement.py, lambda_function.py, ops/__init__.py, ops/schwab_entitlement_admin.py, org/standards/NFRA_OPLGTW_CONTRACT.json; ops/schwab_entitlement_admin.py is byte-equal to the gateway source, as the face requires, so the build cannot rewrite line 49.",
        "b1.AC1.sh / b1.AC2.sh put the zip at ${TMPDIR:-/tmp}/mp_b1_acN_$$/mcpw.zip; on this host that path has more than 5 ancestors, so parents[5] resolves there and the in-zip import succeeds."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "MP-b-1 section 1: the grant writer 'cannot run as packaged' because lambda_function.py climbs parents[5]; staging the import closure beside it, with lambda_function.py climbing nothing, makes it run from its own zip.",
    "world_is": "Removing the climb from lambda_function.py moves the same IndexError one module down: the gateway's ops/schwab_entitlement_admin.py climbs parents[5] at import. Separately, even once the import succeeds, admin.load_contract() (called by lambda_function.handle on the narrow path) opens parents[5]/org/standards/NFRA_OPLGTW_CONTRACT.json, which is not where the zip carries it (org/standards/... at the zip root, i.e. /var/task/org/standards/...). The fix is in infra/aws/ec2/opal-gateway/ops/ (a lazy or guarded path, or a contract path the caller passes), which is outside this order's <paths>.",
    "notes": "Not repaired here (face section 2 item 3; ops/ is read-only for this cell). AC1-AC3 are recorded as their scripts print them; this row states what they cannot see."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W1-S4",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~1",
    "surfaced_at": "2026-09-25T15:20Z",
    "one_line": "b1.AC1.sh and b1.AC2.sh cannot PASS on this host's interpreter: the in-zip import reaches app/config.py, which calls python-dotenv's load_dotenv() at import when dotenv is installed (it is: python-dotenv 1.2.2), and under `python -` with the modules inside a zip, find_dotenv() walks every frame (no frame's file exists on disk) and raises AssertionError, which config.py's `except ImportError` does not catch.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "b1.AC1.sh at 0da92f4675: `IMPORT-FAILED AssertionError:` / `build rc=0 built zip=yes; lambda_handler callable=no; app and ops resolved inside the zip 0 of 2` / RESULT: FAIL exit=1. b1.AC2.sh: `RUN-FAILED AssertionError:` / verdict=NONE / RESULT: FAIL exit=1.",
        "Traceback reproduced with the check's own shape (python - <zip>, cwd the temp dir): lambda_function.py:43 -> ops/schwab_entitlement_admin.py:46 `from app import context` -> app/context.py:18 `from .config import get_config` -> app/config.py:9 `load_dotenv()` -> dotenv/main.py:367 `assert frame.f_back is not None` -> AssertionError.",
        "Control: the SAME zip imported by `python .scratch/tb.py <zip>` (a __main__ whose file exists) prints `OK import`, so find_dotenv stops at the script frame; the tests (gateway tree on sys.path, real files) pass 4 of 4.",
        "infra/aws/ec2/opal-gateway/app/config.py@af11e91097 :7-11 `try: from dotenv import load_dotenv; load_dotenv() except ImportError: pass` -- only ImportError is caught."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "MP-b-1 section 2 item 1: the local interpreter supplies PyJWT for the import, and AC1/AC2 need nothing else from it.",
    "world_is": "The local interpreter also supplies python-dotenv, which app/config.py loads at import; with the check's stdin __main__ and zip-internal module paths, dotenv raises AssertionError, so the verdict of AC1 and AC2 is decided by the interpreter, not by the package. At /var/task dotenv is not in the layer (ImportError, caught) and the extracted files exist, so this path does not fire there. Meeting the check from this cell would need a dotenv block in lambda_function.py or an edit to app/config.py, neither of which the face names; refused.",
    "notes": "AC1 and AC2 are recorded FAIL with this measurement; the order stays open."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W1-S5",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~1",
    "surfaced_at": "2026-09-25T16:54Z",
    "one_line": "MP-b-2 retires the grant writer's MCPORTAL_OWNER_OID env var for MCPORTAL_OWNER_KEY_CLAIM + MCPORTAL_OWNER_KEY (and adds MCPORTAL_CHANGES_TABLE), but infra/aws/lambda/ci/lambda-source-map.json:5064, outside this order's <paths>, still describes the function as exact-matching the oid from MCPORTAL_OWNER_OID. The source map's prose is now stale; nothing reads the var at runtime.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-find 'mcportal_owner_oid|MCPORTAL_OWNER_OID' --corpus default on wk-NFRA_MCPORTAL-1 @fd2db15313 plus this cell's uncommitted edit: 12 hits across 42763 files (DEF=1 CONFIG=4 TEST=1 DOC=6). The only non-record hits outside this order's <paths> are infra/aws/lambda/ci/lambda-source-map.json:5064 (the `_note`, prose) and deliverables/2.0.0_SA_COO~O/round2/checks/b1.AC2.sh:23, which also sets MCPORTAL_OWNER_OID. That extra env var is now unused and harmless; the same line sets MCPORTAL_OWNER_KEY_CLAIM/MCPORTAL_OWNER_KEY, and b1.AC2 PASSes after this change.",
        "infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py (this cell): reads MCPORTAL_OWNER_KEY_CLAIM, MCPORTAL_OWNER_KEY and MCPORTAL_CHANGES_TABLE, and no longer reads MCPORTAL_OWNER_OID. infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf (this cell): var.mcportal_owner_oid is replaced by var.mcportal_owner_key_claim + var.mcportal_owner_key."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "MP-b-2 section 1 item 4: env MCPORTAL_OWNER_KEY_CLAIM / MCPORTAL_OWNER_KEY replace MCPORTAL_OWNER_OID. Section 3 <paths> names lambda_function.py, the two tests, mcportal_grant_writer.tf and the record folders, and does not name lambda-source-map.json.",
    "world_is": "The replacement landed in the code and the Terraform. The source map's `_note` for mcportal-grant-writer-lambda still names MCPORTAL_OWNER_OID and oid-only matching, and it is not writable from this order. The MP-a-1 apply also has to supply the two new variables in place of var.mcportal_owner_oid: any tfvars or apply invocation still passing mcportal_owner_oid now names an undeclared variable.",
    "notes": "Not repaired here (face section 2 item 3). This is a prose record, so it has no runtime effect."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S7",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T17:55Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_MCPORTAL-Z-W2-S7 (owner this seat). The first MP-d-1 release took the gateway DOWN ~17:14-17:31:22Z: the deploy script's .env printf lost the space between its closing quote and \"${REGION}\", so every value shifted onto the wrong key. The worker rolled back. This seat verified live: /health 200, active since 17:31:22Z, server.py md5 = f1f0fc6780's. The face is amended: a fresh release branch carrying the fixed script, a local .env render gate before the act, and a 90-second /health rollback trigger. The branch rel-nfra-mcportal-r2-gateway @c97839d7c8 is NEVER deployed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Character diff of the printf line, base f1f0fc6780 -> broken ece3aab4b5: '...globgrph\\n' \"${REGION}\"' became '...changes-table\\n'\"${REGION}\"' (no space). Base -> fixed 83cbd1a605: only the three new KEY=VALUE lines inserted, with the space kept. Placeholders 9 = args 9 in all three.",
        "Live read by this seat over SSM at ~17:48Z: health=200; active since Fri 2026-09-25 17:31:22 UTC; /opt/opal-gateway/app/server.py md5 42c7fd424ac4 = git show f1f0fc6780:.../app/server.py md5 42c7fd424ac4; the .env key list is the pre-release set.",
        "Ledger: org/critical_paths/change_management/20260925T1636Z_nfra-mcportal-r2-gateway-release_deploy_completion.md, closed as rolled back by the worker (on wk-NFRA_MCPORTAL-2)."
      ]
    },
    "spec_asserts": "NFRA_MCPORTAL-Z-W2-S7 is ARMED: deploying rel-nfra-mcportal-r2-gateway takes the gateway down again.",
    "world_is": "The gateway serves f1f0fc6780, healthy. The defective release branch stays undeployed, and the retry builds a fresh branch behind a render gate and a fast rollback trigger.",
    "notes": "Checker lesson: no criterion or pre-act step rendered the .env the deploy writes. The render gate (face 4a(i)) is the missing pre-act check. The outage is recorded for the CTO's round-2 analysis."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W2-S4",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~2",
    "surfaced_at": "2026-09-25T16:30Z",
    "one_line": "MP-g-1's gateway commit d0ba96d27c also carries a surprise-channel row, so `git cherry-pick --no-commit d0ba96d27c` onto the f1f0fc6780 release base stops on a modify/delete conflict the task order does not name; the channel file was dropped from the release branch (git rm) and never committed to CLOUD.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show --stat d0ba96d27c: 5 files, 4 under infra/aws/ec2/opal-gateway plus org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md (+23).",
        "/c/tmp/mp-2-rel, git cherry-pick --no-commit d0ba96d27c: 'CONFLICT (modify/delete): .../INVESTIGATION_v1.Z.md deleted in HEAD and modified in d0ba96d27c'; resolved by git rm; release commit c97839d7c8 on rel-nfra-mcportal-r2-gateway changes 9 paths, all under infra/aws/ec2/opal-gateway (git diff --name-only f1f0fc6780 c97839d7c8 | wc -l = 9).",
        "Same resolution as the NFRA_OPALAI precedent f1f0fc6780's own commit message (its channel file dropped from rel-nfra-opalai-r1-gateway).",
        "Also on the release tree: the pre-act run of tests/test_owner_gate.py appended one line to the tracked infra/aws/ec2/opal-gateway/audit.jsonl (row W2-S3's class), which would have tripped safe-ec2-deploy.sh Step 1's uncommitted-changes prompt under SOURCE_PATH; restored to HEAD bytes (git cat-file blob) before the act."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MP-d-1 section 1 item 2: 'git -C /c/tmp/mp-2-rel cherry-pick --no-commit the commits above, in order, and commit on that branch under your serial' -- no conflict resolution is named.",
    "world_is": "The third commit's cherry-pick conflicts on a non-gateway file absent at the release base. The gateway census is unaffected (9 files, 0 outside the four commits' set); the release branch carries no channel file.",
    "notes": "INERT: the release commit and the deployed artifact contain only gateway paths; the row itself lives on CLOUD's channel through d0ba96d27c's merge b860f8194e."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W2-S5",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~2",
    "surfaced_at": "2026-09-25T16:50Z",
    "one_line": "The face's literal act command (`cd /c/tmp/mp-2-rel && bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`) exits 1 at the HALT-GATE before Step 2 on 186 ROUTINE pending messages (0 STOP-class) in the issuer's inboxes; it passes only with HALT_ACK=1, which the face does not name. Re-run with HALT_ACK=1 after reviewing the list.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Attempt 1 (16:41:29Z, AGENT_NAME=0.9.0_WK_NFRA_MCPORTAL~2): 'HALT-GATE: 186 pending message(s) -- review before proceeding (safe-ec2-deploy:opal-gateway)' ... 'HALT-GATE: blocked. Review the message(s) above, then re-run with HALT_ACK=1.' exit=1; no Step 2 line, nothing built or uploaded.",
        "Sender tally of the 186: 141 deploy_ledger.py gate-bypass scan RED, 16 deploy_ledger.py on behalf of 0.7.0_AE_CloudOps, 11 4.0.0_SA_CRO~W, 15 further deploy_ledger.py HELD-STALE/on-behalf nudges, 1 2.0.0_SA_COO~Z; '[STOP]'/'[HALT]' token count 0; none names opal-gateway or this release.",
        ".tools/halt-gate-check.sh:13: routine pending -> 'Re-invoke with HALT_ACK=1 to pass (exit 0)'; :14 STOP-class -> hard-block exit 2 (not this case)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MP-d-1 section 1 item 5: 'ACT from the RELEASE worktree with ITS copy of the scripts: cd /c/tmp/mp-2-rel && bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh'.",
    "world_is": "As written the command cannot pass the halt gate while the issuer's base inbox holds unread routine mail; the gate's own documented routine acknowledgement (HALT_ACK=1) was added to the same command.",
    "notes": "INERT for this act (no STOP was bypassed; HALT_OVERRIDE was not used). Recurs for any worker deploy under this issuer while the base COO inbox holds the 141 unread gate-bypass REDs."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W2-S6",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~2",
    "surfaced_at": "2026-09-25T16:35Z",
    "one_line": "EC2_MANIFEST.json services.opal-gateway.file_checksums does not describe the artifact deployed at f1f0fc6780: the record says app/server.py a101f27e..., the S3 artifact opal-gateway-f1f0fc6780.tar.gz (and a clean rebuild of f1f0fc6780) carries 42c7fd42...; same for app/tools.py, app/audit.py, app/config.py.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/EC2_MANIFEST.json@f50bd03775 services.opal-gateway.file_checksums: app/server.py a101f27ea37009d73cb19b247eef26e7, app/tools.py eccf03c379985e5441e8e06182cb635f, app/audit.py 5f8342859f23ad773b059c4030d4c402, app/config.py 20836f8aa54ee27ffb7209686fa27df7.",
        "s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-f1f0fc6780.tar.gz (ETag 4a8b6016294ddfbb53c825606c77cdcc) members: app/server.py 42c7fd424ac441719eb8c75880655596, app/tools.py 7c0d2941b678c063ea2710c495356857, app/audit.py 9b32695304929ca08f84d045b9c30437, app/config.py 881be540ca15f2cbeaa566bbee6e3ece; a clean git-archive rebuild of f1f0fc6780 matches the S3 artifact 69 of 69 members."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "EC2_MANIFEST.json's file_checksums field reads as the deployed files' md5s.",
    "world_is": "The field was not refreshed by earlier deploys; it matches neither f1f0fc6780's artifact nor this release. This order's recording names deployed_commit, mcportal_commit and release_note only, so the field was left untouched.",
    "notes": "INERT: no gate found reading file_checksums in this act; recorded so a reader does not verify the host against it."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W2-S7",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~2",
    "surfaced_at": "2026-09-25T17:20Z",
    "one_line": "The narrow release c97839d7c8 FAILED on the host and was ROLLED BACK: this worker's own deploy-to-ec2.sh commit ece3aab4b5 dropped the space between the .env printf format and its first argument, so every value shifted one key, BIND_PORT received a non-integer and opal-gateway never bound 8080 (down ~17:14Z-17:31:22Z). AC2 and AC3 cannot pass; the release branch still carries the defect.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git diff f1f0fc6780 c97839d7c8 -- infra/aws/ec2/opal-gateway/deploy-to-ec2.sh: the printf line ends `...MCPORTAL_CHANGES_TABLE=mcportal-grant-changes-table\\n'\"${REGION}\"` (no space), so bash joins the region onto the format string; f1f0fc6780 has `...globgrph\\n' \"${REGION}\"`.",
        "ssm:a6aa8d9e-6404-43c0-8be6-b0ea630bea5e Status Failed: 'OK: opal-gateway active' then 'ERROR: opal-gateway active but /health never came up in 30s'; journal 17:14:26Z app/config.py line 154 `BIND_PORT: int = int(os.environ.get(\"BIND_PORT\", \"8080\"))` -> ValueError: invalid literal for int() with base 10 (a GUID); opal-gateway.service Main process exited status=1/FAILURE.",
        "Rollback with the ledger's named command from a clean f1f0fc6780 worktree /c/tmp/mp-2-rb: ssm:469e6d98-0ef0-4d71-ac7f-843623061ab5 'OK: deploy Success', {\"ok\":true}, '/mcp unauth -> 401'. Independent read ssm:0ccf22a4-a835-4570-94b5-9ddc07d06af0: md5 app/server.py 42c7fd42, app/tools.py 7c0d2941, app/audit.py 9b326953, app/config.py 881be540 (== the f1f0fc6780 artifact, 4 of 4), ActiveEnterTimestamp 17:31:22 UTC, /health=200, .env 23 keys with no DASHBOARD_/GRANT_WRITER_/MCPORTAL_ key.",
        "Fix on wk-NFRA_MCPORTAL-2 (this worker's branch, not deployed): the space restored; the new printf line minus the three added .env lines is byte-equal to f1f0fc6780's (.scratch/cmp_printf.py: True), %s count 9 = 9."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MP-d-1 section 1 item 1(b): add the three .env lines and 'Change NOTHING else there'; AC2 expects EC2_MANIFEST.json to record a deployed_commit descending from f1f0fc6780 with NFRA_MCPORTAL's files; AC3 expects /api/admin/whoami and / at 401 or 403 on the served host.",
    "world_is": "The shipped script changed the printf argument binding as well; the release did not serve and was rolled back per BOUNDS #2, so the host serves f1f0fc6780 (whoami and / answer 404) and the manifest records the rollback redeploy of f1f0fc6780.",
    "notes": "ARMED: branch rel-nfra-mcportal-r2-gateway @c97839d7c8 (worktree /c/tmp/mp-2-rel) still carries the broken script and will take the gateway down again if deployed; a re-release must be re-cut with the corrected script (this branch's fix commit) and is not attempted here per BOUNDS #2. Cause of the defect: the edit that added the three lines lost the trailing space of its replacement text; the pre-act checks (bash -n, a grep of the added text, the gateway pytest) do not render the printf and missed it."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W2-S8",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~2",
    "surfaced_at": "2026-09-25T21:50Z",
    "one_line": "The 90-second rollback trigger cannot be met by the named rollback command: safe-ec2-deploy.sh's HALT-GATE spends about 12 minutes scanning the issuer's 186 pending messages before Step 2 reaches the host, with or without HALT_ACK=1, so a triggered rollback leaves the gateway down for 12-15 minutes, not seconds.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "This run, attempt without HALT_ACK from /c/tmp/mp-2-rel2: started 2026-09-25T20:53:38Z, 'HALT-GATE: blocked. Review the message(s) above, then re-run with HALT_ACK=1.' at 21:05:55Z (12 min 17 s in the gate alone; nothing built or uploaded).",
        "This run, attempt with HALT_ACK=1: started 21:08:52Z; 'HALT-GATE: HALT_ACK set -- messages acknowledged. Proceeding.' then Step 2; S3 upload LastModified 21:25:18Z; host ActiveEnterTimestamp 21:25:38Z (about 16 min from invocation to the host, the build and upload taking under a minute of it).",
        "The first attempt's rollback (row NFRA_MCPORTAL-Z-W2-S7) ran the same named command: started ~17:17Z, host active again 17:31:22Z.",
        "The rollback command named in the ledger entry org/critical_paths/change_management/20260925T2034Z_nfra-mcportal-r2-gateway-release_deploy_completion.md @c70844d63a is the same safe-ec2-deploy.sh invocation, so it passes through the same gate."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-MP-d-1 section 1 item 4a(ii) @894cf33916: 'Immediately after the SSM restart, poll /health on the host. If it is not 200 within 90 seconds, run the named rollback AT ONCE'.",
    "world_is": "The trigger can fire within 90 s, but the named rollback's own halt-gate scan takes about 12 minutes before it touches the host, so the outage a triggered rollback bounds is 12-15 minutes. It did not fire this run: /health was 200 within 15 s of the restart.",
    "notes": "ARMED for any later gateway release that relies on this rollback path while the issuer's inbox holds the routine backlog (row NFRA_MCPORTAL-Z-W2-S5 names the same 186 messages). Not measured: whether the scan time scales with the message count. safe-ec2-deploy.sh is read-only to this worker."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S8",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T22:40Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_MCPORTAL-Z-W2-S8 (owner this seat): the proven rollback command spends ~12 minutes in safe-ec2-deploy.sh's halt gate before it touches the host, so a fired 90-second trigger would still mean a 12-15 minute outage. The MP-d-1 release is LIVE and healthy (the trigger did not fire). Every later gateway face this seat cuts arms its rollback PRE-ACKED: the worker reads the halt gate's STOP count at arm time and, if it is 0, the rollback line carries HALT_ACK=1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Worker report 0.9.0_WK_NFRA_MCPORTAL~2 (phase B): the rollback command's halt gate measured 20:53:38Z to 21:05:55Z (186 routine messages, 0 STOP) before any host act.",
        "The release 1f7128201a is live: this seat's own read showed /health 200, active since 21:25:38Z, and server.py md5 13eedf3ffbde equal to the release's."
      ]
    },
    "spec_asserts": "NFRA_MCPORTAL-Z-W2-S8 is ARMED: the 90-second trigger's rollback is not fast.",
    "world_is": "No rollback is pending. The next gateway release faces (NFRA_OPALAI's Z-S18 fix, NFRA_MCPINDEX MX-r-3) carry the pre-acked rollback line.",
    "notes": "The halt gate is safe-ec2-deploy.sh's, read-only to every cell. Pre-acking at arm time keeps the gate's purpose (a STOP still halts) while removing the 12-minute delay from an emergency path."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S9",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-27T07:40Z",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each measured closed at CLOUD HEAD by a read-only audit, and re-cited here. Z-W1-S3: build_package.py:8-14 mirrors the repo layout, so parents[5] resolves inside the zip; MP-b-1 is complete @c09110fefc. Z-W1-S4: the checks were amended @051240c792 (Z-S6) so dotenv no longer breaks them. Z-W2-S7: deploy-to-ec2.sh:196 carries the space before REGION; the broken branch rel-nfra-mcportal-r2-gateway @c97839d7c8 stays on origin under the standing never-deploy rule. Z-W2-S8: ruled at Z-S8 -- later deploy faces pre-acknowledge the halt gate for the rollback (HALT_ACK=1), exercised in OA-g-2 and MX-r-3.",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W1-S3",
      "NFRA_MCPORTAL-Z-W1-S4",
      "NFRA_MCPORTAL-Z-W2-S7",
      "NFRA_MCPORTAL-Z-W2-S8"
    ],
    "one_line": "The issuer closes four ARMED rows whose hazard is gone or ruled at CLOUD. Z-W2-S3 stays open, carried by Z-S5's round-2 enrichment (a conftest fixture pointing AUDIT_PATH at a tmp file).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "build_package.py:8-14, deploy-to-ec2.sh:196 at CLOUD; commits c09110fefc, 051240c792; MX-r-3 ledger 20260927T0438Z (HALT_ACK=1 rollback command)"
      ]
    },
    "spec_asserts": "Each target row's hazard stands until disarmed.",
    "world_is": "The fold read them open only because no adjudicating row existed."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S10",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-09-28T20:55Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "The grant writer's own record writes the OWNER-KEY VALUE into every WRITTEN item: lambda_function.py:266 sets ctx['who'] = '<claim>:<key> <email>' and _record_item puts it in the table's `who` field (:189). On the sub branch that is Andrew's `sub` in mcportal-grant-changes-table, which the gateway's history reads and serves. The CTO's privacy condition @384fd85543 says the value goes ONLY into the function's configuration, never into a log, an audit record or a committed file.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~MP",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py:266 at CLOUD HEAD a9c8a178e3: ctx[\"who\"] = \"%s:%s%s\" % (owner.claim, owner.key, ...); :189 \"who\": s(who) in _record_item.",
        "MP-a-1's face (task-orders/NFRA_MCPORTAL.TO-MP-a-1.writer-apply.md:28-29) quotes the condition: the owner-key VALUE is written ONLY into this function's configuration, never into a log, an audit record or a committed file.",
        "No WRITTEN item exists yet: the writer is not applied (a2.AC2 dry run at the cut: ResourceNotFoundException on the table)."
      ]
    },
    "spec_asserts": "The owner-key value lives only in the writer's configuration (privacy condition @384fd85543).",
    "world_is": "The first WRITTEN outcome, which is Andrew's narrow in the MP-c-1 close run, would store '<claim>:<value> <email>' in the table, where the gateway's history serves it.",
    "notes": "Disarm (the issuer, same turn): the G-CLOSE card that starts Andrew's sitting is NOT sent until 1.0.0_SA_CTO~O rules whether `who` carries the claim NAME and email only. MP-a-2's apply and its no-header refusal write REFUSED items with who=UNVERIFIED, so they are untouched and proceed. Found off-task at the round-3 cut."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S11",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-09-28T21:05Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_MCPORTAL-Z-S10 (disarm owner this seat) against 1.0.0_SA_CTO~O's ruling (msg 26207): `who` on a WRITTEN item carries the claim NAME and the email only. The fix is cell MP-b-3, cut at the round-3 issuance at the head of chain A, so MP-a-2's apply ships it; the G-CLOSE card that starts the first WRITTEN outcome is sent only after MP-a-2 drains.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CTO message 20260928T205744Z (Msg-ID 26207): 'RULED ... The fix is a cell: lambda_function.py :189/:266 drop the value, plus a test ... Cut it ahead of MP-c-1, then release the G-CLOSE card.'",
        "task-orders/NFRA_MCPORTAL.TO-MP-b-3.who-without-owner-key.md and TO-MP-c-1's spawn conditions, in this round's issuance commit."
      ]
    },
    "spec_asserts": "NFRA_MCPORTAL-Z-S10 is ARMED: the first WRITTEN item would store the owner-key value.",
    "world_is": "No WRITTEN item can exist before MP-a-2 applies the writer, and MP-a-2 packages MP-b-3's source; the only live writes before then are REFUSED items with who=UNVERIFIED."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S12",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-09-28T21:05Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "The grant writer's own suite is RED at CLOUD HEAD: tests/test_grant_writer.py::test_owner_write_lands_with_operator_audit expects record types [data_entitlement, operator_audit, principal_profile], but admin.activate now also puts an email_deny record (NFRA_OPLGTW OG-e-1 @3e936f77bd changed access_state.operator_transact, which the writer imports). The writer's POLICY#* grant covers the new POLICY#EMAILDENY# key, so the live path is not refused; the test is stale. Remedied inside MP-b-3.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "b3.AC1 dry run at base: '1 failed, 9 passed'; pytest -vv: 'At index 1 diff: email_deny != operator_audit' at tests/test_grant_writer.py:141.",
        "access_state.py:64 POLICY_RECORD_TYPES includes email_deny; :447-469 'the principal's partition plus at most email_deny puts'; mcportal_grant_writer.tf:87-91 PutItem/UpdateItem on POLICY#* leading keys."
      ]
    },
    "spec_asserts": "The writer's tests are green at the base every cell builds on.",
    "world_is": "One writer test fails at HEAD because an upstream shared module changed under it; no gate ran the writer's suite on that commit.",
    "notes": "A shared-module change in another project's cell did not run this project's dependent suite. Recorded only; no gate is proposed here."
  }
]
```
