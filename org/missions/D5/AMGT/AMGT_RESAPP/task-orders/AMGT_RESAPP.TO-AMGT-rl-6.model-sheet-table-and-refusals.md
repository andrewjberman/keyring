# AMGT_RESAPP task order -- `AMGT-rl-6` -- THE MODEL SHEET AS A TABLE: signed numerals under year heads, a refusal as ONE line per row, absent rows in one footnote, three scores as tiles

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rl-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~135</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the L1 brief at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. react-dom/server harnesses only; no browser, no HTTP, no vendor call.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~135`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. First act:
print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, `test -d org && test -d .tools && echo TREE-OK`,
`test -f portal/scripts/ui-class-census.mjs && echo INSTRUMENT-OK` (absent = BLOCKING row, stop). Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~135;`. **NEVER RUN AN INSTALL. No vite dev server on this cell.** Never
push, merge, rebase, `checkout --` or `clean`. **Portal is a NESTED repository at `<worktree>/portal`:** portal files are
committed inside it (`cd portal && bash ../.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~135 <0.9.0_WK_AMGT_RESAPP~135@opal.agent>" -F <msgfile> -- <paths>`),
then the outer commit carries `portal` and your deliverables. Messages PURE ASCII via the Write tool. Scripts and logs under
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~135/`, never `.scratch/`.

## 1. THE CELL -- `AMGT-rl-6` (round 37, decomposition s.45)

**`FWD-24`:** *"the fiscal table renders as a white heatmap panel with tabular numerals; a REFUSED row renders one status
icon and one navy sentence spanning the row; ABSENT rows fold into a single footnote naming them. ACCEPT: A refusal is
readable once, not ten times. TODAY: the DPS row repeats a 60-char refusal in ten red chips."*

**The target (brief Part V, Model):** ONE white `Panel variant="heatmap"` with the fiscal table at numeral size (14px/400,
tabular, right-aligned), the years as column heads (label 13px/700), every negative value SIGNED (C2); a REFUSED row renders
ONE `status.danger` icon and ONE navy sentence spanning the row (a `colspan` cell), never a chip per cell; ABSENT rows fold
into ONE footnote naming them ("Absent rows: DPS, ..."), at footnote size; the three scores (the Divergence score and its
two companions, exactly as `modelSheet.ts` names them) as tiles ABOVE the table -- build a LOCAL tile inside this file
(`src/ui/components/Stat.tsx` is a dark idiom and is not used): label 13px/700, value 14px/400 tabular, 4px radius, no shadow
-- with "not read" as the EMPTY state when the score is unread. The `machine` marking as a navy outline chip once in the
header. Every empty/loading/error state one of the four designed states (C12).

## 2. BOUNDS

1. **Files:** `tabs/ModelTab.tsx`, `modelSheet.ts`, and the NEW `__harness__/modelPattern.harness.cjs`. Everything else in
   the page directory is another cell's this round; `src/ui/**`, `src/components/**`, `src/api/**` read-only. `IdentityLine`,
   `ProvenanceLine`, `CheckFaceBadge` are being inverted by another cell in parallel -- render them unchanged.
2. **`modelSheet.ts`'s computed shape is KEPT:** every row, year, value, refusal and absence it derives today is still
   derived; the refusal TEXT is byte-identical to the payload's; nothing computed on the page (`C-PRESENTATION-ONLY`;
   value-must-carry-its-claim). The presentation folds repetition; it does not drop a refusal or an absence.
3. **The contract is `portal/DESIGN.md` C1-C12** as in every cell this round: the ladder, weights 400/700, radii
   2/3/4/pill, no shadow, navy ink, status as an icon beside navy text (C6/C9 -- a refusal is NEVER red text), the four
   designed states.
4. **Standing:** no install, no vendor or Bloomberg call, no S3 delete, no key hunting, no push, no promote. **REFUSE, do
   not rescue.**

## 3. THE HARNESS YOU ADD -- `__harness__/modelPattern.harness.cjs`

Same loader as `tabs.harness.cjs` (actual `ModelTab`, installed typescript, `react-dom/server`, hooks stubbed with
`__harness__/tabsFixture.BA_US_Equity.json`'s `thesis` bundle -- its `fiscal_year_figures` carry 165 figures including a
REFUSED row -- plus a second render with the scores unread). Prints `CHECK <name> <value> (expected <value>)` per line and
`CHECKS-OK n of n`; expected counts READ OFF THE FIXTURE: `panel_is_heatmap` (the `heatmap` variant, no `dark-band`) ·
`year_heads` == the fixture's fiscal years · `rows_rendered` == the fixture's rows minus the absent ones ·
`negative_values_signed` (every negative figure's cell text begins with a minus sign) · `refused_rows` == the fixture's
refused rows and `refusal_sentences` == `refused_rows` (ONE sentence per refused row) · `refusal_chips` == 0 ·
`refused_row_icon_danger` (the danger icon beside navy text, no red text class) · `absent_footnote` == 1 and it names every
absent row · `score_tiles` == 3 · `score_empty_state` == "not read" on the unread render · `machine_chip_once` == 1.

## 4. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/modelSheet.ts
portal/src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.BA_US_Equity.json
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/components/IdentityLine.tsx
portal/src/pages/SecurityAnalysis/components/ProvenanceLine.tsx
portal/src/pages/SecurityAnalysis/components/CheckFaceBadge.tsx
portal/src/pages/SecurityAnalysis/refusalPresentation.ts
portal/scripts/ui-class-census.mjs
portal/DESIGN.md
portal/src/ui/components/states/index.ts
portal/src/ui/components/panels/Panel.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~135/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

Of these you WRITE only the first three; the rest are read-only inputs.

## 5. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rl-6"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs</invocation><expect>THE BUILT BEHAVIOUR: CHECKS-OK 12 of 12 with every CHECK line printed beside its fixture-derived expected value -- panel_is_heatmap true, year_heads equal to the fixture's fiscal years, rows_rendered equal to rows minus absent, negative_values_signed true, refused_rows equal to the fixture's refused rows, refusal_sentences equal to refused_rows, refusal_chips 0, refused_row_icon_danger true, absent_footnote 1 naming every absent row, score_tiles 3, score_empty_state "not read", machine_chip_once 1</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rl-6"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-class-census.mjs src/pages/SecurityAnalysis/tabs/ModelTab.tsx src/pages/SecurityAnalysis/modelSheet.ts</invocation><expect>THE INVERSION IS COMPLETE ON YOUR FILES: FILES 2 TOTAL 0, both lines idiom=0 size=0 weight=0 radius=0 shadow=0 (the walk counted 18 in ModelTab before this cell; a non-zero FAILS)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rl-6"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs; echo "tabs-exit=$?"</invocation><expect>THE SHARED HARNESS STILL RENDERS THE MODEL TAB: every model-related CHECK line reads its expected value (the fiscal figures rendered of the fixture's 165, the refusal faces present, the model_status line) with no check NEWLY WRONG-WAY; exec_officers_rendered is reported AS-IS (it read false at DEV HEAD before this round and belongs to another cell)</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~135/AMGT_RESAPP.TO-AMGT-rl-6.model-sheet-table-and-refusals.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` from the
worktree root. **The status flip is the ISSUER'S**; leave the record face alone and say so. **Report once, naming:** the
fixture denominators (years, rows, refused, absent), the two commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

# pipeline-override: LIMB 6 only -- the BRIEF half reads STALE at 8da812bf80 (owed by 4.0.0_SA_CRO~Z, asked 05:59Z); R-10 (Andrew-direct 2026-09-23 ~21:2xZ, 'agreed with your rec': the L4-R signature is not a BAR for AMGT, the review is kept) + ADDENDUM B B.6 + 1.0.0_SA_CTO~Z msg 25282 (3) 'no round is held on it'; the review stays owed and is not skipped. The PRD_HEADER key refusal is CLEARED at 8da812bf80; coverage is NOTED at EXECUTING (enrichment recut).

**ISSUER NOTES:** wave 1, spawned after rl-1 merges. The local score tile duplicates rl-2's `StatTile` deliberately: the
two cells run in parallel and neither may import a file the other is creating; the drain's follow-up (rl-9 or the
round-37 analysis) may unify them as an enrichment item.

<status>pending</status>
<round>37</round>
<slot>~135</slot>
<fabric>site-z</fabric>
