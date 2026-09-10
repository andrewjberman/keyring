# AMGT_RESAPP.TO-AMGT-s-3 -- THE PROVENANCE FACE: source, basis and vintage beside every figure, wired from the records the model block persists -- as a data contract, a validator and the print-path fragment

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-s-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~1</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-3; manifest row S3; verb: wire)

```
AMGT-s-3. THE PROVENANCE FACE -- source, basis and vintage beside every figure, WIRED from the raw and
derived records `AMGT-s-1` persists; never composed from a second read.

FWD-3's bar, verbatim: "An analyst can defend every number on the page in a meeting. DONE WHEN
EXERCISED -- a figure has actually been challenged and answered from the page." The EXERCISED bar is a
person's; this cell makes the answer available beside the number.

WHAT "WIRE" MEANS AT THIS CUT: no page exists and no .tsx may be written until the design spec is
approved (C-DESIGN-SPEC-FIRST; AMGT-s-5 owns the spec). A wire cell in this round delivers the DATA
FACE the page will read and the PRINT-PATH fragment Adam's artifact will carry, both exercised on the
records AMGT-s-1 landed. The .tsx that renders it is a later order after approval.

WHAT TO PRODUCE, under lib/research/provenance/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~1/:

  (a) THE CONTRACT  lib/research/provenance/schema.json -- a JSON Schema for one figure's provenance:
      {source, basis: {mnemonic, definition}, vintage, unit, sign, unit_status, sign_status,
      check_verdict?} -- REQUIRED: source, basis.mnemonic, basis.definition, vintage, unit, sign; every
      *_status from the closed set MEASURED|INFERRED|UNRESOLVED. This is the shape AMGT-s-1's
      model_block.json already carries per figure (its AC5 proved every figure has the six fields);
      the schema NAMES it so a consumer can reject on it.

  (b) THE VALIDATOR  lib/research/provenance/validate.py -- validates a landed model_block.json against
      (a) and prints "PROVENANCE: N figures, N valid, 0 invalid" or the invalid ones by figure id.
      Exercise it on every model_block AMGT-s-1 landed (read them from the store or from that slot's
      deliverables copies).

  (c) THE PRINT-PATH FRAGMENT  lib/research/provenance/render_print.py -- for one figure, the text that
      sits beside the number in Adam's printed pack: "<value> <unit> · <mnemonic> (<definition>) · as of
      <vintage> · Bloomberg" -- and for a figure whose unit_status is not MEASURED, the marker
      "[UNRESOLVED UNIT]" in place of the unit, never a blank and never a silently-dropped row
      (C-MARK-NOT-DEGRADE). Render the full model block for one security to
      .../deliverables/0.9.0_WK_AMGT_RESAPP~1/provenance_render_<security_key>.md.

  (d) THE SPEC SECTION  .../deliverables/0.9.0_WK_AMGT_RESAPP~1/SPEC_SECTION_provenance.md -- the
      page's provenance behaviour in the design-spec vocabulary (what appears on hover / beside the
      figure / in the print), for AMGT-s-5 to fold into DESIGN_SPEC.md. Text, not .tsx.
```

## DEPENDENCIES

`AMGT-s-1` (the records this wires from). Same slot (~1), next in the queue: continue on the same
context after that cell's drain.

## BOUNDS -- what this cell may not cross

