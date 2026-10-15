# TO IRPT_BCKEND.TO-IB-pr-572 -- READ the split-adjusted holdings price return: where holdings_performance_daily computes the price contribution, where the custodian's STK STOCK SPLIT rows live per firm, the measured split ratios against the close-price ratio, and the served DELTA the fix would move; READ ONLY

<to_id>IRPT_BCKEND.TO-IB-pr-572</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~415</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~PD</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_ICRO_VUG_STOCK_SPLIT_NONFLOW_SPLIT_ADJUST_HOLDINGS_RETURN_20261015.md` (@9913bf3ed4, msg 8251) on the CRO's research @fe343dbc14 | **Decomp cell:** `IB-pr-572` (decomposition section 207) | **outcome_ref:** FWD-21

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-415`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~415 <0.9.0_WK_IRPT_BCKEND~415@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Where the command rail denies an AWS enumeration it prints the command that answers: run that; or add a trailing `# rail-checked: <why>`. Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**The worktree is a sparse checkout without `data/`:** your first act is `git sparse-checkout add data/assets/scripts/gold/irpt_holdings_performance` and `git sparse-checkout add data/assets/scripts/gold/investor_reporting` (local settings, never committed, nothing wider), so the producer, its declaration and its tests resolve under the worktree root.

**Client data rule:** counts, dates, hashes, commit ids, column names, reason codes and file paths only in any tracked file; **no CUSIP (the ruling names four; list none), no account id, household id, client id, name, quantity, value or holding name.** Scratch lives OUTSIDE the worktree (`C:/dev/_scratch415/`); delete downloaded partitions from scratch after you read them.

**Cell `IB-pr-572` (inlined).** The CTO ruled (@9913bf3ed4): the 2026-04-21 VUG rows (`tran_srcde` STK, "STOCK SPLIT", `tr_cd` IC, `sb_cd` RO; 972 rows, 840 accounts, quantity exactly x6.0, close 492.58 to 81.50) are a 6-for-1 **stock split**, non-flow. **The defect is in `holdings_performance_daily`'s price-only return: it is not split-adjusted.** The fix: the holdings price return adjusts a position's price basis on a split day by the custodian's own split ratio, taken from the same-day `STK` "STOCK SPLIT" row (quantity after over quantity before for an account with no same-day trade in the security), confirmed against the close-price ratio; no outside split calendar becomes a source (yfinance a control only); a security-day whose ratio cannot be measured (for example every holder also traded that day) is `SPLIT_RATIO_ABSENT` and is not graded; the three other CUSIPs split that day are in the same fix and the other two firms are read for split days; every reader classifies by `(tran_srcde, tr_cd, sb_cd)`. The change moves served numbers, so it lands under a never-widen pair that counts the DELTA per account-day. **This order READS the inputs the pair and the build need. It changes nothing.**

