# AMGT_RESAPP task order -- `AMGT-rl-4` -- EXEC MANAGEMENT IN PATTERN: the catalyst table on a white panel, the inversion of 26 idioms, and the red officers check made green through the component

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rl-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~133</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the L1 brief at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. react-dom/server harnesses only; no browser, no HTTP, no vendor call.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~133`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. First act:
print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, `test -d org && test -d .tools && echo TREE-OK`,
`test -f portal/scripts/ui-class-census.mjs && echo INSTRUMENT-OK` (absent = BLOCKING row, stop). Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~133;`. **NEVER RUN AN INSTALL. No vite dev server on this cell.** Never
push, merge, rebase, `checkout --` or `clean`. **Portal is a NESTED repository at `<worktree>/portal`:** portal files are
committed inside it (`cd portal && bash ../.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~133 <0.9.0_WK_AMGT_RESAPP~133@opal.agent>" -F <msgfile> -- <paths>`),
then the outer commit carries `portal` and your deliverables. Messages PURE ASCII via the Write tool. Scripts and logs under
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~133/`, never `.scratch/`.

## 1. THE CELL -- `AMGT-rl-4` (round 37, decomposition s.45)

The brief calls Exec Management *"already the closest surface to pattern"* -- and the walk still counted **26 light-on-dark
idioms** in `ExecManagementTab.tsx`, a `Panel variant="mixed"` band, 743 characters at 10px and 14 at 2.3:1. This cell
serves `FWD-29`'s page-wide predicates for this tab (one band per page, the ladder, the weights, the radii, no shadow,
contrast) and `FWD-28` for its own panel states.

**The target (brief Part V, Exec Management):** ONE white panel (`Panel variant="nested"`) with the catalyst table:
officer, role, role start, tenure (numeral 14px/400 tabular, right-aligned), profile (a secondary button or a navy link;
"ABSENT" as an icon-plus-text cell, never a blank), confirmed (a status dot -- pill radius -- WITH its label, never colour
alone: C6). The averages line as the panel footer. The "machine" marking as a navy outline chip at label size where the
payload marks it. Every empty/loading/error state one of the four designed states (C12).

⚠ **THE STARTING STATE YOU INHERIT, NOT YOUR FAULT:** at DEV HEAD `c1ac41ec` in this environment
`__harness__/tabs.harness.cjs` reads `CHECKS-WRONG-WAY exec_officers_rendered` -- its exec arm expected true and read
false. `tabs.harness.cjs` is ANOTHER cell's file this round: read it to learn what the arm asserts (officers rendered of
the fixture's officers; the CEO reading; the pool line), make the COMPONENT satisfy it, and never edit the harness.

## 2. BOUNDS

1. **Files:** `tabs/ExecManagementTab.tsx`, `__harness__/execText.harness.cjs` and `__harness__/execFallback.harness.cjs`
   (yours; keep both green), and the NEW `__harness__/execPattern.harness.cjs`. Everything else in the page directory is
   another cell's this round; `src/ui/**`, `src/components/**`, `src/api/**` read-only. `CheckFaceBadge`, `IdentityLine`,
   `ProvenanceLine`, `GenerationCaption` are being inverted by another cell IN PARALLEL -- render them unchanged.
2. **The contract is `portal/DESIGN.md` C1-C12** as in every cell this round: nothing below 11px, weights 400/700, radii
   2/3/4/pill, no shadow, navy ink, `#6B7280` secondary on a panel only, status colour never as text on a light ground,
   the four designed states from `@/ui/components/states`.
3. **KEPT:** the officer set and every figure the payload carries (nothing computed on the page; `C-PRESENTATION-ONLY`);
   the ABSENT/READ_FAILED distinction; the pinned-copy discriminators `execText` and `execFallback` assert.
4. **Standing:** no install, no vendor or Bloomberg call, no S3 delete, no key hunting, no push, no promote. **REFUSE, do
   not rescue.**

## 3. THE HARNESS YOU ADD -- `__harness__/execPattern.harness.cjs`

Same loader as `execText.harness.cjs` (actual `ExecManagementTab`, installed typescript, `react-dom/server`, hooks stubbed
with the exec fixtures already in `__harness__/` -- `execFixture.CAT_US_Equity.json` and one more of your choice; expected
counts READ OFF THE FIXTURE). Prints `CHECK <name> <value> (expected <value>)` per line and `CHECKS-OK n of n`:
`panel_is_light` (no `dark-band`/`variant="mixed"` in the markup) · `table_columns` == 6 (officer, role, role start,
tenure, profile, confirmed, in that order) · `officers_rendered` == the fixture's officer count · `tenure_tabular_right`
(the tenure cells carry the tabular-numerals class and right alignment) · `absent_profile_cells` == the fixture's officers
without a profile url, each rendered as icon+text "ABSENT", none blank · `confirmed_dot_with_label` (every confirmed cell
carries a pill dot AND a text label) · `footer_averages_line` == 1 · `empty_state_designed` (a render with zero officers
carries `PanelEmpty`-shaped markup, not a bare sentence) · `machine_chip_once_per_marked_row`.

## 4. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/execText.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execFixture.6861_JP_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/execFixture.ASML_NA_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/execFixture.CAT_US_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/execFixture.CSL_AU_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.BA_US_Equity.json
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/components/CheckFaceBadge.tsx
portal/src/pages/SecurityAnalysis/components/IdentityLine.tsx
portal/src/pages/SecurityAnalysis/components/ProvenanceLine.tsx
portal/scripts/ui-class-census.mjs
portal/DESIGN.md
portal/src/ui/components/states/index.ts
portal/src/ui/components/panels/Panel.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~133/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

Of these you WRITE only the first four; the rest are read-only inputs.

## 5. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rl-4"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/execPattern.harness.cjs</invocation><expect>THE BUILT BEHAVIOUR: CHECKS-OK 9 of 9 with every CHECK line printed beside its fixture-derived expected value -- panel_is_light true, table_columns 6, officers_rendered equal to the fixture's officer count, tenure_tabular_right true, absent_profile_cells equal to the fixture's profile-less officers with none blank, confirmed_dot_with_label true, footer_averages_line 1, empty_state_designed true, machine_chip_once_per_marked_row true</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rl-4"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-class-census.mjs src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx</invocation><expect>THE INVERSION IS COMPLETE ON YOUR FILE: FILES 1 TOTAL 0 -- idiom=0 size=0 weight=0 radius=0 shadow=0 (the walk counted 26 idioms before this cell; a non-zero FAILS)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rl-4"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs; echo "tabs-exit=$?"; node src/pages/SecurityAnalysis/__harness__/execText.harness.cjs &amp;&amp; node src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs</invocation><expect>THE SHARED HARNESSES: tabs.harness.cjs prints CHECK exec_officers_rendered true (expected true) -- the arm that read false at DEV HEAD now reads true THROUGH THE COMPONENT, with no other check newly WRONG-WAY; execText prints EXECTEXT CHECKS 5/5 and execFallback prints EXECFALLBACK CHECKS 5/5 (both read 5/5 before this cell; a regression FAILS)</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~133/AMGT_RESAPP.TO-AMGT-rl-4.exec-management-in-pattern.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` from the
worktree root. **The status flip is the ISSUER'S**; leave the record face alone and say so. **Report once, naming:** WHAT
made `exec_officers_rendered` read false (the cause, at the bytes) and what changed it, the fixture denominators, the two
commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

# pipeline-override: LIMB 6 only -- the BRIEF half reads STALE at 8da812bf80 (owed by 4.0.0_SA_CRO~Z, asked 05:59Z); R-10 (Andrew-direct 2026-09-23 ~21:2xZ, 'agreed with your rec': the L4-R signature is not a BAR for AMGT, the review is kept) + ADDENDUM B B.6 + 1.0.0_SA_CTO~Z msg 25282 (3) 'no round is held on it'; the review stays owed and is not skipped. The PRD_HEADER key refusal is CLEARED at 8da812bf80; coverage is NOTED at EXECUTING (enrichment recut).

**ISSUER NOTES:** wave 1, spawned after rl-1 merges. The `exec_officers_rendered` red is recorded in s.45f as the starting
state at DEV HEAD in this environment; if the worker finds the cause is NOT in the component (a fixture, a stub or the
harness itself), that is a row and AC3 is refused with the measurement, not rescued.

**ISSUER CLOSE-OUT, 2.0.0_SA_COO~Z, 2026-09-24 ~09:0xZ.** Flipped by the ISSUER; the worker left the record face alone.
3 of 3 criteria PASS, proof-of-spec rc=0 VALID (re-run by this seat inside the worker's worktree C:/tmp/wk-amgt-37-133).
execPattern.harness.cjs CHECKS-OK 9 of 9; ui-class-census FILES 1 TOTAL 0 (was 26); tabs.harness.cjs 20 of 20 (exec_officers_rendered
now 5 of 5 -- data-ceo-profile carries the object's own reading, ExecManagementTab.tsx:196-200), execText 5 of 5, execFallback 5 of 5
(its two pinned byte-identity checks re-cut to fact checks plus a positive marker, per the file's own Z-S193/rk-80 precedent). No rows.
Drained @2488c1bf0d; portal DEV ae1b9f42 (merge of 62ee58b3), gitlink cd1a7146 -> ae1b9f42. Drain-time ui-contract-check
(contract-check-after-rl-4/): exec state unchanged at band 2 / weights / sizes / radii / shadows / purpleFills 4 -- those read on the
shared chrome (lead panel, list) that rl-8 and rl-9 own. The PASS is owed by rl-9's re-assert.

<status>complete</status>
<round>37</round>
<slot>~133</slot>
<fabric>site-z</fabric>
