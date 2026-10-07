# TO MDPF_SECCLASS.TO-SC-e35 -- round 8 SC-e-35: FWD-5 -- the old list stops growing in the Black Diamond tree

<to_id>MDPF_SECCLASS.TO-SC-e35</to_id>
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

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-35` (`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none (slot ~27's queue: this order first, then TO-SC-e36, then TO-SC-e37)

---

## WORKER FACE

### THE CELL

`SC-e-35`. FWD-5: "The old Black Diamond copy of the list is gone, and it can be shown that nothing needed it" (PRD
`org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.12). The PRD's contract note: "The old list stops growing
first. Three writers add rows to it daily. Each is stopped, as a named cell in its own tree, before FWD-5's check can read
zero." This cell is the Black Diamond tree's stop: `B_01b`'s step leaves the gold dispatch, and the four classification
scripts are retired from any trigger. You write code and a half REQUEST. You deploy nothing.

The old list is the DynamoDB table `bd-securities` (us-east-1). The shared list is `etf-classifications`.

**What writes the old list in this tree (measured 2026-10-07 at the cut):**
- `data/black_diamond/scripts/gold/B_01b.classify_new_securities.py`: scans `holdings_lots` partitions newer than its
  watermark, classifies new (ticker, asset_name) pairs through OpenAI and writes them to `bd-securities`. Its S3 copy is
  `s3://opal-data-bd/code/gold/B_01b.classify_new_securities.py` (13,748 bytes, 2026-09-27).
- `data/black_diamond/scripts/gold/gold_dispatch.sh` (1,593 lines) runs it. It is named on 10 non-comment lines: the
  registry line `B_01b|B_01b.classify_new_securities.py|--upload` (:101), `CHAIN_HOLDINGS_SEED="B_01 B_01b"` (:149),
  `CHAIN_CANONICAL="B_00 B_01 B_01b E_18 B_02 B_03 C_00 C_01 C_02 C_04"` (:162), `GROUP_B` (:177), the PHASE_B3 block
  (:568-570), and the help text (:906, :920-922, :944). E_18 (`E_18.detect_new_securities.py`, FWD-7's scheduled writer of
  the SHARED list, non-fatal) runs right after `B_01b` and stays.
- The four classification scripts in `data/black_diamond/scripts/classification/`: `classify_bd_securities.py`,
  `seed_bd_securities.py`, `seed_canonical_securities.py`, `backfill_name_aliases.py`. No trigger, dispatcher or Terraform
  file in the repo names any of them (read at the cut). Their S3 copies are under `s3://opal-data-bd/code/classification/`
  (March and April 2026).

**Readers of the old list in this tree** (they keep reading; switching them is a later round). `B_01.holdings_lots.py`,
`build_canonical_prices_v2.py`, `lib/etf_classifier.py`, `lib/s3_layout.py` and `E_18.detect_new_securities.py` name
`bd-securities`. After this cell, a security first seen tomorrow gets no `bd-securities` row. Your half says what each of
these readers then does with such a security (read the code, cite lines).

**Build:**
1. **The dispatcher.** Remove `B_01b` from every chain, group, phase, registry line and help line of `gold_dispatch.sh`, so
   no non-comment line names it. Keep `B_01 -> E_18 -> B_02` in order, with E_18 still non-fatal. Leave a one-line comment
   where the step was: `# B_01b retired: MDPF_SECCLASS FWD-5 SC-e-35 (the old list stops growing)`. `bash -n` must accept
   the file.
2. **The five writers refuse.** In each of the five scripts above, make the first statement under
   `if __name__ == '__main__':` (before argparse and before any AWS or model client is made) print one line starting
   `RETIRED:` that names the script and `MDPF_SECCLASS FWD-5 SC-e-35`, then `sys.exit(3)`. Leave each script's functions in
   place, because other code may import them.
   - ASCII only.
   - Read-only library functions stay callable.
3. **The half request.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_OLD_LIST_WRITERS_20261007.md`
   with these sections: `## The act`, `## Blast radius`, and `Rollback per key`. It must carry the word `candidate` and contain no `{{slot}}`.
   - **The act.** Upload the edited dispatcher and the five edited scripts to their `s3://opal-data-bd/code/` keys. It is the
     issuer's act under DS lane `.tools/safe-deploy.sh`, never yours.
   - **Blast radius:**
     - the candidate diff (the commit on your branch);
     - the rows `bd-securities` would have received. Measure them READ-ONLY: scan `bd-securities` for rows whose
       `classified_by` or `last_updated` shows `B_01b` wrote them in the last 30 days, and print the count per day;
     - each reader above and what it does with a security that has no row;
     - the next scheduled BD gold run that would first run without the step.
   - **Rollback per key.** For each of the six S3 keys, its current `VersionId` (from `aws s3api list-object-versions`,
     read-only) and the repo commit to revert.

**THE PUSH HAZARD (rows S35, S38-S41 in the investigation file).** The pre-push deploy gate uploads every changed gold
script in a pushed range to S3 at the push, BEFORE any half is signed. On 2026-10-07 it put an unsigned Cottonwood `B_01b`
live at 04:16:37Z, and it re-uploaded the rolled-back bytes at 07:09:42Z. So your edits must not reach a pushed range
before both halves are signed. You commit on YOUR branch only. The issuer holds the merge until the half is signed. Never
push and never merge.

### ACCEPTANCE

<criterion id="SC8-e35-AC1" cell_refs="SC-e-35"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_bd_old_list_writers_check.py</invocation><expect>OLD-LIST-WRITERS-RETIRED tree=bd</expect></criterion>
`SC8-e35-AC1`: the dispatcher no longer names `B_01b` and passes `bash -n`. Each of the five writers, run with `--upload`
and AWS unreachable, exits 3 with a `RETIRED:` line.

<criterion id="SC8-e35-AC2" cell_refs="SC-e-35"><invocation>python -m pytest -q data/black_diamond/scripts/gold/tests</invocation><expect>passed</expect></criterion>
`SC8-e35-AC2`: the Black Diamond gold tests folder still passes, with no failure (76 passed at the base). Run this folder
alone. It cannot share a pytest process with the Cottonwood folder (TO-SC-e20 amendment 2 correction).

<criterion id="SC8-e35-AC3" cell_refs="SC-e-35"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_OLD_LIST_WRITERS_20261007.md</invocation><expect>HALF-READY</expect></criterion>
`SC8-e35-AC3`: the half request exists, for the issuer to sign and send.

<expected_criteria>SC8-e35-AC1,SC8-e35-AC2,SC8-e35-AC3</expected_criteria>

Dry run at the base 2026-10-07 (@1640a0e86e, worktree `coo-m1-secclass-r8`):
- AC1 base: FAIL as expected (`NOT-RETIRED tree=bd dispatch_live_refs=10 dispatch_syntax=ok writers_retired=0/5`);
- AC2 base: PASS as expected (76 passed in 4.75 s; a control);
- AC3 base: FAIL as expected (half absent).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under
  `.scratch/`, uncommitted.
- **No deploy, no S3 write, no table write, no trigger change, no push, no merge.** Reading `bd-securities` and listing S3
  object versions are allowed, read-only.
- **No vendor or model call.** Never run a writer with real credentials.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a surprise row (id
  `MDPF_SECCLASS-W27-S<k>`). Do not weaken the test.

<paths>
data/black_diamond/scripts/gold/gold_dispatch.sh
data/black_diamond/scripts/gold/B_01b.classify_new_securities.py
data/black_diamond/scripts/classification/classify_bd_securities.py
data/black_diamond/scripts/classification/seed_bd_securities.py
data/black_diamond/scripts/classification/seed_canonical_securities.py
data/black_diamond/scripts/classification/backfill_name_aliases.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_OLD_LIST_WRITERS_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ everything else named here and never edit it, including the R10 check scripts.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-35`.
<owned_cells>SC-e-35</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e35-AC1, SC8-e35-AC2, SC8-e35-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~27/MDPF_SECCLASS.TO-SC-e35.bd-old-list-writers-stop.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e35-AC1,SC8-e35-AC2,SC8-e35-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the lines removed from the dispatcher, the five guards, the 30-day row count, each reader's behaviour with
lines cited, the six VersionIds, commits (branch only).

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery (comp-schedule --owner 2.0.0_SA_COO~M --budget 120, 2026-10-07 ~07:3xZ): 8 open ledgers, none names the BD gold dispatch's B_01b step. The cell removes a step from the scheduled BD gold chain. The schedule itself is untouched, and the served change lands only under the issuer's half.
comp-iam: RUN -- R8 battery (comp-iam gaps, DESIRED plane, 541 .tf files): 0 gap lines name bd-securities. The cell changes no grant. BLIND: the live grants on bd-securities (FWD-5's later IAM read).
comp-adversary: RUN -- cell-specific reads at the cut: gold_dispatch.sh (10 live B_01b refs, measured by R10 check), the four classification scripts (no trigger in repo; S3 copies under opal-data-bd/code/classification/), comp-find bd-securities over both gold trees (76 hits / 220 files), rows S35 S38-S41 (the push gate deploys before a half). BLIND: whether an out-of-repo scheduler (SSM document, cron on an instance) invokes a classification script. The guard makes such an invocation refuse either way.
lane: the <paths> block IS the grant.
</preflight>

Source: DECOMP_R8 @495efa3c32 cell SC-e-35; PRD v0.12 @87ad6d2e4c contract notes; CTO ruling 106036 (one issuer, ~M1).
