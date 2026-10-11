# TO IRPT_BCKEND.TO-IB-pr-457 -- READ ONLY: the date-basis producer's design as a read -- where the module would be called, what it would serve, every consumer; and the short-history count

<to_id>IRPT_BCKEND.TO-IB-pr-457</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~313</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>153</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msgs 5896 and 5933 (PRD v0.44 @84fec7b9b4, ratified-text half SIGNED @7b75b691c1) | **Decomp cell:** `IB-pr-457` (decomposition section 145) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-313/` (bash `/c/dev/wk-irpt-bckend-313`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it). **A READ, NOT A BUILD.** You edit no product file, build no producer, no schema, no
`sources.json` entry and no schedule, and you write no order for one: you describe what exists and what a producer would need.
READ ONLY toward AWS. For the ONE count below: ONE external source, Yahoo Finance through the repo's reader, ONE PASS (count the
distinct tickers BEFORE fetching; above 1,500 STOP and file a row; each ticker asked once, at most 50 a call, paced, never in
parallel; nothing re-asked). NO YCharts call, NO Bloomberg call. Counts only: no account id, balance or holding of an account.

**The contract.** PRD ADDENDUM v0.34 (search `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` for `## ADDENDUM v0.34`)
says where the claim is to live: the entry's basis is declared `PER_ACCOUNT_DAY` in `sources.json`; the HOLDINGS GOLD carries,
on every account-day, a `date_basis_claim` the grading instrument measured; a RETURN is served for an account-day only when that
day and the prior trading day each read own-date or nothing-to-grade; the anchor lands about 09:46Z and the firm's partition
about 11:46Z the next day, so day t is graded the day after by a SCHEDULED producer that runs after both; and "the release that
first serves this gold names every reader of the holdings gold and of the performance route with its key policy, and one read
through each, in its pair." Addenda v0.35 to v0.44 (the end of the PRD) fix the rule; the module that implements it is
`data/assets/scripts/gold/irpt_reporting/date_basis_grading.py` (merged; no importer, no producer). Read both whole.

