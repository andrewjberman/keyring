# AMGT_RESAPP.TO-AMGT-s-5 -- THE PRINT RENDERER: the design spec FIRST (the F10 precedent's own gate), then Adam's printed artifact from a pack -- the modal's .tsx HELD on the spec's approval

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-s-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~1</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-5; manifest row S5)

```
AMGT-s-5. THE PRINT RENDERER -- Adam's artifact. FIRST: THE DESIGN SPEC for the Security Analysis
page, in the form the F10 precedent gated ("no .tsx files written until approved"). SECOND, HELD on
that approval: the PDF-in-modal render reproducing the template's four blocks (F1) so the printed
output replaces the circulated document.

FWD-5's bar, verbatim: "Adam forwards a printed pack without reformatting it. DONE WHEN EXERCISED --
Adam has actually forwarded one." That bar is Adam's; this cell produces the artifact he would forward.

TWO DELIVERABLES; THE SECOND'S PORTAL HALF IS HELD:

  (1) THE DESIGN SPEC  .../deliverables/0.9.0_WK_AMGT_RESAPP~1/DESIGN_SPEC.md
      In the form of the estate's precedent: read portal/src/pages/SecurityScanner/DESIGN_SPEC.md
      (F10: 560 lines, gated "no .tsx files written until approved") and follow its section grammar.
      The spec covers the Security Analysis page: the header panel (ticker, company, Bloomberg
      session-state indicator -- PART V says the session's state must be VISIBLE to the user), the
      tabs, and ONE SECTION PER SURFACE S1..S15 saying what the page shows for it, what state it shows
      when the surface is UNRESOLVED / FAILED / HELD BACK (C-MARK-NOT-DEGRADE; C-RULE-MUST-EXIST), and
      what "fetching now" looks like (AMGT-s-2's status object). Fold in the SPEC_SECTION_*.md files
      the wire cells produced (AMGT-s-3 provenance; -7, -9, -10, -14 if landed) verbatim as sections.
      Every displayed number carries its vintage (pre-brief notes s.5). State the print path (2) as a
      section. Close with an APPROVAL block: "Approved by: ____ on ____" left EMPTY -- the approval is
      not this cell's to give.

  (2) ADAM'S ARTIFACT -- the server-side PDF, BUILDABLE NOW; the modal that previews it is .tsx and HELD.
      lib/research/print/render_pack.py: from a pack (AMGT-s-1's model_block.json for one security +
      the provenance fragment from AMGT-s-3 + placeholders for the sections no engine has filled yet,
      each placeholder MARKED as such), produce a PDF that reproduces the template's four blocks in
      order -- the blank template is at
          C:\Users\Opal Bloomberg\OneDrive - Opal Capital\Shared - Documents\Adam\NEW Research Pack Template 2026 03 09_v1.docx
      (READ-ONLY; F1: 11 paragraphs, 3 tables, 1 image; four blocks: the pasted Excel model block /
      RECOMMENDATION + COMPANY DESCRIPTION / THESIS | RISKS / bio) and a filled pack for comparison
      lives in each name folder under Asset Management/Research/. Render ONE pack for one of the
      securities AMGT-s-1 pulled to .../deliverables/0.9.0_WK_AMGT_RESAPP~1/pack_<security_key>.pdf,
      and extract its text to pack_<security_key>.txt for the checks. Use a library `python` already
      has or one the repo already vendors; state which.
```

## DEPENDENCIES

`AMGT-s-1` (the figures) and `AMGT-s-3` (the provenance fragment). Same slot (~1), third in the queue.
The spec folds in whichever SPEC_SECTION files have landed by then; a missing one is noted as a gap in
the spec, never invented.

## BOUNDS -- what this cell may not cross

```
⛔ C-DESIGN-SPEC-FIRST: NO .tsx, NO file under portal/, until the spec's approval block is filled by
someone who is not this worker. AC5 refuses a .tsx. The approval is NOT this cell's to give and NOT
this issuer's: it is left empty and surfaced.
⛔ THE TEMPLATE IS A FLOOR, NOT THE PACK (pre-brief notes s.3.1): the analyst-specific sections are the
value and this project DRAFTS TOWARD them; a render that fills the four blocks and calls the pack done
has reproduced the skeleton. Placeholders are MARKED as machine-empty.
⛔ C-NO-CONTACT: no seat contacts Adam Muller. The artifact is produced; whether he forwards it is his.
⛔ THE CORPUS AND THE TEMPLATE ARE READ-ONLY. Nothing is written into the OneDrive library.
⛔ C-MARK-NOT-DEGRADE: a figure the check face refused, or an engine that has not landed, appears as a
MARKED value or a MARKED placeholder in the print -- never as a blank that looks complete.
⚠ Bound every invocation under `timeout 120`; a PDF render of one pack fits.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
F1 (CITED): template and packs are consistent; provenance confirmed by a shared misspelling
    (CONSDIERATIONS). The four blocks are the print's skeleton.
F10 (CITED): SecurityScanner provides ScannerHeaderPanel, tabs/ on shared useTabNavigation,
    utils/asOf.ts, and a 560-line DESIGN_SPEC.md gated "no .tsx files written until approved".
comp-cache (RUN): 94 distinct keys, 0 type mismatches; the spec names this page's key namespace so the
    later .tsx order does not collide.
comp-routes (RUN): the page rides the /* SPA default; the spec says so and names any new API route
    AMGT-s-2 declared.
comp-schedule (RUN): 25 gates armed, none this project's; G-21 (no device-specific logic in portal)
    binds the later .tsx order and the spec states it.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/print/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-5.print-renderer-design-spec-then-adams-artifact.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~1/`. portal/src/pages/SecurityScanner/DESIGN_SPEC.md,
