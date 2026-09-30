# DSGN_AMGTV1 task order -- `AV-n-5` -- THE MODEL TAB SHOWS THE MODEL'S LANDED VERSIONS AND WHAT MOVED BETWEEN TWO, NAMING THE EARLIER ONE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-n-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~44</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call from the page build; the fixtures are the issuer's read-only captures at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 2bb60cc3 -- versions.cjs 0 of 3 (FAIL as expected: no versions surface, no caller of /versions or /compare); green arm 3 of 3 (13 versions newest first; oldest -> newest compare 212 added / 0 removed / 7 changed / 172 unchanged); ALL 16 of 16 harnesses on the green arm with the two named harness lines below; portal tsc -b rc=0; 0 control bytes. Blind spot: static markup with the estate chrome stubbed; the selects' interaction is the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-n-5` (round 11, decomposition v11; serves AMGT_RESAPP FWD-6)

AMGT_RESAPP FWD-6 (its PRD :469-474): "An analyst returns to a company researched before and can say what moved, naming the earlier
version that shows it. Refreshing adds a version; it does not overwrite the old one." AMGT_RESAPP's round-51 ruling 1 routes the page
surface to this project; the deployed scoped API already serves both routes and the portal has no caller:
- `GET /api/scoped/amgt/security/{key}/versions` -> `{ security_key, prefix, versions: [{stamp, object_key}] (newest LAST, stamps like
  "20260929T024521Z"), denominators: {versions, objects_listed}, latest, read: {status SERVED|ABSENT|READ_FAILED, reason, ...},
  identity }`;
- `GET /api/scoped/amgt/security/{key}/compare?from=<stamp>&to=<stamp>` -> `{ available_stamps, compared: {from_stamp, to_stamp,
  added[figure-id], removed[figure-id], changed[{figure, mnemonic, fiscal_year, scope, from, to}]} | null, reason, denominators:
  {versions, figures_from, figures_to, added, removed, changed, unchanged}, read, identity }` (a figure id is
  "scope|fiscal_year|mnemonic"; with fewer than two stamps `compared` is null and `reason` says why).
Build (C-PRESENTATION-ONLY -- from those served routes only):
1. **Client + hooks:** in `portal/src/api/endpoints/amgt-lead-panel.ts`, calls following its
   `${BASE}/security/${encodeURIComponent(securityKey)}/<leaf>` convention (compare with a `from` / `to` query string); query keys in
   `portal/src/pages/SecurityAnalysis/constants.ts` (`AMGT_QUERY_KEYS`); response types in `portal/src/pages/SecurityAnalysis/types.ts`
   (TYPES ONLY there -- no runtime value exported from types.ts); hooks `useModelVersions(securityKey)` and
   `useModelCompare(securityKey, from, to)` in `portal/src/pages/SecurityAnalysis/hooks/useLeadPanelApi.ts` (the useQuery shape of
   `useThesisBundle`; the compare runs only once both stamps are set).
2. **The versions surface, INLINE in `tabs/ModelTab.tsx`** (no new module), on `[data-model-versions]`: every landed version NEWEST
   FIRST on `[data-model-version="<stamp>"]`, each dated in the long form with the page's `dateWords.ts` helpers (no raw stamp in
   visible text); a read that is not SERVED reads one designed sentence (no status token).
3. **The compare, on `[data-model-compare]`:** by default from = the OLDEST landed stamp and to = the NEWEST (two plain selects let
   the PM choose); it states the served counts ("212 figures added, 0 removed, 7 changed, 172 unchanged"), names the earlier
   version's date in the long form, and lists each changed figure with its line name and its served from and to values. A line is
   named from the served `model.line_names` first, then the page's own label maps (the Model sheet's line names, the header-card and
   stat-tile labels); a line with no name reads "a line this page has no name for yet" -- never a raw mnemonic. When `compared` is
   null it shows the served reason.
