# NFRA_MCPORTAL task order -- `MP-pc-3` -- WORKSTREAM PC ROUND 1: the People page (FWD-21 read) and the three refusal states on the Git state panel (G1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pc-3</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pc-3</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~22</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a page; it reads when opened and refreshes while open, as the Gateway page does.
comp-iam: DECLARED-NOT-APPLICABLE -- a front-end bundle; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (a person holding nothing, absent claims, the three refusal states, the route list).
EGRESS CLASS, declared: none. Tests run against fixtures; no network call.
</preflight>

## 1. THE CELL -- `MP-pc-3` (workstream PC round 1, decomposition sections PC.1, PC.2 and PC.3)

You have two worktrees, nested:
- the workspace worktree `C:/tmp/mp-pc-22`, branch `wk-NFRA_MCPORTAL-pc-22`;
- inside it, the mcportal worktree `C:/tmp/mp-pc-22/mcportal`, based on mcportal `0e02a1f` (the commit live on the
  gateway today: Control Plane, Open Calls and the Gateway page). `node_modules` is linked. Do not run `bun install` or
  `bun add`.

All your code changes are in the mcportal worktree. Commit them there with plain `git commit`, author
`0.9.0_WK_NFRA_MCPORTAL~22 <0.9.0_WK_NFRA_MCPORTAL~22@opal.agent>`. mcportal is its own repo, outside the workspace's
safe-commit lanes. Your proof-of-spec instance and any surprise row are committed in the workspace worktree via
`.tools/safe-commit.sh`. Never push either repo.

Two things, both against fixed backend shapes that parallel cells build. Build against them exactly.

**A. The People page (PRD v0.8 FWD-21, the read half).** Andrew picks a person and sees what that person reaches
through the gateway. The route is fixed. `GET /api/admin/people` (owner-gated, same origin) answers 200 with:
```
{ "read_at": "<ISO Z>",
  "kill_switch": true | false,
  "people": [
    { "who": "<text>", "kind": "person" | "population", "how": "<text>", "tier": "<text>" | "unresolved",
      "channels": [
        { "id": "<text>", "name": "<text>",
          "tools": [ { "name": "<tool>",
                       "history_depth": {"claim": "measured" | "inferred" | "absent", "value": <any> | null, "reason": "<text>" | null},
                       "freshness":     {"claim": "measured" | "inferred" | "absent", "value": <any> | null, "reason": "<text>" | null},
                       "cadence":       {"claim": "absent", "value": null, "reason": "<text>"} } ] } ] } ],
  "people_basis": "<text>",
  "grant_store": {"status": "read" | "unreadable", "principals": <int> | null, "reason": "<text>" | null} }
```
- Add `getPeople()` to `src/api/admin.ts`, beside `getGatewayBreakdown()`, with the same fetch discipline (credentials
  included; a non-JSON 200 refused with a plain reason, as `getGatewayBreakdown` does), its types, and a test in
  `src/api/admin.test.ts`.
- A new page folder `src/pages/people/` (copy the Gateway page's structure: a container that fetches when opened, on
  Refresh and every 60 s via `startAutoRefresh`, and a pure view component). The page shows:
  - a person picker listing every `who`, in the order given, so Andrew picks one person;
  - for the picked person, their `how` and `tier`, then each channel with its tools in a table with columns Tool,
    History depth, Freshness and Cadence. Each figure cell prints its `value` and its `claim`. An `absent` claim prints
    the word "absent" and its reason, never blank;
  - a person with `channels: []` prints "holds nothing";
  - with `kill_switch` true, a line "kill switch on: no one may call";
  - `grant_store.status` "unreadable" prints its reason, and never reads as "no grants";
  - `people_basis` beneath.
- Route `/people` in `src/App.tsx`; an entry in `src/shell/pages.ts` directly after the Gateway entry (label "People");
  update `src/shell/sidebar.test.ts` for the new entry; add `/people` to `public/routes.json` (sorted). The existing
  test "routes json equals the app routes" must still pass.
- Follow the page's colour law as the Gateway page does: the light canvas, white hairline panels, navy ink, ONE band.

**B. The Git state panel's refusal cell (G1, row Z-C-S31).** `GET /api/admin/fabric/gitstate`'s per-box
`integration_refused` becomes one of three shapes (the gateway half is a parallel cell):
- `{"refused": true, "at": "<ISO>", "note": "<text>"}`, printed `refused <clock(at)>: <note>`;
- `{"refused": false, "at": "<ISO>"}`, printed `no (<clock(at)>)`;
- the string `"not recorded"`, printed `not recorded`.
Each box also carries `integration_refused_basis` (a string). Update the `GitBox` type in `src/api/admin.ts` and both
places in `src/pages/control-plane/GitStatePanelView.tsx` that print the cell (about `:24-26` and `:55-57`): today they
print `refused ...` for ANY object, which would show "refused" for a clean pass. Use the existing `clock` helper. Show
`integration_refused_basis` as the cell's title attribute.

**Tests, by these exact names** (bun prints a name only on failure, so the check reads them from your sources):
- "people page lists every person with channels and tools"
- "a person holding nothing reads holds nothing"
- "depth freshness and cadence show their claims and absent is said"
- "routes json equals the app routes" (existing; keep it passing)
- "git state reads no with the pass time for a clean integrate" (in `src/pages/control-plane/control-plane.test.tsx`)
- "git state reads refused with time and note"
- "git state reads not recorded without a pointer"

## 2. BOUNDS

1. Write surface: exactly the paths in section 3, all inside the mcportal worktree except your deliverables and rows.
   Do not change the Gateway, Open Calls or Entitlements pages, any other control-plane panel, the build config, or
   `package.json`/`bun.lock`. Make no deploy and no network call.
2. Standing rules: no push of either repo and no vendor call. If you cannot meet a criterion as written, REFUSE it with
   its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
mcportal/src/pages/people/
mcportal/src/pages/control-plane/GitStatePanelView.tsx
mcportal/src/pages/control-plane/control-plane.test.tsx
mcportal/src/api/admin.ts
mcportal/src/api/admin.test.ts
mcportal/src/App.tsx
mcportal/src/shell/pages.ts
mcportal/src/shell/sidebar.test.ts
mcportal/public/routes.json
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~22/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `mcportal/src/pages/gateway/**` (your model for structure, fetch and style), every other mcportal
file, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pc/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W22-S<k>` (the next free k for W22). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an
ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your WORKSPACE worktree root `C:/tmp/mp-pc-22` after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pc-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pc/checks/pc3.AC1.sh; echo "exit=$?"</invocation><expect>bun test rc=0; named tests present in sources 7 of 7; routes.json lists /people: yes; pass>=7; fail=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~22/NFRA_MCPORTAL.TO-MP-pc-3.people-page-and-refused-states.proof_of_spec.json`.
Report once, with:
- the check output;
- the mcportal commit hash or hashes, and the workspace commit hash;
- the files you touched;
- any part of either shape you could not render as written, and why;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PC issuance (decomposition v9) from PRD v0.8 FWD-21 @7da54894cf and the C17 round-2
analysis @d0dd3f0964 (F1, and G1's panel half; the panel half rides this cell because both mcportal halves write
`src/api/admin.ts`). Check dry-run at base 9be88c9134: AC1 FAIL (`mcportal/src/pages/people` absent). The drain runs `bun run build`
and the typecheck once (hygiene off the face). Lives through MP-pc-5.

<status>pending</status>
<round>1</round>
<workstream>PC</workstream>
<slot>~22</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

<status>complete</status>
