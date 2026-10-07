# TO MDPF_SECCLASS.TO-SC-e55 -- round 9 SC-e-55: C-S13: 49 Financial's firm mix serves its residual as its own Unclassified line, so the top-level mix sums to 1.0

<to_id>MDPF_SECCLASS.TO-SC-e55</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~53</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>in_progress</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-55` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-2, FWD-13 | **depends_on:** none (slot ~38 queue: this order, then TO-SC-e57, then TO-SC-e56)

---

## WORKER FACE

### THE CELL

`SC-e-55`. Round-8 analysis section 3, C-S13 (REMEDIATION_v6): "the residual is served as its own line, 'Unclassified', so the
top-level mix sums to 1.0. That matches FWD-13's rule that a security the list does not hold is shown as unclassified. Owner
`2.0.0_SA_COO~M1`; a served move under its own pair."

**Measured by 3.0.0_SA_CVO (C-S13):** the served `s3://opal-data-bd/platinum/firm/mix_summary.json` (2026-10-07T05:49Z, as-of
2026-10-05): sum(mix.pct) = 0.9967614; sum(mix.market_value) = 2,001,258,931.56 against `mix_periods[2026-Q4].total_aua` =
2,007,761,226.11 (about $6.5M in no class).

**The producer:** `data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py`. Its top-level `mix` deliberately omits `unclassified`
("top-level mix is 3-class per the frozen shape (census-refusal-confirmed); unclassified rides the period rows + composition bucket",
~:158-163), while `composition.unclassified` carries the residual. Its SUM-IDENTITY guard (classes + unclassified == total) stays.

**Build:**
1. `mix` carries a fourth key `unclassified` (market_value, pct) equal to the residual the emitter already computes. If a shape census
   (`--census`) refuses the new key, the census file that freezes the shape is part of the change: name it in your report and in a
   row, and do NOT edit any file outside `<paths>` (stop on that criterion instead).
2. A test `data/assets/scripts/gold/runners_49f/tests/test_d06_unclassified_line.py`: on a fixture with an unclassified position the
   four pcts sum to 1.0 and the four market values to the total.
3. A LOCAL run of the emitter against the live canonical inputs with
   `--out org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/D06_MIX_DRY_RUN_20261007.json`, never uploaded (the inputs are opal-data-bd; read the a07 and b01 paths from the emitter's
   own CLI and its runner).
4. The half request `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_D06_UNCLASSIFIED_20261007.md`: the act (the served
   `platinum/firm/mix_summary.json` gains the line at the next scheduled run after the code ships), its blast radius (every reader of
   that key: list them), both branches, rollback per key, both halves UNSIGNED.

**Shipped file:** `data/assets/scripts/gold/` is a shared home the pre-push deploy gate ships (`.tools/safe_deploy_core.py`
`shared_repo_homes`): your branch stays OFF every pushed range until both halves sign.

### AMENDMENT 3 (issuer, 2.0.0_SA_COO~M1, 2026-10-07 ~16:5xZ; on row W53-S1)

W53-S1 is right. The issuer's cherry-pick stopped after 46bda757e1 (the pick of 4e73b996d0 conflicted on the channel and did not
apply), so the staged blobs were the pre-amendment build, and `d00_census_out.json` was missing. The issuer re-staged all FOUR files
from 4e73b996d0. Each blob is now EQUAL to 4e73b996d0's (measured), and the 49F suite reads 148 passed plus 1 failure that pre-exists
at the base. `data/assets/scripts/gold/runners_49f/d00_census_out.json` joins `<paths>`. Re-run AMENDMENT 2's steps over four files,
and file a row resolving W53-S1 by this amendment.

### AMENDMENT 2 (issuer, 2.0.0_SA_COO~M1, 2026-10-07 ~16:4xZ; release mode, CTO round-11 analysis @fc96f7c48c section 2 item 2)

**The release port.** e55 (46bda757e1 + amendment-1 build 4e73b996d0, ~38) is complete and VALID on the held-38 line. Its three files
cherry-pick CLEAN onto the round head a6e799fa0d (CLOUD plus round records, S58/S59; no old S55), and the d06 test passes 5 of 5.
AC2 stays WITHDRAWN per amendment 1: its live dry-run is the release seat's precondition in the half.

Slot ~53 on branch `secclass-r12-rel-e55` commits that port. The issuer's lane refuses these paths.

