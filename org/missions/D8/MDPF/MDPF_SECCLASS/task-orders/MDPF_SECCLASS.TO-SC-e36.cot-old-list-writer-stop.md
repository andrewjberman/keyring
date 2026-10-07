# TO MDPF_SECCLASS.TO-SC-e36 -- round 8 SC-e-36: FWD-5 -- the old list stops growing in the Cottonwood tree

<to_id>MDPF_SECCLASS.TO-SC-e36</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~27</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-36` (`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none (slot ~27's queue: after TO-SC-e35, before TO-SC-e37)

---

## WORKER FACE

### THE CELL

`SC-e-36`. FWD-5: "The old Black Diamond copy of the list is gone, and it can be shown that nothing needed it" (PRD
`org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.12). The PRD's contract note: "The old list stops growing
first ... Each is stopped, as a named cell in its own tree." This cell is the Cottonwood tree's stop: `B_01b`'s step leaves
the Cottonwood gold dispatch. You write code and a half REQUEST. You deploy nothing. Do for Cottonwood exactly what
TO-SC-e35 did for Black Diamond's `B_01b` and dispatcher (no classification-scripts folder exists in this tree).

The old list is the DynamoDB table `bd-securities` (us-east-1), shared across firms. The shared list is `etf-classifications`.

**What writes the old list in this tree (measured 2026-10-07 at the cut):**
- `data/cot/scripts/gold/B_01b.classify_new_securities.py` classifies new (ticker, asset_name) pairs from `holdings_lots`
  through OpenAI and writes them to `bd-securities`.
  - Its S3 copy is `s3://opal-data-cot/code/gold/B_01b.classify_new_securities.py`. The latest version (07:09:42Z) has
    ETag `eedfd1d1c5deb0c7e9e9e6100bbd3f77`, byte-equal to repo HEAD and to the rolled-back body (row S40).
  - The 04:16:37Z version (ETag `28b33a17...`) was the unsigned change rows S38-S41 rolled back.
- The Cottonwood gold dispatcher is **`data/cot/scripts/gold/gold_dispatch.sh`** (1,335 lines; R8 left this unread, and it
  is resolved here). It names `B_01b` on 10 non-comment lines:
  - the registry line `B_01b|B_01b.classify_new_securities.py|--upload` (:86);
  - `CHAIN_HOLDINGS_SEED="B_01 B_01b"` (:132);
  - `CHAIN_CANONICAL="B_00 B_01 B_01b B_02 B_03 C_00 C_01 C_02 C_04"` (:139);
  - `GROUP_B` (:151);
  - the PHASE_B3 block (:410-411);
  - the help text (:730, :743-745, :767).
  - Unlike Black Diamond, there is no E_18 step in this chain.
- `data/cot/scripts/gold/tests/test_other_admission.py` is in your grant because R8 placed it there. At the cut it does not
  name `B_01b`. Edit it only if your change breaks one of its tests, and say why in your report.

**Readers of the old list in this tree** (they keep reading; switching them is a later round):
`B_01.holdings_lots.py`, `build_canonical_prices_v2.py`, `lib/etf_classifier.py`, `lib/s3_layout.py` and
`E_18.detect_new_securities.py` name `bd-securities`. Your half says what each does with a security that has no row.

**Build:**
1. **The dispatcher.** Remove `B_01b` from every chain, group, phase, registry line and help line, so no non-comment line
   names it. Keep `B_01 -> B_02` in order. Leave the comment
   `# B_01b retired: MDPF_SECCLASS FWD-5 SC-e-36 (the old list stops growing)`. `bash -n` must accept the file.
2. **The writer refuses.** In `B_01b.classify_new_securities.py`, make the first statement under
   `if __name__ == '__main__':` (before argparse and before any AWS or model client) print one line starting `RETIRED:`
   that names the script and `MDPF_SECCLASS FWD-5 SC-e-36`, then `sys.exit(3)`. Leave its functions in place. ASCII only.
3. **The half request.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_OLD_LIST_WRITER_20261007.md`
   with these sections: `## The act`, `## Blast radius`, and `Rollback per key`. It must carry the word `candidate` and contain no `{{slot}}`.
   - **The act.** Upload the two edited files to their `s3://opal-data-cot/code/gold/` keys. It is the issuer's act, never
     yours.
   - **Blast radius:**
     - the candidate diff;
     - the rows Cottonwood's `B_01b` added to `bd-securities` in the last 30 days. Measure them read-only and print the
       count per day;
     - each reader above, with lines cited;
     - the next scheduled Cottonwood gold run that would first run without the step.
   - **Rollback per key.** For each S3 key, its current `VersionId` (read-only `list-object-versions`) and the repo commit
     to revert.

**THE PUSH HAZARD (rows S35, S38-S41).** The pre-push deploy gate uploads every changed gold script in a pushed range to
S3 at the push, BEFORE any half is signed. This exact file went live unsigned at 04:16:37Z today. You commit on YOUR branch
only. The issuer holds the merge until both halves sign. Never push and never merge.

### ACCEPTANCE

<criterion id="SC8-e36-AC1" cell_refs="SC-e-36"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_cot_old_list_writer_check.py</invocation><expect>OLD-LIST-WRITERS-RETIRED tree=cot</expect></criterion>
`SC8-e36-AC1`: the Cottonwood dispatcher no longer names `B_01b` and passes `bash -n`. `B_01b`, run with `--upload` and AWS
unreachable, exits 3 with a `RETIRED:` line.

<criterion id="SC8-e36-AC2" cell_refs="SC-e-36"><invocation>python -m pytest -q data/cot/scripts/gold/tests</invocation><expect>passed</expect></criterion>
`SC8-e36-AC2`: the Cottonwood gold tests folder still passes, with no failure (21 passed at the base). Run this folder
alone, never in one process with the Black Diamond folder.

<criterion id="SC8-e36-AC3" cell_refs="SC-e-36"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_OLD_LIST_WRITER_20261007.md</invocation><expect>HALF-READY</expect></criterion>
`SC8-e36-AC3`: the half request exists, for the issuer to sign and send.

<expected_criteria>SC8-e36-AC1,SC8-e36-AC2,SC8-e36-AC3</expected_criteria>

Dry run at the base 2026-10-07 (@1640a0e86e):
- AC1 base: FAIL as expected (`NOT-RETIRED tree=cot dispatch_live_refs=10 dispatch_syntax=ok writers_retired=0/1`);
- AC2 base: PASS as expected (21 passed in 2.36 s; a control). R8's handoff named 27 at an earlier drain; 21 is measured
  after the S29 restore;
- AC3 base: FAIL as expected (half absent).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under
  `.scratch/`, uncommitted.
- **No deploy, no S3 write, no table write, no trigger change, no push, no merge.** Read-only reads of `bd-securities` and
  of S3 object versions are allowed.
- **No vendor or model call.**
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a surprise row (id
  `MDPF_SECCLASS-W27-S<k>`). Do not weaken the test.

<paths>
data/cot/scripts/gold/gold_dispatch.sh
data/cot/scripts/gold/B_01b.classify_new_securities.py
data/cot/scripts/gold/tests/test_other_admission.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_OLD_LIST_WRITER_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ everything else named here and never edit it.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-36`.
<owned_cells>SC-e-36</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e36-AC1, SC8-e36-AC2, SC8-e36-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~27/MDPF_SECCLASS.TO-SC-e36.cot-old-list-writer-stop.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e36-AC1,SC8-e36-AC2,SC8-e36-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the dispatcher lines removed, the guard, the 30-day row count, each reader's behaviour, the VersionIds, commits
(branch only).

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery (2026-10-07 ~07:3xZ): ledger secclass-cot-repoint-m-20261002 is OPEN (Cottonwood re-point, leg S page walk); it names no B_01b step. The cell removes a step from the scheduled Cottonwood gold chain. The served change lands only under the issuer's half.
comp-iam: RUN -- R8 battery: 0 gap lines name bd-securities; no grant changes.
comp-adversary: RUN -- cell-specific reads at the cut: data/cot/scripts/gold/gold_dispatch.sh (10 live B_01b refs, R10 check), S3 version list of code/gold/B_01b (07:09:42Z re-upload byte-equal to the rollback), rows S38-S41. BLIND: comp-pipescript deployed --firm cot reads every Cottonwood gold script MISSING_ON_S3 while s3 lists them present, so that instrument is not a deploy oracle for this tree.
lane: the <paths> block IS the grant.
</preflight>

Source: DECOMP_R8 @495efa3c32 cell SC-e-36; PRD v0.12 @87ad6d2e4c contract notes; CTO ruling 106036.
