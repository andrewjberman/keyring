# TO IRPT_ANLREQ.TO-AR-y-301.resident-apply-scripts-r28 -- WRITE the three host scripts the resident applier will run for release 28 (pre-read, install with read-backs, rollback) from the release-19 scripts, and stage the package sums

<to_id>IRPT_ANLREQ.TO-AR-y-301</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~119</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>31</round>
<workstream>YV</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-301` (`decompositions/IRPT_ANLREQ_DECOMP_R31A_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~119`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-119` (branch `wk-IRPT_ANLREQ-119`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~119 <0.9.0_WK_IRPT_ANLREQ~119@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W119-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no `aws`, `ssh` or SSM, no push, no deploy, no upload, no apply, no invoke. You write files; you run none of them. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-301`, inlined) -- WRITE ONLY. Nothing is run on the host, uploaded, installed or applied. The scripts are files; the applier `0.7.0_AE_CloudOps~YC2` runs them under a later order.

*The resident leg (L4) of the signed release-28 pair (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release28/NEVER_WIDEN_PAIR_ANLREQ_RELEASE28_FWD1_CONSOLIDATED_FOUR_LEG.md`, COO blob `e9bb20d7fe`, CTO half signed) installs root `0485393f3a-r28` over the running `0485393f3a-r19`. Release 19 ran three scripts through `host_read.py` (Systems Manager): `pre_read_r19.sh` (the stop-reads before anything moves), `install_r19.sh` (fetch the signed host script and the package sums BY KEY and verify their sha256, run it, read the running package back) and `rollback_r19.sh` (put the previous root back; it exits before moving anything if the rollback root, its receipt copy or the library is missing), under `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release19/`. The tarball (`C:/dev/irpt-release-r28/irpt-resident-0485393f3a-r28.tar.gz`, sha256 `80f4743091a10c0d82b6cba4f66ba4afb6188ece0b64b269066c5426a6335a68`), the host script (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~118/r30/resident_host_install_0485393f3a-r28.sh`, sha256 `bbead0d2b560ca49be3ab1e758d3111c22174e755771a46bce23ae3977122832`) and the build record (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~118/r30/RESIDENT_BUILD.json`) exist. What does not exist: the three wrapper scripts for release 28 with the right constants and read-backs, and the package sums file as a separate staged key (release 19 staged `irpt-resident-0485393f3a-r19.package.SHA256SUMS` beside its tarball). These scripts run as root-equivalent on a production host, so they are written against the old ones line by line and checked by `bash -n`, never improvised.*

