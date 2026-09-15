# TO NFRA_OPLGTW.TO-OG-q-3 -- snapshot and metric semantics

<to_id>NFRA_OPLGTW.TO-OG-q-3</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~5</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-q-3` | **outcome_ref:** FWD-2, FWD-5 | **depends_on:** `OG-q-2` | **slot:** ~5, queue position 5

---

## WORKER FACE

### THE CELL

`OG-q-3` -- **snapshot and metric semantics**: a new module `infra/aws/ec2/opal-gateway/app/integrations/schwab/semantics.py`
and the dataset descriptions in `.../schwab/datasets.json`. These are the rules that keep an answer true: which sums are
meaningful, which are refused, and what each field means.

The PRD's C3, verbatim:
- *"Positions/balances are snapshots at one date. Grouping never removes master/date identity and never sums snapshots
  across dates. Both-master questions use separate tool calls/results; date comparisons use separately authorized
  snapshots and exact decimal deltas. Vendor balance fields overlap: permit a named field's sum across approved accounts,
  never construct a cash/AUA total by adding different balance fields. Quantity sums require grouping by CUSIP and
  long/short indicator; price is nonadditive. Duplicate/conflicting source grains produce unavailable, not silent
  deduplication. Dataset description records grain, field type, unit, sign and null semantics from measured source plus
  independent fixtures. Unsupported/unverified metrics are refused."*
- *"The asset reference dataset carries only its approved security fields. For a partial-account grant restrict its
  CUSIPs to holdings of the authorized accounts for that same master/date, using a qualified position snapshot solely
  for policy selection. This internal policy filter is not a user-facing enrichment join. Its position objects count
  toward the same object/byte/deadline limits; absent qualification denies the asset read. No other cross-dataset join is
  enabled in v1."*

Contract: `fields`, `additive_fields` (dim_position: the five quantity/market-value fields; dim_balance: the seven balance
fields; dim_asset: none), `quantity_sum_required_groups` = `cusip`, `l_s`. Measured source types (certified L4
rectangle, S3-data): positions quantity fields `decimal128(15,5)`, `market_value_settled_unsettled` `decimal128(17,4)`,
`closing_price` `decimal128(16,5)`, `business_date` `date32`; proposed balance value fields `decimal128(15,2)`; `dim_asset`
has no `business_date` column (use the partition date). Cite `data/assets/scripts/silver/schwab_schemas.py` and
`schwab_projections.py` for each field description.

**Read:** the PRD's "C3" and "C4"; the contract; `data/assets/scripts/silver/schwab_schemas.py`, `schwab_projections.py`;
`app/integrations/schwab/query.py` and `engine.py` (the previous cells' modules).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGQ3-AC1" cell_refs="OG-q-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_semantics.py::test_ogq3_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ3-AC1` (`test_ogq3_ac01`) -- grouping never drops master or date identity.

<criterion id="OGQ3-AC2" cell_refs="OG-q-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_semantics.py::test_ogq3_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ3-AC2` (`test_ogq3_ac02`) -- a sum across dates is refused.

<criterion id="OGQ3-AC3" cell_refs="OG-q-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_semantics.py::test_ogq3_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ3-AC3` (`test_ogq3_ac03`) -- a both-master question returns separate results and no combined total.

<criterion id="OGQ3-AC4" cell_refs="OG-q-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_semantics.py::test_ogq3_ac04 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ3-AC4` (`test_ogq3_ac04`) -- a date comparison uses separately authorized snapshots and an exact decimal delta.

<criterion id="OGQ3-AC5" cell_refs="OG-q-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_semantics.py::test_ogq3_ac05 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ3-AC5` (`test_ogq3_ac05`) -- a named balance field's sum across approved accounts is allowed.

<criterion id="OGQ3-AC6" cell_refs="OG-q-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_semantics.py::test_ogq3_ac06 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ3-AC6` (`test_ogq3_ac06`) -- a cash or AUA total built from different balance fields is refused.

