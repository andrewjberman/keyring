# AMGT_RESAPP task order -- `AMGT-bl-3` -- THE TEN-NAME BROWSER WALK ON A LOCAL BUILD OF THE PROD RELEASE THAT CARRIES THE HEADER FEATURE, DRAWN BY SHA256 (FWD-40 (a), (d); A WALK RUN)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bl-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~440</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bl-3.the-ten-name-browser-walk-on-a-local-build-of-the-prod-release-with-the-currency-and-reasons-feature</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot walk; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms and disarms the dormant UI-walker account itself under its own lease (`.claude/skills/ui-walk`); no grant, key or policy is touched by this order.
comp-adversary: RUN at the cut -- `r103_walk_draw.py --selftest` reads `R103 WALK DRAW ARMS: YES`; the draw over the census's 93 reads `10 of 93 drawn (date 2026-10-14)`; the walker was dry-run by the issuer on the PROD release commit in round 103 (ARMED, LOGGED IN, 0 guard aborts, `DISARM ... REFUSED`, `walk void: no`).
EGRESS CLASS, declared: the dev server's reads of the live services through the deployed front door (GET/HEAD/OPTIONS only: the walker's own network guard aborts any other request).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-440` (branch `wk-AMGT_RESAPP-440`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-440`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bl-3` (round 105, decomposition s.114)

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

Round 105 changed three things the page shows (all Security Analysis, Opal-internal): a money symbol prints ONLY for the figure's own currency (PBR US's research-team model figures print `BRL ` and no `$`; a USD figure keeps `$`; a figure with no known currency prints no symbol); BATS LN's Thesis-tab segment tables no longer show an empty `Period 4` column (one sentence says why instead); and a `--` cell in the Model tab's Key Figures table shows its reason in words (the served reason, or `Not served for this name`). Round 104's header changes (USD as `$`, header dash reasons, the derived forward P/E) are already on PROD. This walk is the read of those on PROD: PBR US and BATS LN are both in the draw.

The local build of the PROD release commit is ALREADY RUNNING: portal PROD `7db035e4` (the release that carries the currency-symbol and reasons feature AND the AI-fill page feature; the CTO's word, msg 5405), your nested portal worktree `C:/dev/wk-resapp-440/portal`, `bun run dev:live --port 5174`, started by the issuer. DO NOT start, stop or restart it; check `curl -s -o /dev/null -w "%{http_code}" http://localhost:5174/` reads 200 before each walk and if it does not, STOP and file a BLOCKING row (never use another port: portal dev builds use 5174 ONLY).

THE DRAW is deterministic and PREPARED: the 93 resolved names with an exact-key pack, sorted by sha256(walk date + ' ' + key), the first ten (AC1 prints it; the same ten are committed in `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round104/walk_draw_20261014.json`). The walker types each name's search text (`8316 JP`, `NKE US`, ...) into the page and, for each name, walks the overlay, the timeline day, Thesis, Exec Management, Peers, Model (with its version selects) and Posture, screenshots every step and prints in-page checks. THE CHECKS ARE POINTERS, NOT THE VERDICT: the walk grades nothing.