**Your work:** the three files below are ALREADY STAGED (the issuer's cherry-pick, uncommitted). Do not rebuild.
1. Confirm each blob equals 4e73b996d0's (`git rev-parse :<path>` vs `git rev-parse 4e73b996d0:<path>`).
2. Commit them.
3. Run AC1 and AC3.
4. Write and validate the proof instance (slot ~53, ids SC9-e55-AC1,SC9-e55-AC3), flip status to complete, and commit.

### ACCEPTANCE

<criterion id="SC9-e55-AC1" cell_refs="SC-e-55"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/assets/scripts/gold/runners_49f/tests/test_d06_unclassified_line.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC9-e55-AC1` -- the four-key mix sums to 1.0 on a fixture.

`SC9-e55-AC2` -- WITHDRAWN by AMENDMENT 1 (its live dry-run moves into the half request as the release seat's precondition).
`SC9-e55-AC2` -- the local run against live inputs: four keys, pct sum 1.0, market values equal total_aua, the new line equal to composition.unclassified.

<criterion id="SC9-e55-AC3" cell_refs="SC-e-55"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_D06_UNCLASSIFIED_20261007.md</invocation><expect>HALF-READY</expect></criterion>
`SC9-e55-AC3` -- the half request carries the act, blast radius, both branches, rollback and two UNSIGNED halves.

<expected_criteria>SC9-e55-AC1,SC9-e55-AC3</expected_criteria>

Dry-run at the base (5d70aab6c9, 2026-10-07): SC9-e55-AC1 FAIL as expected (PYTEST-BAD rc=4, no test file); SC9-e55-AC2 FAIL as expected (no D06_MIX_DRY_RUN file); SC9-e55-AC3 FAIL as expected (NOT-READY: half absent).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, curl or tool fetch, into any environment; row S49).
- No upload, no deploy, no S3 write: the local run writes only the `--out` file.
- Never push: a shipped shared-home file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W53-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py
data/assets/scripts/gold/runners_49f/tests/test_d06_unclassified_line.py
data/assets/scripts/gold/runners_49f/d00_census_out.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_D06_UNCLASSIFIED_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-55`.
<owned_cells>SC-e-55</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e55-AC1, SC9-e55-AC2, SC9-e55-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~53/MDPF_SECCLASS.TO-SC-e55.d06-unclassified-line.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e55-AC1,SC9-e55-AC3` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** the residual before and after, the dry-run line, every reader of the served key, the census file if one refused, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery (2026-10-07 ~07:3xZ); the emitter's schedule is read by the worker from its runner, unchanged by this cell.
comp-iam: DECLARED-NOT-APPLICABLE no grant changes; the local run reads opal-data-bd with the box's existing read.
comp-adversary: RUN -- the frozen-shape census (a new key may be refused: stop, do not widen); the SUM-IDENTITY guard (kept); the served key's readers (listed in the half); BLIND: consumers outside the repo.
lane: the <paths> block IS the grant.
</preflight>

Source: round-8 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md` @1ca9e97fc9; PRD v0.13 @90f99888cd (ADMITTED); DECOMP_R9 @5d70aab6c9.

## AMENDMENT 1 (2.0.0_SA_COO~M1, 2026-10-07 ~12:0xZ) -- rulings on BLOCKING rows W38-S1 and W38-S2

- **W38-S2, granted.** 1.0.0_SA_CTO~DELL1's round-8 analysis section 3 (C-S13) rules the residual served as its own "Unclassified"
  line; adding that one key to the frozen `mix` node is the ruling's own shape change. `data/assets/scripts/gold/runners_49f/d00_census_out.json`
  joins `<paths>`: add exactly the one key (`unclassified`) to family `platinum/firm/mix_summary`'s `mix` node, nothing else; prove the
  emitter's shape check passes with it and refuses any other new key (a control in AC1's test file).
- **W38-S1, ruled.** The emitter's live inputs (`s3://opal-data-49financial/gold/advi/`) are denied to this box's principal, and the
  read-only fence join being cut covers only `irpt/<firm>/platinum/holdings/`. AC2 is WITHDRAWN from this order: a live dry-run cannot
  run here. It moves into the half request as the release seat's FIRST step (a laptop seat the bucket admits runs `d06_mix_sum_check.py`
  against a live dry-run and STOPS on `ok=False`). Add that precondition to the half request.
- **W38-S3** (the measured legacy key is D_04's, not d06's) is carried to 1.0.0_SA_CTO~DELL1 by the issuer; this order stays on d06.
- Then re-run AC1 and AC3, update the proof instance (AC2 recorded withdrawn with this pointer), flip. Gate limb: none graded this
  modification (no new order; no `<placeholders>`).

