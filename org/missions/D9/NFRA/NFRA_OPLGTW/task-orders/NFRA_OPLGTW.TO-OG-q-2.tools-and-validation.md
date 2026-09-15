# TO NFRA_OPLGTW.TO-OG-q-2 -- the five tools, request validation, the response envelope, cursors

<to_id>NFRA_OPLGTW.TO-OG-q-2</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~5</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-q-2` | **outcome_ref:** FWD-2, FWD-3, FWD-5 | **depends_on:** `OG-z-1`, `OG-z-3`, `OG-k-1`, `OG-o-1`, `OG-q-1` | **slot:** ~5, queue position 4

---

## WORKER FACE

### THE CELL

`OG-q-2` -- **the five Schwab tools, request validation, the response envelope and cursors**: new modules under
`infra/aws/ec2/opal-gateway/app/integrations/schwab/` (`integration.py`, `query.py`, `envelope.py`, `cursor.py`) and the
integration's registration in `app/integrations/registry.py`. You compose the merged pieces: the guard (`OG-z-1`), the
alias (`OG-z-3`), the catalog (`OG-k-1`), the audit entry point (`OG-o-1`) and the engine (`OG-q-1`).

The PRD's C4, verbatim, the paragraphs this cell owns:
- *"Five tools only: schwab_get_access returns authorized capabilities/current revision and availability;
  schwab_list_files accepts one master/dataset and bounded dates and returns opaque catalog IDs/date/format/size/download
  mode; schwab_describe_dataset returns authorized fields/types/units/grain/metric definitions; schwab_query executes one
  master/dataset/date; schwab_prepare_download accepts an authorized catalog ID or normalized query definition and returns
  an identity-bound ticket link. Shared get_access metadata is itself scoped and contains no hidden account IDs, storage
  keys or signed credentials."*
- *"Query shape is a typed object with master, dataset, business_date, mode, columns, filters, group_by, aggregates,
  order_by, page_size and optional cursor. Require exactly one rows/aggregate mode. Validate every field reference against
  the grant, including filters/groups/sorts. Filter values must match measured types; is_null has no value, in is a
  bounded list, all other operators take one value. Limit 20 filters, 100 values in any in-list, 10 group fields, 10
  aggregates and 10 order fields. An aggregate declares function/field/output alias; aliases must be unique and cannot
  shadow fields. Count rows or a named non-null field explicitly. No expressions, SQL fragments, regex evaluation,
  filesystem paths, code, external URLs or executable content are accepted."*
- *"Response envelope includes master ID/label, business date, dataset, opaque source/version references, scope
  summary/revision, matched row count, returned count, truncation, completeness and available-date/staleness metadata.
  Exact decimals are strings with schema-declared scale/unit, never lossy floating-point totals ... Aggregate totals are
  computed over the whole authorized match set before pagination. A row page may be truncated only with explicit counts
  and a cursor; an incompletely scanned aggregate is an error."*
- *"Limit the entire serialized MCP result to 500 rows, 100,000 Unicode codepoints and 131,072 UTF-8 bytes, including all
  content blocks, structuredContent and duplicated text. Serialize and measure before emission, reducing a rows page or
  failing if metadata alone exceeds the cap. Cursor lifetime is 5 minutes and binds identity/revision/query/source
  snapshots and stable order; it is opaque and authenticated, never caller-editable offset authority. Tie-break rows
  deterministically using a validated unique source grain. If a dataset lacks that grain, reject paging until the input is
  corrected."*
- From C2: *"All cache/cursor/ticket keys bind principal, revision, master, dataset, dates, projection and source
  versions. Before response emission or download start, re-read the revision; discard stale work."*

Contract enums you validate against: `tools`, `query_modes`, `filter_operators`, `aggregate_operators`,
`order_directions`, `error_codes`, `fields`, `limits` (`response_rows` 500, `response_unicode_codepoints` 100000,
`response_utf8_bytes` 131072, `cursor_seconds` 300, `filter_count` 20, `filter_in_values` 100, `group_fields` 10,
`aggregates` 10, `order_fields` 10). `schwab_prepare_download` registers here and hands its ticket to `OG-x-1`'s export
module, which lands later in this queue: register the tool with its validated input and a ticket-issuing call site
that `OG-x-1` fills.

**The flag.** Decomposition bound 9 says the feature flag defaults off. The integration registers only when its
enablement configuration is on, and the default configuration leaves it off (AC24).

**Read:** the PRD's "C2" (cache/cursor paragraph) and "C4"; the contract; `app/integrations/base.py`,
`app/integrations/registry.py`, `app/integrations/ycharts/integration.py` (an existing integration's shape),
`app/data_entitlement.py`, `app/account_ref.py`, `app/schwab_audit.py`, `app/integrations/schwab/catalog.py` and
`engine.py`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGQ2-AC1" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC1` (`test_ogq2_ac01`) -- exactly the contract's five tools are registered.

