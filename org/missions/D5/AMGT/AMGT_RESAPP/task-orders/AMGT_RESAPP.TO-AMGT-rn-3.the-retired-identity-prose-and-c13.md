# AMGT_RESAPP task order -- `AMGT-rn-3` -- THE RETIRED IDENTITY'S PROSE AND C13: thirteen sites stop asserting `--bg-band == #0A1733`, and DESIGN.md carries the ratified overflow clause

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rn-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~148</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the round-38 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AMGT-rn-3` (round 39, decomposition s.47)

**Two edits, both text.** (A) Row `AMGT_RESAPP-Z-S251`: the band token was re-pointed (`--bg-band` is `rgb(25,38,67)`; the
header is `#0A1733`), and thirteen sites still assert the OLD equality in comments, docstrings, a README, one smoke instruction and
one literal: `Panel.tsx:8,:47`, `index.css:88,:94`, `designTokens.ts:13`, `ExportModal.tsx:37`, `TicketCenter.tsx:12`,
`Controls.tsx:27,:59,:91`, `HeroGraphic.tsx:27`, `PanelStates.tsx:21`, `panels/README.md:7`, `ui-smoke.mjs:630` (tell the person
to check the HEADER strip, not "the ONE #0A1733 band"), and `PrintExportAction.tsx:136`'s scrim `bg-[rgba(10,23,51,0.6)]`, which
becomes the header token at 60% (an inline `color-mix(in srgb, hsl(var(--bg-header)) 60%, transparent)` or the project's existing
token form -- say which). Correct each sentence to what is true now (band = `--bg-band`, header = `--bg-header`), never delete a
comment that carries other information. NOT touched: `brand.ts`, `brand.tokens.json`, `print.css` (token definitions and IRPT's own
render), `uiMeasureFixture.html` (pins `--bg-header` correctly), `ui-measure.mjs` (its re-keyed comments are correct and it is
another cell's file). (B) `portal/DESIGN.md` gains **C13 verbatim** from
`org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_COMPLETION_20260923/L4R_C13_RATIFIED.md` section 5 (the fenced clause, all five
bullets, after C12, numbered C13); nothing else in DESIGN.md moves.

## 2. BOUNDS

1. **No server.** Your criteria are text and a class census; the render is graded by the issuer after the merge.
2. **Portal is a nested repository** at `<worktree>/portal`, branch `wk-AMGT_RESAPP-148-portal` at DEV `5e339ffd`.
3. No styling changes beyond the scrim's token form; AC3 refuses any. Standing: no install, no push, no promote. REFUSE, do not rescue.

## 3. SURFACES

<paths>
portal/DESIGN.md
portal/scripts/ui-smoke.mjs
portal/src/index.css
portal/src/lib/designTokens.ts
portal/src/pages/InvestorReporting/export/ExportModal.tsx
portal/src/pages/TicketCenter/TicketCenter.tsx
portal/src/ui/components/Controls.tsx
portal/src/ui/components/graphic/HeroGraphic.tsx
portal/src/ui/components/panels/Panel.tsx
portal/src/ui/components/panels/README.md
portal/src/ui/components/states/PanelStates.tsx
portal/src/pages/SecurityAnalysis/components/PrintExportAction.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~148/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rn-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round39/checks/rn-3.AC1.sh; echo "exit=$?"</invocation><expect>outside the allow-list (0): -- an empty list, and exit=0; the allow-listed count printed beside it</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rn-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round39/checks/rn-3.AC2.sh; echo "exit=$?"</invocation><expect>C13 heading + five bullets present: 6 of 6 -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rn-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round39/checks/rn-3.AC3.sh; echo "exit=$?"</invocation><expect>class census IDENTICAL to the baseline -- and exit=0 (no counted weight, radius, shadow or size token moved)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~148/AMGT_RESAPP.TO-AMGT-rn-3.the-retired-identity-prose-and-c13.proof_of_spec.json`.
Report names the scrim's token form chosen, the sites corrected (13 of 13), the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.7 items 4 + 5 consolidated, as the analysis directs; the DESIGN.md writer is a worker under this order (the
lane `POD_DE_ANY` binds by reading; the CTO and this seat are not among its agents). The instrument paragraph the CTO's amendment
three moved out of C13 lands in `ui-measure.mjs`'s docstring under rn-4, that file's owner this round.

<status>pending</status>
<round>39</round>
<slot>~148</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
