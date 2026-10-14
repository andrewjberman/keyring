# TO COMM_ASSIST.TO-CA-j-15 -- round 18 CA-j-15: dell2's reader job publishes mentions.json and mail_log.json (a read-only pick-up check; FWD-13)

<to_id>COMM_ASSIST.TO-CA-j-15</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.7.0_AE_CloudOps~CA2</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>DELL2PICKUP</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-j-15` (`decompositions/COMM_ASSIST_DECOMP.round18.md`, AMENDMENT 10) | **outcome_ref:** FWD-13 |
**depends_on:** CA-j-13 (merged `0ea947e32d`, already on `origin/box/dell2`). Addressed by crossbox ORDER to device dell2. It asks you to CHANGE nothing.

---

## SEAT FACE (read in full; this order is your whole context)

### THE CELL

You host the muse reader folder on dell2 (`MuseReaderRefresh`, every 15 minutes, folder `%USERPROFILE%\muse-reader`). The reader code, `data/transcripts/scripts/muse_reader/refresh.py`, now writes two more files beside the existing ones: `mentions.json` (channel @mentions of Andrew) and `mail_log.json` (the recent considered mails), both METADATA ONLY, and lists six sources in `INDEX.json`. Muse (Andrew's operator agent) will read them to alert him of new items. The assistant that WRITES the records in AWS is deployed by a separate act, so until it is, both files should read `absent` (nothing recorded yet), which is correct and honest: an absent source is never an empty list. This order asks you to confirm that your job runs the new code and that the folder is clean. You install nothing, register nothing, change no environment variable and no task.

### DO, IN THIS ORDER

1. **Precondition.** From the repository root of the dell2 checkout run `git merge-base --is-ancestor 0ea947e32d HEAD`. If it exits 0, the checkout holds the new reader. If not, run this box's normal sync (`.tools/box-sync.sh`) once and run it again. Still not: stop and file a BLOCKING row with the output.
2. **The folder BEFORE.** Run `python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_k4_folder.py"` once and save its output line in your deliverables folder (`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA2/r18/`). It will probably read `ok=False` (the last scheduled run may have happened before the checkout held the new code); that is the base measurement, not a failure. Also record the four old sources' statuses from `INDEX.json` (names and status words only).
3. **Run the existing job once.** `Start-ScheduledTask -TaskName MuseReaderRefresh`, then wait until `(Get-ScheduledTaskInfo -TaskName MuseReaderRefresh).LastTaskResult` reads 0 and `LastRunTime` is newer than your step-2 read. It is the same task, run as the same user, doing the same AWS reads (a DynamoDB scan of the assistant's state table, now read for the two new lists) plus the same writes into the folder. If its result is not 0, or any of the four old sources that read `ok` in step 2 now reads `unreadable`, STOP and report with the INDEX status words: that is a regression the issuer will revert in the repository; you change nothing.
4. **Read it back.** Run the AC1 command below once. It must print `ok=True`.
5. **The report.** The AC1 line; the task's `LastTaskResult` and `LastRunTime`; the folder's file NAMES; each source's status word before and after; and nothing else from inside the files (no item text). Any surprise is a row `COMM_ASSIST-CA2-S<k>` appended to the investigation file; keep its line endings.

### RULES

- Edit nothing: no file in the checkout, no task, no variable, no policy, no firewall or sshd setting, no key. The only act beyond reading is starting the EXISTING task once.
- AWS: read-only (the job's own reads). Do not run any write.
- This is not an alert, monitor or notification, and builds none.
- A refused or unmet criterion is reported with its measurement, never repaired by widening it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAj15-AC1" cell_refs="CA-j-15"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_k4_folder.py"</invocation><expect>K4-FOLDER ok=True</expect></criterion>
`CAj15-AC1` -- the issuer's folder check (read it; do not edit it), run ON dell2 from the repository root after step 3: `INDEX.json` lists exactly six sources including `mentions` and `mail_log`; both files exist as valid envelopes with status `ok` or `absent` (an `absent` source has null items; `unreadable` fails); the folder was written within the last 20 minutes; an `ok` source's items have exactly the contracted keys; `README.txt` names both files; and no address, key or token shaped string appears in ANY file of the folder (FWD-11). It reads ok=False before the new code has run.

<criterion id="CAj15-AC2" cell_refs="CA-j-15"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i1_ages.py"</invocation><expect>I1-AGES ok=True arms=5 of 5</expect></criterion>
`CAj15-AC2` -- the bound, a control that PASSES at the base and must still pass on dell2's checkout: the reader's ages on the existing sources.
</proof_of_spec>

<expected_criteria>CAj15-AC1,CAj15-AC2</expected_criteria>

Each invocation runs from the repository root under `timeout 200`. Write the proof instance to `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA2/COMM_ASSIST.TO-CA-j-15.dell2-publishes-the-two-new-sources.proof_of_spec.json`, pin each artifact row to the commit that carried it, validate it with `python .tools/proof-of-spec-check.py <instance> CAj15-AC1,CAj15-AC2` from inside the checkout AFTER your last commit, and flip `<status>` to `complete` only when both pass and the instance is VALID at the final head. Commit with `.tools/safe-commit.sh` under your own serial. Your surprise rows are `COMM_ASSIST-CA2-S<k>`.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round18.md</decomp_doc>
<owned_cells>CA-j-15</owned_cells>
</decomp_ref>

<paths>
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-15.dell2-publishes-the-two-new-sources.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA2/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the act creates no schedule: it starts the EXISTING task `MuseReaderRefresh` once, as the same user; its 15-minute schedule is unchanged. No cron, alarm, monitor or notification is created.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves; the new readers perform the same read-only DynamoDB scan the drafts reader already performs, with the same dell2 identity.
comp-adversary: RUN -- the new reader breaking the folder muse already reads (refused: step 3 stops on a non-zero result or an old source turning unreadable, and AC2 re-runs the ages control; the repository carried the same code through 561 passed tests and the issuer's reader checks 7 of 7, 5 of 5 and the failure-shape control); an `absent` source shown as an empty list (refused: AC1 `files` arm requires null items for absent); a secret, key or address reaching the folder (refused: AC1 `clean` arm scans every file, FWD-11, and the CVO carries the pattern-scrub limit for the record cells); the extra scan load on the state table (one more full scan per new source per 15 minutes: 671 items today; measured live, not here). BLIND: the issuer has not read dell2's folder before this order (the base is the seat's step-2 measurement), and no real @mention or considered-mail row exists yet, so `ok` rows are not exercised here (cells CA-j-14 and CA-j-16).
lane: the <paths> block IS the grant; the seat edits nothing else and installs nothing.
</preflight>

Base: CAj15-AC1 base: not measured by the issuer (dell2's folder is on dell2); expected `ok=False` until the new reader has run there (step 2 records it). CAj15-AC2 base: PASS as measured on the trunk (5 of 5). AC1's arms were proved on a generated folder: a good folder reads 6 of 6, and a missing file, a four-source INDEX, a stray address and an unreadable source each fail exactly one arm.
Source: CTO ruling on call 608c (msg 109140); muse's requested shape (Gmail thread, 2026-10-14 13:16Z); the CVO's CA-j-14 half (re-read FWD-11 when the records reach dell2); round-18 decomposition AMENDMENT 8.
