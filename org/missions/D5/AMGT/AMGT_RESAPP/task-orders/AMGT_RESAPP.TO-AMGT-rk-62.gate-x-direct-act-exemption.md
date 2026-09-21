# AMGT_RESAPP task order -- `AMGT-rk-62` -- GATE (x)'s missing-`<round>` branch gets a narrow, line-anchored exemption for an order that explicitly declares itself round-less (`<direct_act>true</direct_act>`), so `AMGT-rk-58`'s own minter can land a legal order while a bare omission is still refused exactly as today

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-62</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~62</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits two repository tools and two test files; it arms no
  cron, alarm, monitor or cadence, reads no schedule and writes none; the standing no-monitor moratorium is
  unaffected.
comp-iam: DECLARED-NOT-APPLICABLE -- this order performs NO live AWS act of any kind: no invoke, no read of a
  live policy, no Terraform, no deploy. Every read and write is local git-tracked source and a scratch git repo
  the tests build themselves.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~62`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~62;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-62` (R15-T1; row `AMGT_RESAPP-Z-W58-S2`; process)

**The analysis row, verbatim (`ROUND_ANALYSIS.round14.md` @93cb6416e4 s.2.1, `:53-69`):** *"GATE (x) vs the `rk-58`
direct-act minter (W58-S2, packet finding 6 / adjudication s.4 item 8). RULED. `to-pipeline-gate.py`'s
one-issuer-per-round limb refuses an order with no `<round>` element; `rk-58` built a direct-act minter that emits
orders WITHOUT a round by design (a direct act is not a round cell). The two orders land contradictory requirements
on the same gate ... RULING: the gate's missing-`<round>` branch gets a narrow exemption, not a general weakening.
An order that declares itself round-less EXPLICITLY (a `<direct_act>true</direct_act>` element, or equivalent,
present and readable by the same parser this gate already uses) is exempted from the one-issuer-per-round check; an
order that is simply missing `<round>` with no such declaration is refused exactly as today. This keeps the
one-issuer-per-round protection intact for every round cell (the class the gate exists to protect) while giving the
minter's own declared shape a legal path. ... Not ruled here, and why: the exact element name and its exemption's
own negative control (an order that lies about being a direct act) are the cutting cell's to design and prove --
this seat is ruling the SHAPE of the fix, not writing the diff."*