1. AC1: the draw. 2. AC2, AC3, AC4: three walks (4, 4 and 2 names; about 100 seconds a name, so each stays inside the shell tool's 600 s cap; set your tool timeout to 600000 ms). A walk that prints `HELD by` instead of `ARMED` means the walker's account lease is taken: STOP, file a BLOCKING row, do NOT run `disarm` on a holder that is not yours. A walk whose log reads `ERROR login did not complete (still on /login)` has disarmed itself: run THAT SAME walk once more; a second failure is a BLOCKING row. If a walk dies midway, run `python .claude/skills/ui-walk/ui_walker_account.py status`, and only if it reads `armed=yes` with YOUR holder, `disarm <holder>`.
3. After EACH walk copy its output folder `tmp/ui-walk/<stamp>` to `C:/dev/ui-walk-evidence/bl-3/<A|B|C>/` (outside the repository). NEVER commit a screenshot, never paste one into a message.
4. Then READ with the Read tool, for each of the ten names, the Model-tab shot, the Exec-Management shot AND the first overlay shot with the header tiles (`shots/NNN-<NAME>-Model.png`, `-Exec-Management.png`, and the overlay/header shot of that name), and write ONE line per name saying what you SAW, in exact text: a money amount printed with `$` beside a non-USD currency, or with `USD ` where a `$` belongs; a dash tile or a Key Figures `--` cell with NO reason beside it; an empty column header on a table; a raw code or vendor mnemonic as a row label; a placeholder word; an empty section with no reason; two figures that disagree (a P/E that does not follow from the printed EPS and price); or 'clean'. You do not grade FWD-40: the CVO reads every shot.
5. RE-SEAT NOTE (second pass): AC1 and AC2 are DONE and committed by the first pass (`bf2e54af06`, `8eda4a5bd4`: the draw and walk A of 8316 JP, NKE US, BATS LN, GOOGL US on PROD 7db035e4). Your remaining work: AC3 and AC4 (the walks of PBR US, QXO US, COST US, 8035 JP and of ISP IM, ENEL IM), the shot reads of the six names not yet read (PBR US first), the instance re-recorded with the invocations exactly as the criteria below now print them, and the checker re-run. If a walk prints `ERROR Command failed: ... ui_walker_account.py arm` or `HELD by`, the walker lease is held by another seat: wait 60 seconds (`sleep 60`), run `python .claude/skills/ui-walk/ui_walker_account.py status`, and retry that same walk once the status reads `armed=no`; never disarm a holder that is not yours; a third failure is a BLOCKING row. Do NOT redo AC1 or AC2.
5b. BEFORE every walk: Git Bash rewrites a leading `/` argument into a Windows path (measured: the walker received `--route C:/Program Files/Git/security-analysis` and the walk was void). Prefix each `node .claude/skills/ui-walk/walk.mjs` call with `MSYS_NO_PATHCONV=1 ` (the order's AC invocations are to be run with that prefix; the output is read the same way). If the walk's first lines show a `--route` that is not `/security-analysis`, kill nothing, disarm nothing you do not hold, and file a BLOCKING row. The page now also renders the AI-fill blocks (each with a `Machine-written` chip): on every name read, say in your one line whether such a block rendered, with its chip, and whether any other section broke or went blank.
6. Report, from each `walk_<A|B|C>.txt`: the `STEP` lines with a non-zero finding count, verbatim, and the SUMMARY line.


Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Run ONLY the four invocations below. Do not edit the walker, the draw or any product file; do not change the draw or the walk date.
2. Read-only against the world: the walker's guard aborts every request that is not GET/HEAD/OPTIONS or its own sign-in; you write nothing to S3, DynamoDB or the function.
3. Your files: your deliverables folder (the walk text files, the draw, the instance) and `C:/dev/ui-walk-evidence/bl-3/`. No push of shared branches. No `pip install`. Port 5174 only.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~440/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1500)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bl-3"><invocation>cd C:/dev/wk-resapp-440 &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_walk_draw.py" --census "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round104/census_v3.json" --date 2026-10-14 --out "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~440/walk_draw.json"; echo "exit=$?"</invocation><expect>ten rows from `1  8316_JP_Equity` to `10  ENEL_IM_Equity`, the line `R103 WALK DRAW: 10 of 93 drawn (date 2026-10-14)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bl-3"><invocation>cd C:/dev/wk-resapp-440 &amp;&amp; MSYS_NO_PATHCONV=1 timeout 590 node ".claude/skills/ui-walk/walk.mjs" --route /security-analysis --security "8316 JP" --security "NKE US" --security "BATS LN" --security "GOOGL US" --max-minutes 9 > "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~440/walk_A.txt" 2>&amp;1; echo "exit=$?"; tail -6 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~440/walk_A.txt"</invocation><expect>`exit=0`, then in the last lines `OK: DISARMED`, a `LOGIN WITH THE WALK PASSWORD AFTER DISARM: HTTP 401 ... -> REFUSED` line and `SUMMARY: ... walk void: no`; and the walk file holds one `STEP <name>-Model` and one `STEP <name>-Exec Management` line for each of the names asked</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bl-3"><invocation>cd C:/dev/wk-resapp-440 &amp;&amp; MSYS_NO_PATHCONV=1 timeout 590 node ".claude/skills/ui-walk/walk.mjs" --route /security-analysis --security "PBR US" --security "QXO US" --security "COST US" --security "8035 JP" --max-minutes 9 > "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~440/walk_B.txt" 2>&amp;1; echo "exit=$?"; tail -6 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~440/walk_B.txt"</invocation><expect>`exit=0`, then in the last lines `OK: DISARMED`, a `LOGIN WITH THE WALK PASSWORD AFTER DISARM: HTTP 401 ... -> REFUSED` line and `SUMMARY: ... walk void: no`; and the walk file holds one `STEP <name>-Model` and one `STEP <name>-Exec Management` line for each of the names asked</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-bl-3"><invocation>cd C:/dev/wk-resapp-440 &amp;&amp; MSYS_NO_PATHCONV=1 timeout 590 node ".claude/skills/ui-walk/walk.mjs" --route /security-analysis --security "ISP IM" --security "ENEL IM" --max-minutes 9 > "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~440/walk_C.txt" 2>&amp;1; echo "exit=$?"; tail -6 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~440/walk_C.txt"</invocation><expect>`exit=0`, then in the last lines `OK: DISARMED`, a `LOGIN WITH THE WALK PASSWORD AFTER DISARM: HTTP 401 ... -> REFUSED` line and `SUMMARY: ... walk void: no`; and the walk file holds one `STEP <name>-Model` and one `STEP <name>-Exec Management` line for each of the names asked</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-bl-3" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~440 <0.9.0_WK_AMGT_RESAPP~440@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~440/AMGT_RESAPP.TO-AMGT-bl-3.the-ten-name-browser-walk-on-a-local-build-of-the-prod-release-with-the-currency-and-reasons-feature.proof_of_spec.json` with `to_id` equal to the `<to_id>` line above, character for character; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters; if the checker refuses the instance for a missing `decomp_ref`, add it from the order's own `<decomp_ref>` block. Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.

Report once:
- the commit hash;
- the four criteria's output lines;
- per name, one line of what you saw (Model, Exec Management and the header tiles);
- each walk's non-zero STEP lines and SUMMARY line, verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** FWD-40 (a) re-grade after round 105: the census (issuer's run of round 104, `round104/census_v3.txt`, 95 of 95 names, UNEXPLAINED 3 = thesis.model_cases on BABA_US, BA_US, PBR_US, STATE_ONLY 187; re-run by the issuer for this cell as `round105/census_v4.txt`) and this walk. PBR US is in the draw. AC5 is JUDGMENT: the screenshot read, graded by the CVO, never self-graded; the worker's one line per name is evidence for it. The criteria are four because the walker's wall time (about 100 s a name) does not fit one shell call of 600 s (a fourth mechanical criterion with its reason on the face). The build under walk is the running server in this worktree's nested portal: it must stay up until the walk files are committed.

