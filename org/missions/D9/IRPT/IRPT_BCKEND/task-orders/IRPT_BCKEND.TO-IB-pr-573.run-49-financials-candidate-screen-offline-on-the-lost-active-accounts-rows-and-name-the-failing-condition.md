# TO IRPT_BCKEND.TO-IB-pr-573 -- RUN 49 Financial's candidate screen OFFLINE on the lost ACTIVE account's source rows and name the failing condition; say whether it is the condition Cottonwood's IB-pr-571 finds; the fix options in the code; READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-573</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~416</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PE</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 8256 ("cut the 49F candidate-screen READ now, beside Cottonwood's") on the 49 Financial refusal READ (IB-pr-570, merged @a9eb88ed54) | **Decomp cell:** `IB-pr-573` (decomposition section 208) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-416`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~416 <0.9.0_WK_IRPT_BCKEND~416@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Where the command rail denies an AWS enumeration it prints the command that answers: run that; or add a trailing `# rail-checked: <why>`. Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/investor_reporting` (local, never committed). The validator's import chain may sit elsewhere (the Cottonwood sibling, IB-pr-571, needed `infra/aws/lambda/investor-reporting`): read the `import` lines of what you call and add, with the same local command, EXACTLY the directories they need and nothing wider.

**Client data rule:** counts, dates, hashes, commit ids, condition names, class names and file paths only in any tracked file; **no account id, household id, client id, name, quantity, value or holding name; the account is described by class and count, never by id.** Scratch lives OUTSIDE the worktree (`C:/dev/_scratch416/`); delete downloaded partitions from scratch after you read them.

**Cell `IB-pr-573` (inlined).** The 49 Financial refusal READ (`deliverables/0.9.0_WK_IRPT_BCKEND~413/IB210-1_49f_refusal_read.json`, rows `D2-W413-S1`, `S2`; READ THEM FIRST) found: 49 Financial is served at 2026-10-12 (two trading days behind T-1); the candidate for 2026-10-13 was refused on `account_lost` count 1; the lost account is marked **ACTIVE** in the directory (so the closed-account exemption cannot apply); it is absent from the candidate, and **the candidate builder's filter that omits it was not read**, so the cause is inferred. The CTO (msg 8256) wants it measured: **run 49 Financial's candidate screen OFFLINE on the lost account's source rows and name the exact failing condition; say whether it is the same condition Cottonwood's IB-pr-571 finds** (that READ is in flight; compare with its record `deliverables/0.9.0_WK_IRPT_BCKEND~414/IB210-2_cot_validator_read.json` if it is on box/dell2 when you reach that step, else say what you could not compare). **Offline means:** the source rows are read (GET of the existing partition objects to scratch), the screen or validator function is imported from the repository file and called on those rows in a scratch script outside the repository; nothing is published, no producer is run, no served prefix is written. The guard is untouched; no bypass is widened.

