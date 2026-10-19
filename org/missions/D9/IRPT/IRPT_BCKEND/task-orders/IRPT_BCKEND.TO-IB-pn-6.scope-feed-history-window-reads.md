# TO IRPT_BCKEND.TO-IB-pn-6 -- Two READ-ONLY reads for ADDENDUM 5: the history window (earliest start date, N) and the size of the first run's feed objects (CTO ruling @2f780e14a6)

<to_id>IRPT_BCKEND.TO-IB-pn-6</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~N2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>
<workstream>~PO</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` ruling `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO~DELL2/RULING_IB_PN5_BRONZE_ENVELOPE_FIX_WRITER_FIRST_20261019.md` (@2f780e14a6): "IB2's two read-only reads may run now" | **Decomp cell:** `IB-pn-6` (`IRPT_BCKEND_DECOMP_R11_N.md`) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pn-6` (inlined).** The history backfill of the Scope account feed (ADDENDUM 2) is held while the issuer's worker fixes the bronze writer (order `IRPT_BCKEND.TO-IB-pn-5`). The CTO's ADDENDUM 5 will carry two measured facts that only you can read: how far back the history window goes, and how big the first scheduled run's feed objects are. **This order is READ ONLY: nothing is written to AWS, no Orion request is made, no ledger is opened.** Paths you post are `file:///` absolute URIs or markdown links to them, with the repo-relative form for another box (CLAUDE.md rule 33). No identifier of any account, household or client goes in any record or message: counts, dates, bytes and flags only.

**Do, in this order. A STOP is reported to the issuer and writes nothing further.**

1. **First run's day (READ).** List the feed's bronze table prefix (the address the builder gives for source `orion`, scope `inflection`, tier bronze, table `scope_account_returns`; `lib/opal_naming.address()` or the live `scope_feed_addresses.json` sidecar beside the script) for `date=` partitions. Exactly ONE is expected (the 2026-10-18 chain's day); if there are none or more than one, STOP and report the count. Record that day as `first_run_day`.
2. **The roster (READ).** Take the newest roster snapshot and the positions silver for `first_run_day`, and form the feed's universe the way the script does (accounts in roster membership that are held on that day). Record: `earliest_start_date` (the minimum non-null `accountStartDate` over that universe), `accounts_in_universe`, `accounts_with_null_start_date`, and `household_count` (distinct households of the newest roster snapshot; at most 294). `day_count_n` is the number of days from `earliest_start_date` to `first_run_day` (their date difference); `n_within_limit` is true when `day_count_n` is at most 4000 (the script's `MAX_FROM_DAYS_BACK`). You may run the script's own PLAN-ONLY mode (`--from-date <earliest_start_date> --pull-date <first_run_day>`, NO `--upload`; it prints `PLAN ONLY: no Orion call and no write`) in a flat directory built from the live code prefixes, as in step 4(b)(iii) of `IRPT_BCKEND.TO-IB-pn-4`, to cross-read `days=` and `households=`; the record rests on your own reads either way.
3. **The size of the first run's objects (READ).** For the bronze key and the silver key of `first_run_day`: key count (1 each), version count (1 each expected) and `ContentLength` in bytes (head or list; no object body is downloaded).
4. **Write the record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IBN6-1_reads_record.json` with exactly these members and no others: `{"reads":{"read_at_utc":"<YYYY-MM-DDTHH:MM:SSZ>","first_run_day":"<YYYY-MM-DD>","earliest_start_date":"<YYYY-MM-DD>","day_count_n":<int>,"n_within_limit":<true|false>,"household_count":<int>,"accounts_in_universe":<int>,"accounts_with_null_start_date":<int>,"bronze_object":{"keys":1,"versions":1,"bytes":<int>},"silver_object":{"keys":1,"versions":1,"bytes":<int>}},"aws_writes_made":0,"orion_requests":0}`. Commit it with `bash .tools/safe-commit.sh --author "0.7.0_AE_CloudOps~IB2 <0.7.0_AE_CloudOps~IB2@opal.agent>" -F <msgfile> -- <paths>`.
5. **Run the three criteria below** from the repository root under `timeout 120`, record the output and exit code verbatim in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IBN6-1_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`. Commit them, then flip this order's `<status>` to `complete` only when every criterion passes. **Report once to the issuer, under 150 words:** `day_count_n`, `n_within_limit`, the two byte sizes, `household_count`.

