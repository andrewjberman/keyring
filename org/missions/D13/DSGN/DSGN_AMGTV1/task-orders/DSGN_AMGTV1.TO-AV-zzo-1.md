# DSGN_AMGTV1 task order -- `AV-zzo-1` -- THE THESIS WINDOW SAYS NOTHING FALSE ABOUT THE DESCRIPTION, AND A FIGURE OPENS ITS PASSAGE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzo-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~135</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; page files, harnesses and issuer checks, run offline.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 against portal ce3b0cc4 (= origin DEV, round 62) -- r63b.cjs 1 of 5 (arms 1-4 FAIL as expected; PLANTED passes); battery29 ALL PASS at the base (round-62 candidates).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzo-1` (round 63, decomposition v63; serves FWD-27 and the layout outcomes)

Paths are under `portal/src/pages/SecurityAnalysis/`. Read `org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round62.md` section 2 first. Do the items in this order.

The Thesis card opens a window (`components/ThesisCards.tsx`, `ThesisCardDetail`) that prints each sentence of the section with the
passages it rests on under it (`SentenceBlock`).

1. **No false absence** (`ThesisCardDetail`, the `hasDescription && description &&` branch, about lines 362-386). The served
   `description_verdict_state` tests only the section's FIRST sentence. On ASML it reads FAILED while the section serves 1,535
   characters of business text, and the page then prints "No company description is on file yet." above that text. Remove that line
   from the branch that prints the description's sentences. When there is no description at all, the existing `missingLine` path
   already says so. Keep `data-thesis-description-verdict` on the wrapper as it is: instruments read the verdict there.
2. **No fixed caption.** Head the description by its served label, `heading={description.label}`, whatever the verdict. Remove the
   string "Filed detail (does not describe the business)" from the file. The page states nothing about whether the text describes the
   business.
3. **Figures as pieces** (NEW file `components/thesisSpans.ts`, which imports nothing from the page or the app):
   `export function splitOnSpans(text, spans)` returns pieces `[{ text, span }]`.
   - The pieces' texts join back to the sentence exactly.
   - Each served span that occurs in the text is its own piece with `span: true`: its first occurrence at or after the previous span,
     taken in the served order, never overlapping.
   - A span not found is skipped. No spans (empty or absent) gives one piece with `span: false`.
   - Nothing is computed: the spans are the sentence's served `quoted_spans`.
4. **A figure opens its passage** (`SentenceBlock`):
   - Draw the sentence text through `splitOnSpans(sentence.text, sentence.quoted_spans)`.
   - Each span piece is a `<button type="button" data-figure-span="">` styled as inline text (underlined, same size). It names the
     sentence's first passage with `aria-controls`; give that passage's `blockquote` a stable id.
   - Pressing it scrolls that passage into view and focuses it (`tabIndex={-1}` on the blockquote).
   - A sentence with no evidence draws its spans as plain text.
   - Any change to `__harness__/` must keep each harness's claim (re-anchor only; record each re-anchor in the instance).
5. **AMENDMENT 1 (after the close walk) -- the whole sentence is the press, laid out inline.** This replaces item 4's per-span button.
   The walk on ASML at 11:24Z showed two problems:
   - the served `quoted_spans` are phrases, not figures, so "EUR 2.9 billion" stayed unpressable;
   - each span `<button>` rendered inline-block, so a long quoted phrase broke its sentence onto a new line.

   Change `SentenceBlock` so that:
   - The sentence's text sits inside ONE `<button type="button" data-sentence-press="">`, styled to read as running text: class
     `inline` (never `inline-block`, `block` or a flex layout), `text-left`, the sentence's own font, no border or background. A hover
     underline and a focus ring are allowed.
   - That button names the sentence's first passage with `aria-controls`. Pressing it scrolls that passage into view and focuses it,
     exactly as item 4's button does today.
   - Inside it, each served span piece from `splitOnSpans` is a `<span data-figure-span="">` (underlined), never a button. Plain pieces
     stay plain text. The machine chip and the check badge stay outside the button.
   - A sentence with no evidence draws its text and spans with no button.
   - AC1 is r63b.cjs, whose arm 4 now reads this.

## 2. BOUNDS

1. No server, no fetch, no network, no install (`bun install`, `bun add`, `npm`, `npx` are refused here), no push, no deploy.
   REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel).
3. **Move and fold, never reword served text; never compute a figure the page does not serve** (C-PRESENTATION-ONLY).
   `reasonWords.ts` and `cscTable.ts` are not yours. No non-ASCII characters (use `--`). Keep each file's line endings as you find
   them (read them first). Edit tool for existing files.
4. Portal files commit inside `portal/` on your portal branch (set the author with `-c user.name=... -c user.email=...`; the nested repo
   has no identity), then the outer commit with safe-commit. Do not commit the portal gitlink.
5. If an item cannot be met within your paths, file a row and stop on that criterion. In particular, if battery29 goes red on a
   harness file outside your paths, file a row naming the harness and the assertion, and stop: the issuer rules it.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx
portal/src/pages/SecurityAnalysis/components/thesisSpans.ts
portal/src/pages/SecurityAnalysis/__harness__/
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~135/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `lib/research/api/scoped_amgt.py` (company_description_verdict, ~:4260-4300), and the issuer's check `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round63/checks/r63b.cjs` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzo-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round63/checks/r63b.cjs"; echo "exit=$?"</invocation><expect>ROUND 63 THESIS WINDOW: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzo-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzo-1" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded on the issuer's signed-in walk at the close (never self-graded): ASML's Thesis window prints its description under its own label with no 'No company description' line, and pressing a figure moves to its passage.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~135/DSGN_AMGTV1.TO-AV-zzo-1.proof_of_spec.json`
(AC3 UNVERIFIABLE-BY-INSTRUMENT, status_reason "graded at the round-63 close walk"). **Flip this order's `<status>` to `complete` in the
SAME commit as your proof instance**, only when AC1 and AC2 pass.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W135-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the diff (per file, one line each), the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**REOPENED (AMENDMENT 1, 2.0.0_SA_COO~D1, 2026-10-09 ~11:3xZ):** AC3 missed in part on the close walk (`tmp/ui-walk/20261009T112329Z` shot 008, ASML_NA_Equity Investment-thesis window). Items 1-2 read as ordered (the 'COMPANY DESCRIPTION' heading, no false absence). Item 4's per-span buttons left the figures unpressable (the served spans are phrases) and broke sentences onto new lines (inline-block). Item 5 replaces item 4; r63b arm 4 is amended to read it. The first build @e469fa1021 stays merged; the fix lands as a second commit on candidate f8eee17d. Graded by no gate limb at cut (a modification; GATE viii does not apply, `<placeholders>` NONE).

**ISSUER NOTES:** round 63 = `ledger/ROUND_ANALYSIS.round62.md` @4b7ce964a2 section 2, five items in three cells by file surface
(decomposition v63). Prep: `round63/PREP.md`. Base portal ce3b0cc4 (= origin DEV). LF only (ruling R2, row D1-S1).

<status>complete</status>
<round>63</round>
<to_id>DSGN_AMGTV1.TO-AV-zzo-1</to_id>
<slot>~135</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
