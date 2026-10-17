# AMGT_RESAPP task order -- `AMGT-bp-2` -- THE GRID-OPENED BROWSER WALK OF VLO US, RIO LN AND WALMEX* MM ON A LOCAL BUILD OF PROD PLUS THE `bp-1` CANDIDATE (A WALK RUN, THE RE-RUN OF `bo-3` AC5) -- STAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bp-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~491</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bp-2.walk-three-names-on-prod-plus-the-crash-fix</to_id>
<placeholders>NONE</placeholders>
<workstream>WALK</workstream>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot walk; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms and disarms the dormant UI-walker account itself under its own lease (`.claude/skills/ui-walk`); no grant, key or policy is touched by this order.
comp-adversary: RUN at the cut -- the same walk run in round 108 on a local build of PROD `15bc21b3` WITHOUT the fix (`bo-3` walk D, `walk_D.txt`) printed `OPEN-FIRST "All figures": opened` for two of these three names (VLO US 151 rows, WALMEX* MM 144 rows) and `not found in RIO LN-Model` for the third, because RIO LN's Model tab rendered the page error screen; so AC1's expectation of three opened lines is unmet on unpatched PROD, as expected. The walk itself is the act and is NOT run at the cut: it needs the `bp-1` candidate, which does not exist until `AMGT-bp-1` completes.
EGRESS CLASS, declared: the dev server's reads of the live services through the deployed front door (GET/HEAD/OPTIONS only: the walker's own network guard aborts any other request).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-491` (branch `wk-AMGT_RESAPP-491`, cut from the issuance commit at the GO). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-491`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bp-2` (round 109, decomposition s.118)

Round 108's walk (`bo-3`) could not open the All-figures grid on RIO LN, because RIO LN's Model tab crashed the page (`TypeError: value.trim is not a function`). Round 109's `AMGT-bp-1` fixes the crash in a portal candidate. This cell re-runs that one walk, on the three names of the failed walk, on a local build that carries the fix, and reads the result. What the page should now do on RIO LN: the Model tab renders (no error screen), the All-figures grid opens with rows visible, and the What Changed table shows the earnings-announcement figure as a plain reading (`<date> (<period>)`), never an error.

The local build is started by the ISSUER at the GO from your nested portal worktree (`C:/dev/wk-resapp-491/portal`, cut at the `bp-1` candidate head printed in the GO notes) with `bun run dev:live --port 5174`. DO NOT start, stop or restart it; check `curl -s -o /dev/null -w "%{http_code}" http://localhost:5174/` reads 200 before the walk and if it does not, STOP and file a BLOCKING row (never use another port: portal dev builds use 5174 ONLY).

