# MDPF_CANON task order -- `CN-s-4` -- THE VARIANT 2 MODELS BAND IS NEVER CARRIED FORWARD ON OR AFTER THE PER-MODEL BOUNDARY (FWD-9 head a; PORTAL CANDIDATE, CLIENT-FACING AT THE LANDING)


<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-s-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~31</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; one portal source file.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS contact at all (the checks run `bun` on a pure module and on a fixture of a served object that is committed).
comp-adversary: RUN by the issuer on DELL1 at the base (portal DEV 39dab87f3b) -- `r11_cn_s_4.py pure` pure 4 of 6 (S1 and S2 red), `real` real 3 of 5 (R2 and R3 red: 9 of 498 rows draw the band with a model line, and the stack exceeds the Total on all 9 carried dates); a scratch reference reads green on every arm; planted mutants (the band carried again, a model line dropped from the carried row) each turn their named arm red; `selftest` prints OK.
EGRESS CLASS, declared: none.
</preflight>

**Your worktree:** the spawn names it (outer branch `wk-MDPF_CANON-31`, cut from the issuance commit). The portal is a NESTED repository at `<worktree>/portal`, provisioned on its own branch `wk-MDPF_CANON-31-portal` cut from portal `DEV` at the `portal_ref` the issuance commit names (`39dab87f3b`). `node_modules` is linked. Start every shell call with `cd` into the outer worktree path.
**Line endings: `src/lib/trendGrouping.ts` is CRLF in EVERY line. Keep it.** A multi-line text you insert must end each line with CRLF (after your edits run `git -C "<worktree>/portal" diff --stat` and check that no line is LF-only).

## 1. THE CELL -- `CN-s-4` (round 11)

**The cell, verbatim from the decomposition:** the Variant 2 Models band is never carried forward on or after `per_model_detail_begins`: a non-internal Global session draws the band only before the boundary, and on the 9 carried dates after it no row draws the band together with the model stack, so the drawn stack never exceeds the served Total (one condition in the roll-forward loop of `buildGlobalTrendRows`).

