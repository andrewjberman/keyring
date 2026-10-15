# TO IRPT_BCKEND.TO-IB-pr-569 -- READ why Cottonwood's account is absent from the holdings candidate (row D2-S158): the refusal records, the account's state in the source and the directory, whether it clears, and where the acceptance path lives in the publisher; READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-569</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~412</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PC</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 8020 (the S158 READ in a later ~P round), row D2-S158 | **Decomp cell:** `IB-pr-569` (decomposition section 205) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-412`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~412 <0.9.0_WK_IRPT_BCKEND~412@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Where the command rail denies an AWS enumeration it prints the command that answers: run that; or add a trailing `# rail-checked: <why>`. Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** counts, dates, hashes, commit ids, field names, class names and file paths only in any tracked file; **no account id, household id, client id, name, quantity, value or holding name; the lost account is described by its class, never by its id.** Scratch lives OUTSIDE the worktree (`C:/dev/_scratch412/`); delete a downloaded refusal record from scratch after you read it.

**Cell `IB-pr-569` (inlined).** Row `IRPT_BCKEND-D2-S158` (READ IT FIRST, in `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`): Cottonwood's served Investor Reporting holdings are STALE. The newest accepted publication is business date 2026-10-08; the candidates for 2026-10-09 onward were REFUSED by the holdings publish guard (`data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`, the `account_lost` condition near line 3058) on ONE condition: `account_lost` count 1, an account in the served snapshot absent from the candidate. 49 Financial and Inflection are at 2026-10-12 and later (no refusal blocks them). This is a client-facing staleness. The row says what was NOT read: **why the account is absent from the candidate** (a terminated or closed account, a data gap in the source, a mapping break, a directory exclusion, a candidate filter), whether the refusal clears on its own, who owns the acceptance path, and whether the code has one. This order READS those four things. **It changes nothing, publishes nothing, bypasses nothing and writes nothing to AWS.**

