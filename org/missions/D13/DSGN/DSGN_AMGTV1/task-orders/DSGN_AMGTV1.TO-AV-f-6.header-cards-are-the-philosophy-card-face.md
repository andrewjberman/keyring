# DSGN_AMGTV1 task order -- `AV-f-6` -- THE SELECTED-NAME HEADER CARDS ARE THE /PHILOSOPHY CARD FACE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-f-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~57</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; every check renders page sources statically from fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV a41cf763 -- cardface.cjs 0 of 3 (FAIL as expected: no shared module, 4 of 4 header cards not through the card face, no module to mutate); green arm (scratch r15-green-b @69653d85) 3 of 3 (/philosophy row 14540 B byte-identical before and after), tsc -b rc=0. Blind spots: static render only (no dialog-open state); the design-law read of white cards inside the band is the L9 read.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-f-6` (round 15, decomposition v15; serves FWD-23)

The CTO's round-14 analysis s.3 row 3, the header half (PRD v0.6 FWD-23; C-ESTATE-FIXTURES: a needed piece that lives inline in another
page is EXTRACTED into a shared module, and that page renders byte-identically before and after). Build:
1. **`portal/src/ui/components/graphic/GraphicCard.tsx` (new), exporting `GraphicCard`:** the card face that
   `portal/src/pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx` (~183-214, with `HeroGraphic.tsx`) renders inline today,
   extracted whole. `PhilosophyPillars.tsx` renders through it, and the /philosophy card row's static markup is BYTE-IDENTICAL before and
   after (`CapitalMarketAssumptions.tsx:122` mounts it).
2. **`portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx`:** each of the four selected-name header cards renders through `GraphicCard` (keep
   `data-header-card` on each card), with the words each card shows today kept, and no raw code in visible text. Colours from
   `lib/chartColors.ts` and the card face; no hex. Do NOT edit `LeadPanel.tsx` (another order on another slot writes it).

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing it is not served
(the ONE exception the shared CONTRACT s.2 writes: the page orders price bars by the absolute value of the served
`return_30d_pct`). C-FRIDAY -- a served unit prints as served, never rescaled; the page never constructs a date. C-ESTATE-FIXTURES --
estate pieces, colours from `portal/src/lib/chartColors.ts`. **Design law (portal `DESIGN.md`, portal `CLAUDE.md` colour law):** a code,
field name or path may sit in a data attribute or in code, never in visible text; no light ink on a white panel. The shared Friday
CONTRACT: `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` (read it).

**Granted harness changes (exact, tested on the green arm):** `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/fixtures/r15b.grant.{errorEmpty,posture,shell,tabs}.harness.cjs.diff`
-- each adds a structural stub for the new `GraphicCard` module (and `PanelEyebrow`). Apply each with `git -C portal apply`. No other
harness may change.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change. A harness listed in `<paths>` changes ONLY by its granted diff (re-anchor, never a deleted
   check).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c` (a heredoc turns a regex `\b` into a 0x08 byte;
   AC3 scans for it).

## 3. SURFACES

<paths>
portal/src/ui/components/graphic/GraphicCard.tsx
portal/src/pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx
portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx
portal/src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/posture.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/shell.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~57/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/` and `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/`
(never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-f-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/cardface.cjs"; echo "exit=$?"</invocation><expect>THE HEADER CARDS ARE THE PHILOSOPHY CARD FACE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-f-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bound.cjs" F6 errorEmpty.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>F6 BOUND: 3 of 3 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-f-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-f-6" judgment="true"/>
</proof_of_spec>

AC1: arm 1 renders the /philosophy card row from the b336b141 sources and from your checkout and compares the static markup byte for
byte (and requires PhilosophyPillars to import the shared module); arm 2 renders HeaderCards on BA's served overlay: four cards, each
through the card face, words kept, raw code 0; arm 3 the controls (the base cards fail; a planted mutant of the module breaks
byte-identity). About 2 seconds. AC2 the harness bound (posture.harness.cjs reads S3 live and is excluded; apply its grant anyway); AC3
no control byte. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the close-render PNG beside /philosophy: a reviewer reads the same
card family.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~57/DSGN_AMGTV1.TO-AV-f-6.header-cards-are-the-philosophy-card-face.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** analysis s.3 row 3, header half; the issuer split row 3 into this order (extraction + HeaderCards, no LeadPanel) and AV-f-3 (the panel header, chained on ~56 after this chain drains) so the extraction runs beside the bars. Chain ~57 alone. Base: cardface 0 of 3; green r15-green-b @69653d85 3 of 3.

<status>pending</status>
<round>15</round>
<slot>~57</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