**The defect (row MDPF_CANON-D1-S29):** `buildGlobalTrendRows(served, stitch, mode, begins)` in `portal/src/lib/trendGrouping.ts` sets the Models band only when `mode === 'variant2'` and the period is before `begins` (the fold's `per_model_detail_begins`, 2026-05-15). But the loop that rolls a null FORWARD on a carried date also rolls the last known band onto a carried date AFTER the boundary, beside the five model lines that are drawn there: on the 9 carried dates the stack (band + lines + groups) is drawn above the served Total. Find the roll-forward loop (around lines 230-260 at the base) and add the one condition that stops the band label (`MODELS_BAND_LABEL`) from being carried to a period on or after `begins`. Nothing else changes: the five primary lines, Custom Models, the three groups and the Variant 1 path keep their behaviour. The check's scratch reference shows an expected shape of the edit: read the `selftest` code in `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/r11_cn_s_4.py` (it applies the repair to a temp copy); you may use that edit.

## 2. BOUNDS

1. You change `portal/src/lib/trendGrouping.ts` and nothing else in the portal (a new `src/lib/trendGrouping*.test.ts` is allowed). `ModelPortfolios.tsx` is NOT yours in this order (CN-s-5 and CN-s-3, queued behind you, edit it).
2. The page does NO arithmetic on a served value: do not recompute the Total or a group, do not round a served value, do not fill a null with 0.
3. A non-internal session must not receive a single-firm value by any route: unchanged.
4. No AWS contact, no deploy, no push, no `bun install`, no browser launch.
5. **CLIENT DATA:** never print a client figure or an account id in your report, a row or a file.
6. No non-ASCII character in any line you add. Use the Edit tool; keep CRLF.
7. Do not edit the issuer's checks or the committed fixtures under `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/`. If a step cannot be done as written, file a row naming the step and stop on that step.
8. Do not run repo-wide hygiene as a criterion (the issuer runs the type check and the real run at the drain). Write the code so it type-checks: the module's interfaces are strict.

## 3. SURFACES

<paths>
portal/src/lib/trendGrouping.ts
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-s-4.variant2-band-not-carried.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~31/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/` (the check and `ref/`).

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-s-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 120 python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/r11_cn_s_4.py" pure; echo "exit=$?"</invocation><expect>ROUND 11 CN-S-4 PURE: 6 of 6 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-s-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 120 python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/r11_cn_s_4.py" real; echo "exit=$?"</invocation><expect>ROUND 11 CN-S-4 REAL: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-s-4" judgment="true"/>
</proof_of_spec>

AC1 runs the pure module under `bun` on a small fixture; AC2 runs it on the committed copy of the real served Global object (the issuer fetched it read-only; it is the object as served 2026-10-15) and asserts that no row draws the band together with the model stack and that no drawn group is above the Total on the 9 carried dates. They cannot prove what the page DRAWS. AC3 is JUDGMENT, graded at the round close (never self-graded): the issuer renders the Global Trend for a non-internal session at a STATED portal commit on `bun run dev:live --port 5174` and looks at the 9 carried dates. You do not render.

## 5. WHEN YOU ARE DONE

1. Commit `portal/src/lib/trendGrouping.ts` (and a test file if you wrote one) INSIDE the nested repo as ONE portal commit for this cell (CN-s-5 follows as a SEPARATE commit on the same branch, so this one can ship alone): `git -C "<worktree>/portal" add -- <those paths>` then `git -C "<worktree>/portal" commit --author "0.9.0_WK_MDPF_CANON~31 <0.9.0_WK_MDPF_CANON~31@opal.agent>" -F <msgfile>` (message file written with the Write tool). If a portal hook refuses, file a row with its text and stop: do not bypass it.
2. Write the proof instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~31/MDPF_CANON.TO-CN-s-4.variant2-band-not-carried.proof_of_spec.json`, AC3 UNVERIFIABLE-BY-INSTRUMENT with status_reason "graded at the round close". **Flip this order's `<status>` to `complete` in the SAME commit as the instance**, and only when AC1 and AC2 both pass.
3. Commit the OUTER files via `.tools/safe-commit.sh --author "0.9.0_WK_MDPF_CANON~31 <0.9.0_WK_MDPF_CANON~31@opal.agent>" -F <msgfile> -- <paths>` (outer paths only; do not stage `portal`). Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W31-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at filing.
Report once: the portal branch and commit hash, the diff stat (one line), the output lines of AC1 and AC2, the outer commit hash, and any row. Then STOP: the issuer hands you the next order (CN-s-5) by continuing you.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 11, issuer 2.0.0_SA_COO~D1, on the CTO's round-10 analysis (msg 6731) item 1 and PRD v2.23 @1fb9ac96ab ("the Models band is never carried forward on or after per_model_detail_begins; test it on the real object"). The CTO's criterion: the Variant 2 Total equals the served Total on all 9 carried dates; the real-object arm R3 reads it as "no drawn group above the Total" on those dates. The served Total is null on the 9 carried dates and the module carries the last measured Total there (arm R4: 489 of 489 dated rows equal the served Total, 9 of 9 carried dates carry the last measured one); the base reads R3 red on all 9 (the stack exceeds the Total by $1.32B on 2026-05-30). The repair is client-facing and rides the next portal promote on Andrew's 2026-10-15 word ("it should get added on to the next prod promote of the portal", `ANDREW_DIRECT_20261015_162xZ_DEMO_GLOBAL_TREND_USES_VARIANT1_NEXT_PROMOTE.md`); it disarms row D1-S29 on its PROD read (with CN-s-5, per the row). LANDING (CLAUDE.md Portal): a client-facing row for Andrew (the approval row is cut FROM PROD with a cherry-pick of this ONE commit; portal DEV is written only by `.tools/portal-merge-forward.sh`). This order's commit is separate from CN-s-5's on purpose: 4b is held on the edge call and 4a is not.
**Fanout:** 2 of 2 chains; chain 1 is `CN-s-4` -> `CN-s-5` -> `CN-s-3` on ONE worker (shared `trendGrouping.ts` and `ModelPortfolios.tsx`). `portal_ref:` 39dab87f3b (portal DEV at the cut).

<status>pending</status>
<round>11</round>
<to_id>MDPF_CANON.TO-CN-s-4</to_id>
<slot>~31</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
