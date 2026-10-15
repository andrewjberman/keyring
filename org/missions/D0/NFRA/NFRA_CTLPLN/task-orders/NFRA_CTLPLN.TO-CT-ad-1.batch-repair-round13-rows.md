# TO NFRA_CTLPLN.TO-CT-ad-1 -- workstream BATCH round 2 (cell CT-ad-1): the round-13 batch repair -- routes.tf comments, the fence check's stale premises, the coverage-frame line, the census `--out` default

<to_id>NFRA_CTLPLN.TO-CT-ad-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~92</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run: ROUND14-BATCH arms=9/9 ok=True; proof-of-spec-check self-test RESULT: 63 of 63 arm(s) behaved (unchanged); FENCE-SCOPED rows_today=45 ... ok=True (unchanged); proof instance VALID on the committed state; the routes.tf diff holds only the two comment lines. Rows W92-S1..S3 accepted as INERT: the fence check calls AWS read-only on every run, so batch arm 2 compares the executable AST with the base instead; the coverage frame prints only beside a coverage violation, so the NOTE assertion sits on the one-unexpected fixture; proof-of-spec-check refuses instances outside its tree, so fixtures sit under the ignored .scratch/. coverage_check now takes an optional frames list; the self-test arm that filtered coverage-frame lost that filter, output byte-identical. The instance's expect for CTad1-AC2 is the regex arm\(s\) behaved (criterion text unchanged).</status_reason>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>BATCH</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ad-1` (`decompositions/NFRA_CTLPLN_DECOMP.round14.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Four small defects found in round 13, repaired in ONE cell. Each is INERT today. Read the named row first with the Grep tool (`"id": "<row id>"` in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`).

1. **`W87-S2`** -- `infra/aws/terraform/nfra-ctlpln-identity/routes.tf` lines about :23 and :30 are comments that still say a file named `simulate_policy.py` reads the route Deny document. That file was deleted in round 13. Reword both comments so they name no deleted file and say the authority is each apply's live policy simulation. Comment text only: no resource, no variable, no non-comment byte changes (a `git diff` of the file shows only `#` lines).
2. **`W89-S2`** -- `infra/aws/terraform/shared-infra/tests/check_fence_scoped_rows.py`: its docstring still states premises the registry has outgrown. Rewrite the stale paragraph (the "AMENDMENT 7" text, "the registry holds no scoped row now") to say what the row's `world_is` says: the registry holds real scoped rows and a grants object; the expected Deny count per row follows from its actions (AnyOtherAction always, ObjectsOutsidePrefix with an object action, ListingOutsidePrefix with ListBucket); the selector substitution applies only to the before roots over today's registry, and `before_pre` keeps the pinned selector. Docstring only: no executable line changes, and the check's printed result lines and exit code are byte-identical to the base on the same inputs.
3. **`W91-S2`** -- `.tools/proof-of-spec-check.py` `coverage_check` inserts its `coverage-frame` informational line into the violations list, so it prints as `VIOLATION:` and is counted in `violations=`. Verdict and exit code are unaffected today. Move that line out of the violations list so it prints with a non-violation prefix (`NOTE:`) and `violations=` counts only real violations. Every existing self-test arm keeps its meaning; an arm that counted the frame line as a violation is updated and the update is named in your report.
4. **`W8-S7`** -- `infra/aws/terraform/shared-infra/tests/dell_fence_census.py` (about :33 and :730) defaults `--out` to the baseline file `tests/dell_fence_census.json`, which `check_dell_fence_join.py` and `check_fence_scoped_rows.py` read; a `--live` re-take therefore silently changes the baseline. Fix: with `--live` the tool refuses to run unless `--out` is given explicitly, and an explicit `--out` equal to the baseline path prints `WARN: overwriting the baseline` first. Without `--live` the behaviour is unchanged. It must still make no AWS call when run in the test.

### BUILD

