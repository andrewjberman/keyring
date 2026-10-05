# AMGT_RESAPP task order -- `AMGT-at-5` -- THE 30-OUTCOME SWEEP: EVERY GRADEABLE FWD EXERCISED ON THE DEPLOYED FUNCTION AGAINST ITS DONE WHEN

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-at-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~230</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one read of the deployed function.
comp-iam: DECLARED-NOT-APPLICABLE -- invokes the deployed function and reads stores the operator already reads; no write.
comp-adversary: RUN by the issuer at the cut -- the sweep script does not exist at the base; the stale board (ledger/FWD_BOARD_ROUND69.md) carries 19 of 20 NOT_REALIZED grades from round 51, with 9 disagreements.
EGRESS CLASS, declared: NONE. No vendor or model call.
</preflight>

**Your worktree:** `C:/tmp/r70-230` (branch `wk-AMGT_RESAPP-230`, cut from the issuer's tree after the round-70 redeploy). Work and commit
only there. Start every shell call with `cd /c/tmp/r70-230`.

## 1. THE ACT -- `AMGT-at-5` (round 70, decomposition s.78; CTO round-69 analysis s.6 @030d5d1e87)

The PRD `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` (v0.37) defines 39 outcomes, FWD-1..FWD-39, in its ENDPOINT fence.
FWD-21..FWD-29 are RE-HOMED to DSGN_AMGTV1 (Addendum C, section C.1). That leaves **30 gradeable outcomes**: FWD-1..20 and
FWD-30..39. The last compiled board, `org/missions/D5/AMGT/AMGT_RESAPP/ledger/FWD_BOARD_ROUND69.md`, is stale: most grades date
from round 51.

1. **Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~230/fwd_sweep.py`.** For each of the 30 gradeable
   FWDs, quote its DONE WHEN from the PRD and exercise it ONCE on the DEPLOYED function. Use the same Lambda invoke the existing
   checks use: `deliverables/0.9.0_WK_AMGT_RESAPP~158/capture_lib.py` `_invoke`. Record:
   - `fwd`, `done_when` (quoted), `route(s)` read and the `denominator` (names or rows read);
   - `status`: one of `MEETS`, `DOES_NOT_MEET` or `UNMEASURABLE_WITH_REASON` (a human act, a qualified wait, an Andrew act), with
     the reason;
   - `evidence`: the measured values.
   - FWD-21..29 print `RE-HOMED` and are not graded.
   - **Grade on the DONE WHEN, never the ACCEPT** (CTO s.6). FWD-30 is the named case.
2. **Write `FWD_SWEEP_ROUND70.json` and a short `FWD_SWEEP_ROUND70.md` table** in the same folder.
3. **Print one line per FWD (39 lines)** and a final `SWEEP: <n> of 30 read` line.

## 2. BOUNDS

1. A read and nothing else. No deploy, no store write, no vendor or model call, no portal write.
2. Never mark a FWD `MEETS` without a measured value that satisfies its DONE WHEN. A FWD you cannot read is `UNMEASURABLE_WITH_REASON`.
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~230/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 2400)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-at-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~230/fwd_sweep.py" --where deployed; echo "exit=$?"</invocation><expect>39 FWD lines (30 graded with a status in MEETS / DOES_NOT_MEET / UNMEASURABLE_WITH_REASON, FWD-21..29 RE-HOMED); the final line reads SWEEP: 30 of 30 read; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-at-5" judgment="true"/>
</proof_of_spec>

AC2 is graded by `3.0.0_SA_CVO~Z` at round-70 L9: each status against its DONE WHEN. Record it as UNVERIFIABLE-BY-INSTRUMENT, naming
the CVO.

## 5. WHEN YOU ARE DONE

Commit via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~230 <0.9.0_WK_AMGT_RESAPP~230@opal.agent>" -F <msgfile> -- <paths>`.
Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~230/AMGT_RESAPP.TO-AMGT-at-5.thirty-outcome-sweep.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Report once:
- the commit hash;
- the 39 lines;
- the counts per status;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-69 analysis s.6 @030d5d1e87 (msg 29506). Staged until at-6 lands, so the sweep reads the round-70 deployed
state.

<status>staged</status>
<round>70</round>
<slot>0.9.0_WK_AMGT_RESAPP~230</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER GO (2.0.0_SA_COO~Z, 2026-10-05 ~09:0xZ):** at-6 landed, so the deployed function is `GS//XHnV` (the round-70 state). The
worker is spawned with this order's face, in worktree `C:/tmp/r70-230`.

<status>pending</status>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-05 ~14:0xZ):** CLOSED.
- Worker ~230: sweep `ff12c5e3a1`, instance `e403b87c07`, proof-of-spec-check VALID (rc=0).
- AC1 PASS: SWEEP 30 of 30 read on deployed `GS//XHnV` (unchanged across the run); 95 of 95 names answered 200 on all 7 routes.
- Counts: MEETS 9 (FWD-9, 13, 32-36, 38, 39); DOES_NOT_MEET 8 (FWD-2, 4, 7, 11, 12, 14, 16, 20); UNMEASURABLE_WITH_REASON 13;
  RE-HOMED 9.
- AC2 (judgment) is for 3.0.0_SA_CVO~Z at L9.
- Rows: Z-W230-S1 (ARMED, this seat: the round-45 page-render grader is stale against DSGN's new imports, so FWD-30's page
  comparison is unread), and Z-W230-S2 and Z-W230-S3 (INERT).

<status>complete</status>
