# AMGT_RESAPP task order -- `AMGT-rl-8` -- THE LEAD PANEL: the Dashboard's controls, weight-and-rule segmented controls, the captions in a "Source:" footer with the day the list is dated

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rl-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~137</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the L1 brief at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. react-dom/server harnesses only; no browser, no HTTP, no vendor call.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~137`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. First act:
print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, `test -d org && test -d .tools && echo TREE-OK`,
`test -f portal/scripts/ui-class-census.mjs && echo INSTRUMENT-OK` (absent = BLOCKING row, stop). Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~137;`. **NEVER RUN AN INSTALL. No vite dev server on this cell.** Never
push, merge, rebase, `checkout --` or `clean`. **Portal is a NESTED repository at `<worktree>/portal`:** portal files are
committed inside it (`cd portal && bash ../.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~137 <0.9.0_WK_AMGT_RESAPP~137@opal.agent>" -F <msgfile> -- <paths>`),
then the outer commit carries `portal` and your deliverables. Messages PURE ASCII via the Write tool. Scripts and logs under
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~137/`, never `.scratch/`.

## 1. THE CELL -- `AMGT-rl-8` (round 37, decomposition s.45)

**`FWD-27`:** *"Movement and Subject render as segmented controls whose active state is WEIGHT AND RULE, the generation and
resolution lines sit in a 'Source:' footer, and the rendered state reads purpleFills == 0 in Universe mode and == 1
(Refresh) in Security mode. ACCEPT: One purple action per view (C8). TODAY: a filled purple view chip plus two 10-px
caption lines above the rows."* The walk counted 26 idioms in `LeadPanel.tsx`, 19 in `RankedChart.tsx`, 16 in
`RankedList.tsx`, 10 in `StarredList.tsx`, and 4 purple fills on the list state.

**The target (brief Part V, Lead Panel):** the Lead Panel stays the ONE BAND in UNIVERSE mode (`Panel variant="mixed"`
is correct HERE and only here). `PanelHeader` with the title; the crossed controls (Movement: Trending/Breakout; Subject:
Chatter/Price) as two `Segmented` controls from `@/ui/components/Controls` (read-only import) whose active state is
weight and rule (700 + underline), never a filled chip; Starred as a toggle; list/chart as an icon segmented control;
search at the right. The generation caption and the resolution line move into the panel's "Source:" FOOTER (`PanelFooter`)
-- and that footer ALSO carries the day the list is dated: the `/rankings` payload already serves `dated`,
`requested_as_of` and `as_of_date` (R-17: client-side only, the route serves both fields), so the footer reads
"Source: <generation> -- dated <dated> (requested <requested_as_of>)", and a `dated` older than `requested_as_of` is
SAID, not hidden ("a nine-day-old list under a fresh timestamp" is the defect this closes). Rows as today: rank, ticker,
name and the score on one line at numeral size, tabular; the headline placeholder removed until the feed carries one.
Band ink is `#E8ECF5` on `#0A1733` (15:1); secondary band ink `#A8B0C0` (8.14:1) -- the ONLY ground where it is text.
Every empty/loading/error state one of the four designed states (C12), in the band's frame.

**SECURITY MODE IS NO LONGER THIS COMPONENT'S.** From this round the page shell renders the identity header itself when a
security is selected and does not render `LeadPanel` at all in that mode (another cell, in parallel). Strip the
Security-mode branch (the `SecurityOverlay` render and its props) from `LeadPanel.tsx` as dead code; keep the props the
shell passes today so the shell compiles against either version until the drain (`selectedSecurityKey`,
`onSelectSecurity`, `onClearSecuritySelection` stay in the props type; the panel simply never renders the overlay).

## 2. BOUNDS

1. **Files:** `components/LeadPanel.tsx`, `components/RankedList.tsx`, `components/RankedChart.tsx`,
   `components/StarredList.tsx`, `__harness__/errorEmpty.harness.cjs` (yours; keep it 12 of 12), and the NEW
   `__harness__/leadPanelPattern.harness.cjs`. Everything else in the page directory is another cell's this round;
   `src/ui/**`, `src/components/**`, `src/api/**` read-only. `SecurityOverlay.tsx`, `HeaderBrief.tsx`,
   `GenerationCaption.tsx` are another cell's -- import `GenerationCaption` unchanged if you still render it; do not edit.