5. A NEW test `.tools/tests/test_round14_batch.py` (standard library, temporary directories only, no AWS, no network) with one or more arms per item: (1) the `git diff` of `routes.tf` against its base holds only comment lines, and neither comment names `simulate_policy`; (2) running `check_fence_scoped_rows.py` on its saved inputs prints the same result lines as the base (compare with the base copy via `git show HEAD:<path>` into a temporary directory) and its docstring no longer contains the text "holds no scoped row"; (3) a fixture instance whose acceptance rows are all expected prints `violations=0` and the `coverage-frame` line begins `NOTE:`, and a fixture with one unexpected row prints `violations=1`; (4) `dell_fence_census.py --live` with no `--out` exits non-zero before any AWS call (put a stub `aws` first on PATH that fails the arm if called), and with `--out <temporary file>` the baseline file's bytes are unchanged. Final line `ROUND14-BATCH arms=<k>/<n> ok=<True|False>`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. No aws call (the stub on PATH records any), no network, no push, no `terraform` command. `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink. ASCII only; Python 3.11. CLAUDE.md and org/XXX.md are LOCKED. Do NOT touch `s3-lgic-firm-buckets.tf` (row `W89-S3` is withheld from this cell). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it (`git log --oneline -1 -- <path>`), never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W92-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTad1-AC1" cell_refs="CT-ad-1"><invocation>python .tools/tests/test_round14_batch.py</invocation><expect>ok=True</expect></criterion>
`CTad1-AC1` -- every arm of the batch test passes (base: the file does not exist); report the whole last line with its denominator.

<criterion id="CTad1-AC2" cell_refs="CT-ad-1"><invocation>python .tools/proof-of-spec-check.py --self-test</invocation><expect>arm(s) behaved</expect></criterion>
`CTad1-AC2` -- the checker's own self-test still passes after item 3 (base: `RESULT: 63 of 63 arm(s) behaved`, a control); report the whole last line.

<criterion id="CTad1-AC3" cell_refs="CT-ad-1"><invocation>python infra/aws/terraform/shared-infra/tests/check_fence_scoped_rows.py</invocation><expect>ok=True</expect></criterion>
`CTad1-AC3` -- the fence-scoped check still passes after items 2 and 4 (base: `ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTad1-AC1,CTad1-AC2,CTad1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~92/NFRA_CTLPLN.TO-CT-ad-1.batch-repair-round13-rows.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTad1-AC1,CTad1-AC2,CTad1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round14.md</decomp_doc>
<owned_cells>CT-ad-1</owned_cells>
</decomp_ref>

<paths>
infra/aws/terraform/nfra-ctlpln-identity/routes.tf
infra/aws/terraform/shared-infra/tests/check_fence_scoped_rows.py
infra/aws/terraform/shared-infra/tests/dell_fence_census.py
.tools/proof-of-spec-check.py
.tools/tests/test_round14_batch.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; the Terraform file edit is comments only and nothing is applied.
comp-adversary: RUN -- a comment edit that changes a non-comment byte of routes.tf (arm 1 diffs the lines); a docstring edit that changes the fence check's result lines (arm 2 compares against the base output); the frame-line move hiding a real violation (arm 3 keeps a one-violation fixture); the census refusal firing on the non-live path (arm 4 runs both); BLIND: a consumer elsewhere that parses the `VIOLATION:` prefix of the coverage-frame line (the worker greps the repo for `coverage-frame` and reports the readers).
lane: the <paths> block IS the grant (worker RULING 1). `routes.tf` sits in the identity root whose lane is the CTO and the COO~C; the worker's grant here is the order's own, as in round 13's CT-ac-1.
</preflight>

risk: WORLD is declared because the L6 gate derives a floor from the infra path (routes.tf); this cell makes no AWS call and applies nothing.

Base checks, dry-run by the issuer before the cut: CTad1-AC1 base: FAIL as expected (the file does not exist); CTad1-AC2 base: PASS as expected (`RESULT: 63 of 63 arm(s) behaved`); CTad1-AC3 base: see the issuer's dry-run note in the issuance commit.
Source: CTO round-13 analysis section 4 item 1 (`ledger/ROUND_ANALYSIS.round13.md` @7d271cb57b), rows W87-S2, W89-S2, W91-S2, W8-S7. W89-S3 is WITHHELD (see the decomposition).
