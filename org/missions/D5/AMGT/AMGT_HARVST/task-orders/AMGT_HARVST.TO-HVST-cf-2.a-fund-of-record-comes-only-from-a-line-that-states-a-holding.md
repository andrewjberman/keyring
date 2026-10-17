# AMGT_HARVST task order -- `HVST-cf-2` -- ROUND 91, workstream CS61-FIX: `fund_of_record` COMES ONLY FROM A LINE THAT STATES A HOLDING; A CANDIDATE, AN INITIATION, AN INTEREST OR A TEMPLATE PLACEHOLDER IS SERVED AS SUCH, NEVER AS THE FUND OF RECORD (row C-S61; CTO round-90 analysis item 2; measured by HVST-cf-1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cf-2.a-fund-of-record-comes-only-from-a-line-that-states-a-holding</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cf-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~160</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and offline tests, plus READ-ONLY S3 reads of the bucket `opal-data-harvest` in step 2 ONLY (the census), through the repo shim `.tools/aws` (`s3api list-objects-v2` and `get-object` on named keys or prefixes; never `put`, `delete`, `copy`, `sync`, a recursive `cp` or a bare `aws` call). Budget: at most 800 requests and 500 MiB in all, counted in `cf2_census.out`. NO gold writer is RUN (`write_one`, `--write`, `production_sequence` are NEVER run), NO deploy, NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is a classifier that is right on the census phrases and wrong on the next one (so the default for an unclassified phrase is NOT a holding), a fix that changes a holding line's value (every holding value must stay byte-identical, with no new key), a fix that drops `last_stated_position` for a candidate (it is served, with its stance), a method-version bump that is forgotten (the gold writer never overwrites: the same object name with other bytes raises `GoldImmutableError`), and a test that passes whatever the code does.
</preflight>

## 0. THE CELL

Round 90's `HVST-ce-2` made a pdf `Recommendation:` line a fallback; its census and the CTO's graduated row `C-S61` show that `fund_of_record` takes the first fund token of a line WHATEVER ITS VERB, so `RECOMMENDATION: CANDIDATE FOR PFOE` (MNST) is served as fund of record `PFOE`: a candidate reads as a holding. `HVST-cf-1` (read it: `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~159/cf1_census.out`, 94 of 94 securities, 22 distinct phrases) prints every phrase before the fund token. The CTO ruled: **fund_of_record and last_stated_position take a fund only from a holding verb (maintain, hold, add, and so on, as the census names them); a candidate or watch line is served as such, in its own field or with an absent reason, never as the fund of record.** The issuer's classification of the 22 census phrases (the CTO ratifies it in the never-widen pair of the rebuild; the code and its tests are LOCAL):
- **HOLDING (17 phrases):** `maintain <N>.<N>% position in`, `maintain <N>% position in`, `maintain position in`, `maintain positions in`, `maintain in`, `maintain or consider increasing position in`, `mainain <N>.<N>% position in`, `maitain <N>% position in`, `maitain <N>.<N>% position in`, `maitain a position in`, `maintain <N>% positive in`, `retain <N>% position in`, `no change remain at <N>.<N>% in`, `increase position in`, `potential add in`, `<N>-<N>% position in`, `~<N>% position in`.
- **NOT A HOLDING (4 phrases):** `candidate for` (stance `candidate`: CLX, and 9 names served since round 90), `initiate ~<N>% position in` (stance `candidate`: CNR, a position not yet held), `interesting exposure for` (stance `candidate`: ST_SP), `[buy in` (stance `template`: ML_FP, the bracketed placeholder `[BUY IN IDVZ TO X%]`).
- **NO FUND TOKEN (1 phrase, 7 names; 4 are a COMPANY DESCRIPTION paragraph):** `[no fund token]`: unchanged by this cell (no fund is served from it; a separate defect, see the issuer note).

