# TO IRPT_DASHBD.TO-DB-b-156 -- the open half of the rewritten-original finding: does any reader the tie-out or the served dashboard uses key on the FILE's day and not the transaction's own date; and for the two sampled days, the ids' own dates against the files they now sit in

<to_id>IRPT_DASHBD.TO-DB-b-156</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~126</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>81</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 5937 (2026-10-11 ~21:58Z) | **Rows:** IRPT_DASHBD-D2-W124-S1 | **Decomp cell:** `DB-b-156` (decomposition section 83) | **outcome_ref:** FWD-12 (the tie-out) | **depends_on:** DB-b-151 (drained @7dbb71c512).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-126` (branch `wk-irpt-dashbd-81-126`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~126/`. Read first: each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`, and the records this order names.

**Why.** DB-b-151 found that the original Black Diamond transactions day objects were rewritten after this project's copy was taken:
the files for 2026-08-22 and 2026-08-23 now hold 0 rows (row `IRPT_DASHBD-D2-W124-S1`; record
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~124/COPY_VS_ORIGINAL.json`). The store's owner, 1.0.0_SA_CTO~DELL1, measured within the
hour that no transaction id was lost: 5,580 of 5,580 ids of those two days are present in the current files, re-attributed to other
days by later runs (its record, on another box's branch: `git fetch origin box/dell1` then
`git show origin/box/dell1:org/tier1_exec/1.0.0_SA_CTO/deliverables/BD49F_SILVER_TRANSACTIONS_LOSS_CHECK_20261011.md`; read it). It
names what it leaves open as this project's. The CTO (msg 5937): "One cell, read-only, counts only: does any reader this project's
tie-out or the served dashboard uses key on the file's day and not the transaction's own date? For the two sampled days, the ids' own
dates against the files they now sit in. The row closes on that."

**The cell (`DB-b-156`).** A read. You change no code and edit no other worker's record.
1. **The readers, as a printed denominator.** Two populations, listed before you class any:
   (a) the SERVED DASHBOARD's: the readers of the transactions store that DB-b-143 classed as served
   (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~116/ORIGINAL_STORE_SHAPE.json`, its readers list: take every one whose output is served);
   (b) the TIE-OUT's: the producing scripts of the figures DB-b-151 classed as read from the COPY (its `figure_sources` entries with
   store `COPY`; the scripts are tracked under `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~118/producers/`), one entry per distinct script.
   `readers_considered` is the length of that list; say how many came from each population.
2. **Class each reader** by reading its code at the line where it selects rows by day: `keys_on` is `FILE_DAY` (it takes the day from
   the object's key or partition name, or loads "the file for day D" and treats every row in it as day D), `TRANSACTION_DATE` (it
   filters or groups on a date column of the row itself: name the column), `BOTH`, `NEITHER` (it reads every file and uses no day at
   all) or `NOT_ESTABLISHED`. `readers`: [{file, line, used_by (TIE_OUT, SERVED_DASHBOARD or BOTH), keys_on, date_column, basis}].
   `file_day_keyed` is the count classed FILE_DAY or BOTH.
3. **The two days' ids.** For 2026-08-22 and 2026-08-23: read the oldest version of the original's day object (transaction id and the
   row's own date columns only: say which date columns exist, by name) and the current objects. `days`: [{day, ids_then (distinct ids
   in the file then), ids_found_now, files_now (how many current day files hold them), own_date_equals_then_file_day (how many ids'
   own date equals the day of the file they sat in THEN), own_date_equals_now_file_day (how many ids' own date equals the day of the
   file they sit in NOW), date_column_used}]. If the row carries more than one date column, give the two counts for the one the
   file-day-keyed readers would be compared against and say which, and list the others' counts under `other_date_columns`.
4. **The answer.** `answer`: {any_reader_keys_on_file_day (true, false or "NOT_ESTABLISHED"), basis, what_it_means (if a reader keys
   on the file day: for these two days, how many ids such a reader would now place on a different day than before, as a count; you do
   NOT recompute any served figure)}.
5. `s3_writes: 0`, `limits`. No account id, client name or amount; write days with separators; the check refuses a record holding any
   run of 8 or more digits. Private files go under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~126/`. Record `FILE_DAY_READERS.json`.

<criterion id="DB81-1-AC1" cell_refs="DB-b-156"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r81/p81_round81.py" . DB81-1-AC1</invocation><expect>DB81-1-AC1 PASS</expect></criterion>
`DB81-1-AC1` -- every reader considered is classed by what it keys on with file and line, the two sampled days' ids are counted by their own date against the file day then and now, and whether any reader keys on the file day is answered from that table. Base: FAIL.

<expected_criteria>DB81-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS READS allowed, through the `.tools/aws` shim or boto3 as the existing readers build their client, and nothing else, all in the ONE firm's Black Diamond bucket DB-b-151 read: for 2026-08-22 and 2026-08-23, the OLDEST version of the original's day object (the version DB-b-151 found equal to the copy), projected to the transaction id and the transaction's own date columns only; and the CURRENT day objects of the original that now hold those ids, projected to the same columns. NO money column, NO account column. A denial is recorded verbatim, not retried by another route.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~126/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W126-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~126/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-156.readers-keyed-on-file-day.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 83 (round 81), cell `DB-b-156`.
<owned_cells>DB-b-156</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB81-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~126/IRPT_DASHBD.TO-DB-b-156.readers-keyed-on-file-day.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB81-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; how many readers you considered and how the list was made; how many key on the file's day, each named with file and line and whether the tie-out or the served dashboard uses it; for each of the two days, how many ids the day's file held then, how many are found now and in how many files, and how many ids' own date equals the file day then and now; what you could not establish; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a table of readers and counts of ids; nothing is changed, no producer is edited.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; governed reads; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
