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
  },
  {
    "id": "NFRA_OPALAI-Z-W3-S1",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~3",
    "surfaced_at": "2026-09-24T23:40Z",
    "one_line": "t2.AC2.sh and t2.AC3.sh capture rc from a `cmd | tr -d '\\r'` pipeline with pipefail OFF, so `$?` is always tr's exit (0), never the underlying provision-account.ps1/verify-boundary.ps1 exit code -- their PASS conditions (`rc=3`, `rc=4`) can never be satisfied by any script, correct or not.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "`set -o | grep pipefail` in this worktree's bash: `pipefail off`; t2.AC2.sh/t2.AC3.sh (and _root.sh) never set it.",
        "Direct invocation (no pipe) of `opal_ai/opal/runtime/provision/provision-account.ps1 -Config <cfg>` in this non-elevated session: prints 'ELEVATION REQUIRED ...', `direct_rc=3` -- exactly the AC2 spec.",
        "Direct invocation of `verify-boundary.ps1 -Config <cfg>` (no Opal_Agent account on this box): prints 'BOUNDARY: NOT-PROVISIONED', `direct_rc=4` -- exactly the AC3 spec.",
        "Running the check scripts as issued, post-commit 2d83bdb8: t2.AC1.sh -> rc=0, PLAN acts matched 8 of 8, RESULT PASS, exit=0 (its expected rc=0 happens to equal tr's own exit, masking the bug). t2.AC2.sh -> 'session elevated=False; rc=0; ELEVATION REQUIRED lines=1; ...', RESULT FAIL, exit=1 (rc=0 fails the script's own `[ \"$rc\" = 3 ]` test). t2.AC3.sh -> 'rc=0; BOUNDARY: NOT-PROVISIONED', RESULT FAIL, exit=1 (rc=0 fails `[ \"$rc\" = 4 ]`)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "AC2 expects `rc=3; ELEVATION REQUIRED lines>=1; ... -- RESULT: PASS -- exit=0`; AC3 expects `rc=4; BOUNDARY: NOT-PROVISIONED -- RESULT: PASS -- exit=0`.",
    "world_is": "provision-account.ps1 and verify-boundary.ps1 both produce the exact specified refusal text and exit code when run directly; the check scripts that grade them lose that exit code to an un-guarded pipe before ever comparing it, so AC2 and AC3 read FAIL for any conforming implementation. Left alone, no worker on this cell can ever produce a PASS-by-output on AC2/AC3 as literally invoked.",
    "notes": "t2.AC2.sh and t2.AC3.sh are 2.0.0_SA_COO~O's own artifacts, outside this order's <paths> (Read-only, not granted to write); not repaired here per bound 2.3 (never repair a criterion). A one-line fix (`set -o pipefail` before the pipe, or `${PIPESTATUS[0]}`) would let both scripts grade correctly."
  },
  {
    "id": "NFRA_OPALAI-Z-S7",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T00:30Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_OPALAI-Z-W3-S1 (owner this seat): the checks' rc capture read tr's exit status, not the command's; fixed at CLOUD @0ad710832f with set -o pipefail in the shared _root.sh and carried onto wk-NFRA_OPALAI-3, where t2.AC2(rc=3)+t2.AC3(rc=4) now PASS.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Issuer re-dry-run under pipefail @0ad710832f: base builds FAIL with their expected sign; the same checks on wk-NFRA_OPALAI-3 PASS (recorded in the fix commit's message).",
        "The defect was the issuer's: `out=$(cmd | tr -d CR); rc=$?` without pipefail yields tr's exit (0); the assignee refused rather than repaired and proved the direct exit codes."
      ]
    },
    "spec_asserts": "NFRA_OPALAI-Z-W3-S1 is ARMED with this seat as disarm_owner.",
    "world_is": "The criteria now read the command's own exit; the order's instance is rewritten by a fresh worker on this slot against the fixed checker.",
    "notes": "Swept on the trigger: 19 check files read rc=$?, all through the one sourced root. No gate is built here."
  },
  {
    "id": "NFRA_OPALAI-Z-W6-S1",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~6",
    "surfaced_at": "2026-09-24T23:55Z",
    "one_line": "w3.AC2.sh's rc=$? reads the exit status of the trailing `tr -d '\\r'` in its capture pipe, never run_checks.sh's own exit code, so the criterion's `[ \"$rc\" != 0 ]` limb can never be true regardless of what run_checks.sh does -- AC2 is structurally unable to PASS as written.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/w3.AC2.sh: `out=$(cd \"$T/c\" && timeout 100 env -u PYTHONPATH bash opal/checks/run_checks.sh 2>&1 | tr -d '\\r'); rc=$?` -- no `set -o pipefail` in this file or in the sourced `_root.sh`.",
        "Positive control run in this worktree: `out=$(false | tr -d '\\r'); echo $?` prints 0 -- the pipe's reported status is always the last stage's (tr), never the first stage's (the command whose failure the criterion needs).",
        "Running w3.AC2.sh against my built opal_ai/opal/checks/run_checks.sh (planted broken+non-ASCII file) printed `rc=0; CHECKS: FAIL; py_compile named=2; ascii named=2` -- every other limb of the criterion is satisfied (CHECKS: FAIL, both checks named) but `rc=0` fails the `[ \"$rc\" != 0 ]` test, so the script prints RESULT: FAIL, exit=1."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OA-w-3 AC2 expects: rc!=0; CHECKS: FAIL; py_compile named>=1; ascii named>=1 -- RESULT: PASS.",
    "world_is": "The check's own pipe construction discards run_checks.sh's exit status before `rc=$?` reads it, so `rc` is always 0 (tr's own exit) no matter whether run_checks.sh exits 0 or 1 on a planted defect. A correct run_checks.sh that exits 1 on failure (as mine does, verified directly and via AC1's own `env -u PYTHONPATH bash opal/checks/run_checks.sh` PASS at exit=0) cannot make this criterion PASS; only editing the check's own pipeline (e.g. `set -o pipefail`, or reading `${PIPESTATUS[0]}`) would let it observe rc.",
    "notes": "w3.AC2.sh is a COO deliverable outside this order's <paths> (org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/**); this worker did not edit it. AC2 is reported FAIL-by-output per the recorded invocation, with this row citing the cause."
  },
  {
    "id": "NFRA_OPALAI-Z-S8",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T00:30Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_OPALAI-Z-W6-S1 (owner this seat): the checks' rc capture read tr's exit status, not the command's; fixed at CLOUD @0ad710832f with set -o pipefail in the shared _root.sh and carried onto wk-NFRA_OPALAI-6, where w3.AC2(rc!=0) now PASS.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Issuer re-dry-run under pipefail @0ad710832f: base builds FAIL with their expected sign; the same checks on wk-NFRA_OPALAI-6 PASS (recorded in the fix commit's message).",
        "The defect was the issuer's: `out=$(cmd | tr -d CR); rc=$?` without pipefail yields tr's exit (0); the assignee refused rather than repaired and proved the direct exit codes."
      ]
    },
    "spec_asserts": "NFRA_OPALAI-Z-W6-S1 is ARMED with this seat as disarm_owner.",
    "world_is": "The criteria now read the command's own exit; the order's instance is rewritten by a fresh worker on this slot against the fixed checker.",
    "notes": "Swept on the trigger: 19 check files read rc=$?, all through the one sourced root. No gate is built here."
  },
  {
    "id": "NFRA_OPALAI-Z-S10",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T01:20Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "OA-t-4's parent side is HELD unmerged, and its row NFRA_OPALAI-Z-W4-S1 (ARMED, owner this seat, on branch wk-NFRA_OPALAI-4 only) is carried here: the live D7 ticket-intake runner imports .claude/skills/teams-assist/teams-watch.py by path and calls its Claude-credential token selection, so moving the watch as the order says would break a production pipeline. Disarmed by the hold; the fix is a cross-directive decision routed to 1.0.0_SA_CTO~O.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "integrations/ticketing/intake/runner.py at CLOUD HEAD, read by this seat: :69 TEAMS_WATCH = REPO_ROOT / '.claude' / 'skills' / 'teams-assist' / 'teams-watch.py'; :107 'Import the estate's ONE pinned-token selection (teams-watch.py) -- never re-implement it'; :121-123 sets tw.PIN_SERVER and calls tw.read_token(). Scheduled every 5 min as OPAL_D7_ticket_intake (worker report).",
        "Worker 0.9.0_WK_NFRA_OPALAI~4 on TO-OA-t-4, branch wk-NFRA_OPALAI-4 @182c475633: AC1 3 of 3, AC2 live metadata PASS, AC3 FAIL (the old path still named by runner.py and by OA-t-1's own SKILL.md); instance VALID (rc=0, issuer re-run). Its nested watch (own OAuth refresh family, never reads ~/.claude/.credentials.json) is merged into opal_ai branch r1-drain @79f7ad3; the opal_ai checks pass there.",
        "Not merged: wk-NFRA_OPALAI-4's parent commit e459c5d6df removes .claude/skills/teams-assist/teams-watch.py; CLOUD keeps it."
      ]
    },
    "spec_asserts": "TO-OA-t-4: the watch moves into opal_ai and its parent copy is removed on the branch (C1, move never copy).",
    "world_is": "The workspace copy has a second consumer outside NFRA_OPALAI -- a D7 production runner -- that depends on exactly the behaviour the Analyst's watch is moving away from (reading Claude Code's own token). C1's 'move, never copy' cannot hold for this file without the D7 runner's own change.",
    "notes": "Decision asked of 1.0.0_SA_CTO~O: (a) the D7 runner owns its own token selection (its owner writes it; the Analyst's watch moves), or (b) the runner re-points to the moved watch and adopts its refresh family. OA-t-4 stays open until then. No gate is built here."
  },
  {
    "id": "NFRA_OPALAI-Z-W5-S1",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~5",
    "surfaced_at": "2026-09-25T01:13Z",
    "one_line": "install-owned-paths.sh --submodule <path> resolves REPO_ROOT from the invoking shell's AMBIENT cwd, not from anything tied to the intended repo -- a caller that invokes it by absolute path without first cd-ing into that repo silently targets whichever repo the ambient cwd sits in instead.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "This cell's own bound #1 (\"never install a hook into the real opal_ai... the real install is the issuer's act at the round's last merge\") already anticipates the risk that a --submodule invocation could reach the real tree; it names WHO may do it, not a mechanism that refuses when they do not mean to.",
        "REPRODUCED THIS SESSION: an exercise call of `bash \"$P/.tools/git-hooks/install-owned-paths.sh\" --submodule opal_ai` (absolute script path, no prior `cd \"$P\"`) was issued while this worker's own harness had reset its Bash-call cwd to the PRIMARY workspace root between calls (per this harness's own documented behavior) -- `git rev-parse --show-toplevel` from that cwd resolved to the REAL main tree, and `SUB_ABS=\"$REPO_ROOT/opal_ai\"` resolved to the REAL opal_ai submodule checkout, which exists there (unlike in this worker's own worktree, where opal_ai is uninitialised).",
        "Effect measured: `/c/Users/Opal Bloomberg/Desktop/ajb_workspace/.git/modules/opal_ai/hooks/pre-commit` was created (905 bytes, this cell's own wrapper text verbatim, including its 'OA-w-2 (2026-09-24)' comment) at 20:49 local -- confirmed by `cat`, byte-identical to install-owned-paths.sh's generated WRAPPER.",
        "Found and removed same-turn by this worker: `rm -f` on that path at 2026-09-25T01:08Z; `ls` immediately after shows only git's stock `*.sample` files in that hooks dir (applypatch-msg.sample .. update.sample, all timestamped 19:10, the submodule's own init), i.e. the real opal_ai's hooks dir is back to its pre-incident state. `git status`/`git -C opal_ai status` at the main tree show no other unexpected change from this; the one unrelated staged change there (`.gitmodules` +mcportal submodule) predates this session and is another live seat's work."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The build spec's bound (\"never install a hook into the real opal_ai... the round's issuer is the only caller with standing to name the real one\") is enforced by WHO is allowed to pass the real path, and that is sufficient.",
    "world_is": "Nothing in install-owned-paths.sh itself distinguishes a scratch fixture from the real tree, and its only signal is a resolved-path string in its own stdout (\"OK: ... installed at <path>\") that a caller must read to notice a wrong target -- a silent cwd mismatch (this harness's own reset-between-calls behavior is one concrete source) reaches the real opal_ai with no refusal. Left alone, the round's own last-merge install call carries the identical exposure this row measured on itself.",
    "notes": "Not fixed here (out of this cell's stated build): a hardening would have the script print (or the caller verify) the RESOLVED repo identity before writing, or accept an explicit --root override instead of trusting ambient cwd. Left for the disarm_owner's real install to read this row first."
  },
  {
    "id": "NFRA_OPALAI-Z-S11",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T01:45Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_OPALAI-Z-W5-S1 (owner this seat): the hook the worker briefly installed into the real opal_ai is gone -- the main tree's .git/modules/opal_ai/hooks holds 14 files, all stock .sample, and no pre-commit -- so no nested commit is being graded mid-round; install-owned-paths.sh --submodule's reliance on ambient cwd is recorded for the round-1 read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Issuer read 2026-09-25 ~01:4xZ: `ls --indicator-style=none <main>/.git/modules/opal_ai/hooks` = 14 entries, non-.sample 0, pre-commit absent. (A first count read 14 non-sample because ls here appends '*' to executables and defeats a $-anchored pattern; recounted without indicators.)",
        "Worker report 0.9.0_WK_NFRA_OPALAI~5 on TO-OA-w-2 @77043416d3: the install happened from a call without an explicit cd (the harness resets cwd per call to the workspace root), and was removed the same turn."
      ]
    },
    "spec_asserts": "NFRA_OPALAI-Z-W5-S1 is ARMED with this seat as disarm_owner; TO-OA-w-2 bound 1 forbids a hook in the real opal_ai mid-round.",
    "world_is": "The bound was crossed briefly and restored; the real install stays the issuer's act at the round's last merge. Defect for the L10 read: the installer should resolve REPO_ROOT from its own location, not from cwd.",
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
  },
  {
    "id": "NFRA_OPALAI-Z-S12",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T02:10Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_OPALAI-Z-W4-S1 (owner this seat): per the CTO's ruling I-3 (@c1717499bf) the workspace teams-watch.py STAYS as the operator plane's tool, so the D7 intake runner keeps its import; the order was amended (@7095d441ee), the operator files restored byte-for-byte on this branch (4891cbb72a), and the re-run passes 3 of 3.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Ruling I-3, org/missions/D6/NFRA/NFRA_OPALAI/deliverables/1.0.0_SA_CTO~O/ROUND1_ANALYSIS_INPUTS.md @c1717499bf: option (c), the parent watch stays; only the Analyst's use ends at cutover.",
        "Worker 0.9.0_WK_NFRA_OPALAI~4 re-run @d0482ca3f7: AC3 'moved watch committed in opal_ai=yes; operator teams-watch.py byte-equal to the cut=yes; operator /teams-assist SKILL.md byte-equal to the cut=yes'; instance VALID (issuer re-run rc=0)."
      ]
    },
    "spec_asserts": "NFRA_OPALAI-Z-W4-S1 is ARMED with this seat as disarm_owner.",
    "world_is": "No production consumer loses its file: the branch's net change to .claude/ against CLOUD is zero.",
    "notes": "Enrichment (ruling I-3): the operator watch's header should name its real consumers. No gate is built here."
  },
  {
    "id": "NFRA_OPALAI-Z-S13",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T02:46Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_OPALAI-Z-W1-S4 and NFRA_OPALAI-Z-W1-S5 (owner this seat; both on wk-NFRA_OPALAI-1): OA-t-1 stays OPEN and its parent side does not merge before the cutover window, so the 6 DATA_CATALOG.yaml census_ref lines still naming the old refs/ path reach no served reader; the 6 are a gate-scope question routed to the CTO as a decision.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Reproduced by this seat at 02:45Z: the full 31-line re-point of infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml (CR bytes preserved, 1338 of 1338 lines CRLF) run through python .tools/naming-gate.py --diff --enforce prints 'NAMING-GATE: REFUSE 6 graded' at :648 :672 :695 :718 :740 :763, each 'EXISTING and OUT-OF-PATTERN as S3Key in a surface remediations.json assigns to the live remediation MDPF_CANON: REFUSE unless the diff removes it'. The changed field on each line is file:, not key:.",
        "infra/logic/registry/remediations.json: MDPF_CANON (owner_directive D8, status active, L5 not started) owns s3-prefix opal-data-portal-v2 platinum/mdpf/. The gate's only waiver carrier, org/standards/NAMING_LEGACY_READS.json, is a Python-AST call-site allowlist (naming-gate.py legacy_read_ok) and cannot reach a YAML line.",
        "Grep of census_ref over infra/aws/ec2/opal-gateway/**/*.py: 0 hits, so the gateway has no runtime reader of the field; the parent tree is unchanged on CLOUD (OA-t-1 is unmerged, status pending).",
        "W1-S4 (CRLF smudge): the branch head carries the CRLF-preserving edit; no other open order of this round writes DATA_CATALOG.yaml."
      ]
    },
    "spec_asserts": "NFRA_OPALAI-Z-W1-S4 and -Z-W1-S5 are ARMED with this seat as disarm_owner.",
    "world_is": "Nothing has landed: CLOUD still carries the refs/ tree at its old path and all 31 catalog references resolve there. AC2 stays FAIL (25 of 31) and OA-t-1 stays open; the issuer does not amend AC2, because 25 of 31 would lower the bar.",
    "notes": "The decision asked of 1.0.0_SA_CTO~O is whether rule 30's non-application (an existing pipeline reaches conformance through its own migration, never as a rider) admits a line whose key is byte-unchanged, or whether OA-t-1 waits for MDPF_CANON. Any fix to the gate belongs to that gate's lane, not to this project. Any face that edits a CRLF-committed file must name 'preserve CR bytes'."
  },
  {
    "id": "NFRA_OPALAI-Z-S14",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T02:55Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_OPALAI-Z-W2-S4 (owner this seat): the OA-t-6 manifest record did land (9f323c7452, 0 graded lines), and the one further gateway deploy this seat will issue this round (NFRA_MCPORTAL MP-t-6) will name the Step-3 ERROR line and the LF hand-record as its read. The fix, stripping CR from jq's temp output, is owned by safe-ec2-deploy.sh's lane, not this project.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "wk-NFRA_OPALAI-2 commit 9f323c7452 records deployed_commit f1f0fc6780 on EC2_MANIFEST.json in an LF copy; the OA-t-6 instance (57cbdd7921) AC2 reads it back PASS.",
        "The worker's row W2-S4 grounds the cause: 658 of 658 CRLF in the release worktree's jq-rewritten copy, and 'NAMING-GATE: REFUSE 89 graded' at the script's Step 3. The script prints ERROR and continues, by its own design."
      ]
    },
    "spec_asserts": "NFRA_OPALAI-Z-W2-S4 is ARMED with this seat as disarm_owner.",
    "world_is": "The OA-t-6 record is complete. The hazard stands for any other seat that deploys an EC2 service through safe-ec2-deploy.sh on this device and misses the Step-3 ERROR line.",
    "notes": "The fix and its owner are named in W2-S4's notes: add tr -d CR on the jq temp output before the mv, the pattern the script already applies at its SOURCE_PATH read. No gate is built here."
  },
  {
    "id": "NFRA_OPALAI-Z-W2-S4",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~2",
    "surfaced_at": "2026-09-25T02:20Z",
    "one_line": "safe-ec2-deploy.sh's own Step 3 manifest auto-commit refuses on this host because jq.exe rewrites EC2_MANIFEST.json with CRLF line endings, turning every one of the file's 658 lines into a diff hunk and pulling ~89 pre-existing unrelated naming-gate rows into the graded set -- REFUSE, non-fatal by the script's own design, but the manifest record is then left uncommitted on whichever branch the deploy ran from.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-ec2-deploy.sh opal-gateway run from /c/tmp/oa-2-rel (release worktree rel-nfra-opalai-r1-gateway): Step 3 printed '[naming-gate] NAMING-GATE: REFUSE 89 graded' then 'ERROR: Manifest safe-commit failed (contamination guard / owned-paths). The deploy LANDED --'.",
        "git -C /c/tmp/oa-2-rel diff -- infra/aws/ec2/EC2_MANIFEST.json after that run showed every one of the file's lines as changed ('-{' / '+{' from line 1); python byte count on that worktree's copy: 658 of 658 newlines were CRLF (\\r\\n). This worktree's (oa-2) untouched copy of the same file: 0 of 658 CRLF.",
        "The deploy itself (S3 upload, SSM pull+restart, on-box md5) succeeded and is unaffected; only the script's own bookkeeping commit is broken by this. Worked around by hand-editing only the two changed fields plus one added field on oa-2's own LF copy and committing there (9f323c7452), which the naming-gate then correctly scoped to 0 graded lines."
      ]
    },
    "spec_asserts": "The task order's step 3 (\"record the release on THIS branch\") reads as: run the deploy, and its EC2_MANIFEST.json record lands through the script's own Step 3 commit.",
    "world_is": "The script's own commit step cannot land the manifest record on this device class (jq.exe CRLF output at that write site, undocumented elsewhere), so every future opal-gateway (and likely every other jq-rewritten EC2_MANIFEST.json) deploy through safe-ec2-deploy.sh on this device silently degrades to the 'record manually' fallback the script prints -- a standing hazard for any worker who does not notice the ERROR line among the deploy's otherwise-successful output.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not fixed here: infra/aws/ec2/safe-ec2-deploy.sh is READ-ONLY under this task order's bounds (section 2.1: 'the deploy script and safe-ec2-deploy.sh are READ, never edited'). The fix is a tr -d '\\r' on the jq TEMP output before mv, the same pattern already applied at this script's SOURCE_PATH read (comment at safe-ec2-deploy.sh's SOURCE_PATH lookup)."
  },
  {
    "id": "NFRA_OPALAI-Z-W7-S1",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~7",
    "surfaced_at": "2026-09-25T03:40Z",
    "one_line": "OA-w-4 bound 2 asserts portal is NOT provisioned in this worktree and must read UNINITIALISED, but at build time portal IS a real initialised checkout here (its own .git file, HEAD fe618e50, git log works) and counts 589 commits/30d -- the bound's premise does not hold; the build followed the general spec (an integer when initialised) instead.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-OA-w-4 section 2 bound 2: \"'portal' is NOT provisioned in your worktree, so it must read UNINITIALISED.\"",
        "`cat portal/.git` in this worktree: 'gitdir: C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal/.git/worktrees/portal3'; `cd portal && git log -1 --oneline` prints fe618e50 (a real commit), `git rev-parse --show-toplevel` = C:/tmp/oa-7/portal.",
        "`git submodule status opal_ai portal mcportal`: opal_ai and portal both show a '+' (checked out, differs from index), mcportal shows '-' (not initialised, no .git entry present in mcportal/); mcportal is the one genuinely UNINITIALISED mapped path here.",
        "fabric-commits.py --json --days 30 by_repo: {'parent': 15972, 'opal_ai': 4, 'portal': 412, 'mcportal': 'UNINITIALISED'}; activity-check.py --days 30 repos: parent=17219 opal_ai=7 portal=589 mcportal=UNINITIALISED."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "portal is NOT provisioned in this worktree and must read UNINITIALISED.",
    "world_is": "portal is initialised in this worktree (a linked worktree of the shared portal repo, sharing its .git/worktrees admin dir with the main tree's own portal checkout) and reads as an integer, same as opal_ai; only mcportal reads UNINITIALISED here. Both proof scripts (w4.AC1.sh, w4.AC2.sh) accept 'UNINITIALISED or an integer' for portal, so grading is unaffected either way.",
    "notes": "Not repaired: the build follows section 1's general rule (an integer count when a mapped path's .git entry is present, else UNINITIALISED), which is the spec's own instruction and does not depend on the bound's stale prediction. No gate is built here."
  },
  {
    "id": "NFRA_OPALAI-Z-W7-S2",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~7",
    "surfaced_at": "2026-09-25T03:55Z",
    "one_line": "w4.AC2.sh's `... | grep -m1 -oE ... || echo \"(no repos: field)\"` runs BOTH branches under `set -o pipefail`: grep -m1 quits after its first match and SIGPIPEs the upstream `tr`, so `tr` exits 141, the pipeline as a whole is non-zero despite grep having matched, and the `||` fallback text is appended after the real match -- harmless here (the real line is still first in $h and the regex extraction still finds it), but the printed 'RESULT' output is not what the script's author intended.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Reproduced this session: `bash -c 'set -o pipefail; h=$(timeout 100 python .tools/activity-check.py --days 30 2>&1 | tr -d \"\\r\" | grep -m1 -oE \"repos: .*\" || echo FALLBACK); echo \"H=[$h]\"'` prints both the real match and FALLBACK, 2 lines.",
        "Running w4.AC2.sh as issued: stdout carried 'repos: parent=... opal_ai=... portal=...' followed immediately by '(no repos: field)', then 'RESULT: PASS -- exit=0' (the sed extraction on $h's first line still succeeds, so grading is unaffected)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "w4.AC2.sh's fallback branch `(no repos: field)` fires only when no 'repos:' line is found in activity-check.py's output.",
    "world_is": "Under `set -o pipefail` (sourced from _root.sh), a `-m1` grep that matches early SIGPIPEs an upstream `tr`, making the pipeline's own exit non-zero even though the intended match succeeded -- so the `||` fallback always co-prints alongside a real match on this construction. AC1-AC2 both PASS by output regardless (the real line sorts first and the numeric extraction still lands), so this is cosmetic to this order's grading, not a criterion defect.",
    "notes": "Not fixed here: w4.AC2.sh is a COO deliverable outside this order's <paths> (Read-only). A fix would use `${PIPESTATUS[1]}` (tr's own exit) or drop `-m1` in favour of `grep -oE ... | head -1` outside the pipefail'd stage."
  },
  {
    "id": "NFRA_OPALAI-Z-S15",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T04:25Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "OA-t-1's worker bumped the parent's opal_ai gitlink on its branch (56b3208888) under GIT_COMMIT_AUTHOR_OVERRIDE; the bare gitlink path is outside the order's <paths>, and the face names no gitlink move. The branch is held for the cutover window, so nothing has landed, and the issuer sets the gitlink to r1-drain's final commit at cutover.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Worker report 0.9.0_WK_NFRA_OPALAI~1 (amendment pass): 'Advanced the opal_ai gitlink to 2e48f7b in a separately-scoped commit 56b3208888 (GIT_COMMIT_AUTHOR_OVERRIDE applied and audited, since the bare gitlink path has no matching <paths> entry)'.",
        "Face NFRA_OPALAI.TO-OA-t-1 section 2.3: 'Never repair a criterion, widen it, or meet it by a route this face does not name'; its <paths> list no bare opal_ai entry.",
        "Decomposition: the parent gitlink moves only in the cutover window (C1). OA-t-1 stays unmerged until then; its nested commits are in opal_ai r1-drain at 99190d1."
      ]
    },
    "spec_asserts": "A worker writes exactly the <paths> its order names; an escape through the author override is the lane's audited instrument, not a worker's route.",
    "world_is": "One worker commit sits outside the grant, taken through the audited override. Its effect is inert until the cutover merge, which re-sets the gitlink anyway.",
    "notes": "For the CVO's read. A face that moves files into a submodule should say whether the worker bumps the gitlink; this one said nothing, and the worker filled the gap."
  },
  {
    "id": "NFRA_OPALAI-Z-S16",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T04:45Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_OPALAI-Z-W3-S2 (owner this seat; on wk-NFRA_OPALAI-3): the AC2 hit was the issuer's checker over-reaching. The face REQUIRES workspace_probe_file to name a workspace file, so the scan now exempts that one key. Fixed at 4c183eef3c on CLOUD and df6be72199 on the branch; the worker re-runs.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Face NFRA_OPALAI.TO-OA-t-3 item 5(a): the gate's read of workspace_probe_file must be DENIED, so the key names a workspace path by design. opal_ai r1-drain opal/runtime/provision/runtime.config.example.json:4 names ajb_workspace/CLAUDE.md, as OA-t-2 wrote it.",
        "Dry-run of the fixed check by this seat: base FAIL; wk-NFRA_OPALAI-3 @faae15254b PASS (runtime files naming workspace/AWS/serial=0); mutant with a workspace path appended to opal/runtime/CLAUDE.md FAIL, reverted."
      ]
    },
    "spec_asserts": "NFRA_OPALAI-Z-W3-S2 is ARMED with this seat as disarm_owner.",
    "world_is": "No runtime file the agent loads names the workspace. The only hit was the probe key the spec mandates. OA-t-3's built files are unchanged.",
    "notes": "A checker defect: a scan scoped by directory counted a value the same spec mandates. It is filed for the round-1 checker lessons."
  },
  {
    "id": "NFRA_OPALAI-Z-S17",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T05:10Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "The issuer installed the owned-paths hook into the real opal_ai and exercised it. In the main nested checkout it BLOCKS an unordered worker serial and passes this seat. In an opal_ai linked worktree OUTSIDE any parent worktree it fails OPEN: a WARN, the lane check skipped, and the violation commit landed. The wrapper's fallback reads the first 'git worktree list' entry, which for a submodule is the gitdir .git/modules/opal_ai, and that has no superproject.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bash .tools/git-hooks/install-owned-paths.sh --submodule opal_ai: 'OK: owned-paths hook installed at .git/modules/opal_ai/hooks/pre-commit', rc=0.",
        "Main checkout, scratch branch: the violation arm (author 0.9.0_WK_NFRA_OPALAI~9) exits rc=1 with 'VIOLATION: opal_ai/HOOK_PROBE.md -- lane=ANY_EXEC_OR_AE'; the granted arm (author 2.0.0_SA_COO~O) exits rc=0. The scratch branch was deleted and the checkout restored to 90ca424.",
        "Linked worktree /c/tmp/oa-hookprobe: 'WARN: owned-paths-check.sh not found at C:/tmp/oa-hookprobe/.tools/git-hooks/owned-paths-check.sh -- skipping lane check', rc=0, and the violation commit landed on a scratch branch that was then deleted.",
        "rev-parse --show-superproject-working-tree: worker-shaped nested checkouts /c/tmp/oa-1/opal_ai and /c/tmp/oa-3/opal_ai resolve to their parent worktree; /c/tmp/oa-r1-drain and /c/tmp/oa-hookprobe resolve to empty."
      ]
    },
    "spec_asserts": "OA-w-2: a commit inside a nested repo is graded by the parent's gates.",
    "world_is": "True wherever the nested checkout sits inside a parent worktree, which covers every worker face this round. False for a nested linked worktree outside any parent (issuer drain worktrees), where the wrapper fails open.",
    "notes": "Enrichment for round 2: the fallback should resolve the parent through 'git rev-parse --git-common-dir' (.git/modules/<name> -> the parent's .git) and fail CLOSED when it cannot. The fail-open WARN predates OA-w-2 (ADHC_OWNPTH.003's portability posture)."
  },
  {
    "id": "NFRA_OPALAI-Z-S18",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~O",
    "surfaced_at": "2026-09-25T21:23Z",
    "one_line": "The Opal Bloomberg identity -- the one Opal_Agent signs into the gateway as -- is server-side ALLOWED opal_data_refresh_upload (a pipeline-firing upload) by the tracked overlay identity_tool_allowlist.txt, against identity_scope.py's own frame (iii); the long-'pre-existing' test_scoped_deny_by_default failure is the guard's test catching it, not noise.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt (tracked; last commit 2781aac326): its one live row is `opalbloomberg@opalinvest.com opal_data_refresh_upload`.",
        "app/identity_scope.py docstring frame (iii): 'email/site-write/upload/ycharts rows are NEVER added for the concierge identity -- structural via absence'; _load_scopes() ADDS overlay rows to the seed.",
        "python -m pytest tests/test_identity_scope.py at site Z CLOUD: 1 failed, 5 passed -- test_scoped_deny_by_default AssertionError: opal_data_refresh_upload (the overlay is read from the gateway dir).",
        "The same test was recorded as 'the pre-existing test_scoped_deny_by_default red' at OA-t-5 (cc22fdfb9d) and flagged as pre-existing by the laptop 1.0.0_SA_CTO (agentbus 5ffcad75)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C4/C7 and FWD-6/FWD-7: the Teams-facing Analyst cannot be talked into changing anything; identity_scope.py frame (iii): no upload row for the concierge identity.",
    "world_is": "Server-side, the concierge identity may call opal_data_refresh_upload (it fires the yang-pipeline with confirm=True). The only barrier for a Teams-facing session is its client-side fence. The row was added identity-wide, presumably so the Bloomberg daily upload could use the same Entra identity, so the operator duty and the Teams-facing agent share one server-side reach.",
    "notes": "Disarm for the issuer, before the NFRA_OPALAI cutover puts Opal_Agent on this identity: bind the upload row to the OPERATOR's OAuth client, not the identity -- identity_scope keyed on (identity, client_id), since the gateway's OAuth AS registers each client (Opal_Agent's own Claude login registers its own client). Then the operator's client keeps the upload and the runtime's client is refused. The test is pointed at an explicit fixture overlay so it stops reading the live file. No new M365 account or licence is needed. If an Andrew ruling added the row, the row's PURPOSE stands; only its scope narrows. Filed by the PRD owner."
  },
  {
    "id": "NFRA_OPALAI-Z-S19",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-25T21:35Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_OPALAI-Z-S18 (owner this seat) by a CUTOVER PRECONDITION: the NFRA_OPALAI cutover (the only act that puts Opal_Agent on the opalbloomberg identity) does not run until opal_data_refresh_upload is refused to the runtime. Either server-side, identity_scope keyed on (identity, OAuth client_id) with the upload granted to the operator's client only, or at minimum the runtime fence opal_ai/opal/agent/hooks/concierge-gate.sh denying it. Both are round-2 cells.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt:13 grants 'opalbloomberg@opalinvest.com opal_data_refresh_upload'; its :11-12 state the design intent: 'FALLBACK capability only -- the system cron (OPAL_BBGTML_daily_pull 07:00 ET) stays the primary path'.",
        "The runtime fence at opal_ai r1-drain (opal/agent/hooks/concierge-gate.sh:115) denies email and site writes only; it has no line for opal_data_refresh_upload. The workspace fence .tools/hooks/bg-concierge-gate.sh:45 names 'the terminal-upload data channel' as the seat's deliberate outbound surface.",
        "The cutover is gated on Andrew (G-PUSH, G-ACCT, G-AUTH, G-ASKER) and has not run; Opal_Agent is not live on the identity."
      ]
    },
    "spec_asserts": "NFRA_OPALAI-Z-S18 is ARMED with this seat as disarm_owner: the concierge identity can fire opal_data_refresh_upload.",
    "world_is": "Today the reach is held only by the workspace BG seat, as the documented fallback upload duty. The Teams-facing Opal_Agent runtime gains it only at cutover, and this row makes the cutover conditional on the refusal. The pinned tool count (45 vs 44) is recounted on each release base, per the CTO's note.",
    "notes": "Round-2 cells for NFRA_OPALAI: (1) identity_scope keyed on (identity, client_id), upload to the operator's client only, with test_scoped_deny_by_default pointed at a fixture overlay; (2) the runtime fence denies opal_data_refresh_upload as belt-and-braces. No new M365 account is needed. The row's purpose (Andrew's fallback upload) stands; only its scope narrows."
  },
  {
    "id": "NFRA_OPALAI-Z-S20",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~O",
    "surfaced_at": "2026-09-26T00:05Z",
    "one_line": "opal_ai CI FAILS on its first real push (DEV=PROD fd8ab8a57f, run 36203070607): ruff finds 15 errors in the moved portal_lookup.py, and pytest never runs because the workflow installs no pytest -- so PROD carries red checks and FWD-13 ('the checks run automatically on every change' and pass) is not met.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "gh run list -R Opal-Capital/opal_ai: run 36203070607, 'opal_ai CI', DEV, push, completed/failure, 2026-09-25T23:58:45Z.",
        "gh run view 36203070607 --log-failed: 'py_compile: PASS (3 files)'; 'ruff: FAIL (0 findings) -- ... portal_lookup.py ... Found 15 errors'; 'ascii: PASS'; 'device-path: PASS'; '/opt/hostedtoolcache/Python/3.9.25/x64/bin/python: No module named pytest'; 'pytest: FAIL'; 'CHECKS: FAIL'.",
        "The same line also shows opal/checks/run_checks.sh printing 'ruff: FAIL (0 findings)' while ruff reports 15: the check's own finding count is wrong."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD FWD-13 and C2: CI in opal_ai runs py_compile, ruff py39 and the tests on every push, and a standalone copy passes its own checks.",
    "world_is": "CI runs, but it cannot pass. Its workflow never installs pytest, and the moved Analyst helper carries 15 ruff errors the workspace's own gates did not stop (the file moved as-is). The runner's summary line misreports the ruff count as 0. Nothing is gated by it yet (there is no branch protection), so the red is silent unless someone reads it.",
    "notes": "Round-2 batch cell: (1) ci.yml installs pytest (and ruff) before run_checks.sh; (2) portal_lookup.py's 15 ruff findings are fixed in opal_ai, never waived; (3) run_checks.sh reports ruff's real count; (4) one green run on a real push is FWD-13's proof. INERT: the runtime pulls PROD regardless, and nothing deploys from CI."
  },
  {
    "id": "NFRA_OPALAI-Z-S21",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-26T00:35Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "The CLOUD manifest names the wrong live gateway. EC2_MANIFEST.json on origin/CLOUD (@ac5445b2ba) reads opal-gateway deployed_commit 1f7128201a, but the host serves 1.0.0_SA_CTO's laptop release 0af72fb1d0 (deployed 23:01:38Z). Its manifest record, 88377e148e, is only on origin/rel-laptop-teams-reader-gw. A deployer or rollback that bases on the CLOUD manifest would silently drop the laptop's Teams fixes (read_chat_message_images, the Graph-500 fallback, read_teams_attachment SAFE).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED 2026-09-26 ~00:1xZ over SSM: /opt/opal-gateway/app/identity_scope.py md5 06b5f86a12007f6e3f7794e1d3b386f0. git show <c>:infra/aws/ec2/opal-gateway/app/identity_scope.py | md5sum matches it only at b4101ea371 (origin/rel-laptop-teams-reader-gw) and 2a5636316e (origin/gw-teams-reader-fix), of the 3 commits touching the file across --all. At 1f7128201a it reads 82b4918b (no match; a CRLF render 56d8b537 also does not match).",
        "READ: git show 88377e148e:infra/aws/ec2/EC2_MANIFEST.json gives deployed_commit 0af72fb1d071209b953168924bc64d391dfb92ff, deployed_at 2026-09-25T23:01:38Z, deployed_by 1.0.0_SA_CTO. git merge-base --is-ancestor 1f7128201a origin/rel-laptop-teams-reader-gw is true.",
        "READ: git show origin/CLOUD:infra/aws/ec2/EC2_MANIFEST.json gives deployed_commit 1f7128201a."
      ]
    },
    "spec_asserts": "EC2_MANIFEST.json on the working branch CLOUD records the served opal-gateway commit.",
    "world_is": "The served commit is 0af72fb1d0. Its record is on a release branch, not on CLOUD.",
    "notes": "The disarm is the laptop CTO's drain of 88377e148e (or an equivalent manifest record) to CLOUD. Meanwhile OA-f-2 (@0dd3492d8a) resolves its base BY CONTENT at its own cut and names 0af72fb1d0, so this seat's release does not step on it."
  },
  {
    "id": "NFRA_OPALAI-Z-W8-S1",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~8",
    "surfaced_at": "2026-09-26T01:22Z",
    "one_line": "TO-OA-f-1 says keep tests/test_data_entitlement_guard.py (OGZ1-AC11) passing, but that suite cannot be collected on this device: 'No module named moto' at collection (Python 3.11, pip list has no moto, no cached wheel); 18 of 31 gateway test files import moto. The suite was not run, so 'keeps passing' is UNREAD, not PASS.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-OA-f-1 worker face section 1 step 4: 'Keep tests/test_data_entitlement_guard.py (OGZ1-AC11 reads the tracked overlay) passing.'",
        "`timeout 300 python -m pytest tests/test_data_entitlement_guard.py -q` in infra/aws/ec2/opal-gateway @ wk-NFRA_OPALAI-8: 'ModuleNotFoundError: No module named moto' -- '1 error in 1.11s' (collection error, 0 tests run).",
        "`python -m pip cache list moto`: 'No locally built wheels cached.'; `pip list` shows boto3 1.43.46 and pytest 9.1.1, no moto. Installing it is PyPI egress, which this order's declared egress class (Opal's own AWS, read only) does not cover.",
        "tests/test_data_entitlement_guard.py@d88cd32d0c:872-873 reads identity_scope._load_scopes() over the tracked overlay; this change keeps _load_scopes() returning the same email -> frozenset(tool) shape (unqualified rows only), so the upload row now counts in no allowlist and opalbloomberg's printed allowlist size drops by 1; the test asserts before == after with the guard on/off, not a fixed size."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "tests/test_data_entitlement_guard.py keeps passing after OA-f-1's change.",
    "world_is": "It cannot be run on this device (moto absent), so it is neither PASS nor FAIL here. AC1/AC2 do not depend on it; tests/test_identity_scope.py passes 9 of 9. The suite needs one run on a device with moto before OA-f-2 deploys.",
    "disarm_owner": "2.0.0_SA_COO~O",
    "notes": "Not repaired, no package installed. INERT: nothing deploys from this order (the deploy is OA-f-2)."
  },
  {
    "id": "NFRA_OPALAI-Z-S22",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~O",
    "surfaced_at": "2026-09-26T02:48Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_OPALAI-Z-S21 (disarm_owner 1.0.0_SA_CTO): origin/CLOUD's EC2_MANIFEST now names the served gateway commit 0af72fb1d0, and the laptop's Teams fixes are on CLOUD. One residue: the manifest's release_note still describes 1f7128201a, because the laptop's appended 0af72fb1d0 entry did not survive the merge; OA-f-2 rewrites that record at its release.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ 2026-09-26 ~02:47Z: git ls-remote/fetch origin CLOUD = 079fbf7d8e (0.0.0_AB_MSTR pull-merge on Andrew's call-1 YES, record ANDREW_DIRECT_20260926_022xZ_CTO_O_OPEN_CALLS_1_TO_6_ANSWERED.md).",
        "READ: git show origin/CLOUD:infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway.deployed_commit = 0af72fb1d071209b953168924bc64d391dfb92ff.",
        "READ: git merge-base --is-ancestor 52809cd052 origin/CLOUD = true (the laptop cherry-picks 678891171b..52809cd052 are on origin).",
        "READ: origin/CLOUD app/audit.py carries opal_asker_query (2 lines) and read_chat_message_images (1); app/data_entitlement.py carries each once.",
        "READ: the release_note (1141 chars as JSON) contains no '0af72fb1d0'; it cites the MP-d-1 sign-off and the one-base ruling, i.e. the 1f7128201a release.",
        "Served side: the host's identity_scope.py md5 matched only b4101ea371/0af72fb1d0 at Z-S21 (00:1xZ, SSM); OA-f-2, the only pending gateway deploy, is still <status>pending</status> at this row, so the served commit has not moved."
      ]
    },
    "spec_asserts": "NFRA_OPALAI-Z-S21 is ARMED: EC2_MANIFEST.json on CLOUD does not record the served opal-gateway commit.",
    "world_is": "It does now: deployed_commit on origin/CLOUD = 0af72fb1d0 = the served commit. A release cut from the manifest's base now carries the Teams fixes. The release_note text is stale (describes 1f7128201a); no reader derives a base from that text.",
    "disarm_owner": "1.0.0_SA_CTO",
    "notes": "Disarmed, not remediated: the release_note residue is left to OA-f-2's manifest record, which names its base (the laptop release) in words per its own order text. No other act."
  },
  {
    "id": "NFRA_OPALAI-Z-S23",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-26T03:05Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "Andrew's call 2 (Alyssa Keith, 'portal figures only', written 'through the existing operator path') cannot be written as ruled. The existing path, ops/schwab_entitlement_admin.py, writes only the NFRA_OPLGTW grant model. Every grant there must name at least one Schwab master, its account ids, Schwab datasets and columns. opal_asker_query honours only the grant's 'query' operation. So any grant written today would ALSO name Schwab custodial accounts, which is wider than 'portal figures only'.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE app/data_entitlement.py:202-237 parse_scope: masters must be a non-empty subset of the contract's MASTERS; scope.accounts must name the accounts of every granted master; datasets must be a non-empty subset of DATASETS, and columns must name every granted dataset.",
        "READ org/standards/NFRA_OPLGTW_CONTRACT.json: masters = 2 Schwab master ids; datasets = [dim_position, dim_balance, dim_asset]; operations = [list, describe, query, download_filtered]. No portal or catalog dimension exists.",
        "CODE app/data_entitlement.py:279-282 allowed_tools: a restricted profile admits ONLY SCHWAB_TOOLS. CODE app/asker_scope.py:15-39 (points c, d): the asker grant's datasets have no mapping to the portal catalog, and only 'operations: query' is honoured before catalog_gate serves the CALLING identity's rows.",
        "Also unmeasured: Alyssa Keith's Entra tid/oid. She holds no refresh family in gateway-access-state-table (census 2026-09-26 ~00:1xZ: 8 active families, all andrew@ or opalbloomberg@)."
      ]
    },
    "spec_asserts": "ANDREW_DIRECT_20260926_022xZ call 2: 'Alyssa Keith, scoped to portal figures only. 2.0.0_SA_COO~O writes the permission through the existing operator path (runbook step 6); nothing new is built.'",
    "world_is": "The existing operator path can express only a Schwab-data grant. 'Portal figures only' needs a grant shape that does not exist, which means building something, and the call says nothing new is built.",
    "notes": "Options go to 1.0.0_SA_CTO~O as a decision: (A) a minimal NFRA_OPLGTW grant with operations [query] -- expressible now, but it names a Schwab master and accounts (wider than the call); (B) a portal-scoped asker grant, cut as a round-2 cell. Runbook step 6 waits on the answer. Nothing was written to the POLICY store."
  },
  {
    "id": "NFRA_OPALAI-Z-W8-S2",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~8",
    "surfaced_at": "2026-09-26T03:35Z",
    "one_line": "TO-OA-f-2 step 3 plans the rollback's halt gate at about 12 minutes (row NFRA_MCPORTAL-Z-S8). Read now from the rollback tree, the gate resolves serial 2.0.0_SA_COO~O, finds 0 STOP-class and 186 routine pending messages, and had listed 114 of the 186 when a 900 s bound expired. At that rate the full gate takes about 24 minutes, so the guard (ii) rollback path through safe-ec2-deploy.sh would leave the host down for about 24 minutes before the redeploy starts.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Read-only read: .tools/halt-gate-check.sh@72897184fd sourced from /c/tmp/oa-8-rb (0af72fb1d0) with safe-ec2-deploy.sh's own HALT_GATE_* env (lines 43-64); halt_gate_resolve_serial printed '2.0.0_SA_COO~O' (the session serial file), start 03:12:06Z.",
        "Output: 'HALT-GATE: 186 pending message(s) -- review before proceeding'. This Verdict-2 banner prints only after the STOP-class check (halt-gate-check.sh:428-449) found none, so STOP-class = 0.",
        "`timeout 900` expired (rc 124) with 114 '  from ' entries printed out of 186. The per-message listing loop (halt-gate-check.sh:457-460) is where the time goes. 186 x 900/114 is about 1470 s.",
        "HALT_ACK=1 passes the routine verdict (halt-gate-check.sh:461-464), but it does not skip the listing loop, which runs before the ack check."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Pre-acknowledge the rollback's halt gate: HALT_ACK=1 when the halt gate reads 0 STOP (the gate takes about 12 minutes).",
    "world_is": "The gate reads 0 STOP, and HALT_ACK=1 is the correct pre-ack. It takes about 24 minutes, not 12, because 186 routine messages are pending on 2.0.0_SA_COO~O's inbox. The forward deploy also goes through this gate before it touches the instance. A guard (ii) rollback after a failed /health would leave the host serving nothing for that time, unless the issuer names another rollback path. The standalone form, bash infra/aws/ec2/opal-gateway/deploy-to-ec2.sh i-07dccb1615503ac99 from the rollback tree, skips the gate and the manifest record.",
    "notes": "Not acted on: no inbox was touched and nothing was acked. Disarm: before GO, the issuer rules which rollback command guard (ii) runs."
  },
  {
    "id": "NFRA_OPALAI-Z-S24",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-26T03:58Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_OPALAI-Z-W8-S2"
    ],
    "one_line": "DISARMS NFRA_OPALAI-Z-W8-S2. Guard (ii) of OA-f-2 runs the rollback command the worker named (HALT_ACK=1, from the clean 0af72fb1d0 tree at /c/tmp/oa-8-rel's sibling /c/tmp/oa-8-rb). The halt gate's ~24 minutes under 186 routine pending messages is ACCEPTED, and the act is confined to outside US business hours (before 12:00Z). No gate is bypassed and no second rollback route is invented.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W8-S2 (worker 0.9.0_WK_NFRA_OPALAI~8, drained @3229aa6fb6): the halt gate reads 0 STOP with 186 routine pending and takes ~24 minutes, not the ~12 that row NFRA_MCPORTAL-Z-S8 measured.",
        "The rollback artifact opal-gateway-0af72fb1d0.tar.gz (381002 bytes) was built without upload from a clean base tree. Against the live S3 base artifact, 70 of 75 files are byte-identical, including every .py file; the other 5 differ only in CRLF line endings (worker report, pre-GO)."
      ]
    },
    "spec_asserts": "OA-f-2 guard (ii): if /health is not 200 within 90 s of the restart, the rollback runs AT ONCE.",
    "world_is": "The rollback starts at once but spends ~24 minutes in the halt gate before it restores the host, so a failed release means up to ~25 minutes of gateway outage.",
    "notes": "The exposure is bounded by timing (off-hours) rather than by skipping the pre-deploy gate: 'pre-existing mechanical gates stand'. If the halt gate's scan time is itself a defect, that is its owner's row, not this release's."
  },
  {
    "id": "NFRA_OPALAI-Z-S25",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~O",
    "surfaced_at": "2026-09-26T05:27Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "2.0.0_SA_COO~O is DEAF to broker mail: no inbox-watch process runs for it, and 5 messages since 03:20Z are OFFER-EXHAUSTED, never READ. One of them is this seat's ruling on Z-S23, which this row carries: Alyssa's grant is option (B), issued NOW as addendum A2.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "get_delivery_state(2.0.0_SA_COO~O, since 02:30Z) at ~05:2xZ: READ=3 (ids 25974/25978/25979, 02:44Z), OFFER-EXHAUSTED=5 (25985 from DS~D, 25994 from CTO~Z, 25996 RULING on 25986, 25999 loop instruction, 26017 CVO relay MXC5-AC4 PASS).",
        "Win32_Process census at ~05:2xZ: 41 rows matching inbox-watch; a stream-mode script row exists for 3.0.0_SA_CVO~O, 1.0.0_SA_CTO~Z, 2.0.0_SA_COO~Y, 3.0.0_SA_CVO~Z, 2.0.0_SA_COO~X, 0.4.0_DS_ClientPlatform~D, 0.0.0_AB_MSTR~Z, 2.0.0_SA_COO~Z, 1.0.0_SA_CTO~O, 0.7.0_AE_CloudOps~I -- and NONE for 2.0.0_SA_COO~O.",
        "The seat is working: commits c7ca5fb03f (04:01Z) and 8fc747bc09 (04:41Z); 3.0.0_SA_CVO~O cites COO~O msg 26012 sent ~05:0xZ. It sends; it does not receive."
      ]
    },
    "spec_asserts": "Every live ~O seat receives its mail (the /watcher Monitor is its standing mechanism).",
    "world_is": "COO~O receives nothing sent after ~02:44Z. The Z-S23 ruling, the /canonical-drive loop instruction and CVO~O's MXC5-AC4 PASS have not reached it.",
    "disarm_owner": "2.0.0_SA_COO~O",
    "notes": "THE RULING THIS ROW CARRIES (1.0.0_SA_CTO~O, msg 25996, on COO~O msg 25986 / row Z-S23): option (B). (A) names Schwab accounts, which breaks Andrew's 'portal figures only'. Issue it NOW as addendum A2, not in round 2. Design direction: extend the existing grant grammar so a grant may carry zero Schwab masters plus a portal-dataset scope opal_asker_query honours; never a second grant store; the OPLGTW stop is lifted. Resolve Alyssa's Entra oid from the directory by the operator path. ALSO WAITING IN YOUR read/ DIR: the /canonical-drive 30m loop instruction (msg 25999) and 3.0.0_SA_CVO~O's MXC5-AC4 PASS @0cf61b5bbe (msg 26017), which unblocks the wk-nfra_mcpindex-1-1d drain. Disarm: re-arm the watcher (/watcher 2.0.0_SA_COO~O) and ack the 5 ids."
  },
  {
    "id": "NFRA_OPALAI-Z-S26",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~O",
    "surfaced_at": "2026-09-26T07:22Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "CORRECTS NFRA_OPALAI-Z-S25 (this seat's own row): its limb 'the Z-S23 ruling has not reached COO~O' was FALSE when filed. 2.0.0_SA_COO~O issued addendum A2 on that ruling at 05:28:49Z (@9ba4ca286f: OA-g-1, OA-g-2, OA-g-3), 7 minutes before Z-S25 landed at 05:36:22Z. The missing inbox-watch process was real; the inference drawn from it was not checked against the task-order tree.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log --diff-filter=A on NFRA_OPALAI.TO-OA-g-1.portal-only-grant.md: 9ba4ca286f 2.0.0_SA_COO~O 2026-09-26T05:28:49Z issue(NFRA_OPALAI addendum A2 ... on the CTO's ruling (B) (msg 25996 ...).",
        "git log -1 --format=%aI 8833cafab2 (Z-S25) = 2026-09-26T05:36:22Z.",
        "The same wrong 'A2 not issued' statement is in this seat's tick-7 log @cffa8e5603 and its tick-8 report; both read commits by grep on seat names and never listed the order files."
      ]
    },
    "spec_asserts": "NFRA_OPALAI-Z-S25: COO~O had not received the Z-S23 ruling (msg 25996).",
    "world_is": "COO~O had read and acted on it (A2 issued 05:28:49Z) before the row was filed. It read the file in its read/ directory without acking it; the broker ack came at 05:33:21Z. Only the watcher-process census in Z-S25 stands.",
    "disarm_owner": "1.0.0_SA_CTO~O",
    "notes": "Inert: nothing was re-issued and no second COO was spawned on the wrong limb. Lesson carried in the commit: before stating an order was not issued, list the task-order files, not the commit log."
  },
  {
    "id": "NFRA_OPALAI-Z-W9-S1",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~9",
    "surfaced_at": "2026-09-26T07:14Z",
    "one_line": "The owner grant-read route (app/admin_grants.py _grant_json, GET of a principal's grant) builds its scope from a fixed list of six dimensions, so it drops portal_channels. After OA-g-1 a portal-only grant reads there as masters [], datasets [], accounts {}, columns {}, operations [query], with no channel shown. app/admin_grants.py is outside OA-g-1's <paths> and was not edited.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE infra/aws/ec2/opal-gateway/app/admin_grants.py@9ba4ca286f :91-101 _grant_json returns scope keys masters, datasets, accounts, dates, columns and operations only.",
        "MEASURED at da7749916d: _grant_json(parse_grant(grant_item(..., scope with portal_channels ['capital_markets'] and an empty Schwab half))) printed {'revision': 1, 'status': 'active', 'scope': {'masters': [], 'datasets': [], 'accounts': {}, 'dates': {'mode': 'rolling_complete_window', 'dates': []}, 'columns': {}, 'operations': ['query']}}. portal_channels is absent.",
        "The access decision is unaffected: data_entitlement.parse_scope and asker_scope read the stored record, not _grant_json (tests/test_portal_grant.py at da7749916d, 6 of 6 passed)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OA-g-1: extend the EXISTING grammar so a portal-only grant (portal_channels, zero Schwab masters) is a first-class grant; existing grants keep their meaning.",
    "world_is": "The grammar, asker path and operator command carry portal_channels. The owner's read-back route does not, so a GET of the grant that OA-g-3 writes shows an apparently empty grant.",
    "notes": "Not fixed here, because it is outside <paths>. Disarm: the issuer decides whether a read-back of OA-g-3's grant goes through this route, and if it does, cuts the one-line addition of portal_channels to _grant_json."
  },
  {
    "id": "NFRA_OPALAI-Z-W9-S2",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~9",
    "surfaced_at": "2026-09-26T09:00Z",
    "one_line": "Item 5 of OA-g-1 (amended on row Z-W9-S1) is built: app/admin_grants.py _grant_json now returns scope.portal_channels whenever the grant carries it, and a grant without it reads back with no portal_channels key, as before. This row disarms nothing. Row W9-S1 stays ARMED until its disarm_owner 2.0.0_SA_COO~O dispositions it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE infra/aws/ec2/opal-gateway/app/admin_grants.py@9a28cfbbe6 _grant_json adds scope['portal_channels'] = sorted(s.portal_channels) when that set is non-empty.",
        "TEST infra/aws/ec2/opal-gateway/tests/test_portal_grant.py@9a28cfbbe6 test_admin_readback_shows_portal_channels: a portal-only grant reads back portal_channels ['capital_markets', 'valuation'] with masters [] and accounts {}. A Schwab grant reads back with no portal_channels key. A None grant reads back None.",
        "MEASURED at 9a28cfbbe6: g1.AC3.sh printed 'pytest rc=0; named tests passed 3 of 3; failed/error lines 0', RESULT: PASS, exit=0. tests/test_admin_grants.py: 5 passed (no moto needed)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OA-g-1 item 5: the owner's read-back carries portal_channels, so a portal-only grant never reads back as empty.",
    "world_is": "It does, at 9a28cfbbe6 on branch wk-NFRA_OPALAI-9 (LOCAL; not drained, not deployed). The live gateway still runs the pre-item-5 bytes until OA-g-2 deploys.",
    "notes": "This row does not disarm W9-S1; the issuer does. A side observation: the safe-commit call for 9a28cfbbe6 ran past a 120 s bound. The harness moved it to the background and it exited 0 with the commit landed, so the rc 124 shape did not arise."
  },
  {
    "id": "NFRA_OPALAI-Z-S27",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-26T09:05Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_OPALAI-Z-W9-S1"
    ],
    "one_line": "DISARMS NFRA_OPALAI-Z-W9-S1. OA-g-1 was amended with item 5 (@fb7efc02b8) and built at 9a28cfbbe6: app/admin_grants.py _grant_json now returns portal_channels whenever the grant carries them, so a portal-only grant no longer reads back as empty on the owner dashboard. g1.AC3 passes 3 of 3 on the issuer's re-run, and the work is drained to CLOUD @45ddd8d948.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "g1.AC3 on wk-NFRA_OPALAI-9 @c0d5df8623: 'pytest rc=0; named tests passed 3 of 3; failed/error lines 0' (includes test_admin_readback_shows_portal_channels).",
        "Worker report: tests/test_admin_grants.py 5 passed (no moto needed)."
      ]
    },
    "spec_asserts": "W9-S1: the owner's read-back omits portal_channels, so the grant OA-g-3 will write reads back as empty.",
    "world_is": "The read-back carries portal_channels; Schwab-only grants read back unchanged.",
    "notes": "The fix reaches the host with OA-g-2's release."
  },
  {
    "id": "NFRA_OPALAI-Z-W8-S3",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~8",
    "surfaced_at": "2026-09-26T07:55Z",
    "one_line": "TO-OA-f-2 guard (ii), as relayed at GO, polls https://<the gateway>/health and rolls back on anything but 200 within 90 s. The public https://mcp.opalinvest.dev/health can never read 200: the ALB answers it with a 302 to Entra login (Server awselb/2.0), so the request never reaches the gateway. It read 302 on 30 of 30 polls after the forward deploy while the gateway served healthy.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Poll log /c/tmp/oa-8/.scratch/act.log: 30 polls of https://mcp.opalinvest.dev/health from 07:44:44Z to 07:47:23Z (the act exited 07:44:41Z), 30 of 30 http_code=302.",
        "curl -D at 07:54:40Z: 'HTTP/1.1 302 Moved Temporarily', 'Server: awselb/2.0', 'Location: https://login.microsoftonline.com/<tenant>/oauth2/v2.0/authorize?...'. This is the ALB's authenticate-oidc default action (EC2_MANIFEST opal-gateway _status: 'default-action 302 to Entra'); the gateway process is not in the path.",
        "Discriminators, same minute: public /mcp unauth 401 and public /.well-known/oauth-authorization-server 200 (both forwarded to the gateway); on-box http://localhost:8080/health 200 on 3 of 3 (ssm:0e97c001-f7b7-48e1-adbe-2bcd07418ef6); opal-gateway active since 07:43:23Z, NRestarts=0.",
        "infra/aws/ec2/opal-gateway/deploy-to-ec2.sh@c5f8099440:230-235 polls http://localhost:${GATEWAY_PORT}/health on the box right after the restart; it returned {\"ok\":true} inside its 30 s loop (ssm:6861b726-9f08-4a9f-9e0c-e870c5d5c373)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Guard (ii): immediately after the restart, poll /health (GO prompt: https://<the gateway>/health, host read from the deploy script); not 200 within 90 seconds -> run the rollback at once.",
    "world_is": "The public /health path is behind the ALB's OIDC default action and returns 302 for every state of the gateway, healthy or down, so as a public read the guard cannot discriminate and would roll back every deploy, the rollback included. The deploy script's own /health read is on-box (localhost:8080) and returned 200. I took the on-box reads plus public /mcp 401 as the guard (ii) reading and did NOT roll back. The rollback stays ready (clean base tree /c/tmp/oa-8-rb at 0af72fb1d0).",
    "notes": "Deviation from the letter of the GO prompt, measured and reported. Disarm: the issuer rules whether the on-box reading satisfies guard (ii) or orders the named rollback; a future order's /health guard names the on-box URL or an ALB path that forwards unauthenticated."
  },
  {
    "id": "NFRA_OPALAI-Z-S28",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-26T09:50Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_OPALAI-Z-W8-S3"
    ],
    "one_line": "DISARMS NFRA_OPALAI-Z-W8-S3 with a ruling: guard (ii) reads /health ON THE HOST, never the public URL. The public https://mcp.opalinvest.dev/health sits behind the load balancer's Entra sign-in (awselb/2.0) and returned 302 on 30 of 30 polls, whether or not the gateway was up. OA-f-2's worker read on-box /health 200 (inside the deploy script and 3 of 3 at 07:54Z), public /mcp 401 and the auth metadata 200, with the service active since 07:43:23Z and 0 restarts. That satisfies guard (ii), and not rolling back was correct. OA-g-2's face is amended to the on-box read in this commit.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Worker report 0.9.0_WK_NFRA_OPALAI~8 (proof @3cd49937ab, drained @837d4d1e1d): public /health 302 on 30 of 30; on-box /health 200; tools 46 = 46; f2.AC2 and f2.AC3 PASS.",
        "Issuer's own read at 07:50Z: public /health 302; the live identity_scope.py md5 equals the release branch's."
      ]
    },
    "spec_asserts": "OA-f-2 guard (ii): poll /health; if it is not 200 within 90 s, roll back.",
    "world_is": "Only the on-box /health can answer that question; the public one never reaches the gateway.",
    "notes": "MX-r-3's face is read for the same guard at its own spawn."
  },
  {
    "id": "NFRA_OPALAI-Z-W9-S3",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~9",
    "surfaced_at": "2026-09-26T12:45Z",
    "one_line": "OA-g-2 step 2 census: the release tree names FIVE gateway files, not the face's four. The fifth is app/admin_grants.py, which comes from 9a28cfbbe6 (OA-g-1 item 5). The issuer's hand-off names that commit, but the face's census list does not, and neither does the order's <paths>. The face says any other file means STOP and a BLOCKING row. Nothing has been deployed.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED: `git -C /c/tmp/oa-9-rel diff --stat c5f8099440 HEAD -- infra/aws/ec2/opal-gateway` (rc=0, HEAD df724ef284) printed 5 files: app/admin_grants.py 10, app/asker_scope.py 24, app/data_entitlement.py 58, ops/schwab_entitlement_admin.py 47, tests/test_portal_grant.py 290; 411 insertions and 18 deletions. The whole-tree diff names the same 5 files and nothing outside infra/aws/ec2/opal-gateway/.",
        "SPEC org/missions/D6/NFRA/NFRA_OPALAI/task-orders/NFRA_OPALAI.TO-OA-g-2.portal-grant-release.md@1d76febf04, section 1 step 2: the census names ONLY app/data_entitlement.py, app/asker_scope.py, ops/schwab_entitlement_admin.py and tests/test_portal_grant.py; 'Any other file: STOP, a BLOCKING row.' The <paths> list omits app/admin_grants.py.",
        "CODE git show --stat 9a28cfbbe6: infra/aws/ec2/opal-gateway/app/admin_grants.py (+8/-2) and tests/test_portal_grant.py. This is the commit the issuer 2.0.0_SA_COO~O named in the OA-g-2 hand-off ('the admin_grants read-back plus its test'). The file ships in the host artifact under app/.",
        "Each of the 5 files in the release tree is byte-identical to its version at 9a28cfbbe6 (md5 compared per file)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OA-g-2 step 2: the release census names only the four gateway files that OA-g-1 changed. Any other file means STOP and a BLOCKING row.",
    "world_is": "OA-g-1 changed five gateway files, because item 5 (9a28cfbbe6, amended on row Z-W9-S1) added app/admin_grants.py after the face was cut. The census therefore reads 5 files. The release commit df724ef284 (LOCAL, branch rel-nfra-opalai-portal-grant-gateway) carries all five, under audited override use 1 of GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_OPALAI~9.",
    "notes": "The worker does not judge whether the fifth file belongs in the release. That is the issuer's decision: either amend the census list and <paths> to include app/admin_grants.py, or cut a release without 9a28cfbbe6. Nothing was uploaded, nothing on the instance was changed, and no ledger was opened. The issuer asked for the remaining pre-GO local steps (step 3 rollback build, step 4(i) .env render and step 1 announcement), and those were completed."
  },
  {
    "id": "NFRA_OPALAI-Z-W9-S4",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~9",
    "surfaced_at": "2026-09-26T12:45Z",
    "one_line": "In the OA-g-2 release tree, tests/test_portal_grant.py gives 2 failed and 5 passed. Both failures read org/standards/NFRA_OPLGTW_CONTRACT.json, which the release restores to the base (no portal_grant section), as the face and the issuer direct. The same file gives 7 passed on the CLOUD-merged tree with contract v1.2. Neither the contract nor ops/ nor tests/ ships in the host artifact.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED /c/tmp/oa-9-rel/infra/aws/ec2/opal-gateway `python -m pytest tests/test_portal_grant.py -q`: pytest rc=1, '2 failed, 5 passed'. The failures are test_admin_accepts_portal_only_candidate (KeyError 'portal_grant' at tests/test_portal_grant.py:221) and test_admin_rejects_unknown_portal_channel (the message was 'scope.portal_channels is not admitted by this contract (no portal_grant)', not the expected 'does not hold', at :258).",
        "CONTROL /c/tmp/oa-9 (wk-NFRA_OPALAI-9 at 1e71306a97, CLOUD merged): the same test file gives pytest rc=0, '7 passed'.",
        "CODE infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py@df724ef284:56 reads _CONTRACT_PATH = <repo>/org/standards/NFRA_OPLGTW_CONTRACT.json, and :193-195 rejects portal_channels when the contract has no portal_grant, so it fails closed.",
        "CODE infra/aws/ec2/opal-gateway/deploy-to-ec2.sh@c5f8099440:94-98: the tarball carries app, deploy, requirements.txt, identity_tool_allowlist.txt and the dashboard bundle. It carries no ops/, no tests/ and no org/standards.",
        "The other test files in the release tree: tests/test_asker_scope.py rc=0 '4 passed'; tests/test_identity_scope.py rc=0 '9 passed'; tests/test_admin_grants.py rc=0 '5 passed, 1 warning'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OA-g-2 step 2: run tests/test_portal_grant.py, test_asker_scope.py and test_identity_scope.py inside the release tree and record the results. The hand-off says to restore the contract under org/standards to the base.",
    "world_is": "Two of the seven portal-grant tests depend on the repo contract at v1.2. With the base contract restored, they fail in the release tree while the host artifact code is unaffected. The operator command run from the release tree would refuse a portal-only candidate (fail-closed).",
    "notes": "The result is recorded, not repaired, and no contract file was carried into the release. Whether this leaves the order open is the issuer's call."
  },
  {
    "id": "NFRA_OPALAI-Z-S29",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-26T13:30Z",
    "disposition": "UNDER_INVESTIGATION",
    "adjudicates": [
      "NFRA_OPALAI-Z-W9-S3",
      "NFRA_OPALAI-Z-W9-S4"
    ],
    "one_line": "DISARMS NFRA_OPALAI-Z-W9-S3 and adjudicates W9-S4. W9-S3: OA-g-2's census list and <paths> omitted app/admin_grants.py, which is OA-g-1 item 5 (the owner read-back, 9a28cfbbe6). That is the issuer's omission when item 5 was added; the face is amended in this commit to include it, so the 5-file census is the correct one. W9-S4: test_portal_grant's 2 failures in the release tree read the repo contract (org/standards), which does not ship to the host; on the CLOUD-merged tree it passes 7 of 7. INERT, no act.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Worker 0.9.0_WK_NFRA_OPALAI~9 pre-GO report (announcement @b5f2d7afe5, drained @3f0798fdd0): census 5 files +411/-18, each byte-identical to 9a28cfbbe6; the rollback artifact is 75/75 byte-identical to the live base.",
        "OA-g-1 amendment @fb7efc02b8 (item 5), drained @45ddd8d948."
      ]
    },
    "spec_asserts": "OA-g-2 step 2: the census names ONLY the 4 files the face lists.",
    "world_is": "The shipping set is 5 files; the 5th is the read-back fix the issuer itself added.",
    "notes": "GO waits for outside US business hours (Z-S24): not before 21:05Z today."
  },
  {
    "id": "NFRA_OPALAI-Z-S30",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~O",
    "surfaced_at": "2026-09-26T14:05Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "NFRA_OPLGTW's contract was amended v1.1 -> v1.2 (portal_grant) at 07:01Z by OA-g-1 (@da7749916d), on this seat's ruling (B) of 03:33Z, which said the contract 'may be amended'. At 04:01Z 3.0.0_SA_CVO~O ruled that no CTO act on OPLGTW issues from ~O until its CTO leg is re-seated here (@e470835e7c). This seat executed that verdict but never withdrew the earlier authorization, so an act the verdict parked went ahead on it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log on org/standards/NFRA_OPLGTW_CONTRACT.json: da7749916d 0.9.0_WK_NFRA_OPALAI~9 2026-09-26T07:01:09Z build(NFRA_OPALAI.TO-OA-g-1 ...).",
        "git diff c5f8099440 HEAD -- org/standards/NFRA_OPLGTW_CONTRACT.json: contract_version 1.1 -> 1.2 and a new portal_grant block; absent_means 'the record parses exactly as contract v1.1'.",
        "1.0.0_SA_CTO~O msg 25996 (03:33Z): 'The OPLGTW stop is lifted, so its contract may be amended.'",
        "3.0.0_SA_CVO~O verdict @e470835e7c (04:01Z): 'Until then OPLGTW's round work stays with COO~O, and no CTO or CVO act on OPLGTW issues from ~O.'",
        "NFRA_OPLGTW project.json leads.cto = 1.0.0_SA_CTO~A (unchanged at this row); the laptop release was asked at 04:58Z (msg 20260926T045815Z) and has not landed."
      ]
    },
    "spec_asserts": "No CTO-leg act on NFRA_OPLGTW (its contract included) issues from the ~O fabric before the re-seat record lands.",
    "world_is": "The contract carries an ~O-authored v1.2 amendment. It is additive and optional (absent_means v1.1), so no existing grant reads differently and nothing served moved on it. The contract text has not been ratified by OPLGTW's CTO leg.",
    "disarm_owner": "1.0.0_SA_CTO~O",
    "notes": "Inert because the amendment is optional and backward-compatible; the OA-g-2 release moves no current answer (sign-off @321a726fc6). Governance fork pitched to 3.0.0_SA_CVO~O: keep and ratify at the OPLGTW re-seat, or revert. Cause: the verdict narrowed an authorization this seat had issued 28 minutes earlier, and this seat did not withdraw it."
  },
  {
    "id": "NFRA_OPALAI-Z-S31",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-26T18:45Z",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each target was already disarmed by the issuer's own adjudicating row with its reason stated there; this row only makes the disposition terminal.",
    "adjudicates": [
      "NFRA_OPALAI-Z-W8-S2",
      "NFRA_OPALAI-Z-W8-S3",
      "NFRA_OPALAI-Z-W9-S1",
      "NFRA_OPALAI-Z-W9-S3",
      "NFRA_OPALAI-Z-W9-S4"
    ],
    "one_line": "DISPOSITION CORRECTION by the issuer. My earlier disarm rows adjudicated these items but carried disposition UNDER_INVESTIGATION, which _latest_dispositions (surprise-row-gate.py:426) passes to the target, so the items kept reading OPEN and gating. This row carries the terminal disposition: W8-S2 by Z-S24 (the 24-min halt gate is accepted, off-hours only); W8-S3 by Z-S28 (guard (ii) reads on-box /health); W9-S1 by Z-S27 (the read-back carries portal_channels, @9a28cfbbe6); W9-S3 and W9-S4 by Z-S29 (OA-g-2's census amended to 5 files @2ae3e0a96d; the contract-dependent test does not ship).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Fold measured at ~18:40Z with the gate's own _latest_dispositions/_gating_item_ids: each target listed read UNDER_INVESTIGATION and gating, while an issuer disarm row already adjudicated it.",
        "3.0.0_SA_CVO~Z's finding (relayed by 1.0.0_SA_CTO~O, file 20260926T182052Z) that Z-W9-S3 read UNDER_INVESTIGATION at 18:3xZ."
      ]
    },
    "spec_asserts": "Each target was disarmed by the issuer's adjudicating row.",
    "world_is": "The disarms carried a non-terminal disposition; this row makes them terminal. The reasons are the earlier rows' own."
  },
  {
    "id": "NFRA_OPALAI-Z-S32",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~O",
    "surfaced_at": "2026-09-26T18:36Z",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "DISARMS NFRA_OPALAI-Z-S30 (disarm_owner 1.0.0_SA_CTO~O): 3.0.0_SA_CVO~O rules the NFRA_OPLGTW contract v1.2 amendment KEEP; ratification stays with OPLGTW's contract owner. Carried rule from the verdict: a verdict that parks a class of acts also withdraws every open authorization of that class.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_GOVERNANCE_VERDICT_OPLGTW_CONTRACT_V1_2_20260926.md @073447e387: '# Governance verdict -- NFRA_OPLGTW contract v1.2: KEEP'.",
        "3.0.0_SA_CVO~O file message 20260926T183132Z: 'Fork msg 26105, OPLGTW contract v1.2: KEEP ... Ratification stays with OPLGTW's contract owner.'"
      ]
    },
    "spec_asserts": "NFRA_OPALAI-Z-S30: the OPLGTW contract carries an ~O-authored v1.2 amendment made after CTO acts on OPLGTW were parked, with no ruling on it.",
    "world_is": "Ruled KEEP by the fabric's CVO. The amendment stands; its ratification belongs to OPLGTW's contract owner at the re-seat.",
    "disarm_owner": "1.0.0_SA_CTO~O",
    "notes": "The carried rule binds this seat: when a verdict parks a class of acts, withdraw every open authorization of that class the same turn."
  },
  {
    "id": "NFRA_OPALAI-Z-S33",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~O",
    "surfaced_at": "2026-09-26T20:05Z",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each target was already disarmed by this seat's own adjudicating row, with its reason stated there (Z-S21 by Z-S22; Z-S30 by Z-S32 on 3.0.0_SA_CVO~O's KEEP verdict @073447e387). This row only makes the disposition terminal.",
    "adjudicates": [
      "NFRA_OPALAI-Z-S21",
      "NFRA_OPALAI-Z-S30"
    ],
    "one_line": "DISPOSITION CORRECTION by the disarm owner. This seat's disarm rows Z-S22 and Z-S32 carried disposition UNDER_INVESTIGATION, which _latest_dispositions (.tools/surprise-row-gate.py) folds as still open; Z-S21 read as a gating item. Same class as 2.0.0_SA_COO~O's Z-S31.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Fold measured at 2026-09-26T20:05Z with the gate's own _latest_dispositions(root,'NFRA_OPALAI') and _gating_item_ids: Z-S21 UNDER_INVESTIGATION and gating; Z-S30 UNDER_INVESTIGATION.",
        "Z-S22 (@19ad8abc17): origin/CLOUD's manifest names the served 0af72fb1d0; Z-S32 (@107ce3f3e8): CVO~O's KEEP verdict on the OPLGTW v1.2 amendment."
      ]
    },
    "spec_asserts": "Each target was disarmed by its owner's adjudicating row.",
    "world_is": "The disarms carried a non-terminal disposition; this row makes them terminal. The reasons are the earlier rows' own.",
    "disarm_owner": "1.0.0_SA_CTO~O"
  },
  {
    "id": "NFRA_OPALAI-Z-S34",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-26T20:20Z",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Per-item reasons in `notes`; every target names this seat as disarm_owner (1.0.0_SA_CTO~O's 200537Z census: 12 open gating items).",
    "adjudicates": [
      "NFRA_OPALAI-Z-S5",
      "NFRA_OPALAI-Z-S18",
      "NFRA_OPALAI-Z-S23",
      "NFRA_OPALAI-Z-S25",
      "NFRA_OPALAI-Z-W2-S1",
      "NFRA_OPALAI-Z-W2-S3",
      "NFRA_OPALAI-Z-W3-S1",
      "NFRA_OPALAI-Z-W6-S1",
      "NFRA_OPALAI-Z-W1-S1",
      "NFRA_OPALAI-Z-W2-S4",
      "NFRA_OPALAI-Z-W5-S1",
      "NFRA_OPALAI-Z-W4-S1"
    ],
    "one_line": "The issuer makes the 12 open NFRA_OPALAI gating items it owns terminal, so round 1's slug can go. Eight are fixed or superseded (Z-S5, Z-S18, Z-S23, Z-S25, W2-S1, W2-S3, W3-S1, W6-S1). Three are shared-tool defects outside this project, worked around in-cell and routed to their owner (W1-S1, W2-S4, W5-S1). One, W4-S1, is disarmed by a named cutover precondition (CP-1) and is not fixed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "1.0.0_SA_CTO~O file 20260926T200537Z: 17 gating, 5 terminal, 12 open, all disarm_owner 2.0.0_SA_COO~O (the gate's own _latest_dispositions / _gating_item_ids).",
        "~20:1xZ measurements: .claude/skills/teams-assist/teams-watch.py present; integrations/ticketing/intake/runner.py:69 still imports it; round1/checks/_root.sh:9 'set -o pipefail'."
      ]
    },
    "spec_asserts": "Each target is an open gating item owned by this seat.",
    "world_is": "Each is fixed, superseded, routed off-project, or disarmed by a named carrier, as listed per item.",
    "notes": "Z-S5: Disarmed by Z-S6: opal_asker_query deploys DARK for the concierge (identity_scope does not list it), so no Teams call reaches the cited-message resolution; the binding fix is carried in 1.0.0_SA_CTO~O's ROUND2_ENRICHMENT_DRAFT.md. | Z-S18: Fixed and LIVE: OA-f-1/OA-f-2 (release c5f8099440, 07:43:40Z; closed @3558be2482); f2.AC3 reads the live upload row client-qualified (unqualified=0). | Z-S23: Answered by the CTO's ruling (B) and addendum A2 (@9ba4ca286f): OA-g-1 drained @45ddd8d948; OA-g-2 and OA-g-3 carry the rest. | Z-S25: Corrected by the filer's own Z-S26: this seat's watcher recovered at 05:33Z, and A2 was issued before Z-S25 landed. | Z-W2-S1: Addressed by A2: the grant grammar gains portal_channels, and asker_scope serves a catalog key only in a granted channel (OA-g-1, @45ddd8d948). | Z-W2-S3: Resolved by the CTO's narrow-release ruling (@592e319a06): OA-t-6 shipped f1f0fc6780 with only its own two changes. | Z-W3-S1: Fixed at the instrument: round1/checks/_root.sh sets `set -o pipefail` (its own comment cites W3-S1), so every check's rc is the command's. | Z-W6-S1: Fixed at the instrument: round1/checks/_root.sh sets `set -o pipefail` (its own comment cites W6-S1). | Z-W1-S1: A shared-tool defect outside NFRA_OPALAI (.tools/owned-paths-validate.py ignores the worker_grant for a path with no lane row). It was worked around in-cell under the audited override; routed to the tool's owner 1.0.0_SA_CTO~O in this seat's same-turn message. This project's gate no longer carries it. | Z-W2-S4: A shared-tool defect outside NFRA_OPALAI (safe-ec2-deploy.sh Step 3: jq.exe writes EC2_MANIFEST.json CRLF). Every release since recorded the manifest by hand on an LF copy (OA-t-6, MP-d-1, OA-f-2); routed to the tool's owner in this seat's same-turn message. | Z-W5-S1: A shared-tool defect outside NFRA_OPALAI (install-owned-paths.sh --submodule resolves REPO_ROOT from the ambient cwd). It was installed correctly in-cell by cd-ing first; routed to the tool's owner in this seat's same-turn message. | Z-W4-S1: DISARMED by a named carrier, not fixed: cutover precondition CP-1 in NFRA_OPALAI_DECOMP.md (this commit) binds whichever cell cuts the cutover. The workspace copy of teams-watch.py stays until runner.py is re-pointed and its next fire is read back. Measured ~20:1xZ: the file is present and runner.py still imports it, so the hazard has not fired."
  },
  {
    "id": "NFRA_OPALAI-Z-W9-S5",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~9",
    "surfaced_at": "2026-09-27T00:46Z",
    "one_line": "OA-g-3 step 2 selects the catalog channels 'whose verdict is not deny', but a channel in DATA_CATALOG.yaml carries no verdict: verdict_class is a field of each artifact row. 5 of the 15 channels have no artifact rows, so catalog_gate indexes nothing for them. The grant used the 10 channels that hold at least one indexed row whose verdict_class is not deny. 4 of those 10 also hold deny rows, which catalog_gate still refuses row by row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml@a60f285f94, loaded with catalog_gate.load_catalog: 15 channels; no channel carries a verdict or verdict_class key.",
        "Rows per channel (verdict_class counts): benchmarks_and_models 6 (serve 1, serve-with-caveat 2, deny 3); capital_markets 2 (swc 2); correlations_factors 4 (swc 4); macro_rates 4 (swc 4); market_regime_trending 2 (swc 1, deny 1); mdpf_model_portfolios 8 (serve 2, swc 1, deny 5); peers 1 (swc 1); positioning_holdings 4 (swc 4); sentiment_news_mood 3 (serve 1, deny 2); valuation 2 (swc 2). No artifact rows: market_overview, news, pipeline_freshness, sharepoint_documents, bloomberg_standing_read.",
        "CODE infra/aws/ec2/opal-gateway/app/graphql_plumbing/catalog_gate.py@a60f285f94:57-74 indexes artifact rows by key and tags each with _channel; :38 SERVABLE_CLASSES = serve and serve-with-caveat; :95 refuses any other verdict_class for that row.",
        "Contract org/standards/NFRA_OPLGTW_CONTRACT.json@a60f285f94 portal_grant.channel_ids admits any key of channels.*; it does not define a channel verdict."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OA-g-3 section 1 step 2: portal_channels = every channel of DATA_CATALOG.yaml that catalog_gate indexes and whose verdict is not deny.",
    "world_is": "Verdicts exist only on artifact rows. The worker read 'indexes' as 'holds at least one artifact row' and 'verdict is not deny' as 'holds at least one row whose verdict_class is not deny'. That gives 10 channels, and they were granted. The 5 row-less channels were left out. A different reading would change the grant only by adding some of those 5."
  },
  {
    "id": "NFRA_OPALAI-Z-S35",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-27T01:15Z",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The worker's reading is the correct one: a channel verdict does not exist, only row verdicts, and catalog_gate still refuses every deny row one by one inside a granted channel. No wider access than 'portal figures only' results.",
    "adjudicates": [
      "NFRA_OPALAI-Z-W9-S5"
    ],
    "one_line": "RULES Z-W9-S5 (OA-g-3's channel selection). The order said 'channels whose verdict is not deny', but only artifact ROWS carry a verdict. The worker granted each channel with at least one indexed non-deny row: 10 of 15; the other 5 have no indexed rows. Four of the 10 also hold deny rows, which catalog_gate refuses row by row. Accepted as the issuer's intended reading.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "OA-g-3 worker report; drain @da3a2cafbe; g3.AC1/AC2 PASS on CLOUD (items=159 policy=10 active_profiles=1 portal_only_active=1 operations=[['query']])."
      ]
    },
    "spec_asserts": "OA-g-3 step 2: portal_channels = the catalog channels whose verdict is not deny.",
    "world_is": "Verdicts are per row; the grant names the 10 channels with any non-deny indexed row, and deny rows stay refused by the gate."
  },
  {
    "id": "NFRA_OPALAI-Z-S36",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~AI",
    "surfaced_at": "2026-09-28T20:50Z",
    "one_line": "First moto-enabled read of tests/test_data_entitlement_guard.py (row Z-W8-S1's UNREAD) at CLOUD HEAD, before any round-2 change: 2 failed, 10 passed. test_ogz1_ac05 raises KeyError 'unclassified' on the guard's report, and test_ogz1_ac08's pinned route-class set no longer equals the app's 35 routes. 'Keeps passing' was never true to begin with; it was unmeasured.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cd infra/aws/ec2/opal-gateway && PYTHONPATH=C:/tmp/moto-target;. python -m pytest tests/test_data_entitlement_guard.py -q -> '2 failed, 10 passed' (moto 5.2.3, installed under G-MOTO, record @f8d1103a38).",
        "tests/test_data_entitlement_guard.py:622 `assert report[\"unclassified\"] == [\"fresh_unclassified\"]` -> KeyError: 'unclassified'.",
        "tests/test_data_entitlement_guard.py:712 `assert len(routes) == len(ge.server.app.routes) and set(ROUTE_CLASS) == set(routes)` -> 35 == 35 but the sets differ (a route renamed or added since the pin)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Round-1 analysis R-5 / row Z-W8-S1: the entitlement guard suite keeps passing across gateway changes; E1 records its pass count.",
    "world_is": "At CLOUD HEAD the suite is already red on 2 of 12, from changes that predate round 2. So E1's R-5 criterion is graded as NO NEW FAILURE against this base (the same 2 named failures, at least 10 passed), never as all-pass. The two failures are the NFRA_OPLGTW OG-z-1 guard's own pins, and they stay open for their owner.",
    "notes": "Filed by the issuer at the cut. INERT: the served gateway does not run tests. The OA-e-1 order carries the base count."
  },
  {
    "id": "NFRA_OPALAI-Z-S37",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~AI",
    "surfaced_at": "2026-09-28T21:40Z",
    "one_line": "G-ACCT cannot run from opal_ai PROD: provision-account.ps1:101 passes New-LocalUser a -Description of 86 characters, the cmdlet's limit is 48, so the real (elevated) run refuses before any act. OA-t-2's dry run and refusal arms never reached New-LocalUser, so the defect shipped to PROD fd8ab8a57f unseen.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "0.0.0_AB_MSTR~Z report 20260928T213328Z (elevated run of HANDOFF_G-ACCT_ELEVATED_20260928.md step 2): exit 1, ParameterBindingValidationException 'The character length of the 86 argument is too long ... fewer than or equal to \"48\" characters'; Opal_Agent, the credential file and the state dir all absent after, so no rollback was needed.",
        "git -C opal_ai show fd8ab8a57f:opal/runtime/provision/provision-account.ps1 :97-101 -- New-LocalUser ... -Description 'Opal Teams-facing runtime agent account (provisioned by provision-account.ps1, OA-t-2)' (86 characters), read by this seat."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "disarm_owner": "2.0.0_SA_COO~AI",
    "spec_asserts": "Runbook Part A step 2 / G-ACCT handoff step 2: the real elevated run of provision-account.ps1 creates Opal_Agent and prints one OK line per act.",
    "world_is": "The real run refuses at act 1 on a parameter-length validation that no unelevated arm exercises. Andrew's switchover sitting (Parts A-B) is held until a fixed script reaches the checkout the run uses.",
    "notes": "Remedy routed to 1.0.0_SA_CTO~O as ONE ask: a direct-act addendum cell fixing the one Description literal (<=48 chars) in opal_ai, plus how the fix reaches C:\\opal_runtime\\opal_ai before the cutover G-PUSH window."
  },
  {
    "id": "NFRA_OPALAI-Z-S38",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~AI",
    "surfaced_at": "2026-09-28T22:10Z",
    "one_line": "This seat's R-3 re-confirm (@73e5968e67), the round-2 decomposition and three release/census orders named the served gateway as fe94911257 from a six-file md5 match. The host serves 6a98a0553a (OG-s-1), which descends from fe94911257 and differs from it only in deploy-to-ec2.sh, so an app-file md5 subset matches BOTH and names the ancestor.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "1.0.0_SA_CTO~O msg 26242 and 2.0.0_SA_COO~O @e992df46c4: the live .env carries SPRINT_VIEW_ALLOWED_EMAILS, which only 6a98a0553a's deploy template writes.",
        "git merge-base --is-ancestor fe94911257 6a98a0553a -> true; git diff --stat fe94911257 6a98a0553a -- infra/aws/ec2/opal-gateway -> 1 file, deploy-to-ec2.sh (read by this seat)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OA-r-1 / OA-e-3 / OA-e-9 step 0: the live base is resolved BY CONTENT as the commit whose files ALL match.",
    "world_is": "An app-file md5 set cannot separate a release from an ancestor whose app files are identical, so 'all match' names more than one commit. A release cut on the ancestor would ship the older .env template.",
    "notes": "Remedied by the issuer in the same act (amendment commit): the three orders gain a tie-break on the live .env KEY names against each candidate's deploy template, and the card and the re-confirm record are corrected in place. No release has run, so nothing shipped on the wrong base."
  },
  {
    "id": "NFRA_OPALAI-Z-S39",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~AI",
    "surfaced_at": "2026-09-28T22:25Z",
    "one_line": "An OWNER principal cannot hold any data grant without losing every legacy gateway tool, permanently: a profile makes the principal restricted to the Schwab tools its grant allows (a portal-only grant allows none), and a revoked record is a tombstone that never restores the legacy path. So Andrew cannot be profiled as an asker, and the widening of Alyssa to Menachem's entitlements is the only asker-side grant this round can write safely.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/app/data_entitlement.py docstring at HEAD: 'a profile (restricted): exactly the Schwab tools its active grant's operations allow; every other tool and the direct REST routes are denied'; 'a principal with ANY profile record -- pending, active or revoked -- is restricted. Nothing reactivates the legacy unlisted-user path'.",
        "data_entitlement.py decide() (~:368-372): access.restricted -> only tools in access.tools pass.",
        "1.0.0_SA_CTO~O msg 26243 asked for Andrew's portal-only grant; this seat measured the no-narrowing condition before writing, found it fails by construction with no possible rollback, and wrote nothing (msg 26252); the CTO ruled card option (b) instead (msg 26254)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Test card option (a) / CTO msg 26243: an owner can be given a portal-only asker grant without narrowing anything he holds today.",
    "world_is": "Any profile restricts, and restriction is permanent. An asker grant for an owner or operator seat would silently cost that seat its email, Teams, YCharts, upload and /query/v0 reach.",
    "notes": "Candidate enrichment item for round 2's L10 (CTO msg 26254): an asker-only grant shape (or an owner class) that scopes the ASKER path without restricting the principal's own tools, specified by the PRD owner. INERT: nothing was written, and no owner holds a profile. It binds any future grant written for a seat that also calls tools itself."
  },
{
  "id": "NFRA_OPALAI-Z-W13-S1",
  "project": "NFRA_OPALAI",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_OPALAI~13",
  "surfaced_at": "2026-09-28T12:00:00Z",
  "one_line": "Nested commit of SKILL.md refused by the owned-paths lane gate: the order's opal_ai/... path is not matched for the nested repo's commit",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "Order OA-e-4 bound 1: git -C opal_ai commit --author <serial> -F <msgfile> -- opal/agent/skills/bbg-teams-assist/SKILL.md lands, and <paths> lists opal_ai/opal/agent/skills/bbg-teams-assist/SKILL.md.",
  "world_is": "The commit was refused (owned-paths block mode): 'agent=0.9.0_WK_NFRA_OPALAI~13 not in permitted_agents -- WORKER: no NON-TERMINAL task order at HEAD issued_to this serial names this path in its <paths> block'. The order file exists at HEAD b17a43ca9a and names the path with the opal_ai/ prefix. The edit is in the nested working tree, uncommitted; AC1 (reads nested HEAD) FAILs 0/0/0, AC2 and AC3 PASS. No override used.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git -C opal_ai commit ... -> 'VIOLATION: opal_ai/opal/agent/skills/bbg-teams-assist/SKILL.md -- lane=ANY_EXEC_OR_AE ... not in permitted_agents'",
      "e4.AC1.sh at nested HEAD fd8ab8a57f: read_chat_message_images=0; hostedContents/pasted lines=0; decline sentence=0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
},
{
  "id": "NFRA_OPALAI-Z-W13-S2",
  "project": "NFRA_OPALAI",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_OPALAI~13",
  "surfaced_at": "2026-09-28T13:00:00Z",
  "one_line": "Fix fd0aa6ba57 is not live for the nested commit from worktree oa-13: the hook execs the worktree's own .tools",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "Issuer message: fd0aa6ba57 is live in the main tree the nested hook execs, so re-running the nested commit clears.",
  "world_is": "Re-run refused with the identical VIOLATION text. The nested pre-commit wrapper (.git/modules/opal_ai/hooks/pre-commit) runs ${_SUPER}/.tools/git-hooks/owned-paths-check.sh, and _SUPER is /c/tmp/oa-13, whose .tools predates the fix: git merge-base --is-ancestor fd0aa6ba57 HEAD -> 1; git diff HEAD fd0aa6ba57 -- .tools/owned-paths-validate.py shows 15 insertions, 2 deletions. .tools is outside my <paths>, so I cannot bring the fix in.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "nested commit rerun -> same owned-paths VIOLATION",
      "is-ancestor fd0aa6ba57 HEAD in /c/tmp/oa-13 -> rc=1"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
},
  {
    "id": "NFRA_OPALAI-Z-W10-S1",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~10",
    "surfaced_at": "2026-09-28T21:50Z",
    "one_line": "e1.AC1.sh cannot print PASS for the four named arms on this device, though all four pass. Its matcher greps '^PASSED tests/test_asker_binding.py::<name>', but pytest 9.1.1 prints the -rA line with a BACKSLASH ('PASSED tests\\test_asker_binding.py::<name>') when it is run from infra/aws/ec2/opal-gateway, because the rootdir is the workspace root (pytest.ini there) and the node id is shown relative to the invocation dir with the OS separator. The script reports 'named arms passed 0 of 4' and RESULT: FAIL.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e1.AC1.sh -> 'named arms passed 0 of 4; failed/errored tests 0; summary: 20 passed in 1.41s' / 'RESULT: FAIL' / exit=1, at the worker's branch wk-NFRA_OPALAI-10.",
        "cd infra/aws/ec2/opal-gateway && python -m pytest tests/test_asker_binding.py -rA -p no:cacheprovider --color=no -> 'rootdir: C:\\tmp\\oa-10' / 'configfile: pytest.ini' and 'PASSED tests\\test_asker_binding.py::test_old_message_from_wider_person_refused'.",
        "The same command with --rootdir=. prints 'PASSED tests/test_asker_binding.py::test_old_message_from_wider_person_refused' (forward slash). --rootdir is not in the script's invocation, so it was not used to meet the criterion.",
        "The four named tests PASSED in the -rA output: test_old_message_from_wider_person_refused, test_reply_to_other_chat_refused, test_group_chat_unprofiled_member_refused, test_same_chat_recent_message_served; tests/test_asker_scope.py 4 of 4 passed; 20 passed, 0 failed."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "e1.AC1.sh: each named arm appears as '^PASSED tests/test_asker_binding.py::<name>' in the pytest -rA output, so 'named arms passed 4 of 4' prints and the script exits 0.",
    "world_is": "On this Windows device pytest renders that line with 'tests\\'. The matcher can never see a forward slash, so AC1 reads 0 of 4 whatever the tests do. The same matcher shape in any other round-2 check that greps pytest -rA output from the gateway directory reads the same way. The worker did not edit the check, add a pytest.ini under the gateway directory, or pass --rootdir, and reports AC1 as a refusal with these measurements.",
    "notes": "Not ARMED: a check that cannot pass fails closed. The issuer's fix is one of: match '[/\\\\]' in the grep, or add --rootdir=. to the pytest line of the check."
  },
  {
    "id": "NFRA_OPALAI-Z-W10-S2",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~10",
    "surfaced_at": "2026-09-28T21:55Z",
    "one_line": "The OA-e-1 repair turns two existing tests in tests/test_portal_grant.py red: test_asker_portal_scope_admits_granted_channel and test_asker_portal_scope_refuses_other_channel. Their fake Graph message carries tenant 22222222-... (not the configured Opal TENANT_ID) and no createdDateTime, so handle_asker_query now refuses them asker_message_stale (and, once that is fixed, asker_tenant_denied). The file is outside this order's paths, so the worker did not edit it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cd infra/aws/ec2/opal-gateway && PYTHONPATH='C:/tmp/moto-target;.' python -m pytest tests/test_tool_classification_composition.py tests/test_identity_scope.py tests/test_portal_grant.py tests/test_teams_reader_fallback.py -q -> '2 failed, 26 passed'; the 2 failed are the two named tests; the other 26 pass.",
        "tests/test_portal_grant.py:39 _TID = '22222222-2222-2222-2222-222222222222' and :27 os.environ.setdefault('TENANT_ID', '11111111-...'); the fake _graph_call at :93 returns no createdDateTime. Assertion at :183: \"guard_denied\" not in result -> code asker_message_stale.",
        "The order's paths (section 3) name tests/test_asker_scope.py and tests/test_asker_binding.py only; tests/test_portal_grant.py is not among them."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Order OA-e-1 section 1: only tests/test_asker_scope.py must keep passing; tests/test_portal_grant.py is not named.",
    "world_is": "Both refusals are the specified behaviour (a message with no parseable createdDateTime is refused; a non-Opal tenant is refused). Those two tests pass a foreign tenant and an undated message on purpose or by omission. Fixing them takes a tenant equal to the configured TENANT_ID and a recent createdDateTime in that file's _graph_call, in a cell whose paths include it. OA-r-1 cherry-picks this change, so those two tests will be red on CLOUD after the drain until then.",
    "notes": "Not ARMED: the gateway does not run tests at serve time."
  },
  {
    "id": "NFRA_OPALAI-Z-W17-S1",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~17",
    "surfaced_at": "2026-09-28T21:10Z",
    "one_line": "The E11 fix does not reach an already-installed wrapper: install-owned-paths.sh returns 'already wired ... idempotent no-op' when the destination hook mentions owned-paths-check.sh, so the real opal_ai hooks dir keeps the old fail-open wrapper until it is removed and the installer re-run.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~AI",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/git-hooks/install-owned-paths.sh 'Already wired check' block: `grep -q owned-paths-check.sh $HOOK_DEST` then exit 0 without rewriting (unchanged by this order; bound 1 forbids widening).",
        "Read-only measure of the real ajb_workspace .git/modules/opal_ai/hooks/pre-commit: grep -c 'owned-paths-check.sh' = 3 (old wrapper wired) and grep -c 'worktree list' = 1 (the first-entry resolution E11 replaces). Nothing was written there."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO OA-e-11 bound 2: 'The issuer installs at the drain' -- the installed wrapper carries the new resolution afterwards.",
    "world_is": "A re-run of install-owned-paths.sh --submodule opal_ai at the drain is a no-op against the existing old wrapper, so a linked worktree of the real opal_ai outside every parent worktree still skips the lane check (exit 0). The wrapper file must be deleted (or replaced) first, then the installer run; the hook script owned-paths-check.sh itself is read live from the parent and takes the fix without reinstall.",
    "notes": "Fix is one issuer act at the drain: remove .git/modules/opal_ai/hooks/pre-commit, run the installer with --submodule opal_ai, confirm 'worktree list' no longer appears in it. Filed by the worker; not done here (bound 2)."
  },
  {
    "id": "NFRA_OPALAI-Z-W11-S1",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~11",
    "surfaced_at": "2026-09-28T21:45Z",
    "one_line": "The nested commit the order prescribes is refused by the owned-paths pre-commit hook for a path the order's own <paths> block names: the hook's worker-grant census runs git with the nested repo's GIT_DIR inherited, so it finds no task orders and admits nothing. The three OA-e-2 nested edits are made and UNCOMMITTED; the worker did not bypass the gate.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED: `git -C opal_ai commit --author '0.9.0_WK_NFRA_OPALAI~11 <...>' -F msg -- opal/agent/hooks/concierge-gate.sh opal/agent/hooks/test_concierge_gate.sh opal/agent/refs/RELAUNCH.md` -> ERROR owned-paths lane violation(s), 3 of 3 paths: 'agent=0.9.0_WK_NFRA_OPALAI~11 not in permitted_agents -- WORKER: no NON-TERMINAL task order at HEAD issued_to this serial names this path in its <paths> block'. The three paths are named verbatim, parent-relative (opal_ai/opal/agent/...), in TO-OA-e-2 section 3 <paths>, whose <status> is pending and <issued_to> is this serial.",
        "MEASURED, same input, two environments: `printf 'opal_ai/opal/agent/hooks/concierge-gate.sh' | python3 .tools/owned-paths-validate.py --check-agent 0.9.0_WK_NFRA_OPALAI~11 .owned-paths.yaml` from the parent worktree C:/tmp/oa-11 -> no VIOLATION line (rc 0); the same command with GIT_DIR set to the nested repo's absolute git dir -> 'VIOLATION: ... not in permitted_agents ... no NON-TERMINAL task order'. Git exports GIT_DIR/GIT_INDEX_FILE into a pre-commit hook.",
        "CODE .tools/owned-paths-validate.py _worker_orders (lines ~176-205) runs `git ls-files` and `git show HEAD:<path>` with cwd=root but the hook's environment, so GIT_DIR outranks cwd and the census reads the nested repo. .tools/git-hooks/owned-paths-check.sh defines `_git_x` (env -u GIT_DIR ...) for exactly this hazard and applies it to its own superproject probe, but the validator subprocess calls do not.",
        "The hook wrapper at the shared module's hooks/pre-commit (C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.git/modules/opal_ai/hooks/pre-commit) resolves the superproject to C:/tmp/oa-11 correctly; the prefix rebase to opal_ai/<path> is correct; only the census env is wrong."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OA-e-2 section 2.1: the worker commits its nested files with `git -C opal_ai commit --author ... -F <msgfile> -- <nested paths>`, and the order's <paths> is the write grant.",
    "world_is": "The gate refuses that commit for a granted path (validator census reads the wrong repo under a hook's GIT_DIR). The worker did not use --no-verify, GIT_COMMIT_AUTHOR_OVERRIDE or plumbing (order section 2.3: no route the face does not name). Edits sit in the worktree C:/tmp/oa-11/opal_ai (branch wk-NFRA_OPALAI-11-opal_ai, HEAD fd8ab8a57f, 3 modified files). e2.AC1 and e2.AC2 read the nested ref and cannot pass until a commit exists; e2.AC3 reads PASS only vacuously (0 files changed). Fix owner is the tooling lane: env -u GIT_DIR -u GIT_INDEX_FILE -u GIT_WORK_TREE on the census subprocesses in _worker_orders, or the issuer commits the three files after reading them.",
    "notes": "Nested-commit workers before this round were never graded by this hook (row Z-W5-S1: the hook was absent from the shared module), so this path had not been exercised by a worker. The COO decides whether to commit the three files or to fix the validator and re-issue."
  },
  {
    "id": "NFRA_OPALAI-Z-W11-S2",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~11",
    "surfaced_at": "2026-09-28T21:50Z",
    "one_line": "e2.AC1 bounds the fence's own test at 60 s (`timeout 60 bash $TT`), but test_concierge_gate.sh takes about 89 s on this device (28 cases, one jq process chain per case), so AC1 reads 'no summary' and FAILs even on a correct commit.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED: e2.AC1.sh at the pinned/unchanged HEAD printed \"fence test 'no summary'\" (the 60 s bound cut the test before its RESULT line). The same script text is `summ=$(timeout 60 bash \"$TT\" ...)`.",
        "MEASURED: `time (timeout 500 bash test_concierge_gate.sh | tail -5)` on the edited working tree -> 'RESULT: 28 passed, 0 failed (denominator: 28 cases)', real 1m28.708s. The new deny arm reads 'ok [DENY] -bbg opal_data_refresh_upload'. A first run under `timeout 60` was 'Terminated' before any RESULT line."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "e2.AC1 expects `fence test 'RESULT: N passed, 0 failed ...'` within its own bounds.",
    "world_is": "The fence test's runtime on this device exceeds the check's inner 60 s bound, so the criterion cannot be met as written regardless of the commit. The worker did not repair the criterion. The edited fence itself passes its whole test (28 of 28) and the three arms of AC1 were exercised by the test's own cases (upload DENY, -bbg whoami/poll PASS, send_email DENY) on the UNCOMMITTED working tree.",
    "notes": "Suggested for the issuer: raise the inner bound to 240 s (the outer 120 s harness bound also needs to admit it), or replace the full-suite call with the upload arm only."
  },
  {
    "id": "NFRA_OPALAI-Z-W11-S3",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~11",
    "surfaced_at": "2026-09-28T22:20Z",
    "one_line": "Rows Z-W11-S1 and Z-W11-S2 are cleared on this branch: with the issuer's validator fix and the amended AC1 bound, the nested commit landed through the hook with no override (opal_ai 7c6473c) and e2.AC1-AC3 all read RESULT: PASS. This row disarms nothing; the issuer dispositions S1 and S2.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED: `git -C opal_ai commit --author ... -F msg -- <3 paths>` -> '[wk-NFRA_OPALAI-11-opal_ai 7c6473c] ... 3 files changed, 11 insertions(+), 8 deletions(-)' on parent HEAD d750cba8c4 (carrying fix @fd0aa6ba57 and amendment @c7a5391c18 as cherry-picks).",
        "MEASURED: e2.AC1 'upload=DENY read_chat_messages=PASS send_email=DENY; fence test names upload=1; ... RESULT: 28 passed, 0 failed (denominator: 28 cases)' exit=0; e2.AC2 '/terminal-upload=0; upload lines=1, of which without never/not=0; publish_to_portal.py=1' exit=0; e2.AC3 'files changed=3, outside the cell's three=0; fence lines removed outside G4=0' exit=0."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Issuer message: S1 (validator census inherited the nested GIT_DIR) fixed @fd0aa6ba57; S2 (AC1 inner bound) raised 60 s -> 105 s at c7a5391c18.",
    "world_is": "Both hold on this branch: the hook admitted the nested commit and AC1 completed its fence test inside the new bound."
  },
  {
    "id": "NFRA_OPALAI-Z-W16-S1",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~16",
    "surfaced_at": "2026-09-28T22:05Z",
    "one_line": "E10's LOGIN_USES=0 is a count over 2026-07-14..2026-09-28, not since the /authorize go-live: the host journal starts 21 days after the commit that registered /authorize.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM i-07dccb1615503ac99 2026-09-28: journalctl -u opal-gateway first line 2026-08-15T03:02:10+0000; journalctl _COMM=uvicorn first line 2026-07-14T09:48:50+0000; /login count 0 on both.",
        "git log -S: 63e61ca77b 2026-06-23 (authored, UNAPPLIED); org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~16/E10_LOGIN_CENSUS.md."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OA-e-10 section 1: LOGIN_USES is the number of /login requests since the MCP /authorize sign-in went live, read from journalctl -u opal-gateway.",
    "world_is": "journalctl -u opal-gateway starts 2026-08-15 (the unit rename); the whole journal starts 2026-07-14T09:48:50Z under the earlier unit m365-mcp-gateway. /authorize was registered at 63e61ca77b (2026-06-23). The worker counted both unit names (0 and 0) and named the gap in the census; the 21 days before the journal are unmeasured and not recoverable on the host."
  },
  {
    "id": "NFRA_OPALAI-Z-W16-S2",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~16",
    "surfaced_at": "2026-09-28T22:05Z",
    "one_line": "E10 NARROW's 'a config list' is derived from the two existing settings OTP_MAILBOX and MS_INGEST_IDENTITY, because app/config.py is outside the order's paths.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/app/server.py _login_allowed_identities (worker commit on wk-NFRA_OPALAI-16).",
        "tests/test_login_retire.py::test_login_fails_closed_when_empty passed."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OA-e-10 section 1 NARROW: /login admits only the server identities the census named (a config list, fail closed when empty).",
    "world_is": "The order writes only app/server.py, so a new config key could not be added. The allow-list is computed in server.py from cfg.OTP_MAILBOX and cfg.MS_INGEST_IDENTITY (the two server-held identities the census named); empty -> admits nobody. A separate list key would need config.py and a host .env edit at release."
  },
  {
    "id": "NFRA_OPALAI-Z-W16-S3",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~16",
    "surfaced_at": "2026-09-28T22:05Z",
    "one_line": "The census's host read printed the first 4 characters of OTP_BEARER, MS_INGEST_BEARER and the two identity values into the worker's own tool output (never into a committed file).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM command output in the worker session 2026-09-28 ~21:55Z (ENV_KEYS block); grep of the committed census for the prefixes: absent."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OA-e-10 bound 3: no token, cache content, secret or email is printed, committed or put in the census.",
    "world_is": "The worker's SSM script derived the two cache file names from .env and, in an extra diagnostic line, echoed each key's first 4 value characters. Nothing was written to the repo, the census or this row. The prefixes sit in the worker's session output only; a 4-character prefix of a static bearer is not usable as a credential."
  },
  {
    "id": "NFRA_OPALAI-Z-W16-S4",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~16",
    "surfaced_at": "2026-09-28T22:20Z",
    "one_line": "e10.AC2.sh cannot pass on this Windows device: it greps pytest -rA lines for 'PASSED tests/test_login_retire.py::<name>' with a forward slash, but pytest here prints 'PASSED tests\test_login_retire.py::<name>' with a backslash. The tests pass; the named-test count reads 0.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e10.AC2.sh at HEAD 8ed37b3266 -> 'branch=NARROW named=test_login_narrowed passed=0 failed/errored=0; summary: 2 passed' RESULT: FAIL exit=1.",
        "python -m pytest tests/test_login_retire.py -rA (cat -A) -> 'PASSED tests\test_login_retire.py::test_login_narrowed$' and '...::test_login_fails_closed_when_empty$'; e10.AC2.sh grep pattern is ^PASSED tests/test_login_retire.py::$want( |$)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OA-e-10 AC2: the test named for the census's branch passed>=1, failed/errored=0, read from e10.AC2.sh.",
    "world_is": "With pytest printing OS-native path separators, the check's forward-slash pattern matches nothing on this device, so named=0 whatever the tests do (the same script would pass on a POSIX device). The worker did not edit the check or the invocation, and could not change the separator inside its <paths>. Disarm owner is the issuer: the pattern needs to accept either separator, e.g. tests[/\\]test_login_retire.py. The other two OA-e-10 criteria pass and the mutant control fired (guard removed -> both tests fail)."
  },
  {
    "id": "NFRA_OPALAI-Z-W15-S1",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~15",
    "surfaced_at": "2026-09-28T21:30Z",
    "one_line": "OA-e-7 (2): the 13 ruff 0.16.9 findings are in opal/agent/teams_watch/teams-watch.py, not portal_lookup.py; that file is outside the order's <paths>, so they cannot be fixed by this worker.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PATH=C:/tmp/ruff-0.16.9/bin:$PATH; ruff check --target-version py39 --output-format concise --color never opal -> 'Found 13 errors.' all in opal\u0007gent\teams_watch\teams-watch.py; same command on opal/agent/tools/portal_lookup.py -> 'All checks passed!' (opal_ai fd8ab8a)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Order section 1: all 13 findings (8 SIM115, 3 BLE001, 1 SIM102, 1 UP031) are in opal/agent/tools/portal_lookup.py.",
    "world_is": "portal_lookup.py is clean under ruff 0.16.9 ('All checks passed!'); the 13 findings (8 SIM115, 3 BLE001, 1 SIM102, 1 UP031) are in opal/agent/teams_watch/teams-watch.py (lines 228..790). AC2's clean run cannot read CHECKS: PASS until that file is fixed."
  },
  {
    "id": "NFRA_OPALAI-Z-W15-S2",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~15",
    "surfaced_at": "2026-09-28T21:30Z",
    "one_line": "Nested opal_ai commit refused by the lane gate: the order's opal_ai/** paths are not resolved as this serial's grant (owned-paths, lane ANY_EXEC_OR_AE).",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C opal_ai commit ... -> 'VIOLATION: opal_ai/.github/workflows/ci.yml -- lane=ANY_EXEC_OR_AE ... not in permitted_agents'; git -C opal_ai log -1 still fd8ab8a."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Order section 2.1: nested files commit with git -C opal_ai commit --author <serial> -F <msgfile>; <paths> lists opal_ai/.github/workflows/ci.yml and opal_ai/opal/checks/run_checks.sh.",
    "world_is": "Both the git -C opal_ai commit and safe-commit.sh from inside opal_ai refuse: 'agent=0.9.0_WK_NFRA_OPALAI~15 not in permitted_agents -- WORKER: no NON-TERMINAL task order at HEAD issued_to this serial names this path'. The edits to ci.yml and run_checks.sh sit uncommitted in C:/tmp/oa-15/opal_ai; AC2/AC3 read committed HEAD and so read FAIL. No override used."
  },
  {
    "id": "NFRA_OPALAI-Z-S40",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~AI",
    "surfaced_at": "2026-09-28T23:40Z",
    "one_line": "The D7 ticket-intake runner (Scheduled Task OPAL_D7_ticket_intake, every 5 min), which imports the operator teams-watch.py (cutover precondition CP-1), has not succeeded since 2026-09-03: 8712 exit-2 passes against 613 exit-0 in its log, and since 2026-09-18 every pass dies 'no mcpOAuth record matches the pin (--server=opal-gateway-bbg --identity=opalbloomberg)'. It predates round 2 and is unchanged by OA-e-7's comment-only header merge.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "%USERPROFILE%\\opal_ticket_intake\runner.log: last 'intake pass exit 0' at [Thu 09/03/2026 4:29:48]; first 'no-token-for-identity' after [Fri 09/18/2026 1:59:46]; counts exit 2 = 8712, exit 0 = 613 (grep -c, read by this seat 2026-09-28 ~23:4xZ).",
        "Get-ScheduledTaskInfo OPAL_D7_ticket_intake: LastTaskResult=2 at 23:29:46Z (before the OA-e-7 merge) and 23:34:46Z (after the merge b3b3d3bc39); py_compile and a by-path import of the merged teams-watch.py both OK.",
        "OA-e-5 (@79da942995) read 4 of 4 Teams reads OK through the same watch with the --server pin alone, so the store holds the opal-gateway-bbg record; the runner's extra --identity=opalbloomberg pin is what finds no match."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Ruling I-3 / CP-1: the parent teams-watch.py STAYS as the operator plane's tool, and the D7 intake runner keeps running on it through the cutover.",
    "world_is": "The runner has not delivered a pass in 25 days, and the dark D7 lane (OPAL_TICKET_VNEXT, no COO lane since 2026-09-11) has no reader of its LastTaskResult. CP-1's 'read the next scheduled fire back' will read a failure that is not the cutover's.",
    "notes": "Owner: OPAL_TICKET_VNEXT (no live COO lane). Routed as an observation through the round-2 drain message to 1.0.0_SA_CTO~O; not repaired here (outside this project's write surface). The likely cause is the --identity pin not matching how the store names the Opal Bloomberg record; not verified."
  },
  {
    "id": "NFRA_OPALAI-Z-S41",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~AI",
    "surfaced_at": "2026-09-28T23:50Z",
    "one_line": "The four files pA/pB/pC.txt and probe_whoami.txt found in C:\\opal_runtime\\state (owner Opal_Agent, 22:30-22:32Z) were written by THIS seat, 2.0.0_SA_COO~AI, not by a worker: diagnostic probes of Start-Process -Credential as Opal_Agent with the stored DPAPI credential, run while investigating G-ACCT step 3 (the WinRM stop), under no task order. Each ran `whoami` and wrote 'opal_bloomberg\\opal_agent'. Cleared before the re-run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "This seat's session: three PowerShell probes at ~22:30-22:33Z, Import-Clixml of %USERPROFILE%\\.opal_runtime\\opal_agent_cred.xml, then Start-Process cmd.exe /c whoami > C:\\opal_runtime\\state\\<file> -Credential; the tool reported 'Access is denied' each time, yet the files were written.",
        "0.0.0_AB_MSTR~Z report 20260928T233948Z and 1.0.0_SA_CTO~O msg 26294 found the files (owner Opal_Agent, 27 bytes each); removed by this seat ~23:5xZ (os.remove, 4 of 4; the dir is now empty)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "G-ACCT handoff: Opal_Agent sessions are started only by the elevated executor (0.0.0_AB_MSTR~Z) under the handoff, and the state dir holds only the runtime's own state.",
    "world_is": "The issuer used the stored Opal_Agent credential directly for diagnosis, outside any order, and left four files in the runtime's state dir. The probes also measured two facts: (1) Opal_Agent's logon WORKS (whoami ran as it); (2) from this unelevated session, Start-Process -Credential -Wait/-PassThru throws 'Access is denied' AFTER the child starts, so an unelevated operator running launcher.ps1 may see that throw on its -Wait gate launch.",
    "notes": "Named honestly for the CTO's ask (msg 26294), which guessed the OA-f-4 worker. Fact (2) is a candidate risk on the step-6 launcher path; step 6 is run elevated by 0.0.0_AB_MSTR~Z, where it did not occur. No further direct credential use by this seat."
  },
  {
    "id": "NFRA_OPALAI-Z-W10-S3",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~10",
    "surfaced_at": "2026-09-28T23:20Z",
    "one_line": "OA-r-1 step 0's tie-break ('keep candidates whose .env template writes the live key set; if more than one survives, the base is the newest') picks the WRONG base here. Two candidates survive the four-file md5 and the .env key-set test: 6a98a0553a and rel-nfra-mcpindex-r3-gateway (2dedae93df, a descendant of 6a98a0553a). Their four named files and their 27-key .env sets are identical; they differ in 3 other files and in the VALUE of ENABLED_INTEGRATIONS. The live host's other files match 6a98a0553a and do not match 2dedae93df.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM (i-07dccb1615503ac99, status Success, 2026-09-28 ~23:1xZ) md5 of /opt/opal-gateway/app/{asker_scope,tools,identity_scope,data_entitlement}.py = f21b86141a7145fb70b5f77d37774d85, 6c888e51a3c652dfe89c74654fde39e3, 442c9755d14aa1ffbbccf5bf0fe73656, 964504343c24d412a266da74e7108e69. These four equal 6a98a0553a, fe94911257, rel-nfra-oplgtw-sprint-owner (6a98a0553a) and rel-nfra-mcpindex-r3-gateway (2dedae93df); 12 rel-* refs (local and origin) and 2 pinned commits were compared.",
        "Live .env key names (27, values never read) equal the deploy-to-ec2.sh line-197 key set at 6a98a0553a, 2dedae93df and rel-nfra-oplgtw-sprint-owner; fe94911257 and rel-nfra-oplgtw-email-deny write 26 (no SPRINT_VIEW_ALLOWED_EMAILS) and are excluded. Read with .scratch/keys.py against git show <c>:infra/aws/ec2/opal-gateway/deploy-to-ec2.sh.",
        "git diff --stat 6a98a0553a rel-nfra-mcpindex-r3-gateway -- infra/aws/ec2/opal-gateway: 5 files, app/integrations/opal_discover/integration.py, app/integrations/portal_index/integration.py, app/refs/DATA_CATALOG.yaml, deploy-to-ec2.sh (ENABLED_INTEGRATIONS value only), tests/test_opal_discover.py.",
        "SSM md5 of the three app files that differ: live 9f80030ee9085a3e17d9944aead2f4c8 (opal_discover/integration.py), 41c6b834fd60a7c4996012e63fd482b5 (portal_index/integration.py), a19baa4c4600614bfa49ad7df950d87d (DATA_CATALOG.yaml) = all three at 6a98a0553a; at 2dedae93df they are 33d6b06075f92fb97bdc3af1894cef06, a4c28bef2a6d18c97a3a13e9c2571d87, bfffd6254d290303023687c5cdc0c9ad.",
        "infra/aws/ec2/EC2_MANIFEST.json at 90cbe69b07: services.opal-gateway.deployed_commit 6a98a0553a0a01c7e1acc6aea2b2ce5b82fc0f9b, deployed_at 2026-09-27T22:17:33Z."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OA-r-1 step 0 (AMENDED, row Z-S38): among candidates whose app files and .env key set match the host, 'the base is the newest, and you name every survivor'.",
    "world_is": "Applying 'newest' literally gives 2dedae93df, a release the host is not running (three of its files are not on the host). Building the release on it would ship the MX-r-4 opal_discover/portal_index changes and an ENABLED_INTEGRATIONS value change beside OA-e-1. The worker resolved the base as 6a98a0553a on the content of three further files, an addition to the four the order names, and reports both survivors. The order's tie-break should say to break a tie of survivors by the files in which they differ.",
    "notes": "Not ARMED for this order once the base is 6a98a0553a. The same tie-break in another cell's release order would pick the newest survivor whether or not the host runs it."
  },
  {
    "id": "NFRA_OPALAI-Z-W10-S4",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~10",
    "surfaced_at": "2026-09-28T23:40Z",
    "one_line": "OA-r-1 step 2 STOPPED before any deploy: the release tree's pytest run (the order's four-file list) reads 2 failed, 34 passed, and the order says 'Any failure: STOP, no deploy'. Both failures are in tests/test_portal_grant.py's OPERATOR half (test_admin_accepts_portal_only_candidate: KeyError 'portal_grant'; test_admin_rejects_unknown_portal_channel: message 'scope.portal_channels is not admitted by this contract (no portal_grant)'). They fail identically at the pure base 6a98a0553a: the tests read org/standards/NFRA_OPLGTW_CONTRACT.json, which the release tree does not carry at v1.2 (base has 0 'portal_grant', CLOUD has 1). The four named arms PASSED.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Release tree /c/tmp/oa-10-rel, branch rel-nfra-opalai-r2-asker-binding-gateway, HEAD d287ffb346 (base 6a98a0553a + 2254910889 + a2c96703b1 as one commit, GIT_COMMIT_AUTHOR_OVERRIDE used once). Census: git diff --name-only 6a98a0553a HEAD = the 5 expected gateway files, no other.",
        "cd /c/tmp/oa-10-rel/infra/aws/ec2/opal-gateway && python -m pytest tests/test_asker_binding.py tests/test_asker_scope.py tests/test_portal_grant.py tests/test_identity_scope.py -rA -q -> '2 failed, 34 passed'; transcript at org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~10/OA-r-1_NEGATIVE_ARMS.txt; the four named arms PASSED.",
        "Control at the pure base: git archive 6a98a0553a infra/aws/ec2/opal-gateway org/standards extracted to /c/tmp/oa-10-basechk; tests/test_portal_grant.py there (the base's own file, the base's own app) -> '2 failed, 5 passed': the same two admin tests.",
        "git show 6a98a0553a:org/standards/NFRA_OPLGTW_CONTRACT.json | grep -c portal_grant = 0; the same at CLOUD 90cbe69b07 = 1."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OA-r-1 step 2: the four-file pytest list runs in the release tree and any failure stops the deploy; the order expects the list to pass there.",
    "world_is": "tests/test_portal_grant.py holds an operator half (ops/schwab_entitlement_admin.py) whose two tests read the contract file outside infra/aws/ec2/opal-gateway. The release tree is the base plus five gateway files, so it carries the base's contract (no portal_grant). Those two tests fail there before and after OA-e-1, and neither touches asker_scope.py or tools.py. The worker did not deploy, opened no ledger entry, and touched nothing on the instance beyond the read-only SSM of step 0. Options for the issuer: amend step 2's list to deselect those two tests (with the reason), or supply the v1.2 contract to the census. The worker will not choose.",
    "notes": "Not ARMED: nothing is deployed. The release worktree /c/tmp/oa-10-rel and branch rel-nfra-opalai-r2-asker-binding-gateway (d287ffb346) exist and are unpushed. Scratch /c/tmp/oa-10-basechk holds the base control and can be removed."
  },
  {
    "id": "NFRA_OPALAI-Z-W10-S5",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~10",
    "surfaced_at": "2026-09-28T23:55Z",
    "one_line": "OA-r-1 cannot start its act: safe-ec2-deploy.sh's halt gate refuses this worker from the release tree with exit 3 (SERIAL RESOLVES TO NO KNOWN AGENT). The gate admits a 0.9.0_WK_<CODE>~<n> worker only while a non-terminal task order under <CODE> is issued_to it AT HEAD OF THE CALLING WORKTREE (halt-gate-check.sh:166-185, git ls-files + git show HEAD:p). The release tree is HEAD 6a98a0553a + d287ffb346 and holds 0 task orders under NFRA_OPALAI (33 under NFRA_OPLGTW); the slot branch holds 31. The wrapper pins HALT_GATE_REPO_ROOT to the calling toplevel, so the release tree cannot be told otherwise.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cd /c/tmp/oa-10-rel && ( . .tools/halt-gate-check.sh; halt_gate_check oa-r-1-preview ) -> 'HALT-GATE: SERIAL RESOLVES TO NO KNOWN AGENT -- BLOCKED (fail-closed)', 'Resolved serial: 0.9.0_WK_NFRA_OPALAI~10', gate rc=3. Before the serial file existed in the release tree the session file resolved to the parent COO's serial 2.0.0_SA_COO~AI, also rc=3.",
        "git -C /c/tmp/oa-10-rel ls-files -- 'org/missions/D*/*/NFRA_OPALAI/task-orders/*.md' | wc -l = 0; the same in /c/tmp/oa-10 = 31.",
        ".tools/halt-gate-check.sh:185 reads git -C $HALT_GATE_REPO_ROOT ls-files; infra/aws/ec2/safe-ec2-deploy.sh assigns HALT_GATE_REPO_ROOT=$(git rev-parse --show-toplevel) of its own checkout unconditionally, so an env override does not survive.",
        "Prior OPALAI releases passed because their release bases already held NFRA_OPALAI orders; the OPLGTW OG-s-1 base 6a98a0553a holds none.",
        "I created org/mcp/sessions/<session>.serial (gitignored, my own serial) inside /c/tmp/oa-10-rel to test the gate; it changes no tracked file."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OA-r-1 step 5: ACT from the release worktree with its scripts, halt gate pre-acknowledged with HALT_ACK=1 when it reads 0 STOP.",
    "world_is": "HALT_ACK covers a routine unread inbox (exit 1), not an unadmitted serial (exit 3), and HALT_OVERRIDE covers a STOP (exit 2). Nothing in the wrapper admits a worker whose release tree predates its orders. Routes that would pass, none taken: (a) commit the OA-r-1 task order into the release branch (breaks the five-file census), (b) run the wrapper from /c/tmp/oa-10 (a HEAD deploy, forbidden), (c) edit .tools/halt-gate-check.sh or the wrapper (read-only for this order). The issuer decides which, or provides another.",
    "notes": "Not ARMED: nothing is deployed and no ledger entry is open. Done before the stop, all proven: step 2 (release d287ffb346, census 5 of 5, 34 passed 2 deselected, transcript saved); step 3 (rollback artifact opal-gateway-6a98a0553a.tar.gz 398873 bytes from /c/tmp/oa-10-rb, 79 of 79 files identical to the live host, not uploaded); step 4(i) the .env render, 27 keys, all 9 markers on their own keys, no misalignment."
  },
  {
    "id": "NFRA_OPALAI-Z-W10-S6",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~10",
    "surfaced_at": "2026-09-29T00:10Z",
    "one_line": "Amendment 4's route (a) cannot be executed as ruled: safe-commit's TO issuance gate (.tools/to-pipeline-gate.py) REFUSES the record-only commit of the OA-r-1 task order on the release branch, 3 violations, and GIT_COMMIT_AUTHOR_OVERRIDE does not cover it. The commit aborted, files unstaged; HEAD of both trees is unchanged.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cd /c/tmp/oa-10-rel && GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_OPALAI~10 bash .tools/safe-commit.sh --author ... -F msg -- org/missions/D6/NFRA/NFRA_OPALAI/task-orders/NFRA_OPALAI.TO-OA-r-1.asker-binding-release.md -> 'ERROR: BLOCKED -- pipeline layer 2 (TO issuance gate). Commit aborted; files unstaged.' The file was byte-identical to CLOUD 2751f0be77 (md5 0b42025c6aae273930a119345cd51b79). The rollback tree was not attempted: it carries the same gate.",
        "Violation 1: 'a NEW tree task order committed under 0.9.0_WK_NFRA_OPALAI~10. COO is the only agent that does task orders (LD-0521 A3): a new file under org/missions/*/*/*/task-orders/ commits only under 2.0.0_SA_COO or a ~lane of it.'",
        "Violation 2: 'NO project row at org/missions/D6/NFRA/NFRA_OPALAI/project.json' (the release tree predates the project; project.json is absent).",
        "Violation 3: 'this commit adds NEW tree task order(s) but project.json reads dep_stage=None after it' (dep_stage EXECUTING must ride the issuance commit).",
        "The gate's own remedy is a '# pipeline-override: <reason>' line INSIDE the task order (.tools/to-pipeline-gate.py:63, audited to org/to-pipeline-override-audit.log), which would make the file differ from CLOUD's copy; the ruling requires byte identity.",
        "Both trees restored: rel HEAD d287ffb346 gateway tree e6cd9d235cd8a996f4e91b9813282172135a9bd1; rb HEAD 6a98a0553a gateway tree cd33c1e8d69f4e70ee03611f443d5c118f1825cf; no tracked change; my two file copies removed."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Issuer amendment 4: the halt gate admits the worker once the OA-r-1 task order, byte-identical to CLOUD, is committed as one record-only commit under the audited author override.",
    "world_is": "The override that safe-commit honours for a lane refusal does not reach the TO issuance gate, which refuses a worker adding a task order, an unregistered project and a missing dep_stage. Passing it needs one of: a '# pipeline-override:' line in the file (not byte-identical, and an audit-log write in the release tree), project.json plus dep_stage=EXECUTING beside it (more files in the release branch), or a committer that is 2.0.0_SA_COO or a ~lane of it (the issuer commits it). The worker took none of them: each changes the ruled bytes or the ruled identity. Also unresolved: the halt gate reads only ls-files + HEAD of the calling worktree, so any admitted route still needs the file in HEAD of both trees.",
    "notes": "Not ARMED: nothing is deployed, no ledger entry open. Everything before the act is proven and waiting: release d287ffb346, transcript, rollback 79 of 79, .env render."
  },
  {
      "id": "NFRA_OPALAI-Z-W22-S1",
      "project": "NFRA_OPALAI",
      "fabric": "site-z",
      "surfaced_by": "0.9.0_WK_NFRA_OPALAI~22",
      "surfaced_at": "2026-09-29T01:23Z",
      "one_line": "A store-borne `portal_channels: []` never reaches handle_asker_query's new branch: the real grant parser rejects an empty list as Malformed, so it is refused asker_store_unavailable, not asker_no_portal_channels.",
      "class": "OBSERVATION",
      "hazard_standing": "INERT",
      "grounding": {
          "status": "GROUNDED",
          "evidence": [
              "infra/aws/ec2/opal-gateway/app/data_entitlement.py:204-206 _strings(): raises Malformed 'must be a non-empty list of strings' for an empty list; :243-244 calls it whenever the key is present.",
              "Measured in worktree wk-NFRA_OPALAI-22: with a fake store carrying portal_channels [] the handler returned code asker_store_unavailable, guard_denied True, no data, no fetch (first run of tests/test_asker_nochannels.py, before the empty-arm was rewritten).",
              "Only an ABSENT key parses to an empty frozenset, and that path is refused asker_no_portal_channels (test_grant_without_portal_channels_denied PASSED)."
          ]
      },
      "disposition": "UNDER_INVESTIGATION",
      "spec_asserts": "OA-f-7 cell: an active profile whose grant has `portal_channels: []` is refused `asker_no_portal_channels`, and no fetch runs (tests built with fakes like test_asker_binding.py's fake store).",
      "world_is": "Through the real store and parser, `portal_channels: []` is refused earlier with asker_store_unavailable (still fail closed, nothing fetched), because data_entitlement.py (outside this order's paths, bound 1) rejects the empty list. The empty-set branch is reachable only when the key is absent. test_grant_with_empty_portal_channels_denied therefore asserts the store-borne [] is refused (code asker_store_unavailable or asker_no_portal_channels, no fetch) and reaches the handler's empty-set branch with a fake access layer (de.current_access wrapped to return the parsed grant with an empty portal_channels set). If the issuer wants the literal code for [], that is a data_entitlement.py change, not this order's.",
      "notes": "Not ARMED: both shapes fail closed with nothing fetched."
  },
  {
    "id": "NFRA_OPALAI-Z-S42",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~AI",
    "surfaced_at": "2026-09-29T03:40Z",
    "one_line": "Each opal-gateway release restart produces a short burst of per-identity 429s as every MCP client reconnects at once: 11 x 429 on /mcp in the minute of OA-e-3's restart (03:25Z) and 3 in MX-r-4's (02:45Z), 14 in 24h, none since. One client (0.0.0_AB_MSTR~Z's opalgateway) dropped with {\"error\":\"rate_limited\",\"scope\":\"identity\"}.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM on i-07dccb1615503ac99, journalctl -u opal-gateway -o short-iso since 2026-09-29 00:00Z, ' 429 ' bucketed per minute: 3 @02:45, 11 @03:25; since 2026-09-28 03:00Z: 14 total. ActiveEnterTimestamp 03:25:06Z (OA-e-3's restart).",
        "0.0.0_AB_MSTR~Z message 20260929T033653Z (the client-side drop); this seat's opalgateway whoami answered normally at ~03:38Z (the burst cleared)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OA-r-1 / OA-e-3 release guards: /health 200 and the tool list unchanged mean the release is clean for colleagues.",
    "world_is": "Both guards passed, but the restart itself trips the per-identity rate limiter for clients that reconnect in the same minute, and a client can drop and need a manual reconnect. No release guard reads it. It is a property of every opal-gateway restart, not of either release's code.",
    "notes": "INERT: transient, cleared within the minute, and no data or grant was affected. A candidate for the gateway owner (the limiter, or a reconnect grace after restart) and for the release guards (count 429s in the restart minute). Not repaired here."
  },
  {
    "id": "NFRA_OPALAI-Z-S43",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~AI",
    "surfaced_at": "2026-09-29T03:50Z",
    "one_line": "The OA-e-3 drain merge (safe-merge, d45ab2cf53) committed infra/aws/ec2/EC2_MANIFEST.json at the OLD value (0bce8d322a) although the merge's three sides were base 0bce / CLOUD 0bce / branch f791522306, and left the correct merged content as an UNSTAGED working-tree modification in the shared tree. The file is lane SHARED_CLOUD_OPS; the COO's own direct commit of it was refused by that lane, and it landed only under the audited override (9353136df3).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log -1 --format=%p d45ab2cf53 -> 4dd214bfc1 82b68d5ce2; merge-base 3158a81810; opal-gateway.deployed_commit at 3158a81810 = 0bce8d322a, at d45ab2cf53^1 = 0bce8d322a, at 82b68d5ce2 = f791522306, at d45ab2cf53 = 0bce8d322a.",
        "Right after the drain, git status: ' M infra/aws/ec2/EC2_MANIFEST.json', with the working-tree block = f791522306 (prev 0bce8d322a), 5 lines vs HEAD.",
        "/c/tmp/merge10e.log: 'missions-tree-check -- 4 tree/register path(s) staged'; no line names the manifest. safe-commit of the file as 2.0.0_SA_COO~AI: 'VIOLATION: infra/aws/ec2/EC2_MANIFEST.json -- lane=SHARED_CLOUD_OPS'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "/dispatch Step 5 + safe-merge.sh: the drain merge lands the worker's branch as merged, graded on the merged index, or refuses loud.",
    "world_is": "A lane-owned path the branch changed was dropped from the merge commit without a refusal. The correct content sat uncommitted in the shared tree, where another seat's commit or checkout could have lost it, and CLOUD's manifest named a release the host no longer served. The mechanism (index manipulation by safe-merge or a hook, versus a concurrent seat) is NOT measured here.",
    "notes": "Repaired by this seat at 9353136df3 (the worker's own record carried under the audited SHARED_CLOUD_OPS override; no new content). For the safe-merge owner: a drain should fail loud when a path the branch changed is absent from the merge commit. OA-r-1's drain (9f520b8bb3) carried its manifest change correctly, so this is intermittent or state-dependent."
  },
  {
    "id": "NFRA_OPALAI-Z-S44",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~AI",
    "surfaced_at": "2026-09-29T05:40Z",
    "one_line": "safe-merge.sh reported '*** CONFLICT -- THE MERGE IS OPEN AND NOTHING HAS LANDED ***' (1 conflicted path, --continue/--abort advice) when the merge never started: git failed to create .git/index.lock (another process held it), 'fatal: stash failed', and no MERGE_HEAD existed afterwards.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "/c/tmp/e9drain.log (OA-e-9 drain of wk-NFRA_OPALAI-10): 'error: Unable to create .../.git/index.lock: File exists' ... 'fatal: stash failed' ... 'safe-merge: *** CONFLICT -- THE MERGE IS OPEN AND NOTHING HAS LANDED. *** 1 conflicted path(s):' with no path listed.",
        "Immediately after: test -f .git/MERGE_HEAD -> absent; git diff --name-only --diff-filter=U -> empty; 72870fc8d6 not an ancestor of HEAD."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "safe-merge.sh: a CONFLICT verdict means an open merge the caller must resolve with --continue or --abort.",
    "world_is": "A lock race is reported as a CONFLICT. A caller following the advice would run --continue or --abort against a merge that does not exist, which in a shared tree acts on whichever peer's MERGE_HEAD is present at that moment.",
    "notes": "For the safe-merge owner: distinguish a failed git invocation (lock, stash failure) from an open merge by testing MERGE_HEAD before printing CONFLICT. This seat retried after the lock cleared."
  },
  {
    "id": "NFRA_OPALAI-Z-W10-S7",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPALAI~10",
    "surfaced_at": "2026-09-29T05:10Z",
    "one_line": "OA-e-9's population command, git rev-list --no-merges BASE..HEAD -- infra/aws/ec2/opal-gateway, counts 51 commits, but the same range with --full-history counts 53: git's default history simplification drops two gateway commits that CLOUD holds. Both are this worker's OA-e-3 commits (c06a3a4379, 685fabc691), which are on the host through the release branch's cherry-picks. The census DENOMINATOR is 51 because AC2 fixes the command; the two are listed under the table, not as rows.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git rev-list --no-merges f791522306..60fb85b5dd -- infra/aws/ec2/opal-gateway | wc -l = 51; the same with --full-history = 53; comm -13 of the two sorted lists = 685fabc691 and c06a3a4379 (both 0.9.0_WK_NFRA_OPALAI~10, OA-e-3 part A).",
        "git merge-base --is-ancestor c06a3a4379 HEAD and 685fabc691 HEAD both true (they are on CLOUD). The cause is git's default history simplification (a merge treated as TREESAME to one parent for the path); which merge did it was not traced.",
        "org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e9.AC2.sh recounts with the default command, so it agrees with 51."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OA-e-9 step 3: the population is git rev-list --no-merges <BASE>..<HEAD> -- infra/aws/ec2/opal-gateway; its count is the DENOMINATOR.",
    "world_is": "The default command undercounts CLOUD's gateway commits here (by the simplification named above). It hid two commits here, both released. A later census that reads the same command can hide an UNRELEASED commit the same way. The worker followed the face and reported the two separately.",
    "notes": "Not ARMED for this order. The E9 move should cut its population with --full-history, or from the tree diff BASE..HEAD, so a hidden commit cannot go unmoved."
  },
  {
    "id": "NFRA_OPALAI-Z-S45",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~O",
    "surfaced_at": "2026-09-29T18:45Z",
    "one_line": "Two 2.0.0_SA_COO~AI drain merges kept CLOUD's side for every file their worker branch changed: d45ab2cf53 (OA-e-3, 9 of 9 files) and 33076ebc84 (OA-f-3, 3 of 3). Ten files are still missing from CLOUD: OA-e-3's identity_scope.py seed row for opal_asker_query, its two test files, the TO flip to complete, the proof, ANNOUNCE, the release-tree tests and the deploy completion record, plus OA-f-3's proof and session_log. This traces the merge that W10-S7 left untraced.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~AI",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "For each file the branch changed (git diff --name-only $(git merge-base M^1 M^2) M^2), the merge blob equals the M^1 blob and differs from the M^2 blob, while M^1 never touched the file: 9 of 9 for d45ab2cf53, 3 of 3 for 33076ebc84.",
        "At CLOUD HEAD (after 680afc11fd), existence-aware check: 8 OA-e-3 files and 2 OA-f-3 files still hold the merge-result state (4 modified files at the old blob, 6 added files ABSENT). EC2_MANIFEST.json moved on legitimately (deployed_commit 093fc247c6); the OA-f-3 TO flip was restored later.",
        "Scan of 167 first-parent CLOUD merges since 2026-09-26: 5 merges carry such drops (d45ab2cf53, 33076ebc84; 0e98284fa2 and 8e0a9b6400 by 2.0.0_SA_COO~D, since restored; 789d4bb967 by 2.0.0_SA_COO~MI, since superseded).",
        "The shared tree holds all 10 files at exactly the branch-parent blobs (git hash-object == git rev-parse <M^2>:<path>, 10 of 10). Their mtimes equal the drain times (18:56:09 and 01:42:34 ET), consistent with S44 (safe-merge ran while index.lock was held and the stash failed).",
        "On the CLOUD tree with the files restored: pytest tests/test_asker_scope.py tests/test_identity_scope.py = 14 passed."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A drain merges the worker's branch into CLOUD, so every file the order's worker changed reaches CLOUD (spine L7 drain; .tools/safe-merge.sh).",
    "world_is": "Both drains produced a merge commit whose tree is CLOUD's side for every branch file. Git then counts the worker commits as merged, so no later merge of the branch can carry them. On CLOUD, OA-e-3 reads <status>pending</status> and the Analyst seed lacks opal_asker_query, while the live gateway (093fc247c6) serves it. A gateway release cut from CLOUD's tree would remove the tool silently, and the round's close reads OA-e-3 as open.",
    "notes": "Disarm: re-land the 10 files through a drain (a branch off CLOUD that cherry-picks the worker's original commits, which keeps their authorship, merged with .tools/safe-merge.sh), not EC2_MANIFEST.json. The lane gate refused a direct 1.0.0_SA_CTO~O commit (infra/aws is CLOUD_OPS_OR_ETL; deliverables/<serial>/ admits only that serial). The safe-merge defect that makes the tree equal CLOUD's side is for the safe-merge owner, beside S44."
  }
]
```
