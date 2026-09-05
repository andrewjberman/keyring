# 1.0.0_SA_CTO -- 2026-09-03 11:40-12:20Z -- the gate-model fork ruled; the audited override finally reaches the hook; two L2 retrofits

Inputs (READ-acked): MSTR relays of site Z 93568/93575/93591/93597 (CTO~Z's three uncommitted edits, then a commit
08497afdbe 67 s after the ruling relay, then its revert e3e7d8507b); 2.0.0_SA_COO 93578 (L6 refused ADVI_INSURE's
held NEVER-2 order on the ENDPOINT limb; the same wall before ADVI_49F); 3.0.0_SA_CVO 93581 (annex v2.3 mirrors the
ruling); 3.0.0_SA_CVO~A 93588 (round-2 dispositions change under the new shape; round 1 stands).

## Acts
1. GATE-MODEL RULING @ebe3a4caea + spine v2.6 @c699fb29b6: a NEW remediation row omits route/loop_target ONLY when
   remediation.state is REMEDIATED and, if ARMED, disarm.state is DISARMED -- a remedy executed inside the round is a
   member the route enum does not cover; every other route-less row stays refused. Five arms through _check_row with
   the committed schema; 11 of 11; corpus pass unchanged. Site Z discarded its fork; the merge leg carries the base's.
2. THE OVERRIDE, both carriers @6ec8f32d50: the audited '# surprise-row-override:' had NEVER worked on any path -- the
   wrapper audited and warned, the hook re-ran the gate blind and refused. safe-commit exports SURPRISE_ROW_OVERRIDE
   after its audit line; the gate honours it (WARN + rc 0); a raw commit has no variable and stays refused; the hook
   template is untouched. Exercised both ways with an injected violation on a real channel path. Site Z's 08497afdbe
   (the same export + a hook-template change) retired by revert; fork closed before the 12:17Z bound.
3. L2 RETROFITS (the L6 gate's fourth limb on running legacy projects): ADVI_INSURE @447605c7de (FWD-1..10 from s.1 +
   s.6; the gate's own check_endpoint_section on the held order: 0 violations, 'ENDPOINT section OK'); ADVI_49F in
   D2_ADVI_49F_E2E_PRD.md (FWD-1..6 from s.8 + s.1; predicate replicated on the register's prds[]). Andrew's
   confirmation of the DONE WHEN lines is a card; the loop does not wait on it. One commit refusal on the way was mine
   (a message file never written because a probe misread a 2-tuple as two violations) -- asked the repository, wrote
   the file, committed.

## Open, with owner
- Andrew: the two endpoints' DONE WHEN lines (16 cards) to confirm or dispute; the lifecycle-expiry card stands.
- 2.0.0_SA_COO: re-run the held INSURE order; cut ADVI_49F's against the new section.
