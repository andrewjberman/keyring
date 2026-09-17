# TO NFRA_OPLGTW.TO-OG-q-5 -- the dim_asset partial-account restriction on the live path, and a census of every C3 rule

<to_id>NFRA_OPLGTW.TO-OG-q-5</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~5</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-17</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.9 @e09219470f | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.1 | **Decomp cell:** `OG-q-5` | **outcome_ref:** FWD-2, FWD-5 | **depends_on:** `OG-q-2`, `OG-q-3` (merged), `OG-q-4` (its drain precedes this hand-off) | **precedes:** `OG-v-2`'s last re-hand | **slot:** ~5

---

## WORKER FACE

### THE CELL

`OG-q-5` -- **two halves, and the second is why this cell exists.**

**HALF ONE: the `dim_asset` partial-account restriction, wired on the live path.** PRD C3 states it:
*"The asset reference dataset carries only its approved security fields. For a partial-account grant restrict its
CUSIPs to holdings of the authorized accounts for that same master/date, using a qualified position snapshot solely
for policy selection. This internal policy filter is not a user-facing enrichment join. Its position objects count
toward the same object/byte/deadline limits; absent qualification denies the asset read."* `OG-v-2`'s integrated
harness measured that this is NOT enforced on the path a caller reaches (row `NFRA_OPLGTW-W6-S8`, ARMED, owner
`1.0.0_SA_CTO`; its `test_ogv2_a06` fails for this reason). Nothing is deployed, so nothing served is wrong today.

