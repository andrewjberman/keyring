# TO IRPT_DASHBD.TO-DB-b-140 -- the 18 tie-out segments where the custodian's flow rows do not reproduce the served flow day by day: read day by day until the difference has a cause -- counts and cause only

<to_id>IRPT_DASHBD.TO-DB-b-140</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~113</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>74</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-74 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_74_20261011.md` @d8b69fa413, its one cell, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v30.md` @dbf7c2e292 | **Rows:** IRPT_DASHBD-D2-W111-S1 | **Decomp cell:** `DB-b-140` (decomposition section 76) | **outcome_ref:** FWD-12 (the tie-out) | **depends_on:** DB-b-138 (drained @9ff4f71824).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-113` (branch `wk-irpt-dashbd-74-113`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~113/`. Read first: the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v30.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**What is open (row D2-W111-S1).** DB-b-138 read the 51 flow-timing-class segments against the custodian's transaction rows. In all 51
the custodian's flow DAYS equal the served flow days; but in 18 of them the custodian's external-flow day TOTALS differ from the served
flow dollars, on 50 flow days, and excluding fee rows does not reconcile them (record
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~111/CONTESTED_51.json`). The CTO: "Read them day by day until the difference has a
cause; counts and cause only. Until then the tie-out is shown with 51 contested, 18 unreproduced and 8 unclassed beside it and is not
called closed." **The 18 are a subset of the 51 contested**, not a fourth group: keep the denominators that way.

**The cell (`DB-b-140`).** Read-only; you change no code and no served thing. Workers ~108's and ~111's per-segment tables, downloads
and scripts are outside the repo under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~108/` and `.../0.9.0_WK_IRPT_DASHBD~111/`; read
them in place and reuse their readers. Yours go under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~113/`.
1. **Take the 18 and their differing flow days** from ~111's table and reproduce both counts (18 segments; 50 flow days). A
   different count is a STOP with a row.
2. **Day by day.** For each differing flow day, put the custodian's rows for that account and day beside the served flow for that day
   and find what makes the difference, from the rows themselves: a transaction TYPE the served flow counts and the custodian's
   external-flow total does not (or the reverse): transfers between accounts, journal entries, dividends or interest taken as cash,
   reinvestments, corporate actions, a reversal and its re-entry, a row posted on one date and effective on another, a security
   delivered in or out in kind. Read how the SERVED flow is built (the producer's flow rule in
   `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` and what it reads) so you compare like with like, and say what you
   read (file and line).
3. **Causes.** `causes`: [{cause, segments, flow_days, rule}]: a segment sits under the cause that explains ALL of its differing days;
   a segment whose days have different causes sits under a cause named for the combination, or under `no_cause` if any day is
   unexplained. A cause is a rule over the rows a reader could re-apply, to the cent or within a stated tolerance, never a guess.
   `no_cause` {segments, flow_days, why}. The segments sum to 18. `flow_days` {total, differing}.
4. **Whether it matters to the tie-out.** For the explained segments, say in one sentence per cause whether the difference is in what
   the custodian's "external flow" means (a definition) or in the served flow itself (a defect in the served number, which is a row).
   Do not rule on the contested timing question: it stays contested.
5. **The tie-out's state**, restated: `tieout_state` {total: 244, classed: 185, contested: 51, unclassed: 8,
   unreproduced_within_contested (the segments still under `no_cause`, at most 18), called_closed: false}.
6. `client_figures: 0`, `s3_writes: 0`. Counts, transaction TYPE names and rules only in the repo and in your report: no account id,
   no client name, no dollar amount. The check refuses a record holding any run of 8 or more digits. Record `UNREPRODUCED_18.json`.

<criterion id="DB74-1-AC1" cell_refs="DB-b-140"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r74/p74_round74.py" . DB74-1-AC1</invocation><expect>DB74-1-AC1 PASS</expect></criterion>
`DB74-1-AC1` -- each of the 18 segments is read flow day by flow day and placed under a cause with a rule or under no cause with why, and the tie-out's state is restated and not called closed. Base: FAIL.

<expected_criteria>DB74-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS READS allowed, through the `.tools/aws` shim or boto3 as the existing readers build their client, and nothing else: 49 Financial's OWN Black Diamond transactions tree, its valuation tables and its served `account_return_daily` gold, exactly the prefixes workers ~108 and ~111 read (take them from their scripts, never typed), limited to the accounts and windows of the 18 segments, and only if their existing download does not already hold what you need. No other firm's prefix, no other bucket. A denial is recorded verbatim (`read_denied`), not retried by another route.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~113/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W113-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~113/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-140.unreproduced-18-flow-days-read-day-by-day.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 76 (round 74), cell `DB-b-140`.
<owned_cells>DB-b-140</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB74-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~113/IRPT_DASHBD.TO-DB-b-140.unreproduced-18-flow-days-read-day-by-day.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB74-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; how you took the 18 and the differing flow days; ONE table of causes: cause, segments, flow days, the rule; the segments with no cause and why; the tie-out's state; what you read; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; reads of one firm's custodian tree and its served gold; nothing served, nothing written but a record.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; governed reads; a denial is a result and is not widened.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
