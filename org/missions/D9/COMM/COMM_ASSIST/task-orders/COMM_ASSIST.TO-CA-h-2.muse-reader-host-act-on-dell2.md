# TO COMM_ASSIST.TO-CA-h-2 -- round 16 CA-h-2: host the muse reader folder on dell2 (install, schedule, identity read-back, SSH key list; FWD-6, FWD-11)

<to_id>COMM_ASSIST.TO-CA-h-2</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.7.0_AE_CloudOps~CA2</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>DELL2HOST</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-h-2` (`decompositions/COMM_ASSIST_DECOMP.round16.md`) | **outcome_ref:** FWD-6, FWD-11 |
**depends_on:** CA-h-1 (merged @bfaa09da63); NFRA_CTLPLN TO-CT-ab-2 admin-group apply (COMPLETE, COO~C msg 108903, commits 8ef2c65918 and 84fbeec988). Addressed by crossbox ORDER to device dell2; the lane `0.7.0_AE_CloudOps~CA2` is seated by `1.0.0_SA_CTO~DELL2` (msg 7135).

---

## SEAT FACE (read in full; this order is your whole context)

### THE CELL

Andrew will read "what is waiting on me?" from a folder on dell2, over SSH, from a tailnet VM called muse that has NO cloud access. A refresh
script (built and merged: `data/transcripts/scripts/muse_reader/refresh.py`, `README.txt` it writes) reads AWS read-only and writes four JSON
files, `INDEX.json` and `README.txt`. You host it on THIS box (dell2): put it where the dell2 account can run it, schedule it on dell2's own
clock, and prove it runs under dell2's own AWS identity. You install nothing else, build nothing, and change no policy, no key and no
firewall rule. FWD-7 (Andrew's signed ANSWER path) is NOT this order: no `answers/` folder, no forwarder, no SQS send.

### DO, IN THIS ORDER

1. **Pin.** In the dell2 checkout run `git merge-base --is-ancestor bfaa09da63 HEAD`. If it is not an ancestor, run this box's normal sync
   (`.tools/box-sync.sh`) once and test again. Still not: stop and file a BLOCKING row with both outputs. Do not cherry-pick.
2. **Identity read-back FIRST.** Run `python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r16/checks/check_h2_identity.py"`
   from the repository root. It must print `ok=True` BEFORE anything is installed. If it prints `ok=False`, stop and file a BLOCKING row with
   the line: the admin-group apply has not reached this user, and nothing below is yours to fix.
3. **Tools.** Measure and report (do not install anything not already present): `python --version`, `aws --version`, `ssh-keygen -V`. If
   python or the AWS CLI is missing, file a BLOCKING row naming which and stop: installing a runtime is a separate act.
4. **Folder and task.** The folder is `%USERPROFILE%\muse-reader` for the user the task runs as (the checks read `MUSE_READER_ROOT`, else
   `<home>\muse-reader`). Run the script once by hand to create it:
   `python data/transcripts/scripts/muse_reader/refresh.py --root "%USERPROFILE%\muse-reader"`. Then register ONE Windows scheduled task named
   `MuseReaderRefresh`, every 15 minutes, no end date, run as the same user, whether or not logged on if the box allows it, executing the same
   command from the repository root. Register it with `Register-ScheduledTask` (or `schtasks`); record the exact registration command in your
   report. Start it once with `Start-ScheduledTask -TaskName MuseReaderRefresh` and wait for it to finish.
5. **SSH read.** Run `check_h2_ssh.py` (same folder as AC1) from the repository root. It lists the SHA256 fingerprints of the keys this box
   accepts, so the issuer can compare them with muse's key (row COMM_ASSIST-S3: no repo file holds muse's key, and NFRA_CTLPLN round 12 does not
   read it back). You do not decide whether muse's key is among them and you do not add one.
6. **Rows and report.** Any surprise is a row `COMM_ASSIST-CA2-S<k>` appended to the investigation file; keep its line endings.

### RULES

- Edit nothing outside `<paths>` and the two dell2 things above (the folder and the one scheduled task). AWS: read calls only, under this
  box's own identity. No `put`, no `update`, no `delete`, no `apply`, no IAM change, no firewall or sshd change, no new key.
