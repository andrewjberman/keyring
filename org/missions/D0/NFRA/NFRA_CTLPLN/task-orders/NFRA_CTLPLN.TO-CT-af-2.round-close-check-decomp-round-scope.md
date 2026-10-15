# TO NFRA_CTLPLN.TO-CT-af-2 -- workstream ROUNDCLOSE round 1 (cell CT-af-2): round-close-check scopes an order to the round its decomposition names, not to its workstream-round tag (CTO round-15 ruling 4)

<to_id>NFRA_CTLPLN.TO-CT-af-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~101</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>ROUNDCLOSE</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-af-2` (`decompositions/NFRA_CTLPLN_DECOMP.round16.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`.tools/round-close-check.py --project <CODE> --round <n>` is the gate that says whether a round may be counted finished. It selects the orders of round `n` in `read_orders` (about :307-349) by comparing the order's `<round>` tag with `n` (about :336). In this project an order's `<round>` tag holds its WORKSTREAM's round (for example `<round>3</round>` on `NFRA_CTLPLN.TO-CT-ae-3`), while `--round` is the ISSUANCE round (15). So `--round 15` counts no `CT-ae` order at all: it read MAY-CLOSE over 31 older seat-folder orders and none of the three orders of the round. The CTO's ruling: the check reads the issuance round from the decomposition. Each order names its decomposition in `<decomp_ref><decomp_doc>...NFRA_CTLPLN_DECOMP.round<N>.md</decomp_doc>`.

### BUILD

1. In `read_orders`, derive each order's SCOPING ROUND: if the order's text carries a `<decomp_doc>` whose file name matches `\.round(\d+)\.md`, that number is the scoping round; otherwise (no `<decomp_ref>`, or a decomposition file name without `roundN`) the scoping round is the `<round>` tag exactly as today. Compare the scoping round with `--round`. Keep the existing seat-folder rule (an untagged flat-folder order is counted in every round and named as untagged), the `--workstream` filter, the one-order-per-id rule and the tree-wins rule unchanged.
2. Print one new line in the check output, after the `ORDERS scope ...` line: `  TREE orders counted by decomposition round: <k> (<ids>)`, listing the tree orders whose scoping round came from their decomposition (k may be 0; then print `0 ()`).
3. A NEW test `.tools/tests/test_round_close_decomp_round.py` (standard library, temporary directories only, no AWS; build a fixture the way the self-test in `round-close-check.py` does, reading it for the harness). Arms: (a) an order tagged `<round>3</round>` whose `<decomp_doc>` names `...round15.md` is counted by `--round 15` and NOT by `--round 3`; (b) an order with no `<decomp_ref>` and `<round>3</round>` is still counted by `--round 3` (fallback); (c) an order whose decomp file name has no `roundN` falls back to its tag; (d) a seat-folder order with no tag is still counted in every round and named untagged; (e) two tree orders of different decomposition rounds, each counted only in its own round; (f) the new line prints `0 ()` for a round with no decomposition-scoped order. Final line `ROUND-CLOSE-DECOMP-ROUND arms=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. Read-only on every project file other than the two named tools. No aws, no network, no push. `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink. ASCII only; Python 3.12. CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~99/NFRA_CTLPLN.TO-CT-ae-3.batch-repair-round14-rows.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W101-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTaf2-AC1" cell_refs="CT-af-2"><invocation>python .tools/tests/test_round_close_decomp_round.py</invocation><expect>ok=True</expect></criterion>
`CTaf2-AC1` -- every arm passes (base: the file does not exist); report the whole last line with its denominator.

<criterion id="CTaf2-AC2" cell_refs="CT-af-2"><invocation>python .tools/round-close-check.py --selftest</invocation><expect>ok=True</expect></criterion>
`CTaf2-AC2` -- the tool's own self-test still passes (base: `ROUND-CLOSE-SELFTEST cases=30/30 ok=True`, a control); report the whole last line.

<criterion id="CTaf2-AC3" cell_refs="CT-af-2"><invocation>python .tools/round-close-check.py --project NFRA_CTLPLN --round 15</invocation><expect>TREE orders counted by decomposition round: 3</expect></criterion>
`CTaf2-AC3` -- on the real project the three round-15 orders are counted (base: FAIL as expected, the line does not exist and the check reads no `CT-ae` order); report the new line and the `ROUND-CLOSE` verdict line.
</proof_of_spec>

<expected_criteria>CTaf2-AC1,CTaf2-AC2,CTaf2-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 240`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~101/NFRA_CTLPLN.TO-CT-af-2.round-close-check-decomp-round-scope.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTaf2-AC1,CTaf2-AC2,CTaf2-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round16.md</decomp_doc>
<owned_cells>CT-af-2</owned_cells>
</decomp_ref>

<paths>
.tools/round-close-check.py
.tools/tests/test_round_close_decomp_round.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- an order moved out of the round it belongs to by the new rule (arms a, b, c, e); the untagged seat-folder rule weakened (arm d); a round that reads MAY-CLOSE because its orders were dropped (the real-project criterion counts the three orders); BLIND: a decomposition file name with a round number that is not the issuance round (for example `DECOMP.round1.md` beside a tag of 7), which the rule would re-scope silently (the worker reports how many existing project orders change round under the new rule, by running the check over the earlier rounds and comparing).
risk: LOCAL -- read-only tool and a temporary-directory test.
lane: the <paths> block IS the grant (worker RULING 1). `.tools/round-close-check.py` is on every COO's drain path.
</preflight>

Base checks, dry-run by the issuer before the cut: CTaf2-AC1 base: FAIL as expected (the file does not exist); CTaf2-AC2 base: `ROUND-CLOSE-SELFTEST cases=30/30 ok=True` (a control); CTaf2-AC3 base: FAIL as expected (the check prints no TREE line; `--round 15` read 31 seat-folder orders and no CT-ae order).
Source: CTO round-15 analysis ruling 4 and section 4 item 2 (`ledger/ROUND_ANALYSIS.round15.md` @0be7eb664c); the CVO's instrument note in `ADJUDICATION_v20.md`.
