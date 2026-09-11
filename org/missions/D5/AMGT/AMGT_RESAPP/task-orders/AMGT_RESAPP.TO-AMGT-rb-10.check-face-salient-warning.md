# AMGT_RESAPP.TO-AMGT-rb-10 -- THE CHECK-FACE SALIENT WARNING, IN THE READING: a PROVISIONAL/REFUSE figure leads with a salient status marker so it is unmistakable at a glance, never a second trailing word on a number-first line

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rb-10</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~3</issued_to>

## THE CELL, INLINED IN FULL (round 2b, FWD-10; fixes AMGT-r-10 / finding C-S12 FAIL)

```
AMGT-rb-10. THE CHECK-FACE SALIENT WARNING, IN THE READING. AMGT-r-10 (round 2) tried to fix AMGT-s-10's
AC6 by APPENDING a second trailing text tag: `12345 [PROVISIONAL]` became `12345 [PROVISIONAL] [WARN]`.
The CVO graded it FAIL (C-S12): that is another plain suffix word on the SAME number-FIRST presentation
round 1 already rejected -- render_print.py appends the icon as bracketed text and never renders a leading
status or the colour_token, so a fast reader still hits the number first and it still skims as "a number,
fine". And the round-2 test compared DIFFERENT values (500 vs 12345), so string-inequality never proved
the marker made the difference. The token contract (green/OK, amber/WARN, red/BLOCKED) is sound and is
PRESERVED; only the READING is unfixed.

WHAT TO PRODUCE, under lib/research/checkface/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~3/:

  (a) THE SALIENT RENDER  make render_value (lib/research/checkface/render_print.py) put the status marker
      FIRST for a REFUSE and a PROVISIONAL figure -- a LEADING ASCII status token drawn from the closed
      contract (e.g. `[WARN]` for PROVISIONAL, `[BLOCKED]` for REFUSE) BEFORE the value, so the reader's
      eye reaches the warning before the number. A PASS figure still renders its bare value (PASS staying
      unmarked is what makes a warned row a genuine departure). The value is never dropped or zeroed
      (C-MARK-NOT-DEGRADE); count in == count out. NO non-ASCII -- no glyph/emoji; a leading ASCII token
      IS the print-path equivalent of visual prominence.

  (b) THE DIFFERENCE ARM, SAME NUMBER  a fixture and a test that render the SAME figure value (one number,
      e.g. 12345) under PASS and under PROVISIONAL (and under REFUSE), and assert the PROVISIONAL/REFUSE
      render LEADS with a status marker (its first visible character is not the value's digit) while the
      PASS render is the bare value. Varying ONLY the verdict, never the number, is the whole point -- the
      round-2 test's 500-vs-12345 comparison is exactly what proved nothing.

  (c) THE SPEC SECTION  update SPEC_SECTION_checkface.md so the design spec names the LEADING salient
      marker per verdict "at a glance" (the ASCII token the print path uses now and the colour_token the
      later .tsx will bind), and that a refused/provisional value is reachable but never presented as
      trusted or read-first. Text, not .tsx.
```

## DEPENDENCIES

**NONE.** Independent of the other round-2b cells. Reads AMGT-s-10's landed check_face fixtures and
AMGT-r-10's landed render_print.py / markers.py (both landed at HEAD).

## BOUNDS

```
BLOCK C-DESIGN-SPEC-FIRST: NO .tsx, no file under portal/. The salient render is a DATA + PRINT + SPEC
  artifact the later .tsx reads; AC3 refuses a .tsx.
BLOCK NO NON-ASCII in production code/logs: the leading status marker is an ASCII token (OK/WARN/BLOCKED
  or a bracketed word), never a glyph or emoji; AC4 refuses a non-ASCII render_print.py.
BLOCK C-MARK-NOT-DEGRADE: a marker is added, never a figure dropped or zeroed; count in == count out.
BLOCK THE DIFFERENCE ARM MUST VARY ONLY THE VERDICT: the fixture holds the number FIXED and varies PASS
  vs PROVISIONAL vs REFUSE; a test comparing two different numbers does not meet AC1/AC2.
BLOCK THE MARKER SET STAYS CLOSED AND DISTINCT PER VERDICT (green/OK, amber/WARN, red/BLOCKED); preserved
  from AMGT-r-10, carried into the eventual approved design.
WARN Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
CVO evidence @b3acbcf3dd (C-S12, BLOCKING): "the rendered fixture changes 12345 [PROVISIONAL] to 12345
    [PROVISIONAL] [WARN], adding another plain suffix word to the same number-first presentation previously
    rejected. There is still no rendered color, warning glyph, leading status, or equivalent change in
    visual prominence. The test compares different values (500 versus 12345), so string inequality does not
    prove a marker makes the difference ... no .tsx is required to demonstrate a salient print fixture."
L10 round-2 analysis @c48576bf85 s.2: "a visibly salient warning in the permitted print fixture (no .tsx
    needed -- S5's render_print.py), comparing the SAME number under PASS vs PROVISIONAL; regrade AC4."
AMGT-r-10 (landed): render_print.py render_value appends marker.get('icon') as trailing bracket text and
    never renders colour_token; markers.py is the closed distinct-per-verdict set; C-MARK-NOT-DEGRADE.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/checkface/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rb-10.check-face-salient-warning.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~3/`. AMGT-s-10's and AMGT-r-10's deliverables
