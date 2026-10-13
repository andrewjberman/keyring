# AMGT_RESAPP task order -- `AMGT-bj-11` -- THE TEN-NAME BROWSER WALK ON A LOCAL BUILD OF THE PROD RELEASE COMMIT, DRAWN BY SHA256 (FWD-40 (d); A WALK RUN)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bj-11</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~412</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bj-11.the-ten-name-browser-walk-on-a-local-build-of-the-prod-release-commit</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot walk; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms and disarms the dormant UI-walker account itself under its own lease (`.claude/skills/ui-walk`); no grant, key or policy is touched by this order.
comp-adversary: RUN at the cut -- `r103_walk_draw.py --selftest` reads `R103 WALK DRAW ARMS: YES`; the draw over the census's 93 reads `10 of 93 drawn (date 2026-10-13)`; the walker itself was dry-run by the issuer on this build (portal PROD 63c4f9e3, `bun run dev:live --port 5174`): ARMED, LOGGED IN, 34 screenshots for one name over overlay, timeline day, Thesis, Exec Management, Peers, Model (with its version selects) and Posture, 0 guard aborts, `DISARM ... REFUSED`, `walk void: no`.
EGRESS CLASS, declared: the dev server's reads of the live services through the deployed front door (GET/HEAD/OPTIONS only: the walker's own network guard aborts any other request).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-412` (branch `wk-AMGT_RESAPP-412`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-412`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bj-11` (round 103, decomposition s.112)

FWD-40 (d) of PRD v0.44 (ratified text, inlined):

```
(d) a browser walk of 10 names on a LOCAL build of the
                    PROD release commit (`bun run dev:live --port 5174`,
                    which reaches the live services whatever a box's
                    `.env.local` says), screenshots read (the estate's walker
                    refuses a non-localhost base). The draw: the 93 keys
                    sorted by sha256(walk date + ' ' + key), the first ten,
                    the draw printed with the walk
```

The local build of the PROD release commit is ALREADY RUNNING: portal PROD `63c4f9e3` (Andrew's whole-DEV promote of 2026-10-13T19:24Z), your nested portal worktree `C:/dev/wk-resapp-412/portal`, `bun run dev:live --port 5174`, started by the issuer. DO NOT start, stop or restart it; check `curl -s -o /dev/null -w "%{http_code}" http://localhost:5174/` reads 200 before each walk and if it does not, STOP and file a BLOCKING row (never use another port: portal dev builds use 5174 ONLY).

THE DRAW is deterministic and PREPARED: the 93 resolved names with an exact-key pack, sorted by sha256(walk date + ' ' + key), the first ten (AC1 prints it; the same ten are committed in `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103/walk_draw_20261013.json`). The walker types each name's search text (`SAN FP`, `KPN NA`, ...) into the page and, for each name, walks the overlay, the timeline day, Thesis, Exec Management, Peers, Model (with its version selects) and Posture, screenshots every step and prints in-page checks. THE CHECKS ARE POINTERS, NOT THE VERDICT: the walk grades nothing.

