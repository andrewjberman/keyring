# TO IRPT_BCKEND.TO-IB-pr-261 -- Ship lib/silver_ids.py to where the INF gold runner resolves it, then ONE real chain run reaches the raw writers

<to_id>IRPT_BCKEND.TO-IB-pr-261</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~97</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO ROUND-25 ~P ANALYSIS section 1 (ruling 103057: SHIP, not revert;
`org/missions/D9/IRPT/IRPT_BCKEND/ledger/ROUND_ANALYSIS.round25P_sweep3_4.md` @dd4c69b696); rows W86-S1 (BLOCKING) and S216 (BLOCKING) |
**Decomp cell:** `IB-pr-261` (decomposition section 24) | **outcome_ref:** FWD-3 (INF) | **depends_on:** none

---

## WORKER FACE

**The cell.** Since 2026-09-28 the Inflection gold chain on EC2 `inf-gold-layer-runner` (`i-0ed5afded2ebd4ed4`) dies at its
third step `INF_API_SILVER_REPS` with `ModuleNotFoundError: No module named 'lib.silver_ids'`, so the three raw writers that
sit after it (`INF_API_PULL_TXN`, `INF_API_PULL_PERF`, `INF_API_PULL_POSITIONS_DAILY`) never run and no
`bronze/{transactions,performance,positions}/<date>.jsonl.gz` has landed since 09-27. Today's scheduled run
`chain_full_20260930_113346` failed the same way at 11:34:54Z (`s3://opal-data-inf/telemetry/inf-gold-layer-runner/status.json`).
Cause (row W86-S1, diagnosis `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~86/ON_INSTANCE_DIAGNOSIS.json`):
`data/inf/scripts/silver/_orion_api_silver_lib.py:284` reads `from lib.silver_ids import DEFAULT_SILVER_ID_COLS, coerce_silver_ids`
(moved into `lib/silver_ids.py` by 8cd218cd05 on 09-28) and that changed lib was deployed to `s3://opal-data-inf/code/silver/` at
07:17:53Z the same day WITHOUT its new dependency: `lib/silver_ids.py` is in no `code/` prefix (HeadObject 404 on
`code/gold/lib/silver_ids.py`, `code/lib/silver_ids.py`, `code/silver/lib/silver_ids.py`; `code/silver/silver_ids.py`,
`code/gold/silver_ids.py`, `code/bronze/silver_ids.py`, `code/manual_api/silver_ids.py` also printed nothing at the cut -- re-measure).

**The ruling you execute (CTO 103057).** SHIP `lib/silver_ids.py`; do NOT revert the import to an inline copy. The deploy is a code
deploy that moves no served key: no never-widen half is owed, but it carries a change-management ledger entry opened BEFORE the first
S3 write and closed at completion (CLAUDE.md NEVER-2). And the CTO's one condition, verbatim in scope: **you print how the running
box resolves `lib.` BEFORE you copy anything -- the S3 code layout the runner syncs and the sys.path a step builds are the two
readings, and a guess at either is a refusal.**

**What the issuer read at the cut (you re-read and cite; if your reading differs, YOUR reading wins and you say so):**
1. *Sync layout.* `data/inf/scripts/gold/orion-gold-dispatch.sh:65` sets `SCRIPTS="/tmp/orion_gold_scripts"`; `sync_scripts()`
   (about lines 545-620) inventories `code/gold/`, `code/manual_api/`, `code/silver/`, `code/bronze/` and writes ONE FILE PER BASENAME
   into that flat directory (`open(os.path.join(dest, fname))`), refusing loud on a basename present in two prefixes with different
   bytes. No subdirectory survives the sync: `code/gold/lib/dtype_coerce.py` lands as `/tmp/orion_gold_scripts/dtype_coerce.py`, which
   is why every INF gold script imports it FLAT (`from dtype_coerce import coerce_id_columns`, e.g.
   `data/inf/scripts/gold/INF_A_00.accounts_dimension.py:80`). `_orion_api_silver_lib.py` is the ONLY file under `data/inf/scripts`
   that imports `from lib.` (comp-find at the cut: 1 hit across 174 files). The deployed dispatch is
   `s3://opal-data-inf/code/gold/orion-gold-dispatch.sh` (LastModified 2026-08-30, 113,320 bytes); compare its sha256 to the repo
   copy (repo sha at the cut `d6b00f6fdd75...`) and cite which one you read.
