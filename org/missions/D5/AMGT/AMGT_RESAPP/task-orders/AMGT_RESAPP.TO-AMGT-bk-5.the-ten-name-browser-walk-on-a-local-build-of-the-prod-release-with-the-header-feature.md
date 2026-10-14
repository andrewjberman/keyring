# AMGT_RESAPP task order -- `AMGT-bk-5` -- THE TEN-NAME BROWSER WALK ON A LOCAL BUILD OF THE PROD RELEASE THAT CARRIES THE HEADER FEATURE, DRAWN BY SHA256 (FWD-40 (a), (d); A WALK RUN)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bk-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~418</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bk-5.the-ten-name-browser-walk-on-a-local-build-of-the-prod-release-with-the-header-feature</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot walk; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms and disarms the dormant UI-walker account itself under its own lease (`.claude/skills/ui-walk`); no grant, key or policy is touched by this order.
comp-adversary: RUN at the cut -- `r103_walk_draw.py --selftest` reads `R103 WALK DRAW ARMS: YES`; the draw over the census's 93 reads `10 of 93 drawn (date 2026-10-14)`; the walker was dry-run by the issuer on the PROD release commit in round 103 (ARMED, LOGGED IN, 0 guard aborts, `DISARM ... REFUSED`, `walk void: no`).
EGRESS CLASS, declared: the dev server's reads of the live services through the deployed front door (GET/HEAD/OPTIONS only: the walker's own network guard aborts any other request).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-418` (branch `wk-AMGT_RESAPP-418`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-418`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bk-5` (round 104, decomposition s.113)

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

Round 104 changed two things the page shows: the Security Analysis header prints USD as `$` (not `USD `) and every dash tile shows its reason in words (`Not served for this name` or the served reason); the historical P/E is now price over reported EPS of the same fiscal year, and a year whose price and EPS are in different currencies shows a stated reason instead of a value. This walk is the first read of those on PROD.

The local build of the PROD release commit is ALREADY RUNNING: portal PROD `7d5cb34d` (the release that carries the header feature), your nested portal worktree `C:/dev/wk-resapp-418/portal`, `bun run dev:live --port 5174`, started by the issuer. DO NOT start, stop or restart it; check `curl -s -o /dev/null -w "%{http_code}" http://localhost:5174/` reads 200 before each walk and if it does not, STOP and file a BLOCKING row (never use another port: portal dev builds use 5174 ONLY).

THE DRAW is deterministic and PREPARED: the 93 resolved names with an exact-key pack, sorted by sha256(walk date + ' ' + key), the first ten (AC1 prints it; the same ten are committed in `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round104/walk_draw_20261014.json`). The walker types each name's search text (`8316 JP`, `NKE US`, ...) into the page and, for each name, walks the overlay, the timeline day, Thesis, Exec Management, Peers, Model (with its version selects) and Posture, screenshots every step and prints in-page checks. THE CHECKS ARE POINTERS, NOT THE VERDICT: the walk grades nothing.

