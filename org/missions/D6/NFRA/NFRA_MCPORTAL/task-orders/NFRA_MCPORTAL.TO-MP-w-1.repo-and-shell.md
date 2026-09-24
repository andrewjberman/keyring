# NFRA_MCPORTAL task order -- `MP-w-1` -- HOP 1: the mcportal repo wired in, and the dashboard shell

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-w-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: GIT-FETCH of https://github.com/Opal-Capital/mcportal.git (Opal's own private repo) and `bun install` from the npm registry inside the nested repo only. No push.
</preflight>

## 1. THE CELL -- `MP-w-1` (round 1, decomposition s.2/s.3)

`mcportal` is Andrew's operator console at `mcp.opalinvest.dev`, and only Andrew uses it. Its repo
`Opal-Capital/mcportal` exists: private, `DEV` = `PROD` = `fa1ff9693b0868c29c8ff421d403449db8a1ee39` (a README only).
The gateway will serve its built pages. Build:
1. **Parent**: `.gitmodules` gains `mcportal` (`url = https://github.com/Opal-Capital/mcportal.git`, `branch = DEV`)
   BESIDE the existing `portal` and `opal_ai` entries (leave those byte-unchanged), and the gitlink `mcportal` at
   `fa1ff9693b0868c29c8ff421d403449db8a1ee39`.
2. **Nested `mcportal`**: a React + Vite + TypeScript scaffold on bun:
   - `package.json` with `build` (Vite, to `dist/`), and tests through `bun test`;
   - it follows the portal's design law in `portal/DESIGN.md` (read it; the colors, type and panel rules bind);
   - a SHELL: a left sidebar listing the pages in the order of the brief
     `docs/briefs/mcportal-tech-ops-dashboard-brief-20260917.md` at pin `8d1f5c362b` (read it with
     `git show 8d1f5c362b:docs/briefs/mcportal-tech-ops-dashboard-brief-20260917.md`; Andrew's page order is in it);
   - a Home route, and placeholder routes for the other pages. The pages themselves are later cells.
   - `src/shell/sidebar.test.ts` holds the test named exactly `sidebar lists the pages in the brief's order`,
     asserting the sidebar's labels equal that list in order.
   - `dist/` is NOT committed (add it to `.gitignore`).

## 2. BOUNDS

1. **Nested repo:** the main tree has no `mcportal` yet, so after adding the mapping, initialise it INSIDE your worktree
   (`git submodule update --init mcportal`, which lands at `fa1ff9693b`). Then create the branch
   `wk-NFRA_MCPORTAL-1-mcportal` in it and commit your nested files there with `git -C mcportal commit --author
   "0.9.0_WK_NFRA_MCPORTAL~1 <0.9.0_WK_NFRA_MCPORTAL~1@opal.agent>" -F <msgfile> -- <paths>`, where the msgfile is
   written with the Write tool. That nested repo has no hooks. Its git dir lives under your worktree's; the issuer
   fetches your nested branch at the drain, before teardown. Do NOT move the parent gitlink off `fa1ff9693b`: the
   issuer bumps it when the nested commits reach the remote (G-PUSH). Parent files go through `safe-commit.sh`.
2. `bun install` inside `mcportal/` is permitted; nothing is installed anywhere else. No server is started (port 5174
   belongs to the portal).
3. Standing: no push, no vendor API call, no AWS. REFUSE a criterion you cannot meet as written, and report the refusal
   with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
.gitmodules
mcportal
mcportal/
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read (never write): `portal/DESIGN.md`; the brief at `8d1f5c362b`.

Rows: `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_MCPORTAL-Z-W1-S<k>`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after both repos are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-w-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/w1.AC1.sh; echo "exit=$?"</invocation><expect>mcportal.url=https://github.com/Opal-Capital/mcportal.git mcportal.branch=DEV, opal_ai and portal still mapped, gitlink=160000 fa1ff9693b0868c29c8ff421d403449db8a1ee39 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-w-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/w1.AC2.sh; echo "exit=$?"</invocation><expect>build rc=0; dist/index.html=yes; js assets>=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-w-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/w1.AC3.sh; echo "exit=$?"</invocation><expect>bun test rc=0; named test lines>=1; fail=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/NFRA_MCPORTAL.TO-MP-w-1.repo-and-shell.proof_of_spec.json`. Report once: what you changed and where, the commit hashes in BOTH repos, the sidebar order you read from the brief, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** spawned only after NFRA_OPALAI's OA-w-1 merged (it writes `.gitmodules`); plain worktree off HEAD. At
the drain, BEFORE teardown: `git submodule update --init mcportal` in the main tree, then fetch the worker's nested
branch `wk-NFRA_MCPORTAL-1-mcportal` from the worktree's module git dir into it. Later mcportal cells are provisioned
`--nested mcportal=wk-NFRA_MCPORTAL-1-mcportal`. The FE render check is the issuer's real run at close.

<status>pending</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