- **ROLLBACK (yours to run on the issuer's word, and the report states it):** `Unregister-ScheduledTask -TaskName MuseReaderRefresh -Confirm:$false`,
  then remove the folder `%USERPROFILE%\muse-reader`. The folder is a regenerable copy; nothing else is touched.
- Nothing in the folder may hold a key, token, header or address: the script already withholds them; do not copy any file into it by hand.
- This is not an alert, monitor or notification: the task only writes files. If you think it needs one, stop and file a row.
- A refused or unmet criterion is reported with its measurement, never repaired by widening it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAh2-AC1" cell_refs="CA-h-2"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r16/checks/check_h2_identity.py"</invocation><expect>H2-IDENTITY ok=True</expect></criterion>
`CAh2-AC1` -- the identity read-back: the running caller is a dell2 agent user and a member of `AdministratorAccessOpalCapital`. It prints ok=False at the base (a laptop caller).

<criterion id="CAh2-AC2" cell_refs="CA-h-2"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r16/checks/check_h2_scheduled.py"</invocation><expect>H2-SCHEDULED ok=True</expect></criterion>
`CAh2-AC2` -- the seam against the real neighbours: the scheduled task exists with last result 0, and the folder's `INDEX.json` was written by that task under 35 minutes ago with `drafts` and `open_calls` ok and nothing unreadable. It prints ok=False at the base.

<criterion id="CAh2-AC3" cell_refs="CA-h-2"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r16/checks/check_h2_ssh.py"</invocation><expect>H2-SSH ok=True</expect></criterion>
`CAh2-AC3` -- the box is dell2, something listens on port 22, and the key file's fingerprints are read and listed. It prints ok=False at the base.
</proof_of_spec>

<expected_criteria>CAh2-AC1,CAh2-AC2,CAh2-AC3</expected_criteria>

Each invocation runs from the repository root under `timeout 120`. Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA2/COMM_ASSIST.TO-CA-h-2.muse-reader-host-act-on-dell2.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CAh2-AC1,CAh2-AC2,CAh2-AC3` from inside the checkout, and flip `<status>` to
`complete` only when all three pass and the instance is VALID. Commit with `.tools/safe-commit.sh` under your own serial. Your final report
names: the python, AWS CLI and ssh-keygen versions, the exact scheduled-task registration command, the three output lines, the fingerprints AC3
printed, and the rollback command. Your surprise rows are `COMM_ASSIST-CA2-S<k>`.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round16.md</decomp_doc>
<owned_cells>CA-h-2</owned_cells>
</decomp_ref>

<paths>
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-h-2.muse-reader-host-act-on-dell2.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA2/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a Windows scheduled task on one dell2 account, not an EventBridge rule or Lambda trigger; the 15-minute cadence is the order's own, named in step 4 and checked by AC2's 35-minute freshness bound.
comp-iam: RUN-BY-CHECK no grant moves; AC1 reads the caller and its groups. The admin-group apply is TO-CT-ab-2 (COMPLETE, 84fbeec988); this order only reads it back.
comp-adversary: RUN -- a task that exists but never ran (refused: AC2 needs last result 0 and a fresh INDEX run_at); a folder refreshed by hand and called scheduled (refused: AC2 requires run_at within 2 minutes of the task's LastRunTime); a green run under the laptop's identity (refused: AC1 and AC3 require a dell2 caller and device); an answers folder or forwarder installed early (refused: THE CELL, FWD-7 is round 17). BLIND: whether muse's key is among AC3's fingerprints, and the off-tailnet refusal, are the issuer's reads and not graded here; the dell2 firewall scope is not read by this order.
naming: a local scheduled-task name and a user-profile folder; no S3 address, AWS resource or registry name is created (CLAUDE.md rule 30 non-application).
lane: the <paths> block IS the grant (worker RULING 1); the scheduled task and the folder are the two named dell2 writes and are not repo paths.
</preflight>

Base: CAh2-AC1 base: FAIL as expected (caller Andrew_Berman is not a dell2 user); CAh2-AC2 base: FAIL as expected (task MuseReaderRefresh not found); CAh2-AC3 base: FAIL as expected (box is laptop, not dell2).
Source: CTO direction `DIRECTION_COO_CA_COMM_ASSIST_MUSE_20261013.md` @4e963d4a12 points 4-5; ruling @2f0ed70e40 sections 1-2 and @53acd6fe5f; PRD v0.6 FWD-6, FWD-11; row COMM_ASSIST-S3; CVO grade `COMM_ASSIST-C-S1` (FWD-7's receiver-side check is round 17, outside this order).
