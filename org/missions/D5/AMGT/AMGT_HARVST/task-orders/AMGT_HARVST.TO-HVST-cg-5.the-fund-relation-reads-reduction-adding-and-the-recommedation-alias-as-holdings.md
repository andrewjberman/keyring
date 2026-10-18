# AMGT_HARVST task order -- `HVST-cg-5` -- ROUND 92, workstream FUNDREL-CLASSIFY: `fund_relation` READS `reduction` AND `adding` AS HOLDING WORDS AND ACCEPTS THE ONE ALIAS `RECOMMEDATION` (CTO msg 7782; rows D1-S46, D1-W161-S2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cg-5.the-fund-relation-reads-reduction-adding-and-the-recommedation-alias-as-holdings</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cg-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~163</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and offline tests, plus READ-ONLY S3 reads of the bucket `opal-data-harvest` under the prefix `amgt/harvest/silver/research-report/` ONLY, in the census step (list and get of the parquet parts, through `lib.research.harvest.store._default_client()`; never `put`, `delete`, `copy`, `sync` or a bare `aws` call). Budget: at most 40 requests and 50 MiB in all, counted in the census's last line. NO silver or gold writer is RUN, NO deploy, NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is a fuzzy header match (a second misspelling guessed into a header: it must surface as `none`), an alias that matches AFTER the fund token, a holding word that matches inside a longer word (`reductions`, `additional`), a change that moves any of the 117 rows already read `holding` or the 14 `candidate`, and a census that is not re-run after the change.
</preflight>

## 0. THE CELL

`HVST-cg-1` (merged `ad116e0037`) added `lib/research/corpus/fund_relation.py`: `classify(fund, fund_evidence)` returns one of seven relations for a silver `research-report` row. Its census over the 353 stored reports (`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~161/cg1_census.out`, read it) shows two holdings read wrong, and the CTO ruled (msg 7782):
- **(a)** `ORA_FP_Equity`, 2 rows: `RECOMMENDATION: Consider size reduction in IDVZ` reads `unclassified`. The line means the fund holds the name now, so it is a `holding`: **add the whole word `reduction` to the holding words.**
- **(b)** `CPA_US_Equity`, 2 rows: the header is misspelled `RECOMMEDATION`, so the row's `fund_evidence` is the bare-token fallback window (it may begin with a stray character: `1 RECOMMEDATION: Consider adding 50-100bps in IDVZ taking it to 150-2...`) and the row reads `none`. **Accept that ONE token as a closed-list alias.** No fuzzy matching: any other misspelling must keep reading `none`, never be guessed.
- **(c) The issuer adds `adding` to the holding words:** the CPA line says `Consider adding ... in IDVZ taking it to 150-200bps` (a position the fund already holds), and `add` matches only the whole word, so after (b) the row would read `unclassified`. The CTO's expected result needs it: **`holding=121 unclassified=0 none=213`** (117 + the 2 ORA + the 2 CPA = 121; 2 unclassified become holding; 215 minus the 2 CPA = 213).
This cell changes `fund_relation.py` and its tests only, re-runs the census, and touches no other source file.

## 1. THE BUILD (LOCAL, about 25 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. In `lib/research/corpus/fund_relation.py`:
   - `_HOLDING_WORD_RE` gains the whole words `reduction` and `adding`: `\b(?:maintain|mainain|maitain|retain|increase|add|adding|reduction)\b|\bno change\b`. Update the module docstring: the word patterns are "copied from `continuation.py` lines 443-445 PLUS `adding` and `reduction` (CTO msg 7782; `continuation._line_stance` is not changed)"; the drift test (arm 4 of `tests/test_fund_relation.py`) is unchanged and must still pass because none of the 21 census phrases contains either word;
   - a closed alias constant `_HEADER_ALIASES = ("RECOMMEDATION",)`. The generic header (anchored at the start of `fund_evidence`) is tried first, as today. If it does not match, look for an alias as a whole word, case-insensitive, followed by `\s*:?\s*`, ANYWHERE in `fund_evidence` but only BEFORE the first fund token; when found, the text after the alias up to the fund token is the body, classified exactly as before. An alias after the fund token, or no alias, returns `none` as today. No other change to `classify`.
