# AMGT_RESAPP task order -- `AMGT-rh-1` -- THE SERVED ROUTE, END TO END -- the last producer-side distance in this project

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rh-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~15</issued_to>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**You are `0.9.0_WK_AMGT_RESAPP~15`.** Work ONLY in the worktree whose absolute path is given to you
in your spawn prompt. **YOU HOLD ONE ORDER.**

⭐ **YOUR TOOLCHAIN IS ALREADY PROVISIONED AND THAT IS DELIBERATE.** `portal/node_modules` is a
junction to the main tree's installed packages -- **263 entries, with `typescript`, the `tsc` binary,
`vite`, `react` and `recharts` all resolving, verified before you were spawned.** Round 8's workers
correctly reported that their toolchain was missing; that was true of a fresh submodule clone and
**the issuer wrongly generalised it to the estate** (row `AMGT_RESAPP-Z-S66`). It is not missing. It
is here.

⛔ **AND THEREFORE: NEVER RUN AN INSTALL.** No `bun install`, no `npm install`, no `npx --package`
that fetches. The junction points at the **main tree's shared** `node_modules`, so an install would
write through it into a directory five other seats depend on. **You need no network for any criterion
in this order.** If something appears to be missing, that is a row, not an install.

## 1. THE CELL, inlined in full -- `AMGT-rh-1` (from the L10 round-8 analysis s.6, serving FWD-9 explicitly)

**THE COMPONENT IS PROVEN AND THE ROUTE IS NOT.** Round 7 measured the page joining **0 of 183**
fiscal figures. Round 8 repaired the join **at the component**, with the before/after control firing:
`PRE-REPAIR fiscal 0/183` against `REPAIRED fiscal 183/183`, header `13/13` holding on both arms. And
round 8 repaired the chart's incomplete read: `PRE-REPAIR absent == retry-exhausted` on equal hashes,
3 of 3 pairwise distinct after.

**Nobody has assembled those repairs into a route and run it.** The distance between "the component
returns the right answer" and "the application builds, compiles and serves with that component in it"
is the last producer-side gap in this project.

**DELIVER: the assembled route, exercised locally, against real captured data.**

⛔ **NO PROMOTE. NO GITLINK MOVE. NO REMOTE PUSH. NO DEV OR PROD MERGE.** Andrew-direct 03:21:46Z,
twice in one sentence: *"no promote"* and *"despite not pushing to promote until a future date."* A
local dev server is not a publish. **Commit yes, promote no.**

⛔ **WHAT THIS CELL DOES NOT CLAIM, AND YOU MUST NOT CLAIM IT EITHER: A BROWSER RENDER.** You hold no
browser-driving tool. Criteria that would need one -- pixels, navigation, visible marking -- are
**explicitly out of your scope and are exercised by `2.0.0_SA_COO~ZZZ`, which holds that instrument.**
Say so plainly in your instance. **A cell that claims a screen it cannot see is the defect this
project has spent two rounds removing.**

## 2. WHERE THIS CAME FROM

**ROUND 9**, cut from `1.0.0_SA_CTO~Z`'s L10 round-8 analysis @`f99eff5726` s.6, whose recommendation
reads: *"Exercise the full served route locally end to end against real data ... NO promote, NO
gitlink move, NO remote push. Its bar is a rendered route, not a passing test. Cover FWD-9
explicitly, because it is the only outcome whose bar a served page alone can close and it currently
carries the thinnest coverage in the whole set at one order."*

Coverage at that analysis: 46 orders, 15 outcomes declared, 15 covered, **uncovered EMPTY**, no PRD
addendum. **This is the only cell round 9 cuts.**

## 3. SURFACES -- what you may read and write

<paths>
portal/src/pages/SecurityAnalysis/
portal/src/api/endpoints/amgt-lead-panel.ts
lib/research/checkface/scopes.py
lib/research/checkface/run_checks.py
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rh-1.the-served-route-end-to-end.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** You are admitted to exactly those paths and nothing
  else (RULING 1). Do not route around a missing path; file a row and stop on that clause. Your
  `deliverables/0.9.0_WK_AMGT_RESAPP~15/` home needs no entry -- the tree convention grants it.
- ⭐ **`run_checks.py` IS NAMED HERE DELIBERATELY, AND THAT IS ROW `Z-W13-S3`'s REMEDY.** Round 8
  granted `scopes.py` as "the producer's identity contract", but `scopes.py` declares only the scope
  VOCABULARY -- the `figure_id` COMPOSITION lives in `run_checks.py:figure_id()`, which the grant did
  not name. **The round-8 worker read it anyway and DISCLOSED that it had**, which is what made it
  correctable. **The present exception disposition, recorded as the remedy requires: that read was
  outside its grant, correct source grounding does not retroactively supply one, and no producer-ID
  rewrite or worker recut is inferred from it.** Both files are READ-ONLY for you.
- `portal/node_modules` is a junction and is **NOT** a write surface.