2. *sys.path.* A step runs the script from the flat directory, so `sys.path[0]` is `/tmp/orion_gold_scripts`;
   `_orion_api_silver_lib.py:279-282` inserts `_REPO_ROOT` = four directories above itself, which from
   `/tmp/orion_gold_scripts` is `/`. The name `lib` therefore resolves as a namespace package over `/lib` (a real system directory
   with no `silver_ids.py`) -- exactly the error text. Confirm from the traceback in
   `s3://opal-data-inf/diagnostic/chain_logs/chain_full_20260930_113302.log` (or the newest `chain_full_20260930_*.log`).
   If the box materializes a `lib/` directory anywhere on that path (it does not, per the sync code -- but the reading decides),
   ship to the key that lands there and skip the fallback below.

**The ship, as the readings above predict it (two objects, one ledger):**
- (a) `aws s3 cp lib/silver_ids.py s3://opal-data-inf/code/silver/silver_ids.py` -- flat, beside its importer, the same convention
  every other INF script uses. `lib/silver_ids.py` stays the ONE implementation in the repo (byte-identical copy on S3; it imports
  only pandas). Before the copy, probe the same basename in every OTHER synced prefix (`code/gold/silver_ids.py`,
  `code/bronze/silver_ids.py`, `code/manual_api/silver_ids.py`) with `aws s3api head-object` and record the HTTP result of each; a
  200 with different bytes is a refusal (the flat sync would abort the whole chain).
- (b) In `data/inf/scripts/silver/_orion_api_silver_lib.py` replace line 284 with the repo import FIRST and the flat fallback second:
  ```python
  try:
      from lib.silver_ids import DEFAULT_SILVER_ID_COLS, coerce_silver_ids  # noqa: E402,F401
  except ModuleNotFoundError:
      # The EC2 gold runner syncs every code/ prefix FLAT by basename (orion-gold-dispatch.sh sync_scripts), so on
      # the box silver_ids.py sits beside this file; the repo layout keeps lib/silver_ids.py as the one implementation.
      from silver_ids import DEFAULT_SILVER_ID_COLS, coerce_silver_ids  # noqa: E402,F401
  ```
  Commit it in your worktree (`.tools/safe-commit.sh` under your serial), then deploy it with the Rule-13 mechanism:
  `bash .tools/safe-deploy.sh --author 0.9.0_WK_IRPT_BCKEND~97 data/inf/scripts/silver/_orion_api_silver_lib.py`.
  If safe-deploy refuses your serial, record the refusal text verbatim in the readings deliverable and do the deploy as
  `aws s3 cp data/inf/scripts/silver/_orion_api_silver_lib.py s3://opal-data-inf/code/silver/_orion_api_silver_lib.py`; either way
  the target's sha256 must equal your committed file (P26-1-AC1 verifies).
- Ledger: `python .tools/deploy_ledger.py open --slug inf-silver-ids-ship-20260930 --title "<one line>" --author 0.9.0_WK_IRPT_BCKEND~97
  --leg "U1|verify|the two readings + collision census|readings deliverable written, every collision probe 404"
  --leg "D1|activation|code/silver/silver_ids.py + code/silver/_orion_api_silver_lib.py|sha256 of each S3 object equals the committed file"
  --leg "R1|verify|one real full chain run|status.json newer run, SILVER_REPS ok, PULL_POSITIONS_DAILY ok, raw jsonl.gz for the run date"`
  BEFORE the first S3 write; `close-leg` each with its proof; `close` at the end. Commit the entry AND the sentinel
  `org/critical_paths/.open_deploys/inf-silver-ids-ship-20260930.json` as soon as they exist (the sentinel is what survives).
- The readings deliverable: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~97/RESOLUTION_READINGS.json` with
  keys `sync_layout`, `deployed_dispatch`, `sys_path_reading`, `resolved_targets` (list of `{s3_key, repo_path, sha256}`),
  `collision_census` (list of `{s3_key, http}`), each a measured statement with the line or key it cites.

**The real run (the CTO's acceptance; the copy's rc is not it).** Dispatch is RELEASED at the live trigger
(`INF_GOLD_DISPATCH_RELEASE` reads the sentinel, read at the cut). Invoke ONE ad-hoc full run:
`.tools/aws lambda invoke --function-name inf-gold-trigger --cli-binary-format raw-in-base64-out --payload '{"mode":"full","source":"manual-IRPT_BCKEND-IB-pr-261"}' <your deliverables dir>/trigger_invoke.json`
then poll `s3://opal-data-inf/telemetry/inf-gold-layer-runner/status.json` (`aws s3 cp ... -`) in calls of at most 100 s each
(`sleep 60` inside) until `status` is terminal or 100 minutes have passed -- never one unbounded loop. The full chain is 65 steps and
ran about an hour on 09-27. A refusal from the trigger (the dispatch lock held by another run, or a hold) is recorded verbatim; wait
for the lock's TTL (5,400 s from the other run's start) and invoke once more, not a third time.
After the run, record (in the readings deliverable, key `after_run`): the run_id and status, and which of
`bronze/positions/2026-09-28.jsonl.gz`, `bronze/positions/2026-09-29.jsonl.gz`, and the run date's three raw files exist. If the
09-28/09-29 raw positions did NOT land (the daily pull is a snapshot of the run day), that is a FINDING in a surprise row, not a
failure of this cell. Do not restart, reboot or SSM into any instance; the trigger starts the box itself.

