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
  }
]
```
