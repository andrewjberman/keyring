# TO NFRA_OPLGTW.TO-OG-z-4 -- a refused call is flagged as an error to the CONSUMER, not only in its body

<to_id>NFRA_OPLGTW.TO-OG-z-4</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~6</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.9 @e09219470f | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.1 | **Decomp cell:** `OG-z-4` | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** `OG-z-1` (the guard), `OG-q-5` (whose fix unmasked this) | **precedes:** `OG-v-2`'s last re-hand | **slot:** ~6

---

## WORKER FACE

### THE CELL

`OG-z-4` -- **the guard's denial is correct in its BODY and says SUCCESS in its ENVELOPE. Fix the envelope.**

`app/tools.py:70-75`, `_PolicyGuardedMCP.call_tool()`:

```
denial = await anyio.to_thread.run_sync(functools.partial(data_entitlement.tool_denial, name, principal))
if denial:
    audit.log_call(get_current_email(), name, {}, "denied", denial["error"])
    return denial
```

That `return denial` hands `data_entitlement.py`'s raw denial dict back as an ORDINARY tool result. The MCP error
flag is never set, so a client reading the protocol's own success/failure signal is told the call SUCCEEDED and
must parse prose to learn it was refused. **The class's own docstring (`:56-61`) says a denied call returns "a
terminal tool error" -- the code does not make that true.** Two carriers of one claim disagreeing, and the code is
the one that ships.

