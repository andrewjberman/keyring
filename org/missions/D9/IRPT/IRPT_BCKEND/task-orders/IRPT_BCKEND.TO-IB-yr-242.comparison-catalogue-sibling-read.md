# TO-IB-yr-242 -- a sibling scoped GET serves the comparison catalogue, named or verbatim

<to_id>IRPT_BCKEND.TO-IB-yr-242</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~88</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-242` (`decompositions/IRPT_BCKEND_DECOMP_R25_Y.md`)

---

## WORKER FACE

### THE CELL

Manual walk 2, items W2-04 and W2-05. The Analysis composer cannot resolve or NAME a comparison before Add, so it
prints `Comparison {n}` and refuses only the cap and duplicates. The composer documents the gap itself at
`GenerateComposer.tsx:20-25`: ResolvedScope v1 *"carries no catalogue of selectable comparisons"*.

**The shape is RULED and is not yours to revisit.** `1.0.0_SA_CTO` 103038, on this lane's measurement that
`_contracts/ResolvedScope.schema.json` is `additionalProperties: false` with 12 properties and 9 required:

- **ResolvedScope stays v1. Do NOT add the catalogue to it** -- that is the option the ruling rejected.
- The catalogue is served by a **SIBLING scoped GET** that *"sits under the existing
  `/api/scoped/investor-reporting/` family behind the same authz guard and tenant check."*
- It *"gets its own new `_contracts` schema (v1, `additionalProperties` false)"*, and the portal validates against it.
- *"Any new resource name is builder output (rule 30)"* -- if you need a resource name, it comes from
  `lib/opal_naming.py`, never typed by hand. A builder refusal is a missing registry row, not a workaround.

**The SOURCE is RULED and is not yours to revisit either.** `1.0.0_SA_CTO` 103035: names come from the **Opal model
catalogue + etf-classifications**, and there is **no substitution to bd-securities** -- *"Andrew is retiring
bd-securities, so a new reader of it is the fork he named."* Do not read bd-securities, even though its coverage is
better. A ticker neither source names **shows its ticker verbatim with no name, never `Comparison N`**.

**Expect the verbatim path to be the COMMON case, not the exception.** `2.0.0_SA_COO~M`'s census
(`deliverables/IRPT_MVP_M/ETF_CLASSIFICATIONS_COVERAGE_20260928.json`) measured `etf_classifications` at **285 items**,
covering 179 of 847 cottonwood tickers and 228 of 1,449 bd tickers -- about one in five. So roughly four entries in
five take the verbatim path, and it must look deliberate rather than broken. The coverage gap itself is
`MDPF_SECCLASS`'s work, not yours.

**Build:**

1. A new module `comparison_catalogue.py` beside the generate entry, exposing exactly two callables the battery uses:
   - `build_catalogue(tenant=...)` -> the served payload;
   - `entry_for_ticker(ticker, tenant=...)` -> one entry, named from the model catalogue
     (`generate/templates.json` `comparison_catalog.entries` -- 4 entries, keys/labels/`security_id`) or from
     etf-classifications, **or carrying the ticker verbatim**.
2. Register the GET in the entry's `ROUTES` table (`ycharts/generate/entry.py`) **and** in the published
   `docs/contracts/investor-reporting/v1/routes.json`, which `test_unguarded_census` checks `ROUTES` against -- they
   must agree or that census fails.
3. Add `_contracts/ComparisonCatalogue.schema.json`, v1, `additionalProperties: false`, and make
   `build_catalogue`'s payload validate against it.
4. The read goes through **the same authz guard and tenant check** as the family's other scoped reads. It is a READ:
   it writes nothing.

**Change nothing else.** ResolvedScope is untouched, the existing `POST .../analysis` route keeps mapping to
`analysis-requests`, and no external lookup is made -- vendor egress needs Andrew's per-use word and this cell does
not have it. **AC4 is the control that proves ResolvedScope stayed v1.**

### ACCEPTANCE (run from your worktree root)

<criterion id="Y24-2-AC1" cell_refs="IB-yr-242"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R24_CHECKS/test_r24_y2_catalogue_read.py::test_route_registered_under_the_scoped_family</invocation><expect>1 passed</expect></criterion>

<criterion id="Y24-2-AC2" cell_refs="IB-yr-242"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R24_CHECKS/test_r24_y2_catalogue_read.py::test_catalogue_contract_is_closed</invocation><expect>1 passed</expect></criterion>

<criterion id="Y24-2-AC3" cell_refs="IB-yr-242"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R24_CHECKS/test_r24_y2_catalogue_read.py::test_unnamed_ticker_is_verbatim</invocation><expect>1 passed</expect></criterion>

<criterion id="Y24-2-AC4" cell_refs="IB-yr-242"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R24_CHECKS/test_r24_y2_catalogue_read.py::test_existing_surface_unchanged</invocation><expect>1 passed</expect></criterion>

<expected_criteria>Y24-2-AC1,Y24-2-AC2,Y24-2-AC3,Y24-2-AC4</expected_criteria>

**Issuer's base dry-run at CLOUD HEAD, measured:** AC1 FAIL (no GET under the family), AC2 FAIL (no
`ComparisonCatalogue.schema.json`), AC3 FAIL (no `comparison_catalogue` module), **AC4 PASS**. The battery imports the
new module INSIDE the tests that need it, precisely so AC4 stays runnable while the cell is unbuilt -- **AC4 passing at
the base is what makes the three failures measured absences** rather than a broken fixture.

**Also run the census the route table answers to**, and say its number in your report:
`python -m pytest -q -p no:cacheprovider infra/aws/lambda/investor-reporting/_authz/tests/test_guarded_entries.py`

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
  `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R24_CHECKS/` is **READ-ONLY** -- do not edit the battery.
  `_contracts/ResolvedScope.schema.json` is **READ-ONLY**: if the cell seems to need it, you have taken the option the
  CTO rejected -- stop and refuse.
- **No AWS call, no deploy, no Terraform, no vendor/external network call.** Served code moves only through
  `2.0.0_SA_COO~P`'s rebuild, never by you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the test to pass.
- **Row ids** are `IRPT_BCKEND-W88-S<k>`. Other seats append to that channel concurrently: re-read it immediately
  before you write and re-check your `<k>`. `hazard_standing` must be `ARMED` or `INERT` -- nothing else is in the enum.
- **Verify every commit with git, not the tool's stdout** (`git status --porcelain <path>` empty). An `rc=128` here is
  usually a shared-index race; re-run and re-check. Write commit-message files with the Write tool or python, never a
  shell heredoc and never a `python -c "..."` whose body contains double quotes.
- **MSYS trap (row IRPT_BCKEND-S215):** a unix path like `/c/Users/...` embedded in a `python -c` SOURCE BODY is not
  converted and Windows Python cannot open it. Pass paths as **argv**, or use Windows-style paths.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/comparison_catalogue.py
infra/aws/lambda/investor-reporting/ycharts/generate/entry.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_comparison_catalogue.py
infra/aws/lambda/investor-reporting/_contracts/ComparisonCatalogue.schema.json
docs/contracts/investor-reporting/v1/routes.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R25_Y.md</decomp_doc> round 25, workstream ~Y, cell `IB-yr-242`.
<owned_cells>IB-yr-242</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y24-2-AC1, Y24-2-AC2, Y24-2-AC3, Y24-2-AC4. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~88/IRPT_BCKEND.TO-IB-yr-242.comparison-catalogue-sibling-read.proof_of_spec.json`
(the ORDER FILE's basename), validated with
`python .tools/proof-of-spec-check.py <instance> Y24-2-AC1,Y24-2-AC2,Y24-2-AC3,Y24-2-AC4` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** each criterion's output line, the guarded-entries census number, the diff summary,
and the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched; the cell adds a read.
comp-blast: DECLARED-NOT-APPLICABLE -- a NEW route plus a new module; no existing served route, handler or contract changes, and AC4 asserts that. ~P rebuilds; nothing served moves in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- the read uses the family's existing authz guard and the role's existing reads (templates.json ships in the bundle; etf-classifications is read by the same account the estate already grants). No new boto3 call is introduced by this cell; if the worker finds one is required, that is a REFUSAL and a row, not a silent IAM assumption.
comp-adversary: RUN -- three risks. (1) The catalogue leaks something scoped: it does not, because the read sits behind the same authz guard and tenant check as the family's other scoped reads and the payload is a closed v1 contract. (2) The unnamed path looks like a bug: that is why AC3 asserts the ticker appears VERBATIM and forbids positional or placeholder labels, and why the face states that ~4 entries in 5 take that path on measured coverage (285 items, ~1 ticker in 5). (3) The worker reaches for bd-securities because its coverage is better: explicitly forbidden with the CTO's reason quoted, since a new reader of a source Andrew is retiring is the fork he named. Scanned ResolvedScope/StatusEnvelope contracts, generate/entry.py ROUTES and build_entry, templates.json comparison_catalog, and ~M's coverage census. Blind to whether the published routes.json requires a version bump for a new v1 route -- if the census refuses the addition, that is a REFUSAL to report, not a file to force.
lane: the <paths> block IS the grant; no open order holds these files.
</preflight>
