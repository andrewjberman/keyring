# DSGN_AMGTV1 task order -- `AV-g-4` -- THE CHATTER FACE IS A DESIGNED SENTENCE UNTIL THE MONTHLY ROUTE IS SERVED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-g-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~60</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV 209678ff -- unavailable.cjs 2 of 3 (FAIL as expected: "Read failure" and the ranking SourceCaption under the unserved chatter face; arm 2 the negative and arm 3 the planted controls PASS by design). Green arm (scratch r16-green-g) in progress at the cut. Blind spots: hooks are stubbed, so the route wiring after RESAPP round 57 is graded by the close walk, not here; contrast and placement are the L9 read.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-g-4` (round 16, decomposition v16; serves FWD-21, FWD-19)

The CTO's round-15 analysis s.4 row 4 and ruling 3 (CONTRACT s.4: a designed state, never a raw failure). This order follows AV-g-2 on the
same worktree: keep its work whole. THE CONTRACT (quoted from `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round16/checks/unavailable.cjs`): LeadPanel on subject CHATTER, when the monthly
collected-articles read (`useCollectedChatter`) is NOT SERVED -- the read FAILED (an HTTP 404 or 500), or it answered a payload that is
not the CONTRACT s.1 shape -- shows the estate's designed empty state (`PanelEmpty` from `@/ui/components/states`) carrying ONE
plain-words sentence that the monthly counts are not available yet (it names "month" -- monthly / per month -- and says "not available
yet" or "not yet available"; it is the state's only sentence: no detail, no hint, no cause). The face shows NO "Read failure", NO
"UNKNOWN", no PanelError, no status token, no HTTP code, no text of the read's error, no raw code, and NO ranking SourceCaption under it.
Served (the s.1 shape), the face is the bubbles as round 15 built them. The route wiring is already in (AV-f-2's client call to the
mounted template): when AMGT_RESAPP round 57 deploys the route, the same face reads it with no change. Build in
`portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx` (its chatter face) and, if needed, `ChatterBubbles.tsx`. **Walker rule (CTO msg 27641):** do NOT run `.claude/skills/ui-walk/walk.mjs` or `ui_walker_account.py arm|disarm|secret` -- the one walker account is shared across two devices; no criterion here needs a walk.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served
(the ONE exception the shared CONTRACT s.2 writes: the page orders price bars by the absolute value of the served
`return_30d_pct`). C-FRIDAY -- a served unit prints as served, never rescaled; the page never constructs a date. C-ESTATE-FIXTURES --
estate pieces, colours from `portal/src/lib/chartColors.ts`. **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour law):** a code,
field name or path may sit in a data attribute or in code, never in visible text; no light ink on a white panel. The shared Friday
CONTRACT: `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` (read it).

**Harness changes (ISSUER AMENDMENT 1):** `errorEmpty`, `tabs` and `leadPanelPattern` may change ONLY to re-anchor a claim about the chatter face's ranking caption (ruling 3 removes it): the green arm (r16-green-g @9cea7642) moved their caption renders to the Price face -- the same fact.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change. A harness listed in `<paths>` changes ONLY by its granted diff (re-anchor, never a deleted
   check).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c` (a heredoc turns a regex `\b` into a 0x08 byte;
   AC3 scans for it).

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/components/ChatterBubbles.tsx
portal/src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~60/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/`
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-g-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round16/checks/unavailable.cjs"; echo "exit=$?"</invocation><expect>THE CHATTER FACE IS DESIGNED WHEN UNSERVED: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-g-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bubbles.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round16/checks/headerchrome.cjs"; echo "exit=$?"</invocation><expect>CHATTER IS BUBBLES BY MONTH: 3 of 3 arms, then THE HEADER CHROME MEETS C1 AND C3: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-g-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" G4 leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>G4 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-g-4" judgment="true"/>
</proof_of_spec>

AC1 renders LeadPanel on Chatter five unserved ways (FAILED 404, FAILED 500, the ranking payload, {}, {"message":"Not Found"}) and once
served: each unserved face is ONE designed sentence with nothing of the failure and no SourceCaption; the served face is 9 bubbles and "9
of 22 covered names"; arms 2-3 the negative and planted controls. AC2 keeps the bubbles and AV-g-2's header chrome green (about 10
minutes). AC3 the harness bound. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the walk's chatter PNG before the deploy: a person
reads a designed sentence, not a failure.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~60/DSGN_AMGTV1.TO-AV-g-4.the-chatter-face-is-designed-when-unserved.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** AMENDED before hand-over (leadPanelPattern added to the write surface; helper G's green arm r16-green-g @9cea7642 unavailable 3 of 3; graded on modification by to-pipeline-gate GATE viii only).  analysis s.4 row 4 (ruling 3). Second on chain ~60 (LeadPanel.tsx). Base unavailable 2 of 3.

<status>complete</status>
<round>16</round>
<slot>~60</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
