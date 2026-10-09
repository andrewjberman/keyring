# NFRA_MCPORTAL task order -- `MP-p-2` -- WORKSTREAM CP2 ROUND 1: the Overlap and Git state panels and the Open Calls page (FWD-15..17)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-p-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-p-2</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~11</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- page code; the 60 s re-fetch while the page is open is MP-x-2's page refresh (C12 ruling, CTO~O msg 32041), never an alert or notification (C8).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM, no AWS; the page calls only same-origin /api/admin routes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (absent list, not recorded box, the close round trip).
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MP-p-2` (workstream CP2 round 1, decomposition sections CP2.1, CP2.3 and CP2.4)

You have two worktrees, nested:
- the workspace worktree `C:/tmp/mp-cp2-11`, branch `wk-NFRA_MCPORTAL-cp2-11`;
- inside it, the mcportal worktree `C:/tmp/mp-cp2-11/mcportal`, based on mcportal `d60b4e0`. That commit holds the
  Control Plane page (MP-x-2) that ships in the next release. `node_modules` is linked. Do not run `bun install` or
  `bun add`.

All your code changes are in the mcportal worktree. Commit them there with plain `git commit`, author
`0.9.0_WK_NFRA_MCPORTAL~11 <0.9.0_WK_NFRA_MCPORTAL~11@opal.agent>`. mcportal is its own repo, outside the workspace's
safe-commit lanes. Your proof-of-spec instance and any surprise row are committed in the workspace worktree via
`.tools/safe-commit.sh`. Never push either repo.

Andrew wants three more things on the control plane:
- where two or more boxes are on the same surface, rated by risk (FWD-15);
- each box's git state (FWD-16);
- every open call on every box, with a close carrying his ruling (FWD-17).

Parallel cells build the backend. The four routes are fixed and you build against them exactly. All sit under
`/api/admin`. An unreadable store answers **503** `{"error": "store unreadable", "reason": "<text>"}`.

**`GET /api/admin/fabric/overlap?hours=N`** (N 1..24, default 6):
```
{ "window": {"hours": N, "start": "<ISO Z>", "end": "<ISO Z>"}, "read_at": "<ISO Z>",
  "records_scanned": <int>, "records_skipped": <int>, "source": "<s3 uri>",
  "rules": {"file": "<path>", "version": "<string>"},
  "deploys": [ {"box": "<name>", "status": "read" | "absent", "published_at": "<ISO Z>" | null, "open": <int> | null} ],
  "overlaps": [ { "surface": "<key>", "cls": "INFRA" | "CODE" | "REGISTRY" | "TOOL" | "RECORD" | "APPEND",
                  "boxes": [ {"box": "<name>", "commits": <int>, "seats": ["<serial>"], "last": "<ISO Z>"} ],
                  "last": "<ISO Z>",
                  "deploys_open": [ {"box": "<name>", "slug": "<slug>", "status": "<status>", "opened_at": "<ISO>"} ],
                  "rating": <int>, "label": "<text>" } ] }       (already sorted, highest risk first)
```
**`GET /api/admin/fabric/gitstate`:**
```
{ "read_at": "<ISO Z>", "source": "<s3 uri>",
  "trunk": {"head": "<12>" | null, "first_seen": "<ISO Z>" | null, "claim": "inferred", "basis": "<text>"},
  "boxes": [ { "box": "<name>", "status": "recorded" | "not recorded", "at": "<ISO Z>" | null,
               "box_branch": "<text>" | null, "box_head": "<12>" | null, "origin_box_head": "<12>" | null,
               "trunk_head": "<12>" | null, "unpushed": <int> | null, "pushed_not_on_trunk": <int> | null,
               "behind_trunk": <int> | null,
               "state": "committed, not pushed" | "pushed, not on trunk" | "on trunk" | "not recorded",
               "unread": ["<text>"],
               "last_pass": {"mode": "<text>", "rc": <int>, "note": "<text>", "serial": "<text>"} | null,
               "integration_refused": {"at": "<ISO Z>", "note": "<text>"} | "not recorded" } ] }
