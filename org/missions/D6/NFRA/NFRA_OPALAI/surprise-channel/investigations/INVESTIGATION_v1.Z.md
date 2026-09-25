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
    "id": "NFRA_OPALAI-Z-W2-S1",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~2",
    "surfaced_at": "2026-09-24T21:40Z",
    "one_line": "A query_v0 catalog key has no field mapping it onto data_entitlement's `datasets`/`operations` scope dimensions -- the two models are disjoint data domains, so opal_asker_query cannot narrow a catalog fetch by the asker's own dataset scope without inventing a dimension.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "app/data_entitlement.py:64 DATASETS = ('dim_position','dim_balance','dim_asset') and SCOPE_DIMENSIONS carry masters/datasets/accounts/dates/columns/operations for the Schwab custodial grant model.",
        "app/graphql_plumbing/catalog_gate.py:77-122 gate() branches ONLY on principal_class ('opal-internal'|'firm') + principal_firm, read from app/refs/DATA_CATALOG.yaml row fields firm/verdict_class/allowlist/firm_resolution -- no row carries a `dataset` or `operation` field of any kind, checked by reading the file's ~1338 lines (channels: benchmarks_and_models, etf_dashboards, etc., none named dim_position/dim_balance/dim_asset).",
        "app/query_v0.py:82-91 _principal() resolves (principal_class, principal_firm) from the request's own validated email domain -- not from any Schwab scope object at all."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OA-t-5 cell 1: 'Measure how a catalog key maps onto the grant's scope dimensions (datasets, operations). If the model cannot express it without a NEW dimension, REFUSE that part with a row. Never invent a dimension.'",
    "world_is": "asker_scope.py honours the `operations` dimension only (the asker's active grant must carry 'query' or the call is denied before any catalog lookup); it does NOT and CANNOT restrict WHICH catalog keys/channels an asker may reach by their own `datasets` grant -- that axis is governed solely by the calling identity's own principal_class/firm (catalog_gate, unmodified), so two askers with different Schwab dataset grants but the same calling identity see the identical catalog surface through this tool. Left alone through a future deploy, opal_asker_query under-scopes relative to PRD C10's per-asker-entitlement intent for the query_v0 catalog specifically (Schwab-tool scoping is unaffected and correct).",
    "notes": "A real fix needs either (a) a new catalog-row field mapping keys/channels to data_entitlement datasets (an Andrew-ruled schema widening, R-0006/R-0009 four-postulate record required), or (b) a ruling that query_v0's catalog is out of PRD C10's asker-scoping scope entirely (a different, narrower, entitlement domain by design). Both are CTO/COO calls, not a worker's to invent."
  },
  {
    "id": "NFRA_OPALAI-Z-W2-S2",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~2",
    "surfaced_at": "2026-09-24T21:40Z",
    "one_line": "app/audit.py's _ARGS_ALLOWLIST does not declare 'opal_asker_query', so its fail-closed default omits every arg (asker oid/key/verdict included) rather than carrying them -- adding the row is outside this order's <paths>.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "app/audit.py:71-119 _ARGS_ALLOWLIST maps tool name -> allowed field set; _safe_args() returns {'_omitted': ...} for any tool not in that map, per its own docstring 'undeclared field OR unknown tool -> omitted'.",
        "grep of app/audit.py's _ARGS_ALLOWLIST keys (ms_site_children, otp_fetch, whoami, teams_poll, plus the ycharts_/query_v0 rows named in its comment) contains no 'opal_asker_query' entry at fee6c9f89c6178c2e111774d3aa39e3dba3bdebc.",
        "TO-OA-t-5 <paths> lists app/asker_scope.py, tests/test_asker_scope.py, app/tools.py, app/data_entitlement.py and the deliverables/surprise-channel folders only -- app/audit.py is in neither the write list nor the named Read-only list."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OA-t-5 cell 1(f): 'writes an audit row with the asker oid, key and verdict, and no values.'",
    "world_is": "asker_scope.handle_asker_query calls audit.log_call with {asker_oid, key, verdict[, bytes]} on every branch (never a value), so the row lands and never raises; but until app/audit.py adds an 'opal_asker_query' row to _ARGS_ALLOWLIST, the emitted record fail-closed-omits those fields too (stricter than the letter of the criterion, never a widening) -- the audit trail under-delivers, it does not over-disclose.",
    "notes": "A one-line _ARGS_ALLOWLIST addition ({'asker_oid','key','verdict','bytes'}) closes this; it needs a lane that can write app/audit.py, which this order does not grant."
  },
  {
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-24T22:45Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "NFRA_OPALAI-Z-S2",
    "one_line": "DISARMS NFRA_OPALAI-Z-W2-S1 (owner this seat): per-dataset narrowing of opal_asker_query is refused by construction, not silently widened, and the tool is not deployed; the mapping of a catalog key onto a grant dimension is a design decision routed to the round-1 analysis, not a live exposure.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Worker report 0.9.0_WK_NFRA_OPALAI~2 on TO-OA-t-5, branch wk-NFRA_OPALAI-2 @00976eb082: asker_scope.py honours `operations` ('query' required, else denied before any catalog lookup); `datasets` has no field on a DATA_CATALOG.yaml row (firm, verdict_class, allowlist, firm_resolution) to map onto.",
        "Proof instance NFRA_OPALAI.TO-OA-t-5.asker-scoped-query-tool.proof_of_spec.json: proof-of-spec-check rc=0 (VALID), AC1-AC3 PASS-by-output, read by this seat at the drain.",
        "The served host at the drain runs deployed_commit 1764e54a16 (EC2_MANIFEST.json), which carries no asker_scope.py: nothing is live."
      ]
    },
    "spec_asserts": "NFRA_OPALAI-Z-W2-S1 is ARMED with this seat as disarm_owner.",
    "world_is": "The residual is a precision gap, not a breach: an asker with the 'query' operation reaches every catalog key the catalog gate allows their firm, and cannot be narrowed to a subset of keys by grant until a key-to-dataset mapping exists. Refusal, not invention, is what the cell built.",
    "notes": "Routed to the L10 read as an enrichment candidate: give catalog rows a dataset field (or map channels to datasets) so C10's intersection can narrow by key. Owner of the decision: 1.0.0_SA_CTO~O (the PRD). No gate is built here."
  },
  {
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-24T22:45Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "NFRA_OPALAI-Z-S3",
    "one_line": "The runtime agent's identity cannot yet call opal_asker_query: app/identity_scope.py's concierge allowlist does not name it, and its own docstring requires Andrew's ruling to widen -- so FWD-1's close run needs that ruling (a gate, G-SCOPE), not a cell.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Worker report 0.9.0_WK_NFRA_OPALAI~2 on TO-OA-t-5 @00976eb082, declared_exclusions: identity_scope.py outside <paths>; its docstring requires an Andrew ruling to widen the concierge allowlist.",
        "PRD v0.5 C10: the effective scope is the INTERSECTION of the asker's policy and the agent's own identity allowlist -- so the tool must be in that allowlist for any asker to be served."
      ]
    },
    "spec_asserts": "Round 1's thread ends in one live exchange through opal_asker_query (decomposition s.8).",
    "world_is": "Until the allowlist names opal_asker_query, every call from the Opal Bloomberg identity is denied at identity_scope before the asker is resolved; the tool is correct and unreachable.",
    "notes": "Carried to Andrew with the close-run gates (G-ACCT, G-AUTH, G-ASKER, G-PUSH) as G-SCOPE: one line in identity_scope.py's concierge allowlist on his word, then a gateway deploy. Not widened by any worker or by this seat."
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
  },
  {
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-24T23:05Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "NFRA_OPALAI-Z-S4",
    "one_line": "DISARMS NFRA_OPALAI-Z-W1-S1 (owner this seat): the lane resolver returned UNDEFINED for the granted path opal_ai before consulting the worker grant; the worker's audited author override covered exactly its three granted paths, and OA-w-2's lane rows for opal_ai/** close the gap for this project's later nested-path commits.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/git-author-override-audit.log, read by this seat at the drain: 2026-09-24T22:20:40Z BLOCK 0.9.0_WK_NFRA_OPALAI~1 3 (VIOLATION: opal_ai -- UNDEFINED); 22:27:53Z OVERRIDE 3; 22:45:46Z PASS 3.",
        "Branch wk-NFRA_OPALAI-1 @074be9bf5f, git diff --stat fee6c9f89c..HEAD: .gitmodules, .tools/wk-provision.sh, opal_ai (gitlink 160000 90ca424fc7), the proof instance, a session log, the channel -- every staged path inside TO-OA-w-1's <paths> or its deliverables folder.",
        "TO-OA-w-2 <paths> carries .owned-paths.yaml and its cell text lands lane rows for opal_ai/** BEFORE any hook."
      ]
    },
    "spec_asserts": "NFRA_OPALAI-Z-W1-S1 is ARMED with this seat as disarm_owner.",
    "world_is": "No out-of-grant path moved. The residual is the resolver's ordering (a worker grant is never consulted for a path with no lane row), a fabric gate defect whose owner is the gate's, carried to the CTO in this round's drain-end read; NFRA_MCPORTAL's MP-w-1 (the mcportal gitlink) meets the same ordering.",
    "notes": "No gate is built here."
  },
  {
    "id": "NFRA_OPALAI-Z-W4-S1",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~4",
    "surfaced_at": "2026-09-24T21:10Z",
    "one_line": "OA-t-4's move (remove `.claude/skills/teams-assist/teams-watch.py`, change its whole auth model) breaks a LIVE PRODUCTION consumer neither OA-t-1 nor OA-t-4 names: integrations/ticketing/intake/runner.py imports that exact path and calls its read_token()/PIN_SERVER/PIN_IDENTITY/_gateway_call directly as the D7 ticket-intake buzz-send path, fired every 5 minutes by the Windows Scheduled Task OPAL_D7_ticket_intake.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "integrations/ticketing/intake/runner.py@b9da668e16 line 69: TEAMS_WATCH = REPO_ROOT / '.claude' / 'skills' / 'teams-assist' / 'teams-watch.py'; lines 106-115 _load_teams_watch() imports it by that literal path via importlib.util.spec_from_file_location; lines 118-138 gateway_send_factory() sets tw.PIN_SERVER/tw.PIN_IDENTITY module attributes and calls tw.read_token() and tw._gateway_call(...) directly.",
        "runner.py's own header (lines 43-49): 'LIVE PRODUCTION -- executed by the Windows Scheduled Task OPAL_D7_ticket_intake, EVERY 5 MINUTES, FROM THIS WORKING TREE.'",
        "Neither TO-OA-t-1 (product-files-move) nor TO-OA-t-4 (this order)'s <paths> or cell text names integrations/ticketing/intake/runner.py; TO-OA-t-4's own face states the parent copy is 'removed on your branch' as a premise, and TO-OA-t-1's face lists what it moves/removes without this file.",
        "The new opal_ai/opal/agent/teams_watch/teams-watch.py (this order's build) has no read_token() function at all -- ensure_fresh_access_token()/_post_form() replace it -- so even a path re-point in runner.py would not restore the old call shape without its own rewrite."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OA-t-4 section 1: 'Move the file to opal_ai/opal/agent/teams_watch/teams-watch.py (the parent copy removed on your branch)' and AC3: 'no code/config files naming the old path' (grep scope: .claude/, .tools/, org/mcp/, *.ps1).",
    "world_is": "The parent copy was NOT already removed at this order's cut (measured: byte-identical to the pre-move HEAD, git diff b9da668e16..HEAD -- .claude/skills/teams-assist/ empty before this cell's own edit); AC3's grep scope does not reach integrations/ticketing/intake/runner.py, so the check can PASS while a real 5-minute-cadence production consumer starts raising FileNotFoundError/AttributeError on every fire once this branch's removal lands at the round's cutover.",
    "notes": "Not fixed here: integrations/ticketing/intake/runner.py is outside this order's <paths> (write) and outside its named Read-only set. A fix needs either (a) runner.py re-pointed at the new path and rewritten against the new ensure_fresh_access_token()/state-dir contract (its own OAuth client/state, since it cannot share teams-watch's runtime state dir from a workspace-side scheduled task), or (b) a ruling that the D7 runner keeps its own independent, un-migrated copy of the old CREDS-reading logic. Both are CTO/COO calls; named disarm_owner is the issuer per this project's standing 'issuer as disarm_owner' convention."
  }
]
```
