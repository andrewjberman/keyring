# TO NFRA_OPLGTW.TO-OG-k-1 -- the authorized catalog and the assumed-role credential adapter

<to_id>NFRA_OPLGTW.TO-OG-k-1</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~5</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-k-1` | **outcome_ref:** FWD-2, FWD-3, FWD-5 | **depends_on:** `OG-d-1`, `OG-z-1`, `OG-c-1` | **slot:** ~5, queue position 3

---

## WORKER FACE

### THE CELL

`OG-k-1` -- **the authorized catalog and the assumed-role credential adapter**: new modules
`infra/aws/ec2/opal-gateway/app/integrations/schwab/catalog.py` and `.../schwab/aws_roles.py`, and a new AuthKind in
`app/integrations/base.py`. The catalog decides which master/dataset/date snapshots exist, from the producer's qualified
completion records and the exact silver object versions they name, and hands the engine opaque file IDs.

What the source does today (certified L4 rectangle, S4-query): *"AuthKind values delegated_user/shared_secret/none;
assumed-role kind not declared"*; *"comp-find assume_role and aws_entitlements each returned zero in 47 gateway app files"*.

What it must do -- the PRD's C3 and C6, verbatim:
- *"Gateway catalog construction validates the closure record and independently HEADs every named silver object. It
  persists an immutable catalog snapshot with the closure version, table/master/date, object VersionIds, sizes, schema
  fingerprint, row counts, validation result and opaque authorized file IDs. GET every data object by that VersionId.
  Reject null/unversioned identities or changed/unavailable versions. Revalidate source membership and byte bounds; no
  marker may introduce another bucket/master/dataset. Legacy markers are nonqualifying until a controlled producer replay
  or metadata backfill reconciles against original inputs and exact current output versions."*
- *"For each master/dataset the rolling window includes the latest qualified complete business date and the previous 29
  calendar days; do not silently fill missing dates from another master or dataset. The available dates and latest
  qualified date are returned explicitly. A fixed-date grant is an enumerated date set. Staleness is reported as days
  since the qualified business date and source observation time."*
- *"All silver reads use the dedicated assumed role ... No fallback to Gateway instance credentials, broad
  opal-assets-read role, role selected by model, or role chaining."* and *"a separate Gateway-assumable
  `opal-mcp-schwab-catalog-read` role for the two exact completion prefixes ... The data role does not gain metadata
  access."*

The record schema is `OG-c-1`'s (its result file under `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/`);
the scope is `OG-z-1`'s; storage is `OG-d-1`'s adapter under `RUNTIME#catalog`. The live role names are in
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/SCHWAB_IDENTITIES.json` if merged; your code reads
them from configuration, and your tests use moto (S3 with versioning, STS).

**Read:** the PRD's "C3" and "C6"; the contract (`data_prefixes`, `completion_prefixes`, `catalog_statuses`,
`grant_date_modes`, `reader_role`, `catalog_role`); `app/integrations/base.py`, `app/access_state.py`,
`app/data_entitlement.py`; `OG-c-1`'s result file.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGK1-AC1" cell_refs="OG-k-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_catalog.py::test_ogk1_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGK1-AC1` (`test_ogk1_ac01`) -- the assumed-role adapter is a new AuthKind, and calls STS with the role's dedicated ExternalId.

<criterion id="OGK1-AC2" cell_refs="OG-k-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_catalog.py::test_ogk1_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGK1-AC2` (`test_ogk1_ac02`) -- the data-policy check precedes every credential fetch, by a call-order assertion.

<criterion id="OGK1-AC3" cell_refs="OG-k-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_catalog.py::test_ogk1_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGK1-AC3` (`test_ogk1_ac03`) -- (difference) with the adapter failing, no S3 client is built from ambient or instance credentials, and with it healthy the role session is used.

<criterion id="OGK1-AC4" cell_refs="OG-k-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_catalog.py::test_ogk1_ac04 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGK1-AC4` (`test_ogk1_ac04`) -- closure validation uses the catalog role only and data HEADs use the data role only.

<criterion id="OGK1-AC5" cell_refs="OG-k-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_catalog.py::test_ogk1_ac05 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGK1-AC5` (`test_ogk1_ac05`) -- every named silver object is HEADed by its VersionId.

<criterion id="OGK1-AC6" cell_refs="OG-k-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_catalog.py::test_ogk1_ac06 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGK1-AC6` (`test_ogk1_ac06`) -- a null, unversioned, changed or unavailable object yields incomplete or unavailable, one fixture each.

<criterion id="OGK1-AC7" cell_refs="OG-k-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_catalog.py::test_ogk1_ac07 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGK1-AC7` (`test_ogk1_ac07`) -- a marker naming another bucket, master or dataset is rejected.

