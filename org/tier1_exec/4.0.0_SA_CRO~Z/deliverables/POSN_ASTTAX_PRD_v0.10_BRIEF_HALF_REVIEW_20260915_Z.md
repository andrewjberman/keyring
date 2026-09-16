# L4-R REVIEW -- POSN_ASTTAX PRD v0.10 @59113e257a, BRIEF HALF -- SIGN

**Reviewer:** 4.0.0_SA_CRO~Z (brief half; `TREE_PRD_SIGNOFF`; the SEATED CRO lane for POSN_ASTTAX per `project.json`
`seats.cro`, and per Andrew-direct ~03:5xZ: *"the ~W agents are only working on AMGT_RESAPP ... the ~Z agents work on
POSN_ASTTAX"*, record @9dfee40ce0)
**Delivered by:** `1.0.0_SA_CTO~Z` msg 22993, 2026-09-15T03:55:53Z, withdrawing its 22976-22979 routing of this half to `~W`
**Reviewed:** 2026-09-15 ~04:0xZ (sixteenth review of this PRD by this seat)

## CONTROLS RUN BEFORE THE STAMP

| control | read | result |
|---|---|---|
| last-touch of the PRD == the review pin | `git log -1 -- prd/POSN_ASTTAX_PRD.md` -> `59113e257a` (1.0.0_SA_CTO~Z, 2026-09-14T23:23:29-04:00) | MATCH |
| bump scope measured | `git diff 8eabf98d81 59113e257a -- <prd>` -> +57 / -7: header version; ONE new s.0 ADDENDUM v0.10 block; in ENDPOINT, FWD-6 DONE WHEN rewritten to the presence rule, FWD-7 DONE WHEN / ACCEPT to the per-measure blank rule, the provenance line removed | nothing else moved |
| which half changed | ENDPOINT edits are the CVO's half; the addendum is brief half | both re-open, as delivered |
| **heading denominator vs the brief at the named pin** | `git show 03f1d00ec4:<brief>` -> headings at :5, :22, :29, :39, :47, :55 -- **6 non-title headings** (four `##`, two `###`), titles matching map rows 1-6 word for word; positive control: 3,790 bytes read at the pin | MATCH -- denominator 6, covered 6 |
| cited commits resolve | `git cat-file -t` on d3d2ffc4a5, 3cb95a7074, 365580f244, 27a54b7550, fcb3b55f19 | 5 of 5 -> commit |
| bytes at cited lines (a citation ages separately from the text it quotes) | `etf_positioning_gold.py:731` = `def load_history(...)`; `:855` = `def compute_returns(...)`; `yang-generate-positioning/lambda_function.py:1845-1853` = the `periods` map with `'1Q': latest_date - timedelta(days=90)` | all three MATCH the addendum's claims (loader, rule, 90-day 1Q) |
| gate at review | `prd-signoff.py status` -> ADMITTED on the `~W` stamps (ratified-text 3.0.0_SA_CVO~W, brief 4.0.0_SA_CRO~W), read before this stamp | this stamp lands beside `~W`'s as the SEATED lane's; the CTO's 22993 says the gate rests on the `~Z` signatures once landed |

## CONTENT CHECK -- each brief-half entry, CONTENT not pointer

| entry | carries | verdict |
|---|---|---|
| verbatim | Andrew ~03:0xZ *"vendor change approved go get it"* @365580f244 | pinned; matches relay 22972 held here |
| adoption of the two v0.9 refusals | CVO~W: provenance line out of ENDPOINT, FWD-6 amended to the presence rule (the v0.9 "reads through" gloss superseded), FWD-7 per-measure blank rule; CRO~W: the BRIEF COVERAGE map | both refusals were sound (this seat's own v0.9 review had flagged the ENDPOINT provenance line as note 1); adopted in full, with the review paths and pins |
| C-HOLDING-MEASURES, the GAP sentence superseded | Bloomberg-sourced returns = the estate's own ETF rule (`compute_returns` over `load_history`), history landed under ledger `posn-bbg-gld-vxx-return-history-backfill` (script @3cb95a7074; ledger closed @d3d2ffc4a5: GLD + VXX, PX_LAST + daily total return, 2021-01-04..2026-09-11, NEW keys only); GLD/VXX outside the 172-name ETF universe so no ETFs-mode figure moves; **method difference disclosed** (Yang: strictly after the start day, 1Q = 90; estate rule: start-inclusive, 1Q = 91); one satellite ticker takes the second rule, 23 take Yang's; active/credit NULL for a bbg-sourced ticker; CASH NULL | content present with the split stated; this closes the note this seat left on v0.9 (returns computable from history) |
| B6 guidance | import the two functions from their home, never copy; the package mirrors repo paths as `build_package.py` already does | one rule, one place -- correct |
| BRIEF COVERAGE map | denominator 6, covered 6; rows 1 and 6 marked CONTEXT with reasons; row 3 carries the colour supersession (gold -> yellow token; Structured = pink family) and the ruled sub-assets; row 4 carries the three-surface -> `C-POSITIONING-ONLY` supersession; row 5 resolves both "deliberately not decided" items by ruling (`C-RETAG-SET`) and by measurement (two stores, both written by R1; seeder guarded; `bd-securities` out) | substance and consumer named per row; matches the brief at the pin |

## ONE PROCESS NOTE, NON-BLOCKING, for the L4 owner (not a correction to the bytes)

`prd-signoff.py status` routes an owed half to the FIRST LIVE lane of the base serial (alphabetical, `~W` before `~Z`),
not to the SEATED lane in `project.json` `seats.*`. That is what produced two verdicts on one half at v0.9 and the
withdrawn 22976-22979 routing at v0.10. Andrew has now ruled the fabric split by name; the durable fix is `route_half`
reading the project's seated lane (or the fabric letter) before falling back to alphabetical -- `1.0.0_SA_CTO~W` has
carried that REC to Andrew as an open call, and this seat concurs. Nothing in v0.10's bytes depends on it.

## VERDICT

**SIGN.** Stamp: `python .tools/prd-signoff.py sign POSN_ASTTAX --half brief --review <this file>@<its pin>`.
