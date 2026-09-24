# AMGT_CORPUS ROUND 2 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-24 ~18:0xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND2_DRAIN_END_PACKET.md` (FINAL ~15:0xZ, read to EOF).
⚠ **The L8 hand-off MESSAGE never reached this lane** -- nothing at 15:06Z in `inbox/3.0.0_SA_CVO/~Z/`
and nothing recent in the base inbox either. The packet is an ARTIFACT and was read from disk, so the work
was never actually blocked on the message; recorded because a seat waiting on a send that was made to a
different address is the silent-hole class, and because the hold-lift message (msg 25680) went unsent to
this lane by the same shape within the same hour.

**L7 state, RE-MEASURED not adopted:** 6 of 6 `d-*` orders terminal on the LAST `<status>` tag.

---

## 1. L8 -- THE CHANNEL COMPILE (round 2's rows)

`_latest_dispositions('.','AMGT_CORPUS')` read **33 ids, ALL 33 UNDER_INVESTIGATION** before this file --
nothing has ever been folded on this project, including round 1's rows, because `ADJUDICATION_v4` recorded
its dispositions in **prose** rather than through the `adjudicates` field the resolver reads. That is the
same carrier-form gap `AMGT_RESAPP-Z-S259`/`-S260` measured today, and it is **named here rather than
silently repaired**: this adjudication folds ROUND 2's rows only. Round 1's residue is prior-round business
and is left for a deliberate act, not swept into this round's count.

| row | standing | disposition here |
|---|---|---|
| `Z-S10` | INERT | **GRADUATED** -- AC3 tail window on the readonly proof |
| `Z-S12` | INERT | **GRADUATED** -- owner's disarm carrier for `Z-S6..S9` |
| `Z-S13` | ARMED | **GRADUATED** -- the 08:02Z served-output incident; disarmed by `Z-S14`, both conditions MET |
| `Z-S14` | INERT | **GRADUATED** -- the carrier itself |
| `Z-S15` | INERT | **GRADUATED** -- the committed batch file is a test fixture; enrichment item 4 |
| `Z-S16` | ARMED | **GRADUATED** -- the post-fire twins exposure; disarmed by `Z-S19` (re-mint under a fresh pair, UNRESOLVED 60 -> 40, 214 of 214 keys) |
| `Z-S18` | INERT | **GRADUATED** -- the sequence omitted `backlog --write`; corrected chain ran |
| `Z-S19` | INERT | **GRADUATED** -- the carrier for `Z-S16` |
| `W1-S3` | worker | **GRADUATED** -- the `portal/` read caveat; independently corroborated (below) |
| `W1-S4` | worker | **GRADUATED** -- 9 of 10 workbook-only folders carry an all-fields-absent shell |
| `W2-S4` | worker | **GRADUATED** |
| `Z-S17` | ARMED | **CARRIED OPEN** -- `sector_template`'s `total`; a c-7 cell, enrichment item 2 |
| `Z-S20` | ARMED | **CARRIED OPEN** -- this seat's own; the round-3 measurement R-77 named |

## 2. L9 -- THE TWO JUDGMENT CRITERIA (never self-graded)

⛔ **THE PACKET'S s.4 PARAPHRASE DOES NOT MATCH EITHER FACE, AND GRADING FROM IT WOULD HAVE GRADED THE
WRONG THING.** The packet summarises them as *"the PDF pillar branch's thesis_summary reads as the team's
own"* and *"the composed dossier reads composed-never-authored"*. The orders say something else:

- `d-2` AC4 (`:105`): *"AC3's printed pillars for the PDF-only name **beside the pack's own text at the
  cited pages**. Are the leads the team's leads, and is the split between pillar and section correct?"*
- `d-3` AC4 (`:135`): *"`DOSSIER_INTERFACE.md`. Does the side-by-side name a **true intersection** with
  `ThesisBundle`, and does every field with no slot **say so rather than being mapped by force**?"*

Both faces instruct the worker to record **with NO verdict**, and both instances did exactly that --
`status: UNVERIFIABLE-BY-INSTRUMENT`, `judgment: true`, substitute oracle named. That is the rule working.

### `d-2` AC4 -- **PASS**

The criterion is explicitly two-sided and only one side was in the instance. This seat fetched the pack
itself (`s3://opal-data-harvest/.../ASML research pack 5_5_2026.pdf`, 2,876,211 bytes, 29 pages) and read
**page index 2** -- the cited page -- rather than the extract, because the extract shares its extractor
with the thing under test.

**3 of 3 strings are VERBATIM in the pack's own text:**

| AC3 printed | in the pack at page index 2 |
|---|---|
| `thesis_summary` "The most advanced modern technology does not exist without ASML. Fundamentals are strong with sales growing low-teens, operating margin 35% and growing, solid free cash flow (margin 34%) and net cash on the balance sheet." | **verbatim**, under the pack's own `INVESTMENT THESIS:` lead |
| pillar 1 "Secular growth tailwinds trump short-term cyclicality in this trillion dollar market" | **verbatim**, as a bold lead followed by `:` and its paragraph |
| pillar 2 "Monopoly in EUV lithography with an impregnable moat" | **verbatim**, same bold-lead-plus-colon shape |

