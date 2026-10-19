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
  }
]
```
