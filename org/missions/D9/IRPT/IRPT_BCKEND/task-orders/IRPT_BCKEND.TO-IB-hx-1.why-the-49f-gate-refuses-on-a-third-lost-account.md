# TO IRPT_BCKEND.TO-IB-hx-1 -- READ ONLY: why 49 Financial's holdings gate refuses the 2026-10-16 candidate on `account_lost` beyond the 2 listed absent-at-source accounts: which served account is gone and not exempt, and which test of the exemption it fails, in hashed ids and counts (row D2-S240; IB2 msg 10712)

<to_id>IRPT_BCKEND.TO-IB-hx-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~458</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>15</round>
<workstream>~PM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `IB-hx-1` (decomposition section 252) | **outcome_ref:** FWD-3 (the served holdings are current) | **Ordered by:** the issuer, on the row `IRPT_BCKEND-D2-S240` and the first fire's after-read `deliverables/0.7.0_AE_CloudOps~IB2/IB236-1_after_read_20261019.json`. **This order READS. It writes nothing to AWS, nothing to S3, and changes no source file.**

---

## WORKER FACE

**Cell `IB-hx-1` (inlined).** The holdings producer's gate (`data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`, lines about 3395 to 3440) refused 49 Financial's candidate of business date 2026-10-16: condition `account_lost`, count 1, beyond the 2 accounts it LISTED as absent at source. The rule (lines about 3401 to 3425): `gone = served["account_ids"] - have` (served accounts missing from the candidate); `closed = closed_accounts() & gone` is listed and not refused; the rest, `lost`, is passed to `absent_at_source_exempt(lost, evidence)` (lines about 3025 to 3080: an account is exempt ONLY when the source shows it with NO positions, absent or zero, in BOTH tables (`positions`, `balance`) on the candidate day AND the prior trading day, and ALL FOUR of those partitions are COMPLETE: account count at least 95 percent of the prior day's); what stays `lost` refuses because 49 Financial marks no closures. **So one served account is gone from the candidate, is not a recorded closure, and fails an exemption test. Find which account class it is and which test it fails. Do not fix anything.**

**Privacy (a hard rule, graded mechanically).** Hashed ids and counts only. An account is named in your files ONLY as the first 12 lowercase hex characters of `sha256(<the account id string as the producer holds it>)`. No `cli_` or `acc_` id, no custodian account number or household id, no name, no e-mail, no digit run of 9 or more, and no hex string of any length other than exactly 12 (a full 64-hex sha256 of a source LINE is allowed; cite commits by their first 10 characters). Raw output stays in a scratch directory OUTSIDE the repository and is deleted when you finish; your notes quote no output line that carries an id.

**Do, in this order:**
1. **Read the code (no data yet).** In `holdings_snapshot.py` read the gate (lines about 3395 to 3440), `absent_at_source_exempt`, `closed_accounts`, `marks_no_closures`, and the function that supplies `absent_at_source_evidence` (how the four partitions and the per-account positions sets are read). In `IB-hx-1_notes.md` (file name `IBhx1_notes.md`) list, as numbered `file:line` plus one clause, the order in which an account is tested.
2. **Replay the gate, read-only, with the earlier harness as the model.** `deliverables/0.9.0_WK_IRPT_BCKEND~437/IB233-1_49f_transplant_reread_harness.py` (IB-pr-602's driver) runs the built gate over the live pinned inputs and the served publication; COPY it into a scratch directory outside the repository (do not edit it) and run it for 49financial with candidate day 2026-10-16 so it reproduces the refusal and names the gone, non-exempt account. Under no path may it write: no upload, no `put`, no local mirror inside the repository. **If it cannot reproduce the refusal, or any read is AccessDenied, STOP: write what failed (prefix names only, no ids) into `IBhx1_notes.md` with `verdict` `UNDETERMINED` and report; do not widen any access.**
3. **The three accounts.** For the ONE gone, non-exempt account and for the TWO listed absent-at-source accounts, count the rows each has in each source table and on each of the two days: `source_rows.positions.{candidate,prior}` and `source_rows.balance.{candidate,prior}` (rows with positions above zero for `positions`, rows for `balance`, exactly as the evidence function counts them), and record `closed_marker` (is it in `closed_accounts()`; true or false).
4. **The four partitions.** For `positions` and `balance`, candidate day 2026-10-16 and prior day 2026-10-15, record `account_count` and `prior_account_count` (the denominator the 95 percent floor uses for THAT partition: read how the function defines it) and `percent_of_prior` = floor(account_count * 100 / prior_account_count). If the floor is not met for any partition, say so in `evidence_for_verdict`.
5. **The count per refusing fire, since 2026-10-14.** The producer's refusal record for 49financial holds one object version per refusing fire (IB2's facts file names the four fire times under `refusals_by_fire_utc`; find the refusal object's key in the producer code and read its four versions). For the fires of 2026-10-14, 2026-10-15, 2026-10-16 and 2026-10-19 record `lost_count_per_fire`: the `account_lost` count that fire's refusal carried and how many accounts that fire LISTED as absent at source (0 if the exemption was not yet minted that day). Counts only.
6. **Say, in `evidence_for_verdict`, whether the gone account would pass EACH of the exemption's tests** (no positions in `positions` on both days, none in `balance` on both days, all four partitions at least 95 percent), because the CTO's rule is: if it is absent at source by the SAME tests that admitted the first two, the exemption is extended by an addendum under both halves; if it fails for any other reason, that is a fix, not an exemption.
7. **Write `IBhx1_findings.json`** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~458/` with exactly these fields (the check reads them):
```
{"firm":"49financial","candidate_day":"2026-10-16","prior_day":"2026-10-15",
 "accounts":[{"hashed_id":"<12 hex>","role":"gone_not_exempt"|"exempt_listed","closed_marker":<bool>,
              "source_rows":{"positions":{"candidate":<int>,"prior":<int>},"balance":{"candidate":<int>,"prior":<int>}}}, ... exactly 3: one gone_not_exempt, two exempt_listed],
 "partitions":[{"table":"positions"|"balance","day":"candidate"|"prior","account_count":<int>,"prior_account_count":<int>,"percent_of_prior":<int>}, ... exactly 4],
 "lost_count_per_fire":[{"fire_date":"2026-10-14"|"2026-10-15"|"2026-10-16"|"2026-10-19","account_lost_count":<int>,"listed_absent_at_source":<int>}, ... exactly 4, one per date],
 "decision_line":{"file":"<repo-relative path>","line":<int>,"excerpt_sha256":"<64 hex: sha256 of that line, stripped, at HEAD>","what":"<one sentence, 10 to 300 chars>"},
 "why_not_exempt":"HAS_POSITIONS_IN_A_SOURCE_TABLE"|"PARTITION_INCOMPLETE"|"PRIOR_PARTITION_ABSENT"|"CLOSED_MARKER_MISSING"|"OTHER",
 "verdict":"BUILD_FAULT_ACCOUNT_HAS_SOURCE_POSITIONS"|"SOURCE_ABSENT_BUT_EXEMPTION_TESTS_FAIL"|"CLOSURE_WITHOUT_MARKER"|"UNDETERMINED",
 "evidence_for_verdict":"<10 to 400 chars, no ids>",
 "reads":{"aws_writes":0,"s3_puts":0}}
```
The check computes `excerpt_sha256` from the line you cite, so cite the line that DECIDES (the test that fails for this account), not a comment. Write the proof instance named under proof_of_spec, validate it with `python .tools/proof-of-spec-check.py <instance>`, and write `IBhx1_criteria_output.txt` (AC1 and AC2 output verbatim, run BEFORE the commit; AC3 after).
8. **ONE commit** with explicit paths (`.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~458 <0.9.0_WK_IRPT_BCKEND~458@opal.agent>" -F <msgfile> -- <paths>`, the message file written by the Write tool): your deliverables folder and any surprise row. If safe-commit is slow it is waiting on other seats: wait, never run it twice at once, never amend. Do not push. Report once, under 150 words: the failing test (file:line), the reason and verdict, the counts, AC3's result.

**Criteria (run each under `timeout 300` from the repository root; AC3 reads `HEAD~1..HEAD`, so run it AFTER your one commit):**

<criterion id="IBHX1-AC1" cell_refs="IB-hx-1"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r258/p258_cells.py" . IBHX1-AC1</invocation><expect>IBHX1-AC1 PASS</expect></criterion>
<criterion id="IBHX1-AC2" cell_refs="IB-hx-1"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r258/p258_cells.py" . IBHX1-AC2</invocation><expect>IBHX1-AC2 PASS</expect></criterion>
<criterion id="IBHX1-AC3" cell_refs="IB-hx-1"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r258/p258_cells.py" . IBHX1-AC3</invocation><expect>IBHX1-AC3 PASS</expect></criterion>

<expected_criteria>IBHX1-AC1, IBHX1-AC2, IBHX1-AC3</expected_criteria>

What the checks grade: AC1 the findings file's shape, three accounts with distinct 12-hex ids and non-negative counts, four partition records whose percent matches their counts, four lost-count records for the refusing fires, the cited decision line existing at HEAD with the stated hash, and the reason and verdict from their closed sets; AC2 that nothing in your deliverables folder carries a raw identifier or an odd-length hex run; AC3 that your one commit touches only this order's paths. **They do not grade whether your answer is TRUE: the issuer re-reads the source itself before it rules.** Do not edit the checks.

## BOUNDS

- **Grant:** write `deliverables/0.9.0_WK_IRPT_BCKEND~458/`; the surprise channel for rows; read the repository; read S3 under the identity the shell holds and run the copied harness read-only. **NO AWS write of any kind; NO S3 put; NO source, Terraform or registry change; NO Lambda invoke; NO SSM command; NO raw identifier in any file; NO edit of the harness in its home folder; NO push.**
- **Refusal clause:** STOP and report, writing nothing further beyond the notes, if a read is denied, if the replay cannot reproduce the refusal, or if answering would need a write. File a surprise ROW for anything odd and keep working; a broker message is never the carrier.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~458/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-hx-1.why-the-49f-gate-refuses-on-a-third-lost-account.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 252 (round 15, workstream ~PM), cell `IB-hx-1`.
<owned_cells>IB-hx-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBHX1-AC1, IBHX1-AC2, IBHX1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~458/IRPT_BCKEND.TO-IB-hx-1.why-the-49f-gate-refuses-on-a-third-lost-account.proof_of_spec.json` (the file stem of THIS order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only investigation; nothing is deployed or written; the replay uses a copy of an existing read-only harness outside the repository.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is changed; a denied read is a STOP, never a widening.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface is touched.
comp-adversary: RUN -- p258_cells.py IBHX1 dry-run at base on dell2 2026-10-19: AC1, AC2, AC3 FAIL (no findings). Positive control (control258.py) over synthetic git repos with a source file to cite: the clean findings and a notes file holding a full sha256 and a ten-hex commit PASS; 23 AC1 negatives (a lost-count record missing, only three, the wrong dates, a negative count, a wrong firm, a wrong candidate day, two accounts only, two gone_not_exempt, duplicate ids, an id not 12 hex, a negative row count, missing balance rows, a non-boolean closed marker, three partitions, a duplicate partition, an inconsistent percent, a zero prior count, a wrong excerpt hash, a line out of range, a cited file absent, an invalid reason, an invalid verdict, an AWS write), 5 AC2 negatives (a cli_ id, an acc_ id, a 12-digit run, an e-mail address, a 40-hex run) and 3 AC3 negatives (a file outside the paths, a write under data/, the findings not in the commit) each fail their own arm, 0 unexpected. NOT measured by me: whether the cited line is the deciding one (the issuer's re-read), the replay itself, any live read.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~458`. Class WORLD (the work reads live client data from S3 under the agent identity; it writes nothing).
</preflight>
