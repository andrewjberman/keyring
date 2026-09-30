# TO-IB-yr-271 -- the contract seam suite resolves `opal://` refs, and the one dangling ref resolves

<to_id>IRPT_BCKEND.TO-IB-yr-271</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~90</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<issued_date>2026-09-30</issued_date>
<status>dispatched</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-271` (`decompositions/IRPT_BCKEND_DECOMP_R27_Y.md`)

---

## WORKER FACE

### THE CELL

`_contracts/tests/test_seam_paired.py` is the estate's contract seam check and **it cannot grade anything today**: 33
of its 58 nodes are red, its own `test_control_*` nodes among them, for ONE cause. Line 570 derives a document name as
`r.split("#")[0][len("../"):][: -len(".schema.json")]` -- it assumes every `$ref` is a relative `../X.schema.json`. The
published convention is `opal://irpt/contracts/v1/X.schema.json`, so stripping three characters yields
`l://irpt/contracts/v1/X` and no fixture or schema ever resolves.

**`1.0.0_SA_CTO` 103081 RULED WHICH SIDE MOVES, and it is not yours to revisit. Verbatim:** *"The parser learns
opal://; the published convention (18 of 18) stands. The test is the defect, not the contract. Cut the fix in round 27:
resolve opal:// refs and keep relative refs working; acceptance is the suite green with its test_control_* nodes still
able to fail (one mutant re-run red). No published schema changes."*

**Build:**

1. **Teach the ref resolver `opal://irpt/contracts/v1/<Name>.schema.json`** wherever the suite derives a document name
   or resolves a `$ref` -- line 570 is the one the issuer measured, and it is **not** promised to be the only site:
   find them by making the suite green, not by trusting that number. **Relative `../X.schema.json` refs must keep
   working** -- some schemas use them and the ruling says so explicitly. Do not special-case by filename.
2. **Publish the ONE missing contract so the landed ref resolves.** `responses/comparison-catalogue.response.schema.json`
   refs `opal://irpt/contracts/v1/ComparisonCatalogue.schema.json`, and **that file does not exist** in the published
   v1 directory -- a census this session read **1 dangling ref of 18 response schemas**, the other 17 fine. The contract
   itself exists at `infra/aws/lambda/investor-reporting/_contracts/ComparisonCatalogue.schema.json` (round 25's
   deliverable, 3322 bytes). Publish it into `docs/contracts/investor-reporting/v1/` in the form its 23 published
   siblings take. Row `IRPT_BCKEND-S223`.
   - **This is NOT the move the ruling forbids.** Adding a MISSING contract that an already-landed route references is
     completing round 26. Bending an EXISTING published schema to satisfy the test is what is forbidden, and **AC3
     machine-checks exactly that distinction**: no existing published schema may be MODIFIED.
3. **Add the fixture pair the seam suite needs for the new document**, `_contracts/fixtures/ComparisonCatalogue.valid.json`
   and `.invalid.json`, following the 12 existing pairs (they are wrapped: `{_fixture, _source, _expect, instance}`).
   The valid one must conform to the contract and the invalid one must violate it.
4. **Leave every published schema's CONTENT alone otherwise**, and make no change under
   `infra/aws/lambda/investor-reporting/ycharts/` or `reports/`.
5. **Cell `IB-yr-272`, a separate and much smaller thing in the same worktree:** `_authz/tests/test_unguarded_census.py`
   asserts `17` routes at `:99` (`len(table)`), `:114` (`verdict["routes"]`) and `:141` (`whole["routes"]`), against a
   published file that now holds 18 after `IB-yr-261`. Move all three to `18` and date the change in a comment naming
   `IB-yr-272` and row `IRPT_BCKEND-W89-S2`. **Keep the literal a literal.** A count derived from the file it checks
   asserts nothing; this pin exists so that a route added or lost is a loud edit here, and the suite's own docstring
   records that twice before, the pin's failure WAS the notice that a gap had closed. The issuer measured the result:
   **before 7 failed / 1 passed, after 6 failed / 2 passed** -- so you should read 6/2, and 6 is not a failure of yours.

### ACCEPTANCE (run from your worktree root unless the invocation says otherwise)

<criterion id="Y27-1-AC1" cell_refs="IB-yr-271"><invocation>cd infra/aws/lambda/investor-reporting && python -m pytest -q -p no:cacheprovider _contracts/tests/test_seam_paired.py</invocation><expect>0 failed (report the passed count and the collected total)</expect></criterion>

