# TO IRPT_BCKEND.TO-IB-pr-440 -- READ ONLY: can a served holdings answer carry a sleeve leaf with no security node beneath it?

<to_id>IRPT_BCKEND.TO-IB-pr-440</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~298</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>138</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5373 (on `2.0.0_SA_COO~D2`'s row DSGN_IRPTV1-D2-S18) | **Decomp cell:** `IB-pr-440` (decomposition section 130) | **outcome_ref:** FWD-5

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-298/` (bash `/c/dev/wk-irpt-bckend-298`). Work only there. READ ONLY: code reads, and ONE served
artifact read from S3 through `.tools/aws` (a `get-object` / `head-object` of the published holdings answer). No call to the
served API, no invoke of any function, no write to any AWS resource, nothing built or served.

**Why.** On the portal's Holdings page a TEST FIXTURE shows the card reading 1,000,000 and the table listing 750,000: two SMA
sleeve nodes, 250,000 together, have no security node beneath them, and the table lists security nodes only. Card and table
state the same total and the page says nothing about the unlisted quarter. The question is whether that shape can occur in an
answer this project SERVES. If it cannot, the fixture is wrong and the portal's seat repairs it. If it can, it is a defect on a
client-facing page and the portal's seat adds a sentence. The ratified outcome it bears on is FWD-5: "the view starts at the
model breakdown and drills into accounts and securities ... missing attribution stays VISIBLE without double-counting or
redistributing the residual".

**Read, in this order:**
1. **The producer's rule, in code.** `infra/aws/lambda/investor-reporting/holdings/` (`snapshot.py`, `resolve.py`, `stage.py`,
   `publication.py`, `handler.py`, `entry.py`, and what they import under `lib/` there) and the contract
   `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` (`nodes`, `class_totals`, `attribution_holdouts`,
   `coverage`). Establish: what kinds of node the producer emits; how a sleeve (a separately managed account or model sleeve
   under an account) becomes a node; and whether a sleeve node can be emitted with a value and NO security node beneath it (for
   example a sleeve the overlay vendor reports only as a total; an attribution holdout; a position with no look-through). Quote
   the lines (file:line) that decide it. State the rule in words, and its claim: `measured` only if a test in the folder's
   `tests/` or a line of code shows the case directly; otherwise `inferred`.
2. **One firm's served answer for one day, counts only.** The firm is the one whose overlay carries SMA sleeves (the SmartX
   overlay firm of FWD-5). Find the object the holdings route serves for it from the code (`publication.py` /
   `holdings_publication_port.py`: the firm's index and the publication it points at; addresses come from `lib/opal_naming.py`,
   do not hand-type one). Read the latest served publication: record its key (with any account or client identifier replaced by
   `<id>`), its version id or ETag, and its as-of. If the publication is one object per account set or per relationship, read
   the firm's WHOLE publication for that day (every object the index names) and say how many objects that was. Count:
   `nodes_total`; `nodes_by_kind` (summing to it); `sleeve_nodes`; of them, those with one or more security nodes beneath and
   those with NONE; `accounts_holding_such_a_leaf` (a count); and, for the leaves with none, how the answer itself labels them
   (a kind, a flag, a holdout entry), as a count per label. COUNTS ONLY: no account id, no client name, no value, no balance, no
   position of any account in any file. Say how a sleeve node is recognised (which member and value).
3. **The verdict.** Is the fixture's shape reachable in a served answer? One sentence, following from 1 and 2. If the rule says
   it can occur but the day you read has none, say both and that the count is one firm on one day.
4. **Control.** A small planted snapshot (four nodes: an account, a sleeve with two security nodes, a sleeve with none) run
   through your counting code: `control.planted` must equal `control.read`.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~298/`: `IB138-1_sleeve_leaf_read.json` with
`{producer_rule:{can_emit_a_sleeve_leaf_with_no_security_node, claim, in_words, code_lines:["<file>:<line>", ...], node_kinds},
served_answer:{object, objects_read, version_or_etag, as_of, read_by, nodes_total, nodes_by_kind, sleeve_nodes,
sleeve_nodes_with_a_security_node_beneath, sleeve_nodes_with_none, accounts_holding_such_a_leaf, labels_on_the_leaves_with_none,
how_a_sleeve_node_is_recognised}, verdict:{the_fixture_shape_is_reachable_in_a_served_answer, in_one_sentence},
control:{planted, read}, nothing_written_or_served:true}`; and a one-page `IB138-1_SLEEVE_LEAF_READ.md`.

<criterion id="IB138-1-AC1" cell_refs="IB-pr-440"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r138/p138_cells.py" . IB138-1-AC1</invocation><expect>IB138-1-AC1 PASS</expect></criterion>
<criterion id="IB138-1-AC2" cell_refs="IB-pr-440"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r138/p138_cells.py" . IB138-1-AC2</invocation><expect>IB138-1-AC2 PASS</expect></criterion>
<criterion id="IB138-1-AC3" cell_refs="IB-pr-440"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r138/p138_cells.py" . IB138-1-AC3</invocation><expect>IB138-1-AC3 PASS</expect></criterion>

<expected_criteria>IB138-1-AC1, IB138-1-AC2, IB138-1-AC3</expected_criteria>

The checks grade the shape, the sums and that the verdict follows from the count. Whether the answer is yes or no is UNMEASURED
by the issuer; either is a pass.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file, no portal file, no fixture.
- **Refusal clause:** if the served publication cannot be read with the rights this box has, record the refusal's exact line in
  `served_answer.read_by`, give the rule from code alone, file a row and report; do not call the served API instead. If a
  criterion cannot be met as written, stop, file a row and report. Never weaken a check; do not edit `p138_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W298-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's existing line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~298" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~298@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~298 <0.9.0_WK_IRPT_BCKEND~298@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push. Write no firm name as a literal in any file: say "the SmartX-overlay firm".

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~298/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-440.served-holdings-sleeve-leaf-with-no-security.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 130 (round 138, workstream ~P), cell `IB-pr-440`.
<owned_cells>IB-pr-440</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB138-1-AC1, IB138-1-AC2, IB138-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~298/IRPT_BCKEND.TO-IB-pr-440.served-holdings-sleeve-leaf-with-no-security.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the rule in words with its code lines and claim; the object read, its version and as-of; the
node counts and the two sleeve counts; how the answer labels a leaf with none; the verdict in one sentence; the control; each
criterion's last line; the proof checker's result; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; code reads and one read of a published object; no product file, route, function or served byte changes.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission change; a refusal of the one object read is recorded, not worked around.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p138_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~16:5xZ: IB138-1-AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. Both answers (yes and no) pass the checks. Not measured by the issuer: the producer's rule, the served object's address and layout; the face gives each to the worker with a stop.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