the template, the corpus and the sibling cells' deliverables are READ. `portal/` is NOT in your write surface.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
⛔ REFUSE a criterion you cannot satisfy as written and report the refusal with its measurement; never
repair the criterion, widen it, or satisfy it by a route this order did not name. If you need a
surface that is not listed, file a surprise ROW in the investigation file above and STOP on that
criterion. Your surprise row id is `AMGT_RESAPP-Z-W1-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`,
inside the file's fenced json array; a BLOCKING row is read by the COO in your final report; an
OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-s-5"><invocation>python -c "import io,re; t=io.open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/DESIGN_SPEC.md',encoding='utf-8').read(); s=[n for n in range(1,16) if re.search(r'(^|\n)#+[^\n]*\bS%d\b' % n, t)]; print('surface sections', len(s), 'of 15 | session-state indicator', bool(re.search('session.state|signed.?out', t, re.I)), '| approval block empty', bool(re.search(r'Approved by:\s*_+', t)))"</invocation><expect>"surface sections 15 of 15 | session-state indicator True | approval block empty True" -- one section per manifest surface, the Bloomberg session state named as visible to the user, and the approval left for someone who is not this worker; fewer than 15 or a filled approval is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-s-5"><invocation>python -c "import glob,io; fs=glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/pack_*.txt'); t=io.open(fs[0],encoding='utf-8').read().upper() if fs else ''; blocks=['RECOMMENDATION','COMPANY DESCRIPTION','THESIS','RISKS']; print('pdf text extracted', bool(fs), '| template blocks present', sum(1 for b in blocks if b in t), 'of', len(blocks), '| machine-empty markers', t.count('[MACHINE-EMPTY'))"</invocation><expect>"pdf text extracted True | template blocks present 4 of 4" with a machine-empty marker count of 1 or greater -- the printed artifact reproduces the template's four blocks in the text a reader can extract, and the sections no engine has filled are MARKED rather than blank; fewer than 4 blocks is a skeleton that does not match the circulated document and is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-s-5"><invocation>python -c "import glob,io; fs=glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/pack_*.txt'); t=io.open(fs[0],encoding='utf-8').read() if fs else ''; print('figures with vintage in print', t.count('as of '), '| bloomberg basis lines', t.count('Bloomberg'))"</invocation><expect>"figures with vintage in print" greater than 0 and "bloomberg basis lines" greater than 0 -- the provenance fragment from AMGT-s-3 reaches the printed page beside the numbers (FWD-3 on paper); 0 of either means the print dropped the provenance and is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-s-5"><invocation>python -c "import glob,os; fs=glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/pack_*.pdf'); print('pdfs', len(fs), '| bytes', [os.path.getsize(f) for f in fs])"</invocation><expect>"pdfs 1" with a byte size greater than 10000 -- one real PDF for one security, not an empty file; a 0-byte or missing PDF is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-s-5"><invocation>git status --porcelain -- portal/ | grep -c -E '\.(tsx|ts|css)$'</invocation><expect>exactly "0" -- NEGATIVE: no portal source was written; the spec's approval block is empty and C-DESIGN-SPEC-FIRST holds</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-s-5" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical, a census): the spec covers every surface, names the session state, and leaves the approval to a person.
- **AC2** (mechanical): the four blocks are in the printed text; the empty sections are marked.
- **AC3** (mechanical): provenance survives into print.
- **AC4** (mechanical): a real PDF exists.
- **AC5** (mechanical, NEGATIVE): no .tsx. The F10 gate, in one line.
- **AC6** (JUDGMENT -- never self-graded; record its output UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): put the rendered PDF beside a filled pack from the same name's folder in the corpus -- would Adam forward this one unreformatted, or does it read as a screenshot of a dashboard? And does the spec say, for every surface, what the page shows when that surface is NOT there?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>3</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5+L6, round 1 issuance, round-3 cell) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L1 brief @19ce7d5b4d -> L2 endpoint @3bc8f5f2c4 -> L4 PRD v0.3 @f68818832b -> L5 decomposition v0.2 @ed25feaee5 -> this issuance.
**Chain:** Q1, third in `AMGT-s-1 -> AMGT-s-3 -> AMGT-s-5`; slot ~1 continues on the same context.
**HOLD, NAMED (decomposition s.9):** the modal's .tsx phase is HELD on the design spec's approval. The approval is not this issuer's to give and no agent-made gate is minted here: the spec's approval block is left empty and SURFACED to Andrew in the drain-end read; whoever fills it, the next order writes the .tsx.
**Provenance:** the cell text is the decomposition's row verbatim. The server-side PDF is cut NOW because a print artifact is not a portal component: C-DESIGN-SPEC-FIRST gates .tsx, and Adam's artifact is the PDF, not the modal that previews it.
<preflight>
comp-schedule: RUN -- --budget 500 to completion, 5 of 5 carriers, 25 gates armed, none this project's; G-21 stated in the spec for the later .tsx order
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; this cell touches no AWS resource
comp-adversary: RUN -- on the L5 decomposition v0.2 at read-vintage @d09e26e1b1; 10 of 10 cited pins VERIFIED
comp-routes: RUN -- 28 CloudFront behaviors; the page rides the /* SPA default, stated in the spec
comp-cache: RUN -- 118 of 118 useQuery sites, 94 keys, 0 type mismatches; the spec names this page's key namespace
comp-find --corpus aws: RUN -- 2382 nodes at 12:24:50Z; this cell reads the store and the corpus and writes a library and a PDF
</preflight>

**Preflight disposition:** mandatory core RUN at the L5 vintage. comp-blast DECLARED-NOT-APPLICABLE: a spec document, a library and a PDF; no deployed resource changes. comp-transform DECLARED-NOT-APPLICABLE until the .tsx order exists.