<criterion id="Y27-1-AC2" cell_refs="IB-yr-271"><invocation>cd infra/aws/lambda/investor-reporting && python - &lt;&lt;'PY'
import io, json, subprocess
P = "_contracts/fixtures/AnalysisRequest.valid.json"
orig = io.open(P, encoding="utf-8").read()
d = json.loads(orig)
d["instance"]["stage"] = 12345      # stage is an 8-value string enum; 12345 violates it outright
io.open(P, "w", encoding="utf-8", newline="\n").write(json.dumps(d, indent=2) + "\n")
r = subprocess.run(["python", "-m", "pytest", "-q", "-p", "no:cacheprovider",
                    "_contracts/tests/test_seam_paired.py::test_control_a_known_good_document_conforms_and_a_known_bad_one_does_not[analysis-requests]"],
                   capture_output=True, text=True)
io.open(P, "w", encoding="utf-8", newline="\n").write(orig)   # ALWAYS revert
print(r.stdout[-700:])
PY</invocation><expect>1 failed, and the message names the ENUM violation on `stage` (12345) -- NOT "no valid fixture"</expect></criterion>

<criterion id="Y27-1-AC3" cell_refs="IB-yr-271"><invocation>git diff --diff-filter=M --name-only HEAD -- docs/contracts/investor-reporting/v1/</invocation><expect>no output (no EXISTING published schema modified; added files are permitted and do not appear)</expect></criterion>

<expected_criteria>Y27-1-AC1,Y27-1-AC2,Y27-1-AC3</expected_criteria>

**Issuer's base dry-run, every number measured in the MAIN worktree at HEAD:**

- **AC1 -- `33 failed, 25 passed`** (58 collected). Cwd-independent: the same 33 from `investor-reporting/`, from
  `_contracts/` and from `_contracts/tests/`.
