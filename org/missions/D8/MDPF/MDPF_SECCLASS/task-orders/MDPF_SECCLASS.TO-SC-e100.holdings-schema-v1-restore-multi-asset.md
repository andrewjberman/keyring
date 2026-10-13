# TO MDPF_SECCLASS.TO-SC-e100 -- round 24 SC-e-100: restore `multi_asset` in the frozen v1 HoldingsSnapshot schema (three copies), with a test that the producer emits it on 0 rows

<to_id>MDPF_SECCLASS.TO-SC-e100</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~90</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>24</round>
<workstream>~M1.schema</workstream>

**Risk note:** declared WORLD because `<paths>` names `infra/aws/lambda/...` (the gate's path floor, spine v3.19 L6); the cell is a repo edit and deploys nothing. **Workstream:** `~M1.schema`, a second workstream of the project (the gate's own rule: its write surface is disjoint from SC-e-99's, and its source is the CTO's addendum, not the first issuance).

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-100` (`decompositions/MDPF_SECCLASS_DECOMP_R24.md`, addendum 1) |
**outcome_ref:** FWD-1 | **depends_on:** none | **source:** CTO round-23 analysis ADDENDUM 2 (msg 4622) on `1.0.0_SA_CTO~DELL2` msg 6784 (relayed by
`0.0.0_AB_MSTR~DELL1` msg 4620)

---

## WORKER FACE

### THE CELL

`SC-e-100`. Commit `01e843ce2e` (this project's `TO-SC-e62` release port, 2026-10-07, worker ~51) removed the class `multi_asset` from the five
asset-class enums of the **frozen v1 HoldingsSnapshot schema**, in each of its three copies:
`docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`, `infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json` and
`infra/aws/lambda/investor-reporting/holdings/contracts/HoldingsSnapshot.schema.json`. A frozen v1 admits additive members only: a narrowing belongs in a
v2. The producer's six-class rule (`data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` :852, `ASSET_CLASS_VALUES`, "the table holds 0 rows;
the six-class rule refuses it") stays exactly as it is: enforcement is at the producer, not by narrowing the contract. Nothing is served or deployed by this
cell: it is a repo change to three schema files and one test.

1. **Restore the members.** Re-insert the member `"multi_asset",` in each of the 5 enums of each of the 3 copies, in the position it had: between
   `"commodities",` and `"cash",`, same indentation. Do NOT restore the whole file from before the port: the three copies carry later additive changes
   (`7ace854890`, the account_* members). The clean way: `git diff 01e843ce2e^ 01e843ce2e -- <the three paths> | git apply -R`; if that does not
   apply cleanly, insert the 15 lines by hand. Nothing else in the three files changes (the check below proves it byte for byte against trunk).
2. **Add `data/assets/scripts/gold/investor_reporting/tests/test_holdings_multi_asset_v1_enum.py`**, a pytest in the style of its siblings
   (`test_holdings_narrowed.py`, `test_holdings_snapshot.py`, `test_holdings_publish_gate.py`: read them first), with no AWS call, covering:
   (a) each of the three copies' asset-class enums admits `multi_asset` (5 places per copy: count them, do not assume);
   (b) the producer path emits `multi_asset` on **0 rows**: build a snapshot from a fixture that carries a classification row whose class is
   `multi_asset` and assert no emitted node has `asset_class == "multi_asset"` (the six-class rule maps or refuses it as the producer does today;
   say in the test's docstring which one it is, from the code you read);
   (c) the three copies are the same set of members (a drift guard between the copies).
3. **If an existing test breaks** because it encoded the narrowed enum (for example the helper `_contract_admits_multi_asset` in
   `test_holdings_publish_gate.py`, whose docstring says the v1 enum "already rejects multi_asset at validation"): change ONLY that helper or assertion to
   the restored truth, state each change in your report, and weaken nothing else. Measure the four sibling test files at the BASE first
   (`test_holdings_publish_gate.py`, `test_holdings_narrowed.py`, `test_holdings_snapshot.py`, `test_holdings_cusip_fallback.py`) and report their
   pass counts before and after. (`test_holdings_rearm_trigger.py::test_rearm_trigger_live` already FAILS at the base: it is a live AWS check, not this
   cell's, and is out of the criteria.)
4. **Do not deploy, push or edit** the producer, `CHANGELOG.json` or any lambda package: the `_contracts` copy ships with the lambda code, and
   whether and when a new package is built is IRPT_BCKEND's act, which this cell names in your report and does not take.

### ACCEPTANCE

<criterion id="SC24-e100-AC1" cell_refs="SC-e-100"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R24_CHECKS/r24_multi_asset_restore_check.py</invocation><expect>MULTI-ASSET-RESTORE ok=True</expect></criterion>
`SC24-e100-AC1` -- all three copies carry `multi_asset` in 5 enums each, between `commodities` and `cash`, and the files minus those 15 lines equal trunk byte for byte.

<criterion id="SC24-e100-AC2" cell_refs="SC-e-100"><invocation>python -m pytest data/assets/scripts/gold/investor_reporting/tests/test_holdings_multi_asset_v1_enum.py -q</invocation><expect>passed</expect></criterion>
`SC24-e100-AC2` -- the new test file passes (the contract admits `multi_asset` in all copies, the producer emits it on 0 rows, the copies agree) and reports no `failed`.

<criterion id="SC24-e100-AC3" cell_refs="SC-e-100"><invocation>python -m pytest data/assets/scripts/gold/investor_reporting/tests/test_holdings_publish_gate.py data/assets/scripts/gold/investor_reporting/tests/test_holdings_narrowed.py data/assets/scripts/gold/investor_reporting/tests/test_holdings_snapshot.py data/assets/scripts/gold/investor_reporting/tests/test_holdings_cusip_fallback.py -q</invocation><expect>passed</expect></criterion>
`SC24-e100-AC3` -- the four sibling holdings test files pass as at the base (or with only the helper change item 3 allows), and report no `failed`.

<expected_criteria>SC24-e100-AC1, SC24-e100-AC2, SC24-e100-AC3</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-13 ~04:3xZ): AC1 FAIL as expected (`MULTI-ASSET-RESTORE ok=False copies=0 of 3 members=0 ...`); a
minimally restored set of temp copies (15 lines inserted) passes every arm of the check and one with an extra edit fails the byte-equality arm; AC2
FAIL as expected (the file is absent); AC3 is measured at the base by you (item 3).

### AMENDMENT 1 -- the drift guard becomes "the contract admits the producer's six, plus the one retired member" (issuer 2.0.0_SA_COO~M1, 2026-10-13 ~05:0xZ; answers your rows MDPF_SECCLASS-D1-W90-S1 and S2)

Your stop was right, and the failing test is the other half of the same narrowing. `test_holdings_snapshot.py::test_every_published_asset_class_enum_is_the_producers_list`
asserts `sorted(enum) == sorted(hs.ASSET_CLASS_VALUES)`: the port (`01e843ce2e`, e62) made the contract enum EQUAL the producer's six, and this test pinned
that. The CTO's ruling (round-23 analysis ADDENDUM 2, msg 4622) is that the frozen v1 contract keeps its additive-only shape and the six-class rule is
enforced AT THE PRODUCER. Andrew's own word (`ANDREW_DIRECT_20261007_004xZ_NO_MULTI_ASSET_CLASS_SIX_CLASSES_ONLY.md`) is six classes, no `multi_asset`,
and it routed "the Holdings contract's `multi_asset` entries" to `1.0.0_SA_CTO`, who has ruled: the producer's values stay six (this test's first assertion,
`"multi_asset" not in hs.ASSET_CLASS_VALUES`, STAYS), the contract admits the retired member.
1. **Edit that one test.** In `data/assets/scripts/gold/investor_reporting/tests/test_holdings_snapshot.py` change ONLY
   `test_every_published_asset_class_enum_is_the_producers_list`: keep the schema load, the three enums and the `"multi_asset" not in hs.ASSET_CLASS_VALUES`
   assertion; replace the equality loop with, for each enum: `set(hs.ASSET_CLASS_VALUES) <= set(enum)` (the contract admits every class the producer
   emits) and `set(enum) - set(hs.ASSET_CLASS_VALUES) == {"multi_asset"}` (the ONE extra member is the frozen v1 member and nothing else: any other drift
   still fails). Rewrite its leading comment to say so: six classes only at the producer (Andrew-direct 2026-10-07, SC-e-22); the frozen v1 contract is
   additive-only and keeps `multi_asset` (CTO round-23 ADDENDUM 2); enforcement at the producer, not by narrowing the contract.
2. **Fix the helper's docstring** in `test_holdings_publish_gate.py` (`_contract_admits_multi_asset`): it says the enum "already rejects multi_asset at
   validation (a build defect, a bare raise)"; after the restoration that is false. Make the docstring true (the contract now admits it; the helper
   keeps the gate test independent of the contract's content) and change nothing else there. If the helper's monkeypatch is now a no-op, say so in
   your report and leave it (not your cell's to remove).
3. **The grant grows by one path:** `data/assets/scripts/gold/investor_reporting/tests/test_holdings_snapshot.py`. Everything else in your `<paths>`
   and `<bounds>` stands. Row W90-S1 (BLOCKING, ARMED) is dispositioned by items 1 and 3; W90-S2 by item 2.
4. **Re-run** AC1, AC2 and AC3 (AC3 must now read all four sibling files green: the base's 70 and your 8 new), validate the proof instance, flip
   `complete` only when all three pass, commit with the grown path list and report as before.
5. **Gate limb.** The issuer amends its own criteria and grant without a CTO ruling; no gate limb grades an amendment to an existing order's criteria and
   `<status>` (this order declares `<placeholders>NONE`; a path added to a new-in-this-round order's grant is the issuer's own).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind.**
- **No AWS call** of any kind is needed or allowed in this cell. Never push. No deploy, no lambda package, no terraform.
- **Never edit** the producer `holdings_snapshot.py`, `CHANGELOG.json`, `.tools/`, or any file outside `<paths>`; the schema files are edited ONLY by
  inserting the 15 member lines.
- **Refusal clause.** If a criterion cannot be met as written (for example the reverse patch applies to a file that has since been restructured), stop.
  Write the reason in your report and file a surprise row (id `MDPF_SECCLASS-D1-W90-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not
  weaken the check and do not change another line of a frozen contract.

