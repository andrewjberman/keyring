# AMGT_RESAPP task order -- `AMGT-ae-2` -- FWD-18 READ ON THE PAGE: ASML'S DRIVER CHART

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ae-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~196</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the check reads the deployed function by Invoke (read-only); this order writes nothing to AWS.
comp-adversary: RUN by the issuer at the cut -- AC1 reads ASML's page and a control (AMD) on the grader's own render; at the cut ASML reads SERVED / filing / 3 points and the control carries no filing chart.
EGRESS CLASS, declared: NONE. Opal's own AWS, read-only.
</preflight>

## 1. THE CELL -- `AMGT-ae-2` (round 55, decomposition s.63)

FWD-18 is the thesis tab's driver chart: ASML's is served from its filing (the D-1 document's spliced `thesis_driver`). This cell grades
it ON THE PAGE -- the SecurityAnalysis page rendered from a capture of the DEPLOYED function -- by running the check below, then
recording the result. It is a READ: build nothing, change nothing.

## 2. BOUNDS

1. Run the check and write the proof instance. No product file, no check edit, no AWS write. Standing: no install, no push, no promote,
   no deploy, no vendor call. REFUSE, do not rescue: a NO is a result to report, never a thing to fix here.
2. Python from the repo root with `PYTHONPATH="$(pwd)"`; node is on PATH for the render.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~196/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ae-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; T="$(mktemp -d)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round55/checks/ae_2_driver.py --cache "$T/cache"; echo "exit=$?"</invocation><expect>ASML page: chart ['SERVED'] source ['filing'] points of at least 3; the AMD control carries no SERVED filing chart; FWD-18: ASML'S DRIVER CHART IS SERVED FROM ITS FILING ON THE PAGE: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~196/AMGT_RESAPP.TO-AMGT-ae-2.fwd18-on-the-page.proof_of_spec.json`. Report once: the check's output lines, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-54 analysis item 2. A read cell: AC1 PASSES at the base by design (the outcome it grades already exists; the
cell records the grade). Dry-run at the cut: ASML SERVED / filing / 3 points; AMD control none; 16 s.

<status>pending</status>
<round>55</round>
<slot>~196</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