<criterion id="OGQ2-AC2" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC2` (`test_ogq2_ac02`) -- an unknown enum value or an extra property is refused.

<criterion id="OGQ2-AC3" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC3` (`test_ogq2_ac03`) -- a request carries exactly one of rows mode or aggregate mode.

<criterion id="OGQ2-AC4" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac04 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC4` (`test_ogq2_ac04`) -- a field reference outside the grant, in columns, filters, groups, sorts or aggregates, is refused without revealing the field (A6).

<criterion id="OGQ2-AC5" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac05 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC5` (`test_ogq2_ac05`) -- filter values match their measured types, `is_null` takes no value, and `in` takes at most 100 values.

<criterion id="OGQ2-AC6" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac06 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC6` (`test_ogq2_ac06`) -- more than 20 filters, 10 group fields, 10 aggregates or 10 order fields is refused.

<criterion id="OGQ2-AC7" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac07 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC7` (`test_ogq2_ac07`) -- an aggregate declares function, field and alias, and a duplicate or shadowing alias is refused.

<criterion id="OGQ2-AC8" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac08 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC8` (`test_ogq2_ac08`) -- no expression, SQL fragment, regex, path, code or URL is accepted, by a fuzz corpus.

<criterion id="OGQ2-AC9" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac09 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC9` (`test_ogq2_ac09`) -- (difference) a cache warmed under a broader grant is not served to the narrower grant, and the same request under the broader grant is (A6).

<criterion id="OGQ2-AC10" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac10 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC10` (`test_ogq2_ac10`) -- after revocation, a warmed cache entry is denied.

<criterion id="OGQ2-AC11" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac11 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC11` (`test_ogq2_ac11`) -- cache, cursor and ticket keys bind principal, revision, master, dataset, dates, projection and source versions.

<criterion id="OGQ2-AC12" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac12 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC12` (`test_ogq2_ac12`) -- the envelope carries master ID and label, business date, dataset, opaque source references, scope summary and revision, matched count, returned count, truncation, completeness and available-date and staleness metadata.

<criterion id="OGQ2-AC13" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac13 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC13` (`test_ogq2_ac13`) -- decimals are strings with their schema scale and unit.

<criterion id="OGQ2-AC14" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac14 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC14` (`test_ogq2_ac14`) -- aggregate totals cover the whole authorized match set before pagination.

<criterion id="OGQ2-AC15" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac15 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC15` (`test_ogq2_ac15`) -- an incompletely scanned aggregate returns an error.

<criterion id="OGQ2-AC16" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac16 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC16` (`test_ogq2_ac16`) -- the whole serialized result stays within 500 rows, 100,000 codepoints and 131,072 UTF-8 bytes, counting every block, measured before emission (A18).

<criterion id="OGQ2-AC17" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac17 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC17` (`test_ogq2_ac17`) -- metadata alone over the cap returns an error.

<criterion id="OGQ2-AC18" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac18 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC18` (`test_ogq2_ac18`) -- a cursor is authenticated, lives 5 minutes and binds identity, revision, query and snapshots.

<criterion id="OGQ2-AC19" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac19 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC19` (`test_ogq2_ac19`) -- an edited cursor and an expired cursor are each refused.

