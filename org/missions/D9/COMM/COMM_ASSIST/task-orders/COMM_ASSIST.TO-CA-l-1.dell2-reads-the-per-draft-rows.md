# TO COMM_ASSIST.TO-CA-l-1 -- round 20 CA-l-1: dell2's reader publishes one drafts row per open mail draft (a read-only pick-up check; FWD-13, FWD-4)

<to_id>COMM_ASSIST.TO-CA-l-1</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.7.0_AE_CloudOps~CA2</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>DELL2PERDRAFT</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-l-1` (`decompositions/COMM_ASSIST_DECOMP.round20.md`) | **outcome_ref:** FWD-13, FWD-4 |
**depends_on:** CA-k-1 (merged `2d0a8f5027`, deployed in CA-k-4). Addressed by crossbox ORDER to device dell2. It asks you to CHANGE nothing.

---

## SEAT FACE (read in full; this order is your whole context)

### THE CELL

You host the muse reader folder on dell2 (`MuseReaderRefresh`, every 15 minutes, folder `%USERPROFILE%\muse-reader`). Since round 19 the assistant keeps a LIST of open mail drafts on its mail object (a newer considered mail adds a draft and never overwrites the older one), and the reader code, `data/transcripts/scripts/muse_reader/refresh.py`, publishes ONE row in `drafts.json` for each open draft, each with its own `seq` (a mail row is identified by `object_id` plus `seq`). Muse (Andrew's operator agent) reads that file to alert him. This order asks you to confirm that your checkout holds the new reader, that the reader's logic gives one row per open draft on the code YOU run, and that your job still writes a clean folder. You install nothing, register nothing, change no environment variable and no task.

### DO, IN THIS ORDER

1. **Precondition.** From the repository root of the dell2 checkout run `git merge-base --is-ancestor 2d0a8f5027 HEAD`. If it exits 0, the checkout holds the CA-k-1 reader. Then confirm the issuer's check exists: `test -f "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r20/checks/check_m1_perdraft.py"`. If either fails, run this box's normal sync (`.tools/box-sync.sh`) once and run both again. Still not: stop and file a BLOCKING row with the output.
2. **The folder BEFORE.** Run `python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_k4_folder.py"` once and save its output line in your deliverables folder (`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA2/r20/`). Also record each source's status word from `INDEX.json` (names and status words only).
3. **Run the existing job once.** `Start-ScheduledTask -TaskName MuseReaderRefresh`, then wait until `(Get-ScheduledTaskInfo -TaskName MuseReaderRefresh).LastTaskResult` reads 0 and `LastRunTime` is newer than your step-2 read. It is the same task, run as the same user, doing the same AWS reads (a DynamoDB scan of the assistant's state table) plus the same writes into the folder. If its result is not 0, or any source that read `ok` in step 2 now reads `unreadable`, STOP and report with the INDEX status words: that is a regression the issuer will revert in the repository; you change nothing.
4. **Read it back.** Run the three criteria below once each and read the deciding line.
5. **The report.** The three deciding lines; the task's `LastTaskResult` and `LastRunTime`; the folder's file NAMES; each source's status word before and after; and, for `drafts.json` ONLY, the number of rows and the number of DISTINCT `object_id` values (counts only, no item text, no draft text). Any surprise is a row `COMM_ASSIST-CA2-S<k>` appended to the investigation file; keep its line endings.

### RULES

- Edit nothing: no file in the checkout, no task, no variable, no policy, no firewall or sshd setting, no key. The only act beyond reading is starting the EXISTING task once.
- AWS: read-only (the job's own reads). Do not run any write.
- This is not an alert, monitor or notification, and builds none.
- A refused or unmet criterion is reported with its measurement, never repaired by widening it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAl1-AC1" cell_refs="CA-l-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r20/checks/check_m1_perdraft.py"</invocation><expect>M1-PERDRAFT ok=True arms=6 of 6</expect></criterion>
`CAl1-AC1` -- the issuer's check (read it; do not edit it), run ON dell2 from the repository root: it loads THIS checkout's `refresh.py` with the AWS call replaced by a stand-in and requires one `drafts` row per open mail draft (two drafts on one mail object give two rows with distinct `seq` and `tag`; an object with only the older single `pending` gives one row; a chat object gives one), with exactly the contracted row keys. It reads 3 of 6 on a reader older than CA-k-1 and 6 of 6 on the trunk (both measured by the issuer).

<criterion id="CAl1-AC2" cell_refs="CA-l-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_k4_folder.py"</invocation><expect>K4-FOLDER ok=True</expect></criterion>
`CAl1-AC2` -- the round-18 folder check (read it; do not edit it), run ON dell2 after step 3: `INDEX.json` lists the six sources; every file is a valid envelope with status `ok` or `absent` (`unreadable` fails); the folder was written within the last 20 minutes; an `ok` source's items have exactly the contracted keys; `README.txt` names both new files; and no address, key or token shaped string appears in ANY file of the folder (FWD-11).

<criterion id="CAl1-AC3" cell_refs="CA-l-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i1_ages.py"</invocation><expect>I1-AGES ok=True arms=5 of 5</expect></criterion>
`CAl1-AC3` -- the bound, a control that PASSES at the base and must still pass on dell2's checkout: the reader's ages on the existing sources.
</proof_of_spec>

<expected_criteria>CAl1-AC1,CAl1-AC2,CAl1-AC3</expected_criteria>

Each invocation runs from the repository root under `timeout 200`. Write the proof instance to `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA2/COMM_ASSIST.TO-CA-l-1.dell2-reads-the-per-draft-rows.proof_of_spec.json`, pin each artifact row to the commit that carried it, validate it with `python .tools/proof-of-spec-check.py <instance> CAl1-AC1,CAl1-AC2,CAl1-AC3` from inside the checkout AFTER your last commit, and flip `<status>` to `complete` only when all three pass and the instance is VALID at the final head. Commit with `.tools/safe-commit.sh` under your own serial.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round20.md</decomp_doc>
<owned_cells>CA-l-1</owned_cells>
</decomp_ref>

<paths>
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-l-1.dell2-reads-the-per-draft-rows.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA2/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the act creates no schedule: it starts the EXISTING task `MuseReaderRefresh` once, as the same user; its 15-minute schedule is unchanged. No cron, alarm, monitor or notification is created.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves; the reader performs the same read-only DynamoDB scan it already performs, with the same dell2 identity.
comp-adversary: RUN -- the new rows breaking the folder muse already reads (refused: step 3 stops on a non-zero task result or an `ok` source turning `unreadable`, AC2 re-reads every file, AC3 re-runs the ages control); two mails reading as one row on dell2 (refused: AC1 `two-rows-one-object` and `distinct-seq-and-tag` run on dell2's own checkout); a mail row with no seq so muse cannot tell two apart (refused: AC1 requires a distinct `seq` and `tag` for each); a secret, key or address reaching the folder (refused: AC2 scans every file, FWD-11). BLIND: no real pair of considered mails exists, so `drafts.json` on dell2 carries single rows only until a real pair arrives; AC1 proves the reader's LOGIC on dell2's code with a stand-in table, and the report's row counts show what the live table holds today. The issuer has not read dell2's folder before this order.
lane: the <paths> block IS the grant; the seat edits nothing else and installs nothing.
</preflight>

Base: CAl1-AC1 base: FAIL on a reader older than CA-k-1 (3 of 6, measured by the issuer against `refresh.py` as of `ad67a9b9a4`); PASS on the trunk at `d6605d65cd` (6 of 6). CAl1-AC2 base: not measured by the issuer (the folder is on dell2); expected ok=True. CAl1-AC3 base: PASS as measured on the trunk (control, 5 of 5).
Source: CTO round-19 analysis ruling 1 (`ledger/ROUND_ANALYSIS.round19.md` @b4f6d499d0, msg 109356); the round-19 L8 packet's first enrichment candidate; the CA-j-15 order as the precedent; `refresh.py` `_open_drafts` and `read_drafts`.
