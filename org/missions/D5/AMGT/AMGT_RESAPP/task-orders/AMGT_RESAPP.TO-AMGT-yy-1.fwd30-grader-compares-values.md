# AMGT_RESAPP task order -- `AMGT-yy-1` -- FWD-30'S GRADER COMPARES VALUES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-yy-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~176</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- local checks; read-only lambda:Invoke of the deployed function through capture_lib.
comp-adversary: RUN by the issuer at the cut -- AC1 and AC2 are the CVO's two value plants (page, export), each reproduced at the base reading EQUAL; AC3 the live grade on three names.
EGRESS CLASS, declared: NONE. Opal's own deployed function, S3 and DynamoDB, read-only.
</preflight>

## 1. THE CELL -- `AMGT-yy-1` (round 50, decomposition s.58)

FWD-30's one grader is `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/sweep.py` (with
`page_render.cjs` beside it). Round 49 re-keyed it on the page's data attributes: `render_page_html(fixture)`,
`page_facts_from_html(html)`, `rich_facts(rich_text, fixture)` and `compare_facts(page, rich)` (four sets keyed FIGURES, CITES,
ABSENCES, CASES; `reason` names every class that differs). **But each fact is only its IDENTITY** -- e.g.
`('FISCAL', 'IS_EPS', '2023')` -- so a wrong number reads equal. Measured at the cut on AMD_US_Equity: the page's `IS_EPS` row's
first `data-model-cell` reads `-0.6`; planting `999.99` there reads verdict OK; planting it on the export's `| IS_EPS |` line
(`-0.6 PER SHARE ...`) reads OK.

**Build (CTO round-49 ruling 1):** the attribute picks WHICH fact; the grader then compares the fact's VALUE on both sides.
- A FIGURE fact carries its value: the numeric text of the attribute-keyed cell (`data-model-row` x `data-model-cell`, the year from
  the sheet header as now; header-card figures by their attribute) against the served figure the export states for the same fact,
  normalised for unit and precision (e.g. `-0.6` equals `-0.60`; a thousands separator or a unit word is not a difference) --
  never by prose. A value that differs is a FIGURES difference.
- A CASE fact compares its served value the same way where the page carries one.
- The export's base-case line: take its label from the SERVED payload (`model.cases.base.label`), never a literal -- another cell
  (yy-4) is renaming it to "Opal's historical-multiple reference" this round and the grade must not move on that.
- A value the page does not carry as an attribute (the identity line, three absence reasons, a case's value where absent, the
  driver chart -- rows Z-W173-S1..S4): list it, do not guess it; those are asks to DSGN_AMGTV1, already sent.
- The grade line becomes
  `FWD-30 GRADE: equal E of I identified names; values equal V of I; unidentified U of F folders; keyed on: data-attributes`
  and the sweep exits 0 only when E == V == I.

## 2. BOUNDS

1. Write only inside `round45/checks/` (plus your deliverables and the surprise channel). `portal/**` and `lib/**` are READ-ONLY.
2. No S3 write, no deploy, no server, no vite. Standing: no install, no push, no promote, no vendor call. REFUSE, do not rescue.
3. Python from the repo root with `PYTHONPATH="$(pwd)"`; node from `portal/` (its `node_modules` are provisioned).

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~176/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-yy-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round50/checks/yy_1_plant.py --side page; echo "exit=$?"</invocation><expect>unplanted verdict 'OK'; page plant -&gt; 999.99: verdict 'NOT_OK' naming FIGURES; THE PAGE VALUE PLANT FAILS THE GRADE: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-yy-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round50/checks/yy_1_plant.py --side export; echo "exit=$?"</invocation><expect>unplanted verdict 'OK'; export plant -&gt; 999.99: verdict 'NOT_OK' naming FIGURES; THE EXPORT VALUE PLANT FAILS THE GRADE: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-yy-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round50/checks/yy-1.AC3.sh; echo "exit=$?"</invocation><expect>FWD-30 GRADE: equal 3 of 3 identified names; values equal 3 of 3; ...; THE GRADE COMPARES VALUES ON THE NAMED SET: YES -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 and AC2 the CVO's two plants as falsifiers (each with its unplanted arm); AC3 the value-comparing grade on three live names.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~176/AMGT_RESAPP.TO-AMGT-yy-1.fwd30-grader-compares-values.proof_of_spec.json`. Report once: what you changed, how each class's value is read on each side and normalised, the facts left value-unchecked (listed), the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-49 analysis s.4 row 1, ruling 1 (@c95a9a16a4). Base: AC1 FAIL (page plant reads OK), AC2 FAIL (export
plant reads OK), AC3 FAIL (grade line carries no values count). The full 96-folder value sweep is the issuer's real run at the
drain (expected: 95 of 95 identified value-equal, or the value gaps named).

<status>pending</status>
<round>50</round>
<slot>~176</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
