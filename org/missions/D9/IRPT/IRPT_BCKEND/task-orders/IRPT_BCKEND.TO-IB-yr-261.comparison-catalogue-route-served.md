# TO-IB-yr-261 -- the comparison-catalogue GET is registered AND served by the deployed boundary

<to_id>IRPT_BCKEND.TO-IB-yr-261</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~89</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<issued_date>2026-09-30</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-261` (`decompositions/IRPT_BCKEND_DECOMP_R26_Y.md`)

---

## WORKER FACE

### THE CELL

Round 25 built the comparison catalogue and left its route unregistered. **That was the right call and the previous
order's grant was too narrow -- the fault was the issuer's, recorded in `IRPT_BCKEND_DECOMP_R25_Y.md` amendment 1.**
Your cell is the same outcome with a grant that can contain it. On CLOUD already, do not rebuild them:
`ycharts/generate/comparison_catalogue.py`, `_contracts/ComparisonCatalogue.schema.json`,
`ycharts/generate/tests/test_comparison_catalogue.py` (7 passing), and in `ycharts/generate/entry.py` both
`CATALOGUE_OPERATION` and `read_comparison_catalogue`, already wired into `build_entry`'s `operations`.

**WHY THE ROUTE COULD NOT SIMPLY BE ADDED, so you do not rediscover it.** `reports/generate_installed.py:337` does
`routes = dict(generate_entry.ROUTES)`, then `:341` passes `operations={generate_entry.OPERATION: compute,
UPLOAD_OPERATION: upload}` -- its OWN two operations, not the entry module's. `_authz/served.py:643-648` raises
`EntryError` at construction for any route naming an operation the Entry does not serve. So the DEPLOYED boundary is a
second, independent wiring site, and a key in `ROUTES` without it fails **every** request to `irpt-ycharts-generate`,
the analysis POST included.

**Build, all five parts -- the route is not served until every one is done:**

1. **`ycharts/generate/entry.py`** -- add the route key to `ROUTES`, mapping to `CATALOGUE_OPERATION`. The held-out
   comment block above `read_comparison_catalogue` explains why it was absent; replace it with what is now true.
   Route key: `GET /api/scoped/investor-reporting/analysis/comparisons`.
2. **`reports/generate_installed.py`** -- `build_boundary` must serve the catalogue operation:
   add it to the `operations` dict it passes to `served.Entry`. Decide deliberately whether it needs a
   `prospect_modes` entry and say which in your report -- `served.py:773` reads `prospect_modes.get(operation)`, so an
   absent entry means "not a prospect operation", and a scoped authenticated read is not one. Its docstring says "the
   function's two routes"; make it true again.
3. **`docs/contracts/investor-reporting/v1/routes.json`** -- add the row AND move `_denominator.declared` and
   `_denominator.total` from 17 to 18. Copy the shape of an existing row exactly: `route_key`, `handler`, `cell`,
   `status`, `note`, `operation`, `consumer_operation`, `response_schema`. The file's convention is
   `response_schema: "responses/<slug>.response.schema.json"` -- use it. Where `consumer_operation` is null the file
   requires a stated reason beside it; `_operations._what_this_is` says why, in the file's own words: *"an absence
   cannot be read as a statement"*.
4. **`docs/contracts/investor-reporting/v1/responses/comparison-catalogue.response.schema.json`** -- the response
   schema the row names, plus whatever conforming fixture the seam suite needs for its `[comparison-catalogue]` node
   (AC3 is how you know). Follow the `responses/` files already there.
5. **`reports/tests/test_generate_installed.py:117-119`** -- the route pin is an exact-equality assertion on
   `boundary.routes` and on `set(boundary.operations)`. **UPDATE it to the true three-route table. That is required and
   is not weakening it.** Deleting it, or relaxing `==` to a subset check, IS weakening it and is refused.

**Two patches in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~88/` show ~88's intent. DO NOT
APPLY THEM** -- the issuer measured `git apply --3way` failing on both at HEAD (`entry.py` has already moved on,
`routes.json` too), and `held_route_registration_routes_json.patch` uses a `response_contract` key that is not the
file's convention. Read them, then write the real thing.

