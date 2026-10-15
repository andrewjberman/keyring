# TO IRPT_BCKEND.TO-IB-pr-574 -- READ how Cottonwood's one EMPTY-at-the-source account is accepted as closed: the directory's TERMINATED mark (who writes it, its shape, the precedent), the guard's reading, the evidence dates, and an OFFLINE guard run with the mark applied to the one account; READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-574</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~417</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PF</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 8263 ("rule Cottonwood now; accept the loss on the source's own evidence by a pair; file the directory's missing TERMINATED mark as a row for the directory's owner"), on the Cottonwood validator READ (IB-pr-571, merged @61fd06850f) and the CTO's S158 ruling | **Decomp cell:** `IB-pr-574` (decomposition section 209) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-417`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~417 <0.9.0_WK_IRPT_BCKEND~417@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Where the command rail denies an AWS enumeration it prints the command that answers: run that; or add a trailing `# rail-checked: <why>`. Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting` (local, never committed), plus EXACTLY the directories the import chain of what you call needs (the Cottonwood sibling, IB-pr-571, needed `infra/aws/lambda/investor-reporting` and a currency file; read your imports and add only those, nothing wider).

**Client data rule:** counts, dates, hashes, commit ids, field names, status names and file paths only in any tracked file; **no account id, household id, client id, name, quantity, value or holding name; the account is described by class and count, never by id.** Scratch lives OUTSIDE the worktree (`C:/dev/_scratch417/`); delete downloaded partitions and directory objects from scratch after you read them.

**Cell `IB-pr-574` (inlined).** Rows `IRPT_BCKEND-D2-S158`, `D2-S193`/`D2-S194` (READ THEM FIRST) and the Cottonwood validator READ (`deliverables/0.9.0_WK_IRPT_BCKEND~414/IB210-2_cot_validator_read.json`): Cottonwood's one residual lost account has ONLY no-position rows in the custodian source (the validator refuses an empty custody frame at `holdings_snapshot.py` line 403; zero independent-total rows on 2026-10-13), so it is EMPTY at the source, not silently lost. The CTO (msg 8263) ruled that this is the "closed at the source" branch of his S158 ruling: the acceptance is a **never-widen pair bound to that one account and the first date it is accepted from, evidence = the source rows' dates and zero position counts; blast radius one account leaving Cottonwood's served snapshot; rollback the prior publication (2026-10-08); the guard unchanged, no general override, no custodian contact.** The guard exempts an account only through the directory's TERMINATED mark (`closed_account_ids`, `holdings_snapshot.py` lines 2980 to 2989, and the exclusion near line 3051). The directory carries no entry for this account (it holds 271 entries: 2 TERMINATED, 269 UNKNOWN). The pair needs the MECHANISM: this order READS it and proves it offline. **It writes nothing to the directory, the guard or any bucket.**

