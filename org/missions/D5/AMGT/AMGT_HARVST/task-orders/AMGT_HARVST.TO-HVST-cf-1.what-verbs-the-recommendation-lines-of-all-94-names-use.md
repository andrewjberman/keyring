# AMGT_HARVST task order -- `HVST-cf-1` -- ROUND 91, workstream CS61-MEASURE: WHAT VERB EACH OF THE 94 NAMES' RECOMMENDATION LINE USES BEFORE ITS FUND TOKEN, AND WHICH SERVED `fund_of_record` CAME FROM A LINE THAT IS NOT A HOLDING (CTO round-90 analysis item 1; graduated row C-S61)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cf-1.what-verbs-the-recommendation-lines-of-all-94-names-use</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cf-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~159</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- READ-ONLY S3 reads of the bucket `opal-data-harvest` through the repo shim `.tools/aws` (`s3api list-objects-v2` and `get-object` on named keys or prefixes; never `put`, `delete`, `copy`, `sync`, a recursive `cp` or a bare `aws` call). Budget: at most 800 requests and 500 MiB in all, counted in `cf1_census.out`. NO gold writer is RUN (`write_one`, `--write`, `production_sequence` are NEVER run), NO deploy, NO Secrets Manager, NO browser, NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is a verb table built from a sample (the census is ALL 94 securities), a normalisation that merges phrases the CTO needs to tell apart (so keep the raw first 120 characters of every line beside the normalised phrase), a count that mixes the rule's two paths without saying which supplied each line, and a list of "affected names" taken from the code's prediction instead of from what is SERVED (read the served objects for the 31 rebuilt names).
</preflight>

## 0. THE CELL

Round 90 made `lib/research/corpus/continuation.py` read a pdf `Recommendation: <content>` line as a fallback (`HVST-ce-2`), and rebuilt 31 securities' gold continuation and dossier objects (`HVST-ce-4`). The CTO's analysis (`ledger/ROUND_ANALYSIS.round90.md` @307764abfe) graduated a served correctness defect, row `C-S61`: `MNST_US_Equity`'s pack line `RECOMMENDATION: CANDIDATE FOR PFOE` is served as `fund_of_record` `PFOE`, so a candidate reads as a holding. The derivation takes the first fund token of the line whatever the verb (`continuation.py::_resolve_fund_and_position`: `fund_of_record` is the first `IDVZ|PFOE|DIVZ` in the first candidate that names one; `last_stated_position` is the first candidate's text). How many names carry the same class is NOT counted. This cell counts: a read-only census over ALL 94 securities of the verb phrase before the fund token, and the list of every name whose `fund_of_record` is served from a line that is not a holding. It decides nothing about which verbs are holdings: it prints what the lines say and the CTO and the issuer classify.

## 1. THE WORK (read-only; the output is `cf1_census.out`)

