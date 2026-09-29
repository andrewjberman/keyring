# TO IRPT_BCKEND.TO-IB-m23-231 -- a per-file census of every irpt-m-* branch (row S208)

<to_id>IRPT_BCKEND.TO-IB-m23-231</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~81</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-231`
(`decompositions/IRPT_BCKEND_DECOMP_R23_M.md`) | **outcome_ref:** none directly (act 4's M leg) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-mr-231` -- row `IRPT_BCKEND-S208`: the M leg of 0.0.0_AB_MSTR's "act 4" (drain the seat branches to CLOUD) names a
branch that does not exist. 2.0.0_SA_COO~M's pre-relaunch work sits on ten local branches named `irpt-m-*`. Some of it
is already in CLOUD, some was re-cut differently, some may be missing. Nothing may be drained until each branch's fate
is named per file. The issuer's first read (15:3xZ, each branch's net diff applied reversed and forward against a CLOUD
index): `irpt-m-r4-holdings` ANCESTOR of CLOUD; `irpt-m-s125-20260924` PRESENT; `irpt-m-b01b-skip` and
`irpt-m-s152-cloud` ABSENT (apply clean, 2 files each); `irpt-m-cot-b1`, `irpt-m-cot-cash-line`,
`irpt-m-cot-cash-line-act`, `irpt-m-s125-publish`, `irpt-m-s152` DIVERGED.

**Build (record only -- read git, write one JSON and one short note):**
1. For EVERY local branch matching `irpt-m-*` (list them yourself: `git branch --list 'irpt-m-*'`), take the net diff
   `git diff $(git merge-base CLOUD <b>) <b>` and, for EACH file in it, decide:
   - `PRESENT` -- CLOUD already carries this change (show the CLOUD commit that landed it, or the reversed-apply result);
   - `SUPERSEDED` -- CLOUD carries a later, different version of the same rule (name the CLOUD commit and say how it
     supersedes; read the commit messages on both sides, e.g. the cash-line rule re-cut in `holdings_snapshot.py`,
     S152's re-cut on CLOUD);
   - `CARRY` -- the change is missing from CLOUD and still wanted (say why it is still wanted, from the row or ruling the
     branch commit cites);
   - `DROP` -- missing and no longer wanted (a ledger/CI record of an act that never happened, a stale artefact, a
     ruling that reversed it -- cite it).
2. Give each branch one disposition: `WORLD-DONE` (every file PRESENT), `SUPERSEDED` (no CARRY, at least one
   SUPERSEDED), `DRAIN` (one or more CARRY -- list them), `RETIRE` (everything DROP).
3. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R23_M_BRANCH_CENSUS_20260929.json` as
   `{"measured_at", "cloud_head", "branches": [{"branch", "tip", "ahead", "disposition", "evidence", "files":
   [{"path", "disposition", "evidence"}]}]}` and a one-page note beside it,
   `R23_M_BRANCH_CENSUS_20260929.md`, with one line per branch (branch, disposition, the reason in one sentence).

### ACCEPTANCE

<criterion id="IBM23-231-AC1" cell_refs="IB-mr-231"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R23_CHECKS/r23_branch_census.py</invocation><expect>CENSUS-COMPLETE followed by the branch and file counts</expect></criterion>
`IBM23-231-AC1` -- every irpt-m-* branch, and every file in its net diff, carries a disposition with evidence.

<expected_criteria>IBM23-231-AC1</expected_criteria>

Dry-run at the base 2026-09-29 15:3xZ: NOT-COMPLETE (census JSON absent) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **Read-only on git beyond your two files.** No merge, no cherry-pick, no branch delete or rename, no push, no code
  edit. The drain (or retirement) is the issuer's and 0.0.0_AB_MSTR's act after your census.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `IRPT_BCKEND-W81-S<k>`), and do not weaken the test to pass.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R23_M_BRANCH_CENSUS_20260929.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R23_M_BRANCH_CENSUS_20260929.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R23_M.md</decomp_doc> (round 23, workstream ~M), cell `IB-mr-231`.
<owned_cells>IB-mr-231</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM23-231-AC1. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~81/IRPT_BCKEND.TO-IB-m23-231.irpt-m-branch-census.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM23-231-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** one line per branch (disposition, files by state), every CARRY file named, commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS read or write.
comp-adversary: RUN -- 10 branches measured by the issuer at 15:3xZ (git cherry + net-diff reverse/forward apply on a CLOUD index): 1 ancestor, 1 present, 2 absent-clean, 5 diverged (one branch, irpt-m-comparison-consumer, is patch-equivalent 2/2); BLIND: the per-file reason for each DIVERGED file is unread at the cut (the cell reads it).
lane: the <paths> block IS the grant; the branches are ~M's own.
</preflight>

Source: row IRPT_BCKEND-S208 (@ebd80df827, 2.0.0_SA_COO~Y); CLAUDE.md NEVER-2.
