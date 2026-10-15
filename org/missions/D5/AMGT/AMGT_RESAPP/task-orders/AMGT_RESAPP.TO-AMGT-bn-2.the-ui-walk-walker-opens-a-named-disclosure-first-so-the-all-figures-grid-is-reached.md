# AMGT_RESAPP task order -- `AMGT-bn-2` -- THE UI-WALK WALKER OPENS A NAMED DISCLOSURE FIRST (`--open-first "All figures"`), SO THE SECURITY ANALYSIS MODEL TAB'S ALL-FIGURES GRID IS REACHED, PROVED BY ONE REAL ONE-NAME WALK

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bn-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~472</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bn-2.the-ui-walk-walker-opens-a-named-disclosure-first-so-the-all-figures-grid-is-reached</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a tool change and one walk; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms and disarms the dormant UI-walker account itself under its own lease (`.claude/skills/ui-walk`); no grant, key or policy is touched by this order.
comp-adversary: RUN at the cut -- `r107_walker_open_first_check.mjs` reads `NO (0 of 2 arms)` against the unchanged tree (the helper module is absent) and `YES (8 of 8 arms)` against a temporary reference implementation of the contract (a green control, read here and then discarded).
EGRESS CLASS, declared: the dev server's reads of the live services through the deployed front door (GET/HEAD/OPTIONS only: the walker's own network guard aborts any other request); the check script reads files only.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-472` (branch `wk-AMGT_RESAPP-472`, cut from the issuance commit at the GO). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-472`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bn-2` (round 107, decomposition s.116)

**Why.** The walker (`.claude/skills/ui-walk/walk.mjs`) walks Security Analysis names tab by tab; on each tab `exploreScope()` (about line 314) clicks the first closed `<details> > <summary>` it finds, up to 20 clicks, in page order. On a Model tab the What Changed table carries 26 `Full figures` disclosures BEFORE the `All figures` disclosure (the 27th closed `<details>`), so the cap is spent and the All-figures grid is never opened: round 106's walk could not exercise the grid (the CTO's item 2 of round 107).

**The change.**
1. A new pure module `.claude/skills/ui-walk/open_first.mjs` exporting `orderSummaries(texts, openFirst)`. Its contract is fixed by the check file `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_walker_open_first_check.mjs` (read it first; its header states the contract and its 8 arms are AC1). In words: it returns an array of indices, a permutation of `0..texts.length-1`; an index whose text, trimmed and lower-cased, equals an `openFirst` entry (trimmed, lower-cased) comes before every other index; matching indices follow the order of their entries in `openFirst`, then original index; every other index follows in original order; empty or absent `openFirst` returns the identity order; an entry matching nothing changes nothing and does not throw.
2. `walk.mjs` gains the repeatable option `--open-first <summary text>` (parsed beside the other options, documented in the file's usage comment, and one line in `.claude/skills/ui-walk/SKILL.md`). In `exploreScope()` the closed-summary expansion uses `orderSummaries(...)` over the closed summaries' texts, so an `--open-first` entry is clicked FIRST, before the 20-click cap is spent; the cap of 20 and the `DO_NOT_CLICK` refusal stay exactly as they are. Because each click removes a summary from the `details:not([open])` set, click by the entry's TEXT (the first still-closed summary with that text), not by a stale index.
3. A log line per entry per scope. When an entry is clicked: `OPEN-FIRST "<text>": opened (<n> table row(s) visible inside it)`, where `<n>` is the count of visible `tr` elements inside the `<details>` that was opened, read after the page settles. When no closed summary with that text exists in the scope: `OPEN-FIRST "<text>": not found in <label>` (`<label>` is the scope's own label, e.g. `SHOP CN-Model`). Not found is not an error.
4. With NO `--open-first` the walker behaves exactly as today: the same clicks in the same order.

Edit only `.claude/skills/ui-walk/` (the new module, `walk.mjs`, `SKILL.md`). Do not edit anything else of the walker's behaviour, the page, or any product file.

**The build under walk (AC2)** is started by the ISSUER at the GO from your nested portal worktree (`C:/dev/wk-resapp-472/portal`, cut at PROD `e0b43076`) with `bun run dev:live --port 5174`. DO NOT start, stop or restart it; check `curl -s -o /dev/null -w "%{http_code}" http://localhost:5174/` reads 200 before the walk and if it does not, STOP and file a BLOCKING row (never use another port: portal dev builds use 5174 ONLY).