Work in your worktree. Write only the files named in `<paths>`. Start from `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~156/ce2_census.py` (it fetches every silver row's extraction through the repo shim, builds `items` as `continuation.py` builds them and runs `_resolve_fund_and_position`; read it and `ce1_repro.py` beside `ce1_measure.out` in `deliverables/0.9.0_WK_AMGT_HARVST~155/`). Write `cf1_census.py` in your deliverables folder and run it once.
a. **The population:** every security of the silver research-report table (`amgt/harvest/silver/research-report/`, about 355 rows, 94 securities). For each security compute, with the code of the merged tree you are on (HEAD, which holds `HVST-ce-2` and `HVST-ce-6`): the candidate list (`continuation._recommendation_candidates_ex(items)` returns `(candidates, line_only)`), the candidate that supplies `fund_of_record` (the first candidate whose content names a fund token) and the candidate that supplies `last_stated_position` (the first candidate), with each candidate's `report_id`, `report_class`, `period` and file type.
b. **The verb phrase:** for each supplying candidate, the content up to (not including) the first fund token, lowercased, every digit run replaced by `<N>`, whitespace collapsed, trimmed (a content with no fund token has the phrase `[no fund token]`); ALSO keep the raw first 120 characters of the content. Print one line per distinct phrase, sorted by count then phrase: `PHRASE n=<count> | <phrase> | via=<old|line|both> | e.g. <up to three security keys> | raw=<first 120 characters of one example>`; `via` says which path supplied the lines of that phrase (`old` the label-start rule, `line` the pdf-line fallback; `both` if mixed).
c. **The names:** a section `NAMES` with one line per security that has a `fund_of_record`: `NAME <security_key> | phrase=<phrase> | fund=<token> | via=<old|line> | rebuilt_in_ce4=<yes|no> | report_id=<id> | served_matches_code=<yes|no|n/a>`. `rebuilt_in_ce4` is read from `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round90/ce4_securities.txt`. For the 31 names in that file also read what the gateway SERVES now from the stored gold objects (`amgt/harvest/gold/research-continuation/security_key=<KEY>/` newest by LastModified; read the object's `fund_of_record` and `last_stated_position` entries) and set `served_matches_code` to `yes` when the served fund token equals the one the code computes, `no` when it differs, `n/a` for names outside the 31.
d. **Position lines with no fund token:** a section `NOFUND` listing every security whose first candidate has no fund token, with its phrase and raw 120 characters (their `last_stated_position` is served with `fund` null).
e. End `cf1_census.out` with exactly two lines: `PHRASES distinct=<n>` (the number of distinct phrases of section b) and `CENSUS-C-S61 securities=<n> with_fund=<n> with_position=<n> rebuilt_in_ce4=<n> gets=<n> bytes=<n>` (`securities` is the number you ran, against 94; `rebuilt_in_ce4` counts names in the file that you found with a fund). A security whose extraction cannot be read is a line `UNREADABLE <security_key> <reason>`.
f. Anything odd: one row, then keep working. Do not summarise or classify: print.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~159/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cf-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~159/cf1_census.out</invocation><expect>(?m)^PHRASES distinct=\d+$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cf-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~159/cf1_census.out</invocation><expect>(?m)^CENSUS-C-S61 securities=94 with_fund=\d+ with_position=\d+ rebuilt_in_ce4=\d+ gets=\d+ bytes=\d+$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-17 ~20:0xZ):** AC1 and AC2 FAIL as expected (`cat` of a file that does not exist). The issuer reads the content, not only the two lines.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W159-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~159/AMGT_HARVST.TO-HVST-cf-1.what-verbs-the-recommendation-lines-of-all-94-names-use.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cf-1.what-verbs-the-recommendation-lines-of-all-94-names-use` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cf-1.what-verbs-the-recommendation-lines-of-all-94-names-use.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO round-90 analysis (`ledger/ROUND_ANALYSIS.round90.md` @307764abfe, msg 7721) item 1 ("measure first: a no-write census over all 94 names of the recommendation line's verb and fund token. It prints each distinct verb phrase with its count, and lists every name whose served fund_of_record came from a non-holding verb"); graduated row `C-S61` (the CVO's, `ADJUDICATION_v84.md`).
- **My error that this census repairs:** when I read the round-90 census I took lines such as `CANDIDATE FOR PFOE` for genuine stated positions and did not separate a candidate from a holding; the served `fund_of_record` of those names says PFOE where the report says only that PFOE is a candidate. The 30 absent-to-value names were meant to carry a stated holding; the census (`ce2_census.out`) printed `CANDIDATE FOR ...` for at least `8035_JP`, `ADBE`, `BZLFY`, `CDNS`, `CELH`, `HEI`, `MNST`, `MSCI`, `SNPS`.
- **Order of work (CTO):** this census, then the fix (`HVST-cf-2`, defined, not cut: the issuer and the CTO classify the phrases into holding and not-holding, and the cell is cut from that), then a forward rebuild of the affected names (`HVST-cf-4`) under its own pair. Gold writes never overwrite and nothing is deleted: the fix writes NEWER objects.
- **Class:** `<paths>` names deliverables and the channel file only (LOCAL); the cell is a direct act (`<direct_act>true</direct_act>`); the S3 reads are READ-ONLY and bounded in the preflight.
- Slot ~159, worktree `C:/dev/wk-harvst-159`, branch `wk-AMGT_HARVST-159`. Widen the sparse set at provision with `lib/research`, `.claude/agents`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922` and `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~155`, `~156` and `2.0.0_SA_COO_W1/round90`.
- **SENT:** with the round-91 issuance.

**COMPLETE 2026-10-17T20:4xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** worker `0.9.0_WK_AMGT_HARVST~159` (worker, haiku, high), commits `6a2e2a49cd` (first run, superseded), `b5238574f8` (the counted run), `f17ac0edfe`, `37cb805f43` (rows), `c01d052258` (proof), merged `934ecb88c5` (safe-merge fast lane, index check 0 of 4; the first merge attempt was REFUSED because another seat's changes were staged in the shared index, and was retried after it cleared). Read by this seat: the 22 `PHRASE` lines, the 69 `NAME` lines for the names behind the non-holding and borderline phrases, the `NOFUND` section, and the two result lines; proof instance VALID rc 0 (re-run here).
- **AC1 PASS:** `PHRASES distinct=22`. **AC2 PASS:** `CENSUS-C-S61 securities=94 with_fund=69 with_position=76 rebuilt_in_ce4=30 gets=389 bytes=100842396`. The census's RECON check reproduces the code's fund and position on all 94 names (0 mismatches); served against code: 30 of 30 rebuilt names with a code fund match; `KMB_US_Equity` has no fund in code and none served.
- **What it shows:** the three most frequent phrases are `maintain <N>.<N>% position in` (18), `maintain position in` (14) and `candidate for` (10). `candidate for` is the C-S61 class: 9 of the 10 names are the round-90 rebuilds (`8035_JP`, `ADBE`, `BZLFY`, `CDNS`, `CELH`, `HEI`, `MNST`, `MSCI`, `SNPS`); the tenth, `CLX_US_Equity` (a docx, the old rule), was served that way BEFORE round 90. Three more non-holding phrases: `initiate ~<N>% position in` (`CNR`), `interesting exposure for` (`ST_SP`), and the bracketed template `[BUY IN IDVZ TO X%]` (`ML_FP`, also pre-round-90). Seven names have no fund token; 4 of them (`8306_JP`, `8316_JP`, `8766_JP`, `9433_JP`) serve a `COMPANY DESCRIPTION:` paragraph as `last_stated_position`, a defect that predates round 90.
- **Rows** `D1-W159-S1` (ARMED, disarm owner this seat: the `ML_FP` template is taken as fund `IDVZ`; `ML_FP` is not among the 31), `-S2` (INERT: the first census run inherited a `ce2_census.py` that dropped the misfiled-reports filter and showed a false KMB mismatch; corrected in `b5238574f8`), `-S3` (INERT: the two runs total 844 requests against the 800 cap; the counted run reads 421). `-S1` stays open until `HVST-cf-2` and the rebuild.
- **Mistake of mine, named:** I chained the worktree teardown after the merge in one command; the merge was refused, the teardown ran anyway (the branch survived, the commits were safe) and the merge was retried.

<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker</worker_class>
<status>complete</status>
<round>91</round>
<workstream>CS61-MEASURE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
