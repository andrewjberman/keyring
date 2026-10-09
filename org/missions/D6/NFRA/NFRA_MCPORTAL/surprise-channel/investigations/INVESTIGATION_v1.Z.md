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
  }
]
```
