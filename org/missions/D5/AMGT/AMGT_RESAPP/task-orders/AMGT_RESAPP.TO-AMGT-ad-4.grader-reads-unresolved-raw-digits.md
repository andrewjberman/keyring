# AMGT_RESAPP task order -- `AMGT-ad-4` -- FWD-30'S GRADER READS AN UNRESOLVED FIGURE'S RAW DIGITS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ad-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~195</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the checks read the deployed function by Invoke (read-only); this order writes nothing to AWS.
comp-adversary: RUN by the issuer at the cut -- AC1 on TSM's real render: as captured the fact differs (base), a raw-figure plant and an export-resolved control must still differ; PASSED on a simulated fix. AC2 sweeps TSM plus two controls (base: 2 of 3).
EGRESS CLASS, declared: NONE. Opal's own AWS, read-only.
</preflight>

## 1. THE CELL -- `AMGT-ad-4` (round 54, decomposition s.62)

FWD-30's grader is `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/sweep.py`. For each name it reads a
VALUE from the rendered page and the export and grades them with `values_agree(page_text, export_token, export_unit)` inside
`value_diffs`. One fact in 96 names still differs: TSM_US_Equity's `('HEADER', 'CURR_ENTP_VAL')`. The page cell reads
`unit not resolved -- raw figure 71,993,494.73` and the export reads `71993494.73205896` with a unit beginning `UNRESOLVED-ON-TSM ...`.
Both sides say the unit is unresolved and both carry the same digits; the grader compares the page's leading WORDS, so it reports a
difference.

**Build:** when the page's value text is the page's unresolved-unit form (`unit not resolved -- raw figure <number>`), the grader reads
`<number>` as the value -- and grades it equal ONLY when the export's unit is also UNRESOLVED and the digits agree by the rule the grader
already uses for an UNRESOLVED unit. A page that says "unit not resolved" against an export whose unit IS resolved is a DIFFERENCE. No
other value reading changes.

## 2. BOUNDS

1. `sweep.py` only (its `values_agree` / `read_number` / `value_diffs` area). No product file, no page change, no AWS write. Standing: no
   install, no push, no promote, no deploy, no vendor call. REFUSE, do not rescue.
2. Python from the repo root with `PYTHONPATH="$(pwd)"`; node is on PATH for the render.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/sweep.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~195/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ad-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; T="$(mktemp -d)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round54/checks/ad_4_unresolved.py --cache "$T/cache"; echo "exit=$?"</invocation><expect>(0) difference lines 0; (a) raw-figure plant difference lines 1; (b) export-resolved control difference lines 1; THE GRADER READS AN UNRESOLVED FIGURE'S RAW DIGITS, BOTH SIDES UNRESOLVED ONLY: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ad-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round54/checks/ad-4.AC2.sh; echo "exit=$?"</invocation><expect>FWD-30 GRADE: equal 3 of 3, values equal 3 of 3; differ=0; TSM AND TWO CONTROLS READ VALUES-EQUAL: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~195/AMGT_RESAPP.TO-AMGT-ad-4.grader-reads-unresolved-raw-digits.proof_of_spec.json`. Report once: the rule you added, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-53 analysis item 4, RE-SCOPED by measurement (s.62b.3): CORPUS round 25's re-derive (COO~X msg 27279) fixed TSM
CUR_MKT_CAP; the one NOT_OK fact is CURR_ENTP_VAL, still UNRESOLVED on both sides, so a re-run alone cannot move it. The full 96-name
re-grade is the issuer's real run at the drain. Base: AC1 FAIL (1 difference line as captured), AC2 FAIL (2 of 3). Positive arm (ruling
1): AC1 PASS with a simulated rule (the raw figure read only when the export is UNRESOLVED); the plant and the control still differ.

<status>complete</status>
<round>54</round>
<slot>~195</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
