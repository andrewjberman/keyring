# AMGT_RESAPP task order -- `AMGT-rk-56` -- every order is ISSUED with a `<status>` element the worker can flip, checked on the newly-added limb of the L6 gate

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-56</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~56</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits a commit-time gate and its tests; it arms no cron,
  alarm, monitor or cadence, reads no schedule and writes none; the no-monitor moratorium is unaffected.
comp-iam: DECLARED-NOT-APPLICABLE -- this order touches no AWS resource, no Terraform and no grant; every
  invocation is a local git and python act on the worktree.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~56`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~56;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-56` (R14-T2; process; row `AMGT_RESAPP-Z-S153`)

**The analysis row (`ROUND_ANALYSIS.round13.md` s.4 @9c8e04cd9a, row R14-T2 `:142`):** *"S153: every order issued
with a `<status>` element, checked on the newly-added limb"* -- process; co-sign no.

**The row, inlined (`INVESTIGATION_v1.md`, id `AMGT_RESAPP-Z-S153`, surfaced by `4.0.0_SA_CRO~Z` 2026-09-17
15:28Z, class OBSERVATION, owner `2.0.0_SA_COO~Z`).** `one_line`: *"All 15 round-13 task orders (AMGT-rk-19..rk-30,
first issued @f0cbb2d813, re-cut @7acf65b08b) carry NO <status> tag, while each worker face's closing step says to
flip `<status>` to complete; round-12 orders carried one from their adding commit (rk-9 @2726497094: 1 tag), and
to-check.py lists all 15 with status '??'. Twelve round-13 worker worktrees are already running on these bytes."*
`spec_asserts`: *"A task order's record face carries <status>, the worker flips it at close, and the order-reading
tools key on it -- as every round-12 order did from its adding commit."* `world_is`: *"Round 13's fifteen orders
have no status element; to-check cannot classify them, and each running worker's closing instruction targets a
field that does not exist, so each will have to invent the line at close. What other status-keyed readers (drain
refusers, the L10 open-order count) make of an untagged order was NOT traced here."* The row's own evidence
(`:7786`): *".tools/to-pipeline-gate.py:2506 STATUS_RE = re.compile(r'<status>\s*([A-Za-z_-]+)');
check_complete_flip (:2525-2540) acts only when the staged value is a done-word, so an untagged order meets that
limb only once a worker writes a tag."*

**THE MEASURED STATE, at HEAD (`.tools/to-pipeline-gate.py` last moved @458fbb65ba, 2834 lines; cite these lines):**
- The gate's ONLY status limb is `check_complete_flip()` `:2524-2560`, which runs on every staged order (`:2792-2794`)
  and acts only when `STATUS_RE` (`:2506`, NOT line-anchored) finds a DONE word (`DONE_WORDS` `:2507`: complete,
  completed, closed, done). An order issued with no `<status>` element at all meets NO limb of `check_file()`
  (`:2402-2505`): GATE (i) tier, (vii) issued_by, (v) paths, (viii) placeholders, (iv) issuer, cell refs, (iv-b)
  criterion grammar, (ix) output vocabulary, project stage, LIMBS 4-6, preflight -- none reads the record face's
  status. That is how 15 of 15 round-13 orders were born untagged twice.
- The status readers downstream key on the element: `.tools/to-check.py:113-122` `_extract_status_tag()` (masks
  inline code spans, then reads the element; `UNKNOWN` prints as `??` `:60`); `.tools/surprise-row-gate.py:1125-1165`
  `_open_tos_census()` reads `TO_STATUS_RE` and classes `<no status tag>` as OPEN unless the proof widens it
  (`:1150-1157`); `.tools/owned-paths-validate.py:125-140` reads the element LINE-ANCHORED after row Z-S15 measured a
  prose mention (*"Carries NO <status> tag at all"*) captured as the tag. The lesson every reader learned is the
  one this limb must be born with: **the element is read on its own line, never from prose.**
- Census at the cut over `org/missions/D5/AMGT/AMGT_RESAPP/task-orders/*.md`: 97 orders, 94 carry a line-anchored
  `<status>WORD</status>` element, 3 carry none (`rk-20.price-generation-contract`,
  `rk-23.artifact-name-encoding`, `rk-30.scores-adapter-model-tab` -- all terminal by proof per S169's bucket; NOT
  back-filled by this cell). Re-measure at spawn (AC3 prints it).
- The gate's self-test is `_self_test()` `:665` (pure arms; the `arms` list at `:695`); the real-index battery
  pattern is `.tools/tests/test_gate_viii_modify.py` (`:1-40`).

