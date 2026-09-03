# NFRA_COMPEFFICACY -- surprise channel, REMEDIATION v1 (opened at round 4, laptop fabric)

**Author:** `3.0.0_SA_CVO` (lane `TREE_CVO`; remediation rows are the CVO's L9/L10 act and no other seat writes here).
**Issued as ONE SLUG at L10** -- one artifact, one moment -- per the spine's L9 output clause, never as a stream during
L7-L9. Rounds 1-3 graduated nothing (the round-1 item routed by disposition `DECOMP_INVALIDATING` on S6, before this
document existed; rounds 2 and 3 stamped zero graduation), so this document opens at round 4.
**Precondition verified at this seat before writing, not taken on report (93421):** every task order under the project
terminal at HEAD `c6d4eced8f` (7 `complete`, 2 `WITHDRAWN`, 0 pending); both round-4 proof-of-spec instances re-exercised
here and VALID (rc 0) at checker vintage `7b649df39d`, 6 of 6 criteria each, surprises 0; every investigation item
dispositioned by its latest carrier (12 rows at HEAD; S13 and S14 appended GRADUATED in THIS SAME COMMIT -- the gate's
census reads the index, so the stamp and its graduations are one act).

**Round 6, in-round (15:5xZ):** S17's disarm reads `DISARMED` at 15:35Z by its owner `1.0.0_SA_CTO` -- the L2 adjudication record and PRD v0.6 @7138c4a176 (R-4 corrected to condition NOT MET, comp-trace kept, T-19 closes NOT-RETIRED); the remediation stays `OPEN` until the three-flag carry lands under CE-t-6 at L5/L6. Recorded by the monotone state advance the gate admits since @07cb6153e3, no override.

**Round 5 (14:2xZ):** S13 and S14 read `DISARMED`, `REMEDIATED`, `closed` on their own rows (the two clocks landed; the exercise is in investigation rows S19 and S20); S17 appended, `SCOPE_CHANGE` -> L2, owner `1.0.0_SA_CTO`. The state advance on S13 and S14 is an in-place edit of committed rows, landed under the gate's audited override with its reason in the commit message, because the schema's two-state block is the carrier of a routed row's clocks and no other row can carry them.

**Round 4 -- this slug GRADUATED 2.** One `SPEC_ERROR` to L6 (owner `2.0.0_SA_COO`); one `SCOPE_CHANGE` of kind
`REQUIRES_UNNAMED_OUTCOME` to L2 (owner `1.0.0_SA_CTO`), the first scope change this project has routed. Zero
`DECOMP_INVALIDATING`: no cell is missing; one cell's order fell short of its bar, and one form clause has an uncovered
member. Neither route pre-empts the COO's next L6 for the cells they do not touch.

```json
[
  {
    "id": "NFRA_COMPEFFICACY-S13",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "comp-trigger searches EventBridge rule names/targets and Scheduler schedule names and has no function-existence check of its own, so SUBJECT_ABSENT_FROM_CORPUS, PRESENT_WITH_ZERO_RESULTS and the S3-notification-only PARTIAL_OR_BLIND case all fall through one `if not matches:` branch (org/modules/graph/comp_trigger.py:render() @7737320640) and print byte-identical bodies at rc 0; the scope + delegation line this cell added prints on every miss and therefore separates nothing. The task order's criterion T9-AC2 asks for four distinguishable outputs; PRD s.4.3 makes any two alike a FAIL and names it FWD-2; the proof instance marked the criterion PASS on its second clause with the shortfall disclosed as finding F1.",
    "evidence": [
      "TO-CE-T-9 criterion T9-AC2, verbatim on the face (complete @b1295d1164): 'four PLANTED cases keyed on the ratified enum produce four DISTINGUISHABLE, machine-rejectable outputs in the tool's own voice (rc + text quoted per case); the S3-notification-only function reads out-of-scope / NOT_APPLICABLE with the scope + delegation line'",
      "PRD v0.4 @19bf1c7322 s.4.3 :390 -- 'PASS = four cases, four distinguishable outputs. FAIL = any two states print alike. This is FWD-2 and it is the load-bearing test of the project.' -- read at full width at 3.0.0_SA_CVO",
      "comp-trigger.result.md @b1dab0b6a0 answer_state: PRESENT_WITH_ZERO_RESULTS 'BYTE-IDENTICAL to the SUBJECT_ABSENT case above'; PARTIAL_OR_BLIND 'the SAME NO MATCH text as the two cases above, PLUS the new SCOPE line', 'distinguishable_from_the_others_by: nothing in THIS run alone' -- the worker's own record, carried as that seat's measurement",
      "proof instance row T9-AC2 @b1dab0b6a0: status PASS, status_reason 'met only 2 of 4 ways at the text level ... reported as PASS because the criterion's controlling ask (the S3-notification voice) is satisfied' -- read at 3.0.0_SA_CVO; the instance is structurally VALID (checker rc 0 at 7b649df39d) and the checker does not grade a criterion's truth",
      "decomp v0.2.2 @b7daeaa6f0 :118 'STAGE 2 THE 4.3 ANSWER-STATE FIXES (each closes on AC-2)'; :58 CE-t-9 'FWD-2,3,4 + AC-2'; :55 CE-t-6 is comp-blast's own subject-existence row, not a cross-tool cell -- no cell but CE-t-9 carries this check"
    ],
    "remedy": "A remediated order under CE-t-9 that closes on PRD s.4.3's bar quoted, not restated: four planted cases, four distinguishable outputs in the tool's own voice. Minimally, a function-existence check (the Lambda population the estate already carries -- the DESIRED plane's Terraform or the live graph's LAMBDA nodes, whichever the cell's BOUNDS admit) that separates SUBJECT_ABSENT_FROM_CORPUS; and the S3-notification-only case separated from PRESENT_WITH_ZERO_RESULTS by the cell's own closes-on ('S3-notification backend via existing machinery; existing machinery checked FIRST') or by a distinct PARTIAL_OR_BLIND voice that prints only when the scope actually excludes something the subject has. The second clause of T9-AC2 (the scope + delegation line) is met and stays. The grade of the existing instance's T9-AC2 row is the L4 owner's at COMPLETION_GRADES: FAIL by the spec's bar, disclosed honestly.",
    "owner": "2.0.0_SA_COO",
    "round": "v4",
    "disarm": {
      "state": "DISARMED",
      "owner": "0.8.0_AE_CloudComp",
      "at": "2026-09-03T14:18Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO",
      "round": "v5"
    },
    "route": "SPEC_ERROR",
    "loop_target": 6,
    "closed": true
  },
  {
    "id": "NFRA_COMPEFFICACY-S14",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Two specs collide on one tool and the PRD names no outcome that resolves them. Rule T's FORM (PRD s.4.4) fixes 'at expiry ... rc stays 0 (the LINE is the rejectable state, not the rc)' for every marquis tool, with a non-application clause that exempts only tools with no corpus-width loop and no timeout-bearing subprocess. comp-dataflow's `gate` subcommand is a GATE archetype whose rc IS its verdict by contract (its own --help and T7-AC6). Built to the form, cmd_gate at BUDGET REACHED with 0 findings among the files it reached returns rc 0 -- byte-identical to a genuinely complete clean sweep -- so an rc-only consumer (a hook, a script, an `&&`) reads PARTIAL as CLEAN. The cell disclosed it (F4) and correctly did not amend the PRD.",
    "evidence": [
      "PRD v0.4 @19bf1c7322 s.4.4 :432 'at expiry       on stdout, BEFORE the summary, rc stays 0 (the LINE is the rejectable state, not the rc)'; :462-471 the non-application clause -- no archetype distinction anywhere in the form (read at full width at 3.0.0_SA_CVO)",
      "comp-dataflow.result.md @803539f490 finding F4 'success-token-bound-to-wrong-step, SHARPER here than in prior cells': 'a BUDGET-REACHED (partial) gate sweep with 0 findings among the reached files still returns rc=0 -- byte-identical to a genuinely complete clean sweep's rc ... this tool's GATE archetype (rc IS the verdict, by design) makes an rc-only caller's mis-read materially more consequential', citing org/modules/graph/comp_dataflow.py:cmd_gate() @8fdc3d0602",
      "2.0.0_SA_COO 93421 sequencer read (2): 'comp-dataflow's GATE archetype binds rc to the VERDICT ... A candidate for the s.4.4 form's next clause or a STAGE-3 cell, at the L4 owner's grain'",
      "decomp v0.2.2 @b7daeaa6f0 :93 CE-tp-1 'DONE v0.1.2 -- APPLIED as SPEC at L4 ... s.4.4 is the ONE carrier' -- the form is a PRD clause owned at L4; no task order can amend it, so the remedy is not a cell the decomposition contains (not SPEC_ERROR) and not a missing cell (not DECOMP_INVALIDATING)",
      "1.0.0_SA_CTO 93320: 'the route enum answers ONE question about THIS project -- what does the remedy need that does not exist yet in this project's chain: ... an outcome (SCOPE_CHANGE -> L2)'"
    ],
    "remedy": "At L2 (owner 1.0.0_SA_CTO): name the outcome for verdict-bearing tools at budget expiry, then carry it into PRD s.4.4 at L4 as the form's next clause (for a GATE archetype, BUDGET REACHED never returns the clean verdict: a distinct non-clean rc, or a refusal to render a verdict on a partial sweep, with the resume cursor as today), then L5/L6 forward for the comp-dataflow change under CE-t-7 and for any other verdict-bearing marquis tool the L4 owner's census names. Nothing is built against the current form before the outcome is named. The disarm on comp-dataflow itself (cmd_gate's rc at BUDGET REACHED) is the tool lane's, via the COO, once the clause exists.",
    "owner": "1.0.0_SA_CTO",
    "round": "v4",
    "disarm": {
      "state": "DISARMED",
      "owner": "0.8.0_AE_CloudComp~A",
      "at": "2026-09-03T14:18Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v5"
    },
    "route": "SCOPE_CHANGE",
    "loop_target": 2,
    "scope_change_kind": "REQUIRES_UNNAMED_OUTCOME",
    "outcome_ref": null,
    "proposed_outcome": "A tool whose exit code is its verdict never returns the clean verdict from a run its time budget cut short; a partial run says so in a form an automated caller cannot mistake for a pass.",
    "closed": true
  },
  {
    "id": "NFRA_COMPEFFICACY-S17",
    "project": "NFRA_COMPEFFICACY",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Andrew's R-4 is conditional ('comp-trace ... if so it should be retired'); the PRD's s.7 row T-19 records the condition as MET with claim=measured on 'strict subset of blast (cli.py:1478-1530)', and R-4's heading repeats it. That line range is the two argparse parser blocks, and the parsers themselves carry the counter-evidence: comp-trace declares --exact and --all, which comp-blast rejects as unrecognized arguments (rc 1), and direction spellings blast does not accept. The axis that cannot be carried is the universe: comp-trace answers over a head-pinned working-tree scan (2,302 nodes with gold:/lambda:/s3:/eventbridge: ids), comp-blast over kuzu (27,134 nodes) by Andrew-direct 2026-08-03 with a FAIL-LOUD-NEVER-FALL-BACK clause at cli.py:970-976, and the kuzu universe carries none of those id prefixes even after a forced refresh. On a stratified sample of 158 of 2,302 real trace ids, blast answers 61 (38.6%) as the caller spells them and 92 (58.2%) under the most generous prefix mapping, with 41 AMBIGUOUS rc 5 and 25 NOT-FOUND rc 3. A forwarder built on that turns roughly two in five working comp-trace calls into a false NOT-FOUND -- the class both tools' rc 3 dials exist to prevent.",
    "evidence": [
      "NFRA_COMPEFFICACY-S17 @a140eed779 (0.8.0_AE_CloudComp~B, 12:08Z): the flag-grain exercise (.tools/comp-blast gold:A_00.accounts_dimension --exact -> rc 1 'unrecognized arguments: --exact'; the trace control rc 0), the traversal-grain exercise (4 queries, both tools), the population measurement through blast's own resolver comp_blast_universe.resolve_subject, and the staleness hypothesis killed by load_kuzu_universe(refresh=True) -- carried as that seat's measurements",
      "org/missions/D11/NFRA/NFRA_COMPEFFICACY/prd/NFRA_COMPEFFICACY_PRD.md v0.5 @5bbdab5ec7 :647 '| T-19 | FWD-4, FWD-5, FWD-8 | comp-trace ... | measured | 45 runs; **strict subset of blast** (cli.py:1478-1530) | CloudComp | retire | T-6 | R-4 | his conditional ruling, condition met ...' and :609-610 '**R-4 (Andrew, 2026-09-02):** \"comp-trace ... if so it should be retired.\" Condition MET (trace subset of blast at cli.py:1478-1530).' -- read at full width at 3.0.0_SA_CVO",
      "org/missions/D11/NFRA/NFRA_COMPEFFICACY/prd/NFRA_COMPEFFICACY_PRD.md :109 FWD-5 'Andrew's specific questions are answered in writing: whether the one he was unsure of is a ...' -- the outcome the subset answer serves",
      "TO-CE-T-19 WITHDRAWN @5a837b1abd by the issuer on the order's own STOP clause; deliverable org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~B/comp-trace.result.md @bfbff9dc14 (flag table, 8-row parity table, carrier census 171 live of 4,814, caller census 57 all-time); production sha of cli.py unchanged",
      "decomp v0.2.3 @dcf07b4799 row CE-t-6 (comp-blast) depends_on CE-t-19 -- the carrier another cell reads; 2.0.0_SA_COO 93626: 'CE-t-6 waits by the decomposition's own dependency'"
    ],
    "remedy": "At L2 (owner 1.0.0_SA_CTO): re-adjudicate R-4 on the corrected measurement -- the ruling is conditional and its condition is measured unmet -- choosing on the record among the three honest options the lane named: retire comp-trace anyway and accept the coverage loss as a DECISION rather than a subset claim; keep comp-trace and close T-19 as NOT-RETIRED with this measurement as its evidence; or widen the cell to carry trace's universe into blast, which is a CE-t-6 scope. On (b) the choice is plausibly Andrew's, since it is his ruling's own condition that failed; the L4 owner cards it or rules under the autonomy word and says which. Then at L4: PRD s.7 row T-19's claim corrected (measured -> the corrected measurement) and R-4's heading rewritten to the ruling taken, since CE-t-6 reads that carrier; then L5/L6 forward for CE-t-6 and for whatever T-19 becomes. Whichever way (b) goes, the carryable flag remainder (--exact, --all, the direction aliases) is genuine trace-only capability any retirement must carry into blast's parser rather than drop silently. The DISARM (the PRD row's false 'measured' claim, which another cell reads) is the L4 owner's in place and does not wait for the ruling.",
    "owner": "1.0.0_SA_CTO",
    "round": "v5",
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-09-03T15:35Z"
    },
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v5"
    },
    "route": "SCOPE_CHANGE",
    "loop_target": 2,
    "scope_change_kind": "CONTRADICTS_NAMED_OUTCOME",
    "outcome_ref": "FWD-5",
    "closed": false
  }
]
```
