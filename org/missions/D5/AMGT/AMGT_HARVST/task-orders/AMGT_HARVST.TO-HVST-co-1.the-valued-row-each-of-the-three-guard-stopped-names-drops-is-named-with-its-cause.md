# AMGT_HARVST task order -- `HVST-co-1` -- ROUND 100, workstream GUARD-STOPS: A READ-ONLY CELL NAMES THE VALUED ROW EACH OF THE THREE GUARD-STOPPED NAMES (`BZLFY_US_Equity`, `PBR_US_Equity`, `TSM_US_Equity`) DROPS ON TODAY'S FIRE, WITH ITS CAUSE (CTO round-99 analysis item 1; row `AMGT_HARVST-D1-S68`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-co-1.the-valued-row-each-of-the-three-guard-stopped-names-drops-is-named-with-its-cause</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-co-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~185</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- READ-ONLY S3 reads of the bucket `opal-data-harvest` ONLY: list and get under `amgt/harvest/gold/research_dossier/`, `derived/model_block/`, the bronze objects the model block derives from and the objects `dossier.build` reads for the named names, through `lib.research.harvest.store._default_client()`; never `put`, `delete`, `copy`, `sync` or a bare `aws` call. Budget: at most 4500 requests and 700 MiB in all, counted in the last line. NO gold or silver writer is RUN (`dossier.write_one` and every `--write` are NEVER run; only `dossier.build` in memory). NO Bloomberg, NO model call, NO network beyond the S3 client. NO edit of any source file, NO edit outside `<paths>`; you DO NOT call the live gateway.
comp-adversary: RUN at L5 -- the adversary is a comparator that reports a dropped row only because of key order or whitespace (compare parsed values), a "dropped" row that is merely the same row under a different label, a cause assigned from the mnemonic's NAME instead of from the two model blocks the dossiers cite (read both blocks), a stored value read from a different dossier than the one the gateway serves (use the gateway's `_pick_dossier` rule), a build that tries a network call (STOP and report), a finder that cannot see a missing row (it has a negative control), a name whose guard stop is assumed to be the same cause as PBR's, and a census whose expectation is edited to match.
</preflight>

## 0. THE CELL

The first scheduled dossier refresh (ECS task `bc80a834255049eb89c1731792eef625`, 2026-10-20 14:00Z) wrote 92 names and the model-block guard stopped three: `BZLFY_US_Equity` (valued rows built 55, stored 56), `PBR_US_Equity` (55 against 56) and `TSM_US_Equity` (53 against 54). A stopped name keeps its previous dossier. For PBR an earlier cell (`HVST-cn-2`, `deliverables/0.9.0_WK_AMGT_HARVST~180/cn2_pbr.out`) named the row `typecast|BEST_DPS|FY1` and the cause `field_absent_in_new_block` (the stored 2026-10-17 model block carried a FY1 dividend figure 9.546; the 2026-10-18 block listed it unresolved with the reason `HELD_OFF: SA fallback held off by --no-sa-fallback`). **The CTO wants the same finding for BZLFY and TSM, and PBR re-measured on today's fire.** Whatever the cause, each is a row. This cell writes nothing and changes no source file.

## 1. THE BUILD (a read-only script; no product code)

