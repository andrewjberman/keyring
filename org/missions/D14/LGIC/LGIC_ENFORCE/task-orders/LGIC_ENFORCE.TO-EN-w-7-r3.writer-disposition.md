# TO LGIC_ENFORCE.TO-EN-w-7-r3 -- DEC-4(ii) for R-20's four legacy writers, and the applied fence still equal to the builder

<to_id>LGIC_ENFORCE.TO-EN-w-7-r3</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-16</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.3 (ADMITTED; both halves current) | **Decomp cell:** `EN-w-7` = round-3 cell 7 (decomposition v3.2, section 0c) | **outcome_ref:** FWD-2 | **depends_on:** EN-r-5-r3 (same slot, runs after it)

---

## WORKER FACE

### THE CELL

`EN-w-7` -- the fence's existing-writer disposition (DEC-4(ii) in `../prd/LGIC_ENFORCE_PRD.md`; RULINGS R-20 and R-25 in `org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md`).

**WHAT IS ALREADY DONE, so you do not redo it.** The GENERATED, deny-by-default fence is APPLIED on `opal-data-49financial` (round 1, EN-f-2; ledger `org/critical_paths/change_management/20260915T0334Z_lgic-enforce-fence-49financial_deploy_completion.md`, CLOSED 4 of 4 legs; the three probe roles were created, exercised and destroyed). R-25 rules FWD-2's EXERCISED bar met by that round-1 probe. **You do not re-apply the fence and you do not mint probe roles.**

**WHAT IS YOURS.** R-20 measured four live IAM roles carrying a firm key but LEGACY-NAMED, so the generated fence catches none: `irpt-core-firm-49financial`, `irpt-core-firm-inflection`, `irpt-core-firm-cottonwood`, `demo-transform-runner-ec2-role`. For each, write ONE disposition to `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/FENCE_WRITER_DISPOSITION.r3.json`, shape `{"rows": [{"role": ..., "bucket": ..., "disposition": ..., "evidence": ...}]}`, the bucket being that firm's (`opal-data-49financial`, `-inf`, `-cot`, `-demo`):
- **`NOT_A_PRINCIPAL`** -- the role did not read or write that bucket in the window, from the CloudTrail data events live on those buckets (DEC-4(ii)), evidence stating the query, window and result count. **`evidence` of at least 40 characters.**
- **`EXEMPTED`** -- the role is a real principal of that bucket; add it to `infra/logic/registry/exemptions.json` under that bucket with its reason, then `python lib/opal_naming.py generate` (which re-stamps `generated_locals.tf` and the two test fixtures).
- **`RENAMED`** -- only if the role's OWNER has already renamed it under `name()`; a rename is NEVER yours (R-20).

**THE ONE STOP.** An `EXEMPTED` row under `opal-data-49financial` changes the APPLIED Deny, so it needs never-widen sign-off by `1.0.0_SA_CTO` AND `2.0.0_SA_COO` BEFORE any apply (NEVER #1), naming the principal whose access changes and the rollback (the prior policy, kept verbatim in a change-management ledger entry). You cannot obtain that sign-off: **file a BLOCKING row naming the principal and its evidence, do not apply, and finish every other row.** Exemptions under `-inf`, `-cot` and `-demo` change no applied policy (no fence is applied on those buckets) and need no apply.

**AT CLOSE the applied Deny must still equal the builder's output** (R-25's regression read) -- if you added no `opal-data-49financial` exemption, it does so unchanged.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="W7R3-AC1" cell_refs="EN-w-7"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py w7-writers-dispositioned org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/FENCE_WRITER_DISPOSITION.r3.json</invocation><expect>PASS-W7-WRITERS-DISPOSITIONED</expect></criterion>

<criterion id="W7R3-AC2" cell_refs="EN-w-7"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py regress-w7-applied-deny</invocation><expect>PASS-W7R-APPLIED-DENY-EQUALS-BUILDER</expect></criterion>

<criterion id="W7R3-AC3" cell_refs="EN-w-7" judgment="true"/>

<expected_criteria>W7R3-AC1, W7R3-AC2, W7R3-AC3</expected_criteria>

**AC1 reads RED at the cut** (no disposition file; none of the four named in `exemptions.json`). It confirms each disposition against the ARTIFACT, not your word: EXEMPTED must be present in `exemptions.json` with a reason, RENAMED is re-measured absent on the live plane. **AC2 reads PASS at the cut** (17 of 17: one pattern plus 16 exemptions) and must still PASS at your close; it reads the real bucket's policy live. **W7R3-AC3, for `3.0.0_SA_CVO` at L9:** each NOT_A_PRINCIPAL's CloudTrail evidence names its query, window and count, and any BLOCKING row for an `opal-data-49financial` exemption names the principal and its evidence.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, including `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py`. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot). Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **A value that must be read from the estate is read with the instrument this order names**, and its denominator is printed beside it.
- **No apply without the sign-off above.** No rename of any role. No edit to the bucket policy by hand -- it is generated.
- **Do not edit `systems.json`, `scopes`, `tiers` or `resources`.** `systems.json` is the previous cell's.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
infra/logic/registry/exemptions.json
infra/aws/terraform/modules/opal_name/generated_locals.tf
infra/aws/terraform/modules/opal_name/tests/vectors.json
infra/aws/terraform/modules/opal_name/tests/opal_name.tftest.hcl
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.2, round-3 cell 7 (section 0c; the v3.1 and v3.2 amendments).
<owned_cells>EN-w-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `W7R3-AC1`, `W7R3-AC2`, `W7R3-AC3`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/LGIC_ENFORCE.TO-EN-w-7-r3.writer-disposition.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> W7R3-AC1,W7R3-AC2,W7R3-AC3 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-w-7-r3.writer-disposition.md` BEFORE the `complete` flip.
Result file `writer-disposition.r3.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`W7R3-AC3` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-3 cut. This cell is gated by G-C and by EN-r-5-r3's drain (same slot).
comp-iam: RUN -- the four roles are live principals; the disposition reads CloudTrail data events and an EXEMPTED row under opal-data-49financial changes an applied resource policy, which is held for never-widen sign-off.
comp-adversary: RUN -- NOT_A_PRINCIPAL is the tempting disposition; W7R3-AC3 grades its CloudTrail evidence, and AC1 re-measures RENAMED on the live plane.
lane: exemptions.json PLATFORM_LOGIC_DOCS, the opal_name module files, the change-management ledger and sentinel directories; the <paths> block is the grant (R-23).
contention: the two opal_name test fixtures are also regenerated by EN-r-5-r3, which runs first in this slot.
</preflight>

Seating: slot ~2, queue position 2. Round 3 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-2 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND2_20260916.md`); issued by `2.0.0_SA_COO~G`. Decomposition v3.2, section 0c. Rulings carried: DEC-4, R-20, R-23, R-25, R-16.