<status>complete -- 2026-10-14T04:4xZ by the issuer (2.0.0_SA_COO~R1): worker ~440 (three seats: the first stopped by the issuer when the CTO named PROD 7db035e4; the second walked A and met a held walker lease; the third finished AC3, AC4 and the reads) @3a2a36398a merged @e8d8b5286c, proof instance VALID (rc=0). AC1 to AC4 PASS: the draw (10 of 93, date 2026-10-14) and three walks of 4, 4 and 2 names on a local build of PROD 7db035e4 (`bun run dev:live --port 5174`; it carries bl-1 and ~R2's AI-fill feature), each ARMED then DISARMED with the post-disarm login REFUSED, `walk void: no`, 0 guard aborts; the walker account reads dormant after; screenshots OUTSIDE the repository at C:/dev/ui-walk-evidence/bl-3/{A,B,C}. AC5 is JUDGMENT: graded by the CVO, NOT here. The issuer's own read of PBR US's Model shot (B/20261014T041917Z/shots/015): `Figures in BRL`, `EPS (per share, BRL)`, `EBITDA (millions, BRL)`, no `$` in the table, every `--` cell with its reason (`No consensus estimate is served for this line`, `Bloomberg reports no history for this line`), the header's price `$25.30` (the USD quote) and market cap, EV and net debt dashes carrying `Bloomberg does not confirm this figure's currency`. The worker's reads agree and add the candidates listed in the round-105 packet. A reading, not a grade.</status>
<round>105</round>
<workstream>WALK</workstream>
<slot>0.9.0_WK_AMGT_RESAPP~440</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
