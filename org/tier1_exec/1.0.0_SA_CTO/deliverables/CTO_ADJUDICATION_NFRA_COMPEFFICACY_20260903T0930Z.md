# CTO ADJUDICATION -- NFRA_COMPEFFICACY, 2026-09-03 ~09:30Z (spine v2.3 L2 re-entry; `/open-calls --adjudicate`)

**Trigger:** 3.0.0_SA_CVO's round-4 L10 stamp @153522a509 routes `NFRA_COMPEFFICACY-S14` to L2 as `SCOPE_CHANGE`,
`scope_change_kind REQUIRES_UNNAMED_OUTCOME`, `outcome_ref null`, owner `1.0.0_SA_CTO`. Under Andrew's word of
2026-09-03 ~05:2xZ (record `ANDREW_DIRECT_20260903_052xZ_WHO_DECIDES_DONE_COO_COMPLETION_REPORT_CTO_GRADES_TWO_READS.md`,
message 5: "if there is a scope change, the CTO can run /open-calls on the subject and then CTO adjudicates on the recs
... autonomous after Limb 2") the CTO builds the cards, rules on each, records the ruling here, appends the outcome,
re-issues the PRD, and the loop runs forward from L4. Nothing here waits on Andrew.

**Inputs read:** the S14 investigation row and its remediation row (verbatim in the channel files); PRD v0.4 s.4.4 (Rule
T's form: "at expiry ... rc stays 0 (the LINE is the rejectable state, not the rc)" for every marquis tool; the
non-application clause exempting only no-loop / no-subprocess tools) and s.4.3 (the answer-state bar); comp-dataflow's
gate contract (T7-AC6: the gate's rc IS its verdict); `org/standards/COMPTOOL_ANSWER_STATE.enum.json` (PARTIAL_OR_BLIND's
tool-voice token `NOT-DECIDABLE`; live carriers comp-schedule and iam_cli.py:50, the latter returning rc 2 "DEFERRED --
never mistaken for a deny").

```
+-- CALL 1 of 2 ---------------------------------------------------+
  **What does a VERDICT-BEARING tool return at budget expiry: (a) a
  non-clean rc distinct from both CLEAN and FAIL, carrying the
  PARTIAL_OR_BLIND state in its own voice, or (b) a refusal to render
  any verdict on a partial sweep?**
  Rule T fixes rc 0 at expiry for every marquis tool; comp-dataflow's
  gate rc IS its verdict, so a budget-cut sweep with 0 findings among
  the files it reached reads CLEAN to any rc-only consumer.
  --------------------------------------------------------------------
  **REC -- (a).** The estate already has the value: PARTIAL_OR_BLIND's
  tool-voice is NOT-DECIDABLE and iam_cli returns it as rc 2, never
  read as a deny. (b) throws away the prefix the tool did scan. Either
  way the rule is one sentence: a verdict-bearing tool NEVER returns
  its clean verdict from a partial run.
  --------------------------------------------------------------------
  **RULING -- (a).** New outcome FWD-10 appended at the next unused id;
  PRD s.4.4 gains the `verdict-bearing` row of the form (BUDGET REACHED
  + the PARTIAL_OR_BLIND state in the tool's voice + a non-clean rc
  distinct from CLEAN and FAIL + the resume cursor as today). Rule T's
  rc-0 clause stays for every non-verdict tool; the form is now MECE
  over the archetypes it governs (Rule 24 (i): the uncovered member
  was "the tool whose rc is an answer", and it is named).
+---------------------------------------------------------------------+

+-- CALL 2 of 2 ---------------------------------------------------+
  **T-7 F2 (the L4 owner's call): comp-dataflow prints the same REFUSE
  shape and rc 3 for SUBJECT_ABSENT_FROM_CORPUS on `origin` and for
  NOT_APPLICABLE on `gate`, distinguishable only by the echoed
  subcommand. Under s.4.3's bar, is that FAIL?**
  s.4.3: "four cases, four distinguishable outputs; any two states
  print alike is FAIL". The bar did not say at which grain.
  --------------------------------------------------------------------
  **REC -- grain = ONE invocation, judged by the STATE TOKEN.** Two
  subcommands answer two questions; sharing an rc across them is not
  the defect. The defect is a line that does not NAME the state.
  --------------------------------------------------------------------
  **RULING -- the grain sentence lands in s.4.3:** distinguishability is
  judged within one invocation's output by the state token in the
  tool's own voice; a bare REFUSE shape whose state is carried only
  by the echoed argument is FAIL; two subcommands may share an rc if
  each prints which of the four states it is. T-7 F2 is therefore a
  FAIL on the token, not on the rc, and closes when comp-dataflow
  prints the state name on both branches.
+---------------------------------------------------------------------+
```

**Not a card, recorded for the close (COMPLETION_GRADES):** S13 (T9-AC2 self-marked PASS while three of four planted
cases print byte-identical bodies) is routed `SPEC_ERROR` to L6 and is `2.0.0_SA_COO`'s; for the grade, FWD-2 ("each
tool has one written account ... four distinguishable outputs") reads NOT_REALIZED for comp-trigger until CE-t-9's
remediated order closes on s.4.3's bar quoted, not restated. The CVO's correction of T-3 F2's placement (CE-t-6 is
comp-blast's row) is read; no act here.

**What follows (the loop, in order):** PRD v0.5 at the tree home with `endpoint_outcomes` carrying FWD-10 (this turn,
the L4 notifier fires to `2.0.0_SA_COO`); L5: the COO's decomposition gains the cell(s) for the verdict-bearing clause
(comp-dataflow under CE-t-7, and any other verdict-bearing marquis tool the census names); L6: fresh task orders; L7
onward as always. The disarm on comp-dataflow itself is the tool lane's, via the COO, and nothing is built against the
old form.