## 1. THE BUILD (LOCAL, about 80 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. In `lib/research/corpus/continuation.py`:
   - add a small pure classifier `_line_stance(content)` returning `"holding"`, `"candidate"`, `"template"` or `"unclassified"` from the text BEFORE the first fund token (lowercased, whitespace collapsed; if the content has no fund token, the whole content). Order of tests: (1) the phrase starts with `[` -> `template`; (2) it contains a whole word `candidate`, `initiate` or `interesting` -> `candidate`; (3) it contains a whole word `maintain`, `mainain`, `maitain`, `retain`, `increase`, `add`, or the words `no change`, or it matches a size statement `^~?\d+(\.\d+)?(-\d+(\.\d+)?)?%` -> `holding`; (4) otherwise `unclassified`. Only `holding` counts as a holding; `unclassified` is NOT a holding (the default never claims a holding without evidence). Tests (1) and (2) run BEFORE (3): `initiate ~2% position in` carries a size and is not a holding;
   - `fund_of_record`: take the fund token from the first candidate (recency order) whose stance is `holding` and whose content names a fund token. If none: the field is absent with the reason `no stated holding line: the lines found are candidate, template or unclassified (see last_stated_position)` when there are candidates, and the reason of today when there are none;
   - `last_stated_position`: stays the FIRST candidate's text exactly as stated. For a `holding` stance the value is byte-identical to today (no new key). For a non-holding stance the value dict gains ONE key `"stance"` (`candidate`, `template` or `unclassified`) and its `"fund"` key is None; the fund token found in such a line goes in a second new key `"candidate_fund"`. The `line_only` key rule stays as it is;
   - bump `METHOD_VERSION` from `"amgt-corpus-continuation/4"` to `"amgt-corpus-continuation/5"` (the object name is a hash over the method version and the inputs; the gold writer never overwrites); update ONLY the two assertions that name `/4` (`tests/test_continuation_pdf_recommendation_line.py` line 258 and `tests/test_continuation_terms.py` line 149);
   - amend the module docstring section "RULED -- RECOMMENDATION-LINE RESOLUTION" with a short ASCII paragraph: `AMENDED round 91 (CTO round-90 analysis item 2, row C-S61; measured by HVST-cf-1): fund_of_record is taken only from a line whose verb states a holding; a candidate, initiation, interest or bracketed template line is served in last_stated_position with a stance and is never the fund of record.`
b. New test `lib/research/corpus/tests/test_continuation_holding_stance.py`, offline, following `tests/test_continuation_pdf_recommendation_line.py` (read it first; copy the helpers you need, edit nothing else in it except the one assertion). Arms:
   - (1) a table test over ALL 22 census phrases, each with its raw example from `cf1_census.out` (the `raw=` text, a fund token appended where the raw text carries it): the 17 holding phrases classify `holding`, `candidate for` / `initiate ~<N>% position in` / `interesting exposure for` classify `candidate`, `[buy in` classifies `template`; the `[no fund token]` examples have no fund token and no `fund_of_record`;
   - (2) MNST: a pdf page whose line is `Recommendation: CANDIDATE FOR PFOE` and no other candidate: `fund_of_record` absent with the reason above; `last_stated_position` text `CANDIDATE FOR PFOE`, `fund` None, `stance` `candidate`, `candidate_fund` `PFOE`, `line_only` True;
   - (3) UNH: `Recommendation: Maintain positions in PFOE and DIVZ`: `fund_of_record` `PFOE` and the position value EQUAL to the round-90 value (no `stance`, no `candidate_fund`, `line_only` True);
   - (4) a security with TWO reports, the newer a candidate line and the older a holding line: `fund_of_record` is the older report's fund, `last_stated_position` is the newer report's text with its stance;
   - (5) the old-rule docx path: `RECOMMENDATION: MAINTAIN 2.25% POSITION IN IDVZ` is byte-identical to today (no new key); a docx `Candidate for DIVZ` (CLX) gets stance `candidate` and no `fund_of_record`;
   - (6) a phrase the classifier has never seen (`watch list name for PFOE`) is `unclassified` and is not a holding;
   - (7) `METHOD_VERSION == "amgt-corpus-continuation/5"`, and the object name for one fixed input set differs from the one under `/4`;
   - (8) **A MUTANT:** with `continuation._line_stance` monkeypatched to return `"holding"` always, arm (2) FAILS (assert that it does).
c. Do not run any gold writer; do not edit any other file. A surprise is a row; keep working.

## 2. THE CENSUS (read-only; the effect of the rule on the whole population)

