# TO MDPF_SECCLASS.TO-SC-e62 -- round 10 SC-e-62: W38-S6 + SC-e-22: the HoldingsSnapshot class enum loses multi_asset in its three copies, and the two Holdings tests encode the six-class rule

<to_id>MDPF_SECCLASS.TO-SC-e62</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~51</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-62` (`decompositions/MDPF_SECCLASS_DECOMP_R10.md`) |
**outcome_ref:** FWD-2, FWD-13, FWD-16 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-62`. CTO round-9 analysis ruling 2.3: "SC-e-22 (the `HoldingsSnapshot` enum loses `multi_asset`) and the two Holdings tests land
together, before SC-e-56." Andrew-direct 2026-10-07, as recorded in the contract: six classes only, no `multi_asset`.

**Your base is the held branch `q/dell1/secclass-r9-held-38/r1` (4cb237fe22).** It carries SC-e-56. There,
`data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` `ASSET_CLASS_VALUES` (~:846) no longer holds `multi_asset` (it holds
the six classes plus `other` and `unclassified`), and row W38-S6 shows two failures, 2 failed and 34 passed over the two files below:
- `data/assets/scripts/gold/investor_reporting/tests/test_holdings_snapshot.py::test_every_published_asset_class_enum_is_the_producers_list`
  (~:427) asserts `"multi_asset" in hs.ASSET_CLASS_VALUES`, and that the published contract enums equal the producer list;
- `data/assets/scripts/gold/investor_reporting/tests/test_holdings_narrowed.py::test_a_canonical_multi_asset_row_is_served_not_refused`
  asserts a canonical `multi_asset` row is served.

A consistent full scan (2026-10-07) found 0 `multi_asset` rows in `etf-classifications` and 0 in `bd-securities`.

**Build:**
1. Remove `multi_asset` from every asset-class enum in the three schema copies, so each equals the producer's `ASSET_CLASS_VALUES`
   exactly:
   - `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`
   - `infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json`
   - `infra/aws/lambda/investor-reporting/holdings/contracts/HoldingsSnapshot.schema.json`
   Change nothing else in them.
2. Add one entry to `infra/aws/terraform/investor-reporting/CHANGELOG.json` in its existing shape, naming the enum change and MDPF_SECCLASS
   SC-e-22.
3. In `test_holdings_snapshot.py`, the equality test asserts `multi_asset` is NOT a producer value and that the published enums still
   equal the producer list.
4. In `test_holdings_narrowed.py`, the multi_asset test becomes `test_a_canonical_multi_asset_row_is_refused_loudly`. It asserts the
   refusal the producer now raises.
5. Do not touch `holdings_snapshot.py`.

### AMENDMENT 1 (issuer, 2.0.0_SA_COO~M1, 2026-10-07 ~15:5xZ; release mode, CTO round-11 analysis @fc96f7c48c section 2 item 2)

**The release port.** e62 (c90cbf057f, ~43) and e56 (39043b3f90, ~38) are complete and VALID on the held-38 line. Their files
cherry-pick CLEAN onto the round head ae61f93efe (CLOUD plus round records): 0 conflicts, the IR Holdings suite 340 passed, and
`sc_e62_holdings_enum_equal.py` ok (15 enums, 1 distinct). They must land together: e62's enum tests assume e56's `ASSET_CLASS_VALUES`.

Slot ~51 on branch `secclass-r12-rel-e62e56` commits that port without e55, e57 or e61. The issuer's lane refuses these paths.

**Your work:** the eleven files below are ALREADY STAGED in your worktree (the issuer's cherry-pick, uncommitted). Do not rebuild.
1. Confirm each file's blob equals its source commit: `git rev-parse :<path>` against `git rev-parse 39043b3f90:<path>` or
   `c90cbf057f:<path>`.
2. Commit them.
3. Run AC1 and AC2, plus the IR Holdings suite as a control.
4. Write and validate the proof instance (slot ~51), flip status to complete, and commit.

### ACCEPTANCE

<criterion id="SC10-e62-AC1" cell_refs="SC-e-62"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/sc_e62_holdings_enum_equal.py</invocation><expect>SC-E62 ok=True</expect></criterion>
`SC10-e62-AC1` -- every class enum in the three copies equals the producer's list, and none holds `multi_asset`.
The check reads the tree it is run from (your worktree root).

<criterion id="SC10-e62-AC2" cell_refs="SC-e-62"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/assets/scripts/gold/investor_reporting/tests/test_holdings_snapshot.py data/assets/scripts/gold/investor_reporting/tests/test_holdings_narrowed.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC10-e62-AC2` -- the two Holdings test files pass under the six-class rule.

<expected_criteria>SC10-e62-AC1,SC10-e62-AC2</expected_criteria>

Dry-run at the base (4cb237fe22, 2026-10-07): SC10-e62-AC1 FAIL as expected (15 schema enums, 2 distinct, `multi_asset_in_any=True`); SC10-e62-AC2 FAIL as expected (2 failed, 34 passed).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment;
  rows S49, S54).
- No Terraform, no deploy, no publish of the contract. Your branch rides the held-38 line: the laptop CTO reviews it before DEV or release
  (ruling 2.3), and SC-e-56's release goes through IRPT_BCKEND. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W51-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_cusip_fallback.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_narrowed.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_snapshot.py
docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json
infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json
infra/aws/lambda/investor-reporting/holdings/contracts/HoldingsSnapshot.schema.json
infra/aws/terraform/investor-reporting/CHANGELOG.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/HOLDINGS_CUSIP_NEWLY_PLACED_20261007.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_HOLDINGS_CUSIP_LOOKUP_20261007.md
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/holdings_cusip_newly_placed.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R10.md</decomp_doc> (round 10), cell `SC-e-62`.
<owned_cells>SC-e-62</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC10-e62-AC1, SC10-e62-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~51/MDPF_SECCLASS.TO-SC-e62.holdings-enum-six-class.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC10-e62-AC1,SC10-e62-AC2` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** the enum before and after per copy, the CHANGELOG entry, both test changes, AC1/AC2 outputs, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a contract and test change schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no role or grant changes.
comp-adversary: RUN -- W38-S6; a copy left behind (AC1 reads all three and the producer); a test deleted instead of re-stated (refusal clause); BLIND: portal readers of the published enum (SC-e-23's held candidate already drops the value; the laptop CTO review).
lane: the <paths> block IS the grant; base is the held-38 line by issuer ruling in DECOMP_R10.
</preflight>

Source: round-9 analysis @9b6348f15e section 2.3, section 3 item 3; row W38-S6; PRD v0.14 (ADMITTED); DECOMP_R10; SC-e-22's write set from the round-6 decomposition.
