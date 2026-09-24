# NFRA_OPALAI -- surprise channel, INVESTIGATION v1 (site-Z fabric)

**Opened by:** `2.0.0_SA_COO~O`, 2026-09-24, at L5. **Home:** the project tree's channel. Lane `ANY`;
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project).
**Append-only.**

**Id grammar on this fabric:** a seat's row is `NFRA_OPALAI-Z-S<k>`; a worker's row is `NFRA_OPALAI-Z-W<n>-S<k>`
with `<n>` its slot; `<k>` restarts at 1 per coordinate. `"project": "NFRA_OPALAI"` and `"fabric": "site-z"` on
every new row. The CVO's adjudication rows live in `adjudications/`, never here.

---

```json
[
  {
    "id": "NFRA_OPALAI-Z-S1",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-24T21:15Z",
    "one_line": "G-ACCT cannot be a worker act on this box: the fabric session runs at Medium integrity, not elevated, and creating a local account requires elevation, so the runtime account is created by one elevated run of the provisioning script at close.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Measured by this seat 2026-09-24 ~21:1xZ in PowerShell: WindowsPrincipal.IsInRole(Administrator) = False; whoami /groups carries 'Mandatory Label\\Medium Mandatory Level' S-1-16-8192.",
        "Get-LocalUser -Name Opal_Agent: absent at the same read.",
        "PRD v0.3 @1645cbb7ab, SURFACE MANIFEST gates: 'G-ACCT: create the runtime account, an admin act on this box. Holder: a worker under this project, on R1.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A worker under this project creates the runtime account (G-ACCT) as an admin act.",
    "world_is": "A worker is a subagent of a Medium-integrity session; it can build and dry-run the provisioning script, but the account creation needs an elevated shell, which only a person at the box (Andrew or a seat he names in an elevated session) can open.",
    "notes": "The decomposition (s.8) routes the elevated run to Andrew at close and keeps the build in cell OA-t-2, whose script refuses without elevation and changes nothing. No gate is built here."
  },
  {
    "id": "NFRA_OPALAI-Z-W1-S1",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~1",
    "surfaced_at": "2026-09-24T22:30Z",
    "one_line": "owned-paths-validate.py never consults the worker_grant (task-order-paths, ADHC_OWNPTH.005) stanza for a path with ZERO existing lane row -- a worker's own granted-but-brand-new path (opal_ai, the new gitlink) reads UNDEFINED and is refused before check_agent(), which is the only place the stanza is read.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "`printf 'opal_ai\\n.gitmodules\\n.tools/wk-provision.sh\\n' | python .tools/owned-paths-validate.py --check-agent 0.9.0_WK_NFRA_OPALAI~1 .owned-paths.yaml` at wk-NFRA_OPALAI-1 HEAD fee6c9f89c printed exactly one violation: 'VIOLATION: opal_ai -- UNDEFINED (no matching path rule; agent=0.9.0_WK_NFRA_OPALAI~1)'; .gitmodules and .tools/wk-provision.sh (both already carry a lane in .owned-paths.yaml) passed clean.",
        ".tools/owned-paths-validate.py:280-282 (check_agent): `lane_name = resolve_lane(path, paths_config); if lane_name is None: return False  # unmapped path` -- this early return fires BEFORE the ADHC_OWNPTH.005 clause at line 330 (`_owns_task_order_paths`), which lives only inside the `isinstance(permitted, list)` branch reached from an EXISTING lane's own `check_agent` call.",
        ".tools/owned-paths-validate.py:411-416 (the --check-agent CLI loop) independently calls resolve_lane() first and appends the UNDEFINED violation directly, never calling check_agent() at all when lane_name is None -- so a wholly-undefined path never reaches the worker-grant clause by either route.",
        "`.tools/git-hooks/owned-paths-check.sh:11-12,118-121` documents and implements the escape hatch used to land the commit: `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_OPALAI~1 bash .tools/safe-commit.sh ... -- .gitmodules opal_ai .tools/wk-provision.sh` committed 69288c8ca0 (rc=0; every staged path is inside this order's own <paths> grant, so the override crosses no other lane)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order's <paths> block names `opal_ai` as this worker's write surface, and the registry's worker_grant stanza (.owned-paths.yaml:44-47, ADHC_OWNPTH.005) states a worker serial is admitted to exactly the <paths> a non-terminal task order issued_to it names at HEAD.",
    "world_is": "A path with NO existing lane row in .owned-paths.yaml (any first-mint top-level path, not opal_ai-specific) is refused as UNDEFINED before the worker_grant clause is ever consulted, because both the CLI loop and check_agent() return on an unresolved lane before reaching ADHC_OWNPTH.005 -- so the grant only ever supplements an EXISTING lane's permitted_agents, never covers a path that has none. Left alone this refuses every future worker's first commit of a brand-new top-level path (OA-w-2 lands `opal_ai/**` lane rows, which covers the SUBTREE but not the pattern class itself, so the next wholly-new path anywhere in the estate hits the identical wall).",
    "notes": "Not fixed here: .owned-paths.yaml and .tools/owned-paths-validate.py are outside this order's <paths> grant. The commit itself landed clean via the documented override; this row is the standing gate-gap, not a blocked commit."
  }
]
```
