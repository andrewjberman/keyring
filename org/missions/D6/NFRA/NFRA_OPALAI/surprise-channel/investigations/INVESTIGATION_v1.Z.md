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
  }
]
```