b. In `lib/research/corpus/tests/test_fund_relation.py` (the file exists: add arms at its end, change no existing arm) add:
   - (18) `classify("IDVZ", "RECOMMENDATION: Consider size reduction in IDVZ")` returns `holding`; `reductions` and `additional` do NOT make a holding (`RECOMMENDATION: reductions in IDVZ` and `RECOMMENDATION: additional work on IDVZ` return `unclassified`);
   - (19) the two CPA evidences, verbatim `1 RECOMMEDATION: Consider adding 50-100bps in IDVZ taking it to 150-200b` and `RECOMMEDATION: Consider adding 50-100bps in IDVZ taking it to 150-200b`, with fund `IDVZ`, return `holding`; `RECOMMENDATION: Consider adding 50-100bps in IDVZ` returns `holding`;
   - (20) no guessing: `1 RECOMENDATION: Maintain position in PFOE` (a different misspelling, fallback window) returns `none`; `Maintain position in PFOE then RECOMMEDATION: x` (the alias AFTER the token position... build it so the alias sits after the fund token) returns `none`;
   - (21) the 22-phrase table of arm 1 is unchanged and still passes;
   - (22) **A MUTANT:** with `fund_relation._HEADER_ALIASES` monkeypatched to `()`, arm (19) FAILS (assert that it does).
c. **The census, re-run.** Copy `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~161/cg1_census.py` UNCHANGED to your deliverables folder as `cg5_census.py` (read it; if it names its own output path or folder, change only that), and run it once in the FOREGROUND with `python -u`, stdout to `cg5_census.out`. Its output format is that of `cg1_census.out`. The expected last-but-one line is `CENSUS-FUND-RELATION rows=355 reports=353 securities=94 holding=121 candidate=14 initiate=2 interest=2 template=1 unclassified=0 none=213 gets=<n> bytes=<n>` and the last line is the six-name `PROOF-NAMES` line of `cg1_census.out`, unchanged. **If a count differs, DO NOT edit the expectation or the code to match: print the actual lines, add a row, and report.** Then write `cg5_moved.out` with `diff` of the `RELATION` lines of `cg1_census.out` against `cg5_census.out` (it must show exactly the four rows: the 2 ORA rows `unclassified` to `holding` and the 2 CPA rows `none` to `holding`) and its last line exactly `MOVED_ROWS=<n>`.
d. Do not touch any other file; do not run any silver or gold writer. A surprise is a row; keep working.

<paths>
lib/research/corpus/fund_relation.py
lib/research/corpus/tests/test_fund_relation.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~163/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cg-5"><invocation>python -m pytest lib/research/corpus/tests/test_fund_relation.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^2[2-9] passed in|^[3-9]\d passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cg-5"><invocation>python -m pytest lib/research/corpus/tests/test_typed.py lib/research/corpus/tests/test_typed_misfiled_reports.py lib/research/corpus/tests/test_fund_form.py lib/research/corpus/tests/test_substrate.py lib/research/corpus/tests/test_continuation_holding_stance.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^58 passed in</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cg-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~163/cg5_census.out</invocation><expect>(?m)^CENSUS-FUND-RELATION rows=355 reports=353 securities=94 holding=121 candidate=14 initiate=2 interest=2 template=1 unclassified=0 none=213 gets=\d+ bytes=\d+$</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-cg-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~163/cg5_moved.out</invocation><expect>(?m)^MOVED_ROWS=4$</expect></criterion>
</proof_of_spec>

- A fourth criterion, with its reason: AC4 is the control that nothing but the four named rows moved (a holding word that matched too widely would move more); AC3 is the CTO's expected count.
- AC1's pattern: the file held 17 tests at `ad116e0037` and gains at least five arms, so it reads 22 or more passed.
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-18 ~00:0xZ):** AC1 base: reads `17 passed` and the pattern does not match, FAIL as expected; AC2 PASS as expected (`58 passed`); AC3 and AC4 FAIL as expected (`cat` of a file that does not exist). If your base count differs, say so with both counts and do not weaken the pattern.
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W163-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~163/AMGT_HARVST.TO-HVST-cg-5.the-fund-relation-reads-reduction-adding-and-the-recommedation-alias-as-holdings.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cg-5.the-fund-relation-reads-reduction-adding-and-the-recommedation-alias-as-holdings` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cg-5.the-fund-relation-reads-reduction-adding-and-the-recommedation-alias-as-holdings.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO msg 7782 ("YES to both": `reduction` is a holding verb; `RECOMMEDATION` as a single closed-list alias; "re-run the census after both changes, before the rewrite"; expected holding 121, unclassified 0, none 213). Decomposition section 122c.
- **The issuer's addition `adding`** is named to the CTO in the close message: without it the two CPA rows read `unclassified`, not `holding`, and the CTO's expected counts do not hold. `continuation._line_stance` is not changed, so gold and silver differ on these three words for a phrase gold never reads as a candidate (ORA and CPA have a holding report in gold already).
- **Sequencing:** `HVST-cg-2` (the silver rewrite) waits on this cell: the rewrite fixes the classifier into every row.
- Slot ~163, worktree `C:/dev/wk-harvst-163`, branch `wk-AMGT_HARVST-163`. Widen the sparse set at provision with `lib/research`, `.claude/agents`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922`, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~159` and `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~161`.
- **SENT:** with the round-92 recut.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>92</round>
<workstream>FUNDREL-CLASSIFY</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