**Change nothing else.** `_contracts/ResolvedScope.schema.json` stays v1 and untouched -- that is the option CTO 103038
rejected. No new source of names: CTO 103035 ruled the Opal model catalogue plus etf-classifications, **no
bd-securities**, ticker verbatim otherwise. `comparison_catalogue.py` needs no change for this cell; if you think it
does, say why in your report before you touch it.

### ACCEPTANCE (run from your worktree root unless the invocation says otherwise)

<criterion id="Y26-1-AC1" cell_refs="IB-yr-261"><invocation>python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R24_CHECKS/test_r24_y2_catalogue_read.py::test_route_registered_under_the_scoped_family</invocation><expect>1 passed</expect></criterion>

<criterion id="Y26-1-AC2" cell_refs="IB-yr-261"><invocation>cd infra/aws/lambda/investor-reporting && python -m pytest -q -p no:cacheprovider reports/tests/test_generate_installed.py</invocation><expect>13 passed</expect></criterion>

<criterion id="Y26-1-AC3" cell_refs="IB-yr-261"><invocation>cd infra/aws/lambda/investor-reporting && python -m pytest -q -p no:cacheprovider "_contracts/tests/test_seam_paired.py::test_control_a_known_good_document_conforms_and_a_known_bad_one_does_not[comparison-catalogue]"</invocation><expect>1 passed</expect></criterion>

<expected_criteria>Y26-1-AC1,Y26-1-AC2,Y26-1-AC3</expected_criteria>

**Issuer's base dry-run at CLOUD HEAD, every number measured, not predicted:**

- **AC1 -- `1 failed`** at base (`AssertionError: no GET route under /api/scoped/investor-reporting/ is registered`).
  This is the criterion round 25 recorded NOT MET; it is the cell's own outcome.
- **AC2 -- `13 passed` at base. THIS IS THE CONTROL AND IT IS ALREADY GREEN.** With the route registered but the
  boundary unwired it reads **4 failed**, every one `served.EntryError`. So AC2 is exactly the check that tells you
  whether part 2 landed, and a green AC1 with a red AC2 means the route is declared and the function is broken.
- **AC3 -- `no tests ran` at base (rc=5), which is NEITHER a pass NOR a failure.** The suite parametrizes over the
  operations in `routes.json`, so the `[comparison-catalogue]` node does not exist until your row mints it. Do not read
  rc=5 as a red you must explain; it is the node's absence, and AC3 passing is the proof the node now exists AND
  conforms.

**Two suites in this area are BROADLY RED at HEAD and are NOT your doing** (issuer row `IRPT_BCKEND-S220`, measured in
the main worktree and cwd-independent): `_contracts/tests/test_seam_paired.py` is **33 failed / 25 passed** and
`_authz/tests/test_unguarded_census.py` is **6 failed / 2 passed**, each with its own control or mutant nodes among the
failures. That is why AC3 names ONE node id and why no criterion here asks you for a green file. **Do not try to fix
either suite** -- the census's three unguarded routes are the export routes on `irpt-export-render`, which is
`2.0.0_SA_COO~P`'s lane, ARMED there and out of your grant.

