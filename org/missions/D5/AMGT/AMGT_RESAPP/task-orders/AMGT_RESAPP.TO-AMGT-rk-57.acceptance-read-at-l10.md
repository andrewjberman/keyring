# AMGT_RESAPP task order -- `AMGT-rk-57` -- the L10 precondition gains an ACCEPTANCE READ: per criterion, over every order of the round, PASS / FAIL / UNVERIFIABLE with the denominator printed, beside the open-order census that counts a failing order terminal

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-57</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~57</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits a commit-time gate's READ limb and its tests; it arms
  no cron, alarm, monitor or cadence, reads no schedule and writes none; the no-monitor moratorium is unaffected.
comp-iam: DECLARED-NOT-APPLICABLE -- this order touches no AWS resource, no Terraform and no grant; every
  invocation is a local git and python act on the worktree.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~57`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~57;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-57` (R14-T3; process; row `AMGT_RESAPP-Z-S169`)

**The analysis row (`ROUND_ANALYSIS.round13.md` s.4 @9c8e04cd9a, row R14-T3 `:143`):** *"S169 (s.3.3)"* -- process;
co-sign no. **The ruling, s.3.3 (`:81-85`), verbatim:** *"Acceptance at L10 (S169, OPEN, ARMED; disarm owner
`2.0.0_SA_COO~Z`). RULED: a TOOL cell; hand sweep until then. The census counts an order terminal on a VALID
instance whatever its verdicts, so a close can read clean over failing criteria. The L10 precondition gains an
acceptance read: per criterion, over every order of the round, in three classes (PASS / FAIL / UNVERIFIABLE),
denominator printed. Until the tool lands, every close runs the sweep by hand, as this one did."* Round 13's hand
sweep (s.1 `:28-33`): **26 PASS / 3 FAIL / 0 UNVERIFIABLE** over the round's 15 orders, the three FAILs criterion
defects (`rk-23` AC1, `rk-20` AC1, `rk-30` adapter AC1), and `rk-2` AC6 / `rk-8` AC4 NOT_EVALUATED naming a missing
instrument.

**The row, inlined (`INVESTIGATION_v1.md`, id `AMGT_RESAPP-Z-S169`, surfaced by `1.0.0_SA_CTO~Z` 2026-09-18 02:17Z,
class BLOCKING, ARMED, disarm owner `2.0.0_SA_COO~Z`).** `one_line`: *"AN ORDER WITH A GENUINELY FAILING
ACCEPTANCE CRITERION IS COUNTED TERMINAL BY THE OPEN-ORDER CENSUS, AND THE L10 PRECONDITION IS GRADED ON THAT
CENSUS. AMGT-rk-30's PAGE half records AC1 PASS and AC2 FAIL in its own proof instance; proof-of-spec-check returns
VALID (rc=0); and _open_tos_census therefore lists it in the 'terminal by a VALID proof-of-spec instance at HEAD'
bucket and REMOVES IT FROM THE OPEN SET. ... THE CAUSE IS THAT 'VALID' NAMES WELL-FORMEDNESS, NOT PASSING: the
checker's frames grade the surprises set, invocation alignment, count bars and drives declarations, and NOT ONE OF
THEM READS A CRITERION'S PASS/FAIL VERDICT. So a round whose close is graded off the open-order census can close
over a failing acceptance test."* `spec_asserts`: *"The L10 order is loaded-bearing (CLAUDE.md Rule 27, LD-0521):
L10 runs only after every task order is TERMINAL. The open-order census is the instrument the fabric uses to read
that precondition, and 'terminal by a VALID proof-of-spec instance at HEAD' is one of its two terminal classes."*
`world_is`: *"VALID is a well-formedness verdict. An instance recording a FAIL is still VALID, so an order whose
acceptance genuinely fails can be counted terminal and drop out of the open set. rk-30's page half is in exactly
that state right now: AC2 FAILS, the issuer says the order stays open, and the census says 2 of 97 open without
it."* The row's own rule (`notes`): *"a count or a verdict is evidence about the PROPERTY ITS CODE READS, never
about the property its NAME suggests; read the frames, not the label ... FOR THE ROUND CLOSE: the L10 precondition
needs BOTH reads -- the census for terminality AND a per-order acceptance sweep."*

