# TO IRPT_DASHBD.TO-DB-b-162 -- on the 234 flow-bearing days behind the 51 segments, a count by when the deposited cash was first invested -- same day, next trading day, later, never in the window -- under a rule written before the count, on a copy; a read, not a ruling

<to_id>IRPT_DASHBD.TO-DB-b-162</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~131</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>84</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 6130 (2026-10-11 ~23:29Z) | **Rows:** NONE | **Decomp cell:** `DB-b-162` (decomposition section 86) | **outcome_ref:** FWD-8 / C-FLOWTIME | **depends_on:** DB-b-158 (drained @6fe2f4518b).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-131` (branch `wk-irpt-dashbd-84-131`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~131/`. Read first: the records this order names.

**Why.** The tie-out shows the other system does not use END for flow timing and cannot tell START from MID; nothing either party
publishes says which. PRD v0.11 keeps END by default and writes no winner. The CTO, from the reviewer's note (msg 6130): "one cell
[...] a read and not a ruling: on the 234 flow-bearing days, a count by when the deposited cash was first invested (same day, next
trading day, later, never in the window), under a rule written before the count, on a copy. It will not pick a convention; it gives
Andrew a fact about these accounts beside the vendor's answer."

**The cell (`DB-b-162`).** A read and a private count. You change no code and rule nothing.
1. **The rule FIRST, committed before any count.** Before you read a single transaction of these accounts, write `RULE.md` in your
   folder and commit it alone. It states, so that another seat would count the same way: what a DEPOSIT day is (a flow-bearing day
   whose net external flow is cash coming in: name the column and the sign) against a WITHDRAWAL day and any OTHER day (transfers in
   kind, mixed days: say how each is told apart); what "invested" means (the first purchase of a security in that account, by which
   transaction types, excluding money-market sweeps and reinvested income if the data lets you tell them: name the types you will
   count and the ones you will not); what size counts (any purchase, or one that is at least a stated share of the deposit: pick one
   and say why); the trading calendar used for "next trading day" (`lib/trading_calendar.py`); and the WINDOW (the segment's own end
   date, so "never in the window" means no qualifying purchase from the deposit day to the segment's end). Also what goes in
   `not_determinable`. You may read CODE and SCHEMAS (column names, type vocabularies) to write the rule; you may not look at these
   accounts' rows. If, after the count starts, the rule proves unworkable, do NOT edit it: add a dated `RULE_ADDENDUM.md`, say what
   changed and why, and report the count under BOTH readings.
2. **The days.** Take the 234 flow-bearing days and the 49 accounts from DB-b-158
   (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~127/FLOWTIME_DENOMINATOR.json` and its tracked script, which reads the private per-segment
   tables). If you count a different number, state both. `flow_bearing_days`, `deposit_days`, `withdrawal_days`, `other_days`,
   `accounts`.
3. **The count.** For each deposit day find the first qualifying purchase in that account on or after it, from the transactions
   store an earlier tie-out cell read (DB-b-151's record names the stores: say which you read and why; if the copy and the original
   differ for these days, say so). `classes`: {same_day, next_trading_day, later, never_in_window, not_determinable}, summing to
   `deposit_days`. Also, as counts: `later_trading_days` in three bands (2 to 5, 6 to 20, over 20) and `deposits_into_accounts_with_
   a_standing_purchase_plan` if you can tell (else omit).
4. **What it is not.** `picks_no_convention: true`, with `what_it_cannot_say`: a same-day purchase does not show the custodian
   counted the cash from the start of the day; the count describes these accounts' trading, not either system's method.
5. `rule` {file: "RULE.md", sha256 (of the file's bytes as committed), commit (the hash that carried it), written_before_count:
   true}; `on_a_copy: true`; `s3_writes: 0`; `limits`. NO account id, client name, amount or security name in the record or your
   report: counts only; days with separators. Private files under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~131/`. Record
   `FLOW_DAYS_FIRST_INVESTED.json`.
6. **`the_39`** {count: 39, accrual_class: 31, unclassed: 8, statement}: 39 of the 90 two-sided segments close under NO timing; nothing
   here changes them; a change of convention would not close the tie-out.

<criterion id="DB84-1-AC1" cell_refs="DB-b-162"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r84/p84_round84.py" . DB84-1-AC1</invocation><expect>DB84-1-AC1 PASS</expect></criterion>
`DB84-1-AC1` -- the rule is written and committed before the count and its bytes are unchanged, the flow-bearing days are split into deposit, withdrawal and other days, and every deposit day is placed in one of five classes. Base: FAIL.

<expected_criteria>DB84-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS READS allowed, through the `.tools/aws` shim or boto3 as the existing readers build their client, and nothing else: for the ONE firm the tie-out reads, the transactions of the accounts behind the 51 segments on and after each flow-bearing day (the store an earlier tie-out cell read them from, named in its record), read into a private copy. No write. No other firm's prefix. A denial is recorded verbatim, not retried by another route.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~131/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W131-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~131/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-162.flow-days-by-when-cash-was-first-invested.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 86 (round 84), cell `DB-b-162`.
<owned_cells>DB-b-162</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB84-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~131/IRPT_DASHBD.TO-DB-b-162.flow-days-by-when-cash-was-first-invested.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB84-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the rule in its own words and the commit that carried it before the count; the flow-bearing days split into deposit, withdrawal and other; the five class counts; how many accounts; which store the transactions came from; what the count cannot say; the sentence on the 39; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a private count and a count record; nothing served, nothing ruled.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; governed reads; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
