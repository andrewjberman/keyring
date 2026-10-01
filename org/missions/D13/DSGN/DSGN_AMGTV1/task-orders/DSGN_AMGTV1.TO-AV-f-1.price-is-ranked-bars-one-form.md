# DSGN_AMGTV1 task order -- `AV-f-1` -- PRICE IS RANKED HORIZONTAL BARS, AND THE PANEL HAS ONE FORM PER SUBJECT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-f-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~56</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV a41cf763 -- pricebars.cjs 2 of 3 (FAIL as expected: 0 bars for 32 served rows, a View toggle, a Movement control and the list table on the price face; arm 2 the negative on b336b141 and arm 3 six planted mutants PASS by design); green arm (scratch r15-green-a @7cb92a05, an issuer-spawned helper) 3 of 3, tsc -b rc=0, the four granted harnesses green. Blind spots: hooks are stubbed, so the live read limit is not graded by the check (the cell text requires the full universe); bar length and colour and the cursor click are not measured by a static render (the L9 read); loading/error/empty faces of the bars are not graded.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-f-1` (round 15, decomposition v15; serves FWD-22, FWD-18, FWD-2)

The CTO's round-14 analysis @950ae4bb4f s.3 row 1 (PRD v0.6 FWD-22; placement rulings R3, R5, R6): price is ranked horizontal
bars, chatter and price each have ONE form, Trending only through the demo. Build in `portal/src/pages/SecurityAnalysis/`:
1. **`components/PriceBars.tsx` (new):** one horizontal bar per served row, the measure the served `return_30d_pct` (signed percent; the
   field is typed on `PriceRankingRow` at DEV a41cf763), ordered by its ABSOLUTE value, longest first (CONTRACT s.2), the sign shown by
   colour from `lib/chartColors.ts` (no hex in the file), each bar labelled with the company name (or the served ticker when no name is
   served) and its value printed as served with sign and "%" (e.g. "+9.2%", "-25.0%"). Each bar carries `data-price-bar="<security_key>"`.
   A row with no served `return_30d_pct` renders no bar and is counted in one plain sentence under the chart. Reuse the horizontal-bar
   idiom of `portal/src/**/RSIBars.tsx` (~202). Clicking a bar selects the security exactly as a row click does today.
2. **`components/LeadPanel.tsx`:** subject Price renders PriceBars. REMOVE from the render: the List/Chart view `Segmented` (and the
   `RankedChart` line chart behind it), the Movement `Segmented` (movement is TRENDING only through the demo), and the `RankedList`
   table on the price face. "Starred only" filters the bars (no list). Keep the chatter face as it is in this order (the next order on
   your slot replaces it). Leave the props the shell passes compiling (unused props may stay typed).
3. **The read:** the price bars read the WHOLE served universe of the trending price ranking (the served list is about 95 names), not
   the head the list view used (`RANK_SERIES_TOP_N` / any row limit in `hooks/useLeadPanelApi.ts`): a biggest faller ranked last by the
   server must appear. Change only the limit argument of the existing read.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served
(the ONE exception the shared CONTRACT s.2 writes: the page orders price bars by the absolute value of the served
`return_30d_pct`). C-FRIDAY -- a served unit prints as served, never rescaled; the page never constructs a date. C-ESTATE-FIXTURES --
estate pieces, colours from `portal/src/lib/chartColors.ts`. **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour law):** a code,
field name or path may sit in a data attribute or in code, never in visible text; no light ink on a white panel. The shared Friday
CONTRACT: `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` (read it).

**Granted harness changes (exact, tested on the green arm):** `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/fixtures/r15a.grant.{leadPanelPattern,errorEmpty,tabs,shell}.harness.cjs.diff`
-- Movement and View graded as absent, the row checks read `RankedList` directly, a hook stub. Apply each with `git -C portal apply`.
No other harness may change.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change. A harness listed in `<paths>` changes ONLY by its granted diff (re-anchor, never a deleted
   check).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c` (a heredoc turns a regex `\b` into a 0x08 byte;
   AC3 scans for it).

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/PriceBars.tsx
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/hooks/useLeadPanelApi.ts
portal/src/pages/SecurityAnalysis/constants.ts
portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/shell.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~56/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/`
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-f-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/pricebars.cjs"; echo "exit=$?"</invocation><expect>PRICE IS RANKED BARS, ONE FORM: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-f-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" F1 leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>F1 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-f-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-f-1" judgment="true"/>
</proof_of_spec>

AC1 renders LeadPanel on the served trending price ranking with `return_30d_pct` (fixture `r15a.rankings.TRENDING_PRICE.return30d.json`, 32
rows, the largest move a faller listed last): one `data-price-bar` per row in descending |value|, each value as served with its sign and
"%", each labelled; 0 line chart, 0 View toggle, 0 Movement control, 0 list table. Arm 2 is the negative on the b336b141 page and arm 3
the planted mutants (both pass by design). About 3 seconds. AC2 the bound on the four harnesses that load the panel (with the grants);
AC3 no control byte. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's close-render PNG of the price face, never
self-graded: a PM reads the biggest mover first and the sign of each move, and the panel reads as one design family with the portal.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~56/DSGN_AMGTV1.TO-AV-f-1.price-is-ranked-bars-one-form.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 15 = the round-14 analysis @950ae4bb4f s.3 row 1, CTO amendment msg 27547 (cells 1-4 unchanged). Leads chain ~56 (f-1 -> f-2 -> f-3; all three write LeadPanel.tsx). The served-field types were landed by the issuer at DEV a41cf763 before the cut (green arms a and c conflicted in types.ts). Base a41cf763: pricebars 2 of 3; green r15-green-a @7cb92a05 3 of 3.

<status>complete</status>
<round>15</round>
<slot>~56</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
