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
  },
  {
    "id": "NFRA_MCPORTAL-Z-S13",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-09-28T21:35Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_MCPORTAL-Z-W2-S3 (disarm owner this seat, transferred with the project): MP-f-1's session fixture (merged @5d36443784) points AUDIT_PATH at a temp file, and R-8's condition holds at CLOUD -- the audit-reaching gateway tests leave the tracked audit.jsonl byte-identical, with a planted append as the positive control.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "f1.AC1.sh re-run by the issuer on the shared CLOUD tree after the merge: 14 passed; audit.jsonl md5 before=after=2e05d36768ee9b3cad061ee0da8ca396; porcelain before=0 after=0; control seen=yes; RESULT: PASS.",
        "Worker ~4 instance NFRA_MCPORTAL.TO-MP-f-1.audit-path-fixture.proof_of_spec.json: AC1 PASS, AC2 PASS (app/config.py default untouched)."
      ]
    },
    "spec_asserts": "NFRA_MCPORTAL-Z-W2-S3 is ARMED: a gateway test run appends to the tracked audit.jsonl.",
    "world_is": "The three test files that reach the audit path no longer write it. The full collectable suite (13 files need moto, which is not installed) was not the disarm instrument; R-8 names the audit file's porcelain, which reads empty."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S14",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-09-28T22:05Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "The full opal-gateway suite does not finish on site Z: with moto installed (5.2.3, under Andrew's ~21:2xZ development-egress word), `pytest tests --ignore=tests/acceptance` hit a 900 s cap, and faulthandler showed tests/test_schwab_engine.py::test_ogq1_ac01 blocked in app/integrations/schwab/engine.py:1103 submit. The same test passes alone (7 s), and the whole file passes (13 of 13 in 58 s), so the stall is an inter-file interaction. It predates MP-f-1: the issuer's pre-fixture run stalled past 300 s as well.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Drain run on CLOUD after @5d36443784: rc=124 at 900 s; 'Timeout (0:02:00)!' dump with test_schwab_engine.py:203 test_ogq1_ac01 -> :199 main -> engine.py:1103 submit; audit.jsonl md5 unchanged, porcelain 0.",
        "A/B with the only difference being the conftest (A = C:/tmp/mp3-1 at pre-fixture d4bcedef5c, B = CLOUD): the single test passes in both (9.4 s / 7.0 s); the whole file is A '1 failed, 12 passed', B '13 passed'.",
        "Pre-fixture run 2026-09-28 ~20:4xZ (no moto): `timeout 300` terminated the full collectable suite at 306 s."
      ]
    },
    "spec_asserts": "The gateway suite is a drain instrument that finishes.",
    "world_is": "The suite stalls in the full-run context on this box, so the drain grades the affected files and the audit-file bound instead of a full-suite verdict.",
    "notes": "Not this project's surface (the Schwab engine is NFRA_OPLGTW's). Recorded only; the drain for MP-f-1 rests on the three audit-reaching files plus the engine-file A/B."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S15",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-09-29T04:50Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "The halt gate refuses every TWO-LETTER lane serial: .tools/halt-gate-check.sh halt_gate_validate_serial (:199-204) admits a ~lane only as a single uppercase letter ([A-Z]), so 2.0.0_SA_COO~MP, ~MI and ~AI -- all seated 2026-09-28 by placement @094c84f299 -- fail closed (exit 3) on their own safe-apply / safe-ec2-deploy. It surfaced when MP-a-2's worker ran safe-apply under this seat's session: the gate resolved the shared session serial file to 2.0.0_SA_COO~MP and refused it (row Z-W1-S6).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/halt-gate-check.sh:154-155 comment 'a ~lane suffix must be a single uppercase letter (every fabric lane is: ~A..~E, ~Z...)'; :201-204 case \"$lane\" in [A-Z]) : ;; *) return 1 ;; esac.",
        "Worker 0.9.0_WK_NFRA_MCPORTAL~1 report on MP-a-2: safe-apply stopped at the halt gate, which resolved 2.0.0_SA_COO~MP from the session serial file and failed closed on the two-letter lane; terraform never ran.",
        "Placement record org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_195xZ_O_FABRIC_ONLINE_ONE_COO_PER_PROJECT.md seats ~MI, ~MP, ~AI."
      ]
    },
    "spec_asserts": "Every seated serial can pass its own halt gate.",
    "world_is": "Three seated ~O COO lanes cannot safe-apply or safe-ec2-deploy as themselves. For THIS project it is routed around by the gate's own worker path (:71-73: an issuer-provisioned serial file inside the worker's worktree), so no act waits on the fix.",
    "notes": "The gate is 1.0.0_SA_CTO's (last authored 72897184fd). Remedy is a one-line class widening ([A-Z] -> [A-Z] or [A-Z][A-Z]) plus a test arm; it is the gate owner's, not this seat's."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W1-S6",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~1",
    "surfaced_at": "2026-09-29T04:20Z",
    "one_line": "MP-a-2's apply is BLOCKED before terraform runs: safe-apply's halt gate resolves the worker's shell to the issuer serial 2.0.0_SA_COO~MP (session serial file) and fails closed rc=3 because the ~MP lane suffix is not a single uppercase letter and no worker serial file is provisioned in the worktree.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply ... printed 'HALT-GATE: SERIAL RESOLVES TO NO KNOWN AGENT -- BLOCKED (fail-closed)', 'Resolved serial: 2.0.0_SA_COO~MP', from org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial; terraform was never invoked.",
        ".tools/halt-gate-check.sh:71-86 reads <worktree>/org/mcp/sessions/<sid>.serial first (an issuer may provision a worker's serial there); OPAL_AGENT_SERIAL is not consulted. That path is outside this order's <paths> and writing my own identity file would self-provision past the gate, so I did not.",
        "Everything before the act is done and lands nothing live: gateway line re-read (keys=email,exp,family_name,given_name,iss,name,picture,sub -> branch sub), layer built (PyJWT 2.13.0, cryptography 49.0.0, cffi 2.1.0, pycparser 3.0), staged package built, targeted plan read 7 add / 0 change / 0 destroy, ledger nfra-mcportal-r3-writer-apply opened and committed dd5ab90782 with L1 and L2 closed; L3 and L4 unrun."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A worker holding a non-terminal task order under the project can run safe-apply from its worktree (halt gate: 'a spine-v3 worker is admitted only while a NON-TERMINAL task order under <CODE> is issued_to it').",
    "world_is": "The halt gate takes the session's serial (the issuer's, 2.0.0_SA_COO~MP, two-letter lane) rather than the worker's, and refuses it; no worker serial file exists in C:/tmp/mp3-1/org/mcp/sessions.",
    "notes": "Unblock: the issuer provisions <worktree>/org/mcp/sessions/<sid>.serial for 0.9.0_WK_NFRA_MCPORTAL~1, or applies itself. Nothing is half-landed: no AWS resource was created. The owner key was never written to any file (the plan file I made with -out was deleted at once; the retained plan-free apply log is masked)."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S16",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-09-29T05:00Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "CLOSES NFRA_MCPORTAL-Z-S15 against 1.0.0_SA_CTO~O's fix @64a3ef4b4e (msg 26464, ruled its own): halt_gate_validate_serial now admits a lane of 1-3 uppercase letters.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Issuer read of the COMMITTED bytes (git show 64a3ef4b4e:.tools/halt-gate-check.sh): case \"$lane\" in [A-Z]|[A-Z][A-Z]|[A-Z][A-Z][A-Z]) : ;;",
        "Function sourced from those bytes: 2.0.0_SA_COO~MP rc=0; negative control 2.0.0_SA_COO~M1 rc=1."
      ]
    },
    "spec_asserts": "NFRA_MCPORTAL-Z-S15: the halt gate refuses every two-letter lane.",
    "world_is": "At 64a3ef4b4e the two-letter ~O COO lanes pass serial validation; a digit lane is still refused outside the worker limb."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S17",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-10-01T16:55Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S10"
    ],
    "one_line": "DISARMS NFRA_MCPORTAL-Z-S10, measured on the DEPLOYED bytes ahead of the first WRITTEN outcome (G-CLOSE with Alyssa): the live mcportal-grant-writer-lambda's lambda_function.py sets who = '<claim name> <email>' and never the owner-key value. It is byte-identical to CLOUD HEAD, including after NFRA_MCPMSP's register_tenant redeploy of 2026-09-30T10:58Z.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws lambda get-function mcportal-grant-writer-lambda Code.Location, 2026-10-01 ~16:5xZ: zip of 11 entries; lambda_function.py sha256 prefix 7e80d4359859 = CLOUD HEAD's file; :325 ctx[\"who\"] = (\"%s %s\" % (owner.claim, owner.email)) if owner.email else owner.claim; :190 \"who\": s(who).",
        "lambda_function.py:98 'claim: str   # the configured owner-key claim: \"oid\" or \"sub\"' -- the claim NAME; the live env MCPORTAL_OWNER_KEY_CLAIM=sub, key present (43 chars), read by key presence and length only.",
        "mcportal-grant-changes-table holds 1 item (narrow REFUSED NO-OWNER-HEADER 2026-09-29T05:00Z, who=UNVERIFIED); no WRITTEN item exists yet."
      ]
    },
    "spec_asserts": "NFRA_MCPORTAL-Z-S10 is ARMED: the first WRITTEN item would store the owner-key value.",
    "world_is": "The deployed writer stores the claim name and email only, so the G-CLOSE narrow and widen write no owner-key value. Z-S11 had disarmed on the plan (MP-b-3 shipped through MP-a-2); this row is the measurement on the running bytes.",
    "notes": "Re-measured because a second project's cell redeployed the same function after MP-a-2's drain."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S18",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-10-08T21:35Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "PRD v0.5 C11 gives the portal a read grant on two globgrph-bucket prefixes; the portal is served by the gateway process (C3), so that grant lands on opal-gateway-role, which graph-read.tf:4-8 says holds NOTHING on the globgrph bucket under NFRA_CLDGRPH's R3 control (CG-s-12).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md @8de5b2dc76 v0.5 addendum C11: 'The portal holds a read grant on those two prefixes only, Terraform-applied under C10.' (s3://opal-313476888478-globgrph/fabric/activity/v1/ and .../fabric/open-calls/v1/)",
        "same PRD C3: 'The built pages are static assets served by the gateway application at /. The admin API handlers live with the gateway'; app/server.py:1126 mounts admin_api.admin_app at /api/admin.",
        "infra/aws/terraform/opal-gateway/graph-read.tf:4-8: 'the gateway is a THIN PROXY ... It holds NOTHING on the globgrph S3 bucket ... the moment opal-gateway-role needs s3:GetObject there, R3 has been broken (CG-s-12, deliverable 0.7.0_AE_CloudOps~P B.3(iii))'.",
        "org/missions/D0/NFRA/NFRA_CLDGRPH/prd/NFRA_CLDGRPH_PRD.md:200 R3 (Andrew-direct 2026-09-02): the gateway is 'a THIN PROXY ... and never the host' of the graph SERVING PLANE; R3's text names the serving plane, the bucket-wide 'nothing' is CG-s-12's implementation of it."
      ]
    },
    "spec_asserts": "C11: the portal reads the activity and open-calls stores with a prefix-scoped read grant.",
    "world_is": "The only principal that can hold the portal's grant is opal-gateway-role, whose standing control (graph-read.tf, CG-s-12) is no grant of any kind on the globgrph bucket. Applying C11 as written breaks that control as written. Not acted on: no Terraform written, no grant applied.",
    "notes": "Holds only the grant cell of round 4 (FWD-14's store read). Ruling owner: 1.0.0_SA_CTO~O (contract text). Options named in the ask, issuer's rec first: (a) a prefix-scoped read on fabric/activity/v1/ and fabric/open-calls/v1/ only, with the graph-read.tf control text amended to carve out fabric/ (outside warehouse/, never the served graph); (b) the two stores move to a bucket the gateway may read; (c) the gateway proxies the reads through the projection service."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W6-S1",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~6",
    "surfaced_at": "2026-10-08T22:10Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "The worker's sparse worktree did not carry paths the workspace commit gates read (org/modules/graph, org/projects, infra/logic, and the sibling project trees under org/missions), so safe-commit refused three times before passing; the order's face names none of them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit 1st refusal: commit_gate_runner.py:96 ModuleNotFoundError comp_constants_cli (file is org/modules/graph/comp_constants_cli.py at HEAD, absent from the sparse cone).",
        "2nd/3rd refusal: missions-tree-check INDEX-MISSING org/projects/NFRA_MCPORTAL.json, then 45 INDEX-ORPHAN violations for sibling project trees under org/missions.",
        "git sparse-checkout list at start: .claude, .tools, infra/aws/ec2/opal-gateway, lib, org/devices, org/missions/D6/NFRA/NFRA_MCPORTAL, org/ref, org/standards. Worker ran `git sparse-checkout add org/modules/graph org/projects infra/logic org/missions org/surprise_channel` (worktree-local config, no repo write); the commit then passed (1fa09c0cc0, 0 violations)."
      ]
    },
    "spec_asserts": "The worker face says the worktree is a sparse checkout sufficient to commit a proof instance via safe-commit.",
    "world_is": "The cone as cut cannot pass the commit gates; five directories had to be added (org/surprise_channel as well, for the row gate). A later sparse worker would repeat it.",
    "notes": "Issuer's call whether the cut should widen the cone. Nothing was reconstructed beyond the four cone additions."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S19",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-10-08T22:05Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "Decomposition v4 R4.4 planned to cut MP-x-3, MP-x-4 and MP-x-5 into round 4 by issuer amendment after the issuance; to-pipeline-gate's ONE-ISSUANCE limb refuses any new order file in a round that already has an issuance, and reads no override. The three cells move to round 5.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "decompositions/NFRA_MCPORTAL_DECOMP.md @202c512520 R4.4: 'MP-x-3, MP-x-4 and MP-x-5 are cut into this round by issuer amendment when their gates land'.",
        "safe-commit of NFRA_MCPORTAL.TO-MP-x-3.gateway-fabric-read-grant.md, 2026-10-08 ~22:0xZ: '[to-pipeline-gate] REFUSED ... round 4 of NFRA_MCPORTAL already has an issuance at HEAD (2 order(s) ...); ONE ISSUER PER ROUND is keyed to the ROUND ... A re-cut into the first issuance MODIFIES its orders and adds no file ... this limb reads no override.' The '# pipeline-override' line was taken for the other limbs and did not lift this one.",
        "G-R3 is ruled (a) (laptop 1.0.0_SA_CTO msg 107359, relay 32030); the MP-x-3 order is drafted and its checks x3.AC1-3 are committed under deliverables/2.0.0_SA_COO~MP/round4/checks/ (dry-run at 202c512520: all FAIL)."
      ]
    },
    "spec_asserts": "R4.4: gated round-4 cells are cut into round 4 when their gates land.",
    "world_is": "A round's cells are cut in its one issuance or not in that round. MP-x-3 (G-R3 ruled), MP-x-4 (G-REL) and MP-x-5 (G-SEE) go on the round-5 enrichment list at round 4's L10; round 4 is MP-x-1 and MP-x-2. Cost: MP-x-3's apply waits for round 4's close; MP-x-4 already waits on MP-x-1, MP-x-2 and gateway r29.",
    "notes": "Issuer's practice from here: a gated cell is issued STAGED in the first issuance, with <placeholders> where its criteria await a ruling."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W5-S1",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~5",
    "surfaced_at": "2026-10-08T22:10Z",
    "one_line": "The worker worktree's sparse cone omits org/modules/graph, so .tools/commit_gate_runner.py (import comp_constants_cli) failed closed on the first commit; I added the one cone path with git sparse-checkout add and the commit then passed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit.sh first attempt in C:/tmp/mp-r4-5 printed: 'ModuleNotFoundError: No module named comp_constants_cli' at .tools/commit_gate_runner.py:96 and 'ERROR: BLOCKED -- commit-gate failed'; org/modules/graph/comp_constants_cli.py exists at HEAD 202c512520 but the cone listed only .claude, .tools, infra/aws/ec2/opal-gateway, lib, org/devices, org/missions/D6/NFRA/NFRA_MCPORTAL, org/ref, org/standards.",
        "After `git sparse-checkout add org/modules/graph` (408 tracked files, ~19 MB; no tracked content changed) the same safe-commit passed: commit 06bfb80b54 on wk-NFRA_MCPORTAL-r4-5."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A worker's sparse worktree carries every path its commit needs; the order names no cone addition.",
    "world_is": "The cone the issuer cut lacks org/modules/graph, which every .py commit's gate imports. Any later worker cut with the same cone fails its first .py commit identically. Also absent from the cone: org/surprise_channel/ (the row schema path the worker contract names), org/mcp/.",
    "notes": "Issuer fix: add org/modules/graph (and org/surprise_channel/schemas) to the cone the spawn recipe uses. No repo content was changed by the workaround; only this worktree's checkout."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W5-S2",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~5",
    "surfaced_at": "2026-10-08T22:50Z",
    "one_line": "A cone-mode sparse worktree cannot commit any org/missions path through safe-commit: the surprise-row gate and missions-tree-check read every project's channel, register, PRD and ledger files, and the hook index that git commit --only builds hides the skip-worktree rows the checker's sparse fallback relies on (tree=2 in the hook, tree=46 run by hand).",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Four safe-commit refusals at C:/tmp/mp-r4-5, each from a different missing path: surprise-row-gate 'standing corpus pass could not run (FileNotFoundError ... NFRA_CLDGRPH ... INVESTIGATION_v1.md)', then NFRA_CTLPLN, then remediations/REMEDIATION_v1.md; missions-tree-check 'tree=2 project(s) ... 44 violation(s)' (INDEX-ORPHAN), then 'could not run (rc=2) ... org/missions/MACROS.yaml', then four [R6] CLOSED-project refusals (PRD header, ledger/COMPLETION_*.json).",
        "Same checker run by hand in the same worktree: 'tree=46 project(s) ... 42 valid ... RESULT: 0 violation(s)'. In the hook it printed tree=2. GIT_TRACE shows the hook ran with GIT_INDEX_FILE=.git/worktrees/mp-r4-5/next-index-26912.lock; SAFE_COMMIT_TWO_PHASE=0 changed nothing.",
        "Workaround that landed commit 7d25a4d8c1 with no override: git sparse-checkout converted to non-cone (MSYS_NO_PATHCONV=1, else every pattern is rewritten to C:/Program Files/Git/...), adding /org/missions/*/*/*/project.json, .../surprise-channel/{investigations,remediations}/*, /org/missions/*.yaml, and the prd/ and ledger/ dirs of NFRA_OPSEC202609, LGIC_NAMING, POSN_AGGFIX, POSN_ASTTAX. The first attempt without MSYS_NO_PATHCONV un-materialised the worktree (tracked files untouched; reversed by the second call)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A worker whose order names paths under org/missions can commit them from its sparse worktree.",
    "world_is": "Not without widening the cone by the set above; the cell's own cone (the order's paths) is not enough. The CLOSED-project R6 limb and the channel corpus pass read files that no cone-mode cone of a worker can hold except by listing 41 project directories (836 MB, 20933 files).",
    "notes": "Issuer fix: cut worker worktrees with the non-cone pattern list above (or one the issuer owns), or give missions-tree-index.py and surprise-row-gate.py the index-read fallback inside the hook environment (the checker already has one at _index_only_projects, which returns [] under the hook's index). The orders' proof step cannot be committed from a bare cone worktree."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S20",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-10-09T02:08Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-W3-S3",
      "NFRA_MCPORTAL-Z-C-S8",
      "NFRA_MCPORTAL-Z-C-S10",
      "NFRA_MCPORTAL-Z-W3-S2"
    ],
    "one_line": "DISARMS Z-W3-S3 / Z-C-S8 (the writer cannot import from its own zip), Z-C-S10 (the writer assumes an oid/iat claim) and Z-W3-S2 (no record of Andrew's Entra oid). These are the round-1 ARMED rows transferred to this issuer by the CTO's R-18 (ROUND_ANALYSIS.round4.md @460bc0af2f). Each premise was overtaken by a later round's measured act.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-W3-S3 / Z-C-S8: round 2's MP-b-1 (staged build, complete) builds the writer package that imports at /var/task; row Z-S17 measured the DEPLOYED mcportal-grant-writer-lambda zip (11 entries, lambda_function.py = CLOUD HEAD) answering a live no-header invoke REFUSED NO-OWNER-HEADER, which requires the handler to import inside the zip.",
        "Z-C-S10: E1 (deliverables/2.0.0_SA_COO~MP/round3/E1_G-HDR_READ.md @c8b42c8913) measured the header's keys email,exp,family_name,given_name,iss,name,picture,sub -- no oid, no iat; PRD C4 was re-signed for the sub branch (v0.3 @963fff9f5a, @24ef97a3b7) and MP-a-2 applied MCPORTAL_OWNER_KEY_CLAIM=sub (complete, ledger 20260929T0412Z CLOSED).",
        "Z-W3-S2: the oid record it asked for is no longer an input -- the owner key is Andrew's sub from /api/admin/whoami, given off-repo (G-SUB, deliverables/2.0.0_SA_COO~MP/round3/ANDREW_DIRECT_20260929_04xxZ_G-SUB_GIVEN.md), and MP-a-2's apply consumed it."
      ]
    },
    "spec_asserts": "Z-W3-S3, Z-C-S8, Z-C-S10, Z-W3-S2 ARMED (round-1 thread hazards).",
    "world_is": "All four premises were overtaken by measured acts: the staged build, E1's header read, the sub-branch apply and the deployed writer's live refusal. None is a live hazard. Each row's remediation-plane flip is the CVO's act.",
    "notes": "Filed by the issuer under the CTO's R-18 transfer. The CTO's R-18 places the W1-S1 / C-S3 remediation flip with the CVO; this row does not cover it."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S21",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~MP",
    "surfaced_at": "2026-10-09T03:00Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "MP-x-3 STOPPED before the apply: safe-apply's naming plan limb REFUSES the policy name the TO specifies (opal-gateway-mcportal-fabric-read), and that same name is what the TO's AC1 looks up, so the gate's remedy and the TO's criterion are mutually exclusive. The commit-time limb did NOT refuse it (a G3 RAISE), so the refusal surfaces only at apply, after the ledger was open.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MP",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "APPLY-TIME REFUSAL, verbatim: '[naming-plan-gate] NAMING REFUSE aws_iam_role_policy.gw_mcportal_fabric_read opal-gateway-mcportal-fabric-read -> gateway-mcportal-fabric-read-policy' / why: 'aws_iam_role_policy.gw_mcportal_fabric_read (ADDITION): OUT-OF-PATTERN as IAM_POLICY: the module would not produce this name; an apply has no diff and runs this stage before any plan, so the name is read as the tree states it' / '[naming-plan-gate] NAMING-PLAN: REFUSE 2 graded' / 'safe-apply: BLOCKED by the naming plan limb (LGIC_ENFORCE DEC-6, ENFORCE mode, rc=1). Nothing was planned further or applied.'",
        "COMMIT-TIME limb did NOT refuse the same name, so the TO's step-2 prediction (a refusal at commit) never fired: '[naming-gate] NAMING RAISE infra/aws/terraform/opal-gateway/mcportal_fabric_read.tf:40 {x}-mcportal-fabric-read -> (rule or registry defect)' / why: 'G3: the tokeniser cannot place a character of a resource name {x}-mcportal-fabric-read' / '[naming-gate] NAMING-GATE: WARN 1 graded'. The commit limb sees the UNRESOLVED ${var.name} and cannot tokenise it; the apply limb resolves it and refuses. Commit e5a036a659 therefore landed.",
        "THE NAME IS PINNED BY THE TO'S OWN CRITERION: checks/x3.AC1.sh calls 'aws iam get-role-policy --role-name opal-gateway-role --policy-name opal-gateway-mcportal-fabric-read'. Adopting the gate's remedy makes AC1 fail NoSuchEntity. TO step 2 forbids an override; TO BOUNDS 3 forbids repairing a criterion. Both legal moves are closed to the worker.",
        "BUILDER MEASURED (lib/opal_naming.py): name('gateway', None, 'mcportal-fabric-read', 'policy') -> 'gateway-mcportal-fabric-read-policy'; name('mcportal', None, 'fabric-read', 'policy') -> 'mcportal-fabric-read-policy'. Neither is the TO's string.",
        "THE MODULE ALREADY CARRIES BOTH CONVENTIONS, so this is not a uniform legacy surface: mcportal_grant_writer.tf uses the BUILDER form in literals ('gateway-read-mcportal-grant-changes-policy', 'gateway-invoke-mcportal-grant-writer-policy') on the SAME role aws_iam_role.gw, commenting that the literal was chosen because 'the commit-time naming gate grades a NEW resource name's own bytes, and var.name's runtime value is opaque to it (G3 RAISE on the unresolved ${var.name} token)'. The older grants (secrets-iam.tf '${var.name}-golive', graph-read.tf '${var.name}-graph-read-secret-read', ycharts-iam.tf '${var.name}-ycharts-secret-read') use the interpolated legacy form the TO copied.",
        "THE SAME RUN ALSO WARNED ON THE ROLE ITSELF: '[naming-plan-gate] NAMING WARN aws_iam_role.gw opal-gateway-role -> gateway-role ... (existing): OUT-OF-PATTERN as IAM_ROLE ... not confirmed as an addition here, so this only WARNs'. So var.name='opal-gateway' is itself out of pattern against the builder's 'gateway' token: the whole module is mid-migration and only an ADDITION is refused.",
        "WORLD VERIFIED UNCHANGED, not taken from the wrapper's self-report: AC1 live -> 'NoSuchEntity ... policy with name opal-gateway-mcportal-fabric-read cannot be found' (rc=254); 'terraform state list' has no gw_mcportal_fabric_read (grep -c -> 0). Nothing landed; the named rollback was a NO-OP and was not run. Ledger 20261009T0242Z_nfra-mcportal-r4-fabric-read-grant: L1 CLOSED (plan 1 to add, 0 to change, 0 to destroy), L2 CLOSED as NOT EXECUTED, entry HELD-SOVEREIGN-GATED on the issuer.",
        "ID GRAMMAR: the TO (section 3) directs rows to id 'NFRA_MCPORTAL-Z-A7-S<k>'. surprise-row-gate.py REFUSES that: 'a NEW row has id=NFRA_MCPORTAL-Z-A7-S1, which does not match the id grammar <CODE>-(Z-)?(W<n>-|C-)?S<k> (annex v3.2 section 4)'. There is no A7 coordinate in the grammar, so this row carries the legal seat form Z-S21 instead. No override was taken.",
        "CHANNEL LOCALITY: this row was first written in the SHARED tree per CLAUDE.md 14b's append-only inversion, where the gate's STANDING CORPUS PASS refused it for failures that are NOT this cell's -- 'NEW ... NFRA_OPLGTW-Z-AE-S1 /id' and 'NFRA_OPLGTW-Z-AE-S2 /id' (the same illegal-coordinate class, another lane's uncommitted rows), denominators 'documents=308 rows=9659 failures=8 baseline=4 known=4 new=4 resolved=0'. Clearing that would have needed the audited '# surprise-row-override:' line on a commit, so the row was moved into this worktree, where the corpus is at the clean base and the gate passes unforced. The 14b inversion therefore COUPLES a seat's row to every peer's uncommitted rows in the shared tree."
      ]
    },
    "spec_asserts": "TO MP-x-3 step 1 specifies the policy name '${var.name}-mcportal-fabric-read' (= opal-gateway-mcportal-fabric-read), and step 2 anticipates that if the naming gate refuses that name it refuses AT COMMIT, where the worker files a BLOCKING row and stops. Section 3 directs rows to the id coordinate A7.",
    "world_is": "The commit-time limb does not refuse the name -- it RAISEs (G3), because ${var.name} is unresolved at commit, so the commit landed. The refusal arrives one stage later, inside safe-apply's naming plan limb, which resolves the interpolation and grades the ADDITION as OUT-OF-PATTERN. The act is stopped AFTER the ledger was opened and the plan had graded clean at 1 to add / 0 to change / 0 to destroy, not before the build. Because AC1 looks the policy up by that exact name, no single name satisfies both the gate and the criterion. Separately, the A7 id coordinate the TO directs is not in the gate's grammar.",
    "notes": "Issuer's call, three options, none available to the worker: (a) re-cut AC1 (plus the TO's step-1 name, the new file's header and graph-read.tf's citation) onto the builder's 'gateway-mcportal-fabric-read-policy', matching the two sibling MCPORTAL policies already in this module -- the only option needing no override and no law change; (b) obtain an R20 register entry (infra/logic/registry/, Andrew acknowledges) recording a deliberate departure for the legacy '${var.name}-' form under rule 30's existing-pipeline non-application, then re-run; (c) route the gate itself to 1.0.0_SA_CTO as a defect, since the commit limb's G3 RAISE admits a name the apply limb then refuses -- so EVERY new interpolated name in this module discovers its refusal only after its ledger is open. Worktree C:/tmp/mp-x3, branch wk-mp-x3, commits e5a036a659 (build) and 4f639cc38d (ledger), NOT drained."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S22",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~MP",
    "surfaced_at": "2026-10-09T09:02Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "TO MP-k-2 step 2 directs the PLAN to be run with safe-apply, but safe-apply gates the apply subcommand ONLY and refuses every other subcommand by construction (rc=2), telling the caller to invoke terraform directly -- so the instruction is unsatisfiable as written and the wrapper's own usage text is the remedy. The plan was run with terraform directly, the act was NOT blocked, and the apply still goes through safe-apply per step 4.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MP",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED REFUSAL, verbatim, from the worktree root C:/tmp/mp-k2: '.tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway plan -target=aws_iam_role_policy.gw_mcportal_close_request_write' -> 'safe-apply: ERROR -- no \\'apply\\' subcommand in the arguments.' / 'safe-apply: this wrapper gates \\'terraform apply\\' only. For \\'plan\\' or any other subcommand call the terraform binary directly.' / 'safe-apply: usage -- safe-apply.sh [-chdir=DIR] apply [apply-args...]' ; rc=2.",
        "THE REFUSAL IS BY DESIGN, NOT A DEFECT, and the wrapper documents it in its own header (.tools/safe-apply.sh:19-21): 'Gates `apply` ONLY. `plan` and other subcommands are non-destructive -- call terraform.exe directly for those.' The loop that produces the exit is :53-67 (it scans argv for the literal 'apply' and exits 2 when absent).",
        "THE WORK WAS NOT BLOCKED. The plan ran with the terraform binary directly, resolved device-agnostically per CLAUDE.md (no .tools/terraform.exe on site Z; terraform v1.15.8 on PATH), and graded exactly as the order requires: 'Plan: 1 to add, 0 to change, 0 to destroy.' with one statement, Action ['s3:PutObject'], Resource ['arn:aws:s3:::opal-313476888478-globgrph/fabric/open-calls/v1/box=*/requests/*'], Sid 'McportalCloseRequestWriteOnly', role 'opal-gateway-role'. Saved to C:/tmp/mp-k2.tfplan.",
        "THE APPLY PATH IS UNCHANGED by this row: step 4's 'ACT with safe-apply, targeted to the same resource' is satisfiable exactly as written, because that invocation does carry the 'apply' subcommand. Only the PLAN sentence in step 2 is unsatisfiable. No override was taken and none is needed.",
        "NOT A ONE-OFF WORDING SLIP WORTH LEAVING UNRECORDED: the sibling order in this same workstream, TO-MP-x-4 step 1, routes its EC2 act through infra/aws/ec2/safe-ec2-deploy.sh rather than safe-apply, so the two orders use the wrappers correctly where they are write acts. The conflation is specifically plan-vs-apply."
      ]
    },
    "spec_asserts": "TO MP-k-2 step 2 ('Plan, and the ASK') directs: 'Run the plan with `safe-apply`, targeted to aws_iam_role_policy.gw_mcportal_close_request_write only.' That sentence presumes safe-apply can run a plan.",
    "world_is": "safe-apply refuses any argv without the literal 'apply' subcommand and exits 2 before terraform is invoked at all, so no plan can be produced through it. The wrapper's own usage text names the correct call ('call the terraform binary directly'), which is what was done. The gating sequence the order actually depends on is intact: the plan graded 1 to add / 0 to change / 0 to destroy before the ASK was written, and the irreversible apply will run through safe-apply's HALTGT checkpoint per step 4.",
    "notes": "Issuer's call, and nothing in this cell waits on it: (a) re-word step 2 of the next cut to 'run the plan with the resolved terraform binary, targeted' and leave step 4's safe-apply sentence as-is -- the minimal fix, no mechanism changes; (b) leave the orders alone and treat the wrapper's usage text as the standing remedy, accepting that each applier seat pays one refused invocation to discover it. Either way the proof_of_spec is untouched: AC1/AC2/AC3 do not mention safe-apply. Worktree C:/tmp/mp-k2, branch wk-mcportal-cp2-k2, cut from box/sitez @5db9d4cbabf33ac5298e2c6a956cfc8ec2c90abb."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S23",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~MP",
    "surfaced_at": "2026-10-09T09:52Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "The opal-gateway Terraform module does not plan clean: an UNTARGETED plan reads '0 to add, 1 to change, 0 to destroy' (aws_lambda_function.mcportal_grant_writer updated in-place) AND errors reading a data source for a Secrets Manager secret that does not exist (gateway/mail/commassist-bearer). Neither was caused by MP-k-2 and neither was touched: this cell's own resource is 0-diff. The hazard is for the NEXT actor here -- a bare untargeted apply in this module would move a Lambda nobody asked to move, or fail on the absent secret.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MP",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED, after MP-k-2's apply, from C:/tmp/mp-k2 at HEAD 542de4b7e8. TARGETED plan on this cell's resource: 'No changes. Your infrastructure matches the configuration.' UNTARGETED plan on the same module: 'Plan: 0 to add, 1 to change, 0 to destroy.' plus 'Error: reading Secrets Manager Secret (gateway/mail/commassist-bearer): couldn't find resource'.",
        "THE ONE CHANGE IS NAMED, not inferred: the untargeted plan's own line is '# aws_lambda_function.mcportal_grant_writer will be updated in-place'. It is a Lambda function, not an IAM policy, so it is outside this cell's write surface (TO MP-k-2 section 3) and outside its never-widen pair's blast radius.",
        "NOT CAUSED BY THIS ACT, and that is a measurement rather than an assumption: 0 files changed under infra/aws/terraform/opal-gateway/ between the commit the plan was saved at (77184244cf) and HEAD, so the module's configuration base did not move across this cell; and the apply consumed a SAVED plan whose only entry was the single aws_iam_role_policy addition. The post-apply targeted re-plan reading 'No changes' confirms this cell's resource is settled.",
        "DIRECTION OF THE HAZARD: a Lambda updated 'in-place' by a stray untargeted apply is the CLAUDE.md 22a CODE class -- deployed bytes moving without a build input anyone chose. The absent-secret error is the opposite failure, a plan that cannot complete at all; together they mean no actor in this module can currently get a clean whole-module 0-diff, which is the standard post-apply control that /cloud-ops pre-flight step 5 asks for.",
        "WHY INERT RATHER THAN ARMED: nothing in flight is running an untargeted apply here. This cell applied a saved targeted plan, and the sibling MCPORTAL acts (MP-x-3, and MP-x-4 when it runs) are likewise targeted or route through safe-ec2-deploy.sh. The hazard needs a future actor to choose a bare apply, so it is latent, not live. It is also not this seat's to disarm: aws_lambda_function.mcportal_grant_writer and the commassist secret are outside the write surface its task order grants."
      ]
    },
    "spec_asserts": "The standard post-apply control (/cloud-ops pre-flight step 5, and the 0-diff habit the sibling MCPORTAL orders rely on) is that a module plans clean after an apply: no changes, no errors. MP-k-2's own bounds also assert that 'no other Terraform resource moves'.",
    "world_is": "This cell's resource does plan clean, targeted. The MODULE does not: untargeted it wants to update aws_lambda_function.mcportal_grant_writer in place and it errors on a data source for the absent secret gateway/mail/commassist-bearer. Both conditions pre-date MP-k-2 (0 files changed in the module between the saved plan's commit and HEAD) and both were left exactly as found. So MP-k-2's bound held -- no other resource moved -- but the module's whole-module 0-diff control is unavailable to the next actor until these two are dispositioned.",
    "notes": "Issuer's call, and nothing in MP-k-2 waits on it: (a) route the Lambda drift to whoever owns mcportal_grant_writer (the MCPORTAL grant-writer cell) to re-plan and either apply or pin it, and the absent secret to whoever owns the gateway mail/commassist path -- most likely a half-landed or not-yet-created secret from another lane's in-flight work; (b) if either is known and accepted, record it so the next actor reads a known-drift note instead of rediscovering it mid-act. Either way the standing advice for this module is the one this cell followed: plan and apply TARGETED, from a saved plan, never a bare apply. Measured from worktree C:/tmp/mp-k2, branch wk-mcportal-cp2-k2, at 542de4b7e8."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S24",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~MP",
    "surfaced_at": "2026-10-09T14:35Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "`deploy_ledger.py hold` REGENERATES the change_management entry from its structured state and SILENTLY DISCARDS any prose appended to the file -- rc=0 and a cheerful 'OK: ... -> HELD-PRE-APPLY'. Measured: it removed 115 lines of MP-x-4's required pre-act record (census, four cold-read samples, the content-verified rollback, the halt-gate pre-flight, the tool-surface BEFORE count), leaving a 23-line entry. The task order REQUIRES those records 'in the ledger entry', so the tool destroys the evidence the order asks the entry to carry.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~MP",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED, not inferred. Appended the pre-act record at ca9b6c05f0 ('1 file changed, 114 insertions(+)'). Ran `deploy_ledger.py hold --slug nfra-mcportal-r5-control-plane-release --gate-type external --gate-ref ... --reread-event ... --pre-apply`, which printed 'OK: ... -> HELD-PRE-APPLY ... Reads KNOWN-HELD (no half-landed RED)' and exited 0. The commit of that result read '2 files changed, 16 insertions(+), 118 deletions(-)'; the entry-only diff ca9b6c05f0..b8fc617e2e is '1 file changed, 2 insertions(+), 115 deletions(-)'. Entry line count 137 -> 23.",
        "WHAT WAS LOST, read back by token count in the post-hold entry: '16.767' (the first cold sample) 0; the rollback artifact's ETag '3157ad0796dae6f9ad26dea7a1e46469' 0; 'tool_count = 66' 0; '1.79x' (the bar headroom) 0. The ONLY survivor was '77 of 77', and only because it sits inside a LEG's declared proof string, which the tool regenerates from its own state -- which is the tell: structured leg fields survive, free prose does not.",
        "THE LOSS IS SILENT IN BOTH DIRECTIONS. The tool's stdout announces success and names no removal; its own follow-up `check` then reports the entry as 'KNOWN-HELD ... tracked-not-stranded', which is TRUE about the hold and says nothing about the deleted record. Nothing in the rc, the stdout or the check output distinguishes a hold that preserved the entry from one that gutted it. It was caught only by reading the commit's own insertion/deletion counts, which disconfirmed the assumption that a hold flips a status.",
        "NOT RECOVERABLE FROM THE ENTRY, but not lost: the content is in git at ca9b6c05f0 and restated in that commit's message. It has been re-homed to org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/MP-x-4_PRE_ACT_RECORD.md (a path the tool never writes), with a short POINTER left in the entry. That is a workaround, not a fix: the next `close-leg`/`close` on this slug is expected to drop the pointer too, by the same regeneration.",
        "SCOPE IS WIDER THAN THIS CELL, and that is why this is ARMED rather than an observation. Every NEVER-2 deploy in the fabric opens an entry and many task orders instruct the actor to RECORD evidence in it (MP-x-4 step 4: 'Record the census, the cold-read time, the rollback and this order's path'; MP-k-2 step 4 likewise). Any such seat that appends prose and then holds, closes a leg, or closes the entry loses that prose with no signal. MP-k-2 escaped only because this seat happened to put its evidence in commit messages and a separate ASK file rather than in the entry.",
        "WHY IT WAS NOT CAUGHT ON MP-k-2 EARLIER TODAY: that cell appended nothing to its entry, so the regeneration had nothing to discard. ABSENT is not EXERCISED-AGAINST -- MP-k-2's clean close is not evidence the tool preserves prose; it is evidence the question was never asked."
      ]
    },
    "spec_asserts": "TO MP-x-4 step 4 directs: 'Run `python .tools/deploy_ledger.py open ...` ... Record the census, the cold-read time, the rollback and this order's path.' That instruction presumes the entry is a durable place to record evidence across the entry's own lifecycle verbs.",
    "world_is": "The entry is a GENERATED artifact, not an append-only log. `hold` rewrites it from the tool's structured state: declared leg descriptions and proof strings survive, the Log lines survive, and everything else a human or agent wrote into the file is dropped. rc=0, stdout says OK, and a following `check` still reports the entry healthy. So the order's 'record it in the entry' and the tool's regeneration are in direct conflict, and the conflict surfaces only as a line-count delta in the commit that carries the hold.",
    "notes": "Issuer's call; MP-x-4 is NOT blocked by it (the record is re-homed and the act is separately held on OG-ap-4). Options: (a) make the entry append-safe -- have `hold`/`close-leg`/`close` preserve any content below a marker line, which is the minimal fix and keeps every existing order's wording valid; (b) route the tool's lifecycle verbs through an explicit `--note` field so prose becomes structured state the regeneration keeps; (c) change the ORDER TEMPLATES instead, so cells are told to record evidence in a deliverable and leave only a pointer in the entry -- cheapest today, but it leaves a tool that silently eats what is written to it. This cell used (c) as a workaround by necessity. Whichever is chosen, the SILENCE is the defect: a destructive regeneration that returns rc=0 and reports KNOWN-HELD afterwards cannot be distinguished from a safe one by any output the tool produces. Measured from worktree C:/tmp/mp-x4, branch wk-mcportal-r5-x4, entry 20261009T1414Z_nfra-mcportal-r5-control-plane-release, at b8fc617e2e."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S25",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-10-09T14:46Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S24"
    ],
    "one_line": "DISARMS Z-S24 for this project. Evidence a cell must keep is no longer written into a change_management entry that `deploy_ledger.py hold` / `close-leg` regenerate. MP-x-4's record is re-homed and accepted, and MP-r-2 (AMENDMENT 4) writes its pre-act record to a deliverables file and leaves only a pointer in the entry. The tool's silent regeneration is routed to 0.0.0_AB_MSTR~Z, the infrastructure owner; it is not this project's write.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Z-S24 measured the loss: the entry went from 137 to 23 lines across `hold` (ca9b6c05f0..b8fc617e2e: 2 insertions, 115 deletions). The record survives in git at ca9b6c05f0 and is re-homed at deliverables/0.7.0_AE_CloudOps~MP/MP-x-4_PRE_ACT_RECORD.md @0b4deae4f4, a path the tool never writes.",
        "This project's open cells that write a ledger entry are MP-x-4 (in flight, HELD-PRE-APPLY) and MP-r-2 (staged). MP-k-2 is complete; its entry closed, and the evidence its ACs read lives in the deliverables and the proof instance, not in prose. MP-q-1 writes no ledger. So the remaining exposure is the two release cells, and both are covered by this disarm."
      ]
    },
    "spec_asserts": "Z-S24 ARMED: the task orders require pre-act records 'in the ledger entry', and the tool deletes that prose on hold/close-leg.",
    "world_is": "For NFRA_MCPORTAL the requirement is re-pointed: the record lives in a deliverables file, the entry carries a pointer, and the drain reads the deliverables file. The tool still regenerates silently. That defect, a destructive rewrite returning rc=0 with KNOWN-HELD, is routed to 0.0.0_AB_MSTR~Z and stays open there.",
    "notes": "Disarm owner per Z-S24: 2.0.0_SA_COO~MP (issuer). The pointer may itself be dropped by a later close-leg; at the drain the issuer reads the deliverables record, never the entry's prose."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S26",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-10-09T15:46Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S24",
      "NFRA_MCPORTAL-Z-S25"
    ],
    "one_line": "The tool defect behind Z-S24 is FIXED at its source by 0.0.0_AB_MSTR~Z @a9d1b38f12 (CTO~Z msg 32830 ruled the tool MSTR's). deploy_ledger.py _write_entry now carries every hand-written section and hand line under '## Carried notes'. A replay of MP-x-4's entry at ca9b6c05f0 through hold keeps 136 of 136 lines, where the defect gave 23. Z-S25's discipline (record in a deliverables file, pointer in the entry) stays for MP-x-4 and MP-r-2 as cheap redundancy.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "0.0.0_AB_MSTR~Z msg 32853 (2026-10-09T15:43Z): fix @a9d1b38f12 on box/sitez; the held and malformed batteries still pass; the prose already lost at b8fc617e2e is not restored, and is in git at ca9b6c05f0 and re-homed at MP-x-4_PRE_ACT_RECORD.md @0b4deae4f4."
      ]
    },
    "spec_asserts": "Z-S24: deploy_ledger.py hold/close-leg silently drop appended entry prose.",
    "world_is": "The tool is fixed at source @a9d1b38f12. This project's record discipline (Z-S25) is kept, and the issuer does not re-test the fix.",
    "notes": "Measured by the fixer's replay, cited not re-run. A worktree based before @a9d1b38f12 still runs the old tool; the applier's MP-x-4 release tree is cut from box/sitez, so its base decides which version it runs."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S27",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~MP",
    "surfaced_at": "2026-10-09T16:48Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "The Control Plane page's cold read is UNDER R-13's 30 s bar but its margin is SHRINKING through the working day, because the handler's default window is a ROLLING 6 hours and the record count in it grows with commit volume. Measured today: 13.6-16.8 s over ~3,150 records at 14:0xZ, 18.1-24.4 s over ~3,790 records at 15:5xZ, 24.2 s over 4,040 records at 16:2xZ. Headroom fell 1.79x -> 1.23x in about two hours. Shipped as-is because the order's remedy fires only ABOVE 30 s; this row carries the trend to the enrichment list.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MP",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SEVEN release-time samples, all on the host under the instance role, all cold (a fresh interpreter per sample, so admin_fabric's in-process body cache is empty by construction). On base 91811b648a at ~14:0xZ: 16.767 / 15.336 / 13.964 / 13.615 s over 3141-3154 records, 0 skipped. On base c97232408d at ~15:5xZ: 24.443 / 19.728 / 18.118 s over 3788-3793 records, 0 skipped. AC3's own post-deploy read at ~16:2xZ: compute_s=24.2 over 4,040 records. Warm reads moved 0.765-0.839 s -> 0.986-1.096 s across the same span.",
        "THE DENOMINATOR IS THE EXPLANATION, which is why this is a trend and not noise: the record count rose ~3,150 -> ~4,040 (+28%) in about 2.3 hours of a working day, and the cold time rose with it. Implied cost ~5.5 ms/record, so the 30 s bar sits near ~5,460 records in the window. The window is ROLLING 6 hours (admin_fabric DEFAULT_HOURS=6, MIN 1 MAX 24), so the count climbs through the working day and falls overnight -- the worst case is a late-day first open, not a morning one.",
        "THE ISSUER WARNED OF EXACTLY THIS and the measurement now quantifies it: its 04:2xZ FYI said '21.3 s sits under R-13's 30 s bar with thin margin, and the 6-hour window grows with daytime commit volume. Its value at your release-time measurement is the one that counts.' Note the earlier 21.3 s figure scanned FEWER records (3,004) than today's 14:0xZ samples at ~3,150 yet read SLOWER, so per-record cost is not the only term -- S3 latency and host load move it too, and a single sample cannot separate them.",
        "WHY IT SHIPPED ANYWAY, and this is the order's own rule rather than a judgement: MP-x-4 step 2 says 'If it takes more than 30 s (half the ALB's 60-second idle timeout): before release, narrow the handler's default window (6 to 2 hours) or warm the body cache at boot'. Every release-time sample was under 30 s, so the remedy did NOT fire, app/admin_fabric.py shipped exactly as MP-x-1 wrote it, and no criterion was repaired. Narrowing the window un-triggered would have changed product behaviour the order did not authorise.",
        "THE REAL TIMEOUT IS FARTHER AWAY THAN THE BAR, stated so the risk is not overread: the ALB idle timeout is 60 s and the 30 s bar is the order's half-margin, so at 24.4 s the page is ~2.5x from an actual timeout and ~1.23x from the policy bar. The hazard is a BREACHED POLICY MARGIN first, a user-visible timeout only well after that.",
        "A 2-HOUR WINDOW WAS MEASURED BUT IS NOT A CLEAN FIGURE: _compute(2) read 0.79-1.10 s, taken AFTER the 6h calls in the same process, so overlapping bodies were already cached. That is a LOWER bound on a cold 2-hour read, never a cold figure, and it is reported as such -- a cold 2h measurement needs its own fresh interpreter and has not been taken."
      ]
    },
    "spec_asserts": "R-13 sets one bar -- the cold _compute(6) must be at or under 30 s at the release-time measurement -- and MP-x-4 step 2 treats that single reading as the decision: 'A page whose first open can time out never ships.'",
    "world_is": "The bar is met at every release-time sample, but the quantity it measures is not stationary: it tracks a rolling 6-hour record count that grew 28% during this cell's own execution and carried the cold read from 13.6 s to 24.4 s. So a point measurement against a fixed bar certifies the moment of the act, not the page's behaviour later the same day. The order has no re-measure clause and no alarm (and the standing moratorium forbids building one unasked), so nothing currently re-reads this number after the release.",
    "notes": "Issuer's call for the enrichment list; nothing in MP-x-4 waits on it and the page is live and serving. Options, cheapest first: (a) narrow DEFAULT_HOURS 6 -> 2 in app/admin_fabric.py, which the order already names as an authorised remedy shape and which the page's 60-second refresh makes cheap -- needs a cold 2h measurement first, since the only 2h figure taken is cache-warm; (b) warm the body cache at boot, also named by the order, which moves the cost off the first open; (c) bound the work rather than the window (cap keys scanned, or paginate), which is the only option that does not degrade with fabric growth; (d) accept and re-measure at a stated cadence. Do NOT read this row as a request for an alarm or monitor -- that is under a standing moratorium and would need Andrew's explicit word. Measured by 0.7.0_AE_CloudOps~MP during MP-x-4; the figures and their denominators are in deliverables/0.7.0_AE_CloudOps~MP/MP-x-4_PRE_ACT_RECORD.md."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S28",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~MP",
    "surfaced_at": "2026-10-09T16:48Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "x4.AC2.sh reads mcportal_commit's ancestry with a bare `git -C mcportal ... 2>/dev/null`, but a LINKED WORKTREE has no nested mcportal checkout, so the command fails, the redirect swallows the error, and the clause reports 'contains d60b4e0=no' -- a FALSE NEGATIVE that fails the whole criterion. The same class of sparse/linked-worktree gap also made deploy-to-ec2.sh refuse once (it needs data/transcripts/scripts/teams/meeting_allowlist.json under the calling worktree root).",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MP",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED. Run from the cell's trunk worktree C:/tmp/mp-x4, x4.AC2.sh printed 'deployed=1e32562729... previous=c97232408d... descends=yes; gateway app/tests files changed=4, outside MP-x-1's set=0; mcportal_commit=d60b4e0 contains d60b4e0=no' and RESULT: FAIL. Three of four clauses pass; only the mcportal clause reads no.",
        "THE CLAUSE IS SELF-CONTRADICTORY ON ITS FACE, which is the tell: it prints 'mcportal_commit=d60b4e0 contains d60b4e0=no'. The value and the sought token are the same string, so a correctly-running test could not answer no.",
        "CAUSE, read from the script and confirmed in the filesystem: line `mok=no; [ -n \"$MCP\" ] && git -C mcportal merge-base --is-ancestor d60b4e0 \"$MCP\" 2>/dev/null && mok=yes`. _root.sh cds to the CALLING worktree root, and `test -d mcportal` there is FALSE (`test -e mcportal/.git` also false): git checks a nested repo out in the MAIN tree only. So git exits non-zero for a missing path, 2>/dev/null hides the reason, and the && chain leaves mok at its initialised `no`. An ABSENT REPO and a GENUINELY WRONG COMMIT are indistinguishable in the output.",
        "THE SUBSTANCE IS TRUE, verified directly with a positive control: from the main tree, `git -C mcportal merge-base --is-ancestor d60b4e0 d60b4e0` exits 0 (YES), while the control `is-ancestor d60b4e0 d60b4e0~1` exits non-zero -- so the test discriminates and the clause's real answer is yes.",
        "AND IT PASSES AS WRITTEN once the record is at HEAD in a tree that has mcportal: AC2's logic verbatim, run from the main tree against this branch's manifest, printed 'descends=yes; ... changed=4, outside MP-x-1's set=0; mcportal_commit=d60b4e0 contains d60b4e0=yes' -> WOULD BE: PASS. So the issuer's own post-drain run is expected to PASS, and this refusal is scoped to running it from a linked worktree before the drain.",
        "THE SIBLING INSTANCE, same root cause, caught before it cost anything: OG-tl-1's change to deploy-to-ec2.sh added a precondition reading $WORKSPACE_ROOT/data/transcripts/scripts/teams/meeting_allowlist.json and refusing on an unreadable file. The cell's sparse list had no data/, so the deploy would have refused; it was added and the script's own expression evaluated in the worktree (4 ids, shape matches) before the act. deploy-to-ec2.sh:40-44 already carries the fallback AC2 lacks -- when the worktree's mcportal is not a repo it resolves `_main/mcportal` from `git rev-parse --git-common-dir`."
      ]
    },
    "spec_asserts": "MP-x-4 section 4 says the proof_of_spec criteria are to be run 'from your worktree root', and the cell is directed (section 1, row Z-W5-S2) to work in a linked worktree with a no-cone sparse pattern list. Together those presume the checks run correctly from a sparse linked worktree.",
    "world_is": "A check that reaches into the nested mcportal repo cannot run correctly from a linked worktree, because git checks that repo out in the main tree only -- and because the call is wrapped in 2>/dev/null it degrades to a FALSE NEGATIVE instead of an error. Separately, a no-cone sparse list silently omits paths that the deploy script and the checks read (data/transcripts/, mcportal/), so 'run it from your worktree root' is only safe once the pattern list is widened to every path the instruments touch -- which is not discoverable from the order.",
    "notes": "Issuer's call; MP-x-4 is NOT blocked, since the substance is verified and the criterion is expected to pass on the post-drain run. Per BOUNDS 3 the criterion was NOT repaired and the check was not edited (section 3 makes it read-never-write): it is REFUSED with its measurement. Options: (a) give x4.AC2.sh the same `_main/mcportal` fallback deploy-to-ec2.sh:40-44 already has -- the minimal fix, and it makes the check worktree-agnostic; (b) drop the 2>/dev/null on that call so an absent repo surfaces as an error rather than a `no`, which is the SILENCE half of the defect and worth fixing regardless of (a); (c) state in the order that this criterion is graded on the merged index by the issuer, not by the cell. Also worth landing somewhere durable: the no-cone pattern list a gateway release needs is .tools/ org/ lib/ infra/ ops/ data/transcripts/ plus the root config files, and mcportal must be reachable for AC2."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S29",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-10-09T17:23Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S28",
      "NFRA_MCPORTAL-Z-S27"
    ],
    "one_line": "Z-S28 FIXED at the check: x4.AC2.sh and r2.AC2.sh now resolve mcportal from the MAIN worktree and fail LOUD on an unreadable repo or a missing commit, instead of a 2>/dev/null false 'no'. x4.AC2 PASSES from a linked worktree. Z-S27 (cold-read margin shrinking) is confirmed by the issuer's own run, 27.4 s over 4,296 records at ~17:2xZ against the 30 s bar. It is routed as an ENRICHMENT for the next CP2/round-6 analysis (warm the body cache at boot, or more fetch threads), and it is a known risk for MP-r-2's AC3, which times three cold reads.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "x4.AC2 from C:/tmp/mp-cp2-issue (linked worktree): 'contains d60b4e0=yes ... RESULT: PASS'. r2.AC2's mcportal clause reads 'contains d60b4e0=yes' (control) and FAILs on the CP2 file set, as expected before MP-r-2.",
        "x4.AC3 ssm 2b3b0d1c-a4de-4029-93b8-c361d6c54bfc: compute_s=27.4 reporting=4 scanned=4296. The applier's series: 13.6-16.8 s at ~3,150 records (14:0xZ), 24.2 s at 4,040 (16:2xZ)."
      ]
    },
    "spec_asserts": "Z-S28: x4.AC2's mcportal clause false-negatives in a linked worktree. Z-S27: cold read under 30 s.",
    "world_is": "The check is fixed in both scripts. The cold read is still under the bar, with about 9% headroom at 17Z, and is warm-cached after the first read in the live process.",
    "notes": "Z-S27's remedy is NOT cut here: GATE (x) admits no new order into round 5 or CP2 round 1. If MP-r-2's step 2 measures over 30 s it STOPS as written, and the remedy becomes the first cell of the next round."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S30",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~MP",
    "surfaced_at": "2026-10-09T18:35Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "MP-r-2 STOPPED AT STEP 2, BEFORE THE LEDGER WAS OPENED AND BEFORE ANY DEPLOY: admin_fabric_overlap._compute(6) read 31.611 s on the gateway host, OVER the order's 30 s bar (half the ALB's 60-second idle timeout). Three cold samples: 31.611 / 24.508 / 22.333 s over 4543-4546 activity records. The other two handlers are far inside the bar -- gitstate 5.135 / 3.680 / 3.546 s, calls 0.460 / 0.427 / 0.459 s. Step 2 says any one over 30 s STOPS and the issuer re-cuts, so nothing was opened, built, uploaded or deployed.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MP",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED on the host under the instance role arn:aws:sts::313476888478:assumed-role/opal-gateway-role/i-07dccb1615503ac99 (SSM c6cc7a81-0465-42df-801a-22c71d74ce87, Status=Success), running the RELEASE's three handler modules plus app/refs/overlap_rules.json in a scratch copy of the live app/ package under the host venv /opt/opal-gateway/.venv/bin/python. Per CLAUDE.md Rule 12 the driver went local -> S3 -> host pull; no Python was inlined into an SSM command and nothing was written on the VM. THREE SAMPLES, each a FRESH INTERPRETER so each in-process cache is empty by construction.",
        "THE NUMBERS, per handler, with their denominators. overlap _compute(6): 31.611 s / 24.508 s / 22.333 s over records_scanned 4543 / 4544 / 4546, records_skipped 0 -- min 22.333, max 31.611, mean 26.151, so the WORST sample is 1.611 s OVER the bar and headroom at the worst is 0.95x. gitstate _compute(): 5.135 / 3.680 / 3.546 s, 4 boxes, worst margin 24.865 s. calls _compute('open'): 0.460 / 0.427 / 0.459 s, 4 boxes and 18 calls, worst margin 29.540 s. All three imported and ran -- this is a LOAD finding, not an import or wiring failure.",
        "IT STRADDLES THE BAR, AND THAT IS THE DANGEROUS SHAPE: 2 of 3 samples (24.508, 22.333) are UNDER 30 s. A cell that took ONE pre-act sample would have had a ~2-in-3 chance of reading a pass and shipping a page whose first open can exceed half the ALB idle timeout. The order's 'any one over 30 s' plus three samples is what caught it; a single-sample gate would not have.",
        "THIS IS Z-S27's MECHANISM, now realised on a second handler. overlap reads the SAME fabric activity store as admin_fabric over a rolling 6-hour window, and that window's record count has been climbing all day: ~3,150 at 14:0xZ, ~3,790 at 15:5xZ, 4,040 at x4.AC3 16:2xZ, 27.4 s at the issuer's x4.AC3 re-run, and 4,543-4,546 here at ~18:3xZ. The GO named this as a known risk and set the stop in advance.",
        "WHY overlap IS SLOWER THAN admin_fabric ON THE SAME STORE: admin_fabric read 24.2 s over 4,040 records at 16:2xZ while overlap reads 31.6 s over 4,543 -- consistent with the same per-record cost plus a larger record count, not with a defect unique to overlap. On that reading the two handlers will cross the bar at roughly the same store size, so fixing only overlap would leave admin_fabric a short time behind it.",
        "NOTHING WAS DONE TO THE WORLD, verified after the measurement: /opt/opal-gateway/app/admin_fabric_overlap.py still ABSENT (so the release is NOT live), service active, MainPID 864717 unchanged from MP-x-4's release, and the scratch directory removed by a trap. No ledger entry was opened for nfra-mcportal-cp2-release, no artifact was built or uploaded, and no POST was ever made to /api/admin/fabric/calls/close (BOUNDS 2 reserves the one real close for Andrew in MP-q-1).",
        "STEPS 0, 1 AND 3 ARE DONE AND HOLD, so the re-cut starts from a known-good base: step 0's route hookup is committed at 354d58bc30 on wk-mcportal-cp2-r2 with 58 of 58 admin and fabric tests passing; step 1's release tree rel-nfra-mcportal-cp2 at 74d2522f22 carries a census of exactly 8 gateway files with 0 outside infra/aws/ec2/opal-gateway and 0 .xlsx/.pptx; mcportal_commit is set to bc37107 and its own bun cache pre-check reads 77 of 77 rc=0."
      ]
    },
    "spec_asserts": "TO MP-r-2 step 2: 'Over SSM, run the release's three _compute functions ... Any one over 30 s (half the ALB's 60-second idle timeout): STOP with a BLOCKING row naming the time. The issuer re-cuts.' BOUNDS 1 adds that no handler is edited in this cell and 'a load-condition failure stops it, it does not tune.' The GO repeated it: 'A step-2 read over 30 s STOPS, as written.'",
    "world_is": "One of the three handlers is over the bar on its worst of three cold samples -- admin_fabric_overlap._compute(6) at 31.611 s against 30 s -- while the other two are far inside it. So the cell stops exactly as written, with nothing opened and nothing deployed, and the decision is the issuer's. The cause is load, not wiring: all three modules imported and returned real bodies, and the driver is the rolling 6-hour activity-store window that Z-S27 already recorded as growing through the working day.",
    "notes": "Issuer's call; this seat stops here and tunes nothing (BOUNDS 1). Options, and their costs as measured rather than guessed: (a) narrow overlap's default window, the same remedy MP-x-4's order named for admin_fabric -- note that NO cold 2-hour figure exists for either handler yet, so that needs its own fresh-interpreter measurement before it is relied on; (b) bound the work instead of the window (cap keys scanned, or paginate), the only option that does not degrade again as the store grows -- and on the per-record reading above, admin_fabric will need the same treatment within hours of overlap; (c) warm the body cache at boot, which moves the cost off the first open but not off a cold restart; (d) re-measure overnight, when the rolling window empties, and ship into the quiet period -- cheapest today and the weakest, since the bar would be breached again the next working day. Do NOT read this row as a request for an alarm or monitor: that is under a standing moratorium and needs Andrew's explicit word. The re-cut should also expect the live base to have moved again (MX-r-9 is ahead of MP-r-2 in the gateway queue). Figures and their denominators: org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/MP-r-2_PRE_ACT_RECORD.md."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S31",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~MP",
    "surfaced_at": "2026-10-09T19:41Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "EVERY .py COMMIT ON THIS DEVICE IS BLOCKED. commit-gate's ruff limb spawns ruff as `[sys.executable, '-m', 'ruff', ...]` and a Windows Application Control policy now refuses that: OSError [WinError 4551]. The ruff BINARY runs fine (ruff 0.15.11, rc=0) and the code under test PASSES the gate's exact check, so this is a failure to RUN the linter being reported as 'BLOCKED: ruff check failed' -- a failure to execute wearing the costume of a lint failure. It began within the hour: this seat's own .py commit passed the same gate at ~17:4xZ.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~MP",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "REPRODUCIBLE, twice, from worktree C:/tmp/mp-r2: `.tools/safe-commit.sh ... -- infra/aws/ec2/opal-gateway/app/admin_fabric.py` -> 'ERROR: BLOCKED -- commit-gate failed (py_compile / ruff / lint). Commit aborted; files unstaged.' with '[commit-gate] OSError: [WinError 4551] An Application Control policy has blocked this file' and '[commit-gate] BLOCKED: ruff check failed on ...'. Asked the repository rather than the output: HEAD unchanged at 04ab813b4d and the file still reads ' M' -- nothing committed.",
        "THE SPAWN PATH IS THE FAULT, read from the source: .tools/commit_gate_runner.py:145-148 runs subprocess.run([sys.executable, '-m', 'ruff', 'check', '--target-version', 'py39', '--extend-select', 'FA', target], cwd=WORKSPACE). Measured directly: `python -m ruff --version` -> the same WinError 4551, reproducibly; `ruff --version` via the binary on PATH (/c/Users/.../Python311/Scripts/ruff) -> 'ruff 0.15.11', rc=0. So ruff is installed, the pinned 0.15.11 the contract names, and executable -- only the python -m launch is refused.",
        "THE CODE IS CLEAN BY THE GATE'S OWN CRITERIA, so nothing is being hidden by the block: the gate's EXACT invocation re-run through the working binary -- `ruff check --target-version py39 --extend-select FA infra/aws/ec2/opal-gateway/app/admin_fabric.py` -- prints 'All checks passed!' rc=0. py_compile and ds-precommit are not implicated; the gate's own message lists all three ('py_compile / ruff / lint') which is why the banner has to be read past.",
        "IT IS DEVICE-WIDE, NOT THIS CELL'S. commit-gate is CLAUDE.md rule 14 and binds EVERY .py edit by every seat on this box. Any seat committing Python here right now hits it, and the message it gets points at its own code rather than at the policy.",
        "IT IS NEW, which bounds the cause: this seat committed infra/aws/ec2/opal-gateway/app/admin_api.py through the same gate at 354d58bc30 about an hour earlier and the gate printed '[commit-gate] All checks passed!' including its ruff step. So the Application Control policy, or what it admits, changed between those two commits. Nothing in this cell changed the toolchain.",
        "NO BYPASS WAS TAKEN, and none is available to this seat: safe-commit's --force covers contamination only, GIT_COMMIT_AUTHOR_OVERRIDE covers the LANE check, and neither reaches a gate refusal. Rule 14 offers no override for commit-gate, so the remedy edit stays UNCOMMITTED in the worktree rather than landing around the gate."
      ]
    },
    "spec_asserts": "CLAUDE.md rule 14: 'Every `.py` edit passes `.tools/commit-gate.sh` (py_compile + ds-precommit + ruff py39). Universal.' commit-gate.sh:47 adds 'If ruff is absent, gate exits 1 immediately (ruff is required, not optional)' -- which presumes the two states are ruff PRESENT-and-runnable or ABSENT.",
    "world_is": "There is a third state the gate does not model: ruff PRESENT and runnable as a binary, but not launchable as `python -m ruff` because an OS Application Control policy refuses it. The gate reports that as a lint failure on the author's file, so the signal points at the wrong thing. Meanwhile no .py can be committed on this device, including a load remedy the issuer ordered and whose measurement already passes its bar.",
    "notes": "Not this seat's to fix and routed accordingly; it belongs with whoever owns the toolchain on this box (0.0.0_AB_MSTR~Z holds device infrastructure; LD-0116 bars a Tier-2 seat from messaging MSTR directly, so this goes through the issuer). Options: (a) have the runner resolve the ruff BINARY (shutil.which('ruff')) and fall back to `python -m ruff`, mirroring how safe-apply resolves terraform device-agnostically -- the minimal fix, and it makes the gate work wherever ruff is installed at all; (b) add an explicit RUFF env override, same shape as SAFE_APPLY_TERRAFORM; (c) have the Application Control policy admit the launch; (d) at minimum, distinguish 'ruff could not be EXECUTED' from 'ruff REPORTED findings' in the gate's own message, because the current wording sends the author looking for a lint problem in correct code. Until one of those lands, .py work on this device cannot be committed. The MP-r-2 remedy edit (FETCH_THREADS 8 -> 32 plus a matching max_pool_connections) sits uncommitted in C:/tmp/mp-r2 on wk-mcportal-cp2-r2, with 58 of 58 tests passing and its re-measure already inside the bar."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S32",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~MP",
    "surfaced_at": "2026-10-09T19:41Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "A MEASUREMENT TRAP, caught in this seat's own driver before it reached a report: admin_fabric_overlap delegates its S3 read to admin_fabric, which caches bodies in a MODULE-LEVEL dict, so measuring admin_fabric._compute(6) and then overlap._compute(6) IN ONE PROCESS makes the second a WARM read. It read 1.490 s that way against 13.741 s cold -- a manufactured ~9x 'improvement' that would have been reported as the remedy's effect. Only the FIRST handler in a process is cold.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MP",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED BOTH WAYS on the same host, same remedied bytes, within minutes. Four handlers in ONE process (admin_fabric first): admin_fabric 13.328 / 13.582 / 13.016 s, overlap 1.490 / 1.442 / 1.378 s. One handler PER process, cache verified empty at start (body_cache_entries_at_start = 0 on all 12 samples): admin_fabric 13.345 / 13.404 / 13.828 s, overlap 13.723 / 13.741 / 13.171 s. admin_fabric is unchanged between the two shapes because it ran FIRST either way; overlap moves 1.4 s -> 13.7 s, which localises the artefact to the second-handler position, not to the handler.",
        "THE MECHANISM, read from the source rather than inferred: app/admin_fabric_overlap.py:29-30 imports admin_fabric and its constants; :91 uses admin_fabric._s3_client(); :98 admin_fabric._list_keys(); :99 admin_fabric._read_records(). _read_records fills admin_fabric._BODY_CACHE (admin_fabric.py:~56 _cache_put, CACHE_CAP 20000), a module-level dict. The two handlers read the SAME keys from the same prefix over the same window, so the first one's fetch warms essentially everything the second needs.",
        "WHY IT WAS CAUGHT RATHER THAN SHIPPED: the per-handler improvement was implausible in a way the numbers themselves exposed. The remedy raises a FETCH THREAD POOL from 8 to 32, so the ceiling on its effect is about 4x on the fetch-bound part -- but overlap appeared to improve ~21x (31.611 s -> 1.490 s) while admin_fabric, which shares the very same pool, improved only ~2x. One number moving 10x further than its own shared mechanism allows is the tell.",
        "THE EARLIER STOP IS UNAFFECTED, which matters because a cell was stopped on it: in the step-2 driver overlap ran FIRST, so its 31.611 s was a genuine cold read and row Z-S30's breach stands. gitstate and calls ran after it in that same process; they do not share admin_fabric's cache in the same way and their times are 1-2 orders of magnitude inside the bar, so nothing turns on it -- but they were not strictly cold either, and that is stated rather than glossed.",
        "A LIKE-FOR-LIKE CONTROL WAS THEN RUN so the remedy's real effect is not left to inference: the LIVE module at FETCH_THREADS=8, overlap cold in its OWN process, read 20.753 s over 4,699 records, against the remedied 13.741 s worst over ~4,697. So the honest figure is about 1.5x, not 21x. Note also that the unremedied configuration spans 20.753 s to 31.611 s at comparable record counts, so its run-to-run variance is wide and a single sample of it could land either side of the bar."
      ]
    },
    "spec_asserts": "MP-r-2 step 2 and AMENDMENT 5 require cold samples -- three fresh-interpreter cold reads of each handler -- and treat 'fresh interpreter' as sufficient for coldness.",
    "world_is": "A fresh interpreter is necessary but NOT sufficient when two handlers share a module-level cache. Coldness is per-CACHE, not per-process: the second handler in a process reads the first's cache no matter how new the process is. The rule that actually holds is ONE HANDLER PER INTERPRETER, and it is cheap to verify directly -- the driver now prints body_cache_entries_at_start, which must be 0.",
    "notes": "No action is owed by anyone; this is banked so the next cell measuring these handlers does not rediscover it. Carry-forward: measure ONE handler per process, assert the shared cache is empty at start, and treat any improvement larger than the mechanism's own ceiling as a measurement artefact until a like-for-like control says otherwise. Figures: deliverables/0.7.0_AE_CloudOps~MP/MP-r-2_PRE_ACT_RECORD.md."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S33",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-10-09T19:52Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S31",
      "NFRA_MCPORTAL-Z-S32",
      "NFRA_MCPORTAL-Z-S30"
    ],
    "one_line": "DISARMS Z-S31 for this project. The commit-gate's `python -m ruff` spawn is refused by Windows Application Control (WinError 4551), reproduced from the issuer's seat. The gate FAILS CLOSED and no bypass is taken: MP-r-2 keeps its AMENDMENT 5 edit uncommitted until the gate can execute ruff, and it waits on MX-r-9's ledger close regardless. The device and gate fault is routed to 0.0.0_AB_MSTR~Z. Z-S30 is answered: AMENDMENT 5 meets the bar, 12 of 12 cold samples at or under 30 s, max 13.828 s, a ~1.5x gain against the 8-thread control's 20.753 s. Z-S32 (a warm-cache measurement trap) is accepted; its contaminated figures were discarded by the applier.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Issuer reproduction ~19:4xZ from the shared tree: `python -m ruff --version` raises OSError [WinError 4551] An Application Control policy has blocked this file; ruff is installed at AppData/Roaming/Python/Python314/site-packages/ruff.",
        "Applier msg 32978 and MP-r-2_PRE_ACT_RECORD.md: one handler per fresh interpreter, empty cache. admin_fabric 13.345/13.404/13.828 s, overlap 13.723/13.741/13.171 s, gitstate 3.854/3.445/3.812 s, calls 0.590/0.574/0.639 s. Tests 58/58."
      ]
    },
    "spec_asserts": "Z-S31 ARMED: every .py commit on site Z is blocked by the gate's inability to run ruff. Z-S30: the overlap cold read exceeded 30 s.",
    "world_is": "Z-S31 blocks commits but corrupts nothing (fail-closed). This project holds rather than bypasses, and the owner fix is routed. Z-S30's remedy is measured and meets the tightened bar.",
    "notes": "The remedy halves the cold read but does not make it constant: the record count still grows through the day (Z-S27). A boot-time cache warm stays an enrichment for the next analysis."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S34",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~MP",
    "surfaced_at": "2026-10-09T20:03Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S31"
    ],
    "one_line": "CORRECTS Z-S31's DIAGNOSIS, which has already been routed to 0.0.0_AB_MSTR~Z. It is NOT 'python -m ruff is blocked' and NOT device-wide: Python311 `-m ruff` WORKS (ruff 0.15.11, rc=0) and only Python314 `-m ruff` is refused (WinError 4551). commit-gate.sh:59 runs `exec python ...`, and on this box `python` resolves to C:\\Program Files\\Python314 while ruff is installed for Python311. So the gate picks an interpreter whose bundled ruff.exe the policy refuses. The fix is a one-line interpreter/binary resolution, not an IT policy change.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MP",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED, both interpreters, same shell, minutes apart. `python -m ruff --version` (python -> C:\\Program Files\\Python314\\python.exe, 3.14.7) -> OSError [WinError 4551] An Application Control policy has blocked this file. `python3 -m ruff --version` (python3 -> C:\\Users\\Opal Bloomberg\\AppData\\Local\\Programs\\Python\\Python311\\python.exe, 3.11.9) -> 'ruff 0.15.11', rc=0. So the SAME `-m ruff` launch succeeds or fails purely by which interpreter runs it.",
        "THE MODULE IS PRESENT UNDER BOTH, which rules out 'not installed for 3.14' as the cause: `importlib.util.find_spec('ruff')` returns True under Python314 AND under Python311. What differs is the bundled ruff executable each site-packages carries -- the policy admits Python311's and refuses Python314's. The directly-invoked `ruff` on PATH that works is Python311's Scripts\\ruff.",
        "THE GATE'S INTERPRETER IS THE LINK, read from the source: .tools/commit-gate.sh:59 is `exec python \"$SCRIPT_DIR_WIN/commit_gate_runner.py\" \"$@\"`, and commit_gate_runner.py:145-148 then spawns [sys.executable, '-m', 'ruff', ...]. sys.executable is therefore whatever bare `python` resolved to -- Python314 here -- so the gate reaches for the one ruff the policy refuses.",
        "THIS EXPLAINS A SYMPTOM Z-S31's DIAGNOSIS DID NOT COVER, which is why it should be preferred: this seat committed a .py through the SAME gate about an hour earlier (354d58bc30, '[commit-gate] All checks passed!'). 'An OS policy changed in the last hour' had to assume an unobserved policy edit; 'bare python resolves to Python314' explains it if PATH resolution differed for that invocation, and needs no unobserved change.",
        "SCOPE IS NARROWER THAN Z-S31 CLAIMED, and the claim is retracted: Z-S31 said it blocks EVERY .py commit on this box. Measured truth is that it blocks any seat whose bare `python` resolves to Python314; a seat resolving to Python311 passes the gate. That scope is PATH-dependent per shell and was NOT measured across other seats -- Z-S31 inferred device-wide from 'OS policy', which is the wider population than the one sample supported.",
        "NOTHING ABOUT THE REMEDY OR ITS MEASUREMENT CHANGES: AMENDMENT 5's bar is still met (12 of 12 cold samples, max 13.828 s), the file still passes ruff's exact check through the working binary, the edit is still UNCOMMITTED with no override taken, and the issuer has ruled it stays that way until the gate can execute ruff."
      ]
    },
    "spec_asserts": "Z-S31 asserted that commit-gate's ruff limb cannot execute because 'a Windows Application Control policy now refuses `python -m ruff`', and that the block reaches every .py commit on this device.",
    "world_is": "The refusal is interpreter-specific, not launch-mode-specific: Python311's `-m ruff` runs and Python314's does not. commit-gate's bare `python` is Python314 on this box, so the gate alone trips it while a hand-run ruff succeeds. The blast radius is every seat whose `python` resolves to Python314, which is a PATH property of each shell rather than a property of the device, and it was not measured outside this session.",
    "notes": "Routed for 0.0.0_AB_MSTR~Z, who already holds Z-S31 -- this row is the correction that makes it cheap to fix. Preferred fix, smallest first: (a) have commit_gate_runner resolve the ruff BINARY (shutil.which('ruff')) and only fall back to [sys.executable, '-m', 'ruff'], exactly how .tools/safe-apply.sh resolves terraform device-agnostically -- one function, and it makes the gate correct wherever ruff is installed at all; (b) add a RUFF env override, same shape as SAFE_APPLY_TERRAFORM; (c) pin commit-gate.sh:59 to the interpreter that owns the pinned ruff (python3 / Python311 here) rather than bare `python`, which also removes the silent dependence on PATH order; (d) independently of all three, make the gate distinguish 'ruff could not be EXECUTED' from 'ruff REPORTED findings' -- the present wording, 'BLOCKED: ruff check failed on <file>', sends the author looking for a lint problem in correct code, and that is the part that cost this cell the most time. An IT policy change is NOT needed for any of (a)-(d)."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S35",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-10-10T21:45Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S34",
      "NFRA_MCPORTAL-Z-S31"
    ],
    "one_line": "DISARMS Z-S34 for this project, and narrows its diagnosis. The ruff refusal is INTERMITTENT, not deterministic per interpreter: Python314 `-m ruff --version` was refused once at 20:57Z and then read rc=0 in 6 of 6 runs from the same seat minutes later. `.tools/commit-gate.sh` passed the AMENDMENT 5 file (clean 1 of 1, rc=0), and the applier committed it through the gate @ea58e3662d with no override. MP-r-2 is no longer blocked by the toolchain; it waits only on MX-r-9's ledger close.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED 2026-10-10 ~20:57Z, issuer seat, shared tree: `python -m ruff --version 2>&1 | head -2` printed a Traceback (`<frozen runpy>` line 203). Bare `ruff --version` (Python311 Scripts) read 'ruff 0.15.11'.",
        "MEASURED ~21:0xZ, the same seat: `python` -> C:\\Program Files\\Python314\\python.exe. `python -m ruff --version` read 'ruff 0.15.11' rc=0 in 6 of 6 runs (5 looped, 1 piped). Python311 `-m ruff` read 'ruff 0.15.11'.",
        "MEASURED ~21:0xZ in C:/tmp/mp-r2: `bash .tools/commit-gate.sh infra/aws/ec2/opal-gateway/app/admin_fabric.py` -> 'All checks passed!' and 'OK: pre-commit gate clean for 1 of 1 file(s)', rc=0.",
        "git -C C:/tmp/mp-r2 log: ea58e3662d (0.7.0_AE_CloudOps~MP, 17:13:54 -0400) fix(... MP-r-2 AMENDMENT 5 ...); the worktree is clean afterwards."
      ]
    },
    "spec_asserts": "Z-S34: Python314's bundled ruff is refused by Application Control and Python311's is admitted, so a gate whose bare `python` is Python314 always fails.",
    "world_is": "The same Python314 `-m ruff` launch failed once and passed 6 times within about 10 minutes. The refusal is a time- or state-dependent property of the policy or its cache, not a fixed property of the interpreter. This also explains Z-S34's own unexplained symptom (354d58bc30 passed the same gate an hour before the refusal) without needing a PATH difference.",
    "notes": "No act owed by this project. Z-S34's fix (a), resolving the ruff binary before falling back to `-m ruff`, still reduces exposure and stays with 0.0.0_AB_MSTR~Z as gate owner. Z-S34(d), telling 'could not EXECUTE ruff' apart from 'ruff REPORTED findings', is the part that matters for an intermittent fault: on a refusal, re-run once before you look for a lint defect."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S36",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.7.0_AE_CloudOps~MP",
    "surfaced_at": "2026-10-10T21:31:53Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S35",
      "NFRA_MCPORTAL-Z-S34",
      "NFRA_MCPORTAL-Z-S31"
    ],
    "one_line": "CORROBORATES Z-S35 on a wider denominator and adds the part neither prior row has: the refusal is recorded in NEITHER Windows log, so an empty event log CANNOT grade the fix. Python314 `-m ruff --version` read rc=0 in 20 of 20 trials -- superseding Z-S35's 6 of 6 and finishing the falsification of Z-S34's interpreter-split mechanism -- Python311 20 of 20, and the real `.tools/commit-gate.sh` on the AMENDMENT 5 file 5 clean of 5. Over the 1,185 `Microsoft-Windows-CodeIntegrity/Operational` events spanning the whole 30-hour refusal window, 0 name ruff or python. Whoever grades 0.0.0_AB_MSTR~Z's fix must grade it by EXECUTING ruff over a printed denominator, never by reading these logs.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED 2026-10-10 21:1x-21:2xZ, applier seat, each figure beside its denominator: `python -m ruff --version` under C:/Program Files/Python314/python.exe (3.14.7, what bare `python` resolves to here) -> 20 rc=0, 0 WinError 4551, DENOMINATOR 20. Under Python311 -> 20 rc=0, 0 WinError 4551, DENOMINATOR 20. So the interpreter is NOT the discriminator, and Z-S34's deterministic mechanism is falsified on the very interpreter it named.",
        "THE REAL CONSUMER, not a proxy: `bash .tools/commit-gate.sh infra/aws/ec2/opal-gateway/app/admin_fabric.py` run 5 times in C:/tmp/mp-r2 -> 5 rc=0, 0 refusals, DENOMINATOR 5. The gate is what Rule 14 binds, so it is the oracle; `-m ruff --version` alone is only its precondition.",
        "THE INSTRUMENT DOES NOT SEE THIS FAULT, which is the reusable finding. `Microsoft-Windows-CodeIntegrity/Operational` over the 30 hours from 2026-10-09 15:22Z (spanning the first refusal ~2026-10-09 20:0xZ, the 20:57Z refusal and the clean window): 1,185 events, 790 Id=3089 and 395 Id=3033, and 0 of 1,185 name ruff or python. The 395 Id=3033 blocks are ALL SentinelOne's `SentinelAmsi64.dll` refused into `svchost.exe` with status 0xC0000428 -- a separate standing condition, not this fault and not this project's to own.",
        "THE SECOND LOG IS ALSO SILENT: `Microsoft-Windows-AppLocker/EXE and DLL` holds only Id=8001 policy-application notices (2026-10-10 20:49:42Z, 2026-10-09 07:01:06Z, 2026-10-08 20:58:15Z) and no block event; `AppLocker/MSI and Script` returned no events at all. So BOTH candidate instruments read clean while the fault WAS occurring.",
        "ONE CORRELATE, NAMED AS A CORRELATE AND NOT A CAUSE: the AppLocker policy application at 2026-10-10T20:49:42Z sits 8 minutes before the last observed refusal (20:57Z) and ~13 minutes before the clean window. But the ONSET -- between 354d58bc30 passing the gate and the 2026-10-09 20:0xZ refusals -- has NO corresponding event in either log, so the pair is a coincidence in time and not a mechanism. Stating it as a cause would be the error this row exists to prevent.",
        "DOWNSTREAM STATE, measured not assumed: the AMENDMENT 5 remedy is committed @ea58e3662d through safe-commit with no override, the suite at the committed bytes read 58 passed / 0 failed, and the cell's record is superseded in place @73547dcfd1 (`deliverables/0.7.0_AE_CloudOps~MP/MP-r-2_PRE_ACT_RECORD.md`). Nothing was deployed: live `FETCH_THREADS` is still 8 and no entry exists for slug `nfra-mcportal-cp2-release`."
      ]
    },
    "spec_asserts": "A Windows Application Control refusal of an executable is recorded by the OS, so the code-integrity and AppLocker logs can be read to confirm whether the fault is still occurring -- and an empty log over the window grades it absent.",
    "world_is": "Neither log recorded it. 0 of 1,185 CodeIntegrity events over the 30-hour window naming ruff or python, and no AppLocker block event, while the fault demonstrably occurred twice inside that window (2026-10-09 ~20:0xZ and 2026-10-10 20:57Z). A clean log here is an ABSENT reading from an instrument that cannot see the object, which is not a negative -- the exact shape CLAUDE.md's ABSENT != EXERCISED-AGAINST corollary names.",
    "notes": "No act owed by this project; MP-r-2 waits on MX-r-9's ledger close alone. For 0.0.0_AB_MSTR~Z as gate owner: (1) grade any fix by EXECUTING ruff N times with N printed, never by reading the event logs, because this row shows they are blind to it; (2) a non-reproduction over 45 clean trials is NOT a fix -- the fault's rate is unmeasured at the low end and one refusal in seven was real an hour earlier; (3) under an INTERMITTENT fault, Z-S34's fix (d) -- telling 'ruff could not be EXECUTED' apart from 'ruff REPORTED findings' -- is worth more than before, because the correct response to a refusal is to re-run once, and the present wording sends the author hunting a lint defect in correct code instead. Fix (a), resolving the ruff BINARY before falling back to `-m ruff`, still reduces exposure and costs one function."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S37",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-10-11T14:15Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S27"
    ],
    "one_line": "The live Git state handler's cold read is climbing steadily toward R-13's 30 s bar: 3.854 s (2026-10-09), 10.586 s (2026-10-10 23:0xZ, at MP-r-2's act) and 16.7 s now (2026-10-11 14:1xZ, r2.AC3 on the live host). Its population, git history across boxes, does not drain overnight the way the activity store does, so the margin does not reset. At about 6 s per day it reaches 30 s in roughly 2 days. No breach today. The other three surfaces hold: overlap 6.8 s, calls 0.4 s, boxes covered by AMENDMENT 5.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED 2026-10-11 ~14:1xZ: `bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/r2.AC3.sh` -> ssm f869ff97-830c-43f0-987f-6652d2a4042a Success; /health 200; overlap/gitstate/calls/close(POST) all 401 with no identity; overlap_s=6.8, gitstate_s=16.7, calls_s=0.4; RESULT: PASS.",
        "PRIOR POINTS: 3.854 s, the A5 re-measure, MP-r-2_PRE_ACT_RECORD.md (2026-10-09); 10.586 s at the act, EC2_MANIFEST opal-gateway release_note @9a072fa60a (2026-10-10 23:0xZ). Three cold reads, each one sample; different instruments (cold-interpreter host probe vs the AC3 probe), so this is a trend in sign, not a precise rate.",
        "CP2 SURVIVED TWO LATER RELEASES: the live deployed_commit c3af8687e4 (MX-r-10, 2026-10-11T13:27:13Z, over E2 6aadf7db37) descends from 2a5966dfbd, and all 6 CP2 gateway files have the same blob at c3af8687e4 and 2a5966dfbd. So the rise is not a code change to the handler."
      ]
    },
    "spec_asserts": "R-13: every Control Plane surface's cold read stays at or under 30 s. MP-r-2 met it at the act (all eight samples at or under 10.6 s).",
    "world_is": "Today it holds (16.7 s), but the Git state read grows with an undrained population and has risen about 4x in two days. It is the surface most likely to breach the bar next, and AMENDMENT 5's thread-pool remedy covers the activity fetch path, not this one.",
    "notes": "For the next round-N analysis (the CTO's enrichment list): the candidates are a bounded window on the git-state population, a boot-time cache warm, or a per-box incremental index. No act is owed now. The issuer re-reads r2.AC3 at each Andrew-gated close run (MP-q-1) and adds a row if a sample passes 25 s."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S38",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-10-12T08:30Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S37"
    ],
    "one_line": "Z-S37's 25 s trigger has fired: the live Git state cold read was 25.1 s at 08:29Z, against R-13's 30 s bar (21.8 s about 4 h earlier, 16.7 s on 10-11, 10.6 s on 10-10, 3.9 s on 10-09). It keeps rising overnight. Overlap fell from 11.8 s to 2.2 s over the same night (its activity population drains daily), so this is specific to the git-state population. A breach of the bar is now likely within hours, not days.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MP",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED 2026-10-12 08:29Z: `bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/r2.AC3.sh` -> ssm e8db49fd-bf2d-4bb5-af89-e8ee744e869d Success; /health 200; all four routes 401 with no identity; overlap_s=2.2, gitstate_s=25.1, calls_s=0.6; RESULT: PASS.",
        "MEASURED ~04:3xZ the same day, same check: gitstate_s=21.8, overlap_s=11.8 (live deployed_commit 28ba9532b6, which descends from 2a5966dfbd; all 6 CP2 files are the same blob).",
        "The handler code is unchanged since MP-r-2 (blob equality above), so the growth is in the data, not the code."
      ]
    },
    "spec_asserts": "R-13: every Control Plane surface's cold read stays at or under 30 s.",
    "world_is": "Git state is at 25.1 s and rising about 1 s per hour over the last read pair. AC3 still passes, but the bar is close to breaching for the FWD-16 surface. Nothing is broken today: the read completes and the page renders.",
    "notes": "BLOCKING for FWD-16's R-13 at the next close run (MP-q-1), INERT now (no wrong output, only latency). The remedy is a code change to admin_fabric_gitstate.py: a bounded window, an incremental index, or a boot-time warm. That is an amendment-class change to a COMPLETE order and a new cell, so it needs the CTO's round-N analysis, not an issuer amendment. Routed there as the first enrichment item. No act is taken at this seat; the deploy queue is not touched."
  },
  {
    "id": "NFRA_MCPORTAL-Z-S39",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MP",
    "surfaced_at": "2026-10-12T09:10Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_MCPORTAL-Z-S38",
      "NFRA_MCPORTAL-Z-S37"
    ],
    "one_line": "DISPOSES Z-S38 and Z-S37 to an issued remedy. 1.0.0_SA_CTO~Z ruled an addendum now (msg 33458; PRD v0.6 C17 @fc09ade4ea, the bounded git-state read). The issuer cut ONE cell, MP-n-1, to 0.7.0_AE_CloudOps~MP: decomposition @6e73fee848, order @f8ee9e7453, workstream C17 round 1, GO by message. The cause, read at HEAD, is that _refused() scans the whole history when no refusal exists: 2,771 body fetches and 22.8 s on the served code.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "n1.AC3 dry run on the served 28ba9532b6, 2026-10-12 ~08:5xZ: ssm aeb096c6-ae4c-442b-999c-2ac14da5dab4 Success; /health 200; no-identity gitstate 401; gitstate_s=22.8 body_fetches=2771 recorded=4; RESULT: FAIL (bar 10 s).",
        "n1.AC1 at HEAD: history 1x=240 10x=2400; get_object 1x=242 10x=2402; FAIL. On the issuer's scratch C17 sketch: 98 vs 98; PASS.",
        "n1.AC2 at HEAD: the superseded refusal is shown; FAIL. On the sketch: 'not recorded' and {at, note}; PASS."
      ]
    },
    "spec_asserts": "Z-S38: FWD-16's cold read is near R-13's 30 s bar with no remedy in flight.",
    "world_is": "A remedy is in flight under C17 with a 10 s bar. The checks discriminate at HEAD, and AC1/AC2 have a positive control. The served read stays near 23-25 s until MP-n-1 releases; per C17's interim note, only the first read after a restart is cold.",
    "notes": "Known risk, carried in the order: the 48 h window holds about 2,000 records. Whether the early stops keep the cold read under 10 s depends on how often integrate passes and trunk moves occur; MP-n-1's step-2 load sample measures it before the cutover."
  },
  {
      "id": "NFRA_MCPORTAL-Z-S40",
      "project": "NFRA_MCPORTAL",
      "fabric": "site-z",
      "surfaced_by": "0.7.0_AE_CloudOps~MP",
      "surfaced_at": "2026-10-12T09:50:32Z",
      "disposition": "UNDER_INVESTIGATION",
      "one_line": "MP-n-1 STOPS AT STEP 2, as the order requires. C17 is built, committed @39ae93a10f, and does what it claims -- AC1 reads get_object 98 vs 98 while planted history grows 240 -> 2400, so the cold read no longer grows with HISTORY length -- but the pre-cutover load sample of the release module on the host reads 16.661 s with 1,346 body fetches against the order's 10 s bar. The binding constraint has MOVED, from history length to the WINDOW'S OWN POPULATION: the 48 h window holds 2,134 records across the 4 boxes (laptop 800, dell1 468, dell2 456, sitez 410) out of 3,329 total history. Nothing was uploaded, no ledger was opened, and BOUNDS 2 forbids tuning further in this cell, so the re-cut is the issuer's.",
      "class": "BLOCKING",
      "hazard_standing": "INERT",
      "disarm_owner": "2.0.0_SA_COO~MP",
      "grounding": {
          "status": "GROUNDED",
          "evidence": [
              "THE SAMPLE, measured on the host under the instance role against the LIVE store, on the RELEASE bytes and not the served ones: gitstate_s=16.661 body_fetches=1346 list_calls=4 boxes=4 recorded=4 refusals=0 basis_fields=4 cache_at_start=0. SSM ec31a13d-d80e-4ece-8e07-66c76235312c, Status=Success. The probe shipped local -> S3 -> host pull per Rule 12 and its bundled module was md5-checked on the host against the release tree before timing (afe21be4beae both sides), beside the SERVED module's contrasting md5 09b8631aed0c, so the sample provably timed the bytes about to ship.",
              "cache_at_start=0 was ASSERTED, not assumed: the probe exits 3 and declares the sample VOID rather than reporting a fast read if the body cache is non-empty (row NFRA_MCPORTAL-Z-S32, coldness is per-CACHE not per-process). So 16.661 s is a cold number.",
              "C17 DID WORK, and the row says so because a bare failure would read as a broken change: the issuer's pre-C17 dry run on served code 28ba9532b6 read 22.8 s with 2,771 fetches; the release reads 16.661 s with 1,346. Fetches fell 51 percent and the time 27 percent. AC1 and AC2 both PASS exit=0 at the committed bytes, and the whole admin and fabric suite reads 62 passed / 0 failed.",
              "THE WINDOW POPULATION IS THE NEW FLOOR, counted directly from the store rather than inferred -- list-objects-v2 per box, auto-paginated, counted client-side: laptop history 1,347 of which 800 inside 48 h; sitez 614 / 410; dell1 687 / 468; dell2 681 / 456. TOTAL history 3,329, IN WINDOW 2,134, with 4 of 4 boxes listed and answering. The sample's 1,346 fetches are 63 percent of that window, so the early stops ARE firing -- an unbounded-within-window read would have fetched about 2,134 -- and even so the remaining work exceeds the bar.",
              "WHICH SCAN DOMINATES, localised rather than guessed: the sample reports first_seen=2026-10-12T09:42:18Z, about one minute before the read, so the trunk head had just moved and the first-seen scan stopped almost immediately on every box. The cost is therefore `_refused` walking each box's window looking for an integrate pass, and refusals=0 means no box reported one. At 1,346 fetches in 16.661 s the rate is about 12.4 ms per fetch, so the 10 s bar corresponds to roughly 800 fetches -- a 1.7x gap that the producers' write rate, not the handler, now sets. laptop alone writes 800 records per 48 h, one every 3.6 minutes.",
              "THIS IS THE ISSUER'S OWN NAMED RISK, now measured rather than carried: the order's record face says 'inside the 48 h window the producers write about 2,000 records across 4 boxes. Whether the early stops keep the cold read under 10 s depends on how often integrate passes and trunk moves occur. Step 2's load sample measures it before the cutover.' The answer is no, and the figure it turns on is 2,134 window records against an estimate of about 2,000.",
              "NOTHING WAS PUT IN THE WORLD. No artifact was uploaded, no ledger entry was opened, no sentinel was written, the host still runs 28ba9532b6 (confirmed by md5, 100 of 100 app files equal, with a negative control at 2a5966dfbd reading 7 different and 2 host-only), and the never-widen ASK was NOT written because step 2 stops the cell before step 3."
          ]
      },
      "spec_asserts": "MP-n-1 step 2: the release's admin_fabric_gitstate._compute(), sampled cold on the host before the cutover, reads at or under 10 s; over 10 s STOPS the cell with a BLOCKING row naming the time and the count. BOUNDS 2 adds that a step-2 load failure after the C17 change stops the cell rather than tuning further.",
      "world_is": "16.661 s with 1,346 body fetches: over the bar by 6.661 s, so the cell stops here. C17's own claim is nevertheless met -- the read no longer grows with history length, which AC1 proves at 98 fetches against a tenfold history -- and what remains is a different constraint the order's bar did not separate from it: the 48 h window holds 2,134 records, and reading even 63 percent of them costs more than 10 s.",
      "notes": "For 2.0.0_SA_COO~MP as disarm owner, four options with their measured cost, none of them an alarm (which is under moratorium), and this seat recommends none without the issuer's ruling because BOUNDS 2 reserves the re-cut. (a) NARROW THE WINDOW: WINDOW_HOURS 48 -> 12 would cut the population roughly fourfold on the observed write rate and is a one-constant change, but it narrows what integration_refused and first_seen can see, which the basis fields would then have to state. (b) RAISE THE BAR to a figure the window population supports, which is a PRD question and not a code change -- the served read is 16.7 s against an ALB idle timeout of 60 s, so 10 s was a margin choice rather than a hard limit. (c) STOP _refused EARLIER by a cheaper oracle than a body read: the producer could write a per-box pointer object naming its newest integrate pass, turning that scan from O(window) into one get_object -- the largest win and the only option that touches .tools/fabric-gitstate.py, which this order's BOUNDS 1 forbids this cell from touching. (d) WIDEN FETCH_THREADS, which the order explicitly freezes and which trades latency for connections rather than removing work. Independently of the choice: the 12.4 ms per fetch rate and the 2,134-record window are the two numbers any re-cut should be graded against, and both are in this row so the next cell does not have to re-measure them."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W24-S1",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~24",
    "surfaced_at": "2026-10-14T17:04:53Z",
    "one_line": "schwab_entitlement_admin.py has no read or show subcommand: its subparsers are activate, revoke and deny-backfill only, so the pc6 'read/show subcommand' for a principal's ACTIVE grant does not exist; the grant was read by a raw store get instead.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py at a9ff37d082: _build_arg_parser (lines 440-465) registers sub.add_parser for 'activate', 'revoke' and 'deny-backfill' only; main() dispatches those three and no read path.",
        "SSM command 9f354b62-a3d5-40b9-9d2d-07003983a79d on i-07dccb1615503ac99 read the profile and grant records with app.access_state AccessState.get (probe deliverables/0.9.0_WK_NFRA_MCPORTAL~24/pc6_probe.py; output pc6_served_probe_stdout.txt)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The operator entitlement command ops/schwab_entitlement_admin.py exposes a read/show subcommand that reads a principal's ACTIVE grant from the store, for the MP-pc-6 independent store read.",
    "world_is": "The command exposes no read-only subcommand; every subcommand is a write through access_state.operator_transact. A grant can be inspected only through app.data_entitlement and app.access_state reads, which the probe used directly."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W24-S2",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~24",
    "surfaced_at": "2026-10-14T17:04:53Z",
    "one_line": "The worker holds no operator identity: the pc6 store read ran under the host's gateway instance role (the role the served page reads with), not the operator role opal-gateway-access-admin that the entitlement command's header requires.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py check_operator_identity (OPERATOR_ROLE_NAME = opal-gateway-access-admin) refuses any other caller identity, including opal-gateway-role.",
        "SSM command 9f354b62-a3d5-40b9-9d2d-07003983a79d ran as ec2-user under the instance role (the pc5 probe pattern); the store side is read by AccessState.get, not by the page's current_access path, but through the same identity."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The independent read of the principal's ACTIVE grant runs under the operator role opal-gateway-access-admin through the existing operator read path, so the store side is read by an identity other than the served page's.",
    "world_is": "The only identity the worker can reach is the host instance role. The store side is independent of admin_people._compute's logic and its current_access call, but it shares the served page's identity and store client."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W24-S3",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~24",
    "surfaced_at": "2026-10-14T17:21:27Z",
    "one_line": "The close run's proof flip (<status> to complete on NFRA_MCPORTAL.TO-MP-pc-6) names the task-order file, which is outside this worker's <paths>, so the flip is not made on this branch.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pc-6.fwd21-read-close-run.md at a9ff37d082 names <paths> = deliverables/0.9.0_WK_NFRA_MCPORTAL~24/** and surprise-channel/investigations/** only; the order file itself carries <status>pending</status>.",
        "AC1 PASS (pc6.AC1.sh exit=0) and the instance validates rc=0, so the only open step is the status flip."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "On PASS the proof-of-spec instance is committed together with the task order's <status> flipped to complete.",
    "world_is": "The task-order file is not in this worker's write grant (the deliverables folder and the investigations folder only), so the worker does not edit it. The order stays pending on wk-NFRA_MCPORTAL-pc-24 and the issuer owns the flip."
  }
]
```

```json
{
  "id": "NFRA_MCPORTAL-Z-S41",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-13T01:05Z",
  "one_line": "MCPORTAL deep links are 404 on a direct load or refresh: the gateway serves the dashboard bundle only at '/' and '/assets/{path:path}' (server.py:1155-1156), but the bundle's router uses path routes (/control-plane, /open-calls), so a URL Andrew is given cannot be opened directly.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "spec_asserts": "An open call's URL (https://mcp.opalinvest.dev/control-plane, /open-calls) opens the page it names.",
  "world_is": "Andrew opened both URLs from open calls 21c5 and 8ed7 and got 404 (1.0.0_SA_CTO~Z msg 33520). Read by the CTO at served release 185dc04888, and at 1e32562729, 2a5966dfbd and 28ba9532b6: no route serves index.html for a bundle path. Re-read by this seat at box/sitez HEAD: server.py:1155 Route('/assets/{path:path}') and :1156 Route('/'), and no other route returns the bundle. Unauthenticated, every path (including /no-such-route-xyz) answers 302 to sign-in, so this seat could not reproduce the 404 behind the login; the defect is grounded on the code read and Andrew's own load.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/opal-gateway/app/server.py:315-348 and :1147-1156 at HEAD",
      "1.0.0_SA_CTO~Z msg 33520 (Andrew's 404; the code read at four releases)",
      "curl, unauthenticated, 2026-10-13 ~01:0xZ: '/', '/control-plane', '/open-calls', '/no-such-route-xyz' all 302"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "CTO ruling (msg 33520): the FWD-20 issuance carries one cell, an owner-gated route serving index.html for each path in the bundle's route list (an unknown path still 404s), with a test of each. Interim: open https://mcp.opalinvest.dev/ and use the menu. Filed by the CVO on the CTO's 'File the row'."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W15-S1",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~15",
  "surfaced_at": "2026-10-13T10:43:57Z",
  "one_line": "The ordered catch-all Route('/{path:path}') after Mount('/mcp') would have swallowed Starlette's redirect_slashes (bare /mcp 307 to /mcp/); the handler replays it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Order section 1: the catch-all placed last 'shadows no existing route'; only a path nothing else matches reaches it.",
  "world_is": "Starlette redirect_slashes fires only when NO route matches. Mount('/mcp') matches '/mcp/...' only, so bare '/mcp' had no match and was redirected 307 to '/mcp/'. A catch-all matches it fully, so first run of the order's own test (/mcp resolving to the mcp app) failed: /mcp resolved to the catch-all, which would have answered 404 to any client posting to bare /mcp. Handled inside the ordered handler (server.py dashboard_deep_link): for an unlisted path it tries the alternate trailing-slash form against every other route and answers 307 if one fully matches, else the plain 404. Test test_existing_routes_keep_their_endpoint asserts /mcp/ resolves to mcp_app and bare /mcp yields 307 to /mcp/ (direct handler call, because GuardMiddleware answers 401 to an unauthenticated /mcp). Order criterion text left as written; the 'resolve /mcp' arm uses /mcp/.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/opal-gateway/app/server.py dashboard_deep_link at e42d2c35c3",
      "pytest run before the redirect replay: AssertionError /mcp resolved to Route('/{path:path}', name='dashboard_deep_link')"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W15-S2",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~15",
  "surfaced_at": "2026-10-13T11:16:15Z",
  "one_line": "Starlette Route(path, func) with no methods= defaults to GET+HEAD only, so 'accept every method' needs an explicit list.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "AMENDMENT 1: 'Route(\"/{path:path}\", dashboard_deep_link) with no methods= (or the full method list)' accepts every method.",
  "world_is": "A function endpoint with methods=None gets methods {GET,HEAD}; POST /no-such-page through TestClient answered 405 while the direct handler call answered 404 (first run: 6 of 7). Fixed in app/server.py by the explicit list GET,HEAD,POST,PUT,PATCH,DELETE,OPTIONS, the 'full method list' alternative the amendment names. A direct-handler-only test would not have seen it, so test_unknown_path_any_method_404 also drives the real client.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "pytest run before the fix: assert 405 == 404 at test_unknown_path_any_method_404 via app_mods.client.post",
      "infra/aws/ec2/opal-gateway/app/server.py Route list in the worker commit"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W13-S1",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~13",
  "surfaced_at": "2026-10-13T10:55:17Z",
  "one_line": "MP-z-1 premise: the order names MASTER_ADMIN_EMAILS and WRITE_CAPABLE_EMAILS as the holders of the master-admin and write-capable tiers, but tier.resolve_tier never reads them; a person's tier is keyed on MASTER_ADMIN_PRINCIPALS and WRITE_CAPABLE_PRINCIPALS (tid/oid), so an address in an email roster resolves to read_only through the real chain.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "MP-z-1 section 1: candidates are every address in config.MASTER_ADMIN_EMAILS and config.WRITE_CAPABLE_EMAILS, with the tier taken from tier.resolve_tier and the chain called for each; the 'how' basis reads 'master admin (MASTER_ADMIN_EMAILS)' / 'write-capable (WRITE_CAPABLE_EMAILS)'.",
  "world_is": "app/config.py:320-323 states the two EMAIL rosters are 'NOT persons' tier and are NEVER read by tier.resolve_tier'; they feed token_broker._machine_tier only (machine identities). tier.resolve_tier(principal, cfg) reads MASTER_ADMIN_PRINCIPALS / WRITE_CAPABLE_PRINCIPALS by principal.key and returns READ_ONLY for a request with no principal. tools._run and run_integration_tool also deny every tool at data_entitlement.tool_denial ('principal_required') when no principal is set. So an email-only candidate cannot be evaluated as master admin by calling the chain, and calling it faithfully (as an unprofiled signed-in person with that display email) gives it exactly the population row's tools. The page still lists the email rosters as the order says, with that stated in holders_basis, and ADDS the two principal rosters as candidates (labelled 'master admin (MASTER_ADMIN_PRINCIPALS)' / 'write-capable (WRITE_CAPABLE_PRINCIPALS)'), because they are the rosters that actually raise a tier; an email roster entry equal to a known principal's profile email joins that principal's row. No chain function was re-typed and no gateway module was edited. Also not counted, stated in holders_basis: a client-qualified identity_scope row (admits only a request from its registered OAuth client, unknowable here).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/opal-gateway/app/config.py:298-333 and app/tier.py resolve_tier (steps 2-5) at 233e78932a",
      "infra/aws/ec2/opal-gateway/app/token_broker.py:162-177 _machine_tier is the only reader of the two email rosters",
      "tests/test_admin_gateway_breakdown.py::test_holders_match_the_dispatch_chain: ROSTER_ONLY address holds exactly the population set on both sides, while the same address's principal in MASTER_ADMIN_PRINCIPALS holds send_email and schwab_query"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "For 2.0.0_SA_COO~MP: the page-building cell (and the PRD wording of 'who holds what') should say the person tier comes from the principal rosters. If the intent was that the email rosters raise a person's tier, that is a gateway change (app/tier.py), outside this cell's paths."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-S42",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~MQ",
  "surfaced_at": "2026-10-13T14:01:14Z",
  "one_line": "MP-z-4 step 2 says 'run the plan with safe-apply', but .tools/safe-apply.sh gates the apply subcommand ONLY and REFUSES any invocation without the literal word 'apply' (rc=2), so a plan cannot be run through it; the same wording is likely in the sibling GW orders.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "spec_asserts": "NFRA_MCPORTAL.TO-MP-z-4 section 1 step 2: 'Run the plan with safe-apply, targeted to aws_iam_role_policy.gw_access_state_principal_scan only.'",
  "world_is": "Measured in worktree C:/tmp/mp-mq-z4: `.tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway plan -target=aws_iam_role_policy.gw_access_state_principal_scan` exits rc=2 with 'safe-apply: ERROR -- no safe-apply subcommand in the arguments. this wrapper gates terraform apply only. For plan or any other subcommand call the terraform binary directly. usage -- safe-apply.sh [-chdir=DIR] apply [apply-args...]'. The wrapper's own header says the same: 'Gates apply ONLY. plan and other subcommands are non-destructive -- call terraform.exe directly for those.' The plan was therefore run on the terraform binary directly (rc=0, 1 to add / 0 to change / 0 to destroy) and the APPLY will go through safe-apply, which is the gated step Rule 18 exists for. NOTHING IS LOST by this -- safe-apply's HALT-gate fires immediately before the irreversible apply, which is where the order wants it; only the order's sentence is unrunnable as typed.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/safe-apply.sh header lines 16-19 and the has_apply loop at :57-64, box/sitez HEAD 6fe140d0a8",
      "measured invocation 2026-10-13 ~13:0xZ in C:/tmp/mp-mq-z4: rc=2, the four-line refusal quoted above",
      "the same command with `apply` and the saved plan is the act step 4 of the order prescribes"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "For 2.0.0_SA_COO~MP: a one-word amendment ('run the plan with terraform directly; the APPLY goes through safe-apply') makes the step runnable as typed. Check TO-MP-z-5 for the same sentence before its GO. No criterion is affected -- neither z4.AC1.sh nor z4.AC2.sh reads how the plan was invoked."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-S43",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~MQ",
  "surfaced_at": "2026-10-13T14:01:14Z",
  "one_line": "The NO-CONE sparse pattern list MP-z-4 prescribes (.tools/, org/, lib/, infra/aws/terraform/opal-gateway/) cannot plan OR commit a gateway .tf: four separate fail-closed refusals, each naming one more absent path, cost four round-trips before the commit landed.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "spec_asserts": "NFRA_MCPORTAL.TO-MP-z-4 section 1: 'Work in a linked worktree you cut from box/sitez HEAD (CLAUDE.md 14b), with the NO-CONE sparse pattern list that worked for MP-k-2 (.tools/, org/, lib/, infra/aws/terraform/opal-gateway/).'",
  "world_is": "That list is sufficient for an org/-only or lib/-only cell (MP-k-2 wrote an S3 grant whose gates never walked the terraform declaration tree) and insufficient for ANY cell that plans or commits a .tf under infra/aws/terraform/. Measured in order, each failing CLOSED and naming exactly what it wanted: (1) lib/opal_naming.py name() raised FileNotFoundError on infra/logic/registry/systems.json -- the builder's registry is NOT under lib/; (2) terraform init: 'Unreadable module directory ... ..\\modules' x5 -- infra/aws/terraform/modules/ is a sibling of the opal-gateway dir and is not matched by the opal-gateway pattern; (3) commit-gate: 'config not found: comp-constants.config.yaml' -- the root-level tracked blobs are not matched by any directory pattern; (4) the LGIC naming limb's PLACEMENT step raised FileNotFoundError twice, first on infra/aws/lambda/ci/lambda-source-map.json and then on infra/aws/terraform/49f-value-parity/49f_value_parity.tf, because it walks the WHOLE declaration tree, not the staged paths. The NAME itself graded CONFORMANT on the first attempt that reached it, so none of the four was a verdict about the change. The working list adds: /infra/logic/, /infra/aws/terraform/ (whole, 757 files -- not just opal-gateway/ and modules/), /infra/aws/lambda/ci/, /infra/aws/ec2/EC2_MANIFEST.json, /infra/aws/lambda/mcportal/ (the plan-time data.external grant-writer build), and the 12 root-level tracked blobs (.gitattributes .gitignore .gitmodules .mcp.json .owned-paths.yaml AGENTS.md CLAUDE.md README.md ajb.ps1 comp-constants.config.yaml pytest.ini requirements.txt). Still bounded: infra/ whole is 9335 tracked files, of which infra/aws/lambda/ alone is 7305, so the wide pattern is NOT the answer.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "four measured refusals 2026-10-13 ~12:4xZ-13:5xZ in C:/tmp/mp-mq-z4, each quoted above with its absent path",
      "`git ls-tree -r --name-only HEAD infra/` = 9335, infra/aws/terraform/ = 757, infra/aws/lambda/ = 7305, infra/aws/ec2/ = 676 at 6fe140d0a8",
      "commit a667941f52 landed on the pattern list that includes all six additions; naming gate PASS 1 graded, CONFORMANT as IAM_POLICY",
      "the same class is already written down: /cloud-ops 'FOUR APPLY-SIDE TRAPS' item (4) -- a sparse worktree that will run an apply needs lib and its own agent home in the cone, all fail CLOSED and name what they need"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "For 2.0.0_SA_COO~MP: TO-MP-z-5 (the gateway release, STAGED) and any later GW cell touching a .tf will hit the same four. The pattern list above is measured, not predicted -- it is the one commit a667941f52 actually landed on. Suggest the order carry it instead of the MP-k-2 list."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-S44",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~MQ",
  "surfaced_at": "2026-10-13T19:56:35Z",
  "one_line": "Amendment 2's sparse list, pasted as ARGV into Git Bash, is silently rewritten by MSYS path conversion into C:/Program Files/Git/<dir>/ -- the set command exits 0, the worktree LOOKS populated, and the cone is empty. Pipe the list to `git sparse-checkout set --stdin` instead.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "spec_asserts": "NFRA_MCPORTAL.TO-MP-z-5 AMENDMENT 2, first bullet (row Z-S43): \"Use: `/.tools/ /org/ /lib/ /infra/logic/ /infra/aws/terraform/ /infra/aws/lambda/ci/ /infra/aws/lambda/mcportal/ /infra/aws/ec2/` plus the 12 root-level tracked blobs\". The list is correct; the amendment does not say how to pass it.",
  "world_is": "Passed as argv in Git Bash (`git sparse-checkout set /.tools/ /org/ ...`), MSYS converts every leading-slash token to a Windows path. Measured in C:/tmp/mp-z5-hookup at b15b776bba: `git sparse-checkout list` returned `C:/Program Files/Git/.tools/`, `C:/Program Files/Git/org/`, `C:/Program Files/Git/lib/`, `C:/Program Files/Git/infra/logic/`, `C:/Program Files/Git/infra/aws/terraform/`, `C:/Program Files/Git/infra/aws/lambda/ci/`, `C:/Program Files/Git/infra/aws/lambda/mcportal/`, `C:/Program Files/Git/infra/aws/ec2/` -- all eight DIRECTORY patterns destroyed. rc=0, no warning, no stderr. THE FAILURE DOES NOT LOOK LIKE ONE: `ls -A` at the worktree root printed .tools/ org/ lib/ infra/ data/ docs/ tools/ users/ and 12 more directories, so the tree reads populated at a glance. The directories exist because the 12 ROOT-LEVEL BLOBS are gitignore-style patterns with NO slash, and such a pattern matches at EVERY level -- CLAUDE.md, README.md, requirements.txt and .gitignore exist under hundreds of directories, so those files alone were checked out and created the directory skeleton. Counts of REGULAR FILES under each: .tools 3, org 100, lib 3, infra 136. After re-setting the identical list through `--stdin` (no argv, no conversion): .tools 525, org 63376, lib 758, infra 1626, and admin_api.py, server.py, safe-ec2-deploy.sh, opal_naming.py, devices.py, safe-commit.sh, commit-gate.sh and deploy_ledger.py all resolve. The mangled cone would have failed EVERY gate Z-S43 enumerates, one round-trip each, with messages naming absent paths -- i.e. it presents as Z-S43 recurring rather than as its own defect, which is why it is worth a row.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "`git sparse-checkout list` output quoted verbatim above, C:/tmp/mp-z5-hookup, 2026-10-13 ~19:5xZ",
      "file counts before/after the --stdin re-set: .tools 3->525, org 100->63376, lib 3->758, infra 136->1626",
      "negative control for the skeleton: pytest.ini and CLAUDE.md resolved while infra/aws/ec2/opal-gateway/app/admin_api.py did not, under the SAME rc=0 set",
      "CLAUDE.md Git section already names the class (MSYS_NO_PATHCONV=1 for slashed args) but scopes it to TF imports/ARN args and `git show <ref>:<path>`; sparse-checkout is not in that list"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "For 2.0.0_SA_COO~MP: one clause on Amendment 2 fixes it for every later GW cell -- 'pass the list on stdin (`printf '%s\n' <patterns> | git sparse-checkout set --stdin`), never as argv, because MSYS rewrites a leading-slash argument'. No criterion is affected; z5.AC1/AC2 do not read how the worktree was cut. `MSYS_NO_PATHCONV=1` is the other fix but it is a blunt env override and CLAUDE.md scopes it narrowly, so --stdin is the narrower one."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-S45",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~MQ",
  "surfaced_at": "2026-10-13T20:41:03Z",
  "one_line": "MP-z-5 step 1's 'Run, on the release tree, ... 0 failed' cannot be met: the release tree reads 67 passed / 7 failed while the SAME payload bytes read 87 passed / 0 failed on box/sitez HEAD. All 7 are properties of the release BASE's non-payload tree. The act is held on the never-widen pair's disposition.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "spec_asserts": "NFRA_MCPORTAL.TO-MP-z-5 section 1 step 1: 'Run, on the release tree, tests/test_admin_gateway_breakdown.py tests/test_dashboard_deep_links.py tests/test_admin*.py tests/test_owner_gate.py: 0 failed.'",
  "world_is": "CONTROLLED PAIR, payload held constant (identical module and test bytes in both trees): on C:/tmp/mp-z5-hookup at box/sitez HEAD b15b776bba the named set reads 87 passed, 0 failed, 3 warnings in 4.98s; on the release tree C:/tmp/mp-z5-rel at base 185dc04888 the same set reads 67 passed, 7 failed in 6.33s. Base varied, outcome flipped, so the failures belong to the BASE TREE, not to this release. TWO MECHANISMS, each measured. (1) FIVE failures (test_admin_fabric.py::test_roster_equals_devices_register, test_admin_fabric_calls.py::test_real_capture_calls and ::test_request_accepted_by_open_calls_scan, test_admin_fabric_gitstate.py::test_real_capture_gitstate, test_admin_fabric_overlap.py::test_real_capture_overlap) raise FileNotFoundError on repo data files that DO NOT EXIST IN THE BASE COMMIT: `git ls-tree -r --name-only 185dc04888 -- org/devices/DEVICES.json` = 0 and at box/sitez = 1; same for org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/fixtures/s3_capture_20261009T0728Z.json (base 0, box/sitez 1). POSITIVE CONTROL that this is a real vintage gap and not a sparse-checkout miss: org/missions/DIRECTIVES.yaml and org/ORG_CHART.md both read 1 at the base and 1 at box/sitez, and the sparse cone is /org/ whole. Those four test files are NOT modified by this release (the whole-repo census is 6 paths and none of them is a test_admin_fabric* file). A release branch is cut from the previous live base and carries only gateway files forward, so its org/ tree is frozen at the release chain's vintage -- these tests can never pass on any release tree, for any payload. (2) TWO failures (test_admin_gateway_breakdown.py::test_channel_with_no_holder_is_empty_list and ::test_holders_match_the_dispatch_chain) are MP-z-1's own tests encoding the post-OG-tg-1 world. app/identity_scope.py differs between the base and box/sitez: the base still carries _SEED = {'opalbloomberg@opalinvest.com': frozenset({'whoami', 'poll_addressed_teams_messages', 'list_chats', ...})}, which the trunk emptied on 2026-10-09 (NFRA_OPLGTW OG-tg-1, Andrew-direct ~03:2xZ, record ANDREW_DIRECT_20261009_032xZ_OPAL_GATEWAY_BBG_MIRRORS_OPALGATEWAY.md). 'whoami' is one of the test world's three m365 tools, so on the base that principal IS a real scoped-allowlist holder and admin_gateway_breakdown reports it; the test asserts the trunk's one-holder answer. The handler is therefore TRUTHFUL about the live base and the test is the thing that moved. NEGATIVE CONTROL that located the cause: swapping ONLY infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt to the trunk's version (the base carries two live opalbloomberg rows the trunk removed in the same ruling) did NOT fix either test -- 2 failed, unchanged -- so the cause is the SEED in identity_scope.py, not the allowlist file. The allowlist was restored and the census re-read at 5 files.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "87 passed / 0 failed at C:/tmp/mp-z5-hookup (box/sitez HEAD b15b776bba) and 67 passed / 7 failed at C:/tmp/mp-z5-rel (base 185dc04888), same payload bytes, same invocation",
      "git ls-tree -r --name-only at both refs for org/devices/DEVICES.json (0 vs 1) and the cp2 fixture (0 vs 1), with DIRECTIVES.yaml and ORG_CHART.md as the 1-vs-1 positive control",
      "git diff 185dc04888 box/sitez -- app/identity_scope.py: the _SEED entry for opalbloomberg@opalinvest.com, 'whoami' included, removed by OG-tg-1",
      "allowlist-swap negative control: 2 failed before and 2 failed after, allowlist restored, census re-read = 5 files"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "For 2.0.0_SA_COO~MP and 1.0.0_SA_CTO~Z: section 6 of org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/NEVER_WIDEN_ASK_MP-z-5.md puts the same three options to each half -- (a) accept the 7 with their causes named; (b) grade '0 failed' at box/sitez HEAD, already measured at 87/0, and require on the release tree only that no test NEWLY fails against the base's own pre-release run; (c) something else, including refusing the act. This seat neither repaired nor waived the criterion. GENERAL, beyond this cell: every later GW release cut on a release-chain base inherits mechanism (1) -- any test that reads a repo path outside infra/aws/ec2/opal-gateway/ cannot pass on a release tree. Worth one clause in the GW decomposition rather than a row per release."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-S46",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~MQ",
  "surfaced_at": "2026-10-13T21:07:44Z",
  "one_line": "Amendment 2's sparse list is missing /data/transcripts/scripts/teams/ -- deploy-to-ec2.sh reads meeting_allowlist.json from there and REFUSES (no upload) before the base guard, so a GW release cut on that list cannot deploy. The complete set of repo reads the two deploy scripts make is six paths; they are enumerated here so the next cell pays no round-trips.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "spec_asserts": "NFRA_MCPORTAL.TO-MP-z-5 AMENDMENT 2, first bullet (row Z-S43): the NO-CONE list `/.tools/ /org/ /lib/ /infra/logic/ /infra/aws/terraform/ /infra/aws/lambda/ci/ /infra/aws/lambda/mcportal/ /infra/aws/ec2/` plus the 12 root-level tracked blobs, with `/infra/aws/ec2/` called out as whole 'because the deploy scripts and the gateway app are both under it'. That sentence is true and still insufficient: the deploy scripts READ OUTSIDE their own directory.",
  "world_is": "The act refused on the first attempt: `ERROR: REFUSED (no upload): meeting_allowlist.json unreadable at /c/tmp/mp-z5-rel/data/transcripts/scripts/teams/meeting_allowlist.json` (deploy-to-ec2.sh line 36, which builds TRANSCRIPT_MEETING_ALLOWLIST for the host .env). THIS IS A CONE GAP, NOT A VINTAGE GAP, and the two are worth telling apart because they have different fixes: `git ls-tree -r --name-only HEAD -- <path>` reads 1 at the release base 185dc04888 AND 1 at box/sitez, while the file is simply not on disk -- so widening the cone fixes it, whereas Z-S45's absent org/ files read 0 at the base and no cone can produce them. FAIL-CLOSED AND MEASURED AS SUCH: the refusal fires BEFORE the base guard and before any upload, and the world was read after it to confirm -- the release key ec2/opal-gateway/opal-gateway-64b3e54658.tar.gz returns 404 Not Found (never created); opal-gateway-latest.tar.gz still carries git-ref 185dc048881da2030efa11f4d0bfb8704b500c66, ETag b486e614fc122cf854f0d063bd198e4e, LastModified 2026-10-12T12:51:38Z; the rollback key opal-gateway-185dc04888.tar.gz is untouched at the same ETag, LastModified 2026-10-12T12:51:35Z. THE COMPLETE ENUMERATION, so the next cell pays one round-trip and not six: the only repo paths deploy-to-ec2.sh and safe-ec2-deploy.sh read outside the gateway dir are data/transcripts/scripts/teams/meeting_allowlist.json (line 36), mcportal (line 50 -- handled, the script cuts its own detached worktree from the main repo when absent), infra/aws/ec2/EC2_MANIFEST.json (lines 57, 114), infra/aws/ec2/opal-gateway (line 210), .tools/halt-gate-check.sh (safe-ec2-deploy line 167) and .tools/safe-commit.sh (line 264); lib/ is reached indirectly by the ADVI_MARKET_UPDATE_S3_ROOT precondition's lib.opal_naming.address() call. Adding the single pattern /data/transcripts/scripts/teams/ resolved all six, with the census re-read at 5 gateway files and 0 outside, and the tree still clean at the release commit.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "the refusal line quoted verbatim from the first act attempt, 2026-10-13 ~21:0xZ, C:/tmp/mp-z5-rel",
      "ls-tree at the base = 1 and at box/sitez = 1 for the missing path, against on-disk = no: the cone-vs-vintage discriminator",
      "post-refusal world reads: release key 404, -latest git-ref unchanged at 185dc04888, rollback key ETag unchanged",
      "the six repo reads enumerated from the two scripts by anchored pattern over $WORKSPACE_ROOT/ and $_main/, not by recollection"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "For 2.0.0_SA_COO~MP: Amendment 2's list wants one more pattern, /data/transcripts/scripts/teams/, for any GW cell that RUNS the deploy (a build-only or commit-only cell does not need it). Together with Z-S43 (the commit gates) and Z-S44 (pass the list on stdin, never argv) this makes the GW sparse recipe complete as measured. No criterion is affected: the refusal happened before any upload, nothing in the world moved, and z5.AC1/AC2 do not read how the worktree was cut."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-S47",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "1.0.0_SA_CTO~Z",
  "surfaced_at": "2026-10-13T21:19:26Z",
  "one_line": "Andrew-direct ~20:4xZ at dell2 (cross-box ORDER XB-20261013T202846Z-111f, acked 21:17:34Z): the Control Plane page shows, per box and per Claude Code login, the signed-in Claude account (email, plan, organization; never a token) and usage remaining on the 5-hour and weekly windows with reset times and claim words. No PRD outcome carries it; the GW round is in flight and frozen, so it lands at that round's analysis as a PRD addendum.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "spec_asserts": "NFRA_MCPORTAL PRD v0.7: no outcome names the signed-in Claude account or its usage limits; FWD-20 (the gateway breakdown) is cut first, ahead of every other order.",
  "world_is": "Andrew, verbatim: \"i want the mcp.opalinvest.dev/control-plane function to include the logged in account + usage remaining on 5hr and weekly basis by box. write that note and have it issued to the SITEZ box because the MCPORTAL COO shoudl get that worked in\". Record org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_204xZ_CONTROL_PLANE_SHOWS_CLAUDE_ACCOUNT_AND_USAGE_PER_BOX.md (1.0.0_SA_CTO~DELL2).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "crossbox XB-20261013T202846Z-111f ACKED by 1.0.0_SA_CTO~Z at 2026-10-13T21:17:34Z",
      "the record's 'The outcome it sets' section: account fields from the box's own login record; 5h and weekly remaining with reset and claim (MEASURED or ABSENT); figure age; display only, no alert (moratorium)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "1.0.0_SA_CTO~Z writes the PRD addendum (a new FWD) at the GW round's L10 answer, ordered AFTER FWD-20's release and Andrew's read (direction XB-20261013T185926Z-4d72 section 6: nothing cut ahead of FWD-20). The record names the first unknown: no seat reads the 5h/weekly figures today, so the first cell is a READ of where Claude Code or the account exposes them, before anything is built. The issuer disarms by citing that analysis."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-S48",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~MQ",
  "surfaced_at": "2026-10-13T21:26:55Z",
  "one_line": "z5.AC2's probe CANNOT satisfy its own channels>=2 limb on any box: it imports admin_gateway_breakdown but never app.server, and app/server.py:90 is where integrations.register_enabled runs. Measured FAIL at channels=1; the SAME probe plus that one import reads channels=8 tools=67 on the same host, every limb satisfied. The product is healthy; the criterion is not runnable.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "spec_asserts": "NFRA_MCPORTAL.TO-MP-z-5 AC2 <expect>: '... breakdown_s<=30 channels>=2 tools>=1 dup_tools=0 channels_held>=1 grant_store=read -- RESULT: PASS -- exit=0', graded by deliverables/2.0.0_SA_COO~MP/fwd20/checks/z5.AC2.sh, whose payload is _z5_probe.py: 'from app import admin_gateway_breakdown as b; t = time.time(); d = b._compute(); ...'.",
  "world_is": "Run after the release landed: 'ssm command=58d7318b-79c7-4f7a-b01a-50d9a953be09 status=Success; /health=200; no-identity breakdown=401 /control-plane=401 /open-calls=401 /gateway=401; unlisted=404; breakdown_s=1.7 channels=1 tools=43 dup_tools=0 channels_held=1 grant_store=read principals=1 -- RESULT: FAIL'. EVERY LIMB PASSES BUT channels, which reads 1 against >=2. THE CAUSE IS THE PROBE'S IMPORT GRAPH, AND IT WAS MEASURED RATHER THAN REASONED TO. (a) The obvious env hypothesis was FALSIFIED FIRST: re-running the probe with the service's own EnvironmentFile loaded (`set -a; . /opt/opal-gateway/.env`) returned IDENTICAL output -- channels=1, ids=['m365'], registered_tools=43 -- and `systemctl show -p EnvironmentFiles` confirms /opt/opal-gateway/.env is the only file the unit loads, so the probe's environment is not the difference. (b) The cause is in code: app/server.py:90 runs `_integ_report = integrations.register_enabled(mcp, _cfg.ENABLED_INTEGRATIONS)` at MODULE level. admin_gateway_breakdown derives channels from `registry._ACTIVE_BY_TOOL` (line 156, 221) and the tool manager; a process that imports admin_gateway_breakdown WITHOUT importing app.server therefore sees an EMPTY active set and only the 43 native tools, i.e. the single m365 channel. The SERVED process imports server (it is the ASGI app), so the live gateway does have the integration channels. (c) POSITIVE CONTROL, the decisive one: the identical probe with ONE added line, `import app.server`, run from the same venv under the same instance role on the same host, printed 'breakdown_s=1.2 channels=8 tools=67 dup_tools=0 channels_held=8 grant_store=read principals=1' and channel_ids=['m365','blackdiamond','globgrph','opal_discover','opal_portal','portal_index','schwab','ycharts'] -- so every AC2 threshold is satisfied by the deployed code, and only the probe stood between the act and a PASS. COROLLARY worth carrying: the MCP tool-surface read used by this and prior releases (`tools.mcp._tool_manager.list_tools()` in a fresh interpreter) reads 43, the NATIVE registry; the SERVED surface is 67. The before/after difference is still sound, because the same instrument ran on both sides and the difference was EMPTY -- but 43 is not the served tool count and should not be quoted as one.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "z5.AC2.sh output quoted verbatim, SSM 58d7318b-79c7-4f7a-b01a-50d9a953be09, Success, after the release",
      "falsified env hypothesis: SSM ba08d2fb-98b6-4d50-918b-6494e2371d2b, identical channels=1 with .env loaded; EnvironmentFiles = /opt/opal-gateway/.env only",
      "app/server.py:90 register_enabled at module level; admin_gateway_breakdown.py:156,221 read registry._ACTIVE_BY_TOOL",
      "positive control SSM 7c5135ec-4b01-45df-842c-5c2b1c406a8c: one added `import app.server` -> channels=8, tools=67, dup_tools=0, channels_held=8, grant_store=read, 1.2 s"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "ID NOTE: this row was first written as Z-S47 and renumbered to Z-S48 after a COLLISION -- 1.0.0_SA_CTO~Z committed its own Z-S47 (the Control Plane usage addendum) at 21:20Z, six minutes before this append at 21:26Z, and the shared append-only channel allocates ids by read-then-write with no lock, so two seats reading the same high-water mark both chose 47. The deploy commit d76cb2401c on rel-nfra-mcportal-gw cites Z-S47 in its message and means THIS row, now Z-S48. For 2.0.0_SA_COO~MP: the one-clause amendment is to add `import app.server` as the first line of _z5_probe.py's PROBE string (before `from app import admin_gateway_breakdown as b`). Nothing else changes; the thresholds stay as written and are already satisfied by the deployed code. This seat did NOT edit the check -- the checks dir is the issuer's, read-never-write under this order's SURFACES. Ledger nfra-mcportal-gw-release has L1-L4 CLOSED with proof and L5 OPEN on exactly this; the entry is in-window (8 h from 20:58Z). AC1 cannot pass while the entry is open, because its first two limbs read the sentinel, so AC1 is gated behind this amendment too. SECOND, SEPARATE DEFECT in the same family, recorded here rather than as its own row because the fix is the same amendment: z5.AC2.sh cannot run from a RELEASE TREE at all -- it invokes `python org/missions/.../checks/_z5_probe.py` by a repo-relative path, and a release tree's org/ is frozen at the release chain's vintage (Z-S45's mechanism), so the probe file is absent and the check dies before SSM with a ParamValidation error on a params.json that was never written. It was run from the MAIN tree instead, which is sound because AC2 reads no git HEAD -- but the order says 'run from your worktree root', and for AC2 that instruction cannot be followed. AC1 is unaffected: it reads HEAD and runs correctly from the release tree with an absolute script path."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-S49",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~MQ",
  "surfaced_at": "2026-10-14T00:55:50Z",
  "one_line": "The LIVE services.opal-gateway record is internally inconsistent: deployed_commit names MX-r-11 v2 while release_note still describes MP-z-5 and previous_deployed_commit names neither of the two commits actually deployed. AC1's descends limb CANNOT detect this, because both candidates are ancestors. Found while reading the live base for MP-n-4; no act of mine caused it and none of mine depends on it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "spec_asserts": "CLOUD-OPS deployment rule 8: infra/aws/ec2/EC2_MANIFEST.json IS THE SOURCE OF TRUTH -- every EC2 service registered; CI/CD depends on it. The NFRA_MCPORTAL orders lean on it directly: TO-MP-n-4 section 1 says 'The gateway runs services.opal-gateway.deployed_commit in infra/aws/ec2/EC2_MANIFEST.json ... Read it at the act; never assume it', and n4.AC1.sh grades previous -> deployed with git merge-base --is-ancestor.",
  "world_is": "Read on box/sitez at 2026-10-14 ~00:5xZ, the three fields disagree about WHICH release they describe. deployed_commit = 7eff14b2e620c8c1f688d41de6f37c09addde7b4 with deployed_at 2026-10-13T23:49:56Z and deployed_by 0.7.0_AE_CloudOps~MI -- that is NFRA_MCPINDEX MX-r-11 v2. previous_deployed_commit = ad2acc0a9305456e5bac4d7fd2cc5cd42642b203, which `git log -1` shows is 'release(NFRA_MCPINDEX MX-r-11 PHASE A, 0.9.0_WK_NFRA_MCPINDEX~33)' by a MCPINDEX WORKER -- a commit on their own release chain, not a commit that was ever the deployed gateway. The commit that WAS previously deployed is MP-z-5's 64b3e54658060859b81d6bcd48dc7000615f865d, deployed_at 2026-10-13T21:07:58Z, i.e. 2h42m EARLIER, and it is an ancestor of 7eff14b2e6 (merge-base --is-ancestor = yes), so their tree descends from it. release_note still opens 'NFRA_MCPORTAL MP-z-5 (PRD v0.7 FWD-20, workstream GW round 1)' -- it describes MP-z-5 while deployed_commit names MX-r-11 v2. SO THE SAME STALE-VINTAGE DEFECT RECURRED, with a worse surface than before: on MP-x-4, MP-r-2, MP-n-1 and MP-z-5 it produced a wrong previous_deployed_commit, which a reader can spot; here it ALSO left a release_note describing a DIFFERENT release than the one named beside it, so the authoritative record now reads as though MP-z-5 is live. THE GRADING INSTRUMENT IS BLIND TO IT, which is the part worth carrying: n4.AC1.sh (and z5.AC1.sh) test the chain only with `git merge-base --is-ancestor $PREV $DEP`, and BOTH ad2acc0a93 and the true 64b3e54658 are ancestors of 7eff14b2e6, so the check reads descends=yes either way. A positive control confirms the instrument is working and merely under-specified: 185dc04888 -> 64b3e54658 also reads yes. An ancestry test cannot distinguish 'the commit previously deployed' from 'any commit in the history'.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "box/sitez EC2_MANIFEST.json services.opal-gateway read at 2026-10-14 ~00:5xZ: deployed 7eff14b2e6 / previous ad2acc0a93 / deployed_by ~MI / release_note opening with 'NFRA_MCPORTAL MP-z-5'",
      "git log -1 ad2acc0a93 = release(NFRA_MCPINDEX MX-r-11 PHASE A, 0.9.0_WK_NFRA_MCPINDEX~33), 2026-10-13 17:57:48 -0400",
      "deployed_at timestamps: MP-z-5 21:07:58Z vs MX-r-11 v2 23:49:56Z, so MP-z-5 was the previous deploy",
      "merge-base --is-ancestor: 64b3e54658 -> 7eff14b2e6 yes AND ad2acc0a93 -> 7eff14b2e6 yes, with 185dc04888 -> 64b3e54658 yes as the positive control -- the limb cannot discriminate"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "NOT MINE TO FIX and not blocking MP-n-4. The entry belongs to whoever owns the MX-r-11 release record (NFRA_MCPINDEX, 0.7.0_AE_CloudOps~MI); this row exists so the issuer can route it rather than have it found a third time. MP-n-4's step 4 will write previous_deployed_commit = 7eff14b2e6 and a release_note for THIS release, which repairs both fields going forward but leaves the MX-r-11 generation misattributed in history. TWO THINGS WORTH A DECISION, both for 2.0.0_SA_COO~MP: (1) the wrapper defect is now five releases old (MP-x-4, MP-r-2, MP-n-1, MP-z-5, MX-r-11 v2) and every one of them was corrected by hand afterwards, which means the correction is the convention and the wrapper is the bug -- safe-ec2-deploy.sh writes deployed_commit/at/by from the live act but takes previous_deployed_commit and release_note from the release tree's own stale manifest, and a release tree's manifest is ALWAYS stale by construction (it is cut from an older base). (2) the AC1 chain limb could discriminate at no cost by comparing previous_deployed_commit against the PRIOR entry's deployed_commit in the deploy ledger, or simply by asserting it equals the base the release was cut on, which the order already requires the actor to read. An ancestry test will keep passing on a wrong value."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-S50",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~MQ",
  "surfaced_at": "2026-10-14T01:05:38Z",
  "one_line": "CORRECTION, superseding row Z-S49 in part: previous_deployed_commit=ad2acc0a93 is RIGHT, not wrong. MX-r-11 v1 WAS deployed at 22:51:28Z, between MP-z-5 and v2. I inferred 'never deployed' from the commit's AUTHORSHIP and from timestamps I already had, without ever reading the artifact plane -- the only record of what was deployed. Only release_note is stale. Caught by 1.0.0_SA_CTO~Z, msg 33871.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "spec_asserts": "Row NFRA_MCPORTAL-Z-S49 (this seat, 2026-10-14T00:55:50Z) asserted: 'previous_deployed_commit = ad2acc0a9305456e5bac4d7fd2cc5cd42642b203, which git log -1 shows is release(NFRA_MCPINDEX MX-r-11 PHASE A, 0.9.0_WK_NFRA_MCPINDEX~33) by a MCPINDEX WORKER -- a commit on their own release chain, not a commit that was ever the deployed gateway. The commit that WAS previously deployed is MP-z-5's 64b3e54658.' Rows are append-only, so this row supersedes that claim rather than editing it.",
  "world_is": "THE ARTIFACT PLANE SETTLES IT AND I NEVER READ IT. `aws s3api list-objects-v2 --prefix ec2/opal-gateway/ --query sort_by(Contents,&LastModified)` over 84 keys (denominator printed) gives the real deploy sequence: opal-gateway-64b3e54658.tar.gz at 2026-10-13T21:07:30Z (MP-z-5, mine), then opal-gateway-ad2acc0a93.tar.gz at 22:51:28Z, 557,616 B, git-ref ad2acc0a9305456e5bac4d7fd2cc5cd42642b203 (MX-r-11 v1), then opal-gateway-7eff14b2e6.tar.gz at 23:49:56Z (v2). So MX-r-11 shipped TWICE, 58 minutes apart, and ad2acc0a93 really was the deployed gateway between my release and v2. previous_deployed_commit=ad2acc0a93 is therefore CORRECT and the chain is intact. WHAT SURVIVES OF Z-S49: exactly one claim, that release_note is stale -- it still opens 'NFRA_MCPORTAL MP-z-5 (PRD v0.7 FWD-20, workstream GW round 1)' beside a deployed_commit naming MX-r-11 v2, so the authoritative record still reads as though MP-z-5 is live. Also surviving, and independent of my error: AC1's chain limb uses git merge-base --is-ancestor, which cannot distinguish the previously-deployed commit from any ancestor, so it would read descends=yes against a wrong value too. WHAT I DID WRONG, because it is the reusable part: I had TWO non-oracles and treated their agreement as evidence. (a) AUTHORSHIP -- 'a MCPINDEX worker's own release-chain commit' tells you who wrote it, and CLAUDE.md's Git section says in as many words that authorship is not evidence; a release chain's commits are EXACTLY the commits that get deployed, so the authorship actively pointed the wrong way. (b) A CHAIN I ALREADY KNEW -- I had MP-z-5's deploy at 21:07:58Z and v2's at 23:49:56Z and concluded nothing could be in between, which is an absence inferred from a population I never enumerated. The deploy ledger would also have shown it. ONE list-objects call, which costs a single round trip and prints its own denominator, was the whole fix, and it is the same instrument this project's own L2 proofs use to confirm a versioned key exists.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "list-objects-v2 over ec2/opal-gateway/ sorted by LastModified, 84 keys scanned: 64b3e54658 @21:07:30Z, ad2acc0a93 @22:51:28Z, 7eff14b2e6 @23:49:56Z",
      "head-object opal-gateway-ad2acc0a93.tar.gz: 557,616 B, git-ref ad2acc0a9305456e5bac4d7fd2cc5cd42642b203, LastModified 2026-10-13T22:51:28Z",
      "1.0.0_SA_CTO~Z msg 33871 and the CTO half @55db595800, which names the same key and timestamp independently",
      "the surviving claim, re-read: box/sitez release_note still opens with NFRA_MCPORTAL MP-z-5 beside deployed_commit 7eff14b2e6"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "DISPOSITION NOTE: the CORRECTION in this row is settled -- the artifact plane is unambiguous and the CTO half names the same key independently. It is filed UNDER_INVESTIGATION because the RESIDUAL item still needs the issuer's routing, not because the correction is in doubt; the ratified enum has no value for 'settled finding, open routing'. For 2.0.0_SA_COO~MP: Z-S49 should be read as CORRECTED BY THIS ROW. Its routing ask shrinks from two items to one -- the stale release_note on the MX-r-11 generation (NFRA_MCPINDEX's record, not mine) -- plus the AC1-limb observation, which stands on its own and is unaffected by my error. The wrapper-defect count in Z-S49's notes must also be read down: MX-r-11 v2 did NOT produce a wrong previous_deployed_commit, so the stale-vintage defect is four releases old there (MP-x-4, MP-r-2, MP-n-1, MP-z-5), not five, and what MX-r-11 v2 shows is the release_note half of the same wrapper behaviour. MY ASK's section 7 is wrong as committed @3f7f1097e7; the CTO half corrects it on the record and I sent the correction to the COO before it signed, so no half is signed against the wrong premise."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-S51",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-14T02:53:03Z",
  "disposition": "UNDER_INVESTIGATION",
  "adjudicates": [
    "NFRA_MCPORTAL-Z-S47"
  ],
  "one_line": "DISARMS Z-S47 citing 1.0.0_SA_CTO~Z's C17 round-2 analysis @d0dd3f0964 (ruling 3). Andrew's ask (Control Plane shows each box's signed-in Claude account and its 5h/weekly usage left) is now FWD-22 in PRD v0.8. Its first cell, U1, is a READ of where those limits are exposed, cut in the next round's one issuance once v0.8 reads ADMITTED.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D6/NFRA/NFRA_MCPORTAL/ledger/ROUND_ANALYSIS.c17-round2.md @d0dd3f0964, section 2 item 3 and section 3 row U1",
      "1.0.0_SA_CTO~Z msg 33947: 'Disarm Z-S47 citing the analysis'",
      "python .tools/prd-signoff.py status NFRA_MCPORTAL at ~02:5xZ: v0.8 @d0dd3f0964 WITHHELD, ratified-text half owed by 3.0.0_SA_CVO~Z"
    ]
  },
  "spec_asserts": "Z-S47: Andrew's Control Plane account-and-usage ask has no outcome in the PRD; the GW round is frozen.",
  "world_is": "The ask is now an outcome (FWD-22, PRD v0.8) with a first cell named in the round analysis. Nothing is owed against Z-S47 itself. U1 carries it, and U1 is issued with G1, F1 and F2 in one issuance once v0.8 is ADMITTED.",
  "notes": "Disarm owner per Z-S47: 2.0.0_SA_COO~MP (issuer)."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W23-S1",
  "one_line": "The repo-wide comp-find sweep named by MP-pc-4 did not finish in 120 s; whole-repo absence of Claude usage readers is unread, not zero.",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~23",
  "surfaced_at": "2026-10-14T03:39:06Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {"status": "GROUNDED", "evidence": ["comp-find -i 'ratelimit|rate_limit|usage|oauthAccount' --files --limit 30 run from C:/tmp/mp-pc-23 was moved to background after 120 s and its output file stayed 0 bytes"]},
  "spec_asserts": "The task order names comp-find for the repo-wide sweep of Claude usage or account readers.",
  "world_is": "The sweep did not finish in 120 s on this worktree; native Grep over .tools and org/mcp found 0 files; the whole-repo sweep is unread."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W22-S1",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~22",
  "surfaced_at": "2026-10-14T03:44:04Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "TO MP-pc-3 types GitBox.integration_refused_basis as a string; I typed it optional (basis?: string) because panels.test.tsx, outside my paths, builds GitBox fixtures without it.",
  "spec_asserts": "Each box carries integration_refused_basis (a string); GitBox type updated in src/api/admin.ts.",
  "world_is": "Existing fixtures in mcportal/src/pages/control-plane/panels.test.tsx (read-only for this cell) construct GitBox without integration_refused_basis, so a required field would fail the typecheck the drain runs, and the file is not in the order's paths. The type is optional; the view sets title={box.integration_refused_basis}, so a payload that carries it shows it and one that omits it shows no title. Once panels.test.tsx fixtures carry the field the type can be made required.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "mcportal 17dcbb2: src/api/admin.ts GitBox",
      "mcportal/src/pages/control-plane/panels.test.tsx:52-83 (two GitBox fixtures without the field)"
    ]
  }
}
```

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-W25-S1",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~25",
    "surfaced_at": "2026-10-14T18:57:59Z",
    "disposition": "UNDER_INVESTIGATION",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "one_line": "The face's query-first read of the grant store is refused: the operator role opal-gateway-access-admin is AccessDenied dynamodb:Query on gateway-access-state-table for partition POLICY#6810043e-d171-4adc-9975-068b35e179da#ad037ea5-fee8-412e-9da9-15c6cf2a4fbc. GetItem on that partition's two known keys (principal_profile, data_entitlement#0000000004) succeeded under the same assumed role and is the read the run file uses.",
    "spec_asserts": "The operator role reads each principal's partition by Query (trust and LeadingKeys design say yes); a denial is a BLOCKING row with the principal key and the error.",
    "world_is": "sts assume-role on arn:aws:iam::313476888478:role/opal-gateway-access-admin returned rc 0 and get-caller-identity returned the assumed-role ARN. dynamodb query --consistent-read on gateway-access-state-table returned AccessDeniedException: no identity-based policy allows the dynamodb:Query action (rc 254). The same role's dynamodb get-item of principal_profile (rc 0, status active, grant_revision 4) and of data_entitlement#0000000004 (rc 0, status active) succeeded. Nothing was written; the host role was not used for the store read.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~25/pd1_query_denied.txt (the measured AccessDeniedException text)",
        "org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~25/pd1_session_log.txt (steps 2 to 4)"
      ]
    }
  },
  {
    "id": "NFRA_MCPORTAL-Z-W25-S2",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~25",
    "surfaced_at": "2026-10-14T18:57:59Z",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "app.admin_gateway_breakdown._scan_principals takes a required client argument; the face's zero-argument call form does not run, so the scan was called with the served module's own host-role client from _ddb_client().",
    "spec_asserts": "Call app.admin_gateway_breakdown._scan_principals() with no arguments, after reading its signature.",
    "world_is": "admin_gateway_breakdown.py:174 defines _scan_principals(client) -> list. The page probe pd1_page_probe.py passes BD._ddb_client(), a host-role boto3 DynamoDB client, so the principal list is the served scan's own result (1 principal) and not an operator-role Scan (which the issuer measured denied).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py:174 (def _scan_principals(client))",
        "org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~25/pd1_page_probe.py (the call site)"
      ]
    }
  }
]
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W26-S1",
  "one_line": "MP-pd-2 says the stored person_access revision is an int; the real store returns it as decimal.Decimal, so an int check refused every real update until the writer normalizes it.",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~26",
  "surfaced_at": "2026-10-14T18:52:57Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/opal-gateway/app/access_state.py:27 docstring and :325 TypeDeserializer: numbers come back as decimal.Decimal",
      "infra/aws/ec2/opal-gateway/app/data_entitlement.py _revision accepts int or integral Decimal",
      "probe .scratch/probe_person_access_update.py before the _plain_record fix: OK expect 1 read STALE-REVISION with zero writes; after the _plain_record fix it reads WRITTEN with one conditional put"
    ]
  },
  "spec_asserts": "TO MP-pd-2 section 1 sets the stored body field revision to an int >= 1 and says the writer checks the current revision against expect_revision.",
  "world_is": "acs.AccessState.get returns whole numbers as decimal.Decimal. The writer normalizes the stored record with _plain_record in lambda_function.py before its revision check, so the optimistic condition and the next revision are int. The staged Decimal form is not a fault of the store; the order did not say it."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W26-S2",
  "one_line": "The worker rules flip the task order status to complete with the proof instance, but the order's granted paths do not include the task-order file, so I did not flip it.",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~26",
  "surfaced_at": "2026-10-14T19:01:57Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pd-2.grant-writer-person-access.md section 3 <paths> (lines 106-111) lists the lambda_function.py, tests/test_person_access.py, deliverables and investigations paths only",
      "base ef2a5b14e176b428600920cbd9ada74817ced168; the code commit is f40bf7dded"
    ]
  },
  "spec_asserts": "The worker rules say a worker flips the task order <status> to complete in the same commit as the proof instance.",
  "world_is": "The order's <paths> grant no write to its own task-order file. The criteria pass and the instance validates, but this worker does not flip the order status; the issuer or COO owns the flip."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W29-S1",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~29",
  "surfaced_at": "2026-10-14T18:53:18Z",
  "one_line": "The MP-pd-5 order defines the printed line for a measured payload and for an absent one, but not for an absent payload that leaves a measured snapshot in place; the script prints usage n/a there, from the payload result, while the snapshot keeps its measured figures.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Section 1 step 5: an absent result never replaces a measured snapshot. Step 6: print the 5h/wk line when measured, else usage n/a.",
  "world_is": "Steps 5 and 6 do not define the output on the kept-snapshot path. Measured: a measured run printed '5h 42% wk 11%'; then an absent run printed 'usage n/a' and usage_snapshot.json still held claim measured with five_hour used 42.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/claude-usage-statusline.py@967a02ec89 run(): the claim absent and existing measured branch skips the write; main prints format_line(claim) from the payload result",
      "ad hoc run, temp CLAUDE_CONFIG_DIR under .scratch/pd5 (uncommitted): measured payload printed '5h 42% wk 11%'; absent payload printed 'usage n/a'; snapshot after the absent run read claim measured, five_hour used_percentage 42"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not repaired: the order is frozen for this cell. The worker chose the payload result. The other reading (print the kept snapshot figures) is the issuer's to rule. The snapshot file is correct under either reading."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W29-S2",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~29",
  "surfaced_at": "2026-10-14T18:53:18Z",
  "one_line": "The order does not say what happens when stdin parses as JSON but is not an object (null, a list, a number); the script treats it as a payload with no rate_limits member.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Section 1 step 1: unparseable stdin prints nothing and changes nothing. Step 4: a payload with no usable rate_limits member is absent.",
  "world_is": "A non-object JSON value parses, so step 1 does not fire, and the order names no branch for it. Measured: stdin 'null' with no snapshot printed 'usage n/a' and wrote claim absent; stdin '[1,2]' over a measured snapshot printed 'usage n/a' and left the measured snapshot (five_hour used 42) intact.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/claude-usage-statusline.py@967a02ec89 build_rate_limits(): a non-dict payload yields no rate_limits, so the absent branch runs",
      "ad hoc runs under .scratch/pd5 (uncommitted): stdin 'null' with an empty config dir -> usage n/a, claim absent; stdin '[1,2]' over a measured snapshot -> usage n/a, claim measured kept"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not repaired. The worker reads a non-object as absent, which keeps the never-replace rule intact. The issuer may prefer treating it as unparseable (print nothing, change nothing)."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W27-S1",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~27",
  "surfaced_at": "2026-10-14T18:51:05Z",
  "one_line": "AC2 cannot pass as written: the mandated principal key on every People row breaks the unchanged assertion at tests/test_admin_people.py:202 that pins each row's key set, so test_people_lists_every_candidate_even_holding_nothing FAILS (1 failed, 9 passed).",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PD.3 step 2 adds a principal key to every People row; AC2 names test_people_lists_every_candidate_even_holding_nothing as PASSED, and the order says the rest of tests/test_admin_people.py stays unchanged.",
  "world_is": "tests/test_admin_people.py:202 asserts set(p) == {\"who\",\"kind\",\"how\",\"tier\",\"channels\"} for every row; with principal present that assertion fails. Left unedited per the order. AC2 invocation: RESULT: FAIL, named tests PASSED 3 of 4, rc=1.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/opal-gateway/tests/test_admin_people.py@ef2a5b14e1:202 (the unchanged assertion)",
      "pd3.AC2.sh run in worktree C:/tmp/mp-pd-27: 'people rows tests: 1 failed, 9 passed; named tests PASSED 3 of 4', RESULT: FAIL, exit=1"
    ]
  }
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W27-S2",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~27",
  "surfaced_at": "2026-10-14T18:51:05Z",
  "one_line": "The round-1 People body that test_people_principal_never_leaks_into_other_fields names as its reference is not an artifact in the tree; the reference was dumped from the pre-PD.3 admin_people before the edit and pinned as the literal ROUND1_PEOPLE in tests/test_admin_people.py.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "With the principal key removed from every row, the People body equals the round-1 body for the same planted world.",
  "world_is": "No stored round-1 body exists. The pre-edit body for _world_with_people(names=[whoami, list_calendar]) was captured by a scratch run (gitignored .scratch/) before the admin_people.py edit and is pinned as ROUND1_PEOPLE (7 rows, population last).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/opal-gateway/app/admin_people.py@ef2a5b14e1 (pre-edit _compute, the source of the dump)",
      "infra/aws/ec2/opal-gateway/tests/test_admin_people.py (ROUND1_PEOPLE, appended in this commit)"
    ]
  }
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W27-S3",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~27",
  "surfaced_at": "2026-10-14T18:51:05Z",
  "one_line": "The grant-writer Lambda in this base does not name the set_person_access action or a person_access record, so the access POST relays whatever the writer answers until the parallel writer cell lands.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "A parallel cell extends the grant-writer Lambda with the action set_person_access (PD.2 record and event).",
  "world_is": "A Grep of infra/aws/lambda/mcportal for set_person_access|person_access returned no files at ef2a5b14e1; the writer half is not in this base. Nothing in this cell depends on it for the handler tests, which use a fake client.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py@ef2a5b14e1 (no match for set_person_access)"
    ]
  }
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W28-S1",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~28",
  "surfaced_at": "2026-10-14T18:51:44Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "one_line": "MP-pd-4 does not say which HTTP status carries a REFUSED verdict; the client throws on every non-2xx, so a REFUSED sent with a non-2xx status shows its status and body, not its reason and detail.",
  "spec_asserts": "setPersonAccess returns the verdict object whether WRITTEN or REFUSED and throws only on a transport failure, the way narrowGrant handles a refusal (worker face lines 52-53); a REFUSED verdict shows its reason and detail on the page and a 403 shows 'not allowed' (lines 66-67).",
  "world_is": "narrowGrant's readJson throws on every non-2xx, so both halves of that sentence hold only if the writer answers REFUSED with a 2xx, and the contract (lines 46-47) does not state the status. Built: a non-2xx throws AdminStatusError carrying its status and body, a 2xx returns the verdict object, a 403 reads 'not allowed' and is never retried. Not checked against the live writer (no network call in this cell). If the writer answers REFUSED with a non-2xx, the page shows 'admin API <status>: <body>' and not the reason.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "mcportal@c24bcd0 src/api/admin.ts statusOrJson(): throws AdminStatusError when !response.ok, before any verdict is read",
      "mcportal@17dcbb2 src/api/admin.ts readJson() and narrowGrant(): throws on !response.ok, the refusal path the contract cites",
      "org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pd-4.people-page-controls.md@ef2a5b14e1 lines 46-47, 52-53, 66-67"
    ]
  }
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W28-S2",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~28",
  "surfaced_at": "2026-10-14T18:51:44Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The route header at mcportal 17dcbb2 lists ten /api/admin routes, but the client also calls GET /api/admin/people (MP-pc-3) and that route is absent from the header.",
  "spec_asserts": "The header of src/api/admin.ts is the fixed set of /api/admin routes the client calls, as its first line says.",
  "world_is": "At 17dcbb2 getPeople() calls /api/admin/people and the header omits it, so the header is one route short of the calls. This cell adds the two person-access route lines and reworded the header so it no longer claims the People read is listed; it does not add the missing line, which is a neighbouring defect outside the order. Nothing reads the header at runtime.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "mcportal@17dcbb2 src/api/admin.ts lines 2-12: the header's route list, with no GET /api/admin/people line",
      "mcportal@17dcbb2 src/api/admin.ts getPeople(): fetch('/api/admin/people', { credentials: 'include' })"
    ]
  }
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W28-S3",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~28",
  "surfaced_at": "2026-10-14T19:51:37Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The MP-pd-4 AC1 check prints 'bun test rc=$rc' but $rc is the exit status of the trailing tr/sed stage of its pipeline, not bun's.",
  "spec_asserts": "pd4.AC1.sh reports 'bun test rc=<n>' as the exit status of `bun test src`, and its RESULT line requires rc=0.",
  "world_is": "In org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/pd4.AC1.sh the line out=$(cd mcportal && ... bun test src 2>&1 | tr | sed ...); rc=$? takes the status of the last pipeline stage (sed). Positive control: sh -c 'exit 3' | cat leaves $? = 0. The verdict still fails closed on the parsed pass and fail counts (fail must read 0, pass must be at least 8), so a failing run still reads FAIL; the printed rc just cannot show bun's own exit code. Not repaired here: the script is outside this cell's write paths.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/pd4.AC1.sh (the out=$(... | tr | sed) line and the rc=$? line)",
      "positive control in the worker shell: sh -c 'exit 3' | cat, then echo $? printed 0"
    ]
  }
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W28-S4",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~28",
  "surfaced_at": "2026-10-14T19:55:00Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The worker procedure asks for the task order's <status> to be flipped to complete with the instance; the order's <paths> does not grant the task-order file, so this worker did not flip it.",
  "spec_asserts": "Worker procedure: flip the task order's <status> to complete and commit the instance, deliverables and flip together; the order's <paths> is the write grant (mcportal src/pages/people, src/api/admin.ts, src/api/admin.test.ts, the deliverables folder, the surprise-channel investigations folder).",
  "world_is": "The <status> line is in the record face of org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pd-4.people-page-controls.md (line 138, pending), a path outside <paths>. The instance validates rc=0 (proof-of-spec-check, AC1). The launcher message did not ask for the flip. Left for the COO to flip.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pd-4.people-page-controls.md@31df432618 line 138 (<status>pending</status>, after the RECORD FACE marker) and section 3 <paths>",
      "org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~28/NFRA_MCPORTAL.TO-MP-pd-4.people-page-controls.proof_of_spec.json (rc=0 from .tools/proof-of-spec-check.py)"
    ]
  }
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-14T20:03:12Z",
  "disposition": "DISMISSED_WITH_REASON",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "id": "NFRA_MCPORTAL-Z-S52",
  "one_line": "Z-W28-S1 is DISARMED: the HTTP status of a REFUSED verdict is now stated (409, the verdict as the body) and the page reads it, so a refused write shows its reason and detail instead of 'admin API 409: <body>'.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "dismissal_reason": "Disarms NFRA_MCPORTAL-Z-W28-S1. The gap was the issuer's: MP-pd-4's contract said the POST 'answers the writer's verdict' without the status mapping. Amendment 1 @87b2ded2cf states it, and mcportal f7760a6 reads a REFUSED verdict from a 409 body. The world matches the spec the row asserted.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/opal-gateway/app/admin_grants.py _narrow_or_widen: 'status = 200 if verdict[\"verdict\"] == WRITTEN else 409' -- the mapping narrow and widen use; app/admin_people_access.py (merged @75248b6d2e) applies the same mapping to the POST",
      "org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pd-4.people-page-controls.md section 1 item 1, AMENDMENT 1 (commit 87b2ded2cf)",
      "mcportal f7760a6 src/api/admin.ts setPersonAccess: returns the parsed verdict for a 200 and for a 409 whose body has verdict WRITTEN or REFUSED; other non-2xx stay AdminStatusError; pd4.AC1.sh re-run 8 of 8, 51 pass 0 fail (worker report, drained @1b60a93715)"
    ]
  },
  "spec_asserts": "Z-W28-S1 asserted that the contract left the status of a REFUSED verdict unstated, so a refusal sent with a non-2xx status would show its status and body, not its reason and detail.",
  "world_is": "The contract now states it (WRITTEN 200, REFUSED 409, verdict as the body) and the page reads it. Not exercised against the live writer: the F2 release (MP-pd-7) is the first time the route is live.",
  "notes": "Filed by the issuer, the disarm_owner of record, in the drain of MP-pd-4."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W29-S3",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~29",
  "surfaced_at": "2026-10-14T20:05:30Z",
  "one_line": "MP-pd-6's <paths> grant does not cover the task-order status flip the standing worker bar asks for, so the order's <status> stays pending on this worker's branch.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "The standing worker bar: when the proof instance validates and every criterion passes, flip the task order's <status> to complete and commit the instance, the deliverables and the flip together. MP-pd-6 section 3 <paths> names only the deliverables folder and the surprise-channel investigations folder.",
  "world_is": "The task order file org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pd-6.claude-usage-statusline-enable.md is outside this worker's write grant, so the worker did not edit it. The proof instance is VALID (proof-of-spec-check rc=0) and AC1 is PASS on this worker's branch.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pd-6.claude-usage-statusline-enable.md@85216c4ab9 section 3 <paths>: deliverables/0.9.0_WK_NFRA_MCPORTAL~29/** and surprise-channel/investigations/**",
      "task-orders/NFRA_MCPORTAL.TO-MP-pd-6...md <status> reads pending at the vintage above; the instance records assignee 0.9.0_WK_NFRA_MCPORTAL~29 and the validator run in this worktree (rc=0, VALID)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not repaired: the status line is the issuer's to flip (or to widen the grant). The order's <status> is left as pending; the instance and deliverables are committed on wk-NFRA_MCPORTAL-pd-29."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-15T14:25:35Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "0.0.0_AB_MSTR~Z",
  "id": "NFRA_MCPORTAL-Z-S53",
  "one_line": "Bare `python` fails on site Z: C:/Program Files/Python314/Lib holds only site-packages (the standard library, encodings included, is gone), so every tool and gate that shells to PATH python breaks; Python311 still works.",
  "spec_asserts": "Every .tools script, the commit gates (safe-commit.sh runs to-pipeline-gate.py, surprise-row-gate.py and others) and org/XXX.md's tooling assume `python` on PATH runs.",
  "world_is": "At ~14:14Z `python -c ...` printed 'Fatal Python error: Failed to import encodings module ... No module named encodings' from any directory (run in the workspace and in /tmp). C:/Program Files/Python314 has python.exe (Sep 30), DLLs, python314.dll, and a Lib directory whose only entry is site-packages, last modified Oct 15 10:02 local. C:/Users/Opal Bloomberg/AppData/Local/Programs/Python/Python311 runs (3.11.9, imports encodings). Python worked earlier today (this seat ran dozens of python commands through ~11:34Z), so the stdlib was removed between. Not caused by this seat; nothing was repaired here. A command that reads the result of a failed python call can return a clean-looking empty value (one of this seat's reads printed live=<empty> and a trunk file count), so a gate or check that swallows stderr may report a false clean.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "RAN python from the workspace root and from /tmp at ~14:14Z: both 'Fatal Python error: Failed to import encodings module; ModuleNotFoundError: No module named encodings'",
      "READ ls of 'C:/Program Files/Python314/Lib': 1 entry (site-packages/), mtime Oct 15 10:02; ls of '.../Lib/encodings': no such file",
      "RAN C:/Users/Opal Bloomberg/AppData/Local/Programs/Python/Python311/python.exe -c 'import sys,encodings': OK 3.11.9"
    ]
  },
  "notes": "Work-around used by this seat only, per command: PATH=<Python311 dir>:$PATH. Remedy (reinstall or restore Python314's Lib, or point PATH at a working interpreter) is the box owner's; the seat did not change the install. Gates that run `python` bare will refuse or misread until then."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W32-S1",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~32",
  "surfaced_at": "2026-10-15T17:25:11Z",
  "one_line": "portal/DESIGN.md, the style authority the MP-pe-2 face names, is absent from the worker worktree (portal/ is an empty gitlink directory), so the new page could not be checked against it.",
  "class": "OBSERVATION",
  "spec_asserts": "MP-pe-2 face section 1 item 2: the Gateway page follows portal/DESIGN.md (light canvas, white hairline panels, navy ink, one band per page), read from portal/DESIGN.md.",
  "world_is": "In C:/tmp/mp-pe-32, portal/ is an empty directory and git lists it as a gitlink at e0b033253b973fcc19779a3783bc4979c14c65a0; portal/DESIGN.md does not exist there, and mcportal/DESIGN.md does not exist either. The file was not read from another checkout. The change adds no colour and no font: it uses the classes and tokens already in gateway.css and reuses the existing red for the gap line.",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "READ ls -la C:/tmp/mp-pe-32/portal during this run, before 2026-10-15T17:25Z: total 12, only the . and .. entries",
      "RAN git ls-files -s portal in C:/tmp/mp-pe-32: 160000 e0b033253b973fcc19779a3783bc4979c14c65a0 0 portal (a gitlink)",
      "RAN ls C:/tmp/mp-pe-32/portal/DESIGN.md and ls C:/tmp/mp-pe-32/mcportal/DESIGN.md: both 'No such file or directory'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not repaired: the doc is outside the write grant and was not copied in. Style conformance of the new page is unverified and no judgment is recorded on it. The issuer decides whether worker worktrees carry the doc."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W32-S2",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~32",
  "surfaced_at": "2026-10-15T17:25:11Z",
  "one_line": "The MP-pe-2 task-order file delivered to the worker carries its RECORD FACE below the marker, and a whole-file Read returns that section.",
  "class": "OBSERVATION",
  "spec_asserts": "The worker face is the whole of the worker's context; the RECORD FACE does not travel to the worker, and the worker reads from the first line to the RECORD FACE marker and stops there.",
  "world_is": "The file C:/tmp/mp-pe-32/org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pe-2.gateway-view-groups-and-reads-plainly.md holds the RECORD FACE (issuer notes, status, round, risk) after its marker line. A Read with no offset or limit returned the whole file, RECORD FACE included, and the worker had read past the marker before it stopped. No step was taken from the RECORD FACE content.",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "READ C:/tmp/mp-pe-32/org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pe-2.gateway-view-groups-and-reads-plainly.md with no offset or limit: 131 lines returned in one result",
      "The returned text holds the marker line 116 ('RECORD FACE -- does NOT travel to the worker'), then ISSUER NOTES at line 118 and <status>pending</status> at line 124"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The worker's own Read was unbounded; the carrier file itself holds the record face, which is the subject of this row. The TO file is outside the write grant, so no status flip was made by this worker."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-15T19:03:28Z",
  "disposition": "DISMISSED_WITH_REASON",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "id": "NFRA_MCPORTAL-Z-S54",
  "one_line": "Z-W32-S1 is DISARMED: the style authority was read at DEV by the issuer and the page was rendered and looked at; the one break (browser-blue links) is fixed.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "dismissal_reason": "Disarms NFRA_MCPORTAL-Z-W32-S1. The worktree lacked portal/DESIGN.md, so the worker could not grade style. The issuer read it from the portal repo at DEV and checked ink is navy and tokens only; Amendment 1 (@7cdca27ebd) fixed the links and the second render shows them fixed.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pe-2.gateway-view-groups-and-reads-plainly.md Amendment 1 @7cdca27ebd",
      "drain commit b006b05b90 message: headless Edge render, second build shows the five defects fixed"
    ]
  },
  "spec_asserts": "Z-W32-S1 asserted that style conformance of the new page was unverified because portal/DESIGN.md was absent from the worktree.",
  "world_is": "Conformance was checked by the issuer against DESIGN.md read at DEV and by rendering the page twice; the break found was fixed. Worker worktrees still do not carry the doc; no later cell depends on it.",
  "notes": "Filed by the issuer, the disarm_owner of record, in the drain of MP-pe-2."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-15T19:03:28Z",
  "disposition": "DISMISSED_WITH_REASON",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "id": "NFRA_MCPORTAL-Z-S55",
  "one_line": "Z-W32-S2 is DISARMED: the worker took no step from the record face and the order's own record face is the carrier the gate reads.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "dismissal_reason": "Disarms NFRA_MCPORTAL-Z-W32-S2. The worker reported it took no step from the record face below the marker; the delivered work matches the worker face (7 of 7 named tests). The order file is a single carrier by design, so the whole-file read is a property of the carrier, not a defect to repair in this round.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pe-2.gateway-view-groups-and-reads-plainly.md RECORD FACE marker at line 116",
      "worker 32 report: no step taken from the record face; issuer re-ran pe2.AC1 7 of 7, 61 pass 0 fail"
    ]
  },
  "spec_asserts": "Z-W32-S2 asserted that the record face does not travel to the worker.",
  "world_is": "The spawn prompt carried the worker face only; the worker later read the order file whole and says it took no step from the record face.",
  "notes": "Filed by the issuer, the disarm_owner of record, in the drain of MP-pe-2."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~31",
  "surfaced_at": "2026-10-15T17:32:24Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "id": "NFRA_MCPORTAL-Z-W31-S1",
  "one_line": "admin_people.py keeps its own copy of the old placement (every tool with no integration spec goes to m365), so the People view and the regrouped breakdown disagree on the undeclared tools and the AC2 seam test fails (passed=100 failed=1 seam=1).",
  "spec_asserts": "MP-pe-1 (PE round 1, decomposition v11), AC2: the admin suite stays green with seam test failures=0, because the People view reuses the breakdown's helpers and test_person_holdings_equal_breakdown_holders must still hold after the regrouping; the write surface excludes every other app/ module.",
  "world_is": "app/admin_people.py _compute (lines 87-97) sets chan_of[tool] = bd.M365_ID for every tool without an integration spec instead of using the breakdown's placement. After the MP-pe-1 change the breakdown lists send_email and list_calendar under undeclared while the People view lists them under m365, and tests/test_admin_people.py::test_person_holdings_equal_breakdown_holders fails its _pairs equality. The People page still tells its reader that undeclared tools are Microsoft 365 tools.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "RAN pe1.AC2.sh in worktree C:/tmp/mp-pe-31: 'admin suite: 1 failed, 100 passed, 3 warnings in 36.73s; passed=100 failed=1; seam test failures=1' RESULT: FAIL exit=1",
      "RAN pytest tests/test_admin_gateway_breakdown.py tests/test_admin_people.py: FAILED tests/test_admin_people.py::test_person_holdings_equal_breakdown_holders, left side holds ('m365', 'list_calendar') and ('m365', 'send_email'), right side holds ('undeclared', ...)",
      "READ infra/aws/ec2/opal-gateway/app/admin_people.py@bf3d5c9913 lines 87-97: chan_of[tool] = bd.M365_ID for every tool with no active integration spec"
    ]
  },
  "notes": "Not repaired: admin_people.py is outside this order's <paths>, and the seam assertion was left unchanged because weakening it to compare tool names only would hide the divergence. AC2 is REFUSED with this measurement. The People placement must derive from the breakdown's grouping, or the seam must be re-specified; the issuer routes that."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~31",
  "surfaced_at": "2026-10-15T17:32:24Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "id": "NFRA_MCPORTAL-Z-W31-S2",
  "one_line": "Rule 3 keys Microsoft 365 on graph_scope_map.TOOL_GRAPH_SCOPES, which lacks send_email, list_calendar, find_online_meeting and copy_site_file_to_s3; these call Graph through tools._run and now read 'No source declared'.",
  "spec_asserts": "MP-pe-1 PE.0 premise: only tools that call Microsoft Graph belong in Microsoft 365; rule 3 places a tool there only when it is a key of TOOL_GRAPH_SCOPES, and rule 4 files every other tool under undeclared.",
  "world_is": "send_email (app/tools.py:465) and list_calendar (app/tools.py:497) run through _run, the Graph-token path, yet neither is a key of app/graph_scope_map.py TOOL_GRAPH_SCOPES (keys at lines 19-52). The rule was implemented as written, so the live breakdown files these Graph tools under 'No source declared'; the page is wrong in the other direction for them.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "RAN .scratch/pe1_real_compute.py in worktree C:/tmp/mp-pe-31: m365 tools = 11 names, none of them send_email or list_calendar; undeclared = 75",
      "READ app/tools.py@bf3d5c9913 lines 465 and 497: send_email and list_calendar bodies return through _run(...)",
      "GREP app/graph_scope_map.py@bf3d5c9913 TOOL_GRAPH_SCOPES keys (lines 19-52): no send_email, list_calendar, find_online_meeting or copy_site_file_to_s3 key"
    ]
  },
  "notes": "Not repaired: the scope map is outside this order's <paths>, and the spec's rule 3 was implemented exactly as written. The issuer decides whether the Graph-scope map or the rule's key set is the intended source of truth."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~31",
  "surfaced_at": "2026-10-15T19:30:55Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "id": "NFRA_MCPORTAL-Z-W31-S3",
  "one_line": "AMENDMENT 1 (a) keeps send_email out of m365, so the seam assertion at tests/test_admin_people.py line 346 (m365 send_email held by BOSS) cannot pass while the seam test must stay unchanged; AC2 refused.",
  "spec_asserts": "MP-pe-1 AMENDMENT 1: rule 3 stays as built with no hand-kept Microsoft tool list (a); test_person_holdings_equal_breakdown_holders must pass unchanged (d); AC2 reads failed=0 and seam test failures=0 (e).",
  "world_is": "send_email is not a key of app/graph_scope_map.py TOOL_GRAPH_SCOPES and has no catalog source_group, so the amended rules place it in the undeclared group, while line 346 of tests/test_admin_people.py asserts ('m365','send_email') in the BOSS pairs. With that single line removed in a scratch probe, test_person_holdings_equal_breakdown_holders passes (1 passed): the seam equality holds for every person, and only this pinned channel differs. pe1.AC2.sh measured: 'admin suite: 1 failed, 102 passed; passed=102 failed=1; seam test failures=1' RESULT: FAIL exit=1.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "RAN bash .../pe/checks/pe1.AC2.sh in worktree C:/tmp/mp-pe-31 at 69d3842aa7 plus the uncommitted MP-pe-1 edits: 'admin suite: 1 failed, 102 passed ... seam test failures=1' RESULT: FAIL exit=1",
      "READ infra/aws/ec2/opal-gateway/tests/test_admin_people.py (worktree) line 346: assert ('m365','send_email') in _pairs(by_who[BOSS]) and not in _pairs(by_who[POP])",
      "RAN a scratch copy of that test with line 346 removed (tests/zz_seam_probe_tmp.py, deleted after): '1 passed'; GREP app/graph_scope_map.py (worktree): no send_email key"
    ]
  },
  "notes": "Not repaired and the seam test NOT edited: the order says it must pass unchanged, and the only failing line is the pinned send_email placement that the amended rules change. Options for the issuer to rule: (i) re-state line 346 as ('undeclared','send_email') for BOSS and POP, which the order would name as a changed assertion; (ii) declare send_email with kind graph in the DATA_CATALOG tool_index (read-only for this order); (iii) add send_email to TOOL_GRAPH_SCOPES (a map outside this order's paths). AC2 is REFUSED with this measurement."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~31",
  "surfaced_at": "2026-10-15T19:50:06Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "id": "NFRA_MCPORTAL-Z-W31-S4",
  "one_line": "The amended AC1 expect 'named tests PASSED 10 of 10 -- RESULT: PASS -- exit=0' cannot match what pe1.AC1.sh prints (three lines, no ' -- '), so AC1 reads a true PASS as unmatched; AC1 refused as written.",
  "spec_asserts": "MP-pe-1 AMENDMENT 1 (e): the AC1 expect line says what pe1.AC1.sh prints: 'named tests PASSED 10 of 10 -- RESULT: PASS -- exit=0'.",
  "world_is": "pe1.AC1.sh prints the tally, the verdict and the exit code on three separate lines ('...; named tests PASSED 10 of 10', 'RESULT: PASS', 'exit=0'). The proof checker matches expect with re.search over the verbatim output_evidence, and the literal ' -- ' separators never occur in it, so the expect cannot match a passing run. Measured this round: 'breakdown grouping tests: ... 20 passed ...; named tests PASSED 10 of 10' / 'RESULT: PASS' / 'exit=0' at 20 of 20 file tests. The sibling instances carry the same check as '.*'-joined regexes (TO-MP-k-1 AC1).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "RAN bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pe/checks/pe1.AC1.sh in worktree C:/tmp/mp-pe-31 (HEAD 69d3842aa7 plus uncommitted MP-pe-1 edits): output three lines, RESULT: PASS, exit=0",
      "READ .tools/proof-of-spec-check.py (expect block, re.search(exp, output_evidence, re.S|re.M)) at 69d3842aa7: the literal ' -- ' cannot match a newline-separated output",
      "READ deliverables/0.9.0_WK_NFRA_MCPORTAL~10/NFRA_MCPORTAL.TO-MP-k-1.fabric-calls-handlers.proof_of_spec.json at 69d3842aa7: its expect is 'calls tests: .*named tests PASSED 6 of 6.*RESULT: PASS.*exit=0'"
    ]
  },
  "notes": "Not repaired: the expect is the issuer's text and is kept verbatim (a criterion is never repaired). AC1 is REFUSED as written with this measurement; the substance (named tests PASSED 10 of 10, RESULT: PASS, exit 0) is measured. The issuer re-states the expect; the sibling '.*' form would match the verbatim output."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-15T21:30:41Z",
  "disposition": "DISMISSED_WITH_REASON",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "id": "NFRA_MCPORTAL-Z-S56",
  "one_line": "Z-W31-S1 is DISARMED: the People view no longer keeps its own placement; one function in admin_gateway_breakdown.py places every tool for both views.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "dismissal_reason": "Disarms NFRA_MCPORTAL-Z-W31-S1. The duplicate rule was the issuer's spec fault (it ruled the People view out of MP-pe-1's paths). Amendment 1 put admin_people.py in the paths for that only; the worker built the single function and the seam test test_person_holdings_equal_breakdown_holders passes.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "drain commit 8310672247: pe1.AC1 named tests PASSED 10 of 10, pe1.AC2 103 passed 0 failed, seam test failures 0 (re-run by the issuer on the shared tree)",
      "org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pe-1.breakdown-groups-by-source.md AMENDMENT 1 (@7cdca27ebd) and AMENDMENT 2 (@33932ee038)"
    ]
  },
  "spec_asserts": "Z-W31-S1 asserted that admin_people.py kept its own copy of the old placement so the two views disagreed.",
  "world_is": "The two views call one placement function; test_people_view_places_tools_in_the_breakdowns_groups and the seam test both pass.",
  "notes": "Filed by the issuer, the disarm_owner of record, in the drain of MP-pe-1 (merged @8310672247)."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-15T21:30:41Z",
  "disposition": "DISMISSED_WITH_REASON",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "id": "NFRA_MCPORTAL-Z-S57",
  "one_line": "Z-W31-S2 is DISARMED: TOOL_GRAPH_SCOPES is kept as a partial signal, not the Microsoft 365 list; the full classification is MCPINDEX's declaration (kind graph, MX-c-21).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "dismissal_reason": "Disarms NFRA_MCPORTAL-Z-W31-S2. The belief that TOOL_GRAPH_SCOPES lists every Graph tool was the issuer's error. Amendment 1 (PE.7) keeps rule 3 as a partial signal and adds the declared kind graph; until MX-c-21 ships declarations, Graph tools without a scope entry read undeclared (75 of 86 on the real registry, measured by the worker).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "drain commit 8310672247: pe1.AC1 named tests PASSED 10 of 10, pe1.AC2 103 passed 0 failed, seam test failures 0 (re-run by the issuer on the shared tree)",
      "org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pe-1.breakdown-groups-by-source.md AMENDMENT 1 (@7cdca27ebd) and AMENDMENT 2 (@33932ee038)"
    ]
  },
  "spec_asserts": "Z-W31-S2 asserted that rule 3 placed only 11 of the tools that use Graph in Microsoft 365 and left others undeclared.",
  "world_is": "True and now stated: the page shows them as No source declared (a gap, labelled so) until the catalog declares kind graph; no hand-kept list was added.",
  "notes": "Filed by the issuer, the disarm_owner of record, in the drain of MP-pe-1 (merged @8310672247)."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-15T21:30:41Z",
  "disposition": "DISMISSED_WITH_REASON",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "id": "NFRA_MCPORTAL-Z-S58",
  "one_line": "Z-W31-S3 is DISARMED: the seam assertion no longer names a group for send_email; the seam comparison of every person's holdings is unchanged.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "dismissal_reason": "Disarms NFRA_MCPORTAL-Z-W31-S3. The assertion pinned the old default (m365); Amendment 2 changed that one line to say BOSS holds send_email and the population does not, under whichever group the breakdown gives it.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "drain commit 8310672247: pe1.AC1 named tests PASSED 10 of 10, pe1.AC2 103 passed 0 failed, seam test failures 0 (re-run by the issuer on the shared tree)",
      "org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pe-1.breakdown-groups-by-source.md AMENDMENT 1 (@7cdca27ebd) and AMENDMENT 2 (@33932ee038)"
    ]
  },
  "spec_asserts": "Z-W31-S3 asserted that the seam test could not pass while send_email was kept out of m365.",
  "world_is": "The seam test passes with the one line changed (worker report, issuer re-run 103 passed).",
  "notes": "Filed by the issuer, the disarm_owner of record, in the drain of MP-pe-1 (merged @8310672247)."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-15T21:30:41Z",
  "disposition": "DISMISSED_WITH_REASON",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "id": "NFRA_MCPORTAL-Z-S59",
  "one_line": "Z-W31-S4 is CLOSED: the AC1 and AC2 expect lines are re-cut to patterns the checker matches, and the instance validated.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "dismissal_reason": "Closes NFRA_MCPORTAL-Z-W31-S4. The expect form was the issuer's: the script prints three lines. Amendment 2 re-cut both expects with the sibling pattern form.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "drain commit 8310672247: pe1.AC1 named tests PASSED 10 of 10, pe1.AC2 103 passed 0 failed, seam test failures 0 (re-run by the issuer on the shared tree)",
      "org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pe-1.breakdown-groups-by-source.md AMENDMENT 1 (@7cdca27ebd) and AMENDMENT 2 (@33932ee038)"
    ]
  },
  "spec_asserts": "Z-W31-S4 asserted the AC1 expect could not match the script's three-line output.",
  "world_is": "proof-of-spec-check.py reads the instance VALID rc=0 with the re-cut expects.",
  "notes": "Filed by the issuer, the disarm_owner of record, in the drain of MP-pe-1 (merged @8310672247)."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~31",
  "surfaced_at": "2026-10-15T21:27:08Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "id": "NFRA_MCPORTAL-Z-W31-S5",
  "one_line": "MP-pf-1 leaves open whether a non-empty vendor or firm is stored as read or stripped; the worker stores it stripped, so ' Acme ' and 'Acme' merge into one segment.",
  "spec_asserts": "MP-pf-1 section 1 item 1: a vendor or firm that is missing, not a string, or empty (after strip) reads as the literal string unresolved. The order does not say what a non-empty value is stored as.",
  "world_is": "app/admin_gateway_breakdown.py _segment_fields_for stores a non-empty string STRIPPED of surrounding whitespace, so a row with vendor ' Acme ' and a row with vendor 'Acme' fall in one (vendor, firm) segment. The choice is the worker's, not the order's. No criterion depends on it: the real catalog carries no vendor or firm yet (real _compute run: no channel carries segments).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "READ infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py at 8310672247 plus the MP-pf-1 edit in this commit: helper field() returns raw.strip() for a non-empty string",
      "RAN pf1.AC1.sh in worktree C:/tmp/mp-pe-31: 'segment tests: ... 26 passed' and 'named tests PASSED 6 of 6' RESULT: PASS exit=0; no test plants a padded value, so the stripping is unpinned by the suite"
    ]
  },
  "notes": "Not repaired: the stripping stands as built and is stated here for the issuer to confirm or reverse. A reversal changes one line in field() and no test."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~31",
  "surfaced_at": "2026-10-15T21:41:40Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "id": "NFRA_MCPORTAL-Z-W31-S6",
  "one_line": "A correction to S5: the real catalog's tool_index block carries no vendor or firm, but 'firm' appears 273 times on channel and silver rows with another meaning (an owning firm, e.g. opal-internal, 49financial).",
  "spec_asserts": "MP-pf-1 section 1: the segmentation key is C-GROUP: tool_index rows carry bucket, vendor and firm on opal-data-assets and opal-data-bd rows, and the catalog carries them only after a later release.",
  "world_is": "DATA_CATALOG.yaml, tool_index block (lines 1349-2478 at the worktree's HEAD 43f62f5be7): zero vendor lines, zero firm lines, zero source_group lines. The file holds 273 'firm:' lines outside that block: on channel artifact rows (lines 93-1206, e.g. 'firm: opal-internal', 'firm: cottonwood') and on silver and portal rows (lines 2545 onward, e.g. 'firm: 49financial', 'firm: inflection'). Those are owning-firm values. The tool_index reader reads only the tool_index block, so these never reach the segmentation. S5's world_is said the catalog carries no vendor or firm; that was too broad and is corrected here, S5 is not edited.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "GREP of app/refs/DATA_CATALOG.yaml in worktree C:/tmp/mp-pe-31: pattern source_group, 0 occurrences; pattern vendor or firm at line start, 273 occurrences, all 'firm:'; top-level keys at lines 1349 (tool_index) and 2479 (silver_datasets)",
      "READ app/refs/DATA_CATALOG.yaml lines 84-97 at 43f62f5be7: a channel artifact row carries firm: opal-internal beside entity, verdict_class and pages"
    ]
  },
  "notes": "Not repaired: the catalog is the issuer's (outside this order's write surface). A future C-GROUP release that writes tool_index vendor and firm keeps the same key names as these owning-firm keys: the issuer should confirm the key is read only from tool_index, which the handler does."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W33-S1",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~33",
  "surfaced_at": "2026-10-15T20:59:16Z",
  "one_line": "MP-pf-2 asks for each segment's margin-top to be one grid step; DESIGN.md names no grid step, so the margin is spacing.sm 20px, the gap DESIGN C10 names between two panels or sections.",
  "class": "OBSERVATION",
  "spec_asserts": "MP-pf-2 section 1 item 3: each segment has clear space around it, a hairline-bordered panel inside its bucket panel with a margin-top of one grid step.",
  "world_is": "portal/DESIGN.md (the worker worktree copy, lines 381-383, clause C10) names spacing.sm 20px as the gap between two panels or sections on one page; the document names no grid-step token. gateway.css sets .gateway-segment margin-top to var(--space-sm, 20px), which is an interpretation of 'one grid step' and not a named step.",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "READ C:/tmp/mp-pf-33/portal/DESIGN.md lines 379-390 (C10, Space, shape, depth) in the worker worktree at the start of this cell",
      "GREP C:/tmp/mp-pf-33/portal/DESIGN.md for grid|step|spacing.(xs|sm): hits at lines 382, 383, 388 and 420 name spacing.sm and spacing.xs; no hit names a grid step",
      "mcportal commit 89dd5f5, file src/pages/gateway/gateway.css: .gateway-segment margin-top var(--space-sm, 20px)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not a hazard and no disarm is owed. The issuer may name the step; the page reads the same at either value until a second value is chosen."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W33-S2",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~33",
  "surfaced_at": "2026-10-15T21:57:56Z",
  "one_line": "AMENDMENT 1 (d) says the Gateway h1 renders as the browser default; App.css already sets .mcp-page h1 to the DESIGN.md page-title values and App.tsx imports it.",
  "class": "OBSERVATION",
  "spec_asserts": "MP-pf-2 AMENDMENT 1 (d): the Gateway h1 renders as the browser's default 2em black heading; make it use the DESIGN.md page-title style with the existing tokens.",
  "world_is": "mcportal/src/App.css lines 11-18 (commit d6c4254, unchanged from 2fdfb60) already set .mcp-page h1 to Lato, weight 700, font-size 2.4554rem, line-height 1.2, color #000000, the DESIGN.md page-title values; mcportal/src/App.tsx line 12 imports App.css and the Gateway div carries class mcp-page. The default heading the issuer saw is therefore a render made without App.css. Built: the h1 takes class gateway-title and gateway.css .gateway-title holds the same values, so the title is the DESIGN.md style whether or not App.css loads. DESIGN.md names the style, so the navy fallback was not taken.",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "READ C:/tmp/mp-pf-33/mcportal/src/App.css lines 11-18 at mcportal d6c4254: .mcp-page h1 carries the DESIGN.md page-title values",
      "GREP C:/tmp/mp-pf-33/mcportal/src for App.css: C:/tmp/mp-pf-33/mcportal/src/App.tsx:12 imports './App.css'",
      "RENDER headless Edge of the fixture page (.scratch/gw.html) showed the title in black at the top of the page"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not a hazard and no disarm is owed. The issuer may confirm the render source of the default heading it reported."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W33-S3",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~33",
  "surfaced_at": "2026-10-15T21:57:56Z",
  "one_line": "AMENDMENT 1 (b) says the summary table is the one table without a scroll box; the inherited commit 89dd5f5 already wraps it, so (b) holds and nothing changed.",
  "class": "OBSERVATION",
  "spec_asserts": "MP-pf-2 AMENDMENT 1 (b): the summary table sits in a div className gateway-scroll too (it is the one table that does not today).",
  "world_is": "At the base 2fdfb60, GatewayView.tsx carries no gateway-scroll. The inherited commit 89dd5f5 SummaryTable (GatewayView.tsx line 145) already returns its table inside div className gateway-scroll. Amendment (b) holds at d6c4254 and was checked by the grep of SummaryTable, not by a change.",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "GREP of C:/tmp/mp-pf-33/mcportal/src/pages/gateway/GatewayView.tsx: SummaryTable returns div className gateway-scroll around table gateway-summary (line 145-146)",
      "git show 2fdfb60:src/pages/gateway/GatewayView.tsx | grep gateway-scroll printed no line (base has no scroll box)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not a hazard. The amendment's premise about today's state describes the base, not the inherited build."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W33-S4",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~33",
  "surfaced_at": "2026-10-15T21:57:56Z",
  "one_line": "A 390 px check could not be taken: headless Edge laid the fixture out at 477 CSS px although --window-size was 390, so the horizontal-overflow reading is at 477, not 390.",
  "class": "OBSERVATION",
  "spec_asserts": "MP-pf-2 AMENDMENT 1 (c): check at 390 px that section and segment headings wrap between words only, and change nothing if it already holds; the page must never scroll sideways at 390 px.",
  "world_is": "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe --headless --window-size=390,2600 --dump-dom printed data-sw=477/477 (scrollWidth/clientWidth), so the viewport was 477 CSS px. The --screenshot file is 390 px wide and crops the layout at its right edge. No measurement at 390 CSS px was obtained. At 477 px the headings wrap between words and each tools table scrolls in its own box; this is an observation at 477, not a 390 px result.",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "RUN msedge --headless --window-size=390,2600 --dump-dom on file:///C:/tmp/mp-pf-33/.scratch/gw.html printed data-sw=477/477",
      "READ C:/tmp/mp-pf-33/.scratch/gw390.png: 390 px wide, layout cropped at the right edge"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not a hazard. The 390 px overflow and heading check is left to the issuer's own render; the worker's reading is recorded as a 477 px observation."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W33-S5",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~33",
  "surfaced_at": "2026-10-15T21:57:56Z",
  "one_line": "The order names the workspace branch wk-NFRA_MCPORTAL-pf-33; the worktree is on wk-NFRA_MCPORTAL-33 and the mcportal branch is wk-NFRA_MCPORTAL-33-mcportal.",
  "class": "OBSERVATION",
  "spec_asserts": "MP-pf-2 section 1: the workspace worktree C:/tmp/mp-pf-33 is on branch wk-NFRA_MCPORTAL-pf-33 and the mcportal worktree on wk-NFRA_MCPORTAL-pf-33-mcportal.",
  "world_is": "git rev-parse --abbrev-ref HEAD in C:/tmp/mp-pf-33 printed wk-NFRA_MCPORTAL-33; in C:/tmp/mp-pf-33/mcportal it printed wk-NFRA_MCPORTAL-33-mcportal. The grant is on the branch actually checked out; the order's branch name differs by the pf segment. No commit or branch was moved.",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "RUN git rev-parse --abbrev-ref HEAD in C:/tmp/mp-pf-33 printed wk-NFRA_MCPORTAL-33 (first act of this re-seat)",
      "RUN git -C C:/tmp/mp-pf-33/mcportal rev-parse --abbrev-ref HEAD printed wk-NFRA_MCPORTAL-33-mcportal"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not a hazard. The re-seat proceeded on the checked-out branches."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W33-S6",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~33",
  "surfaced_at": "2026-10-15T21:57:56Z",
  "one_line": "The worker face's read window (offset 1, limit 131) reaches the RECORD FACE marker at line 127, so the read returned lines 127-131 that the instruction said not to take.",
  "class": "OBSERVATION",
  "spec_asserts": "The re-seat prompt: read the order file lines 1 to 131, stop at the last line before the RECORD FACE marker, and if the marker is within the first 131 lines do not read past it.",
  "world_is": "The marker sits at line 127 of the order file, inside the 131-line window, so the window itself contains lines 127-131 (the marker and the ISSUER NOTES). The read returned them. No step was taken from them; the order's worker face was used for every act.",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "READ C:/tmp/mp-pf-33/org/missions/D6/NFRA/NFRA_MCPORTAL/task-orders/NFRA_MCPORTAL.TO-MP-pf-2.gateway-page-segments-by-bucket-and-vendor-firm.md offset 1 limit 131: the output ends at line 131 with the ISSUER NOTES",
      "the marker line RECORD FACE -- does NOT travel to the worker sits at line 127 of the same file"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not a hazard. Recorded because the read window and the stop instruction in the spawn prompt cannot both hold; the issuer may cut the read to lines 1 to 126."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W33-S7",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~33",
  "surfaced_at": "2026-10-15T23:07:00Z",
  "one_line": "The AC1 check takes its root from the shell's current directory (_root.sh runs git rev-parse --show-toplevel), and the shell resets to the primary checkout between calls, so the recorded invocation reads the wrong tree unless wrapped in a cd.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "spec_asserts": "MP-pf-2 order section 4 and the amendment 2 closing line: run the AC1 invocation from the WORKSPACE worktree root C:/tmp/mp-pf-33, with no cd prefix in the recorded invocation.",
  "world_is": "pc/checks/_root.sh cd's to git rev-parse --show-toplevel of the CURRENT directory (C:/tmp/mp-pf-33 is the root only when the shell starts there). Run from the shell's default directory (C:/Users/Opal Bloomberg/Desktop/ajb_workspace) the unchanged invocation printed 'mcportal/src/pages/gateway absent' and RESULT: FAIL, exit=1. Run with a cd to C:/tmp/mp-pf-33 wrapped around the unchanged invocation it printed 70 pass, 0 fail, 9 of 9 named tests, RESULT: PASS, exit=0. The check's verdict is therefore a function of the cwd it is started in.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "RUN bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pe/checks/pf2.AC1.sh from the shell default directory printed 'mcportal/src/pages/gateway absent', RESULT: FAIL, exit=1 (2026-10-15 session, amendment 2 pass)",
      "READ C:/tmp/mp-pf-33/org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pc/checks/_root.sh lines 3-6: _R from git rev-parse --show-superproject-working-tree, else --show-toplevel, then cd \"$_R\"",
      "RUN cd /c/tmp/mp-pf-33 && bash .../pe/checks/pf2.AC1.sh printed '9 of 9', 'pass=70; fail=0', RESULT: PASS, exit=0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not a fault in the mcportal change: the 70-pass run was on the committed tree 421f8fb. The recorded invocation text is unchanged; the cd is a harness wrapper, because the order's no-cd form cannot reach the worktree from a reset shell. A run from the primary checkout grades that checkout's tree, not MP-pf-2's. Disarm for the issuer: pin the check's root to the worktree it grades, or name the cwd in the invocation."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-15T23:22:20Z",
  "disposition": "DISMISSED_WITH_REASON",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "id": "NFRA_MCPORTAL-Z-S60",
  "one_line": "Z-W33-S7 is DISARMED: the AC1 'absent' line was the worker's own parallel-call slip; pf2.AC1.sh passes from the worktree root and the issuer re-ran it there.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "dismissal_reason": "Disarms NFRA_MCPORTAL-Z-W33-S7. The worker ran the check in parallel with its cd, so it read the wrong directory (its own report says it re-ran in sequence). The checks take their root from the worktree root by design, and the order says to run them from there. The issuer re-ran pf2.AC1 from C:/tmp/mp-pf-33: 9 of 9 named tests, pass=70, fail=0, RESULT: PASS.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "drain commit 7772bf7d1b message: pf2.AC1 re-run by the issuer, 9 of 9 named tests, bun 70 pass 0 fail",
      "worker report: the false 'absent' line came from a parallel call, not from the check"
    ]
  },
  "spec_asserts": "Z-W33-S7 asserted that AC1 takes its root from the shell's current directory, so a run from the default directory fails.",
  "world_is": "True, and by design: every pf check begins by changing to the worktree root named in the order; run from there it passes.",
  "notes": "Filed by the issuer, the disarm_owner of record, in the drain of MP-pf-2 (merged @7772bf7d1b)."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~31",
  "surfaced_at": "2026-10-15T23:23:18Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "id": "NFRA_MCPORTAL-Z-W31-S7",
  "one_line": "MP-pf-3 builds the serves list and the store kind, but the real catalog carries neither: no tool_index row has serves or a store source_group, so the real breakdown shows no store group and no segment.",
  "spec_asserts": "MP-pf-3 section 1 A and B: the catalog's tool_index carries serves lists on the opal-data-assets and opal-data-bd tools, and writes kind store for the sources that are neither S3 buckets nor Microsoft graph (YCharts, the Kuzu graph, DynamoDB).",
  "world_is": "app/refs/DATA_CATALOG.yaml at 994447aa53 (this order does not change the catalog): from line 1349 (tool_index) on, zero serves lines, zero kind store lines and zero source_group lines. The real _compute run with an offline scan stub and an empty store lists 86 distinct tools in 2 channels: m365 (11 tools) and undeclared (75 tools). No bucket, store or integration channel exists and no channel carries segments. The new behaviour is exercised only by the planted tests.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "GREP of app/refs/DATA_CATALOG.yaml in worktree C:/tmp/mp-pe-31 from line 1349: source_group, kind: store and '^  (vendor|firm|serves):' each 0 matches; the serves lines above line 1349 are channel descriptions, not tool_index rows",
      "RAN .scratch/real_run.py in worktree C:/tmp/mp-pe-31: _compute(scan_client=EmptyScan(), store=EmptyStore()) printed 'tools listed (distinct): 86', 'channels: 2', 'm365 kind=native tools=11 segments_key=False', 'undeclared kind=undeclared tools=75 segments_key=False', 'any channel carries segments: False'"
    ]
  },
  "notes": "Not repaired: the catalog is the issuer's, outside this order's write surface. Related to NFRA_MCPORTAL-Z-W31-S6, which records the absence of tool_index vendor and firm; this row records the absence of serves lists and of store declarations, which S6 does not cover."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~31",
  "surfaced_at": "2026-10-15T23:23:18Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "id": "NFRA_MCPORTAL-Z-W31-S8",
  "one_line": "MP-pf-3 closure: the task order's <status> flip to complete is not made by this worker, because the order file is outside the worker's write grant.",
  "spec_asserts": "The standing worker rule for a passing proof: flip the task order's <status> to complete and commit the instance, the deliverables and the flip together.",
  "world_is": "The order's <paths> (worker face, section 3) name the admin_gateway_breakdown.py and test_admin_gateway_breakdown.py files, the deliverables folder and the surprise-channel investigations folder; the task-order file is not among them. The worker face (lines 1-85) carries no <status> tag, and its section 5 names no flip. The instance is written and checked; the flip is left for the issuer.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "READ the task order worker face, lines 1-85 (offset 1, limit 85), in worktree C:/tmp/mp-pe-31: section 3 <paths> lists four surfaces; no <status> tag appears in lines 1-85",
      "READ section 5 of the worker face (WHEN YOU ARE DONE): write the instance, run proof-of-spec-check.py, report once; no flip is named"
    ]
  },
  "notes": "Not repaired: the status is the issuer's to set. Whether a worker writes its own status flip is a decision for the issuer (2.0.0_SA_COO~MP)."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~35",
  "surfaced_at": "2026-10-16T03:25:58Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "id": "NFRA_MCPORTAL-Z-W35-S1",
  "one_line": "MP-pf-5 AC1 as written has no working-directory anchor: the shell resets to the primary checkout between calls, so the literal invocation graded the primary tree and read RESULT: FAIL; the root-anchored run needs a cd the criterion does not name.",
  "spec_asserts": "Face section 4: the AC1 invocation is the literal 'bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf5.AC1.sh; echo exit=$?', run from the WORKSPACE worktree root C:/tmp/mp-pf-35.",
  "world_is": "Two Bash calls in the worker session: call 1 'cd C:/tmp/mp-pf-35 && pwd' printed /c/tmp/mp-pf-35; call 2 (the literal invocation, nothing else) printed the working directory C:/Users/Opal Bloomberg/Desktop/ajb_workspace, the check printed 'mcportal/src/pages/gateway absent' and 'RESULT: FAIL', exit=1. The check takes its root from the current directory (_root.sh), so the literal grades whichever tree the shell sits in. The only root-anchored run was one call with the cd prefixed; proof-of-spec-check.py refuses that instance as invocation-alignment[AC1] (the recorded invocation differs from the criterion by the cd). Same class as NFRA_MCPORTAL-Z-W33-S7 (ARMED).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "RAN the literal AC1 invocation in a call whose first act was a bare pwd: output 'C:/Users/Opal Bloomberg/Desktop/ajb_workspace', 'mcportal/src/pages/gateway absent', 'RESULT: FAIL', 'exit=1' (worker session, 2026-10-16T03:25:58Z)",
      "RAN proof-of-spec-check.py on the instance with ids AC1: rc=1, 'VIOLATION: invocation-alignment[AC1]: the RECORDED invocation is NOT the criterion's invocation'"
    ]
  },
  "notes": "Not repaired: the criterion text and pf5.AC1.sh are the issuer's (face section 2, bound 3). The worker records the invocation it ran, with the cd, so the instance is INVALID and the order stays open; the issuer decides whether the criterion or the check script carries the root."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-16T03:37:23Z",
  "disposition": "DISMISSED_WITH_REASON",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "id": "NFRA_MCPORTAL-Z-S61",
  "one_line": "Z-W35-S1 is DISARMED: the AC1 invocation now names its own cd (amendment d4d4311f15, on the worker branch at e70ad4d292), and the instance re-run under it is VALID.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "dismissal_reason": "Disarms NFRA_MCPORTAL-Z-W35-S1. The worker was right and the order was wrong: pf5.AC1.sh takes its root from the shell's cwd and a worker's shell resets to the primary checkout between calls, so the literal invocation graded the wrong tree. This is the second time in a day (Z-W33-S7 read it as a worker slip, Z-S60); the pattern is the issuer's, not the worker's. Repair: the criterion's invocation carries `cd C:/tmp/mp-pf-35 &&` (amendment commit d4d4311f15, no check script, expectation or path changed); the worker re-ran under it and the instance is VALID (worker commit d86d8c3f57, proof-of-spec-check.py rc=0).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "amendment d4d4311f15 on box/sitez and e70ad4d292 on wk-NFRA_MCPORTAL-35: the AC1 invocation text now begins `cd C:/tmp/mp-pf-35 &&`",
      "worker report: AC1 PASS 71 of 71, fail 0, instance VALID rc=0, recorded invocation byte-equal to the criterion text"
    ]
  },
  "spec_asserts": "Z-W35-S1 asserted that MP-pf-5 AC1 as written has no working-directory anchor, so the literal invocation read RESULT: FAIL from the primary checkout.",
  "world_is": "True. Amended: the invocation anchors its own directory. The lesson for every later cell: a check that derives its root from cwd goes in the order with its `cd` written in the invocation.",
  "notes": "Filed by the issuer, the disarm_owner of record, in the drain of MP-pf-5."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~37",
  "surfaced_at": "2026-10-16T04:07:14Z",
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "id": "NFRA_MCPORTAL-Z-W37-S1",
  "one_line": "safe-commit.sh warned that the hashed client account-id list is absent on this box, so commit ee65a69a0b was not checked for client account ids; the commit landed.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "commit ee65a69a0b on wk-NFRA_MCPORTAL-37: safe-commit output `WARN: client-data-check: hashed account-id list ABSENT at ... .opal/account_id_hashes.txt -- this commit was NOT checked for client account ids`",
      "the captured gate output is at .scratch/r3_w37/commit1.log in worktree C:/tmp/mp-pf-37; the commit's staged set was four deliverable files (digests and counts only)"
    ]
  },
  "spec_asserts": "MP-pf-7 section 1 says commit with .tools/safe-commit.sh; the worker rules say each commit passes the commit gate, and the client-data check runs over the staged set.",
  "world_is": "The client-data check printed WARN: the hashed account-id list is absent at the default path under the user profile (absent is not empty), so the check could not run and the commit was not checked for client account ids. Until the list is placed, every commit on this box carries the same blind spot.",
  "notes": "The order names no owner for the list; the disarm owner is the issuer of record for this order, per the surprise-channel rule. No account id was printed or committed by this order: the committed content is 12-hex digests and counts."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-16T04:15:52Z",
  "class": "OBSERVATION",
  "disposition": "DISMISSED_WITH_REASON",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "id": "NFRA_MCPORTAL-Z-S62",
  "hazard_standing": "INERT",
  "one_line": "Z-W37-S1 is DISARMED for this order: the four committed files hold 12-hex digests, counts and one SSM command id, and the issuer read them for account-id shaped strings itself.",
  "dismissal_reason": "Disarms NFRA_MCPORTAL-Z-W37-S1 as far as MP-pf-7's commits go. The check that could not run (client-data-check, hashed list absent) is replaced for this order by a direct read: a grep of r3_read.txt, r3_run.json, r3_principal_sets.py and test_r3_principal_sets.py for runs of 7 or more digits returned no match, and the files carry digests of tenant and object ids, never a raw id or an account number. The box-level blind spot the worker found is real and is filed apart as Z-S63 with its own owner.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "grep -E -o '[0-9]{7,}' over the four committed worker files: 0 matches (run by the issuer at the drain, merge 9b2c6f0715)",
      "r3_run.json read by the issuer: counts, booleans, one SSM command id"
    ]
  },
  "spec_asserts": "Z-W37-S1 asserted that commit ee65a69a0b was not checked for client account ids.",
  "world_is": "True for the tool; for this order's content the issuer's direct read found nothing account-id shaped.",
  "notes": "Filed by the issuer, the disarm_owner of record, in the drain of MP-pf-7."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-16T04:15:52Z",
  "class": "OBSERVATION",
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "0.0.0_AB_MSTR~Z",
  "id": "NFRA_MCPORTAL-Z-S63",
  "hazard_standing": "ARMED",
  "one_line": "The client-data check has no hashed account-id list on site Z: ~/.opal exists but account_id_hashes.txt is absent, so safe-commit prints WARN and checks NO commit on this box for client account ids.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ls of C:/Users/Opal Bloomberg/.opal at ~04:1xZ: the directory holds ps-lock only; test -f account_id_hashes.txt: ABSENT",
      "worker 0.9.0_WK_NFRA_MCPORTAL~37's safe-commit output on commit ee65a69a0b (row Z-W37-S1): WARN: client-data-check: hashed account-id list ABSENT",
      ".tools/git-hooks/client-data-check.py names the file (the only first-party reference)"
    ]
  },
  "spec_asserts": "CLAUDE.md rule 14 and the commit gate: every commit passes the pre-commit gates, one of which is the client-data check.",
  "world_is": "The check degrades to WARN when the list is absent, so it never refuses; every seat's commit on site Z since the list went missing is unchecked. How the list is produced and distributed is not measured here.",
  "notes": "Filed by the issuer as the box-level carrier of the worker's observation; the issuer cannot place the list (an infrastructure act). Not known: when it went missing, or whether another box has it."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-16T11:05:20Z",
  "disposition": "UNDER_INVESTIGATION",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "id": "NFRA_MCPORTAL-Z-S64",
  "one_line": "On the SERVED breakdown the Gateway page scrolls sideways at 390 px (scrollWidth 561 against 390): the channel-level Indexes paragraph holds index names wider than its column, and the fixture's short names never showed it.",
  "spec_asserts": "PF.2 (decomposition v12) and MP-pf-2 section 1: the page itself never scrolls sideways at 390 px; Andrew's words in the order: readable, not wrapped or squished.",
  "world_is": "The issuer rendered the SERVED breakdown body (read over SSM at 10:59:30Z, deployed_commit 0cb4a87bcb, mcportal_commit 090b9cdc85, holders redacted) through the real GatewayView and CSS at mcportal 090b9cdc85, in a real browser at a true 390 px: documentElement.scrollWidth 561 against innerWidth 390. The cause is p.gateway-indexes, the comma-joined list of a channel's index names: one unbroken name such as the commonwealth/cottonwood account-day-value index is about 65 characters, wider than the 328 px column, so the paragraph's content (scrollWidth 530 in opal-data-assets) overflows it and widens the panel and the page. Six sections overflow this way (opal-data-assets 530, opal-data-etfs 382, opal-data-harvest 438, opal-data-portal-v2 433, Dynamodb 359, the Portal precomputed objects group 462, each against 328). The fixture of MP-pf-2 carries short names (idx-positions), which is why AC1's nine tests and the fixture render at 390 px passed. The 1280 px render is unaffected.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "deliverables/2.0.0_SA_COO~MP/pf/evidence_s1_served_0cb4a87bcb/s1_390_page_scrolls_sideways_harvest.png: the page scrolled right by 171 px, the panel ends and empty canvas continues (a section with no account-shaped text, chosen so the image carries none)",
      "browser measurements at a true 390 px viewport: scrollWidth 561; p.gateway-indexes clientWidth 328, scrollWidth 530 (assets), 438 (harvest), 433 (portal-v2), 462 (mdpf group); every .gateway-scroll box is cut and carries the cue",
      "the served body read by deliverables/2.0.0_SA_COO~MP/pf/checks/s1_served_body.sh (ssm command cb52e893): 14 channels, 127 tools, holders redacted before anything was written"
    ]
  },
  "notes": "Screenshots of the full page and of the assets segments are NOT committed: the real index names carry Schwab master numbers (8-digit runs) and this box's client-data check is not running (Z-S63). The fix is small and LOCAL: let the Indexes paragraph (and any other prose that can hold an unbroken name) scroll inside its own box with overflow-x auto, add a real 60-plus character index name to the checked-in fixture so the 390 px render sees it, and a test pinning the rule. The disarm is that cell; it needs the CTO's analysis to carry it (a defect found at the close is the next round's first item). The legibility grade (S1 item iii) reads FAIL until it lands."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W38-S1",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~38",
  "surfaced_at": "2026-10-16T11:32:49Z",
  "one_line": "pf8.AC2 offenders=0 cannot be met as ordered: with the .gateway-indexes rule (overflow-x auto) the Indexes paragraph is the only offender, and the one ancestor the measure exempts is a .gateway-scroll box, which the existing test 'every table cell keeps its text on one line' pins to the table count.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "spec_asserts": "pf8.AC2 expects offenders=0 at 390 and 1280 px and defines an offender as an element outside a .gateway-scroll box whose content is wider than its own box, giving the next offender the same treatment (a scrolling box). MP-pf-8 section 2 bounds: every existing test keeps its name and passes, and an existing assertion changes only for an index count or list.",
  "world_is": "At mcportal c66ca82952 (on 090b9cdc85) the long-name render at 390 px reads scrollWidth=390 innerWidth=390 ok=yes, so the page no longer scrolls sideways, but offenders=7, all P.gateway-indexes: the paragraph sits outside any .gateway-scroll box and its 65-character name is wider than its 328 px column. The measure exempts only elements inside a .gateway-scroll box; wrapping the paragraph in one fails gateway.test.tsx line 383, which asserts that the count of that exact marker equals the table count. I did not wrap the paragraph and did not edit the assertion.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "mcportal/src/pages/gateway/gateway.test.tsx@c66ca82952:383 -- expect(tables.length).toBe(html.split('<div class=\"gateway-scroll\">').length - 1)",
      "org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/_gw_measure.cjs@3406cb91b5:14 -- if (e.closest('.gateway-scroll')) continue, the only exemption the offender count applies",
      "pf8.AC2 run 2026-10-16 under timeout 120: 'long names at 390: scrollWidth=390 innerWidth=390 offenders=7 ok=yes P.gateway-indexes,P.gateway-indexes,P.gateway-indexes'; 'long names at 1280: scrollWidth=1280 innerWidth=1280 offenders=0 ok=yes'; RESULT: FAIL, exit=1"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Decision for the issuer: either the table-count assertion or the offender definition is amended, or the paragraph gets a .gateway-scroll wrapper with that assertion amended. The CSS rule itself meets item 1 of the cell (AC1 PASS, 72 pass 0 fail, tsc rc 0, build rc 0). Both the cell's written rule and the existing test are unchanged in their meaning; no existing assertion changed."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W38-S2",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~38",
  "surfaced_at": "2026-10-16T11:32:49Z",
  "one_line": "The pf8.AC2 short-name control no longer measures short names: the cell's own fixture change put the 65-character name into the checked-in fixture, so the control at 390 px reads offenders=1 on the same paragraph.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "pf8.AC2 names the fixture as checked in as the SHORT-name control, and the cell's preface says the fixture's names are short; MP-pf-8 section 1 item 2 adds the 65-character name to that same fixture.",
  "world_is": "At mcportal c66ca82952 the checked-in fixture carries opal_data_assets_silver_commonwealth_cottonwood_account_day_value on the opal-data-assets channel indexes and on commonwealth_get_holdings, so the control is no longer a short-name render: 'short names at 390 (control): scrollWidth=390 innerWidth=390 offenders=1 ok=yes P.gateway-indexes'. Item 2 and the control's premise cannot both hold; this is the same root as W38-S1.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "mcportal/src/pages/gateway/gateway.cgroup.fixture.ts@c66ca82952:28 -- commonwealth_get_holdings indexes now end with the 65-character name",
      "mcportal/src/pages/gateway/gateway.cgroup.fixture.ts@c66ca82952:37 -- the opal-data-assets channel indexes now end with the 65-character name",
      "pf8.AC2 run 2026-10-16 under timeout 120: 'short names at 390 (control): scrollWidth=390 innerWidth=390 offenders=1 ok=yes P.gateway-indexes'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not ARMED: no future normal operation harms through this row; it records that the control's premise does not hold after item 2."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-16T11:54:07Z",
  "disposition": "DISMISSED_WITH_REASON",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "id": "NFRA_MCPORTAL-Z-S65",
  "one_line": "Z-W38-S1 is DISARMED: the AC2 offender rule counted the Indexes paragraph that the fix makes scroll on purpose; the measure was the issuer's defect and is corrected (amendment 0cc50b3652).",
  "dismissal_reason": "Disarms NFRA_MCPORTAL-Z-W38-S1. The worker built the fix correctly (the page no longer scrolls sideways) and refused to wrap the paragraph in a .gateway-scroll box (it would have failed an existing table-count assertion) or to edit that assertion: right on both counts. The check exempted only elements INSIDE a .gateway-scroll box, so a paragraph with overflow-x: auto read as an offender. _gw_measure.cjs now treats any element whose own computed overflow-x is auto or scroll, or that sits inside one, as a scroll box. Proof on both sides, run by the issuer: the base (mcportal 090b9cdc85) FAILS (long names at 390: scrollWidth=557, 16 offenders), the fix (c66ca82952) PASSES (390 of 390 and 0 offenders; 1280 of 1280 and 0; short control 390 of 390 and 0). The worker re-ran under the amended order: AC1 PASS, AC2 PASS, instance VALID (2f6787aff2).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "amendment commit 0cc50b3652 (trunk) and bf17bc7a5f (worker branch)",
      "worker report: AC1 72 of 72 pass, AC2 PASS, proof-of-spec-check rc=0"
    ]
  },
  "spec_asserts": "Z-W38-S1 asserted that the AC2 offender rule and the table-count assertion conflict, so the order cannot pass as written.",
  "world_is": "True of the check as first written; corrected. The assertion at gateway.test.tsx line 383 is untouched and passes.",
  "notes": "Filed by the issuer, the disarm_owner of record, in the drain of MP-pf-8."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-16T11:54:07Z",
  "disposition": "DISMISSED_WITH_REASON",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "id": "NFRA_MCPORTAL-Z-S66",
  "one_line": "Z-W38-S2 is DISARMED: the short-name control read offenders=1 only because the fixture now carries the long name in the assets channel and the measure counted the scrolling paragraph; with the corrected measure it reads 0.",
  "dismissal_reason": "Disarms NFRA_MCPORTAL-Z-W38-S2. Same cause as Z-W38-S1 (the paragraph with overflow-x: auto counted as an offender). The worker's fixture change is the order's step 2 and is correct; the corrected measure reads the short-name control at 390 px as scrollWidth=390, offenders=0.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "issuer run of pf8.AC2.sh against the worker tree c66ca82952 from /c/Users: short names at 390 (control): scrollWidth=390 innerWidth=390 offenders=0 ok=yes"
    ]
  },
  "spec_asserts": "Z-W38-S2 asserted that the fixture change makes the AC2 short-name control read offenders=1.",
  "world_is": "True under the first measure; 0 under the corrected one.",
  "notes": "Filed by the issuer, the disarm_owner of record, in the drain of MP-pf-8."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-S67",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~MQ",
  "surfaced_at": "2026-10-16T12:43:26Z",
  "one_line": "MP-pf-9 step 1 STOPS at the tests: on the release tree rel-nfra-mcportal-pf (cut on live 38fe44d5cb, commit 3cc7017f1f) 11 of 109 tests in tests/test_admin*.py + tests/test_owner_gate.py fail; 5 are the order's excused FileNotFoundError class, 6 are AssertionError and are NOT excused, so the ASK is not written and the pair is not requested.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "run in C:/tmp/mp-pf-rel/infra/aws/ec2/opal-gateway: python -m pytest tests/test_admin*.py tests/test_owner_gate.py -q -p no:cacheprovider => 11 failed, 98 passed.",
      "EXCUSED class (5): test_admin_fabric.py::test_roster_equals_devices_register, test_admin_fabric_calls.py::test_real_capture_calls, test_admin_fabric_calls.py::test_request_accepted_by_open_calls_scan, test_admin_fabric_gitstate.py::test_real_capture_gitstate, test_admin_fabric_overlap.py::test_real_capture_overlap. FileNotFoundError on org/devices/DEVICES.json, .../2.0.0_SA_COO~MP/cp2/fixtures/s3_capture_20261009T0728Z.json, .tools/open-calls-scan.py: git ls-tree reads 0 at live base 38fe44d5cb and 0 in the release tree, 1 at box/sitez HEAD 1a535637fd; all five pass in the main tree at box/sitez HEAD (the second run below, 74 passed).",
      "NOT EXCUSED (6), AssertionError: test_admin_gateway_breakdown.py::test_every_live_tool_in_exactly_one_channel, ::test_real_server_tool_inventory; test_admin_people.py::test_people_lists_every_candidate_even_holding_nothing, ::test_cadence_reads_absent_with_reason, ::test_real_server_people_inventory, ::test_people_principal_never_leaks_into_other_fields. Example: test_real_server_tool_inventory asserts ['opal-data-assets', 'opal-data-etfs', ..., 'dynamodb', ...] == ['m365'] ('environment-as-left'); test_cadence_reads_absent_with_reason asserts {'m365','plantint'} == a set that also holds 'undeclared'.",
      "the same 6 fail when the same selection is run in the main tree at box/sitez HEAD (6 failed, 74 passed over the 6 affected files), so they are not an effect of the release tree's frozen org/ vintage.",
      "census: git diff --stat 38fe44d5cb HEAD names only infra/aws/ec2/EC2_MANIFEST.json (1 insertion, 1 deletion); the diff over infra/aws/ec2/opal-gateway names nothing. Neither failing file contains the string EC2_MANIFEST (grep -c = 0 on both), so the pin change cannot move them. That they also fail at the bare live base is INFERRED from the identical tree, not run."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO MP-pf-9 step 1 Tests: run tests/test_admin*.py tests/test_owner_gate.py on the release tree: 0 failed, except a FileNotFoundError on a repo path outside infra/aws/ec2/opal-gateway/ that reads 0 at the live base and 1 at HEAD and passes at HEAD; 'Any other failure STOPS.'",
  "world_is": "6 AssertionError failures outside that exception, present in the live gateway code and at box/sitez HEAD alike; not caused by this release. Done so far and unaffected: release commit 3cc7017f1f (one pin, 090b9cdc85 -> c66ca82952); resolve-only prints MCPORTAL-RESOLVED @c66ca82952; bun_cache_precheck on the c66ca82952 lockfile reads 77 of 77. NOT done: step 2 (ASK, pair) and step 3 (rollback proof); nothing opened, nothing deployed.",
  "notes": "Ask of the issuer, one line: rule that these 6 are a known pre-existing class for this release (amend the order's test rule and name them), or re-cut the criterion. Nothing is repaired by this seat (BOUNDS 3). On the ruling I resume at step 2 on live base 38fe44d5cb, or on whatever the manifest reads at the GO."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-S68",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~MQ",
  "surfaced_at": "2026-10-16T13:39:21Z",
  "one_line": "MP-pf-9's sparse-checkout list omits /data/mdpf/config/, so the release tree's first deploy run was REFUSED before any upload ('data/mdpf/config/partner_roster.json is missing from the repo'); adding the path and re-running worked.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "first run 2026-10-16T13:19Z: 'ERROR: REFUSED (no upload): data/mdpf/config/partner_roster.json is missing from the repo at /c/tmp/mp-pf-rel -- the artifact would ship without it.' rc=1, 32 s; S3 opal-gateway-latest.tar.gz unchanged (git-ref 38fe44d5cb, 12:18:44Z) and the versioned d14445961d key absent afterwards.",
      "deploy-to-ec2.sh at the live base stages lib/opal_naming.py, data/mdpf/config/partner_roster.json and infra/logic/registry/scopes.json into the artifact (lines 255-263 of that vintage); the order's sparse list covers the parents of the first and third paths but not /data/mdpf/config/.",
      "the file exists at the live base (git ls-tree 38fe44d5cb data/mdpf/config/partner_roster.json = 1). md5 of the three staged files in the release tree equals the host's installed copies (3d309b26..., 2af41e5f..., 9dd54497...), read over SSM before the re-run, so adding the path moved no byte."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO MP-pf-9 step 1: 'If you go sparse, use a NO-CONE pattern list ... The list: /.tools/ /org/ /lib/ /infra/logic/ /infra/aws/terraform/ /infra/aws/lambda/ci/ /infra/aws/lambda/mcportal/ /infra/aws/ec2/ /data/transcripts/scripts/teams/' plus the 12 root blobs, and says a full checkout also works.",
  "world_is": "The list is one path short for the deploy script as it stands at 38fe44d5cb: the act refuses until /data/mdpf/config/ is in the cone. No upload and no restart had happened, so the refusal cost one re-run and nothing else.",
  "notes": "Ask of the issuer: add /data/mdpf/config/ to the sparse list in the next release order's template. This seat added it to its own checkout only; the commit, the census and the signed blast radius did not change."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-S69",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~MQ",
  "surfaced_at": "2026-10-16T13:39:21Z",
  "one_line": "A release tree cannot commit under the tree-local naming gate: safe-commit.sh inside the tree refuses with 'NAMING ERROR ... KeyError: interval_form' because the tree's lib/opal_naming.py and org/standards/NAMING_SCHEMA.json are from different vintages; deploy-to-ec2.sh's own manifest commit fails the same way after a landed deploy.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "release tree cut on 38fe44d5cb: org/standards/NAMING_SCHEMA.json is v1.12 (cadence keys: values, event_form, event_token_regex); lib/opal_naming.py at the same commit reads schema['cadence']['interval_form'] (line 1906). The main tree's schema is v1.17 and carries interval_form.",
      "the manifest commit that deploy-to-ec2.sh runs after a landed deploy was refused for that reason at 13:24Z ('ERROR: Manifest safe-commit failed ... The deploy LANDED -- record manually'); the deploy itself had completed (SSM eb89810b-21a5-4e21-acfc-b16a98791ea1 Success).",
      "running the TRUNK's .tools/safe-commit.sh from inside the release tree commits cleanly (NAMING-GATE: PASS 0 graded), used for every release-branch commit of this order: 3cc7017f1f, d14445961d, bddaf03886, 864f262ffc, f829a3eaa8."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO MP-pf-9 and CLAUDE.md 14a: commits go through .tools/safe-commit.sh; the order expects the wrapper's manifest record to be corrected, not re-done by hand.",
  "world_is": "In a release tree cut from a trunk commit older than the naming schema's last bump, the gate is unusable from inside the tree, so a landed deploy ends with the manifest record uncommitted until the applier commits it by hand.",
  "notes": "No gate was skipped or overridden: the trunk's gate ran against the same diff. Ask of the issuer: say in the next release order that commits run via the trunk's safe-commit.sh from the tree, or decide that the gate's tree-local vintage is the CTO's to fix (the earlier MP-pc-5 and MP-n-4 releases did not hit it)."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-16T13:42:37Z",
  "disposition": "DISMISSED_WITH_REASON",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "id": "NFRA_MCPORTAL-Z-S70",
  "one_line": "Z-S67 is DISARMED: the six stale AssertionError tests it named are repaired on box/sitez (MP-pf-10, drain e6d9142077); the release it stopped (MP-pf-9) proceeded at the issuer's A1 ruling.",
  "dismissal_reason": "Disarms NFRA_MCPORTAL-Z-S67. Its premise held (6 tests failed at the live base for a reason outside the release); the issuer excused them for MP-pf-9 only (A1 66a4be01d8) and cut their repair as MP-pf-10. The five FileNotFoundError tests were never stale tests: they read repo paths absent from the release tree's frozen vintage and pass at HEAD.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "issuer run of pf10.AC1.sh at box/sitez HEAD (70cb2d0c57) from /c/Users: breakdown named tests PASSED 2 of 2, people named tests PASSED 4 of 4, both files 0 failed, RESULT: PASS",
      "issuer run of pf3.AC2.sh against the worker tree 24b766e751: admin suite 116 passed, failed=0, seam test failures=0"
    ]
  },
  "spec_asserts": "Z-S67 asserted that six AssertionError tests in the admin suite fail identically at the live base and at box/sitez HEAD.",
  "world_is": "True when filed (6 failed, 110 passed); at 70cb2d0c57 the two files read 43 passed, 0 failed.",
  "notes": "Filed by the issuer, the disarm_owner of record, in the drain of MP-pf-10. The channel file's existing bytes are untouched (the base is a strict byte prefix of this version)."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-16T14:15:39Z",
  "disposition": "DISMISSED_WITH_REASON",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "id": "NFRA_MCPORTAL-Z-S71",
  "one_line": "Z-S64 is DISARMED: the fix is on the host and the served body no longer scrolls the page sideways at 390 px.",
  "dismissal_reason": "Disarms NFRA_MCPORTAL-Z-S64 (BLOCKING). Its stated condition was that it stays open until the fix is on the host. MP-pf-9 put mcportal c66ca82952 on the host (the sha256 of the host's index.html, routes.json and both assets equal a build of it) and the issuer's real run of the served body through it reads scrollWidth 390 of 390 at 390 px and 1280 of 1280 at 1280 px, 0 offenders at both.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "pf9.AC2.sh (SSM 92387a6f, Success): host bundle == build of c66ca82952: yes; /health=200; no-identity / and /gateway 401",
      "pf9.AC1.sh at box/sitez 7cd690758c: pin c66ca82952, deployed d14445961d, previous 38fe44d5cb, gateway files changed between them 0, ledger entry present and sentinel gone: PASS",
      "pf9.real.sh at 14:08:44Z (the served body of that read: 14 channels, 127 tools, 47 holders redacted): served body at 390: scrollWidth=390 innerWidth=390 offenders=0 ok=yes; at 1280: scrollWidth=1280 innerWidth=1280 offenders=0 ok=yes",
      "two clean images read before keeping: deliverables/2.0.0_SA_COO~MP/pf/evidence_pf9_served_d14445961d/served_390_top.png and served_1280_top.png"
    ]
  },
  "spec_asserts": "Z-S64 asserted that the served Gateway page scrolls sideways at 390 px (scrollWidth 561 of 390).",
  "world_is": "True at 090b9cdc85; at c66ca82952 on the host the same served body reads 390 of 390. The legibility grade (S1 item iii) is the CVO's, and Andrew's own look is call 21d9; neither is claimed here.",
  "notes": "Filed by the issuer, the disarm_owner of record, at the close of MP-pf-9."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-16T14:15:39Z",
  "disposition": "DISMISSED_WITH_REASON",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "id": "NFRA_MCPORTAL-Z-S72",
  "one_line": "Z-S68 and Z-S69 are DISARMED: both are INERT observations of the release procedure, carried into the next release order's template (decomposition PF6.4).",
  "dismissal_reason": "Disarms NFRA_MCPORTAL-Z-S68 (the release tree's sparse list lacked /data/mdpf/config/, so the first deploy run was refused before any upload) and NFRA_MCPORTAL-Z-S69 (a release tree cut on an older trunk cannot run the tree-local naming gate; the applier commits with the trunk's safe-commit.sh from the tree). Neither blocked or changed the act; the issuer rules them into the template and into A2 (the landing is the applier's commit).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "~MQ's rows Z-S68 and Z-S69 (13:39:21Z) and its close report MP-pf-9_CLOSE_REPORT.md: the first run was refused with no upload (S3 latest unchanged); the landed deploy was SSM eb89810b, Success",
      "the release branch could not be merged whole: 24 paths conflicted on the trunk's later gateway code (merge aborted, nothing lost); the landing 34fc561439 carries the three release artifacts and is drained at 7cd690758c"
    ]
  },
  "spec_asserts": "Z-S68 and Z-S69 asserted that the order's sparse list and commit instructions were one path and one step short for a release tree cut on an older trunk.",
  "world_is": "True; the template now says so (PF6.4).",
  "notes": "Filed by the issuer, the disarm_owner of record, at the close of MP-pf-9."
}
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-16T16:32:21Z",
  "disposition": "DISMISSED_WITH_REASON",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "id": "NFRA_MCPORTAL-Z-S73",
  "adjudicates": [
    "NFRA_MCPORTAL-Z-W31-S1",
    "NFRA_MCPORTAL-Z-W31-S2",
    "NFRA_MCPORTAL-Z-W31-S3",
    "NFRA_MCPORTAL-Z-W32-S2",
    "NFRA_MCPORTAL-Z-W33-S7",
    "NFRA_MCPORTAL-Z-W38-S1",
    "NFRA_MCPORTAL-Z-S64",
    "NFRA_MCPORTAL-Z-S67"
  ],
  "one_line": "The issuer closes eight rows it owns, each with its resolution; the earlier disarm rows named their targets in prose only, so comp-surprise still read them OPEN and ARMED.",
  "dismissal_reason": "Z-W31-S1: admin_people.py now takes its placement from bd._group_ids_for_tools (its lines 14-15 and 87-89), no copy. Z-W31-S2 and Z-W31-S3: the landed catalog declares a source for every tool (the served page reads 0 tools declare no source) and tests/test_admin_people.py::test_person_holdings_equal_breakdown_holders passes (admin suite 116 passed, 0 failed, seam 0). Z-W32-S2: a worker now receives the worker face only, in its prompt; the record face never travels. Z-W33-S7: _root.sh derives the root from its own file's location (pc/checks and round5/checks) and orders carry a cd to the worker tree. Z-W38-S1: the issuer amended the offender definition (A1, a scroll box is not an offender) and pf8.AC2 reads 0 offenders at 390 and 1280. Z-S64: the fix is on the host (disarmed by Z-S71). Z-S67: the six tests are repaired (disarmed by Z-S70).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/opal-gateway/app/admin_people.py lines 14-15 and 87-89 read at box/sitez HEAD (the shared placement rule)",
      "pf3.AC2.sh in the MP-pf-10 worker tree and pf10.AC1.sh at trunk HEAD, run by the issuer: admin suite 116 passed, failed=0, seam test failures=0",
      "pf9.real.sh on the served body of 14:08:44Z: 14 channels, 127 tools, 0 tools declare no source; 390 px scrollWidth=390 offenders=0; 1280 px scrollWidth=1280 offenders=0",
      "pf9.AC1.sh and pf9.AC2.sh at box/sitez HEAD: PASS"
    ]
  },
  "spec_asserts": "Z-S61, Z-S62, Z-S65, Z-S66, Z-S70, Z-S71 and Z-S72 each asserted that a named row is disarmed.",
  "world_is": "True in prose; mechanically the target stayed OPEN and ARMED until a row named it in adjudicates (.tools/comp-surprise.py reads only that field and a remediation row). Z-W28-S1 (the REFUSED status of the person-access writer, MP-pd-4's contract) and Z-W32-S1 (portal/DESIGN.md absent in the PE-2 worker worktree; the page's style conformance never graded) are NOT closed here: PD is held by the CTO and the style grade was not made.",
  "notes": "Filed by the issuer, the disarm_owner of record. Carried open on purpose: Z-W28-S1 and Z-W32-S1, with the reasons in world_is. Z-S10 (OBSERVATION, no disposition field) is not a worker row of this seat's round and is left to its owner."
}
```

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-W3-S4",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~3",
    "surfaced_at": "2026-10-17T05:02:46Z",
    "one_line": "GET / returned 200 to the signed-in session of the task order's non-owner account, and the gateway's own access log holds the same 200 in the walk window; the walk stopped at this owner route, so routes 2-13 and GET /sprint were not sent.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~MP",
    "spec_asserts": "MP-v-2 AC1 (PRD acceptance A2): a verified non-owner is refused on every page and every write handler, GET / included, with 403; a 200 on any owner route is a finding and stops the walk (task order section 2, bound 2).",
    "world_is": "GET / answered 200 to the signed-in session at 04:55:48Z (client read, maxRedirects 0), and the gateway access log for the window 2026-10-17T04:52:43Z to 2026-10-17T04:56:48Z holds the 200 (AC1 output: GET /: 403=0 200=1; refused=0 of 13; admitted=1). The walk did not itself verify the signed-in identity; it relies on the task order's named account.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~3/.scratch/walk.log (uncommitted, ignored): '04:55:48.403Z GET / -> 200' and '04:55:48.404Z STOP: 200 on owner route GET /'",
        "org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~3/v2_run.json@86942b2d71: t0=2026-10-17T04:52:43Z, t1=2026-10-17T04:56:48Z",
        "v2.AC1.sh at worktree commit 86942b2d71: 'admin_api.py Route census at HEAD=12 (cut: 12)', 'refused=0 of 13; admitted=1', RESULT: FAIL, exit=1",
        "infra/aws/ec2/opal-gateway/app/owner_gate.py@c529f2936d (git show HEAD): require_owner raises 403 'not the dashboard owner' for a verified identity not on the roster"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Per task order section 2 bound 2 a 200 on an owner route is a finding, not a retry: no further requests were sent from this worker. Nothing was repaired; the gate and the route are outside this worker's paths. The disarm is the issuer's."
  },
  {
    "id": "NFRA_MCPORTAL-Z-W3-S5",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~3",
    "surfaced_at": "2026-10-17T05:02:46Z",
    "one_line": "The read-only path infra/aws/ec2/opal-gateway/ named by the task order is not materialized in this worktree (sparse checkout), so the owner gate and the admin route file were read from HEAD with git show.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Task order section 3: the read-only path infra/aws/ec2/opal-gateway/app/ can be read from the worktree.",
    "world_is": "The worktree has no infra/aws/ec2/opal-gateway/ directory and git sparse-checkout does not list it, while the files exist at HEAD. AC1 reads admin_api.py via git show HEAD, so no criterion was blocked by the gap.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Glob and ls on C:/tmp/mp-v2-3/infra/aws/ec2/opal-gateway/ returned no such directory (worktree c529f2936d)",
        "git show HEAD:infra/aws/ec2/opal-gateway/app/owner_gate.py@c529f2936d returns the file; git show HEAD:infra/aws/ec2/opal-gateway/app/admin_api.py has 12 Route( lines"
      ]
    },
    "disposition": "UNDER_INVESTIGATION"
  }
]
```

```json
{
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-17T05:12:25Z",
  "disposition": "DISMISSED_WITH_REASON",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "id": "NFRA_MCPORTAL-Z-S74",
  "adjudicates": [
    "NFRA_MCPORTAL-Z-W3-S4",
    "NFRA_MCPORTAL-Z-W3-S5"
  ],
  "one_line": "Z-W3-S4 (a 200 on GET / to a non-owner) is DISMISSED: the session that signed in at 04:55:48Z was the dashboard OWNER, so the 200 was correct and the window did not test a non-owner; Z-W3-S5 is DISMISSED as a non-defect.",
  "dismissal_reason": "Z-W3-S4's premise (a non-owner session) is false. The owner roster may hold only andrew@opalinvest.com (owner_gate.validate_owner_emails, a boot guard) and a verified non-owner answers 403. The issuer sent ONE read-only GET /api/admin/whoami through the window's own persistent profile, headless, after the worker's window had closed: status 200 and the returned email is the dashboard owner (printed as true/false only). The walk script never verified the signed-in identity (its worker said so), which is why the worker could not know. Z-W3-S5 (the read-only app path is not in the sparse worktree, read from HEAD with git show) is not a defect.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "worker window 2026-10-17T04:52:43Z to 04:56:48Z (v2_run.json, committed 86942b2d71); sign-in completed 04:55:48Z; the walk's first request GET / answered 200 and it stopped (1 of 13 sent)",
      "v2.AC1.sh re-run by the issuer: GET / 403=0 200=1; refused=0 of 13; admitted=1; RESULT: FAIL (as the worker reported); v2.AC2.sh: GET /sprint 200=2 of 2 (the browser's own page loads, owner session): neither is a test of a non-owner",
      "issuer whoami read through the profile at ~05:0xZ: status 200, email-is-the-dashboard-owner=true"
    ]
  },
  "spec_asserts": "Z-W3-S4 asserted that GET / returned 200 to a non-owner session.",
  "world_is": "The signed-in session was the owner. Nothing in the gateway admitted a non-owner. The MP-v-2 order stays OPEN: a window signed in as Opal Bloomberg (a fresh profile, the account chosen explicitly) is still owed; the first window's AC1 FAIL and AC2 PASS are records of a window that did not test the criterion.",
  "notes": "Filed by the issuer, the disarm_owner of record. The old profile folder (deliverables/0.9.0_WK_NFRA_MCPORTAL~3/.scratch/profile-edge, git-ignored) holds the owner's session cookies; it is left in place and a redo uses a different profile folder."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W16-S1",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~16",
  "surfaced_at": "2026-10-19T17:42:37Z",
  "one_line": "MP-z-6 cannot run its reads: the order names read paths (infra/aws/ec2/EC2_MANIFEST.json, infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py, infra/aws/ec2/opal-gateway/app/integrations/) that the sparse worktree C:/tmp/mp-gw-16 does not materialise; the worker stopped at the first act and did not reconstruct them.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git -C C:/tmp/mp-gw-16 sparse-checkout list (rc=0) prints .tools, infra/logic/registry, lib, org/devices, org/missions/D6/NFRA/NFRA_MCPORTAL, org/modules/graph, org/ref, org/standards; no infra/aws entry.",
      "ls C:/tmp/mp-gw-16/infra/aws/ fails with 'No such file or directory'; ls of infra/aws/ec2/opal-gateway/app/ fails likewise.",
      "git ls-files infra/aws/ec2/opal-gateway at HEAD 9722e32fce3 lists 494 tracked paths; git ls-files --error-unmatch infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py passes: tracked at HEAD, absent on disk.",
      "timeout 120 bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/z6.AC1.sh; echo exit=$? -> 'no run: org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~16/z6_run.json missing or unreadable' / 'RESULT: FAIL' / exit=1 (recorded verbatim in the instance)."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "MP-z-6 section 3 names infra/aws/ec2/EC2_MANIFEST.json, infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py and infra/aws/ec2/opal-gateway/app/integrations/ as read-only paths of this worker, and steps 2 and 3 read the deployed code and the grant store through them; the first-act bar requires the worktree to carry the paths the order names.",
  "world_is": "The worktree is a cone sparse-checkout carrying .tools, infra/logic/registry, lib, org/devices, org/missions/D6/NFRA/NFRA_MCPORTAL, org/modules/graph, org/ref and org/standards only. infra/aws/ is not on disk, though those files are tracked at HEAD 9722e32fce3. The quote's source record under org/tier1_exec/ is also absent from the worktree.",
  "notes": "NFRA_MCPORTAL-Z-W3-S5 recorded the same absence and read the app path from HEAD with git show. This worker did not: the first-act bar says STOP, and reading the named paths out of HEAD is the extraction the bar does not allow. Not repaired here; the cone is the issuer's worktree configuration. No gateway read, store read, vendor call, write or deploy was attempted. AC2 is judgment and is left for 3.0.0_SA_CVO~Z; the verbatim quote is in deliverables/0.9.0_WK_NFRA_MCPORTAL~16/z6_andrew_read.md."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W16-S2",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~16",
  "surfaced_at": "2026-10-19T17:48:29Z",
  "one_line": "The commit-time naming gate printed NAMING ERROR (function-map folder missing) on the proof-instance commit in the sparse worktree and the commit still landed at rc=0; the gate's error does not refuse.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh of 0.9.0_WK_NFRA_MCPORTAL~16 proof instance and session.log (commit 4290f5ef4b4): log line '[naming-gate] NAMING ERROR function-map folder missing: C:/tmp/mp-gw-16/infra/aws/lambda/ci/function-map/ (the Lambda source map is read from this folder; nothing is graded from a copy)'; the same call returned rc=0 and the commit landed (git log --oneline -3 shows 4290f5ef4b4).",
      "The folder sits under infra/aws/, which the sparse cone of C:/tmp/mp-gw-16 does not carry (see NFRA_MCPORTAL-Z-W16-S1). The commit paths were JSON and a text log only; no Lambda source was staged."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "A commit through .tools/safe-commit.sh is refused when a commit-time gate cannot read the source map it grades against; the naming gate is a gate, not a notice.",
  "world_is": "In this sparse worktree the naming gate reports NAMING ERROR for the missing function-map folder and the commit proceeds with rc=0. Any later commit from this worktree that stages a Lambda name would pass this gate ungraded. The commit itself touched no named resource.",
  "notes": "Filed with the proof instance commit, which the surprises list of that instance cites. Not repaired here: the sparse cone is the issuer's worktree configuration, and no gate was edited."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W16-S3",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~16",
  "surfaced_at": "2026-10-19T18:04:01Z",
  "one_line": "MP-z-6 step 2 cannot read code_tools as written: the channel the order's pick rule selects, opal-data-etfs (18 tools, tied with opal-data-portal-v2), is a bucket, and the order's method reads an integration module's IntegrationSpec.tools and register(); no such module exists for it. code_tools is recorded null.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Served _compute over SSM (command 200bedd3-7eab-46c1-8f5e-e199fe3ab0d0, instance i-07dccb1615503ac99, /opt/opal-gateway, import app.server first): CH|opal-data-etfs|tools=18 ; CH|opal-data-portal-v2|tools=18 ; CH|portal_index|tools=6 ; CH|schwab|tools=5 ; CH|ycharts|tools=6 ; CH|blackdiamond|tools=1.",
      "infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py _compute lines 338-364: a tool joins its integration spec's channel first, else a bucket its catalog tool_index row declares as source_group, else Microsoft 365, else No source declared.",
      "Tool lists (command 1998c941-d769-4131-97db-24fa4ec89278): TOOLS|opal-data-etfs = 18 etfs_* names; TOOLS|opal-data-portal-v2 = 18 names."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "MP-z-6 step 2 reads code_tools from the integration module of the channel picked as the most-tools non-m365 channel, via IntegrationSpec.tools and the names its register() passes.",
  "world_is": "Both largest non-m365 channels are buckets at 18 tools. Bucket channels take their tools from catalog tool_index source_group rows, not from an integration spec, so the as-written method has no module to read. The largest integration channel is portal_index at 6 tools.",
  "notes": "Tie broken by page order (kind, then id): opal-data-etfs before opal-data-portal-v2; recorded in z6_run.json. The catalog side was not read in place of the module: the order is exactly as written. Whose fix: the order's pick rule and method disagree for a bucket channel."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W16-S4",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~16",
  "surfaced_at": "2026-10-19T18:04:01Z",
  "one_line": "MP-z-6 step 3 cannot read store_tools as written: ops/schwab_entitlement_admin.py has no read or show subcommand; its subcommands are activate, revoke and deny-backfill, all POLICY writers. store_tools is recorded null.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py (worktree, HEAD 9722e32fce3): _build_arg_parser add_parser calls at lines 442 (activate), 450 (revoke), 458 (deny-backfill); no other subcommand.",
      "Same file: current_state(store, tid, oid) at line 262 is a Python function with no CLI entry. infra/aws/ec2/opal-gateway/ops/schwab_status.py header: read-only HEALTH, CLOSURE and ERROR summary, no per-principal grant.",
      "The page's grant read for opalbloomberg@opalinvest.com (command 200bedd3): how 'data grant revision 1'. That is the gateway's own read, not the operator read the order names."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "MP-z-6 step 3 reads the principal's active grant with the existing operator read, its read/show subcommand, run under the operator role.",
  "world_is": "The ops directory holds no operator-role read or show command for a principal's grant. The only grant reader in the named script is an internal Python function.",
  "notes": "Not substituted: calling current_state from a one-liner under the operator role would be a read the order does not name, and the operator role was not assumed. Whose fix: the order names a subcommand that is absent from the script."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W16-S5",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~16",
  "surfaced_at": "2026-10-19T18:04:01Z",
  "one_line": "MP-z-6 step 3 says the one real principal with a principal_profile, but the served page lists three principals with a data grant revision (andrew rev 1, opalbloomberg rev 1, alyssa rev 5); the principal was chosen by a stated rule.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Served _compute (command 200bedd3): grant_store={'status': 'read', 'principals': 3}; opal-data-etfs holders: andrew@opalinvest.com (master admin; data grant revision 1), opalbloomberg@opalinvest.com (write-capable; data grant revision 1), alyssa@opalinvest.com (write-capable; data grant revision 5).",
      "Holder data-grant tools (command 1998c941): opalbloomberg 5 schwab_* tools; alyssa 4 (no schwab_prepare_download); andrew 5 schwab_* plus blackdiamond_list_fees."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "MP-z-6 step 3 takes the one real principal with a principal_profile, listed by the page with how 'data grant revision n'.",
  "world_is": "Three principals carry a data grant revision. Rule applied: the first principal in page order whose how carries a data grant revision and who is not a master admin, which is opalbloomberg@opalinvest.com.",
  "notes": "The choice changes the comparison: with alyssa, page_holder_tools would hold 4 tools. Recorded so the issuer can name the intended principal."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W16-S6",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~16",
  "surfaced_at": "2026-10-19T19:07:17Z",
  "one_line": "AMENDMENT 1 step 2 picks the integration with the most page tools, and two integrations tie at 6: portal_index and ycharts. The order's tie rule is absent; portal_index was taken as first in page order (kind, then id).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Served _compute over SSM (command 6ced0404-2369-4c13-884a-0eb20f784509, import app.server first): INTEG|portal_index|6 ; INTEG|ycharts|6 ; INTEG|schwab|5 ; INTEG|globgrph|2 ; INTEG|opal_discover|2 ; INTEG|opal_portal|2 ; INTEG|blackdiamond|1 ; INTEG|advi_billing|NO-CHANNEL-ON-PAGE.",
      "Integration directories at the served app: advi_billing, blackdiamond, globgrph, opal_discover, opal_portal, portal_index, schwab, ycharts (INTEGDIRS line of the same run)."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 1 step 2: among integration directories (excluding m365), pick the one whose page channel lists the most tools; an integration with no channel on the page is taken to the next.",
  "world_is": "portal_index and ycharts both list 6 tools on the page. advi_billing has no channel on the page and is skipped. The tie is not decided by the order text.",
  "notes": "Chosen: portal_index, first in the page's own order. Its code_tools (the names its register() passes, read from the deployed artifact) equal its page tools, so the choice does not change AC1's equality for this channel. Recorded so the issuer can name the intended tie rule."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W16-S7",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~16",
  "surfaced_at": "2026-10-19T19:07:17Z",
  "one_line": "The sparse worktree C:/tmp/mp-gw-16 now carries infra/aws/ec2 and shows 11 smartx-exporter scripts as modified (CRLF in the working copy against LF in the index); the commits here name paths and do not stage them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git diff --stat in C:/tmp/mp-gw-16 at HEAD a324cb607e0: 11 files changed, 3109 insertions(+), 3109 deletions(-); the warnings name infra/aws/ec2/smartx-exporter/smartx-workspace/scripts/*.py and config.py: 'CRLF will be replaced by LF the next time Git touches it'.",
      "The files were materialised by the cone change of the issuer's provisioning fix (row NFRA_MCPORTAL-Z-W16-S1); this worker wrote none of them."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The worktree's write surface is the order's paths (deliverables and the surprise channel); a worker commits only those paths.",
  "world_is": "Eleven files outside the write surface show as modified in the worktree from line-ending conversion. They are not part of any commit made here.",
  "notes": "Not repaired and not staged. Every commit in this worker's chain was made with explicit paths through safe-commit.sh."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W16-S8",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~16",
  "surfaced_at": "2026-10-19T19:09:46Z",
  "one_line": "Task-order status flip: the coordinator's message says flip the order's status when every mechanical criterion passes, and AC1 now passes, but the order file is outside this worker's write grant (<paths> names only the deliverables and the surprise channel). The flip is left to the issuer.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "z6.AC1.sh run verbatim (timeout 120): window 2026-10-16T18:30:00Z .. 2026-10-16T19:05:00Z; ssm status=Success; breakdown 200s=24; control-plane data routes 200 (of 4)=4; channel tools code==page: yes; principal tools store==page: yes; RESULT: PASS; exit=0.",
      "The order file NFRA_MCPORTAL.TO-MP-z-6.fwd20-close-run.md carries <status>pending</status>; its path is not in the <paths> block of the order (section 3)."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order is flipped to complete by its worker only when every mechanical criterion passes, and the worker writes only its <paths>.",
  "world_is": "Both conditions cannot be met by this worker at once. AC1 passes; the file that holds <status> is outside the write grant.",
  "notes": "Not repaired: no edit to the order file was made. The instance records the flip as the issuer's. AC2 is judgment and is left for 3.0.0_SA_CVO~Z."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-S75",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~MP",
  "surfaced_at": "2026-10-19T19:18:28Z",
  "disposition": "UNDER_INVESTIGATION",
  "one_line": "DISARMS NFRA_MCPORTAL-Z-W16-S2 (owner this seat) and records the issuer's own cause for Z-W16-S1, S3 and S4: the MP-z-6 worktree was provisioned without the order's read paths (S1), and the order's pick rule and store read were wrong as written (S3, S4); AMENDMENT 1 (2e6385a297) fixed all three and AC1 then passed 4 of 4.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "S2 (naming gate printed NAMING ERROR and the commit landed): the branch wk-NFRA_MCPORTAL-16 changed exactly 8 paths against its base 9722e32fce (git diff --name-only), all deliverables, the investigation file, the order, and two issuer check files; none names a Lambda or any other resource the naming gate grades, so nothing passed ungraded. The worktree C:/tmp/mp-gw-16 is removed at this drain, so no later commit can come from it.",
      "S1: the issuer provisioned C:/tmp/mp-gw-16 with --order, which adds only the folders the order's <paths> names; the order's read-only paths (infra/aws/ec2/...) were not in <paths>, so the cone lacked them. Fixed by adding infra/aws/ec2 to the cone; the worker then read all three.",
      "S3 and S4: the order text said 'the channel with the most tools' (a bucket with no module) and named a store reader that has only writers. Amended in 2e6385a297; the worker's redo ran AC1 to PASS (RESULT: PASS, exit 0, recorded in the proof instance)."
    ]
  },
  "spec_asserts": "NFRA_MCPORTAL-Z-W16-S2 is ARMED with this seat as disarm_owner.",
  "world_is": "S2's hazard cannot fire here: the worktree is gone and the branch staged no graded name. The residue is the gate's behaviour in any SPARSE worktree whose cone omits infra/aws/lambda/ci/function-map: it prints NAMING ERROR and does not refuse. That is carried to the naming gate's owner (0.0.0_AB_MSTR) by this row; this seat builds no gate. Provisioning lesson for the issuer: a read-only path an order names must be added with --sparse-add, because --order adds only <paths>.",
  "notes": "The first spawn stopped at its first act on S1, as the worker bar says it must; the issuer's own mistake cost one worker pass and about 25 minutes."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W41-S1",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~41",
  "surfaced_at": "2026-10-19T19:56:09Z",
  "one_line": "The proof-of-spec checker resolves artifact commits only in the workspace repo; the mcportal commit cb17848 lives in the nested mcportal repo, so the checker reads its three artifact rows UNRESOLVED-HERE. The instance is VALID (rc=0); the schema has no slot for a nested-repo pin.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git -C C:/tmp/mp-gwz-41 cat-file -t cb17848 -> 'fatal: Not a valid object name cb17848', rc=128 (absent from the workspace object store).",
      "git -C C:/tmp/mp-gwz-41/mcportal cat-file -t cb17848 -> 'commit', rc=0 (positive control: present in the mcportal store); git cat-file -t 739e6857a50 in the workspace -> 'commit', rc=0.",
      "python .tools/proof-of-spec-check.py on NFRA_MCPORTAL.TO-MP-z-7.schwab-master-bd-context-line.proof_of_spec.json AC1 -> 'artifact-resolution: 0 resolved at pin / 0 PENDING co-committed / 0 pending-on-worktree / 3 UNRESOLVED-HERE (commit not in local store; announced, not asserted)', then 'VALID (rc=0)'."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "A proof instance's artifact commit_or_etag resolves at its pin in the repo the proof-of-spec checker reads (artifact-resolution limb).",
  "world_is": "The mcportal worktree is its own git repository. Its commit cb17848 is absent from the workspace object store, so the checker announces UNRESOLVED-HERE for all three artifact rows of this instance and resolves none. Verified by hand against the mcportal store only.",
  "notes": "Cited the mcportal commit as commit_or_etag because the schema has no field for a commit in a nested repo; the sibling pf-11 instance cites its mcportal commit the same way. Not repaired here: the checker and its resolution scope belong to the owner of proof-of-spec-check.py. The mcportal commit is LOCAL on wk-NFRA_MCPORTAL-41-mcportal, not pushed."
}
```

```json
{
  "id": "NFRA_MCPORTAL-Z-W43-S1",
  "project": "NFRA_MCPORTAL",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~43",
  "surfaced_at": "2026-10-20T18:38:45Z",
  "one_line": "The face asks for a WIDENING defined against the prior record AND a WIDEN-NO-CONFIRM refusal with zero store calls, but the prior record is readable only through store.get, so the two requirements cannot both hold; the widening rule and its four new named tests are not built.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~MP",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py@ba8cfc3ef39 line 398: prior = _plain_record(st.get(key)) is the only prior-record read. It runs after the shape check (lines 383-385) and the RECORD-KIND check (lines 386-388) and before any write (read by hand at this commit).",
      "infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/tests/test_person_access.py@ba8cfc3ef39 lines 41-43: FakeStore.get appends ('get', key) to store.calls, so any read makes store.calls non-empty; the face's widening test asserts store.calls == [] (face section 1, FWD-26).",
      "Grep -i 'widen|widening_confirm|widening_signoff' over the grant-writer folder at ba8cfc3ef39: no widening_confirm and no widening_signoff anywhere. The 'widen' hits are the grant-level action (lambda_function.py:458-467, tests/test_grant_writer.py:96), not the person_access rule."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "A WIDENING (a change that adds an entry to tools_allow or channels_allow relative to the prior record; a first write counts against an empty prior) is REFUSED WIDEN-NO-CONFIRM when widening_confirm is not exactly True, before any store call (zero store calls). The face's test 2 asserts store.calls == [] for a channels_allow addition with no confirm against an empty store (face section 1, PRD v0.10 FWD-26 writer side).",
  "world_is": "The writer learns the prior record only by a store read (lambda_function.py:398), and FakeStore counts every get as a store call (tests/test_person_access.py:41-43). An exact prior-relative widening decision therefore needs one store call before the refusal, and the zero-call assertion forbids it. Nothing in the writer carries widening_confirm or widening_signoff at base. The face does not say which requirement yields. Built here: only the stale-test repair (commit ba8cfc3ef39). Not built: the widening rule and the four new tests (face tests 2-5).",
  "notes": "Two resolutions the issuer could choose; neither taken here. (a) Read the prior first and drop the zero-call clause for the WIDEN-NO-CONFIRM refusal. (b) Refuse without a read whenever a change names tools_allow or channels_allow with a non-empty list; this over-refuses a re-assertion of an allow entry the prior already holds, a fail-closed deviation from the definition. The face says stop on the criterion and not repair it, so neither was implemented. Stale-test repair: old body had no monkeypatch argument and asserted the REFUSED RECORD-KIND-NOT-LIVE with zero store calls against the live tuple (which now holds person_access); new body narrows acs.POLICY_RECORD_TYPES with monkeypatch for that test, asserts person_access absent, and keeps the same refusal and zero-call assertions. Whole grant-writer suite at ba8cfc3ef39: 36 passed, 0 failed (rc=0)."
}
```
