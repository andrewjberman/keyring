# TO-AR-g-85 -- the report variant the filer asked for reaches the Opal engine: the accept step stamps a server-derived report_variant and the resident selects the pinned element map by it

<to_id>IRPT_ANLREQ.TO-AR-g-85</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~185</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>13</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-85` (`decompositions/IRPT_ANLREQ_DECOMP_R13_G.md`) |
**outcome_ref:** FWD-7 (Comparison and Multi-Comp variants) | **depends_on:** `AR-g-67` (merged `c11be0ffdb`, the same two product files).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~185`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-185` (branch `wk-IRPT_ANLREQ-185`), provisioned by the issuer with the whole of `infra/`, `docs/` and `data/` on disk. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~185 <0.9.0_WK_IRPT_ANLREQ~185@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W185-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`): two files of the package share module names and a mixed run collides.

### Read first (under `C:/dev/wk-irpt-anlreq-185/infra/aws/lambda/investor-reporting/`)

- `ycharts/generate/acceptance.py` (`DynamoAcceptance.accept`, the record literal near line 131) and its two existing tests named below.
- `reports/resident_installed.py` (`OPAL_MAP_BINDING` line 64, `make_opal_stores` line 258, `_opal_map_loader` line 288, and the call that wires them near line 407) and `reports/tests/test_resident_installed.py` (how the doubles are built).
- `ycharts/generate/resident_worker.py` `producer_for` (line 177) and `run_opal` (line 516): they read the accepted record and call `opal_stores(principal, record)`. You change neither file.
- `ycharts/generate/tests/test_ticket_stamp.py` and `ycharts/generate/tests/test_producer_for_ticket.py` (merged, AR-g-67): the harness for a mocked DynamoDB `accept` call and for `make_opal_stores` with a confirmed record.

### THE CELL (`AR-g-85`, inlined)

Today every Opal job renders the Overview map, whatever the filer asked: the engine loads the one pinned Overview map for every job and the accepted record does not say which variant was asked (Overview with no comparison, Comparison with one, Multi-Comp with two or more). This cell makes the record say it, and makes the resident pick the map by it. It pins no new file: the Comparison and Multi-Comp maps join the package in the later release cell. Until then a Comparison or Multi-Comp record on the Opal path refuses with `OPAL_MAP_BINDING_REQUIRED` instead of silently rendering an Overview: the honest failure.

1. **`ycharts/generate/acceptance.py`, `DynamoAcceptance.accept`.** A NEW record gets the key `report_variant`: `"overview"` when `browser["comparison_keys"]` is empty, `"comparison"` when it holds exactly one key, `"multicomp"` when it holds two or more. `browser` is the validated public request already in hand, so the value is server-derived and never read from a client field. `validate_public_request` keeps refusing a client-sent `report_variant` (it is not a public field; add no allowed key). A replay returns the prior record exactly as stored: an old record is never given the key.
2. **`reports/resident_installed.py`, the loader.** Add the constant `OPAL_MAP_BINDINGS = {"overview": "opal_map", "comparison": "opal_map_comparison", "multicomp": "opal_map_multicomp"}` beside `OPAL_MAP_BINDING` (keep that one). `_opal_map_loader(bindings, base)` returns `load(variant="overview")`:
   - a `variant` that is not a `str` key of `OPAL_MAP_BINDINGS` -> `ResidentInstallRefused("OPAL_VARIANT_UNKNOWN")`;
   - the variant's binding missing, or not a dict with `path` and `sha256` -> `ResidentInstallRefused("OPAL_MAP_BINDING_REQUIRED")`;
   - the file absent -> `ResidentInstallRefused("PINNED_FILE_ABSENT:" + <the binding name>)`; the sha256 differs -> `ResidentInstallRefused("PINNED_FILE_DIFFERS:" + <the binding name>)`. For the overview the binding name is `opal_map`, so its two messages are unchanged.
3. **`reports/resident_installed.py`, `make_opal_stores` -> `opal_stores(principal, record)`.** After the existing listed-principal and identity checks and BEFORE any map read or client open: `variant = record.get("report_variant", "overview")` (a record accepted before this change carries none and is an overview). A value that is not a key of `OPAL_MAP_BINDINGS` -> `ValueError("OPAL_VARIANT_UNKNOWN")`. The map is `load_map()` with NO argument when the variant is `"overview"`, and `load_map(variant)` otherwise (the existing test doubles take no argument). Everything else in `opal_stores` is unchanged.
4. **Not in this cell:** `verify_pins`, the bindings file, `build_resident_package.py`, `resident_worker.py`, `opal_producer.py`, any map file. Do not touch them.
5. **Two existing tests pin the exact accepted-record shape and change by exactly the new key:** in `ycharts/generate/tests/test_acceptance_actor.py` the expected key set gains `"report_variant"`; in `ycharts/generate/tests/test_commentary_requested_member.py` the `expected` record literal gains `"report_variant": "overview"`. That second test also rewrites `ycharts/generate/tests/commentary_requested_records.json` when it runs: commit the regenerated file as it stands after your last run.