<criterion id="P26-1-AC1" cell_refs="IB-pr-261"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r26/p26_1_ac1_silver_ids_shipped.py" .</invocation><expect>P26-1-AC1 PASS</expect></criterion>
`P26-1-AC1` -- the readings deliverable exists with all five keys non-empty; every `resolved_targets` object on S3 is byte-equal
(sha256) to the worktree file it names; every `collision_census` probe reads 404. Base: FAIL (deliverable absent), measured at the cut.

<criterion id="P26-1-AC2" cell_refs="IB-pr-261"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r26/p26_1_ac2_chain_real_run.py"</invocation><expect>P26-1-AC2 PASS</expect></criterion>
`P26-1-AC2` -- `status.json` reads a run newer than `chain_full_20260930_113346` whose `steps_done` carries `INF_API_SILVER_REPS` ok
and `INF_API_PULL_POSITIONS_DAILY` ok, and `bronze/positions/<run date>.jsonl.gz` exists with LastModified after 12:00Z today.
Base: FAIL (run 113346 status failed at SILVER_REPS), measured at the cut. Run it only after the chain is terminal.

<criterion id="P26-1-AC3" cell_refs="IB-pr-261"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r26/p26_ledger_closed.py" . inf-silver-ids-ship-20260930 P26-1-AC3</invocation><expect>P26-1-AC3 PASS</expect></criterion>
`P26-1-AC3` -- the ledger entry for the slug is CLOSED with every leg closed and no sentinel. Base: FAIL (no entry), measured at the cut.

<expected_criteria>P26-1-AC1,P26-1-AC2,P26-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. `lib/silver_ids.py` is READ only (never
  edited; it is fabric-owned). No edit to `orion-gold-dispatch.sh`, to any gold script, or to the trigger.
- **AWS writes admitted:** the two `code/silver/` objects named above, the one `lambda invoke` of `inf-gold-trigger`, nothing else.
  No `ec2 start-instances`, no SSM, no other bucket, no Terraform.
- **Refusal clause.** If a reading contradicts the predicted shape and no key makes `lib.silver_ids` importable without editing a file
  outside the grant, stop, write the reading and the reason in your report and a surprise row (`IRPT_BCKEND-W97-S<k>`), and do not
  weaken a check.

<paths>
lib/silver_ids.py
data/inf/scripts/silver/_orion_api_silver_lib.py
data/inf/scripts/gold/orion-gold-dispatch.sh
org/critical_paths/change_management/
org/critical_paths/.open_deploys/inf-silver-ids-ship-20260930.json
org/safe-deploy-bypass-audit.log
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r26/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 24 (round 26, workstream ~P), cell `IB-pr-261`.
<owned_cells>IB-pr-261</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P26-1-AC1, P26-1-AC2, P26-1-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~97/IRPT_BCKEND.TO-IB-pr-261.silver-ids-ship-and-real-run.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P26-1-AC1 P26-1-AC2 P26-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hashes, each criterion's last line, the run_id and the raw files that landed, and any
surprise row id (`IRPT_BCKEND-W97-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule changes; the ad-hoc run is a QA run of the existing daily chain (CLAUDE.md: ad-hoc runs permitted for QA; the scheduled fire stays the acceptance and fires tomorrow 11:3xZ on the same code).
comp-iam: DECLARED-NOT-APPLICABLE -- 0 roles touched; the runner already reads code/silver/.
comp-blast: RUN -- two S3 code objects under code/silver/ (one new basename, one changed importer); the chain's 65 steps read the flat sync; a basename collision is refused loud by the sync itself.
comp-routes: DECLARED-NOT-APPLICABLE.
comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- P26-1-AC1 base FAIL (deliverable absent); P26-1-AC2 base FAIL (run 113346 failed at SILVER_REPS, read 14:1xZ); P26-1-AC3 base FAIL (no entry); p26_ledger_closed positive control on the CLOSED W24 entry PASS.
lane: the <paths> block IS the grant.
ruling_scope: the flat fallback import keeps `from lib.silver_ids` first and is the flat-sync accommodation every INF script already carries; it is not the revert CTO 103057 refused. Stated in the issuance commit; the CTO reads it at the round-26 analysis.
</preflight>
