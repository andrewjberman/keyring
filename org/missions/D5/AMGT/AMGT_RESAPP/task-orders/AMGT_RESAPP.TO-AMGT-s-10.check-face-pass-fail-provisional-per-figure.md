# AMGT_RESAPP.TO-AMGT-s-10 -- THE CHECK FACE: pass, fail or provisional per figure -- a failure renders as a MARKED VALUE, never a blank, a zero or a row that vanished

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-s-10</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~8</issued_to>

## THE CELL, INLINED IN FULL (outcome FWD-10; manifest row S10; verb: wire)

```
AMGT-s-10. THE CHECK FACE -- pass, fail or provisional per figure, on the page. A failure renders as a
MARKED VALUE, never a blank, a zero or a row that vanished.

FWD-10's bar, verbatim: "A figure that failed its check is visible as failed. DONE WHEN EXERCISED -- a
check has actually refused something and the refusal was seen on the page. ACCEPT: A figure that failed
or skipped its check looks different from one that passed, and the analyst can tell which. A failure
shows as a marked value -- never as a blank, a zero, or a row that quietly disappeared."

C-MARK-NOT-DEGRADE (PRD s.3): a failed stage MARKS the pack; it never silently produces a thinner one. A
thin pack that looks whole is the exact failure FWD-10 exists to prevent. C-CHECK-MUST-REFUSE: a check
that cannot fail is not a check -- this face MUST show a refusal in its exercise.

WHAT "WIRE" MEANS AT THIS CUT: no page until the spec is approved. This cell delivers the DATA FACE and
the PRINT-PATH render; the .tsx is a later order.

WHAT TO PRODUCE, under lib/research/checkface/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~8/:

  (a) THE CHECK RUN  lib/research/checkface/run_checks.py -- for a landed model block, apply AMGT-s-11's
      FIGURE rule (lib/research/rules; the categorical rule: a figure whose unit_status or sign_status is
      not MEASURED is REFUSED; PROVISIONAL where the rule is held back) to EVERY figure and write
      check_face.json: [{figure_id, value, verdict: PASS|REFUSE|PROVISIONAL, reason}]. COUNT IN EQUALS
      COUNT OUT: no figure is dropped for failing.

  (b) THE EXERCISE THAT MUST REFUSE: run it on (i) every real block AMGT-s-1 landed, and (ii) a FIXTURE
      block that carries one figure with unit_status INFERRED and one with a UNRESOLVED sign -- the
      fixture run MUST produce at least two REFUSE verdicts, or the check cannot fail and the cell has
      not met C-CHECK-MUST-REFUSE. Record both runs.

  (c) THE PRINT-PATH RENDER  lib/research/checkface/render_print.py -- for a check_face.json, the
      per-figure line for Adam's artifact: a PASS figure renders its value; a REFUSE renders
      "[REFUSED: <reason>]" IN PLACE OF the value (the value is still recorded in the JSON, never shown
      as if trusted); a PROVISIONAL renders the value with "[PROVISIONAL]" beside it. NEVER a blank,
      NEVER a zero substituted, NEVER a dropped line. Render both runs from (b) to .md.

  (d) SPEC_SECTION_checkface.md for AMGT-s-5: how PASS / REFUSE / PROVISIONAL look on the page "at a
      glance", and that a refused figure's value is reachable (hover / expand) but never presented as
      trusted.
```

## DEPENDENCIES

`AMGT-s-11` (the figure rule). Same slot (~8), second in `AMGT-s-11 -> AMGT-s-10`; continue on the same
context. Reads `AMGT-s-1`'s landed blocks (the real runs).

## BOUNDS -- what this cell may not cross

