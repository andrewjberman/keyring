# AMGT_RESAPP task order -- `AMGT-aa-1` -- THE VERIFIER LOCATES A STORED POINT BY ITS STATED VALUE (A RE-VERIFICATION OF A RESCALED OBJECT KEEPS ALL OF ITS POINTS)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aa-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~390</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-aa-1.the-verifier-locates-a-point-by-its-stated-value</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a verifier rule and its tests, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- r94_rescale_table.py reads stored filing objects and silver rows with the caller's own credentials (GET only); r95_reverify_idempotent.py reads nothing.
comp-adversary: RUN at the cut -- r95_reverify_idempotent.py FAILs I1-I4 at the base (kept 1 of 3, held 2) and PASSes I5, I6, and PASSes 6 of 6 against a throwaway candidate (the two raw-claim lines taking `stated_value`); r94_rescale_table.py FAILs T1 at the base (SAP stored 3, expected 1) and reads equal 12 of 12 against the candidate.
EGRESS CLASS, declared: NONE (S3 GETs by the table check; no vendor, SEC or model call).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-390` (branch `wk-AMGT_RESAPP-390`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-390`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-aa-1` (round 95, decomposition s.103)

CTO~DELL1 round-94 analysis item 1 (row `D1-S24`, ARMED). Round 94's `AMGT-ff-3` stores a rescaled point as `value` = the figure on the series unit's scale (13.745) with
`stated_value` (13745), `stated_scale` ('million') and `rescaled_to` ('billion') beside it. `lib/research/filings/analyze.py::reverify_stored_thesis_driver` builds its raw
claim from each stored point's `value` only (two list comprehensions, `raw_points`, over `driver["points"]` and `driver["held_uncited"]`), so the excerpt never prints 13.745 as
a whole number and a second re-verification of SAP's already rescaled object keeps 1 of 3 points. Make the verifier locate a stored point by the figure the passage prints:

1. In `reverify_stored_thesis_driver`, build each raw point's `value` from `p.get("stated_value", p["value"])` for BOTH `points` and `held_uncited`. Change nothing else in
   the function or in `_apply_point_verification` (a point with no `stated_value` is located by its `value` exactly as before).
2. Add `lib/research/filings/tests/test_reverify_stated_value.py` (pure, no network; the stored object, the source row and the S3 client are in-memory fixtures as
   `r95_reverify_idempotent.py` builds them): one test per arm I1-I6.

The close is the arms below: re-verifying SAP's written object keeps 3 of 3, byte-equal; a stored value no excerpt prints is held (the negative arm); an object a fresh run held
whole is held again. This is a producer-side rule with its tests; NO stored object is written by this cell (SAP's object is not re-verified by anyone until it is merged).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W390-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call.
2. No `bun`, `npm` or `pip install`. The checks' S3 and DynamoDB reads (GET only) are permitted; nothing else is fetched.
3. Standing: no S3 delete, no push of shared branches.
4. Edit the named product files minimally: do not reformat them and touch no function the cell does not name.

## 3. SURFACES

<paths>
lib/research/filings/analyze.py
lib/research/filings/tests/test_reverify_stated_value.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~390/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-aa-1"><invocation>cd C:/dev/wk-resapp-390 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_reverify_idempotent.py"; echo "exit=$?"</invocation><expect>PASS I1 (an already rescaled object re-verifies to the same three points), PASS I2, PASS I3 (a figure no excerpt prints is held with a reason), PASS I4, PASS I5, PASS I6; arms passed 6 of 6; R95 REVERIFY IDEMPOTENT: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aa-1"><invocation>cd C:/dev/wk-resapp-390 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_rescale_table.py"; echo "exit=$?"</invocation><expect>12 objects listed; SAP_GY_Equity reads stored 3 | expected 3 and every other object equal (changed 0); PASS T1, PASS T2; R94 RESCALE TABLE: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-aa-1"><invocation>cd C:/dev/wk-resapp-390 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_rescale.py" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/filings/tests -q -p no:cacheprovider; echo "exit=$?"</invocation><expect>the control: R94 RESCALE: YES (7 of 7, the fresh-run rule unchanged) and every test of lib/research/filings/tests passes (no failed, no error); and exit=0</expect></criterion>
</proof_of_spec>


<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-94 analysis @ROUND_ANALYSIS.round94.md section 3 item 1: "D1-S24, the verifier locates a point by its stated_value (and held_uncited the same). Close: re-verifying SAP's written object keeps 3 of 3, byte-equal. Negative arm: a stored value no excerpt prints is held. Then SAP may be re-verified again. It is a producer-side rule with its tests, and no served write." `r94_rescale_table.py` T1 (SAP stored 3, expected 3) IS the live arm; `r94_sap_served.py` (the served route) is unchanged by construction. Disarms row D1-S24 at its merge; the procedural hold (no re-verify of SAP) lifts then.

<status>complete -- 2026-10-11T16:24Z by the issuer (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-390 @d53c2af66a (code @c3922a4602) merged @84c2876f3c, proof instance VALID; issuer re-run on the merged tree: AC1 R95 REVERIFY IDEMPOTENT YES (6 of 6; the base read 2 of 6), AC2 R94 RESCALE TABLE YES (12 objects, SAP stored 3 | expected 3, changed 0; the base read stored 3 | expected 1), AC3 R94 RESCALE YES (7 of 7) + lib/research/filings/tests 341 passed. analyze.py +4/-2 (two raw-claim lines take `p.get("stated_value", p["value"])`), one new test file of six. Producer-side: no stored object is written; row D1-S24 disarmed by this merge, and the procedural hold on re-verifying SAP's object (ff-5 ledger L8) lifts.</status>
<round>95</round>
<slot>0.9.0_WK_AMGT_RESAPP~390</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
