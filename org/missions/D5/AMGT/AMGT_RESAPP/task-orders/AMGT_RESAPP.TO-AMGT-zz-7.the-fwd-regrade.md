# AMGT_RESAPP task order -- `AMGT-zz-7` -- THE FWD-1..31 RE-GRADE AGAINST THE SERVED STATE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-zz-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~182</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- read-only Invokes of the deployed function and S3/DynamoDB reads with the seat's existing credentials.
comp-adversary: RUN by the issuer at the cut -- AC1's grader was run against the round-46 file as a control: 31 of 31 parsed, every fence quote verbatim; it refused that file on unmet-without-reason and on the stale code_sha256.
EGRESS CLASS, declared: NONE. Opal's own AWS, read-only.
</preflight>

## 1. THE CELL -- `AMGT-zz-7` (round 51, decomposition s.59)

The last full pass over the PRD's 31 forward outcomes was round 46's (`deliverables/0.9.0_WK_AMGT_RESAPP~167/FWD_EVIDENCE_ROUND46.json`,
graded at CodeSha `CtIvirvM...`); rounds 47-50 graded only FWD-30. **Re-run the pass, per FWD, against the SERVED state now**
(`opal-amgt-scoped-api` CodeSha `pVa+sgzj8XNZ9uvJqCOwRNCJn0IZhUklnWZh6JbO7B0=`; re-read it at the start and at the end -- if it moves
during your pass, stop, file a row, and report).

Read the PRD's ENDPOINT section (`prd/AMGT_RESAPP_PRD.md`, lines 416-830; the FWD clauses sit at 427-783) and grade each FWD-1..31
AS WRITTEN. Write `deliverables/0.9.0_WK_AMGT_RESAPP~182/FWD_EVIDENCE_ROUND51.json` in the round-46 file's shape: top-level `prd`
(path@commit), `run_at` (UTC), `code_sha256` (the deployed value you read), `state_rule`, `instrument_key`, `tally` (count + ids per
state), and `outcomes` -- one object per FWD with `id`, `fence_quote` (a VERBATIM span of that FWD's clause, copied from the PRD),
`instrument` (what you ran, exactly), `output_excerpt` (what it printed), `state` in {met, unmet, unmeasurable}, and `reason` (required
for unmet and unmeasurable: which condition read false, or why no instrument can read it). A state is your MEASUREMENT of the clause,
never a carried grade: every FWD needs an instrument run in THIS pass (reusing the round-46 instruments is fine; their outputs are not).
Read-only helpers you may use: `deliverables/0.9.0_WK_AMGT_RESAPP~158/capture_lib.py` (`_invoke`, read-only Invokes), the FWD-30
grader `deliverables/2.0.0_SA_COO~Z/round45/checks/sweep.py --served` (bound it: `--only` a few keys per call), and the round-50/51
checks under `deliverables/2.0.0_SA_COO~Z/round5{0,1}/checks/` that name a served read.

## 2. BOUNDS

1. READ ONLY. No product file, no S3/DynamoDB write, no deploy, no Invoke that writes (GET routes only), no vendor call. Every
   invocation under `timeout 120`; batch a population across several calls rather than one unbounded sweep.
2. Your write surface is your deliverables folder and the investigation file.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~182/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-zz-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round51/checks/zz_7_fwd.py; echo "exit=$?"</invocation><expect>rows 31 of 31; states {...}; graded at the deployed CodeSha; THE FWD-1..31 PASS IS COMPLETE AND GROUNDED: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-zz-7" judgment="true"/>
</proof_of_spec>

AC2 (judgment, graded by `3.0.0_SA_CVO~Z` at L9, never self-graded): each outcome's `state` follows from its `output_excerpt` read
against its `fence_quote`. Record it under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming the CVO.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~182/AMGT_RESAPP.TO-AMGT-zz-7.the-fwd-regrade.proof_of_spec.json`. Report once: the tally, every FWD whose state differs from round 46's with the reason, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-50 analysis ruling 6. Base: AC1 FAIL (file absent). Graded at `pVa+sgzj` BEFORE zz-8 moves the base; the
issuer grades AC1 at this order's drain, ahead of the zz-8 GO.

<status>pending</status>
<round>51</round>
<slot>~182</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
