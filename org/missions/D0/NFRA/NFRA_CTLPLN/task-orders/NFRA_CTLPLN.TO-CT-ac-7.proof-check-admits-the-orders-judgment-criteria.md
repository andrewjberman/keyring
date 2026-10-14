# TO NFRA_CTLPLN.TO-CT-ac-7 -- workstream SEATS round 4 (cell CT-ac-7): `proof-of-spec-check.py` admits the governing order's `judgment="true"` criteria as expected, so it and `round-close-check.py` agree (row D2-S5, from dell2)

<to_id>NFRA_CTLPLN.TO-CT-ac-7</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~91</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run: PROOF-JUDGMENT-EXPECTED cases=4/4 ok=True and proof-of-spec-check --self-test RESULT: 63 of 63 arm(s) behaved (base 59); proof instance VALID on the committed state. Rows W91-S1 (the order's crits-map premise was wrong; judgment read via the round-close-check rule) and W91-S2 (coverage-frame line prints as VIOLATION:, pre-existing, verdict unaffected) accepted as INERT observations.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>SEATS</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ac-7` (`decompositions/NFRA_CTLPLN_DECOMP.round13.md`, Recut 3) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Read row `NFRA_CTLPLN-D2-S5` (search the id with the Grep tool in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`; filed by 1.0.0_SA_CTO~DELL2, recurring on IRPT_DASHBD rounds 101-107). Two checkers disagree. `.tools/round-close-check.py` (header, cell CT-s-8, and its line ~24) requires a row in the proof instance for EVERY `judgment="true"` criterion of a round's orders. `.tools/proof-of-spec-check.py` `coverage_check(inst, expected_arg)` (about :550) compares the instance's acceptance rows with an EXPECTED set that its caller passes as the second argument (the order's `<expected_criteria>`), and REFUSES any instance row outside that set (`unexpected addition`). When an order's `<expected_criteria>` omits its own judgment criterion (IRPT_DASHBD's orders do), a seat must break one checker: keep the judgment row and proof-of-spec-check returns INVALID (rc 1); move it to `declared_exclusions` and round-close-check reads REFUSED. MEASURED at your base: `python .tools/proof-of-spec-check.py --self-test` prints `RESULT: 59 of 59 arm(s) behaved`. The checker already has a binding option: `--governing-order <path>` sets `_BOUND_ORDER` (about :2545-2550) and reads that order's criteria (the `crits` map built about :930-940, with each criterion's `judgment` attribute).

### BUILD

1. In `.tools/proof-of-spec-check.py`, when a governing order is bound, the expected set used by `coverage_check` also contains the id of every `judgment="true"` criterion of that order. An instance row for such a criterion is then NOT an unexpected addition, and its ABSENCE is a `silent omission` violation exactly as for any expected id (round-close-check needs that row). With NO bound order, behave exactly as today. A row for a criterion that is neither expected nor a judgment criterion of the bound order is still an unexpected addition. Print one `NOTE:` line naming the judgment ids it added.
2. Add self-test arms to the checker's own `--self-test` (follow the pattern of the existing arms; they build their own temporary orders and instances): (a) an order with `AC1` (mechanical) and `J1` (`judgment="true"`), `<expected_criteria>AC1</expected_criteria>`, bound with `--governing-order`: an instance carrying AC1 and J1 (J1 `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO) -> 0 violations; (b) the same without J1 -> a `silent omission` violation naming J1; (c) the same instance with NO bound order -> the old `unexpected addition` for J1 (unchanged behaviour); (d) a row `X9` that is neither -> still an unexpected addition. Keep every existing arm.
3. A NEW test file `.tools/tests/test_proof_judgment_expected.py` (standard library, temporary directories only, runs the checker as a subprocess) with the same four cases end to end through the command line, printing `PROOF-JUDGMENT-EXPECTED cases=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. No aws, no network, no push. `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink. ASCII only; Python 3.11. CLAUDE.md and org/XXX.md are LOCKED. Do not edit `round-close-check.py` (outside your paths; it is the side that is right). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it (`git log --oneline -1 -- <path>`), never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W91-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTac7-AC1" cell_refs="CT-ac-7"><invocation>python .tools/tests/test_proof_judgment_expected.py</invocation><expect>ok=True</expect></criterion>
`CTac7-AC1` -- the four end-to-end cases pass (base: the file does not exist); report the whole last line with its denominator.

<criterion id="CTac7-AC2" cell_refs="CT-ac-7"><invocation>python .tools/proof-of-spec-check.py --self-test</invocation><expect>arm(s) behaved</expect></criterion>
`CTac7-AC2` -- the checker's own self-test passes with the new arms (base: `RESULT: 59 of 59 arm(s) behaved`; report the whole last line, now more than 59).
</proof_of_spec>

<expected_criteria>CTac7-AC1,CTac7-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~91/NFRA_CTLPLN.TO-CT-ac-7.proof-check-admits-the-orders-judgment-criteria.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTac7-AC1,CTac7-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round13.md</decomp_doc>
<owned_cells>CT-ac-7</owned_cells>
</decomp_ref>

<paths>
.tools/proof-of-spec-check.py
.tools/tests/test_proof_judgment_expected.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- a judgment row admitted when NO order is bound (case c keeps the old refusal); a judgment criterion silently absent from the instance (case b); a non-judgment extra row let through by the widening (case d); the existing 59 arms weakened (they all stay); BLIND: an order whose judgment criterion is written in a form the checker's criterion parse does not read.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base checks, dry-run by the issuer before the cut: CTac7-AC1 base: FAIL as expected (the file does not exist); CTac7-AC2 base: PASS as expected (`RESULT: 59 of 59 arm(s) behaved`; the criterion's expected text `arm(s) behaved` is in it).
Source: row NFRA_CTLPLN-D2-S5 (1.0.0_SA_CTO~DELL2; the checkers' cell owner is this project's SEATS workstream).