**Tests.** Two NEW test files, offline, with these exact test function names (the checker looks for each by name):
- `ycharts/generate/tests/test_report_variant_stamp.py`: `test_accept_stamps_overview_without_comparison_keys`, `test_accept_stamps_comparison_for_one_key`, `test_accept_stamps_multicomp_for_two_or_more_keys` (two keys and three keys), `test_replay_returns_the_prior_record_unchanged` (the prior record has no `report_variant` and no write is made), `test_client_cannot_send_report_variant` (`validate_public_request` raises `SubmissionRefused`).
- `reports/tests/test_opal_variant_binding.py`: `test_loader_reads_each_variants_pinned_map` (three small map files in a temp folder with their sha256), `test_loader_default_is_overview`, `test_unknown_variant_is_refused` (`"x"`, `""`, `None`, `5`, `"OVERVIEW"`), `test_missing_variant_binding_is_refused_while_overview_still_loads`, `test_absent_and_changed_pin_name_the_binding`, `test_make_opal_stores_selects_the_map_by_the_record_variant` (a comparison and a multicomp record; `load_map` records its arguments), `test_record_without_variant_takes_overview_with_no_argument` (no key, and `"overview"`: `load_map` is called with NO argument), `test_bogus_variant_refused_before_any_client_opens` (`"bogus"`, `None`, `5`, `""`: no map read, no client opened). Use a record that `producer_for` admits without touching the allow list: `"ticket_confirmed": True` and an owner that is on no list.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR85-g-AC1" cell_refs="AR-g-85"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g85_checks.py g85</invocation><expect>^AR-G85-OK</expect></criterion>

<criterion id="AR85-g-AC2" cell_refs="AR-g-85"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g85_checks.py regress</invocation><expect>^AR-G85-REGRESS-OK</expect></criterion>

<expected_criteria>AR85-g-AC1,AR85-g-AC2</expected_criteria>

- AC1 asks the loader, `make_opal_stores` and `accept` sixteen direct cases with fakes, then checks that the thirteen named tests exist and pass. At base it FAILs (no variant argument).
- AC2 runs seven existing test files one at a time (65 tests) and needs all of them to pass: it is the guard that your two test edits are exactly the new key. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_report_variant_stamp.py
infra/aws/lambda/investor-reporting/reports/tests/test_opal_variant_binding.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_acceptance_actor.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_commentary_requested_member.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/commentary_requested_records.json
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~185/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-85.variant-reaches-the-opal-map.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R13_G.md</decomp_doc> round 13, workstream ~G, cell `AR-g-85`.
<owned_cells>AR-g-85</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR85-g-AC1, AR85-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~185/IRPT_ANLREQ.TO-AR-g-85.variant-reaches-the-opal-map.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-85`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR85-g-AC1,AR85-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the functions you changed or added with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- the accepted record gains one key read by no consumer: `producer_for` reads `owner` and `ticket_confirmed`, `lookup` returns the record whole, and no closed schema validates the record (the last key added, `acting_principal_id`, touched only `acceptance.py` and its tests). `opal_stores` is called from `resident_worker.run_opal` with the same two arguments. Nothing is deployed, so no edge changes until the release cell ships both files.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against the compose read (ENGINE_COMPOSE_READ.json q3, the smallest change). Traps: the variant read from a client field; the key stamped on a replayed old record (the prior record must come back byte for byte); the stamp derived from the wrong count (one key read as multicomp); the loader reading the overview pin for every variant (a Comparison request rendered as an Overview, silently); `load_map(variant)` always passed (the existing zero-argument doubles break); a bogus variant opening the classifier or the research store before it is refused; a missing binding for the new variants reported as a different code than the overview's. The checker feeds a green arm (a reference build passes all sixteen cases, the thirteen named tests and the 65 regress tests) and five mutant arms (stores ignore the record variant: 3 cases fail; loader always reads the overview pin: 6; `load_map` always given the variant: 2; stamp always overview: 2; absent pin loses its binding name: 1).
</preflight>

- Cut on the compose read (`q3`) and CTO msg 8377. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR85-g-AC1` FAILs and `AR85-g-AC2` PASSes, as expected.
- The pins for the two other maps (`build_resident_package.py`, `verify_pins`, the bindings) are the later release cell's; the engine fills the YCharts-field tables of those maps with NOT_AVAILABLE, since no vendor call is made (compose read q3), and that stays so.
