# AMGT_RESAPP task order -- `AMGT-bn-4` -- THE FRESH-DRAW TEN-NAME BROWSER WALK, PLUS TWO NAMED RE-TEST NAMES, WITH THE ALL-FIGURES GRID OPENED, ON A LOCAL BUILD OF PROD THAT CARRIES THE TEAM ESTIMATE MARK (A WALK RUN) -- STAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bn-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~474</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bn-4.the-fresh-draw-walk-with-the-all-figures-grid-open-on-a-local-build-of-prod</to_id>
<placeholders>NONE</placeholders>
<workstream>WALK</workstream>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot walk; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms and disarms the dormant UI-walker account itself under its own lease (`.claude/skills/ui-walk`); no grant, key or policy is touched by this order.
comp-adversary: RUN at the cut -- `r103_walk_draw.py --census round106/census_v5.json --date 2026-10-16` reads `R103 WALK DRAW: 10 of 93 drawn (date 2026-10-16)` and shares exactly ONE name with round 106's draw of 2026-10-15 (OMAB MM; the other nine differ); five of its ten (ZURN SW, 939 HK, ICT PM, 1299 HK, NOVN SW) are among the 20 names whose forward P/E the served block withholds; the walker's `--open-first` flag was merged at `21a23e0a80` (`AMGT-bn-2`: one real walk opened the All-figures grid, 193 visible rows); the walker was walked by the issuer on the candidate build earlier today.
EGRESS CLASS, declared: the dev server's reads of the live services through the deployed front door (GET/HEAD/OPTIONS only: the walker's own network guard aborts any other request).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-474` (branch `wk-AMGT_RESAPP-474`, cut from the issuance commit at the GO). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-474`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bn-4` (round 107, decomposition s.116)

FWD-40 (a) and (d) of PRD v0.44 (ratified text, inlined for (d)):

```
(d) a browser walk of 10 names on a LOCAL build of the
                    PROD release commit (`bun run dev:live --port 5174`,
                    which reaches the live services whatever a box's
                    `.env.local` says), screenshots read (the estate's walker
                    refuses a non-localhost base). The draw: the 93 keys
                    sorted by sha256(walk date + ' ' + key), the first ten,
                    the draw printed with the walk
```

The CTO's round-106 analysis (`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round106.md`): bm-5 AC5 (round 106) was graded NOT MET because change 3 did not show on SHOP CN and change 2 (the All-figures grid) was never opened. Round 107 changed two things on the page and the walker; the CTO re-grades both at THIS walk. The walk date is **2026-10-16** (round 106's draw was 2026-10-15). The walk names are the ten of the fresh draw PLUS two NAMED re-test names, `SHOP CN` and `PBR US`, the two cases that exposed the defect; the issuer adds them to the ten (the FWD-40 (d) draw is unchanged).
1. **A Key Figures P/E cell that the page fills from the research team's sheet, where the vendor ratio is withheld, prints a visible `research team estimate` line** (`AMGT-bn-1`, PROD `e0e69da7`, portal-v2.1.227). Expected on `SHOP CN`: 2025 `74x-193.1x`, 2026E `67.8x`, 2027E `53.0x` each carry the line; on `PBR US`: 2026E `5.9x` and 2027E `6.1x` each carry it and its 2025 range `3.6x-5x` does NOT (nothing is withheld there; the CTO ruled that correct). The vendor figure never prints once withheld. Five of the ten drawn names are withheld names (ZURN SW, 939 HK, ICT PM, 1299 HK, NOVN SW).
2. **The Model tab's All-figures grid is OPENED by the walker** (`--open-first "All figures"`, `AMGT-bn-2`) so its dashes can be read: a research-team row's dash states its reason, the team sentence prints ONLY on a team row, and a Bloomberg or model row's dash prints its served reason or `Not served for this name` (round 106's change 2, never walked).

The AI-fill blocks are HELD off the served API (the `ai_fill` section reads ABSENT on every name): the page prints its fixed `not prepared` sentence on the always-shown placements and hides the others.

The local build of PROD is started by the ISSUER at the GO from your nested portal worktree (`C:/dev/wk-resapp-474/portal`, cut at `origin/PROD`, the head printed in the GO notes) with `bun run dev:live --port 5174`. DO NOT start, stop or restart it; check `curl -s -o /dev/null -w "%{http_code}" http://localhost:5174/` reads 200 before each walk and if it does not, STOP and file a BLOCKING row (never use another port: portal dev builds use 5174 ONLY).

