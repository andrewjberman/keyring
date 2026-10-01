# DSGN_AMGTV1 task order -- `AV-g-2` -- THE HEADER CARDS FILL THEIR GRID, AND EVERY EYEBROW MEETS C1 AND C3

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-g-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~60</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV 209678ff -- headerchrome.cjs (FAIL as expected: sizes 10px and lowContrast in all six states; header-card widths 137/195/86/169; arm 3 the /philosophy byte-identity control); green arm (scratch r16-green-e @ea7b0a9b) 3 of 3 (11px, 0 lowContrast in six states, four cards 317.5px), cardface/panelhead/headerread 3 of 3, tsc 0. Blind spots: layout measured at 1440 and 1024 only; contrast by the instrument's own rule.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-g-2` (round 16, decomposition v16; serves FWD-23, FWD-20)

The CTO's round-15 analysis s.4 row 2 and ruling 4 (the round-15 close render: `sizes` FAIL 10px and `lowContrastChars` FAIL in all six
states; the four header cards at uneven widths, "MARKET FEATURES" over its icon). Build in `portal/src/pages/SecurityAnalysis/components/` -- NOT in
`portal/src/ui/components/graphic/GraphicCard.tsx` (/philosophy must stay byte-identical; round15 cardface.cjs grades it):
1. **`HeaderCards.tsx`:** the four selected-name header cards each fill their grid column at equal widths (within 2px), the eyebrow
   never overlaps its icon and is never clipped, the eyebrow is >= 11px (C1), and its ink passes contrast on the card's navy face (C3,
   C5): give the navy panel a solid background colour under its image so contrast is graded against navy, not the white base.
2. **`LeadPanel.tsx`:** the panel header's eyebrow the same (>= 11px, contrast PASS). Change only the header's chrome.
**Walker rule (CTO msg 27641):** do NOT run `.claude/skills/ui-walk/walk.mjs` or `ui_walker_account.py arm|disarm|secret` -- the one walker account is shared across two devices; no criterion here needs a walk.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served
(the ONE exception the shared CONTRACT s.2 writes: the page orders price bars by the absolute value of the served
`return_30d_pct`). C-FRIDAY -- a served unit prints as served, never rescaled; the page never constructs a date. C-ESTATE-FIXTURES --
estate pieces, colours from `portal/src/lib/chartColors.ts`. **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour law):** a code,
field name or path may sit in a data attribute or in code, never in visible text; no light ink on a white panel. The shared Friday
CONTRACT: `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` (read it).

**Harness changes:** none were needed on the green arm. No harness may change.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change. A harness listed in `<paths>` changes ONLY by its granted diff (re-anchor, never a deleted
   check).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c` (a heredoc turns a regex `\b` into a 0x08 byte;
   AC3 scans for it).

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~60/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/`
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-g-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round16/checks/headerchrome.cjs"; echo "exit=$?"</invocation><expect>THE HEADER CHROME MEETS C1 AND C3: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-g-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/cardface.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/panelhead.cjs"; echo "exit=$?"</invocation><expect>THE HEADER CARDS ARE THE PHILOSOPHY CARD FACE: 3 of 3 arms, then THE LEAD PANEL HEADER LOOKS LIKE THE PORTAL: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-g-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" G2 leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>G2 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-g-2" judgment="true"/>
</proof_of_spec>

AC1 builds the page from your worktree (vite), runs the render instrument with `--states-sweep` and requires `sizes` and `lowContrastChars`
PASS in all six states, then measures the four `[data-header-card]` boxes at 1440 and 1024 wide (equal within 2px, filling their cells,
eyebrow and icon disjoint, eyebrow not clipped); arm 2 the base build fails; arm 3 /philosophy byte-identical. About 10 minutes. AC2
keeps the card face and the panel header green. AC3 the harness bound (`tabs.harness.cjs` needs the workspace `lib/` -- your outer
worktree has it). AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the close-render PNGs beside /philosophy.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~60/DSGN_AMGTV1.TO-AV-g-2.the-header-chrome-meets-c1-and-c3.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** analysis s.4 row 2 (ruling 4). Leads chain ~60 (g-2 -> g-4; both write LeadPanel.tsx). Green r16-green-e @ea7b0a9b 3 of 3 (write set HeaderCards.tsx + LeadPanel.tsx).

<status>complete</status>
<round>16</round>
<slot>~60</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
