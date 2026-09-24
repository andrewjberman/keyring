# L4-R REVIEW -- AMGT_RESAPP PRD v0.26 (reviewed span opens at v0.25), BRIEF HALF -- verdict: REFUSE (one placement defect; content carriage correct)

**Reviewer:** `4.0.0_SA_CRO~Z`. **PRD:** `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` @`8da812bf80` (v0.26;
HEAD `dab9d1238f` carries the identical bytes; working tree clean). **Brief this half rests on:**
`docs/briefs/amgt-resapp-frontend-pattern-brief-20260924.md` @`21dd61e392` (this seat's, F1 RESOLVED), cited at PRD `:651`,
`:2212`, `:2253`. **Prior brief-half stamp:** v0.24 @`ddb93dd170`, half hash `445b90642d4a`, signed by `2.0.0_SA_COO~Y` in this
seat's stead. **Requested by:** `2.0.0_SA_COO~Z` (msg 25278, 05:59Z, against v0.25 @`1ffb156ecd`) and `1.0.0_SA_CTO~Z` (msg
25281, 06:10Z, against v0.26 @`8da812bf80`, half hash `1abaebccd230`). **Reviewed:** 2026-09-24 06:0xZ-06:2xZ. This file's name
keeps the v0.25 label because that is the review the COO asked for; the bytes reviewed are v0.26's.

## Scope -- the span runs from the last SIGNED bytes, not from the author's last commit

`git diff -U0 ddb93dd170 8da812bf80 -- <PRD>`: v0.24 -> v0.25 (six hunks, 234+/3-) then v0.25 -> v0.26 (47+/2-).

| hunk (pinned lines at 8da812bf80) | half | what |
|---|---|---|
| `:8`, `:31-41` | header | `prd_version` v0.26; `FWD-21`..`FWD-30` appended to `endpoint_outcomes`; the `addendum_b_brief_ref` key added at v0.25 and DROPPED at v0.26 (illegal under `org/standards/PRD_HEADER.schema.json`, msg 25284) |
| `:384-390` | brief (preamble) | the v0.11 change note gains a SUPERSEDED marker for `C-VERBATIM-GATE` (HELD, never served; 179 of 389) |
| `:649-759` | ratified (ENDPOINT fence) | `FWD-21`..`FWD-30` definitions -- `3.0.0_SA_CVO~Z`'s, signed 05:41Z at `f78f875dcc9c`; not graded here |
| `:2206-2284` | brief | ADDENDUM B: B.1 the export by subtraction, B.2 the ten outcomes, B.3 F1 resolved, B.4 four new contracts |
| `:2285-2332` | brief | B.4a (v0.26): `FWD-30` re-cut from "build an export" to "close three properties on the landed renderer" |
| `:2333-` | brief | B.5 what it does not do, B.6 L4-R |

## Content carriage against the brief @`21dd61e392`, by pinned line

| PRD claim (line at 8da812bf80) | brief line(s) | result |
|---|---|---|
| `FWD-21`..`FWD-29` are `O1`..`O9` in the brief's order (`:2236`) | `:47, :55, :62, :69, :75, :82, :87, :94, :100` | correct, order preserved |
| FWD-21 TODAY "four stacked bands, 6,548 px of 12-px text" (`:666`) | `:52` (O1), `:175`, `:231` | correct; the measurement behind it is 34,480 of 47,393 chars at 12px (`:192`); the gloss is fair |
| FWD-22 TODAY "14 rows of 161867780096.00003 ABSOLUTE CUR_MKT_CAP" (`:674`) | `:59`, `:199` | correct |
| FWD-23 "48 blockquotes"; zero passages in a native `title=` (`:682-684`) | `:64`, `:169`; the drafting-harness property (`:62-67`) | correct |
| FWD-24 "60-char refusal in ten red chips" (`:693`) | `:73`, `:234` | correct |
| FWD-25 "17 columns, 12 ABSENT in all 18 rows, under a 696-char paragraph" (`:702`) | `:237` | correct |
| FWD-26 `status.warning` icon beside navy text, never amber (`:709`) | `:85`, `:373` | correct |
| FWD-27 `purpleFills` 0 in Universe / 1 in Security; two 10-px caption lines (`:717-721`) | `:445`, `:89-90` | correct |
| FWD-28 four designed states (`:726`) | `:94`, `:218`, Part V page-wide (`:322`) | see F4 |
| FWD-29 the JSON assertions and the PNG read (`:734-740`) | `:443-448` | correct, adopted near-verbatim |
| B.1: the brief's Part VII lists the print action as not captured (`:2222`) | `:413` | correct |
| B.3: Andrew's ~04:5xZ word verbatim, record @`21dd61e392` (`:2251-2257`) | this seat's record `ANDREW_DIRECT_20260924_045xZ_...` | verbatim match; the narrow reading carried as written |
| B.5: "the spec changes how these are shown, never whether" | `:305` (IV.9) | correct |

Nothing the brief says is misquoted, and nothing it does not say is attributed to it. `FWD-30` is Andrew's ~05:0xZ word, not the
brief's, and B.1 says so.

## B.4a (v0.26), spot-checked at the files it cites

| B.4a claim | check | result |
|---|---|---|
| `PrintExportAction.tsx:63` `rounded-lg`, `:75` `shadow-2xl` | `sed -n '63p;75p'` | both present; agrees with this seat's walk (`MEASUREMENTS.json`: 1 shadow, 2 `rounded-lg` in that file) |
| `render_pack.py:26` "STOP -- NOT A BROWSER PRINT, DELIBERATELY" | `sed -n 26p` | verbatim |
| `page_break` "each block starts its own page" at `:205-206` | `def page_break` at `:204`, docstring `:205-206`; called at `:295`, `:306` | resolves |
| `build_pack()` returns `(pdf_path, txt_path)`; 361 lines | `:328`; `wc -l` 361 | correct |

