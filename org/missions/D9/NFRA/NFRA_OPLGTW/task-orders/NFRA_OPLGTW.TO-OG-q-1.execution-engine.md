# TO NFRA_OPLGTW.TO-OG-q-1 -- the bounded execution engine

<to_id>NFRA_OPLGTW.TO-OG-q-1</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~5</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-q-1` | **outcome_ref:** FWD-5, FWD-7 | **depends_on:** `OG-p-1` | **slot:** ~5, queue position 2

---

## WORKER FACE

### THE CELL

`OG-q-1` -- **the bounded execution engine**, a new module `infra/aws/ec2/opal-gateway/app/integrations/schwab/engine.py`
that runs every Schwab query and export job in a child process with hard limits, plus the PyArrow and DuckDB pins in
`infra/aws/ec2/opal-gateway/requirements.txt`. The tool layer above you (`OG-q-2`) never touches Parquet or SQL directly.

The PRD's C4, verbatim: *"Use PyArrow for Parquet projection and a local DuckDB engine for validated, parameterized
relational operations after account/column policy is applied. Disable external access, extension loading, remote files
and SQL supplied by callers; use explicit types and whitelisted generated operators. Run each job in a cancellable child
process outside the Gateway event loop, with 256 MiB resident-memory cap and clean temporary files. The initial hard caps
are design ceilings to benchmark, not measured capacity: 1 job per principal, 2 globally, no waiting queue; 30 seconds for
query or export, 12 compressed source objects/64 MiB including policy dependencies. Return BUSY or LIMIT_EXCEEDED with a
safe narrowing suggestion when limits would be exceeded. A killed/timed-out job produces no partial successful total."*
And: *"Admission must reserve the measured existing Gateway peak RSS plus 25 percent and 128 MiB operating headroom before
starting a child, even below the global job cap; insufficient headroom returns BUSY."*

Contract `limits`: `job_memory_bytes` 268435456, `query_deadline_seconds` 30, `export_deadline_seconds` 30,
`source_objects` 12, `source_compressed_bytes` 67108864, `per_principal_jobs` 1, `global_jobs` 2, `queue_size` 0;
`capacity.admission_existing_peak_rss_multiplier` 1.25, `admission_os_reserve_bytes` 134217728.

**The measured peak RSS** is `OG-p-1`'s, in `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/BASELINE.json`
(merged at your hand-off). Use that value as the engine's configured default and cite it; AC7's test reads the file. The
host's Python version, which AC13's wheel check targets, is in the same file.

**Read:** the PRD's "C4" and "Operator journey, audit and release" (capacity paragraph); the contract's `limits` and
`capacity`; `requirements.txt` (the `mcp==1.28.0` pin and why it is pinned); the baseline above.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGQ1-AC1" cell_refs="OG-q-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py::test_ogq1_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ1-AC1` (`test_ogq1_ac01`) -- each job runs in a child process outside the event loop.

<criterion id="OGQ1-AC2" cell_refs="OG-q-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py::test_ogq1_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ1-AC2` (`test_ogq1_ac02`) -- (difference) the event loop's latency probe stays responsive while a job runs, against the same probe with a blocking in-loop job.

<criterion id="OGQ1-AC3" cell_refs="OG-q-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py::test_ogq1_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ1-AC3` (`test_ogq1_ac03`) -- a job over 256 MiB resident memory is killed and returns LIMIT_EXCEEDED.

<criterion id="OGQ1-AC4" cell_refs="OG-q-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py::test_ogq1_ac04 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ1-AC4` (`test_ogq1_ac04`) -- a job over 30 seconds is killed and returns no partial total (the test may lower the deadline through the engine's configuration to stay inside the 120-second bound).

<criterion id="OGQ1-AC5" cell_refs="OG-q-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py::test_ogq1_ac05 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ1-AC5` (`test_ogq1_ac05`) -- a second concurrent job for one principal returns BUSY.

<criterion id="OGQ1-AC6" cell_refs="OG-q-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py::test_ogq1_ac06 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ1-AC6` (`test_ogq1_ac06`) -- a third concurrent job globally returns BUSY, with no queue.

<criterion id="OGQ1-AC7" cell_refs="OG-q-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py::test_ogq1_ac07 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ1-AC7` (`test_ogq1_ac07`) -- admission reserves `OG-p-1`'s measured existing peak RSS (value cited, read from its baseline file) times 1.25 plus 128 MiB, and insufficient headroom returns BUSY.

