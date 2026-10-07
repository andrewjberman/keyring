# TO MDPF_SECCLASS.TO-SC-e50 -- round 9 SC-e-50: FWD-17 -- the whole old list counted under the held definition, and the reclassification set refreshed with the cash rows re-planned under the contract bound

<to_id>MDPF_SECCLASS.TO-SC-e50</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~36</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-50` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-17 | **depends_on:** MDPF_SECCLASS.TO-SC-e54 (the contract's `sub_asset_class.values_by_class`, the bound the cash
rows are planned under). Slot `~36`, third in its queue; the issuer hands it once `TO-SC-e54` has drained.

---

## WORKER FACE

### THE CELL

`SC-e-50`: "FWD-17 (2.4, 2.5): the whole-old-list census under the held definition (non-zero market value in the latest served
holdings partition; dell1 reads `inferred`, a served grade is a laptop seat's row), and the reclassification set refreshed with the
15 cash rows re-planned under the contract bound" (DECOMP_R9). Rulings, verbatim
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md`):
- **2.4:** "The population is the whole old list, held or not (FWD-17's own ACCEPT: 'held today or not'), counted at the round-9
  census with its denominator. 'Held' means present with a non-zero market value in the latest served holdings partition of any of
  the three firms on the census as-of. It is read by a seat whose principal the firm buckets admit (2.9). The '58' is retired."
- **2.5:** "The contract's closed `sub_asset_class` list is the bound for every class, cash included. A DIRECT or AI verdict lands if
  it is a member of the contract's list, not only of the values the table happens to hold. The 15 old cash rows are re-planned under
  that bound."
- **2.9:** until a read-only grant lands, "dell1 grades every held set as `inferred`, and a grade that needs the served bytes is read
  by a laptop seat and filed as a row".

**Round 8's inputs (`M/` = `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/`):** `M/OLD_LIST_CENSUS_20261007.json`
(TO-SC-e26: 10,965 `bd-securities` rows; held 3,152 from local builds), `M/OLD_LIST_RECLASSIFY_SET_20261007.tsv` (TO-SC-e32: header
`old_key shared_key held route asset_class sub_asset_class clean_name`; present 2,381, direct 5,796, ai 2,785, unplaced 3), its
planner `M/R10_CHECKS/old_list_reclassify_set.py`, and row W26-S6 (the 15 cash rows could not land: the table holds 0 cash rows).

**Build (NO table write, NO model call):**
1. `M/R11_CHECKS/old_list_census_held.py`: one consistent scan of `bd-securities` (the denominator), and each firm's held set as a
   LOCAL producer build (`data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` without `--upload`, via
   `M/R10_CHECKS/old_list_census.py` `build_firm()`, as-of the newest date the builds reach); held = a non-zero market value on that
   as-of. Writes `M/OLD_LIST_CENSUS_HELD_20261007.json` with `as_of, held_definition` (quote ruling 2.4's sentence), `claim:
   "inferred"`, `denominator, held, not_held, per_firm`, and names the served-bytes read as a laptop act in a `served_read` field.
   Print `OLD-LIST-CENSUS-HELD denominator=<n> held=<n> not_held=<n> claim=inferred`.
2. `M/OLD_LIST_RECLASSIFY_SET_V2_20261007.tsv`: round 8's set refreshed with step 1's `held` column and re-planned under the
   contract bound: every DIRECT or AI row's `sub_asset_class` is a member of `values_by_class[asset_class]`; the cash rows are
   re-planned (W26-S6). Reuse round 8's planner logic; you may copy it into a new file under `.scratch/`, never edit it.
3. ASCII only.

### ACCEPTANCE

<criterion id="SC9-e50-AC1" cell_refs="SC-e-50"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/old_list_held_census_check.py census</invocation><expect>OLD-LIST-HELD-CENSUS ok=True</expect></criterion>
`SC9-e50-AC1` -- the census's denominator is the live old list, held plus not-held sums to it, the held definition is ruling 2.4's,
and the claim is inferred.

<criterion id="SC9-e50-AC2" cell_refs="SC-e-50"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/old_list_held_census_check.py set</invocation><expect>OLD-LIST-SET-V2 ok=True</expect></criterion>
`SC9-e50-AC2` -- every old key once, every placed verdict inside the contract's bound for its class, cash rows planned.

<expected_criteria>SC9-e50-AC1,SC9-e50-AC2</expected_criteria>

Dry-run at the base 5d70aab6c9: AC1 FAIL as expected (`missing=OLD_LIST_CENSUS_HELD_*.json`); AC2 FAIL as expected
(`missing=OLD_LIST_RECLASSIFY_SET_V2_*.tsv`; it also refuses until SC-e-54's bound exists).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
- **No table write, no model call, no upload of any producer build.** The reclassification write is the issuer's act under its pair.
  Read no firm bucket by any route the box's principal is denied; assume no role.
- Do not edit round 8's planner, the contract or the producer; the R11 issuer check is READ-ONLY to you.
- **No package install and no download of any kind** (row S49). On this box no run counts trading days before 2010-01-01.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W36-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/old_list_census_held.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_CENSUS_HELD_20261007.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_RECLASSIFY_SET_V2_20261007.tsv
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-50`.
<owned_cells>SC-e-50</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e50-AC1, SC9-e50-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~36/MDPF_SECCLASS.TO-SC-e50.old-list-held-census-and-set-v2.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e50-AC1,SC9-e50-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the census line, the as-of the builds reached per firm, the set's counts per route against round 8's, every cash row's
planned sub-class, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a census and a row set; nothing is scheduled.
comp-iam: RUN -- round 8 (W25-S1): dell1 is denied the firm buckets; held sets are local builds, inferred; the read-only fence join for dell1 is asked of NFRA_CTLPLN (1.0.0_SA_CTO~DELL1 msg 195).
comp-adversary: RUN -- rulings 2.4, 2.5, 2.9 read; round 8's census (10,965) and set counts; the check refuses until SC-e-54's bound exists. BLIND: the served-bytes held grade (a laptop seat's row).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.13 FWD-17 @90f99888cd; analysis rulings 2.4, 2.5, 2.9 @1ca9e97fc9; DECOMP_R9 @5d70aab6c9; TO-SC-e26, e32 (round 8).

## AMENDMENT 1 (2.0.0_SA_COO~M1, 2026-10-07 ~12:4xZ) -- ruling on BLOCKING row W36-S4: the set check grades what exists before the model runs

AC2 graded AI-routed rows against the contract bound, but an AI row has no verdict until the model runs, which this order bars. The
issuer's check is amended (the defect was the check's): DIRECT rows are graded against the bound as before; AI rows must be BLANK in
asset_class and sub_asset_class; the bound on the AI path is graded on its output, after its own half. Issuer controls: the worker's set at
8be44af815 reads `ok=True rows=10965 direct=5811 ai=2770 cash_planned=15`; one AI row prefilled reads `ok=False ai_prefilled:ADC`.
AC2's invocation and expectation are unchanged. Re-run AC2, update the proof instance, flip. Gate limb: none graded this modification.