Work in your worktree. Change only the files named in `<paths>`.
a. Read first: `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~180/cn2_pbr.py` and `cn2_pbr.out` (START FROM THE SCRIPT: its served pick, build, finder, cause decision and controls are the method to reuse unchanged), and `lib/research/corpus/dossier.py` (how a `model_rows` row is built and counted for the guard).
b. **Write `co1_names.py`** in your deliverables folder (copy the method of `cn2_pbr.py`, loop it over the three names in sorted order: `BZLFY_US_Equity`, `PBR_US_Equity`, `TSM_US_Equity`) and run it once in the FOREGROUND with `python -u`, stdout to `co1_names.out` (open it with `newline="\n"`). For EACH name print: `NAME <key> served=<object name> built_as_of=<date> stored_block=<stamp> built_block=<stamp>`; then `ROWMISS <identity> stored_value=<first 60 characters> built=<the built row's value or its absent reason, first 80 characters>` for every row with a value in the stored dossier and none in the build, and `ROWNEW <identity> ...` for the reverse; then for each ROWMISS `CAUSE <identity> <field_absent_in_new_block | value_null_in_new_block | row_moved_to_other_fiscal_year | build_rule_dropped_it | other>` with its evidence from the TWO BLOCKS (the block key and the field in each, or the line of `dossier.py` whose rule dropped it; never from the mnemonic's name); then the name's line, exactly: `DROPPED-ROW <key> rows_stored=<n> rows_built=<n> rows_missed=<n> rows_new=<n> cause=<the cause word, or mixed|none>`.
c. **The controls (rule 22):** POSITIVE: the same comparison for `UNH_US_Equity` prints `CONTROL-POSITIVE UNH_US_Equity rows_missed=0` (if UNH's build moves a row, say so plainly and do not hide it); NEGATIVE: copy BZLFY's stored `model_rows`, delete ONE valued row from the copy, compare the copy against the stored rows with the SAME finder and print `CONTROL-NEGATIVE planted_row_dropped rows_missed=1 identity=<the planted row's identity>`.
d. The last line, exactly: `GUARD-STOPS names=3 gets=<requests> bytes=<bytes>`. **The issuer expects `rows_missed=1` for each name (the guard's own counts); the counts and causes are the FINDING: do not change anything to make them read so.** If any name reads otherwise, print what you read and file a row.
e. File ONE surprise row per distinct cause found (or one row saying the three share a cause), naming the rows, causes and evidence; do not touch any source file. A surprise is a row; keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~185/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-co-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~185/co1_names.out</invocation><expect>(?ms)^DROPPED-ROW BZLFY_US_Equity rows_stored=\d+ rows_built=\d+ rows_missed=\d+ rows_new=\d+ cause=\S+$.*^DROPPED-ROW PBR_US_Equity rows_stored=\d+ rows_built=\d+ rows_missed=\d+ rows_new=\d+ cause=\S+$.*^DROPPED-ROW TSM_US_Equity rows_stored=\d+ rows_built=\d+ rows_missed=\d+ rows_new=\d+ cause=\S+$.*^GUARD-STOPS names=3 gets=\d+ bytes=\d+$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-co-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~185/co1_names.out</invocation><expect>(?s)CONTROL-POSITIVE UNH_US_Equity rows_missed=0.*CONTROL-NEGATIVE planted_row_dropped rows_missed=1 identity=\S+</expect></criterion>
</proof_of_spec>

- AC1 is the finding (one `DROPPED-ROW` line per name; `cause` is the finding). AC2 holds both controls (the finder sees no miss where there is none and exactly the planted one). **If a line reads otherwise, DO NOT edit the expectation or the finder to match: print the actual line, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-20 ~16:46Z):** both FAIL as expected (`cat` of a file that does not exist). If a base state differs, say so and do not weaken a pattern.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your first row id is `AMGT_HARVST-D1-W185-S1`. The channel file has MIXED line endings and is append-only: READ ITS TAIL for the id sequence, append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body AND run the gate against your row WITHOUT the override first.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~185/AMGT_HARVST.TO-HVST-co-1.the-valued-row-each-of-the-three-guard-stopped-names-drops-is-named-with-its-cause.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-co-1.the-valued-row-each-of-the-three-guard-stopped-names-drops-is-named-with-its-cause` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-co-1.the-valued-row-each-of-the-three-guard-stopped-names-drops-is-named-with-its-cause.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-99 analysis (`ledger/ROUND_ANALYSIS.round99.md` @f6e9ee7ec4, msg 8708) item 1 and the ruling on row `D1-S68`: the one-row guard STOP stays the limit; round 101 may rule a carry-forward only if every cause is a vendor field absent in the new block.
- Chain A of round 100 (its own worker `~185`: no dependency on another chain; disjoint write set). Slot ~185, worktree `C:/dev/wk-harvst-185`, branch `wk-AMGT_HARVST-185`. **Sparse set at provision (each named file CHECKED BY NAME, and `python -c "import lib.research.corpus.dossier"` RUN in the worktree after the add, because the code reads files its order does not name):** `.claude/agents`, `lib`, `integrations/bloomberg/research`, `infra/aws/ec2/opal-gateway/app`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922` (`continuation.KPI_LEXICON_PATH` reads `research_docx_kpi_census.json` from it: the miss that blocked `~179` and `~180`), and the deliverables folders `0.9.0_WK_AMGT_HARVST~180`, `~178`, `~175`.

- **COMPLETE (issuer, 2026-10-20 ~17:2xZ):** worker `~185`, branch merged `78a38ea7ad` (finder and output `c3c1565ba0`, proof `a0c46b4b0e` VALID rc 0). THE FINDING: all THREE names drop the same row, `typecast|BEST_DPS|FY1` (stored values BZLFY 0.391, PBR 9.546, TSM 131.309), cause `field_absent_in_new_block`: the 2026-10-20 model blocks list `BEST_DPS` FY1 as unresolved with `HELD_OFF: SA fallback held off by --no-sa-fallback; gap left unfilled`. Counts `BZLFY 56/55`, `PBR 56/55`, `TSM 54/53` equal the guard's own; controls `CONTROL-POSITIVE UNH_US_Equity rows_missed=0` (92 of 92) and `CONTROL-NEGATIVE planted_row_dropped rows_missed=1`. READ BY ME (not the worker's word): I read TSM's TWO model blocks from S3 myself (`derived/model_block/TSM_US_Equity/20261018T130948Z` carries `BEST_DPS` forecast figures 131.309 and 193.687; `.../20261020T131131Z` lists `BEST_DPS` FY1, FY2 and FY3 unresolved with the HELD_OFF reason). NOT read by me: BZLFY's blocks, PBR's 2026-10-20 block, and I did NOT re-run the script (800 requests, 145 MB). WHAT THIS GIVES THE CTO: every cause is a vendor field absent in the new block, which is the condition his ruling on `D1-S68` names for round 101 to rule a carry-forward of the stored value marked as carried; the common cause is the daily induction run's `--no-sa-fallback` hold-off.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>100</round>
<workstream>GUARD-STOPS</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