`1.0.0_SA_CTO` ruling R-OG-20 (msg 97775, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_NFRA_OPLGTW_20260916.md` @bb15319584) cut this cell on row
`NFRA_OPLGTW-W5-S18`, and stated the bar this cell exists to satisfy: **a criterion about a REFUSAL grades the
signal the CONSUMER reads, never only the text the producer wrote.** A refusal a consumer cannot detect is not a
refusal; it is a success carrying disappointing text. This survived because every test read the BODY -- and it was
found only when `OG-q-5`'s fix removed an assertion that had been failing ahead of it.

What this cell does, and nothing else:
- Make a guard-denied call return the MCP error flag TRUE while keeping the denial's existing structured body and
  its contract `error_codes` value unchanged. No new error code, no new enum value, no change to WHICH calls are
  denied -- `data_entitlement.py`'s decision is not this cell's and is not edited.
- Keep the audit line exactly as it is (`audit.log_call(..., "denied", ...)`): `OG-o-1` owns the audit shape.
- Reconcile the docstring with the code in the same commit: either the code makes "a terminal tool error" true, or
  the docstring says what the code does. Do not leave the pair disagreeing.
- Change no other tool's behaviour, and do not touch `list_tools()`'s discovery filtering.

**Read:** `app/tools.py` (`_PolicyGuardedMCP`, both methods); `app/data_entitlement.py`'s `tool_denial()` and the
denial dict it builds; the contract's `error_codes`; `tests/acceptance/conftest.py` and
`tests/acceptance/test_local_acceptance.py::test_ogv2_a06` (the arm at `:488` that measured this -- read it, do
not edit it); the MCP library's own result type for how the flag is set (`mcp==1.28.0`, not raised).

**The probe** for AC3 is
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_z4.py`, taking the short id,
printing its measurement with its denominator, then exactly one line `VERDICT: PASS-OGZ4-AC<n>` or
`VERDICT: FAIL-OGZ4-AC<n> <reason>`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGZ4-AC1" cell_refs="OG-z-4"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_denial_envelope.py::test_ogz4_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ4-AC1` (`test_ogz4_ac01`) -- through the real app on `OG-v-2`'s live-app harness, a guard-denied tool call returns the MCP error flag TRUE **as the protocol result a consumer reads**, and its body still carries the same contract `error_codes` value it carries today; the test prints the flag and the code.

<criterion id="OGZ4-AC2" cell_refs="OG-z-4"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_denial_envelope.py::test_ogz4_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ4-AC2` (`test_ogz4_ac02`) -- (difference) in the same harness, a PERMITTED call returns the MCP error flag FALSE, so the flag discriminates and is not set unconditionally; both flags printed side by side.

<criterion id="OGZ4-AC3" cell_refs="OG-z-4"><invocation>cd <WS> && timeout 420 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_z4.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGZ4-AC3(?![0-9])</expect></criterion>
`OGZ4-AC3` -- (mutant control) with the flag-setting line removed in a scratch copy of `app/`, the probe runs AC1 and AC2 against that copy and passes only if AC1 FAILS while AC2 still passes; it prints both outcomes and leaves no tracked file modified (`git status --porcelain` before and after, printed and equal).

<criterion id="OGZ4-AC4" cell_refs="OG-z-4"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_data_entitlement_guard.py -q -p no:cacheprovider --color=no -m "not live"</invocation><expect>(?m)^[1-9][0-9]* passed(?![^\n]*(failed|error))</expect></criterion>
`OGZ4-AC4` -- `OG-z-1`'s own guard module still passes unchanged: every denial decision this cell did not touch behaves as before, the pass count printed.

<criterion id="OGZ4-AC5" cell_refs="OG-z-4"><invocation>cd <WS> && timeout 420 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_z4.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGZ4-AC5(?![0-9])</expect></criterion>
`OGZ4-AC5` -- the docstring and the code AGREE: the probe prints `_PolicyGuardedMCP`'s docstring lines about the denial and the lines that build the returned result, and passes only if the docstring's claim is true of the code as written at this HEAD (either the code sets the error flag, or the docstring no longer claims a terminal tool error).

<expected_criteria>OGZ4-AC1, OGZ4-AC2, OGZ4-AC3, OGZ4-AC4, OGZ4-AC5</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **`data_entitlement.py` is NOT yours** (`OG-z-1`'s, merged): WHICH calls are denied does not change in this cell, only how the denial is signalled. A needed change there is a BLOCKING row.
- **`tests/acceptance/**` is `OG-v-2`'s and that order is OPEN:** read `test_ogv2_a06` and the harness, never edit them. `test_ogv2_a18` (row `S26`) is another cell's defect -- do not touch it and do not count it against your criteria.
- **The audit line stays as written** -- `OG-o-1` owns the audit shape.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at hand-off. Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` serves every invocation; if absent, rebuild it as `cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`. Never commit `.venv-og/` or `.scratch/`.
- **One module per pytest process.** Two test modules in one process collide on the MCP session manager; a harness fact, not a defect to fix here.
- **`mcp==1.28.0` is not raised**, and no dependency is added.
- **The known red test.** `tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1). Never edit it or `identity_tool_allowlist.txt`.
- **Nothing deploys.** No apply, no host act, no image, no AWS write. The harness is moto; no Schwab object is read.
- **No egress off Opal infrastructure. No new monitor, alarm, SNS or notification path. No secret in evidence.**
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh` (ruff, Python 3.9 syntax).
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W6-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/tests/test_schwab_denial_envelope.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 as amended 2026-09-18, cell `OG-z-4`, round 1 (section 3, S2).
<owned_cells>OG-z-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGZ4-AC1` .. `OGZ4-AC5` (5). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/NFRA_OPLGTW.TO-OG-z-4.denial-envelope.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @e09219470f, decomp_ref.doc the
decomposition as amended, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGZ4-AC1,OGZ4-AC2,OGZ4-AC3,OGZ4-AC4,OGZ4-AC5`
BEFORE the `complete` flip. Result file `denial-envelope.result.md` beside it, naming the changed line by
`file:line` and quoting the docstring as it reads after the change. **Flip `complete` only when every MECHANICAL
criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN 2026-09-18 ~01:5xZ, ~15 minutes before this cut and in the same session with no intervening estate change of its carriers -- --budget 600, 5 of 5 carriers scanned (C1 184, C2 6, C3 12, C4 21, C5 334), 25 gates armed, 0 lines naming NFRA_OPLGTW. The interval is stated rather than the run being claimed as simultaneous with the cut. Binding on this cell: the no-new-monitor moratorium and the nothing-deploys bound.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell changes how an in-process denial is signalled; it adds no AWS operation, policy, principal or role, and its harness is moto.
comp-adversary: RUN 2026-09-18 ~01:5xZ on the PRD at HEAD (v0.9 @e09219470f), same interval caveat -- 4 of 4 cited commits VERIFIED; 7 cited paths, 5 stable, 2 flagged (one GONE: an external RFC URL parsed as a repo path); complement sources 5 run, 4 declared-excluded; pins are READ-VINTAGE only.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant); infra/aws/ec2/** admits a worker only by this order's <paths>.
</preflight>

Added mid-round on 2026-09-18 by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO` ruling R-OG-20 (msg 97775 @bb15319584),
closing call 18 on row `NFRA_OPLGTW-W5-S18` (ARMED, owner `1.0.0_SA_CTO`, disarming on this cell's DRAIN). Slot ~6,
which was idle: `OG-v-2` takes its last re-hand ONCE after BOTH this cell and `OG-q-6` land, so its AC2 is graded
whole instead of failing twice on other cells' rows.

NOT FOLDED INTO `OG-q-6`, and the reason is the ruling's own: `tools.py` is a DIFFERENT CALL SITE from the query
path, and folding it in would break exactly the one-cell premise `OGQ6-AC5`'s mutant exists to test. The ruling
adopted that reasoning without amendment.

R-OG-20's bar is this cell's whole point and is written into the criteria rather than the prose: **a criterion
about a REFUSAL grades the signal the CONSUMER reads.** Three instances of that class landed this week -- a
renderer graded by comparing its output to ITSELF (`W4-S19`), `OGQ2-AC7`/`AC15` asserting the forbidden shape was
accepted, and this row -- each asserting something TRUE about the wrong surface while the property a consumer
depends on went unasserted.