THE DRAW is deterministic and PREPARED: the 93 resolved names, sorted by sha256(`2026-10-16` + ' ' + key), the first ten (AC1 prints it; the same ten are in `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107/walk_draw_20261016.json`): ZURN SW, ML FP, 939 HK, ICT PM, 1299 HK, IDXX US, OMAB MM, COST US, NOVN SW, CLX US. The walker types each name's search text into the page and, for each name, walks the overlay, the timeline day, Thesis, Exec Management, Peers, Model (with its version selects) and Posture, screenshots every step and prints in-page checks. With `--open-first "All figures"` it opens the All-figures disclosure FIRST on the Model tab and prints `OPEN-FIRST "All figures": opened (N table row(s) visible inside it)`. THE CHECKS ARE POINTERS, NOT THE VERDICT: the walk grades nothing.

1. AC1: the draw. 2. AC2 to AC5: four walks of three names each (about 125 seconds a name with the grid open, so each stays inside the shell tool's 600 s cap; set your tool timeout to 600000 ms). A walk that prints `HELD by` instead of `ARMED` means the walker's account lease is taken: wait 60 seconds (`sleep 60`), run `python .claude/skills/ui-walk/ui_walker_account.py status`, retry that same walk once the status reads `armed=no`; never `disarm` a holder that is not yours; a third failure is a BLOCKING row. A walk whose log reads `ERROR login did not complete (still on /login)` has disarmed itself: run THAT SAME walk once more; a second failure is a BLOCKING row. If a walk dies midway, run `python .claude/skills/ui-walk/ui_walker_account.py status`, and only if it reads `armed=yes` with YOUR holder, `disarm <holder>`.
3. After EACH walk copy its output folder `tmp/ui-walk/<stamp>` to `C:/dev/ui-walk-evidence/bn-4/<A|B|C|D>/` (outside the repository). NEVER commit a screenshot, never paste one into a message.
4. Then READ with the Read tool, for each of the twelve names, the Model-tab shot AFTER the grid was opened (`shots/NNN-<NAME>-Model-expanded.png`), the Exec-Management shot and the first overlay shot with the header tiles (`shots/NNN-<NAME>-Exec-Management.png` and the overlay/header shot), and write ONE line per name saying what you SAW, in exact text. Say: whether the All-figures grid is open with rows visible; a grid dash with NO reason beside it; the research-team sentence on a dash of a row that is not the team's; on the Key Figures P/E row, for each team figure in a column whose vendor ratio is withheld, whether `research team estimate` is under it, and any vendor P/E figure printed in a withheld column; plus the bm-5 classes: a money amount printed with `$` beside a non-USD currency, or with `USD ` where a `$` belongs; a dash tile or a Key Figures `--` cell with NO reason; a historical P/E with NO price line under it; an empty column header on a table; a raw code or vendor mnemonic as a row label; a placeholder word; an empty section with no reason; two figures that disagree; or 'clean'. For `SHOP CN` and `PBR US` say what each P/E cell of the Key Figures row shows (2025, 2026E, 2027E). You do not grade FWD-40: the CVO and the CTO read every shot.
5. BEFORE every walk: Git Bash rewrites a leading `/` argument into a Windows path (measured: the walker received `--route C:/Program Files/Git/security-analysis` and the walk was void). Prefix each `node .claude/skills/ui-walk/walk.mjs` call with `MSYS_NO_PATHCONV=1 ` (the order's AC invocations carry it). If the walk's first lines show a `--route` that is not `/security-analysis`, kill nothing, disarm nothing you do not hold, and file a BLOCKING row. On every name read, say in your one line whether an AI-fill block rendered (it should not) and whether any other section broke or went blank.
6. Report, from each `walk_<A|B|C|D>.txt`: the `STEP` lines with a non-zero finding count, verbatim, the `OPEN-FIRST` lines, and the SUMMARY line.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Run ONLY the five invocations below. Do not edit the walker, the draw or any product file; do not change the draw, the named names or the walk date.
2. Read-only against the world: the walker's guard aborts every request that is not GET/HEAD/OPTIONS or its own sign-in; you write nothing to S3, DynamoDB or the function.
3. Your files: your deliverables folder (the walk text files, the draw, the instance) and `C:/dev/ui-walk-evidence/bn-4/`. No push of shared branches. No `pip install`. Port 5174 only.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~474/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 2400; five mechanical criteria, the fourth walk and the fifth with a reason: the walker's wall time (about 125 s a name with the grid open) does not fit one shell call of 600 s, so the twelve names are four walks)

<proof_of_spec>
  <!-- the graded instance, under a short name because this order's own file name would make the canonical path pass this box's MAX_PATH: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~474/AMGT-bn-4.proof_of_spec.json` -->
  <criterion id="AC1" cell_refs="AMGT-bn-4"><invocation>cd C:/dev/wk-resapp-474 &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_walk_draw.py" --census "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round106/census_v5.json" --date 2026-10-16 --out "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~474/walk_draw.json"; echo "exit=$?"</invocation><expect>ten rows from `1  ZURN_SW_Equity` to `10  CLX_US_Equity`, the line `R103 WALK DRAW: 10 of 93 drawn (date 2026-10-16)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bn-4"><invocation>cd C:/dev/wk-resapp-474 &amp;&amp; MSYS_NO_PATHCONV=1 timeout 590 node ".claude/skills/ui-walk/walk.mjs" --route /security-analysis --security "ZURN SW" --security "ML FP" --security "939 HK" --open-first "All figures" --max-minutes 9 > "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~474/walk_A.txt" 2>&amp;1; echo "exit=$?"; grep -c "OPEN-FIRST \"All figures\": opened" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~474/walk_A.txt"; tail -6 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~474/walk_A.txt"</invocation><expect>`exit=0`; a count of at least 3 (one `OPEN-FIRST "All figures": opened (N table row(s)...` line per name asked, N at least 5); then in the last lines `OK: DISARMED`, a `LOGIN WITH THE WALK PASSWORD AFTER DISARM: HTTP 401 ... -> REFUSED` line and `SUMMARY: ... walk void: no`; and the walk file holds one `STEP <name>-Model` and one `STEP <name>-Exec Management` line for each of the names asked</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bn-4"><invocation>cd C:/dev/wk-resapp-474 &amp;&amp; MSYS_NO_PATHCONV=1 timeout 590 node ".claude/skills/ui-walk/walk.mjs" --route /security-analysis --security "ICT PM" --security "1299 HK" --security "IDXX US" --open-first "All figures" --max-minutes 9 > "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~474/walk_B.txt" 2>&amp;1; echo "exit=$?"; grep -c "OPEN-FIRST \"All figures\": opened" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~474/walk_B.txt"; tail -6 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~474/walk_B.txt"</invocation><expect>`exit=0`; a count of at least 3 (one `OPEN-FIRST "All figures": opened (N table row(s)...` line per name asked, N at least 5); then in the last lines `OK: DISARMED`, a `LOGIN WITH THE WALK PASSWORD AFTER DISARM: HTTP 401 ... -> REFUSED` line and `SUMMARY: ... walk void: no`; and the walk file holds one `STEP <name>-Model` and one `STEP <name>-Exec Management` line for each of the names asked</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-bn-4"><invocation>cd C:/dev/wk-resapp-474 &amp;&amp; MSYS_NO_PATHCONV=1 timeout 590 node ".claude/skills/ui-walk/walk.mjs" --route /security-analysis --security "OMAB MM" --security "COST US" --security "NOVN SW" --open-first "All figures" --max-minutes 9 > "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~474/walk_C.txt" 2>&1; echo "exit=$?"; grep -c "OPEN-FIRST \"All figures\": opened" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~474/walk_C.txt"; tail -6 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~474/walk_C.txt"</invocation><expect>`exit=0`; a count of at least 3 (one `OPEN-FIRST "All figures": opened (N table row(s)...` line per name asked, N at least 5); then in the last lines `OK: DISARMED`, a `LOGIN WITH THE WALK PASSWORD AFTER DISARM: HTTP 401 ... -> REFUSED` line and `SUMMARY: ... walk void: no`; and the walk file holds one `STEP <name>-Model` and one `STEP <name>-Exec Management` line for each of the names asked</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-bn-4"><invocation>cd C:/dev/wk-resapp-474 &amp;&amp; MSYS_NO_PATHCONV=1 timeout 590 node ".claude/skills/ui-walk/walk.mjs" --route /security-analysis --security "CLX US" --security "SHOP CN" --security "PBR US" --open-first "All figures" --max-minutes 9 > "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~474/walk_D.txt" 2>&amp;1; echo "exit=$?"; grep -c "OPEN-FIRST \"All figures\": opened" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~474/walk_D.txt"; tail -6 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~474/walk_D.txt"</invocation><expect>`exit=0`; a count of at least 3 (one `OPEN-FIRST "All figures": opened (N table row(s)...` line per name asked, N at least 5); then in the last lines `OK: DISARMED`, a `LOGIN WITH THE WALK PASSWORD AFTER DISARM: HTTP 401 ... -> REFUSED` line and `SUMMARY: ... walk void: no`; and the walk file holds one `STEP <name>-Model` and one `STEP <name>-Exec Management` line for each of the names asked</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-bn-4" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~474 <0.9.0_WK_AMGT_RESAPP~474@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~474/AMGT-bn-4.proof_of_spec.json` (THIS SHORT NAME: the block above names it, because this order's full name would make the path pass this box's MAX_PATH) with `to_id` equal to the `<to_id>` line above, character for character; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters; the schema's enum values are fixed (read the checker's refusal lines if it refuses; add `decomp_ref` from the order's own `<decomp_ref>` block if it asks). Run `python .tools/proof-of-spec-check.py <instance>` from `C:/dev/wk-resapp-474` on the committed bytes and report its verdict line.

Report once:
- the commit hash;
- the five criteria's output lines;
- per name (twelve), one line of what you saw;
- each walk's non-zero STEP lines, its OPEN-FIRST lines and its SUMMARY line, verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED SHELL cut 2026-10-15 ~22:5xZ (2.0.0_SA_COO~R1). CTO round-106 analysis (msg 6249): "bm-5 AC5 change 3 is re-graded against this reading at the next walk"; item 2: "one browser walk that opens the grid on the release build, with screenshots and the ui-walk classes graded". THE GO: given on or after 2026-10-16T00:00Z (the walk date is the UTC date of the walk; round 106's draw of 2026-10-15 would repeat for a walk today). The issuer cuts the worktree `C:/dev/wk-resapp-474` with `--sparse-add .claude/skills/ui-walk` (round 106's `W443-S1`), the nested portal at the current `origin/PROD` (`e0e69da7` at the cut, the head printed at the GO), starts `bun run dev:live --port 5174` there, and confirms the walker account reads dormant. The draw is computed from the issuer's round-106 census (`round106/census_v5.json`, 95 of 95 names read after `AMGT-bm-3`; the live served function has not been redeployed since: the scoped API's last deploy is round 106's `bm-3`). THE TWO NAMED NAMES are the issuer's choice inside the CTO's reading: SHOP CN is where the round-106 walk read change 3 as not shown, PBR US is the fixture the mark was first built against; neither is in the fresh draw. AC6 is JUDGMENT: the shot read, graded by the CVO and read by the CTO, never self-graded; the worker's one line per name is evidence for it. A walk-date wait is the one dependency of this order: the hourly drive tick after 00:00Z gives the GO. Build under walk: the running server in this worktree's nested portal; it must stay up until the walk files are committed.

<status>pending</status>
<round>107</round>
<slot>0.9.0_WK_AMGT_RESAPP~474</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