2. **`C-SERVER-SIDE-RANKING` is KEPT:** rows render in the order the payload returns them; nothing sorts, scores or
   re-ranks on the page; the `RankedList` click payload (the unresolved-row rule, AMGT-rj-1) is unchanged -- `errorEmpty`
   asserts it.
3. **The contract is `portal/DESIGN.md` C1-C12** as in every cell this round, read for a BAND: the band is full-bleed and
   square, carries no primary action (`#5F3BE3` on `#0A1733` is 2.72:1, C8), its ink is `#E8ECF5`/`#A8B0C0`, its focus ring
   is the on-band ring (C11); inside it the ladder, weights 400/700, radii 2/3/4/pill and no shadow bind as everywhere.
4. **No route, DTO, query key or figure moves.** `dated`/`requested_as_of` are READ from the payload the panel already
   holds; nothing is computed.
5. **Standing:** no install, no vendor or Bloomberg call, no S3 delete, no key hunting, no push, no promote. **REFUSE, do
   not rescue.**

## 3. THE HARNESS YOU ADD -- `__harness__/leadPanelPattern.harness.cjs`

Same loader as `errorEmpty.harness.cjs` (actual `LeadPanel`, `RankedList`, `StarredList`, `RankedChart`, installed
typescript, `react-dom/server`; the rankings payload from `__harness__/uiContractFixtures.json`'s
`/api/scoped/amgt/lead-panel/rankings/trending/chatter` entry, which carries `dated`, `requested_as_of`, `as_of_date`
and `ranking_status`). Prints `CHECK <name> <value> (expected <value>)` per line and `CHECKS-OK n of n`; expected values
READ OFF THE PAYLOAD: `band_is_lead_panel` (the ONE `dark-band` container) · `segmented_controls` == 2 (Movement,
Subject) with the active option carrying weight-and-rule classes and NO purple fill class · `purple_fill_classes` == 0 in
the Universe render · `starred_toggle` and `view_icon_segmented` present · `source_footer` == 1 and it carries the
generation caption text AND "dated <payload.dated>" AND "requested <payload.requested_as_of>" · `stale_dated_said` (a render
with `dated` earlier than `requested_as_of` says so in words) · `rows_rendered` == the payload's rows, in payload order ·
`row_line_tabular` (rank, ticker, name, score on one line with the tabular class) · `headline_placeholder_absent` ·
`overlay_not_rendered` (a render with `selectedSecurityKey` set carries NO `SecurityOverlay`/identity-header markup) ·
`empty_state_designed_in_band` (zero rows renders `PanelEmpty`-shaped markup inside the band).

## 4. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/components/RankedList.tsx
portal/src/pages/SecurityAnalysis/components/RankedChart.tsx
portal/src/pages/SecurityAnalysis/components/StarredList.tsx
portal/src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/uiContractFixtures.json
portal/src/pages/SecurityAnalysis/__harness__/rankSeriesCompleteness.json
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/constants.ts
portal/src/pages/SecurityAnalysis/hooks/useLeadPanelApi.ts
portal/src/pages/SecurityAnalysis/hooks/useSecurityAnalysisState.ts
portal/src/pages/SecurityAnalysis/components/GenerationCaption.tsx
portal/src/ui/components/Controls.tsx
portal/src/ui/components/panels/PanelFooter.tsx
portal/src/ui/components/panels/PanelHeader.tsx
portal/scripts/ui-class-census.mjs
portal/DESIGN.md
portal/src/ui/components/states/index.ts
portal/src/ui/components/panels/Panel.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~137/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

Of these you WRITE only the first six; the rest are read-only inputs.

