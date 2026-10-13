# NFRA_MCPORTAL task order -- `MP-z-2` -- WORKSTREAM GW ROUND 1: the Gateway page and the bundle's route list (FWD-20, S16)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-z-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-z-2</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~14</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a page; read when opened (PRD C8), no refresh loop beyond the existing pattern.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM, no AWS; the page calls one same-origin /api/admin route.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (no holder, unrated, unreadable store, route list drift).
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MP-z-2` (workstream GW round 1, decomposition sections GW.1, GW.3 and GW.4)

You have two worktrees, nested:
- the workspace worktree `C:/tmp/mp-gw-14`, branch `wk-NFRA_MCPORTAL-gw-14`;
- inside it, the mcportal worktree `C:/tmp/mp-gw-14/mcportal`, based on mcportal `bc37107` (the commit live on the
  gateway today: Control Plane and Open Calls). `node_modules` is linked. Do not run `bun install` or `bun add`.

All your code changes are in the mcportal worktree. Commit them there with plain `git commit`, author
`0.9.0_WK_NFRA_MCPORTAL~14 <0.9.0_WK_NFRA_MCPORTAL~14@opal.agent>`. mcportal is its own repo, outside the workspace's
safe-commit lanes. Your proof-of-spec instance and any surprise row are committed in the workspace worktree via
`.tools/safe-commit.sh`. Never push either repo.

Andrew wants ONE page that shows the gateway's full breakdown: every vendor or channel, the tools and catalog indexes on
each, and who is entitled to each today (PRD v0.7 FWD-20). A parallel cell builds the backend. The route is fixed and
you build against it exactly:

`GET /api/admin/gateway/breakdown` (owner-gated, same origin) answers 200 with:
```
{ "read_at": "<ISO Z>",
  "kill_switch": true | false,
  "channels": [
    { "id": "m365" | "<integration id>", "name": "<text>", "kind": "native" | "integration",
      "auth": "<text>", "min_tier": "<text>",
      "rating": {"value": "<R0..R4>" | "unrated", "reason": "<text>" | null},
      "tools": [ { "name": "<tool>", "access": "read" | "write", "write_class": "<text>" | null,
                   "data_class": "<text>", "graph_scopes": ["<scope>"] | null, "indexes": ["<catalog id>"] } ],
      "indexes": ["<catalog id>"],
      "holders": [ { "who": "<text>", "how": "<text>", "tools": ["<tool>"] } ],
      "holders_basis": "<text>" } ],
  "grant_store": {"status": "read" | "unreadable", "principals": <int> | null, "reason": "<text>" | null} }