4. **No raw mnemonic anywhere on the Model tab:** the served case reasons can carry mnemonic tokens (BA's base case reads "forward
   EPS (FY1 BEST_EPS) ..."). `caseAbsenceWords` strips them with the page's existing `formulaInWords` and closes the brackets left
   behind; the full served reason keeps riding `data-model-case-reason`.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: no figure is computed,
converted or guessed, no name is looked up or joined beyond the page's own label maps, and a value the payload does not carry reads
as a designed empty state. **Design law (portal `DESIGN.md`):** a code, field name, key or path may sit in a data attribute or in
code, never in visible text; white panels, navy ink, one dark band per page.

**If a bound harness check is anchored on the raw text this cell changes,** re-anchor that ONE check onto the same fact as the page
now states it, keep its claim, never drop it; only a harness named in `<paths>` may be edited. Measured on the green arm, the
required change NECESSARILY breaks exactly these two (their stub of `hooks/useLeadPanelApi` names only the hooks they already use;
each fails "useModelVersions is not a function"), each granted with its exact change:
- `modelPattern.harness.cjs` (line ~79, the `useLeadPanelApi` loader stub): add
  `useModelVersions: () => ({ data: undefined, isLoading: false, isError: false }), useModelCompare: () => ({ data: undefined,
  isLoading: false, isError: false })` beside `useThesisBundle` in the returned object.
- `tabs.harness.cjs` (`SOURCE_STUBS['src/pages/SecurityAnalysis/hooks/useLeadPanelApi.ts']`, after
  `useCoverageSet: () => ({ data: undefined, isLoading: false }),`): add
  `useModelVersions: () => ({ data: undefined, isLoading: false }), useModelCompare: () => ({ data: undefined, isLoading: false }),`.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc; AC3 scans for control bytes.
5. This slot's next order, AV-n-6 (the input ledger), follows on the same worktree after you finish; do not start it.

## 3. SURFACES

<paths>
portal/src/api/endpoints/amgt-lead-panel.ts
portal/src/pages/SecurityAnalysis/constants.ts
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/hooks/useLeadPanelApi.ts
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~44/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `lib/research/api/scoped_amgt.py` (the /versions and /compare builders, :4047 and
:4094), `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` (FWD-6), `portal/src/pages/SecurityAnalysis/dateWords.ts`,
`portal/src/pages/SecurityAnalysis/modelSheet.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 180)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-n-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/checks/versions.cjs"; echo "exit=$?"</invocation><expect>VERSIONS AND WHAT MOVED: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-n-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/checks/bound.cjs" Q5 modelPattern.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10 errorEmpty.harness.cjs:12; echo "exit=$?"</invocation><expect>Q5 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-n-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-n-5" judgment="true"/>
</proof_of_spec>

AC1 is the built surface on the SERVED BA US /thesis, /versions (13 stamps) and oldest -> newest /compare, plus labelled variants (a
null compare with its reason; a READ_FAILED versions read); AC2 the bound on every harness that loads the Model tab or the page
around it; AC3 no control byte in the page's source. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in
walk (BA's Model tab), never self-graded: an analyst returning to the name can say what moved and name the earlier version that shows
it (RESAPP FWD-6). Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~44/DSGN_AMGTV1.TO-AV-n-5.versions-and-what-moved.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each harness change (old -> new), the output line of every criterion, the portal and outer
commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 11 = the round-10 analysis s.4 item 5 (RESAPP round-51 ruling 1). Chain ~44: n-5 then n-6 (shared write set:
ModelTab, types, constants, hooks, the endpoint file). Base 2bb60cc3: versions.cjs 0 of 3; the green arm (issuer scratch r11-green-b
by an issuer-spawned helper agent, merged over r11-green-a) 3 of 3; ALL 16 of 16 with the two stub lines; tsc rc=0. The
caseAbsenceWords mnemonic strip was found by the green arm (BA's served base-case reason carries BEST_EPS).

<status>pending</status>
<round>11</round>
<slot>~44</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