1. AC1: the draw. 2. AC2, AC3, AC4: three walks (4, 4 and 2 names; about 100 seconds a name, so each stays inside the shell tool's 600 s cap; set your tool timeout to 600000 ms). A walk that prints `HELD by` instead of `ARMED` means the walker's account lease is taken: STOP, file a BLOCKING row, do NOT run `disarm` on a holder that is not yours. A walk whose log reads `ERROR login did not complete (still on /login)` has disarmed itself (the issuer's dry run met it once, 34 s after arming, and the next attempt logged in): run THAT SAME walk once more; a second failure is a BLOCKING row. If a walk dies midway, run `python .claude/skills/ui-walk/ui_walker_account.py status`, and only if it reads `armed=yes` with YOUR holder, `disarm <holder>`.
3. After EACH walk copy its output folder `tmp/ui-walk/<stamp>` to `C:/dev/ui-walk-evidence/bj-11/<A|B|C>/` (outside the repository). NEVER commit a screenshot, never paste one into a message.
4. Then READ with the Read tool, for each of the ten names, the Model-tab shot and the Exec-Management shot (`shots/NNN-<NAME>-Model.png`, `shots/NNN-<NAME>-Exec-Management.png`: 20 images), and write ONE line per name saying what you SAW: a raw code or vendor mnemonic as a row label, a placeholder word, an empty section with no reason, two figures that disagree, or 'clean'. Name each thing you saw by the exact text. You do not grade FWD-40 (d): the CVO reads every shot.
5. Report, from each `walk_<A|B|C>.txt`: the `STEP` lines with a non-zero finding count, verbatim, and the SUMMARY line.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W412-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Run ONLY the four invocations below. Do not edit the walker, the draw or any product file; do not change the draw or the walk date.
2. Read-only against the world: the walker's guard aborts every request that is not GET/HEAD/OPTIONS or its own sign-in; you write nothing to S3, DynamoDB or the function.
3. Your files: your deliverables folder (the walk text files, the draw, the instance) and `C:/dev/ui-walk-evidence/bj-11/`. No push of shared branches. No `pip install`. Port 5174 only.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~412/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1500)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bj-11"><invocation>cd C:/dev/wk-resapp-412 &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_walk_draw.py" --census "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103/census_v2.json" --date 2026-10-13 --out "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~412/walk_draw.json"; echo "exit=$?"</invocation><expect>ten rows from `1  SAN_FP_Equity` to `10  NOKIA_FH_Equity`, the line `R103 WALK DRAW: 10 of 93 drawn (date 2026-10-13)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bj-11"><invocation>cd C:/dev/wk-resapp-412 &amp;&amp; timeout 590 node ".claude/skills/ui-walk/walk.mjs" --route /security-analysis --security "SAN FP" --security "KPN NA" --security "TSM US" --security "HSBA LN" --max-minutes 9 > "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~412/walk_A.txt" 2>&amp;1; echo "exit=$?"; tail -6 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~412/walk_A.txt"</invocation><expect>`exit=0`, then in the last lines `OK: DISARMED`, a `LOGIN WITH THE WALK PASSWORD AFTER DISARM: HTTP 401 ... -> REFUSED` line and `SUMMARY: ... walk void: no`; and the walk file holds one `STEP <name>-Model` and one `STEP <name>-Exec Management` line for each of the names asked</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bj-11"><invocation>cd C:/dev/wk-resapp-412 &amp;&amp; timeout 590 node ".claude/skills/ui-walk/walk.mjs" --route /security-analysis --security "MA US" --security "CDNS US" --security "UNH US" --security "UBER US" --max-minutes 9 > "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~412/walk_B.txt" 2>&amp;1; echo "exit=$?"; tail -6 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~412/walk_B.txt"</invocation><expect>`exit=0`, then in the last lines `OK: DISARMED`, a `LOGIN WITH THE WALK PASSWORD AFTER DISARM: HTTP 401 ... -> REFUSED` line and `SUMMARY: ... walk void: no`; and the walk file holds one `STEP <name>-Model` and one `STEP <name>-Exec Management` line for each of the names asked</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-bj-11"><invocation>cd C:/dev/wk-resapp-412 &amp;&amp; timeout 590 node ".claude/skills/ui-walk/walk.mjs" --route /security-analysis --security "AZN LN" --security "NOKIA FH" --max-minutes 9 > "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~412/walk_C.txt" 2>&amp;1; echo "exit=$?"; tail -6 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~412/walk_C.txt"</invocation><expect>`exit=0`, then in the last lines `OK: DISARMED`, a `LOGIN WITH THE WALK PASSWORD AFTER DISARM: HTTP 401 ... -> REFUSED` line and `SUMMARY: ... walk void: no`; and the walk file holds one `STEP <name>-Model` and one `STEP <name>-Exec Management` line for each of the names asked</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-bj-11" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~412 <0.9.0_WK_AMGT_RESAPP~412@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~412/AMGT_RESAPP.TO-AMGT-bj-11.the-ten-name-browser-walk-on-a-local-build-of-the-prod-release-commit.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character; each criterion's `expect` recorded as an ordered regex of the printed lines when the prose has regex-active characters.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- the four criteria's output lines;
- per name, one line of what you saw on its Model and Exec Management shots;
- each walk's non-zero STEP lines and SUMMARY line, verbatim;
- any row.
The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** GO 2026-10-13T20:0xZ by the issuer (2.0.0_SA_COO~R1): port 5174 is free and the PROD-commit dev build is running in this worktree's nested portal; the walker's account is dormant (`status=disabled armed=no`) and arms for each walk; AC1 to AC4 are bounded at 590 s each. THE REST: FWD-40 (d): ten names drawn by sha256 of the walk date over the 93, a LOCAL build of the PROD release commit (`bun run dev:live --port 5174`), screenshots read. The criteria are four because the walker's wall time (about 100 s a name) does not fit one shell call of 600 s: AC1 the draw and AC2 to AC4 the walks of 4, 4 and 2 names (a fourth mechanical criterion with its reason on the face). AC5 is JUDGMENT: the screenshot read, graded by the CVO, never self-graded; the worker's one line per name is evidence for it, not its verdict. The CTO's 5113/5117: the Model tab's raw-code labels are a HYPOTHESIS (the e7f2 note is from 10-11; no model-row label candidate appears in the payloads); this walk is the first read and includes the Model tab for all ten. The issuer's own dry run of the walker on `ASML` and on `SAN FP` and `NOKIA FH` is the control. The build under walk is the running server in this worktree: it must stay up until the walk files are committed.

<status>pending</status>
<status>complete -- 2026-10-13T20:4xZ by the issuer (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-412 @408fefd61e merged, proof instance VALID (rc=0). AC1 to AC4 PASS: the draw (10 of 93, date 2026-10-13) and three walks of 4, 4 and 2 names on the PROD release commit 63c4f9e3 (`bun run dev:live --port 5174`), each ARMED then DISARMED with the post-disarm login REFUSED, `walk void: no`, 0 guard aborts; 285 screenshots held OUTSIDE the repository at C:/dev/ui-walk-evidence/bj-11/{A,B,C} (never committed). AC5 is JUDGMENT: graded by the CVO, NOT here. WHAT THE WORKER SAW on the 20 Model and Exec Management shots (a reading, not a grade) and the issuer's own read of two (SAN FP, TSM US) confirms: NO raw code or vendor mnemonic as a Model row label on any of the ten (the CTO's hypothesis of msg 5113 is not borne out on this draw); what shows instead: the placeholder sentence `The research team fills it in.` on SAN FP, KPN NA, HSBA LN, UNH US and NOKIA FH; the line `no management section ... 2026-Q2` in place of text on KPN NA, HSBA LN and UNH US; a header `Enterprise value --` and `Market cap --` / `Net debt --` beside figures that carry the same quantity (TSM US, HSBA LN, AZN LN); `Figures in USD` beside a GBp share price (HSBA LN, AZN LN); the team's cases printed with no currency beside a different quote currency (TSM US, AZN LN, MA US); a 2025 P/E that does not follow from the printed EPS and price on SAN FP (20.4x against 6.40 at EUR 72.09, which is 11.3x), CDNS US, UNH US, UBER US and NOKIA FH while the 2026E P/E does; on MA US the Exec text names a CFO the table does not and a role listed twice. Every one is a CANDIDATE for the CVO's read and the CTO's round-103 analysis. No row filed.</status>
<round>103</round>
<workstream>V1WALK</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~412</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
