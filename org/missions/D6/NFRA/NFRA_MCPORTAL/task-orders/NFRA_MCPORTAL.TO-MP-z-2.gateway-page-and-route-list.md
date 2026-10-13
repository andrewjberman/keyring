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
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~14/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `mcportal/src/pages/control-plane/`, `mcportal/src/pages/open-calls/`, `mcportal/src/pages/mcp-server/`,
`mcportal/src/styles/tokens.css`, `mcportal/vite.config.ts`, `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W14-S<k>` (the next free k for W14). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an
ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your WORKSPACE worktree root after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-z-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/z2.AC1.sh; echo "exit=$?"</invocation><expect>bun test rc=0; named tests present in sources 5 of 5; fail=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-z-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/z2.AC2.sh; echo "exit=$?"</invocation><expect>build rc=0; dist/routes.json: version=1 paths=N missing=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

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
