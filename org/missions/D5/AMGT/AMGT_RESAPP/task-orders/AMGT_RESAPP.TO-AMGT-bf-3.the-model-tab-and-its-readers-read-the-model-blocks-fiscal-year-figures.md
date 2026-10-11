# AMGT_RESAPP task order -- `AMGT-bf-3` -- THE MODEL TAB AND ITS READERS READ THE MODEL BLOCK'S `fiscal_year_figures` (PORTAL DEV CANDIDATE, STEP 1 OF THE PAYLOAD DE-DUPLICATION)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bf-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~396</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bf-3.the-model-tab-and-its-readers-read-the-model-blocks-fiscal-year-figures</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- source and fixture edits, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS; the checks read local files and the nested repository.
comp-adversary: RUN at the cut -- r99_repoint_readers.py FAILs R1 (5 top-level reads), R3 and R4 at the base and PASSes R2 and R5, then reads 5 of 5 / YES against a throwaway candidate built in a scratch worktree at DEV 44ec7e70a9 (src/pages/SecurityAnalysis is byte-identical at the ref ad774c6f9e55; the five edits below plus r99_fixture_model_copy.py, 6 of 8 fixtures written); on the same candidate the stock harnesses read tabs 21 of 21, modelPattern 12 of 12, posturePattern 13 of 13, posture 32 of 32, execPattern 9 of 9, thesisLadder 10 of 10, drafting 8 of 8, shell 10 of 10, peersPattern 13 of 13 and join 'harness green', and `bun run typecheck` exits 0; every one of them reads the same at the base. The served payload carries the two copies EQUAL for 95 of 95 names (r99_fy_figures_equal.py, local handler on the live pool).
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-396` (branch `wk-AMGT_RESAPP-396`, cut from the issuance commit; its nested portal worktree is `C:/dev/wk-resapp-396/portal`, branch `wk-AMGT_RESAPP-396-portal`, cut from portal DEV ad774c6f9e55). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-396` (or the portal path); a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bf-3` (round 99, decomposition s.107)

CTO~DELL1 round-98 analysis section 2 step 1. The Thesis payload serves `fiscal_year_figures` TWICE (top level and as `model.fiscal_year_figures`, equal for every name, 32.3 percent of the
response each). Both portal builds read the TOP-LEVEL copy today; the footer's time list already reads `model.fiscal_year_figures[].vintage`. This cell repoints every reader of the
top-level copy to the model copy, so the API can later drop the top-level one. In the PORTAL repository, in the nested worktree `C:/dev/wk-resapp-396/portal` on a branch
`wk-AMGT_RESAPP-396-portal` cut from `DEV`, make exactly these edits (a CRLF file stays CRLF; ASCII only):

1. `src/pages/SecurityAnalysis/tabs/ModelTab.tsx`: the two uses of `data.fiscal_year_figures` (the `buildModelSheet(...)` call's first argument, and `historySheet`'s first argument) become
   `(data.model?.fiscal_year_figures ?? [])`.
2. `src/pages/SecurityAnalysis/postureCites.ts`: `thesis.fiscal_year_figures ?? []` becomes `thesis.model?.fiscal_year_figures ?? []`.
3. `src/pages/SecurityAnalysis/components/CardFooter.tsx`: in `footerFor.model`'s sources list drop the entry `'fiscal_year_figures[].source'` (the list already names
   `'model.fiscal_year_figures[].source'`); in `whatChangedSources` replace `'fiscal_year_figures[].source'` with `'model.fiscal_year_figures[].source'`.
4. `src/pages/SecurityAnalysis/types.ts`: `interface ThesisModelBlock` gains `fiscal_year_figures?: ModelFigure[] | null` (with a one-line comment). The `ThesisBundle.fiscal_year_figures`
   declaration STAYS (the API still serves the top-level copy until its own step 3).
5. The harness fixtures predate the model block: run `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round99_prep/checks/r99_fixture_model_copy.py C:/dev/wk-resapp-396/portal`; it adds `model.fiscal_year_figures` (an EQUAL copy) to the six
   fixtures whose top-level list is non-empty, in each file's own serialisation, and prints `fixtures changed 6 of 8`. A fixture it REFUSES is a row, never a hand edit.

Nothing else moves: no other file, no component, token or served field; the harness `.cjs` and `.mjs` files stay as they are (they read the fixtures' top-level copy, which stays).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W396-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only, nested worktree `C:/dev/wk-resapp-396/portal`, branch `wk-AMGT_RESAPP-396-portal` from `DEV`; never push; never touch `PROD`.
2. Edit only the four source files and the six fixtures named; no other file, no new file in the portal.
3. No deploy, no store write, no AWS call, no network. `bun install` is NOT allowed (the worktree's `node_modules` is a link to the main tree's).
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/postureCites.ts
portal/src/pages/SecurityAnalysis/components/CardFooter.tsx
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.BABA_US_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.BA_US_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.SAP_GY_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/thesisBundle.BABACVOCTRL_US_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/thesisBundle.BABA_US_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/thesisBundle.drafted.BA_US_Equity.json
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~396/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bf-3"><invocation>cd C:/dev/wk-resapp-396/portal &amp;&amp; python "C:/dev/wk-resapp-396/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round99_prep/checks/r99_repoint_readers.py" C:/dev/wk-resapp-396/portal --base ad774c6f9e55; echo "exit=$?"</invocation><expect>run in the PORTAL worktree: PASS R1 (0 top-level reads), PASS R2 (the control sees a model.fiscal_year_figures read), PASS R3 (ThesisModelBlock declares it), PASS R4 (every fixture with top-level figures carries an equal model copy), PASS R5 (nothing else of the fixtures moved); arms passed 5 of 5; R99 REPOINT READERS: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bf-3"><invocation>cd C:/dev/wk-resapp-396/portal &amp;&amp; for h in tabs modelPattern posturePattern posture execPattern thesisLadder drafting shell peersPattern; do node src/pages/SecurityAnalysis/__harness__/$h.harness.cjs | grep -E "^CHECKS-OK"; done &amp;&amp; node src/pages/SecurityAnalysis/__harness__/join.harness.mjs | tail -1; echo "exit=$?"</invocation><expect>the stock harnesses still read, in this order, CHECKS-OK 21 of 21, CHECKS-OK 12 of 12, CHECKS-OK 13 of 13, CHECKS-OK 32 of 32, CHECKS-OK 9 of 9, CHECKS-OK 10 of 10, CHECKS-OK 8 of 8, CHECKS-OK 10 of 10, CHECKS-OK 13 of 13, then 'OK: harness green.' (the control: nothing else on the page moved, the repointed readers render what they rendered); and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bf-3"><invocation>cd C:/dev/wk-resapp-396/portal &amp;&amp; bun run typecheck; echo "exit=$?"</invocation><expect>the portal typechecks (tsc -b) with 0 errors; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit the portal change inside the nested worktree (cwd `C:/dev/wk-resapp-396/portal`; the same `safe-commit.sh` with the author line below, `-F` a message file written with the Write tool,
`--` the ten paths relative to the portal root), then commit your deliverables in `C:/dev/wk-resapp-396` via
`.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~396 <0.9.0_WK_AMGT_RESAPP~396@opal.agent>" -F <msgfile> -- <paths>` (confirm each with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~396/AMGT_RESAPP.TO-AMGT-bf-3.the-model-tab-and-its-readers-read-the-model-blocks-fiscal-year-figures.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal` in the outer worktree.
Report once:
- the commit hash (and the portal branch and commit hash);
- every criterion's output lines;
- the diff of each edited source file, in full (not the fixtures);
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-98 analysis section 2 step 1: "Portal: repoint every reader of the TOP-LEVEL `fiscal_year_figures` to `model.fiscal_year_figures`. It is a candidate reviewed by this seat before DEV. Close: `git grep` at DEV shows 0 top-level readers, and the page renders byte-equal on a sampled set." The render equality follows from the payload's two copies being EQUAL for 95 of 95 names (measured) and the stock harnesses over fixtures that now carry the model copy. The CTO reviews the candidate before any DEV push (the product file touched); step 2 (the PROD promote, `e7f2`) is Andrew's and gates step 3 (the API drop, a later redeploy pair).