**The row this cell closes, `AMGT_RESAPP-Z-W58-S2`** (carried forward from round 14, adjudication s.4 item 8, packet
finding 6): GATE (x)'s missing-`<round>` branch refuses `AMGT-rk-58`'s own direct-act minter's rendered orders,
because the minter deliberately emits no `<round>` element (`.tools/direct-act-order.py` `_self_test_no_round_element`,
row `AMGT_RESAPP-Z-W58-S1`'s repair) and the gate's missing-key branch (added for `AMGT-rk-55`, row S154) refuses
ANY new tree order with no `<round>` element, with no exception.

**THE ELEMENT NAME, ruled by this seat as the cutting cell (the analysis licenses it):** `<direct_act>true</direct_act>`,
line-anchored, the SAME discipline as `ROUND_ELEMENT_RE` (`to-pipeline-gate.py:1835`) and `PLACEHOLDERS_TAG_RE` --
a prose mention elsewhere in the face is inert and is not read as the element.

**THE MEASURED STATE, at HEAD (cite these lines; do not re-derive them from memory):**
- `.tools/to-pipeline-gate.py:1835`: `ROUND_ELEMENT_RE = re.compile(r"^[ \t]*<round>\s*([0-9]+)\s*</round>[ \t]*$", re.M)`.
- `.tools/to-pipeline-gate.py:1874-1902`, function `_round_issuer_violations(rel, text, head_rounds)`: when
  `ROUND_ELEMENT_RE.search(text or "")` finds no match, it UNCONDITIONALLY returns a one-item violation list naming
  the missing key (`:1886-1891`). This is the branch that refuses `rk-58`'s minted orders.
- `.tools/to-pipeline-gate.py:917-934`: the self-test arms for GATE (x) (`round-issuer RED`/`GREEN` entries in the
  `arms` list inside the self-test function), 85 of 85 passing at this cut (`python .tools/to-pipeline-gate.py
  --self-test`).
- `.tools/tests/test_gate_x_round_issuer.py`: the real-index battery for GATE (x), 4 of 4 passing at this cut
  (`python .tools/tests/test_gate_x_round_issuer.py`). Helper `_order_text(round_line, status="issued")` at
  `:87-113` builds a fixture order body; `round_line` is inserted verbatim when not `None`.
- `.tools/direct-act-order.py:179-254`, function `render_order(...)`: builds the RECORD FACE at `:248-253` --
  `RECORD_FACE_MARKER`, `<status>pending</status>`, `<slot>~%s</slot>`, `<fabric>%s</fabric>` -- with NO `<round>`
  element anywhere in the render (confirmed by `grep round` over the file: only the CLI arg name and one prose
  sentence at `:225`, "bounding this DIRECT act; round %s.", which is NOT line-anchored as `<round>...</round>` and
  is correctly never matched by `ROUND_ELEMENT_RE`).
- `.tools/direct-act-order.py:512-535`, `_self_test_no_round_element()`: asserts `"<round>" not in rendered and
  "</round>" not in rendered` on a fixture render. This assertion is UNCHANGED by this cell -- it is still true
  after your edit (you are ADDING an element, not a `<round>` element).
- `.tools/direct-act-order.py:538-580`, `self_test()`: the `arms` list, 10 of 10 passing at this cut.

**RULED, what you build:**

1. **`.tools/to-pipeline-gate.py`** -- add ONE regex constant immediately after `ROUND_ELEMENT_RE` (`:1835`), same
   style:
   ```python
   DIRECT_ACT_ELEMENT_RE = re.compile(r"^[ \t]*<direct_act>\s*true\s*</direct_act>[ \t]*$", re.M)
   ```
   Then change `_round_issuer_violations` (`:1874-1902`) so the missing-`<round>` branch (`:1886-1891`) checks for
   the new element BEFORE refusing:
   ```python
   m = ROUND_ELEMENT_RE.search(text or "")
   if not m:
       if DIRECT_ACT_ELEMENT_RE.search(text or ""):
           return []
       return ["%s: NO line-anchored <round>N</round> element -- ONE ISSUER PER ROUND is keyed to "
               "the ROUND, never the serial (Rule 27; row AMGT_RESAPP-Z-S154), and this limb needs "
               "the key on its own line to enforce it. A prose mention of <round> elsewhere in the "
               "face is not the element. Add '<round>N</round>' naming this order's round, or a "
               "line-anchored '<direct_act>true</direct_act>' declaring this order round-less by "
               "design (row AMGT_RESAPP-Z-W58-S2)." % rel]
   ```
   **The rest of the function is UNCHANGED**: when `<round>` IS present, grading proceeds exactly as today on the
   round-collision branch (`:1892-1901`) -- a `<direct_act>true</direct_act>` element alongside a `<round>` element
   changes NOTHING; the round element is authoritative and the collision check still runs. This is the negative
   control the analysis named ("an order that lies about being a direct act cannot use the marker to dodge
   collision review").
   Then update the docstring comment block above the function (`:1874-1881`) to add one sentence naming the new
   exemption and its row.
   Add FOUR new arms to the `arms` list in the self-test function, immediately after the existing four
   `round-issuer` arms (after the one ending `:934`, before the `# GATE (xi)` comment at `:935`), same style as the
   existing entries:
   ```python
   ("round-issuer GREEN: no <round> but a line-anchored <direct_act>true</direct_act> -> admitted (row AMGT_RESAPP-Z-W58-S2)",
    lambda: _round_issuer_violations(tree, "<direct_act>true</direct_act>\n" + v3, {}) == []),
   ("round-issuer RED: a prose mention of <direct_act>true</direct_act> is inert -- still refused as missing",
    lambda: any("line-anchored" in x for x in
                _round_issuer_violations(tree, "this order sets <direct_act>true</direct_act> nowhere\n" + v3, {}))),
   ("round-issuer RED: <direct_act>false</direct_act> does not exempt -- declares NOT round-less, still refused as missing",
    lambda: any("line-anchored" in x for x in
                _round_issuer_violations(tree, "<direct_act>false</direct_act>\n" + v3, {}))),
   ("round-issuer RED: <round>13</round> together with <direct_act>true</direct_act> does not exempt -- round collision still enforced (an order cannot claim direct-act to dodge collision review)",
    lambda: any("round 13" in x and "S154" in x for x in
                _round_issuer_violations(tree, "<direct_act>true</direct_act>\n<round>13</round>\n" + v3,
                                         {13: ["org/missions/D0/X/X_PRJ/task-orders/X_PRJ.TO-0.md"]}))),
   ```
   Use the EXACT `tree` and `v3` names already bound in that function's scope (read the surrounding arms to confirm
   their values before pasting -- do not redefine them).

2. **`.tools/tests/test_gate_x_round_issuer.py`** -- add TWO new real-index arms after the existing "RED: a new
   order with no `<round>` element" arm (`:173-183`), same style (a real scratch git repo, the gate's own CLI, real
   committed bytes):
   - GREEN: a new order carrying `_order_text(None)` but with `<direct_act>true</direct_act>` spliced in as an
     additional line (extend `_order_text` with an optional `direct_act_line` parameter, default `None`, inserted
     on its own line the same way `round_line` is inserted at `:97-98`; do not change any existing caller's
     behavior -- the default keeps every existing arm byte-identical) -- staged `A`, gate rc tolerant of other
     limbs, `_round_lines(out, rel)` empty (admitted by GATE (x)).
   - RED: the same shape with `<direct_act>false</direct_act>` -- staged `A`, `_round_lines(out, rel)` non-empty,
     containing `"line-anchored"`.
   Update the module docstring's arm table (`:11-25`) to add these two rows, and update `RESULT: %d arm(s) failed
   of %d`'s expected denominator in your own report (it is computed, not hardcoded, so no source change is needed
   there).

3. **`.tools/direct-act-order.py`** -- in `render_order` (`:179-254`), add ONE line to the RECORD FACE, immediately
   after `lines.append("<status>pending</status>")` (`:250`):
   ```python
   lines.append("<direct_act>true</direct_act>")
   ```
   Add ONE new self-test function, immediately after `_self_test_no_round_element` (`:512-535`), same fixture
   shape (copy the fixture call, change only the assertion):
   ```python
   def _self_test_direct_act_element():
       """Row AMGT_RESAPP-Z-W58-S2's repair (GATE (x)'s narrow exemption): a DIRECT act's render must now carry a
       line-anchored <direct_act>true</direct_act> element on its own line, so GATE (x)'s missing-<round> branch
       can read it as an explicit round-less declaration rather than an omission."""
       ... (same fixture call as _self_test_no_round_element, reusing its exact arguments) ...
       return "\n<direct_act>true</direct_act>\n" in rendered or rendered.count("<direct_act>true</direct_act>") == 1
   ```
   Build the fixture call by reusing the identical arguments already written in `_self_test_no_round_element`
   (read them, copy them verbatim into the new function -- do not diverge). Register it in `self_test()`'s `arms`
   list (`:538-580`), immediately after the `"a DIRECT act is UNROUNDED"` arm (`:573-574`):
   ```python
   arms.append(("a DIRECT act declares itself round-less -- the render emits <direct_act>true</direct_act> (row AMGT_RESAPP-Z-W58-S2)",
                _self_test_direct_act_element()))
   ```

**What this cell does NOT change:** the round-collision branch's own text or logic (`:1892-1901`); `ROUND_ELEMENT_RE`
itself; any other GATE limb; `AMGT_RESAPP.TO-AMGT-rk-58.direct-act-minted-order.md` (already `complete`, immutable);
`.tools/tests/test_direct_act_order.py` (no existing assertion there touches round or direct_act text -- confirm
this remains true after your edit; if it does not, that is a STOP-and-row, not a silent extra edit outside
`<paths>`).

**THE VALIDATION BAR (`C-VALIDATION-NAMES`, PRD v0.13 @1699960261 `:1652-1658`):** this is a process cell with no
security population; proven entirely on the tools' own self-tests and the real-index battery, offline, no live AWS
act, no vendor call.

## 2. WHERE THIS CAME FROM

**ROUND 15**, decomposition s.23 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-14 analysis
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round14.md` @93cb6416e4 s.2.1 (`:53-69`) and s.3 (`:101-105`
row R15-T1); the row `AMGT_RESAPP-Z-W58-S2` (carried from round 14's adjudication s.4 item 8 and packet finding 6).
PRD v0.13 @1699960261: no FWD or `C-` contract is touched (process/tooling cell; no PRD addendum this round per the
analysis s.5, "every ruling above is a tool or test fix, not a product contract change").

## 3. SURFACES -- what you may read and write

<paths>
.tools/to-pipeline-gate.py
.tools/direct-act-order.py
.tools/tests/test_gate_x_round_issuer.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~62/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-62.gate-x-direct-act-exemption.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (read `.tools/tests/test_direct_act_order.py`,
  `.tools/owned-paths-validate.py`, `.owned-paths.yaml`, the round-14 packet and analysis freely); this block
  governs WRITES. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~62 <0.9.0_WK_AMGT_RESAPP~62@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every
  `.py` you commit passes `.tools/commit-gate.sh` (py_compile + ds-precommit + ruff py39) inside safe-commit.

## 4. BOUNDS

**NO LIVE AWS ACT, NO DEPLOY, NO VENDOR CALL** -- none is named. PORTAL FROZEN (not your surface). **COLLECTION
STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or freshness checker.** No non-ASCII in anything you
write. **PUSH: never.** Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular, never weaken the round-collision
branch itself and never make the exemption apply to anything but the exact `<direct_act>true</direct_act>` shape.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- the self-test and battery
denominators (85, 10, 4) are re-measured at spawn by AC1/AC3/AC4; they may have moved if a sibling cell landed first.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W62-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-62"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/to-pipeline-gate.py --self-test 2>&1 | tail -30</invocation><expect>the final line reads "RESULT: 0 arm(s) failed of N" with N at least 89 (85 pre-existing plus the 4 new round-issuer arms this cell adds); the 4 new arm names print PASS immediately above the RESULT line, covering: a direct_act-true order with no round admitted; a prose mention of direct_act inert and still refused; direct_act-false not exempting; and a round-collision that also carries direct_act-true still refused on the collision -- zero failed overall</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-62"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/tests/test_gate_x_round_issuer.py 2>&1 | tail -20</invocation><expect>"BATTERY PASS" with "RESULT: 0 arm(s) failed of N" and N at least 6 (4 pre-existing plus the 2 new real-index arms: GREEN direct_act-true with no round admitted through the gate's own CLI on a real staged file; RED direct_act-false with no round refused, the refusal text containing "line-anchored")</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-62"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/direct-act-order.py --self-test 2>&1 | tail -15</invocation><expect>"RESULT: 0 arm(s) failed of N" with N at least 11 (10 pre-existing plus the new arm asserting the render now carries a line-anchored <direct_act>true</direct_act> element); the pre-existing "a DIRECT act is UNROUNDED" arm still PASSES unchanged (you added an element, you did not add a <round> element)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-62"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest .tools/tests/test_direct_act_order.py -q 2>&1 | tail -10</invocation><expect>a final line "N passed" with N unchanged from this file's pre-existing count and 0 failed -- your edit to render_order's RECORD FACE does not break any existing assertion in this file (none of them tests for round or direct_act text; re-confirm that by reading the file before you claim this, not by assumption)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-62"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import io
for f in ('.tools/to-pipeline-gate.py', '.tools/direct-act-order.py', '.tools/tests/test_gate_x_round_issuer.py'):
    py_compile_ok = True
    try:
        compile(io.open(f, encoding='utf-8').read(), f, 'exec')
    except SyntaxError as exc:
        py_compile_ok = False
        print(f, 'SYNTAX ERROR', exc)
    b = io.open(f, 'rb').read()
    print(f, 'compiles', py_compile_ok, 'non_ascii_bytes', len(b) - len(b.decode('utf-8')), 'crlf', b.count(b'\r\n'))
"</invocation><expect>all three files print compiles True, non_ascii_bytes 0 (pure ASCII) and crlf 0 (LF only) -- the two edited tool files and the one edited test file are syntactically valid and carry no non-ASCII or CRLF this cell introduced</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~62/AMGT_RESAPP.TO-AMGT-rk-62.gate-x-direct-act-exemption.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, naming the four self-test/battery denominators you
measured (85->89, 10->11, 4->6, and AC4's pytest count), so the next round can cite them without re-deriving.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>15</round>
<slot>~62</slot>
<fabric>site-z</fabric>
