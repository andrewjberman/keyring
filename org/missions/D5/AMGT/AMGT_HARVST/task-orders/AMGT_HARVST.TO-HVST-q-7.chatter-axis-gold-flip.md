# AMGT_HARVST task order -- `HVST-q-7` -- ROUND 27 chain 7: FLIP `CHATTER_AXIS_SOURCE` TO `gold` ON THE DECLARED-SET RULE, UNDER A PAIR -- expected outcome from `q-3`'s population; below 10 eligible it is a HOLD with its `empty_reason` (FWD-7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-q-7</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- amgt-resapp-chatter-axis is a SCHEDULED producer (chatter-axis-schedule.tf); this act changes one environment variable (and the code the q-4 merge ships) and no schedule.
comp-iam: RUN at L5 -- the gold branch reads amgt/harvest/gold/chatter_daily; the role's GET on that prefix is read on the APPLIED plane at signing.
comp-adversary: RUN at L5 -- the adversary is a flip that "succeeds" while the next run still writes legacy, or a rank outside the expected population. AC1 invokes once and reads the served rank; AC2 compares it to the halves' expected outcome, both branches.
</preflight>

## 0. BEGIN ONLY WHEN ALL FOUR HOLD

1. `HVST-q-3` and `HVST-q-4` are `complete` and merged on CLOUD.
2. BOTH never-widen halves are COMMITTED and named in the dispatch:
   - the COO half, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round27/NEVER_WIDEN_HALF_COO_Q7.md`;
   - `1.0.0_SA_CTO~Z`'s half.

   **Act only inside them.**
3. ONE NEVER-2 entry under `org/critical_paths/change_management/` is opened AND COMMITTED before the apply.
4. The issuer's checks exist in `.../round27/checks/`.

## 1. THE ACT

1. Print the plan for `infra/aws/terraform/harvest/` with `CHATTER_AXIS_SOURCE = "gold"` and the build carrying the merged
   `q-4` code. A plan that moves anything the halves do not name is a REFUSAL.
2. ONE `safe-apply`.
3. ONE on-demand invoke of `amgt-resapp-chatter-axis`. Run AC1 and AC2.
4. **Rollback** (named in the halves): set the variable back to `legacy`, safe-apply forward, invoke once, and close the
   entry ROLLED BACK.
5. Close the NEVER-2 entry in the same session.

## 2. SURFACES

<paths>
infra/aws/terraform/harvest/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-q-7"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round27/checks/q-7.AC1.py</invocation><expect>AC1 RESULT: PASS</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-q-7"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round27/checks/q-7.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

## 4. WHEN YOU ARE DONE

Write the instance at
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~A/AMGT_HARVST.TO-HVST-q-7.chatter-axis-gold-flip.proof_of_spec.json`
with `to_id` `AMGT_HARVST.TO-HVST-q-7.chatter-axis-gold-flip`. Report once, with:
- the plan's resource list;
- the invoke's generation and population;
- both criteria's output;
- the NEVER-2 open and close commits.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** `ROUND_ANALYSIS.round26.md` s.4 item 7. This re-cuts `n-4` (withdrawn in round 24) on the declared-set rule.
- **Cut in this issuance; dispatched only after `q-3` and `q-4` merge and both halves are committed.**
- **`q-7.AC1.py` / `q-7.AC2.py` are issuer-written after `q-3` and `q-4`**, from `q-3`'s N and `q-4`'s in-memory
  population. This is the same recorded departure as `n-4`.
  - **If N < 10, the halves' expected outcome is a HOLD** with `empty_reason`: the prior generation is served and the
    legacy rank stays visible. The pair says so for both branches (ruling, s.4 item 7).
- **The seat** is `0.7.0_AE_CloudOps~A`, as for `a-2`, `i-4` and `ww-1` on the same root.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>27</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
