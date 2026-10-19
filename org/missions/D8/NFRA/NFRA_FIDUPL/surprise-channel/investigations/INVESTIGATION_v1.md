# NFRA_FIDUPL -- surprise channel, INVESTIGATION v1 (round 1, dell1 fabric)

**Opened by:** `2.0.0_SA_COO~P1` at the L6 cut (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`).
Lane `ANY`.
**Id grammar:** a worker's row is `NFRA_FIDUPL-D1-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that coordinate); a
seat's row is `NFRA_FIDUPL-D1-S<k>`; the CVO's adjudication rows live in `../adjudications/` as `NFRA_FIDUPL-D1-C-S<k>`.
**Append-only during the round.** Never edit an existing row.

```json
[
  {
    "id": "NFRA_FIDUPL-D1-S1",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~P1",
    "surfaced_at": "2026-10-19T20:15:59Z",
    "one_line": "The naming builder homes the code and state tiers of scope alongside in opal-data-alongside, a bucket that does not exist, and admits no meta or _ops tier, so round 1 puts the run record in the bronze tier as table _runs and delivers box code by SSM instead of an S3 code home.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~DELL1 (owns the confirmation of the _runs home and the final code home; this seat only surfaces)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -c \"import sys; sys.path.insert(0,'lib'); import opal_naming as o; print(o.address('fidelity','alongside','state','daily_pull','20261016','run.json'))\" (2026-10-19 ~20:0xZ) printed s3://opal-data-alongside/fidelity/alongside/state/daily_pull/20261016/run.json",
        "the same call with tier 'code' printed s3://opal-data-alongside/fidelity/alongside/code/canonical-fidelity/x; with tier 'meta' and with '_ops' it raised: tier is not one of NAMING_SCHEMA.json key.tier (enum bronze, silver, gold, platinum, state, code)",
        "address('fidelity','alongside','bronze','_runs','20261016','run.json') printed s3://opal-data-assets/fidelity/alongside/bronze/_runs/20261016/run.json",
        "CTO msg 8473: opal-data-alongside is NOT provisioned"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C-NAMES: every address is lib/opal_naming.py address() output; the Schwab run record lives under {source}/{scope}/_ops/daily_pull/ and meta/pulls/ and its code under an S3 code prefix.",
    "world_is": "For scope alongside the builder gives the code and state tiers a bucket that does not exist and has no tier for a run record, so a builder-clean run record and code home exist only in the bronze tier of opal-data-assets (the _runs table) and by SSM delivery to the box.",
    "notes": "Decision recorded in decompositions/NFRA_FIDUPL_DECOMP.md section 7 items 1 and 2. Nothing acts on a typed path."
  },
  {
    "id": "NFRA_FIDUPL-D1-W3-S1",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~3",
    "surfaced_at": "2026-10-19T20:32:10Z",
    "one_line": "The handoff contract's failure field admits only four strings, so an unexpected exception in read_secret, open_session, fetch_day or close has no legal failure value; box/run.py writes failure null with all six names in missing, a run_error key holding stage and exception class name, and returns non-zero.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~P1 (owns the failure vocabulary for an unexpected stage exception; the lander's handling of failure null with missing names is unverified until FU-s-4 lands)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md section 5 (worktree HEAD 58aa7802b5): failure is null or exactly one of sign-in refused, code never arrived, export not generated yet, download refused",
        "infra/aws/ec2/canonical-fidelity/box/run.py in worktree wk-NFRA_FIDUPL-3 (uncommitted at filing): run_error branches in run_once write failure None",
        "task order NFRA_FIDUPL.TO-FU-s-5 names only the SigninError failure path; the other exception paths are not specified"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Reference section 9: whatever stage fails, land is still called on a handoff directory whose listing.json carries the failure, so the record is always written.",
    "world_is": "For a non-sign-in exception the listing cannot carry a contract failure string; it carries failure null, missing lists all six names, and run_error names the stage. A lander that reads failure null as a clean day would record a silent empty run, so the missing list is the only guard.",
    "notes": "Decision for the COO: a fifth failure string, or a rule that missing names with failure null is a failure. Nothing acts on this until ruled."
  },
  {
    "id": "NFRA_FIDUPL-D1-W3-S2",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~3",
    "surfaced_at": "2026-10-19T20:32:10Z",
    "one_line": "The sibling modules signin.py, fetch.py, land.py and quo_otp.py are not in this worktree at HEAD 58aa7802b5, so box/run.py wires them from the reference section 9 signatures alone and the wiring is unverified.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "ls infra/aws/ec2/canonical-fidelity/ in worktree wk-NFRA_FIDUPL-3 printed no such directory at HEAD 58aa7802b5",
        "box/run.py main() calls quo_otp.QuoOtpReader(quo_otp.default_api_key, line_id=..., sender=...), signin.open_session(config, creds, otp), fetch.fetch_day(fetch.PlaywrightSession(handle.context), day, out_dir), land.land(handoff, scope)",
        "reference section 9 gives the signatures; whether api_key_provider is a callable and whether PlaywrightSession takes a context are not measured"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Reference section 9: each module is built against fakes and the cells compose through the fixed interfaces.",
    "world_is": "The composed wiring is exercised only by fakes in this cell; the first live composition is FU-x-1.",
    "notes": "Tests inject fakes via a dict of callables; main() wiring is not exercised by any test in this cell."
  },
  {
    "id": "NFRA_FIDUPL-D1-W3-S3",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~3",
    "surfaced_at": "2026-10-19T20:32:10Z",
    "one_line": "The bootstrap assumes Amazon Linux 2023 offers python3.12 and python3.12-pip through dnf, a package name not measured; the sibling exporter installs into a python3.9 site-packages path on the same OS family.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "infra/aws/ec2/inf-exporter/user-data.sh line 20 (worktree HEAD 58aa7802b5): python3 -m pip install --target=/usr/lib/python3.9/site-packages/",
        "infra/aws/ec2/canonical-fidelity/box/bootstrap.sh amzn branch: dnf install -y python3.12 python3.12-pip (not run; no AL2023 host was reached from this worktree)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Reference section 1: the box runs Python 3.12 or newer.",
    "world_is": "The package name and its availability on AL2023 are unmeasured; bootstrap.sh fails loud when the interpreter is older than 3.12, so an absent package surfaces as an explicit error, not a silent old interpreter.",
    "notes": "FU-x-1 or the first bootstrap run on a fresh host measures it."
  },
  {
    "id": "NFRA_FIDUPL-D1-W3-S4",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~3",
    "surfaced_at": "2026-10-19T20:40:00Z",
    "one_line": "The worktree is a cone-mode sparse checkout whose cone omits infra/aws/ec2/canonical-fidelity, a granted path that did not exist at the cut, so git add and safe-commit could not stage the new box and test files; the worker added that one granted path to its own worktree cone with git sparse-checkout add.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git config core.sparseCheckout true and git sparse-checkout list in worktree wk-NFRA_FIDUPL-3 (before the add) listed .tools, infra/aws/ec2/bd-exporter, infra/aws/ec2/inf-exporter, lib, org paths and no canonical-fidelity",
        "git add -n -f -- infra/aws/ec2/canonical-fidelity/box/run.py printed: matched paths that exist outside of your sparse-checkout definition, so will not be updated in the index",
        "safe-commit.sh stage then failed with pathspec did not match any file(s) known to git for the three new files; no commit was made"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Lane gate: a worker writes exactly the paths its order names; the cut built the worktree from the order's paths and the paths existing at the cut.",
    "world_is": "A granted path that is created by the order itself is absent from the cone built at the cut, so a new module directory cannot be staged until the cone includes it. The fix touches only this worktree's sparse definition and no file outside the grant.",
    "notes": "The cut's sparse-cone builder reads existing paths only. Whether other cells of the round hit the same cone gap is for the COO to check across the seven other worktrees."
  },
  {
    "id": "NFRA_FIDUPL-D1-W2-S1",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~2",
    "surfaced_at": "2026-10-19T20:37:00Z",
    "one_line": "The worktree sparse-checkout names infra/aws/ec2/canonical-fidelity, yet git refuses to stage the new lander files there, so safe-commit commits nothing and the FU-s-4 code stays uncommitted.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git sparse-checkout list in C:/tmp/fidupl-w2 includes infra/aws/ec2/canonical-fidelity; git config --show-origin reports core.sparsecheckout=true and core.sparsecheckoutcone=true in .git/worktrees/fidupl-w2/config.worktree",
        "git add --dry-run -- infra/aws/ec2/canonical-fidelity/land.py printed add rc=0 (a dry run; nothing staged)",
        "bash .tools/safe-commit.sh with -F .scratch/msg_code.txt and the two files: git add printed 'matched paths that exist outside of your sparse-checkout definition, so will not be updated in the index'; commit --only printed 'did not match any file(s) known to git'; safe-commit rc=1; HEAD stayed 58aa7802b5"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker reference and the TO: a worker's new files are committed by safe-commit under the paths the order names, in a worktree whose sparse-checkout carries those paths.",
    "world_is": "git treats the new files under canonical-fidelity as outside the sparse definition although the definition names the directory, so the lander cannot be committed in this worktree. Cause not isolated on git 2.55.0.windows.5.",
    "notes": "The worker stopped at this row. No sparse config was edited and nothing was pre-added: both are outside the grant and the no-pre-add rule. The code and tests exist uncommitted in the worktree and pass FU4-AC1 and FU4-AC2 on disk."
  },
  {
    "id": "NFRA_FIDUPL-D1-W2-S2",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~2",
    "surfaced_at": "2026-10-19T20:37:00Z",
    "one_line": "The run record's closed failure_class set has no class for a file-level failure, so a failed run can carry failure_class null beside a non-null failed_step and exit 1.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~P1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/land.py in worktree wk-NFRA_FIDUPL-2 (uncommitted at filing): _examine, _land_one, _read_listing and land() set failed_step and a per-file reason with failure_class None for these cases",
        "worker reference section 6 closed set: null, sign-in refused, code never arrived, export not generated yet, download refused, content date unreadable, content date is not a trading day",
        "test_missing_file_exits_nonzero (11 passed on the worktree) asserts failed_step read for an absent file; the other cases are by construction in land.py, not separately measured"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Reference section 6: failure_class is null or one of the closed strings, and the run exits 0 only when failure_class is null and every file is landed or skipped_existing.",
    "world_is": "The TO names no class for a missing file, a destination holding different bytes, a calendar coverage gap, a head or put refusal, or an absent listing.json. These record as failed_step with failure_class null and a per-file reason, and the run exits 1. A reader that gates on failure_class alone would read a failed day as clean.",
    "notes": "Lander behavior as built: a per-file failure lands nothing for that file and the other files still land. The closed set is the decision to confirm (add classes, or keep null with failed_step as the signal)."
  },
  {
    "id": "NFRA_FIDUPL-D1-W2-S3",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~2",
    "surfaced_at": "2026-10-19T20:37:00Z",
    "one_line": "The TO says a re-served day lands once but does not say what a re-serve with different bytes does; the lander refuses to overwrite and records that file failed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/land.py _land_one (worktree wk-NFRA_FIDUPL-2, uncommitted at filing): an existing object whose sha256 metadata differs gives action failed with reason 'destination already holds different bytes; not overwritten'",
        "TO FU-s-4 item 2: skipped_existing when the same sha256 is already at the destination; no rule is stated for a different sha256"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO FU-s-4 item 2 and reference section 5a: each file lands raw once at its builder address, and the same sha256 at the destination is skipped_existing.",
    "world_is": "A corrected re-serve of the same content date and file name cannot land over the first copy, so the first bytes stay authoritative until a person decides. The lander never overwrites raw history.",
    "notes": "For the CTO or COO to confirm: keep refuse-overwrite, or land a versioned key beside the first copy."
  },
  {
    "id": "NFRA_FIDUPL-D1-W2-S4",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~2",
    "surfaced_at": "2026-10-19T20:37:00Z",
    "one_line": "Reference section 9 gives land.py a config-file fallback for locating lib/opal_naming.py; the lander takes no config, so it finds lib only by walking up from its own file.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/land.py _find_lib (worktree wk-NFRA_FIDUPL-2, uncommitted at filing) walks up from its own file for lib/opal_naming.py and raises ImportError when none is found",
        "worker reference section 9, land.py bullet: find lib by walking up, else from the repo_root key of the config file"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker reference section 9, land.py bullet: find lib/opal_naming.py walking up, else from the repo_root key of the config file.",
    "world_is": "On the box the lander resolves lib only when a lib directory sits above its own code directory. FU-s-5 or FU-s-7 must ship the mirror at that place or pass the path, because the lander does not read config.json.",
    "notes": "No box behavior runs in this order. The fallback is left for FU-s-5 or FU-s-7 to decide."
  },
  {
    "id": "NFRA_FIDUPL-D1-W2-S5",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~2",
    "surfaced_at": "2026-10-19T20:37:00Z",
    "one_line": "The run record carries keys reference section 6 does not list (content_date, failed_step, failure_class and reason per file; reason at top level), and a dry-run file action named planned.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/land.py _public() and land() (worktree wk-NFRA_FIDUPL-2, uncommitted at filing): file keys name action bytes sha256 dest content_date failed_step failure_class reason; top-level keys include reason",
        "land.py exit_code(): requires failed_step null, failure_class null, a non-empty files list and every action in landed, skipped_existing or planned"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Reference section 6: the record shape and the three file actions landed, skipped_existing and failed; exit 0 only when failure_class is null and every file is landed or skipped_existing.",
    "world_is": "The keys are additive. The action planned appears only in a dry-run return value and is never written. The exit rule is stricter than the TO's, because it also requires failed_step null. FU-x-1's r1_checks reads source, failure_class, the landed count and business_date_in_content, all of which are present.",
    "notes": "The record is written by the lander only. FU-s-5 and FU-x-1 read it; the CTO confirms the shape with the _runs decision in NFRA_FIDUPL-D1-S1."
  },
  {
    "id": "NFRA_FIDUPL-D1-W2-S6",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~2",
    "surfaced_at": "2026-10-19T20:37:00Z",
    "one_line": "The completion step flips the TO status in NFRA_FIDUPL.TO-FU-s-4, but that file is not in this order's paths block, so the worker cannot make the flip.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "NFRA_FIDUPL.TO-FU-s-4 paths block lists infra/aws/ec2/canonical-fidelity/land.py, infra/aws/ec2/canonical-fidelity/tests/test_land.py and this investigation file only",
        "worker face PROOF step: flip the task order status to complete and commit instance, deliverables and flip together; the TO file carries status pending at 58aa7802b5"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker face PROOF step: flip the task order status to complete in the same commit as the instance and the deliverables.",
    "world_is": "The grant admits no path to the TO file, so the flip falls to the issuer or the gate. The proof instance cannot be validated against a pinned code commit until the code commit lands (see NFRA_FIDUPL-D1-W2-S1).",
    "notes": "Worker stopped before the proof. FU4-AC1 and FU4-AC2 passed on disk; no commit exists yet to pin."
  },
  {
    "id": "NFRA_FIDUPL-D1-W1-S1",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~1",
    "surfaced_at": "2026-10-19T20:30:11Z",
    "one_line": "The live Quo probe proves the line resolution, the sender filter and the incoming and from fields, but not the createdAfter parameter or the createdAt timestamp that the recency window depends on, so the window path is unexercised against live Quo.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FU-s-1 criterion FU1-AC2: the reader's seam against the real Quo, read only; the reader returns the newest code inside a recency window opened at the SMS-send step (worker reference section 2).",
    "world_is": "The probe printed QUO-PROBE-OK line=PNEJ5tafLm sender_messages=4 and sent no createdAfter parameter and read no createdAt value; the live acceptance of createdAfter and the createdAt format on this line are UNMEASURED until the FU-x-1 live sign-in.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python infra/aws/ec2/canonical-fidelity/quo_otp.py --probe (worktree wk-NFRA_FIDUPL-1, 2026-10-19 ~20:30Z) printed QUO-PROBE-OK line=PNEJ5tafLm sender_messages=4 with rc 0",
        "quo_otp.py _poll_once sends createdAfter in the %Y-%m-%dT%H:%M:%SZ form and _parse_created accepts the %Y-%m-%dT%H:%M:%S.%fZ form measured in org/tier1_exec/4.0.0_SA_CRO/scripts/google_oauth_handler.py line 118 (2026-09-10)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Worker-side observation only; no action taken. The FU-x-1 live trace is the exercise that proves the window path."
  },
  {
    "id": "NFRA_FIDUPL-D1-W1-S2",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~1",
    "surfaced_at": "2026-10-19T20:34:29Z",
    "one_line": "The worktree's sparse-checkout definition omits infra/aws/ec2/canonical-fidelity, the new directory the order names, so safe-commit refuses to stage FU-s-1's module and tests and the cell cannot be committed from this worktree.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "FU-s-1 WHAT TO BUILD: build infra/aws/ec2/canonical-fidelity/quo_otp.py and tests/test_quo_otp.py in worktree C:/tmp/fidupl-w1 on branch wk-NFRA_FIDUPL-1, and commit them there with safe-commit (worker face, the grant block).",
    "world_is": "git sparse-checkout list in the worktree names .tools, infra/aws/ec2/canonical-schwab-si2, infra/aws/ec2/inf-exporter, infra/logic/registry, lib, org/devices, org/missions/D8/NFRA/NFRA_FIDUPL, org/modules/graph, org/ref, org/standards, org/surprise_channel/schemas and two org/tier1_exec paths, and does not name infra/aws/ec2/canonical-fidelity; HEAD tracks zero files under that directory, so it is a new path the cut did not admit; safe-commit refused with 'matched paths that exist outside of your sparse-checkout definition' (rc=1, nothing committed).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C C:/tmp/fidupl-w1 sparse-checkout list (2026-10-19 ~20:34Z) printed the list above, with no infra/aws/ec2/canonical-fidelity entry; git config core.sparseCheckout = true",
        "git ls-tree -r --name-only HEAD infra/aws/ec2/canonical-fidelity in the worktree returned 0 files; git status --short shows ?? infra/aws/ec2/canonical-fidelity/",
        "bash .tools/safe-commit.sh --author ... -F .scratch/msg_code.txt -- infra/aws/ec2/canonical-fidelity/quo_otp.py infra/aws/ec2/canonical-fidelity/tests/test_quo_otp.py exited rc=1 with 'exist outside of your sparse-checkout definition'; git log -1 shows HEAD 38d4f70df7 unchanged"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No action taken: the worker did not change the sparse-checkout definition, did not force the stage and did not rebuild the tree. The two files exist untracked on disk and passed FU1-AC1 (R1-FU1-OK passed=14) and FU1-AC2 (QUO-PROBE-OK line=PNEJ5tafLm sender_messages=4) in the worktree. A COO-side cut that adds the directory to the sparse definition, or a re-cut of this worktree, is the unblock; the worker's branch then commits the two paths and the proof instance."
  },
  {
    "id": "NFRA_FIDUPL-D1-W1-S3",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~1",
    "surfaced_at": "2026-10-19T20:51:22Z",
    "one_line": "Every selector and request field name in PlaywrightDriver, PlaywrightGUI and ContextSession that no capture measured is listed here for FU-x-1 to prove live: the page selectors, the factor token source, the G-selector dialog, and the status.json and downloadExport.do bodies.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FU-s-2 WHAT TO BUILD A: PlaywrightDriver drives the real Wealthscape pages; its live selectors and request bodies are UNMEASURED and FU-x-1 proves them (worker reference section 9, signin.py).",
    "world_is": "Unmeasured assumptions in the round-1 code. Login page: input[name='username'], input[type='password'], button[type='submit'] (username, password and next steps), button[data-action='authorize'] and input[name='securityCode'] (authorize and code entry). Factor: the factor name is read from the authenticators[].uri key of the POST /user/session/login response and clicked by [data-authenticator='<name>']; the HAR shows the keys authenticators[].uri and authenticators[].title but the value token OTPSMS was not read (values are never printed). G-selector dialog: text=User Options, text=G Number Selection, select[name='gNumber'] with option values, button:has-text('Save'); the dialog's current-G read and its Set As Default checkbox were never observed. status.json body {iEtype, dateString, startPage, pageLength} and the downloadExport.do params are the reference values, not captured in the HAR. accountList.json length value '300' is assumed (the key name length is measured).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "/c/Users/Test/Downloads/wealthcentral.advisorchannel.com2.har (98 MB, 441 entries) read by a stdlib script that printed only method, URL path and JSON or form key names (.scratch/har/har_keys.py, not committed), 2026-10-19 ~20:50Z",
        "key names measured: POST /auth/login form username, productId, wealthscapeDomain; POST ecaap /user/factor/password/authentication json username, password; POST ecaap /user/session/login response authenticators[].uri and authenticators[].title; POST ecaap /user/factor/otp/sms/authentication json phone, template; PUT the same path json securityCode; POST /ssc/platform-authorization/api/v2/authorize json loginType, loginSite, appName",
        "no status.json or downloadExport.do entry appears in the HAR (zero matches for those paths in the key-name output)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No action taken. FU-x-1 owns the proof: a live run that finds a selector, token or body different from the list above files its own row and does not guess."
  },
  {
    "id": "NFRA_FIDUPL-D1-W1-S4",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~1",
    "surfaced_at": "2026-10-19T20:51:22Z",
    "one_line": "The HAR's accountList.json request carries an accountNumber form field that the cell's probe does not send, and the HAR holds no status.json or downloadExport.do entry, so the account.txt read and the probe's request shape are not HAR-proven.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FU-s-2 WHAT TO BUILD B: probe_g_switch posts accountList.json with form fields length, sourceCode=BROK, custodianCode=FID; main reads account.txt through one status.json list and one downloadExport.do (worker reference section 4).",
    "world_is": "The captured accountList.json POST carries four form fields: length, accountNumber, sourceCode, custodianCode. The probe sends three (no accountNumber), which is the cell's specified shape, so the server's acceptance of the three-field form is UNMEASURED. ContextSession duplicates the session surface that fetch.PlaywrightSession (FU-s-3) owns; it is a stand-in until FU-s-3 lands and is to be replaced by that adapter.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "key-name output of the Downloads HAR (.scratch/har/keys.txt, not committed): POST /ssc/accountsearch/wc/channel/accountList.json form:length, form:accountNumber, form:sourceCode, form:custodianCode; response accountListResponse.numberOfAccounts",
        "signin_recon.py _count_accounts sends fields {length, sourceCode, custodianCode} and reads accountListResponse.numberOfAccounts (commit ccd25ab7db)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No action taken. The FU-x-1 live run of --run-live is the proof of the three-field form and of the status.json and downloadExport.do shapes."
  },
  {
    "id": "NFRA_FIDUPL-D1-W1-S5",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~1",
    "surfaced_at": "2026-10-19T21:00:37Z",
    "one_line": "The handoff contract has no failure class for a refused status list, so fetch_day raises FetchError and writes no listing.json for that run, leaving the lander's run record without the failure it is meant to carry.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FU-s-3 WHAT TO BUILD 2: fetch_day returns the listing and does not raise for the contract's failure classes; the handoff failure is null or one of four strings (worker reference section 5).",
    "world_is": "The four strings in section 5 cover a missing day, a missing file and a refused download, and no string covers a refused status list (non-200 from status.json). fetch.py raises FetchError with the status code and writes no listing.json, so box/run.py has no handoff record for that stage. The worker chose the raise over an invented class; the contract owner decides the class or the record.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "worker reference section 5 lists exactly four failure strings: sign-in refused, code never arrived, export not generated yet, download refused",
        "fetch.py fetch_day raises FetchError when status != 200 or the body is not a dict (commit dafda501f1); tests/test_fetch.py test_status_refused_raises_fetch_error covers it"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No action taken. The COO or the CTO decides whether a refused status list gets a class (for example download refused) or stays a raised error that run.py records."
  },
  {
    "id": "NFRA_FIDUPL-D1-W1-S6",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~1",
    "surfaced_at": "2026-10-19T21:00:37Z",
    "one_line": "The status-row and download field names that fetch.py reads (fileName, fileType, profileId, requestId, fileStatusDescription, fileCreatedTimestamp) and the downloadExport.do parameter names come from reference section 4, not from any capture, so FU-x-1 must prove them against the live list.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FU-s-3 WHAT TO BUILD 1: fetch_day posts the status list and keeps COMPLETED rows of the six names, then GETs downloadExport.do with the four row values as parameters (worker reference section 4).",
    "world_is": "The HAR capture holds no status.json and no downloadExport.do entry (see NFRA_FIDUPL-D1-W1-S4), so every field name fetch.py reads from a status row and every query parameter name it sends to downloadExport.do is UNMEASURED. The names are used exactly as reference section 4 states them.",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "worker reference section 4 states the status row keys and the downloadExport.do query parameters (fileName, fileType, profileId, requestId)",
        "the Downloads HAR key-name output (.scratch/har/keys.txt, not committed) has zero status.json or downloadExport.do entries"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No action taken. The FU-x-1 live --run-live proof of the status list and the account.txt download covers these names."
  },
  {
    "id": "NFRA_FIDUPL-D1-W1-S7",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~1",
    "surfaced_at": "2026-10-19T21:00:37Z",
    "one_line": "Two copies of the session adapter now exist: fetch.PlaywrightSession (the shared one, FU-s-3) and signin_recon.ContextSession (FU-s-2's stand-in), and nothing in round 1 retires the stand-in.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FU-s-2 note and worker reference section 9: fetch.py owns the real PlaywrightSession and signin_recon.ContextSession is a stand-in to be replaced by it.",
    "world_is": "signin_recon.py (outside the FU-s-3 grant, so not edited here) still defines ContextSession with the same surface. --run-live in signin_recon uses that copy. Replacing it with fetch.PlaywrightSession is a one-import change for a later order whose grant includes signin_recon.py.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "signin_recon.py class ContextSession (commit ccd25ab7db) defines xsrf_token, post_json, post_form and get_bytes; fetch.py class PlaywrightSession (commit dafda501f1) defines xsrf_token, post_json and get_bytes, which is all fetch_day calls",
        "the FU-s-3 paths block lists signin_recon.py as read-only for this order"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No action taken. Retiring the copy is for the COO to route; it is not a blocker for FU-x-1 because both copies implement the same calls."
  }
]
```
