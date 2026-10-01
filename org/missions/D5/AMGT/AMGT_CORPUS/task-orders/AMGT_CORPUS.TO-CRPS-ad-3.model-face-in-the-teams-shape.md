# AMGT_CORPUS task order -- `CRPS-ad-3` -- ROUND 28: the Model face carries the team's shape, its forecasts, and never contradicts itself

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ad-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV a41cf763 -- face.cjs 2 of 8 (FAIL as designed: arms 3 and 6 are controls and pass at base); bound 4 of 4 green at base; tsc -b rc 0. Arm 8 needs CRPS-ad-1's forecast parameter, so this order starts on a worktree carrying ad-1's merged head. Blind spots: one name (BA) and in-memory variants of it; static render only; "figure" on the bare face is a digit test inside the case, team-case and score blocks.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 28, second order (after `CRPS-ad-1`). Serves FWD-12 (the team's shape),
FWD-21 (the forecasts on the page) and FWD-15 (one face, no contradiction). By CONTRACT amendment 1 (CTO msg 27546) AMGT_CORPUS is the
one writer of `ModelTab.tsx` through the Friday freeze; DSGN does not edit it.

## 1. THE CELL -- `CRPS-ad-3`

In `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx`:
1. **No score tiles.** `ScoreTiles` (Robustness, Peer valuation, Divergence) is rendered on neither the SERVED nor the ABSENT face.
2. **No Opal rule lines.** `CasesBlock` / `ModelCaseLine` (the "Opal's rule-based upside/base/downside" and "Opal's
   historical-multiple reference ..." lines) are rendered on neither face. The research team's own Upside / Base / Downside cases
   (`TeamBase`) still render exactly as the team's.
3. **The forecasts.** Pass the served `data.model?.forecast_figures` as the fourth argument of `buildModelSheet` (the parameter
   `CRPS-ad-1` added); the sheet's header then shows the `2026E`-`2028E` columns and their cells render through the same cell
   component as the history.
4. **One face (CVO v16 k-5, DSGN round-14 ruling 1, moved here).** On the ABSENT face, a figure is shown with its label, or the empty
   sentence is shown, never both: the face never says "No figure, case or estimate is shown" while a team figure is on it. A bare
   ABSENT face (no team case served) still says there is no model.
5. **No presupposed pack (COO~D msg 27552).** BA's served reasons say there is no pack (`model.reason` "no landed model block for this
   name"; the team cases' class-A report is missing). The ABSENT face's words follow the served reason: it never says something is
   missing "in the research pack" or "in this pack".
6. Words a PM reads: nothing on the face reads "ABSENT", "REFUSED" or "not read" (FWD-20).

**Harness re-anchor, NECESSARY, granted.** `__harness__/modelPattern.harness.cjs` anchors `score_tiles` (= 3), `score_empty_state` and
`year_heads` (the fixture's fiscal years), and `__harness__/tabs.harness.cjs:384` counts sheet cells against the fiscal figure count.
Items 1 and 3 break them by design. Re-anchor each such check onto the SAME fact it guards in the new shape (no score tile renders;
the header's years are the sheet's years including the E columns; the history cells equal the fiscal count), keep its claim, and keep
each harness at or above its floor (modelPattern 12, tabs 20). Never drop a check. Edit no other harness.

**The rules every cell keeps (PRD CONTRACTS):** C-PRESENTATION-ONLY -- the page derives nothing. **Design law (portal `DESIGN.md`):**
a code, field name or path may sit in a data attribute or in code, never in visible text.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change. Do not edit `modelSheet.ts` (ad-1's, merged).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`; a heredoc on this machine turns `\b` into a
   0x08 byte.
5. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k), with `disarm_owner 2.0.0_SA_COO~X`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-ad-3.model-face-in-the-teams-shape.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ad-3.model-face-in-the-teams-shape.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md`, `portal/src/pages/SecurityAnalysis/modelSheet.ts`, the issuer's
checks under `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round28/` and DSGN's loader and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 300)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ad-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round28/face.cjs"; echo "exit=$?"</invocation><expect>THE MODEL FACE IN THE TEAM'S SHAPE: 8 of 8 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ad-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bound.cjs" AD3 modelPattern.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10 errorEmpty.harness.cjs:12; echo "exit=$?"</invocation><expect>AD3 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-ad-3"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node_modules/.bin/tsc -b --noEmit; echo "exit=$?"</invocation><expect>(?m)^exit=0$</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-ad-3" judgment="true"/>
</proof_of_spec>

- AC1 (`face.cjs`, eight arms on BA's served `/thesis` capture and in-memory variants): no score tile and no Opal rule line on the
  SERVED face (1) or the ABSENT face (2); the three team cases still render on both (3); with the team's Base case served on an
  ABSENT face, its figures show and the face does not claim "No figure, case or estimate is shown" (4); a bare ABSENT face says there
  is no model and shows no figure (5); no "ABSENT" / "REFUSED" / "not read" on any face (6); the ABSENT faces never say "in the research
  pack" / "in this pack" (7); BA's sheet header carries 2026E-2028E and the served forecasts add at least 17 sheet cells (8).
- AC2: the page's harnesses that load the Model tab stay green at their floors (after your granted re-anchors).
- AC3: the portal typechecks.
- AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's real run (BA's Model tab on the local DEV build), never
  self-graded: the Model tab reads like the analyst's SharePoint sheet.

## 5. WHEN YOU ARE DONE

1. Write the instance at the proof path in section 3.
2. Run `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` AFTER your final commit, and pin
   each artifact row to the commit whose BYTES you graded (verify with `git show <pin>:<path>`). It must return rc 0.
3. Only if every mechanical criterion passes, append a new status tag reading complete at the END of this file, in the SAME commit as
   your proof instance.
4. Report ONCE: what changed and where (the visible wording on the ABSENT face), each harness re-anchor (old check -> new check), the
   output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-27 analysis s.3 item 3 @`99b83b495a`; CONTRACT amendment 1 @`c7f9fa44fa`; COO~D msg 27552 (pack wording).
Base portal DEV `a41cf763`: face.cjs 2 of 8; bound 4 of 4; tsc rc 0. Handed to slot ~1 after ad-1 drains, on a worktree carrying
ad-1's merged head. `exportCompare.harness.cjs` reads RED at base (rc 2) and is outside the bound.
<risk>LOCAL</risk>
<status>pending</status>
<round>28</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<worker_class>worker</worker_class>
<status>complete</status>
