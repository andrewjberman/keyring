# AMGT_RESAPP task order -- `AMGT-rk-28` -- the criteria-quality checker gains a shape for the data-vacuity class

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-28</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~30</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the standing
  collection-stays-off / no-monitor moratorium is unaffected and no schedule is read or written.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes only to already-provisioned resources (the existing
  S3 bucket/prefixes and DynamoDB table this project already reads and writes) under the existing Lambda
  execution role; it grants no new permission and provisions no new resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~30`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the
paths in section 3 exist; if any is absent, STOP with a BLOCKING row. **YOU HOLD CHAIN CK, one order, the
whole of `.tools/criteria_quality_checker.py` for this round.** Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~30;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-28` (S121; sibling of `AMGT-rk-9` AC4)

**THE MEASURED STATE.** `.tools/criteria_quality_checker.py` (358 ln, built by `AMGT-rk-9`) refuses five
shapes via `evaluate(criteria)` (`:195-208`): `shape1_zero_collected` (`:128`), `shape2_rc_swallowed`
(`:139`), `shape3_grain_mismatch` (`:151`, cross-row), `shape4_inexact_capture` (`:179`),
`shape5_no_timeout` (`:187`) -- each sealed in `_self_test()` (`:228-320`) with a planted-mutant/clean-control
pair. `AMGT-rk-9` AC4 is a JUDGMENT criterion (graded by the CVO at L9) asking whether this checker WOULD HAVE
refused round-11's two unfailable criteria -- it is not itself the fix.

**The gap, S121's new instance (round 12's `rk-15` AC3):** a criterion counting occurrences of a FIELD NAME
in source text (e.g. `"points"` or `"points_emitted"`) can PASS while every counted value is invented,
missing, or unverified -- the count asserts the field's PRESENCE, never its VALUE. This is a SIBLING class to
`shape1_zero_collected` (which flags a zero count) but distinct: `shape1` catches "nothing was collected";
this new shape must catch "something was collected, and the criterion never checks what it actually holds."

**RULED:** add `shape6_data_vacuity(c)` to `.tools/criteria_quality_checker.py`, following `shape1`'s exact
pattern (`:128-136`) -- same function signature, same return shape. It detects an invocation whose `expect`
counts a field-name TOKEN (a bare occurrence/count pattern) while asserting NOTHING about the counted items'
VALUES or CONTENT (no comparison against a source excerpt, no per-item value check). Wire it into
`evaluate()`'s per-criterion loop (`:200`), in the same position/order style as the other five shapes. Add
ONE sealed mutant + one clean control to `_self_test()` (`:228-320`), mirroring `rk-15` AC3 VERBATIM as the
planted mutant (a criterion whose `expect` reads something like "points-emitted >= N" against an invocation
that counts a token, never a value) and a criterion that DOES check a value as the clean control.

## 2. WHERE THIS CAME FROM

**ROUND 13**, decomposition v1.7 s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-12 analysis s.3.6 @`9419550eb1`
("ENDORSED, with one more measured instance"). PRD v0.10, ADMITTED, no PRD change (a QA-tooling improvement,
not a new outcome).

## 3. SURFACES -- what you may read and write

<paths>
.tools/criteria_quality_checker.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~30/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-28.checker-data-vacuity-shape.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Write only `.tools/criteria_quality_checker.py` -- do not
  touch `AMGT-rk-9`'s own task order file or any existing shape function's body. Scratch is
  `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~30 <0.9.0_WK_AMGT_RESAPP~30@opal.agent>" -F <msgfile> -- <paths>`.
  Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

Not portal-touching, not vendor-touching. **NO alarm, monitor, SNS/SES-send, notification or freshness
checker.** No non-ASCII in anything you write. **PUSH: never.**
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row;
never repaired, widened, or satisfied by a route this order did not name.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W30-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP
WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-28"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
from importlib import import_module
mod = import_module('tools.criteria_quality_checker') if False else None
import sys
sys.path.insert(0, '.tools')
import criteria_quality_checker as cqc
print('has_shape6', hasattr(cqc, 'shape6_data_vacuity'))
mutant = {'id': 'AC3', 'invocation': 'python -c \"print(open(\\'x\\').read().count(\\'points\\'))\"', 'expect': 'points-emitted >= 6'}
clean = {'id': 'AC9', 'invocation': 'python -c \"import json; d=json.load(open(\\'x\\')); print(d[\\'value\\'])\"', 'expect': 'value equals 42, matched against the source excerpt'}
print('mutant_flagged', bool(cqc.shape6_data_vacuity(mutant)) if hasattr(cqc, 'shape6_data_vacuity') else 'NO FUNCTION')
print('clean_passes', not bool(cqc.shape6_data_vacuity(clean)) if hasattr(cqc, 'shape6_data_vacuity') else 'NO FUNCTION')
"</invocation><expect>has_shape6 is True; mutant_flagged is True (the rk-15 AC3-shaped criterion, a bare token count with no value assertion, IS refused); clean_passes is True (a criterion that names a specific expected value and checks it against a source is NOT refused) -- if the worker's actual function/mutant shape differs from this literal example, it names the real one and re-runs an equivalent substitution, showing both the flag and the pass</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-28"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/criteria_quality_checker.py --self-test 2>&1 | tail -20</invocation><expect>the self-test suite passes with SIX sealed shape pairs now present (not five), the new shape6 mutant/clean pair among them, and no existing shape's pair regresses -- print the pass/fail line for every shape, not just an overall OK</expect></criterion>
</proof_of_spec>

**Record the ACTUAL OUTPUT and DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~30/AMGT_RESAPP.TO-AMGT-rk-28.checker-data-vacuity-shape.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>13</round>
<slot>~30</slot>
<fabric>site-z</fabric>
