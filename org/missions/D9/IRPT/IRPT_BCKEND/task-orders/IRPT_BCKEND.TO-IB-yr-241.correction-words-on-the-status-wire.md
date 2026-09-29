# TO-IB-yr-241 -- a correction-bearing status offers CORRECT with words, from an enumerated mapping

<to_id>IRPT_BCKEND.TO-IB-yr-241</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~87</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<issued_date>2026-09-29</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>24</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-241` (`decompositions/IRPT_BCKEND_DECOMP_R24_Y.md`, amendment 2)

---

## WORKER FACE

### THE CELL

Manual walk 2, item W2-06. Today a user who is told to correct something is not told WHAT.
`ProspectJobStatus.tsx:61-76` renders the state word plus `publicReasonCode`, and
`OwnedRequestHistory.tsx:110` adds *"Open it to see what to change"* to every non-READY row -- because nothing on the
wire says what to change. `1.0.0_SA_CTO` 103026 placed the fix on the wire, not in a page mapping.

**This cell adds NO field and changes NO contract.** `_contracts/StatusEnvelope.schema.json` is
`additionalProperties: false`, and `public_reason_code` is documented as *"a code, never a message"* --
`build_envelope` enforces that itself at `ops/status.py:117-120`. But the envelope already has the home:
`actions[]` items are `{action, safe, description}`, all REQUIRED, the `action` enum **already contains `CORRECT`**,
and `description` is documented as *"what the action does"*. It already carries prose on the live wire -- W22's Y1
response carried `{"action": "WAIT", "safe": true, "description": "accepted work is queued for processing"}`
(`ycharts/generate/entry.py:131-135`).

**Build, in `ops/status.py` only:**

1. Add an **enumerated, server-side mapping** from `public_reason_code` -> a short correction sentence. It is a
   literal table in the module. **No free text, no exception body, no vendor material, no interpolation of anything
   a caller supplied.**
2. In `build_envelope`, when the state is a correction-bearing one and the reason code is in that mapping, ensure the
   returned `actions` carries `{"action": "CORRECT", "safe": True, "description": "<the mapped sentence>"}`. A
   caller that already supplied its own `CORRECT` action wins -- do not duplicate or overwrite it.
3. **An unmapped code adds nothing.** Degrade to exactly today's behaviour rather than inventing advice.

**The one mapping that is load-bearing and measured.** `RESOLVE_RETRY_EXHAUSTED` must **NOT** advise replacing or
re-uploading the file. Rows `IRPT_BCKEND-S206` and `IRPT_BCKEND-S215` measured that the file is not the cause: the
same upload normalized in 1 s when run solo and exhausted over 203 s while another generation was in flight. Words
that blame the file would hard-code a wrong remedy into the product. Say what is true -- the request could not be
resolved while other work was in flight, and it can be submitted again.

**Change nothing else.** No new state, no change to `state` or `public_reason_code`, no new enum value, no change to
which actions are offered for any other code, and no change to the `EnvelopeRefused` rules. **AC3 is the control that
proves you did not** -- it asserts the contract's 7 properties, the closed `{action, safe, description}` item shape,
and that a sentence is still refused as a reason code.

### ACCEPTANCE (run from your worktree root)

<criterion id="Y24-1-AC1" cell_refs="IB-yr-241"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R24_CHECKS/test_r24_y1_correction_words.py::test_offers_correct_with_words</invocation><expect>1 passed</expect></criterion>

<criterion id="Y24-1-AC2" cell_refs="IB-yr-241"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R24_CHECKS/test_r24_y1_correction_words.py::test_retry_exhausted_words_do_not_blame_the_file</invocation><expect>1 passed</expect></criterion>

<criterion id="Y24-1-AC3" cell_refs="IB-yr-241"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R24_CHECKS/test_r24_y1_correction_words.py::test_contract_unchanged</invocation><expect>1 passed</expect></criterion>

<expected_criteria>Y24-1-AC1,Y24-1-AC2,Y24-1-AC3</expected_criteria>

**Issuer's base dry-run at CLOUD HEAD, measured:** AC1 FAIL (no `CORRECT` action is offered today), AC2 FAIL (no
words to inspect), **AC3 PASS**. The control passing is what makes the two failures MEASURED ABSENCES rather than a
broken fixture -- an earlier draft of this battery failed all three on a `ModuleNotFoundError`, and only fixing the
path and seeing AC3 go green established that.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `R24_CHECKS/` and the
  `_contracts/` schemas are **READ-ONLY** -- if the cell seems to need a contract edit, it is being built wrong; stop
  and refuse. No AWS call, no deploy, no Terraform.
- **Served code moves only through `2.0.0_SA_COO~P`'s rebuild**, never by you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the test to pass.
- **Row ids** are `IRPT_BCKEND-W87-S<k>`. Other seats append to that same channel file concurrently: re-read it
  immediately before you write and re-check your `<k>`.
- **Verify every commit with git, not with the tool's stdout** -- `git status --porcelain <path>` must come back
  empty. An `rc=128` here is usually a shared-index race; re-run and re-check.

<paths>
infra/aws/lambda/investor-reporting/ops/status.py
infra/aws/lambda/investor-reporting/ops/tests/test_status.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R24_Y.md</decomp_doc> round 24, workstream ~Y, cell `IB-yr-241`.
<owned_cells>IB-yr-241</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y24-1-AC1, Y24-1-AC2, Y24-1-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~87/IRPT_BCKEND.TO-IB-yr-241.correction-words-on-the-status-wire.proof_of_spec.json`
(the ORDER FILE's basename), validated with `python .tools/proof-of-spec-check.py <instance> Y24-1-AC1,Y24-1-AC2,Y24-1-AC3`
BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** each criterion's output line, the diff summary, and the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched; one source file.
comp-blast: DECLARED-NOT-APPLICABLE -- one shared status module; nothing served moves in this cell (~P rebuilds).
comp-iam: DECLARED-NOT-APPLICABLE -- no new AWS call; the cell adds a literal mapping and one action entry.
comp-adversary: RUN -- the risk is that "words on the wire" becomes a leak or a wrong remedy. It does not: the words come from a literal server-side table keyed by an already-public reason code, never from an exception body or caller input, so nothing protected can reach the line; AC3 asserts the contract's closed shape so no field is added; and AC2 encodes the one remedy the fabric has MEASURED to be wrong (S206/S215: RESOLVE_RETRY_EXHAUSTED is not the file's fault), which is exactly the failure a page-side mapping would have baked in. Scanned ops/status.py (build_envelope, ACTIONS, REASON_CODE_RE, the nine states, the classifier at :268-282) plus StatusEnvelope/PublicStatusEnvelope and ycharts/generate/entry.py's live actions example. Blind to which codes the SERVED status path actually emits most often, which is why an unmapped code must degrade to today's behaviour rather than guess.
lane: the <paths> block IS the grant; no open order holds these files.
</preflight>
