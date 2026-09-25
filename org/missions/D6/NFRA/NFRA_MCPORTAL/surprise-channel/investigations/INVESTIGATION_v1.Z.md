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
  }
]
```
