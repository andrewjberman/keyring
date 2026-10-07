# TO MDPF_SECCLASS.TO-SC-e44 -- round 9 SC-e-44: FWD-5, FWD-7, FWD-10 -- the canonical producer gains an input that is not the old list

<to_id>MDPF_SECCLASS.TO-SC-e44</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~34</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-44` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-5, FWD-7, FWD-10 | **depends_on:** none. Slot ~34's only order. `TO-SC-e45` waits for this cell AND for the issuer
act "producer live" (this cell deployed, then a run with a live canonical write count above 0).

---

## WORKER FACE

### THE CELL

`SC-e-44`: `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` (605 lines; the canonical producer, FWD-7) gains a
NON-old-list input, so a security first held after the old-list writers stop can still get an `etf-classifications` row. Dry-run it over
the latest held set and list the keys it would now plan.

- Why: round 8's trace graded this producer NEEDS-OLD-LIST: its only wired direct input is the old list (`default_bd_securities_lookup`,
  `get_item` on `bd-securities`, ~:526-545, through the direct-input function ~:371-391). CANONICAL-PRODUCER is NONE for every real
  reader: `updated_by = 'e18-scheduled'` has written 0 rows; `mdpf-secclass-scheduled` 348 rows, all CUSIP-keyed, 2026-09-30. The round-8
  analysis section 2.10: a writer stop waits for a canonical producer with a live write count above 0.
- **The new input:** the Bloomberg/GICS leg through `infra/aws/lambda/v2_portal/_shared/rivalfunds_classification.py`
  (`classify_canonical_row()`, `parse_bloomberg()`), and the Schwab security master where a held row carries a CUSIP. Wire it as a
  direct input BEFORE the old list, keep the old list as the last fallback, and record which input produced each planned item. Six
  classes only. A key the table already holds is never planned (consistent get); a key nothing resolves is listed unresolved, never guessed.
- **Read first:** the module's existing direct-input order, `classify_canonical_row`, and how FWD-10's producer
  (`infra/aws/lambda/mdpf-secclass/new-security-classifier/lambda_function.py`) already builds items from the same leg, so the two agree.
- **Tests** in `infra/aws/lambda/v2_portal/_shared/tests/test_etf_classification_scheduled.py`: add tests whose names carry `non_old_list`
  (with DynamoDB and S3 stubbed): a held key with a Bloomberg/GICS row plans from that input with no old-list read; a key with only an
  old-list row still plans from it; a key the table holds is not planned; a key nothing resolves is unresolved.
- **The dry run:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/producer_input_dry_run.py` runs the producer's
  planner read-only over the latest held set (a local build, `inferred`, row W25-S1) WITHOUT the old-list input (to show the new input
  alone), and writes `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/PRODUCER_INPUT_DRY_RUN_20261007.json`:
  `{"as_of", "held_source": "... inferred", "planned": [{"key", "input", "asset_class"}], "unresolved": [...], "old_list_reads": 0}`.
- **The half request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_PRODUCER_INPUT_20261007.md`
  with `## The act` (the module ships to `code/gold/lib/_shared/` in opal-data-bd and opal-data-cot through `.tools/safe-deploy.sh`
  beside a byte-equal carrier gold script -- the gate ships a `lib/_shared` member only beside a gold script, row S50 -- and the Lambdas
  that package `_shared` take it at their next build), `## Blast radius` (the planned keys, the readers that see them), a local candidate
  diff, and `Rollback per key` (the two keys' live VersionIds). Both halves UNSIGNED; the issuer signs.

### ACCEPTANCE

<criterion id="SC9-e44-AC1" cell_refs="SC-e-44"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/v2_portal/_shared/tests/test_etf_classification_scheduled.py -k non_old_list</invocation><expect>PYTEST-OK</expect></criterion>
`SC9-e44-AC1` -- the producer plans a held key from the new input with no old-list read, keeps the old list last, never plans a present key, lists the unresolved.

<criterion id="SC9-e44-AC2" cell_refs="SC-e-44"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/issuer_check_sc_e44.py</invocation><expect>SC-E44-INPUT ok=True</expect></criterion>
`SC9-e44-AC2` -- the dry run plans keys from a non-old-list input only, every one absent from the live table and inside the six classes.

<criterion id="SC9-e44-AC3" cell_refs="SC-e-44"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_PRODUCER_INPUT_20261007.md</invocation><expect>HALF-READY</expect></criterion>
`SC9-e44-AC3` -- the half request carries the act, the blast radius with a local candidate diff, and the rollback per key.

<expected_criteria>SC9-e44-AC1,SC9-e44-AC2,SC9-e44-AC3</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (`PYTEST-BAD rc=5`, 12 deselected: no `non_old_list` test yet); AC2 FAIL as expected
(`no PRODUCER_INPUT_DRY_RUN_*.json`); AC3 FAIL as expected (`NOT-READY: ... absent`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
  The issuer checks are READ-ONLY to you.
- **SHIPPED FILE.** `etf_classification_scheduled.py` is one of the three `lib/_shared` members the deploy gate ships
  (`.tools/safe_deploy_core.py:95-99`). Your commit stays on YOUR branch; the issuer holds it off every pushed range until both halves sign.
  Never push.
- **No deploy, upload, table or S3 write, no model or vendor call.** The dry run reads only.
- **NO package install and NO download of any kind** (row S49).
- Lint that predates your edit on a file you own: fix annotation- or comment-only, no runtime change; say so in a row.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W34-S<k>`), and do not weaken the test.

<paths>
infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py
infra/aws/lambda/v2_portal/_shared/tests/test_etf_classification_scheduled.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/producer_input_dry_run.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/PRODUCER_INPUT_DRY_RUN_*.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_PRODUCER_INPUT_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-44`.
<owned_cells>SC-e-44</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e44-AC1, SC9-e44-AC2, SC9-e44-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~34/MDPF_SECCLASS.TO-SC-e44.producer-non-old-list-input.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e44-AC1,SC9-e44-AC2,SC9-e44-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the new input's order among the direct inputs, the dry run's planned and unresolved counts, the Lambdas that package this
module, the two shipped keys' VersionIds, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell adds no schedule; the producer's existing schedules (E_18 in the BD and Cottonwood trees, the FWD-7 and FWD-10 Lambdas) are read, not changed.
comp-iam: RUN -- the new input reads the Bloomberg characteristics leg and (where a CUSIP is held) the Schwab master; the worker names each caller's role and whether it grants that read (a missing grant is a row and part of the half). E_18's EC2 roles hold no etf-classifications grant (R8 trace, W25 rows).
comp-adversary: RUN -- the producer must never plan a present key (a double write) and never guess an unresolved one; the issuer's check re-reads the live table. Shipped lib/_shared member: held off pushed ranges; S50 showed the gate ships it only beside a gold script, so the half names the carrier. BLIND: the served holdings bytes (W25-S1; the held set is inferred).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.13 @90f99888cd (FWD-5, FWD-7, FWD-10); CTO round-8 analysis @1ca9e97fc9 sections 2.10 and 4 item 1; DECOMP_R9 @5d70aab6c9.
