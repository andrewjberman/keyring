# DSGN_AMGTV1 task order -- `AV-q-1` -- THE WALKER WAITS FOR THE OPENED DAY'S STATE, NOT FOR TIME

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-q-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~29</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read walk.mjs and run its extracted wait against a stub page.
comp-adversary: RUN by the issuer at the cut on walk.mjs @4a0628755b (portal DEV ab7e1e49) -- daystate.cjs 0 of 3 (FAIL as expected: no waitForDayState, every day and event shot follows settle(page, 1500), timeline-days.json written only under --day); green arm 3 of 3 (ceiling 20000 ms; the held route reads "ceiling"); walkerbound.cjs 3 of 3 at base and on the green arm; walkvoid.sh YES at base (5174 serving). Blind spot: the wait runs against a stub page and a fake clock; the live day latency is the issuer's walk.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-q-1` (round 8, decomposition v8; serves AMGT_HARVST FWD-5 and FWD-6)

The CTO's ruling (round-7 analysis, ruling 1): the walker shoots an opened day 1,500 ms after the press, while the deployed
`/timeline/day` answers in ~5.5 s for a day with articles -- so every opened day was shot as a skeleton. The walker waits for the
day's STATE, not for time. The panel (`portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx`, read-only) already marks
all three states under the opened day's container `[data-timeline-selected-day="<date>"]`: rows
`[data-timeline-dissection="SERVED"] [data-timeline-article]`, empty `[data-timeline-day-empty]`, failed
`[data-timeline-dissection="FAILED"]`. Build, in `.claude/skills/ui-walk/walk.mjs`:
1. A top-level `const DAY_STATE_CEILING_MS = <n>` with n >= 15000, and a top-level `async function waitForDayState(page, date)`
   that polls `page.locator(<selector>).count()` for the three states above (each selector prefixed by the date's container),
   sleeps between polls with `page.waitForTimeout(<ms>)` where 0 < ms <= 500, times with `Date.now()`, and returns
   `{ state: 'rows' | 'empty' | 'failed', waited_ms }` on the first state seen, or `{ state: 'ceiling', waited_ms }` when the
   ceiling passes with none -- a held route never reads as rows.
2. Every opened day waits for its state before its shot, with no `settle(page, 1500)` between the press and the
   `checks(page, ...)` shot: the `--day` step (the function pressing `[data-day-bar="${date}"]`), and in `walkTimeline` the
   newest-day press (read the pressed bar's `data-day-bar` date) and the event open (the first day of
   `data-timeline-event="<first>..<last>"`). The `--day` step reads article rows only when the state is `'rows'`.
3. Every opened day is recorded: `timelineDays.push({...})` with `via: 'day'` (the --day step, keeping security, date, pressed,
   article_rows_in_page_order), `via: 'newest'` and `via: 'event'`, each carrying `state` and `waited_ms`; `timeline-days.json` is
   written whenever `timelineDays.length` is non-zero (not only under `--day`). A 'ceiling' is its own recorded result, never a shot
   graded as rows.
One paragraph in `.claude/skills/ui-walk/SKILL.md`: the state wait, its ceiling, and the `via` / `state` / `waited_ms` fields of
`timeline-days.json`. No panel file changes (the attributes are already served).

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: no figure is computed,
converted or guessed, no name is looked up or joined, and a value the payload does not carry reads as a designed empty state
naming, in plain words, what is missing and which team fills it -- never a project code, serial or storage path.
C-ESTATE-FIXTURES -- windows are the estate's HeroDialog + DialogStamp, panels and states are the estate's; nothing forked.
**Design law (portal `DESIGN.md`):** white panels with navy ink (C3); ONE dark band per page; no translucent white (C5.8); no
shadow (C11). A code, field name or path may sit in a data attribute or in code, never in visible text -- and text inside a
collapsed `<details>` is still visible text.

**If a bound check is anchored on the raw text this cell removes,** re-anchor that ONE check onto the same fact as the walker now
states it, keep its claim, never drop it. The three walker checks in AC2 read `--thread`, `--day`, the legend pick and the timeline
steps: keep each step's existing marker text (the `--day` press, `timeline-days.json`, `timeline:day-not-found`) so no re-anchor is
needed -- measured on the green arm, all three green unchanged. The issuer's checks are never edited.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue. AC3 reads the 5174 dev build the issuer
   keeps serving, signed OUT; if 5174 does not answer, report that line as the result -- never start a server.
2. Only the files in `<paths>` change; every other page, component, tab, harness and skill file is unchanged.
3. Never run the walker signed in; never arm, disarm or read the secret of the walker account.

## 3. SURFACES

<paths>
.claude/skills/ui-walk/walk.mjs
.claude/skills/ui-walk/SKILL.md
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~29/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx` (the three state
attributes), `.claude/skills/ui-walk/signin_detect.mjs`, `.claude/skills/ui-walk/ui_walker_account.py` (never run it), and the
issuer's checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round8/` and the earlier rounds' checks AC2 runs
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-q-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round8/checks/daystate.cjs"; echo "exit=$?"</invocation><expect>WALKER WAITS FOR DAY STATE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-q-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round8/checks/walkerbound.cjs"; echo "exit=$?"</invocation><expect>WALKER BOUND: 3 of 3 checks green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-q-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round8/checks/walkvoid.sh"; echo "exit=$?"</invocation><expect>SIGNED-OUT CONTROL: the walk FAILS on the sign-in page: YES -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-q-1" judgment="true"/>
</proof_of_spec>

AC1 is the wait's behaviour (rows at once; rows after 6,000 ms; empty; failed; a HELD route -> "ceiling" at >= 15,000 ms) run on a
stub page and a fake clock, plus the wiring and the record read from walk.mjs; AC2 the walker's earlier steps (pick, thread, day)
stay whole; AC3 the signed-out control. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in re-walk
(`--day "992 HK=2026-08-13"` plus one event open), never self-graded: the opened day's shot shows its articles strongest first, not
a skeleton, and `timeline-days.json` records the state the walker saw for every opened day (AMGT_HARVST FWD-5, FWD-6).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~29/DSGN_AMGTV1.TO-AV-q-1.the-walker-waits-for-the-day-state.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the outer commit hash,
and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 8 = the round-7 analysis s.4 item 1 with ruling 1 (ruling 3 grades FWD-6's last clause on the same re-walk).
Base walk.mjs @4a0628755b: daystate.cjs 0 of 3; green (scratch walk.mjs, ceiling 20000) 3 of 3; walkerbound 3 of 3 at base and green;
walkvoid YES at base (not run on the green arm: the green change touches no sign-in or void path).

<status>pending</status>
<round>8</round>
<slot>~29</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