**Do, in this order:**
0. `git sparse-checkout add data/assets/scripts/gold/investor_reporting` (and the import-chain directories as above). `git rev-parse HEAD` before your first commit is `base_commit`; `read_date` is `date -u +%F`.
1. **Find the lost account without recording it.** From the refusal record (49 Financial, candidate 2026-10-13, `account_lost` count 1) identify the one account that is in the served 2026-10-12 snapshot and absent from the candidate; keep its id in memory or scratch only. Read its rows from the source partition the 49 Financial candidate is built from (`source_rows` = `{"count":<n>,"distinct_dates":<n>}`).
2. **Read the 49 Financial candidate builder in the code** (`data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`: the builder for 49 Financial, its per-account screen or validator, the place that drops an account from the candidate). `validator_site` = `{"file":"<repo path>","line":<n>,"identifier":"<text on that line>"}` for the validator or condition checks it applies to an account; `screen_site` likewise for the function that drops accounts from the candidate. Each is a line you read at HEAD (the check reads it).
3. **Run it offline** exactly as the builder calls it, in a scratch script outside the repository: `offline_run` = `{"performed":true,"read_only":true,"writes":0,"published":false,"invocation":"30+ characters: the command, WITHOUT any account id","outcome":"refused|accepted"}`. If it REFUSES: `failing_condition` = `{"name":"<the condition name the code gives>","claim":"measured","site":{"file","line","identifier"} (the line that raises it),"explanation":"60+ characters: what it checks, in words, no value"}`. If it ACCEPTS (so the account is dropped for another reason in the builder, such as a different input shape, a join or a prior filter), say so: `failing_condition` = `{"name":"","claim":"inferred|absent","statement":"60+ characters naming what you read instead (the builder's own code path)","explanation":"60+ characters"}`.
4. **Same as Cottonwood?** `same_as_cottonwood` = `{"same":bool,"claim":"measured|inferred|absent","statement":"60+ characters: the condition names compared, or what you could not compare and why"}`.
5. **The fix options, read in the code.** `fix_options` = `[{"option":"20+ characters","site":{"file","line","identifier"},"effect":"30+ characters"},...]`, at least two (a correction in the screen or validator at the line you named; a custodian-confirmed TERMINATED mark through the closed-account exclusion; others you read). Each `site` a line you read at HEAD. Do not propose a guard bypass. `ids_private` is true.
6. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~416/IB212-1_49f_screen_offline_read.json` with exactly: `base_commit`, `read_date`, `validator_site`, `screen_site`, `source_rows`, `offline_run`, `failing_condition`, `same_as_cottonwood`, `fix_options`, `ids_private`, `notes` (at least three lines of 30+ characters), and the six counters at 0 (`functions_invoked`, `sign_ins_made`, `aws_writes_made`, `rows_written`, `figures_written`, `vendor_requests_sent`).

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB212-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB212-1-AC1" cell_refs="IB-pr-573"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r212/p212_cells.py" . IB212-1-AC1</invocation><expect>IB212-1-AC1 PASS</expect></criterion>
<criterion id="IB212-1-AC2" cell_refs="IB-pr-573"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r212/p212_cells.py" . IB212-1-AC2</invocation><expect>IB212-1-AC2 PASS</expect></criterion>
<criterion id="IB212-1-AC3" cell_refs="IB-pr-573"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r212/p212_cells.py" . IB212-1-AC3</invocation><expect>IB212-1-AC3 PASS</expect></criterion>

<expected_criteria>IB212-1-AC1, IB212-1-AC2, IB212-1-AC3</expected_criteria>

What the checks grade: AC1 the validator and screen sites verified at HEAD, the source rows counted, the offline run PERFORMED, read only (a record that did not run it is not graded); AC2 the failing condition named from the code (the line that raises it verified, a measured claim) or the acceptance said in words, the comparison with Cottonwood's condition and the fix options read in the code; AC3 notes, the six counters 0 and no long digit run (no id). Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS: `s3api head-object`, `get-object` and `list-objects-v2` of EXISTING objects (49 Financial's source partitions, its refusal record, the directory), `list`, `describe`. **Nothing is published, bypassed, run against a served prefix, invoked, written to AWS, signed or sent. The producer is NOT run. The guard stays.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends; a need to run the producer against a served prefix; an account id, name or value in a tracked file; a need to type an object address for a NEW object. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W416-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~416/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 208 (round 1, workstream ~PE), cell `IB-pr-573`.
<owned_cells>IB-pr-573</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB212-1-AC1, IB212-1-AC2, IB212-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~416/IRPT_BCKEND.TO-IB-pr-573.run-49-financials-candidate-screen-offline-on-the-lost-active-accounts-rows-and-name-the-failing-condition.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads existing partitions and the publisher's code with the worker's own identity and writes one record; the screen runs offline in scratch on one account's rows, nothing is published or run against a served prefix, so no served byte moves; the fix is the CTO's ruling and a later act under one never-widen pair that states the served DELTA.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p212_cells.py IB212-1 dry-run at base on dell2 2026-10-15 ~11:5xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp tree the run created itself (the real calendar, a stub publisher file, a synthetic record; removed): all three PASS; fifteen negatives, each failing its own arm: a wrong validator line, a wrong screen identifier, no source rows, a run that wrote, a run not performed, a run that published, an accepted run without a performance, a refused run claimed inferred, a wrong condition line, one fix option, a same-as-Cottonwood flag not boolean, a short statement, ids not private, short notes, a counter above 0.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~416` (worktree `C:/dev/wk-IRPT_BCKEND-416`). Class SERVED (reads a served surface and writes only the worker's records).
</preflight>
