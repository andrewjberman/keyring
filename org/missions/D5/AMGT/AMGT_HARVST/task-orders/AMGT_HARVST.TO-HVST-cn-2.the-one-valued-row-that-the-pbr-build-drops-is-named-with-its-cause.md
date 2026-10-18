# AMGT_HARVST task order -- `HVST-cn-2` -- ROUND 99, workstream PBR-GUARD-STOP: A READ-ONLY CELL NAMES THE ONE VALUED ROW THAT THE `PBR_US_Equity` BUILD DROPS (55 VALUED ROWS BUILT AGAINST 56 STORED) AND ITS CAUSE (CTO round-98 analysis item 2: "It is a row whatever the cause; the guard was right to stop")

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cn-2.the-one-valued-row-that-the-pbr-build-drops-is-named-with-its-cause</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cn-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~180</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- READ-ONLY S3 reads of the bucket `opal-data-harvest` ONLY: list and get under `amgt/harvest/gold/research_dossier/`, `derived/model_block/`, the bronze objects the model block derives from and the objects `dossier.build` reads for ONE name (`PBR_US_Equity`), through `lib.research.harvest.store._default_client()`; never `put`, `delete`, `copy`, `sync` or a bare `aws` call. Budget: at most 2500 requests and 300 MiB in all, counted in the last line. NO gold or silver writer is RUN (`dossier.write_one` and every `--write` are NEVER run; only `dossier.build` in memory). NO Bloomberg, NO model call, NO network beyond the S3 client. NO edit of any source file, NO edit outside `<paths>`; you DO NOT call the live gateway.
comp-adversary: RUN at L5 -- the adversary is a comparator that reports a dropped row only because of key order or whitespace (compare parsed values), a "dropped" row that is merely the same row under a different label, a cause assigned from the mnemonic's NAME instead of from the two model blocks the dossiers cite (read both blocks), a stored value read from a different dossier than the one the gateway serves (use the gateway's `_pick_dossier` rule), a build that tries a network call (STOP and report), a finder that cannot see a missing row (it has a negative control), and a census whose expectation is edited to match.
</preflight>

## 0. THE CELL

`HVST-cm-4` (merged `aab57546ec`, `deliverables/0.9.0_WK_AMGT_HARVST~178/cm4_census.out`) measured that a dossier refresh would stop on exactly ONE name by the model-block guard: `PBR_US_Equity`, with `valued_rows_built=55` against `valued_rows_stored=56` (stored model block `20261017T130744Z`, built `20261018T130759Z`). A refresh that writes it would LOSE one valued `model_rows` entry. **The CTO wants the one row named and its cause found:** which `model_rows` row has a value in the stored dossier and none in the build, and why (the new model block does not carry the field; the row moved to another fiscal year; a vendor value that disappeared; a build rule). Whatever the cause, it is a row. This cell writes nothing and changes no source file.

## 1. THE BUILD (a read-only script; no product code)