<criterion id="OGQ3-AC7" cell_refs="OG-q-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_semantics.py::test_ogq3_ac07 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ3-AC7` (`test_ogq3_ac07`) -- a quantity sum without grouping by `cusip` and `l_s` is refused.

<criterion id="OGQ3-AC8" cell_refs="OG-q-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_semantics.py::test_ogq3_ac08 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ3-AC8` (`test_ogq3_ac08`) -- a price aggregation is refused.

<criterion id="OGQ3-AC9" cell_refs="OG-q-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_semantics.py::test_ogq3_ac09 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ3-AC9` (`test_ogq3_ac09`) -- a duplicate or conflicting grain returns unavailable and never deduplicates.

<criterion id="OGQ3-AC10" cell_refs="OG-q-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_semantics.py::test_ogq3_ac10 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ3-AC10` (`test_ogq3_ac10`) -- every field's description carries grain, type, unit, sign and null semantics, each with its source.

<criterion id="OGQ3-AC11" cell_refs="OG-q-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_semantics.py::test_ogq3_ac11 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ3-AC11` (`test_ogq3_ac11`) -- under a partial-account grant, `dim_asset` returns only CUSIPs the authorized accounts hold on the same master and date, by a qualified position snapshot.

<criterion id="OGQ3-AC12" cell_refs="OG-q-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_semantics.py::test_ogq3_ac12 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ3-AC12` (`test_ogq3_ac12`) -- those position objects count toward the object, byte and deadline limits.

<criterion id="OGQ3-AC13" cell_refs="OG-q-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_semantics.py::test_ogq3_ac13 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ3-AC13` (`test_ogq3_ac13`) -- an unqualified position snapshot denies the asset read.

<criterion id="OGQ3-AC14" cell_refs="OG-q-3"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_semantics.py::test_ogq3_ac14 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ3-AC14` (`test_ogq3_ac14`) -- an unsupported or unverified metric is refused.

<expected_criteria>OGQ3-AC1, OGQ3-AC2, OGQ3-AC3, OGQ3-AC4, OGQ3-AC5, OGQ3-AC6, OGQ3-AC7, OGQ3-AC8, OGQ3-AC9, OGQ3-AC10, OGQ3-AC11, OGQ3-AC12, OGQ3-AC13, OGQ3-AC14</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off (after `OG-q-2` merged). Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **Tests.** Each criterion names one test function in `tests/test_schwab_semantics.py`; write exactly that name. Synthetic fixtures only; no Schwab object is read.
- **No enrichment join.** The asset policy filter selects CUSIPs for policy only; it is never offered as a user-facing join.
- **The known red test.** `tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1). Never edit it or `identity_tool_allowlist.txt`.
- **Code.** The commit gate lints with ruff for Python 3.9 syntax. `mcp==1.28.0` is not raised. Nothing deploys.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W5-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/app/integrations/schwab/semantics.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/datasets.json
infra/aws/ec2/opal-gateway/app/integrations/schwab/query.py
infra/aws/ec2/opal-gateway/tests/test_schwab_semantics.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-q-3`, round 1 (section 3, S6).
<owned_cells>OG-q-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGQ3-AC1` .. `OGQ3-AC14` (14). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/NFRA_OPLGTW.TO-OG-q-3.snapshot-semantics.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGQ3-AC1,OGQ3-AC2,OGQ3-AC3,OGQ3-AC4,OGQ3-AC5,OGQ3-AC6,OGQ3-AC7,OGQ3-AC8,OGQ3-AC9,OGQ3-AC10,OGQ3-AC11,OGQ3-AC12,OGQ3-AC13,OGQ3-AC14`
BEFORE the `complete` flip. Result file `snapshot-semantics.result.md` beside it. **Flip `complete` only when every
MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. No project gate holds this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell adds rules over data already read; it adds no AWS operation, policy, principal or role.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~5, queue position 5, handed after `OG-q-2` merges. Round 1 of NFRA_OPLGTW, issued by `2.0.0_SA_COO~O`
(seated msg 96971, LD-0567). Decomposition v1 @8768f46770.
