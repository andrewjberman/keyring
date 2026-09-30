# DSGN_AMGTV1 task order -- `AV-m-3` -- A PM NEVER PARSES A RAW FLOAT AND CAN STILL DISPUTE ANY FIGURE: HEADER CARDS, WHAT MOVED AND RULE LINES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-m-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~46</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut (read-only invokes).
comp-adversary: RUN by the issuer at the cut on portal DEV 846ecc6c -- figures.cjs 0 of 3 (FAIL as expected: no card figure carries a tooltip; BA's what-moved lines read "Enterprise value: 193510.78009600003 to 187187.819936" and "a line this page has no name for yet: 2.903939 to 3.036011"; 10 numbers with more than 4 fractional digits on the Model tab, incl. "-0.8280000000000001"); green arm (scratch r12-green-b @e19a38e2 over AV-m-2) 3 of 3, versiontime still 3 of 3; modelPattern 12/12 WITH the granted stub line (RED without it); tabs 20/20, shell 10/10, errorEmpty 12/12; bytes 3/3; portal tsc -b rc=0. Blind spots: static markup (hover is the walk's); the check reads the served figures from /overlay while the what-moved lines read the /thesis bundle's copy -- the two agree on today's fixtures.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-m-3` (round 12, decomposition v12; serves FWD-13)

FWD-13: "every figure on the four header cards carries its units and tabular numerals, its tooltip carries the mnemonic and the
full-precision value verbatim, and price, market cap, net debt, enterprise value, beta and short interest each sit on one named
card. ACCEPT: No 161867780096.00003 anywhere; every figure traceable to its field." The CTO's ruling 3: FWD-13 binds EVERY rendered
figure -- header cards, What-moved and rule lines -- and SHORT_INT_RATIO gets its line name from the served field names, never a
page-side dictionary guess. This order follows AV-m-2 on the same worktree; keep its version labels whole. Build, under
`portal/src/pages/SecurityAnalysis/`:
1. **Header cards** (`components/HeaderCards.tsx`): every SERVED figure row of a card window (`HeaderCardDetail`, each
   `[data-card-figure-mnemonic]` row) and each card face's lead figure keeps its tabular numerals and units and gains a hover
   tooltip in the page's StatTile pattern: an element with `role="tooltip"`, `data-figure-tooltip="<MNEMONIC>"` and
   `data-full-value="<the served value, String(value), verbatim>"`, holding the estate `DataTooltip` (header "<label>
   (<MNEMONIC>)", rows incl. the full value and the mnemonic). A shared tooltip component may live in `components/StatTile.tsx`.
2. **What moved** (`tabs/ModelTab.tsx`, `ChangedFigure`): each changed line prints its from and to for reading -- through the
   page's own `formatStatValue` with that mnemonic's format (from `HEADER_CARD_DEFS` / `STAT_TILE_DEFS`) and the served figure's
   unit and currency where the page has them (the /thesis bundle's served header figures carry `unit`, `currency`,
   `basis.definition`), else grouped digits with at most 4 fractional digits -- so no visible number has more than 4 fractional
   digits and no integer of 5+ digits is ungrouped; and carries a tooltip element with `data-figure-tooltip="<MNEMONIC>"`,
   `data-full-from` and `data-full-to` holding String(from) / String(to) verbatim. A line the page's maps do not name takes the
   served header figure's `basis.definition` (e.g. SHORT_INT_RATIO -> "Short interest ratio (days-to-cover)") before the fixed
   phrase.
3. **The rest of the Model tab:** no visible number with more than 4 fractional digits -- e.g. Opal's rule line "forward EPS (FY1)
   is -0.8280000000000001" comes from a served reason: round the numbers IN VISIBLE TEXT and keep the served sentence verbatim in
   a tooltip or data- attribute. The fiscal table's served figures are unchanged.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: rounding a served number
for display is presentation; the full value stays verbatim one hover away; no figure is computed, converted or guessed.
**Design law (portal `DESIGN.md`):** a code, field name or path may sit in a data attribute or in a tooltip FWD-13 names, never in
visible text.

**Harness grant, measured on the issuer's green arm:** ModelTab importing from StatTile brings `@/components/DataTooltip` into
`__harness__/modelPattern.harness.cjs`, which has no stub for it ("Cannot find module '@/components/DataTooltip'"). In its
`const STUBS = {`, after the line `  '@/lib/utils': { cn: (...xs) => xs.filter(Boolean).join(' ') },` add
`  '@/components/DataTooltip': { DataTooltip: () => null },`. Any other bound check anchored on text this cell changes: re-anchor
that ONE check onto the same fact, keep its claim, record old -> new.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`; AC3 scans for control bytes.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx
portal/src/pages/SecurityAnalysis/components/StatTile.tsx
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/constants.ts
portal/src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~46/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md`, `portal/src/components/DataTooltip.tsx`, and the issuer's checks
and fixtures under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 180)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-m-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/checks/figures.cjs"; echo "exit=$?"</invocation><expect>NO RAW FLOAT, EVERY FIGURE TRACEABLE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-m-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/checks/bound.cjs" Q2 modelPattern.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10 errorEmpty.harness.cjs:12; echo "exit=$?"</invocation><expect>Q2 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-m-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-m-3" judgment="true"/>
</proof_of_spec>

AC1 is the built header cards (every card window's served rows and the four faces) on the SERVED BA /overlay, and BA's Model tab
on the SERVED /thesis and /compare (7 changed header figures incl. CUR_MKT_CAP 161867780096.00003): tabular figures, a tooltip with
the mnemonic and the served value verbatim, each named figure on exactly one card; readable what-moved lines, each named (short
interest ratio by its served definition) and traceable; 0 visible numbers with more than 4 fractional digits across the Model tab,
the fiscal table unchanged. AC2 is the bound on every harness that loads the Model tab or the header; AC3 no control byte. Also keep
AV-m-2's check green: `node ".../round12/checks/versiontime.cjs"` must still read 3 of 3 (report its line). AC4 is JUDGMENT, graded
by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk (BA's header and Model tab), never self-graded: a PM never parses a raw
float and can open any figure to its mnemonic and full value (FWD-13). Portal typecheck, if you run one: `node_modules/.bin/tsc -b
--noEmit` inside `portal/`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~46/DSGN_AMGTV1.TO-AV-m-3.no-raw-float-every-figure-traceable.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the harness change (old -> new), the output line of every criterion (and versiontime.cjs), the
portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 12 = the round-11 analysis s.4 item 3 with ruling 3. After AV-m-2 on slot ~46. Base 846ecc6c: figures.cjs 0
of 3; green r12-green-b @e19a38e2 3 of 3 (144+/15-: HeaderCards, StatTile, ModelTab, modelPattern harness). constants.ts granted
defensively (the green arm did not need it).

<status>pending</status>
<round>12</round>
<slot>~46</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
