# TO NFRA_OPLGTW.TO-OG-q-4 -- the semantics checks wired into the live query path

<to_id>NFRA_OPLGTW.TO-OG-q-4</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~5</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-17</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.9 @e09219470f | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.1 | **Decomp cell:** `OG-q-4` | **outcome_ref:** FWD-2, FWD-5 | **depends_on:** `OG-q-2`, `OG-q-3` (both merged) | **precedes:** `OG-v-2`'s re-hand | **slot:** ~5

---

## WORKER FACE

### THE CELL

`OG-q-4` -- **wire `semantics.py`'s additivity and grouping checks into the live query path.** `OG-q-3` built
`app/integrations/schwab/semantics.py` and proved it in isolation. Nothing calls it: `assert_sum_allowed` is defined at
`semantics.py:273` and referenced nowhere outside `tests/test_schwab_semantics.py`, and no module under `app/` imports
`semantics`. So the contract's own rules -- a nonadditive field is not summed, a quantity sum is grouped by `cusip` and
`l_s` -- are NOT enforced on the path a caller reaches. `OG-v-2`'s integrated harness measured it against the real app
and refused its own AC2 (row `NFRA_OPLGTW-W6-S6`, ARMED). Nothing is deployed, so nothing served is wrong today.

`1.0.0_SA_CTO` ruling R-OG-13 (msg 97629, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_NFRA_OPLGTW_20260916.md` @9798d9dda5) cut this cell, with its
STANDING BAR: **a criterion whose subject is a check, a guard or a refusal names the CALL SITE it runs through, is
graded on the live path, and carries a mutant control that removes that call site.** Every criterion below is written
that way.

What this cell does, and nothing else:
- Call the checks `semantics.py` already exports from the request-validation path in
  `app/integrations/schwab/query.py`, at the point where an aggregate's function, field and grouping are known and
  before any object is read. `app/integrations/schwab/integration.py` is granted for the wiring it needs, no more.
- A refusal uses the contract's existing `error_codes` and reveals no field the grant does not carry. Never a new
  error code, never a new enum value, never a widened limit.
- `semantics.py` and `datasets.json` are `OG-q-3`'s and are NOT edited. A check you need that `semantics.py` does not
  export is a BLOCKING surprise row on that criterion, never a local re-implementation and never an edit there.
- No cache, cursor, envelope, audit or engine behaviour changes. Nothing deploys.

**The two defect-asserting tests (amended on re-hand, on `1.0.0_SA_CTO` ruling R-OG-15, msg 97648, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_NFRA_OPLGTW_20260916.md` @f3309bc39d; row
`NFRA_OPLGTW-W5-S10`).** Your first hand-off wired the checks and its mutant fired as designed, but AC5 refused:
`tests/test_schwab_query.py::test_ogq2_ac07` and `::test_ogq2_ac15` ASSERT that an ungrouped quantity sum is
accepted -- the shape the contract forbids and your AC2 now refuses. Those two tests are yours for exactly this:
- Flip each of the two to expect the contract's refusal. NO OTHER LINE of that file is touched, and no other test's
  expectation changes.
- Each flipped assertion cites, in a comment on the assertion, the contract clause it now encodes.
- This is NOT a re-open of `OG-q-2`: its cell is closed and its other 27 criteria stand. AC6 and AC7 grade the
  correction; AC5 then reads the module green.

**Read:** `app/integrations/schwab/semantics.py` (its exported checks and their signatures);
`app/integrations/schwab/query.py` (the validation path); `app/integrations/schwab/integration.py` (the tool
registration and `export_query`); `org/standards/NFRA_OPLGTW_CONTRACT.json` (`error_codes`, `aggregate_operators`,
`fields`); the PRD's "C4"; `tests/acceptance/conftest.py` (`OG-v-2`'s harness -- the live-path fixture your tests use);
`tests/test_schwab_semantics.py` (how the checks are exercised in isolation, for contrast).