**Do this in order.** (1) Run AC1 once on the unchanged tree: it must print `NO`; record that run. (2) Write `open_first.mjs`, then the `walk.mjs` edit, then the `SKILL.md` line. (3) Run AC1 again: `YES (8 of 8 arms)`. (4) Run AC2, the one real walk. A walk that prints `HELD by` instead of `ARMED` means the walker's account lease is taken: wait 60 seconds (`sleep 60`), run `python .claude/skills/ui-walk/ui_walker_account.py status`, retry once the status reads `armed=no`; never `disarm` a holder that is not yours; a third failure is a BLOCKING row. A walk whose log reads `ERROR login did not complete (still on /login)` has disarmed itself: run THAT SAME walk once more; a second failure is a BLOCKING row. If a walk dies midway, run `python .claude/skills/ui-walk/ui_walker_account.py status`, and only if it reads `armed=yes` with YOUR holder, `disarm <holder>`. (5) Copy the walk's output folder `tmp/ui-walk/<stamp>` to `C:/dev/ui-walk-evidence/bn-2/` (outside the repository). NEVER commit a screenshot, never paste one into a message. (6) READ with the Read tool the first shot after the `All figures` click (the Model-expanded shot of SHOP CN) and say in one line whether a grid of rows is visible on it. (7) Git Bash rewrites a leading `/` argument into a Windows path (measured: `--route C:/Program Files/Git/security-analysis` voided a walk): the walk invocation carries `MSYS_NO_PATHCONV=1`; if the walk's first lines show a `--route` that is not `/security-analysis`, kill nothing, disarm nothing you do not hold, and file a BLOCKING row.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Edit only the three files named in the change. Read-only against the world: the walker's guard aborts every request that is not GET/HEAD/OPTIONS or its own sign-in; you write nothing to S3, DynamoDB or the function. No push of shared branches. No `pip install`. Port 5174 only.
2. Your files: `.claude/skills/ui-walk/` as above, your deliverables folder, and `C:/dev/ui-walk-evidence/bn-2/`.

## 3. SURFACES

<paths>
.claude/skills/ui-walk/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~472/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bn-2"><invocation>cd C:/dev/wk-resapp-472 &amp;&amp; node "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_walker_open_first_check.mjs" C:/dev/wk-resapp-472; echo "exit=$?"</invocation><expect>the line `R107 WALKER OPEN-FIRST: YES (8 of 8 arms)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bn-2"><invocation>cd C:/dev/wk-resapp-472 &amp;&amp; MSYS_NO_PATHCONV=1 timeout 590 node ".claude/skills/ui-walk/walk.mjs" --route /security-analysis --security "SHOP CN" --open-first "All figures" --max-minutes 8 > "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~472/walk_seam.txt" 2>&amp;1; echo "exit=$?"; grep -n "OPEN-FIRST" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~472/walk_seam.txt"; tail -4 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~472/walk_seam.txt"</invocation><expect>`exit=0`; a line `OPEN-FIRST "All figures": opened (N table row(s) visible inside it)` with N at least 5 (from the `SHOP CN-Model` scope); and in the last lines `OK: DISARMED` and `SUMMARY: ... walk void: no`</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~472 <0.9.0_WK_AMGT_RESAPP~472@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~472/AMGT_RESAPP.TO-AMGT-bn-2.the-ui-walk-walker-opens-a-named-disclosure-first-so-the-all-figures-grid-is-reached.proof_of_spec.json` with `to_id` equal to the `<to_id>` line above, character for character; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters; if the checker refuses the instance for a missing `decomp_ref`, add it from the order's own `<decomp_ref>` block. Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.

Report once:
- the commit hash;
- AC1's run before the edit (the NO line) and after, and AC2's output lines;
- the one line from step 6 (is a grid of rows visible);
- the diff stat of `walk.mjs` and the three lines of `walk.mjs` that parse the option and call `orderSummaries`;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msg 6249 section 2 item 2: one browser walk that opens the All-figures grid on the release build. Measured at the cut: the 2026-10-15 walk (round 106, bm-5) shows `All figures` collapsed in `040-SHOP-CN-Model-expanded.png` because `exploreScope()` caps at 20 closed `<details>` and the What Changed table's 26 `Full figures` precede it (the 27th). The walker is a shared tool (`.claude/skills/ui-walk/`); this cell changes it additively, behind a new flag, with a pure helper so the ordering is testable without a browser. `AMGT-bn-4` (the ten-name walk on the promoted build) runs the merged walker with `--open-first "All figures"`; this cell's own walk is on PROD `e0b43076`, which already carries the grid. A tool edit and the evidence walk are different cells on purpose (round 106's bm-5 bounds read "do not edit the walker"). The worktree is cut with `--sparse-add .claude/skills/ui-walk` (round 106's `W443-S1`: a sparse checkout omitted the walker folder).

<status>pending</status>
<round>107</round>
<slot>0.9.0_WK_AMGT_RESAPP~472</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