**THE MEASURED STATE, at HEAD (`.tools/surprise-row-gate.py` last moved @7f82f66f93, 2805 lines; cite these lines):**
- `_open_tos_census()` `:1125-1165`: lists the project's tracked orders (`git ls-files`, `:1134-1135`), reads each
  at HEAD (or the merged index), classes an order terminal by its status word (`TERMINAL_TO_WORDS` `:152`) OR by
  `_proof_terminal()` `:1056-1113` -> `_proof_verdict()` `:1033-1053`, which runs
  `python .tools/proof-of-spec-check.py <instance> --governing-order <order>` and reads **rc only** (`:1049-1050`).
  No line reads an acceptance row's `status`.
- The census feeds the L10 precondition `_route_precondition_violations()` `:1256-1294`, called from `check_file()`
  at `:1895`; the precondition's NOTES print at `:1943-1946` (*"L10 precondition for %s -- %d task order(s) at
  HEAD on both roots, 0 open; ..."*). Main prints notes at `:2739-2740` and refuses only on violations.
- **A gate refuses an act only when that act can remedy its condition** -- the rule the same file's staleness limb
  was corrected to at @7f82f66f93 (`:968-1008`, *"A GATE REFUSES AN ACT ONLY WHEN THAT ACT CAN REMEDY THE GATE'S
  CONDITION"*). A slug cannot remedy a FAILED criterion (the CVO grades acceptance at L9; the COO recuts at L10), so
  the acceptance read is a DISCLOSURE beside the census, never a refusal.
- The instance's own grammar (`org/standards/PROOF_OF_SPEC.schema.json:183-260`): one `acceptance` row per
  criterion, `criterion_id`, `status` in `PASS | FAIL | UNCOMPUTABLE-BY-CONSTRUCTION | UNVERIFIABLE-BY-INSTRUMENT |
  N/A-BY-CONSTRUCTION | UNCOMPUTABLE`; a judgment row (`judgment: true`, `:255`) carries NO PASS/FAIL. The order's own
  criteria are the criterion tags (id, cell_refs, optional judgment="true") in its proof-of-spec block;
  its round is the line-anchored `<round>N</round>` in its record face (94 of 97 orders at the cut carry one).
- The spine's L10 (`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md:436`, `:487-488`): *"every task order under the
  project is terminal, each finished with a valid proof-of-spec instance"*; terminality is read *"from the
  proof-of-spec instances at HEAD and never from a `<status>` field"*. The spine says VALID; it does not say
  PASSING -- which is exactly why the second read is added BESIDE the first and does not replace it.
- The negative control exists at HEAD: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~31/
  AMGT_RESAPP.TO-AMGT-rk-30.page-scores-render.proof_of_spec.json` records AC1 PASS and AC2 FAIL (S169's own
  measurement); the census counts its order terminal.

**RULED, what you build:**
1. **`_acceptance_sweep(root, code, round_n=None, merging=False)`** in `surprise-row-gate.py`: over the SAME order
   listing `_open_tos_census` uses (HEAD, or the merged index at a merge), for each tree order: read its `<round>`
   (line-anchored; orders without one fall in an `unrounded` bucket that is printed, never dropped), parse its
   criterion ids and judgment flags from its proof-of-spec block, locate its instance with `_proof_terminal`'s OWN
   lookup (the two names, `deliverables/*/`, tracked at the read ref; more than one candidate = ambiguous), and
   class every criterion: **PASS** (the row for that id reads `status: PASS`), **FAIL** (`status: FAIL`),
   **UNVERIFIABLE** (any other status; a judgment criterion; no row for the id; no instance, an unreadable or an
   ambiguous instance -- each with its reason kept on the row). Return `{"orders": [...], "criteria": n, "PASS": a,
   "FAIL": b, "UNVERIFIABLE": c, "round": N or None, "unrounded": k}` with the FAIL and UNVERIFIABLE rows listed as
   `<order basename>:<criterion-id> (<reason>)`. A pure classifier `_classify_acceptance(rows_by_id, criteria)` does
   the mapping so the self-test can grade it without a repo.
2. **The slug-time NOTE.** Where the L10 precondition's note is appended (`:1943-1946`), append ONE more note per
   project and slug: *"ACCEPTANCE (round N, the slug's own): PASS a / FAIL b / UNVERIFIABLE c of d criteria over e
   order(s); FAIL: ...; UNVERIFIABLE: ..."* -- the round read from the new remediation row's own `round`
   (`_round_num` `:927`), the census note kept beside it unchanged. It is a NOTE, never a violation: the slug is
   not refused on a FAIL (the rule at `:991`); the disagreement S169 named becomes VISIBLE in one output, which is
   what the ruling asks for. Whether a FAIL should one day refuse is the COO's and CTO's call, not this cell's.
3. **`--acceptance <CODE> [--round N]`, a read-only CLI limb** (beside `--self-test`): prints the sweep for the
   project (all rounds, or one), rc 0 always -- the hand sweep, mechanized, that every close runs.
4. **Self-test arms** in `_self_test()` (`:1960`; pure: PASS/FAIL mapped; every other status UNVERIFIABLE; a judgment
   criterion UNVERIFIABLE even with a PASS row; a missing row UNVERIFIABLE; the sweep function's output never
   enters the violations list) and a real-bytes battery `.tools/tests/test_acceptance_sweep.py` on THIS project at
   HEAD: the rk-30 page-half instance above classes AC1 PASS and AC2 FAIL; the sweep for round 13 lists
   `rk-30.page-scores-render:AC2` under FAIL while `_open_tos_census` lists that order in its terminal-by-proof
   note -- both reads printed side by side; the battery prints `RESULT: %d arm(s) failed of %d` and `BATTERY PASS`.

**What this cell does NOT change:** `_open_tos_census`, `_proof_terminal`, `_proof_verdict` (terminality keeps the
spine's rule); `proof-of-spec-check.py` and its frames; the L10 precondition's refusal conditions (nothing new
refuses); the standing corpus pass; any instance or order at HEAD; the spine or CLAUDE.md. **The row S169 is
disarmed by its owner `2.0.0_SA_COO~Z` on this cell's landing, not by you** -- you may write an OBSERVATION row
citing your battery's numbers; the disarm is the COO's.

**THE VALIDATION BAR (`C-VALIDATION-NAMES`, PRD `:1652-1658`):** a gate cell is proven on planted rows (pure arms)
and on a READ of this project's own orders and instances at HEAD; it runs no producer and touches no name.

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.22 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round13.md` @9c8e04cd9a s.3.3 (`:81-85`), s.1 (`:28-33`, the
hand sweep 26 / 3 / 0) and s.4 row R14-T3 (`:143`), s.6 (`:207`); the row `AMGT_RESAPP-Z-S169` (INVESTIGATION_v1.md
`:8578-8602`). The spine `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md:436`, `:487-488`. CLAUDE.md Rule 27 (L10
ONLY after every TO is terminal; LD-0521). PRD v0.13 @1699960261 is not moved by this cell (a process cell;
`C-VALIDATION-NAMES` `:1652-1658` binds its proof).

## 3. SURFACES -- what you may read and write

<paths>
.tools/surprise-row-gate.py
.tools/tests/test_acceptance_sweep.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~57/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-57.acceptance-read-at-l10.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (read `.tools/proof-of-spec-check.py`,
  `org/standards/PROOF_OF_SPEC.schema.json`, every instance under `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/`,
  `.tools/tests/test_gate_viii_modify.py` for the battery shape). Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~57 <0.9.0_WK_AMGT_RESAPP~57@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every
  `.py` edit passes `.tools/commit-gate.sh` (py_compile + ds-precommit + ruff py39). Add no non-ASCII to the gate
  file (it already carries some; add none).
- **THE GATE YOU EDIT GRADES YOUR OWN ROWS:** the pre-commit hook runs THIS worktree's `surprise-row-gate.py` on
  your surprise-channel commit, and its standing corpus pass (`:2724-2737`) must still pass; dry-run the gate on
  your staged set before committing (`python .tools/surprise-row-gate.py <staged paths>`), and `--self-test` after
  every edit.

## 4. BOUNDS

**A READ, NOT A GATE** -- nothing new refuses; the acceptance sweep is a NOTE at slug time and a CLI read. Do NOT
make a FAIL refuse the slug: a slug cannot remedy a FAIL (`:991`), and an agent-made approval gate is forbidden.
**NO change to terminality** -- the spine's rule (VALID instance = terminal) stays exactly as `_proof_terminal`
reads it. **NO edit to any instance or order at HEAD** (the rk-30 page half's FAIL is the negative control; leave
it). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or freshness checker.** No vendor
call. No non-ASCII in anything you write. **PUSH: never.**
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- 26 / 3 / 0 over 15 orders is
the CTO's hand sweep at the cut; AC3 re-measures round 13 at spawn and prints what the tool reads (rk-26 was
WITHDRAWN with no instance, so its criteria read UNVERIFIABLE on the tool where the hand sweep counted none --
record the difference, do not force agreement).
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W57-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-57"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/surprise-row-gate.py --self-test 2>&1 | tail -40; echo rc=${PIPESTATUS[0]}</invocation><expect>rc=0 and the printed arm list carries at least FIVE arms whose names begin "acceptance" (PASS and FAIL mapped from the row status; every other status UNVERIFIABLE; a judgment criterion UNVERIFIABLE even beside a PASS row; a missing row UNVERIFIABLE; the sweep contributes NO violation), every arm PASS, every pre-existing arm still PASS -- the self-test is pure and reads no repo</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-57"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/tests/test_acceptance_sweep.py 2>&1 | tail -30; echo rc=${PIPESTATUS[0]}</invocation><expect>rc=0, "RESULT: 0 arm(s) failed of N" with N at least 3 and "BATTERY PASS": on THIS project's real bytes at HEAD, the rk-20 instance (deliverables/0.9.0_WK_AMGT_RESAPP~24/AMGT_RESAPP.TO-AMGT-rk-20.price-generation-contract.proof_of_spec.json) classes AC1 FAIL (ISSUER REPAIR on row W57-S1: the rk-30 page-half control the draft named was fixed at 9074091db1 after the analysis; rk-20 AC1 is the CTO's criterion defect that still reads FAIL live); the round-13 sweep lists rk-20:AC1 under FAIL; and _open_tos_census's note lists the same order as terminal by a VALID instance -- the two reads printed side by side, which is S169's disagreement made visible in one output</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-57"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/surprise-row-gate.py --acceptance AMGT_RESAPP --round 13; echo rc=$?</invocation><expect>rc=0 and the round-13 sweep printed with its denominators: "PASS a / FAIL b / UNVERIFIABLE c of d criteria over e order(s)" with e the round-13 orders carrying <round>13</round> at HEAD (12 at the cut; re-measure), b at least 3 naming rk-23 AC1, rk-20 AC1 and rk-30 scores-adapter AC1 (the CTO's three criterion defects; ISSUER REPAIR on row W57-S2: those three orders now carry a record face with <round>13</round>, added by the issuer on this branch, so the filtered read sees them; rk-30.page-scores-render AC2 is NOT expected under FAIL -- it was fixed at 9074091db1), every UNVERIFIABLE row carrying its reason (rk-26's criteria: no instance tracked), and the unrounded bucket printed with its count</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-57"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import io, re
t = io.open('.tools/surprise-row-gate.py', encoding='utf-8', errors='replace').read()
print('acceptance_sweep_defs', len(re.findall(r'^def _acceptance_sweep\(', t, flags=re.M)))
print('classify_defs', len(re.findall(r'^def _classify_acceptance\(', t, flags=re.M)))
print('ACCEPTANCE_note_sites', len(re.findall(r'ACCEPTANCE \(round', t)))
print('open_tos_census_unchanged_signature', len(re.findall(r'^def _open_tos_census\(root, code, merging=False\):', t, flags=re.M)))
print('proof_verdict_reads_rc_only', 'r.returncode == 0' in t)
"</invocation><expect>acceptance_sweep_defs 1, classify_defs 1, ACCEPTANCE_note_sites at least 1 (the slug-time note text), open_tos_census_unchanged_signature 1 and proof_verdict_reads_rc_only True -- the two new reads exist and the terminality reads are byte-for-byte the spine's, untouched (0 / 0 / 0 / 1 / True at HEAD)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on
this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~57/AMGT_RESAPP.TO-AMGT-rk-57.acceptance-read-at-l10.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, with AC3's round-13 line verbatim so the COO can disarm
S169 against it.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~57</slot>
<fabric>site-z</fabric>