**Criteria (run each under `timeout 120` from the repository root, record the output and exit code verbatim):**

<criterion id="IBN6-1-AC1" cell_refs="IB-pn-6"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r11/pn6_cells.py" . IBN6-AC1</invocation><expect>IBN6-AC1 PASS</expect></criterion>
<criterion id="IBN6-1-AC2" cell_refs="IB-pn-6"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r11/pn6_cells.py" . IBN6-AC2</invocation><expect>IBN6-AC2 PASS</expect></criterion>
<criterion id="IBN6-1-AC3" cell_refs="IB-pn-6"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~N2/checks/r11/pn6_cells.py" . IBN6-AC3</invocation><expect>IBN6-AC3 PASS</expect></criterion>

<expected_criteria>IBN6-1-AC1, IBN6-1-AC2, IBN6-1-AC3</expected_criteria>

What the checks grade: AC1 the roster read (the earliest start date not after the first run's day, `day_count_n` equal to their date difference, the limit flag consistent, households within 294, account counts consistent); AC2 each of the two objects one key, one version, bytes above zero; AC3 read-only (no write, no Orion request) and the record holds exactly the named members. Do not edit the checks. If the order STOPS, the criteria are not run; report the stop and its reason.

## BOUNDS

- **Grant:** READ ONLY. S3 list, head and version reads of the feed's bronze and silver table prefixes, and reads of the newest roster snapshot and the positions silver (schema, dates, counts), the sidecar and code prefixes if you run the PLAN-ONLY cross-read; the record folder and this order file in git. **No S3 write, no object delete, no Lambda invoke, no chain trigger, no runner start or stop, no IAM, schedule, Terraform or catalog change, no Orion request, no ledger entry.**
- **Refusal clause:** STOP and report, writing nothing further, on any of: a need to write anything to AWS; an Orion request; the feed's bronze prefix holding no `date=` partition or more than one; a household count above 294; an object with more than one version or key; a read that needs a grant you lack (name the surface that refused). A STOP is reported, not worked around.
- **Feed keys are production output, not test objects.** Read them; never touch them.
- **Row ids:** put the row text in your report; the issuer appends it as `IRPT_BCKEND-D2-S<k>`. **Report under 150 words.**
- **Your queue:** read-only, so it waits on no ledger window; do it after your open acts of the day.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pn-6.scope-feed-history-window-reads.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R11_N.md</decomp_doc> round 11, workstream ~PO, cell `IB-pn-6`.
<owned_cells>IB-pn-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBN6-1-AC1, IBN6-1-AC2, IBN6-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pn-6.scope-feed-history-window-reads.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- read only: S3 list, head and version reads of two feed objects and the roster and positions silver; the only write is the seat's record file in git. No served byte moves, nothing is deployed, no Orion request.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; a missing read grant is a STOP.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- pn6_cells.py dry-run at base on dell2 2026-10-19 ~14:1xZ: AC1, AC2, AC3 FAIL (no record). control_pn6.py in a temp root it built itself: a synthetic good record passes all three; nine negatives (N not the days between, earliest after the first run, limit flag wrong, households over the bound, null count over accounts, bronze bytes zero, silver two versions, a write made, an Orion request made) and an added identifier member each fail only their own arm; 0 unexpected.
lane: the paths block IS the grant; seat `0.7.0_AE_CloudOps~IB2` (dell2). Class WORLD (read only). Not measured by me: the roster, the positions silver, the feed's objects, the household count (all read by the seat and each a STOP if it breaks the order).
authority: workstream ~PO is this seat's under the CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md` Move 1; the reads are authorized by the CTO ruling `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO~DELL2/RULING_IB_PN5_BRONZE_ENVELOPE_FIX_WRITER_FIRST_20261019.md`.
</preflight>