1. AC1: the draw. 2. AC2, AC3, AC4: three walks (4, 4 and 2 names; about 100 seconds a name, so each stays inside the shell tool's 600 s cap; set your tool timeout to 600000 ms). A walk that prints `HELD by` instead of `ARMED` means the walker's account lease is taken: STOP, file a BLOCKING row, do NOT run `disarm` on a holder that is not yours. A walk whose log reads `ERROR login did not complete (still on /login)` has disarmed itself: run THAT SAME walk once more; a second failure is a BLOCKING row. If a walk dies midway, run `python .claude/skills/ui-walk/ui_walker_account.py status`, and only if it reads `armed=yes` with YOUR holder, `disarm <holder>`.
3. After EACH walk copy its output folder `tmp/ui-walk/<stamp>` to `C:/dev/ui-walk-evidence/bk-5/<A|B|C>/` (outside the repository). NEVER commit a screenshot, never paste one into a message.
4. Then READ with the Read tool, for each of the ten names, the Model-tab shot, the Exec-Management shot AND the first overlay shot with the header tiles (`shots/NNN-<NAME>-Model.png`, `-Exec-Management.png`, and the overlay/header shot of that name), and write ONE line per name saying what you SAW, in exact text: a money amount printed with `USD ` where a `$` belongs, or with `$` beside a non-USD quote; a dash tile with NO reason beside it; a raw code or vendor mnemonic as a row label; a placeholder word; an empty section with no reason; two figures that disagree (a P/E that does not follow from the printed EPS and price); or 'clean'. You do not grade FWD-40: the CVO reads every shot.
5. Report, from each `walk_<A|B|C>.txt`: the `STEP` lines with a non-zero finding count, verbatim, and the SUMMARY line.


Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Run ONLY the four invocations below. Do not edit the walker, the draw or any product file; do not change the draw or the walk date.
2. Read-only against the world: the walker's guard aborts every request that is not GET/HEAD/OPTIONS or its own sign-in; you write nothing to S3, DynamoDB or the function.
3. Your files: your deliverables folder (the walk text files, the draw, the instance) and `C:/dev/ui-walk-evidence/bk-5/`. No push of shared branches. No `pip install`. Port 5174 only.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~418/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1500)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bk-5"><invocation>cd C:/dev/wk-resapp-418 &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_walk_draw.py" --census "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round104/census_v3.json" --date 2026-10-14 --out "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~418/walk_draw.json"; echo "exit=$?"</invocation><expect>ten rows from `1  8316_JP_Equity` to `10  ENEL_IM_Equity`, the line `R103 WALK DRAW: 10 of 93 drawn (date 2026-10-14)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bk-5"><invocation>cd C:/dev/wk-resapp-418 &amp;&amp; timeout 590 node ".claude/skills/ui-walk/walk.mjs" --route /security-analysis --security "8316 JP" --security "NKE US" --security "BATS LN" --security "GOOGL US" --max-minutes 9 > "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~418/walk_A.txt" 2>&amp;1; echo "exit=$?"; tail -6 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~418/walk_A.txt"</invocation><expect>`exit=0`, then in the last lines `OK: DISARMED`, a `LOGIN WITH THE WALK PASSWORD AFTER DISARM: HTTP 401 ... -> REFUSED` line and `SUMMARY: ... walk void: no`; and the walk file holds one `STEP <name>-Model` and one `STEP <name>-Exec Management` line for each of the names asked</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bk-5"><invocation>cd C:/dev/wk-resapp-418 &amp;&amp; timeout 590 node ".claude/skills/ui-walk/walk.mjs" --route /security-analysis --security "PBR US" --security "QXO US" --security "COST US" --security "8035 JP" --max-minutes 9 > "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~418/walk_B.txt" 2>&amp;1; echo "exit=$?"; tail -6 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~418/walk_B.txt"</invocation><expect>`exit=0`, then in the last lines `OK: DISARMED`, a `LOGIN WITH THE WALK PASSWORD AFTER DISARM: HTTP 401 ... -> REFUSED` line and `SUMMARY: ... walk void: no`; and the walk file holds one `STEP <name>-Model` and one `STEP <name>-Exec Management` line for each of the names asked</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-bk-5"><invocation>cd C:/dev/wk-resapp-418 &amp;&amp; timeout 590 node ".claude/skills/ui-walk/walk.mjs" --route /security-analysis --security "ISP IM" --security "ENEL IM" --max-minutes 9 > "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~418/walk_C.txt" 2>&amp;1; echo "exit=$?"; tail -6 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~418/walk_C.txt"</invocation><expect>`exit=0`, then in the last lines `OK: DISARMED`, a `LOGIN WITH THE WALK PASSWORD AFTER DISARM: HTTP 401 ... -> REFUSED` line and `SUMMARY: ... walk void: no`; and the walk file holds one `STEP <name>-Model` and one `STEP <name>-Exec Management` line for each of the names asked</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-bk-5" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~418 <0.9.0_WK_AMGT_RESAPP~418@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~418/AMGT_RESAPP.TO-AMGT-bk-5.the-ten-name-browser-walk-on-a-local-build-of-the-prod-release-with-the-header-feature.proof_of_spec.json` with `to_id` equal to the `<to_id>` line above, character for character; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters; if the checker refuses the instance for a missing `decomp_ref`, add it from the order's own `<decomp_ref>` block. Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.

Report once:
- the commit hash;
- the four criteria's output lines;
- per name, one line of what you saw (Model, Exec Management and the header tiles);
- each walk's non-zero STEP lines and SUMMARY line, verbatim;
- any row.

The `<status>complete -- 2026-10-14T01:3xZ by the issuer (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-418 @b0f9a8da91 merged @ce02c56d12, proof instance VALID (rc=0). AC1 to AC4 PASS: the draw (10 of 93, date 2026-10-14) and three walks of 4, 4 and 2 names on the PROD release 7d5cb34d (`bun run dev:live --port 5174`), each ARMED then DISARMED with the post-disarm login REFUSED, `walk void: no`, 0 guard aborts; the walker account reads dormant (`armed=no`) after; screenshots held OUTSIDE the repository at C:/dev/ui-walk-evidence/bk-5/{A,B,C}. AC5 is JUDGMENT: graded by the CVO, NOT here. The issuer's own read of two shots (GOOGL US overlay and Model): header prints `$351.66`, `$4.28T`, `$4.17T`, `$-63.90B` (no `USD `); Model Key Figures dash cells (EBITDA margin 2026E/2027E, EV/EBITDA, ROE) carry NO reason; the 2025 P/E 28.7x is FY-end price over EPS 10.91 and the FY price is not printed; negative money prints `$-201.80B`. The worker's per-name reads (shot_reads.txt) agree and add: PBR US 2026E/27E P/E beside a USD price and BRL EPS with no currency note; Exec role values with colon codes and truncated words on JP, IM and US names. No name read clean. A reading, not a grade; rows W418-S2 to S4.</status>
<round>104</round>
<workstream>WALK</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~418</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