## 5. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rl-8"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs</invocation><expect>THE BUILT BEHAVIOUR: CHECKS-OK 12 of 12 with every CHECK line printed beside its payload-derived expected value -- band_is_lead_panel true, segmented_controls 2, purple_fill_classes 0, starred_toggle true, view_icon_segmented true, source_footer 1 carrying the generation caption and dated and requested values from the payload, stale_dated_said true, rows_rendered equal to the payload's rows in order, row_line_tabular true, headline_placeholder_absent true, overlay_not_rendered true, empty_state_designed_in_band true</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rl-8"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-class-census.mjs src/pages/SecurityAnalysis/components/LeadPanel.tsx src/pages/SecurityAnalysis/components/RankedList.tsx src/pages/SecurityAnalysis/components/RankedChart.tsx src/pages/SecurityAnalysis/components/StarredList.tsx</invocation><expect>THE INVERSION IS COMPLETE ON YOUR FILES EXCEPT THE BAND'S OWN INK: FILES 4 with size=0 weight=0 radius=0 shadow=0 on every line; idiom counts the census reports for the BAND's own ink classes are LISTED with the class named on each line -- a band-ink idiom (`text-[#E8ECF5]`, `text-[#A8B0C0]` or the token classes the estate uses for them) is admitted INSIDE the band and named; any OTHER idiom (translucent, `text-white/N`, `bg-white/N`, a light hue below 400) reads 0. Print the four lines and the admitted class list; a translucent or opacity-slash idiom surviving anywhere FAILS</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rl-8"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs</invocation><expect>THE ERROR/EMPTY BOUNDARY AND THE CLICK PAYLOAD ARE PRESERVED: CHECKS-OK 12 of 12 exactly as at DEV HEAD c1ac41ec (error differs from empty; the unresolved row did not navigate; the handler count non-zero); any WRONG-WAY check FAILS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~137/AMGT_RESAPP.TO-AMGT-rl-8.lead-panel-controls-and-footer.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` from the
worktree root. **The status flip is the ISSUER'S**; leave the record face alone and say so. **Report once, naming:** the
band-ink classes AC2 admitted, the `dated` and `requested_as_of` values the footer rendered from the fixture, the two
commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

# pipeline-override: LIMB 6 only -- the BRIEF half reads STALE at 8da812bf80 (owed by 4.0.0_SA_CRO~Z, asked 05:59Z); R-10 (Andrew-direct 2026-09-23 ~21:2xZ, 'agreed with your rec': the L4-R signature is not a BAR for AMGT, the review is kept) + ADDENDUM B B.6 + 1.0.0_SA_CTO~Z msg 25282 (3) 'no round is held on it'; the review stays owed and is not skipped. The PRD_HEADER key refusal is CLEARED at 8da812bf80; coverage is NOTED at EXECUTING (enrichment recut).

**ISSUER NOTES:** wave 1, spawned after rl-1 merges. Interface with rl-2: the shell renders `LeadPanel` in Universe mode
only from this round; this cell strips the Security-mode branch while keeping the props type stable so both cells compile
against each other at the drain (`tsc` is the meet). AC2 is the one census in this round that admits named classes,
because the band is the ONE surface whose ink is light BY CONTRACT (C3) -- the admitted set is printed so the drain's
page-wide census can subtract it.

**ISSUER CLOSE-OUT, 2.0.0_SA_COO~Z, 2026-09-24 ~09:4xZ.** Flipped by the ISSUER; the worker left the record face alone.
3 of 3 criteria PASS, proof-of-spec rc=0 VALID (re-run by this seat inside the worker's worktree C:/tmp/wk-amgt-37-137).
leadPanelPattern.harness.cjs CHECKS-OK 12 of 12 (mutant control executed: the pre-cell filled-purple toggle flips purple_fill_classes);
ui-class-census FILES 4 TOTAL 0; errorEmpty.harness.cjs 12 of 12; tsc -b clean. TWO rows: W137-S1 (ARMED -> resolved at this drain:
the shared tabs.harness.cjs gained PanelFooter / Segmented / HelperTip stubs, portal 1267a67e; with them the harness LOADS and reads
CHECKS-WRONG-WAY on three assertions the merged page no longer satisfies by design -- rl-9's AC3), W137-S2 (INERT, `dated` is a
boolean on the live fixture, rendered from as_of_date). Drained @6b1f1d838d; portal DEV 1267a67e (merge of bf1b6149 at ae760a39 plus
the stub commit), gitlink f67117d4 -> 1267a67e. Drain-time ui-contract-check (contract-check-after-rl-8/): list purpleFills 4 -> 3
and bandContainersTopLevel 2 -> 3 (the lead panel's own containers now count as bands on the list state); weights/sizes/radii/shadows
unchanged on every state. The PASS is owed by rl-9's re-assert, which now holds rows Z-S247 and W137-S1's residue.

<status>complete</status>
<round>37</round>
<slot>~137</slot>
<fabric>site-z</fabric>
