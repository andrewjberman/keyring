# TO NFRA_CTLPLN.TO-CT-ac-3 -- workstream FENCE round 1 (cell CT-ac-3): the fence-scoped check `check_fence_scoped_rows.py` re-baselined to today's registry and validator, under four rulings (row ADVI_FIRMBKTS-D1-S43, reasons 1, 3, 4)

<to_id>NFRA_CTLPLN.TO-CT-ac-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~89</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>FENCE</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ac-3` (`decompositions/NFRA_CTLPLN_DECOMP.round13.md`) | **outcome_ref:** FWD-5, FWD-10 |
**depends_on:** none (`CT-ab-2` is applied: the Dell users may call `iam:SimulateCustomPolicy`, and so may the laptop identity this cell runs as)

---

## WORKER FACE

### THE CELL

`infra/aws/terraform/shared-infra/tests/check_fence_scoped_rows.py` (707 lines; read its docstring first) proves the scoped-exemption renderer on scratch copies and prints one last line `FENCE-SCOPED rows_today=<n> unchanged_today=<bool> scoped_rendered=<k>/<m> sim_ok=<a>/<b> refusals_ok=<r>/<s> unknown_key_refused_by=<...> ok=<bool>`. MEASURED by the issuer at your base: `FENCE-SCOPED rows_today=42 unchanged_today=False scoped_rendered=0/0 sim_ok=0/0 refusals_ok=0/7 unknown_key_refused_by=none ok=False`, after `ERROR: root before_strip: init rc=1 ... while calling one(list) ... local.lgic_managed_firm_buckets is object with 2 attributes`. Read row `ADVI_FIRMBKTS-D1-S43` (file `org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md` about :6034-6054, fields `world_is` and `notes`) for the four measured reasons. Reason (2) of that row, the simulator denied to the dell1 identity, is CLEARED by `CT-ab-2`; the other three are yours, under these four RULINGS by the issuer (the row's `notes` asked for them):

- **(b) the pinned fence file's selector.** The PINNED file (commit `06c783b92b`, `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` about :194) selects `lgic_crm_scope = one([for k,s in local.lgic_managed_firm_buckets : s if length(lookup(s, 'masters', [])) > 0])`, which fails over today's registry (two rows). RULED: in the SCRATCH copy of the pinned file only (never the repository file), substitute that one selector line with the one HEAD's own file uses (`restricted_prefix_hosts`), and print one line `BASELINE-SUBSTITUTION selector: <the two lines>` in the output so the substitution is visible. If, after the substitution, a rendered statement OTHER than the selector's own result differs between the before and after renders, STOP and file a BLOCKING row; do not widen the substitution.
- **(c) arms 3 and 4.** The check's refusal cases 3 (a prefix without the trailing `/`) and 4 (actions including `s3:PutObject`) are not refused by `lib/opal_naming.py validate` at HEAD (the control is clean; cases 1, 2, 5, 6, 7 are refused). RULED: read the validator's history (`git log -S` on the rule text, and the registry's commit messages) and find whether those two rules were removed on purpose. If a commit or ruling shows they were, RETIRE the two arms: the denominator becomes 5/5, the output names each retired arm and the commit, and no other arm changes. If you cannot show it was deliberate, STOP on those two arms, file a BLOCKING row naming them, and do not edit the validator (outside your paths).
- **(d) the `grants` field.** `infra/logic/registry/exemptions.json` gained a top-level `grants` object since the first scoped row; `unchanged_today` reads False and `scoped_rendered` reads stale. RULED: `grants` is an admitted top-level field. `unchanged_today` must read the registry diff (never typed) and compare the render without scoped rows against the render at the commit before the first scoped row, attributing any difference exactly to the principals admitted unscoped and to the `grants` change, printing the attribution; it reads True only when nothing else differs. The expected counts of `scoped_rendered` are computed from the registry (never typed).
- **(f) the relocated adapter block (AMENDMENT 1, issuer 2.0.0_SA_COO~C, answering your row `NFRA_CTLPLN-W89-S1`).** Commit `057cfa8a1c` moved the irpt performance adapter's admission and its three `DenyPerformanceAdapter` statements out of `infra/aws/terraform/shared-infra/s3-49financial.tf` and into a scoped registry row. Stripping scoped rows therefore removes what the pinned render held. RULED: the residual is attributable when, and only when, BOTH hold, each read from git and the registry and never typed: (1) the residual in `opal_data_49financial` equals EXACTLY the lines `057cfa8a1c` removed from `s3-49financial.tf` (the adapter admission and the three `DenyPerformanceAdapter` statements, compared as a set of rendered statements); (2) today's registry carries a scoped row for the same adapter principal. Print `ATTRIBUTED relocation <principal>: <commit>` and count it beside the two other attributions (unscoped principals, `grants`). Anything else in the residual keeps `unchanged_today=False` and the UNATTRIBUTED line. Do not widen this beyond that commit and that one principal.
- **(e) the simulator.** The check's `sim_ok` arms call `iam simulate-custom-policy` for a synthetic principal (31 arms). Run them; they must answer. An AccessDenied is reported as such and the arm is not stubbed or skipped.

### BUILD

1. Edit ONLY `check_fence_scoped_rows.py` (and its own fixtures under that `tests/` folder if a fixture needs a refresh) to implement rulings (b), (c), (d); keep every other arm's meaning. Run it.
2. The final line must read `ok=True` with no environment override, `unchanged_today=True`, `sim_ok=<n>/<n>` with n above 0, `refusals_ok=<r>/<r>` (5/5 if arms 3 and 4 are retired), and `scoped_rendered=<k>/<k>`.
3. Report: each ruling applied with the lines changed, the count of arms before and after, and the full last line.

### RULES FOR THIS CELL

Write surface = the `<paths>`. The ONLY AWS calls permitted are `sts get-caller-identity` and `iam simulate-custom-policy`, through the `.tools/aws` shim, exactly as the check already makes them (its docstring); no terraform apply, no object read, no write of any kind, no push. `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink. Firm names live only under `tests/` in this file; the naming gate refuses a new firm token elsewhere (if it REFUSES a commit, STOP and file a BLOCKING row; never encode around it). ASCII only; Python 3.11. CLAUDE.md and org/XXX.md are LOCKED. The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W89-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTac3-AC1" cell_refs="CT-ac-3"><invocation>python infra/aws/terraform/shared-infra/tests/check_fence_scoped_rows.py</invocation><expect>unchanged_today=True</expect></criterion>
`CTac3-AC1` -- the unchanged-today arm reads True against today's registry (base: `unchanged_today=False`); report the whole last line.