```
⛔ C-MARK-NOT-DEGRADE: count in equals count out; a REFUSE is a marked value. AC2 and AC3.
⛔ C-CHECK-MUST-REFUSE: the fixture run refuses something, or the criterion fails. AC2.
⛔ NO THRESHOLD INVENTED: the figure rule is applied as AMGT-s-11 shipped it; where it is held back, the
verdict is PROVISIONAL with the reason, never a guessed PASS.
⛔ NO NEW BLOOMBERG CALL: the checks run over landed blocks. AC5.
⛔ C-DESIGN-SPEC-FIRST: no .tsx.
⚠ Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
AMGT-s-11 (landed): RULES['figure'] with its refusal fixture (an inferred unit) and pass fixture;
    threshold None or drawn from figure_units.json; held_back state as shipped.
AMGT-s-1's model_block_*.json (landed): every figure carries unit_status and sign_status (its AC5); the
    real runs should PASS where MEASURED and PROVISIONAL/REFUSE where not -- record the counts.
F4 (CITED): the units trap; an inferred unit is the REFUSE case that matters most in production.
comp-schedule (RUN): 25 gates armed, none this project's; G-14 binds AC6.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/checkface/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-s-10.check-face-pass-fail-provisional-per-figure.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~8/`. lib/research/rules and AMGT-s-1's
deliverables are READ.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
⛔ REFUSE a criterion you cannot satisfy as written and report the refusal with its measurement; never
repair the criterion, widen it, or satisfy it by a route this order did not name. If you need a
surface that is not listed, file a surprise ROW in the investigation file above and STOP on that
criterion. Your surprise row id is `AMGT_RESAPP-Z-W8-S<k>`, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`,
inside the file's fenced json array; a BLOCKING row is read by the COO in your final report; an
OBSERVATION never interrupts.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-s-10"><invocation>python -c "import json,glob; out=[]; [out.append((f.split('check_face_')[-1], len(json.load(open(f.replace('check_face_','model_block_').replace('~8','~1')))['figures']) if 'fixture' not in f else None, len(json.load(open(f))['checks']))) for f in glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~8/check_face_*.json')]; print('runs', len(out), '| real runs with count in == count out', sum(1 for k,i,o in out if i is not None and i==o), 'of', sum(1 for k,i,o in out if i is not None))"</invocation><expect>"real runs with count in == count out N of N" with N at least 3 -- for every real block AMGT-s-1 landed, the check face carries exactly one verdict per figure and no figure was dropped (C-MARK-NOT-DEGRADE)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-s-10"><invocation>python -c "import json; c=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~8/check_face_fixture.json'))['checks']; v={}; [v.__setitem__(x['verdict'], v.get(x['verdict'],0)+1) for x in c]; print('fixture verdicts', v, '| refusals with a reason', sum(1 for x in c if x['verdict']=='REFUSE' and x.get('reason')))"</invocation><expect>a REFUSE count of 2 or more with "refusals with a reason" EQUAL to it -- the check CAN fail and did, on the inferred-unit and unresolved-sign figures, each refusal carrying its reason (C-CHECK-MUST-REFUSE); fewer than 2 refusals is a check that cannot fail and is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-s-10"><invocation>python -c "import io,json; t=io.open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~8/check_face_fixture.md',encoding='utf-8').read(); c=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~8/check_face_fixture.json'))['checks']; print('lines rendered', sum(1 for l in t.splitlines() if l.strip().startswith('|') and not l.strip().startswith('|-') and 'figure' not in l.lower()), '| checks', len(c), '| REFUSED markers', t.count('[REFUSED:'), '| PROVISIONAL markers', t.count('[PROVISIONAL]'), '| empty value cells', t.count('|  |'))"</invocation><expect>"lines rendered" EQUAL to "checks", "REFUSED markers" EQUAL to the fixture's REFUSE count, and "empty value cells 0" -- every figure has a line, every refusal is a marked value, and nothing is blank</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-s-10"><invocation>python -m pytest lib/research/checkface/tests -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning "3 passed" with no "failed" -- (1) a REFUSE renders as "[REFUSED: reason]" in place of the value; (2) the same figure with MEASURED statuses renders its value (the difference arm); (3) a block of N figures yields N check lines</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-s-10"><invocation>grep -r -c -i -E 'blpapi|blp_client|8194|requests\.get|httpx' lib/research/checkface/ | grep -v -c ':0$'</invocation><expect>exactly "0" -- NEGATIVE: the checks run over landed records; no Bloomberg call, no fetch</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-s-10" judgment="true"/>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): no figure dropped on any real block.
- **AC2** (mechanical): the check refused something, with reasons. The bar that binds all six classes.
- **AC3** (mechanical): every refusal is a marked value in the render; nothing blank.
- **AC4** (mechanical): refuse-renders-marked and pass-renders-value, both arms.
- **AC5** (mechanical, NEGATIVE): no fetch.
- **AC6** (JUDGMENT -- never self-graded; record its output UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO~Z): look at the fixture render -- would an analyst tell at a glance which figures failed, and would the real blocks' PROVISIONAL figures (held-back rule) read as "not yet checked" rather than as "fine"?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>2</round>
<slot>~8</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5+L6, round 1 issuance, round-2 cell) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L1 brief @19ce7d5b4d -> L2 endpoint @3bc8f5f2c4 -> L4 PRD v0.3 @f68818832b -> L5 decomposition v0.2 @ed25feaee5 -> this issuance.
**Chain:** Q8, second in `AMGT-s-11 -> AMGT-s-10`; slot ~8 continues on the same context.
**Provenance:** the cell text is the decomposition's row verbatim. The fixture-that-must-refuse is C-CHECK-MUST-REFUSE applied to the face itself: a check face exercised only on clean data would pass every figure and prove nothing.
<preflight>
comp-schedule: RUN -- --budget 500 to completion, 5 of 5 carriers, 25 gates armed, none this project's
comp-iam: RUN -- 195 TF roles / 188 services / 1084 operations / 304 gaps; this cell touches no AWS resource
comp-adversary: RUN -- on the L5 decomposition v0.2 at read-vintage @d09e26e1b1; 10 of 10 cited pins VERIFIED
comp-routes: RUN -- 28 CloudFront behaviors; no route touched by this cell
comp-cache: RUN -- 118 of 118 useQuery sites; no portal file touched by this cell
comp-find --corpus aws: RUN -- 2382 nodes at 12:24:50Z; nothing this cell writes is in AWS
</preflight>

**Preflight disposition:** mandatory core RUN at the L5 vintage. comp-blast DECLARED-NOT-APPLICABLE: a library, fixtures and deliverables; no deployed resource changes.
