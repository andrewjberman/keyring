# TO NFRA_CTLPLN.TO-CT-v-1 -- round 7 CT-v-1: the pip counterpart of the bun no-egress kit -- find what stops a public package download on a Dell, with no request leaving the machine

<to_id>NFRA_CTLPLN.TO-CT-v-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~63</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-v-1` (`decompositions/NFRA_CTLPLN_DECOMP.round7.md`) | **outcome_ref:** FWD-18 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-18: a box that tries an internet download is stopped and told the route; only the laptop fetches. MEASURED on dell1 (row NFRA_CTLPLN-D1-S1):
`python -m pip download --no-deps -d <tmp> six==1.16.0 --index-url https://pypi.org/simple` returned rc=0 and saved the wheel. Nothing stopped it. The bun
case was solved by a tool that PROVES which disarm works on a given machine without sending a single request out, `org/devices/kit_bun_no_egress.py`
(741 lines; read its docstring and its structure first). You build the same for pip, for `python -m pip` (the form that was used; a PATH shim for `pip`
alone would not catch it).

### BUILD

`org/devices/kit_pip_no_egress.py` (Python 3.9 compatible, standard library only, ASCII only, ruff clean) and `org/devices/test_kit_pip_no_egress.py`.
Reuse the bun kit's shapes (the two loopback listeners that count requests, the order of proof, the fresh working directory outside every git tree, its own
HOME and cache) by copying the pattern, not by importing a private name. Two independent redirects to loopback for every pip process the tool starts: the
index set to `http://127.0.0.1:<port>/simple/` (answers 404, logs method and path) and HTTP_PROXY/HTTPS_PROXY (and lower-case) set to a second loopback
listener that logs every request line, CONNECT included, and answers 502, with NO_PROXY empty. The package every probe asks for is a name with a random
suffix, so even a leak retrieves nothing. NO REQUEST MAY LEAVE THIS MACHINE; the tool never names a public host except as a string it refuses.

Subcommands:
- `measure [--out <json>] [--tmp-base <dir>]`: in the order of proof run (1) a POSITIVE arm: plain `python -m pip download <random> --index-url http://127.0.0.1:<port>/simple/` MUST reach the counting listener (positive_requests >= 1); if it does not, the harness is broken and the tool reports `ok=False` and measures nothing else; (2) the CANDIDATE disarms, each its own arm, and a candidate passes only when the same command makes ZERO requests to either listener AND exits non-zero with an error that names it: (a) `PIP_NO_INDEX=1` in the environment; (b) a user-level pip config file with `no-index = true`; (c) a user-level config `index-url` pointed at a dead loopback port; (d) the wrapper form below. For each candidate also run the EXPLICIT-FLAG arm: the same command plus `--index-url http://127.0.0.1:<port>/simple/` after the disarm is applied, because the measured defect was exactly an explicit `--index-url`; record whether the disarm still held (`holds_against_explicit_index=True|False`).
- `wrap [--from <json>] -- <pip args>`: run `python -m pip <args>` with the passing form applied. The wrapper form (candidate d): REFUSE (exit 3, nothing run) any `install`, `download`, `wheel`, `index`, `search` verb that is not `--no-index`, and any argument `--index-url`, `-i`, `--extra-index-url`, `--find-links`/`-f` with an http(s) URL; the refusal message is exactly `REFUSED: this box does not download. Ask the laptop: org/devices/intake/ (request, check, Taildrop). No request was made.` Allowed unchanged: `list`, `show`, `freeze`, `check`, `--version`, `--help`, and `install --no-index --no-deps <local file>`.
- `selfcheck`: tests the two listeners with Python-made requests; starts NO pip process.
LAST line of measure: `PIP-NO-EGRESS pip=<version> positive_requests=<n> candidates=<k> passing=<p> holds_against_explicit=<h> leaked_public=<0|n> form=<form|NONE> ok=<True|False>`.
The tool records honestly if NO candidate holds against an explicit `--index-url` except the wrapper: say so in the last line (`form=wrapper-only`) and in the docstring. A wrapper is bypassed by a person who types a different interpreter, so the docstring states the limit in one sentence: the real control is a network egress policy, which is outside this cell.
`org/devices/test_kit_pip_no_egress.py`: pure tests of the wrapper's verb and flag classification (a table of at least 24 argument lists with the expected allow/refuse), the listeners' counting, and the refusal text. No pip process, no network.

### RULES FOR THIS CELL

Every pip process runs in the harness only. You never run `pip install`, `pip download` or any registry verb outside the harness, you never touch the machine's real pip config, environment variables or any site-packages, and you send nothing on the agent bus. No box name, user name or path under a user's home is typed into the files. No non-ASCII. Python 3.9 grammar. The law files CLAUDE.md and org/XXX.md are LOCKED.
FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W63-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTv1-AC1" cell_refs="CT-v-1"><invocation>python org/devices/test_kit_pip_no_egress.py</invocation><expect>KIT-PIP-TESTS ok=True</expect></criterion>
`CTv1-AC1` -- the pure tests pass; the last line of the test file's output is `KIT-PIP-TESTS ok=True cases=<k>/<n>`.

<criterion id="CTv1-AC2" cell_refs="CT-v-1"><invocation>python org/devices/kit_pip_no_egress.py measure</invocation><expect>PIP-NO-EGRESS</expect></criterion>
`CTv1-AC2` -- the measurement on this machine, once, whose last line carries `leaked_public=0`; the exit code is not graded (a box whose pip no candidate stops reports `form=NONE`, which is a finding, not a failure of the tool).
</proof_of_spec>

<expected_criteria>CTv1-AC1,CTv1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~63/NFRA_CTLPLN.TO-CT-v-1.pip-no-egress-kit.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTv1-AC1,CTv1-AC2`, and flip `<status>` to `complete` only when both criteria pass and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round7.md</decomp_doc>
<owned_cells>CT-v-1</owned_cells>
</decomp_ref>

<paths>
org/devices/kit_pip_no_egress.py
org/devices/test_kit_pip_no_egress.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a harness that cannot see a request (a positive arm must reach the listener first, or the tool reports ok=False); a leak to a public host (two redirects, a random package name, leaked_public counted); a disarm that holds against config but not against an explicit --index-url (the explicit arm measures it, which was the D1-S1 defect); a wrapper bypassed by another interpreter (stated in the docstring as the limit); BLIND: pip versions other than this machine's, and dell1's own pip until CT-v-3 runs the measurement there.
risk: WORLD is declared only because the L6 gate derives a floor from the `org/devices` paths this kit sits beside; this cell applies nothing and changes no machine.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round6.md` section 4 (E3) and row NFRA_CTLPLN-D1-S1; PRD `prd/NFRA_CTLPLN_PRD.md` v0.25 FWD-18.