```
⛔ C-DESIGN-SPEC-FIRST: NO .tsx, no file under portal/. AC5 refuses one.
⛔ NEVER COMPOSED FROM A SECOND READ: the provenance comes from the record AMGT-s-1 persisted, not from a
fresh Bloomberg call. No DAPI call in this cell at all; AC4 refuses one.
⛔ C-MARK-NOT-DEGRADE: an unresolved unit renders as a marker, never a blank, never a dropped figure.
⛔ C-BLOOMBERG-BASIS: the basis rendered is Bloomberg's mnemonic and definition, verbatim from the record.
⚠ Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
AMGT-s-1's AC5 (landed): every figure carries value, unit, sign, basis, vintage, source. This cell's
    schema is that shape declared; its validator is the consumer that can reject on it.
F4 (CITED, re-measured by AMGT-s-1): units differ across Bloomberg's own field families and may differ
    per security; the render carries the per-security unit the record states.
comp-cache (RUN): 94 distinct keys across 44 portal files, 0 type mismatches -- the later .tsx order
    namespaces under this page; nothing here touches portal/.
comp-schedule (RUN): 25 gates armed, none this project's; G-14 binds AC6.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/provenance/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-3.provenance-face-beside-every-figure.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~1/`. AMGT-s-1's deliverables and the store are READ.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
⛔ REFUSE a criterion you cannot satisfy as written and report the refusal with its measurement; never
repair the criterion, widen it, or satisfy it by a route this order did not name. If you need a
surface that is not listed, file a surprise ROW in the investigation file above and STOP on that
criterion. Your surprise row id is `AMGT_RESAPP-Z-W1-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`,
inside the file's fenced json array; a BLOCKING row is read by the COO in your final report; an
OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-s-3"><invocation>python -m lib.research.provenance.validate org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/model_block_*.json</invocation><expect>for every model block landed by AMGT-s-1, a line "PROVENANCE: N figures, N valid, 0 invalid" with the two N equal and greater than 0 -- the contract is declared and every persisted figure meets it; any "invalid" above 0 is NOT met and the figure ids are recorded</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-s-3"><invocation>python -c "import json; s=json.load(open('lib/research/provenance/schema.json')); r=set(s['required']); print('required', sorted(r), '| status enum', s['properties']['unit_status']['enum'])"</invocation><expect>"required" includes basis, sign, source, unit, vintage (and a nested basis requiring mnemonic and definition, checked by AC1 in practice) and "status enum" is exactly ['INFERRED', 'MEASURED', 'UNRESOLVED'] -- the closed vocabulary a consumer rejects on</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-s-3"><invocation>python -c "import glob,io; fs=glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/provenance_render_*.md'); t=io.open(fs[0],encoding='utf-8').read() if fs else ''; print('renders', len(fs), '| figures rendered', t.count('as of '), '| unresolved markers', t.count('[UNRESOLVED UNIT]'), '| blank units', t.count('  · '))"</invocation><expect>"renders" at least 1, "figures rendered" greater than 0, and "blank units 0" -- every figure line carries its basis and vintage, and an unresolved unit shows as the MARKER, never as an empty gap between separators (C-MARK-NOT-DEGRADE); the unresolved-marker count is recorded, not bounded</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-s-3"><invocation>grep -r -c -i -E 'blpapi|blp_client|ReferenceDataRequest|HistoricalDataRequest|8194' lib/research/provenance/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE: the provenance face is wired from the persisted record and makes no second read of Bloomberg</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-s-3"><invocation>git status --porcelain -- portal/ | grep -c -E '\.tsx$'</invocation><expect>exactly "0" -- NEGATIVE: no .tsx was written; the design spec is not yet approved (C-DESIGN-SPEC-FIRST)</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-s-3" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the contract holds on every landed figure. What FWD-3 leans on.
- **AC2** (mechanical): the vocabulary is closed and named.
- **AC3** (mechanical): the print fragment carries basis and vintage beside every number and marks what it cannot resolve.
- **AC4**, **AC5** (mechanical, NEGATIVE): no second read; no .tsx.
- **AC6** (JUDGMENT -- never self-graded; record its output UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): read one rendered line for a figure whose unit differed between securities in AMGT-s-1's map -- does the line beside the number let an analyst answer "on what basis, as of when" without a spreadsheet?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>2</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5+L6, round 1 issuance, round-2 cell) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L1 brief @19ce7d5b4d -> L2 endpoint @3bc8f5f2c4 -> L4 PRD v0.3 @f68818832b -> L5 decomposition v0.2 @ed25feaee5 -> this issuance.
**Chain:** Q1, second in `AMGT-s-1 -> AMGT-s-3 -> AMGT-s-5`; slot ~1 continues on the same context.
**Provenance:** the cell text is the decomposition's row verbatim. The "wire = data contract + print fragment, .tsx later" reading is the decomposition's s.2c bound (C-DESIGN-SPEC-FIRST) applied to every wire cell of this round; it is stated identically on AMGT-s-7, -9, -10 and -14.
<preflight>
comp-schedule: RUN -- --budget 500 to completion, 5 of 5 carriers, 25 gates armed, none this project's
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; this cell touches no AWS resource
comp-adversary: RUN -- on the L5 decomposition v0.2 at read-vintage @d09e26e1b1; 10 of 10 cited pins VERIFIED
comp-routes: RUN -- 28 CloudFront behaviors; no route touched by this cell
comp-cache: RUN -- 118 of 118 useQuery sites, 94 keys, 0 type mismatches; no portal file touched by this order
comp-find --corpus aws: RUN -- 2382 nodes at 12:24:50Z; this cell reads the store and writes a library
</preflight>

**Preflight disposition:** mandatory core RUN at the L5 vintage. comp-blast DECLARED-NOT-APPLICABLE: a library and deliverables; no deployed resource changes.