**Also run and REPORT these three numbers** (they are the issuer's drain evidence, not your criteria):

- `cd infra/aws/lambda/investor-reporting && python -m pytest -q -p no:cacheprovider _authz/tests/test_unguarded_census.py` -- **baseline 6 failed / 2 passed.** Report the count. A 7th failure means the route resolves to no real entry point.
- `cd infra/aws/lambda/investor-reporting && python -m pytest -q -p no:cacheprovider _contracts/tests/test_seam_paired.py` -- **baseline 33 failed / 25 passed.** Report the count.
- `python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R24_CHECKS/test_r24_y2_catalogue_read.py` -- the whole round-24 battery; AC2/AC3/AC4 of it pass at HEAD, so report **4 passed**.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
  `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R24_CHECKS/` is **READ-ONLY** -- do not edit the battery.
  `_contracts/ResolvedScope.schema.json` is **READ-ONLY**. `ycharts/generate/comparison_catalogue.py` and
  `_contracts/ComparisonCatalogue.schema.json` are **READ-ONLY**: round 25 delivered them and they are not reopened here.
- **No AWS call, no deploy, no Terraform, no vendor/external network call.** Served code moves only through
  `2.0.0_SA_COO~P`'s rebuild, never by you. `irpt-ycharts-generate` is at `CodeSha256 inrij6hL...` /
  `2026-09-29T15:00:32Z` and your commit does not move it.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the test to pass. **The grant was the defect last round -- if a file you need is not in
  `<paths>`, that is a REFUSAL AND A ROW, and it is the issuer's error, not yours.** Name the file.
- **Row ids** are `IRPT_BCKEND-W89-S<k>`. Other seats append to that channel concurrently: re-read it immediately
  before you write and re-check your `<k>`. `hazard_standing` must be `ARMED` or `INERT` -- nothing else is in the enum.
- **Verify every commit with git, not the tool's stdout** (`git status --porcelain <path>` empty). An `rc=128` here is
  usually a shared-index race; re-run and re-check. Write commit-message files with the Write tool or python, never a
  shell heredoc and never a `python -c "..."` whose body contains double quotes.
- **MSYS trap (row IRPT_BCKEND-S215):** a unix path like `/c/Users/...` embedded in a `python -c` SOURCE BODY is not
  converted and Windows Python cannot open it. Pass paths as **argv**, or use Windows-style paths.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/entry.py
infra/aws/lambda/investor-reporting/reports/generate_installed.py
infra/aws/lambda/investor-reporting/reports/tests/test_generate_installed.py
docs/contracts/investor-reporting/v1/routes.json
docs/contracts/investor-reporting/v1/responses/comparison-catalogue.response.schema.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R26_Y.md</decomp_doc> round 26, workstream ~Y, cell `IB-yr-261`.
<owned_cells>IB-yr-261</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y26-1-AC1, Y26-1-AC2, Y26-1-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~89/IRPT_BCKEND.TO-IB-yr-261.comparison-catalogue-route-served.proof_of_spec.json`
(the ORDER FILE's basename), validated with
`python .tools/proof-of-spec-check.py <instance> Y26-1-AC1,Y26-1-AC2,Y26-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** each criterion's output line; the three reported numbers above; whether
`build_boundary` needed a `prospect_modes` entry and why; the diff summary; and the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched; the cell registers a read.
comp-blast: RUN -- this cell's blast radius is the one that bit round 25, and it was MEASURED rather than reasoned about. In a throwaway worktree off HEAD the issuer applied the held change alone and ran four suites before and after: 39 failed / 43 passed -> 45 failed / 38 passed, +6. Per file: reports/tests/test_generate_installed.py 0 -> 4 (every one served.EntryError, the deployed boundary), _authz/tests/test_unguarded_census.py 6 -> 7 (test_every_published_route_resolves_to_a_real_entry_point, which PASSES at base), _contracts/tests/test_seam_paired.py 33 -> 34 (the new [comparison-catalogue] parametrization), _contracts/test_owned_request_contracts.py 0 -> 0. Every file in that delta is in <paths>, which is the whole difference from round 25. Nothing served moves: ~P rebuilds.
comp-iam: DECLARED-NOT-APPLICABLE -- no new boto3 call and no grant. The etf-classifications reader stays unwired (row IRPT_BCKEND-W88-S2), so the catalogue serves the 4 model entries and every ticker verbatim; that is the ruled degrade, not this cell's to close.
comp-adversary: RUN -- four risks. (1) The worker applies ~88's patches and fights the conflicts: the face states the issuer measured both failing `git apply --3way` at HEAD and tells it to read, not apply. (2) The worker reads the 33-red seam suite or the 6-red census as its own damage and either chases them or weakens something: the face gives both baselines as numbers, names row IRPT_BCKEND-S220, and forbids the census fix by naming ~P's lane. (3) The worker treats AC3's rc=5 `no tests ran` as a red and invents an explanation: the face names rc=5 as a third answer state and says why the node cannot exist at base. (4) The worker relaxes the boundary's exact-equality route pin instead of updating it -- the cheapest way to make AC2 green while breaking what it protects: the order says in both faces that updating the assertion to the true table is required and that deleting it or loosening `==` is a refusal. Blind to whether `build_boundary` needs a prospect_modes entry for the catalogue operation: served.py:773 reads prospect_modes.get(operation), so an absent entry means not-a-prospect-operation, which is what a scoped authenticated read should be -- the order asks the worker to decide deliberately and SAY WHICH rather than leaving it silent.
lane: the <paths> block IS the grant; no open order holds these files. reports/generate_installed.py and reports/tests/test_generate_installed.py are shared integration files -- checked at the cut, no open ~P or ~M order names them.
</preflight>
