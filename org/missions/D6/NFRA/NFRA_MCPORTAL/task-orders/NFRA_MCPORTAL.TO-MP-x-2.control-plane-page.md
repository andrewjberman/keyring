# NFRA_MCPORTAL task order -- `MP-x-2` -- ROUND 4: the Control Plane page in mcportal (FWD-14 hop 4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-x-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~6</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a page; no cron, alarm, monitor or cadence (PRD C8, C12: read when opened).
comp-iam: DECLARED-NOT-APPLICABLE -- front-end only; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the five named tests are the adversary arms (absent box, ages, unreadable store, refresh).
EGRESS CLASS, declared: none. Dependencies are already installed from bun's local cache in your worktree; add no package.
</preflight>

## 1. THE CELL -- `MP-x-2` (round 4, decomposition section R4.2 and the contract in R4.3)

You have two worktrees, nested:
- the workspace worktree `C:/tmp/mp-r4-6`, branch `wk-NFRA_MCPORTAL-r4-6`;
- inside it, the mcportal worktree `C:/tmp/mp-r4-6/mcportal`, branch `wk-NFRA_MCPORTAL-r4-6-mcportal`, based on
  `a3bff71`. That commit is the bundle live on the gateway today. `node_modules` is already installed. Do not run
  `bun install` or `bun add`.

All your code changes are in the mcportal worktree. Commit them there with plain `git commit`, author
`0.9.0_WK_NFRA_MCPORTAL~6 <0.9.0_WK_NFRA_MCPORTAL~6@opal.agent>`. mcportal is its own repo, outside the workspace's
safe-commit lanes. Your proof-of-spec instance and any surprise row are committed in the workspace worktree via
`.tools/safe-commit.sh`. Never push either repo.

Andrew wants to open one page and see which box is working on what right now, without asking any seat. A parallel
cell is building the backend: `GET /api/admin/fabric/boxes?hours=N`, with N from 1 to 24 and a default of 6. Its
response is fixed, and you build against it exactly:
```
{ "window": {"hours": N, "start": "<ISO Z>", "end": "<ISO Z>"},
  "read_at": "<ISO Z>", "records_scanned": <int>, "records_skipped": <int>,
  "source": "s3://opal-313476888478-globgrph/fabric/activity/v1/",
  "boxes": [ { "box": "<name>", "status": "reporting" | "not reporting", "commits": <int>,
               "seats": ["<serial>", ...],
               "projects": [ {"code": "<CODE>", "commits": <int>, "last": "<ISO Z>"} ],
               "last_commit": {"when": "<ISO Z>", "sha": "<12>", "seat": "<serial>", "subject": "<text>"} | null,
               "claims": ["measured" | "inferred" | "absent", ...] } ],
  "unrostered": [ "<name>", ... ] }
```
An unreadable store answers **503** `{"error": "store unreadable", "reason": "<text>"}`.

Build:
1. **API client.** In `src/api/admin.ts`, add the types for that response and a function
   `getFabricBoxes(hours?: number)`. It must follow the file's existing fetch pattern: same-origin, credentials included,
   refusing a non-JSON 200 as the existing calls do. Its error shape must carry the 503's `reason` to the caller. Update
   the file's header comment, which lists the fixed route set, to name the fifth route. Add a test to
   `src/api/admin.test.ts` that the function calls `/api/admin/fabric/boxes?hours=<N>`.
2. **The page,** in `src/pages/control-plane/` (new): `ControlPlane.tsx` (fetches), `ControlPlaneView.tsx` (pure render
   from props, so tests use `renderToStaticMarkup` as `src/pages/recent-changes/recent-changes.test.tsx` does),
   `control-plane.css`, `index.ts`, and `control-plane.test.tsx`.
   - **Layout.** One row per box, in the order the response gives. Each row shows the box, its status, commits, seats,
     and its projects with their commit counts.
   - **Last commit.** Show the time, the seat and the subject.
   - **Not reporting.** A "not reporting" box reads the words "not reporting" where its figures would be, and shows no
     0 count.
   - **Age.** Every time shown carries its age next to it, relative to the response's `read_at` (for example
     "14:02Z, 12m ago"). The page header shows the window and `read_at` with its age.
   - **Unrostered.** If `unrostered` is non-empty, list it under the table as "seen but not on the roster".
   - **Refresh.** The view updates while the page stays open: it re-fetches every 60 seconds (export `REFRESH_MS =
     60000`) and on a Refresh button, and every age re-renders against the new `read_at`. Put the schedule in an
     exported function `startAutoRefresh(fetchOnce, setIntervalFn, clearIntervalFn)` that returns a stop function, so a
     test can drive it with a fake timer. It is a page refresh, never an alert or a notification (PRD C8). This is
     AMENDMENT 1 (CTO~O ruling msg 32041 on C12).
   - **Window picker.** It offers 1h, 6h and 24h, default 6h.
   - **Unreadable store.** On a 503 or any fetch error, show "Store unreadable" and the reason, and show NO table and NO
     numbers.
   - **Style.** Follow the page style and the design tokens already in `src/styles/tokens.css` and the existing pages.
     Add no new colour.
