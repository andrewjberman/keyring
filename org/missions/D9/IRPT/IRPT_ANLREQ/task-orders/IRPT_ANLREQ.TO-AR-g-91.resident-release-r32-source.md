# TO-AR-g-91 -- the source of resident release r32: all three variant maps pinned, the priced run shipped switched off, and run 3's producer address in place of run 1's

<to_id>IRPT_ANLREQ.TO-AR-g-91</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~193</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-91` (`decompositions/IRPT_ANLREQ_DECOMP_R18_G.md`) |
**outcome_ref:** FWD-1 run 3 and FWD-7 | **depends_on:** `AR-g-85` (merged `002a88bdc3`, the per-variant map selection), `AR-g-87` (merged `38620fe9f2`), `AR-g-90` (merged `ce2256554b`, the `opal_pricing` binding), CTO msg 8568, `~Y2` msg 8570.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~193`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-193` (branch `wk-IRPT_ANLREQ-193`), provisioned by the issuer with the whole of `infra/`, `docs/`, `data/`, `org/standards` and `org/missions/D9/IRPT` on disk (it has no portal sub-worktree; your cell does not touch the portal). Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~193 <0.9.0_WK_IRPT_ANLREQ~193@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W193-S<k>` (take the next free `<k>`; check the channel file for `W193` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree. You BUILD NO release tarball for delivery: the checks run the builder into a temp folder.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`). The release tests run the builder over the repository's HEAD, so COMMIT your product files before you run acceptance, and re-run acceptance after your last commit.

### Read first (under `C:/dev/wk-irpt-anlreq-193/infra/aws/lambda/investor-reporting/`)

- `reports/build_resident_package.py` (the whole file) and `reports/tests/test_resident_r31_source.py` (how r31's source is tested: the builder run as a subprocess over HEAD).
- `ycharts/generate/resident_worker.py` lines 159-170 (the producer allow list and its comment) and the three tests that pin the list: `reports/tests/test_resident_r31_source.py`, `ycharts/generate/tests/test_resident_worker.py` (near line 770) and `ycharts/generate/tests/test_producer_for_ticket.py` (the `SHIPPED` constant).
- `reports/resident_installed.py`: `OPAL_MAP_BINDINGS` (the three binding names), `_opal_map_loader`, `OPAL_PRICING_BINDING` and `load_bindings` (merged; you do not change this file).

### THE CELL (`AR-g-91`, inlined)

The ONE resident release r32 carries these changes. This cell is its SOURCE: the builder and the list, with their tests. Building the delivered tarball and applying it is a separate act under a signed pair. The package already takes every tracked file of `ycharts/research` (except tests and fixtures), so the new price modules and the four adapters ride along without a change here.

**`ycharts/generate/resident_worker.py`, exactly this:**
1. `OPAL_PRODUCER_PRINCIPALS = ("andrew@opalinvest.com", "fwd1-staff-r41b@opal.invalid")`: run 1's address `fwd1-staff-r41a@opal.invalid` leaves and run 3's enters in the same edit (`~Y2` msg 8570; the CTO's addendum 2 owes r41a's removal).
2. In the comment above it, replace the sentence about the FWD-1 run's synthetic principal so it names `fwd1-staff-r41b@opal.invalid` as unique to run 3 and never reused, says run 1's `fwd1-staff-r41a@opal.invalid` was removed in this release, and says the entry is removed in the next resident release after run 3. Keep the rest of the comment.

**`reports/build_resident_package.py`, exactly this:**
1. Four constants beside `OPAL_MAP_SRC` and `OPAL_MAP_TARGET`: `COMPARISON_MAP_SRC = "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/comparison_map.json"`, `COMPARISON_MAP_TARGET = "ycharts/research/comparison_map.json"`, `MULTI_MAP_SRC = "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/multi_map.json"`, `MULTI_MAP_TARGET = "ycharts/research/multi_map.json"`, with a two-line comment saying the resident picks the pinned map by the accepted record's `report_variant` (AR-g-85).
2. After the overview map is added and its sha computed: `add(COMPARISON_MAP_SRC, COMPARISON_MAP_TARGET)` and `add(MULTI_MAP_SRC, MULTI_MAP_TARGET)`, each followed by its sha256 (`comparison_map_sha`, `multi_map_sha`) taken from the member's bytes as the overview's is.
3. In the bindings dict, beside `"opal_map"`: `"opal_map_comparison": {"path": HOST_ROOT + "/" + COMPARISON_MAP_TARGET, "sha256": comparison_map_sha}` and `"opal_map_multicomp": {"path": HOST_ROOT + "/" + MULTI_MAP_TARGET, "sha256": multi_map_sha}`, and `"opal_pricing": {"enabled": False, "tiers": ["estate", "yfinance"]}` with a one-line comment: the priced Opal run ships OFF and is switched on by a bindings edit once the host has its libraries (AR-g-90).
4. `"built_by"` in the `pin` block becomes `"2.0.0_SA_COO~G2"`.
5. Nothing else in the builder changes (no new member beyond the two maps).

**The three existing tests that pin the list change by exactly the address:** `reports/tests/test_resident_r31_source.py` (`NEW = "fwd1-staff-r41b@opal.invalid"`; its list of other addresses that must take the YCharts path gains the uppercase and padded forms of r41b and the old `fwd1-staff-r41a@opal.invalid`, replacing the old r41a variants), `ycharts/generate/tests/test_resident_worker.py` (the tuple asserted near line 770) and `ycharts/generate/tests/test_producer_for_ticket.py` (`SHIPPED`).

**Tests.** A NEW file `reports/tests/test_resident_r32_source.py`, offline, built like `test_resident_r31_source.py` (the module-scope fixture runs the builder as a subprocess over HEAD with `MSYS_NO_PATHCONV=1`, into a temp folder, with a HOST_ROOT that is a real temp folder, then extracts the tarball into it), with these exact test function names (the checker looks for each by name):
`test_the_bindings_pin_all_three_maps_by_content` (each binding's sha256 equals the sha256 of the map file under `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/`), `test_every_shipped_pin_verifies_and_loads` (`resident_installed._opal_map_loader(bindings, host_root)` loads the overview, comparison and multicomp maps with report types `OVERVIEW`, `COMPARISON` and `MULTI`), `test_pricing_is_shipped_off` (the bindings carry `opal_pricing` with `enabled` False and `resident_installed.load_bindings` accepts the document), `test_the_tarball_carries_the_price_modules_and_the_maps` (the members include `ycharts/research/` `price_source.py`, `swap_replacement.py`, `portfolio_series.py`, `tr_level.py`, the four `price_adapter_*.py` and the three map files, and no member path contains `/tests/` or `/fixtures/`), `test_the_producer_list_is_andrew_and_run_3s_address`.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR91-g-AC1" cell_refs="AR-g-91"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g91_checks.py g91</invocation><expect>^AR-G91-OK</expect></criterion>

<criterion id="AR91-g-AC2" cell_refs="AR-g-91"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g91_checks.py regress</invocation><expect>^AR-G91-REGRESS-OK</expect></criterion>

<expected_criteria>AR91-g-AC1,AR91-g-AC2</expected_criteria>

- AC1 runs the builder over HEAD three times in temp folders and checks it with the issuer's six tests (the two other maps pinned by content; every shipped pin verified against its shipped file and loaded with its own report type; pricing off and the bindings loadable; the tarball's modules, maps and the absence of tests and fixtures; the builder's author line and that two builds have identical members and bindings; the list exactly andrew and r41b with every near-miss routed to YCharts), then checks your five named tests exist and pass. At base it FAILs. Run it under `timeout 590` (about two minutes).
- AC2 runs ten existing test files one at a time (131 tests: the r31 source, the resident worker, the producer choice, the accept step, the ready signal, the producer actor, the Opal thread, the installer) and needs all of them to pass. At base it PASSes. Run it under `timeout 590` (about three minutes).

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs, no delivered tarball.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/reports/build_resident_package.py
infra/aws/lambda/investor-reporting/reports/tests/test_resident_r31_source.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_producer_for_ticket.py
infra/aws/lambda/investor-reporting/reports/tests/test_resident_r32_source.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~193/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-91.resident-release-r32-source.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R18_G.md</decomp_doc> round 18, workstream ~G, cell `AR-g-91`.
<owned_cells>AR-g-91</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR91-g-AC1, AR91-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~193/IRPT_ANLREQ.TO-AR-g-91.resident-release-r32-source.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-91`.
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put the `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR91-g-AC1,AR91-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the lines you changed with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- the builder is run by the release act (a CloudOps seat under a signed never-widen pair) and by the tests; its output is the tarball and bindings the host unpacks. The new bindings keys are read only by this repository's `load_bindings` and `_opal_map_loader` (merged); an older resident ignores unknown keys. The list change decides which accepted principals take the Opal producer: at APPLY time r41a stops and r41b starts, so the pair must name that blast radius (the principals, not a count); at merge time nothing moves. Nothing is deployed.
comp-iam: DECLARED-NOT-APPLICABLE in this cell -- no AWS call and no permission change; the grants the priced run would need (the DEMQUE bucket, `ycharts/credentials`) are not used because the YCharts and DEMQUE tiers are not wired, and the host libraries are a CloudOps pair, needed only once pricing is switched on.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against the r31 source test, the CTO's msg 8568 and `~Y2`'s msg 8570. Traps: both addresses left on the list (run 1's still routed to Opal); an uppercase or padded r41b admitted; a variant map listed in the bindings but absent from the tarball, or pinned to another map's hash (a Comparison request then loads the wrong map or refuses); a binding key spelled differently from the loader's; the priced run shipped ON (the host has no pandas, pyarrow or yfinance, so every tier would error); a test or fixture file packaged; a stale `built_by`. The checker feeds a green arm (a reference build passes the six issuer tests, the five named tests and the 131 regress tests) and seven mutant arms (comparison binding omitted: 2 issuer tests fail; pricing shipped on: 1; run 1's address kept: 1; stale `built_by`: 1; the multicomp pin taken from the comparison map: 2; the multicomp binding misspelled: 2; the multicomp map member replaced: 2).
</preflight>

- Cut on CTO msg 8568 (ADDENDUM 2 @87fe24c71d), `~Y2` msg 8570 and the issuer's reference build on the merged tree. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing built for delivery, nothing deployed. Base: `AR91-g-AC1` FAILs and `AR91-g-AC2` PASSes (131), as expected.
- Change (1) of the CTO's two additions, `irpt-anlreq-x10-v1`, is merged (`AR-g-87`); change (2), run 3's address, is here. The delivered build and the apply are the release act: its never-widen pair (COO half from this seat, CTO half from `1.0.0_SA_CTO~DELL2`) names the blast radius above.
