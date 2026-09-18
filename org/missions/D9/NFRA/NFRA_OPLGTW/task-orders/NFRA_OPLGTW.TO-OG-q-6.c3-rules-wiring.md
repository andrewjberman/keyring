# TO NFRA_OPLGTW.TO-OG-q-6 -- the four remaining NOT-ENFORCED C3 rules, wired on the live path under ONE mutant

<to_id>NFRA_OPLGTW.TO-OG-q-6</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~5</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.9 @e09219470f | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.1 | **Decomp cell:** `OG-q-6` | **outcome_ref:** FWD-2, FWD-5 | **depends_on:** `OG-q-4`, `OG-q-5` (both wired on the live path) | **precedes:** `OG-v-2`'s last re-hand | **slot:** ~5

---

## WORKER FACE

### THE CELL

`OG-q-6` -- **wire the FOUR remaining NOT-ENFORCED C3 rules the census found.** Your own C3 call-path census
(`deliverables/0.9.0_WK_NFRA_OPLGTW~5/C3_CALL_PATH_CENSUS.md`, `OGQ5-AC5` PASS @`5c372a312f`) measured 29 rules and
found 5 NOT-ENFORCED. One was `OG-q-5`'s half one and is now wired. These four remain, each an EXISTING
`semantics.py` function that nothing on the query path calls:

| census row | the C3 rule | the function that exists | 
|---|---|---|
| **R20** [P4.S2] | "Grouping never removes master/date identity and never sums snapshots across dates." | `assert_grouping_preserves_identity()` (`semantics.py:173-181`) |
| **R22** [P4.S4] | the NEGATIVE half: "never construct a cash/AUA total by adding different balance fields" | `assert_field_summable()` and its siblings |
| **R24** [P4.S6] | "Duplicate/conflicting source grains produce unavailable, not silent deduplication." | `assert_unique_grain()` (`semantics.py:285-295`) |
| **R25** [P4.S7] | the dataset description records grain, type, unit, SIGN and NULL semantics (grain and type/unit are already exposed; sign and null are not) | `datasets.json` + the describe path |

**Read the census rows themselves before you start** -- each carries its C3 sentence, its coordinates, the function
it names and why the verdict is NOT-ENFORCED. They are your specification; this table is a summary of them.

