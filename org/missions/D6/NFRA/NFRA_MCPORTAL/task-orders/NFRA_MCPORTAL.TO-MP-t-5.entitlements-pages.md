# NFRA_MCPORTAL task order -- `MP-t-5` -- HOP 4 (pages): the Entitlements tab and Recent Changes

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-t-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: `bun install` inside the nested repo only, if dependencies moved. No other network.
</preflight>

## 1. THE CELL -- `MP-t-5` (round 1, decomposition s.2/s.3)

In the nested `mcportal` repo (your previous order built its shell and sidebar), build the first real pages of Andrew's
dashboard. FWD-1 is: Andrew narrows one colleague's data grant, their next question obeys it, widening works the same
way, and both changes show with before and after.
1. **`src/api/admin.ts`**: a typed client for EXACTLY these routes, same-origin, cookies included (the ALB session):
   `GET /api/admin/grants/{tid}/{oid}`, `POST /api/admin/grants/{tid}/{oid}/narrow`,
   `POST /api/admin/grants/{tid}/{oid}/widen`, `GET /api/admin/changes`. No other `/api/` route. The request and
   response shapes follow the grant store's `data_entitlement` scope (`masters`, `datasets`, `accounts`, `dates`,
   `columns`, `operations`, as documented at `infra/aws/ec2/opal-gateway/app/data_entitlement.py:1-45`), and the
   writer's answer `{"verdict": "WRITTEN"|"REFUSED", "reason"}`.
2. **`src/pages/mcp-server/entitlements/`**, under the sidebar's MCP Server entry:
   - pick a person by tenant + object id;
   - show their current data grant by dimension;
   - a narrow/widen form that submits the scope change;
   - the writer's verdict shown plainly, a REFUSED reason included. No optimistic UI: the page re-reads after a write.
3. **`src/pages/recent-changes/`**: the changes newest first, each with who, when, what, before and after.
4. Tests with `bun test` (a mocked `fetch`, no server), naming exactly:
   - `entitlements shows the person's data grant`;
   - `narrow posts the scope change to the narrow route`;
   - `recent changes lists newest first with before and after`.
5. `portal/DESIGN.md`'s law binds the markup.
The route entries that put the two pages into the shell's router file are HOOKUPS: name them in your report; the
issuer adds them.

## 2. BOUNDS

1. **Nested repo:** your worktree carries `mcportal` as a nested worktree at `<worktree>/mcportal`, on branch
   `<your worktree branch>-mcportal`, off the shell's branch. It has no hooks. Commit with `git -C mcportal commit
   --author "0.9.0_WK_NFRA_MCPORTAL~1 <0.9.0_WK_NFRA_MCPORTAL~1@opal.agent>" -F <msgfile> -- <paths>`, where the msgfile
   is written with the Write tool.
2. No server is started. Standing: no push, no vendor call, no AWS. REFUSE a criterion you cannot meet as written, and
   report the refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does
   not name.

## 3. SURFACES

<paths>
mcportal/src/api/admin.ts
mcportal/src/pages/mcp-server/entitlements/
mcportal/src/pages/recent-changes/
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read (never write): `portal/DESIGN.md`, `infra/aws/ec2/opal-gateway/app/data_entitlement.py`, the shell under `mcportal/src/shell/`.

Rows: `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_MCPORTAL-Z-W1-S<k>`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after the nested commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-t-5"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/t5.AC1.sh; echo "exit=$?"</invocation><expect>bun test rc=0; named tests passing 3 of 3; fail=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-t-5"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/t5.AC2.sh; echo "exit=$?"</invocation><expect>fixed route fragments present 4 of 4; routes outside /api/admin/=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/NFRA_MCPORTAL.TO-MP-t-5.entitlements-pages.proof_of_spec.json`. Report once: what you changed and where, the nested commit hash, the router hookup lines you need, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** S5 + S7 pages. Provisioned `--nested mcportal=wk-NFRA_MCPORTAL-1-mcportal` after MP-w-1 drains. The
render is the issuer's real run.

<status>complete</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