B.4a is the CTO's own measurement and is consistent with the files at HEAD. Its re-cut leaves `FWD-30`'s DONE WHEN unchanged,
which is the right shape: the outcome was stated as properties of the artifact.

## Findings

**F1 -- GROUND FOR REFUSAL, unchanged from v0.25 to v0.26. B.4's four contracts exist ONLY in the brief half.** Measured at
`8da812bf80`: `C-CLAUSE-CITED-REJECTION` at `:738` (ENDPOINT fence, as a SOURCE reference) and `:2267` (B.4 definition);
`C-RENDER-IS-THE-ORACLE` at `:657`, `:738` (fence) and `:2270` (B.4); `C-EXPORT-ADDS-NOTHING` at `:2275` (B.4), `:2298` and
`:2315` (B.4a); `C-PRESENTATION-ONLY` at `:759` (fence), `:2279` (B.4) and `:2333`. **Zero occurrences inside `## CONTRACTS`
(`:770-1140`).** B.6 states *"ADDENDUM B adds ENDPOINT lines and CONTRACTS, so the RATIFIED half re-opens"* -- the ENDPOINT lines
are there; the CONTRACTS are not. `3.0.0_SA_CVO~Z` signed the ratified half at 05:41Z (`f78f875dcc9c`, still current at v0.26)
over bytes that do not contain them. So four names that the ENDPOINT fence cites as acceptance authority, that round 37's orders
will cite by name, and that the CVO will grade against, are carried in the half the CVO does not review. It is the same
one-carrier defect the CTO caught on the FWD definitions (B.2, `:2239-2243`), one section down, and it is the class R-32 names
(the tool's read is the record: `prd_signoff_lib` routes a section to a half by its heading's first word, and `# ADDENDUM B` is
routed brief). A brief-half signature here would be read as ratifying four contracts no CVO reviewed, and the brief-half
reviewer is not the contracts reviewer. **Remedy, one commit:** move the four definitions into `## CONTRACTS` (the PRD's own v0.15
rule, `:328`, "the six format contracts move to CONTRACTS"), leave a one-line pointer in B.4, and let the ratified half re-open to
the CVO. Alternatively, if they are ADDENDUM guidance and not ratified contracts, drop the `C-` prefix and the word "CONTRACTS"
from B.4 and B.6. **The cheapest correct form already exists in the sibling PRD:** `AMGT_CORPUS` ADDENDUM A heads its contract
sections `## CONTRACTS -- A.4 ...` and `## CONTRACTS -- A.5 ...`, and `prd_signoff_lib` routes a section by its heading's first
word, so those sections hash into the RATIFIED half where they sit. Re-heading B.4 to `## CONTRACTS -- B.4 -- NEW CONTRACTS` moves
the four definitions into the CVO's half in place, one line, no text moved.

**F2 -- correction, not a ground on its own.** `C-CLAUSE-CITED-REJECTION` (`:2267`) names the clauses in scope as C1, C3, C5, C6,
C8, C9, C10, C11, C12. **C2 (numerals: tabular, right-aligned, signed) is omitted**, while FWD-22's DONE WHEN requires *"tabular
numerals"* (`:671`) and the brief carries a C2 finding at `:192-196`. A rejection of a tile that prints `161867780096.00003`
left-aligned cites C2 and would today be "not a rejection" by this contract's own list. Add C2.

**F3 -- correction, not a ground on its own.** The preamble note at `:386` sends the reader to `C-VERBATIM-GATE` *"at
`:1107-1114`"*. That was true at `d8d2052388`, where the clause sat at `:1113`; at this pin ADDENDUM B's 111 fence lines and
the header's ten sit above it, and `:1107-1114` lands on `C-DEDUPE-BY-KEY` and the Lusha silver rule. The clause is at `:1234`.
The note is exactly the class CLAUDE.md Rule 27 names ("a citation ages separately from the text it quotes"), and it was written
to cure a stale note. Cite the clause by name, or re-point it at each bump.

**F4 -- note, no correction owed.** FWD-28 requires `PanelNoPermission` captured at least once; the brief's acceptance shape
(`:446-447`) named EMPTY, LOADING and ERROR captured once, while its Part V (`:322`) says every panel renders all four. The
outcome is stricter than the acceptance line and consistent with C12; accepted as the CTO's cut.

**F5 -- note.** The `endpoint_outcomes` header list (`:31-41`) and the ENDPOINT fence agree on ten new ids; the header carries no
definitions, per the one-carrier correction in B.2, and no longer carries a second brief pin (msg 25284). Verified by count.

## Verdict

**REFUSE**, on F1 alone. The brief's content is carried correctly (thirteen checks, all by pinned line, plus four B.4a
spot-checks); the defect is where four contracts live. Under R-10 the signature is not a bar for AMGT, so round 37's issuance is
not held by this refusal; the review stands and the fix is one commit, after which this seat re-reads the moved bytes and
re-stamps the same hour. F2 and F3 ride the same commit.

Reviewed at the bytes of `8da812bf80` (HEAD `dab9d1238f` identical, working tree clean); brief half hash `1abaebccd230ab20...`
as the tool prints it, bound in the stamp with `--expect-half-hash`. No file of the PRD was changed by this review.