**HALF TWO: a CENSUS of every rule PRD C3 states, against its call path.** `1.0.0_SA_CTO` ruling R-OG-17
(msg 97682, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_NFRA_OPLGTW_20260916.md` @70570f36b9) adds it
in these words: **R-OG-13 (additivity), R-OG-15 (grouping) and W6-S8 are the SAME defect three times -- a criterion
written against a module in isolation and proven where nothing calls it -- and all three happened AFTER the
call-site bar, because nobody ever enumerated the POPULATION.** So this cell enumerates it. Finding a fourth one at
a time would be checking the members and never the set they share.

How the census is built, and the method is the point:
- The population is **every rule C3 states** -- the PRD's "C3 - sources, closure and date semantics" section at
  v0.9 @`e09219470f`, six paragraphs. Enumerate them **BY SUBTRACTION from the printed denominator of C3's own
  sentences**, never from a forward list of the rules you happen to remember (CLAUDE.md Rule 24(i)).
- For each rule, one row: its C3 sentence (quoted or line-cited), whether a query-path CALL SITE enforces it
  (`file:line`), and the verdict `ENFORCED-ON-CALL-PATH` / `NOT-ENFORCED` / `NOT-A-CALL-PATH-RULE` (a producer,
  catalog or closure rule this cell's path never reaches -- say which surface owns it instead).
- A verdict is **measured through the app**, not read off the PRD or off a module's own tests: for an
  `ENFORCED-ON-CALL-PATH` row, name the call site AND the exercise that reached it.
- The denominators printed: how many sentences C3 holds, how many are rules, and the three verdict counts summing
  to the rule count.
- **You do not fix what the census finds beyond half one.** Every `NOT-ENFORCED` row is a finding in your result
  file and ONE surprise row; the remedy is the issuer's to place.

**Read:** the PRD's "C3" (the population) and "C4"; `app/integrations/schwab/query.py` (the validation path and
`check_against_grant`, where `OG-q-4` wired the additivity and grouping checks -- the shape to follow);
`app/integrations/schwab/catalog.py` (the qualified position snapshot and the object/byte accounting);
`app/data_entitlement.py` (the grant's accounts and `check_scope`); `tests/acceptance/conftest.py` (`OG-v-2`'s
live-app harness and its partial-account fixtures) and `tests/acceptance/test_local_acceptance.py::test_ogv2_a06`
(the failing arm this half must turn green).

**The probe** for AC4 and AC5 is
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q5.py`, taking the short id,
printing its measurement with its denominator, then exactly one line `VERDICT: PASS-OGQ5-AC<n>` or
`VERDICT: FAIL-OGQ5-AC<n> <reason>`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGQ5-AC1" cell_refs="OG-q-5"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_asset_policy.py::test_ogq5_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ5-AC1` (`test_ogq5_ac01`) -- through the registered `schwab_query` tool on `OG-v-2`'s live-app harness, a partial-account grant reading `dim_asset` returns only the CUSIPs its authorized accounts hold on that master and date, with the returned CUSIP count and the authorized-account denominator printed, and the test names the call site it travelled.

<criterion id="OGQ5-AC2" cell_refs="OG-q-5"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_asset_policy.py::test_ogq5_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ5-AC2` (`test_ogq5_ac02`) -- (difference) in that same response, a CUSIP held ONLY by an account the grant does not carry is ABSENT, and the same CUSIP IS present for a grant that carries that account, both denominators printed.

<criterion id="OGQ5-AC3" cell_refs="OG-q-5"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_asset_policy.py::test_ogq5_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGQ5-AC3` (`test_ogq5_ac03`) -- absent a qualified position snapshot for that master and date, the `dim_asset` read is DENIED rather than served unfiltered, with the denial's contract `error_codes` value printed.

<criterion id="OGQ5-AC4" cell_refs="OG-q-5"><invocation>cd <WS> && timeout 420 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q5.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGQ5-AC4(?![0-9])</expect></criterion>
`OGQ5-AC4` -- (mutant control) with the restriction's call site removed in a scratch copy of `app/`, the probe runs AC1, AC2 and AC3 against that copy and passes only if AC1 and AC2 FAIL there; it prints all three outcomes and leaves no tracked file modified (`git status --porcelain` read before and after, printed and equal).

<criterion id="OGQ5-AC5" cell_refs="OG-q-5"><invocation>cd <WS> && timeout 420 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q5.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGQ5-AC5(?![0-9])</expect></criterion>
`OGQ5-AC5` -- the C3 census exists at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/C3_CALL_PATH_CENSUS.md`, built by subtraction from the printed denominator of C3's sentences at PRD v0.9 @e09219470f, one row per rule carrying its C3 citation, its call site or none, and one of the three verdicts; the probe re-reads that file and passes only if the sentence denominator, the rule count and the three verdict counts are all printed and the verdict counts sum to the rule count.

<criterion id="OGQ5-AC6" cell_refs="OG-q-5"><invocation>cd <WS> && timeout 600 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q5.py AC6</invocation><expect>(?m)^VERDICT: PASS-OGQ5-AC6(?![0-9])</expect></criterion>
`OGQ5-AC6` -- the probe runs `tests/test_schwab_query.py`, `tests/test_schwab_semantics.py`, `tests/test_schwab_wiring.py` and `tests/acceptance/test_local_acceptance.py`, ONE pytest process per module, and passes only if every module's failure count is 0, each module's counts and the denominator 4 printed.

<expected_criteria>OGQ5-AC1, OGQ5-AC2, OGQ5-AC3, OGQ5-AC4, OGQ5-AC5, OGQ5-AC6</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **The census FINDS; it does not FIX.** Half one is the only repair in this cell. Every other `NOT-ENFORCED` rule is a result-file finding plus ONE surprise row, and the issuer places the remedy. Widening this cell to fix a second rule is exactly the re-cut this project keeps paying for.
- **`semantics.py`, `datasets.json`, `data_entitlement.py` and `tests/test_schwab_query.py` are NOT yours** -- they are other cells', merged and closed. A needed change there is a BLOCKING row.
- **`tests/acceptance/` is `OG-v-2`'s** and `OG-v-2` is OPEN: read its harness and fixtures, never edit them. If `test_ogv2_a06` needs a fixture your half cannot reach, that is a BLOCKING row naming the fixture.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at hand-off. Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` serves every invocation; if absent, rebuild it as `cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`. Never commit `.venv-og/` or `.scratch/`.
- **One module per pytest process.** Two test modules in one process collide on the MCP session manager (`StreamableHTTPSessionManager .run() can only be called once per instance`); that is a harness fact, not a defect to fix here.
- **If a name moves, R-OG-16's three limbs bind** (msg 97657): a census of the old name's consumers with its denominator printed, the repoint of every live reader inside your `<paths>` or a carded BLOCKING row, and a re-run of any harness the census names. Nothing in this cell is expected to move a name.
- **The known red test.** `tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1). Never edit it or `identity_tool_allowlist.txt`.
- **Limits are ceilings.** Never raise one to make a test pass. The policy snapshot's objects and bytes count toward C3's limits, as C3 says.
- **Nothing deploys.** No apply, no host act, no image, no AWS write. The harness is moto and synthetic Parquet; no Schwab object is read.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No new monitor, alarm, SNS or notification path.**
- **No secret in evidence, and no customer value in any committed file** -- CUSIPs in this cell are the harness's synthetic fixtures, never a real holding.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh` (ruff, Python 3.9 syntax).
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W5-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/app/integrations/schwab/query.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/catalog.py
infra/aws/ec2/opal-gateway/tests/test_schwab_asset_policy.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 as amended 2026-09-17, cell `OG-q-5`, round 1 (section 3, S6).
<owned_cells>OG-q-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGQ5-AC1` .. `OGQ5-AC6` (6). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/NFRA_OPLGTW.TO-OG-q-5.asset-policy-and-c3-census.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @e09219470f, decomp_ref.doc the
decomposition as amended, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGQ5-AC1,OGQ5-AC2,OGQ5-AC3,OGQ5-AC4,OGQ5-AC5,OGQ5-AC6`
BEFORE the `complete` flip. Result file `asset-policy-and-c3-census.result.md` beside it, naming the call site by
`file:line` and carrying the census's summary counts. **Flip `complete` only when every MECHANICAL criterion PASSES
by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the cut 2026-09-17 ~22:5xZ -- --budget 600 (a 240 s budget EXHAUSTED at C1 partial and was re-run wider rather than recorded partial), 5 of 5 carriers scanned (C1 184, C2 6, C3 12, C4 21, C5 334), 25 gates armed, 0 lines naming NFRA_OPLGTW. Binding on this cell: the no-new-monitor moratorium and the nothing-deploys bound.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell calls existing in-process modules from an existing validation path; it adds no AWS operation, policy, principal or role, and its harness is moto.
comp-adversary: RUN at the cut on the PRD at HEAD (v0.9 @e09219470f) -- 4 of 4 cited commits VERIFIED; 7 cited paths, 5 stable, 2 flagged (one GONE: an external RFC URL parsed as a repo path); complement sources 5 run, 4 declared-excluded; pins are READ-VINTAGE only.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant); infra/aws/ec2/** admits a worker only by this order's <paths>.
</preflight>

Added mid-round on 2026-09-17 by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO` ruling R-OG-17 (msg 97682 @70570f36b9), with
decomposition cell `OG-q-5` added in the same commit, on row `NFRA_OPLGTW-W6-S8` (ARMED, owner `1.0.0_SA_CTO`,
disarming on this cell's DRAIN and not on its cut). Slot ~5, handed after `OG-q-4` drains. The census half is the
ruling's own addition and its reason is stated in the cell text: three cells in a row -- `OG-q-3`'s additivity,
`OG-q-2`'s two defect-asserting tests and this `dim_asset` rule -- were the same defect, and the call-site bar alone
did not stop it because the POPULATION was never enumerated. `OG-v-2` takes its last re-hand after this cell drains,
to re-grade its AC2 whole; re-grading it earlier would fail on `test_ogv2_a06` alone and cost a hand-off for nothing.
