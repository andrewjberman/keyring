# DSGN_AMGTV1 task order -- `AV-x-1` -- THE IDENTITY CARD SHOWS THE SERVED COMPANY NAME ABOVE THE TICKER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-x-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~67</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV f73cd009 -- namecard.cjs 2 of 3 (FAIL as expected: no data-identity-name element; the ticker-only case and arms 2-3 PASS by design). Blind spot: static render on BA's fixture; the issuer's live walk reads AMD, TSM and BA.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-x-1` (round 20, decomposition v20; serves FWD-23, FWD-24, FWD-1)

DIRECT ACT. The CTO's ruling msg 27874 (on COO~Z 27871: `/security/{key}/overlay` serves top-level `display_name`, never empty, never
the raw key). In `portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx` (`IdentityHeader`'s identity card): show the served top-level `display_name`
above the ticker, in an element carrying `data-identity-name` (e.g. "Advanced Micro Devices Inc" over "AMD US"). If the overlay serves
no `display_name` (absent, null or empty), render the ticker only -- no `data-identity-name` element, never a placeholder ("Unknown",
"N/A", ...). Presentation only: no fetch change, no new route. Use a type the overlay bundle allows (add the optional fields to
`SecurityOverlayBundle` in `portal/src/pages/SecurityAnalysis/types.ts` if the type lacks them). Do not run the walker.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served
(the ONE exception the shared CONTRACT s.2 writes: the page orders price bars by the absolute value of the served
`return_30d_pct`). C-FRIDAY -- a served unit prints as served, never rescaled; the page never constructs a date. C-ESTATE-FIXTURES --
estate pieces, colours from `portal/src/lib/chartColors.ts`. **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour law):** a code,
field name or path may sit in a data attribute or in code, never in visible text; no light ink on a white panel. The shared Friday
CONTRACT: `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` (read it).

**Harness changes:** none. No harness may change.

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
portal/src/pages/SecurityAnalysis/types.ts
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~67/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/`
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-x-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round20/checks/namecard.cjs"; echo "exit=$?"</invocation><expect>THE IDENTITY CARD SHOWS THE SERVED COMPANY NAME: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-x-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round19/checks/chattercell.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round16/checks/nolabel.cjs"; echo "exit=$?"</invocation><expect>THE HEADER CHATTER CELL READS THE MONTHLY COUNT: 3 of 3 arms, then NO INTERNAL NAME, THE NAME HEADER IN THE CARD FAMILY: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-x-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; cd portal &amp;&amp; node node_modules/typescript/bin/tsc -b --noEmit &amp;&amp; cd .. &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" X1 leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>tsc rc 0 (no output), then X1 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 renders IdentityHeader on BA's overlay with display_name "The Boeing Company" (the name element above "BA US") and without it (the
ticker only, no placeholder); arm 2 the pinned base; arm 3 planted cards. Seconds. AC2 keeps the round-19 chatter cell and the card family.
AC3 the TYPECHECK and the harness bound. The CTO's acceptance read is the issuer's live walk: AMD, TSM and BA headers read their company
names (compared on the name field).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~67/DSGN_AMGTV1.TO-AV-x-1.the-identity-card-shows-the-served-company-name.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (one file + optional type, LOCAL). CTO ruling 27874; land by 21:30Z. Base namecard 2 of 3 on DEV f73cd009.

<status>pending</status>
<round>20</round>
<slot>~67</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
