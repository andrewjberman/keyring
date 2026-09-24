# AMGT_RESAPP task order -- `AMGT-rk-69` -- the L10 acceptance sweep reads each order's REAL `<proof_of_spec>` block: `_PROOF_BLOCK_RE` is line-anchored the way `_ORDER_ROUND_RE` already anchors `<round>`, so a prose mention of the tag earlier in an order can no longer swallow its criteria (row S176; rk-58's 5 criteria recovered, round 14 reads 165 of 31)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-69</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~69</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits one repository gate tool and its test; it arms no cron,
  alarm, monitor or cadence, reads no schedule and writes none.
comp-iam: DECLARED-NOT-APPLICABLE -- NO live AWS act: the sweep reads git-tracked order and proof-instance files only.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~69`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~69;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.

## 1. THE CELL, inlined in full -- `AMGT-rk-69` (R17 S176-anchor; row `AMGT_RESAPP-Z-S176`; process)

**The ruling, verbatim (`1.0.0_SA_CTO~Z` msg 23928, and `ledger/ROUND16_CTO_RULINGS_20260921.md` s.2a @006dd1e344):**
*"row S176 (my own disarm_owner) is a real, independently-verified defect -- surprise-row-gate.py:1180 _PROOF_BLOCK_RE is
unanchored and binds to a PROSE mention of <proof_of_spec> in rk-58's order text (line 80, in backticks) before the
real block at :191-241, undercounting criteria (160/30 vs true 165/31). ... Under the R4 ruling you both just landed,
the acceptance sweep is now load-bearing for L10 admissibility ... Fix shape: anchor _PROOF_BLOCK_RE the way
_order_round already anchors <round> (:1203-1206). Proof: --acceptance --round 14 reads 165/31 post-fix, existing suite
green."* Deferred from round 16 to round 17 by msg 23931 (no late order into an issued round); cleared to cut by the
round-16 analysis (`ledger/ROUND_ANALYSIS.round16.md` @cc3657503f, msg 23938).

**THE MEASURED STATE, at HEAD `1764686f10` (cite these lines; RE-READ at your branch HEAD before editing):**
- `.tools/surprise-row-gate.py` (3122 lines): `:1180` `_PROOF_BLOCK_RE = re.compile(r"<proof_of_spec>(.*?)</proof_of_spec>", re.S)`
  -- unanchored; `:1184` `_ORDER_ROUND_RE = re.compile(r"^\s*<round>\s*([0-9]+)\s*</round>", re.M)` -- the anchoring
  pattern to follow; `:1187-1200` `_order_criteria(text)` searches the FIRST match (`:1191`) and FALLS BACK to the whole
  text when no block tag is found (`:1192`); `:1203-1206` `_order_round`.
- **Sweep baseline, measured by the issuer:** `python .tools/surprise-row-gate.py --acceptance AMGT_RESAPP --round 14`
  -> `PASS 126 / FAIL 1 / UNVERIFIABLE 33 of 160 criteria over 30 order(s); unrounded 0`.
- **POPULATION CENSUS, measured by the issuer over EVERY one of the 135 AMGT_RESAPP tree orders** (script
  `.scratch/r17_census_proof_block.py` in the issuer's tree -- the anchored pattern
  `^[ \t]*<proof_of_spec>[ \t]*$(.*?)^[ \t]*</proof_of_spec>` with `re.M | re.S` against the current one):
  `same position 134 | naive binds earlier (prose) 1 | anchored MISSES a block 0 | anchored-only 0 | no block 0`; the
  one difference is `AMGT_RESAPP.TO-AMGT-rk-58.direct-act-minted-order.md` -- criteria naive 0, anchored 5. **So an
  opening-and-closing-tag line anchor is SAFE across the whole population (it loses no real block) and fixes exactly
  the known case.** 134 + 1 = 135.
- `.tools/tests/test_acceptance_sweep.py`: `RESULT: 0 arm(s) failed of 7`, `BATTERY PASS` at the cut.

**ISSUER RULE -- THE SHELL EATS `$(` INSIDE A DOUBLE-QUOTED `python -c` (measured at this cut, against this seat's
own first census):** an inline regex containing `$(` in `python -c "..."` is COMMAND SUBSTITUTION to bash -- `.*?`
globbed to `.claude`, the shell printed `.claude: command not found`, substituted an EMPTY STRING, and the "anchored"
regex silently lost its body, so the census reported 135 of 135 missed. **Any criterion or probe you write that
contains `$` in a regex runs from a SCRIPT FILE (Write tool, then `python <file>`) or imports the compiled pattern from
the module -- never an inline double-quoted regex.** The criteria below follow this rule.

**RULED, what you build:**
1. **`.tools/surprise-row-gate.py:1180`** -- line-anchor BOTH the opening and the closing tag:
   `_PROOF_BLOCK_RE = re.compile(r"^[ \t]*<proof_of_spec>[ \t]*$(.*?)^[ \t]*</proof_of_spec>", re.M | re.S)`
   (the exact pattern the issuer's census validated on 135 of 135 orders). A prose mention on a line with other text --
   backticked, mid-sentence -- is no longer the block. **`_order_criteria`'s whole-text fallback (`:1192`) STAYS**
   (a malformed order still yields what it can); add one sentence to its docstring naming the anchoring and row S176.
2. **`.tools/tests/test_acceptance_sweep.py`** -- append arms (no existing arm edited): (a) a fixture order whose prose
   names `` `<proof_of_spec>` `` inline BEFORE its real block of 3 criteria -> `_order_criteria` returns all 3 (HEAD's
   pattern returns the prose span's 0 -- prove it on HEAD's copy loaded from `git show HEAD:.tools/surprise-row-gate.py`
   into a temp file, as the discriminating arm); (b) a normal order (block only) -> unchanged count; (c) an order with
   NO block tag -> the whole-text fallback still yields its criteria (the fallback is preserved).

**What this cell does NOT change:** `_ORDER_ROUND_RE`, `_order_round`, the sweep's classification of PASS / FAIL /
UNVERIFIABLE, any other limb of the gate, any order file. **Other parsers of `<proof_of_spec>` exist** (`.tools/to-pipeline-gate.py`,
`.tools/proof-of-spec-check.py`, `.tools/direct-act-order.py`) -- WALLS for this cell; if you find one carries the same
unanchored shape, file a ROW naming file:line and keep working.

## 2. WHERE THIS CAME FROM

**ROUND 17**, decomposition s.25 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s round-16 analysis
`ledger/ROUND_ANALYSIS.round16.md` @cc3657503f (msg 23938: *"round 17 is cleared to cut -- one cell, S176-anchor"*)
and s.3 @1764686f10 (msg 23943: W38-S5 rides round 17 too); the ruling s.2a @006dd1e344 (msg 23928); the CVO's R4
ruling @335faf48fe (terminality and acceptance are two axes -- why the sweep is now load-bearing). Row
`AMGT_RESAPP-Z-S176` (disarm owner `1.0.0_SA_CTO~Z`). Andrew-direct ~15:12Z (record @1e2a54bf0f): this round's two
orders are written together and issued in one commit.

## 3. SURFACES -- what you may read and write

<paths>
.tools/surprise-row-gate.py
.tools/tests/test_acceptance_sweep.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~69/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-69.acceptance-sweep-anchored-proof-block.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant. Scratch is `<your worktree>/.scratch/` only.
  Collision check at the cut: the sibling round-17 cell `AMGT-rk-70` writes `integrations/bloomberg/research/model_block_pull.py`
  and its test only; the held branch `wk-amgt-14-50` touches neither of your code paths.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~69 <0.9.0_WK_AMGT_RESAPP~69@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`.
  **NOTE: `.tools/surprise-row-gate.py` IS ITSELF A COMMIT GATE** that safe-commit runs on your commit -- your edited
  copy grades your own commit. If it refuses for a reason your edit caused, that is a real defect in your edit: fix it
  within this order's rule or REFUSE with a row; never bypass.

## 4. BOUNDS

**NO LIVE AWS ACT, NO DEPLOY, NO VENDOR CALL.** PORTAL FROZEN. **COLLECTION STAYS OFF.** **NO alarm, monitor,
SNS/SES-send, notification or freshness checker.** No non-ASCII in anything you write. **PUSH: never** (LD-0522).
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular never by removing the whole-text
fallback and never by editing a WALL parser.
**A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator** -- 160/30 (round 14), 135 orders, 7 battery arms are the
issuer's measurements; re-measure them before you edit (a round-16 or round-17 merge may have added orders).
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W69-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`; append by
textual splice inside the one fenced JSON array; never edit an existing row. A pure disarm row, if you file one, sets
`"disposition": "DISMISSED_WITH_REASON"`, never `GRADUATED` (the round-16 analysis's disarm-record contract).

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-69"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/surprise-row-gate.py --acceptance AMGT_RESAPP --round 14 2>&1 | grep -o 'PASS [0-9]* / FAIL [0-9]* / UNVERIFIABLE [0-9]* of [0-9]* criteria over [0-9]* order(s)'</invocation><expect>"PASS 131 / FAIL 1 / UNVERIFIABLE 33 of 165 criteria over 31 order(s)" -- MEASURED BY THE ISSUER AT THE CUT, not predicted: a scratch copy of the gate with exactly this order's ruled pattern substituted at :1180 printed that line for round 14 (HEAD's copy printed "PASS 126 / FAIL 1 / UNVERIFIABLE 33 of 160 criteria over 30 order(s)"), and none of rk-58's five recovered criteria appeared in the FAIL or UNVERIFIABLE lists -- all five PASS. Re-measure the HEAD line at spawn; if it has moved (a later order landed), the bar is HEAD's line plus exactly rk-58's 5 criteria and 1 order, all five PASS</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-69"><invocation>cd "$(git rev-parse --show-toplevel)" && python .tools/tests/test_acceptance_sweep.py 2>&1 | tail -6</invocation><expect>"BATTERY PASS" and "RESULT: 0 arm(s) failed of N" with N equal to the spawn-time count (7 at the cut) plus the arms you appended (at least 3: a-c of section 1 item 2), including the discriminating arm that shows HEAD's pattern returns 0 criteria for the prose-first fixture while the new pattern returns 3</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-69"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import glob, importlib.util; s = importlib.util.spec_from_file_location("srg", ".tools/surprise-row-gate.py"); g = importlib.util.module_from_spec(s); s.loader.exec_module(g); fs = sorted(glob.glob("org/missions/D5/AMGT/AMGT_RESAPP/task-orders/*.md")); lost = [f for f in fs if len(g._order_criteria(open(f, encoding="utf-8").read())) == 0]; print("orders", len(fs), "orders_with_zero_criteria", len(lost), [f.replace(chr(92), "/").rsplit("/", 1)[-1][:50] for f in lost]); print("pattern_is_line_anchored", g._PROOF_BLOCK_RE.pattern.startswith("^") and bool(g._PROOF_BLOCK_RE.flags & 8))'</invocation><expect>orders N (135 at the cut, re-measured) with orders_with_zero_criteria 0 [] -- every tree order yields its criteria through the EDITED sweep's own _order_criteria (at HEAD rk-58 yields 0); pattern_is_line_anchored True (re.M is flag 8). Note this invocation is single-quoted and imports the compiled pattern -- the ISSUER RULE in section 1</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-69"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import io, subprocess; base = subprocess.run(["git", "merge-base", "HEAD", "SITEZ"], capture_output=True, text=True).stdout.strip(); [print(f, "compiles", bool(compile(io.open(f, "rb").read().decode("utf-8"), f, "exec")), "crlf", io.open(f, "rb").read().count(b"\r\n"), "non_ascii_bytes", len(io.open(f, "rb").read()) - len(io.open(f, "rb").read().decode("utf-8")), "| base", len(subprocess.run(["git", "show", base + ":" + f], capture_output=True).stdout) - len(subprocess.run(["git", "show", base + ":" + f], capture_output=True).stdout.decode("utf-8"))) for f in (".tools/surprise-row-gate.py", ".tools/tests/test_acceptance_sweep.py")]'</invocation><expect>both files print compiles True, crlf 0, and a non_ascii_bytes figure EQUAL to its base figure printed beside it (the bar is "this cell added none", read from the merge-base, never an assumed literal)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~69/AMGT_RESAPP.TO-AMGT-rk-69.acceptance-sweep-anchored-proof-block.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, naming AC1's full line and the class each of rk-58's five
recovered criteria landed in.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>17</round>
<slot>~69</slot>
<fabric>site-z</fabric>
