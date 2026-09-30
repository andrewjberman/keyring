# DSGN_AMGTV1 task order -- `AV-n-4` -- THE WALKER WAITS FOR A PICKED NAME AND EACH TAB TO FINISH LOADING, SO THE NO-DOSSIER NAME IS WALKED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-n-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~43</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the walker's own account arming is untouched.
comp-adversary: RUN by the issuer at the cut on walk.mjs at CLOUD HEAD -- loadstate.cjs 0 of 3 (FAIL as expected: no waitForLoaded; the pick and every tab shot follow a fixed settle(page, 3000 / 2500); nothing recorded); green arm (a scratch walk.mjs, CHECK_SRC_OVERRIDE) 3 of 3 (4 of 4 behaviour scenarios, ceiling 45,000 ms); round-8 daystate.cjs 3 of 3 and walkerbound.cjs 3 of 3 on the green arm; node --check OK. Blind spot: the live latency is the issuer's walk; walkvoid.sh not re-run on the green arm (the change touches no sign-in or void path).
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-n-4` (round 11, decomposition v11; serves AMGT_CORPUS FWD-10/11/15/16/18 -- the no-dossier arm)

The CTO's ruling (round-10 analysis s.2, cell 4): the walk opens a dossier-less name's Thesis tab. On walk I, 6501 JP (0 dossier
objects) was typed into the search box and submitted, the page issued its `/overlay` read, and every 6501 shot shows "Loading
identity header": in `.claude/skills/ui-walk/walk.mjs` the `--security` loop waits a FIXED `settle(page, 3000)` after the pick and
`settle(page, 2500)` after each tab click, and moved on while the first read was still running. The estate's panel states carry
`data-panel-state` = loading | error | empty | no-permission (`portal/src/ui/components/states/PanelStates.tsx`). Build, in
`walk.mjs` only:
1. A top-level `const LOAD_STATE_CEILING_MS = <n>` with n >= 30000 (the gateway's own limit is about 29 s; 45000 is fine), and a
   top-level `async function waitForLoaded(page)` that polls `page.locator('[data-panel-state="loading"]').count()` and
   `page.locator('[data-panel-state="error"]').count()`, sleeping with `page.waitForTimeout(<n>)` where 0 < n <= 500 and timing with
   `Date.now()`, and returns `{ state: 'loaded' | 'error' | 'ceiling', waited_ms }`: 'loaded' once no loading panel is on the page,
   'error' once an error panel stands and no loading panel does, 'ceiling' when loading never clears.
2. In the `for (const sec of opt.securities)` loop: after the pick (the row click or the search submit) and BEFORE the
   `${sec}-overlay` shot, call `waitForLoaded(page)`; after each tab click and BEFORE the `${sec}-${tab}` shot, call it again.
   Remove the fixed `settle(page, 3000)` / `settle(page, 2500)` between the action and those shots (a short settle of a few hundred
   ms for the click to register is fine).
3. Push every such wait to a top-level `loadStates` array as `{ security: sec, step: 'overlay' | <tab>, state, waited_ms }`, and
   write `load-states.json` to the walk's output folder (`path.join(OUT, 'load-states.json')`) whenever `loadStates.length` is
   non-zero, beside `timeline-days.json`.
Nothing else changes: the pick, thread, day and timeline steps, the sign-in guard and the account arming stay as they are.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue. AC3 reads the 5174 dev build the issuer
   keeps serving; if 5174 does not answer, report AC3 as NOT RUNNABLE and do not start a server.
2. Only the files in `<paths>` change.
3. Never run the walker signed in, never arm the walker account, never run `ui_walker_account.py secret`.

## 3. SURFACES

<paths>
.claude/skills/ui-walk/walk.mjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~43/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/ui/components/states/PanelStates.tsx` and the issuer's checks under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/` and `round8/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 180)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-n-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/checks/loadstate.cjs"; echo "exit=$?"</invocation><expect>WALKER WAITS FOR THE LOAD STATE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-n-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round8/checks/walkerbound.cjs"; echo "exit=$?"</invocation><expect>WALKER BOUND: 3 of 3 checks green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-n-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/checks/walkvoid.sh"; echo "exit=$?"</invocation><expect>SIGNED-OUT CONTROL: the walk FAILS on the sign-in page: YES -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-n-4" judgment="true"/>
</proof_of_spec>

AC1 is the wait's behaviour (nothing loading; loading for 14,000 ms; an error after loading; a HELD read -> "ceiling" at >= 30,000
ms) run on a stub page and a fake clock, plus the wiring and the record read from walk.mjs; AC2 the walker's earlier steps (pick,
thread, day) stay whole; AC3 the signed-out control. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in
walk (a 0-dossier-object name from the census, e.g. 6501 JP), never self-graded: the no-dossier name's header and Thesis tab are
shot loaded, and the Thesis tab shows the served reason the research team's dossier is absent (AMGT_CORPUS FWD-10/11/15/16/18);
`load-states.json` records the state the walker saw for every name and tab.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~43/DSGN_AMGTV1.TO-AV-n-4.the-walker-waits-for-the-load-state.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the outer commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 11 = the round-10 analysis s.2 cell 4 (o-2's unexercised no-dossier arm). Cause measured by an issuer-spawned
read-only research agent: walk.mjs:449 `settle(page, 3000)` after the pick; the /overlay for "6501 JP" was issued and still pending
("Loading identity header" on all seven 6501 steps, findings.json UIW-009), the netlog records responses only. Base: loadstate.cjs 0
of 3; green 3 of 3; daystate 3/3 and walkerbound 3/3 on green.

<status>pending</status>
<round>11</round>
<slot>~43</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