## 4. PROOF OF SPEC -- one clause per criterion

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rh-1"><invocation>cd portal &amp;&amp; timeout 110 ./node_modules/.bin/tsc -b --force --listFiles --pretty false 2&gt;&amp;1 | tail -40</invocation><expect>the build examines the real program and emits NO `error TS` line. Print, beside the tail, the COUNT of source files the compiler listed -- pipe the same run through a counter and state the integer. STOP: a count of 0 or a small number is the VACUITY defect that let round 6 ship, where a `files: []` references-only root examined ZERO files and therefore could not fail; a count in the low thousands with no error is the met state. STOP: AND THIS CRITERION IS THE ONE THE ISSUER WRONGLY REPORTED AS BLOCKED ON REGISTRY EGRESS -- the compiler is present at `portal/node_modules/.bin/tsc`, verified before your spawn, so an ENOENT here is a FINDING and a row, never a reason to install anything</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rh-1"><invocation>cd portal &amp;&amp; timeout 110 ./node_modules/.bin/vite build --logLevel info 2&gt;&amp;1 | tail -30</invocation><expect>the PRODUCTION build completes and names the emitted bundle files with their sizes. STOP: print the count of emitted assets and the name of the chunk that contains the Security Analysis route, established by searching the build output or the emitted manifest -- a build that succeeds while emitting nothing for this route is the same vacuity one directory over. STOP: a non-zero exit, an unresolved import, or a missing SecurityAnalysis chunk is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rh-1"><invocation>cd portal &amp;&amp; (timeout 100 ./node_modules/.bin/vite --port 5175 --strictPort &gt; /tmp/rh1_vite.log 2&gt;&amp;1 &amp;) ; sleep 12; curl -sS -o /tmp/rh1_index.html -w "HTTP %{http_code} bytes %{size_download}\n" http://127.0.0.1:5175/ ; curl -sS -o /dev/null -w "NEG %{http_code}\n" http://127.0.0.1:5175/zzz-no-such-route-rh1 ; head -5 /tmp/rh1_vite.log</invocation><expect>`HTTP 200` with a non-zero byte count on the root, and the served document referencing the application entry module. STOP: PRINT THE NEGATIVE-CONTROL LINE TOO and say what it means -- a dev server that answers 200 for EVERY path, including the nonsense route, is a server that cannot discriminate, and in that case the 200 on the root is not evidence the route exists. STOP: the vite log's first lines must show the server bound to the port; a `strictPort` failure means something else holds 5175 and that is a row, not a retry on another port</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rh-1"><invocation>cd portal &amp;&amp; timeout 110 node src/pages/SecurityAnalysis/__harness__/join.harness.mjs 2&gt;&amp;1 | tail -20 &amp;&amp; timeout 110 node src/pages/SecurityAnalysis/__harness__/chart.harness.mjs 2&gt;&amp;1 | tail -20</invocation><expect>BOTH round-8 harnesses re-run IN THIS ASSEMBLED CHECKOUT and still print their repaired states with their negative controls FIRING: `PRE-REPAIR fiscal 0/183` against `REPAIRED fiscal 183/183` with header `13/13` on both arms, and `PRE-REPAIR absent == retry-exhausted` with equal hashes against 3 of 3 pairwise distinct. STOP: this is a REGRESSION check, not a re-derivation -- the numbers are round 8's and the question is whether ASSEMBLING the route changed them. A number that MOVES is the finding and is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rh-1"><invocation>cd portal &amp;&amp; for p in .bin/tsc react recharts vite typescript; do printf "%s %s\n" "$p" "$(test -e node_modules/$p &amp;&amp; echo PRESENT || echo ABSENT)"; done; printf "NEG %s\n" "$(test -e node_modules/zzznosuchpkg &amp;&amp; echo PRESENT || echo ABSENT)"; git status --porcelain -- src/pages/SecurityAnalysis/ | head -20; git -C .. ls-files -s portal | cut -c1-60</invocation><expect>all five toolchain markers reading `PRESENT` and the `NEG` line reading `ABSENT`, plus the superproject gitlink line reading `e85f6eb84f`, unmoved. STOP: PRESENCE IS THE INSTRUMENT HERE AND A COUNT IS NOT -- `portal/node_modules` is a DIRECTORY JUNCTION to the main tree, and `ls -1 node_modules | wc -l` reads **1** from this shell because it lists the junction itself rather than what it points at, while `test -e node_modules/react` resolves through it correctly. An entry count would fail for an instrument reason and prove nothing; the issuer measured that before this order was cut. STOP: THE NEG LINE IS WHAT MAKES THE FIVE PRESENT LINES EVIDENCE -- a probe that says PRESENT for a package that does not exist is a probe that says PRESENT for everything. STOP: a marker that reads ABSENT means something disturbed the shared junction and is a BLOCKING row, not a reason to install. A moved gitlink is a hard stop</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rh-1" judgment="true"/>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** `AC6` is a judgment
criterion: record it `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO~Z`, and
offer no verdict. It asks whether the assembled route is the thing a person would call working --
which is precisely the question an instrument you hold cannot answer.