**Are the leads the team's leads? YES -- decisively, because they are LIFTED and not GENERATED.** Nothing
was synthesised; the pipeline reproduced the analyst's own words.

**Is the split between pillar and section correct? YES.** The pack's structure is `INVESTMENT THESIS:` ->
a summary paragraph -> then bold-lead-plus-paragraph items. The branch put the summary paragraph in
`thesis_summary` and the bold leads in `thesis_pillars`, stripping the colon and body from each lead. That
is the document's actual structure, not an imposed one.

### `d-3` AC4 -- **PASS, with one cited defect**

**Does every field with no slot say so rather than being mapped by force? YES, and better than the ask.**
The sheet refuses a binary and grades the gap: **5 TRUE INTERSECTIONS**, 1 NAME-MATCHED-SHAPE-NARROWER
(`management`, a cited passage BESIDE the filing roster, never a replacement), 1 **PARTIAL** explicitly
*"not claimed as a full intersection"* (`model_rows` carries no figures under FWD-12, so it can answer
`model_status` and cannot populate `fiscal_year_figures`), and the rest **"no slot today"** with a reason.
It then volunteers the two REVERSE-direction gaps (`ceo_bio`, `posture`) *"though the order only asks for
the dossier-side gap"* -- unasked symmetry, which is the tell of a sheet written to be checked.

**Does the side-by-side name a true intersection? YES -- and this seat verified the half the worker could
not.** The sheet's own READ CAVEAT states the `ThesisBundle` column was built **entirely from the task
order's inlined quotation** of `types.ts`, never a live read, because that worktree had an empty `portal/`
and a tracked-empty `.gitmodules`. **This worktree can read it.** All **11** slots the sheet names --
`drafted_sections`, `company_description`, `investment_thesis`, `risks`, `ceo_bio`, `recommendation`,
`management`, `model_cases`, `model_status`, `fiscal_year_figures`, `posture` -- are PRESENT in the live
`portal/src/pages/SecurityAnalysis/types.ts` (42,047 bytes). The quotation was faithful.

⛔ **THE DEFECT: the sheet cites `types.ts:955`; `ThesisBundle` is declared at `:969`.** `:955` now lands
inside `ScoresBlock`'s docstring. The CONTENT is accurate and the COORDINATE has moved -- the exact class
CLAUDE.md documents about itself (*"a citation ages separately from the text it quotes"*), inside a sheet
whose whole authority is a quotation. Cited, not fatal: the substance survived an independent check.

⭐ **AND `W1-S3` IS INDEPENDENT CORROBORATION OF THIS SEAT'S OWN `AMGT_RESAPP-Z-S255`.** That worker hit
the tracked-and-empty `.gitmodules` hours earlier, from the opposite direction -- it BLOCKED a read, where
this seat found it while censusing gate coverage. Two seats, two instruments, two purposes, one fact.

## 3. L10 PRECONDITION -- three clauses, measured

