# DSGN_AMGTV1 task order -- `AV-g-5` -- NO FACE SAYS "LEAD PANEL", AND THE SELECTED-NAME HEADER IS IN THE CARD FAMILY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-g-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~59</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV 209678ff -- nolabel.cjs 2 of 3 (FAIL as expected: 9 faults -- the four tabs say "Lead Panel", the identity block is not through the card face; arms 2-3 PASS by design); green arm (scratch r16-green-h @2f48ad29, after the issuer's ruling) 3 of 3, packwords/headerread/cardface/reasonwords 3 of 3, tsc 0. Blind spots: static renders; only BA's identity block; the identity card's ink is the L9 read.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-g-5` (round 16, decomposition v16; serves FWD-23, FWD-11)

The CTO's round-15 analysis s.4 row 5 and ruling 5. This order follows AV-g-1 on the same worktree (file-disjoint). Build in `portal/src/pages/SecurityAnalysis/`:
1. **`tabs/ThesisTab.tsx`, `tabs/PeersTab.tsx`, `tabs/PostureTab.tsx`, `tabs/ExecManagementTab.tsx`:** the no-name empty sentence
   says a person's words, e.g. "Pick a name above to open its Thesis." -- 0 "Lead Panel" in any visible text. (`tabs/ModelTab.tsx`
   is AMGT_CORPUS's through the freeze; it already reads "Pick a name above to open its Model." -- do not edit it.)
2. **`components/SecurityOverlay.tsx`:** the selected-name header's identity block (the name, the sector line) renders through the
   shared card face `@/ui/components/graphic/GraphicCard` (a flat div), the name and sector words kept, 0 "Lead Panel".
**Issuer ruling (row AMGT_RESAPP-Z-W200-S1):** the Thesis pillars sentence keeps "no research pack" -- it is the designed worded form
of the served "class A report" (CTO round-13 ruling 1); do NOT change `reasonWords.ts`. **Walker rule (CTO msg 27641):** do NOT run `.claude/skills/ui-walk/walk.mjs` or `ui_walker_account.py arm|disarm|secret` -- the one walker account is shared across two devices; no criterion here needs a walk.

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
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~59/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/`
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-g-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round16/checks/nolabel.cjs"; echo "exit=$?"</invocation><expect>NO INTERNAL NAME, THE NAME HEADER IN THE CARD FAMILY: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-g-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/headerread.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/packwords.cjs"; echo "exit=$?"</invocation><expect>THE HEADER READS ITS NUMBERS: 3 of 3 arms, then THE PACK SENTENCES READ THEIR OWN REASON: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-g-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" G5 drafting.harness.cjs:8 execPattern.harness.cjs:9 execText.harness.cjs peersPattern.harness.cjs:13 shell.harness.cjs:10 errorEmpty.harness.cjs:12; echo "exit=$?"</invocation><expect>G5 BOUND: 6 of 6 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-g-5" judgment="true"/>
</proof_of_spec>

AC1 renders the four tabs with no name selected and BA's IdentityHeader: 0 "Lead Panel", a person's empty sentence, the identity block
through GraphicCard with the name and sector kept; arms 2-3 the negative and planted controls. Seconds. AC2 keeps round 15's header
readings and pack sentences green. AC3 the harness bound. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the walk's BA header and
tab PNGs: the name header reads as one card family with the portal.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~59/DSGN_AMGTV1.TO-AV-g-5.no-internal-name-the-name-header-in-the-card-family.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** analysis s.4 row 5 (ruling 5). Second on chain ~59 (after g-1, file-disjoint). Issuer ruling on row AMGT_RESAPP-Z-W200-S1 (pillars wording kept; nolabel.cjs PILLARS_GRADED off). Green r16-green-h @2f48ad29 3 of 3.

<status>pending</status>
<round>16</round>
<slot>~59</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