**AND SAY PLAINLY IN YOUR INSTANCE WHAT THIS CELL DOES AND DOES NOT SETTLE:** it settles that the
repaired components COMPILE, BUILD and SERVE together and that their measured behaviour survives
assembly. **It does NOT settle that a human sees correct figures on a screen** -- no browser was
driven, and the outcome bars that need one remain open.

## 5. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~15/AMGT_RESAPP.TO-AMGT-rh-1.the-served-route-end-to-end.proof_of_spec.json`,
graded by **your worktree's own** `.tools/proof-of-spec-check.py` from inside that worktree; flip
`<status>` to `complete`; commit with `--only -- <paths>`. Report once in your final message. **If a
criterion cannot be met, leave the order OPEN and file a row** -- round 8's workers did exactly that
five times and every one of those refusals found a defect in the order rather than in the work.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES and restore from that snapshot. Never
`git checkout --`, never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>9</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>`1.0.0_SA_CTO~Z`'s L10 round-8 analysis @`f99eff5726`, s.6: "Exercise the full served route locally end to end against real data ... NO promote, NO gitlink move, NO remote push. Its bar is a rendered route, not a passing test. Cover FWD-9 explicitly." Coverage at that analysis: 46 orders, 15 declared, 15 covered, UNCOVERED EMPTY, FWD-99 control fires, PRD ACTION NONE. Cell set and subtraction: decomp s.17a over the FOUR OPEN remedy rows of `REMEDIATION_v8.md` @`a51f860e36`, read AT HEAD. Fan-out: decomp s.17d. Andrew-direct 03:21:46Z, VERBATIM: "all the wiring needs to be done" and "I expect frontend for both RESAPP and ASTTAX to be done too, despite not pushing to promote until a future date."</authority>

<preflight>
ALL THREE RUN 2026-09-13 ~04:0xZ, fresh this tick. None declared-not-applicable; each disposition
carries its own denominator and its own stated blindness.

comp-schedule: RUN -- 5 of 5 carriers scanned WITHIN BUDGET (10.359 s of 90 s); REACHED-DENOMINATORS
C1=23, C2=7, C3=12, C4=21, C5=334. C1 SENTINEL (7 gates), C2 DEPLOY-LEDGER (7) and C3 MORATORIA (12)
all DECIDABLE with every gate POSITIVE_RESULT; BLIND on C4 SCOPE-GUARD (SEMI-DECIDABLE, 0 of 21) and
C5 PROJECT-BLOCKING (NOT-DECIDABLE, 0 of 334), both PARTIAL_OR_BLIND in the tool's own voice, plus a
NEEDS-READ prose carrier of 128 more it refuses to count.
  WHAT IT MEANS FOR THIS CELL: nothing here is scheduled. The cell starts a LOCAL dev server and stops
  it; it publishes nothing and deploys nothing. The blind carriers are recorded because a
  decidable-on-3-of-5 result is not a clean scan.

comp-iam: RUN -- 838 call(s) verdicted across 97 mapped role(s): 629 UNRESOLVABLE-RESOURCE, 142
GRANTED, 51 GRANTED-BROAD, 14 UNGRANTED, 2 GRANTED-ACTION/UNGRANTED-RESOURCE; totals 15 missing, 291
deny-present, 1 coverage-unknown, 2 resource-mismatch across 32 service(s); BLIND on 266 call(s) in 26
role-UNMAPPED service(s), NOT resource-checked.
  The denominator is UNCHANGED from round 8's 838/97, which is the expected reading: round 8 registered
  no new Lambda call site and this cell registers none either.
  The tool's two self-declared holes are repeated rather than swallowed: 266 unmapped calls are "an
  honest hole, not a pass"; 51 GRANTED-BROAD rows are "EXCLUDED, NOT CLEARED". THIS CELL TAKES NO AWS
  ACT AND MAKES NO NETWORK CALL.

comp-adversary: RUN -- composed against the round-9 DECOMPOSITION (`compose <artifact> --no-packet`);
complement sources 4 run / 0 deferred-with-reason / 4 declared-excluded; 232 uncited directory siblings
with the display CAP of 25 DECLARED rather than silent. T11 DID NOT RESOLVE in the tool's own voice --
the artifact carries no `<decomp_ref>` because it IS the decomposition, so filesystem adjacency stood
as a WEAKER neighborhood and that is recorded as such. Stage 4 was DISABLED BY THE CALLER
(`--no-packet`), so the complement is POINTERS ONLY and that is a caller's choice, recorded. Its
freshness read returned `verdict: BEHIND` on a pinned source no cell in this round consumes; recorded
because a BEHIND verdict noticed and not recorded is the same as one never run. 14 hex runs were not
parsed as pins where 30 were, and the unparsed list is named rather than dropped.
</preflight>
