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
  }
]
```