1. AC1: ONE walk of three names, VLO US, RIO LN and WALMEX* MM, with the All-figures grid opened first on the Model tab (about 125 seconds a name, so it stays inside the shell tool's 600 s cap; set your tool timeout to 600000 ms). A walk that prints `HELD by` instead of `ARMED` means the walker's account lease is taken: wait 60 seconds (`sleep 60`), run `python .claude/skills/ui-walk/ui_walker_account.py status`, retry that same walk once the status reads `armed=no`; never `disarm` a holder that is not yours; a third failure is a BLOCKING row. A walk whose log reads `ERROR login did not complete (still on /login)` has disarmed itself: run THAT SAME walk once more; a second failure is a BLOCKING row. If the walk dies midway, run `python .claude/skills/ui-walk/ui_walker_account.py status`, and only if it reads `armed=yes` with YOUR holder, `disarm <holder>`.
2. After the walk copy its output folder `tmp/ui-walk/<stamp>` to `C:/dev/ui-walk-evidence/bp-2/A/` (outside the repository). NEVER commit a screenshot, never paste one into a message.
3. Then READ with the Read tool, for each of the three names, the Model-tab shot AFTER the grid was opened (`shots/NNN-<NAME>-Model-expanded.png`), and write ONE line per name saying what you SAW, in exact text. For RIO LN say, in this order: (a) whether the Model tab rendered or shows an error screen (quote any error text); (b) whether the All-figures grid is open with rows visible and how many rows the `OPEN-FIRST` line prints; (c) in the What Changed section, the exact text of the row for the earnings-announcement figure (the row whose figure name or values show dates and periods), both its before and its after side, and whether any `[object Object]` or `undefined` text is printed; (d) the number the `Changed` tile shows against the number of rows listed. For VLO US and WALMEX* MM say: whether the All-figures grid is open with rows visible, whether the Model tab renders, and whether What Changed prints any `[object Object]` or `undefined`. For ALL three say whether an AI-fill block rendered on Exec Management (quote its first line) and whether any section broke or went blank. You do not grade FWD-40: the CVO and the CTO read every shot.
4. BEFORE the walk: Git Bash rewrites a leading `/` argument into a Windows path (the walker received `--route C:/Program Files/Git/security-analysis` and the walk was void). Prefix the `node .claude/skills/ui-walk/walk.mjs` call with `MSYS_NO_PATHCONV=1 ` (the order's AC1 invocation carries it). If the walk's first lines show a `--route` that is not `/security-analysis`, kill nothing, disarm nothing you do not hold, and file a BLOCKING row.
5. Report, from `walk_A.txt`: the `STEP` lines with a non-zero finding count, verbatim, the `OPEN-FIRST` lines, and the SUMMARY line.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Run ONLY the invocation below. Do not edit the walker or any product file; do not change the three names.
2. Read-only against the world: the walker's guard aborts every request that is not GET/HEAD/OPTIONS or its own sign-in; you write nothing to S3, DynamoDB or the function.
3. Your files: your deliverables folder (the walk text file, the instance) and `C:/dev/ui-walk-evidence/bp-2/`. No push of shared branches. No `pip install`. Port 5174 only.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~491/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900; one mechanical criterion, one walk of three names with a reason: the walker's wall time is about 125 s a name with the grid open)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bp-2"><invocation>mkdir -p "C:/dev/wk-resapp-491/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~491" &amp;&amp; cd C:/dev/wk-resapp-491 &amp;&amp; MSYS_NO_PATHCONV=1 timeout 590 node ".claude/skills/ui-walk/walk.mjs" --route /security-analysis --security "VLO US" --security "RIO LN" --security "WALMEX* MM" --open-first "All figures" --max-minutes 9 > "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~491/walk_A.txt" 2>&amp;1; echo "exit=$?"; grep -c "OPEN-FIRST \"All figures\": opened" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~491/walk_A.txt"; tail -6 "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~491/walk_A.txt"</invocation><expect>`exit=0`; a count of at least 3 (one `OPEN-FIRST "All figures": opened (N table row(s)...` line per name asked, N at least 5; the round-108 walk on unpatched PROD printed 2); then in the last lines `OK: DISARMED`, a `LOGIN WITH THE WALK PASSWORD AFTER DISARM: HTTP 401 ... -> REFUSED` line and `SUMMARY: ... walk void: no`; and the walk file holds one `STEP <name>-Model` and one `STEP <name>-Exec Management` line for each of the three names</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bp-2" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~491 <0.9.0_WK_AMGT_RESAPP~491@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~491/AMGT_RESAPP.TO-AMGT-bp-2.walk-three-names-on-prod-plus-the-crash-fix.proof_of_spec.json` (this order's name is short on purpose, so the canonical path opens on this box) with `to_id` equal to the `<to_id>` line above, character for character; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters; AC2 is a judgment criterion: it carries no verdict (`UNVERIFIABLE-BY-INSTRUMENT`, status_reason naming `3.0.0_SA_CVO`); a failing AC1 is recorded as FAIL, never amended. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` from `C:/dev/wk-resapp-491` on the committed bytes and report its verdict line.

Report once:
- the commit hash;
- AC1's output lines;
- per name (three), one line of what you saw;
- the walk's non-zero STEP lines, its OPEN-FIRST lines and its SUMMARY line, verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** PLACED cell of round 109 (decomposition s.118, edge `bp-1 -> bp-2`), cut STAGED at 2026-10-17 ~12:2xZ while `bp-1` (worker ~488) builds, so the GO needs only: (1) `AMGT-bp-1` complete and merged, with its candidate `cand/dell1/amgt-sa-changed-list-value` head named in the GO commit; (2) the issuer cuts `C:/dev/wk-resapp-491` with `.tools/wk-provision.sh provision AMGT_RESAPP 491 --path C:/dev/wk-resapp-491 --portal-ref cand/dell1/amgt-sa-changed-list-value --order <this order> --sparse-add .claude/skills/ui-walk`, starts `bun run dev:live --port 5174` in its nested portal, and confirms the walker account reads dormant (`ui_walker_account.py status`) and port 5174 free. CTO item 1 reads "re-run bo-3's AC5 walk on all 3 grids, on a local build of PROD first": read here as PROD plus the fix (s.118 (d)), because unpatched PROD is the known crash and PROD cannot carry the fix until Andrew promotes it; the walk on a candidate build is as close to PROD as the fix can be before that. The three names are bo-3 walk D's (VLO US, RIO LN, WALMEX* MM); the date-keyed draw does not apply (named names only). AC2 is JUDGMENT: the shot read, graded by the CVO and read by the CTO, never self-graded; the worker's one line per name is evidence for it. The pass for FWD-40 (d) needs this walk's AC1 count of 3 and the RIO LN Model tab rendering.

<status>staged</status>
<round>109</round>
<slot>0.9.0_WK_AMGT_RESAPP~491</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