are READ. A path missing from that block is a path you are REFUSED on. Refuse a criterion you cannot
satisfy as written and report it; file a surprise ROW (`AMGT_RESAPP-Z-W3-S<k>` continuing your prior
sequence -- your next is `AMGT_RESAPP-Z-W3-S6`, project AMGT_RESAPP, fabric site-z) and STOP on that
criterion if you need a surface not listed.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rb-10"><invocation>python -m pytest lib/research/checkface/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning with a passed count and no "failed" -- AMGT-r-10's tests still pass PLUS a new SAME-NUMBER salience test: it renders one fixed value under PASS and under PROVISIONAL (and REFUSE) and asserts the PROVISIONAL/REFUSE render LEADS with a status marker while PASS is the bare value. A test comparing two different numbers, or asserting only a trailing tag, does not meet this</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rb-10"><invocation>python -c "import importlib.util as u; s=u.spec_from_file_location('rp','lib/research/checkface/render_print.py'); m=u.module_from_spec(s); s.loader.exec_module(m); v='12345'; p=m.render_value({'verdict':'PASS','value':v,'figure_id':'f'}); q=m.render_value({'verdict':'PROVISIONAL','value':v,'figure_id':'f','marker':{'colour_token':'amber','icon':'WARN'}}); print('prov_leads_marker', (not q.strip()[0].isdigit()), '| pass_is_bare', p.strip()==v, '| same_value_differs', p!=q, '| ascii', q.isascii())"</invocation><expect>"prov_leads_marker True" AND "pass_is_bare True" AND "same_value_differs True" AND "ascii True" -- the PROVISIONAL render of the SAME value leads with a non-digit status marker, PASS renders the bare number, the two differ, and the render is ASCII. If the PROVISIONAL render still starts with the value's digit (a trailing-tag-only fix), prov_leads_marker is False and this is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rb-10"><invocation>git status --porcelain -- portal/ | grep -c -E '\.(tsx|ts|css)$'</invocation><expect>exactly "0" -- NEGATIVE: no portal source; the salient marker is a print+data+spec artifact and C-DESIGN-SPEC-FIRST holds</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rb-10"><invocation>python -c "print('ascii', open('lib/research/checkface/render_print.py', encoding='utf-8').read().isascii())"</invocation><expect>exactly "ascii True" -- NEGATIVE: render_print.py introduces no non-ASCII (no glyph/emoji); the leading salient marker is an ASCII status token</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rb-10" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical, difference arm): a same-number test proves the PROVISIONAL/REFUSE render is distinguished at the START, not by a trailing word on a different number.
- **AC2** (mechanical, difference arm): the PROVISIONAL render of the SAME value leads with a status marker and PASS is bare -- the exact reading defect C-S12 named cannot recur.
- **AC3** (mechanical, NEGATIVE): no .tsx.
- **AC4** (mechanical, NEGATIVE): the render stays ASCII.
- **AC5** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names 3.0.0_SA_CVO~Z): look at the rendered fixture -- does a PROVISIONAL/REFUSE figure read as visibly not-yet-checked AT A GLANCE (the warning reached before the number), rather than as a number that passed? Is the leading-marker choice one the design spec carries unchanged into the .tsx? This is the AC4 regrade C-S12 asks for.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>2b</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.4 + L6 round 2b) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @a81bd256c9 (GRANDFATHERED for L4-R)
**Authority chain:** L10 round-2 analysis @c48576bf85 (answering CVO slug REMEDIATION_v2 @b3acbcf3dd) -> L5 recut decomposition v0.4 @192c198231 (section 11, AMGT-rb-10) -> this round-2b issuance.
**Chain:** round 2b, an independent chain of one.
**Provenance:** decomposition v0.4 section 11a's AMGT-rb-10 row; the defect is C-S12 (r-10 AC6/AC4 FAIL) per the CVO evidence @b3acbcf3dd and analysis s.2.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- v0.2's run stands; G-14 binds AC5 (judgment never self-graded).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the L10 round-2 analysis @c48576bf85 is the authority; round-1's 10/10 stands.
comp-blast: DECLARED-NOT-APPLICABLE -- no infra act, no served-output move (no .tsx, print fixture only).
</preflight>
**Preflight disposition:** a print+data+spec edit to a landed module; no new gate/IAM/adversary/vendor plane; the authority is the L10 round-2 analysis.