Work in your worktree. Change only the files named in `<paths>`.
a. Read first: `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~178/cm4_census.py` and `cm4_census.out` (its `NAME`, `DIFF` and `GUARD` lines for `PBR_US_Equity`; START FROM THE SCRIPT's pick, build and guard code), `0.9.0_WK_AMGT_HARVST~175/cl3_census.py` (the same in a smaller form), and `lib/research/corpus/dossier.py` (how a `model_rows` row is built from a model block: `build`, `_model_block_read` and the function that turns a block's figures into rows; read how a row with a value is counted for the guard, as the guard counts it).
b. **Write `cn2_pbr.py`** in your deliverables folder and run it once in the FOREGROUND with `python -u`, stdout to `cn2_pbr.out` (open it with `newline="\n"`): (1) the SERVED dossier of `PBR_US_Equity` (the gateway's `_pick_dossier` rule over the partition) and the BUILT dossier (`dossier.build`, in memory); print `PBR served=<object name> built_as_of=<date>`; (2) the two model blocks the dossiers cite (the stored dossier's `model_block` input, `20261017T130744Z`, and the build's, `20261018T130759Z`): read both objects `derived/model_block/<key>/<stamp>/model_block.json` and print each block's size and the count of rows with a value under the guard's own counting rule; (3) compare the stored and built `model_rows` row by row, matching rows by their identity (mnemonic and fiscal year: read how a row is identified and print the identity rule); print `ROWMISS <identity> stored_value=<first 60 characters> built=<the built row's value or its absent reason, first 80 characters>` for EVERY row that has a value in the stored dossier and none in the build, and `ROWNEW <identity> ...` for every row with a value in the build and none in the stored one; (4) **the cause**, decided from the two BLOCKS, never from the mnemonic's name: for each `ROWMISS`, print `CAUSE <identity> <which of: field_absent_in_new_block | value_null_in_new_block | row_moved_to_other_fiscal_year | build_rule_dropped_it | other>` and the evidence (the block key and the field's value in each block, or the line of `dossier.py` whose rule dropped it; read it, do not guess); (5) **the controls (rule 22):** POSITIVE: the same comparison for `UNH_US_Equity` served against built prints `CONTROL-POSITIVE UNH_US_Equity rows_missed=0` (if UNH's build moves a row, say so plainly and do not hide it); NEGATIVE: copy PBR's stored `model_rows`, delete ONE valued row from the copy, compare the copy against the stored rows with the SAME finder and print `CONTROL-NEGATIVE planted_row_dropped rows_missed=1 identity=<the planted row's identity>`; (6) the last line, exactly: `PBR-DROPPED-ROW rows_stored=<n> rows_built=<n> rows_missed=<n> rows_new=<n> cause=<the cause word of the single missed row, or mixed|none> gets=<requests> bytes=<bytes>`. **The issuer expects `rows_stored=56 rows_built=55 rows_missed=1`; the counts are the FINDING: do not change anything to make them read so.** If `rows_missed` is not 1, print what you read and file a row.
c. File ONE surprise row naming the missed row, its cause and the evidence; do not touch any source file. A surprise is a row; keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~180/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cn-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~180/cn2_pbr.out</invocation><expect>(?m)^PBR-DROPPED-ROW rows_stored=56 rows_built=55 rows_missed=1 rows_new=\d+ cause=\S+ gets=\d+ bytes=\d+$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cn-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~180/cn2_pbr.out</invocation><expect>(?s)CONTROL-POSITIVE UNH_US_Equity rows_missed=0.*CONTROL-NEGATIVE planted_row_dropped rows_missed=1 identity=\S+</expect></criterion>
</proof_of_spec>

- AC1 is the CTO's finding (the one row; `cause` is the finding). AC2 holds both controls (the finder sees no miss where there is none and exactly the planted one). **If a line reads otherwise, DO NOT edit the expectation or the finder to match: print the actual line, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-18 ~17:4xZ):** both FAIL as expected (`cat` of a file that does not exist). If a base state differs, say so and do not weaken a pattern.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your first row id is `AMGT_HARVST-D1-W180-S1`. The channel file has MIXED line endings and is append-only: READ ITS TAIL for the id sequence, append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body AND run the gate against your row WITHOUT the override first.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~180/AMGT_HARVST.TO-HVST-cn-2.the-one-valued-row-that-the-pbr-build-drops-is-named-with-its-cause.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cn-2.the-one-valued-row-that-the-pbr-build-drops-is-named-with-its-cause` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cn-2.the-one-valued-row-that-the-pbr-build-drops-is-named-with-its-cause.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-98 analysis (msg 8174) item 2. This cell is the driver's own first real case: the driver skips PBR by its guard until the cause is known.
- Chain B of round 99 (its own worker `~180`: no dependency on chain A; disjoint write set). Slot ~180, worktree `C:/dev/wk-harvst-180`, branch `wk-AMGT_HARVST-180`. **Sparse set at provision (each named file CHECKED BY NAME after the add):** `.claude/agents`, `lib/research`, `integrations/bloomberg/research`, `infra/aws/ec2/opal-gateway/app` and the deliverables folders `0.9.0_WK_AMGT_HARVST~178` and `~175`.
- **SENT:** with the round-99 issuance.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>99</round>
<workstream>PBR-GUARD-STOP</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
