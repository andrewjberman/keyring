# TO NFRA_OPLGTW.TO-OG-c-1 -- the producer's extended completion contract

<to_id>NFRA_OPLGTW.TO-OG-c-1</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~4</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-c-1` | **outcome_ref:** FWD-2, FWD-5, FWD-8 | **depends_on:** -- (head; spawned at issuance) | **slot:** ~4, queue position 1

---

## WORKER FACE

### THE CELL

`OG-c-1` -- **the Schwab producer's extended completion contract**, built and tested in
`data/assets/scripts/silver/conversion_manifest.py` and `data/assets/scripts/silver/schwab_runtime.py`, **not deployed**.
The Gateway's catalog trusts a date only when the producer's completion record proves the whole day, and today's
record cannot.

What the source does today (certified L4 rectangle, S3-data, @c9a44aa896): *"completion_marker:
schwab/{master}/meta/complete/date={date}.json, schema opal.silver.complete/v1. declared_tables derives only fact names
from SPECS. written_tables derives table names from current run results silver_keys, including dimensions and idempotent
existing outputs. Both disagreement directions are retained. Payload carries master/date/run_id/emitted_at/declared_source,
no per-object VersionId or digest. Each run can replace the same date-keyed marker. Existence is not a version-bound
whole-day certificate."* Re-ground it against the file.

What it must do -- the PRD's C3, verbatim:
*"Extend the producer's completion metadata contract, keeping legacy fields for existing consumers, to include a schema
version, master/date, run identity, expected source partitions, explicit non-applicable/empty dispositions, expected
table set, successful/failed outputs, counts and exact versioned silver objects. Publish qualified closure only after the
complete expected set is reconciled. The allowed completion object must carry sufficient sanitized closure facts itself;
the metadata role cannot follow references into meta/conversions or other prefixes. A missing output, failed conversion,
unexplained empty day, inconsistent grain, or ambiguous inventory is incomplete. Do not repair source data or rewrite
silver values as part of this extension."*

**Existing consumers you must not break**, measured at the cut by an unscoped read (`comp-find 'meta/complete' --files
--all`, 361 hits over 172,084 files): `infra/aws/terraform/opal-assets/silver.tf:756-759` -- the S3 notification
`advi-49f-silver-complete-accelerator` fires the 49F gold dispatcher on `s3:ObjectCreated:*` under
`schwab/08335338/meta/complete/`; `infra/aws/terraform/opal-assets/advi_49f_floor.tf` -- the schedule floor that reads the
same markers. AC13 re-runs that census with its own denominator and proves no field they read is removed or renamed.

**The vendored copy is not yours.** `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/` carries a copy of these
scripts for the Lambda package; `OG-c-2` vendors your merged files there and deploys. Do not edit it.

**Read:** the PRD's "C3 - sources, closure and date semantics"; `conversion_manifest.py`, `schwab_runtime.py`,
`schwab_conversion.py`, `schwab_schemas.py`; `data/assets/scripts/silver/tests/test_conversion_manifest.py` (the existing
tests, which stay green).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGC1-AC1" cell_refs="OG-c-1"><invocation>cd <WS> && timeout 120 py -3.12 -m pytest data/assets/scripts/silver/tests/test_conversion_manifest.py::test_ogc1_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGC1-AC1` (`test_ogc1_ac01`) -- the completion object gains a schema version, master and date, run identity, expected source partitions, explicit non-applicable and empty dispositions, the expected table set, successful and failed outputs, counts, and every silver object's key with its VersionId.

<criterion id="OGC1-AC2" cell_refs="OG-c-1"><invocation>cd <WS> && timeout 120 py -3.12 -m pytest data/assets/scripts/silver/tests/test_conversion_manifest.py::test_ogc1_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGC1-AC2` (`test_ogc1_ac02`) -- every legacy field keeps its name and meaning, by a golden test on a legacy fixture.

<criterion id="OGC1-AC3" cell_refs="OG-c-1"><invocation>cd <WS> && timeout 120 py -3.12 -m pytest data/assets/scripts/silver/tests/test_conversion_manifest.py::test_ogc1_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGC1-AC3` (`test_ogc1_ac03`) -- the complete fixture yields a qualified closure.

<criterion id="OGC1-AC4" cell_refs="OG-c-1"><invocation>cd <WS> && timeout 120 py -3.12 -m pytest data/assets/scripts/silver/tests/test_conversion_manifest.py::test_ogc1_ac04 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGC1-AC4` (`test_ogc1_ac04`) -- a partial event yields incomplete.

<criterion id="OGC1-AC5" cell_refs="OG-c-1"><invocation>cd <WS> && timeout 120 py -3.12 -m pytest data/assets/scripts/silver/tests/test_conversion_manifest.py::test_ogc1_ac05 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGC1-AC5` (`test_ogc1_ac05`) -- a failed sibling yields incomplete.

<criterion id="OGC1-AC6" cell_refs="OG-c-1"><invocation>cd <WS> && timeout 120 py -3.12 -m pytest data/assets/scripts/silver/tests/test_conversion_manifest.py::test_ogc1_ac06 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGC1-AC6` (`test_ogc1_ac06`) -- an idempotent existing output yields its stated disposition.

<criterion id="OGC1-AC7" cell_refs="OG-c-1"><invocation>cd <WS> && timeout 120 py -3.12 -m pytest data/assets/scripts/silver/tests/test_conversion_manifest.py::test_ogc1_ac07 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGC1-AC7` (`test_ogc1_ac07`) -- an overwrite yields its stated disposition.