Write `cf2_census.py` in your deliverables folder (start from `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~159/cf1_census.py`, which applies the misfiled-reports exclusion; read it) and run it once, in the FOREGROUND with `python -u` writing its stdout to `cf2_census.out`: for EVERY security of the silver table (94), run `_resolve_fund_and_position` with the code as it was before your change (`git show HEAD:lib/research/corpus/continuation.py` loaded as a second module) and with your changed code on the same fetched inputs. Per security whose `fund_of_record` or `last_stated_position` DIFFERS (value, key set or absent), one line `CHANGED <security_key> fund_before=<value or absent> fund_after=<value or absent> position_before=<first 60 characters or absent> position_after=<first 60 characters or absent> stance_after=<holding|candidate|template|unclassified|none>`. Then lines `ALLOWED_CLASS candidate=<n> template=<n> unclassified=<n>` (the number of CHANGED lines by stance_after) and `HOLDING_CHANGED=<n>` (names whose before-value was a holding line and whose value changed: expected 0), and last exactly `CENSUS-CS61-FIX securities=<n> changed_fund=<n> changed_position=<n> gets=<n> bytes=<n>`. The expected set: CHANGED names are the ones whose served `fund_of_record` came from a non-holding line (`8035_JP`, `ADBE`, `BZLFY`, `CDNS`, `CELH`, `HEI`, `MNST`, `MSCI`, `SNPS`, `CLX`, `CNR`, `ST_SP`, `ML_FP`); any other name that changes is printed and explained.

<paths>
lib/research/corpus/continuation.py
lib/research/corpus/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~160/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cf-2"><invocation>python -m pytest lib/research/corpus/tests/test_continuation_holding_stance.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cf-2"><invocation>python -m pytest lib/research/corpus/tests/test_continuation.py lib/research/corpus/tests/test_continuation_pillar_body.py lib/research/corpus/tests/test_continuation_reader_method.py lib/research/corpus/tests/test_continuation_terms.py lib/research/corpus/tests/test_dossier_method_bump.py lib/research/corpus/tests/test_substrate.py lib/research/corpus/tests/test_continuation_pdf_recommendation_line.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^66 passed in</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cf-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~160/cf2_census.out</invocation><expect>(?m)^CENSUS-CS61-FIX securities=94 changed_fund=\d+ changed_position=\d+ gets=\d+ bytes=\d+$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-17 ~20:4xZ):** AC1 FAIL as expected (the new test file does not exist); AC2 PASS as expected (`53 passed` over the six files plus `13 passed` for the pdf-line test = `66 passed` in one run; the two ran separately here as 53 and 13); AC3 FAIL as expected (`cat` of a file that does not exist). If your base count differs, say so with both counts and do not weaken the pattern.
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W160-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~160/AMGT_HARVST.TO-HVST-cf-2.a-fund-of-record-comes-only-from-a-line-that-states-a-holding.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cf-2.a-fund-of-record-comes-only-from-a-line-that-states-a-holding` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cf-2.a-fund-of-record-comes-only-from-a-line-that-states-a-holding.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO round-90 analysis (`ledger/ROUND_ANALYSIS.round90.md` @307764abfe, msg 7721) item 2; graduated row `C-S61`; `HVST-cf-1` (merged `934ecb88c5`, 22 phrases over 94 names). The CTO ratifies the classification in the rebuild's pair (`HVST-cf-4`); this cell is the code and its tests (LOCAL).
- **The issuer's classification choices, named so the CTO can reverse them:** `potential add in` (IMB: "currently ~2.5%") is a HOLDING (an action on a held position); `maintain or consider increasing position in` (RMS) is a HOLDING; `increase position in` (NOW, ZTS) is a HOLDING; `initiate ~2% position in` (CNR) is NOT (a position not yet held); `interesting exposure for` (ST_SP) is NOT; `NKE`'s `MAINTAIN IN PFOE, CANDIDATE FOR DIVZ` is a HOLDING by its first verb (fund_of_record `PFOE`; the second clause stays in the position text). The default for a phrase the classifier does not know is NOT a holding.
- **A second served defect the census showed, NOT in this cell:** 4 names (`8306_JP`, `8316_JP`, `8766_JP`, `9433_JP`) serve `last_stated_position` = a `COMPANY DESCRIPTION: ...` paragraph (the other 3 of the 7 no-fund-token names, `BABA` `SELL`, `SHOP_CN` `PASS`, `WALMEX*` `CANDIDATE TO TRIM`, are genuine position statements without a fund token), because the old rule reads the next non-blank locator when the label stands alone, and that locator is a section. It predates round 90. Row filed by the issuer; the CTO is asked whether it joins this fix or a later one.
- **Sequencing (decomposition 121):** the rebuild `HVST-cf-4` runs from a worktree pinned AFTER this cell's merge and BEFORE any `fund_form` code change; this cell does not touch `fund_form`.
- **Class:** the gate decides; the first commit attempt declares LOCAL.
- Slot ~160, worktree `C:/dev/wk-harvst-160`, branch `wk-AMGT_HARVST-160`. Widen the sparse set at provision with `lib/research`, `.claude/agents`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922` and `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~159`.
- **SENT:** with the round-91 recut.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>91</round>
<workstream>CS61-FIX</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
