# DSGN_AMGTV1 task order -- `AV-f-2` -- CHATTER IS ONE BUBBLE PER SECURITY, SIZED BY THE MONTH IT IS STEPPED TO

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-f-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~56</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV a41cf763 -- bubbles.cjs 2 of 3 (FAIL as expected: no ChatterBubbles.tsx, no bubbles in LeadPanel; arm 2 the negative on b336b141 and arm 3 four planted mutants PASS by design); green arm (scratch r15-green-a @7cb92a05) 3 of 3, tsc -b rc=0. Blind spots: the cursor buttons are not clicked (stepMonth is graded as a function); bubble layout is not measured by a static render (the L9 read); the live route answers only once AMGT_RESAPP serves it (until then the face must be the designed empty state, not graded here).
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-f-2` (round 15, decomposition v15; serves FWD-21)

The CTO's round-14 analysis s.3 row 2 (PRD v0.6 FWD-21; rulings R4, R5; CONTRACT s.1 and s.6). This order follows AV-f-1 on the
same worktree: keep its work whole. Build in `portal/src/pages/SecurityAnalysis/`:
1. **`components/ChatterBubbles.tsx` (new):** an exported pure `ChatterBubbles({ data, month })` over the CONTRACT s.1 payload
   (`CollectedChatterSet`, typed at DEV a41cf763): one bubble per row that HAS that month in `by_month` (an absent month draws no bubble),
   the bubble's AREA proportional to `collected` (radius ~ sqrt), each bubble an SVG `circle` carrying `data-chatter-bubble="<security_key>"`,
   `data-collected="<n>"` and its radius; the company `display_name` on or beside each bubble; the caption reads "articles collected"
   (never "market chatter"); a month listed in `partial_months` says it is partial in words. Export a pure month-cursor helper
   `stepMonth(months, month, delta)` and render a cursor (this month, M-1, M-2, ... and back) that flips client-side with no fetch per step.
   Reuse the size-scaled scatter idiom of `portal/src/**/InflectionInsightsPanel.tsx` (~476-563) and `motion` for the transition; colours
   from `lib/chartColors.ts`.
2. **`hooks/useLeadPanelApi.ts`:** `useCollectedChatter()` reading the already-mounted template
   `GET /api/scoped/amgt/lead-panel/timeseries/collected/chatter` (CONTRACT s.1: the template is mounted; AMGT_RESAPP serves this
   movement/subject). Add the one client call in `portal/src/api/endpoints/amgt-lead-panel.ts` (an existing endpoints file). Any answer
   that is not the s.1 shape renders the designed empty/error state in words (no fixture data at runtime, ever).
3. **`components/LeadPanel.tsx`:** subject Chatter renders ChatterBubbles and NOTHING else (no list, no line chart, no toggle). The footer
   under the bubbles names the source in words ("Articles collected per month, from the harvest") and the served `as_of`.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served
(the ONE exception the shared CONTRACT s.2 writes: the page orders price bars by the absolute value of the served
`return_30d_pct`). C-FRIDAY -- a served unit prints as served, never rescaled; the page never constructs a date. C-ESTATE-FIXTURES --
estate pieces, colours from `portal/src/lib/chartColors.ts`. **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour law):** a code,
field name or path may sit in a data attribute or in code, never in visible text; no light ink on a white panel. The shared Friday
CONTRACT: `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` (read it).

**Granted harness changes:** the same four harness files as AV-f-1 (`leadPanelPattern`, `errorEmpty`, `tabs`, `shell`), ONLY to keep the
claims they make with the chatter face replaced (re-anchor; the green arm's combined diffs under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/fixtures/r15a.grant.*.diff`
already cover both orders). No other harness may change.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change. A harness listed in `<paths>` changes ONLY by its granted diff (re-anchor, never a deleted
   check).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c` (a heredoc turns a regex `\b` into a 0x08 byte;
   AC3 scans for it).

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/ChatterBubbles.tsx
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/hooks/useLeadPanelApi.ts
portal/src/api/endpoints/amgt-lead-panel.ts
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
  <criterion id="AC1" cell_refs="AV-f-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bubbles.cjs"; echo "exit=$?"</invocation><expect>CHATTER IS BUBBLES BY MONTH: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-f-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/pricebars.cjs"; echo "exit=$?"</invocation><expect>PRICE IS RANKED BARS, ONE FORM: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-f-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" F2 leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>F2 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-f-2" judgment="true"/>
</proof_of_spec>

AC1 renders ChatterBubbles on the CONTRACT s.1 fixture `r15a.collected.chatter.json` (12 rows, 2026-05..2026-10, 2026-10 partial) for the
latest month and M-1: one bubble per row with that month, area ~ count (2%), a size change between the two months, the partial month in
words, the caption "articles collected", and LeadPanel's chatter face is bubbles only; arms 2-3 the negative and the planted mutants.
AC2 keeps AV-f-1's bars green on the same worktree. AC3 the harness bound. (Run `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bytes.cjs` too and report its line.) AC4 is
JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the close-render PNG of the chatter face: a PM says which names were collected most this
month, steps back two months and says what changed.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~56/DSGN_AMGTV1.TO-AV-f-2.chatter-is-bubbles-by-month.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** analysis s.3 row 2. Second on chain ~56. Issuer ruling: the client call to the mounted template is added now (CONTRACT s.1 names the template as already mounted), so no separate wiring cell is needed when RESAPP serves collected/chatter; until then the face is the designed empty state. Base: bubbles 2 of 3; green 3 of 3.

<status>pending</status>
<round>15</round>
<slot>~56</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
