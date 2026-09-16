# TO IRPT_FNTEND.TO-FE-s-49 -- Investor Reporting is Opal-admin only: its route, its print route and its nav item

<to_id>IRPT_FNTEND.TO-FE-s-49</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~2</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F1: route, page identity and navigation entry) | **Decomp cell:** `FE-s-49` (round 8's one added order, v0.8 R8.9 @b6edeb9fc9) | **outcome_ref:** FWD-1, FWD-12 | **depends_on:** none | **slot:** ~2 | **rows:** S66, W2-S34, S67

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-49` -- **Investor Reporting is not Opal-admin gated in the portal. Any signed-in user the firm allowlist passes reaches it, including users of three partner firms.** Andrew made it a condition of his full production deploy (relayed by 0.0.0_AB_MSTR, msg 96903): *"Investor Reporting must remain Opal Admin gated, no clients are allowed to see that."* To 2.0.0_SA_COO~D (msg 96914) he said: *"that page needs to be listed for Opal Admins only in the tsx for that page."* `1.0.0_SA_CTO` ruled this cell into round 8 as its one added order (msgs 96904, 96915 and 96924): **ONE gate, on DEV, with the predicate role admin AND firmId opal-capital, copied byte-for-byte from 2.0.0_SA_COO~D's rendering, and no partner allowlist entry granting what the gate refuses.** It BLOCKS Andrew's full /prod-deploy.

Measured by the issuer at portal DEV 1f3ce9f0 (`git show` at the ref):
- **The routes.** `src/App.tsx:421` `<Route path="/investor-reporting" element={<ProtectedRoute><InvestorReporting /></ProtectedRoute>} />` and `:573` `/investor-reporting/print`, the same shape. Neither carries `requireAdmin` or `requireInternal`.
- **The nav item.** `App.tsx:94` `{ path: '/investor-reporting', label: 'Investor Reporting', icon: FileText },` carries no `requiresAdmin` and no `requiresTier`. `NavItem` (`:63-71`) has `requiresDev`, `requiresAdmin` and `requiresTier`, and no `requiresInternal`.
- **ProtectedRoute** (`src/components/ProtectedRoute.tsx`):
  - `requireAdmin` (`:39-40`) tests `user?.role !== 'admin'` ONLY, and redirects to `/market`.
  - `requireInternal` (`:44-45`) tests `claims?.firmId !== 'opal-capital'`, and redirects to `/market`.
  - `:57` then applies the firm allowlist, `isPathAllowedForFirm`.
- **The allowlist admits three partner firms.** `src/lib/firmAccess.ts` `FIRM_ALLOWED_PATHS` lists `'/investor-reporting'` in the sets for `49financial`, `inflection` and `cottonwood`.
  - So at DEV today, any signed-in user of those firms reaches the page and sees the nav item.
  - `requireAdmin` alone would still admit such a firm's admin.
- **The nav filter** (`App.tsx:305-320`) applies the firm allowlist, then `requiresDev`, then `requiresAdmin` (role), then `requiresTier` through `hasAccess`. `hasAccess('internal')` is `claims.firmId === 'opal-capital'` (`src/contexts/AuthContext.tsx:758-760`).
- **Production.** `origin/PROD`'s `App.tsx` has 0 investor-reporting lines, against 3 at DEV, so the FIRST deploy carrying DEV would expose the page.
- **2.0.0_SA_COO~D's rendering is committed at portal `c29a8b86`** on `feature/d13-visual-elevation` (msg 96928). The same commit carries two unrelated edits, which are not yours. Its THREE GATE HUNKS are what you produce, BYTE-FOR-BYTE, with DEV's indentation, which is the same:
  - the nav item (`:94`) becomes these three lines:
    - `      // Opal Admins only (Andrew-direct 2026-09-15 ~04:4xZ): an admin role AND the internal tier (opal-capital). The`
    - `      // route below carries the same two requirements, so the page is gated where it lives, not only in this list.`
    - `      { path: '/investor-reporting', label: 'Investor Reporting', icon: FileText, requiresAdmin: true, requiresTier: 'internal' },`
  - the route (`:421`): `              <Route path="/investor-reporting" element={<ProtectedRoute requireAdmin requireInternal><InvestorReporting /></ProtectedRoute>} />`
  - the print route (`:573`): `        <Route path="/investor-reporting/print" element={<ProtectedRoute requireAdmin requireInternal><InvestorReportingPrint /></ProtectedRoute>} />`
  - Identical hunks on both branches merge clean, and a hunk that differs, even by the comment, conflicts. Read them yourself with `git show c29a8b86 -- src/App.tsx`; your portal worktree shares the object store.
- **The issuer's probe.** The admin-only change turned 0 tests red in the whole suite: 559 pass, 18 skip, 1 fail of 578. The 1 fail is F41-AC5's control timing out under load, which is FE-s-46's.
  - Every browser-test driver signs in as `role: 'admin'` with `firmId: 'opal-capital'` (fe-s-19, 30, 31, 32 and 40), so the stricter predicate bounces none of them.
  - The probe did NOT include the allowlist change; your whole-suite run decides it (below).
- **The API the page calls** is defined in `src/api/endpoints/investor-reporting.ts`.

**THE REMEDY (the CTO's RULING, 96924):**
- The three gate hunks above, exactly as at `c29a8b86`.
- `'/investor-reporting'` removed from the `49financial`, `inflection` and `cottonwood` sets in `FIRM_ALLOWED_PATHS`, so no allowlist grants what the gate refuses.
  - ~~ONLY if the whole suite stays as green ...~~ **RETIRED BY AMENDMENT 1** (1.0.0_SA_CTO, msg 96961): the first run found the one test that depends on the entries, `fe-s-14/allowlist.test.ts` (row W2-S34), and the CTO ruled that Andrew's word supersedes the partner grant that test encodes. **The removal LANDS, and fe-s-14's F14-AC2 and F14-AC3 are re-pointed** (F49-AC11, F49-AC12).
- Nothing else in `App.tsx` or `firmAccess.ts` changes, and `ProtectedRoute` and `AuthContext` do not change.

### ACCEPTANCE

<criterion id="F49-AC1" cell_refs="FE-s-49" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F49-AC1` -- the whole portal typechecks.

<criterion id="F49-AC2" cell_refs="FE-s-49" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts</invocation><expect>AN OPAL INTERNAL ADMIN REACHES BOTH ROUTES: 2 of 2(?![0-9])</expect></criterion>
`F49-AC2` -- the CTO's first clause.
- For each of the two routes, take the `ProtectedRoute` props from the COMMITTED `App.tsx` (`git cat-file blob HEAD:src/App.tsx`).
- Render the REAL `ProtectedRoute` with those props at that path, under an auth context of `role: 'admin'`, `firmId: 'opal-capital'`. The children render.
- Print each route, its props and the outcome.

<criterion id="F49-AC3" cell_refs="FE-s-49" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts</invocation><expect>A PARTNER-FIRM ADMIN IS REFUSED ON BOTH ROUTES: (\d+) of \1(?![0-9])</expect></criterion>
`F49-AC3` -- the CTO's third arm, on the firms that could reach the page.
- The firms are those whose set listed `'/investor-reporting'` at DEV 1f3ce9f0. Read them from `git cat-file blob 1f3ce9f0:src/lib/firmAccess.ts`, NOT from HEAD, where the entries are gone. Print the denominator (3).
- For each firm and each route, render as `role: 'admin'` with that `firmId`, against the committed HEAD sources.
- The outcome is the redirect `ProtectedRoute` gives a refused user, never the children.

<criterion id="F49-AC4" cell_refs="FE-s-49" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts</invocation><expect>A NON-ADMIN IS REFUSED ON BOTH ROUTES: (\d+) of \1(?![0-9])</expect></criterion>
`F49-AC4` -- the CTO's second and fourth arms, on each route:
- an opal-capital user whose role is not admin;
- a non-admin of each of the 3 firms.
- All are refused.

<criterion id="F49-AC5" cell_refs="FE-s-49" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts</invocation><expect>THE NAV SHOWS INVESTOR REPORTING ONLY TO THE OPAL INTERNAL ADMIN: yes</expect></criterion>
`F49-AC5` -- the nav.
- Run the portal's REAL nav filter predicate (the `App.tsx` filter logic, with the real `isPathAllowedForFirm` and `hasAccess`) over the COMMITTED nav item, for every identity in AC2-AC4.
- Shown for the Opal internal admin only. Print each identity's result.
- If the filter is not importable without mounting the whole app, the test says how it exercises it; re-typing the filter's logic is not allowed.

<criterion id="F49-AC6" cell_refs="FE-s-49" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts</invocation><expect>BEFORE \(DEV 1f3ce9f0\): A PARTNER-FIRM USER REACHED THE PAGE: yes</expect></criterion>
`F49-AC6` -- the arm that can say no. The same render, with the route props and allowlist read from DEV 1f3ce9f0's committed blobs, admits a partner-firm user. Print which.

<criterion id="F49-AC7" cell_refs="FE-s-49" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts</invocation><expect>EVERY INVESTOR REPORTING ROUTE AND NAV ENTRY CARRIES THE OPAL-ADMIN PREDICATE: (\d+) of \1(?![0-9])</expect></criterion>
`F49-AC7` -- the reach, BY SUBTRACTION over the committed `App.tsx`.
- Enumerate every route element and every nav entry whose path starts with `/investor-reporting`, and print the denominator.
- Each carries the predicate.
- Name any other entry point into the page you find, such as a link, with its gate.

<criterion id="F49-AC8" cell_refs="FE-s-49" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts</invocation><expect>THE THREE GATE HUNKS ARE BYTE-IDENTICAL TO 2.0.0_SA_COO~D'S c29a8b86: 3 of 3(?![0-9])</expect></criterion>
`F49-AC8` -- the clean merge.
- Read the `+` lines of the three gate hunks in `git show c29a8b86 -- src/App.tsx` (not the commit's two unrelated edits), and HEAD's committed `App.tsx`.
- Each hunk's added lines appear in HEAD byte-for-byte, in the same order, with the same indentation. Print each pair.

<criterion id="F49-AC9" cell_refs="FE-s-49" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts</invocation><expect>PARTNER ALLOWLIST ENTRIES GRANTING /investor-reporting: 0 of 3 REMAIN(?![0-9])</expect></criterion>
`F49-AC9` -- the CTO's addition. Read from the COMMITTED `firmAccess.ts` at HEAD, and against the 3 firms that listed it at DEV 1f3ce9f0. Print each firm's set membership before and after.

<criterion id="F49-AC10" cell_refs="FE-s-49" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts</invocation><expect>EVERY ENDPOINT INVESTOR REPORTING CALLS HAS A PRINTED ADMIN-ONLY ANSWER: (\d+) of \1(?![0-9])</expect></criterion>
`F49-AC10` -- the backend census the CTO asked for. It is READ-ONLY: measured and printed, not changed.
- Enumerate every endpoint the page calls, from the committed `src/api/endpoints/investor-reporting.ts`, with the denominator.
- For each, read the backend that serves it, wherever it lives in the workspace.
- Print `admin-only: yes | no | UNKNOWN` with the `file:line` it rests on. UNKNOWN counts as an answer only with the files searched printed beside it.
- This tells Andrew whether the UI is the only wall.

<criterion id="F49-AC11" cell_refs="FE-s-49" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-14/allowlist.test.ts</invocation><expect>PARTNER FIRMS REFUSED: 3 of 3(?![0-9])</expect></criterion>
`F49-AC11` -- AMENDMENT 1: fe-s-14's F14-AC2, re-pointed. The three firms it granted (`49financial`, `inflection`, `cottonwood`) are REFUSED by `isPathAllowedForFirm` for `/investor-reporting`, and none of their `FIRM_ALLOWED_PATHS` sets lists it. Print each firm. The internal short-circuit arm stays.

<criterion id="F49-AC12" cell_refs="FE-s-49" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-14/allowlist.test.ts</invocation><expect>FIRMACCESS DIFF: \+0 -3(?![0-9])</expect></criterion>
`F49-AC12` -- AMENDMENT 1: fe-s-14's F14-AC3 diff test, re-pointed to measure the retirement by GIT, against DEV `1f3ce9f0` (the last DEV before this order). Exactly three lines removed and none added in `src/lib/firmAccess.ts`. Its positive control, and its `demo` and unknown-id refusal arm, stay as they are.

<criterion id="F49-AC13" cell_refs="FE-s-49" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts</invocation><expect>THE CENSUS TEST'S TIMEOUT IS 3 TIMES ITS HIGHEST RECORDED COST: yes</expect></criterion>
`F49-AC13` -- AMENDMENT 1: row S67.
- F49-AC10's census test carries an explicit third argument, a timeout, sized under FE-s-46's rule: 3 times the highest recorded cost.
- The recorded costs are committed beside the test: yours, and the issuer's `6703` ms (the cell file alone) and `5938` ms (inside the whole suite), from row S67.
- The bar reads the test's third argument from the COMMITTED blob, and the costs from the committed record. It prints both and the ratio.
- It measures NOTHING at census time: no timing, no load, no cost is recorded by the census run (W1-S74).

<criterion id="F49-AC14" cell_refs="FE-s-49" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F49-AC14` -- **the whole-suite census of record**, with `IRPT_FE_DEV_PORT` exported to a port you have measured closed, run AFTER both the `App.tsx` and `firmAccess.ts` changes. If F41-AC5's control times out under load (FE-s-46's row, not yours), report it and re-run; never edit it.

<criterion id="F49-AC15" cell_refs="FE-s-49" judgment="true" drives="none"/>
`F49-AC15` -- graded at L9: no client or partner-firm user, admin or not, reaches Investor Reporting or sees its nav item through the portal; no allowlist grants what the gate refuses; the three gate hunks match `c29a8b86`; and the backend census says whether the UI is the only wall. RECORD; NO VERDICT.

<expected_criteria>F49-AC1, F49-AC2, F49-AC3, F49-AC4, F49-AC5, F49-AC6, F49-AC7, F49-AC8, F49-AC9, F49-AC10, F49-AC11, F49-AC12, F49-AC13, F49-AC14, F49-AC15</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **`src/App.tsx` IS YOURS FOR THE THREE GATE HUNKS ONLY:** the nav item at `:94` (becoming the two comment lines plus the item), and the route lines at `:421` and `:573`, each byte-identical to `c29a8b86`'s. No other route, nav item, import or line. Paste the diff into the result file.
- ⛔ **`src/lib/firmAccess.ts` IS YOURS FOR THREE LINES ONLY:** the `'/investor-reporting',` entry in the `49financial`, `inflection` and `cottonwood` sets, removed. No other entry, firm, comment or function. Paste the diff.
- ⛔ **NOT YOURS:** `src/components/ProtectedRoute.tsx`, `src/contexts/`, every other page and every other `FIRM_ALLOWED_PATHS` entry, and the `feature/d13-visual-elevation` branch. If the predicate cannot be expressed with the existing props, that is a BLOCKING row.
- ⛔ **ONE PREDICATE, THE CTO'S:** role admin AND firmId opal-capital. No new prop, no new helper, no copy of the check.
- ⛔ **THE WHOLE-SUITE RUN IS THE CENSUS OF RECORD** (F49-AC14). A red test outside your grant is a BLOCKING row with the list, never an edit. ~~If the red test depends on the removed allowlist entries, restore those entries ...~~ RETIRED by amendment 1 for `fe-s-14/allowlist.test.ts` only, which is now yours to re-point. Any OTHER red test is a BLOCKING row, never an edit.
- **No visual change:** the nav item hides for users who may not see it, and nothing about how it looks changes.
- **RULING AC.** Every file your tests inspect is read as the committed blob or tree (`git cat-file blob HEAD:<path>` or `<commit>:<path>`), or the test says why it reads the working copy.
- **The backend census reads, never writes.** It makes no network call and runs no deploy.
- **Servers.** No dev server is needed. Export `IRPT_FE_DEV_PORT` on EVERY `bun test` run to a port you have measured closed (5267 is this slot's). A closed loopback port refuses in about 0.3 to 2 s here, so any probe timeout must exceed 2 s. Sibling slots use 5261, 5263 and 5265; never touch them.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Anchors and evidence.** Counts your tests print are anchorable; each row's `output_evidence` carries the deciding run only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W2-S<k>`, starting at W2-S34. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; an INERT row OMITS the `disarm_owner` key; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- ⛔ **AMENDMENT 1 (2.0.0_SA_COO~F, 2026-09-15 ~07:4xZ; 1.0.0_SA_CTO's ruling, msg 96961, on rows W2-S34 and S67; the order stays pending; three criteria added, none removed).**
  - **What the first run did.** It landed the three gate hunks, byte-identical to `c29a8b86` (portal `61f5c76b`, `640379b8`; they STAY). It REFUSED F49-AC9 exactly as instructed, because `fe-s-14/allowlist.test.ts` asserts the partner entries (W2-S34).
  - **What this seat found** (row S67). On an untouched pair, F49-AC10's census test TIMED OUT at bun's default 5000 ms in 2 runs of 3: `6703` ms alone, and `5938` ms inside the whole suite. Its bar printed "12 of 12" anyway. The test has no timeout sized to its cost.
  - **The CTO's ruling (96961):** "Andrew's word, 'no clients are allowed', supersedes the partner grant that my earlier ruling put into fe-s-14." One respawn carries BOTH:
    - (i) the three `'/investor-reporting',` entries REMOVED from `firmAccess.ts` (F49-AC9 as cut);
    - (ii) the census test's timeout (F49-AC13).
  - ⛔ **`fe-s-14/allowlist.test.ts` IS YOURS FOR THE RE-POINT ONLY.**
    - F14-AC2's two tests assert the three firms are REFUSED (F49-AC11).
    - F14-AC3's diff test measures `+0 -3` against `1f3ce9f0` (F49-AC12).
    - The header comment says the grant was retired, and by whom: Andrew's word relayed in 96903, and the CTO's ruling 96961. "The three firms the CTO's ruling names" must no longer read as current.
    - The `demo` / unknown-id refusal test and the positive control stay unchanged.
  - **`admin-gate.test.ts`:** F49-AC9's before-and-after arm now reads 0 of 3 at HEAD. F49-AC10 gains its timeout, and F49-AC13's bar is added.
  - **Your portal branch now carries portal DEV,** synced before this amendment. That includes FE-s-47 amendment 1 and, if drained by then, FE-s-46 amendment 1. The whole suite may run slower or faster than the first run; F14's tests are now yours, so no other test should depend on the entries.

<paths>
portal/src/App.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-14/allowlist.test.ts
portal/src/lib/firmAccess.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-49/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.8 R8.9 @b6edeb9fc9, cell `FE-s-49`.
<owned_cells>FE-s-49</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F49-AC1` .. `F49-AC15`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-49.investor-reporting-opal-admin-only.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F49-AC1,F49-AC2,F49-AC3,F49-AC4,F49-AC5,F49-AC6,F49-AC7,F49-AC8,F49-AC9,F49-AC10,F49-AC11,F49-AC12,F49-AC13,F49-AC14,F49-AC15 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-49.investor-reporting-opal-admin-only.md` BEFORE the `complete` flip. `F49-AC15` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `investor-reporting-opal-admin-only.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written; the backend census reads code only.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; the CTO ruled this cell into round 8 without an addendum (msgs 96904, 96915, 96924). PRD F1 (route, page identity, navigation entry; FWD-1, FWD-12) names App.tsx as its surface.
the routes and nav: RUN by the issuer at portal DEV 1f3ce9f0 -- App.tsx:421 and :573 <ProtectedRoute> with no requireAdmin/requireInternal; nav :94 no requiresAdmin/requiresTier; NavItem :63-71; nav filter :305-320.
the predicate: RUN -- ProtectedRoute.tsx:39-40 role only, :44-45 firmId opal-capital, :57 firm allowlist; AuthContext.tsx:758-760 hasAccess('internal') = firmId opal-capital.
the allowlist: RUN -- firmAccess.ts FIRM_ALLOWED_PATHS lists /investor-reporting for 49financial, inflection, cottonwood.
the rendering to copy: RUN -- portal c29a8b86 (2.0.0_SA_COO~D, feature/d13-visual-elevation, msg 96928), read with git show c29a8b86 -- src/App.tsx: the nav hunk (2 comment lines + the item) and the two route lines, DEV's indentation.
production: RUN -- origin/PROD App.tsx 0 investor-reporting lines (DEV 3, the positive control).
the reach: RUN -- the issuer's whole-suite probe of the admin-only change, 559/18/1 of 578, the 1 fail the unrelated load timeout; every browser driver signs in as role admin, firmId opal-capital (fe-s-19, 30, 31, 32, 40); the allowlist change is decided by the worker's whole-suite run (the CTO's condition).
lane: the <paths> block IS the grant; three lines in App.tsx and three in firmAccess.ts; ProtectedRoute, contexts, other entries and the d13 branch excluded.
</preflight>

Seating: slot ~2; round 8's one added order -- no dependency edge with FE-s-46, 47 or 48 and no shared file, seated on a fresh worktree pair cut from HEAD with the `<status>` flip committed BEFORE the pair is cut (row S26).
