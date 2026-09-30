# DSGN_AMGTV1 task order -- `AV-m-2` -- EVERY LANDED VERSION IS LABELLED WITH ITS DATE AND ITS TIME, SO TWO VERSIONS OF ONE DAY CAN BE TOLD APART

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-m-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~46</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut (read-only invokes).
comp-adversary: RUN by the issuer at the cut on portal DEV 846ecc6c -- versiontime.cjs 0 of 3 (FAIL as expected: BA's 15 versions read "The version of September 10th, 2026" four times; both pickers repeat labels; the what-moved sentence names days only); green arm (scratch r12-green-b @1e87ce6c, an issuer-spawned helper) 3 of 3; modelPattern 12/12, tabs 20/20, shell 10/10 unchanged; bytes 3/3; portal tsc -b rc=0. Blind spot: static markup; the native select's popup is the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-m-2` (round 12, decomposition v12; serves AMGT_RESAPP FWD-6 page half)

The CTO's ruling (round-11 analysis ruling 2): round 11 put the model's landed versions on the Model tab, but BA's compare picker
offers four identical "September 10th, 2026" entries over four served stamps, so the earlier version cannot be named. The remedy is
presentation only: "each version is labelled with its date AND time (UTC) from the served stamp. Where two stamps share a minute,
the seconds are added. No new route; the stamp is already served." A served stamp reads `20260910T224432Z`. Build, in
`portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx` (its `stampWords`) and `portal/src/pages/SecurityAnalysis/dateWords.ts` (a
helper beside `longDate`, if you want one):
1. Every version label = the page's long date, then the stamp's clock in 24-hour UTC: "September 10th, 2026, 22:44 UTC". Where two
   served stamps of the list share a minute, both labels add the seconds: "22:44:32 UTC" and "22:44:59 UTC"; no other label does.
2. The label applies everywhere a version is named: the versions list (`[data-model-version]`), both compare pickers' options, and
   the what-moved sentence ("What moved from the earlier version of <label> to the version of <label>:").
3. Nothing else moves: the served stamps, their order, the compare's defaults and counts, and a stamp the page cannot read ("an
   undated version") stay as they are; no raw stamp in visible text.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing; the time is the served
stamp's own. **Design law (portal `DESIGN.md`):** a code, field name or path may sit in a data attribute or in code, never in
visible text.

**If a bound harness check is anchored on the raw text this cell changes,** re-anchor that ONE check onto the same fact, keep its
claim, never drop it; only a harness named in `<paths>` may be edited. Measured on the green arm, no harness needs a change.

**This slot's next order, `AV-m-3` (FWD-13 on the Model tab and header cards), follows on the same worktree after you finish.**

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c` (they turn a backslash sequence into a
   control byte); AC3 scans for control bytes.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/dateWords.ts
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~46/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md` and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 180)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-m-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/checks/versiontime.cjs"; echo "exit=$?"</invocation><expect>VERSIONS CARRY THEIR TIME: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-m-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/checks/bound.cjs" Q1 modelPattern.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>Q1 BOUND: 3 of 3 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-m-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-m-2" judgment="true"/>
</proof_of_spec>

AC1 is the built Model tab on the SERVED BA /versions (15 stamps, four on September 10th) and /compare, plus a labelled planted
variant with two stamps in one minute: every label carries its date and UTC time, the labels are distinct in the list and both
pickers, the what-moved sentence names both versions with their times, and seconds appear exactly where a minute is shared. AC2 is
the bound on every harness that loads the Model tab; AC3 no control byte in the page's source. AC4 is JUDGMENT, graded by
`3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk (BA's Model tab), never self-graded: a PM can pick and name the earlier
version of a day that holds several (RESAPP FWD-6). Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside
`portal/`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~46/DSGN_AMGTV1.TO-AV-m-2.versions-carry-their-time.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 12 = the round-11 analysis s.4 item 2 with ruling 2. Chained before AV-m-3 on slot ~46 (both write
ModelTab.tsx). Base 846ecc6c: versiontime.cjs 0 of 3; green r12-green-b @1e87ce6c 3 of 3 (25+/10-, dateWords.ts + ModelTab.tsx).

<status>complete</status>
<round>12</round>
<slot>~46</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
