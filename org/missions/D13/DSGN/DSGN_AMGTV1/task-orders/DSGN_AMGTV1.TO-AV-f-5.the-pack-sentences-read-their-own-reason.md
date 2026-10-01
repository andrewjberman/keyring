# DSGN_AMGTV1 task order -- `AV-f-5` -- THESIS AND EXEC SAY ONLY WHAT THEIR OWN SERVED REASON SAYS ABOUT THE RESEARCH PACK

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-f-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~58</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV a41cf763 -- packwords.cjs 1 of 3 (FAIL as expected: BA's Exec reads "no management section in the research pack or the earnings update" -- a pack its served reason says is missing (class A missing); VLO and 992 HK Exec the same; arm 3 the detector control and the served-reason agreement PASS: BA's served pack reasons AGREE, 6 of 6, so no row to the writer); green arm (scratch r15-green-d @86944155, reasonWords.ts +3/-2) 3 of 3, tsc -b rc=0, round-14 reasonwords and modelhistory 3 of 3. Blind spots: only the pillars and management sentences on BA, VLO, 992 HK and 6501 are graded mechanically; the pack words on ThesisCards and the Exec roster are the L9 read.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-f-5` (round 15, decomposition v15; serves FWD-11)

The CTO's round-14 analysis s.3 row 5 as NARROWED by the CTO's amendment (msg 27547: `tabs/ModelTab.tsx` is AMGT_CORPUS's through the
freeze -- DO NOT EDIT IT): the BA pack absent/present split on the Thesis and Exec tabs (ruling 2: each tab's sentence is mapped from its
OWN served reason; the page never reconciles). Measured at the cut: the served reasons agree (no class-A report); the page adds the
presupposition. This order follows AV-f-4 on the same worktree: keep its work whole. Build in `portal/src/pages/SecurityAnalysis/`:
1. **`reasonWords.ts`:** the management sentence keeps the served reason's "missing" -- e.g. "no management section, because neither a
   research pack nor an earnings update is on file for this name" -- never "in the research pack" when the served reason says the pack
   is missing.
2. **`components/ThesisCards.tsx` and `tabs/ExecManagementTab.tsx`:** wherever an empty line says a figure or roster is "not in this
   pack" / "in this name's pack" while its own served reason names no pack (or says the pack is missing), say what the reason says
   instead (e.g. "No officer list has been published for this name yet"). Each sentence stays a function of its own served reason.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served
(the ONE exception the shared CONTRACT s.2 writes: the page orders price bars by the absolute value of the served
`return_30d_pct`). C-FRIDAY -- a served unit prints as served, never rescaled; the page never constructs a date. C-ESTATE-FIXTURES --
estate pieces, colours from `portal/src/lib/chartColors.ts`. **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour law):** a code,
field name or path may sit in a data attribute or in code, never in visible text; no light ink on a white panel. The shared Friday
CONTRACT: `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` (read it).

**Granted harness changes:** none were needed on the green arm. No harness may change.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change. A harness listed in `<paths>` changes ONLY by its granted diff (re-anchor, never a deleted
   check).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c` (a heredoc turns a regex `\b` into a 0x08 byte;
   AC3 scans for it).

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/reasonWords.ts
portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~58/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/`
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-f-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/packwords.cjs"; echo "exit=$?"</invocation><expect>THE PACK SENTENCES READ THEIR OWN REASON: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-f-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/headerread.cjs"; echo "exit=$?"</invocation><expect>THE HEADER READS ITS NUMBERS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-f-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" F5 drafting.harness.cjs:8 execFallback.harness.cjs execPattern.harness.cjs:9 execText.harness.cjs thesisLadder.harness.cjs:10 shell.harness.cjs:10 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>F5 BOUND: 7 of 7 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-f-5" judgment="true"/>
</proof_of_spec>

AC1 renders the Thesis pillars and Exec management sentences on BA, VLO, 992 HK and 6501 from their served /thesis captures: each sentence
claims nothing about the research pack its own served reason does not carry; arm 3 the detector control and the served-reason agreement.
Under 1 second. AC2 keeps AV-f-4's header green on the same worktree. AC3 the harness bound. Run `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/reasonwords.cjs`,
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/execfooter.cjs` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bytes.cjs` too and report their lines. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the
walk's BA Thesis and Exec PNGs: nothing on the two faces contradicts the other about the pack.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~58/DSGN_AMGTV1.TO-AV-f-5.the-pack-sentences-read-their-own-reason.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** analysis s.3 row 5, narrowed by CTO msg 27547 (ModelTab.tsx -> AMGT_CORPUS; the Model-face half moved to CORPUS round 28). Second on chain ~58 (both orders write reasonWords.ts). Base: packwords 1 of 3; green r15-green-d @86944155 3 of 3. The ModelTab pack lines ("No model in the research pack"; team-case "not in this pack") are routed to 2.0.0_SA_COO~X, the writer.

<status>pending</status>
<round>15</round>
<slot>~58</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