<criterion id="CTac3-AC2" cell_refs="CT-ac-3"><invocation>python infra/aws/terraform/shared-infra/tests/check_fence_scoped_rows.py</invocation><expect>ok=True</expect></criterion>
`CTac3-AC2` -- the whole check reads `ok=True` with no override (base: `ok=False`); report the whole last line with every denominator.
</proof_of_spec>

<expected_criteria>CTac3-AC1,CTac3-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 300` (the check makes simulator calls; its results are cached in a temporary directory so a retry reuses them); record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~89/NFRA_CTLPLN.TO-CT-ac-3.fence-scoped-check-rebaseline.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTac3-AC1,CTac3-AC2`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round13.md</decomp_doc>
<owned_cells>CT-ac-3</owned_cells>
</decomp_ref>

<paths>
infra/aws/terraform/shared-infra/tests/check_fence_scoped_rows.py
infra/aws/terraform/shared-infra/tests/dell_fence_census.json
infra/aws/terraform/shared-infra/tests/dell_fence_join_pairs.json
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: RUN at the first simulate call -- denominator the 31 arms; the laptop identity's grant on `iam:SimulateCustomPolicy`; BLIND to the readers of the bucket policies.
comp-adversary: RUN -- an arm weakened to make ok=True (rulings (b)-(d) name every permitted change); the substitution widened beyond the selector line (the STOP clause); arms 3 and 4 retired without a commit showing the rule was removed on purpose (the STOP clause); a simulator AccessDenied stubbed (forbidden); BLIND: another consumer of the pinned fence file.
lane: the <paths> block IS the grant (worker RULING 1).
risk: WORLD is declared because the L6 gate derives a floor from the infra paths; this cell makes only read-only simulate calls.
</preflight>

Base checks, dry-run by the issuer before the cut: CTac3-AC1 base: FAIL as expected (`unchanged_today=False`); CTac3-AC2 base: FAIL as expected (`ok=False`).
Source: ROUND_ANALYSIS.round12.md section 3 item 4; row ADVI_FIRMBKTS-D1-S43; CTO msg 108726.