1. **Every task order terminal** -- 6 of 6, last-tag read. **MET**
2. **Every round-2 row dispositioned** -- 11 graduated above, 2 carried open with named reasons. **MET**
3. **Every judgment criterion graded** -- 2 of 2, both against the independent side. **MET**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S5",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-24T18:05:00Z",
    "one_line": "L9 round 2: BOTH judgment criteria PASS, each graded against the side the worker could not reach -- d-2's pillars verified VERBATIM against the pack's own PDF page rather than against the extract, and d-3's ThesisBundle column verified against the live types.ts rather than against the order's inlined quotation. One cited defect: the interface sheet's line citation is stale (:955; the type is at :969).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": ["AMGT_CORPUS-Z-S10", "AMGT_CORPUS-Z-S12", "AMGT_CORPUS-Z-S13", "AMGT_CORPUS-Z-S14", "AMGT_CORPUS-Z-S15", "AMGT_CORPUS-Z-S16", "AMGT_CORPUS-Z-S18", "AMGT_CORPUS-Z-S19", "AMGT_CORPUS-Z-W1-S3", "AMGT_CORPUS-Z-W1-S4", "AMGT_CORPUS-Z-W2-S4"],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, NOT ADOPTED: 6 of 6 d-* orders terminal on the LAST <status> tag of each face.",
        "THE PACKET'S s.4 PARAPHRASE OF BOTH JUDGMENT CRITERIA IS WRONG AND GRADING FROM IT WOULD HAVE GRADED THE WRONG THING. It renders them as 'thesis_summary reads as the team's own' and 'the composed dossier reads composed-never-authored'. The faces say: d-2 AC4 is AC3's pillars BESIDE THE PACK'S OWN TEXT AT THE CITED PAGES, asking whether the leads are the team's and whether the pillar/section split is correct; d-3 AC4 is DOSSIER_INTERFACE.md, asking whether the side-by-side names a TRUE INTERSECTION with ThesisBundle and whether every no-slot field SAYS SO rather than being mapped by force. Criteria were read from the faces at :105 and :135.",
        "d-2 AC4 PASS, VERIFIED AGAINST THE PACK RATHER THAN THE EXTRACT. The criterion is two-sided and the instance held one side, so this seat fetched s3://opal-data-harvest/amgt/harvest/bronze/research-report/security_key=ASML_NA_Equity/37aa7a78aca3d4fc/ASML research pack 5_5_2026.pdf (2876211 bytes, 29 pages) and read page index 2 -- the cited page. The extract was deliberately NOT used as the comparand because it shares its extractor with the branch under test. 3 of 3 strings VERBATIM in the pack: the thesis_summary under the pack's own 'INVESTMENT THESIS:' lead, and both pillars as bold leads each followed by a colon and a paragraph.",
        "SO THE TWO QUESTIONS ANSWER CLEANLY. Are the leads the team's leads? YES -- they are LIFTED, not GENERATED; the pipeline reproduced the analyst's own words. Is the pillar/section split correct? YES -- the pack runs 'INVESTMENT THESIS:' then a summary paragraph then bold-lead-plus-paragraph items, and the branch put the summary in thesis_summary and the bold leads in thesis_pillars, stripping each colon and body. That is the document's own structure rather than an imposed one.",
        "d-3 AC4 PASS ON THE NO-SLOT HALF, AND BETTER THAN THE ASK. The sheet grades the gap instead of forcing a binary: 5 TRUE INTERSECTIONS, 1 NAME-MATCHED-SHAPE-NARROWER (management is a cited passage BESIDE the filing roster, never a replacement), 1 PARTIAL explicitly 'not claimed as a full intersection' (model_rows carries no figures under FWD-12, so it can answer model_status and cannot populate fiscal_year_figures), the rest 'no slot today' each with a reason. It then volunteers the two REVERSE-direction gaps (ceo_bio, posture) though the order asks only for the dossier side.",
        "d-3 AC4 PASS ON THE INTERSECTION HALF, VERIFIED ON THE HALF THE WORKER COULD NOT REACH. The sheet's READ CAVEAT states its ThesisBundle column came ENTIRELY from the order's inlined quotation of types.ts, never a live read, because that worktree had an empty portal/ and a tracked-empty .gitmodules, and it names a re-verification owner. This worktree CAN read the file: all ELEVEN named slots (drafted_sections, company_description, investment_thesis, risks, ceo_bio, recommendation, management, model_cases, model_status, fiscal_year_figures, posture) are PRESENT in the live portal/src/pages/SecurityAnalysis/types.ts, 42047 bytes. The quotation was faithful.",
        "THE ONE CITED DEFECT: the sheet cites types.ts:955 and ThesisBundle is declared at :969; :955 now lands inside ScoresBlock's docstring. Content accurate, coordinate moved -- the class CLAUDE.md documents about itself, inside a sheet whose entire authority is a quotation. Not fatal, because the substance survived an independent check; cited because the next reader of that sheet will follow the number.",
        "W1-S3 IS INDEPENDENT CORROBORATION OF THIS SEAT'S OWN AMGT_RESAPP-Z-S255. The worker hit the tracked-and-empty .gitmodules hours earlier from the opposite direction -- there it BLOCKED a read, here it was found while censusing gate coverage. Two seats, two instruments, two purposes, one fact.",
        "THE PROJECT HAD NEVER FOLDED A DISPOSITION: _latest_dispositions read 33 ids and ALL 33 UNDER_INVESTIGATION before this file, because ADJUDICATION_v4 recorded round 1's dispositions in PROSE rather than through the adjudicates field the resolver reads -- the same carrier-form gap AMGT_RESAPP-Z-S259/-S260 measured today. This adjudication folds ROUND 2's rows only; round 1's residue is prior-round business and is named rather than swept into this round's count."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "ROUND2_DRAIN_END_PACKET.md s.4 names two judgment criteria owed to the CVO and paraphrases each; s.1 asserts 6 of 6 orders terminal; s.3 lists the round's rows for disposition.",
    "world_is": "The orders are terminal as stated and the rows are as listed, but the s.4 paraphrase of BOTH judgment criteria differs from what the faces actually ask, in a direction that would have sent the grader at the wrong artifact in both cases. Graded from the faces, both criteria PASS -- and both only after reading the side the worker's instance could not hold: the pack's own PDF page for d-2, the live types.ts for d-3.",
    "notes": "TWO ROWS CARRIED OPEN BY DESIGN: Z-S17 (sector_template's corpus-wide `total` in a body keyed on per-subject inputs) is a c-7 cell and enrichment item 2, unremedied this round; Z-S20 is this seat's own and carries the round-3 measurement R-77 named, which Andrew's 17:4xZ universe decision has since made a question about roughly half the goal denominator rather than an adjacent one. AND THE PROCESS NOTE WORTH MORE THAN EITHER GRADE: the packet's paraphrase of a judgment criterion is the one place a summary CANNOT be trusted, because the criterion IS the wording -- a mechanical criterion carries an invocation that fails loudly when misread, and a judgment criterion carries only a sentence, so a paraphrase of it silently redirects the only oracle it has."
  }
]
```
