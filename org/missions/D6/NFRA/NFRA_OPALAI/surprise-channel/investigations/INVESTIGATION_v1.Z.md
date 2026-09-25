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
    "id": "NFRA_OPALAI-Z-S5",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~O",
    "surfaced_at": "2026-09-24T23:12Z",
    "one_line": "opal_asker_query lets the AGENT choose which message's sender scopes the answer: it resolves the asker from any (chat_id, message_id) the calling identity can read, with no binding to the message being answered or the chat the reply goes to -- so a prompt-injected agent can cite an older message from a profiled, wider person and serve an unprofiled colleague under that person's grant.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/app/tools.py (cc22fdfb9d): `def opal_asker_query(chat_id: str, message_id: str, key: str, params: Optional[dict] = None)` -- chat_id and message_id are agent-supplied arguments.",
        "app/asker_scope.py:91-106 resolve_asker(): GET /chats/{chat_id}/messages/{message_id} with $select=from, principal = from.user.tenantId/id -- no check of the message's age, of its being the message under reply, or of the reply's destination chat.",
        "app/asker_scope.py:149-163: the profile/grant/'query' checks run against THAT resolved principal, so the unprofiled-asker refusal (C10 bullet 4) is bypassed by citing a profiled person's message.",
        "PRD v0.5 C10 bullet 2: 'The agent never asserts whose behalf it acts on, and an identity the agent supplies in a call is ignored. A prompt-injected agent therefore cannot borrow a wider person's reach.' -- choosing the message IS asserting the asker."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C10: the asker is established server-side from the message the gateway read itself, and a prompt-injected agent cannot borrow a wider person's reach.",
    "world_is": "The gateway reads a sender server-side, but the AGENT picks which message. Nothing binds that message to the conversation being answered (no recency window, no match to the chat the reply is sent to, no account of the other members of a group chat), so the asker-scoping holds only for an honest agent. Bounded today by W2-S1 (data reach is the calling identity's catalog reach either way); what the hole defeats is the NO-PROFILE refusal and the 'query'-operation gate.",
    "notes": "Disarm options for the issuer, cheapest first: (1) OA-t-6 deploys with opal_asker_query NOT in the concierge identity's allowlist until fixed (INERT while undeployed for that identity); (2) bind the cited message: reject one older than a short window, and require the reply tool to send only into the SAME chat_id the query cited; (3) for group chats, scope to the intersection over every human member, not the sender alone. (2) is the minimum that restores C10 for 1:1 chats. Filed by the PRD owner; the contract is unchanged, and this is the round-1 analysis's input either way."
  },
  {
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-24T23:30Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "NFRA_OPALAI-Z-S6",
    "one_line": "DISARMS NFRA_OPALAI-Z-S5 (owner this seat): opal_asker_query deploys DARK for the concierge identity -- app/identity_scope.py's concierge allowlist does not name it (Z-S3), so no call from the Teams agent reaches the cited-message resolution; G-SCOPE (Andrew's widening) is not asked until the recency + reply-to-same-chat binding lands as round 2's repair cell.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "NFRA_OPALAI-Z-S3 (merged @7b37d9bd8d): the concierge allowlist omits opal_asker_query; its docstring requires Andrew's ruling to widen, and no cell of round 1 widens it.",
        "1.0.0_SA_CTO~O msg 25807: 'Your cut stands, per your msg 25803: the tool deploys dark, and the recency plus same-chat binding is the round-2 repair cell.'",
        "EC2_MANIFEST.json at this row: opal-gateway deployed_commit 1764e54a16 carries no asker_scope.py; OA-t-6 has not deployed."
      ]
    },
    "spec_asserts": "NFRA_OPALAI-Z-S5 is ARMED with this seat as disarm_owner.",
    "world_is": "The bypass needs an identity that can dispatch the tool; the only runtime identity cannot, by the allowlist, until a ruling this seat will not request before the binding exists. Disarmed, not remediated.",
    "notes": "The close run's G-SCOPE ask is conditioned on the repair cell landing first. No gate is built here."
  },
  {
    "id": "NFRA_OPALAI-Z-W2-S3",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~2",
    "surfaced_at": "2026-09-24T23:48Z",
    "one_line": "OA-t-6's own census (its cell step 1) finds 6 unreleased, non-OA-t-5 commits touching infra/aws/ec2/opal-gateway between the manifest's deployed_commit and this worktree's HEAD; deploying HEAD ships them alongside asker_scope.py. STOPPED per the cell's own instruction; no deploy act taken.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "`git log --oneline 1764e54a16b7bb12d34b36eec7866589b6ea785e..HEAD -- infra/aws/ec2/opal-gateway` at wk-NFRA_OPALAI-2 HEAD 050035f941 lists 7 commits touching the tree: cc22fdfb9d (OA-t-5, this project) and 050035f941 (this order's own audit.py hookup, admitted by the cell face) are the only two this order names; the other 5 are NOT this order's: 650c9a99cb (NFRA_MCPINDEX.TO-MX-c-2, app/refs/DATA_CATALOG.yaml), e8f800e6a9 (MDPF_TAXSMA.TO-TX-g-1 drain merge, app/config.py + app/server.py + new app/taxsma_workbook.py), 9e4074c33a and 6c37cc6b00 (NFRA_OPLGTW OG-r-2 / amend OG-r-1, tests/acceptance/onhost_bench.py + og_r2.py + runbooks/SCHWAB_PILOT_RUNBOOK.md), 8dce9aeb0b and 6abf60e5d5 (MDPF_TAXSMA.TO-TX-g-1, app/taxsma_workbook.py feat+fix) -- `git show --stat <hash> -- infra/aws/ec2/opal-gateway` confirms a real file touch under the tree for each of the 5.",
        "EC2_MANIFEST.json services.opal-gateway.deployed_commit=1764e54a16b7bb12d34b36eec7866589b6ea785e, deployed_at=2026-09-18T05:58:16Z, deployed_by=0.9.0_WK_NFRA_OPLGTW~2 -- unchanged since; none of the 5 non-OA-t-5 commits is an ancestor of it (that is what the `A..B` range printed them means).",
        "`ls org/critical_paths/change_management/ | grep -i gateway` -- the last opal-gateway deploy-completion record is `20260918T1624Z_nfra-oplgtw-gw-runtime-deleteitem_deploy_completion.md`; no later record exists for opal-gateway, so none of the 5 commits has been released through any other order's deploy leg either.",
        "Task order NFRA_OPALAI.TO-OA-t-6.gateway-deploy.md s.1.1: 'If anything in that list is not OA-t-5's and is not already released, STOP: file a BLOCKING row naming each commit. Shipping another project's unreleased gateway change under this order is not yours to decide.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OA-t-6 s.1: census every commit between the manifest's deployed_commit and HEAD touching infra/aws/ec2/opal-gateway; ship only OA-t-5's changes plus this order's own audit.py hookup.",
    "world_is": "Five commits from NFRA_MCPINDEX and MDPF_TAXSMA and NFRA_OPLGTW's OG-r-2/OG-r-1-amend sit unreleased in the same source tree safe-ec2-deploy.sh tarballs whole; no NEVER-2 ledger was opened and no artifact was built, uploaded or SSM-pulled by this worker -- the host still serves 1764e54a16 and EC2_MANIFEST.json is unedited by this order.",
    "notes": "Owner of the decision named by the cell text itself: whoever can rule that the 5 commits are cleared to ship alongside OA-t-5 (or that this deploy must exclude them, e.g. by cherry-picking OA-t-5 + the audit hookup onto a clean branch off 1764e54a16 rather than deploying this worktree's HEAD). AC1-AC3 are not run: no ledger entry exists to read, no deploy commit exists to read, no host was pulled. Reported as BLOCKING, not FAIL -- the criteria are un-met-as-written, not failed."
  },
  {
    "id": "NFRA_OPALAI-Z-S9",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T00:35Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_OPALAI-Z-W2-S3 for THIS order (owner this seat): OA-t-6 took no deploy act -- no ledger entry, no artifact, no SSM pull, no manifest edit -- so nothing shipped; the standing hazard (the next gateway deploy by ANY seat ships 5 unreleased commits of three other projects) is carried to 1.0.0_SA_CTO~O as a release decision.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EC2_MANIFEST.json opal-gateway.deployed_commit still 1764e54a16 at the drain; git log 1764e54a16..HEAD -- infra/aws/ec2/opal-gateway, read by this seat: cc22fdfb9d (OA-t-5) plus 650c9a99cb (NFRA_MCPINDEX MX-c-2), 6abf60e5d5 + 8dce9aeb0b + e8f800e6a9 (MDPF_TAXSMA TX-g-1), 9e4074c33a + 6c37cc6b00 (NFRA_OPLGTW OG-r-2).",
        "2.0.0_SA_COO~O to 1.0.0_SA_CTO~O, 2026-09-25T00:22Z, DECISION message naming the five commits, the recommendation (one coordinated release the CTO rules, each owner's gates cited) and the alternative (OA-t-5 cherry-picked off 1764e54a16)."
      ]
    },
    "spec_asserts": "NFRA_OPALAI-Z-W2-S3 is ARMED with this seat as disarm_owner.",
    "world_is": "OA-t-6 stays open (pending) until the CTO rules the release scope; the worker's refusal was the order's own census clause working as written.",
    "notes": "NFRA_MCPORTAL's gateway merges and NFRA_MCPINDEX's MX-c-4 drain wait on the same ruling. No gate is built here."
  }
]
```
