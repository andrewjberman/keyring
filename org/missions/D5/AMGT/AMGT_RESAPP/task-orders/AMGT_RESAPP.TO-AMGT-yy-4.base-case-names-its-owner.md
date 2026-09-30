# AMGT_RESAPP task order -- `AMGT-yy-4` -- THE BASE CASE NAMES ITS OWNER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-yy-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~178</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a string constant; no AWS action.
comp-adversary: RUN by the issuer at the cut -- AC1 reads the label on four names in process; AC2 is the bound.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AMGT-yy-4` (round 50, decomposition s.58)

The served Base case's label is `lib/research/api/case_rule.py` `BASE_LABEL = "Historical-multiple reference"` (`:76`), read by
`lib/research/api/scoped_amgt.py` at `:3081` and `:3095`. It sits beside the research team's own Base case (`model.team_cases`), and a
reader cannot tell whose it is (DSGN_AMGTV1 round-5 ruling 4).

**Build:** the served label reads exactly `Opal's historical-multiple reference`. Change it at its one definition; every consumer
reads the constant (confirm none types the old string -- `lib/research/print/render_pack.py`'s export line included); update each
test that pins the old words. Nothing else moves: the formula, `formula_words`, the value, the status and every other case are
unchanged.

## 2. BOUNDS

1. `case_rule.py`, `render_pack.py` and their tests only. No page file, no deploy. Standing: no install, no push, no promote.
2. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
lib/research/api/case_rule.py
lib/research/api/tests/
lib/research/print/render_pack.py
lib/research/print/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~178/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-yy-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round50/checks/yy_thesis.py --plane local --what label; echo "exit=$?"</invocation><expect>no BAD line; THE BASE CASE NAMES ITS OWNER: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-yy-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round48/checks/api-suite.sh; echo "exit=$?"</invocation><expect>pytest reports N passed and 0 failed -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~178/AMGT_RESAPP.TO-AMGT-yy-4.base-case-names-its-owner.proof_of_spec.json`. Report once: what you changed, every consumer of the label you found, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-48 s.4b carried item / round-49 s.4 row 4. Base: AC1 FAIL (ADBE base label 'Historical-multiple reference'),
AC2 PASS. SERVED at yy-5. yy-1's grader takes the label from the served payload, so this rename does not move FWD-30.

<status>complete</status>
<round>50</round>
<slot>~178</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