```
A non-200 is shown with its status and body text, the way the Control Plane page shows a 503.

Build, in mcportal:
1. **The Gateway page** at `src/pages/gateway/` (new): the page component and its tests.
   - A header line: the read time, the channel count, the total tool count, and the kill-switch state. When
     `kill_switch` is true, say so in one line above the channels.
   - When `grant_store.status` is "unreadable": one line above the channels, "Grant store unreadable: <reason> -- people
     holding a data grant are not shown". Never print it as "no grants".
   - One section per channel, in response order: name, kind, auth, min tier, and the rating (the value and its reason;
     "unrated" printed as "unrated", never a level).
     - A tools table: name, read or write (with the write class when present), data class ("unclassified" printed as
       is), Graph scopes ("none" when null), indexes ("none" when empty).
     - The channel's indexes ("none" when empty).
     - Who holds it: one row per holder (who, how, the tools it holds); when `holders` is empty print "no one", never a
       blank; then `holders_basis` in small text.
   - Follow the existing pages' idiom and design (read `src/pages/control-plane/` and `src/pages/open-calls/` first and
     match their components, tokens and table style). Light canvas, navy ink, one band per page.
2. **The client function** `getGatewayBreakdown()` in `src/api/admin.ts`, in the style of the existing admin client
   functions (it refuses a non-JSON 200 with a plain reason, as they do). Add its test to `src/api/admin.test.ts`.
3. **The route and the sidebar.** `src/App.tsx`: `<Route path="/gateway" element={...} />`. `src/shell/pages.ts`: append
   `{ id: 'gateway', label: 'Gateway', path: '/gateway' }` LAST, after Open Calls, with a comment citing NFRA_MCPORTAL PRD
   v0.7 FWD-20 / S16; Andrew's order above it is unchanged. Update `src/shell/sidebar.test.ts` for the new last entry.
4. **The route list, `public/routes.json` (new).** `{"version": 1, "paths": [...]}`: every path the app's `<Routes>`
   serves, sorted -- the PAGES paths, `/mcp-server/recent-changes`, and `/gateway`. Vite copies `public/` to the bundle
   root, so the built bundle carries `routes.json` beside `index.html`. The gateway reads it to serve deep links (a
   parallel cell), so it must never drift: add a test, by the exact name below, that reads `public/routes.json` and fails
   if its `paths` differ from the set of `path=` values in `src/App.tsx`'s `<Route>` elements plus every `PAGES` path.
5. **Tests, by these exact names** (bun 1.3.x prints a test name only on failure, so the check reads them from the
   sources; write them exactly):
   - "gateway page lists every channel with its tools and indexes" -- a planted 2-channel response renders both channels,
     every tool row, and "none" for an empty index list.
   - "a channel with no holder reads no one" -- `holders: []` prints "no one".
   - "an unrated channel reads unrated" -- `rating.value` "unrated" prints "unrated" and no level.
   - "an unreadable grant store is shown and never reads as no grants" -- `grant_store.status` "unreadable" prints the
     reason line, and the text "no grants" appears nowhere.
   - "routes json equals the app routes" -- item 4.

**AMENDMENT 1 (issuer, 2026-10-13 ~16:3xZ, on Andrew's word): make Control Plane and Open Calls easier to read.** The
words, recorded in `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ANDREW_DIRECT_20261013_162xZ_CONTROL_PLANE_OPEN_CALLS_READABILITY.md`:
*"I'd like for them to be visually slightly easier to read, particularly on the control-plane side. both can be
articulated better, but open-calls is mostly legible."*

What his screenshots of the live pages show:
- On the Control Plane boxes table, Box, Status and Commits break every one or two letters ("d / el / l2",
  "re / p / or / ti / n / g"), and so do their headers.
- One unbroken comma list of ~40 seat serials takes most of the row.
- Project names break mid-token ("IRPT_AN / LREQ"), and each project's count and age run down the cell one word per line.
- On Open Calls, Box, Project and Asked by break mid-token ("TCKT_VNE / XT", "2.0.0_SA_CO / O~V2"), and Age wraps.

The cause, read by the issuer: `word-break: break-word` on EVERY cell of both tables (`control-plane.css` about `:46-55`,
`open-calls.css` about `:45-54`), with nothing protecting the short columns.

Change, in the two pages' own files only (their CSS and view components):
- **Every table on both pages** (the boxes table, the Overlap and Git state panels, Open Calls):
  - an identifier, code or short value (box, status, counts, project code, seat serial, age, state) never breaks inside a
    token: `white-space: nowrap` or `word-break: normal` on those columns;
  - only prose (a commit subject, a call subject, a note) may wrap, and it wraps at spaces.
  - Remove the blanket `word-break: break-word`.
- **Control Plane boxes table:**
  - Status is a short badge.
  - Seats becomes a count ("41 seats") with the full list behind a native `<details>` disclosure, one serial per line,
    grouped by role prefix (`0.0.0_`, `0.7.0_`, `0.9.0_WK_`, `1.0.0_`, `2.0.0_`, `3.0.0_`, `4.0.0_`, in that order).
  - Projects is one line per project: `<CODE>  <n> commits  last <HH:MMZ> (<age>)`.
  - Last commit puts its time and age on line 1, the serial on line 2, and the subject on line 3, clamped to two lines
    with the full text in `title`.
  - Give Projects and Last commit room, so that no data cell in the screenshots' first row is taller than its projects
    list.
- **Open Calls:** Box, Project, Asked by, Age and the request/close column never wrap. Subject takes the remaining width.
  The call id stays muted on its own line.
- **Keep:** the "absent", "not recorded" and "unreadable" texts verbatim, the refresh behaviour, the design law (light
  canvas, navy ink, one band per page), and every existing test.
- **Add these two tests, by these exact names:**
  - "boxes table shows a seat count with the full list behind a disclosure" (control-plane);
  - "short columns do not wrap mid-token" (either page): assert the class or style that carries `nowrap` on the Box,
    Project and Asked by cells.
- Write surface grows by the two pages' directories (section 3). Your mcportal base is `6fbd25e` (your own Gateway page
  commit, branch `nfra-mcportal-gw-z2`), so all three pages ship in ONE bundle.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not change other pages, `src/styles/`, the build config, the
   lockfile or `package.json`. No backend file, no AWS call, no deploy.
2. Standing rules: no push and no vendor call. If you cannot meet a criterion as written, REFUSE it with its measurement.
   Never repair a criterion.

## 3. SURFACES

<paths>
mcportal/src/pages/gateway/**
mcportal/src/api/admin.ts
mcportal/src/api/admin.test.ts
mcportal/src/App.tsx
mcportal/src/shell/pages.ts
mcportal/src/shell/sidebar.test.ts
mcportal/public/routes.json
mcportal/src/pages/control-plane/**
mcportal/src/pages/open-calls/**
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~14/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `mcportal/src/pages/mcp-server/`,
`mcportal/src/styles/tokens.css`, `mcportal/vite.config.ts`, `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W14-S<k>` (the next free k for W14). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an
ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your WORKSPACE worktree root after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-z-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/z2.AC1.sh; echo "exit=$?"</invocation><expect>bun test rc=0; named tests present in sources 7 of 7; fail=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-z-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/z2.AC2.sh; echo "exit=$?"</invocation><expect>build rc=0; dist/routes.json: version=1 paths=N missing=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-z-2" judgment="true"/>
</proof_of_spec>

AC1 now also requires the two AMENDMENT 1 tests (the check file is amended at the same commit: 7 named). AC3 (JUDGMENT,
graded by `3.0.0_SA_CVO~Z` on the issuer's rendered screenshots of both pages with live data, never by you): Control
Plane and Open Calls read easily at a glance, and no identifier breaks mid-token. Record AC3 under
`UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO~Z`.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~14/NFRA_MCPORTAL.TO-MP-z-2.gateway-page-and-route-list.proof_of_spec.json`.
Report once, with:
- the two check outputs;
- the mcportal commit hash or hashes and the workspace commit hash;
- the `routes.json` paths as committed;
- any part of the response you could not render as written, and why;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the GW issuance (decomposition v7) from PRD v0.7 FWD-20, S16 @cdb5ff66b1, plus the route list
the deep-link cell reads (CTO ruling msg 33519, row Z-S41). Base mcportal `bc37107` = EC2_MANIFEST `mcportal_commit`.
Provision with `wk-provision.sh provision NFRA_MCPORTAL 14 --path C:/tmp/mp-gw-14 --nested mcportal=bc37107`. Checks
dry-run at base 8abe56f2cd: AC1 FAIL (`src/pages/gateway` absent), AC2 FAIL (no routes.json at base). No gate. Lives
through MP-z-5.

<status>pending</status>
<round>1</round>
<workstream>GW</workstream>
<slot>~14</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

<status>complete</status>
<status>in_progress</status>
<!-- REOPENED by the issuer 2026-10-13 ~16:3xZ: AMENDMENT 1 (Andrew-direct readability of Control Plane and Open Calls); slot ~14 re-seated on mcportal 6fbd25e. -->
