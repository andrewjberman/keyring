# AMGT_CORPUS task order -- `CRPS-ao-4` -- ROUND 39: the Model sheet shows FY+3 (2028E) unclipped at 1440 px

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ao-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task, alarm or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the check reads a fixture file.
comp-adversary: RUN by the issuer at the cut on portal origin/DEV e2130d42 -- ao4_check control 2/2. Blind spot: the check is the control only; the fit is graded on the issuer's real 1440 px walk (AC2).
EGRESS CLASS, declared: NONE. Portal source only. NO push of any portal branch: the DEV landing follows the CTO's render review.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 39, continuing in the same worktree after `CRPS-ao-3`.

**Your portal.** The same nested `portal/` repository and portal branch as `CRPS-ao-3`, carrying your ao-3 commits. Portal files
commit INSIDE `portal/` on that branch first, then the outer commit for the outer files. Never commit the portal gitlink.

## 1. THE CELL -- `CRPS-ao-4`

Outcome FWD-21: the Model tab's sheet shows the consensus years 2026E-2028E beside the history. At a 1440 px wide window the CVO
found 2028E clipped at the card's right edge on TSM and on ASML (on ASML, 2027E too). SAP and BA fit. The sheet is a `<table
data-model-sheet className="w-full">` inside `<div className="overflow-x-auto">` (`portal/src/pages/SecurityAnalysis/tabs/
ModelTab.tsx`, about lines 480-481): 10 history years plus 3 estimate years plus the label column, at 14 px with `px-1` cells and
a `whitespace-nowrap` label column (about 526). Large figures (TSM in TWD millions) widen every column.

**Build, in the sheet's layout only:**
1. At 1440 px the whole table, 2028E included, is visible inside the card on TSM and ASML without a horizontal scroll. Choose the
   least change that does it, for example: a compact number form for the sheet's figure cells (the full value stays in the cell's
   tooltip and `data-full-value`, as now), a tighter cell padding, or a wrapping label column. The history columns stay.
2. No figure value, row, label, year or reason changes, and no column is dropped. `data-model-cell` and `data-full-value` keep
   the full served value.
3. **Colour law** (`portal/CLAUDE.md`): navy ink on the light canvas and white panels; reuse the existing classes.

## 2. BOUNDS

1. NO push of any branch, NO deploy, NO AWS call. Do NOT arm the walker or run `.claude/skills/ui-walk/walk.mjs`: the account is
   shared across devices and its slot is the issuer's. You MAY render with the portal's own headless screenshot
   (`portal/scripts/ui-smoke.mjs`, auth-stubbed) to look at your change. Typecheck with `bun run typecheck` inside `portal/`.
2. Only the files in `<paths>` change. Never edit the issuer's checks, fixtures or snapshots, or any `__harness__/` file.
3. Write code with the Edit/Write tools, never a shell heredoc. ASCII only.
4. Rows are `AMGT_CORPUS-Z-W2-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner
   2.0.0_SA_COO~X` and `surfaced_at` from `date -u +%FT%TZ` at filing.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/modelSheet.ts
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-ao-4.sheet-fits-fy3-at-1440.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ao-4.sheet-fits-fy3-at-1440.md
</paths>

Read-only: the whole repository, in particular `portal/CLAUDE.md`, `portal/DESIGN.md` and the issuer's checks under
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round39/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ao-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round39/ao4_check.cjs" portal</invocation><expect>(?m)^ao4 control 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ao-4" judgment="true"/>
</proof_of_spec>

- AC1 (the real `modelSheet.ts` on TSM, BA and ASML captured from the real read path): control -- the history sheet and the full
  sheet (years and every figure value) are unchanged.
- AC2 (JUDGMENT, graded by the CVO at L9 on the issuer's real 1440 px walk of TSM and ASML): 2028E is visible, unclipped, with
  the history beside it. Record it as `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO~Z`; no verdict.

## 5. WHEN YOU ARE DONE

1. Inside `portal/`, run `bun run typecheck` (clean) and `node src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs`.
   Re-run ao-3's three `ao3_check.cjs` arms: they still read build 1/1 control 1/1.
2. Write the instance at the proof path, with its mutant control from the start. Then run `python .tools/proof-of-spec-check.py
   <instance> AC1,AC2 --governing-order <this order>` AFTER your final commit. It must return rc 0.
3. Only if AC1 passes, append a new status tag reading complete at the END of this file, in the SAME outer commit as your proof
   instance.
4. Report ONCE: the layout change and why it fits, AC1's output line, the typecheck, harness and ao3 lines, your portal and outer
   commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-38 analysis @`9619211bcf` ruling 5 + s.4 item 3; CVO `ADJUDICATION_v44.md` FWD-21. Base portal
origin/DEV e2130d42: ao4 control 2/2. Queued behind ao-3 on slot ~2 (same write set). The fit is graded on CRPS-ao-5's walk.
<risk>LOCAL</risk>
<status>pending</status>
<round>39</round>
<slot>~2</slot>
<fabric>site-z</fabric>
