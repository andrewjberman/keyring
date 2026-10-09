# TO MDPF_STRATID.TO-ST-u2 -- round 2 ST-u-2: Global's served record states, per strategy amount, whether it is also inside a Model figure
<to_id>MDPF_STRATID.TO-ST-u2</to_id>
<project>MDPF_STRATID</project>
<issued_to>0.9.0_WK_MDPF_STRATID~7</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `ST-u-2` (`decompositions/MDPF_STRATID_DECOMP_R2.md`) |
**outcome_ref:** FWD-6 | **depends_on:** ST-u-1

---

## WORKER FACE

### THE CELL

`ST-u-2`. FWD-6: nothing in Global is counted twice, and a person can see why. For any strategy amount in Global, a person can tell
whether it is also inside a Model figure, and an account set up to sit in both is held out once and named as held out. You run AFTER
`ST-u-1` in this same worktree. When you start:
- every Cottonwood `cohort_class: "sma"` member is either counted additive at Global or named in `sma_additive_withheld`
  (`{member_id, firm_id, date, value, reason}`);
- a Global additive `by_model` entry carries `firms`;
- each SMA member row of the Global category tree carries `by_firm`.

You add the STATEMENT. You change no number.

**The estate:** `data/mdpf/scripts/gold/mdpf_gold_consolidator.py`, namely `apply_sma_sleeve_overlay` (it writes
`inside_model_figure: False` hard-coded, ~:1863-1866) and the tree `_shape_category_views`. The Cottonwood slice's
`by_model[m]["overlap_model_value"]` is aligned to Cottonwood `dates`. It holds a float for the dollars of member m's sleeve accounts
also inside an Opal Model that date, or None where unmeasured.

**Build:**
1. **On each Global additive SMA `by_model` entry,** add the fields below:
   - `inside_model_value`: a list aligned to Global `dates`, holding the overlap dollars carried the same way the fold carries
     value, or None where unmeasured.
   - `inside_model_figure`: True on the frontier date when that overlap is > 0; False when it is 0.0; None when it is unmeasured.
     This replaces the hard-coded False.
2. **On each SMA member row of the Global category tree,** ETF Strategies and ALT Strategies alike, add:
   - `inside_model_figure`: a bool on the frontier date. It is True if any part of the member's dollars is held out as inside a
     Model, and False otherwise. A carve-out-only member (49financial) states False, and its `by_firm` basis says why.
   - `held_out`: the `sma_additive_withheld` entries for that member on the frontier date, as `{firm_id, value, reason}`, or `[]`.
3. **Move no number.** Every `aum`, total, `sma_additive_aua` and per-firm view stays byte-equal in value.
4. **Tests.** Create NEW `data/mdpf/tests/stratid/test_stratid_round2_inside_model.py`, with its own sys.path preamble, synthetic
   docs and no network, using these exact names:
   - `test_additive_entry_states_inside_model_value_per_date`
   - `test_tree_member_names_held_out_amounts`
   - `test_carve_out_member_states_it_is_not_inside_a_model`
   - `test_statement_moves_no_figure`

### ACCEPTANCE

<criterion id="ST2-u2-AC1" cell_refs="ST-u-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R2_CHECKS/st_u2_tests.py</invocation><expect>U2-OK</expect></criterion>
`ST2-u2-AC1` -- the four named tests pass.

<criterion id="ST2-u2-AC2" cell_refs="ST-u-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R2_CHECKS/st_u2_seam.py</invocation><expect>SEAM-OK</expect></criterion>
`ST2-u2-AC2` -- the seam on real data (read-only S3):
- every Global SMA tree member carries `inside_model_figure` and `held_out`;
- Cottonwood divz (overlap 1,369,280.57 on 2026-10-08) is named held out with reason `OVERLAP`;
- PFDE (overlap 0.0) states `inside_model_value` 0.0 and is not held out.

<criterion id="ST2-u2-AC3" cell_refs="ST-u-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R2_CHECKS/st_u2_regress.py</invocation><expect>U2-REGRESS-OK</expect></criterion>
`ST2-u2-AC3` -- ST-u-1's three checks still pass.

<expected_criteria>ST2-u2-AC1 ST2-u2-AC2 ST2-u2-AC3</expected_criteria>

Run each invocation from the worktree root. At the base (2026-10-09 ~16:08Z):
- AC1: `U2-BAD no file ...`
- AC2: `SEAM-BAD tree member ETF Strategies/divz lacks inside_model_figure or held_out`
- AC3: FAILS until ST-u-1 lands.

## BOUNDS

- **Grant.** Your write grant is the `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes
  under `.scratch/` and is not committed.
- **Read-only AWS only.** No S3 write, no Lambda invoke, no deploy.
- **Edit nothing else.** Do not edit the registry, and change no number the fold computes.
- **Client data, hard bound (0.0.0_AB_MSTR~DELL1 msgs 2721, 2748, 2767).** Do NOT open, search, copy, `git show` or `git log -p`:
  - any `org/**/W73_S*_EVIDENCE.json` or `W73_S2_RESOLUTION.json`;
  - anything under `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/`;
  - any COTBKF or cottonwood account manifest of other workers.
- **Refusal clause.** Same as `ST-u-1`:
  - stop, and write the reason in your report;
  - append a row `MDPF_STRATID-W7-S<k>` to the investigation file below (APPEND-ONLY);
  - do not weaken a check.

<paths>
data/mdpf/scripts/gold/mdpf_gold_consolidator.py
data/mdpf/tests/stratid/test_stratid_round2_inside_model.py
org/missions/D8/MDPF/MDPF_STRATID/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_STRATID/decompositions/MDPF_STRATID_DECOMP_R2.md</decomp_doc> (round 2, workstream 1), cell `ST-u-2`.
<owned_cells>ST-u-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: ST2-u2-AC1, ST2-u2-AC2, ST2-u2-AC3. Instance at `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~7/MDPF_STRATID.TO-ST-u2.inside-model-stated-per-amount.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> ST2-u2-AC1 ST2-u2-AC2 ST2-u2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule change.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call added.
comp-adversary: RUN in the decomposition battery; this cell's hazard (a statement that moves a number) is AC1's test_statement_moves_no_figure. -- coverage: scanned the 6 Global SMA tree members (ETF Strategies 4, ALT Strategies 2) on the served 2026-10-08 view; blind to the portal, which renders none of these fields (frontend is out of scope by the PRD BOUNDARY).
risk: SERVED -- new fields on Global's served output once deployed at the drain under the C-GLOBAL-PAIR.
direct_act: false -- the class is SERVED.
</preflight>

Source: PRD v0.3 ENDPOINT FWD-6, C-OVERLAP; decomposition round 2.