<criterion id="OGC1-AC8" cell_refs="OG-c-1"><invocation>cd <WS> && timeout 120 py -3.12 -m pytest data/assets/scripts/silver/tests/test_conversion_manifest.py::test_ogc1_ac08 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGC1-AC8` (`test_ogc1_ac08`) -- concurrent completion yields exactly one qualified closure.

<criterion id="OGC1-AC9" cell_refs="OG-c-1"><invocation>cd <WS> && timeout 120 py -3.12 -m pytest data/assets/scripts/silver/tests/test_conversion_manifest.py::test_ogc1_ac09 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGC1-AC9` (`test_ogc1_ac09`) -- a typed empty day yields its explicit empty disposition.

<criterion id="OGC1-AC10" cell_refs="OG-c-1"><invocation>cd <WS> && timeout 120 py -3.12 -m pytest data/assets/scripts/silver/tests/test_conversion_manifest.py::test_ogc1_ac10 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGC1-AC10` (`test_ogc1_ac10`) -- an unexplained empty day, an inconsistent grain and an ambiguous inventory each yield incomplete.

<criterion id="OGC1-AC11" cell_refs="OG-c-1"><invocation>cd <WS> && timeout 120 py -3.12 -m pytest data/assets/scripts/silver/tests/test_conversion_manifest.py::test_ogc1_ac11 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGC1-AC11` (`test_ogc1_ac11`) -- the closure validator, given only the completion object, decides without reading another prefix.

<criterion id="OGC1-AC12" cell_refs="OG-c-1"><invocation>cd <WS> && timeout 120 py -3.12 -m pytest data/assets/scripts/silver/tests -q -p no:cacheprovider --color=no</invocation><expect>(?m)^[1-9][0-9]* passed(?![^\n]*(failed|error))</expect></criterion>
`OGC1-AC12` -- the `data/assets/scripts/silver/tests/` suite passes, count printed (the cut's baseline: 289 passed, 11 skipped).

<criterion id="OGC1-AC13" cell_refs="OG-c-1"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/probes/og_c1.py AC13</invocation><expect>(?m)^VERDICT: PASS-OGC1-AC13(?![0-9])</expect></criterion>
`OGC1-AC13` -- every reader of `meta/complete` found by an unscoped repo read (denominator printed; `silver.tf:756-759` and `advi_49f_floor.tf` included) is listed with what it reads, and none reads a field this cell removes or renames. The probe reads a census file your run of `comp-find 'meta/complete' --files --all` saved in your deliverables, and prints `VERDICT: PASS-OGC1-AC13` or `VERDICT: FAIL-OGC1-AC13 <reason>`.

<criterion id="OGC1-J1" cell_refs="OG-c-1" judgment="true"/>
`OGC1-J1` -- graded at L9 by 3.0.0_SA_CVO: the diff composes the marker only and rewrites no silver value. RECORD; NO VERDICT.

<expected_criteria>OGC1-AC1, OGC1-AC2, OGC1-AC3, OGC1-AC4, OGC1-AC5, OGC1-AC6, OGC1-AC7, OGC1-AC8, OGC1-AC9, OGC1-AC10, OGC1-AC11, OGC1-AC12, OGC1-AC13, OGC1-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Interpreter.** `py -3.12` (Python 3.12.10 at the cut, carrying pytest 9.0.2 and PyArrow 18.1.0). No venv and no package install in this cell.
- **Tests.** Each criterion names one test function added to `data/assets/scripts/silver/tests/test_conversion_manifest.py`; write exactly that name. No existing test is edited to make it pass.
- **Nothing deploys.** No `aws s3 cp`, no Lambda update, no Terraform, no replay, no write to `opal-data-assets`. Deploy and replay are `OG-c-2`'s, held on gate G-B.
- **No source repair.** You change how the marker is composed. You never rewrite a silver value or a bronze file.
- **Cross-firm law.** The code serves the two Schwab masters `08242234` and `08335338` under `schwab/`; it references no other firm's bucket or key prefix (`.tools/ds-precommit-check.py` runs in the commit gate).
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh` (py_compile, ds-precommit, ruff py39).
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W4-S<k>`, per the worker definition. Keep working after filing.
- **The preloaded context.** You start with the workspace CLAUDE.md and the auto-memory in context. Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
data/assets/scripts/silver/conversion_manifest.py
data/assets/scripts/silver/schwab_runtime.py
data/assets/scripts/silver/tests/test_conversion_manifest.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-c-1`, round 1 (section 3, S4).
<owned_cells>OG-c-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGC1-AC1` .. `OGC1-AC13`, `OGC1-J1` (14). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/NFRA_OPLGTW.TO-OG-c-1.closure-contract.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGC1-AC1,OGC1-AC2,OGC1-AC3,OGC1-AC4,OGC1-AC5,OGC1-AC6,OGC1-AC7,OGC1-AC8,OGC1-AC9,OGC1-AC10,OGC1-AC11,OGC1-AC12,OGC1-AC13,OGC1-J1`
BEFORE the `complete` flip. Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a
`status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.** Result file
`closure-contract.result.md` beside it, with the record's new schema. **Flip `complete` only when every MECHANICAL
criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. No project gate holds this build; its deploy is OG-c-2's, held on G-B.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell changes a producer's composition logic and deploys nothing; it adds no IAM operation, policy, principal or role to any principal the lens could trace.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood. The unscoped marker census (361 hits, 172,084 files scanned) is the consumer read this cell's AC13 repeats.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant); data/*/scripts/silver/ is the DS pipeline lane and admits a worker only by this order's <paths>.
</preflight>

Seating: slot ~4, queue position 1 (then `OG-c-2`). Round 1 of NFRA_OPLGTW, issued by `2.0.0_SA_COO~O` (seated msg
96971, LD-0567). Decomposition v1 @8768f46770. Suite baseline at the cut: 289 passed, 11 skipped (Python 3.12.10).
