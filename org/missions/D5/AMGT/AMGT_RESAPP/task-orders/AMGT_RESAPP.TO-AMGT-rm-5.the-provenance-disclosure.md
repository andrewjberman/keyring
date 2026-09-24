# AMGT_RESAPP task order -- `AMGT-rm-5` -- THE PROVENANCE DISCLOSURE, TWO LIMBS: `dated` typed on the payload it rides, and the "Source:" caption never clipped

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rm-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~144</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the round-37 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. Proven by react-dom/server harnesses over fixtures; no dev server, no fetch.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~144`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. First act:
print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, `test -d org && test -d .tools && echo TREE-OK`,
`grep -n 'interface RankingDateFields' portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx` (the local augmentation
this cell retires; absent = BLOCKING row, stop). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~144;`.
**NEVER RUN AN INSTALL. No vite dev server on this cell.** Never push, merge, rebase, `checkout --` or `clean`. **Portal
is a NESTED repository at `<worktree>/portal`:** portal files are committed inside it
(`cd portal && bash ../.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~144 <0.9.0_WK_AMGT_RESAPP~144@opal.agent>" -F <msgfile> -- <paths>`),
then the outer commit carries `portal` and your deliverables. Messages PURE ASCII via the Write tool. Scripts and logs under
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~144/`, never `.scratch/`.

## 1. THE CELL -- `AMGT-rm-5` (round 38, decomposition s.46) -- WAVE 0

The round-37 analysis (s.4): *"the same provenance disclosure is broken on TWO INDEPENDENT PATHS: dropped at the type
boundary on one, and truncated mid-word at the container edge on the other ... round 38 should cut them as ONE concern with
two limbs."* **Limb 1 (R-57's ruled defect):** `dated` and `requested_as_of` are EMITTED by `/rankings` and OMITTED from
`RankingSet` at `portal/src/pages/SecurityAnalysis/types.ts:181`; rl-8 typed them LOCALLY in `LeadPanel.tsx`
(`RankingDateFields`, `DatedRankingSet`) because `types.ts` was outside its paths. **Limb 2 (ADJUDICATION_v47 s.2.4):** in
`list.png` the Lead Panel's "Source:" caption is CLIPPED MID-WORD at the container's right edge -- `... -- dated 2026-09-23
(requested 2026-09-24) -- t` and it stops -- at the exact point where it discloses provenance. The strip that hosts it is
`PanelFooter` (rm-2's file, not yours); the caption's own element is yours.

**WHAT YOU BUILD.** (1) `types.ts`: `dated?: boolean` and `requested_as_of?: string` on `RankingSet` itself, with the
one-line doc rl-8 wrote (`dated` is the server's boolean "this is not today's list", never a date; the day it IS dated as is
`as_of_date`); `LeadPanel.tsx` drops `RankingDateFields`/`DatedRankingSet` and reads the fields off `RankingSet`
(`sourceFooterContent(fields: RankingSet | undefined)`, behaviour identical). (2) The caption never clips: the "Source:"
line renders as WRAPPING text inside the footer (`whitespace-normal break-words`, no `truncate`, no `nowrap`, no
`overflow-hidden` on the caption's own element or any wrapper YOU own), and where the disclosure clause is present
(`dated === true`) it renders on its OWN line beneath the generation caption rather than appended to it, so the
"this list is older than the date requested" sentence is never the tail that gets cut. The FACTS of the caption are
unchanged (`generationCaptionText`, `as_of_date`, `requested_as_of`, the clause's words). If `PanelFooter` itself imposes
`truncate`/`nowrap` on `leftContent` or `content`, you cannot fix that there -- file a row naming `PanelFooter.tsx:<line>`
for rm-2 and make your element wrap regardless.

## 2. BOUNDS

1. **Presentation and type only** (`C-PRESENTATION-ONLY`): no route, DTO, query key or served figure moves; the two fields
   are ALREADY served (R-57: "computed, served, paid for, and discarded at the type boundary").
2. **`PanelFooter.tsx`, `App.tsx`, `index.css`, `src/ui/**` are read-only** (rm-2 owns the strip).
3. **Harness arms over the ACTUAL component** (`react-dom/server`, the tabs loader), never a re-derivation.
4. **Standing:** no install, no vendor or Bloomberg call, no S3 delete, no key hunting, no push, no promote. **REFUSE, do
   not rescue.**

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/components/GenerationCaption.tsx
portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/**
portal/src/pages/SecurityAnalysis/components/RankedList.tsx
portal/src/ui/components/panels/PanelFooter.tsx
portal/scripts/ui-class-census.mjs
portal/DESIGN.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~144/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

You WRITE the first five entries (and your deliverables); every other path is a read-only input.

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rm-5"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; grep -n "dated?: boolean\|requested_as_of?: string" src/pages/SecurityAnalysis/types.ts &amp;&amp; grep -c "RankingDateFields\|DatedRankingSet" src/pages/SecurityAnalysis/components/LeadPanel.tsx; npx tsc -b --noEmit; echo "tsc=$?"</invocation><expect>LIMB 1 -- THE FIELDS TYPED WHERE THEY RIDE: both fields present on RankingSet in types.ts (the two grep lines printed, inside the RankingSet interface), the local augmentation gone from LeadPanel.tsx (count 0), and tsc clean (tsc=0)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rm-5"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs</invocation><expect>LIMB 2 -- THE CAPTION WRAPS AND THE DISCLOSURE HAS ITS OWN LINE, proven on the actual LeadPanel through react-dom/server over the fixture whose dated flag is true and whose as_of_date precedes requested_as_of: the harness gains checks source_caption_wraps (the caption element and every wrapper this cell owns carry no truncate / whitespace-nowrap / overflow-hidden class -- read off the rendered markup), disclosure_own_line (the "older than the date requested" clause renders in its own block element beneath the generation caption), and caption_facts_unchanged (generation id, as_of_date and requested_as_of all present verbatim); CHECKS-OK n of n with the three new checks named, no WRONG-WAY line</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rm-5"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-class-census.mjs src/pages/SecurityAnalysis/types.ts src/pages/SecurityAnalysis/components/LeadPanel.tsx src/pages/SecurityAnalysis/components/GenerationCaption.tsx &amp;&amp; node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs</invocation><expect>NOTHING ELSE MOVED: the census over the three files reads FILES 3 TOTAL 0, and the shared tabs harness reads CHECKS-OK 20 of 20 with no WRONG-WAY line (as at the cut)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~144/AMGT_RESAPP.TO-AMGT-rm-5.the-provenance-disclosure.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` from the
worktree root. **The status flip is the ISSUER'S**; leave the record face alone and say so. **Report once, naming:** the
three new check names and their values, whether PanelFooter imposes a clip of its own (and the row if so), the two commit
hashes, and any row. The issuer reads the list state's PNG and `clippedTextBlocks` at the drain with rm-1's instrument.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** wave 0. Item 5 of the round-37 analysis (one concern, two limbs), R-57's ruled defect and
ADJUDICATION_v47 s.2.4's clipped caption. The DOM read of the fix (list state, `clippedTextBlocks` 0 on the caption) is the
issuer's at the drain with rm-1's re-keyed instrument, not a criterion on this face (no dev server on this cell).

<status>pending</status>
<round>38</round>
<slot>~144</slot>
<fabric>site-z</fabric>
