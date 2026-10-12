# TO IRPT_DASHBD.TO-DB-b-159 -- the size of a change of flow convention, both ways, on a copy: for every served account the account-days whose daily return differs between END and START and between END and MID, by size, and the same for each served window at the last served date

<to_id>IRPT_DASHBD.TO-DB-b-159</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~128</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>83</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-83 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_83_20261011.md` @3f7c91e682, section 3 item 2 | **Rows:** NONE | **Decomp cell:** `DB-b-159` (decomposition section 85) | **outcome_ref:** FWD-8 / C-FLOWTIME | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-128` (branch `wk-irpt-dashbd-83-128`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~128/`. Read first: the analysis above, whole (it is one page), and the records this order names.

**Why.** The served daily return uses END: a flow counts in the day's closing value. The tie-out shows END is not what the other
system uses. Before the CTO writes an addendum it needs the SIZE of a change: "for every served account, the account-days whose daily
return differs between END and START, and between END and MID, by size (under 1 basis point, 1 to 10, over 10); and the same for each
served window (month to date, year to date, since inception) at the last served date. On a copy; nothing served."

**The cell (`DB-b-159`).** A read and a private recomputation. You change no code and write nothing served.
1. **The served rule.** Read how the served daily return is computed and where the flow enters it: the producer under
   `infra/aws/lambda/investor-reporting/` (start at `account_return_daily.py`; verify the path) and the PRD's C-METHOD. Cite file and
   line for the END rule. Read how the tie-out's relink function restates a return under START and MID (the proposal's
   `definitions_cited.admitted_timings` names it) and use THAT definition, so your restatement is the one the 51 were scored with.
2. **The copy.** Read the served daily account-return objects for the one firm into a private folder
   (`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~128/`). `served_accounts`, `account_days`, the date range.
3. **Control first.** Restate every account-day under END from its inputs and compare with the served return: `end_reproduces`
   {account_days, equal_within (the tolerance you used, in basis points), not_equal}. If END does not reproduce on a material share,
   STOP the banding, report what you measured and file a row: a restatement that cannot reproduce the served number sizes nothing.
4. **Daily.** `daily`: {end_vs_start, end_vs_mid}, each {differing_days (the absolute difference is above zero at the precision the
   served file carries: say the precision), bands {under_1bp, from_1_to_10bp, over_10bp}, flow_days (the account-days carrying a
   flow), largest_band_note}. The bands sum to differing_days.
5. **Windows.** At the last served date (`windows.as_of`), for month to date, year to date and since inception, chain the daily
   returns as the served file does (cite the rule) under END, START and MID: `windows`: {as_of, mtd, ytd, itd}, each
   {end_vs_start, end_vs_mid}, each {accounts (accounts carrying that window), bands (the same three, on the absolute difference of
   the window return)}. The bands sum to accounts (an account with no difference sits in under_1bp).
6. `on_a_copy: true`, `s3_writes: 0`, `limits`. Keep your per-account-day table privately: the next cell (DB-b-160) reads it, so
   write beside it a short `README.txt` naming its columns. NO return value, account id, client name or amount in the record or your
   report: counts and bands only. Record `CONVENTION_CHANGE_SIZE.json`.
7. **In every record of this round (item 5): `the_39`** {count: 39, accrual_class: 31, unclassed: 8, statement}. The statement says in a
   sentence that 39 of the 90 two-sided segments close under NO timing (31 of the accrual class, 8 unclassed), that nothing in this
   record changes them, and that a change of convention would not close the tie-out. A reader who quotes a number from your record
   must meet that sentence beside it.

<criterion id="DB83-2-AC1" cell_refs="DB-b-159"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r83/p83_round83.py" . DB83-2-AC1</invocation><expect>DB83-2-AC1 PASS</expect></criterion>
`DB83-2-AC1` -- on a private copy of the served daily returns, the days whose return differs under START and under MID are counted in three size bands, and each served window is banded the same way at the last served date. Base: FAIL.

<expected_criteria>DB83-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS READS allowed, through the `.tools/aws` shim or boto3 as the existing readers build their client, and nothing else: the served gold objects the Investor Reporting dashboard's producer writes for the ONE firm the tie-out reads (the daily account return, its flow and its guard flags), read into a private copy outside the repo. No write, no producer run against a served prefix, no other firm's prefix. A denial is recorded verbatim, not retried by another route.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~128/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W128-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~128/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-159.convention-change-size-on-a-copy.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 85 (round 83), cell `DB-b-159`.
<owned_cells>DB-b-159</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB83-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~128/IRPT_DASHBD.TO-DB-b-159.convention-change-size-on-a-copy.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB83-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the served accounts and account-days read; for END to START and END to MID, the differing days in the three bands; for each of the three windows the accounts in the three bands, both ways; how you restated the return and where the served rule is (file and line); that your END restatement reproduces the served return, with the count; the sentence on the 39; what you could not establish; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a private recomputation and a count record; nothing served is written or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; governed reads; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
