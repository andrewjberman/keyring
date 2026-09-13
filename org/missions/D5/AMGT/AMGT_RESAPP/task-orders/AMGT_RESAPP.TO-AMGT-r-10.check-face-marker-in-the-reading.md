# AMGT_RESAPP.TO-AMGT-r-10 -- THE CHECK-FACE MARKER, IN THE READING: a PROVISIONAL or REFUSE figure carries a distinct machine-readable marker so it never skims as a passed number

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-r-10</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~3</issued_to>

## THE CELL, INLINED IN FULL (round 2, FWD-10; fixes AMGT-s-10's AC6 FAIL)

```
AMGT-r-10. THE CHECK-FACE MARKER, IN THE READING. AMGT-s-10's data face carries the verdict
(PASS|REFUSE|PROVISIONAL) correctly, but the AC6 judgment FAILED: '12345 [PROVISIONAL]' skims as "a
number, fine" -- the held-back verdict lives in the DATA and is absent in the READING, so an unchecked
figure ships looking checked. This cell puts the verdict INTO THE READING: a distinct machine-readable
MARKER per verdict, landed BEFORE PROVISIONAL figures ever serve.

WHAT TO PRODUCE, under lib/research/checkface/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~3/:

  (a) THE MARKER  each check-face entry gains a `marker` field: {verdict, colour_token, icon} where
      colour_token and icon are from a small closed set and are DISTINCT per verdict (PASS != PROVISIONAL
      != REFUSE) -- machine-readable values the later .tsx binds, not prose. render_print.py renders the
      marker beside the value (e.g. the icon glyph or token name) so a REFUSE/PROVISIONAL figure is
      visually unmistakable from a PASS in the print path too.

  (b) THE DIFFERENCE, EXERCISED  on the fixture from AMGT-s-10 (a PASS figure, a PROVISIONAL figure, a
      REFUSE figure): the rendered/emitted marker for the PROVISIONAL figure differs from the PASS
      figure's, and the REFUSE figure's differs from both. A marker scheme where PROVISIONAL and PASS
      share a marker has not fixed the defect.

  (c) THE SPEC SECTION  update SPEC_SECTION_checkface.md so the design spec names the marker per verdict
      "at a glance" -- the colour_token and icon the .tsx will use, and that a refused/provisional value
      is reachable but never presented as trusted. Text, not .tsx.
```

## DEPENDENCIES

**NONE.** Independent. Reads AMGT-s-10's landed check_face fixtures and AMGT-s-11's figure rule (both landed).

## BOUNDS

```
⛔ C-DESIGN-SPEC-FIRST: NO .tsx, no file under portal/. The marker is a DATA + SPEC artifact the later
.tsx reads; AC3 refuses a .tsx.
⛔ C-MARK-NOT-DEGRADE: a marker is added, never a figure dropped; count in == count out unchanged.
⛔ THE MARKER SET IS CLOSED AND DISTINCT PER VERDICT: a scheme that collides PASS and PROVISIONAL is the
defect unfixed (AC1's difference arm).
⚠ Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
L10 analysis @4d31cf4caa s.2 (FWD-10): "'12345 [PROVISIONAL]' skims as 'a number, fine': the held-back
    rule is in the DATA and absent in the READING ... Remedy scoped in SPEC_SECTION_checkface.md (a
    colour/icon marker) -- land it BEFORE the .tsx serves PROVISIONAL figures".
AMGT-s-10 (landed): run_checks.py, render_print.py, check_face_*.json, the fixture with a REFUSE and a
    PROVISIONAL; C-MARK-NOT-DEGRADE (count in == count out).
comp-cache (round 1): 94 keys / 0 mismatches; the later .tsx binds the marker under this page's namespace.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/checkface/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-r-10.check-face-marker-in-the-reading.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~3/`. AMGT-s-10's and AMGT-s-11's deliverables are READ.
A path missing from that block is a path you are REFUSED on. Refuse a criterion you cannot satisfy as
written and report it; file a surprise ROW (`AMGT_RESAPP-Z-W3-S<k>` continuing your sequence, project
AMGT_RESAPP, fabric site-z) and STOP on that criterion if you need a surface not listed.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-r-10"><invocation>python -m pytest lib/research/checkface/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning "4 passed" with no "failed" -- AMGT-s-10's original 3 tests still pass, PLUS one new test: a PROVISIONAL figure's marker (colour_token, icon) is DISTINCT from a PASS figure's and a REFUSE figure's marker is distinct from both (the difference arm). A marker scheme that collides any two verdicts fails this test and is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-r-10"><invocation>python -c "import json; c=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/check_face_fixture.json'))['checks']; ms={x['verdict']: (x['marker']['colour_token'], x['marker']['icon']) for x in c if x.get('marker')}; print('checks', len(c), '| with a marker', sum(1 for x in c if x.get('marker')), '| distinct markers', len(set(ms.values())), '| verdicts marked', sorted(ms))"</invocation><expect>"with a marker" EQUAL to "checks", "distinct markers" EQUAL to the number of distinct verdicts present (each verdict a distinct (colour_token, icon) pair), and "verdicts marked" including 'PROVISIONAL' and 'REFUSE' -- every figure carries a marker and no two verdicts share one; a missing marker or a shared pair is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-r-10"><invocation>git status --porcelain -- portal/ | grep -c -E '\.(tsx|ts|css)$'</invocation><expect>exactly "0" -- NEGATIVE: no portal source; the marker is a data+spec artifact and C-DESIGN-SPEC-FIRST holds</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-r-10" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical, difference arm): PROVISIONAL and REFUSE markers are distinct from PASS and each other -- the defect (a provisional that reads as passed) cannot recur.
- **AC2** (mechanical): every figure carries a distinct-per-verdict marker.
- **AC3** (mechanical, NEGATIVE): no .tsx.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names 3.0.0_SA_CVO~Z): look at the fixture render -- would an analyst SEE at a glance that a PROVISIONAL figure is not yet checked, rather than read it as a number that passed? Is the colour/icon choice one the design spec can carry unchanged into the .tsx?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>2</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.3 + L6 round 2) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L10 round-1 analysis @4d31cf4caa -> L5 recut decomposition v0.3 @3d2d7af6e0 (section 10, AMGT-r-10) -> this round-2 issuance.
**Chain:** round 2, an independent chain of one.
**Provenance:** decomposition v0.3 section 10a's AMGT-r-10 row; the defect is s-10 AC6 FAIL and the L10 analysis s.2/s.4.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- v0.2's run stands; G-14 binds AC4 (judgment never self-graded).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the L10 analysis @4d31cf4caa is the authority; round-1's 10/10 stands.
comp-blast: DECLARED-NOT-APPLICABLE -- no infra act, no served-output move (no .tsx).
</preflight>
**Preflight disposition:** a data+spec edit to a landed module; no new gate/IAM/adversary plane; the authority is the L10 analysis.