<paths>
docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json
infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json
infra/aws/lambda/investor-reporting/holdings/contracts/HoldingsSnapshot.schema.json
data/assets/scripts/gold/investor_reporting/tests/test_holdings_multi_asset_v1_enum.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_publish_gate.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. (`test_holdings_publish_gate.py` only per item 3.)

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R24.md</decomp_doc> (round 24, addendum 1), cell `SC-e-100`.
<owned_cells>SC-e-100</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC24-e100-AC1, SC24-e100-AC2, SC24-e100-AC3. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~90/MDPF_SECCLASS.TO-SC-e100.holdings-schema-v1-restore-multi-asset.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC24-e100-AC1,SC24-e100-AC2,SC24-e100-AC3`.
</proof_of_spec>

**REPORT:** the reverse patch's result per file, the count of members per copy, the base and after pass counts of the four sibling test files, each
changed line outside the 15 member lines (there should be none; the test helper change only if item 3 applied), commits, rows, and what the IRPT_BCKEND
seat must do next for the lambda package (named, not done).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a repo edit of three contract files and a test schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no cloud call of any kind.
comp-adversary: RUN -- a restoration that is not byte-minimal (the check compares the files minus the 15 member lines to trunk byte for byte); a restoration at the wrong position (the check requires `commodities` above and `cash` below each member); a test that passes because the fixture never carries a multi_asset class (item 2b requires a fixture row that does, and the worker names the producer's mapping); a quiet edit of a frozen contract beyond the 15 lines (the check is the discriminator). BLIND: consumers of the contract that validate historical snapshots (none is in this repo's tests); the CTO of IRPT_BCKEND owns the deploy and the downstream read.
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-23 analysis ADDENDUM 2 (msg 4622) answering `1.0.0_SA_CTO~DELL2` msg 6784 via `0.0.0_AB_MSTR~DELL1` msg 4620; commit
`01e843ce2e` (TO-SC-e62 release port); DECOMP_R24 addendum 1.
