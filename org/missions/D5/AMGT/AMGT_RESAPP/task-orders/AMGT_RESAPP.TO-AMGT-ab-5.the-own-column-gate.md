# AMGT_RESAPP task order -- `AMGT-ab-5` -- A DRIVER POINT VERIFIES ONLY AGAINST ITS OWN COLUMN

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ab-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~189</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- AC1 has no I/O; AC2 READS the stored ASML objects and writes nothing (dry run).
comp-adversary: RUN by the issuer at the cut -- AC1 plants 2024's number under 2025 (base: verified -- the defect); AC2 is the real-case control (base PASS, must stay).
EGRESS CLASS, declared: NONE. Opal's own S3, read-only.
</preflight>

## 1. THE CELL -- `AMGT-ab-5` (round 52, decomposition s.60)

`lib/research/filings/analyze.py` verifies a thesis driver's points against the filing excerpt through ONE path,
`_apply_point_verification(points, excerpt_text, passage_map, anchor=0)` (`:1160`): `verify_points_against_excerpt` (`:1044`) finds a
value inside the block that carries its own period label (`_period_blocks`, `:1029`), then held points retry through `_columnar_verify`
(`:1108`) for columnar tables. **The defect (row Z-W185-S1):** the LAST located period's block runs to the end of the excerpt, so in a
columnar table (a header run `2023` / `2024` / `2025`, a row label, then values one per line) the last column's block contains EVERY
column's value -- a 2025 point equal to the 2024 number verifies. **Build:** a number verifies only against its OWN column. When the
period labels form a columnar header run, the verification must use the column position (as `_columnar_verify` does), not the
run-to-end block; a value that sits only in another column is HELD with a reason. Every point that sits in its own column still
verifies -- ASML_NA_Equity's 3 real points must stay spanned. Tests: the plant, the control, and a non-columnar (prose) excerpt whose
behaviour is unchanged.

## 2. BOUNDS

1. `analyze.py` and ONE new test file under `lib/research/filings/tests/` only (another cell adds its own test file there; do not edit
   other tests). No S3 write, no live reverify. Standing: no install, no push, no promote, no deploy, no vendor call. REFUSE, do not rescue.
2. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
lib/research/filings/analyze.py
lib/research/filings/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~189/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ab-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round52/checks/ab_5_column.py; echo "exit=$?"</invocation><expect>(a) plant 2025=200 held; (b) control 3 of 3 verified in their own columns; A DRIVER POINT VERIFIES ONLY AGAINST ITS OWN COLUMN: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ab-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round51/checks/zz_6_reverify.py; echo "exit=$?"</invocation><expect>the dry run writes nothing; re-verified points 3 (with span 3); THE DRIVER CHART IS SERVED FROM THE FILING'S VERIFIED POINTS: YES -- and exit=0 (ASML's real points stay verified)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ab-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" timeout 115 python -m pytest lib/research/filings/tests -q; echo "exit=$?"</invocation><expect>N passed and 0 failed, N &gt; 118 (118 at the cut, plus your new tests) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~189/AMGT_RESAPP.TO-AMGT-ab-5.the-own-column-gate.proof_of_spec.json`. Report once: the rule you changed and why prose excerpts are unaffected, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-51 analysis item 5 / ruling 7. Base: AC1 FAIL (plant verified {'2025': '200'}); AC2 PASS (the ASML control, a
component-level check -- the SERVED chart is ab-6's); AC3 PASS 118. analyze.py's packaging is read from ab-6's content diff.

<status>complete</status>
<round>52</round>
<slot>~189</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