**The probe** for AC4 is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q4.py`,
taking the short id, printing its measurement with its denominator, then exactly one line
`VERDICT: PASS-OGQ4-AC<n>` or `VERDICT: FAIL-OGQ4-AC<n> <reason>`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGQ4-AC1" cell_refs="OG-q-4"><invocation>cd <WS> && timeout 180 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_wiring.py::test_ogq4_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ4-AC1` (`test_ogq4_ac01`) -- through the registered `schwab_query` tool on `OG-v-2`'s live-app harness, an aggregate summing a nonadditive field is refused with a contract `error_codes` value, and the test prints the refusal's code and the call site it travelled (`query.py`'s call into `semantics.py`).

<criterion id="OGQ4-AC2" cell_refs="OG-q-4"><invocation>cd <WS> && timeout 180 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_wiring.py::test_ogq4_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ4-AC2` (`test_ogq4_ac02`) -- through the same tool and harness, a quantity sum whose grouping omits `cusip` or `l_s` is refused with a contract `error_codes` value, and the test prints the refusal's code.

<criterion id="OGQ4-AC3" cell_refs="OG-q-4"><invocation>cd <WS> && timeout 180 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_wiring.py::test_ogq4_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ4-AC3` (`test_ogq4_ac03`) -- through the same tool and harness, a legal sum of one named balance field across the grant's approved accounts still succeeds and returns its total in the envelope.

<criterion id="OGQ4-AC4" cell_refs="OG-q-4"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q4.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGQ4-AC4(?![0-9])</expect></criterion>
`OGQ4-AC4` -- (mutant control) the probe copies the worktree's `app/` to a scratch directory, removes the call site there only, runs AC1, AC2 and AC3 against that copy, and passes only if AC1 and AC2 FAIL while AC3 still passes; it prints the three outcomes, and it never edits a tracked file (a `git status --porcelain` read before and after is printed and equal).

<criterion id="OGQ4-AC5" cell_refs="OG-q-4"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q4.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGQ4-AC5(?![0-9])</expect></criterion>
`OGQ4-AC5` -- the probe runs `tests/test_schwab_query.py`, `tests/test_schwab_semantics.py` and `tests/test_schwab_export.py`, ONE pytest process per module, and every module passes, each module's pass count and the denominator 3 printed.

<criterion id="OGQ4-AC6" cell_refs="OG-q-4"><invocation>cd <WS> && timeout 180 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q4.py AC6</invocation><expect>(?m)^VERDICT: PASS-OGQ4-AC6(?![0-9])</expect></criterion>
`OGQ4-AC6` -- the probe prints the diff of `tests/test_schwab_query.py` against your cut base with its LINE COUNT, and passes only if every changed line lies inside `test_ogq2_ac07` or `test_ogq2_ac15`.

<criterion id="OGQ4-AC7" cell_refs="OG-q-4"><invocation>cd <WS> && timeout 180 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q4.py AC7</invocation><expect>(?m)^VERDICT: PASS-OGQ4-AC7(?![0-9])</expect></criterion>
`OGQ4-AC7` -- the probe prints `tests/test_schwab_query.py`'s collected test count before and after the correction, both denominators stated (25 at the cut base, 25 after: 23 untouched plus the 2 corrected), and passes only if the two corrected tests each carry a comment citing the contract clause their new expectation encodes.

<expected_criteria>OGQ4-AC1, OGQ4-AC2, OGQ4-AC3, OGQ4-AC4, OGQ4-AC5, OGQ4-AC6, OGQ4-AC7</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **`semantics.py` and `datasets.json` are not yours.** They are `OG-q-3`'s, merged and closed. A missing export is a BLOCKING row.
- **`tests/test_schwab_query.py` is yours for EXACTLY `test_ogq2_ac07` and `test_ogq2_ac15`.** Any other line in that file is outside your grant and is a BLOCKING row, never an edit.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at hand-off. Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` serves every invocation; if absent, rebuild it as `cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`. Never commit `.venv-og/` or `.scratch/`.
- **One module per pytest process.** Two test modules in one process collide on the MCP session manager (`StreamableHTTPSessionManager .run() can only be called once per instance`); that is a harness fact, not a defect to fix here.
- **The known red test.** `tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1). Never edit it or `identity_tool_allowlist.txt`.
- **Limits are ceilings.** Never raise one to make a test pass.
- **Nothing deploys.** No apply, no host act, no image, no AWS write of any kind. The harness is moto and synthetic Parquet; no Schwab object is read.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No new monitor, alarm, SNS or notification path.**
- **No secret in evidence, and no customer value in any committed file.**
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`. The gate lints with ruff for Python 3.9 syntax.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W5-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/app/integrations/schwab/query.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py
infra/aws/ec2/opal-gateway/tests/test_schwab_wiring.py
infra/aws/ec2/opal-gateway/tests/test_schwab_query.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 as amended 2026-09-17, cell `OG-q-4`, round 1 (section 3, S6).
<owned_cells>OG-q-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGQ4-AC1` .. `OGQ4-AC7` (7). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/NFRA_OPLGTW.TO-OG-q-4.semantics-wiring.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @e09219470f, decomp_ref.doc the
decomposition as amended, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGQ4-AC1,OGQ4-AC2,OGQ4-AC3,OGQ4-AC4,OGQ4-AC5,OGQ4-AC6,OGQ4-AC7`
BEFORE the `complete` flip. Result file `semantics-wiring.result.md` beside it, naming the call site by
`file:line`. **Flip `complete` only when every MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the cut 2026-09-17 ~18:5xZ -- --budget 240, 5 of 5 carriers scanned (C1 184, C2 6, C3 12, C4 21, C5 334), 25 gates armed, 0 lines naming NFRA_OPLGTW. Binding on this cell: the no-new-monitor moratorium and the nothing-deploys bound.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell calls an existing in-process module from an existing validation path; it adds no AWS operation, policy, principal or role, and its harness is moto.
comp-adversary: RUN at the cut on the PRD at HEAD (v0.9 @e09219470f) -- 4 of 4 cited commits VERIFIED; 7 cited paths, 5 stable, 1 GONE (an external RFC URL parsed as a repo path); complement sources 5 run, 4 declared-excluded; pins are READ-VINTAGE only.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant); infra/aws/ec2/** admits a worker only by this order's <paths>.
</preflight>

Added mid-round on 2026-09-17 by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO` ruling R-OG-13 (msg 97629 @9798d9dda5), with
decomposition cell `OG-q-4` added in the same commit, closing call 13 on row `NFRA_OPLGTW-W6-S6`. Slot ~5, whose queue
was empty. `OG-q-2` and `OG-q-3` are NOT re-opened: the ruling placed the defect in the CUT, not the work, and this
seat authored that cut. `OG-v-2` is re-handed after this order drains, to build its 7 unbuilt machine A-rows (row
`NFRA_OPLGTW-W6-S7`) and re-grade its AC2 whole. W6-S6 stays ARMED, owner `1.0.0_SA_CTO`, until this drain lands with
AC4's mutant failing as designed; that drain's proof instance is the disarm evidence.

Amended 2026-09-17 ~19:4xZ, before the re-hand, by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO` ruling R-OG-15 (msg 97648
@f3309bc39d, closing call 15 on row `NFRA_OPLGTW-W5-S10`). The first hand-off passed AC1-AC4 with the mutant firing
and refused AC5 on two `OG-q-2` tests that assert the defect. `tests/test_schwab_query.py` is granted for exactly
those two tests; AC6 and AC7 grade the correction's tightness (changed lines inside the two functions only; the test
count and the contract citation). The drain was HELD at branch tip 881b1a5445 rather than land two knowingly red
tests on CLOUD, and the ruling affirmed the hold. `3.0.0_SA_CVO` grades OGQ2-AC7's and OGQ2-AC15's original passes
UNSOUND AT THEIR VINTAGE at round close, which is a record act, not a re-open. No criterion removed.