**Do, in this order:**
0. `git sparse-checkout add` the two directories above. `git rev-parse HEAD` before your first commit is `base_commit`; `read_date` is `date -u +%F`.
1. **The producer, in the code.** Read `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` (the pure core `holdings_return`, near line 743: the price contribution is `_v * (_p1 / _p0 - 1)`; `price_of`; the partition loader `_frame_for`; the declaration file and `load_declaration`). `producer` = `{"contribution_site":{"file","line","identifier"},"pure_core_site":{..holding "def holdings_return"},"partition_loader_site":{..},"declaration_site":{..},"quantity_basis_statement":"60+ characters: how the price contribution uses the t-1 and day-t prices today and why a split day reads as a loss"}`; each site is a line you read at HEAD (the check reads it).
2. **The custodian's split rows, per firm.** For each of `49financial`, `cottonwood`, `inflection`: find the declared transactions source the firm's rows come from (the declaration entry, `lib/opal_naming.py` `address()` for prefixes; existing objects, head/get/list only); state whether the three columns `tran_srcde`, `tr_cd`, `sb_cd` are present. Count: `split_rows` (rows with `tran_srcde` STK and the "STOCK SPLIT" text), the `split_days` (ISO, sorted, trading days) over the history the firm holds, `split_security_days` (distinct (security, day) pairs), `measurable` (a ratio computable: quantity after over quantity before for an account with NO same-day trade in the security), `ratio_absent` (not computable, for example every holder also traded that day), and of the measurable ones `ratio_agrees_with_close` and `ratio_disagrees_with_close` (the custodian ratio against the close-price ratio of the day-t partition over t-1, within a stated tolerance you name in the notes). `source_found` is false with a claim (`inferred` or `absent`) when a firm keeps no transaction feed. The 2026-04-21 day must appear in at least one firm's `split_days`; `known_cusips_found_on_2026_04_21` is the number of the four ruled CUSIPs you find split that day (0 to 4; list none). `split_source.<firm>` = `{"source_found":bool,"source_description":"30+ characters (the declaration entry, never a bucket name)","columns_present":["tran_srcde","tr_cd","sb_cd"],"split_days":[..],"split_rows":n,"split_security_days":n,"measurable":n,"ratio_absent":n,"ratio_agrees_with_close":n,"ratio_disagrees_with_close":n}`.
3. **The served DELTA and the design.** `delta_projection` = `{"account_days_affected":{"49financial":n,"cottonwood":n,"inflection":n},"total_account_days_affected":n,"graded_disagreed_on_2026_04_21":n (the ruling states 920; state what you count),"claim":"measured|inferred|absent","statement":"60+ characters: how the count was derived (account-days that held a split security on a split day)"}`. `design` = `{"adjustment_formula":"60+ characters","new_inputs":["20+ characters each, at least one: what the pure core must receive (for example a per-(security, day) ratio table read by the loader)"],"reason_codes":["SPLIT_RATIO_ABSENT","SPLIT_UNADJUSTED_COMPARISON"]}`.
4. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~415/IB211-1_split_adjust_read.json` with exactly: `base_commit`, `read_date`, `producer`, `split_source`, `known_cusips_found_on_2026_04_21`, `delta_projection`, `design`, `notes` (at least three lines of 30+ characters: what each fact rests on, the objects read counted, the tolerance, what was not read), and the six counters (`functions_invoked`, `sign_ins_made`, `aws_writes_made`, `rows_written`, `figures_written`, `vendor_requests_sent`), all 0.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB211-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB211-1-AC1" cell_refs="IB-pr-572"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r211/p211_cells.py" . IB211-1-AC1</invocation><expect>IB211-1-AC1 PASS</expect></criterion>
<criterion id="IB211-1-AC2" cell_refs="IB-pr-572"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r211/p211_cells.py" . IB211-1-AC2</invocation><expect>IB211-1-AC2 PASS</expect></criterion>
<criterion id="IB211-1-AC3" cell_refs="IB-pr-572"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r211/p211_cells.py" . IB211-1-AC3</invocation><expect>IB211-1-AC3 PASS</expect></criterion>

<expected_criteria>IB211-1-AC1, IB211-1-AC2, IB211-1-AC3</expected_criteria>

What the checks grade: AC1 the producer sites verified at HEAD; AC2 per firm the columns, the split rows and days (trading days), the measurable and absent ratios summing to the security-days, the close-price agreement summing to the measurable, and 2026-04-21 found; AC3 the DELTA projection (per firm, summing to the total), the design inputs and both reason codes, notes, the six counters 0 and no long digit run (no CUSIP, no id). Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY on AWS: `s3api head-object`, `get-object` and `list-objects-v2` of EXISTING objects (positions and transactions partitions, closes) under the three firms' IRPT and source prefixes, `list`, `describe`. **Nothing is re-run against a served prefix, published, invoked, written to AWS, signed or sent. The producer is NOT run.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, invokes or sends; a need to run the producer; a CUSIP, account id, name or value in a tracked file; a need to type an object address for a NEW object. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W415-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~415/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 207 (round 1, workstream ~PD), cell `IB-pr-572`.
<owned_cells>IB-pr-572</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB211-1-AC1, IB211-1-AC2, IB211-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~415/IRPT_BCKEND.TO-IB-pr-572.read-the-split-adjusted-holdings-price-return-the-custodian-split-rows-the-measured-ratios-and-the-served-delta.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads existing partitions and the producer's code with the worker's own identity and writes one record; nothing is re-run, published or invoked, so no served byte moves; the fix moves served holdings_price_return and the guard's grading of account-days, so it lands later under a never-widen pair that counts the DELTA per account-day.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p211_cells.py IB211-1 dry-run at base on dell2 2026-10-15 ~12:0xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp tree the run created itself (the real calendar, a stub producer file, a synthetic record; removed): all three PASS; eighteen negatives, each failing its own arm: a wrong contribution line, a core that is not holdings_return, a missing declaration file, a short statement, a missing firm, wrong columns, a split day that is not a trading day, a measurable sum wrong, a close sum wrong, 2026-04-21 missing, more than four CUSIPs, a source not found claimed measured, a wrong total, a missing reason code, a short formula, short notes, a counter above 0, a CUSIP leaked into the record.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~415` (worktree `C:/dev/wk-IRPT_BCKEND-415`). Class SERVED (reads served partitions and writes only the worker's records).
</preflight>