**THE ONE-CELL PREMISE, AND IT IS YOURS TO FALSIFY.** `1.0.0_SA_CTO` gave all four to ONE cell because they share
one call site, one harness and one mutant control (ruling R-OG-18, msg 97749, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_NFRA_OPLGTW_20260916.md` @d6466d7697). Its own words: **the
mutant must fail ALL FOUR live-path criteria, and if it fails fewer than four the premise is FALSE and THAT IS THE
FINDING, not an anomaly to work around.** A rule whose criterion survives removal of the shared site is not wired
to it. So AC5 is not a formality: it is the test of why this is one cell instead of four.

- Wire each rule from the query path's validation, the same site `OG-q-4` and `OG-q-5` already call into
  (`query.py`'s grant check, and `integration.py`'s `SchwabService.query()` only where a rule cannot be reached
  from `query.py` -- say which in your result file if you use it).
- A refusal uses the contract's existing `error_codes`, reveals no field the grant does not carry, and adds no new
  enum value, no new code and no widened limit.
- `semantics.py` and `datasets.json` are `OG-q-3`'s: **NOT yours.** A check you need that `semantics.py` does not
  export, or a field description `datasets.json` lacks, is a BLOCKING surprise row on that criterion -- never a
  local re-implementation, never an edit there. R25 may be UNREACHABLE for that reason; if so, refuse it with the
  measurement and keep going.

**Read:** the four census rows above; `app/integrations/schwab/query.py`; `app/integrations/schwab/integration.py`;
`app/integrations/schwab/semantics.py` (the four functions' signatures); the PRD's "C3"; the contract's
`error_codes`; `tests/acceptance/conftest.py` (`OG-v-2`'s live-app harness).

**The probe** for AC5 and AC6 is
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q6.py`, taking the short id,
printing its measurement with its denominator, then exactly one line `VERDICT: PASS-OGQ6-AC<n>` or
`VERDICT: FAIL-OGQ6-AC<n> <reason>`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGQ6-AC1" cell_refs="OG-q-6"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_c3_rules.py::test_ogq6_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ6-AC1` (`test_ogq6_ac01`) -- R20: through the registered `schwab_query` tool on `OG-v-2`'s live-app harness, an aggregate whose grouping drops master or business-date identity is REFUSED with a contract `error_codes` value, the code and the call site printed.

<criterion id="OGQ6-AC2" cell_refs="OG-q-6"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_c3_rules.py::test_ogq6_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ6-AC2` (`test_ogq6_ac02`) -- (difference) R22: through the same tool, a total built by summing TWO DIFFERENT balance fields is REFUSED, while a single named balance field's sum across the grant's approved accounts still SUCCEEDS in the same harness, both outcomes printed.

<criterion id="OGQ6-AC3" cell_refs="OG-q-6"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_c3_rules.py::test_ogq6_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ6-AC3` (`test_ogq6_ac03`) -- R24: through the same tool, a source whose grain is duplicated or conflicting returns UNAVAILABLE rather than a de-duplicated answer, and the returned row count is NOT silently reduced; the contract code and the row counts on both sides printed.

<criterion id="OGQ6-AC4" cell_refs="OG-q-6"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_c3_rules.py::test_ogq6_ac04 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ6-AC4` (`test_ogq6_ac04`) -- R25: through the registered `schwab_describe_dataset` tool on the same harness, every authorized field of one dataset carries grain, type, unit, SIGN and NULL semantics, with the field count printed as the denominator; a field missing sign or null semantics FAILS this criterion.

<criterion id="OGQ6-AC5" cell_refs="OG-q-6"><invocation>cd <WS> && timeout 600 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q6.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGQ6-AC5(?![0-9])</expect></criterion>
`OGQ6-AC5` -- (the ONE mutant control, and the one-cell premise's own test) with the SHARED call site removed in a scratch copy of `app/`, the probe runs AC1, AC2, AC3 and AC4 against that copy and passes only if ALL FOUR FAIL there; it prints each outcome, and **fewer than four failures FAILS this criterion and is reported as the finding that the four rules do not share one site** -- never worked around. It leaves no tracked file modified (`git status --porcelain` before and after, printed and equal).

<criterion id="OGQ6-AC6" cell_refs="OG-q-6"><invocation>cd <WS> && timeout 600 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q6.py AC6</invocation><expect>(?m)^VERDICT: PASS-OGQ6-AC6(?![0-9])</expect></criterion>
`OGQ6-AC6` -- (closing) the C3 census is RE-READ at this HEAD against the PRD's C3 at its then-current pin, **its sentence denominator and rule count RE-PRINTED at re-read time and NEVER inherited from the 29 measured at the earlier vintage** (R-OG-18's qualifier: 29 is a count of a document this project is actively amending), and its NOT-ENFORCED count reads 0; any rule newly appearing in C3 since the first census is enumerated in the re-read and, if NOT-ENFORCED, reported as a finding rather than silently dropped.

<expected_criteria>OGQ6-AC1, OGQ6-AC2, OGQ6-AC3, OGQ6-AC4, OGQ6-AC5, OGQ6-AC6</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **`integration.py` is granted for a call site ONLY**, and only where a rule cannot be reached from `query.py`. Name which rules used it in your result file. Change no other tool's behaviour.
- **`semantics.py`, `datasets.json`, `data_entitlement.py`, `tests/test_schwab_query.py` and `tests/acceptance/**` are NOT yours** -- other cells', merged or open. A needed change there is a BLOCKING row. In particular `test_ogv2_a18` (row `NFRA_OPLGTW-S26`) and `test_ogv2_a06`'s `isError` arm (row `NFRA_OPLGTW-W5-S18`) are OTHER cells' defects: do not touch them, and do not count them against your own criteria.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at hand-off. Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` serves every invocation; if absent, rebuild it as `cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`. Never commit `.venv-og/` or `.scratch/`.
- **One module per pytest process.** Two test modules in one process collide on the MCP session manager; that is a harness fact, not a defect to fix here.
- **R-40 binds any artifact you grade:** a criterion whose subject is a produced artifact records that artifact's CONTENT HASH beside its identity, so a later file at the same path fails rather than satisfies the label. Your census re-read is graded on ITS OWN re-measurement, not on the earlier file's numbers.
- **The known red test.** `tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1). Never edit it or `identity_tool_allowlist.txt`.
- **Limits are ceilings.** Never raise one to make a test pass.
- **Nothing deploys.** No apply, no host act, no image, no AWS write. The harness is moto and synthetic Parquet; no Schwab object is read.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No new monitor, alarm, SNS or notification path. No secret in evidence, and no customer value in any committed file.**
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh` (ruff, Python 3.9 syntax).
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W5-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/app/integrations/schwab/query.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py
infra/aws/ec2/opal-gateway/tests/test_schwab_c3_rules.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 as amended 2026-09-18, cell `OG-q-6`, round 1 (section 3, S6).
<owned_cells>OG-q-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGQ6-AC1` .. `OGQ6-AC6` (6). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/NFRA_OPLGTW.TO-OG-q-6.c3-rules-wiring.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @e09219470f, decomp_ref.doc the
decomposition as amended, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGQ6-AC1,OGQ6-AC2,OGQ6-AC3,OGQ6-AC4,OGQ6-AC5,OGQ6-AC6`
BEFORE the `complete` flip. Result file `c3-rules-wiring.result.md` beside it, naming each rule's call site by
`file:line` and carrying the census re-read's own printed denominator. **Flip `complete` only when every MECHANICAL
criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the cut 2026-09-18 ~01:5xZ -- --budget 600, 5 of 5 carriers scanned (C1 184, C2 6, C3 12, C4 21, C5 334), 25 gates armed, 0 lines naming NFRA_OPLGTW. Binding on this cell: the no-new-monitor moratorium and the nothing-deploys bound.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell calls existing in-process modules from an existing validation path; it adds no AWS operation, policy, principal or role, and its harness is moto.
comp-adversary: RUN at the cut on the PRD at HEAD (v0.9 @e09219470f) -- 4 of 4 cited commits VERIFIED; 7 cited paths, 5 stable, 2 flagged (one GONE: an external RFC URL parsed as a repo path); complement sources 5 run, 4 declared-excluded; pins are READ-VINTAGE only.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant); infra/aws/ec2/** admits a worker only by this order's <paths>.
</preflight>

Added mid-round on 2026-09-18 by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO` ruling R-OG-18 (msg 97749 @d6466d7697), with
decomposition cell `OG-q-6` added in the same commit, closing call 17 on rows `NFRA_OPLGTW-W5-S14`..`W5-S17`. ONE
cell for all four, as this seat recommended and the ruling adopted whole: they share one call site, one harness and
one mutant, and four cells would have bought four cuts, four spawns and four drains against one edit surface with no
extra discrimination. The ruling's ADDITION is AC5 -- the mutant must fail ALL FOUR, and fewer than four is the
FINDING that the premise is false, so the one-cell choice is falsifiable by the cell rather than inherited as an
assumption. Its qualifier is AC6's: the census re-read RE-PRINTS its denominator, because 29 is a count taken at one
vintage of a document this project keeps amending.

⚠ **TIMING, STATED RATHER THAN ASSUMED.** R-OG-18 says "cut it to ~5 after `OG-q-5` closes". `OG-q-5` is NOT closed:
its `OGQ5-AC6` is a measured FAIL whose two failures are OTHER cells' defects (`test_ogv2_a18` = row `S26`, and
`test_ogv2_a06`'s `isError` arm = row `W5-S18`, filed this hand-off). Waiting for it to close would serialise this
cell behind two repairs it does not depend on, while slot ~5's worker sits idle -- and the ruling's REASON for the
ordering was slot availability, which is satisfied. This seat therefore cut it now and says so here and to
`1.0.0_SA_CTO` in the same act, so the reading can be corrected rather than discovered.