**AMENDMENT 1 (2026-10-11T23:5xZ, 2.0.0_SA_COO~R1, the issuer's own order; no gate limb graded it: `.tools/to-pipeline-gate.py` fires on newly-added orders, and this is a modification):** AC2's invocation took `tail -1` of each harness, but `modelPattern.harness.cjs` prints `CHECKS-OK 12 of 12` and then a fixture JSON line, so the criterion read FAIL on a candidate whose every harness is green. The invocation now selects each harness's `CHECKS-OK` line with `grep -E "^CHECKS-OK"`; the expectation is unchanged. **The defect is the issuer's:** the dry-run at the cut ran a different filter (`grep -E "CHECKS-OK|FAIL|rror" | tail -1`) from the invocation written into the order, so the literal string was never run. The issuer ran the amended literal invocation against worker ~396's candidate (portal @cd229995): nine `CHECKS-OK` lines 21, 12, 13, 32, 9, 10, 8, 10, 13, then 'OK: harness green.', exit=0.

<status>complete -- 2026-10-11T23:5xZ by the issuer (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-396 @de92a5cf7b merged @f3d3a97852 (AC2 re-run under AMENDMENT 1), proof instance VALID; portal DEV CANDIDATE on the nested repository's branch wk-AMGT_RESAPP-396-portal @cd229995 (cut from DEV ad774c6f9e55; 4 source files +7/-5, 6 fixtures), NOT pushed, NOT on DEV. Issuer re-run in the worker's portal worktree: AC1 R99 REPOINT READERS YES (5 of 5: 0 top-level reads over 703 files, 6 model accesses, 8 of 8 fixtures equal), AC2 the nine stock harnesses 21, 12, 13, 32, 9, 10, 8, 10, 13 and join green (run on the candidate before the amendment was committed), AC3 typecheck rc 0. The CTO reviews the candidate before any DEV push (a product file is touched).</status>
<round>99</round>
<slot>0.9.0_WK_AMGT_RESAPP~396</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
