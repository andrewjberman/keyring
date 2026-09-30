# AMGT_RESAPP task order -- `AMGT-ac-1` -- FWD-30'S GRADER READS THE DISPLAYED FIGURE, NEVER A HOVER TOOLTIP

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ac-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~190</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- read-only Invokes of the deployed function with the seat's existing credentials; no product file.
comp-adversary: RUN by the issuer at the cut -- AC1 plants a tooltip value (must not move the read) and changes the visible figure (must move it) on a REAL render; base: the plant moves the read.
EGRESS CLASS, declared: NONE. Opal's own AWS, read-only.
</preflight>

## 1. THE CELL -- `AMGT-ac-1` (round 53, decomposition s.61)

FWD-30's grader is `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/sweep.py`: `render_page_html` renders the
Security Analysis page from a captured served fixture (node, `page_render.cjs`), `_PageReader` / `page_facts_from_html` collect facts from
data attributes, and `value_diffs` / `values_agree` compare the page's value text with the rich export's. The redesigned page (DSGN_AMGTV1
round 12) nests a hover tooltip inside each header figure: `<li data-card-figure-mnemonic="PX_LAST" ...><span ...>Price</span><span
class="tabular-nums ...">EUR 1503.20</span><div role="tooltip" data-figure-tooltip="PX_LAST" data-full-value="1503.2" ...><div
data-data-tooltip="...">1503.2 | PRICE ... | PX_LAST | ...</div></div></li>`. The reader takes the element's whole text, so the value read is
"EUR 1503.201503.2 | PRICE ..." and 131 HEADER facts (PX_LAST 95, EQY_BETA 35, CURR_ENTP_VAL 1) grade as differing though nothing moved.

**Build:** the reader reads the DISPLAYED figure only -- text inside a `role="tooltip"` / `data-figure-tooltip` subtree is never part of a
value read (for header figures and for any other value cell that gains a tooltip). Nothing else in the grader moves: same facts, same keys,
same comparison rule. Keep the grader self-contained (no product-file import).

## 2. BOUNDS

1. `sweep.py` only (and a test file beside it if you add one under the same `round45/checks/` folder). No product file, no portal file,
   no AWS write. Every invocation under `timeout 120`.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/sweep.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~190/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ac-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; T="$(mktemp -d)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round53/checks/ac_1_plant.py --cache "$T"; echo "exit=$?"</invocation><expect>(a) tooltip plant: read unchanged: True; (b) visible-figure control: PX_LAST read changed: True; THE GRADER READS THE DISPLAYED FIGURE, NOT THE TOOLTIP: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ac-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round53/checks/ac-1.AC2.sh; echo "exit=$?"</invocation><expect>FWD-30 GRADE: ... values equal 3 of 3; differ=0; THE THREE NAMES READ VALUES-EQUAL ON THE DISPLAYED FIGURES: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~190/AMGT_RESAPP.TO-AMGT-ac-1.grader-reads-the-displayed-figure.proof_of_spec.json`. Report once: the reader rule you changed, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-52 analysis item 1 / ruling 2. Base: AC1 FAIL (the plant moves the read; the control moves PX_LAST), AC2 FAIL
(differ=6 over 3 names). The full 96-name re-grade is the issuer's drain run; FWD-30 is graded again only on this grader.

<status>pending</status>
<round>53</round>
<slot>~190</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