**RULED, what you build:**
1. **GATE (xi) -- the status-element limb, on NEWLY-ADDED tree orders only.** In `to-pipeline-gate.py`, a pure
   function `_status_element_violations(rel, text)` graded inside `check_file()` beside GATE (viii): a NEWLY-ADDED
   tree order must carry a LINE-ANCHORED `<status>WORD</status>` element -- regex
   `^[ \t]*<status>\s*([A-Za-z_-]+)\s*</status>[ \t]*$` (multiline) -- and the word must NOT be terminal at issuance
   (an order is issued open; refuse a word in `DONE_WORDS` `:2507` OR in the sibling gate's wider
   `TERMINAL_TO_WORDS` (`surprise-row-gate.py:152`: complete, completed, closed, done, superseded, cancelled,
   canceled, withdrawn) -- read as one set, stated in the docstring). Refusal text names the row:
   *"a NEW tree task order carries NO <status> element on its own line -- issue it with `<status>pending</status>`
   in the record face; the worker flips it at close and every status reader keys on it (row AMGT_RESAPP-Z-S153:
   15 of 15 round-13 orders were born untagged)"*; a terminal word at issuance is refused as *"born terminal"*.
   Flat-root orders are not graded. A MODIFY is never graded by this limb (a worker adding the element at close
   to a legacy untagged order is a modification and is admitted, as S153's `world_is` anticipates).
2. **A prose mention is inert.** A face whose only `<status>` is inside a backticked instruction (*"flip
   `<status>` to `complete`"*) is refused exactly like a face with none -- the anchored regex cannot match it; a
   self-test arm proves it (the Z-S15 / to-check FIX C class).
3. **`--status-census <CODE>`, a read-only CLI limb** (beside `--sweep` and rk-55's `--rounds`): prints, for the
   project's tree orders at HEAD, orders WITH a line-anchored element, orders WITHOUT (each named), the word
   distribution, and the denominator; rc 0 always.
4. **Self-test arms** in `_self_test()` (pure, RED/GREEN: missing element refused naming S153; prose-only mention
   refused; `pending` admitted; born-`complete` refused; flat-root not graded) and a real-index battery
   `.tools/tests/test_gate_xi_status_element.py` in the `test_gate_viii_modify.py` shape: in a scratch repo, (RED)
   a real order's bytes with the `<status>` line removed, staged as ADDED, refused at rc 1 naming S153; (RED) the
   same bytes with the element replaced by a backticked prose mention only, refused; (GREEN) the same bytes with
   `<status>pending</status>`, admitted by THIS limb (other limbs' output tolerated and named); (GREEN) an untagged
   order COMMITTED, then staged as MODIFIED with the element added, NOT graded by this limb; (RED) born
   `<status>complete</status>`, refused. The battery prints `RESULT: %d arm(s) failed of %d` and `BATTERY PASS`.

**What this cell does NOT change:** `check_complete_flip` and `STATUS_RE` (the flip limb keeps its own regex and
scope); `.tools/to-check.py`; `.tools/surprise-row-gate.py`; the three untagged orders at HEAD (no back-fill --
prospective only, the gate's own doctrine at `:1757-1762`); nothing in the spine or CLAUDE.md; rk-55's `<round>`
limb (a sibling limb, built by `AMGT-rk-55`, not here).

**THE VALIDATION BAR (`C-VALIDATION-NAMES`, PRD `:1652-1658`):** a gate cell is proven on planted orders in a
scratch repo and on a READ of this project's own orders at HEAD; it runs no producer and touches no name.

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.22 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round13.md` @9c8e04cd9a s.4 row R14-T2 (`:142`) and s.6
(`:207`, S153 carried to T2); the row `AMGT_RESAPP-Z-S153` (INVESTIGATION_v1.md `:7770-7793`). CLAUDE.md Rule 27
(the RECORD FACE never travels; the worker flips `<status>`). PRD v0.13 @1699960261 is not moved by this cell (a
process cell; `C-VALIDATION-NAMES` `:1652-1658` binds its proof).

## 3. SURFACES -- what you may read and write

<paths>
.tools/to-pipeline-gate.py
.tools/tests/test_gate_xi_status_element.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~56/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-56.status-element-at-issuance.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (read `.tools/to-check.py:60-140`,
  `.tools/surprise-row-gate.py:152,1125-1165`, `.tools/owned-paths-validate.py:125-140` for the three readers'
  status regexes; `.tools/tests/test_gate_viii_modify.py` for the battery shape). Scratch is
  `<your worktree>/.scratch/` only; the battery's scratch repos live under `.scratch/` and are removed at its end.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~56 <0.9.0_WK_AMGT_RESAPP~56@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every
  `.py` edit passes `.tools/commit-gate.sh` (py_compile + ds-precommit + ruff py39). Add no non-ASCII to the gate
  file.
- **THE GATE YOU EDIT GRADES YOUR OWN COMMIT:** your status flip on this order is a MODIFY (not graded by the new
  limb); dry-run the gate on your staged set before committing.

## 4. BOUNDS

**NO new approval gate** -- this limb is the mechanism of a convention every round-12 order already honoured and
the CTO ruled; it refuses exactly the defect S153 measured. **NO back-fill** of the 3 untagged orders at HEAD.
**SINGLE-WRITER SURFACE:** `.tools/to-pipeline-gate.py` is also edited this round by `AMGT-rk-55` (slot ~55: GATE (x),
the `<round>` limb, `--rounds`, its self-test arms). The COO sequences the two drains; if the spawn prompt says
rk-55 has landed at HEAD, confirm your worktree carries it (`git log --oneline -3 -- .tools/to-pipeline-gate.py`)
before you edit, and add your arms and CLI limb BESIDE its, never over them; if it has not landed, say so in your
report so the second drain rebases on yours. **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send,
notification or freshness checker.** No vendor call. No non-ASCII in anything you write. **PUSH: never.**
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- 97 / 94 / 3 are the cut's
figures; AC3 re-measures them at spawn.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W56-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-56"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/to-pipeline-gate.py --self-test 2>&1 | tail -40; echo rc=${PIPESTATUS[0]}</invocation><expect>rc=0 and the printed arm list carries at least FIVE arms whose names begin "status-element" (missing element refused naming S153; a backticked prose mention alone refused; pending admitted; born-complete refused; flat-root not graded), every arm PASS -- the self-test is pure and reads no repo</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-56"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/tests/test_gate_xi_status_element.py 2>&1 | tail -30; echo rc=${PIPESTATUS[0]}</invocation><expect>rc=0, a line "RESULT: 0 arm(s) failed of N" with N at least 5 and "BATTERY PASS": in a scratch git repo under .scratch/, real order bytes staged as ADDED without a status line are REFUSED by the gate's own CLI at rc 1 with a message naming "S153"; the same bytes with only a backticked prose mention of the element are REFUSED; with <status>pending</status> on its own line they are ADMITTED by this limb; an untagged order COMMITTED then staged as MODIFIED with the element added is NOT graded by this limb; bytes born <status>complete</status> are REFUSED as born terminal; the scratch repo is removed at the end</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-56"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/to-pipeline-gate.py --status-census AMGT_RESAPP; echo rc=$?</invocation><expect>rc=0 and a read-only census of this project's tree orders AT HEAD: orders WITH a line-anchored status element (94 at the cut), orders WITHOUT, each named (3 at the cut: rk-20.price-generation-contract, rk-23.artifact-name-encoding, rk-30.scores-adapter-model-tab), the status-word distribution, and the denominator "97 order(s) at HEAD" (re-measure; round 14's issuance may have moved every number)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-56"><invocation>cd "$(git rev-parse --show-toplevel)" && src=org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-19.adapter-second-join.md && probe=org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-19.zz-status-probe.md && python -c "
import io, re, sys
t = io.open('$src', encoding='utf-8').read()
t2 = re.sub(r'^[ \t]*<status>[^\n]*</status>[ \t]*\n', '', t, flags=re.M)
print('status_lines_removed', len(re.findall(r'^[ \t]*<status>', t, flags=re.M)) - len(re.findall(r'^[ \t]*<status>', t2, flags=re.M)))
io.open('$probe', 'w', encoding='utf-8', newline='\n').write(t2)
" && git add "$probe" && python .tools/to-pipeline-gate.py "$probe" 2>&1 | grep -c "NO <status> element"; git reset -q -- "$probe"; rm -f "$probe"; echo probe_removed=$([ -f "$probe" ] && echo no || echo yes)</invocation><expect>status_lines_removed 1, then the count line reads 1 or more -- a real order copied under a new name with its status line stripped and STAGED (never committed) in this worktree is refused by the live gate with the S153 message -- and probe_removed=yes with the index restored (git status shows no probe path); other limbs' refusals on the same probe may print beside it and are recorded, not counted</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on
this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~56/AMGT_RESAPP.TO-AMGT-rk-56.status-element-at-issuance.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, naming whether rk-55's edit was at HEAD when you edited.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~56</slot>
<fabric>site-z</fabric>
