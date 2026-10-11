# TO-YCD-d-9 -- list the 70 Opal-held elements that have no rule, by input, each with what the repo shows Opal already keeping

<to_id>IRPT_YCDGEN.TO-YCD-d-9</to_id>
<project>IRPT_YCDGEN</project>
<issued_to>0.9.0_WK_IRPT_YCDGEN~12</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `YCD-d-9` (`decompositions/IRPT_YCDGEN_DECOMP_R9.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none.

---

## WORKER FACE

### Read first

`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r8/HELD_STORE_READ_YCD-e-8_PART1_20261011.md`, section 2. Then `infra/aws/lambda/investor-reporting/ycharts/research/held_data.py` in full: `RULES`,
`_STATIC`, `_not_held_reason` and `DEFAULT_REASON`.

### THE CELL

The Overview's element map is `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json`. 158 of its elements have `source.computed` equal to
`OPAL_HELD`. For 70 of them `held_data.RULES` has no entry for the element's `source.group`: Opal computes nothing for them, and
`held_data._not_held_reason(group)` says why in one sentence. Nobody has listed those 70 with what Opal might already keep.

Write ONE file, `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~12/RULE_LESS_ELEMENTS_YCD-d-9.json`, a JSON object:

- `"denominator"`: `{"map_elements": N, "opal_held_elements": N, "rule_less_elements": N}`, each COUNTED by your own script from
  the map and `held_data.RULES`, never typed. Expect 254, 158 and 70; if you count differently, report your numbers and stop.
- `"elements"`: one object per rule-less element, `bond_maturity` groups first, then the rest sorted by group:
  - `"element_id"`, `"group"`, `"field"`, `"page"`: from the map;
  - `"why_no_rule"`: the exact string `held_data._not_held_reason(group)` returns;
  - `"input_family"`: the first two `_`-separated tokens of the group (for example `bond_maturity`);
  - `"repo_evidence"`: a list, possibly empty, of `{"path": "<repo file>", "line": <int>, "what": "<one line>"}` naming where
    the repo shows Opal already keeping data that could feed this input family: a table, a bucket prefix, a column or a
    registry row. Search with the native Grep tool under `infra/`, `lib/`, `docs/contracts/` and `integrations/`. Record what
    the file SAYS; do not infer that data exists from a name alone;
  - `"feedable"`: exactly one of `"YES_SEEN_IN_REPO"` (the evidence names a kept field that carries this figure per security),
    `"PARTIAL"` (related data is kept but not this figure per security), `"NOT_SEEN_IN_REPO"` (your search found nothing; this
    is NOT a claim that Opal lacks it).
- `"search_log"`: one entry per input family, `{"input_family", "patterns": [...], "folders": [...], "files_matched": N}`, so a
  reader can see what you looked through. An empty result with no search log is not a result.

Also write `RULE_LESS_ELEMENTS_YCD-d-9.md` beside it: one table, one row per input family, with the element count, the
`why_no_rule` sentence, the feedable class and the best evidence path.

You read the repo only. No AWS call, no network. You change no product code and no test.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="D9-AC1" cell_refs="YCD-d-9"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r9/r9_checks.py d9</invocation><expect>^R9-D9-OK</expect></criterion>

<expected_criteria>D9-AC1</expected_criteria>

- AC1 re-counts the three denominators itself, then checks your file: the same three numbers; one element object per rule-less
  element with no id missing and none extra; every `why_no_rule` equal to what `held_data._not_held_reason` returns; every
  `feedable` one of the three words; every input family present in `search_log`; and every `repo_evidence` path an existing
  file. At base it FAILs (the file is absent).

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS calls, no HTTP, no installs.
- **Refusal clause.** If the criterion cannot be met as written: stop, report, and do not weaken a check.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_YCDGEN~12" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_YCDGEN~12@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_YCDGEN~12 <0.9.0_WK_IRPT_YCDGEN~12@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool. Do not pre-`git add`.
  - ASCII only. Use the native Grep/Glob/Read tools; a recursive shell grep over the repo is denied by a hook.

<paths>
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~12/
org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-d-9.the-70-rule-less-elements-listed.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R9.md</decomp_doc> round 9, cell `YCD-d-9`.
<owned_cells>YCD-d-9</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: D9-AC1. Instance at
`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~12/IRPT_YCDGEN.TO-YCD-d-9.the-70-rule-less-elements-listed.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_YCDGEN.TO-YCD-d-9`.
- Validate with `python .tools/proof-of-spec-check.py <instance> D9-AC1` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~10/IRPT_YCDGEN.TO-YCD-d-8.remeasure-six-generator-and-builder-rows.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- the criterion's output lines;
- the three denominators you counted;
- a table by input family: elements, feedable class, best evidence path;
- what you searched and found nothing for;
- commits.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- the cell writes two files under its own deliverables folder and changes no product file.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission, no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read held_data.py and the held-store read part 1. Traps: a typed denominator; "not found in the repo" stated as "Opal does not keep it"; evidence inferred from a file name; a family with no search log.
lane: the worker's own deliverables folder.
</preflight>

Source: CTO round-9 analysis @eeb799ce72 section 3 item 4.