**Do, in this order:**
0. **AMENDMENT 1 (issuer, on your rows W412-S2 and S3): the code to read.** The worktree is a sparse checkout without `data/`. Run `git sparse-checkout add data/assets/scripts/gold/investor_reporting` in YOUR worktree (a local setting, never committed, reads only; do not widen it further) so the publisher and its tests are on disk under the worktree root (the check reads each file and line there). If `comp-find --corpus aws` is blocked, find the firm's prefix with `lib/opal_naming.py` `address()` and a read-only list, as you did.
1. **Base and date.** `git rev-parse HEAD` before your first commit is `base_commit`; `read_date` is `date -u +%F`.
2. **The refusals.** Find Cottonwood's holdings publication prefix and its refusal records through the served graph (`comp-find --corpus aws` or the rail's printed command; the firm's bucket and the `publish_refusal.json` objects; head, list and get of EXISTING objects only). Read every refusal record that exists (counts; the schema `irpt-holdings-publish-refusal-v1` names the candidate business date, the served date and the conditions). Record `served` = `{"firm":"cottonwood","business_date":"2026-10-08"}` (re-read it from the firm's current manifest: if it moved, STOP and report), `refusals` = `{"refused_dates":[the candidate business dates refused, ISO, sorted: only trading days after the served date],"first_refused_candidate_date":"<the first>","refusal_records_read":<n>,"condition":"account_lost","lost_count":1,"per_candidate":[...]}`. **AMENDMENT 1, on your row W412-S1: the lost count differs between records** (the first candidate's record names `account_lost` with count 9 and 8 closed accounts listed as not refused; the later ones name count 1). Record EVERY record version: `per_candidate` = `[{"candidate_date":"<ISO>","lost_count":<n>,"closed_not_refused_count":<n>},...]`, one row per refused date in the same order as `refused_dates`; the LATEST candidate's `lost_count` and `refusals.lost_count` must read 1 (row S158's residual account). STOP only on a condition other than `account_lost` or a latest count other than 1.
3. **Where the account is lost.** Without ever recording its id: the account is present in the served 2026-10-08 snapshot and absent from the candidates. For at least two business dates (2026-10-08 and the first refused date) read the SOURCE partition the candidate is built from (the custodian holdings partition the producer reads; find it in `holdings_snapshot.py`) and state whether the account is listed (`listed_in_source`). Read the account directory (the directory the guard's `closed`/exemption logic reads; find it in the code near lines 2888 to 3060 and the tests `test_directory_exemption_source_marks.py` and `test_holdings_publish_gate.py`) and state whether the account carries a mark (`directory_mark` = `{"found":bool,"class":"<the mark's class>","note":"20+ characters, class only"}`). Record `lost_account` = `{"present_in_served":true,"absent_in_candidates":true,"claim":"measured|inferred|absent","source_partition_checks":[{"date":"<ISO>","listed_in_source":bool},...],"directory_mark":{..}}`.
4. **The cause and whether it clears.** `cause` = `{"class":"terminated_or_closed_account|source_data_gap|mapping_break|directory_exclusion|candidate_filter|other","claim":"measured|inferred|absent","statement":"60+ characters","evidence":["30+ characters each, at least two"]}`; `self_clears` = `{"claim":"measured|inferred|absent","statement":"40+ characters: does the account return in the source on later dates, or stay absent"}`. A cause you did not measure is `inferred`, and say what would measure it.
5. **The acceptance path, read in the code.** `acceptance_path` = `{"guard":{"file":"<repo path>","line":<n>,"identifier":"<text on that line, holding account_lost>"},"override_mechanisms":[{"name":"..","file":"..","line":<n>,"identifier":".."},...],"owner":"20+ characters: who the code or the docs name as the decision owner","recommended_path":"40+ characters: the path you recommend, from the mechanisms you read (for example excluding a closed account through the directory mark, or the one-date bypass the tests exercise)"}`. Read the guard, the closed-account exclusion, the one-date bypass (`test_holdings_bypass_one_date.py`) and any directory exemption; each mechanism you list must be a line you read at HEAD (the check reads the line).
6. **The other firms.** `other_firms` = `{"49financial":{"refusal_record_present":bool,"served_business_date":"<ISO>"},"inflection":{..}}` from their prefixes and manifests (existing objects only).
7. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~412/IB209-1_s158_read.json` with exactly: `base_commit`, `read_date`, `served`, `refusals`, `lost_account`, `cause`, `self_clears`, `acceptance_path`, `other_firms`, `notes` (at least three lines of 30+ characters: what each fact rests on, the objects read counted, what was not read), and the counters `functions_invoked`, `sign_ins_made`, `aws_writes_made`, `rows_written`, `figures_written`, `vendor_requests_sent`, all 0.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB209-1_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch (and any downloaded refusal record) if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB209-1-AC1" cell_refs="IB-pr-569"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r209/p209_cells.py" . IB209-1-AC1</invocation><expect>IB209-1-AC1 PASS</expect></criterion>
<criterion id="IB209-1-AC2" cell_refs="IB-pr-569"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r209/p209_cells.py" . IB209-1-AC2</invocation><expect>IB209-1-AC2 PASS</expect></criterion>
<criterion id="IB209-1-AC3" cell_refs="IB-pr-569"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r209/p209_cells.py" . IB209-1-AC3</invocation><expect>IB209-1-AC3 PASS</expect></criterion>

<expected_criteria>IB209-1-AC1, IB209-1-AC2, IB209-1-AC3</expected_criteria>

What the checks grade: AC1 the served date, the refused candidate dates (trading days after it, recomputed against the calendar), the one condition `account_lost` with count 1, the lost account located against the source (two or more dates) and the directory mark; AC2 the cause with its claim and evidence, whether it clears, the acceptance path read in the code (every file and line verified by the check at HEAD) and the other firms' refusal state; AC3 notes, the six counters 0 and no long digit run (no account id). Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS: `s3api head-object`, `get-object` and `list-objects-v2` of EXISTING objects under the three firms' IRPT prefixes (holdings publication, refusal records, manifests, the custodian source partitions and the account directory the guard reads), `list`, `describe`. **Nothing is published, bypassed, re-run, invoked, written to AWS, signed or sent. The producer is NOT run by hand.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends; a need to run the publisher; the served date other than 2026-10-08; a refusal record naming a condition other than `account_lost`, or the latest record a lost count other than 1 (earlier records may name more: record them); an account id, name or value in a tracked file; a need to type an object address for a NEW object. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W412-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~412/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 205 (round 1, workstream ~PC), cell `IB-pr-569`.
<owned_cells>IB-pr-569</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB209-1-AC1, IB209-1-AC2, IB209-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~412/IRPT_BCKEND.TO-IB-pr-569.read-why-cottonwoods-account-is-absent-from-the-holdings-candidate-and-where-the-acceptance-path-lives.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads existing objects (refusal records, manifests, source partition listings, the account directory) with the worker's own identity and writes one record; nothing is published, bypassed or invoked, so no served byte moves; any acceptance of the lost account is a later act under its own signed pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p209_cells.py IB209-1 dry-run at base on dell2 2026-10-15 ~10:5xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp tree the run created itself (the real calendar, a stub publisher file with the guard and override lines, a synthetic record; removed): all three PASS; nineteen negatives, each failing its own arm: a wrong firm, a refused date that is not a trading day, a refused date before the served date, a first-date mismatch, a second condition, a lost count of two, one source check, not present in served, an unknown cause class, one evidence line, a wrong guard line, a missing guard file, no override mechanism, an override identifier absent from its line, a missing other firm, a self-clears with no claim, short notes, a counter above 0, a long digit run.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~412` (worktree `C:/dev/wk-IRPT_BCKEND-412`). Class SERVED (reads a served surface and writes only the worker's records).
</preflight>