<criterion id="OGK1-AC8" cell_refs="OG-k-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_catalog.py::test_ogk1_ac08 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGK1-AC8` (`test_ogk1_ac08`) -- the catalog snapshot persisted under `RUNTIME#` carries the closure version, table, master, date, VersionIds, sizes, schema fingerprint, row counts, validation result and opaque file IDs.

<criterion id="OGK1-AC9" cell_refs="OG-k-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_catalog.py::test_ogk1_ac09 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGK1-AC9` (`test_ogk1_ac09`) -- a second write of one snapshot key is refused.

<criterion id="OGK1-AC10" cell_refs="OG-k-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_catalog.py::test_ogk1_ac10 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGK1-AC10` (`test_ogk1_ac10`) -- (difference) a legacy marker yields unavailable, and the qualified fixture for the same date yields a snapshot.

<criterion id="OGK1-AC11" cell_refs="OG-k-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_catalog.py::test_ogk1_ac11 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGK1-AC11` (`test_ogk1_ac11`) -- the rolling window is the latest qualified business date plus the previous 29 calendar days, per master and dataset.

<criterion id="OGK1-AC12" cell_refs="OG-k-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_catalog.py::test_ogk1_ac12 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGK1-AC12` (`test_ogk1_ac12`) -- fixed-date mode takes an enumerated date set.

<criterion id="OGK1-AC13" cell_refs="OG-k-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_catalog.py::test_ogk1_ac13 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGK1-AC13` (`test_ogk1_ac13`) -- the response returns the available dates and the latest qualified date.

<criterion id="OGK1-AC14" cell_refs="OG-k-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_catalog.py::test_ogk1_ac14 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGK1-AC14` (`test_ogk1_ac14`) -- no date is filled from another master or dataset.

<criterion id="OGK1-AC15" cell_refs="OG-k-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_catalog.py::test_ogk1_ac15 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGK1-AC15` (`test_ogk1_ac15`) -- staleness is reported as days since the qualified business date, with the observation time.

<expected_criteria>OGK1-AC1, OGK1-AC2, OGK1-AC3, OGK1-AC4, OGK1-AC5, OGK1-AC6, OGK1-AC7, OGK1-AC8, OGK1-AC9, OGK1-AC10, OGK1-AC11, OGK1-AC12, OGK1-AC13, OGK1-AC14, OGK1-AC15</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off (after `OG-z-1` and `OG-c-1` merged). Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **Tests.** Each criterion names one test function in `tests/test_schwab_catalog.py`; write exactly that name. Offline against moto; no Schwab object is read in this cell.
- **Cross-firm law.** The catalog admits only `opal-data-assets` under the contract's two masters and three datasets; a marker naming anything else is rejected (AC7), never followed.
- **The known red test.** `tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1). Never edit it or `identity_tool_allowlist.txt`.
- **Code.** The commit gate lints with ruff for Python 3.9 syntax. `mcp==1.28.0` is not raised. Existing AuthKind values and their integrations keep their behaviour. Nothing deploys.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W5-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/app/integrations/schwab/catalog.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/aws_roles.py
infra/aws/ec2/opal-gateway/app/integrations/base.py
infra/aws/ec2/opal-gateway/tests/test_schwab_catalog.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-k-1`, round 1 (section 3, S5).
<owned_cells>OG-k-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGK1-AC1` .. `OGK1-AC15` (15). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/NFRA_OPLGTW.TO-OG-k-1.catalog.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGK1-AC1,OGK1-AC2,OGK1-AC3,OGK1-AC4,OGK1-AC5,OGK1-AC6,OGK1-AC7,OGK1-AC8,OGK1-AC9,OGK1-AC10,OGK1-AC11,OGK1-AC12,OGK1-AC13,OGK1-AC14,OGK1-AC15`
BEFORE the `complete` flip. Result file `catalog.result.md` beside it. **Flip `complete` only when every MECHANICAL
criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. No project gate holds this cell.
comp-iam: RUN at L5 -- comp-iam service opal-gateway, DESIRED plane, 473 .tf files scanned, 3 operations all UNRESOLVABLE-RESOURCE, 27 policy blocks NOT ATTACHED, 2 deny statements unparsed. This cell adds sts:AssumeRole for two roles and s3 HeadObject/GetObjectVersion under them; OG-i-2 owns the grants and their live proof; the instance records the lens re-run over this cell's source.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~5, queue position 3, handed after `OG-q-1` drains and `OG-z-1` and `OG-c-1` merge. Round 1 of NFRA_OPLGTW,
issued by `2.0.0_SA_COO~O` (seated msg 96971, LD-0567). Decomposition v1 @8768f46770.