**Do, in this order:**
0. `git sparse-checkout add data/assets/scripts/gold/investor_reporting` and the import-chain directories. `git rev-parse HEAD` before your first commit is `base_commit`; `read_date` is `date -u +%F`.
1. **The mark.** Read the code that WRITES a directory entry's status (the directory refresh or whatever writes `TERMINATED`; find it from `closed_account_ids` back to its writer: Glob the folder lists, read named files; the directory is read at the routed pointer the guard uses). `mark` = `{"writer_site":{"file","line","identifier"} (the line that sets or writes the status),"guard_reading_site":{"file","line","identifier"} (the line in closed_account_ids or its caller that reads TERMINATED),"shape":"40+ characters: the fields of a directory entry that carry the status and its effective date, no id","owner":"20+ characters: the seat, function or schedule that writes the directory","precedent":{"terminated_entries_in_cottonwood":n,"directory_entries":n,"claim":"measured|inferred|absent","how_set":"40+ characters: how an existing TERMINATED entry came to carry the mark (the data's own evidence or the writer's rule)"}}`. Each site a line you read at HEAD (the check reads it).
2. **The evidence.** For the one account (id in scratch only), read its rows in the custodian source for the dates the S158 READ and IB-pr-571 used and the later trading days up to the read date: `evidence` = `{"accounts":1,"zero_position_dates":[ISO trading days, sorted, at least three, where the source lists the account with zero positions],"positions_on_those_dates":0,"first_accept_date":"<the first of them>","claim":"measured","statement":"60+ characters, in words, no id"}`.
3. **The offline guard run.** In a scratch script OUTSIDE the repository, call the publish gate (`evaluate_publish_gate`, `holdings_snapshot.py` near line 3185) on Cottonwood's newest candidate (built offline, as IB-pr-571 built its rows) with the closed-account provider answering as if the directory held a TERMINATED mark for that ONE account (a stub provider in the scratch script; no directory object is touched), and compare the candidate against the served 2026-10-08 snapshot: `offline_guard` = `{"performed":true,"read_only":true,"writes":0,"published":false,"invocation":"30+ characters (the command, no id)","account_listed_as":"closed_accounts_not_refused (the gate's own listing) or account_lost","outcome":"WOULD_PUBLISH|REFUSED","nodes_changed_other_than_the_account":<count of nodes whose amount or identity differs between the served snapshot and the candidate besides the one account's nodes>,"accounts_leaving":1}`. If the gate still refuses, or other nodes differ, say what and STOP at the record (the check passes only the clean case; a refusal is a row and a report).
4. **The rollback.** `rollback` = `{"statement":"40+ characters: the prior accepted publication and how it returns (the index version), no deletion"}`.
5. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~417/IB213-1_terminated_mark_read.json` with exactly: `base_commit`, `read_date`, `mark`, `evidence`, `offline_guard`, `rollback`, `notes` (at least three lines of 30+ characters), and the six counters (`functions_invoked`, `sign_ins_made`, `aws_writes_made`, `rows_written`, `figures_written`, `vendor_requests_sent`), all 0.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB213-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB213-1-AC1" cell_refs="IB-pr-574"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r213/p213_cells.py" . IB213-1-AC1</invocation><expect>IB213-1-AC1 PASS</expect></criterion>
<criterion id="IB213-1-AC2" cell_refs="IB-pr-574"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r213/p213_cells.py" . IB213-1-AC2</invocation><expect>IB213-1-AC2 PASS</expect></criterion>
<criterion id="IB213-1-AC3" cell_refs="IB-pr-574"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r213/p213_cells.py" . IB213-1-AC3</invocation><expect>IB213-1-AC3 PASS</expect></criterion>

<expected_criteria>IB213-1-AC1, IB213-1-AC2, IB213-1-AC3</expected_criteria>

What the checks grade: AC1 the mark's writer and the guard's reading verified at HEAD, the shape, the owner and the precedent counts; AC2 the evidence: one account, at least three zero-position trading dates (recomputed against the calendar), zero positions, the first accept date, a measured claim; AC3 the offline gate run performed read only, the account listed as closed and not refused, every other node unchanged, one account leaving, the rollback, notes and the six counters 0. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS: `s3api head-object`, `get-object` and `list-objects-v2` of EXISTING objects (Cottonwood's source partitions, directory, served snapshot), `list`, `describe`. **Nothing is published, written to the directory or any bucket, bypassed, run against a served prefix, invoked, signed or sent. The guard is NOT changed. The stub provider lives only in your scratch script.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends; a need to write the directory; an account id, name or value in a tracked file; a need to type an object address for a NEW object. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W417-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working. **File the directory's missing TERMINATED mark as a row for the directory's owner (CTO msg 8263): class and count only.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~417/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 209 (round 1, workstream ~PF), cell `IB-pr-574`.
<owned_cells>IB-pr-574</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB213-1-AC1, IB213-1-AC2, IB213-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~417/IRPT_BCKEND.TO-IB-pr-574.read-how-cottonwoods-empty-account-is-accepted-as-closed-the-directory-mark-its-writer-and-an-offline-guard-run.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads existing objects and the publisher's code with the worker's own identity and writes one record; the gate runs offline in scratch with a stub closed-account provider, nothing is published, written to the directory or run against a served prefix, so no served byte moves; the acceptance itself is a later act under a never-widen pair bound to the one account and its first accept date.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p213_cells.py IB213-1 dry-run at base on dell2 2026-10-15 ~12:4xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp tree the run created itself (the real calendar, a stub publisher file, a synthetic record; removed): all three PASS; eighteen negatives, each failing its own arm: a wrong writer line, a missing guard file, a short shape, precedent counts missing, two accounts, two dates only, a date that is not a trading day, nonzero positions, a first-date mismatch, an inferred claim, a guard not performed, a guard that wrote, a guard that published, the account still refused, other nodes changed, a short rollback, a counter above 0, a long digit run.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~417` (worktree `C:/dev/wk-IRPT_BCKEND-417`). Class SERVED (reads a served surface and writes only the worker's records).
</preflight>
