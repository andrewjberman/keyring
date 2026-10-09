# DSGN_AMGTV1 task order -- `AV-zzp-2` -- THE WALKER CAN PRESS ON /security-analysis AND SHOW THE RESULT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzp-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~139</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files, harnesses and issuer checks, run offline.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 against portal f043b827 (= origin DEV, round 63) -- r64b.cjs 2 of 4 (FLAGS and RECORDED FAIL as expected; GUARDED holds vacuously at the base, where no press path exists; PLANTED passes); battery29 ALL PASS at the base (round-63 candidates).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzp-2` (round 64, decomposition v64; serves FWD-27 and the layout outcomes)

Paths are under `portal/src/pages/SecurityAnalysis/`. Read `org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round63.md` section 2 first. Do the items in this order.

The CVO graded two presses as never exercised: a figure in the Investment-thesis window, and one of ASML's two listing buttons. Each
needs a press and a shot after it. `.claude/skills/ui-walk/walk.mjs` `walkSecurityAnalysis` (about line 532) has no press step; the
existing `--press` applies to plain routes only. This cell adds two read-only press flags. The network guard is unchanged: a press
issues only the GETs the page already makes.

1. **Flags** (the argv loop, about line 58), both repeatable:
   - `--security-press <css>` into `opt.securityPresses`;
   - `--window-press <css>` into `opt.windowPresses`.
2. **Security press** (`walkSecurityAnalysis`, right after `await checks(page, `${sec}-overlay`)`): for each css, find the first visible
   match.
   - None: push finding `walker:press-not-found`.
   - Its text matches `DO_NOT_CLICK`: push `walker:press-refused` and do not press.
   - Otherwise press it, wait for the page (`settle` about 2.5 s, then `waitForLoaded`), and run `checks(page, `${sec}-press-<k>`)`, so
     a shot of the after-state is taken.
3. **Window press** (when the Thesis tab is selected, before `exploreScope`): when `opt.windowPresses` is non-empty, open the
   Investment-thesis card (`[data-thesis-card="investment_thesis"]`) and run `checks(page, `${sec}-Thesis-window`)`. Then, for each css,
   look for the first visible match INSIDE the open dialog (`[role="dialog"]`), with the same not-found and refused rules.
   - Press it and wait about 1.5 s.
   - Read `document.activeElement` (tag, id, `data-thesis-passage`) and whether that element's top is inside the viewport.
   - Run `checks(page, `${sec}-Thesis-window-press-<k>`)`, then press Escape.
   - Append one record per press `{ security, css, pressed, focused: { tag, id, data_thesis_passage }, focused_in_view }` and write them
     to `window-press.json` beside `findings.json`.
4. **SKILL.md:** one short paragraph per flag in the invocation section, in the style of the `--press` paragraph.
5. **No other change:** no new `page.route`, no fetch, no change to the guard, DO_NOT_CLICK, arm/disarm or the other steps.

## 2. BOUNDS

1. No server, no fetch, no network, no install (`bun install`, `bun add`, `npm`, `npx` are refused here), no push, no deploy.
   REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. **Move and fold, never reword served text; never compute a figure the page does not serve** (C-PRESENTATION-ONLY).
   `reasonWords.ts` and `cscTable.ts` are not yours. No non-ASCII characters (use `--`). Keep each file's line endings as you find
   them (read them first). Edit tool for existing files.
4. Portal files commit inside `portal/` on your portal branch (set the author with `-c user.name=... -c user.email=...`; the nested repo
   has no identity), then the outer commit with safe-commit. Do not commit the portal gitlink.
5. If an item cannot be met within your paths, file a row and stop on that criterion. In particular, if battery29 goes red on a
   harness file outside your paths, file a row naming the harness and the assertion, and stop: the issuer rules it.

## 3. SURFACES

<paths>
.claude/skills/ui-walk/walk.mjs
.claude/skills/ui-walk/SKILL.md
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~139/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `.claude/skills/ui-walk/ui_walker_account.py` (never run its `secret` verb), and the issuer's check `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round64/checks/r64b.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzp-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round64/checks/r64b.cjs"; echo "exit=$?"</invocation><expect>ROUND 64 WALKER PRESS: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzp-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node --check .claude/skills/ui-walk/walk.mjs; echo "exit=$?"</invocation><expect>no syntax error printed -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzp-2" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded on the issuer's signed-in walk at the close (never self-graded): the issuer's walk shows, after a figure press, the cited passage focused and in view, and after an ASML listing press, that listing's page.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~139/DSGN_AMGTV1.TO-AV-zzp-2.proof_of_spec.json`
(AC3 UNVERIFIABLE-BY-INSTRUMENT, status_reason "graded at the round-64 close walk"). **Flip this order's `<status>` to `complete` in the
SAME commit as your proof instance**, only when AC1 and AC2 pass.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W139-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the diff (per file, one line each), the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 64 = `ledger/ROUND_ANALYSIS.round63.md` @f7d74e6665 section 2: item 1 is AV-zzp-1, and items 2-3 are the
issuer's close walk, made possible by AV-zzp-2 (the walker's press flags). Base portal f043b827 (= origin DEV). LF only (ruling R2,
row D1-S1).

<status>pending</status>
<round>64</round>
<to_id>DSGN_AMGTV1.TO-AV-zzp-2</to_id>
<slot>~139</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