- **AC2 -- `1 failed` with `AssertionError: no valid fixture for l://irpt/contracts/v1/AnalysisRequest`** at base,
  i.e. red for the PARSING cause. **The criterion is not "it is red" -- it is red FOR THE RIGHT REASON.** After your
  fix the same node with the same mutation must fail naming the `stage` ENUM violation. `stage` is the target because it is an EXISTING 8-value
  string enum in the fixture, so `12345` violates the schema's own vocabulary; adding an unknown property would only trip `additionalProperties:
  false` and would prove less. A green suite whose controls can no
  longer fail is worth nothing, which is why the ruling demands this and why the mutation is applied and reverted
  inside the invocation.
- **AC3 -- empty output** at base. **This is the control and it is already green.** A cell that edits an existing
  published schema to make the parser's assumption true fails it.

**`_authz/tests/test_unguarded_census.py` IS yours, as cell `IB-yr-272` (build step 5 above).** The issuer intended
to do it as a direct act and could not: `2.0.0_SA_COO~Y` is not a permitted agent on the `_authz/**` lane, while YOU
are admitted to exactly the `<paths>` this order names, by the `worker_grant` rule in `.owned-paths.yaml`. **Its other 6
failures are NOT yours**: they are the pre-existing unguarded-export finding and its mutant controls (rows
`IRPT_BCKEND-S220`, `S221`), `2.0.0_SA_COO~P`'s to disarm. So the target is **6 failed / 2 passed**, not green, and
report that count.

## BOUNDS

- **Grant.** The `<paths>` block below plus `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~90/`
  and this order's file. Every EXISTING file under
  `docs/contracts/investor-reporting/v1/` is **READ-ONLY for MODIFICATION** -- you may ADD
  `ComparisonCatalogue.schema.json` and nothing else there.
- **No AWS call, no deploy, no Terraform, no vendor/external network call.** This cell changes no lambda code.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the test to pass. **Two of the last three rounds were refused for an issuer defect and both
  refusals were right** -- if a file you need is not in `<paths>`, or a criterion cannot pass for a reason no grant
  fixes, that is a REFUSAL AND A ROW naming the file or the cause. It is not your shortfall.
- **The suite you are fixing is the one that grades you.** Say plainly in your report which sites you changed and
  whether the suite's collected total moved; a green suite with fewer nodes than 58 is a different claim from a green
  suite with 58, and the issuer grades that difference.
- **Row ids** are `IRPT_BCKEND-W90-S<k>`. Other seats append to that channel concurrently: re-read it immediately
  before you write and re-check your `<k>`. `hazard_standing` must be `ARMED` or `INERT` -- nothing else is in the enum.
  **Give each row a `## <ID> -- <one line>` markdown heading**; `~89` appended bare JSON blocks and the issuer had to
  synthesise the headings at the drain.
- **Commit with** `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~90 <0.9.0_WK_IRPT_BCKEND~90@opal.agent>" -F <msgfile> -- <paths>`. Do NOT pre-`git add`. **The message file must be written by the Write tool or python, never a shell heredoc and never a `python -c "..."` whose body contains double quotes.**
- **Verify every commit with git, not the tool's stdout** (`git status --porcelain <path>` empty). An `rc=128` here is
  usually a shared-index race; re-run and re-check.
- **MSYS trap (row IRPT_BCKEND-S215):** a unix path like `/c/Users/...` embedded in a `python -c` SOURCE BODY is not
  converted and Windows Python cannot open it. Pass paths as **argv**, or use Windows-style paths.
- **Search discipline:** raw recursive `grep`/`find` in Bash is gated in this repo. Use `comp-find '<pattern>' [pathspec]`
  for content, `comp-find --name '<glob>'` for files, or the native Grep/Glob/Read tools. Never pipe a `comp-find` into
  `head`/`grep`.

<paths>
infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py
infra/aws/lambda/investor-reporting/_authz/tests/test_unguarded_census.py
infra/aws/lambda/investor-reporting/_contracts/fixtures/ComparisonCatalogue.valid.json
infra/aws/lambda/investor-reporting/_contracts/fixtures/ComparisonCatalogue.invalid.json
docs/contracts/investor-reporting/v1/ComparisonCatalogue.schema.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R27_Y.md</decomp_doc> round 27, workstream ~Y, cell `IB-yr-271`.
<owned_cells>IB-yr-271,IB-yr-272</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y27-1-AC1, Y27-1-AC2, Y27-1-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~90/IRPT_BCKEND.TO-IB-yr-271.seam-parser-resolves-opal-refs.proof_of_spec.json`
(the ORDER FILE's basename), validated with
`python .tools/proof-of-spec-check.py <instance> Y27-1-AC1,Y27-1-AC2,Y27-1-AC3` BEFORE the flip. Copy the schema shape
from `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~89/IRPT_BCKEND.TO-IB-yr-261.comparison-catalogue-route-served.proof_of_spec.json`.
</proof_of_spec>

**REPORT (your final message):** each criterion's output line; which resolver sites you changed and whether 570 was the
only one; the suite's collected total; the census count (expect 6 failed / 2 passed, unmoved); the diff summary; and the
commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched; the cell fixes a test's ref resolver and publishes one contract.
comp-blast: RUN -- WORLD, and the class was moved by the gate rather than by me: I declared SERVED reasoning that the only outward-facing half is part 2 adding a file to the PUBLISHED contract directory, and to-pipeline-gate GATE xii refused it because <paths> names an infrastructure path, whose inferred floor is WORLD. The floor is right and my reasoning was the narrower read: _contracts/tests/ sits inside the lambda tree, so the cell edits infrastructure whatever its runtime reach. Blast radius measured: docs/contracts/investor-reporting/v1/ holds 23 top-level schemas and 18 response schemas; a census this session found exactly 1 dangling ref of 18, the one round 26 landed, so publishing ComparisonCatalogue.schema.json closes a gap rather than opening one and no existing published file needs to move. AC3 machine-checks that with --diff-filter=M. The test-only half cannot reach a served artifact at all. Nothing served moves in this cell; ~P rebuilds lambda code and this cell touches none.
comp-iam: DECLARED-NOT-APPLICABLE -- no boto3 call, no role, no grant.
comp-adversary: RUN -- four risks. (1) The worker makes the suite green by weakening the controls, which is the cheapest path and the one the ruling explicitly guards: AC2 requires a mutated fixture to turn a control node red AND to do so naming the stage enum violation rather than the parsing cause, the mutation target being an existing enum field rather than an added property so the failure cannot come from additionalProperties alone, with the mutation applied and reverted inside the invocation so it cannot be claimed without being run. (2) The worker bends an existing published schema to fit the parser's ../ assumption -- exactly what 103081 forbids: AC3 is git diff --diff-filter=M over the published directory, empty at base, and additions deliberately do not appear so part 2 stays legal. (3) The worker special-cases the one filename it needs instead of teaching the resolver the scheme, leaving the next opal:// ref broken: the face forbids special-casing by filename and requires it to say whether 570 was the only site, because the issuer measured one site and does not claim it is the only one. (4) The worker over-fixes the census suite: it is now IN the grant for cell IB-yr-272, but only its three stale count literals are the cell -- its other 6 failures are named as rows S220/S221 belonging to another lane, the target is stated as 6 failed / 2 passed rather than green, and the count is a reported number so an over-reach shows up. The order also says WHY the literal must stay a literal, because "improving" it into a derived count is the plausible wrong move and would delete a tripwire. Blind to whether the seam suite's collected total stays 58 once refs resolve -- a new parametrization could appear; the order asks for the collected total rather than assuming it, and a green suite with fewer nodes is graded as a different claim.
lane: the <paths> block IS the grant. Measured, not asserted: over 150 task-order files the only orders naming test_seam_paired.py or test_unguarded_census.py are the terminal round-18-era TO-IB-rt-2 (complete) and this lane's own; no open ~M or ~P order holds either file. Round 27 is shared with ~M (TO-IB-m27-271, TO-IB-m27-272, both pending) -- disjoint write surfaces, and both ~Y cells land in ONE issuance commit from this lane.
</preflight>
