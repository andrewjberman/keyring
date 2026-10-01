# DSGN_AMGTV1 task order -- `AV-i-2` -- THE HEADER'S CHATTER LINE READS THE MONTHLY ROUTE, THE PLURAL CORRECT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-i-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~65</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV c6aacc68 -- headerline.cjs 2 of 3 (FAIL as expected: the footnote prints the legacy "chatter: ranked ... (1 names)" caption and no monthly count; arm 2 the pinned base and arm 3 three planted footnotes PASS by design). Blind spot: static render; the issuer's live walk reads the header PNG.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-i-2` (round 18, decomposition v18; serves FWD-21, FWD-24)

DIRECT ACT. The CTO's msg 27762 (from AMGT_CORPUS ADJUDICATION_v36): the selected-name header's readings line printed "chatter: ranked
October 1st, 2026 (1 names)" -- the legacy chatter ranking, the dead input FWD-21's bubbles replace. Ruled: the line reads the monthly
route, matching the bubble denominator, the plural correct; presentation only (AMGT_RESAPP unchanged). Build:
1. **`portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx`:** in the `[data-axis-footnote]` line, replace the chatter `GenerationCaption` with the monthly
   read (`useCollectedChatter`, already in `hooks/useLeadPanelApi.ts`): "chatter: <k> of <n> covered names collected this month" (k =
   rows with a count in the payload's latest month, n = all rows, the same words as the bubbles' denominator). When the monthly read is
   not served, say nothing about chatter (or that the monthly counts are not available yet) -- never the legacy ranking caption. The
   price part of the line is unchanged.
2. **`portal/src/pages/SecurityAnalysis/components/GenerationCaption.tsx`:** "1 name", never "1 names" (the singular branch for a row count of 1).
Do not run the walker.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served
(the ONE exception the shared CONTRACT s.2 writes: the page orders price bars by the absolute value of the served
`return_30d_pct`). C-FRIDAY -- a served unit prints as served, never rescaled; the page never constructs a date. C-ESTATE-FIXTURES --
estate pieces, colours from `portal/src/lib/chartColors.ts`. **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour law):** a code,
field name or path may sit in a data attribute or in code, never in visible text; no light ink on a white panel. The shared Friday
CONTRACT: `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` (read it).

**Harness changes:** none were found to need it. No harness may change.

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
portal/src/pages/SecurityAnalysis/components/GenerationCaption.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~65/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/`
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-i-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round18/checks/headerline.cjs"; echo "exit=$?"</invocation><expect>THE HEADER CHATTER LINE READS THE MONTHLY ROUTE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-i-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/headerread.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round16/checks/nolabel.cjs"; echo "exit=$?"</invocation><expect>THE HEADER READS ITS NUMBERS: 3 of 3 arms, then NO INTERNAL NAME, THE NAME HEADER IN THE CARD FAMILY: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-i-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" I2 leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>I2 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 renders IdentityHeader on BA's overlay with the monthly read served (the footnote prints "9 of 22 covered names" collected, no legacy
chatter caption, no "1 names") and unserved (no count, no legacy caption), and GenerationCaption at 1 and 32 rows; arm 2 the pinned base
carries the defect; arm 3 planted footnotes. Seconds. AC2 keeps the header readings and the card family. AC3 the harness bound.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~65/DSGN_AMGTV1.TO-AV-i-2.the-header-chatter-line-reads-the-monthly-route.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DIRECT ACT (two files, LOCAL). CTO msg 27762. Base headerline 2 of 3 on DEV c6aacc68. File-disjoint from AV-i-1 (PriceBars.tsx).

<status>pending</status>
<round>18</round>
<slot>~65</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
