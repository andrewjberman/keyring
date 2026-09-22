# AMGT_RESAPP task order -- `AMGT-rk-125` -- the LIVE-ORIGIN RENDER READ: capture what a viewer actually sees on the Security Analysis page for `BA_US_Equity` then `992_HK_Equity`, per tab, and measure whether a failed read is LEGIBLE or SILENT. READ-ONLY -- writes no code, no portal file, no AWS object

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-125</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~125</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell arms no cron, alarm, monitor or cadence and runs no producer.
  It renders a page and reads the result.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, trust or grant is edited, and no credential is minted. The
  capture runs with the instrument's INERT stub session; the live API refuses it, which is the measurement.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~125`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt.
First act: print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~125;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

⛔ **RUN THE INSTRUMENT FROM THE SHARED TREE'S `portal/`, NOT FROM YOUR WORKTREE, AND THIS IS MEASURED.**
`portal` is a gitlink with **no `.gitmodules` mapping**, so a fresh worktree's `portal/` is **EMPTY (0 entries** --
the issuer exercised it at this cut). Even with a portal worktree added, `node_modules/` is gitignored and would be
**absent**, and `ui-smoke.mjs` imports `playwright-core` -- so the capture could only run after an install, and you
may not install. **The shared tree's `portal/node_modules/playwright-core` EXISTS and is what you use.** Running a
script there WRITES NO TRACKED FILE; your own outputs go to your deliverables. **You may not edit any portal file.**

⛔ **RESOLVE `bun`/`node` -- NEVER BAKE A PATH.** The `/frontend-dev` skill hardcodes
`/c/Users/AndrewBerman/.bun/bin/bun`, which is **the OTHER DEVICE'S** path and does not exist here; on this box
`bun` resolves via WinGet and `node` is v26.9.0. Use `command -v node`.

## 1. THE CELL -- `AMGT-rk-125` (round 31, decomposition s.39b)

**THE QUESTION.** `rk-123` fixed the CDN route, and `1.0.0_SA_CTO~Z`'s round-30 analysis holds the line that
**THE PAGE IS NOT GRADED AS RENDERING** until someone looks at it: *"Andrew reported a BLANK PAGE. A route fix
answers the fault we MEASURED, not the symptom he SAW -- and those are the same thing only if there is exactly ONE
fault, which nothing has tested."* This cell looks.

