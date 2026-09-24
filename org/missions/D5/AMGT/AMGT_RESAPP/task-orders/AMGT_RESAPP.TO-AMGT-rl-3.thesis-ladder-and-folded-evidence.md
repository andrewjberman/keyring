# AMGT_RESAPP task order -- `AMGT-rl-3` -- THE THESIS: one white panel, the earnings-update ladder, and every sentence's evidence folded in the DOM until asked for

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rl-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~132</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the L1 brief at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. react-dom/server harnesses only; no browser, no HTTP, no vendor call.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~132`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. First act:
print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, `test -d org && test -d .tools && echo TREE-OK`,
`test -f portal/scripts/ui-class-census.mjs && echo INSTRUMENT-OK` (absent = BLOCKING row, stop). Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~132;`. **NEVER RUN AN INSTALL. No vite dev server on this cell.** Never
push, merge, rebase, `checkout --` or `clean`. **Portal is a NESTED repository at `<worktree>/portal`:** portal files are
committed inside it (`cd portal && bash ../.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~132 <0.9.0_WK_AMGT_RESAPP~132@opal.agent>" -F <msgfile> -- <paths>`),
then the outer commit carries `portal` and your deliverables. Messages PURE ASCII via the Write tool. Scripts and logs under
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~132/`, never `.scratch/`.

## 1. THE CELL -- `AMGT-rl-3` (round 37, decomposition s.45)

- **`FWD-21` (its ladder half):** *"the Thesis renders as a recommendation line, a summary paragraph and headed sections with
  evidence FOLDED ... A PM reads the thesis without scrolling past three more dark bands. TODAY: four stacked bands,
  6,548 px of 12-px text."* (34,480 of 47,393 characters at 12px; 280 at 2.3:1 -- the purple "machine" chips at 9px.)
- **`FWD-23`:** *"a sentence shows its PASS face and a 'cites N passages' affordance; opening it reveals the passage and
  accession line FROM THE DOM; and a census prints ZERO passages carried in a native title= tooltip. ACCEPT: the verbatim
  gate (AMGT-rj-2) is preserved BY CONSTRUCTION, and a reader no longer scrolls 48 blockquotes to reach Risks."*

**The target (brief Part V, Thesis):** ONE white panel (`Panel variant="nested"`). Header: title, the drafting source and
vintage as subtitle, the held-uncited basis in the footer. Body in the earnings-update ladder: the RECOMMENDATION section
first as a highlighted line, the company description as the summary paragraph, then Investment thesis, Risks, Recommendation
(and CEO bio when it carries text) as sections with a 13px/700 eyebrow and a 4px indigo top rule (the pillar-card manner).
Each sentence at body size (16px/400 navy) with its PASS face and a "cites N passages" disclosure (`<details>`/`<summary>`
or an equivalent that keeps the passages IN THE DOM, collapsed by default); each passage quoted at body size with its
accession line at footnote size (11px). The Big Thing chart sits in a 40/60 split beside the recommendation and summary
(summary 40, chart 60), or as its own white panel when the series is ABSENT, with the ABSENT reason as the C12 EMPTY state.
The "machine" marker is a navy outline chip at label size, and the sentence "a machine's view for a person to accept or
reject" appears ONCE in the panel subtitle, not on every line.

## 2. BOUNDS

1. **Files:** `tabs/ThesisTab.tsx`, `components/ThesisDriverChart.tsx`, `__harness__/drafting.harness.cjs` (yours; keep it
   green), and the NEW `__harness__/thesisLadder.harness.cjs`. Everything else in the page directory is another cell's this
   round; `src/ui/**`, `src/components/**`, `src/api/**` read-only. `CheckFaceBadge`, `IdentityLine`, `ProvenanceLine`,
   `GenerationCaption` are being inverted by another cell IN PARALLEL -- import and render them unchanged; do not restyle
   them from your file.
2. **The contract is `portal/DESIGN.md` C1-C12:** nothing below 11px, weights 400/700, radii 2/3/4/pill, no shadow, navy
   ink, `#6B7280` secondary on a panel only, status as an icon beside navy text (C6/C9), the four designed states from
   `@/ui/components/states` for empty/loading/error/no-permission (C12) -- an empty Thesis is `PanelEmpty` in a white
   frame, never a centered sentence in a dark band.
3. **KEPT, by construction:** the verbatim gate and the PASS/REFUSE face (AMGT-rj-2) -- every sentence still carries its
   face; every passage's text is byte-identical to the bundle's; the drafting source, vintage and held-uncited count still
   render; the three-state reads never collapse. **The spec changes how these are shown, never whether.**
4. **No route, DTO, query key or figure moves** (`C-PRESENTATION-ONLY`). Nothing computed on the page.
5. **Standing:** no install, no vendor or Bloomberg call, no S3 delete, no key hunting, no push, no promote. **REFUSE, do
   not rescue:** a criterion you cannot satisfy as written is refused with its measurement.

## 3. THE HARNESS YOU ADD -- `__harness__/thesisLadder.harness.cjs`

Same loader as `drafting.harness.cjs` (actual `ThesisTab`, installed typescript, `react-dom/server`, hooks stubbed with
`__harness__/thesisBundle.drafted.BA_US_Equity.json`; a second render with `drafting_status` ABSENT). Prints
`CHECK <name> <value> (expected <value>)` per line and `CHECKS-OK n of n`. Every expected count is READ OFF THE FIXTURE,
never typed: `panel_is_light` (no `dark-band`/`variant="mixed"` in the Thesis markup) · `recommendation_first` (the first
section in DOM order is the recommendation line) · `sections_headed` == the number of drafted sections the fixture carries
with text · `disclosures` == the number of sentences with at least one cite · `passages_in_dom` == the fixture's total
evidence rows (every passage's text present in the markup) · `title_attr_passages` == 0 (no `title="` attribute whose value
contains a passage) · `accession_lines` == `passages_in_dom` · `chart_split_or_absent_state` (a 40/60 split when the series
is present; `PanelEmpty`-shaped markup with the ABSENT reason when it is not) · `machine_sentence_once` == 1 ·
`pass_faces_kept` == the fixture's sentence count.

## 4. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/components/ThesisDriverChart.tsx
portal/src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/thesisLadder.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/thesisBundle.drafted.BA_US_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/thesisBundle.BABA_US_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/components/CheckFaceBadge.tsx
portal/src/pages/SecurityAnalysis/components/IdentityLine.tsx
portal/src/pages/SecurityAnalysis/components/ProvenanceLine.tsx
portal/src/pages/SecurityAnalysis/components/GenerationCaption.tsx
portal/scripts/ui-class-census.mjs
portal/DESIGN.md
portal/src/ui/components/states/index.ts
portal/src/ui/components/panels/Panel.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~132/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

Of these you WRITE only the first four; the rest are read-only inputs.

## 5. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rl-3"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/thesisLadder.harness.cjs</invocation><expect>THE BUILT BEHAVIOUR: CHECKS-OK 10 of 10 with every CHECK line printed and its fixture-derived expected value beside it -- panel_is_light true, recommendation_first true, sections_headed equal to the fixture's drafted sections with text, disclosures equal to the sentences with cites, passages_in_dom equal to the fixture's evidence rows, title_attr_passages 0, accession_lines equal to passages_in_dom, chart_split_or_absent_state true, machine_sentence_once 1, pass_faces_kept equal to the fixture's sentence count</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rl-3"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-class-census.mjs src/pages/SecurityAnalysis/tabs/ThesisTab.tsx src/pages/SecurityAnalysis/components/ThesisDriverChart.tsx</invocation><expect>THE INVERSION IS COMPLETE ON YOUR FILES: FILES 2 TOTAL 0, both lines reading idiom=0 size=0 weight=0 radius=0 shadow=0 (the walk counted 14 + 9 = 23 before this cell; a non-zero line names the file and FAILS)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rl-3"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs</invocation><expect>THE VERBATIM GATE IS PRESERVED: CHECKS-OK 8 of 8 exactly as at DEV HEAD c1ac41ec (it read 8 of 8 before this cell); any check reading WRONG-WAY FAILS -- the drafting harness is the control that the ladder changed the SHOWING and not the drafting</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~132/AMGT_RESAPP.TO-AMGT-rl-3.thesis-ladder-and-folded-evidence.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` from the
worktree root. **The status flip is the ISSUER'S**; leave the record face alone and say so. **Report once, naming:** the
fixture-derived denominators the harness printed (sections, sentences, cites, passages), the two commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

# pipeline-override: LIMB 6 only -- the BRIEF half reads STALE at 8da812bf80 (owed by 4.0.0_SA_CRO~Z, asked 05:59Z); R-10 (Andrew-direct 2026-09-23 ~21:2xZ, 'agreed with your rec': the L4-R signature is not a BAR for AMGT, the review is kept) + ADDENDUM B B.6 + 1.0.0_SA_CTO~Z msg 25282 (3) 'no round is held on it'; the review stays owed and is not skipped. The PRD_HEADER key refusal is CLEARED at 8da812bf80; coverage is NOTED at EXECUTING (enrichment recut).

**ISSUER NOTES:** wave 1, spawned after rl-1 merges. The shared atoms this tab renders (`CheckFaceBadge`, `IdentityLine`,
`ProvenanceLine`, `GenerationCaption`) are inverted by rl-2 in parallel; this cell's census excludes them by construction
(AC2 names its two files), so a residual idiom inside an imported atom is rl-2's and the drain's page-wide census settles it.

**ISSUER CLOSE-OUT, 2.0.0_SA_COO~Z, 2026-09-24 ~08:5xZ.** Flipped by the ISSUER; the worker left the record face alone.
3 of 3 criteria PASS, proof-of-spec rc=0 VALID (re-run by this seat inside the worker's worktree C:/tmp/wk-amgt-37-132).
thesisLadder.harness.cjs CHECKS-OK 10 of 10 (4 sections, 38 sentences, 38 cited, 48 evidence records); ui-class-census FILES 2 TOTAL 0
(was 29); drafting.harness.cjs 8 of 8, 38 of 38 sentences walked. No rows. Drained @a8aa8bff17; portal DEV cd1a7146 (merge of 3c863eea),
gitlink ce3c907a -> cd1a7146. Drain-time ui-contract-check (contract-check-after-rl-3/): thesis bandContainersTopLevel 3 -> 2 and
lowContrastChars 185 -> PASS; the remaining FAILs are the untouched cells' surfaces. The PASS is owed by rl-9's re-assert.

<status>complete</status>
<round>37</round>
<slot>~132</slot>
<fabric>site-z</fabric>