**Read and state, each with `file:line` and a claim (`measured` = read in code or config at your base):**
1. **`what_is_served_today_for_the_date_basis`:** what the holdings gold and the performance / returns path serve TODAY for the
   firm this rule is about (the one whose silver holdings source the earlier reads used; name the `sources.json` entry by its
   key, not by a firm's name in prose): does any `date_basis` member exist on a served artifact, a route or a schema today,
   what value does it carry, and who writes it (search the native Grep tool for `date_basis`, `price_basis`, `PER_ACCOUNT_DAY`
   under `data/assets/scripts/gold/`, `infra/aws/lambda/investor-reporting/`, `docs/contracts/` and `portal/` if present).
2. **`candidate_call_sites`:** every place the module could be called to produce the claim: the gold producers under
   `data/assets/scripts/gold/irpt_reporting/` (`account_return_daily.py`, `account_class_daily.py`, `account_activity_lots.py`),
   `data/assets/scripts/gold/irpt_holdings_performance/`, the reporting-gold Lambda under
   `infra/aws/lambda/investor-reporting/reporting-gold/`, and any other producer that writes the holdings gold or the returns
   (find them; `comp-pipescript io <script>` and `comp-pipescript postdeps <script>` say what each reads and feeds). For each:
   `site`, `code_line`, `schedule_or_trigger` (the EventBridge rule, Step Function or cron that runs it, read from Terraform or
   the schedule registry; `comp-schedule` may answer; "none found" is an answer), `inputs_in_hand` (what it has loaded at that
   line), `inputs_the_module_needs_and_the_site_lacks`, `serves_today` (the artifact and its address as the code builds it),
   and whether its run time is AFTER both the anchor and the partition land (state the two landing times you can read from
   schedules or records, with their claim).
3. **`module_inputs`:** each input the module's functions take (the account-day's rows, the first witness's closes for the day
   and the prior trading day, the second witness's bars over the 40-day window, the security types by CUSIP, the calendar),
   and `where_it_lives_today`: an S3 address a producer already reads, a cache, or NOWHERE a scheduled producer can read
   (the second witness's bars were fetched from Yahoo Finance by measurement scripts into scratch: say plainly whether any
   scheduled, landed source of those bars exists in the estate; search for an existing landed Yahoo close store with
   `comp-find` and the gold / silver scripts that read `read_yahoo_close`; a reader that fetches at run time from a scheduled
   producer is a design fact the CTO must see, with its egress and its failure mode).
4. **`consumers`:** EVERY consumer of the date-basis member AND of the holdings gold and the returns it would ride on, by
   subtraction: `files_naming_the_member_or_the_gold` (`total`, and each file placed as `consumers`, `writers` or `neither`),
   then `list` (each: `consumer`, `code_line`, `kind` from the kinds you declare, e.g. producer, lambda_reader, route, schema,
   page, test; `on_absent` / `on_unknown_value` / `on_blank`: what it does when the member is missing, carries a value it does
   not know, or the account-day is blank; and `read_a_release_makes_through_it`: the ONE read, named exactly, that would show
   after a release that this consumer reads the gold correctly). `by_kind`, `searched_for`, `not_searched` (for example the
   portal if its submodule is empty in your worktree: say so, never count it as zero).
5. **`short_history_count`** (the CTO's one count, computed BY THE PRODUCT MODULE over the same 85 graded days and nine pairs
   as IB-pr-454; reuse its driver in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~310/` and its record
   `IB150-1_product_form_run.json`; cache in `C:/dev/_scratch313/`, outside the worktree, deleted file by file at the end):
   the rule (window 40, floor 20) leaves a security-day ungraded either because the security is mostly repeating or because
   fewer than 20 days can be compared. Split them: `security_days_not_graded_by_the_rule` = `of_which_short_history_only` +
   `of_which_repeat_rule_with_a_full_or_sufficient_window`. Then the NEWLY HELD question: a security first held by any account
   inside the run has no history of the firm's holding, but its BARS exist from before; say which the floor reads (bars, not
   holdings: confirm from the module) and state `newly_held_rule_in_words`. Count `securities_ever_short_of_history` (short of
   20 compared days on one or more graded days), `newly_held_securities_blank_for_their_first_window` (securities that are
   ungraded for short history on the days after they are first held; 0 is an answer if the bars pre-date the holding),
   `account_days_blank_only_for_short_history` (account-days that would be freed but for a short-history security), and for a
   security that began TRADING inside the run (no bars before), how many there are and how long each stays ungraded
   (`securities_that_began_trading_inside_the_run`). `computed_by: "the product module"`.
6. **`open_design_questions`:** the questions a producer's PRD addendum must answer that this read cannot (a list of plain
   questions, each with what would settle it). Not a design. **`not_established`.**

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~313/`: `IB153-1_producer_design_read.json` with
the members named above plus `base_commit`, `product_files_edited: 0`, `builds_proposed_as_orders: 0`, `served_changes: 0`,
`other_sources_asked: 0`, `claims_regraded_in_product: 0`; your driver script; and a one-page
`IB153-1_PRODUCER_DESIGN_READ.md` in plain sentences, each with its claim, written for the reader who will write the addendum.

<criterion id="IB153-1-AC1" cell_refs="IB-pr-457"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r153/p153_cells.py" . IB153-1-AC1</invocation><expect>IB153-1-AC1 PASS</expect></criterion>
<criterion id="IB153-1-AC2" cell_refs="IB-pr-457"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r153/p153_cells.py" . IB153-1-AC2</invocation><expect>IB153-1-AC2 PASS</expect></criterion>
<criterion id="IB153-1-AC3" cell_refs="IB-pr-457"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r153/p153_cells.py" . IB153-1-AC3</invocation><expect>IB153-1-AC3 PASS</expect></criterion>

<expected_criteria>IB153-1-AC1, IB153-1-AC2, IB153-1-AC3</expected_criteria>

The checks grade the shape: cited lines, claims, the subtraction's arithmetic, the count's two parts summing, the five zeros.
Every answer is UNMEASURED by the issuer; "none found" and "it cannot be told" pass where true.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited; nothing is built.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row and report. Never weaken a check; do not edit
  `p153_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W313-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~313" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~313@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~313 <0.9.0_WK_IRPT_BCKEND~313@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~313/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-457.date-basis-producer-design-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 145 (round 153, workstream ~P), cell `IB-pr-457`.
<owned_cells>IB-pr-457</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB153-1-AC1, IB153-1-AC2, IB153-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~313/IRPT_BCKEND.TO-IB-pr-457.date-basis-producer-design-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; what is served today for the date basis; the candidate call sites with their
schedules and what each lacks; where each module input lives, and whether a landed source of the second witness's bars exists;
the consumers by kind with the subtraction's counts and what was not searched; the short-history count with its two parts and
the newly-held answer; the open design questions; what is not established; each criterion's last line; the proof checker's
result; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read written to the worker's own deliverables folder; nothing is edited, built or served. The consumer census this cell produces is the blast-radius input of the LATER served change's pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; S3 reads the earlier cells of this chain already made.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; schedules are read.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p153_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~22:1xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The sign-off of v0.44 was read by the issuer as a COMMIT (7b75b691c1, author 3.0.0_SA_CVO), not from the tool's status line, which printed SIGNED before that commit existed. The issuer read PRD v0.34's served-design paragraph at lines 772-800 and v0.44's tail. The worktree is cut at the issuance commit (HEAD at the cut) and the face has the worker state its base (row IRPT_BCKEND-D2-S99).
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
