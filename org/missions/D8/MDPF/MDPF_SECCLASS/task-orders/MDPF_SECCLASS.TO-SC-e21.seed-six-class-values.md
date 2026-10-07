# TO MDPF_SECCLASS.TO-SC-e21 -- round 8 SC-e-21: the seed module carries the six-class values the rule-B remap wrote, so a seed plan reads 0 CONFLICT against the live table

<to_id>MDPF_SECCLASS.TO-SC-e21</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~21</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** placement DELL1 (the project row's `fabric` still reads laptop) | **Decomp cell:** `SC-e-21`
(`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) | **outcome_ref:** FWD-3, 1.0.0_SA_CTO's condition 1 on the rule-B remap |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-21`. "The seed module carries the six-class values for the funds the rule-B remap moved, so the seed plan reads 0
CONFLICT against the live table; a seed dry run printed" (R8). It serves FWD-3 (one edit to the seed module is the only way a
seed security's class changes) and the CTO's condition 1 on the remap half
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_MDPF_SECCLASS_MULTI_ASSET_REMAP_B_20261007.md` @ed687ec668): **no seed run until `_shared/etf_classification.py` carries six-class
values.**

**Andrew-direct 2026-10-07 (recorded in `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/ANDREW_DIRECT_20261007_004xZ_NO_MULTI_ASSET_CLASS_SIX_CLASSES_ONLY.md`):**
"there should be no multi-asset class. There are 6 classes: cash, fixed income, equity, structured, alternatives,
commodities." Rule B (`ANDREW_DIRECT_20261007_00xxZ_RULE_B_CATEGORY_RULE_FOR_MULTI_ASSET_FUNDS.md`): target-date, balanced and
allocation funds go to `equity`; income-oriented funds go to `fixed_income`.

**State, measured by the issuer 2026-10-07 at the base of this order:**
- The live table `etf-classifications` (us-east-1): 3,507 rows, 0 `multi_asset`. The 33 rows of the remap set
  `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/MULTI_ASSET_REMAP_B_SET_20261007.tsv` read their target
  class with `updated_by = mdpf-secclass-remap-b` (33 of 33). Column 4 of that file is the row's source: 20 keys are `seed`
  (tickers the module carries), 13 are `scheduled` (12 `CUSIP:` keys and `SCGB1`; the module does not carry them and this
  cell does not touch them). R8 says "19 funds"; the module carries **20** seed tickers in the set.
- `infra/aws/lambda/v2_portal/_shared/etf_classification.py`: the token `multi_asset` occurs **25** times: 20 values in
  `ETF_CLASSIFICATIONS` (lines 325-344: AOR VTHRX VSMGX VTIVX VWELX VWENX ABALX AAETX VTTHX LIPKX FTYPX FBALX CLBAX CAIBX CFIHX
  AMECX FKIQX KAGIX SGIIX MDLOX) and five `# multi_asset (...)` comment lines (324, 471, 763, 925, 1132).
- The check `seed_six_class_dry_run.py` (criterion AC2) at base prints
  `SEED-SIX-CLASS ok=False module_tickers=197 live_rows=3507 remap_seed_keys=20 conflicts=25 off_vocab=20 remap_keys_moved=40 multi_asset_tokens=25`:
  - 20 asset_class conflicts (module `multi_asset`, table the remap's class);
  - 5 sub_asset_class conflicts: the remap RESTORED a sub-class on ABALX (`US Large Cap`), AOR (`Global`), VTHRX (`Global`),
    VWELX (`US Large Cap`), VWENX (`US Large Cap`) where the module says `Fixed Mix` / `Target Date`;
  - 15 keys where the remap CLEARED the sub-class (absent on the row) and the module still carries one (`Target Date`,
    `Flexible`, `Fixed Mix`). Those are not CONFLICTs in the seed script's rule (a blank table value loses to the module), so
    a seed run would silently write the old sub-class back. The check counts them as `remap_keys_moved`.

**Build:**
1. In `ETF_CLASSIFICATIONS`, set each of the 20 seed keys to the class the set's column 5 names (equity or fixed_income).
2. In `ETF_SUB_ASSET_CLASS`, make each of the 20 keys equal what the live row serves: the five restored values above, and
   NO entry for the 15 the remap cleared (remove the key; never write an empty string, because the seed script drops `""` and
   the table's `sub-asset-class-index` refuses it).
3. Rewrite the five `# multi_asset (...)` comments so the module no longer carries the token. Say in one line that the class
   is rule B (Andrew-direct 2026-10-07) and cite the remap set by path.
4. Change no other key and no other dict. Of the module's 197 tickers, only these 20 move.
5. Tests: add to `infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py` tests whose names contain `six_class`:
   (a) every value in `ETF_CLASSIFICATIONS` is one of the six classes `cash fixed_income equity structured alternatives
   commodities`; (b) the module's text carries no `multi_asset`; (c) for each `seed` row of the remap set, the module's class
   equals column 5. Read the set with `encoding="utf-8"` and skip `#` lines. The 19 tests already in the file must still pass.
6. The half REQUEST for the seed run (the run is the issuer's act, never yours):
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_SEED_SIX_CLASS_20261007.md`.
   Follow the shape of `NEVER_WIDEN_HALF_REQUEST_SECCLASS_MULTI_ASSET_REMAP_B_20261007.md` in the same folder:
   - the blast radius as a literal key list;
   - the dry run's output (AC2's full printout);
   - what the seed run writes beyond the 20 keys. Read the check's `rows to write` from the seed script's own dry run:
     `python infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py --dry-run`, which is read-only;
   - **the low_confidence hazard.** The seed script's `merge_item` drops `low_confidence` on every row it writes
     (`MODEL_ONLY_FIELDS`). The remap set `low_confidence: true` on 15 of the 20 seed keys (AAETX AMECX CAIBX CFIHX CLBAX FBALX
     FKIQX FTYPX KAGIX LIPKX MDLOX SGIIX VSMGX VTIVX VTTHX; AC2 prints the list). A seed run strips that flag. Name it as an
     open question for the CTO's half. Do not change the seed script.
   - The COO half and the CTO half stay UNSIGNED.

**Push-gate hazard (rows MDPF_SECCLASS-S35, S39):** the CLOUD push deploy gate uploads changed gold scripts and the shipped
`lib/_shared/etf_classification*.py` copies to S3 AT THE PUSH, before any half is signed. This module is a shipped `_shared`
module. Your commit stays on your branch. The issuer holds the merge into a pushed range until the seed-run half is signed.
You push nothing.

### ACCEPTANCE

<criterion id="SC8-e21-AC1" cell_refs="SC-e-21"><invocation>python -m pytest -q infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py -k six_class</invocation><expect>passed</expect></criterion>
`SC8-e21-AC1` -- the six-class tests pass: no module class outside the six, no `multi_asset` token, every remap seed key's class equals the set.

<criterion id="SC8-e21-AC2" cell_refs="SC-e-21"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/seed_six_class_dry_run.py</invocation><expect>SEED-SIX-CLASS ok=True</expect></criterion>
`SC8-e21-AC2` -- the seed plan, run read-only against the live table with the edited module, reads 0 CONFLICT, 0 off-vocabulary class, and 0 remap key whose class or sub-class it would move.

<expected_criteria>SC8-e21-AC1,SC8-e21-AC2</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (`19 deselected`, no `passed`); AC2 FAIL as expected (line above). The
19 existing tests in the file read `19 passed` at base (control).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted. The check `R10_CHECKS/seed_six_class_dry_run.py` is the issuer's judge: you READ it and never edit it.
- **No seed run, no table write, no S3 write, no deploy, no push.** `seed-etf-classifications.py` runs only with `--dry-run`.
  Both the dry run and AC2 are read-only.
- **No vendor or model call.**
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W21-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
infra/aws/lambda/v2_portal/_shared/etf_classification.py
infra/aws/lambda/v2_portal/_shared/tests/test_seed_fields.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_SEED_SIX_CLASS_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ, and never edit, the seed script, the remap set, the remap half and the check.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-21`.
<owned_cells>SC-e-21</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e21-AC1, SC8-e21-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~21/MDPF_SECCLASS.TO-SC-e21.seed-six-class-values.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e21-AC1,SC8-e21-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the 20 keys and their class and sub-class before and after; AC2's full output, including the `INFO
low_confidence_would_drop` line; the seed script's dry-run `rows to write` count; the half request's path; commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery 2026-10-07 ~07:3xZ (comp-schedule --owner 2.0.0_SA_COO~M --budget 120): 8 open ledgers name this lane, among them secclass-multi-asset-remap-b-m-20261007 (legs H and G open). No schedule runs the seed script; it is a manual issuer act.
comp-iam: RUN -- R8 battery (comp-iam gaps): 0 gap lines name etf-classifications. This cell needs no grant: AC2 reads the table with the issuer's session.
comp-adversary: RUN -- R8 battery on the decomposition (2/2 commits, 21/23 paths stable). Cell-specific reads by the issuer: module token count 25 (equals R8); seed keys 20, not R8's 19; base check output above; the low_confidence drop. BLIND: whether any other job writes these 20 rows between the cut and the seed run.
lane: the <paths> block IS the grant.
risk: WORLD, above R8's SERVED: the L6 gate's floor for an infra/ path (the module is under infra/aws/lambda/) is WORLD; the class is never declared below the floor.
</preflight>

Source: DECOMP_R8 @495efa3c32 (origin 1640a0e86e); PRD v0.12 @87ad6d2e4c; remap half CTO @ed687ec668; remap run 0d9457b639.

## AMENDMENT 1 (2.0.0_SA_COO~M1, 2026-10-07 ~08:5xZ) -- ruling on row W21-S2 (ruff version drift on dell1)

Worker ~21 reported BLOCKING W21-S2: dell1 runs ruff 0.16.10 while `.tools/commit-gate.sh` pins 0.15.11, and the gate refuses the two
`.py` files this order owns on 26 errors that are all present at the base b07521c5dd (22 on `etf_classification.py`, 4 on
`test_seed_fields.py`, `Dict`/`Optional` annotation rules), none on a line the worker touched.

RULING (the issuer's, inside its own decomposition): fix those errors in the two files this order already owns, ANNOTATIONS ONLY --
`from __future__ import annotations`, builtin generics, `X | None` -- with no change to any runtime value, name, signature arity or
import a caller uses. Prove it unchanged: AC1 and AC2 re-run after the fix with the same outputs (`3 passed`; `SEED-SIX-CLASS ok=True
... conflicts=0 off_vocab=0 remap_keys_moved=0 multi_asset_tokens=0`), and the whole test file still reads `22 passed`. Then commit the
`.py` edits and the proof, and flip. Do NOT bypass the gate, install a ruff, or fix any file outside `<paths>`. `<paths>` unchanged.
The box-level drift is routed to 0.0.0_AB_MSTR~DELL1. Gate limb: none graded this modification (no new order; no `<placeholders>`).
