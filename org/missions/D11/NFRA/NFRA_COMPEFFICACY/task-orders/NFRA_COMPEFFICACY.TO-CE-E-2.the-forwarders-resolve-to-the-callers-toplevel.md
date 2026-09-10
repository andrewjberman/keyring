# TO NFRA_COMPEFFICACY.TO-CE-E-2 -- THE FORWARDERS RESOLVE TO THE CALLER'S TOPLEVEL: 186 shims baked to the MAIN tree's `.tools/` make a worker verify its own edit by running the file it did NOT change, and it passes GREEN; the fix is one resolution rule plus a `--which`, and the harness stops writing on a committed baseline and states a bound it has actually measured

<to_id>NFRA_COMPEFFICACY.TO-CE-E-2</to_id>
<project>NFRA_COMPEFFICACY</project>
<issued_to>0.9.0_WK_NFRA_COMPEFFICACY~2</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete -- 0.9.0_WK_NFRA_COMPEFFICACY~2 on branch `wk-nfra_compefficacy-8-1`. `E2-AC1` PASS by output (`timeout 900 python .../test_cee2_forwarders_resolve.py` -> rc 0, `CEE2-FORWARDERS-RESOLVE-TO-CALLER`, **12 of 12 arms**, 186.8 s of a 900 s bound); `E2-AC2` PASS by output (`bash -n .tools/provision-path-shims.sh; echo rc=$?` -> `rc=0`, an EXACT match); `E2-AC3` is judgment -- recorded with evidence and vintages, NO VERDICT, for `3.0.0_SA_CVO` at L9. Proof-of-spec VALID rc 0 (violations 0; 8 artifacts at pin, 4 CONTENT-resolved; surprises limb 5 of 5 rows resolve). BOTH LIMBS LANDED: (i) `.tools/provision-path-shims.sh` @`13df262a9b` -- every generated forwarder resolves `.tools/<name>` from the CALLER'S `git rev-parse --show-toplevel`, answers `--which`, and prints a WARN naming the path it chose when it falls back; **210 of 210** regenerated forwarders carry it on BOTH planes (105 extensionless + 105 `.cmd`), and a marker planted in a fresh worktree's copy EXECUTES from that worktree and not from the main tree. (ii) `.tools/comp-which-routing-test.py` @`9879030790` -- `--out` no longer defaults onto the committed CloudComp baseline (`--rebaseline` now required, two refusals exercised), and the timeout bound is stated from measured runtimes. THE DEPLOY WAS ORDERED per spine v3.9: entry `compefficacy-ce-e-2-forwarder-resolution` OPENED 03:49Z, provisioner RUN 03:59Z, entry CLOSED and COMMITTED @`e5f2fa3eae` before a single grading read; backup of the pre-state at `C:/tmp/wk-compeff-8-1/.scratch/bin-backup-pre-ce-e-2` (211 of 211 files). FOUR DEFECTS THE DRY RUN CAUGHT BEFORE THE FLEET SAW THEM (a baked fallback pointing at the deleted worktree; 105 of 210 protected DACLs re-arming S26 against a live 0 of 211; a cmd parser break; a backtick executing at provision time) plus a FIFTH in this battery's own control (`--which` exits before the exec, so arm (c) would have been a constant). Rows `W2-S5` (OBS/ARMED), `W2-S6` and `W2-S9` (BLOCKING/ARMED, both RESOLVED -- the grant widened @`e618f3f88d` and 06 regenerated IN THIS TREE in the same commit as the harness; `system-current-override:` never spent), `W2-S7` (OBS/INERT, the issuer's, now D0_INFRA_TIGHTENING row 11), `W2-S8` (OBS/ARMED, this criterion's own 900 s bound against a 651.6-826 s subject). The `<status>` was withheld TWICE while limb (ii) was unlanded and is flipped only now that DELIVERABLE 1 is met. ORIGINAL CUT: pending -- GO paired at cut (a seat order is dispatched by its issuance), SEQUENCED AFTER `NFRA_COMPEFFICACY.TO-CE-E-1` on the same slot. Authority: PRD **v0.10** @`1ba8b40a8f` (merged @`6aaf7cb20f`) s.9 row **M-5**, the round-7 L10's addendum on rows W1-S2 / W1-S3 / W1-S4; decomposition **v0.4** s.7, cell `CE-e-2`. The CTO's L10 (94836): "recut M-4 and M-5 as ONE issuance (round 8, one worker, CloudComp's paths, under Andrew's edict)".</status>

**Directive:** D11 | **Fabric:** laptop | **PRD:** `../prd/NFRA_COMPEFFICACY_PRD.md` v0.10 (s.9 row M-5; s.6 ruling R-8) | **Decomp cell:** `CE-e-2` (`../decompositions/NFRA_COMPEFFICACY_DECOMP.md` v0.4, s.7) | **outcome_ref:** FWD-9 (a tool cleared here stays cleared from any seat -- the limb a WORKER seat does not yet satisfy)

---

## THE CELL

`CE-e-2` -- **A TOOL VERIFIED BY ITS BARE NAME MUST BE THE TOOL YOU CHANGED.** `~/bin/` holds 186 generated forwarders emitted by `.tools/provision-path-shims.sh`, and each is baked to a LITERAL absolute path into the MAIN tree's `.tools/<name>`, with a fallback that only swaps `/c` for `/cygdrive/c` and never resolves anything relative to the caller. Spine v3 puts every worker in a LINKED WORKTREE (CLAUDE.md 14b). So a worker that edits a comp-tool in its worktree and verifies it by the bare name **runs the main tree's copy -- the file it did not change -- and the run succeeds, prints a plausible answer and returns rc 0.** That is the false GREEN of round-7 row `W1-S2`: the wrong-object result and the correct result are byte-identical, and nothing in the output says which file answered.

⛔ **THE FIX, BOTH LIMBS, AND THE SECOND IS NOT OPTIONAL.** (i) **RESOLUTION:** `.tools/provision-path-shims.sh` emits forwarders that resolve `.tools/<name>` from the CALLER'S `git rev-parse --show-toplevel`, with the baked path as the fallback, and every forwarder answers `--which` by printing the absolute target it would exec. (ii) **THE HARNESS:** `.tools/comp-which-routing-test.py` moves its `--out` default OFF the committed CloudComp baseline (`org/tier2_senior/0.8.0_AE_CloudComp/deliverables/comp-which-routing-baseline.json` -- its own `--help` already says a regression run must not clobber a committed baseline, and the default contradicts it), and states its timeout bound from a MEASURED runtime rather than a guessed one (round 7 measured rc 124 twice at ~601 s against a 600 s bound, and rc 0 at 680 s and 826 s -- rows `W1-S3` / `W1-S4`).

⛔ **FAIL LOUD, NEVER SILENT, WHEN THERE IS NO TOPLEVEL.** A forwarder invoked from outside any git worktree has no toplevel to resolve. It falls back to the baked path -- and it SAYS SO on stderr. A fallback that is silent re-creates the exact failure this cell exists to kill, one layer down: the caller cannot tell which file answered. State the behavior you built and exercise it.

⛔ **THE BLAST RADIUS IS 186 FILES AND EVERY SEAT ON THIS BOX.** These forwarders are how every shell reaches every comp-tool (profiles never load). A regeneration that breaks one name breaks it for every seat, including seats mid-order right now. So: regenerate, then EXERCISE a sample you name with its denominator, and keep the old forwarder bytes recoverable for the length of the order (a copy in your scratch, named in the record). If a name stops resolving, restore from that copy and file a BLOCKING row -- do not leave the fleet half-provisioned.

⛔ **THE REGENERATION IS A DEVICE-LOCAL DEPLOY, AND SPINE v3.9 @`d8400610bd` FIXES ITS ORDERING.** It writes 186 files OUTSIDE the repo that every seat on this box executes; nothing in git records it, so the only residue a death cannot take with it is what is TRUE IN THE WORLD. Therefore, in this exact order: **(1) OPEN** a change-management entry (`python .tools/deploy_ledger.py open --slug compefficacy-ce-e-2-forwarder-resolution ...`) naming what the run will overwrite (the 186 targets, the backup copy's absolute path) and the ROLLBACK (restore the backup, then re-run the PREVIOUS provisioner from `git show CLOUD:.tools/provision-path-shims.sh`); **(2) ACT** -- run the provisioner; **(3) CLOSE THE ENTRY AND COMMIT IT** before you take a single one of the reads that grade the act; **(4) READ.** A death between (2) and (3) leaves the box changed and the record silent, which is the expensive shape the clause exists to remove. Per row `W1-S16`, any detail the entry must CARRY is appended LAST, after its final ledger mutation, because the tool re-renders the entry from its sentinel on every mutation.

## DELIVERABLE

1. The fix (both limbs), committed on your branch.
2. `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~2/test_cee2_forwarders_resolve.py` -- the battery, and `the-forwarders-resolve-to-the-callers-toplevel.result.md` -- what you measured, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.
3. The proof-of-spec instance (below).

## BOUNDS

- **Your write surface is the `<paths>` block below**, PLUS the two grants the tree convention gives every worker without an entry -- your own `deliverables/<serial>/` folder and this face's `<status>`. A path you need that it does not name is a BLOCKING row, never an override.
- **`~/bin/` IS NOT A REPO PATH AND IS NOT IN `<paths>` -- it is written by RUNNING THE PROVISIONER**, which is. Edit the generator, run it, measure what it produced. Do not hand-edit a forwarder: a hand-edited shim proves nothing about the generator every future seat will run.
- **THE COMMITTED BASELINE IS READ-ONLY TO YOU:** `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/comp-which-routing-baseline.json` is another lane's artifact and is outside your grant. Prove by sha256 before and after that your work did not touch it; changing the harness's DEFAULT is the fix, rewriting the baseline is not.
- **A STORED BASELINE NAMES ITS ENVIRONMENT** (ruling R-8, PRD s.6): every hash, count or ranking you compare against names the tree it was captured in, the ranker mode, and the rendering of every hashed asset. `CE-e-1` lands before this cell for exactly that reason -- state whether it did.
- **EVERY invocation is bounded, and the bound is a number you have MEASURED.** `timeout 300` on reads; for the routing harness, state the bound you set and the runtime you measured beside it -- this cell's own subject is a bound that was smaller than its runtime.
- **Scratch:** `<your worktree>/.scratch/` only (the forwarder backup lives here and is named in the record).
- **A spec-vs-world divergence is a ROW** at `org/missions/D11/NFRA/NFRA_COMPEFFICACY/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `NFRA_COMPEFFICACY-W2-S<k>` (append; cite `path@commit`; never edit an existing row).
- **NEVER `git push`.** Report push state as MEASURED (`git ls-remote origin refs/heads/CLOUD`).

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9.

<criterion id="E2-AC1" cell_refs="CE-e-2"><invocation>timeout 900 python org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~2/test_cee2_forwarders_resolve.py</invocation><expect>CEE2-FORWARDERS-RESOLVE-TO-CALLER</expect></criterion>
`E2-AC1` -- a battery you write, printing the token ONLY when every arm holds: (a) THE POPULATION: the forwarders regenerated by the provisioner, counted, with the denominator RE-DERIVED at your seat and printed beside round 7's cited 186 (say if they differ and why); (b) BOTH DIRECTIONS OF THE RESOLUTION, which is the whole cell: `comp-which --which` from the MAIN tree prints the main tree's `.tools/comp-which`, and from a FRESH LINKED WORKTREE prints THAT worktree's -- both absolute paths printed, and the two differ; (c) THE PLANTED EDIT, because a path that merely PRINTS right can still EXEC wrong: a one-line marker added to the worktree's `.tools/comp-which` appears in the bare-name run FROM that worktree and does NOT appear in the bare-name run from the main tree (both outputs printed), then the marker reverted and the file sha256-verified back; (d) THE NO-TOPLEVEL CASE: a forwarder invoked from a directory that is not inside any worktree falls back to the baked path AND SAYS SO on stderr (the exact line printed) -- rc and stream both recorded; (e) THE HARNESS: its bare invocation writes NOTHING under `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/` (that file's sha256 identical before and after, printed) and completes inside the bound the file now states, with the runtime you measured printed beside the bound; (f) NOTHING ELSE MOVED: a sample of other forwarders you name, exercised after the regeneration, with the denominator (sample of population) -- and the backup copy's location printed. Denominators on every list; every path printed absolute.

<criterion id="E2-AC2" cell_refs="CE-e-2"><invocation>bash -n .tools/provision-path-shims.sh; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`E2-AC2` -- the generator parses. A syntax error in the file that writes 186 forwarders is the one failure that would take every comp-tool on this box down at once, and it costs one line to exclude.

<criterion id="E2-AC3" cell_refs="CE-e-2" judgment="true"/>
`E2-AC3` -- graded by the CVO at L9: whether a worker seat can now verify its own comp-tool edit (FWD-9's sentence, read against a worker seat rather than this one); what the no-toplevel fallback does and whether its loudness is enough to tell a caller which file answered; whether the harness's new bound is stated from a measurement and what its runtime spread was; and what a future worker still cannot see from inside its worktree. Evidence with vintage. NO VERDICT.

<expected_criteria>E2-AC1, E2-AC2, E2-AC3</expected_criteria>

<paths>
.tools/provision-path-shims.sh
.tools/comp-which-routing-test.py
infra/system/06_current_state.md
infra/system/06_current_state.json
org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~2/
org/missions/D11/NFRA/NFRA_COMPEFFICACY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

⛔ **GRANT WIDENED 2026-09-10 ~05:2xZ BY THE ISSUER on row `NFRA_COMPEFFICACY-W2-S9`, AND THIS REVERSES MY OWN
CALL OF FORTY MINUTES AGO.** On `W2-S6` I chose to regenerate `infra/system/06_current_state` MYSELF on CLOUD
rather than widen this grant, reasoning that widening a worker's grant onto a shared estate artifact is the worse
trade because the grant is the lane. **The world refuted that and the assignee measured exactly why: THE LOOP DOES
NOT CONVERGE.** `_source_fingerprint()` reads the WORKTREE (`content_fingerprint(_SOURCES, rel_root=WS)`), so a
regeneration performed on any tree the pending edit is NOT in necessarily re-drifts the moment the edit exists;
`_dirty_sources()` takes `line[3:]` of `git status --porcelain`, so staging does not help either -- a file is dirty
staged or not. Regenerate -> the pending edit re-drifts it -> the gate refuses because a source is uncommitted ->
the edit cannot be committed -> 06 can never cover it. **My remedy was correct AS AN ACT and could never have been
sufficient, and no number of repetitions of it would change that.**

The assignee proved my regeneration landed rather than assuming it: the refusal fingerprints MOVED
(`4270b32... -> f50fbd7...` became `491f0189b4..., 260 -> a8192f19f4..., 260`), and it called
`comp_system._source_fingerprint()` in-process against HEAD's harness to get `491f0189b4...` **byte-identical to
`06_current_state.json`'s own `header/source_fingerprint`** -- so 06 describes every COMMITTED source in that tree
perfectly and the uncommitted edit is the sole remaining delta. It then restored its edited copy and re-verified
the sha256, losing nothing to take the measurement.

**THE ONLY EXIT IS A REGENERATION IN A TREE WHERE THE EDIT IS PRESENT, committing `infra/system/06_current_state.
{md,json}` in the SAME COMMIT as `.tools/comp-which-routing-test.py`.** The two paths above are added for exactly
that and for nothing else. ⛔ **The `system-current-override:` escape remains available and REMAINS UNSPENT, and it
should stay unspent** -- the override exists for a case where regeneration is impossible, and here it is merely
impossible FROM OUTSIDE THE TREE. The predicate's own docstring names the intent it cannot express
(*"regenerating now would launder a PEER'S unlanded work"*): it cannot tell a peer's unlanded work from the file
THIS VERY COMMIT IS LANDING, and that is a real gap in the gate rather than a misuse by this seat.

**RECORDED BECAUSE IT IS THE ISSUER'S ERROR TWICE OVER:** the first version of this order granted `.tools/comp-*`
paths while omitting the one path the gate demands before such a commit can land, which is `D0_INFRA_TIGHTENING`
row 11's own class -- an order asking for an act its own grant forbids. `W2-S7` is the same class on this same
face. I did not amend mid-flight when the seat was unblocked; I am amending now because it is blocked and the
amendment is what unblocks it.


<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_COMPEFFICACY/decompositions/NFRA_COMPEFFICACY_DECOMP.md</decomp_doc> v0.4, cell `CE-e-2`.
<owned_cells>CE-e-2</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-09 ~22:2xZ, its VINTAGE STATED rather than re-run at this issuance -- WITHIN BUDGET, scanned 5 of 5 carriers, 56.25 s of a 90 s default, GATES ARMED 25, REACHED-DENOMINATORS C1=23 C2=6 C3=12 C4=20 C5=335, and ZERO of the 25 armed gates names NFRA_COMPEFFICACY, the shim provisioner, the routing harness or the comp-tool registry. THE VINTAGE HOLDS BECAUSE: no schedule, rule or gate has been created or changed in this project's surface since that read, and this cell touches no scheduled surface. BLIND SPOT, stated: the gate ledger cannot see a PATH-resolution defect in a generated shim -- the accept's two-direction `--which` arm and the planted edit ARE that control.
comp-iam: DECLARED-NOT-APPLICABLE -- no cloud plane touched, nothing granted, nothing applied.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`) plus the two tree-convention grants. Both files' owning lane is CloudComp (T-1/T-3), which holds no session tonight; the CTO's L10 (94836) places the recut here under Andrew's ~22:3xZ edict, and the grant is the paths, stated here and in the decomposition. The CloudComp BASELINE artifact is named READ-ONLY in BOUNDS and is deliberately absent from the grant.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `E2-AC1`, `E2-AC2`, `E2-AC3`. Instance at
`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.9.0_WK_NFRA_COMPEFFICACY~2/NFRA_COMPEFFICACY.TO-CE-E-2.the-forwarders-resolve-to-the-callers-toplevel.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), validated with `python .tools/proof-of-spec-check.py <instance> E2-AC1,E2-AC2,E2-AC3` BEFORE the complete flip, which you commit yourself. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when the mechanical criteria PASS BY OUTPUT and the instance validates rc=0.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