<criterion id="OGQ2-AC20" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac20 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC20` (`test_ogq2_ac20`) -- rows tie-break deterministically on a validated unique grain, and a dataset without one refuses paging.

<criterion id="OGQ2-AC21" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac21 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC21` (`test_ogq2_ac21`) -- (difference) a revision change during a job discards the result, and an unchanged revision releases it.

<criterion id="OGQ2-AC22" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac22 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC22` (`test_ogq2_ac22`) -- prompt-like text inside data comes back as data and invokes no tool, widens no filter and changes no grant (A12).

<criterion id="OGQ2-AC23" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac23 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC23` (`test_ogq2_ac23`) -- every tool call writes its audit event through `OG-o-1` before release.

<criterion id="OGQ2-AC24" cell_refs="OG-q-2"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac24 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ2-AC24` (`test_ogq2_ac24`) -- with the default configuration the Schwab integration is not registered, and with its enablement on it is (decomposition bound 9, made mechanical).

<expected_criteria>OGQ2-AC1, OGQ2-AC2, OGQ2-AC3, OGQ2-AC4, OGQ2-AC5, OGQ2-AC6, OGQ2-AC7, OGQ2-AC8, OGQ2-AC9, OGQ2-AC10, OGQ2-AC11, OGQ2-AC12, OGQ2-AC13, OGQ2-AC14, OGQ2-AC15, OGQ2-AC16, OGQ2-AC17, OGQ2-AC18, OGQ2-AC19, OGQ2-AC20, OGQ2-AC21, OGQ2-AC22, OGQ2-AC23, OGQ2-AC24</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off (after `OG-z-3` and `OG-k-1` merged). Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **Tests.** Each criterion names one test function in `tests/test_schwab_query.py`; write exactly that name. Offline, moto and synthetic Parquet; no Schwab object is read.
- **Limits are ceilings.** Never raise one to make a test pass.
- **The known red test.** `tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1). Never edit it or `identity_tool_allowlist.txt`.
- **Code.** The commit gate lints with ruff for Python 3.9 syntax. `mcp==1.28.0` is not raised. Existing integrations keep their registration and behaviour. Nothing deploys.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No secret in evidence.**
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W5-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/query.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/envelope.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/cursor.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/__init__.py
infra/aws/ec2/opal-gateway/app/integrations/registry.py
infra/aws/ec2/opal-gateway/tests/test_schwab_query.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-q-2`, round 1 (section 3, S6; section 8 bound 9).
<owned_cells>OG-q-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGQ2-AC1` .. `OGQ2-AC24` (24). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/NFRA_OPLGTW.TO-OG-q-2.tools-and-validation.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGQ2-AC1,OGQ2-AC2,OGQ2-AC3,OGQ2-AC4,OGQ2-AC5,OGQ2-AC6,OGQ2-AC7,OGQ2-AC8,OGQ2-AC9,OGQ2-AC10,OGQ2-AC11,OGQ2-AC12,OGQ2-AC13,OGQ2-AC14,OGQ2-AC15,OGQ2-AC16,OGQ2-AC17,OGQ2-AC18,OGQ2-AC19,OGQ2-AC20,OGQ2-AC21,OGQ2-AC22,OGQ2-AC23,OGQ2-AC24`
BEFORE the `complete` flip. Result file `tools-and-validation.result.md` beside it. **Flip `complete` only when every
MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. No project gate holds this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell composes modules that already own their AWS calls (OG-k-1 the reads, OG-o-1 the audit write, OG-d-1 the state); it adds no AWS operation, policy, principal or role of its own.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~5, queue position 4, handed after `OG-k-1` drains and `OG-z-3` merges. Round 1 of NFRA_OPLGTW, issued by
`2.0.0_SA_COO~O` (seated msg 96971, LD-0567). Decomposition v1 @8768f46770. AC24 is the one criterion the cut derives
from a decomposition bound (s.8 bound 9) rather than from the cell's own acceptance list; recorded here so the L9 grade
can weigh it.
