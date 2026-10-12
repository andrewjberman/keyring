# TO MDPF_SECCLASS.TO-SC-e92 -- round 21 SC-e-92: the cross-box deploy check reads a sentinel's status trunk-first and classifies a vanished worktree

<to_id>MDPF_SECCLASS.TO-SC-e92</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~81</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-92` (`decompositions/MDPF_SECCLASS_DECOMP_R21.md`) |
**outcome_ref:** seat-gates (row D1-S28) | **depends_on:** none | **source:** CTO round-20 analysis section 2 (D1-S28), msg 4321

---

## WORKER FACE

### THE CELL

`SC-e-92`, row MDPF_SECCLASS-D1-S28. `.tools/crossbox-deploy-check.py` `measure_open_deploy(repo_root, rel, serial, files=None)` (:326-405)
lists every registered worktree and reads each one's `org/critical_paths/.open_deploys/` at HEAD. The real run of round 20's SC-e-89 read STOP
(4 OPEN-DEPLOY hits) on a one-file-family ship although nothing contended, on two limbs the cell's criteria did not reach:

- **(d) a slug the trunk closed still reads live in a lagging worktree.** A ledger entry that was CLOSED at trunk (its sentinel deleted in a
  trunk commit) keeps its sentinel, at its old HELD status, in the HEAD of any worktree that has not taken the closing commit, and counts as
  a live deploy.
- **(e) a registered worktree whose directory is gone.** `git worktree list` still names it (prunable), `ls-tree` returns rc=128, and the
  tool reports `ls-tree rc=128 (not readable, not clear)` as a hit. The existing VANISHED classification only covers a tree that left the
  list during the read.

**Build (`.tools/crossbox-deploy-check.py` only; nothing else is edited):**
1. **TRUNK is the HEAD of the checkout the check runs in (`repo_root`).** For a slug read from a worktree HEAD but ABSENT at trunk HEAD, read
   the path's history at trunk (`git log -1 --format=%H -- <sentinel path>` at `repo_root`): if trunk's history carries that path, it was
   deleted at trunk, so the sentinel is STALE and draws no hit (print one line per stale slug, with the deleting commit). If trunk's history
   never carried the path, the sentinel is a deploy open on a worker's branch until the drain (CLAUDE.md NEVER-2) and still counts exactly as
   today. A sentinel present at trunk HEAD is read as today.
2. **A registered worktree whose directory does not exist on disk is VANISHED**: counted in the denominator's `vanished=` figure and
   printed as `VANISHED (registered, directory absent)`, never a hit. A registered worktree whose directory EXISTS but whose `ls-tree` fails
   stays a hit (`not readable, not clear`).
3. Keep every other limb, the output grammar and the existing denominator line; add the stale count to that line (`stale=<n>`).

### ACCEPTANCE

<criterion id="SC21-e92-AC1" cell_refs="SC-e-92"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R21_CHECKS/sc_r21_trunk_first.py lagging</invocation><expect>TRUNK-FIRST ok=True case=lagging</expect></criterion>
`SC21-e92-AC1` -- a slug closed at trunk but still HELD in a lagging worktree draws 0 hits.

<criterion id="SC21-e92-AC2" cell_refs="SC-e-92"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R21_CHECKS/sc_r21_trunk_first.py vanished</invocation><expect>TRUNK-FIRST ok=True case=vanished</expect></criterion>
`SC21-e92-AC2` -- a registered worktree whose directory is gone is VANISHED in the denominator and draws 0 hits.

<criterion id="SC21-e92-AC3" cell_refs="SC-e-92"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R21_CHECKS/sc_r21_trunk_first.py planted</invocation><expect>TRUNK-FIRST ok=True case=planted</expect></criterion>
`SC21-e92-AC3` -- the control: a live sentinel at trunk HEAD still draws 1 hit, and a sentinel that exists only on a worker's branch still draws 1 hit.

<criterion id="SC21-e92-AC4" cell_refs="SC-e-92"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R21_CHECKS/sc_r21_trunk_first.py branch</invocation><expect>TRUNK-FIRST ok=True case=branch</expect></criterion>
`SC21-e92-AC4` -- (amendment 1) a worktree whose directory is gone but whose branch carries a deploy open on it is read through that branch and draws exactly 1 hit.

<expected_criteria>SC21-e92-AC1, SC21-e92-AC2, SC21-e92-AC3, SC21-e92-AC4</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-12 ~09:3xZ): SC21-e92-AC1 FAIL as expected (`hits=1`); SC21-e92-AC2 FAIL as expected (`hits=1 vanished=0`);
SC21-e92-AC3 PASS as expected (the control: `trunk_hits=1 branch_only_hits=1`).

### AMENDMENT 1 -- the vanished limb reads the branch (issuer 2.0.0_SA_COO~M1, 2026-10-12 ~10:0xZ; answers your row MDPF_SECCLASS-D1-W81-S2)

Your finding stands and is ruled inside this cell: a worktree whose directory is gone must not read CLEAR while its branch carries a deploy
open on it, which is the one defect BOUNDS forbade. Your order's `<status>` is set back to `in_progress` for this one addition; nothing else
you did is reopened, and your row D1-W81-S1 (the blob rule) is accepted as built.
1. **Build limb e'.** For a registered worktree whose directory is absent, do not stop at VANISHED. Take its ref from the worktree list
   (`git worktree list --porcelain`: the `branch refs/heads/<name>` line under that `worktree` entry, else its `HEAD <sha>` line when it
   is detached) and read `org/critical_paths/.open_deploys/` through it at `repo_root` (`git ls-tree -r <ref> ...`). A sentinel found there is
   read exactly like a sentinel at a worktree's HEAD: the same status, the same carried-file test, the same trunk-first stale rule and the
   same blob rule. The worktree still counts in the denominator's `vanished=` figure and still prints `VANISHED (registered, directory
   absent)`, with the ref it was read through. If no ref can be taken or the ls-tree fails, the registration is a hit again
   (`not readable, not clear`): a vanished worktree is CLEAR only when its ref was read.
2. **Acceptance.** AC1-AC3 stay as they are and must still pass. AC4 (above) is the new arm: the issuer's positive and negative controls
   read it PASS at the base tool (the old not-readable hit) and FAIL at your first build (`hits=0`).
3. **Files.** The same `<paths>` grant. The check script `R21_CHECKS/sc_r21_trunk_first.py` on your branch is replaced by the issuer's
   amended copy (the `branch` arm and an `R21_TOOL` override); do not edit it.
4. **Gate limb.** The issuer amends its own criteria without a CTO ruling; no gate limb grades an amendment to an existing order's
   criteria and `<status>` (`.tools/to-pipeline-gate.py` grades NEWLY-ADDED orders and `<placeholders>`; this order declares `NONE`).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- The three checks build throwaway git repos in a temp directory; no repo of this workspace is written by them. Do not run any deploy, do not push.
- Reading the live workspace's worktrees with the tool is allowed; removing or pruning any worktree is NOT (a vanished registration is the
  tool's input, never your target). The tool is a gate other seats rely on: a change that makes it read CLEAR when a real deploy is open
  on a branch is the one defect this cell must not create, and AC3 is its arm.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-W81-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken any check.

<paths>
.tools/crossbox-deploy-check.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R21.md</decomp_doc> (round 21), cell `SC-e-92`.
<owned_cells>SC-e-92</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC21-e92-AC1, SC21-e92-AC2, SC21-e92-AC3, SC21-e92-AC4. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~81/MDPF_SECCLASS.TO-SC-e92.crossbox-trunk-first-sentinel-status.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC21-e92-AC1,SC21-e92-AC2,SC21-e92-AC3,SC21-e92-AC4`.
</proof_of_spec>

**REPORT:** the old and new rule (file:line), each criterion's output, one real run of the tool on this box's worktrees with its denominator
line (stale and vanished counts), commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a gate tool schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no role, no table, no S3 address.
comp-adversary: RUN -- a deploy open on a worker's branch read as stale because trunk never carried it (AC3's second arm); a sentinel closed at trunk and re-opened later under the same path (trunk's history carries the path, trunk HEAD carries the sentinel: it is read as today); a worktree directory that exists but is unreadable passing as vanished (the existing hit stays). BLIND: a sentinel deleted at trunk by a revert rather than a close (the history reads the same).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-20 analysis section 2 (D1-S28 ruling) and section 3 item 2 (msg 4321); row D1-S28 @611993f406; DECOMP_R21.