```
**`GET /api/admin/fabric/calls?state=open|all`** (default open):
```
{ "read_at": "<ISO Z>", "source": "<s3 uri>",
  "boxes": [ {"box": "<name>", "status": "published" | "absent", "written_at": "<ISO Z>" | null,
              "written_by": "<serial>" | null, "scanned_at": "<ISO Z>" | null, "open": <int> | null} ],
  "calls": [ {"box": "<name>", "id": "<id>", "project": "<CODE>", "subject": "<text>", "asked_by": "<serial>",
              "opened_at": "<ISO Z>", "state": "<state>", "source": "<path>",
              "request": {"id": "<rid>", "state": "PENDING" | "APPLIED" | "REFUSED", "requested_at": "<ISO Z>",
                          "detail": "<text>" | null} | null } ] }
```
**`POST /api/admin/fabric/calls/close`.** The JSON body is `{"box", "call_id", "ruling"}`. The answers are:
- 202 `{"request_id", "key", "state": "PENDING"}`;
- 400 bad input;
- 409 `{"error": "call not open on that box"}`;
- 503 `{"error": "request not written" | "store unreadable", "reason"}`.

The box applies the request on its next scan, within about 10 minutes. Until then the call shows the request as PENDING.

Build:
1. **API client.** In `src/api/admin.ts`, add the types and four functions in the file's existing fetch pattern
   (same-origin, credentials included, refusing a non-JSON 200, and carrying a 503's `reason` as `getFabricBoxes` does):
   - `getFabricOverlap(hours?: number)`;
   - `getFabricGitstate()`;
   - `getFabricCalls(state?: 'open' | 'all')`;
   - `closeFabricCall(box: string, callId: string, ruling: string)`.

   The POST's 400 and 409 bodies reach the caller as an error carrying the `error` text. Update the header comment's
   route list. Add tests to `src/api/admin.test.ts` that each function calls its exact path and method.
2. **Control Plane panels** (`src/pages/control-plane/`). Below the boxes table add two panels, each fetched on mount and
   on MP-x-2's existing refresh (`refresh.ts`, `REFRESH_MS`):
   - **Overlap.**
     - One row per overlap, in the order given: the surface, the label, the boxes with their commits, and `last` with
       its age.
     - A row with `deploys_open` non-empty is visibly marked and names each deploy's box and slug.
     - Under the rows, one line per box from `deploys`: "absent" verbatim where absent, otherwise "<n> open deploys,
       published <age>".
   - **Git state.**
     - One row per box: `state` verbatim; `box_head`, `origin_box_head` and `trunk_head`; the counts; `behind_trunk`; `at`
       with its age; and `integration_refused`, "not recorded" verbatim.
     - A "not recorded" box shows the words "not recorded" and no 0.
     - The header line shows the trunk head and "first seen <time> (inferred)".

   Keep each panel a pure view component taking props, with its own fetch wrapper, so tests can use
   `renderToStaticMarkup` as `control-plane.test.tsx` already does. An error in one panel shows "Store unreadable" and the
   reason in THAT panel only, and leaves the boxes table standing.
3. **Open Calls page** (`src/pages/open-calls/`, new): `OpenCalls.tsx` (fetches), `OpenCallsView.tsx` (pure render from
   props), `open-calls.css`, `index.ts` and `open-calls.test.tsx`.
   - **Box line.** A per-box status line: an "absent" box reads "absent", never an empty list; a published box shows its
     open count and the list's age.
   - **Calls table.** Box, project, asking seat, subject and age (from `opened_at`, against the response's `read_at`), plus
     the call's request state when one exists.
   - **Close form.** Each OPEN call has a Close control: a ruling text area and a Close button. On submit it calls
     `closeFabricCall`. On 202 it shows "PENDING -- the box applies it on its next scan" and re-fetches. On 400 or 409 it
     shows the error text. It never edits the list itself.
   - **Refresh.** Re-fetch on mount, on a Refresh button, and on the same 60 s refresh as Control Plane (reuse
     `startAutoRefresh` from `src/pages/control-plane/refresh.ts`).
   - **Style.** Use the existing tokens in `src/styles/tokens.css` and the existing pages' style. Add no new colour.
4. **Routing and sidebar.**
   - In `src/App.tsx`, route `/open-calls` as `/control-plane` is routed.
   - In `src/shell/pages.ts`, append `{ id: 'open-calls', label: 'Open Calls', path: '/open-calls' }` as the LAST entry,
     after Control Plane.
   - In `src/shell/sidebar.test.ts`, keep `BRIEF_ORDER` and its quotation as they are, and assert `PAGES` labels equal
     `[...BRIEF_ORDER, 'Control Plane', 'Open Calls']`, with a comment citing PRD v0.5 S15.
5. **Tests.** These five, by these exact names, in `src/pages/control-plane/*.test.tsx` or
   `src/pages/open-calls/open-calls.test.tsx`:
   - `"overlap panel lists the deploy-open Terraform surface first"`: a fixture with a `tf:` overlap carrying
     `deploys_open` and an `append:` overlap renders the `tf:` surface first, with the deploy mark and its slug.
   - `"git state panel reads not recorded for an unrecorded box"`: a "not recorded" box renders "not recorded" and no
     digit 0 in its row.
   - `"open calls page reads absent for a box with no list"`: a box with `status` "absent" renders "absent".
   - `"open calls shows box project seat and age"`: with `read_at` 14:14Z and `opened_at` 14:02Z, the row shows the box,
     the project, the asking seat and "12m ago".
   - `"close posts the ruling and shows the request pending"`: with a stubbed `fetch`, submitting a ruling calls
     `POST /api/admin/fabric/calls/close` with `{box, call_id, ruling}` and then renders "PENDING".

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not touch the gateway, Terraform, the manifest, `package.json`,
   `bun.lock`, or the behaviour of any existing page other than Control Plane gaining its two panels. Make no deploy and
   no AWS call.
2. Standing rules: no push and no vendor call. If you cannot meet a criterion as written, REFUSE it with its
   measurement. Never repair a criterion.

## 3. SURFACES

<paths>
mcportal/src/pages/control-plane/**
mcportal/src/pages/open-calls/**
mcportal/src/api/admin.ts
mcportal/src/api/admin.test.ts
mcportal/src/App.tsx
mcportal/src/shell/pages.ts
mcportal/src/shell/sidebar.test.ts
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~11/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `mcportal/src/pages/recent-changes/`, `mcportal/src/pages/mcp-server/`, `mcportal/src/styles/tokens.css`,
`portal/DESIGN.md`, `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W11-S<k>` (the next free k for W11). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED
row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from `C:/tmp/mp-cp2-11` after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-p-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/p2.AC1.sh; echo "exit=$?"</invocation><expect>bun test rc=0; named tests present in sources 5 of 5; pass>=5; fail=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-p-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/p2.AC2.sh; echo "exit=$?"</invocation><expect>build rc=0; dist/index.html=yes; bundle files naming /open-calls>=1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~11/NFRA_MCPORTAL.TO-MP-p-2.control-plane-panels-and-open-calls-page.proof_of_spec.json`.
Report once, with:
- the two check outputs;
- the mcportal commit hash or hashes and the workspace commit hash;
- the built bundle's size;
- any field of the four contracts you could not render as written, and why;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the CP2 issuance (decomposition v6) from PRD v0.5 FWD-15..17, S14, S15 @cecf26d2c9. The mcportal base
d60b4e0 is LOCAL on branch `wk-NFRA_MCPORTAL-r4-6-mcportal`, the commit MP-x-4 releases; mcportal origin DEV is still the
README commit fa1ff96. Provisioned with `wk-provision.sh --nested mcportal=d60b4e0`. Checks dry-run at base 2851a9190d: AC1
FAIL (`src/pages/open-calls` absent), AC2 FAIL (same). No gate. Lives through MP-r-2.

<status>complete</status>
<round>1</round>
<workstream>CP2</workstream>
<slot>~11</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
