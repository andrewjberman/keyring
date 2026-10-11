# ADVI_FIRMBKTS task order -- `FB-g-36` -- THE PARTNERS API LAMBDA'S SIDE-EFFECT-FREE EVENTS, ONE PER SERVED CLASS IT READS (ACT 4c'S OBJECT-LEVEL READ)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-36</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~58</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only census of repository files; nothing is changed or applied.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no grant: you read files only. Do not invoke any function.
comp-adversary: RUN by the issuer -- at base the census file does not exist and `r4_pevents.py` reads 0 of 4 (Q1 to Q4 FAIL by construction). Blindness: the check proves the file's shape, the class partition and that the cited lines exist and hold a seam call; it cannot prove an event runs. The act-4c actor invokes each event before and after the move and diffs the responses.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-36` (round 4, workstream `PEVENTS`; acts 4b and 4c's object-level read)

Act 4c moves `opal-partners-data` to the canonical home by one environment value. Its pair requires the actor to invoke the
Lambda with the SAME printed synthetic events before and after and to diff the response bodies. You write the events from the
repository. You invoke nothing.

### 1a. What to produce (the whole spec)

One JSON file `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~58/PARTNERS_EVENT_CENSUS.json`: an object with:
- `entries`: a list, one entry per SERVED CLASS the Lambda's code reads (or lists) through its seam, each with:
  `class`: the class's LEGACY prefix exactly as `infra/logic/registry/platinum_destinations.json` spells it (e.g.
  `platinum/accounts/`); `handler` (`lambda_function.lambda_handler`); `event`: a JSON OBJECT, the smallest API-Gateway-shaped
  event whose handling reads a key of that class (build it from a test fixture of the Lambda's own tests where one exists, else
  from the fields `lambda_function.py` reads of the event; no real client identifier, use the placeholders the fixtures use);
  `call_chain`: a list of `"path:line"` from the `lambda_handler` line to the line that calls the seam
  (`source(` or `list_target(`), every path under `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/` and every line verified by you;
  `side_effects`: `"none"`, or one sentence naming each write, email, queue send or table put the event would cause;
  `invoke_recommended`: `true` exactly when `side_effects` is `"none"`; `source_of_event`: `"path:line"`;
- `classes_not_read`: the list of registered legacy prefixes (of the 11) the code never reads through the seam;
  `classes_read_by_code`: the list of the others. Together they are the 11 registered prefixes, no overlap.

### 1b. Rules

1. Read only. Do not call AWS, invoke a function, run a test that writes, or edit any repository file.
2. If a class cannot be read without a side effect, say so (`invoke_recommended` false, the write named); do not invent an event
   you could not build from the tree.
3. At least one entry must be invokable. No client or advisor identifier appears in the file.

## 2. BOUNDS

1. The only file you write is `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~58/PARTNERS_EVENT_CENSUS.json`, plus your surprise rows and proof instance under your own deliverables folder.
2. ASCII only. If something cannot be met, file a surprise row and stop.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~58/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~58/ADVI_FIRMBKTS.TO-FB-g-36.partners-event-census.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-36"><invocation>cd /c/dev/wk-firmbkts-58 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_pevents.py --arms census --file org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~58/PARTNERS_EVENT_CENSUS.json --root /c/dev/wk-firmbkts-58; echo "exit=$?"</invocation><expect>ROUND 4 PARTNERS EVENTS: 4 of 4 arms</expect></criterion>
</proof_of_spec>

AC1 reads the file against the tree: every key present, the classes a partition of the 11 registered prefixes, every call-chain
line in the Lambda's directory and ending in a seam call, side effects and the recommendation agreeing. The invocation
terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-36.partners-event-census.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~58`. Commit
the census, your rows, then the instance second. **Do not flip this order's `<status>`**. Row ids:
`ADVI_FIRMBKTS-D1-W58-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1's output, the number of
entries and of invokable ones, `classes_not_read`, any entry with `invoke_recommended` false and its reason, and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the 4b/4c COO half's object-level read names "the partners API's served-JSON path for a sample of the 11
classes' keys". The exec-summary's read is `r4_execeq.py` (its handler cannot be invoked read-only). Workstream `PEVENTS`.
Class LOCAL (read-only).

<status>complete</status>
<round>4</round>
<workstream>PEVENTS</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-36</to_id>
<slot>~58</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
