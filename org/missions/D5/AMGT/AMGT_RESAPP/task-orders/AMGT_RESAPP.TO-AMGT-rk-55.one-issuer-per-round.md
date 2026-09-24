# AMGT_RESAPP task order -- `AMGT-rk-55` -- ONE ISSUER PER ROUND, keyed to the ROUND: the L6 gate refuses a second issuance into a round that already has one at HEAD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-55</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~55</issued_to>
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

**You are `0.9.0_WK_AMGT_RESAPP~55`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~55;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-55` (R14-T1; process; row `AMGT_RESAPP-Z-S154`)

**The analysis row (`ROUND_ANALYSIS.round13.md` s.4 @9c8e04cd9a, row R14-T1 `:141`):** *"S154 (s.3.1)"* -- process;
co-sign no. **The ruling, s.3.1 (`:67-70`), verbatim:** *"One issuer per round (S154, OPEN). RULED: a TOOL cell,
keyed to the round. Round 13 was issued twice by two continuations of one seat serial. A refusal keyed to the
SERIAL cannot see it; the L6 gate refuses a second issuance into a round that already has one, keyed to the ROUND.
If a collision happens anyway, the SECOND issuance is withdrawn and its orders re-cut into the first by its
issuer."*

**The row, inlined (`INVESTIGATION_v1.md`, id `AMGT_RESAPP-Z-S154`, surfaced by `2.0.0_SA_COO~Z` 2026-09-17
15:35Z, class OBSERVATION).** `spec_asserts`: *"CLAUDE.md: 'ONE ISSUER PER ROUND ... two instances issuing into
the SAME round is the collision (two cuts, two issuances, an ambiguous L8)' -- this row is that clause
materializing in real time, between two continuations of the SAME seat identity rather than two different seats,
which the rule's text does not distinguish."* `world_is`: *"Two issuances of round 13 exist (f0cbb2d813 and
7acf65b08b) and two worker generations are executing concurrently; no mechanism available to THIS session can stop
a subagent already backgrounded, nor message a running worker, nor recall a completed one. The only lever this
session actually holds is NOT CONTINUING its own four still-running workers past their current single order when
each next reports, and NOT spawning chain A or chain D from the superseded (first) issuance -- both adopted as of
this row. Whether the OTHER continuation's session holds an equivalent lever over its own seven workers is not
observable from here."* The row's own evidence: both issuances were committed under the SAME author serial
(`2.0.0_SA_COO~Z`), so GATE (iv) (`_issuer_identity_violations`, `to-pipeline-gate.py:225-239`), which grades WHO
commits, passed both.

**THE MEASURED STATE, at HEAD (`.tools/to-pipeline-gate.py` last moved @458fbb65ba, 2834 lines; cite these lines):**
- `main()` `:2712-2826` grades the NEWLY-ADDED set (`_newly_added()` `:1757-1782`: staged `A` and `R` paths) through
  `check_file()` `:2402-2505`, then the set-level carriers `_coverage_violations` (`:537`, ONE issuance covers
  EVERY cell) and `_carrier2_violations` (`:553`, the project row reads EXECUTING). **No limb reads the ROUND.**
  Nothing in the file matches `<round>`: a second commit adding tree orders into a round that already has orders
  at HEAD passes every limb, as it did twice on 2026-09-17.
- The RECORD FACE already carries the key: `<round>N</round>` on its own line (the rk-22 template, the rk-19
  order). Census at the cut over `org/missions/D5/AMGT/AMGT_RESAPP/task-orders/*.md`: 97 orders, 94 carry a
  `<round>` element, 3 carry none, 12 carry `<round>13</round>` (re-measure at spawn; AC3 prints it).
- The merge exemption (`:2718-2750`) exempts a MERGE commit from every task-order limb, deliberately; a merge is
  not an issuance and this limb inherits that exemption unchanged.
- The audited escape exists: `# pipeline-override: <reason>` (`OVERRIDE_RE`, honoured at `:2412-2434`, written to
  `org/to-pipeline-override-audit.log`). It is the ONLY path for a genuinely additional order into an open round
  and this cell adds no second escape.
- The gate's self-test is `_self_test()` `:665` (pure arms, no repo read; the `arms` list at `:695`); the
  real-index batteries live in `.tools/tests/` (`test_gate_viii_modify.py` is the pattern: a scratch git repo,
  the gate's own CLI, real order bytes, RED and GREEN arms, exit 0/1).

**RULED, what you build:**
1. **GATE (x) -- the round-issuer limb, keyed to the ROUND.** In `to-pipeline-gate.py`, a pure function
   `_round_issuer_violations(rel, text, head_rounds)` where `head_rounds` is `{round_number: [order paths]}` for the
   project's TREE orders TRACKED AT HEAD (read with `git ls-files` + `git show HEAD:<path>`, never the worktree; the
   census cached once per gate run, like `_open_tos_census`'s cache in the sibling gate). For a NEWLY-ADDED tree
   order: (a) no line-anchored `<round>N</round>` element -> REFUSED naming the missing key; (b) its round N already
   has one or more orders at HEAD -> REFUSED: *"round N of <CODE> already has an issuance at HEAD (M order(s): ...);
   ONE ISSUER PER ROUND is keyed to the ROUND, never the serial (Rule 27; row AMGT_RESAPP-Z-S154). A re-cut into
   the first issuance MODIFIES its orders and adds no file; a genuinely additional order into an open round takes
   the audited '# pipeline-override: <reason>'."* Flat-root orders are not graded (the legacy population). The
   limb runs in `main()` over the newly-added targets beside the coverage carrier, and the refusal counts every
   colliding file in ONE message so the issuer sees the whole set. A modification (`M`) is never graded -- a
   worker's status flip and a COO re-cut of an existing order are modifications by construction.
2. **The regex is line-anchored:** `^[ \t]*<round>\s*([0-9]+)\s*</round>[ \t]*$` (multiline), the same discipline
   as `PLACEHOLDERS_TAG_RE` `:165` -- a prose mention of `<round>` in a worker face is inert.
3. **`--rounds <CODE>`, a read-only CLI limb** (beside `--sweep`): prints, for the project's tree orders at HEAD,
   `rounds` -> order count, the unrounded count, and the denominator (`N order(s) at HEAD`), rc 0 always. It is the
   read the COO runs before an issuance and the one AC3 records.
4. **Self-test arms** in `_self_test()` (pure, RED/GREEN: collision refused; next round admitted; missing key
   refused; flat-root not graded; a prose `<round>` mention not read as the key), and a real-index battery
   `.tools/tests/test_gate_x_round_issuer.py` in the `test_gate_viii_modify.py` shape: a scratch repo where one
   order with `<round>13</round>` is COMMITTED under author `2.0.0_SA_COO~Z`, then (RED) a second file with
   `<round>13</round>` staged under the SAME author is refused at rc 1 with the message naming round 13 and S154;
   (GREEN) a file with `<round>14</round>` staged is admitted by THIS limb (other limbs' output tolerated and
   named); (GREEN) the committed round-13 order staged as MODIFIED (status flip) is not graded; (RED) a new order
   with no `<round>` element is refused naming the missing key. The battery prints `RESULT: %d arm(s) failed of
   %d` and `BATTERY PASS`.

**What this cell does NOT change:** GATE (iv) (who commits) stays; the merge exemption stays; the override stays
singular and audited; no order at HEAD is back-filled with a `<round>`; nothing in the spine or CLAUDE.md is
edited (the law already says ONE ISSUER PER ROUND -- this is its mechanism); `AMGT-rk-56`'s `<status>` limb is a
sibling limb in the same function and is NOT built here.

**THE VALIDATION BAR (`C-VALIDATION-NAMES`, PRD `:1652-1658`):** a gate cell is proven on planted orders in a
scratch repo and on a READ of this project's own orders at HEAD; it runs no producer and touches no name.

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.22 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round13.md` @9c8e04cd9a s.3.1 (`:67-70`) and s.4 row R14-T1
(`:141`); the row `AMGT_RESAPP-Z-S154` (INVESTIGATION_v1.md `:7795-7815`). CLAUDE.md Rule 27, *"ONE ISSUER PER
ROUND -- and a WORKSTREAM IS A SCOPE, NOT A ROUND"*. PRD v0.13 @1699960261 is not moved by this cell (a process
cell; `C-VALIDATION-NAMES` `:1652-1658` binds its proof).

## 3. SURFACES -- what you may read and write

<paths>
.tools/to-pipeline-gate.py
.tools/tests/test_gate_x_round_issuer.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~55/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-55.one-issuer-per-round.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (read `.tools/surprise-row-gate.py`
  `:1125-1165` for the HEAD-census shape, `.tools/tests/test_gate_viii_modify.py` for the battery shape,
  `.tools/git-hooks/to-proof-of-spec-check.sh` to see what the sibling hook already refuses). Scratch is
  `<your worktree>/.scratch/` only; the battery's scratch repos live under `.scratch/` and are removed at its end.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~55 <0.9.0_WK_AMGT_RESAPP~55@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. Every
  `.py` edit passes `.tools/commit-gate.sh` (py_compile + ds-precommit + ruff py39). No non-ASCII in the gate
  file's new lines (the file already carries non-ASCII in comments; add none).
- **THE GATE YOU EDIT GRADES YOUR OWN COMMIT:** your status flip on this order is a MODIFY (not graded by the new
  limb); confirm with a dry run of the gate on your staged set before committing.

## 4. BOUNDS

**NO new approval gate** -- this limb is the mechanism of a rule CLAUDE.md already states and the CTO ruled; it
refuses exactly the act S154 measured and nothing wider. **The override stays the existing audited one**; do not
add a second token. **NO back-fill**: the 3 unrounded orders at HEAD are left as they are (the limb grades
NEWLY-ADDED only). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or freshness
checker.** No vendor call. No non-ASCII in anything you write. **PUSH: never.**
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- 97 orders / 94 rounded / 12 in
round 13 are the cut's figures; AC3 re-measures them at spawn.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W55-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-55"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/to-pipeline-gate.py --self-test 2>&1 | tail -40; echo rc=${PIPESTATUS[0]}</invocation><expect>rc=0 and the printed arm list carries at least FIVE arms whose names begin "round-issuer" (collision refused naming the round and S154; next round admitted; missing key refused; flat-root not graded; a prose mention of the element not read as the key), every arm PASS -- the self-test is pure and reads no repo</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-55"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/tests/test_gate_x_round_issuer.py 2>&1 | tail -30; echo rc=${PIPESTATUS[0]}</invocation><expect>rc=0, a line "RESULT: 0 arm(s) failed of N" with N at least 4 and "BATTERY PASS": in a scratch git repo under .scratch/, an order with round 13 COMMITTED under author 2.0.0_SA_COO~Z, then a SECOND round-13 file staged under the SAME author is REFUSED by the gate's own CLI at rc 1 with a message naming "round 13" and "S154" (the serial-blind case S154 measured); a round-14 file is ADMITTED by this limb; the committed order staged as MODIFIED (a status flip) is NOT graded by it; a new order with no round element is REFUSED naming the missing key; the scratch repo is removed at the end</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-55"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/to-pipeline-gate.py --rounds AMGT_RESAPP; echo rc=$?</invocation><expect>rc=0 and a read-only census of this project's tree orders AT HEAD: one line per round with its order count (round 13 reading 12 at the cut), the unrounded count (3 at the cut) and the denominator "97 order(s) at HEAD" (re-measure; the numbers may have moved with round 14's issuance) -- the read the COO runs before cutting a round</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-55"><invocation>cd "$(git rev-parse --show-toplevel)" && src=$(ls org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-19.adapter-second-join.md) && probe=org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-19.zz-round-probe.md && cp "$src" "$probe" && git add "$probe" && python .tools/to-pipeline-gate.py "$probe" 2>&1 | grep -c "already has an issuance at HEAD"; git reset -q -- "$probe"; rm -f "$probe"; echo probe_removed=$([ -f "$probe" ] && echo no || echo yes)</invocation><expect>the count line reads 1 or more -- a real round-13 order copied under a new name and STAGED (never committed) in this worktree is refused by the live gate with the round-collision message naming round 13 and its existing orders -- and probe_removed=yes with the index restored (git status shows no probe path); the other limbs' refusals on the same probe (cell_refs, sign-off) may print beside it and are recorded, not counted</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on
this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~55/AMGT_RESAPP.TO-AMGT-rk-55.one-issuer-per-round.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, and say in the report that every round-14 order must
be issued in ONE commit from now on -- a second commit into round 14 is what this limb refuses.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~55</slot>
<fabric>site-z</fabric>