<criterion id="OGQ1-AC8" cell_refs="OG-q-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py::test_ogq1_ac08 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ1-AC8` (`test_ogq1_ac08`) -- a request over 12 source objects or 64 MiB compressed, policy dependencies included, returns LIMIT_EXCEEDED with a narrowing suggestion.

<criterion id="OGQ1-AC9" cell_refs="OG-q-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py::test_ogq1_ac09 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ1-AC9` (`test_ogq1_ac09`) -- DuckDB runs with external access, extension loading and remote files disabled, each setting asserted.

<criterion id="OGQ1-AC10" cell_refs="OG-q-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py::test_ogq1_ac10 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ1-AC10` (`test_ogq1_ac10`) -- no caller-supplied string reaches the generated SQL, by a fuzz corpus.

<criterion id="OGQ1-AC11" cell_refs="OG-q-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py::test_ogq1_ac11 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ1-AC11` (`test_ogq1_ac11`) -- temporary files are gone after success, failure, cancellation and startup cleanup.

<criterion id="OGQ1-AC12" cell_refs="OG-q-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py::test_ogq1_ac12 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ1-AC12` (`test_ogq1_ac12`) -- cancelling the awaiting request terminates the child process.

<criterion id="OGQ1-AC13" cell_refs="OG-q-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q1.py AC13</invocation><expect>(?m)^VERDICT: PASS-OGQ1-AC13(?![0-9])</expect></criterion>
`OGQ1-AC13` -- the pinned PyArrow and DuckDB wheels resolve for linux aarch64 on the host's Python (the probe runs `pip download --only-binary=:all: --no-deps --platform manylinux2014_aarch64 --python-version <host>` for each pin into `.scratch/`, then prints `VERDICT: PASS-OGQ1-AC13` or `VERDICT: FAIL-OGQ1-AC13 <reason>`).

<criterion id="OGQ1-AC14" cell_refs="OG-q-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py::test_ogq1_ac14 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ1-AC14` (`test_ogq1_ac14`) -- `mcp==1.28.0` is unchanged in `requirements.txt`.

<expected_criteria>OGQ1-AC1, OGQ1-AC2, OGQ1-AC3, OGQ1-AC4, OGQ1-AC5, OGQ1-AC6, OGQ1-AC7, OGQ1-AC8, OGQ1-AC9, OGQ1-AC10, OGQ1-AC11, OGQ1-AC12, OGQ1-AC13, OGQ1-AC14</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off (after `OG-p-1` merged). Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. After you pin PyArrow and DuckDB, reinstall from the edited file. Never commit `.venv-og/` or `.scratch/`.
- **Tests.** Each criterion names one test function in `tests/test_schwab_engine.py`; write exactly that name. Fixtures are synthetic Parquet you generate in the test; no Schwab object is read.
- **Limits are ceilings.** You implement the contract's values as configuration; you never raise one to make a test pass.
- **The known red test.** `tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1). Never edit it or `identity_tool_allowlist.txt`.
- **Code.** The commit gate lints with ruff for Python 3.9 syntax. `mcp==1.28.0` is not raised. Nothing deploys.
- **No egress off Opal infrastructure** beyond the package index the Interpreter bound and AC13 name. No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W5-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/app/integrations/schwab/__init__.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/engine.py
infra/aws/ec2/opal-gateway/requirements.txt
infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-q-1`, round 1 (section 3, S6).
<owned_cells>OG-q-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGQ1-AC1` .. `OGQ1-AC14` (14). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/NFRA_OPLGTW.TO-OG-q-1.execution-engine.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGQ1-AC1,OGQ1-AC2,OGQ1-AC3,OGQ1-AC4,OGQ1-AC5,OGQ1-AC6,OGQ1-AC7,OGQ1-AC8,OGQ1-AC9,OGQ1-AC10,OGQ1-AC11,OGQ1-AC12,OGQ1-AC13,OGQ1-AC14`
BEFORE the `complete` flip. Result file `execution-engine.result.md` beside it. **Flip `complete` only when every
MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. No project gate holds this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell's engine reads only what it is handed; credentials and object reads are OG-k-1's, so it adds no AWS operation, policy, principal or role.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~5, queue position 2, handed after `OG-o-1` drains and `OG-p-1` merges. Round 1 of NFRA_OPLGTW, issued by
`2.0.0_SA_COO~O` (seated msg 96971, LD-0567). Decomposition v1 @8768f46770. The cut's interpreter carries PyArrow 18.1.0
and DuckDB 1.5.0 for local tests.
