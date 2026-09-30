# AMGT_HARVST task order -- `HVST-n-4` -- ROUND 24 chain 3 of 5, cell 2 of 2: FLIP `CHATTER_AXIS_SOURCE` FROM `legacy` TO `gold` -- the chatter rank is computed from the graded daily table (FWD-7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-n-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- amgt-resapp-chatter-axis is a SCHEDULED producer (chatter-axis-schedule.tf); this act changes one environment variable on it and no schedule, alarm or cadence.
comp-iam: RUN at L5 -- the producer's gold branch reads amgt/harvest/gold/chatter_daily; whether its role already holds that GET is read on the APPLIED plane at signing and named on the halves. No IAM change is admitted unless the halves name exactly one read-only grant.
comp-adversary: RUN at L5 -- the adversary is a flip that "succeeds" (apply rc 0) while the next scheduled run still writes a legacy rank, or a rank that moves beyond the pair's expected diff. AC1 invokes the producer once after the apply and reads the served rank; AC2 compares it to the halves' expected diff.
EGRESS CLASS, declared: ONE safe-apply on infra/aws/terraform/harvest/ changing CHATTER_AXIS_SOURCE on amgt-resapp-chatter-axis from legacy to gold; at most ONE read-only grant if the halves name it; ONE on-demand invoke of the producer after the apply. No other resource moves.
</preflight>

## 0. BEGIN ONLY WHEN ALL THREE HOLD

1. `HVST-n-3` is `complete` and merged on CLOUD. The dispatch names its merge. Its AC2 is the expected diff.
2. BOTH never-widen halves are COMMITTED and named in the dispatch: the COO half
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round24/NEVER_WIDEN_HALF_COO_N4.md` and
   `1.0.0_SA_CTO~Z`'s half. **Act only inside them.**
3. ONE NEVER-2 entry under `org/critical_paths/change_management/` is opened AND COMMITTED before the apply, with its
   `.open_deploys/` sentinel, and reads back from HEAD.

## 1. THE ACT

1. Print the plan for `infra/aws/terraform/harvest/` with `CHATTER_AXIS_SOURCE = "gold"`
   (`chatter-axis-schedule.tf` ~:70). A plan that moves anything the halves do not name is a REFUSAL: print it, stop,
   report.
2. ONE `safe-apply`.
3. ONE on-demand invoke of `amgt-resapp-chatter-axis` for the halves' as-of. Then run AC1 and AC2.
4. **Rollback** (named in the halves): set the variable back to `legacy`, `safe-apply` forward, invoke once, and close
   the entry as ROLLED BACK.
5. Close the NEVER-2 entry in the same session.

## 2. BOUNDS

One variable, on one function. No code change, no schedule change, no delete of any kind, no vendor call. This producer
feeds AMGT_RESAPP's lead panel: the halves name the RESAPP surfaces it moves.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-n-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round24/checks/n-4.AC1.py</invocation><expect>AC1 RESULT: PASS (0 failure(s))</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-n-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round24/checks/n-4.AC2.py</invocation><expect>AC2 RESULT: PASS (0 failure(s))</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~A/AMGT_HARVST.TO-HVST-n-4.chatter-axis-source-gold-flip.proof_of_spec.json`
with `to_id` `AMGT_HARVST.TO-HVST-n-4.chatter-axis-source-gold-flip`. Report once, with:
- the plan's resource list;
- the invoke's generation;
- both criteria's output;
- the NEVER-2 entry's open and close commits;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **A SEAT ORDER, cut in this issuance and dispatched only after `n-3` drains and both halves are committed.** It is
   issued to `0.7.0_AE_CloudOps~A`, the seat that ran `a-2`, `i-4` and RESAPP `ww-1` on the same terraform root.
2. **`n-4.AC1.py` and `n-4.AC2.py` are issuer-written after `n-3` drains**, from its AC2 expected diff, and dry-run at the
   base before the dispatch.
   - AC1 is written to FAIL at the base (source reads `legacy`).
   - AC2 compares the served rank to `n-3`'s gold expected diff.

   **The files do not exist at this cut.** The dispatch waits for them. This is recorded as the one departure from
   "every check a file at the cut", because the check's content IS `n-3`'s measurement.
3. **Rulings:** `ROUND_ANALYSIS.round23.md` @`d1ec6f4118` s.2 ruling 4 and s.3 item 4. The rollback is the variable back
   to `legacy`.


**AMENDMENT 1 (issuer, 2026-09-30 ~02:5xZ) -- HELD, NOT DISPATCHED (row `Z-W58-S1`, ARMED -> disarmed by this hold).**
- `HVST-n-3` (drained @`49bafe8df9`) measured the producer's OWN `gold` branch as FAILING: `INCOMPLETE_GOLD_INPUT`, RESOLVED 0 of 191 security windows.
  - The gold `chatter_daily` reads `no_coverage` on 5,675 of 5,730 day-reads and `partial` on 55.
  - All 191 rows on 09-29 are `DENIED`.
- A `legacy` -> `gold` flip would therefore STOP the daily rank writes. There is no expected rank diff to sign; the pair this order requires cannot be written.
- The order stays `pending` and is NOT dispatched to `0.7.0_AE_CloudOps~A`.
- Carded to `1.0.0_SA_CTO~Z`. Its ruling decides whether FWD-7 is reached by feeding the gold branch coverage (the `data_status` / `publishers_covered` denominator the guard reads) or by changing the guard.
- A later amendment re-points this order to that ruling. No gate limb graded this record-face note.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>24</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
