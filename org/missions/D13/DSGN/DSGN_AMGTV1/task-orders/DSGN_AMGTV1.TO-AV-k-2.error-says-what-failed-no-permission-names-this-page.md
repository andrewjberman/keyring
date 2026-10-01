# DSGN_AMGTV1 task order -- `AV-k-2` -- ERROR SAYS WHAT FAILED, NO-PERMISSION NAMES THIS PAGE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-k-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~52</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check renders the page's own components on fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV 118cd005 -- states.cjs 1 of 3 (FAIL as expected: with a forced 503 whose body is a JSON object, 7 of 7 Security surfaces render an error panel and six print the body's braces and quotes on the face, the identity header's error has no what-to-do sentence; the page has no no-permission state of its own; arm 3 is the control -- the shared defaults' bytes -- and passes at base by design); green arm (scratch r14-green-b @8b1ee539, an issuer-spawned helper; 9 files, +87/-11) 3 of 3; bytes 3/3; portal tsc -b rc=0; all 16 page harnesses green; stacked OVER AV-k-1 and AV-k-4 in the issuer's scratch root, all three checks 3 of 3; a green page build rendered with --states-sweep showed no brace on any error face and the new no-permission sentence. Blind spots: colour (navy ink, the danger icon) is CSS; the no-permission state is not reachable from a live route (by decision -- no page under src/ renders PanelNoPermission; its only user is the render script's standalone capture); a hand-made element carrying data-panel-state; error branches other than the forced 503 (INVALID, READ_FAILED).
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-k-2` (round 14, decomposition v14; serves FWD-19 and FWD-11)

The CTO's rulings 2 and 3 (round-13 analysis). This order follows AV-k-1 and AV-k-4 on the same worktree: keep their changes whole.
Build:
1. **ERROR states what failed and what to do, in navy text (DESIGN.md C12.3); the response body never reaches the face.** The shared
   `portal/src/ui/components/states/PanelStates.tsx` `PanelError` gains an option (e.g. `causeAt?: 'face' | 'data'`, default `'face'`, so
   every other page is byte-for-byte unchanged) that carries `cause` in a `data-` attribute (e.g. `data-state-cause`) instead of the
   "Cause: ..." line. Every Security Analysis error site uses it: `tabs/ThesisTab.tsx`, `tabs/PostureTab.tsx`, `tabs/PeersTab.tsx`,
   `tabs/ExecManagementTab.tsx`, `components/RankedList.tsx` and `components/SecurityOverlay.tsx` (the identity header's error also gains
   a what-to-do sentence, e.g. "Try again; if it keeps failing, the research feed is down.").
2. **NO-PERMISSION on this page names this page's object and who grants it (C12.4)**: "You do not have access to this security's
   research. Your firm administrator can grant it." -- each sentence starting in a capital. `PanelNoPermission` takes an optional
   page-specific sentence pair; its default (the "advisor book" wording) stays byte-equal. A new
   `portal/src/pages/SecurityAnalysis/components/ResearchNoPermission.tsx` renders this page's sentence (not wired into a route).
3. **The render script's standalone no-permission capture** (`portal/scripts/ui-contract-check.mjs`) renders `ResearchNoPermission`
   instead of the shared default. Change that capture block only.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing. **Design law (portal
`DESIGN.md`):** a code, field name or path may sit in a data attribute or in code, never in visible text.

**If a bound harness check is anchored on the raw text this cell changes,** re-anchor that ONE check onto the same fact, keep its
claim, never drop it; only a harness named in `<paths>` may be edited. Measured on the green arm, no harness needs a change.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`; AC3 scans for control bytes.

## 3. SURFACES

<paths>
portal/src/ui/components/states/PanelStates.tsx
portal/src/pages/SecurityAnalysis/components/ResearchNoPermission.tsx
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/components/RankedList.tsx
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/scripts/ui-contract-check.mjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~52/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md` (C12) and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 180)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-k-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/states.cjs"; echo "exit=$?"</invocation><expect>ERROR SAYS WHAT FAILED, NO-PERMISSION NAMES THIS PAGE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-k-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bound.cjs" K2 errorEmpty.harness.cjs:12 shell.harness.cjs:10 tabs.harness.cjs:20 peersPattern.harness.cjs:13 peersReadFailed.harness.cjs posture.harness.cjs:32 execPattern.harness.cjs:9 leadPanelPattern.harness.cjs:15; echo "exit=$?"</invocation><expect>K2 BOUND: 8 of 8 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-k-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-k-2" judgment="true"/>
</proof_of_spec>

AC1 renders the seven Security surfaces with a forced 503 whose body is a JSON object (no brace or quote character on the face, the
body whole in its data attribute, a what-failed and a what-to-do sentence), this page's no-permission sentence (this page's object,
each sentence capitalised), and the shared defaults' output byte-equal to the base's. Also keep AV-k-1's and AV-k-4's checks green:
`reasonwords.cjs` and `execfooter.cjs` in the same `round14/checks/` folder must still read 3 of 3 (report their lines). AC2 is the bound on
every harness that loads those surfaces; AC3 no control byte. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's
render-run PNGs (`*-error.png`, `standalone-no-permission.png`), never self-graded: what failed and what to do, no response body, this
page's object named (FWD-19, C12). Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~52/DSGN_AMGTV1.TO-AV-k-2.error-says-what-failed-no-permission-names-this-page.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where (the error and no-permission sentences as they now read), the output line of every criterion (and
reasonwords / execfooter), the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 14 = the round-13 analysis @1e7d4bac11 s.4 item 2 with rulings 2 and 3. Last on chain ~52 (it writes the four
tabs and SecurityOverlay the chain writes). Cross-chain overlap, ruled by the issuer: PeersTab.tsx (one `causeAt` line) and
ui-contract-check.mjs (the standalone no-permission block) are also written by chain ~53 (AV-k-7 -> AV-k-3) in other regions;
merge-tree over the green arms reads 0 conflicts; the issuer merges both at the drain. Measured against the CTO's premise: no page under
src/ renders PanelNoPermission; the "advisor book" default's only user is the render script's capture, so ruling 3's "the shared default
is untouched for the page that owns advisor book" is kept as byte-equal defaults. Base 118cd005: states.cjs 1 of 3; green r14-green-b
@8b1ee539 3 of 3; stacked over k-1 and k-4 3 of 3.

<status>complete</status>
<round>14</round>
<slot>~52</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
