# DSGN_AMGTV1 task order -- `AV-v-7` -- THE MODEL READS THE SERVED WORDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-v-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~20</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 09bd04b1 -- servedwords.cjs 1 of 3 (FAIL as expected: 0 of 25 served line names and 0 of 2 served formula words printed; the fallback arm passes, 25 local names on SAP GY); casewords.cjs 1 of 2 (FAIL as expected: the RAW control is exact, the WORDS export line reads missing=1 extra=1); green arms 3 of 3 and 2 of 2; bound 2 of 2 (PASS); vv-5.AC1 YES (PASS). Blind spot: static markup with the estate chrome stubbed; the served payload's words equal the local copy today, so the served-words arms render in-memory difference variants.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-v-7` (round 5, decomposition v5; serves FWD-9, FWD-11; AMGT_RESAPP's round-48 ask)

This is the SECOND order of your slot. The first, AV-v-4 (whose Base case each line is; the divergence tile's name), is already
committed on your branches by this slot; build on top of it and do not change what it built.

AMGT_RESAPP now serves ONE definition of the Model words on the /thesis payload (its order AMGT-ww-4, deployed with ww-1):
`model.line_names` (a map, Bloomberg mnemonic -> the line's name, equal today to `modelSheet.ts` `LINE_NAMES`, 25 entries) and
`model.cases.<case>.formula_words` on every served case that carries a `formula` (a port of `ModelTab.tsx` `formulaInWords`;
the page's cases block reads the top-level `model_cases`, which mirrors `model.cases`). The export (`render_pack`) will print the
same words. Build:
1. The page names its Model lines from the payload: `lineName` (`modelSheet.ts`) takes the served map and reads it first; the local
   `LINE_NAMES` stays ONLY as the fallback when the payload carries no `line_names` (then the served figure `basis.definition`,
   then the fixed phrase, as today). `ModelTab.tsx` passes `model.line_names` through `buildModelSheet`.
2. A served case's formula prints from its served `formula_words`; `formulaInWords` stays ONLY as the fallback when the case
   carries none. The whole raw `formula` keeps riding `data-model-case-formula`.
3. FWD-30's parity harness (`__harness__/exportCompare.harness.cjs`) admits the export's case line in WORDS: today its case set
   compares the export's "<head>: SERVED -- <value> (<formula>)" with the page's line rebuilt from `data-model-case-formula`, so an
   export printing "(<formula_words>)" reads missing=1 extra=1. Make the comparison accept either form for the SAME served case
   (e.g. normalise an export line's words parenthesis to the served formula, reading the fixture's own case), keeping every set
   exact and never weakening a comparison.
Optional fields: declare `line_names?: Record<string, string> | null` and `formula_words?: string | null` in `types.ts` where the
model / case types live. Nothing is looked up or joined: the words come from the producer.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: no figure is computed,
converted or guessed, no name is looked up or joined, and a value the payload does not carry reads as a designed empty state
naming, in plain words, what is missing and which team fills it -- never a project code, serial or storage path.
C-ESTATE-FIXTURES -- windows are the estate's HeroDialog + DialogStamp, panels and states are the estate's; nothing forked.
**Design law (portal `DESIGN.md`):** white panels with navy ink (C3); ONE dark band per page; no translucent white (C5.8); no
shadow (C11). A code, field name or path may sit in a data attribute or in code, never in visible text -- and text inside a
collapsed `<details>` is still visible text.

**If a bound harness check is anchored on the raw text this cell removes,** re-anchor that ONE check onto the same fact as the
page now states it (the words, or a data attribute), keep its claim, never drop it; the harness keeps at least its base
check count (the floor in the bound criterion). Only a harness named in `<paths>` may be edited. Record each re-anchor
(old anchor -> new) in the instance.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` under `portal/` change; every other page, component, tab and harness is unchanged. The next order
   of this slot edits the Model panel header's date: leave the header alone.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/modelSheet.ts
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~20/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md`, the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/` (never edit them; `thesisBundle.AMD_US_Equity.json` is the
served /thesis payload extracted from AMGT_RESAPP's round-48 capture), and
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-5.AC1.sh` (AC4's check).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-v-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/checks/servedwords.cjs"; echo "exit=$?"</invocation><expect>MODEL READS THE SERVED WORDS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-v-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/checks/casewords.cjs"; echo "exit=$?"</invocation><expect>PARITY ADMITS THE WORDS CASE LINE: 2 of 2 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-v-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/checks/bound.cjs" V7 modelPattern.harness.cjs:12 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>V7 BOUND: 2 of 2 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-v-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-5.AC1.sh"; echo "exit=$?"</invocation><expect>FWD-30 HARNESS READS THE REDESIGNED PAGE: YES -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 is the built behaviour (difference variants of the served AMD payload, and SAP GY for the fallback); AC2 the parity harness's new admission (a raw control and a words line); AC3 the bound. A FOURTH criterion, because this cell edits the FWD-30 parity harness itself: AC4 proves the harness still reads the pinned export exactly on all four sets. No judgment criterion: the words are the producer's, graded as its outcome.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~20/DSGN_AMGTV1.TO-AV-v-7.the-model-reads-the-served-words.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** AMGT_RESAPP r48's ask (msg 26588 from 2.0.0_SA_COO~Z; detail `AMGT_RESAPP.TO-AMGT-ww-4...md`), placed by
decomposition v4 "for the first round after ww-1 lands"; ww-1's NEVER-2 entry CLOSED 19:56:55Z (COO~Z msg 26689). Added to round 5
by the issuer (not an item of the round-4 analysis's list). Slot ~20's second order (after AV-v-4; then AV-v-6). Fixture
`round5/fixtures/thesisBundle.AMD_US_Equity.json` = the `payload` object of AMGT_RESAPP round48/captures/
thesis_AMD_US_Equity_20260929T200344Z.json @8f50bcb837, extracted verbatim (no edit). Base 09bd04b1: servedwords 1 of 3,
casewords 1 of 2; green arms (scratch modelSheet.ts lineName(served map) + ModelTab formula_words-first; scratch exportCompare
artifactCases normalising a words parenthesis to the fixture's formula, run via the issuer-only CASEWORDS_HARNESS) 3 of 3 and 2 of
2; V7 bound 2 of 2; vv-5.AC1 YES.

<status>pending</status>
<round>5</round>
<slot>~20</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