1. **Read first, in full:** the three release-19 scripts under `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release19/`, the host script of release 28 and of release 19 (`diff` them; the record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~118/r30/RESIDENT_BUILD.json` names the changed lines), and the build record's `release_input`, `delta_vs_live`, `root_naming`, `host_script` and `tests`. The release-19 order that ran them: `org/tier2_senior/0.7.0_AE_CloudOps~YC2/task_orders/IRPT_ANLREQ.TO-APPLY-R19a.resident-reader-release-yc2.md` (its steps 4 and 5 state what each script is expected to print) and its output `org/tier2_senior/0.7.0_AE_CloudOps~YC2/deliverables/irpt_anlreq_r19/` (`P1_PRE_READ_R19.txt`, `D2_V1_INSTALL_R19.txt`: what the host printed).
2. **Stage the package sums.** Extract the member `SHA256SUMS` from the release-28 tarball and stage it as `C:/dev/irpt-release-r28/irpt-resident-0485393f3a-r28.package.SHA256SUMS`; record its sha256 and line count (expected 298). CONTROL: do the same for the release-19 tarball (`C:/dev/irpt-release-r19/irpt-resident-0485393f3a-r19.tar.gz`) and show the result equals the staged `irpt-resident-0485393f3a-r19.package.SHA256SUMS` there (sha256 `a3dea4ec9afe05db66db96e8110064e70a6ba7ea50e4d04038cdee301ddfa933`): that proves the method is the one release 19 used.
3. **Write `r31/pre_read_r28.sh`** from `pre_read_r19.sh`: the same five stop-reads (each printing exactly `P1 STOP-READ PASS`, `P1 STOP-READ-2 PASS`, ... `-5 PASS`, or a FAIL line, and installing NOTHING). Change ONLY what the old root changed: the running root is now `0485393f3a-r19` (OLD) and the new root `0485393f3a-r28` must NOT exist yet; the reader members read at the r19 values (`intake/uploads.py` sha256 `176682cb1545435eec084376b3c37a578ca70d05f9ad5a376c0f2275f62b05ea`, `intake/template_reader.py` `83ab9b45d59065f53c640803df9fd07a0ddfcc97d89c13540c20622a6bf7bd58`, `READER_VERSION irpt-template-reader.r18.1`); the rollback root for THIS release is `0485393f3a-r19` itself (its directory and its receipt exist); the queue `irpt-generation` reads `0 0`; the capture library and wrapper pins are unchanged from release 19 (read them from the r19 output). Print a `diff` of the two scripts and justify every changed line against the build record or the r19 output.
4. **Write `r31/install_r28.sh`** from `install_r19.sh`: `NEW=0485393f3a-r28`, `OLD=0485393f3a-r19`, `WANT` = the sha256 of the release-28 host script, `WANTSUM` = the sha256 of the staged sums file from step 2; the fetch-by-key and sha256 gates, the run of the host script, and the read-backs stay, with these changes: the member checks print and compare the EIGHT moved code members and the added calendar against the build record's values (the expected sha256 values come from the record, NOT from the script's own computation); `V1 P3` checks the package sums (298 entries, 0 mismatch, as the record's `sha256sums_check` states); the `READER_VERSION` expected is `irpt-template-reader.r19.3`; add read-backs that the new members import (`opal_packager`, the registry port in `resident_worker`, `trading_calendar` from `lib/`) in the same proof-process style as the producer and reader imports, and that `yfinance_check.py` is ABSENT from the root; the rollback root is `0485393f3a-r19`. Keep every guard that makes the script refuse before moving anything. Print a `diff` against `install_r19.sh` and justify every changed line.
5. **Write `r31/rollback_r28.sh`** from `rollback_r19.sh`: it puts `0485393f3a-r19` back as the running root and exits before moving anything if the rollback root, its receipt copy or the library is missing; same guards, constants changed to this release. Print the diff.
6. **Check each script.** `bash -n` on each (rc 0, printed); a scan for non-ASCII (none); a scan that no secret, token or key is in any script; and a DRY run of the sha256 gates only, on THIS machine, outside the host: copy the staged host script and sums into a scratch folder, run the two `sha256sum` comparisons the install script performs against the signed constants (both equal), and show that changing one byte of a copy makes the comparison refuse (the guard fires). Never run the scripts themselves; never run `aws`, `ssh` or SSM.
7. **Write `r31/RESIDENT_APPLY_SCRIPTS.json`:** `scripts` (objects: `name`, `path` (repository-relative), `sha256`, `bytes`, `bash_n_rc`, `lines_changed_vs_r19`, `constants` (name -> value and the source of each), `expected_readbacks` (what each printed line must read and where the value comes from)), `sums_file` {`path`, `sha256`, `lines`, `control_r19_equal`}, `host_script` {`path`, `sha256`}, `tarball` {`path`, `sha256`}, `guard_dry_run`, `claim`, `not_read` (the host; the SSM runner; anything the old output did not show).
8. **In your report:** the sha256 of each script, every constant changed and its source, the guards kept, what the scripts print on success, and anything in the release-19 scripts that does not fit this release.

### ACCEPTANCE

<criterion id="AR301-y-AC1" cell_refs="AR-y-301"><invocation>python C:/dev/wk-irpt-anlreq-119/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y301-scripts --root C:/dev/wk-irpt-anlreq-119</invocation><expect>Y301-SCRIPTS-OK</expect></criterion>
`AR301-y-AC1`: the record names three scripts that exist in the repository with the recorded sha256, bash -n rc 0, the install script's constants equal the signed host script's and the staged sums file's real sha256, and the staged sums file equals the tarball's own SHA256SUMS member (298 lines).

<criterion id="AR301-y-AC2J" cell_refs="AR-y-301" judgment="true"/>
`AR301-y-AC2J` (judgment, graded at L9, never by you): every changed line against the release-19 scripts is justified from the build record or the r19 output, every guard that makes a script refuse before moving anything is kept, the expected read-backs come from the build record and not from the script's own computation, and nothing was run on the host or against AWS.

<expected_criteria>AR301-y-AC1 AR301-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~119/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R31A_Y.md</decomp_doc>
<owned_cells>AR-y-301</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~119/IRPT_ANLREQ.TO-AR-y-301.resident-apply-scripts-r28.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-301`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR301-y-AC1,AR301-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- files in the worker's deliverable folder and a staged sums file outside the repository; no host, SSM or AWS call; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the release-19 install script and its host output against the cell; the lens: a constant carried over from release 19 that is wrong for release 28, a read-back whose expected value the script computes from the thing it checks, a guard dropped to make a diff look small. The order requires every expected value from the build record, every guard kept, and a dry run of the sha256 gates with a one-byte change that must refuse. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the signed release-28 pair (CTO msg 7415) as workstream `YV` round 31: the resident apply scripts the applier `~YC2` will run. The Lambda legs need no new scripts (their orders rebuild from the recorded inputs). Base: `AR301-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
