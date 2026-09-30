# TO MDPF_SECCLASS.TO-SC-e3 -- round 2 SC-e-3: thread-recensus

<to_id>MDPF_SECCLASS.TO-SC-e3</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~4</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-3` (`decompositions/MDPF_SECCLASS_DECOMP_R2.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-3`, analysis item E3 (thread-breaking, first). The FWD-1 Black Diamond thread (round 1: SC-t-1..t-4, drained
@ae7aa281b0) is built and traced (0 bd-securities reads), but its censuses and the thread half
`MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_THREAD_20260929.md` were measured BEFORE the backfill, when 3,699
BD holdings were unclassified. The CVO signs no half whose figures predate 02:2xZ. This cell re-measures and writes the
fresh half. The deploy and the live run are later acts under that half.

**Build (LOCAL build + record: no upload, no deploy, no IAM apply):**
1. **Re-census** the three thread stages on CLOUD's code (the library, the silver assets dimension, and the gold
   C_06/D_03/D_04) on the latest BD day (`opal-data-bd`), reading the LIVE table. Record the moves against TODAY's served
   BD artifacts: the served composition, the client portal summary, and the assets dimension, with their keys and
   versions. Laptop memory limits apply: a `.scratch/` generator may restrict columns, provided it uses the same sources
   and rows; name the workaround. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_THREAD_CENSUS_20260930.json` as
   `{"table_rows_at_build", "bd_securities_reads": 0, "resolution": {...}, "silver": {...}, "gold": {...}}`, where each
   stage is `{"rows", "unclassified", "unclassified_names", "moved", "moves": [{"ticker", "before", "after",
   "artifact"}], "guessed": 0}`.
2. **Fresh half.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_THREAD_R2_20260930.md` (`## The act`,
   `## Blast radius`, `Rollback per key`). At its top, say it supersedes the round-1 thread half, and leave that half
   unedited. It covers:
   - every BD-held ticker whose served class moves, including GLD, PHYS and VXX;
   - the served artifacts and their readers;
   - the BD principal's read on etf-classifications, as an IAM change (desired, not applied), naming the principal
     from the round-1 census and the Terraform file;
   - the deploy mechanics (DS lane `.tools/safe-deploy.sh`, firm tree kept);
   - the COO's one live run of FWD-1 to the page for a real client, as the closing act;
   - rollback per artifact key.

**Standing rulings (carried from the round-2 decomposition):**
- Andrew-direct 2026-09-30 ~02:2xZ: "yes, bd-securities values can seed new rows. THey just don't overwrite existing rows."
  So a bd-securities value may seed a NEW row and never writes into an EXISTING one. A write to an existing row from a
  bd-securities value is outside his word: stop, and name it in the half for his decision.
- CTO C-WRITER ruling (analysis @151c890591, section 1): `classified_by` is `seed` / `scheduled` / `constituents` /
  `legacy`; `seed` always wins; `scheduled` and `constituents` write only where no row exists; a missing label reads as
  `legacy`.
- The live `etf-classifications` holds 2,309 rows (release step 2, ledger CLOSED @f13cddd058). Read and print its row
  count at build time as `table_rows_at_build` in your evidence file.

### ACCEPTANCE

<criterion id="SC2-e3-AC1" cell_refs="SC-e-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_CHECKS/r2_evidence.py thread</invocation><expect>THREAD-CENSUS</expect></criterion>
`SC2-e3-AC1` -- the post-backfill thread census at three stages, nothing guessed, no bd-securities read.

<criterion id="SC2-e3-AC2" cell_refs="SC-e-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_THREAD_R2_20260930.md</invocation><expect>HALF-READY</expect></criterion>
`SC2-e3-AC2` -- the fresh thread half, for the issuer to sign and send.

<expected_criteria>SC2-e3-AC1,SC2-e3-AC2</expected_criteria>

Dry-run at the base 2026-09-30 03:1xZ (@30727a9413): SC2-e3-AC1 NOT-MET (evidence absent); SC2-e3-AC2 NOT-READY -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Build scaffolding goes under
  `.scratch/`, uncommitted.
- **LOCAL build + record.** No table write (dry-run only), no upload, no deploy, no IAM apply, no outside-model call.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W4-S<k>`), and do not weaken the test to pass.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_THREAD_CENSUS_20260930.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_THREAD_R2_20260930.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R2.md</decomp_doc> (round 2), cell `SC-e-3`.
<owned_cells>SC-e-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC2-e3-AC1, SC2-e3-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~4/MDPF_SECCLASS.TO-SC-e3.thread-recensus.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC2-e3-AC1,SC2-e3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three stages' rows, unclassified and moves (the largest by weight), GLD/PHYS/VXX, the principal, the half's path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched
comp-iam: RUN -- 1 file read (infra/aws/terraform/bd-pipeline/iam.tf); BLIND: the production principals are unmeasured at the cut (this cell names them); desired only
comp-adversary: RUN -- 1 analysis read (ROUND1_ANALYSIS_MDPF_SECCLASS_20260930.md @151c890591, item E3), 1 table read (etf-classifications 2,309 rows after release step 2); BLIND: the inputs this cell names or measures are unmeasured at the cut (its census measures them).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-1 analysis @151c890591 (msg 103116), item E3; Andrew-direct 2026-09-30 ~02:2xZ.
