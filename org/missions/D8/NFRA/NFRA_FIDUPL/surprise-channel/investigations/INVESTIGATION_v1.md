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
  },
  {
    "id": "NFRA_FIDUPL-D1-W4-S1",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~4",
    "surfaced_at": "2026-10-19T20:45:00Z",
    "one_line": "The HCL name builder refuses scope alongside at plan time: its generated_locals.tf predates the alongside scope row, so all 13 name calls in the Fidelity root fail a precondition, while the Python name() admits the same scope.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "terraform -chdir=infra/aws/terraform/canonical-fidelity-ec2 plan -input=false -no-color at worktree commit 1b5c10e11a printed 13 'Error: Module output value precondition failed' blocks, each 'local.name_scope_ok is false' with the message 'scope must be the LONG form of a FIRM, GLOBAL or MASTER row' (captured in the worktree at .scratch/fu6_plan.txt, not committed)",
        "infra/aws/terraform/modules/opal_name/generated_locals.tf at 1b5c10e11a carries 0 occurrences of the word alongside in scope_long, scope_short and scope_class; its header names registry@2e6709ab25, which is not an object in this repository",
        "infra/logic/registry/scopes.json at 1b5c10e11a carries the FIRM row key alongside (class FIRM), added by commit bd84d81948 (registry 4.0.0_SA_CRO~FIDELITY), an ancestor of HEAD",
        "python -I lib/opal_naming.py generate --out .scratch/gen failed with FileNotFoundError on data/firm_registry.json, the regeneration input, which this worktree does not carry",
        "python -I -c name('fidelity','alongside','uploader','role') at HEAD returned fidelity-alongside-uploader-role: the Python builder and the HCL builder disagree on the same scope"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md rule 30 and the FU-s-6 cell: every AWS resource name comes from the HCL builder (modules/opal_name) with system fidelity and scope alongside; a builder refusal is a surprise row, never a typed name.",
    "world_is": "The HCL builder's generated table is older than the registry row for alongside, so the HCL builder refuses every name this root asks for; the root validates (FU6-AC1 PASS) and cannot plan (FU6-AC3 FAIL) until the generated table is regenerated from a registry that carries the row.",
    "notes": "No name was typed and no scope was dropped to get around the refusal. Regeneration is outside this order's grant (modules/opal_name is read-only to FU-s-6). Owner of the regeneration: the registry owner (4.0.0_SA_CRO~FIDELITY lineage) or the CTO."
  },
  {
    "id": "NFRA_FIDUPL-D1-W4-S2",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~4",
    "surfaced_at": "2026-10-19T20:45:00Z",
    "one_line": "No builder names the Wealthscape secret: the SECRET grammar {system}/{scope}/{purpose} is graded only, name() refuses a secret kind, and no secret constructor exists, so the Wealthscape secret piece is stopped and the root has no secret, no prevent_destroy, no secret grant and no secret id output.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -I -c name('fidelity','alongside','wealthscape','credentials') at HEAD raised ValueError: kind 'credentials' is neither a NAMING_SCHEMA.json kind nor a cadence",
        "org/standards/NAMING_SCHEMA.json key secret: grammar {system}/{scope}/{purpose}, scope_form SHORT; kind.closed_at_l4 records that the secret kind was DROPPED because secrets keep their own slash-path grammar",
        "grep of lib/opal_naming.py for a secret constructor or def name/address/key over a secret returned none; the SECRET references at lines 906, 2204, 3071-3311 are grading and detection code only",
        "infra/aws/terraform/canonical-fidelity-ec2/main.tf, box.tf and outputs.tf at commit 1b5c10e11a: no aws_secretsmanager_secret resource, no secret grant for the Wealthscape credentials, no secret id output"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FU-s-6 item 3: an aws_secretsmanager_secret for the Wealthscape credentials, metadata only, prevent_destroy true, name from the builder; item 2: the box role grants GetSecretValue on its exact ARN.",
    "world_is": "No builder row can produce the Wealthscape secret name, so that resource and its grant cannot be written without typing a name, which the refusal clause forbids. The box, as planned, cannot read Wealthscape credentials until a builder path exists.",
    "notes": "The Quo key grant (quo/api-key, an existing secret, looked up by data source) is built. Surfaced for the CTO: a SECRET builder or a registered secret-name rule is needed before FU-s-6 can be completed."
  },
  {
    "id": "NFRA_FIDUPL-D1-W4-S3",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~4",
    "surfaced_at": "2026-10-19T20:45:00Z",
    "one_line": "The FU6-AC2 guard refuses any literal 0.0.0.0/0, so it flags the egress-open rule the order requires; the guard cannot tell an egress rule from an ingress rule when both are a bare CIDR string.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu6g at 1b5c10e11a printed R1-FU6G-FAIL 0.0.0.0/0; no prevent_destroy on the secret (process rc 0; the verdict line is the result)",
        "infra/aws/terraform/canonical-fidelity-ec2/box.tf egress block of aws_security_group.box carries cidr_blocks = [0.0.0.0/0] with protocol -1 and no ingress block exists in the root",
        "the order's FU-s-6 item 1 names egress open and no ingress rules; r1_checks.py tf_guard tests the substring 0.0.0.0/0 across all .tf files"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FU6-AC2 (FU-s-6): no ingress, no wildcard secret grant, no secret version, prevent_destroy present; item 1: security group with NO ingress rules and egress open.",
    "world_is": "Egress open means 0.0.0.0/0 on the egress rule, so the guard's substring test fails on a rule the order requires; the no-ingress half of the guard is satisfied. The guard's prevent_destroy clause also fails because of S2.",
    "notes": "The egress literal was not rewritten to evade the guard. The guard's rule needs an egress-aware form, a CTO ruling, before FU6-AC2 can grade PASS."
  },
  {
    "id": "NFRA_FIDUPL-D1-W4-S4",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~4",
    "surfaced_at": "2026-10-19T20:45:00Z",
    "one_line": "The run automation's wait step and stop step call SSM and EC2 describe actions that do not take a resource ARN, and the order forbids a * Resource, so the root grants only the resource-scoped actions and the automation may fail at its wait or stop step at run time.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "infra/aws/terraform/canonical-fidelity-ec2/automation.tf at 1b5c10e11a grants ec2:StartInstances, ec2:StopInstances, ssm:SendCommand and ssm:GetCommandInvocation only, each on the one instance or the one AWS-RunShellScript document",
        "the aws:waitForAwsResourceProperty step calls ssm DescribeInstanceInformation and the aws:changeInstanceState step may call ec2 DescribeInstances; neither is granted because the order forbids a * Resource",
        "the run is plan-only in this round; no AWS call of the automation was made, so the runtime need is INFERRED from the action definitions, not measured"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FU-s-6 item 2: no * Resource; item 4: the automation starts the instance, waits for Online, runs the wrapper and stops the instance in a step that runs whether or not the run failed.",
    "world_is": "The no-star rule and the wait step cannot both hold if the AWS action needs an unscopable Describe grant; the stop step is still reached through onFailure only if the stop step itself can run, which depends on the same grant.",
    "notes": "Proof needed at FU-x-1 or the first enabled run: a live describe of the automation execution. Not checked here (plan only)."
  },
  {
    "id": "NFRA_FIDUPL-D1-W4-S5",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~4",
    "surfaced_at": "2026-10-19T20:45:00Z",
    "one_line": "The schedule role carries iam:PassRole on the automation role, beyond the one action the order names, because SSM requires the starting principal to pass the automation's assume role.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/canonical-fidelity-ec2/schedule.tf at 1b5c10e11a: aws_iam_role_policy.schedule statement PassTheAutomationRoleToSSM grants iam:PassRole on aws_iam_role.automation.arn with condition iam:PassedToService ssm.amazonaws.com",
        "the order's FU-s-6 item 5 names ssm:StartAutomationExecution on that one document as the role's scope"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FU-s-6 item 5: a role EventBridge assumes scoped to ssm:StartAutomationExecution on that one document.",
    "world_is": "The schedule role also holds a PassRole limited to the automation role and to SSM. It is the narrowest grant that lets the document's assume role be used by the start call, and it names no other role.",
    "notes": "Scoped as narrowly as the mechanism allows; a CTO ruling can narrow it further if SSM does not need it on this path."
  },
  {
    "id": "NFRA_FIDUPL-D1-W4-S6",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~4",
    "surfaced_at": "2026-10-19T20:45:00Z",
    "one_line": "The box is created in the running state: aws_instance has no argument to create it stopped, so the first apply leaves the t3.medium running until the automation or a human stops it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~P1 (stop the instance once after the first apply, before any rule is enabled)",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "infra/aws/terraform/canonical-fidelity-ec2/box.tf at 1b5c10e11a sets instance_initiated_shutdown_behavior = stop and manages no state argument, as the order's item 1 requires",
        "the aws_instance resource in the hashicorp/aws 5.x provider has no create-stopped argument (INFERRED from the provider schema; not read from a plan, which was refused at the name precondition)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FU-s-6 item 1: the instance is created stopped-capable and is never left running by this root.",
    "world_is": "The instance will run after the first apply until something stops it, which is a cost exposure and not a data exposure, since no rule is enabled and the box has no inbound path.",
    "notes": "Armed until the first apply is stopped. The root cannot disarm it itself; the disarm owner runs the stop after apply."
  },
  {
    "id": "NFRA_FIDUPL-D1-W4-S7",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~4",
    "surfaced_at": "2026-10-19T20:45:00Z",
    "one_line": "The order names no VPC or subnet, so the root takes the account's default VPC by data source and places the box with a public IP for egress; the default VPC's existence in us-east-1 is not measured by this round.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "infra/aws/terraform/canonical-fidelity-ec2/main.tf at 1b5c10e11a: data aws_vpc default with default = true; box.tf sets associate_public_ip_address = true",
        "the sibling canonical-schwab-ec2 root names no VPC either; the order's item 1 asks for no public IP beyond what egress needs"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FU-s-6 item 1: no public-IP requirement beyond what egress to the internet needs.",
    "world_is": "The default VPC is assumed present and is the placement for the box; the plan was refused before the VPC read could be shown, so the assumption is not measured here.",
    "notes": "A dedicated VPC or subnet is a CTO placement decision; this round uses the default VPC."
  },
  {
    "id": "NFRA_FIDUPL-D1-W4-S8",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~4",
    "surfaced_at": "2026-10-19T21:05:00Z",
    "one_line": "The issuer amendment expects the regenerated name table to add the 08403355 master, but no scopes.json row carries 08403355, so the regenerated table adds alongside and nothing for 08403355.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "grep -c 08403355 over infra/logic/registry/scopes.json at HEAD d88c69d12c returned 0, and over the same file at the CLOUD ref returned 0",
        "python lib/opal_naming.py generate --out .scratch/gen --target infra/aws/terraform/modules/opal_name/generated_locals.tf wrote registry@6572bee9a8823233 and a diff against the committed table showed five added alongside lines and no removed line",
        "infra/aws/terraform/canonical-schwab-ec2/monolith-daily-schedule.tf names 08403355 only as a locals map key and a Tax SMA label, not as a registry scope"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Issuer amendment 2026-10-19 item 1: regenerate generated_locals.tf and check the diff adds the alongside scope and the 08403355 master and removes nothing else.",
    "world_is": "The registry has no 08403355 row, so no regeneration can add a 08403355 master; the regenerated table is correct for the registry as it stands and removes nothing.",
    "notes": "FU-s-6 uses no 08403355 name, so the Fidelity root is unaffected. Whether a 08403355 scope row should exist is a registry question for its owner, not this order."
  },
  {
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~NFRA1",
    "surfaced_at": "2026-10-19T21:30:00Z",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "NFRA_FIDUPL-D1-S2",
    "one_line": "bootstrap.sh fails on the Amazon Linux 2023 box at 'playwright install --with-deps chromium' (apt-get absent, exit 127), so no Chromium is installed and the order's bootstrap leg cannot close.",
    "class": "BLOCKING",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM command 34e5f9fa-8871-4de9-afdb-0084cba13858 on i-028e830f7226cc685: bootstrap_rc=1; log tail 'BEWARE: your OS is not officially supported by Playwright; installing dependencies for ubuntu24.04-x64 as a fallback. ... sh: line 1: apt-get: command not found ... Error: Installation process exited with code: 127'",
        "the same log shows OK lines for python 3.12 (dnf), the venv, and the boto3 and playwright pip install; ls /root/.cache/ms-playwright on the box: No such file or directory"
      ]
    },
    "spec_asserts": "FU-s-7 item 3: run bootstrap.sh on the box (FU-s-5 box/bootstrap.sh, written for amzn or ubuntu).",
    "world_is": "On amzn the dnf branch works but the playwright step uses --with-deps, which shells out to apt-get; the browser and its system libraries are not installed, so a Wealthscape session cannot open (FU-x-1).",
    "notes": "Fix belongs to FU-s-5's file (box/bootstrap.sh), outside this order's grant: on amzn install the chromium system libraries with dnf, then 'playwright install chromium' without --with-deps. The ledger leg L2 is left OPEN; nothing else on the box was changed."
  },
  {
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~NFRA1",
    "surfaced_at": "2026-10-19T21:30:00Z",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "NFRA_FIDUPL-D1-S3",
    "one_line": "The automation document runs 'python3 /opt/fidelity-uploader/box/run.py', which on the box is system Python 3.9 with no boto3 or playwright, while bootstrap.sh installs both only in /opt/fidelity-uploader/venv.",
    "class": "BLOCKING",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/canonical-fidelity-ec2/automation.tf line 6: run_command = python3 /opt/fidelity-uploader/box/run.py",
        "SSM read on i-028e830f7226cc685: 'python3 --version' Python 3.9.25; python3 -c 'import boto3' and 'import playwright' both ModuleNotFoundError; venv/bin/python imports land OK"
      ]
    },
    "spec_asserts": "FU-s-6 and FU-s-5: the run automation starts the wrapper; the wrapper's dependencies are in the venv bootstrap.sh builds.",
    "world_is": "A scheduled or manual automation run would fail at the first boto3 import. The applied root plans to No changes, so the fix is a Terraform edit (run_command to the venv python) plus a re-apply, or a run.py re-exec into the venv.",
    "notes": "Not changed here: the apply is by plan only and automation.tf is outside this order's grant. The schedule rules are DISABLED, so no run is due before this is fixed."
  },
  {
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~NFRA1",
    "surfaced_at": "2026-10-19T21:30:00Z",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "NFRA_FIDUPL-D1-S4",
    "one_line": "land.py finds lib/opal_naming.py only by walking up from its own file, and the config key repo_root (which the reference says is the fallback) is read by nothing, so the repo/ mirror at /opt/fidelity-uploader/repo/ is invisible to it.",
    "class": "OBSERVATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/land.py _find_lib walks up for lib/opal_naming.py and reads no config; grep of box/run.py shows repo_root only in ALLOWED_KEYS",
        "opal_naming.py derives REPO as the parent of its own LIB_DIR (abspath), so a lib symlink alone would miss infra/logic/registry",
        "box check: venv/bin/python -c 'import land' printed IMPORT-land-OK /opt/fidelity-uploader/lib and address() returned s3://opal-data-assets/fidelity/alongside/bronze/account/20261016/account.txt"
      ]
    },
    "spec_asserts": "Worker reference section 9: a module finds lib/opal_naming.py by walking up, else from the repo_root key of the config file (the box carries a minimal mirror; FU-s-7 ships it).",
    "world_is": "Bridged on the box with three symlinks in /opt/fidelity-uploader (lib, infra, org -> repo/...), so the walk-up finds the mirror and REPO resolves to /opt/fidelity-uploader. No code was changed.",
    "notes": "The mirror is 11 registry files, NAMING_SCHEMA.json, opal_naming.py and trading_calendar.py (found by an open() audit hook over address() and is_trading_day()). It is a copy at registry@ the current HEAD and will go stale when the registry changes."
  },
  {
    "id": "NFRA_FIDUPL-D1-S5",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~NFRA1",
    "surfaced_at": "2026-10-20T04:15:00Z",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "one_line": "The Fidelity box, created running and left running per the order, was stopped at 2026-10-20T00:51:18Z by the existing ec2-auto-shutdown-enforcer, so it does not stay up until FU-x-1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws ec2 describe-instances i-028e830f7226cc685 at 2026-10-20T04:07Z: State stopped, StateReason Client.UserInitiatedShutdown, StateTransitionReason User initiated (2026-10-20 00:51:18 GMT)",
        "aws cloudtrail lookup-events on the instance id: StopInstances at 2026-10-19T20:51:18-04:00 by username ec2-auto-shutdown-enforcer; the only other writes are RunInstances and ModifyInstanceAttribute by cloudops-dell1-agent-user at 17:17-17:18 -04:00"
      ]
    },
    "spec_asserts": "FU-s-7 item 5 and row W4-S6: the instance runs from the apply until FU-x-1's first automation run stops it; tell the issuer if the apply-to-FU-x-1 gap exceeds 24 hours.",
    "world_is": "A standing estate enforcer stops EC2 instances overnight (this one 3.6 hours after creation). The stopped state is the box's normal between-runs state; the delivered code and the venv are on its EBS root and survive a stop. Whether the enforcer exempts a tagged instance is not measured here.",
    "notes": "Not restarted: starting it is the automation document's job at the first run (the schedule rules are DISABLED). Nobody stopped it by hand."
  },
  {
    "id": "NFRA_FIDUPL-D1-W1-S8",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~1",
    "surfaced_at": "2026-10-20T13:03:05Z",
    "one_line": "The run automation fails at its first step because the automation role has no ec2:DescribeInstanceStatus, so the one run ended Failed before the wrapper ran; the stop step failed the same way, and the box was stopped by the stop call anyway.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps~NFRA1",
    "spec_asserts": "FU-x-1 WHAT TO BUILD 1: start the same automation the schedule uses by hand and wait for the execution to end; the wrapper runs once and the record is written (worker reference section 6; automation.tf runs the wrapper after start and Online).",
    "world_is": "Execution b065d07e-53e7-47b6-9c07-476c21f1d6df (document fidelity-alongside-uploader-document) ended Failed at 13:02Z. startInstance and stopInstance failed with 'not authorized to perform: ec2:DescribeInstanceStatus' for the assumed role fidelity-alongside-automation-role; waitForOnline and runWrapper stayed Pending, so no command was sent and no sign-in ran. The worktree automation.tf grants ec2:StartInstances, ec2:StopInstances and ec2:DescribeInstances only (its one ec2 describe statement is line 61). The stop call still reached the instance: it was stopped at 13:01:44 GMT (User initiated). Every later run of this document fails the same way before the wrapper runs.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws ssm get-automation-execution --automation-execution-id b065d07e-53e7-47b6-9c07-476c21f1d6df (2026-10-20 ~13:02Z): AutomationExecutionStatus Failed; startInstance Failed and stopInstance Failed with the DescribeInstanceStatus 403; waitForOnline Pending; runWrapper Pending",
        "grep of infra/aws/terraform/canonical-fidelity-ec2 in worktree C:/tmp/fidupl-w1 at commit 11e907bb20: automation.tf line 61 is the only ec2:DescribeInstances statement and no DescribeInstanceStatus appears",
        "aws ec2 describe-instances i-028e830f7226cc685 at 2026-10-20T13:02:32Z: State stopped, StateTransitionReason User initiated (2026-10-20 13:01:44 GMT)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No action taken on the automation or its role: the grant is not this order's. Not retried, per the issuer's one-run bound. The box was started again by this worker for the single recon run. The fix is an IAM statement for ec2:DescribeInstanceStatus in automation.tf (CloudOps seat) and a re-apply; until then a scheduled run would fail before the wrapper."
  },
  {
    "id": "NFRA_FIDUPL-D1-W1-S9",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~1",
    "surfaced_at": "2026-10-20T13:06:17Z",
    "one_line": "The one live recon sign-in ended with a Playwright TimeoutError before any text message was sent, so the live Wealthscape login steps do not match the unmeasured selectors; no trace was kept, so the failing step is not known.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "FU-s-2 PlaywrightDriver and FU-x-1 WHAT TO BUILD 3: signin_recon --run-live on the box mints a session through signin.open_session (login page, username, password, OTPSMS factor, text message) and prints the two counts-only blocks.",
    "world_is": "SSM command 91fa5057-3f37-4551-937e-0fab48001569 on i-028e830f7226cc685 ran /opt/fidelity-uploader/venv/bin/python signin_recon.py --run-live from 13:04:16Z to 13:05:34Z and returned RECON_RC=1 with stderr 'ERROR: live read failed: TimeoutError'. The read-only Quo probe after it printed QUO-PROBE-OK line=PNEJ5tafLm sender_messages=4, the same count as the 2026-10-19 baseline, so no Fidelity text was sent: the attempt did not reach the factor step. The run took about 70 seconds, which fits one 60000 ms selector wait; the step is not known (inference). No trace or screenshot was written.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws ssm get-command-invocation --command-id 91fa5057-3f37-4551-937e-0fab48001569 (2026-10-20 13:05Z): Status Success, StandardOutputContent RECON_RC=1, StandardErrorContent 'ERROR: live read failed: TimeoutError'",
        "python infra/aws/ec2/canonical-fidelity/quo_otp.py --probe in worktree C:/tmp/fidupl-w1 at 2026-10-20 13:05:55Z: QUO-PROBE-OK line=PNEJ5tafLm sender_messages=4 (baseline 4 measured 2026-10-19)",
        "signin.py PlaywrightDriver selectors (input[name='username'], input[type='password'], button[type='submit']) are the unmeasured assumptions listed in NFRA_FIDUPL-D1-W1-S3"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No retry, per the issuer's one-attempt bound. The next live attempt needs a trace (Playwright tracing or a page dump with no values) and a decision by the issuer. The sign-in leg is not proven; FU-x-1 criteria FX1-AC2 and FX1-AC3 have no output."
  },
  {
    "id": "NFRA_FIDUPL-D1-W1-S10",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~1",
    "surfaced_at": "2026-10-20T13:20:54Z",
    "one_line": "The FU-s-2 repair replaces the guessed selectors of row W1-S3 with the CRO-measured login selectors tried first, plus structural fallbacks; the page-3 factor option, shadow-root openness and the 20 second per-step budget are still unproven until the trace-login run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FU-s-2 REPAIR 1: find the login fields by structure with a 20 second timeout per step, and use the CRO-measured selectors first (worker reference section 10; research RESEARCH_20261020_NFRA_FIDUPL_LOGIN_DOM_FROM_HAR2.md).",
    "world_is": "signin.py PlaywrightDriver now tries #userInput and input[type='submit'][value='Next'] (page 1), #passwordInput input and #submitButton (page 2), #continueButton or #submitButton (page 3, Generate code), [formcontrolname='securityCode'] input (page 4), then the structural fallbacks. The W1-S3 selectors (input[name='username'] and the rest) are retired from the driver. Not measured: the page-3 factor radio option markup (data-driven), whether the bwc shadow roots are open, and whether a human sign-in's 18 seconds fits the 20 second per-step budget. The next live proof is signin_recon.py --trace-login, which stops after the text request.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CRO research RESEARCH_20261020_NFRA_FIDUPL_LOGIN_DOM_FROM_HAR2.md (main tree, read-only): pages 1-4 selectors and the not-measured list",
        "signin.py commit 6cbf750807: the P1_, P2_, P3_, P4_ constants and _wait_any candidate order; tests/test_login_trace.py 5 passed",
        "r1_checks.py fu2t at commit 6cbf750807 (worktree C:/tmp/fidupl-w1): R1-FU2T-OK passed=5"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No action taken. The trace-login run is FU-x-1's live proof and costs at most one text message per attempt."
  },
  {
    "id": "NFRA_FIDUPL-D1-S6",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "4.0.0_SA_CRO~DELL1",
    "surfaced_at": "2026-10-20T13:50:00Z",
    "one_line": "Black Diamond's copy of Cottonwood's Fidelity rep codes puts 636 of 655 accounts under two G numbers (PRIMARY and SECONDARY) and only 3 under an advisor G number, so a per-G pull may land most accounts twice and may not separate advisors.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "PRD v0.4.4 C-BACKFILL and C-TENANCY: backfill and daily pulls per G number, Cottonwood's seven first; FWD-9 splits each firm's files on the G Number.",
    "world_is": "In Black Diamond's 2026-10-19 Cottonwood allocations export (forwardfill_v2), the 655 Fidelity accounts carry these rep code sets: PRIMARY+SECONDARY 633, PRIMARY+SECONDARY+RUBOTTOM 2, PRIMARY+SECONDARY+BASS 1, PRIMARY only 11, none 8. SHIPLEY, the G475 and the G482 numbers carry 0. This is Black Diamond's field, not Fidelity's: what the Wealthscape export returns per G number is not measured. If it behaves the same, two per-G pulls return the same account twice, and the advisor G numbers do not carry the advisor books.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-cot/forwardfill_v2/allocations/ALLOCATIONS_DAILY_2026-10-19.xlsx, read 2026-10-20 ~13:5xZ: 1,503 rows, 855 distinct AccountID; Rep Code sets grouped per AccountID over Custodian starting Fidelity (655 accounts)",
        "G number labels from org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_133xZ_COTBOOKS_NO_BD_DEPENDENCY_CUSTODIAN_FIRST.md (masked)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No action taken. The first per-G Wealthscape read answers it: print accounts per G number and accounts present under 2+ G numbers. Context: docs/briefs/advi-cotbooks-custodian-first-rebrief-20261020.md F3."
  },
  {
    "id": "NFRA_FIDUPL-D1-W1-S11",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~1",
    "surfaced_at": "2026-10-20T13:48:28Z",
    "one_line": "The FU-x-1 attempt-2 trace-login run did not reach the text request: the username step reported OK but the page stayed on the username screen, so the password step timed out after 20 seconds with the password field never shown.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "spec_asserts": "FU-x-1 WHAT TO BUILD 0 (ATTEMPT 2): signin_recon.py --trace-login drives the username, the password, the factor choice and the request for the text; the trace must reach the text request before steps 1 and 3 run (worker reference section 3, login steps 1 to 4).",
    "world_is": "SSM command e0b78633-eb35-4e48-8efa-a20709672470 on i-028e830f7226cc685 (2026-10-20 13:47:30Z to 13:48:02Z) returned Status Success with stdout TRACE-LOGIN-FAIL LoginStepError:submit_password and TRACE_RC=1. The failing trace line is: step=submit_password path=/ title=\"Wealthscape Login\" elapsed=20.2s outcome=FAIL:TimeoutError. The step before it, step=submit_username path=/ title=\"Wealthscape Login\" elapsed=0.2s outcome=OK, did not navigate: the outline at the failure still shows input id=userInput and no password field. Which element the Next click hit, and whether the username was accepted, is NOT measured by the trace (inference: the click did not advance the page, for example because the fill or the ng-click binding did not register, or the redirect-info step did not load the page-2 app). No text message was sent, since the run stopped before the factor step.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "aws ssm get-command-invocation --command-id e0b78633-eb35-4e48-8efa-a20709672470 on i-028e830f7226cc685 (2026-10-20 13:48Z): Status Success; StandardOutputContent carries the trace lines and TRACE-LOGIN-FAIL LoginStepError:submit_password; StandardErrorContent empty",
        "the trace outline at the failure lists el tag=input type=text kind=other id=userInput and el tag=input type=submit, and no password element; the page path stayed / with title Wealthscape Login",
        "CRO research RESEARCH_20261020_NFRA_FIDUPL_LOGIN_DOM_FROM_HAR2.md page 1: #userInput fill then input[type=submit][value=Next] ng-click (the measured selectors the driver tried first)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No retry, per the order: step 0 failed, so steps 1 and 3 were not run and no text was requested. The fix needs a trace that records the page state after the Next click (URL and the outline without the fill), which is a worker repair in a later order, or the issuer's decision. The box stays RUNNING, AutoShutdown=disabled."
  },
  {
    "id": "NFRA_FIDUPL-D1-W2-S7",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~2",
    "surfaced_at": "2026-10-20T15:20:00Z",
    "one_line": "The offset field that pages accountList.json past the first 2,000 rows is named start, which the order marks as an assumption: no measured request carries an offset field, so the name is unverified.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/attribute.py@19ed775f82 page_account_list: pages after the first send fields['start'] = str(page * length); the first page is sent without it, as measured",
        "RESEARCH_20261019_FIDELITY_WEALTHSCAPE_HAR_ENDPOINT_MAP.md line 58 (accountList.json form: length, accountNumber, sourceCode, custodianCode) and RESEARCH_20261019_NFRA_FIDUPL_ACCOUNT_TXT_AND_FIRM_SPLIT.md section 2b step 3: no offset field is measured",
        "NFRA_FIDUPL.TO-FR-s-1 WHAT TO BUILD item 2: the field name past 2,000 rows is an ASSUMPTION, unmeasured"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker reference section 11 and the order: accountList.json is paged with length=2000 until a page shorter than 2000 comes back, using an offset field named start.",
    "world_is": "No captured request in the cited research carries an offset field, so the name start is unmeasured. The fake tests fix the name, and the live cell must confirm it against a request past 2,000 rows before the lister is wired.",
    "notes": "Built against fakes only; nothing runs live. The paging loop stops at the first short page and caps at 50 pages, so a server that ignores the offset cannot loop forever."
  },
  {
    "id": "NFRA_FIDUPL-D1-W2-S8",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~2",
    "surfaced_at": "2026-10-20T15:20:00Z",
    "one_line": "The row container of an accountList.json response, the key that holds each page's account records, is not named in any cited measurement, so page_account_list takes the extractor as an injected callable.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/signin_recon.py@19ed775f82 reads only accountListResponse.numberOfAccounts from the accountList.json response; no list key is read",
        "grep of the cited research (ENDPOINT_MAP, G_NUMBERS, ACCOUNT_TXT_AND_FIRM_SPLIT) for accountListResponse and the account-list key: only numberOfAccounts is named",
        "attribute.py@19ed775f82 page_account_list: rows_of is required and raises AccountListError when not supplied; no key is guessed"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker reference section 11: the real account_lister pages accountList.json until a page shorter than 2000 comes back, so each page's record count is read from the response.",
    "world_is": "The response key that holds the account records is unmeasured in the cited research, so a page's count cannot be read by a named key. The fake tests supply their own extractor. The live cell must name the key from a captured response before the real lister is wired.",
    "notes": "No key is guessed in code. Built against fakes only."
  },
  {
    "id": "NFRA_FIDUPL-D1-W2-S9",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~2",
    "surfaced_at": "2026-10-20T15:20:00Z",
    "one_line": "Reference section 11 keys summary.per_label_counts by firm label, while the order bounds say no firm label appears in any output, so the two cannot both hold for a printed summary.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "NFRA_FIDUPL_R1_WORKER_REFERENCE.md section 11 (sweep_attribution return shape): summary.per_label_counts is {label: n}",
        "NFRA_FIDUPL.TO-FR-s-1 BOUNDS: No G number, account number or firm label in any output. Counts and booleans only",
        "attribute.py@19ed775f82 implements the section 11 shape verbatim; sweep_attribution prints nothing"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker reference section 11: summary holds counts only, and per_label_counts maps label to count. The order BOUNDS: no firm label in any output.",
    "world_is": "The two statements conflict for the summary dict: its per_label_counts keys are firm labels. The function prints nothing, so the conflict bites only where a caller prints or logs summary; the caller that writes the full dict to the work directory is unaffected.",
    "notes": "Implemented the section 11 shape as written and did not rename the keys. The issuer decides whether the summary keys change before the day orchestration (box/daily.py) prints anything."
  },
  {
    "id": "NFRA_FIDUPL-D1-W2-S10",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~2",
    "surfaced_at": "2026-10-20T15:20:00Z",
    "one_line": "The proof step flips the status of NFRA_FIDUPL.TO-FR-s-1 to complete, but that task-order file is not in this order's paths block, so the worker cannot make the flip.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "NFRA_FIDUPL.TO-FR-s-1 paths block lists infra/aws/ec2/canonical-fidelity/gswitch.py, attribute.py, tests/test_gswitch.py, tests/test_attribute.py and this investigation file only",
        "worker face PROOF step: flip the task order status to complete and commit instance, deliverables and flip together; the TO file carries status pending at c5ff6eaad5",
        "same gap as NFRA_FIDUPL-D1-W2-S6 (round 1, FU-s-4): the grant admits no path to the task-order file"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker face PROOF step: flip the task order status to complete in the same commit as the instance and the deliverables.",
    "world_is": "The grant admits no path to the TO file, so the flip falls to the issuer or the gate. The proof instance can be validated and pinned to the code commit 19ed775f82, but the status stays pending until the issuer flips it.",
    "notes": "Worker leaves the TO file untouched. The criteria FR1-AC1 and FR1-AC2 both PASS-by-output at 19ed775f82."
  },
  {
    "id": "NFRA_FIDUPL-D1-W3-S5",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~3",
    "surfaced_at": "2026-10-20T15:20:00Z",
    "one_line": "The order asks the record to list conflicts, unplaced accounts and unmapped labels, while its bounds and reference section 11 forbid any account number or label in an output; the split record carries ordinal ids and counts only, and the id-to-value map stays in memory.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/split.py split_day (worktree wk-NFRA_FIDUPL-3, uncommitted at filing): ids conflict-NNN, unplaced-NNN, label-NNN; resolution filled only when the caller passes a dict",
        "TO FR-s-2 item 4 and test name test_record_has_counts_and_lists versus BOUNDS 'no G number, account number or firm label in any output'",
        "tests/test_split.py test_record_has_counts_and_lists asserts no account value, label value or G value appears in the record body (passed on disk)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO FR-s-2 bounds and reference section 11: no G number, account number or firm label in any output; counts and booleans only.",
    "world_is": "A reader of the record can see how many accounts were conflicts, unplaced or under an unmapped label, but cannot name them from the record alone; the mapping from id to value exists only in the caller's memory.",
    "notes": "For the COO to confirm: whether the lists should carry values in an encrypted bronze record (as the raw file does) or stay ids-only as built."
  },
  {
    "id": "NFRA_FIDUPL-D1-W3-S6",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~3",
    "surfaced_at": "2026-10-20T15:20:00Z",
    "one_line": "The order does not say what an account is when one of its G numbers carries an unmapped label and another G number of a single firm; split.py lists it unplaced and lands nothing for it, and it judges conflicts and unplaced over every attributed account, not only the accounts in the day's file.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/split.py _placement and _classify (worktree wk-NFRA_FIDUPL-3, uncommitted at filing): an account in acct_unmapped is unplaced before the single-firm test",
        "TO FR-s-2 item 2 states the single-firm and two-firm rules and the unmapped-label rule, not the mixed case",
        "tests/test_split.py test_unmapped_label_listed_not_landed passes with an unmapped-label account in the export and the unmapped label listed (passed on disk)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO FR-s-2 item 2: an account under G numbers of one firm lands once for that firm; an account under no G, or under a label that matches no firm, goes to unplaced.",
    "world_is": "A mixed account (one mapped G, one unmapped G) lands nowhere, which fails closed; the record counts it as unplaced. An account under a mapped G that is not in the day's file is still counted under unplaced or conflicts.",
    "notes": "For the COO to confirm the mixed-case rule; the fail-closed reading is the one built."
  },
  {
    "id": "NFRA_FIDUPL-D1-W3-S7",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~3",
    "surfaced_at": "2026-10-20T15:20:00Z",
    "one_line": "The order does not say what a firm's object does when a same-day split already sits at the destination with different bytes; split.py refuses to overwrite and records that firm-file failed, the same rule the lander applies to raw files.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/split.py split_day (worktree wk-NFRA_FIDUPL-3, uncommitted at filing): an existing object whose sha256 metadata differs gives action failed with reason 'destination already holds different bytes; not overwritten'",
        "NFRA_FIDUPL-D1-W2-S3 (the lander's same rule, filed 2026-10-20 by 0.9.0_WK_NFRA_FIDUPL~2)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO FR-s-2 item 3: each firm's lines are written once per firm and file; a re-run lands the same bytes or nothing.",
    "world_is": "A re-split of the same day under a changed attribution cannot replace the first firm object; the first bytes stay until a person decides, and the exit code is non-zero.",
    "notes": "Same decision as NFRA_FIDUPL-D1-W2-S3, to be ruled once for both the lander and the split."
  },
  {
    "id": "NFRA_FIDUPL-D1-W3-S8",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~3",
    "surfaced_at": "2026-10-20T15:20:00Z",
    "one_line": "The order's exit rule names three conditions; split.py also exits non-zero on a missing or unreadable file, a failed or refused write, an unkeyed line, or a listing failure, and it performs no trading-calendar check.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/split.py exit_code (worktree wk-NFRA_FIDUPL-3, uncommitted at filing): any record failure, any unkeyed row, or any firm-file action outside landed, skipped_existing or planned, or a row count mismatch, returns 1",
        "TO FR-s-2 item 4: exit 0 only when conflicts and firms_without_scope are empty and every written object's row count matches; the TO does not name the other conditions"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO FR-s-2 item 4: exit code 0 only when conflicts and firms_without_scope are empty and every written object's row count matches.",
    "world_is": "The exit code is stricter than the order's rule; every extra condition makes a run exit non-zero, never zero. The calendar is checked by the lander on the staged day, not again here.",
    "notes": "Stricter-only; the extra conditions can be dropped by a ruling if the box run must not stop on them."
  },
  {
    "id": "NFRA_FIDUPL-D1-W4-S9",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~4",
    "surfaced_at": "2026-10-20T15:14:39Z",
    "spec_asserts": "TO-FR-s-3 WHAT TO BUILD items 1 and 2: plan_windows(today, floor_date, chunk_days) yields non-overlapping windows covering today back to floor_date; backfill_g stops a kind at an EMPTY window whose end is older than floor_date (account open date) and at the 20-year cap.",
    "world_is": "Both cannot hold on one walk: a walk bounded at floor_date never yields a window whose end is older than floor_date, so the account open date stop is unreachable. Built as: plan_windows keeps the named wording (bounded at its floor argument); backfill_g calls it with the cap date as that floor and tests floor_date only at each EMPTY window, so the account open date stop and the cap stop are both reachable.",
    "one_line": "The order's planner bound and its account-open-date stop cannot both be met by one walk; backfill_g walks to the cap and tests floor_date at each EMPTY window.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/NFRA/NFRA_FIDUPL/task-orders/NFRA_FIDUPL.TO-FR-s-3.backfill-planner.md at c5ff6eaad5: WHAT TO BUILD item 1 bounds plan_windows at floor_date and item 2 stops a kind at an EMPTY window older than floor_date",
        "org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md at c5ff6eaad5 section 11: backfill_g walks back from today and stops at the 20-year cap; no planner bound is stated there",
        "infra/aws/ec2/canonical-fidelity/backfill.py in worktree C:/tmp/fidupl-w4 branch wk-NFRA_FIDUPL-4: _walk_kind calls plan_windows(today, cap_date, chunk_days) and tests date_to < floor_date only on EMPTY",
        "timeout 120 python -m pytest -p no:cacheprovider infra/aws/ec2/canonical-fidelity/tests/test_backfill.py in worktree C:/tmp/fidupl-w4: 9 passed, including test_stops_at_account_open_date and test_stops_at_cap_years"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Interpretation only: no retry, no blocked criterion. FR3-AC1 passes on the built reading. The issuer may rule on the planner bound."
  },
  {
    "id": "NFRA_FIDUPL-D1-W5-S1",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~5",
    "surfaced_at": "2026-10-20T15:13:23Z",
    "one_line": "The round-2 modules attribute.py, gswitch.py and split.py are not on the branch at c5ff6eaad5, so box/daily.py and the daily hookup in box/run.py reference their documented names only, and the daily wiring can run only with fakes until they land.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ls infra/aws/ec2/canonical-fidelity/ in worktree wk-NFRA_FIDUPL-5 at HEAD c5ff6eaad5 lists fetch.py land.py quo_otp.py signin.py signin_recon.py and box/ tests/; attribute.py gswitch.py split.py are absent",
        "box/run.py _real_daily_deps imports split inside its wrapper, and the attribute wrapper refuses by design; an absent split module fails only the split stage (ImportError is caught as a stage failure) and the land still runs"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Reference section 11: attribute.py sweep_attribution, gswitch.py GSwitcher and split.py split_day are the documented round-2 interfaces the daily stages call.",
    "world_is": "No module of the three exists on this branch, so the real attribute and split stages cannot run from this worktree; the stage-level failure is loud in the run record and the exit code.",
    "notes": "Nothing is stubbed. The tests inject fakes through the deps dict, so the five daily tests prove the orchestration, not the modules."
  },
  {
    "id": "NFRA_FIDUPL-D1-W5-S2",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~5",
    "surfaced_at": "2026-10-20T15:13:23Z",
    "one_line": "No documented path gives the daily attribute stage its inputs: the signin Session carries only context and close(), gswitch needs a request object with get_text and post_form, and sweep_attribution needs an account_lister whose constructor reference section 11 does not name; the attribute wrapper therefore refuses loudly and every daily run reports partial.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~P1 (names the request adapter and the account lister constructor, or rules where they live; until then each daily run lands and reports attribution and split as not finished)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/signin.py class Session (worktree HEAD c5ff6eaad5): assigns self.context and defines close(); no request, get_text or post_form attribute",
        "decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md section 11 (gswitch): GSwitcher(request) with request as get_text(url) and post_form(url, fields); attribute: account_lister() is injected and its real constructor is not named",
        "box/run.py _real_daily_deps attribute_day raises RuntimeError by design and names this row; the run record and exit code show the failure"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Reference section 11: sweep_attribution reads the form, switches every option, calls the injected account lister, and restores the starting G; the daily stage runs it with the session's request object.",
    "world_is": "The session does not expose the request object the switch needs, and the account lister has no named constructor, so the production attribute stage cannot be built from the documented surfaces. The land stage is unaffected and runs first.",
    "notes": "A repaired adapter or a named lister constructor is a new cell; this worker did not invent either. ARMED because each scheduled daily run would end partial with no attribution until the owner rules."
  },
  {
    "id": "NFRA_FIDUPL-D1-W6-S1",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~6",
    "surfaced_at": "2026-10-20T15:14:00Z",
    "one_line": "The name builder has no kind for an SSM parameter: name() refuses every candidate kind (parameter, param, secret, config), so the per-G SSM parameter and the box role's read grant on it cannot be named, and that piece of TO FR-s-5 is stopped.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -I -c \"import sys; sys.path.insert(0,'lib'); import opal_naming as o; o.name('fidelity','alongside','perg','parameter')\" at HEAD fa72c37046 raised ValueError: kind 'parameter' is neither a NAMING_SCHEMA.json kind nor a cadence; param, secret and config were refused the same way",
        "org/standards/NAMING_SCHEMA.json kind.values has no SSM parameter member; kind.by_type maps no SSM parameter type; tf_unmapped_own_name lists aws_ssm_parameter with the attribute name (its own name, not graded by kind)",
        "name('fidelity','alongside','perg','policy') and ('perg','document') are accepted, but each would mis-state the resource type as an IAM policy or an SSM document; not used",
        "infra/aws/terraform/modules/opal_name/variables.tf validates kind by lowercase kebab-case only, so the HCL builder would emit a name for any kind word; that name would not be the registry's, so it was not used"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO FR-s-5 item 2: one aws_ssm_parameter of type SecureString for the per-G list, its name from the HCL builder (system fidelity, scope alongside); a builder refusal is a surprise row and that piece stops.",
    "world_is": "No kind in the registry names an SSM parameter, so the builder cannot produce its name. The parameter, its box-role read grant (TO item 3) and the output perg_parameter_name are not built. The schedule switch (variables.tf, schedule.tf) is built and plans as No changes at its default.",
    "notes": "The stopped piece needs a registry kind for SSM parameters (or a ruling that parameter names are graded by a grammar). FR5-AC3 cannot reach its expected plan (1 to add) until that is ruled. No G number and no typed name was used."
  },
  {
    "id": "NFRA_FIDUPL-D1-W5-S3",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~5",
    "surfaced_at": "2026-10-20T16:05:00Z",
    "one_line": "The FR-s-6 order names box/daily.py _real_daily_deps for the one wiring edit, but _real_daily_deps lives in box/run.py, which is not in the order's paths, so the refusal that W5-S2 names cannot be removed under this grant; the adapters are built and tested, and a scratch wiring of run.py passes all six adapter tests.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "box/run.py line 270 (worktree wk-NFRA_FIDUPL-5 at HEAD c8aa40c577): def _real_daily_deps(config); line 279 raises RuntimeError with the attribute refusal; box/daily.py defines no _real_daily_deps",
        "NFRA_FIDUPL.TO-FR-s-6.adapters.md paths block: adapters.py, tests/test_adapters.py, box/daily.py and the investigation file; box/run.py is not granted",
        "scratch copy of box/run.py with the refusal replaced by ContextRequest, make_account_lister and GSwitcher, run in the same worktree: tests/test_adapters.py 6 passed rc=0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FR-s-6 wiring: the one edit of box/daily.py _real_daily_deps makes attribute build ContextRequest(handle.context), a GSwitcher on it and make_account_lister, then call attribute.sweep_attribution, and delete the refusal path.",
    "world_is": "The wiring target is in box/run.py, outside the grant, so the daily attribute stage still refuses and every daily run still reports partial. FR6-AC1 cannot pass as written until the grant or the location is ruled.",
    "notes": "Decision for the COO: add box/run.py to the FR-s-6 paths (a 6-line change in one function), or move the attribute wrapper into box/daily.py and have run.py call it. This worker did not edit run.py."
  },
  {
    "id": "NFRA_FIDUPL-D1-W5-S4",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~5",
    "surfaced_at": "2026-10-20T17:10:00Z",
    "one_line": "The request-side field names for paging accountList.json past 2,000 rows are assumed to be start and sessionCacheId, the same words the response carries on pageResponse; the CRO measured the response only, so the request names are unmeasured and the first live multi-page pull settles them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261020_NFRA_FIDUPL_ACCOUNTLIST_SHAPE.md section Paging past 2,000 and Not measured: the request form in the capture carried only length, accountNumber, sourceCode and custodianCode",
        "infra/aws/ec2/canonical-fidelity/adapters.py make_account_lister sends start=<rows collected> from the second page and sessionCacheId when the response carried a non-null one"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "REPAIR of FR-s-6: page by pageResponse.available, sending start and sessionCacheId on later pages; the request-side names are an assumption to file as one row.",
    "world_is": "If the live API names the request fields differently, a later page returns the first page again or no rows. The lister counts and returns DISTINCT account numbers, so repeats cannot fill the total: it either reaches available with distinct numbers or fails loud with the two counts (short of available). It never returns a silent short or duplicated list.",
    "notes": "Settled by the first live multi-page pull, which is the issuer's check on the box. No account value is printed by the pull's counts."
  },
  {
    "id": "NFRA_FIDUPL-D1-S7",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~NFRA1",
    "surfaced_at": "2026-10-20T16:50:00Z",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "one_line": "The fu10x check launches Google Chrome (channel chrome), which is not installed on the box, so FU10-AC2 reads FAIL after the Xvfb install even though a headed bundled Chromium launches under Xvfb.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "r1_checks.py box_headed (line ~496): p.chromium.launch(channel='chrome', headless=False, ...) and the OK text 'a headed Google Chrome launches under it'; the order's FU10-AC2 expect text says 'a headed Chromium launches under it'",
        "SSM on i-028e830f7226cc685 after dnf install of xorg-x11-server-Xvfb (rpm 21.1.13-5.amzn2023.0.11): channel=chrome -> 'Chromium distribution chrome is not found at /opt/google/chrome/chrome'; the bundled chromium headless=False under Xvfb :97 -> LAUNCH-OK; command -v google-chrome google-chrome-stable chrome -> none",
        "r1_checks.py fu10x run at 16:4xZ: R1-FU10X-FAIL ssm status=Failed"
      ]
    },
    "spec_asserts": "Order FU-s-10 SCOPE WIDENED AGAIN: install xorg-x11-server-Xvfb; FU10-AC2 expects R1-FU10X-OK Xvfb present and a headed Chromium launches under it.",
    "world_is": "Xvfb is installed and a headed bundled Chromium launches under it. The check as written needs Google Chrome, an install this order does not ask for and its grant does not cover (playwright install chrome or a Google RPM changes the box beyond the Xvfb leg).",
    "notes": "Not installed: Google Chrome. The issuer decides whether to widen the order (install chrome, FU-s-11 fallback) or change the check to the bundled Chromium. The Xvfb ledger is closed; the code delivery still waits for the named head."
  },
  {
    "id": "NFRA_FIDUPL-D1-W7-S1",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~7",
    "surfaced_at": "2026-10-20T18:42:36Z",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "one_line": "agent_drive.py must not import quo_otp (TO FU-s-12 section 2), but it must build signin.PlaywrightDriver, and signin.py imports quo_otp at module top, so the controller loads the Quo module transitively.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/signin.py:32 at 8c6b6e77175: 'from quo_otp import QuoApiError' (module top level, not inside a function)",
        "infra/aws/ec2/canonical-fidelity/quo_otp.py at 8c6b6e77175: default_api_key() calls boto3 secretsmanager only when invoked; QuoOtpReader is built only by agent_fill.py on the box, never by agent_drive.py",
        "infra/aws/ec2/canonical-fidelity/agent_drive.py at the worker commit: 'import signin' is the only sibling import; the static check test_drive_module_reads_no_secret names quo_otp, QuoOtpReader, default_api_key and secretsmanager and passes, and it reads agent_drive.py text only"
      ]
    },
    "spec_asserts": "agent_drive.py imports no secrets client and no quo_otp (TO FU-s-12 section 2, the static test test_drive_module_reads_no_secret); it builds signin.PlaywrightDriver(page) and reads signin.OTP_SMS.",
    "world_is": "signin.py imports quo_otp at its top level, so importing signin loads quo_otp on dell1. Loading the module reads no key: the key provider runs only when a reader is constructed and asked for a code, and agent_drive.py never constructs one. The text of agent_drive.py names no quo_otp symbol, so the static check holds, but the transitive import is not caught by it. Whether the loaded-module reading counts as the import the TO forbids is the issuer's ruling.",
    "notes": "No value is read on dell1 by this path. Decision needed from the issuer: accept the transitive load (as built), or move the Quo import out of signin.py (signin.py is outside this order's grant and is not to be changed by this worker)."
  },
  {
    "id": "NFRA_FIDUPL-D1-S8",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~NFRA1",
    "surfaced_at": "2026-10-20T21:40:00Z",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "class": "BLOCKING",
    "one_line": "The FU-s-13 premise 'plan reads 0 to add, 1 to change' fails on the whole root: unapplied FR-s-5 work (a new secret and a box role policy change) is pending beside it, so the full plan reads 1 to add, 2 to change.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "terraform plan of canonical-fidelity-ec2 at HEAD before my edit: Plan: 1 to add, 1 to change, 0 to destroy = aws_secretsmanager_secret.perg created (name fidelity/alongside/perg-list) + aws_iam_role_policy.box updated in place + new output perg_secret_id; after my edit the full plan reads 1 to add, 2 to change",
        "git log of the root: fa72c37046b and 1d5e861e75b by 0.9.0_WK_NFRA_FIDUPL~6 (FR-s-5); order NFRA_FIDUPL.TO-FR-s-5 is PLAN ONLY, status complete, and says 'The CloudOps seat applies later by its own order'; no order of this seat covers that apply",
        "terraform plan -target=aws_iam_role_policy.automation: Plan: 0 to add, 1 to change, 0 to destroy, the only diff being + ssm:ListCommands and + ssm:ListCommandInvocations"
      ]
    },
    "spec_asserts": "TO-FU-s-13 item 3: the plan must read exactly Plan: 0 to add, 1 to change, 0 to destroy and the one change must be the role policy; the refusal clause says more than one change is a surprise row and I stop.",
    "world_is": "A plain safe-apply of the root would also create the perg secret and rewrite the box role policy, which this order does not authorize and whose owner (FR-s-5, plan only) has not been given an apply order. Nothing was applied. The edit to automation.tf is committed.",
    "notes": "Held for the issuer: either (a) apply with -target=aws_iam_role_policy.automation (reads exactly the order's plan line and leaves FR-s-5's changes pending), or (b) widen the order to apply FR-s-5 as well after its box role policy diff is read. I recommend (a). No ledger was opened, because an open entry would flip fu7l."
  },
  {
    "id": "NFRA_FIDUPL-D1-W7-S2",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~7",
    "surfaced_at": "2026-10-20T22:33:19Z",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~P1",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "one_line": "REPAIR 1 item 2 orders terminate, wait, then taskkill /PID <pid> /T /F; measured on this box, taskkill /T after the parent has exited finds no child and the child survives, so the order's sequence leaves the forward's child alive.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "local probe, worktree .scratch/tree_probe.py (no AWS, not committed): SPEC-ORDER line 'taskkill-after rc=128 ERROR: The process \"56516\" not found.' and 'child_pid=44292 child_alive=True'",
        "local probe, same script: ALT-ORDER line 'taskkill-before rc=0 SUCCESS: The process with PID 36432 (child process of PID 43356) has been terminated.' and 'child_alive=False'",
        "local probe, worktree .scratch/close_probe.py: Drive._close() of infra/aws/ec2/canonical-fidelity/agent_drive.py on a real parent and child: 'taskkill_calls=2', 'child_alive=False' (the code commit that carries this row holds the change)"
      ]
    },
    "spec_asserts": "REPAIR 1 item 2 (agent_drive.py _close): after terminate() and the wait, kill the forward's whole process tree with taskkill /PID <pid> /T /F on Windows, so the next run does not attach through a dead tunnel left by session-manager-plugin.exe.",
    "world_is": "On Windows the order's sequence does not reach the child: after the parent exits, taskkill /T has no parent-child chain to follow and returns rc 128. The controller now kills the tree while the parent is alive (before terminate) and keeps the order's kill after the wait. Measured on a local parent and child pair only; the live aws.exe and session-manager-plugin.exe pair is not measured here.",
    "notes": "Hazard stands until the first live run confirms that the forward port is free after close. Disarm is the issuer's: confirm on the next live drive that no session-manager-plugin.exe holds 127.0.0.1:9222 after the record is printed. The deviation from the written order's sequence is in the commit that carries this row."
  },
  {
    "id": "NFRA_FIDUPL-D1-W2-S11",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~2",
    "surfaced_at": "2026-10-21T01:02:00Z",
    "one_line": "The REPAIR 1 criterion FU4-AC2 (fu4d) cannot reach dests=6: the checker's synthetic handoff puts the date in field 0 of all six files, and the repaired per-file as-of columns read balance column 3, account column 16 and transact column 17, which that fixture does not carry.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python C:/Dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu4d, cwd /c/tmp/fidupl-w2 at 2026-10-21T01:01Z, printed: R1-FU4D-FAIL rc=1 dests=3 last=ERROR: failed_step=date failure_class=content date unreadable",
        "fidupl_round_checks.py synth_handoff line 159 (main checkout read 2026-10-21): w.writerow([date, 'SYNTH', n, '1']) for every one of the six names, so the date is in field 0 only",
        "land.py at commit ca6db55395: DATE_COLUMN balance 3, account 16, transact 17, the rest 0; the fixture's balance row has 4 fields with '1' in column 3, and its account and transact rows are shorter than column 16 and column 17",
        "python C:/Dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu4 at ca6db55395 printed R1-FU4-OK passed=15 (the fourteen named tests plus one)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "REPAIR 1 (issuer, 2026-10-21) and FU4-AC2: the fu4d dry run still reads dests=6 (expect R1-FU4D-OK dests=6), and the checker's synthetic handoff is the fixture for that run.",
    "world_is": "The checker's synth_handoff writes the as-of date in field 0 of all six synthetic files. Under the per-file columns of REPAIR 1, balance (column 3), account (column 16) and transact (column 17) are unreadable in that fixture, so the dry run prints three DRYRUN lines, reads dests=3 and exits 1. The lander follows the repaired rule; no lander rule reaches dests=6 on this fixture as written.",
    "notes": "Not edited: the checker is the COO's (org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/) and outside this order's grant. The lander and its tests are committed at ca6db55395 and FU4-AC1 passes. FU4-AC2 is recorded FAIL and the order stays open. Decision for the COO: point synth_handoff at the per-file columns, then re-run fu4d; the lander is not to be reverted to field 0 to pass it."
  },
  {
    "id": "NFRA_FIDUPL-D1-S9",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~NFRA1",
    "surfaced_at": "2026-10-21T01:40:00Z",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "one_line": "The ft5i check simulates PutSecretValue with two resource ARNs in one call, which the IAM simulator collapses to one templated result, so it reads FAIL on a role that holds the grant.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft5i at 2026-10-21T01:38Z printed: R1-FT5I-FAIL the box role may not put the per-G list secret",
        "aws iam get-role-policy fidelity-alongside-uploader-policy: statement PergSecretPut = secretsmanager:PutSecretValue on arn:aws:secretsmanager:us-east-1:313476888478:secret:fidelity/alongside/perg-list-WIANxc only (applied by safe-apply, post-apply plan No changes rc=0)",
        "aws iam simulate-principal-policy, ONE resource per call, same role and action: perg-list-WIANxc -> allowed; wealthscape-credentials-gREoMF -> implicitDeny; positive control GetSecretValue on perg-list-WIANxc -> allowed",
        "the same call with both ARNs: one result row whose EvalResourceName is the template arn:aws:secretsmanager:${Region}:${Account}:secret:${SecretId} and EvalDecision implicitDeny, so the checker's dict has no entry for the perg ARN (box_put_grant line ~648, got.get(perg))"
      ]
    },
    "spec_asserts": "TO-FT-s-5 criterion FT-s-5-AC1: ft5i reads R1-FT5I-OK the box role may put the per-G list secret and not the credentials, via an IAM simulator run with the Wealthscape credentials as the negative control.",
    "world_is": "The grant is live and exactly one secret wide. The checker's single multi-resource simulation cannot see it (the simulator's two-or-more resource ARN mode), so AC1 reads FAIL while the single-resource simulations read allowed on the per-G secret and implicitDeny on the credentials.",
    "notes": "Not edited: the checker is the COO's and outside this order's grant. Fix for the issuer: two simulate_principal_policy calls, one ResourceArn each, in box_put_grant. FT-s-5-AC1 is recorded FAIL by its own invocation; the order stays pending until the checker is fixed and ft5i re-run, or the issuer accepts the single-call evidence."
  },
  {
    "id": "NFRA_FIDUPL-D1-W7-S3",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~7",
    "surfaced_at": "2026-10-21T01:36:45Z",
    "one_line": "The per-G stop_reason closed set (entitlement, retention, open_date, run_cap, none) has no value for the planner's lander-failure stop, so backfill_run.py maps a lander failure to none.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/backfill.py (worktree wk-NFRA_FIDUPL-7, HEAD 6bd116284f5): STOP_LANDER = 'lander failure', returned by _walk_kind when the injected lander raises",
        "NFRA_FIDUPL_R1_WORKER_REFERENCE.md section 12: the per-G record stop_reason is entitlement|retention|open_date|run_cap|none",
        "infra/aws/ec2/canonical-fidelity/backfill_run.py (uncommitted at filing) ROW_REASON maps STOP_LANDER to none; tests/test_backfill_run.py test_lander_failure_reads_none_and_stays_resumable passes"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Reference section 12: backfill_run per-G record stop_reason is one of entitlement, retention, open_date, run_cap or none.",
    "world_is": "The planner emits five stop reasons and the closed set has five values with no slot for a lander failure. A row reading none for a lander failure is indistinguishable from a 20-year-cap stop. The runner keeps the planner's reason in the stored record, where a lander failure stays resumable; only the row reads none.",
    "notes": "For the COO to rule: add a value (for example lander_failure) to the closed set, or keep none. Nothing acts on it until ruled."
  },
  {
    "id": "NFRA_FIDUPL-D1-W7-S4",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~7",
    "surfaced_at": "2026-10-21T01:36:45Z",
    "one_line": "Reference section 12 names only records.sessions_today() for the runner's records, but the daily sign-in cap cannot grow without a write path and a per-G resume needs per-kind earliest dates, so backfill_run.py takes load, save and note_session and stores a kinds map beside the row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "NFRA_FIDUPL_R1_WORKER_REFERENCE.md section 12, backfill runner bullet: the only records method named is sessions_today(); the per-G record is {rows:[{ordinal, earliest_date, stop_reason}], remaining}",
        "infra/aws/ec2/canonical-fidelity/backfill.py: backfill_g returns one entry per kind (earliest_date_served, stop_reason); a single per-G earliest across kinds would skip one kind's windows on resume",
        "infra/aws/ec2/canonical-fidelity/backfill_run.py (uncommitted at filing): run() calls records.load(), records.save(g, stored), records.note_session() before session_factory(), and the stored record is {kinds: {kind: {earliest, reason}}}; the returned row keeps the three named keys"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Reference section 12: backfill_run.run(plan_inputs, export_client, lander, session_factory, records, caps) with records.sessions_today() as the records method, and a per-G record of ordinal, earliest_date and stop_reason.",
    "world_is": "No named method records a sign-in, so sessions_today() would never grow past zero; the runner counts a sign-in attempt through note_session() before opening a session, and a refused sign-in is counted too. The stored per-G record keeps per-kind earliest dates and reasons; the output row is the named three keys.",
    "notes": "The records store is keyed by the G value (memory or the box work directory) and never echoes it. The box wiring that supplies the store is not in this cell."
  },
  {
    "id": "NFRA_FIDUPL-D1-W7-S5",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~7",
    "surfaced_at": "2026-10-21T01:36:45Z",
    "one_line": "Reference section 12 says a G with a recorded earliest date resumes from it, but backfill_run.py does not re-walk a kind at a final stop (entitlement, retention, account open date, the 20-year cap), since each re-walk would spend a run's export cap on a refused window every day.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "NFRA_FIDUPL_R1_WORKER_REFERENCE.md section 12 and the cell FT-s-4: 'a G with a recorded earliest date resumes from it, never refetches landed windows'",
        "infra/aws/ec2/canonical-fidelity/backfill.py: a refused window ends a kind with entitlement refusal and that refusal is the account's answer for the window, not a transient failure",
        "infra/aws/ec2/canonical-fidelity/backfill_run.py (uncommitted at filing): _walk_g keeps a kind whose reason is terminal and resumes only run-cap or lander-failure stops, from the recorded earliest less one day; tests/test_backfill_run.py test_terminal_g_is_not_walked_again"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Reference section 12 and the cell FT-s-4: a G with a recorded earliest date resumes from it, never refetches landed windows.",
    "world_is": "A run-cap or lander-failure stop resumes from the recorded earliest date less one day. An entitlement, retention, open-date or 20-year-cap stop is final for its kind and the walk is not repeated. The runner also clamps the walk at the 20-year cap measured from the run's own today, because the planner measures its cap from the top of a resumed walk and would otherwise reach past 20 years.",
    "notes": "For the COO to confirm or reverse. Pinned by test_terminal_g_is_not_walked_again and test_resumes_from_the_recorded_earliest_date."
  },
  {
    "id": "NFRA_FIDUPL-D1-W7-S6",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~7",
    "surfaced_at": "2026-10-21T01:36:45Z",
    "one_line": "The completion step flips the TO status of NFRA_FIDUPL.TO-FT-s-4 to complete, but that file is not in this order's paths block, so the worker cannot make the flip; the criterion passes and the instance validates.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "NFRA_FIDUPL.TO-FT-s-4 paths block lists infra/aws/ec2/canonical-fidelity/backfill_run.py, infra/aws/ec2/canonical-fidelity/tests/test_backfill_run.py and this investigation file only",
        "worker face PROOF step: flip the task order status to complete in the same commit as the instance; the TO file carries status pending at box/dell1 6bd116284f5",
        "same gap as NFRA_FIDUPL-D1-W2-S6 on the FU-s-4 order"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker face PROOF step: flip the task order status to complete in the same commit as the instance and the deliverables, once the FT-s-4-AC1 criterion PASSes.",
    "world_is": "The grant admits no path to the TO file, so the flip falls to the issuer or the gate. FT-s-4-AC1 PASSes (R1-FT4-OK passed=7) and the instance validates at code commit ea910790b1; the order stays pending on the worker side until the issuer flips it.",
    "notes": "Worker stopped before the flip; the instance and the code are committed LOCAL on wk-NFRA_FIDUPL-7. The COO or the gate owns the flip."
  },
  {
    "id": "NFRA_FIDUPL-D1-W4-S10",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~4",
    "surfaced_at": "2026-10-21T01:37:00Z",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~P1",
    "disposition": "UNDER_INVESTIGATION",
    "class": "OBSERVATION",
    "one_line": "box/run.py refuses any config.json that carries perg_secret_id: ALLOWED_KEYS has no such key, so check_pointers raises before any run mode dispatches.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/box/run.py@6bd116284f5 lines 21-25: ALLOWED_KEYS lists wealthscape_secret_id, quo_secret_id, quo_line_id, quo_sender, scope, region, profile_dir, work_dir, repo_root, mode, firm_labels, account_columns; perg_secret_id is absent",
        "local call in worktree C:/tmp/fidupl-w4 at cede76602d, no AWS and no secret: run.check_pointers(config) with a synthetic config carrying perg_secret_id printed 'REFUSED: config holds keys that are not pointers: perg_secret_id'",
        "org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md@6bd116284f5 section 12 names config.json key perg_secret_id (the per-G secret id)"
      ]
    },
    "spec_asserts": "REFERENCE section 12 (round 3): the box config.json carries the key perg_secret_id, and section 7 keeps config.json to POINTERS; box/run.py main() is the box's config gate and refuses keys outside its ALLOWED_KEYS.",
    "world_is": "ALLOWED_KEYS in box/run.py does not list perg_secret_id, so a config carrying the key is refused with 'config holds keys that are not pointers' before any once or daily run starts. perg_seed.py (FT-s-1) does not call check_pointers and reads the key directly, so FT-s-1 is not affected.",
    "notes": "Not edited: box/run.py is outside FT-s-1's grant. Disarm is the issuer's: add perg_secret_id to ALLOWED_KEYS as a string pointer in the cell that writes the key into config.json, or confirm where the key is written. ARMED until a config carrying the key passes check_pointers on the box. Measured on the local worktree only; the box config.json was not read."
  },
  {
    "id": "NFRA_FIDUPL-D1-W6-S2",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~6",
    "surfaced_at": "2026-10-21T01:36:22Z",
    "one_line": "The FT-s-3 status flip edits the task-order file, which is not in the order's <paths> grant; the grant names two code files and this investigation file only.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/NFRA/NFRA_FIDUPL/task-orders/NFRA_FIDUPL.TO-FT-s-3.in-run-signin-recovery.md lines 50-54 at worktree HEAD d8d168cbaa6: the <paths> block lists infra/aws/ec2/canonical-fidelity/signin_recover.py, infra/aws/ec2/canonical-fidelity/tests/test_signin_recover.py and the INVESTIGATION_v1.md file",
        "the same order, BOUNDS line 46: 'Grant. The <paths> block below and your deliverables folder'; line 62 orders the proof instance pinned and the order flipped to complete",
        "the worker standing rule orders the flip of the task order's <status> to complete committed together with the instance and deliverables"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "BOUNDS, Grant: the <paths> block and the deliverables folder are the worker's write surface; everything else the order names is read.",
    "world_is": "The standing flip step writes the task-order file of this order (one line, the status), which the grant does not name. The flip is made on that one file and nothing else in it is touched.",
    "notes": "Decision for the COO: whether the flip rides a grant line for the task-order file or is made by the issuer on the drain. The lane gate's behaviour on this commit is recorded in the commit report, not measured here."
  },
  {
    "id": "NFRA_FIDUPL-D1-W6-S3",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~6",
    "surfaced_at": "2026-10-21T01:36:22Z",
    "one_line": "On this device the client-data check of safe-commit did not grade the FT-s-3 code commit: the hashed account-id list is absent at the path the gate reads.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit output for commit d8d168cbaa6 printed: 'WARN: client-data-check: hashed account-id list ABSENT at C:\\Users\\Test\\.opal\\account_id_hashes.txt -- this commit was NOT checked for client account ids (absent is not empty; set OPAL_ACCOUNT_ID_HASHES or place the list there).'",
        "the commit holds two synthetic-fixture files (signin_recover.py and tests/test_signin_recover.py) and no client data was typed into either"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The safe-commit client-data check grades each commit against the hashed account-id list; a commit is only graded when the list is present.",
    "world_is": "On this device the list is absent, so the check printed a WARN and graded nothing for this commit. The commit is recorded as not checked for client account ids.",
    "notes": "Not fixed by this worker: the list's placement is outside this order's grant. The owner of the device's list decides whether the list is restored on dell1."
  },
  {
    "id": "NFRA_FIDUPL-D1-W6-S4",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~6",
    "surfaced_at": "2026-10-21T01:36:22Z",
    "one_line": "The worktree is sparse: infra/aws/lambda/ci is absent, so the naming gate prints NAMING ERROR on a commit that touches no Lambda path, and the commit still lands.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit output for commit d8d168cbaa6 printed: '[naming-gate] NAMING ERROR function-map folder missing: C:\\tmp\\fidupl-w6\\infra/aws/lambda/ci/function-map/ (the Lambda source map is read from this folder; nothing is graded from a copy)'",
        "bash test -d infra/aws/lambda/ci in the worktree printed 'lambda-ci-present: no'; the same commit printed '[commit-gate] OK: pre-commit gate clean for 2 of 2 file(s)' and the commit landed as d8d168cbaa6"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The naming gate grades the Lambda source map read from infra/aws/lambda/ci/function-map/ and reports a missing folder as NAMING ERROR.",
    "world_is": "On this worktree the folder is absent. The ERROR line printed and the commit landed, so on this path the line did not refuse the commit.",
    "notes": "Not fixed: the worktree is the lane's checkout and is not rebuilt here (the order forbids reconstructing the tree). Whether the gate's ERROR is a refusal on a full checkout is not measured."
  },
  {
    "id": "NFRA_FIDUPL-D1-W6-S5",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~6",
    "surfaced_at": "2026-10-21T01:36:22Z",
    "one_line": "The worktree's tracked copy of the round checker differs from the main-tree copy the COO named: the main tree carries an ft7 entry and a changed IAM simulate block; the ft3 entry is identical in both.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "diff of org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py: worktree HEAD d8d168cbaa6 (tracked, last changed at 6bd116284f5) against C:/Dev/ajb_workspace copy: hunk at line 88 adds the ft7 entry in the main tree; hunk at lines 648-650 changes the IAM simulate call to one ARN per call in the main tree; the dispatch line 861 differs by the ft7 addition",
        "lines 85-88 (TEST_FILES ft3 entry) are not in the diff; python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft3 run from C:/tmp/fidupl-w6 printed R1-FT3-OK passed=5 rc=0; the same command with the main-tree absolute path printed the same line"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The round checker is one file; the criterion invocation it names resolves to the same checker bytes in every tree that runs the round.",
    "world_is": "Two copies of the round checker differ: the main tree carries ft7 and a changed IAM check that the worktree's tracked copy does not. The FT-s-3 entry is identical in both, so the FT-s-3 result does not depend on which copy runs.",
    "notes": "Not fixed: the checker is the COO's and outside this order's grant. Decision for the COO: commit or align the checker so one tree carries the bytes the round grades."
  },
{
  "id": "NFRA_FIDUPL-D1-W8-S1",
  "project": "NFRA_FIDUPL",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~8",
  "surfaced_at": "2026-10-21T01:45:10Z",
  "one_line": "fetch_day takes no G, so a multi-G backfill run in one session fetches the signed-in G's day under every G key; the adapter keys its cache by (g, day) and never switches G.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~P1",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/canonical-fidelity/fetch.py@57170cd231c line 61: def fetch_day(session, date_string, out_dir, now=None) has no G parameter; the session is the only account selector",
      "infra/aws/ec2/canonical-fidelity/backfill_adapter.py@cb74c7aeec8 _day(): the cache key is (g, day) and fetch_day is called with the session wrapper, with no G switch between G values"
    ]
  },
  "spec_asserts": "The order's adapter takes the G argument, accepts it and never prints it, and fetches the day for that G (FT-s-7 item 1).",
  "world_is": "The adapter cannot select a G. Whatever G the one signed-in session holds is what the day folder contains. A runner that walks two G numbers in one session would land the same account's files under both G keys' windows.",
  "notes": "No live call was made; this is read from the code. Disarm: the runner must switch the session to each G before that G's windows, or the issuer must confirm the runner signs in per G. Recorded, not fixed here: the switch belongs to the runner or the switcher, outside this order's grant."
},
{
  "id": "NFRA_FIDUPL-D1-W8-S2",
  "project": "NFRA_FIDUPL",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~8",
  "surfaced_at": "2026-10-21T01:45:10Z",
  "one_line": "The planner's KINDS, EMPTY and COMPLETED constants do not match the six file-type kinds and the served value the FT-s-7 order names for the adapter.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/canonical-fidelity/backfill.py@57170cd231c line 13: KINDS = (transactions, positions_balances); backfill_g lines 127-128 raise ValueError for any other kind",
      "infra/aws/ec2/canonical-fidelity/backfill.py@57170cd231c lines 14-15 and 92-95: COMPLETED and EMPTY; an EMPTY window is skipped with continue, not a stop",
      "infra/aws/ec2/canonical-fidelity/backfill_adapter.py@cb74c7aeec8 wait() returns the string served, and request_export accepts the six file-type kinds"
    ]
  },
  "spec_asserts": "FT-s-7 item 1: the adapter implements the planner's ExportClient, and wait returns served for a day that carries files; an EMPTY listing raises RetentionLimit.",
  "world_is": "The planner's own vocabulary differs in three places: its kinds are two names, its status is COMPLETED or EMPTY, and an EMPTY window continues the walk instead of stopping it. The adapter follows the order (six kinds, served, empty is a stop). A runner that calls backfill_g directly would reject the six kinds, and one that reads the planner's EMPTY as a skip would not stop on the adapter's empty listing.",
  "notes": "The adapter was built to the order. The runner (FT-s-4) must use the same vocabulary as the adapter, and the issuer rules which vocabulary wins; no planner line was edited."
},
{
  "id": "NFRA_FIDUPL-D1-W8-S3",
  "project": "NFRA_FIDUPL",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~8",
  "surfaced_at": "2026-10-21T01:45:10Z",
  "one_line": "The planner yields calendar-day windows of 30 days by default, and a weekday holiday returns an empty listing that the order reads as a retention stop; the adapter refuses weekend and multi-day windows but cannot see a holiday.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~P1",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/canonical-fidelity/backfill.py@57170cd231c line 48: plan_windows(today, floor_date, chunk_days=30), and lines 58-65 yield every calendar day back to the floor",
      "infra/aws/ec2/canonical-fidelity/backfill_adapter.py@cb74c7aeec8 request_export raises ValueError for a weekend date_to and for date_from != date_to",
      "infra/aws/ec2/canonical-fidelity/backfill_adapter.py@cb74c7aeec8 _fetch_once: an empty status list raises RetentionLimit (evidence empty listing); a holiday has no status rows, so it looks the same"
    ]
  },
  "spec_asserts": "FT-s-7 item 1: one business day is one window, and the walk stops when the channel refuses or returns empty.",
  "world_is": "A runner fed the planner's defaults fails loudly on its first window (30-day span or a weekend). A runner fed business days still meets exchange holidays as empty listings, which the walk reads as the retention limit and stops early, so the recorded earliest date would be too recent. No trading-calendar check exists in the adapter.",
  "notes": "Disarm: the runner must hand the adapter single-day business-day windows from the trading calendar, and the issuer must confirm a holiday empty listing is not a retention stop before the live run. Not built here: the calendar belongs to the runner, outside this grant."
},
{
  "id": "NFRA_FIDUPL-D1-W8-S4",
  "project": "NFRA_FIDUPL",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~8",
  "surfaced_at": "2026-10-21T01:45:10Z",
  "one_line": "fetch_day returns the same listing for an empty status list and for a partial day, so the listing alone cannot tell retention from an unfinished export.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/canonical-fidelity/fetch.py@57170cd231c lines 74-76: fewer than six COMPLETED rows set missing to all six and failure to export not generated yet; no count is kept",
      "infra/aws/ec2/canonical-fidelity/backfill_adapter.py@cb74c7aeec8 _StatusTap counts statusElements of the status list itself, so zero rows is the only empty-listing test"
    ]
  },
  "spec_asserts": "FT-s-7 item 1: an EMPTY listing raises RetentionLimit and any other failure propagates.",
  "world_is": "Read from the code, a day with some but not all six files and a day with no rows produce identical listings. The adapter wraps the session and counts the status rows, so a partial day propagates as DayIncomplete. The fetch module does not expose the count.",
  "notes": "Resolved in the adapter; recorded because fetch.py's listing contract does not carry the count and a future caller could read the listing alone."
},
{
  "id": "NFRA_FIDUPL-D1-W8-S5",
  "project": "NFRA_FIDUPL",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~8",
  "surfaced_at": "2026-10-21T01:45:10Z",
  "one_line": "FetchError carries its HTTP status only in the message text, and a refused download never raises, so the entitlement mapping parses text and a download refusal is not classified.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/canonical-fidelity/fetch.py@57170cd231c line 69: raise FetchError(status list refused: HTTP %s) with no status attribute",
      "infra/aws/ec2/canonical-fidelity/fetch.py@57170cd231c lines 83-86: a refused download sets listing failure to download refused and does not raise",
      "infra/aws/ec2/canonical-fidelity/backfill_adapter.py@cb74c7aeec8 _fetch_once parses the status from the message with HTTP nnn and maps 401, 403 and 404 only"
    ]
  },
  "spec_asserts": "FT-s-7 item 1: an HTTP refusal (a FetchError that carries a 401, 403 or 404-class status) raises EntitlementRefused.",
  "world_is": "The status is recoverable only by parsing the message. A refused download is a listing failure, not an exception, so it reaches the adapter as DayIncomplete and propagates. It is not reported as an entitlement stop.",
  "notes": "Recorded for the issuer: an attribute on FetchError would remove the text parse. The download refusal is treated as an unclassified failure, which propagates and does not count as a stop."
},
{
  "id": "NFRA_FIDUPL-D1-W8-S6",
  "project": "NFRA_FIDUPL",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~8",
  "surfaced_at": "2026-10-21T01:45:10Z",
  "one_line": "The completion record's stop reasons have no session-cap value, so a run refused by the session-count rule is recorded as reason none with evidence session cap reached.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/NFRA/NFRA_FIDUPL/task-orders/NFRA_FIDUPL.TO-FT-s-7.backfill-adapter-and-main.md item 2: the stop is retention, entitlement, run_cap, open_date or none",
      "infra/aws/ec2/canonical-fidelity/backfill_main.py@cb74c7aeec8 _record / the session cap branch in main(): reason none, evidence session cap reached"
    ]
  },
  "spec_asserts": "FT-s-7 item 2: the completion record stop reason is one of retention, entitlement, run_cap, open_date or none.",
  "world_is": "The enumeration has no value for a session-count refusal. The record marks it as none with the evidence text, and sign_ins 0 keeps it out of the count.",
  "notes": "Issuer to confirm a session_cap value or accept none with this evidence. No enumeration value was added unilaterally."
},
{
  "id": "NFRA_FIDUPL-D1-W8-S7",
  "project": "NFRA_FIDUPL",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~8",
  "surfaced_at": "2026-10-21T01:45:10Z",
  "one_line": "The runner interface in reference section 12 leaves plan_inputs, the lander call shape, the records class and the session_factory call pattern undefined, and backfill_run.py is not in this worktree.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md section 12: backfill_run.run(plan_inputs, export_client, lander, session_factory, records, caps) with no shape for the first three and the records object",
      "infra/aws/ec2/canonical-fidelity/backfill_main.py@cb74c7aeec8 main() passes plan_inputs with keys today, floor_date, max_days and perg; lander(folder, *args); records from the factory; sessions_today() on it"
    ]
  },
  "spec_asserts": "FT-s-7 item 2: main calls backfill_run.run(...) and counts sessions through records.sessions_today().",
  "world_is": "backfill_run is imported lazily and does not exist in this worktree (FT-s-4 builds it in parallel). The shape main passes is the one this module chose, so the runner must accept it. Until FT-s-4 lands, the real path cannot be exercised.",
  "notes": "Tests use fakes for run and records. The issuer reconciles the shape with FT-s-4 at its merge."
},
{
  "id": "NFRA_FIDUPL-D1-W8-S8",
  "project": "NFRA_FIDUPL",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~8",
  "surfaced_at": "2026-10-21T01:52:00Z",
  "one_line": "The criterion's relative checker path resolves in the worktree to a different copy of fidupl_round_checks.py than the main tree copy the order names; both print R1-FT7-OK passed=9.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "md5sum of org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py in worktree C:/tmp/fidupl-w8: 0f15f1f2d0028531c3d5b5a513570d52",
      "md5sum of C:/Dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py (main tree): e28a2e8903183a97791aca2dcc89861d"
    ]
  },
  "spec_asserts": "FT-s-7 criterion invocation: python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft7 (relative path); the order's worker face says run the main tree's checker by absolute path.",
  "world_is": "The relative path, run from the worktree, reaches a checker copy whose bytes differ from the main tree copy. The ft7 verdict is identical in both (R1-FT7-OK passed=9). The worker ran the main-tree copy by absolute path as directed, and recorded the criterion text as the invocation.",
  "notes": "Not reconciled here: which checker copy is authoritative is the issuer's call (the checker is the COO's file, outside this grant). The divergence is recorded, not fixed."
},
  {
    "id": "NFRA_FIDUPL-D1-W5-S5",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~5",
    "surfaced_at": "2026-10-21T01:40:00Z",
    "one_line": "FT-s-2 reads the logout statuses from the session object (session.logout_statuses), but signin.Session exposes no such attribute: the close writes the statuses only as a text line into the driver's trace, so the coverage record's logout is null on every live run until the session surfaces them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/signin.py@6bd116284f5 line 1129: self._post_lines.append(\"logout statuses=%s,%s\" % (first, second)) inside WealthscapeDriver.logout()",
        "infra/aws/ec2/canonical-fidelity/signin.py@6bd116284f5 lines 1162-1169: Session.close() calls the driver's logout() through getattr and sets no attribute on the session object",
        "comp-find 'logout_statuses|perg_secret_id|perg-list' over infra/aws/ec2/canonical-fidelity in worktree C:/tmp/fidupl-w5 (2026-10-21T01:3xZ): 0 hit(s) across 31 file(s) scanned"
      ]
    },
    "spec_asserts": "TO FT-s-2 item 2: read the logout statuses from the session object (session.logout_statuses if present, else None) and put them in the coverage record as logout; the session close already logs out (logout statuses=a,b in the driver's trace).",
    "world_is": "No class in signin.py at 6bd116284f5 carries a logout_statuses attribute. The statuses exist only in the driver's _post_lines trace text, so getattr(session, 'logout_statuses', None) returns None and the coverage record's logout field is null on the live path.",
    "notes": "Not fixed here: signin.py is outside this order's grant. The coverage record reads getattr(session, 'logout_statuses', None) exactly as the order says and carries the value when a session supplies it. Decision for the COO: whether signin.Session should expose the statuses (a signin.py change in a later cell) or the coverage record should read them from the trace file."
  },
  {
    "id": "NFRA_FIDUPL-D1-W5-S6",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~5",
    "surfaced_at": "2026-10-21T01:40:00Z",
    "one_line": "FT-s-2 names the unattributed landing 'under alongside', but split.py places an account whose label matches no firm_labels entry under unplaced and writes nothing for it; the alongside scope comes only from switcher_list's no-match rule, so the coverage record reports a scope and makes no landing claim.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/split.py@6bd116284f5 _placement(): an unmapped label adds its accounts to acct_unmapped; _classify() returns ('unplaced', None) for them",
        "infra/aws/ec2/canonical-fidelity/split.py@6bd116284f5 split_day(): _dest(firm, ...) is called only for firms that have accounts in by_firm, so no object is written for an unplaced account",
        "NFRA_FIDUPL_R1_WORKER_REFERENCE.md section 12 (switcher_list.firm_for_label: no match returns ('alongside', False))"
      ]
    },
    "spec_asserts": "TO FT-s-2 item 1 and its counts: 'unattributed landed under alongside, named by ordinal only'; the test name test_unattributed_g_lands_under_alongside_and_is_named_by_ordinal.",
    "world_is": "The split stage does not land an unattributed label under alongside: its accounts are listed under unplaced and no file is written for them. Whether any object lands under alongside depends on the box's firm_labels pointers, which this stage does not read.",
    "notes": "Recorded as the coverage record's unattributed.firm_scopes (the switcher's scope), with the ordinal list. The test asserts the scope and the ordinal, never a landed object. Decision for the COO: whether unattributed accounts should land under alongside (a split.py change outside this grant) or stay unplaced as split.py has them."
  },
  {
    "id": "NFRA_FIDUPL-D1-W5-S7",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~5",
    "surfaced_at": "2026-10-21T01:40:00Z",
    "one_line": "The premise that config.json already carries perg_secret_id and that the code reads it is false at the base: check_pointers rejects the unknown key and no module reads it; this cell adds the key to the pointer allow-list and the secret-id check in box/run.py.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/box/run.py@6bd116284f5 ALLOWED_KEYS (lines 21-25) holds no perg_secret_id, so check_pointers raises ConfigError 'config holds keys that are not pointers' for a config that carries it",
        "comp-find 'logout_statuses|perg_secret_id|perg-list' over infra/aws/ec2/canonical-fidelity in worktree C:/tmp/fidupl-w5 (2026-10-21T01:3xZ): 0 hit(s) across 31 file(s) scanned"
      ]
    },
    "spec_asserts": "NFRA_FIDUPL_R1_WORKER_REFERENCE.md section 12: config.json key perg_secret_id holds the per-G secret id (the code reads it; a missing key means no cross-check).",
    "world_is": "At 6bd116284f5 no module reads perg_secret_id and the pointer check refuses it, so the key cannot reach the daily stage. This cell admits the key to the allow-list and to the secret-id check, and wires read_perg and write_coverage as daily deps in box/run.py _real_daily_deps (the reference names no dep for the per-G read or the coverage write).",
    "notes": "The box config.json does not carry the key until the box is provisioned; a missing key gives checked false with one SKIP line, as the reference says. The added deps are the only wiring the order did not name."
  },
  {
    "id": "NFRA_FIDUPL-D1-W5-S8",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~5",
    "surfaced_at": "2026-10-21T01:53:25Z",
    "one_line": "The coordinator's fix (recover_session raises signin_recover.AttachError, which must stop the run with the original refusal) cannot be committed by this worker: the order is complete at HEAD 177617a95d, the owned-paths lane gate treats a terminal order as granting nothing, and the gate refuses run.py and tests/test_box_daily.py.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git commit of box/run.py and tests/test_box_daily.py through .tools/safe-commit.sh at 2026-10-21T01:52Z (worktree C:/tmp/fidupl-w5): 'owned-paths lane violation(s)' with 'no NON-TERMINAL task order at HEAD issued_to this serial names this path in its <paths> block'",
        "NFRA_FIDUPL.TO-FT-s-2 status at HEAD 177617a95dc: <status>complete</status> (the flip commit, admitted while the order was pending)",
        "the fix is uncommitted in the worktree; its diff is saved at .scratch/attach_fix.patch in C:/tmp/fidupl-w5 (not committed)"
      ]
    },
    "spec_asserts": "Coordinator interface fact (box/dell1 signin_recover.py: class AttachError(Exception) raised when the unit does not start, the CDP port does not open, or no page exists): a recovery failure of any kind records recovery failed and stops the run with the original refusal.",
    "world_is": "HEAD 177617a95dc treats AttachError as a run error rather than the refusal, because the hook re-raises the recovery exception. The corrected hook and its test are uncommitted. The lane gate grants no paths to a complete order, so the worker cannot commit the correction.",
    "notes": "Not overridden: no GIT_COMMIT_AUTHOR_OVERRIDE and no force. Decision for the COO: reopen this order or issue a follow-up order that names box/run.py and tests/test_box_daily.py, then the worker or the COO commits .scratch/attach_fix.patch. The order status is left complete at HEAD as committed."
  },
{
  "id": "NFRA_FIDUPL-D1-W8-S9",
  "project": "NFRA_FIDUPL",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~8",
  "surfaced_at": "2026-10-21T02:01:13Z",
  "one_line": "The merged runner cannot drive the merged adapter: it accepts only the planner's two kinds, the planner needs COMPLETED and bytes where the adapter returns served and a folder, so the live walk cannot run end to end.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/canonical-fidelity/backfill_run.py@55b6d748907 line 173: run() raises ValueError unknown export kind for any kind outside backfill.KINDS (transactions, positions_balances); main passes the six file-type kinds",
      "measured: main driven with the real backfill_run.run and the test fakes raised ValueError before any sign-in (run_error ValueError, sign_ins 0) -- scratch check, not committed",
      "infra/aws/ec2/canonical-fidelity/backfill.py@55b6d748907 lines 96-97: a wait() status other than COMPLETED raises RuntimeError; the adapter returns served per the order",
      "infra/aws/ec2/canonical-fidelity/backfill.py@55b6d748907 lines 98 and 106: the planner writes the bytes returned by download() into export.bin; the adapter returns the day folder"
    ]
  },
  "spec_asserts": "FT-s-7 item 1 (order): wait returns served and download returns the day's folder for the lander; FT-s-4 (reference section 12): the runner walks backfill.py's planner with the planner's kinds, statuses and download contract.",
  "world_is": "Both sides are correct to their own spec and the two specs disagree on the kind vocabulary, the status word and the download payload. The fakes in both test files never cross the seam, so the suites pass. A live run through backfill_main stops at the runner's kind check before any sign-in: no harm, no walk.",
  "notes": "The fix is a contract decision for the issuer (one vocabulary across the planner, runner and adapter), not a local edit: it touches backfill.py and backfill_run.py, outside this grant. Until it is made the box command must not be run live. Extends S2."
},
{
  "id": "NFRA_FIDUPL-D1-W8-S10",
  "project": "NFRA_FIDUPL",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~8",
  "surfaced_at": "2026-10-21T02:01:13Z",
  "one_line": "The runner counts every request_export against max_exports_per_run, including the skipped non-trading days the adapter answers without a request, so the 12-export cap covers about eight trading days per run.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/canonical-fidelity/backfill_run.py@55b6d748907 lines 94-100: _Walk.request_export increments self.exports before delegating to the client, so a skipped day is counted",
      "infra/aws/ec2/canonical-fidelity/backfill_main.py@d7123e46c24 plan_inputs chunk_days 1: one window per calendar day, weekends and holidays included"
    ]
  },
  "spec_asserts": "REPAIR 1 item 2 (order): a non-trading day is skipped WITHOUT a request.",
  "world_is": "The adapter sends no channel request for a skipped day, but the runner's cap counter still counts it. With twelve exports a run walks at most twelve calendar days, about eight trading days, and then stops with run_cap. The stop is safe (the walk resumes on the next run) but the per-run rate is lower than the cap implies.",
  "notes": "The counter is the runner's; the adapter cannot change it from inside its grant. The issuer rules whether skipped days are free (a runner change) or the cap is sized in calendar days."
},
  {
    "id": "NFRA_FIDUPL-D1-W3-S9",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~3",
    "surfaced_at": "2026-10-21T02:27:02Z",
    "one_line": "REPAIR 3 names a split.py call at line 170 that still passes one argument to the lander's content-date helper; at the cut the call already passes the file name and the eleven split tests pass, so no REPAIR 3 change was needed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/split.py@fdd09568862 line 170: day = land._content_date(data, name)",
        "infra/aws/ec2/canonical-fidelity/tests/test_split.py@fdd09568862: 11 def test_ functions; python -m pytest on test_split.py at the cut: 11 passed",
        "NFRA_FIDUPL.TO-FR-s-2.firm-split.md REPAIR 3 (issuer, 2026-10-21 ~01:15Z) states the call still takes one argument"
      ]
    },
    "spec_asserts": "TO FR-s-2 REPAIR 3: split.py line 170 still calls land._content_date(data); the module suite shows TypeError in eleven tests.",
    "world_is": "At the cut fdd09568862 the call at line 170 already passes name, and the module suite had no TypeError. The REPAIR 3 premise did not hold at the cut; the fixtures already place each date in its file's own column.",
    "notes": "For the issuer: the REPAIR 3 text describes a state that the base no longer holds. REPAIR 4 was built on the cut as it stands (commit 4ab5a764205)."
  },
  {
    "id": "NFRA_FIDUPL-D1-W3-S10",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~3",
    "surfaced_at": "2026-10-21T02:27:02Z",
    "one_line": "The flip of NFRA_FIDUPL.TO-FR-s-2 to complete needs a write to the task-order file, which the worker grant (the paths block: split.py, tests/test_split.py, the investigation file) does not name.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/NFRA/NFRA_FIDUPL/task-orders/NFRA_FIDUPL.TO-FR-s-2.firm-split.md@fdd09568862 line 8: <status>pending</status>",
        "same file lines 76-80: the paths block names split.py, tests/test_split.py and the investigation file only",
        "NFRA_FIDUPL-D1-W3-S6 (round 1, same gap): the grant admits no path to the TO file"
      ]
    },
    "spec_asserts": "The worker flips the task-order status to complete in the same commit as the proof instance once the criterion PASSes (the user's order for this run).",
    "world_is": "The grant admits no path to the TO file, so the status flip cannot be committed by this worker. The criterion FR2-AC1 is graded here and the instance is pinned; the status stays pending for the issuer or the gate.",
    "notes": "Criterion FR2-AC1 is the BLOCKING criterion of this row for the flip only; the code and tests criterion is unaffected. Recurring: W3-S6 filed the same gap in round 1."
  },
  {
    "id": "NFRA_FIDUPL-D1-W3-S11",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~3",
    "surfaced_at": "2026-10-21T02:40:00Z",
    "one_line": "The FR2-AC1 invocation names a relative checker path that resolves in the worktree, but that worktree copy of fidupl_round_checks.py differs from the main tree's copy (the file the order names), so the two are not the same checker.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cmp of org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py in wk-NFRA_FIDUPL-3 against C:/Dev/ajb_workspace copy: differ at char 35702, line 642",
        "the same fr2 invocation returns R1-FR2-OK passed=13 (rc 0) from the worktree copy and from the main-tree copy by absolute path"
      ]
    },
    "spec_asserts": "TO FR-s-2 REPAIR 4 and the REPORT line: run the criterion with the main tree's checker by absolute path; the criterion's invocation names the relative path org/tier1_exec/.../fidupl_round_checks.py fr2.",
    "world_is": "The relative path in the criterion resolves to a worktree copy that is not the main tree's copy. For the fr2 target both print R1-FR2-OK passed=13; the difference sits at line 642, outside the fr2 path.",
    "notes": "For the issuer: the checker is a shared file and the worktree copy lags or leads the main tree. The main-tree absolute-path run is the run the order names; the proof records both."
  },
  {
    "id": "NFRA_FIDUPL-D1-S10",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~NFRA1",
    "surfaced_at": "2026-10-21T02:42:00Z",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "class": "BLOCKING",
    "one_line": "box/run.py rejects the null account columns the order and split.py require, so the TO-FT-s-8 daily-mode proof run refused at config validation, before any secret read or sign-in.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM 82fbe072-9e23-455e-938d-f3a5e74e53a5 on i-028e830f7226cc685 at 02:37Z (the issuer's GO 8946, one attempt): /opt/fidelity-uploader/venv/bin/python /opt/fidelity-uploader/box/run.py /opt/fidelity-uploader/config.daily.json printed exactly: 'ERROR: config account_columns value for prices.txt is not a column index' then exit=2",
        "infra/aws/ec2/canonical-fidelity/box/run.py line 84: _check_account_columns raises when 'isinstance(column, bool) or not isinstance(column, int) or not 0 <= column <= 200', so a JSON null (None) for prices.txt or security.txt is refused",
        "box/run.py main(), lines 306-310: check_pointers(config) runs before _run_daily_mode / run_once; a ConfigError returns 2 with only the ERROR line, before read_secret and open_session, so no Fidelity sign-in happened",
        "TO-FT-s-8 step 1 and ft8c: account_columns carries prices.txt null and security.txt null (ft8c R1-FT8C-OK); the delivered split.py (eighteenth delivery, fu10m R1-FU10M-OK 21 files) takes a null account column for those two files"
      ]
    },
    "spec_asserts": "TO-FT-s-8 step 2: one run of box/run.py on config.daily.json (prices and security null) signs in once, switches the G number 31 times and writes the split; REPAIR 4 of FR-s-2 gave split.py null account columns.",
    "world_is": "The config validator in box/run.py was not widened to admit null with split.py, so the daily config copy the order requires cannot load. The run refused before doing anything on the box or at Fidelity; config.json, config.daily.json, work/, both profiles and the agent Chrome unit are unchanged.",
    "notes": "Not edited: box/run.py is shipped repo code outside this order's grant, and the issuer allowed ONE attempt with no retry. Fix for the issuer: _check_account_columns accepts None for the unsplit files (prices.txt, security.txt) and a test for it; then one more delivery and a new GO. config.daily.json needs no change. Ledger nfra-fidupl-daily-proof-20261021 stays open on L2."
  },
  {
    "id": "NFRA_FIDUPL-D1-S11",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~NFRA1",
    "surfaced_at": "2026-10-21T02:58:00Z",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "class": "BLOCKING",
    "one_line": "The TO-FT-s-8 daily-mode proof run landed but its attribute stage ended AdapterShapeError, so no split ran and no firm prefix was written; run.py prints only the class name, not the fixed-text shape message.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM 8ee2bbf6-a733-4e30-b32c-0aed29f9a7b6 on i-028e830f7226cc685 at 02:49Z (the issuer's GO 8950, ONE attempt, no retry), status Success, stdout verbatim: 'ERROR: stage attribute did not finish: AdapterShapeError' / 'SKIP: split (no attribution)' / 'SKIP: coverage counts (attribution did not finish)' / 'OK: coverage record written' / 'WARN: partial run: land landed; not finished: attribute' / 'ERROR: daily run 20261021T024959Z business_day=2026-10-20 rc=1' / exit=1",
        "s3://opal-data-assets/fidelity/alongside/bronze/_runs/20261019/run-20261021T025115Z.json: outcome ALL_LANDED, failed_step null, failure_class null (the land stage is clean)",
        "s3://opal-data-assets/fidelity/alongside/bronze/_runs/20261020/coverage-20261021T024959Z.json: counts null, unattributed null, cross_check checked false, logout statuses 204 and 400, recovery not-needed",
        "aws s3api list-objects-v2 for fidelity/{cottonwood,inflection,49financial,keilfinancial,abidingwealth,lighthousewealth,vmwealth}/: 0 keys under every one of the seven prefixes; fidupl_round_checks.py ft8r: R1-FT8R-FAIL no split record under s3://opal-data-assets/fidelity/alongside/bronze/_runs/",
        "adapters.py raises AdapterShapeError at lines 115, 146, 156, 208 and 214 (top-level shape, a row with no scalar key, no pageResponse.available, collected short of available); which one fired is not in the run's output"
      ]
    },
    "spec_asserts": "TO-FT-s-8 step 2: one run of box/run.py on config.daily.json signs in once, sweeps the 31 G numbers, pages accountList, and writes the split under fidelity/<firm>/ plus the coverage record; FT-s-8-AC2 expects four files split and at least three firms with rows.",
    "world_is": "The land stage finished; the attribute stage (switcher sweep / accountList paging through adapters.py) raised AdapterShapeError against the live responses, so split and the coverage counts were skipped. The logout statuses 204 and 400 are as the coverage record shows. Nothing was written under any firm prefix. config.json, work/, both profiles and the agent Chrome unit were not touched by me.",
    "notes": "Not retried (one attempt per the GO). Which AdapterShapeError message fired is the missing fact: run.py logs the class name only, while adapters.py's messages are fixed text naming keys and types, never values. For the issuer: print that fixed text in the stage line (or in the coverage record's failure field) and re-cut; the box needs no change. Ledger nfra-fidupl-daily-proof-20261021 stays open on L2; FT-s-8 stays pending."
  },
  {
    "id": "NFRA_FIDUPL-D1-S12",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~NFRA1",
    "surfaced_at": "2026-10-21T03:12:00Z",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "class": "BLOCKING",
    "one_line": "The live accountList paging stops at the first 2000 rows (collected 2000 of 5204 available), so the attribute stage fails loud and no split runs: the request-side paging field names assumed in row D1-W5-S4 do not page on the live API.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM 2e549230-5b30-485b-8fa7-96eaff99b906 on i-028e830f7226cc685 at 03:04Z (the issuer's GO 8957, ONE attempt, no retry), status Success, stdout verbatim: 'ERROR: stage attribute did not finish: AdapterShapeError' / 'ERROR: attribute shape: accountList short of total: collected 2000 of 5204 available' / 'SKIP: split (no attribution)' / 'SKIP: coverage counts (attribution did not finish)' / 'OK: coverage record written' / 'WARN: partial run: land landed; not finished: attribute' / 'ERROR: daily run 20261021T030437Z business_day=2026-10-20 rc=1' / exit=1",
        "s3://opal-data-assets/fidelity/alongside/bronze/_runs/20261020/coverage-20261021T030437Z.json: attribute_error 'accountList short of total: collected 2000 of 5204 available', counts null, unattributed null, logout 204 and 400; run record _runs/20261019/run-20261021T030546Z.json 2789 bytes (land stage)",
        "adapters.py line 214 raises 'accountList short of total: collected %d of %d available' only when the page loop ends short of pageResponse.available; fidelity/{cottonwood,inflection,49financial,keilfinancial,abidingwealth,lighthousewealth,vmwealth}/ hold 0 keys; fidupl_round_checks.py ft8r: R1-FT8R-FAIL no split record",
        "row NFRA_FIDUPL-D1-W5-S4 (worker 0.9.0_WK_NFRA_FIDUPL~5): 'the request-side names are an assumption ... a later page returns the first page again or no rows ... fails loud with the two counts (short of available)' -- the live outcome is exactly that branch"
      ]
    },
    "spec_asserts": "Row D1-W5-S4 and FR-s-6 REPAIR: page accountList by pageResponse.available, sending start and sessionCacheId on later pages; the proof run reaches the 5204 available (31 G numbers, 8 firms) and writes the split.",
    "world_is": "The first page returns 2000 rows and available 5204, and the following requests do not deliver new distinct rows under the assumed names, so the loop ends at 2000 distinct. The lister counted distinct numbers and failed loud with the two counts, as designed; nothing was split and no firm prefix was written. Which G number the sweep was on when it stopped is not in the output.",
    "notes": "Not retried (one attempt per the GO) and nothing edited. For the issuer: the live request form for page 2 has to be measured (a values-free capture of the second accountList request's field NAMES from the signed-in session, e.g. by the agent Chrome driver), then adapters.py corrected and delivered once more. The box needs no other change. Ledger nfra-fidupl-daily-proof-20261021 stays open on L2; FT-s-8 stays pending."
  },
  {
    "id": "NFRA_FIDUPL-D1-S13",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~NFRA1",
    "surfaced_at": "2026-10-21T03:36:00Z",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "class": "BLOCKING",
    "one_line": "None of the lister's eleven candidate page-2 forms (0-10) added a row on the live API: accountList still ends at 2000 of 5204, so no split ran; no 401 or 403 and no recovery sign-in.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM e6929c3d-e1ab-49ed-8bfd-c5b27eccaa58 on i-028e830f7226cc685 at 03:29Z (the issuer's GO 8969, ONE attempt, no retry), status Success, stdout verbatim: 'ERROR: stage attribute did not finish: AdapterShapeError' / 'ERROR: attribute shape: accountList paging: no form added rows; tried forms 0-10; collected 2000 of 5204 available' / 'SKIP: split (no attribution)' / 'SKIP: coverage counts (attribution did not finish)' / 'OK: coverage record written' / 'WARN: partial run: land landed; not finished: attribute' / 'ERROR: daily run 20261021T032948Z business_day=2026-10-20 rc=1' / exit=1; no 'OK: accountList paging form=' line",
        "s3://opal-data-assets/fidelity/alongside/bronze/_runs/20261020/coverage-20261021T032948Z.json: attribute_error as above, paging_form null, counts null, recovery 'not-needed', logout statuses 204 and 400; land record _runs/20261019/run-20261021T033100Z.json",
        "fidelity/{cottonwood,inflection,49financial,keilfinancial,abidingwealth,lighthousewealth,vmwealth}/ hold 0 keys; fidupl_round_checks.py ft8r: R1-FT8R-FAIL no split record under s3://opal-data-assets/fidelity/alongside/bronze/_runs/",
        "row NFRA_FIDUPL-D1-S12 (same failure before the lister tried candidate forms); no 401 or 403 line in the output"
      ]
    },
    "spec_asserts": "TO-FR-s-6 REPAIR 1 and 2 (issuer msg 8966): the lister tries eleven candidate paging forms for page 2 and keeps the first that adds distinct rows; FT-s-8 step 2 then reaches 5204 and splits.",
    "world_is": "All eleven candidate forms returned no new distinct rows, none was refused with a 401 or 403, and the lister fell back to its loud failure at 2000 of 5204. The live page-2 form is therefore outside the table. Nothing was split; no firm prefix was written. This was the third sign-in in its trailing hour (02:49Z, 03:04Z, 03:29Z); no recovery sign-in fired (recovery not-needed).",
    "notes": "Not retried (one attempt per the GO; the issuer also bars any sign-in before 04:30Z) and nothing edited. For the issuer: guessing further forms spends sign-ins; the page-2 request has to be MEASURED, values-free, from a signed-in session (the agent Chrome driver on the box, CDP) or from the CRO's capture, then adapters.py corrected once. Ledger nfra-fidupl-daily-proof-20261021 stays open on L2; FT-s-8 stays pending."
  },
  {
    "id": "NFRA_FIDUPL-D1-S14",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~NFRA1",
    "surfaced_at": "2026-10-21T06:08:00Z",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "class": "BLOCKING",
    "one_line": "The TO-FT-s-11 live backfill run ended with run_error=TimeoutError after its one sign-in: the walk never started (walk null), no stop reason, no day landed, so FT-s-11-AC1 reads FAIL.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM fa3700a4-30fe-414f-a377-f41a083b7663 on i-028e830f7226cc685 at 06:01:20Z (the issuer's order GO 9004, ONE attempt, no retry), status Success, stdout verbatim: 'ERROR: backfill run did not finish: TimeoutError' / 'ERROR: backfill run_id=20261021T060121Z scope=domain sign_ins=1 stop=none' / six 'FILETYPE <type> days=0 bytes=0 earliest=none' lines / exit=1",
        "s3://opal-data-assets/fidelity/alongside/bronze/_runs/20261021/backfill-20261021T060121Z.json (1074 bytes, finished 06:03:36Z): backfill true, run_error 'TimeoutError', sign_ins 1, stop {evidence none, reason none}, walk null, per_file_type all six days 0 bytes 0 earliest_date null, caps max_days 125 max_exports_per_run 12 max_sessions_per_day 2",
        "fidupl_round_checks.py ft11r: R1-FT11R-FAIL run_error=TimeoutError",
        "aws s3api list-objects-v2 under fidelity/alongside/bronze/ with LastModified from 06:00Z excluding _runs/: 0 keys; a run record _runs/20261019/run-20261021T060236Z.json (2789 bytes, 06:02:37Z) was also written during the run (content not read)"
      ]
    },
    "spec_asserts": "TO-FT-s-11 step 2 and FT-s-11-AC1: one run of backfill_main.py signs in once, walks the New York calendar back through the Export Status list, lands each COMPLETED day by content date, and writes ONE completion record with a stop reason.",
    "world_is": "The run signed in once and raised TimeoutError before the walk began (walk null); the completion record names the error and no stop reason. Nothing was landed (0 data keys), the starting G state is not part of this walk, and no 401, 403 or lockout line appears. Which request timed out is not in the output or the record.",
    "notes": "Not retried (one attempt per the order) and nothing edited. For the issuer: the record carries the error class only; the failing step (a stage that wrote the 06:02:37Z run record, or the Export Status read) and its fixed-text detail need to be printed, as was done for the AdapterShapeError (row D1-S11). Sign-in count: this was the 3rd in its trailing hour (05:31Z, 05:46Z, 06:01Z); no recovery sign-in exists in this walk, so none fired. A re-run needs the issuer's new GO and my count at that time."
  },
  {
    "id": "NFRA_FIDUPL-D1-S15",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~NFRA1",
    "surfaced_at": "2026-10-21T07:06:00Z",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "class": "BLOCKING",
    "one_line": "The TO-FT-s-11 step 3B backfill rerun ran the whole SSM cap of 900 s and was stopped (status TimedOut) with no stdout, no completion record and no data landed, so the walk does not finish inside the cap and a stopped run prints nothing.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM bfd976a6-b9e4-4162-8bb7-1124a1d2bd8b on i-028e830f7226cc685, started 06:47:20Z (the issuer's GO 9009, ONE attempt, no retry), executionTimeout 900: InProgress at 06:58:13Z, TimedOut at 07:02:25Z; the whole output was the single stderr calendar WARN line, no stdout and no 'exit=' line",
        "aws s3api list-objects-v2 under fidelity/alongside/bronze/_runs/ from 06:40Z: one key, _runs/20261019/run-20261021T064829Z.json (2789 bytes, 06:48:31Z); no backfill-<run id>.json completion record",
        "the same listing under fidelity/alongside/bronze/ excluding _runs/ from 06:40Z: 0 keys",
        "SSM pgrep after the stop: no backfill_main, perg_seed, signin, box/run.py, paging_probe or g_export process; fidelity-agent-chrome.service active"
      ]
    },
    "spec_asserts": "TO-FT-s-11 step 3B and FT-s-11-AC1: one run of backfill_main.py (defaults 125 days, 12 exports, 2 sessions a day, 120 s request timeout) ends by itself with a completion record, a stop reason and the DAY lines, inside the SSM executionTimeout of 900.",
    "world_is": "The run did not end by itself inside 900 s. The program prints its DAY and FILETYPE lines and writes its completion record only at the end, so being stopped by the cap left neither. One run record was written about 70 s in and no data was landed. Whether the Fidelity session was logged out is not known (the stop may have skipped the logout path); no process remains on the box.",
    "notes": "Not retried and nothing edited. For the issuer: (1) a run that can last past the cap needs its own heartbeat lines (a DAY line per day flushed as it is read) and a wall-clock budget below the SSM cap that stops it cleanly with the completion record and the logout, or an executionTimeout above the run's own budget; (2) with 120 s per request and up to 12 exports the worst case is far over 900 s, so the budget decides the answer, not the calendar. Sign-ins in the trailing hour: 06:01Z mine, about 06:32Z the issuer's, 06:47Z this run; none fired as a recovery. A ledger was not opened before this rerun (my omission); a post-hoc entry records it."
  },
  {
    "id": "NFRA_FIDUPL-D1-S16",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~NFRA1",
    "surfaced_at": "2026-10-21T07:40:00Z",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "class": "BLOCKING",
    "one_line": "The bounded backfill (step 3C) ended by itself at its wall budget but its record reads run_error=TargetClosedError with stop=none and days=0 for every file type, although day 2026-10-20 printed completed and day 2026-10-19 hung on one downloadExport.do for 452 s.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM 1441ca48-d06c-42c6-9750-90239de00c39 on i-028e830f7226cc685 at 07:22:16Z (the issuer's GO 9019, ONE attempt, executionTimeout 660, --max-seconds 480 --max-sessions 4), Success, stdout lines verbatim in the deliverable NFRA_FIDUPL.TO-FT-s-11.backfill_probe1_step3C_output.md: 'DAY 2026-10-21 result=empty secs=0' / 'DAY 2026-10-20 result=completed secs=30' / 'REQ GET downloadExport.do status=error:WallBudget secs=452' / 'DAY 2026-10-19 result=budget secs=473' / 'ERROR: backfill run did not finish: TargetClosedError' / 'CLOSE ok secs=0' / 'stop=none' / six FILETYPE lines days=0 bytes=0 earliest=none / exit=1",
        "s3://opal-data-assets/fidelity/alongside/bronze/_runs/20261021/backfill-20261021T072217Z.json (1373 bytes): run_error TargetClosedError, stop {reason none, evidence none}, sign_ins 1, walk null, days [2026-10-21 empty 0; 2026-10-20 completed 30; 2026-10-19 budget 473], per_file_type all zero",
        "fidupl_round_checks.py ft11r: R1-FT11R-FAIL run_error=TargetClosedError; 0 data keys under fidelity/alongside/bronze/ (non-_runs) since 07:20Z",
        "the box ran the 170a9c69ce8 file; the issuer's update msg 9026 (head 3d8b85fd61d: per-day partial record, SIGTERM logout) was sent at 07:28:41Z, after the run began, and was delivered at 07:33Z"
      ]
    },
    "spec_asserts": "Step 3C: the run prints every DAY, REQ, SIGNIN and CLOSE line, stops itself at its wall budget with a stop reason, and writes the record; FT-s-11-AC1 expects a record with no run error and a stop reason.",
    "world_is": "The run behaved as designed up to the budget: sign-in, one empty day, one completed day, then a single download that ran 452 s until the wall budget, and a clean CLOSE (logout). After the budget it raised TargetClosedError, so the record carries a run error, no stop reason and zero counts; it is not stated whether day 2026-10-20 was counted as already landed, and no data key was written.",
    "notes": "Not retried (budget and timeout stops are an answer per the issuer) and nothing edited. For the issuer: (1) the budget stop is not recorded as stop=budget and the error class hides it; (2) the counts and the earliest date for a completed day are zero in the record, so the answer to deliverable 2 (earliest date, days, bytes) is not readable from it; (3) the 2026-10-19 download that hangs is the live finding. Sign-ins in the trailing hour: the issuer's 07:08Z, 06:47Z mine, this run 07:22Z."
  },
  {
    "id": "NFRA_FIDUPL-D1-S17",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~NFRA1",
    "surfaced_at": "2026-10-21T08:40:00Z",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "class": "BLOCKING",
    "one_line": "The step 3D backfill served 2026-10-20 (six files) and five of six files of 2026-10-19, but the sixth 2026-10-19 file never returned inside the 480 s budget, the five served files were not landed, and the record again reads TargetClosedError, stop none, days 0 bytes 0.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM 52b0a403-ade6-4b44-b3c6-77bc8e87c4d9 on i-028e830f7226cc685 at 08:22:16Z (the issuer's GO 9032, ONE attempt, --max-seconds 480 --max-sessions 6, executionTimeout 660), Success, exit 1: 11 FILE lines (six for 2026-10-20, five for 2026-10-19, all status 200 with byte counts), 'DAY 2026-10-19 result=budget secs=471', 'ERROR: backfill run did not finish: TargetClosedError', 'CLOSE ok secs=0', stop=none, six FILETYPE lines days=0 bytes=0 earliest=none; verbatim in the deliverable NFRA_FIDUPL.TO-FT-s-11.backfill_probe1_step3D_output.md",
        "s3://opal-data-assets/fidelity/alongside/bronze/_runs/20261021/backfill-20261021T082217Z.json (2525 bytes): run_error TargetClosedError, stop {none, none}, days [2026-10-21 empty, files all 'empty listing'; 2026-10-20 completed 31 s, six files ok, missing none; 2026-10-19 budget 471 s, no files list], per_file_type earliest_served 20261020 and served_days 1 for all six, days 0 bytes 0, earliest_date null",
        "fidupl_round_checks.py ft11r: R1-FT11R-FAIL run_error=TargetClosedError; aws s3api list-objects-v2 under fidelity/alongside/bronze/ excluding _runs/ from 08:20Z: 0 keys",
        "row NFRA_FIDUPL-D1-S16 (step 3C): the same 2026-10-19 day stalled on one download in the previous run (452 s), and the same TargetClosedError followed the budget"
      ]
    },
    "spec_asserts": "Step 3D: the run reads each download inside the browser with a 120 s idle bound, lands a partly served day's files, retries the missing files once at the end and writes the record after every day; FT-s-11-AC1 expects a record with no run error and a stop reason.",
    "world_is": "The 120 s idle bound did not end the stalled 2026-10-19 download before the 480 s wall budget (the day took 471 s), so the budget ended the day before the partly served files were landed or the missing one retried; nothing was landed. The channel serves 2026-10-20 and five of six files of 2026-10-19; the sixth file of 2026-10-19 is the stall (not named in the output). The run closed its session (CLOSE ok) and then raised TargetClosedError, which hides the budget stop in the record.",
    "notes": "Not retried (a stall or budget stop is an answer per the issuer) and no cookie or profile touched. For the issuer: (1) the stall point is one file of one day, repeated in two runs, so a per-file bound below the wall budget would let the other five land; (2) the record should say stop=budget and name the stalled file; (3) the earliest-date answer for deliverable 2 so far is 2026-10-20 fully served (earliest_served) and 2026-10-19 five of six. Sign-ins in the trailing hour ending 08:22Z: 07:22Z mine, 07:49Z the issuer's refused attempt, 08:22Z this run."
  },
  {
    "id": "NFRA_FIDUPL-D1-S18",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~NFRA1",
    "surfaced_at": "2026-10-21T09:10:00Z",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "class": "BLOCKING",
    "one_line": "The step 3E backfill landed four files of the 2026-10-19 export for the first time (balance, position, prices, security, keys under content date 20261016), but transact.txt of 2026-10-19 ran to the wall budget despite the 90 s cap, account.txt was served and not landed, the record dates read 20261019 against keys at 20261016, and the record again ends TargetClosedError with stop none.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM f26b9129-0448-419c-8838-4515ce3da500 on i-028e830f7226cc685 at 08:56:14Z (the issuer's GO 9038 and update 9040, ONE attempt, --max-seconds 480 --max-sessions 8, executionTimeout 660), Success, exit 1: 'FILE_LANDED 2026-10-19 files=4', 'DAY 2026-10-19 result=budget secs=461', 'ERROR: backfill run did not finish: TargetClosedError', 'CLOSE ok secs=0', stop=none; verbatim in the deliverable NFRA_FIDUPL.TO-FT-s-11.backfill_probe1_step3E_output.md",
        "s3://opal-data-assets/fidelity/alongside/bronze/_runs/20261021/backfill-20261021T085615Z.json (2871 bytes): day 2026-10-19 files account/balance/position/prices/security 'ok', transact 'interrupted_WallBudget', landed_on_stop 4, missing ['transact.txt'], secs 461; per_file_type balance/position/prices/security earliest_date 20261019 days 1 with bytes 1223747/30326543/645722/655578, account and transact days 0 bytes 0 earliest_served 20261020; run_error TargetClosedError, stop none",
        "aws s3api list-objects-v2 under fidelity/alongside/bronze/ excluding _runs/ from 08:50Z: exactly four keys, balance/20261016/balance.txt, position/20261016/position.txt, prices/20261016/prices.txt, security/20261016/security.txt, all 09:05:17Z; run records _runs/20261019/run-20261021T085734Z.json and _runs/20261017/run-20261021T090516Z.json",
        "fidupl_round_checks.py ft11r: R1-FT11R-FAIL run_error=TargetClosedError",
        "rows NFRA_FIDUPL-D1-S16 and D1-S17: the same 2026-10-19 day stalled on its last file in the two earlier runs (452 s, 471 s)"
      ]
    },
    "spec_asserts": "Step 3E and msg 9038: a stalled file is cut at 90 s and named missing, the day lands its served files, and the walk goes on to earlier days (2026-10-16 and before); FT-s-11-AC1 expects a record with no run error and a stop reason.",
    "world_is": "The day landed its served files on stop (four) but the 90 s cap did not end the transact.txt request: the day ran 461 s, so the walk never moved to an earlier day. Three discrepancies sit in the output and are not resolved here: (1) account.txt of 2026-10-19 reads ok in the record but is not among the four landed keys; (2) the four landed keys are under content date 20261016 while the record's earliest_date for them is 20261019 and a run record sits under _runs/20261017/; (3) stop is none and run_error is TargetClosedError although the day result is budget.",
    "notes": "Not retried (a stall or budget stop is an answer per the issuer) and no cookie or profile touched. For the issuer: the earliest date the channel served is 2026-10-19 (five of six files) and the first landed content date is 20261016; the open acts are the transact.txt stall, the account.txt non-landing and the stop reason. Sign-ins in the trailing hour ending 08:56Z: 08:22Z and 08:56Z, both mine."
  },
  {
    "id": "NFRA_FIDUPL-D1-W6-S6",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~6",
    "surfaced_at": "2026-10-21T05:02:00Z",
    "one_line": "gswitch.GSwitcher raises GSwitchError with fixed text and no HTTP status on any non-200 change-form read or G switch answer, so the g_export_probe 401/403 stop cannot be applied to those requests; a refused switch is followed by the next ordinal's switch POST.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~P1 (owns whether a switch refusal must end the live probe; the order's stop-on-ANY-request cannot be met for switch and form reads without a gswitch change, which this worker may not make; the live run is not ordered from this worktree until ruled)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/gswitch.py@83a888fca62 lines 76-79: read_form raises GSwitchError('read_form: change form refused') when the status is not 200; the status is not carried",
        "infra/aws/ec2/canonical-fidelity/gswitch.py@83a888fca62 lines 82-89: switch raises GSwitchError('switch: answer refused') when the status is not 200 and GSwitchError('switch: current cell did not match ...') on a mismatch; no status is carried in either exception",
        "infra/aws/ec2/canonical-fidelity/box/g_export_probe.py (worker worktree wk-NFRA_FIDUPL-6, uncommitted at filing): _one_ordinal emits 'switched=error=<class name>' and goes on to the next ordinal, as TO-FT-s-10 names; the stop applies to the status and download answers, which carry their status",
        "org/missions/D8/NFRA/NFRA_FIDUPL/task-orders/NFRA_FIDUPL.TO-FT-s-10.g-export-probe.md: 'A status 401 or 403 on ANY request ends the probe at once'"
      ]
    },
    "spec_asserts": "TO-FT-s-10 WHAT TO BUILD item 2: a status 401 or 403 on ANY request emits 'PROBE stop: HTTP <s>' and ends the probe at once; the finally then skips the restore switch.",
    "world_is": "On a 401 or 403 answer to a change-form read or a G switch the probe cannot see the status. A refused switch emits switched=error=GSwitchError and the probe sends the next ordinal's switch POST, up to three more before the restore; a refused form read ends the probe through the ERROR line. The 401/403 stop therefore holds for the status list and the download only.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not fixed in this cell: the order bars editing gswitch.py. For the issuer before the live run (TO-FT-s-8, CTO msg 8990): either gswitch returns the status with its GSwitchError, or a refused switch stops the probe. Nothing is run live from this worktree."
  },
  {
    "id": "NFRA_FIDUPL-D1-W6-S7",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~6",
    "surfaced_at": "2026-10-21T05:02:00Z",
    "one_line": "TO-FT-s-10 does not fix the row scope of profiles, requests and ids_sha8, nor the line-break rule of rows and line1_sha8, so the probe chose all status rows and bytes.splitlines(); the issuer must confirm these before comparing its 5009-row file.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/NFRA/NFRA_FIDUPL/task-orders/NFRA_FIDUPL.TO-FT-s-10.g-export-probe.md: 'profiles=<distinct profileId count> requests=<distinct requestId count> ids_sha8=<... sha1 of the sorted requestIds ...>' names no row scope; 'line1_sha8=<... sha256 of the first line's bytes>' names no line-break rule",
        "infra/aws/ec2/canonical-fidelity/box/g_export_probe.py (worker worktree wk-NFRA_FIDUPL-6, uncommitted at filing): module docstring 'Hash definitions' and _status_facts / _account_facts"
      ]
    },
    "spec_asserts": "TO-FT-s-10 WHAT TO BUILD item 2: the counts and hashes let the issuer compare the probe's output with the 5009-row file already landed.",
    "world_is": "The order does not define the scope or the line-break rule, so a count or hash computed over a different scope or rule will not match the issuer's figure even when the bytes are the same.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Chosen: profiles, requests and ids_sha8 over every dict row of a 200 status list; rows and line1_sha8 over bytes.splitlines() (CR, LF and CRLF), line1 empty when there is no line. The definitions are printed in the module docstring; the issuer confirms before comparing."
  },
  {
    "id": "NFRA_FIDUPL-D1-W8-S11",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~8",
    "surfaced_at": "2026-10-21T06:15:36Z",
    "one_line": "REPAIR 3 premise fails: the walk makes two non-skipped wait jobs per trading day (one per planner kind), so a DAY line printed per job would give two lines per day and reach the 130-entry days cap after 65 trading days.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/backfill.py@8bd0df7fd84 _walk_kind: for each window of plan_windows(today, cap_date, chunk_days) it calls client.request_export and client.wait for the one kind passed in",
        "infra/aws/ec2/canonical-fidelity/backfill_run.py@8bd0df7fd84 _walk_g: 'for kind in kinds: bf.backfill_g(walk, target[\"g\"], (kind,), top, ...)' walks the same days once per kind (KINDS = transactions, positions_balances)",
        "org/missions/D8/NFRA/NFRA_FIDUPL/task-orders/NFRA_FIDUPL.TO-FT-s-7.backfill-adapter-and-main.md REPAIR 3 item 2: 'prints ... when the job is NOT skipped' under the heading 'One line per trading day', and 'at most 130 entries'"
      ]
    },
    "spec_asserts": "TO-FT-s-7 REPAIR 3 item 2: _StopTap.wait prints one DAY line per trading day when the job is not skipped, and the record's days list holds at most 130 entries, one per trading day.",
    "world_is": "The planner calls wait once per kind for each trading day, so two non-skipped jobs reach the tap per day. A line per job would print each day twice and double the days list.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Resolved in worker commit 06cc1128b87 (wk-NFRA_FIDUPL-8): one DAY line and one days entry per trading day; the first wait of a day is its answer and a repeat wait, answered from the adapter's day cache, adds nothing. Skipped non-trading days print nothing and are not listed. The issuer confirms this reading before the next live run."
  },
  {
    "id": "NFRA_FIDUPL-D1-W2-S12",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~2",
    "surfaced_at": "2026-10-21T09:19:06Z",
    "one_line": "The order text says FU4-AC1 needs fourteen named tests, but the checker's fu4 list as committed names fifteen; the fu4 run reads passed=16 and passes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py@7ac44b0bf3c TEST_FILES fu4 list (lines 171-179) lists 15 test names: the REPAIR 1 fourteen with test_non_trading_day_is_failure absent and two REPAIR 2 names present",
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu4 at f4289cfcb83 (worktree) printed R1-FU4-OK passed=16 rc=0"
      ]
    },
    "spec_asserts": "TO-FU-s-4 REPAIR 2: FU4-AC1 (fu4) now needs the list as the checker prints it (fourteen names, test_non_trading_day_is_failure gone, two new).",
    "world_is": "The checker's fu4 list holds fifteen names: the fourteen of REPAIR 1 with test_non_trading_day_is_failure replaced by two names. The check's bar is passed >= names, so it reads OK with the fifteen names present.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No edit: the checker is the COO's and outside this order's grant. The count in the order text is the only disagreement; the check passes on the names it lists."
  },
  {
    "id": "NFRA_FIDUPL-D1-W2-S13",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~2",
    "surfaced_at": "2026-10-21T09:19:06Z",
    "one_line": "split.py's refusal text for an unreadable as-of still says first field of the first row, although the as-of has been read from the per-file DATE_COLUMN since REPAIR 1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/split.py@7ac44b0bf3c line 179: failures.append((name, 'date', 'first field of the first row is not an 8-digit YYYYMMDD date'))",
        "infra/aws/ec2/canonical-fidelity/land.py@7ac44b0bf3c lines 102-107: _content_date reads DATE_COLUMN.get(name, 0) of the first row (REPAIR 1 per-file column)"
      ]
    },
    "spec_asserts": "TO-FU-s-4 REPAIR 2 item 3: split.py changes only where it takes the content date of a file; nothing else changes.",
    "world_is": "The text names field 0 of the first row, the rule REPAIR 1 replaced. It is left as written because the order names nothing else in split.py to change; the same rule holds for the new landing_date line at f4289cfcb83.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not edited (outside the REPAIR 2 change). The issuer decides whether the text is corrected in a later repair."
  },
  {
    "id": "NFRA_FIDUPL-D1-W2-S14",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~2",
    "surfaced_at": "2026-10-21T09:19:06Z",
    "one_line": "The run record's calendar.trading_day reads the first dated file's as-of flag, so a run that lands every file under Friday with a Saturday account as-of reads trading_day false beside outcome ALL_LANDED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/land.py@f4289cfcb83 record: 'calendar': {'trading_day': dated[0]['trading_day'] ...} with account.txt first of SIX",
        "infra/aws/ec2/canonical-fidelity/tests/test_land.py@f4289cfcb83 test_run_record_carries_both_dates_per_file asserts calendar.trading_day is False and outcome ALL_LANDED for the same run"
      ]
    },
    "spec_asserts": "TO-FU-s-4 REPAIR 2 item 2: calendar.note compares the content_date values; nothing else about the record changes.",
    "world_is": "calendar.trading_day is unchanged and reports the as-of flag of the first dated file. In the live case that file is account.txt with a Saturday as-of, so the record-level flag reads false on a run whose six files all landed under Friday 2026-10-16. Per-file content_as_of keeps the as-of visible.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Kept as the order says (nothing else about the record changes). The issuer decides whether calendar.trading_day should read the landing day's flag in a later repair."
  },
  {
    "id": "NFRA_FIDUPL-D1-W2-S15",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~2",
    "surfaced_at": "2026-10-21T09:19:06Z",
    "one_line": "A CalendarCoverageError now leaves content_date null (no landing date can be computed), where the lander carried the as-of, and split.py records a calendar failure instead of raising.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-fidelity/land.py@7ac44b0bf3c _examine set content_date from the as-of before the calendar try block; @f4289cfcb83 the try block computes is_trading_day and landing_date, and a coverage error returns a calendar failure with content_date unset",
        "infra/aws/ec2/canonical-fidelity/split.py@f4289cfcb83 split_day wraps landing_date in try/except CalendarCoverageError and appends (name, 'calendar', ...); split.py@7ac44b0bf3c had no calendar call"
      ]
    },
    "spec_asserts": "TO-FU-s-4 REPAIR 2 item 1: the fail-closed CalendarCoverageError still propagates as today (the existing calendar failure step stays); content_date is the landing date.",
    "world_is": "No landing date exists when the calendar cannot answer, so the coverage path carries content_as_of and a null content_date, and the business date falls to the next dated file. split.py had no calendar call, so the new except is an addition the order did not name. No test pins the coverage path (the fallback covers 2010-2027).",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Chosen to fail closed without a guessed date. The issuer confirms this reading; the coverage path is not exercised by any criterion."
  },
  {
    "id": "NFRA_FIDUPL-D1-W2-S16",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~2",
    "surfaced_at": "2026-10-21T09:19:06Z",
    "one_line": "The order's status flip to complete sits in the TO file, which is outside this order's paths block, so this worker leaves the order at pending.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/NFRA/NFRA_FIDUPL/task-orders/NFRA_FIDUPL.TO-FU-s-4.lander-and-run-record.md@7ac44b0bf3c <paths> block names land.py, tests/test_land.py, split.py, tests/test_split.py and the investigation file only",
        "the same order's REPAIR 2 text: flip the order's status to complete only when both criteria PASS"
      ]
    },
    "spec_asserts": "TO-FU-s-4 REPAIR 2 closing line: flip the order's status to complete only when both criteria PASS.",
    "world_is": "Both criteria PASS by output at f4289cfcb83 (fu4 passed=16, fu4d dests=6). The status line lives in a file outside the grant, so the lane gate admits no flip from this worker; the order stays pending in the worktree.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The issuer flips the status, as on REPAIR 1 (row NFRA_FIDUPL-D1-W2-S6). Disarm is not an ARMED hazard: the row is INERT."
  },
  {
    "id": "NFRA_FIDUPL-D1-W2-S17",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~2",
    "surfaced_at": "2026-10-21T09:19:06Z",
    "one_line": "safe-commit printed a naming-gate NAMING ERROR (function-map folder missing in this worktree) on the REPAIR 2 commit; the commit still returned rc 0.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bash .tools/safe-commit.sh ... -F .scratch/msg_code.txt -- (4 paths) at worktree C:/tmp/fidupl-w2, output line: [naming-gate] NAMING ERROR function-map folder missing: C:\\tmp\\fidupl-w2\\infra/aws/lambda/ci/function-map/",
        "the same output: [wk-NFRA_FIDUPL-2 f4289cfcb83] committed, 4 files changed, and [msg-verify] MATCH"
      ]
    },
    "spec_asserts": "Worker face: every commit goes through safe-commit.sh, and its gates run clean for the paths committed.",
    "world_is": "The naming gate reported the Lambda function-map folder absent from this worktree and printed a NAMING ERROR; nothing in this order's paths reads that folder, and the commit completed.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not investigated further (off-task). The owner of the naming gate's folder in a worktree decides whether the message is expected."
  },
  {
    "id": "NFRA_FIDUPL-D1-W6-S8",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~6",
    "surfaced_at": "2026-10-21T14:38:29Z",
    "one_line": "The worktree C:/tmp/fidupl-w6 is a sparse checkout that omits org/surprise_channel/: the directory is absent on disk, its schema is readable only from the HEAD tree, and the worker could not read the channel's schema from its own tree.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git config --get core.sparseCheckout in C:/tmp/fidupl-w6 printed true (2026-10-21T14:38Z); git sparse-checkout list printed 10 cone entries",
        "ls org/surprise_channel in C:/tmp/fidupl-w6 printed: No such file or directory; git ls-files org/surprise_channel listed 43 tracked files",
        "git show HEAD:org/surprise_channel/schemas/investigation_item.schema.json parsed as JSON; its required fields are id, surfaced_by, surfaced_at, one_line, class, grounding, disposition"
      ]
    },
    "spec_asserts": "Worker face: the worktree carries the paths the task order names, and the rules named in it (the schema at org/surprise_channel/schemas/) are readable from the worktree.",
    "world_is": "The worktree is a sparse checkout (core.sparseCheckout=true, 10 cone entries). org/surprise_channel/ is tracked at HEAD but absent on disk, so the schema was read from the HEAD tree. The task order's own paths are present on disk.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not investigated further (off-task). The owner of the worktree cone decides whether the channel belongs in worker cones; this row only records the observed state."
  },
  {
    "id": "NFRA_FIDUPL-D1-W6-S9",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~6",
    "surfaced_at": "2026-10-21T14:38:29Z",
    "one_line": "The pre-commit risk reflex answered PARTIAL_OR_BLIND on the FV-s-1 lander commit (danger map 45.3h old, 0 of 2 files scanned), and the commit went through with the reflex undecided.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bash .tools/safe-commit.sh ... -F .scratch/msg_fvs1_code.txt -- infra/aws/ec2/canonical-fidelity/land.py infra/aws/ec2/canonical-fidelity/tests/test_land_psn.py (commit f76f55946d3) printed [risk-reflex] ANSWER STATE: PARTIAL_OR_BLIND and danger map: 45.3h old STALE",
        "the same output printed WITHIN BUDGET: scanned 0 of 2 file(s) and NOT-DECIDABLE: danger map STALE -- the reflex CANNOT clear this diff",
        "the commit then printed [wk-NFRA_FIDUPL-6 f76f55946d3] committed with 2 files changed"
      ]
    },
    "spec_asserts": "Worker face: the pre-commit gate clears the commit as checked clean, or the reflex states what it could not decide.",
    "world_is": "On a sparse worktree the danger map is read from the main tree's map (C:/Dev/ajb_workspace/org/modules/graph/nerves-risk-edges.json) and was 45.3h old; the reflex scanned none of the two files and the commit completed on an undecided reflex.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not investigated further (off-task). The lander diff is synthetic-fixture code with no cloud or infra change. The owner of the danger map's refresh decides whether a stale map is a standing gap."
  },
  {
    "id": "NFRA_FIDUPL-D1-W6-S10",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~6",
    "surfaced_at": "2026-10-21T14:38:29Z",
    "one_line": "The client-data check did not run on the FV-s-1 lander commit: the hashed account-id list is absent on this box, so the commit was not checked for client account ids, and every later commit on this box is unchecked until the list is placed.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~P1 (issuer; routes the placement of the box's hashed account-id list to its owner -- this seat does not hold that list and does not know its owner)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bash .tools/safe-commit.sh (commit f76f55946d3) printed: WARN: client-data-check: hashed account-id list ABSENT at C:\\Users\\Test\\.opal\\account_id_hashes.txt -- this commit was NOT checked for client account ids",
        "ls C:/Users/Test/.opal/account_id_hashes.txt printed: No such file or directory",
        "the commit's two paths hold synthetic fixtures written by this worker; no real export was read"
      ]
    },
    "spec_asserts": "Commit gate: the client account-id check runs on every commit on this box, against the hashed account-id list that the box is given.",
    "world_is": "The hashed account-id list is absent on dell1 (C:/Users/Test/.opal/account_id_hashes.txt), so the client-data check prints WARN and checks nothing; the gate output says absent is not empty.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Armed because the gap persists into every future commit on this box while the list is absent. The disarm owner routes the list; this seat only surfaces it."
  },
  {
    "id": "NFRA_FIDUPL-D1-W6-S11",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~6",
    "surfaced_at": "2026-10-21T14:38:29Z",
    "one_line": "The naming gate printed NAMING ERROR function-map folder missing on the FV-s-1 lander commit, and the commit returned rc 0; the same mechanism as NFRA_FIDUPL-D1-W2-S17, here caused by the sparse cone that omits the folder.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bash .tools/safe-commit.sh (commit f76f55946d3) printed: [naming-gate] NAMING ERROR function-map folder missing: C:\\tmp\\fidupl-w6\\infra/aws/lambda/ci/function-map/",
        "git ls-tree -r --name-only HEAD infra/aws/lambda/ci/function-map printed 243 tracked files; ls -d infra/aws/lambda/ci/function-map printed No such file or directory",
        "the same output printed [wk-NFRA_FIDUPL-6 f76f55946d3] committed and [msg-verify] MATCH"
      ]
    },
    "spec_asserts": "Worker face: every commit goes through safe-commit.sh, and its gates run clean for the paths committed.",
    "world_is": "The naming gate reads the Lambda function-map folder, which is tracked at HEAD (243 files) but absent on disk in this sparse worktree; nothing in this order's paths reads that folder, and the commit completed.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not investigated further (off-task). A repeat of NFRA_FIDUPL-D1-W2-S17 with a sparse-cone cause (see NFRA_FIDUPL-D1-W6-S8). The owner of the naming gate decides whether the message is expected in a sparse worktree."
  },
  {
    "id": "NFRA_FIDUPL-D1-W6-S12",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~6",
    "surfaced_at": "2026-10-21T15:01:21Z",
    "one_line": "The FV-s-2 task order names LongRequestSession as a symbol to import from backfill_main.py, but that class is defined inside backfill_main._real_deps (a closure), so it cannot be imported; hist_walk reaches it only through the open/fetch session deps that _real_deps returns.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "grep of C:/tmp/fidupl-w6/infra/aws/ec2/canonical-fidelity for LongRequestSession printed only backfill_main.py:745 (class LongRequestSession(fetch.PlaywrightSession), indented inside def _real_deps at line 728)",
        "backfill_main.py module-level definitions (grep ^def|^class) list no LongRequestSession; _real_deps returns fetch_session as a closure over LongRequestSession (line 819-820)"
      ]
    },
    "spec_asserts": "FV-s-2 worker face, Read first: backfill_main.py (main, _real_deps and its LongRequestSession ... you IMPORT from it and do not edit it).",
    "world_is": "LongRequestSession is a nested class of _real_deps; it has no module-level name to import. The walk takes the same behaviour through backfill_main._real_deps()['fetch_session'], which is what hist_walk does.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not investigated further (off-task). hist_walk imports backfill_main and calls its _real_deps; no edit to backfill_main was needed. The order's wording is the only mismatch."
  },
  {
    "id": "NFRA_FIDUPL-D1-W6-S13",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~6",
    "surfaced_at": "2026-10-21T15:01:21Z",
    "one_line": "land.land writes one run record per call, and a day folder holding only position.txt and prices.txt makes it record the four absent SIX names as failed read entries, so each walked day writes a PARTIAL run record under _runs even though both files land.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "land.py _examine: a file not present in the handoff directory yields _fail(entry, 'read', None, 'file absent from the handoff directory') (land.py, the _examine function)",
        "land.py land(): outcome is ALL_LANDED only when every entry is in OK_ACTIONS, PARTIAL when some landed and some failed; the record is put to _runs on every non-dry call",
        "hist_walk.py _settle reads the per-file entry for position.txt and prices.txt, so the day result is LANDED for both; the run-level PARTIAL is not read"
      ]
    },
    "spec_asserts": "FV-s-2 WHAT TO BUILD item 4: the position and prices files land through land(folder, scope) after a listing.json whose missing names are the SIX names not present; the lander is called unchanged.",
    "world_is": "The walk's per-day land() call writes a PARTIAL run record for each day that has only two of the six files; the per-file results are correct, the run records carry four read failures per day.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not investigated further (off-task). The spec is followed as written. Whether a two-file run record belongs under _runs is an owner decision (the lander's run-record design), not this seat's."
  },
  {
    "id": "NFRA_FIDUPL-D1-W7-S7",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~7",
    "surfaced_at": "2026-10-21T16:47:59Z",
    "one_line": "The walk sends each account as the string read from the book, in accountNumber and in accountNumbers; the order does not say whether the API takes a JSON string or a JSON number.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "api_walk.py book_from_bytes returns str values; _tx_body and the realized and open bodies send them unchanged (worktree C:/tmp/fidupl-w7, uncommitted at filing)",
        "TO NFRA_FIDUPL.TO-FW-s-1 WORKER FACE measured facts: the transactions body names accountNumber as <n>, the realized body names accountNumbers as [<n>] (7402cd0e3e1)"
      ]
    },
    "spec_asserts": "TO FW-s-1 measured facts: the transactions body is {\"accounts\": [{\"accountNumber\": <n>, ...}]} and the realized body is {\"accountNumbers\": [<n>]}; <n> is not typed as a string or a number.",
    "world_is": "The book is read as CSV text (latin-1), so every account is a string. The live type the API accepts is not among the measured facts. A type mismatch would answer a non-200 on the first call, recorded ERROR per account.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Built on fakes only, so not verified live. The issuer confirms the accepted type before TO-FW-s-2 runs. The walk does not convert the value."
  },
  {
    "id": "NFRA_FIDUPL-D1-W7-S8",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~7",
    "surfaced_at": "2026-10-21T16:47:59Z",
    "one_line": "The ten-window transactions cap (3,650 days) ends an account with older history as ERROR on every run, against the cell's 'as far back as the API serves'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "api_walk.py MAX_WINDOWS = 10 and _tx_account raises AccountError at the cap; WINDOW_STEP_DAYS = 365 (worktree C:/tmp/fidupl-w7, uncommitted at filing)",
        "TO NFRA_FIDUPL.TO-FW-s-1 THE CELL ('as far back as the API serves') and WHAT TO BUILD item 4 ('At most 10 windows per account') (7402cd0e3e1)"
      ]
    },
    "spec_asserts": "TO FW-s-1 THE CELL: every fact table 'as far back as the API serves'. WHAT TO BUILD item 4: 'At most 10 windows per account (a safety stop recorded ERROR)'.",
    "world_is": "Ten windows of 365 days reach about ten years back. An account whose rows go further back is recorded ERROR at the tenth window. The retry on the next run reads the same windows from head, reaches the cap again, and the account ends ERROR with attempts 2, so its older history is never landed. The order does not say which bound governs.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Built as written (cap 10). The issuer decides whether the cap rises, or the realized-style split applies to transactions, before TO-FW-s-2."
  },
  {
    "id": "NFRA_FIDUPL-D1-W7-S9",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~7",
    "surfaced_at": "2026-10-21T16:47:59Z",
    "one_line": "A one-day transactions window that answers 2,000 rows or more cannot be split, and the order does not say what lands for it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "api_walk.py _tx_window: an answer with n >= ROW_CAP on a one-day window sets out['incomplete'] and lands the answer as it is (worktree C:/tmp/fidupl-w7, uncommitted at filing)",
        "TO NFRA_FIDUPL.TO-FW-s-1 WHAT TO BUILD item 4: the split 'recursively down to one day' names no rule at the one-day cap (7402cd0e3e1)"
      ]
    },
    "spec_asserts": "TO FW-s-1 item 4: 'If a window answer holds 2,000 rows or more, split that window in two halves (whole days) and request each half instead of landing the capped answer, recursively down to one day.' No rule for a one-day answer at the cap.",
    "world_is": "The walk lands the capped one-day answer as it is and marks the account INCOMPLETE. The rows past the cap for that day are not reachable by the window split.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Built as an INCOMPLETE leaf, mirroring the realized one-day short answer. Not confirmed by the issuer."
  },
  {
    "id": "NFRA_FIDUPL-D1-W7-S10",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~7",
    "surfaced_at": "2026-10-21T16:47:59Z",
    "one_line": "A run that walks every selected surface once while an ERROR account still awaits its retry ends with the stop reason 'surface_end', which the order does not name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "api_walk.py _walk raises Halt('surface_end') when an account is unfinished and Halt('all_done') when none is (worktree C:/tmp/fidupl-w7, uncommitted at filing)",
        "TO NFRA_FIDUPL.TO-FW-s-1 WHAT TO BUILD item 7 lists the stops auth, throttled, budget, terminated, error, all_done and account_cap; item 9 names 'test_wall_budget_and_surface_end_the_run_with_a_named_stop' (7402cd0e3e1)"
      ]
    },
    "spec_asserts": "TO FW-s-1 item 7 names the stops auth, throttled, budget, terminated, error, all_done and account_cap. Item 9 names a test 'test_wall_budget_and_surface_end_the_run_with_a_named_stop' but no reason for the surface end.",
    "world_is": "The run ends 'surface_end' when every selected surface has been walked once and at least one account is unfinished (ERROR with attempts 1). 'all_done' is used only when no account is unfinished.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The name is the implementer's. The issuer confirms or renames it."
  },
  {
    "id": "NFRA_FIDUPL-D1-W7-S11",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~7",
    "surfaced_at": "2026-10-21T16:47:59Z",
    "one_line": "The state entries carry rows and attempts, and an in-progress account is saved with result null, beyond the order's {result, earliest}.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "api_walk.py _one_account writes {result, earliest, rows, attempts} and an in-progress entry with result None before the account is walked (worktree C:/tmp/fidupl-w7, uncommitted at filing)",
        "api_walk.py _real_deps and the deps list carry no body read (accounts, head, put, put_record only), so windows that already exist cannot be re-read for their dates (worktree)",
        "TO NFRA_FIDUPL.TO-FW-s-1 WHAT TO BUILD item 2: 'a map account -> {\"result\": ..., \"earliest\": ...}' and 'record attempts' (7402cd0e3e1)"
      ]
    },
    "spec_asserts": "TO FW-s-1 item 2: per surface, a map account -> {result, earliest}. An ERROR account is retried once on the NEXT run only and records attempts.",
    "world_is": "Each entry also carries rows and attempts. An account in progress is saved with result null, so an interrupted walk keeps its earliest date and row count across runs. Windows that already exist cannot be read again (no body read in deps), so their dates are known only from the saved state. A SIGKILL between saves loses the in-progress values; the auth, throttle, budget and SIGTERM stops save the state first.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The extra keys serve the record's counts and the earliest content date. The issuer confirms the entry shape."
  },
  {
    "id": "NFRA_FIDUPL-D1-W7-S12",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~7",
    "surfaced_at": "2026-10-21T16:47:59Z",
    "one_line": "The order gives no metadata for an open-lots object; the walk writes sha256, rows and total.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "api_walk.py _open_account passes meta {total} to _put, which adds sha256 and rows (worktree C:/tmp/fidupl-w7, uncommitted at filing)",
        "TO NFRA_FIDUPL.TO-FW-s-1 WHAT TO BUILD item 6 names the open-lots key and the DONE and INCOMPLETE rule but no metadata (7402cd0e3e1)"
      ]
    },
    "spec_asserts": "TO FW-s-1 item 4 gives transactions metadata {sha256, rows, from, to}. Item 5 gives realized 'the same body rule and metadata' with total. Item 6 gives no metadata for the open-lots object.",
    "world_is": "Open-lots objects carry {sha256, rows, total}. The total is the answer's totalCount, which the INCOMPLETE flag depends on.",
    "disposition": "UNDER_INVESTIGATION",
    "notes": "total is the only key added beyond the realized pattern. The issuer confirms it."
  }
]
```
