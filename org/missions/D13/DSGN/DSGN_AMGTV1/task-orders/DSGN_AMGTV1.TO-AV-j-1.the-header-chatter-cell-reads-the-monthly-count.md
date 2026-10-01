# DSGN_AMGTV1 task order -- `AV-j-1` -- THE HEADER'S CHATTER CELL READS THE NAME'S COLLECTED COUNT THIS MONTH

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-j-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~66</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV 4c02f293 -- chattercell.cjs 2 of 3 (FAIL as expected: no data-header-reading="chatter" cell; the base prints "#1 | 0/100"; arms 2-3 PASS by design). round15 headerread.cjs grades this cell's legacy rank and score -- its chatter clause is RETIRED by the CTO ruling 27768 and it is not a criterion here (its breakout clause is carried by the live walk).
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-j-1` (round 19, decomposition v19; serves FWD-21, FWD-24)

DIRECT ACT. The CTO's ruling msg 27768: the selected-name header's chatter cell reads the legacy ranking point ("TRENDING (CHATTER) #1 |
0/100" -- the dead input, read as "no chatter"). In `portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx` (`IdentityHeader`):
1. The chatter cell carries `data-header-reading="chatter"` and shows the selected name's collected count for the latest month of the
   monthly payload (`useCollectedChatter`, the same read as the bubbles; the row whose `security_key` is this name's): e.g. "Collected this
   month: 20". When the name has no count in that month: ONE designed sentence with the word "collected" and no number (e.g. "No articles
   collected for this name this month."). When the monthly read is not served: no count (a designed sentence or nothing).
2. No legacy ranking read on the face: never "#<rank>", never "/100", never "Trending" in that cell; the label is a person's words (e.g.
   "Chatter (this month)"). The Breakout (price) cell and the footnote are unchanged.
Use the payload as react-query returns it (`query.data`); do not add a second unwrapping. Do not run the walker.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served
(the ONE exception the shared CONTRACT s.2 writes: the page orders price bars by the absolute value of the served
`return_30d_pct`). C-FRIDAY -- a served unit prints as served, never rescaled; the page never constructs a date. C-ESTATE-FIXTURES --
estate pieces, colours from `portal/src/lib/chartColors.ts`. **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour law):** a code,
field name or path may sit in a data attribute or in code, never in visible text; no light ink on a white panel. The shared Friday
CONTRACT: `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` (read it).

**Harness changes:** a harness that asserts the legacy chatter rank text may be re-anchored to `data-header-reading="chatter"` (the same cell, re-anchor only).

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change. A harness listed in `<paths>` changes ONLY by its granted diff (re-anchor, never a deleted
   check).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c` (a heredoc turns a regex `\b` into a 0x08 byte;
   AC3 scans for it).

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/__harness__/shell.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~66/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/`
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-j-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round19/checks/chattercell.cjs"; echo "exit=$?"</invocation><expect>THE HEADER CHATTER CELL READS THE MONTHLY COUNT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-j-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round18/checks/headerline.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round16/checks/nolabel.cjs"; echo "exit=$?"</invocation><expect>THE HEADER CHATTER LINE READS THE MONTHLY ROUTE: 3 of 3 arms, then NO INTERNAL NAME, THE NAME HEADER IN THE CARD FAMILY: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-j-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; cd portal &amp;&amp; node node_modules/typescript/bin/tsc -b --noEmit &amp;&amp; cd .. &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" J1 leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>tsc rc 0 (no output), then J1 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 renders IdentityHeader on BA's overlay with the monthly payload where BA has 20 collected this month (the cell prints 20 and
"collected"), where BA has none this month (one designed sentence, no number), and unserved; no "#", "/100" or "Trending" in the cell;
arm 2 the pinned base; arm 3 planted cells. AC2 keeps the round-18 footnote and the card family. AC3 is the TYPECHECK (`tsc -b`; the
round-18 drain caught a type error no criterion saw) plus the harness bound.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~66/DSGN_AMGTV1.TO-AV-j-1.the-header-chatter-cell-reads-the-monthly-count.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (one file, LOCAL). CTO ruling 27768. Base chattercell 2 of 3 on DEV 4c02f293. headerread.cjs chatter clause retired.

<status>complete</status>
<round>19</round>
<slot>~66</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
