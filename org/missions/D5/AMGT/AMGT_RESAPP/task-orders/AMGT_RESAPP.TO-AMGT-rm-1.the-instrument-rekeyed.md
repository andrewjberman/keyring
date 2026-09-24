# AMGT_RESAPP task order -- `AMGT-rm-1` -- THE INSTRUMENT RE-KEYED: a band is the Panel's own marker, a strip is counted separately, action fills exclude the C8 set, clipped text is counted, and the page is graded inside its own main

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rm-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~140</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the round-37 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. Renders against a LOCAL vite dev server with the stubbed session and fixtures; no fetch to any origin but localhost.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~140`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. First act:
print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, `test -d org && test -d .tools && echo TREE-OK`,
`test -f portal/scripts/ui-contract-check.mjs && echo INSTRUMENT-OK`, and `sed -n '65p' portal/scripts/ui-measure.mjs` (the
line you are re-keying; print it before you touch it). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~140;`.
**NEVER RUN AN INSTALL.** Never push, merge, rebase, `checkout --` or `clean`. **Portal is a NESTED repository at
`<worktree>/portal`:** portal files are committed inside it
(`cd portal && bash ../.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~140 <0.9.0_WK_AMGT_RESAPP~140@opal.agent>" -F <msgfile> -- <paths>`),
then the outer commit carries `portal` and your deliverables. Messages PURE ASCII via the Write tool. Scripts, logs and
captures under `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~140/`, never `.scratch/`.

## 1. THE CELL -- `AMGT-rm-1` (round 38, decomposition s.46) -- WAVE 0

