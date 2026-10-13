# AMGT_RESAPP task order -- `AMGT-bk-3` -- THE HEADER RENDERS USD AS `$` IN EVERY PAGE FORMATTER, AND EVERY DASH TILE SHOWS ITS REASON IN VISIBLE WORDS (A PORTAL BUILD; STAFF-ONLY PAGE; NO API FIELD MOVES)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bk-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~416</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bk-3.the-header-renders-usd-as-a-dollar-sign-and-every-dash-tile-shows-its-reason</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a portal change; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- the walker arms and disarms the dormant UI-walker account under its own lease; no grant is changed by this order.
comp-adversary: RUN at the cut -- `r104_walk_classes.py --selftest` reads YES (3 arms); `r104_walk_classes.py` on round 103's three walk folders reads `format:money` once in EACH (the control: the instrument sees the fault this cell removes); `r103_feature_green_v2.sh` is the round-103 non-regression instrument (YES at PROD 15c9754975).
EGRESS CLASS, declared: the dev server's reads of the live services through the deployed front door (GET/HEAD/OPTIONS only: the walker's guard aborts any other request).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-416` (branch `wk-AMGT_RESAPP-416`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-416`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bk-3` (round 104, decomposition s.113)

CTO round-103 analysis item 2 (i) and (ii), and his ruling (msg 5244 (i)): the page renders USD as `$`, PAGE-SIDE; the research team's prose and publishers' headlines are never rewritten. FWD-40 (a) (PRD v0.44, ratified): every section shows content OR a stated reason, and 0 broken values; the CVO confirmed four `format:money` hits (the header prints `USD 453.31` while the team's text prints `$41bn`: TSM US, MA US, CDNS US, UBER US) and found bare `--` header tiles on TSM US, HSBA LN and AZN LN that are neither content nor a stated reason.

Your nested portal worktree is `C:/dev/wk-resapp-416/portal`, at portal DEV `24877b67` on branch `wk-AMGT_RESAPP-416-portal`. Page: `src/pages/SecurityAnalysis/`. TWO changes, and only these:

**(1) USD prints as `$`.** Three formatters build `<code> <amount>`: `components/StatTile.tsx` (`priced`, about line 84), `components/HeaderCards.tsx` (about line 84) and `components/model/WhatChangedPanel.tsx` (about line 198); find any other place the page builds a money string from a currency CODE (search the page for the pattern `currency` followed by an amount). For the currency code `USD` print `$` immediately before the amount with no space (`USD 453.31` becomes `$453.31`, `USD 2.35T` becomes `$2.35T`, `USD 14.72B` becomes `$14.72B`); every OTHER code is unchanged (`EUR 72.09` stays `EUR 72.09`, `GBp 12,052` stays as it is). The tooltips (`figureTooltipRows`) and every served value are untouched. The comment in `StatTile.tsx` that says the page never prints a `$` it was not served is updated: the currency IS served, as `USD`.

**(2) A dash tile says why, in visible words.** A tile whose body reads `--` (its figure absent, its unit unresolved, or its currency unmeasured: `StatTile.tsx` `formatStatValue` returns null, and the reason today is on hover only) shows its reason as a short line of text directly under the dash, in an element carrying `data-stat-reason`. The words: for an unmeasured currency (`isUnmeasuredBasis`) the existing `CURRENCY_UNCONFIRMED_WORDS`; for an unresolved unit the existing `UNIT_NOT_RESOLVED_WORDS`; for a figure the payload does not carry, `Not served for this name`. Reuse those constants; invent no new wording beyond that one phrase. A tile with a number shows no reason line.

**Add ONE harness**, `src/pages/SecurityAnalysis/__harness__/tileMoneyAndReasons.harness.cjs`, in the pattern of `shell.harness.cjs` (the page's own components transpiled with the INSTALLED typescript and rendered by `react-dom/server`; read that file's header and loader first and copy its shape). It must print `CHECKS-OK <n> of <n>` and check at least: (a) a USD price tile renders `$` plus the amount and contains no `USD `; (b) a EUR price tile renders `EUR ` plus the amount unchanged; (c) a USD absolute-currency tile (`currency-abs`) renders `$`; (d) an unmeasured-currency tile renders `--` and a `data-stat-reason` element holding `CURRENCY_UNCONFIRMED_WORDS`; (e) an unresolved-unit tile holds `UNIT_NOT_RESOLVED_WORDS` in `data-stat-reason`; (f) a tile with no figure renders `--` and `Not served for this name`; (g) a tile with a number has no `data-stat-reason`. Run the harness once against the UNCHANGED page first and record that it FAILS there (the control), then make the two changes.

Then run the three criteria. AC3 starts the dev build yourself: `cd C:/dev/wk-resapp-416/portal && bun run dev:live --port 5174` in the background (first read `netstat -ano | grep :5174` and STOP with a BLOCKING row if anything listens: never another port), wait until `curl -s -o /dev/null -w "%{http_code}" http://localhost:5174/` reads 200, run the walks, and STOP the server you started when done (only the process you started).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-416/portal`, branch `wk-AMGT_RESAPP-416-portal` from DEV `24877b67`; never push; never touch `DEV` or `PROD`; no `bun install` (`node_modules` is a link to the main checkout's).
2. Edit only files under `src/pages/SecurityAnalysis/` (the harness included). Never `package.json`, `bun.lock`, `src/lib/firmAccess.ts` or a file of another page. No new dependency.
3. The walker is `.claude/skills/ui-walk/walk.mjs` run as written; it arms and disarms the dormant account itself. If a walk prints `HELD by` instead of `ARMED`, STOP and file a BLOCKING row; never `disarm` a holder that is not yours. A log reading `ERROR login did not complete (still on /login)` disarmed itself: run that walk once more; a second failure is a BLOCKING row.
4. Never commit a screenshot or a walk output folder (`tmp/ui-walk` is gitignored); never paste one into a message. Port 5174 only.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~416/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bk-3"><invocation>cd C:/dev/wk-resapp-416 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_green_v2.sh" "C:/dev/wk-resapp-416/portal" 24877b67 | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness P of T pass, base Q of U, regressions 0, pre-existing: <names>)` with T equal to U plus one (your new harness); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bk-3"><invocation>cd C:/dev/wk-resapp-416/portal &amp;&amp; timeout 120 node src/pages/SecurityAnalysis/__harness__/tileMoneyAndReasons.harness.cjs | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `CHECKS-OK N of N` with N at least 7; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bk-3"><invocation>cd C:/dev/wk-resapp-416 &amp;&amp; timeout 590 node ".claude/skills/ui-walk/walk.mjs" --route /security-analysis --security "TSM US" --security "MA US" --security "CDNS US" --security "UBER US" --max-minutes 9 > "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~416/walk_money.txt" 2>&amp;1; echo "exit=$?"; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round104_prep/checks/r104_walk_classes.py" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~416/walk_money.txt"</invocation><expect>`exit=0`, then a `WALK walk_money.txt` line listing every finding class of the walk and the line `R104 MONEY FORMAT: YES (format:money 0 in 1 walk(s))`; and exit=0 from the classes script</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~416 <0.9.0_WK_AMGT_RESAPP~416@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~416/AMGT_RESAPP.TO-AMGT-bk-3.the-header-renders-usd-as-a-dollar-sign-and-every-dash-tile-shows-its-reason.proof_of_spec.json` with `to_id` equal to the `<to_id>` line above, character for character; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters; if the checker refuses the instance for a missing `decomp_ref`, add it from the order's own `<decomp_ref>` block. Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first (cwd `C:/dev/wk-resapp-416/portal`, the same `safe-commit.sh` from the outer checkout's `.tools`, the paths relative to the portal root), then the deliverables in `C:/dev/wk-resapp-416`; do not stage `portal` in the outer worktree.

Report once:
- the commit hash of the portal branch (nested worktree) and of the outer worktree;
- AC1's, AC2's and AC3's output lines, AC3 including the whole `WALK` line;
- the new harness's FAIL at the unchanged page (the control), with its failing check names;
- the list of every file you changed and, for each money formatter, its path and line;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO RULINGS 5244 (i): page-side, the team's prose untouched. A page-side change on a staff-only page (`requireInternal`): it needs no word from Andrew; the candidate lands on DEV and reaches PROD by the portal release seat. The nested branch is a CANDIDATE: the issuer asks the CTO for the DEV landing at the merge. bk-3's walk checks the four names the CVO confirmed; the full re-walk (ten names) and the 93-name census are bk-5, cut when this is on PROD. The money check is the walker's own (`format:money`: `USD <digit>` AND `$<digit>` on one page): the page may still carry `$` in prose; it must carry no `USD <digit>`. `GBp` and other codes are untouched by design. PROD `10e7664d`, DEV `24877b67` at the cut; the SA page files are equal on both.

<status>pending</status>
<round>104</round>
<slot>0.9.0_WK_AMGT_RESAPP~416</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