3. **Routing.** In `src/App.tsx`, route `/control-plane` to the page, as `/mcp-server` is routed.
4. **Sidebar.** In `src/shell/pages.ts`, append `{ id: 'control-plane', label: 'Control Plane', path: '/control-plane' }`
   as the LAST entry, after Infosec. Andrew's order for the existing entries stands unchanged. In
   `src/shell/sidebar.test.ts`, keep `BRIEF_ORDER` as it is, with his quotation, and assert `PAGES` labels equal
   `[...BRIEF_ORDER, 'Control Plane']`. Add a comment citing PRD v0.5 S14 and the decomposition's R4.6 item 3.
5. **Tests.** `control-plane.test.tsx` holds these five tests by these exact names:
   - `"control plane lists every roster box"`: a fixture with 4 boxes renders 4 rows, each with the box name.
   - `"a not reporting box reads not reporting"`: a box with `status` "not reporting" renders the text "not reporting".
     Its row contains no digit 0 as a count.
   - `"every figure shows its age"`: with `read_at` 14:14Z and a `last_commit.when` of 14:02Z, the row shows "12m ago".
   - `"an unreadable store shows the reason and no numbers"`: the error state renders "Store unreadable" and the reason,
     and renders no table element.
   - `"the view refreshes while open"`: `startAutoRefresh` with a fake interval calls `fetchOnce` once per tick at
     `REFRESH_MS`, and calling the returned stop function clears the interval.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not touch the gateway, Terraform, the manifest, `package.json`,
   `bun.lock` or any existing page's behaviour. Make no deploy and no AWS call.
2. Standing rules: no push and no vendor call. If you cannot meet a criterion as written, REFUSE it with its
   measurement. Never repair a criterion.

## 3. SURFACES

<paths>
mcportal/src/pages/control-plane/**
mcportal/src/api/admin.ts
mcportal/src/api/admin.test.ts
mcportal/src/App.tsx
mcportal/src/shell/pages.ts
mcportal/src/shell/sidebar.test.ts
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~6/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `mcportal/src/pages/recent-changes/`, `mcportal/src/pages/mcp-server/entitlements/`,
`mcportal/src/styles/tokens.css`, `portal/DESIGN.md`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round4/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W6-S<k>` (the next free k for W6). `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from `C:/tmp/mp-r4-6` after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-x-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round4/checks/x2.AC1.sh; echo "exit=$?"</invocation><expect>bun test rc=0; named tests present in sources 5 of 5; pass>=5; fail=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-x-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round4/checks/x2.AC2.sh; echo "exit=$?"</invocation><expect>labels: Home|Operations Report|User Management|User Analytics|MCP Server|Health Check|Cost Management|Infosec|Control Plane; bun test rc=0; fail=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-x-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round4/checks/x2.AC3.sh; echo "exit=$?"</invocation><expect>build rc=0; dist/index.html=yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~6/NFRA_MCPORTAL.TO-MP-x-2.control-plane-page.proof_of_spec.json`,
naming the mcportal commit hash. Report once, with:
- the three check outputs;
- both commit hashes (mcportal and workspace);
- one paragraph on how a "not reporting" box and the error state look;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the round-4 issuance from PRD v0.5 (FWD-14, S14, C12) @cecf26d2c9, signed @8de5b2dc76. The
issuer prepared the worktrees. The mcportal worktree was cut by `git -C mcportal worktree add` at a3bff71 (the
manifest's `mcportal_commit`, live). `bun_cache_precheck.py bun.lock` read 77 of 77, and `bun install
--frozen-lockfile` installed 77 packages from the cache. Checks dry-run in `C:/tmp/mp-r4-6` at base: AC1 FAIL (dir
absent); AC2 FAIL (labels lack Control Plane; bun test rc=0, fail=0); AC3 PASS (build rc=0). AC3 is the deploy's own
build step, and it guards against a regression. The sidebar placement (last) is the issuer's, recorded in decomposition
R4.6 item 3. The mcportal commit reaches the gateway only through MP-x-4, which moves `EC2_MANIFEST.json`
`mcportal_commit`. No gate.

**AMENDMENT 1 (2026-10-08 ~22:0xZ, the issuer, no CTO ruling needed on its own criteria):** the CTO~O ruling
msg 32041 reads C12's "streaming" as the view updating while open. The Refresh bullet, the fifth named test and AC1's
expectation (5 of 5) changed. Graded by to-pipeline-gate on the amendment commit; the worker receives it as a
continuation when it reports (a worker cannot be messaged mid-run).

<status>complete -- drained by 2.0.0_SA_COO~MP 2026-10-08 ~22:5xZ @6b1b7b18dd: AC1 5 of 5, AC2, AC3 PASS (issuer re-run in C:/tmp/mp-r4-6); mcportal d60b4e0 (LOCAL, wk-NFRA_MCPORTAL-r4-6-mcportal) goes live only through the release cell. Was: pending</status>
<round>4</round>
<slot>~6</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