**WHAT THE ISSUER ALREADY MEASURED AT THE CUT, exercising your AC1 invocation once** (evidence PNG committed at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round31_cut_evidence/live_origin_unauthenticated_20260922T2240Z.png`):

- ⭐ **THE PAGE IS NO LONGER BLANK.** Chrome, sidebar, title, Lead Panel and all five tab headers render.
- ⭐ **The Lead Panel's read-failure block WORKS and NAMES THE FAULT:** *"Read failure -- the ranked names could
  not be read ... Error reported by the read: API request failed: 401 - {"error":"Invalid or expired token"}"*.
  That is `AMGT-ri-1`'s block (`RankedList.tsx:139-160`) doing exactly its job.
- **The tab body reads "Select a name from the Lead Panel to open its Thesis."** -- the NO-SELECTION state, not an
  error state, because the Lead Panel never loaded a name to select.
- ⚠ **`LOC` printed `/security-analysis` with NO query string**, so the `?security=...` form did NOT select a name.
  **Finding the form that actually selects a security is the first thing you do** -- until a name is selected, the
  five tabs are never exercised and this cell answers nothing about them.

**THE ACT.** Capture and READ, in this order:
1. `BA_US_Equity` FIRST (the CTO's instruction: **7 of 7** surfaces populated, against Lenovo's 5 of 7 -- so it is
   the name that can show content), then `992_HK_Equity`.
2. For each name, get a security SELECTED, then capture **each of the five tabs** -- thesis, exec_management,
   peers, model, posture (`constants.ts:72-78` declares exactly these five).
3. **READ every PNG with your own eyes** (the Read tool). A screenshot nobody looked at is not evidence.
4. For each of the 10 captures record: does the tab render CONTENT, an ABSENCE sentence, or an EMPTY panel with no
   explanation? **Quote the rendered text.**

⭐ **THE DISCRIMINATOR THIS CELL EXISTS FOR:** `0 of 5` tabs carry an `isError` branch (row `Z-S227`; a
case-insensitive search for `isError|error` across `tabs/` returns **zero**). So for a tab, **a failed read and a
genuinely absent object are byte-identical to a viewer.** The Lead Panel proves the contrast in the SAME capture --
it says `401`, the tabs cannot. **Your report must state, per tab, whether a viewer could tell the difference.**
⚠ **DO NOT be fooled by the string `READ_FAILED` in `PostureTab:323` / `ExecManagementTab:147`** -- that is the
SERVER's status field on a payload that was read SUCCESSFULLY, not a client fetch-failure branch, and it does not
fire when the HTTP read itself fails.

## 2. BOUNDS -- what this cell may NOT do

- ⛔ **NO CREDENTIAL IS MINTED AND NONE IS USED.** `ui-smoke.mjs` supports `--token <jwt|@file>` for a REAL bearer,
  but **the issuer censused the estate and found no in-repo route that mints a portal RS256 token** (every
  `mint_token` hit is a SmartX/vendor token). **So the FULLY AUTHENTICATED read is NOT this cell**, is carded to
  `1.0.0_SA_CTO~Z`, and you must not go looking for a key, a secret or a session to forge one. **If you cannot see
  a tab's authenticated state, that is the honest result -- report it, do not engineer around it.**
- **Read-only.** No code edit, no portal edit, no AWS write, no deploy, no vendor call, zero egress off Opal.
- You write ONLY your deliverables and, if warranted, surprise rows.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~125/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
.scratch/r125/**
</paths>

⚠ **`portal/**` is ABSENT ON PURPOSE.** It is lane `POD_DE_ANY` (`.owned-paths.yaml:1944-1946`), which the ISSUING
seat does not hold; naming it would admit you through the `worker_grant` with no lane consulted, which CVO ruling R5
forbids. You RUN a script that lives there; you do not WRITE there.

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-125"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; command -v node &amp;&amp; node --version &amp;&amp; ls -d portal/node_modules/playwright-core &amp;&amp; ls -l portal/scripts/ui-smoke.mjs</invocation><expect>node resolves and prints its version; portal/node_modules/playwright-core EXISTS; ui-smoke.mjs exists. If playwright-core is ABSENT, STOP with a BLOCKING row -- you may not install it, and the cell cannot run</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-125"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-smoke.mjs "security-analysis" "$(git rev-parse --show-toplevel)/.scratch/r125/base_live.png" --origin https://opalinvest.dev 2&gt;&amp;1 | tail -8</invocation><expect>the capture succeeds and prints IDENTITY, VIEWPORT, LOC, CANVAS and SAVED. CANVAS reads rgb(244, 246, 250). Record LOC verbatim. This reproduces the issuer's cut-time capture and is your control that the instrument works before you vary anything</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-125"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r125/ac2.py</invocation><expect>the MEASURED way a security is selected: print the route/param form the page actually honours, evidenced from portal/src/pages/SecurityAnalysis/SecurityAnalysis.tsx and its router registration -- file:line for each. State plainly whether a URL form CAN select a name, or whether selection is only reachable by CLICKING the Lead Panel. If it is click-only, say so; that is a finding about the instrument's reach, not a failure</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-125"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; ls -1 .scratch/r125/*.png | wc -l &amp;&amp; ls -1 .scratch/r125/*.png</invocation><expect>the capture set you actually produced, listed. TARGET is 10 (2 names x 5 tabs); FEWER IS ACCEPTABLE ONLY WITH A NAMED REASON PER MISSING CAPTURE -- e.g. selection proved click-only and a click could not be driven. A short list with reasons is a result; a short list without them is not</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-125"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; cat org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~125/RENDER_READ.md</invocation><expect>one row per capture: name, tab, what rendered (CONTENT / ABSENCE-WITH-REASON / EMPTY-NO-EXPLANATION), and the QUOTED on-screen text. Plus the verdict this cell exists for, stated per tab: COULD A VIEWER TELL A FAILED READ FROM AN ABSENT OBJECT? Plus the Lead Panel's own behaviour as the positive control, quoted. You must have READ each PNG -- say so</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-125"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; git status --short -- portal &amp;&amp; git -C portal status --short</invocation><expect>BOTH are EMPTY. This cell wrote no portal file, tracked or untracked. A non-empty result is a BLOCKING row against yourself</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~125/AMGT_RESAPP.TO-AMGT-rk-125.live-render-read.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance>
AC0,AC1,AC2,AC3,AC4,AC5` run from inside it (rc 0 is the verdict), then flip `<status>` to `complete` only if every
criterion PASSES. Report once, naming: AC2's selection finding, the capture count with reasons for any missing, and
the per-tab legibility verdict.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**

1. **This cell was DE-SCOPED FROM "the authenticated end-to-end read" at the cut, on evidence.** The CTO ranked that
   second. It needs a real RS256 bearer, and the estate census found **no in-repo minting route**. Cutting a cell
   whose acceptance depends on a credential nobody has is the `Z-S235` defect in its purest form, so the cell was
   narrowed to what IS reachable and the credential question was carded instead.
2. **The issuer exercised AC1 before issuing** and the capture is committed as cut evidence. That is the adopted
   remedy: the literal ran, rc=0, and its output is in the order.
3. **The headline from that exercise is worth more than the cell:** the page is NOT blank, and the Lead Panel names
   a 401 in plain language. **What remains unproven is the five tabs**, which is exactly `Z-S227`.
4. **A second, already-documented divergence is visible in the capture and is NOT this cell's:** the Lead Panel and
   the tab body render as dark navy BANDS while `portal/DESIGN.md` C3 allows ONE band per page over a light canvas.
   `portal/CLAUDE.md` already records this (`Panel variant="chart"/"mixed"` resolve to the band; 4,887 dependent
   light-on-dark idioms) and calls such a page the defect. Named here so nobody reports it as new.

<status>pending</status>
<round>31</round>
<slot>~125</slot>
<fabric>site-z</fabric>
