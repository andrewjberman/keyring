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
  }
]
```