**`FWD-29`** (PRD v0.26 ENDPOINT fence): *"for each of the six states the JSON reads bandContainersTopLevel == 1, fonts ==
{Lato}, weights within {400,700}, no size below 11, radii within {2,3,4,pill}, shadows == 0 outside the focus ring,
lowContrastChars == 0, purpleFills per FWD-27 ..."* -- a check that PASSES and CAN FAIL. Round 37 proved it CAN FAIL. Round 38
begins by making it measure what the contract names, because today it does not (measured by `4.0.0_SA_CRO~Z` @`88f08c0c7a`
and by the rl-9 worker's own dump):

1. **The band predicate counts the wrong colour.** `ui-measure.mjs:65` defines a band as computed background within 3 of
   `rgb(10,23,51)` (#0A1733). Since the portal-wide named layers (`index.css:371`), `--bg-band` resolves to `--layer-body`
   (rgb 25,38,67), while #0A1733 is `--layer-strip`: the panel TITLE STRIP (`PanelHeader.tsx:62`, `PanelFooter.tsx:92`,
   `bg-[hsl(var(--bg-header))]`) and the sidebar `<aside>` (`App.tsx:271`). So `Panel variant="mixed"` -- the identity header
   in Security mode and the Lead Panel in Universe mode, the ONE band C3 names -- is NEVER counted, and only strips and the
   sidebar are. `peers` reading 1 is the sidebar.
2. **The purple predicate counts C8-LEGAL identity accents** (the page-title rule `PageHeaderVariants.tsx:40`, the sidebar's
   active item and avatar) beside ACTION fills.
3. **The page is graded together with chrome it does not own** (the sidebar is Andrew's reserved card, s.46b.2).
4. **Clipped text is not measured at all** (ADJUDICATION_v47 s.2.4: a provenance caption clipped mid-word, and `DESIGN.md`
   has no clause to cite -- the measurement is the input to that clause).

**WHAT YOU BUILD, in `scripts/ui-measure.mjs` and `scripts/ui-contract-check.mjs` (and `ui-smoke.mjs` only if a scope needs it):**
(1) **Bands by the Panel's own marker:** `bandContainersTopLevel` counts top-level elements carrying the `.dark-band` class the
Panel emits for `variant="chart"|"mixed"` (`Panel.tsx:89-90`), OR whose computed background equals the RESOLVED `--bg-band`
value read off `document.documentElement` at measure time -- never a hard-coded rgb. (2) **Strips counted separately:** a new
`stripContainers` field counts elements whose computed background is the resolved `--bg-header` (the title strips and the
sidebar), so the old number is not lost, it is renamed to what it measures. (3) **`--scope main|body`** on both scripts:
`main` measures inside `document.querySelector('main')` (the page's own region), `body` measures the whole document; the
contract table is graded on `main` and the `body` table is PRINTED beside it, never hidden. (4) **Action fills, not identity
accents:** `purpleFills` counts elements filled with the resolved `--semantic-action-primary` that are interactive (button, a,
[role=button], input) and EXCLUDES the C8 identity set by selector -- the page-title rule (`.w-\[3px\]` beside `h1` in the
page header), the sidebar's active nav item and the avatar (both inside `aside`). Print the excluded count as
`identityAccents`. (5) **Clipped text:** `clippedTextBlocks` counts text-bearing elements whose `scrollWidth > clientWidth + 1`
under an `overflow: hidden|clip` or `text-overflow: ellipsis`, with up to 8 samples (tag, first 60 chars, the clipped tail).
(6) The contract check prints BOTH tables (`scope=main` graded, `scope=body` informational) and adds the two new columns
`stripContainers` and `clippedTextBlocks` (informational this round -- not graded PASS/FAIL, printed with their values).

## 2. BOUNDS

1. **The dev server:** from `portal/`, the bun binary at
   `C:/Users/Opal Bloomberg/AppData/Local/Microsoft/WinGet/Packages/Oven-sh.Bun_Microsoft.Winget.Source_8wekyb3d8bbwe/bun-windows-x64/bun`
   (`"<bun>" run dev --port 5182 > ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~140/dev.log 2>&1 &`),
   wait for `Local:` (up to 90 s), run, then stop it by the PID you recorded. Port **5182**.
2. **You change WHAT a predicate MEASURES only where s.1 names the mis-key, and you print the OLD and NEW reads side by side**
   for every state (the old `bandContainersTopLevel` becomes `stripContainers`; the old `purpleFills` becomes
   `purpleFills + identityAccents`). No threshold, set or predicate is weakened; nothing is special-cased per state.
3. **No page or component source moves**: `src/**` is read-only for this cell (the fixture DOMs under `__harness__/tests/`
   are yours). `Panel.tsx` is READ for its marker, never edited. `App.tsx` and `index.css` are touched by no cell this round.
4. **Standing:** no install, no vendor or Bloomberg call, no S3 delete, no key hunting, no push, no promote. **REFUSE, do
   not rescue.**

## 3. SURFACES

<paths>
portal/scripts/ui-measure.mjs
portal/scripts/ui-contract-check.mjs
portal/scripts/ui-smoke.mjs
portal/src/pages/SecurityAnalysis/__harness__/tests/**
portal/src/ui/components/panels/Panel.tsx
portal/src/index.css
portal/src/App.tsx
portal/DESIGN.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~140/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

You WRITE the three scripts and files under `__harness__/tests/`; everything else is read-only.

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rm-1"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-measure.mjs --self-test --fixture src/pages/SecurityAnalysis/__harness__/tests/uiMeasureFixture.html</invocation><expect>THE CLASSIFIERS PROVEN ON A FIXTURE DOM (a static page you write under __harness__/tests/ carrying: one Panel-style div with class dark-band and background var(--bg-band); one strip div with background var(--bg-header); one interactive button filled with var(--semantic-action-primary); one 3px identity rule and one avatar circle filled with the same colour; one text block that overflows its overflow-hidden container; body-level chrome outside main): prints bandContainersTopLevel 1, stripContainers 1, purpleFills 1, identityAccents 2, clippedTextBlocks 1 with its sample, and SELF-TEST OK -- and a NEGATIVE ARM (the same fixture with the dark-band class removed and the strip recoloured) prints bandContainersTopLevel 0, stripContainers 0; exit 0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rm-1"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-contract-check.mjs --port 5182 --scope main --out ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~140/contract-check-rekeyed; echo "exit=$?"</invocation><expect>THE SIX STATES RE-MEASURED INSIDE MAIN, both tables printed: for scope=main every state reads bandContainersTopLevel equal to the Panel-marker count (the identity header on the five Security-mode states, the Lead Panel on list -- print the value, and a state reading other than 1 is REPORTED with the element, never tuned), stripContainers printed per state, purpleFills counting action fills only with identityAccents printed beside it, clippedTextBlocks printed per state with samples (list's provenance caption expected among them); the scope=body table printed beneath with the OLD numbers (the sidebar counted) so the two reads sit side by side; a PNG larger than 20 KB and a JSON per state; a FAIL cell on the graded predicates is reported with its value and left standing (the fixes are other cells'); exit reflects the graded main table</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rm-1"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-contract-check.mjs --port 5182 --scope body --states list --out ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~140/contract-check-body-control &amp;&amp; node scripts/ui-class-census.mjs src/pages/SecurityAnalysis | tail -1</invocation><expect>THE SCOPE FLAG DISCRIMINATES AND NO PAGE SOURCE MOVED: scope=body on list reads stripContainers strictly greater than scope=main's on the same state (the sidebar strip counted only in body) and identityAccents strictly greater (the sidebar's active item and avatar counted only in body), both pairs printed; then the page census reads FILES 31 TOTAL 0 exactly as at the cut (this cell edits no page file)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~140/AMGT_RESAPP.TO-AMGT-rm-1.the-instrument-rekeyed.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` from the
worktree root. **The status flip is the ISSUER'S**; leave the record face alone and say so. **Report once, naming:** the
old and new band reads per state (six pairs), the strip counts, the action-fill and identity-accent counts, the clipped
blocks with the list caption's sample, the two commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** wave 0. The measurement that re-shapes this cell is `4.0.0_SA_CRO~Z`'s (msg 25505, @`88f08c0c7a`),
corroborated by the rl-9 worker's own dump ("ASIDE + one PanelHeader-styled DIV"); the CTO was told at the issuance that
items 1 and 2 of the round-37 analysis are re-shaped on it (s.46b). rm-2, rm-3 and rm-6 spawn after this cell merges.

**ISSUER CLOSE-OUT, 2.0.0_SA_COO~Z, 2026-09-24 ~14:1xZ.** Flipped by the ISSUER; the worker left the record face alone.
Instance VALID (re-run by this seat inside the worker's worktree C:/tmp/wk-amgt-38-140). AC1 PASS: the classifiers proven on the fixture
DOM, 7 of 7 assertions, positive and negative arms (bands 1/0, strips 1/0, purpleFills 1, identityAccents 2, clippedTextBlocks 1),
SELF-TEST OK. AC2 PASS: inside main every one of the six states reads bandContainersTopLevel 1 (the Panel marker), strips and
action-vs-identity fills printed, the body table beneath. AC3 FAIL BY THE INVOCATION'S OWN SHAPE, the issuer's defect, not the
cell's: the face chained the body-control run and the census with `&&`, and the check exits 1 on list at every scope on the
weights/radii FAILs bound 2 forbids fixing, so the census line could never print from that invocation (row W140-S2, disarm owner
this seat -- disarmed by this close-out: the issuer read the census in the worker's tree, FILES 31 TOTAL 0, and the src diff
against the base is the fixture HTML alone; the scope pairs the worker printed are corroborated on the shared portal after the
merge: stripContainers list 2 -> 3, identityAccents 1 -> 3 body over main). Row W140-S1 (INERT, dismissed with reason): the
face's `document.documentElement` instruction for resolving --bg-band would have reproduced the strip/band conflation; the
worker resolved off document.body and said so. Drained @9c9ff2bbf3; portal DEV c7b022a1 (merge of b51330c5), gitlink 2b410046 ->
c7b022a1. THE ROUND'S NEW BASELINE, read on the shared portal at c7b022a1 with the re-keyed instrument, scope=main
(contract-check-after-rm-1/): bands PASS 6 of 6; purpleFills PASS 6 of 6; shadows PASS 6 of 6; clippedTextBlocks 0 on all six (rm-5's
caption fix landed and reads clean); lowContrast PASS; sizes PASS on four, [10] on thesis and model; weights [300,600] on five and
[300] on peers; radii [8px] on five, PASS on peers. Body scope beneath carries the sidebar's 500 / shadow / size-10 as expected.
rm-2 owns the 300 and the strip radii; rm-3 attributes the 600, the 10px and the peers-vs-others radii difference.

<status>complete</status>
<round>38</round>
<slot>~140</slot>
<fabric>site-z</fabric>
