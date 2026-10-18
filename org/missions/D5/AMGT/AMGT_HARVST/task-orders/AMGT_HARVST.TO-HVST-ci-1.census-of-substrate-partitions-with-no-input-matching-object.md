# AMGT_HARVST task order -- `HVST-ci-1` -- ROUND 94, workstream PICK2-CENSUS: A READ-ONLY CENSUS OF EVERY STORED PARTITION THE SUBSTRATE READS, PRINTING WHETHER ANY OBJECT'S INPUTS MATCH TODAY'S (row `W165-S3`; CTO round-93 analysis item 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ci-1.census-of-substrate-partitions-with-no-input-matching-object</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ci-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~169</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- READ-ONLY S3 reads of the bucket `opal-data-harvest` ONLY: list and get under the gold tables that `lib/research/corpus/substrate.py` reads (see section 1), and whatever each producer module's own `current_inputs(...)` reads, through `lib.research.harvest.store._default_client()`; never `put`, `delete`, `copy`, `sync` or a bare `aws` call. Budget: at most 8000 requests and 1 GiB in all, counted in the census's last line (the sister censuses needed 363 to 1,750 requests and 100 to 141 MiB). NO gold or silver writer is RUN: no `write_one`, no `gold_put`, no `--write`. NO deploy, NO edit of any source file, NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is a census that decides "no input match" with an inputs value that is not the one the substrate uses (copy each table's `wanted` from substrate.py lines 214, 248, 268 and 281, never from memory), a census that reads only the continuation table (there are four), a census that prints a count without its denominator, a "moves" column computed with the CHANGED module instead of a reimplemented rule, a comparator that cannot see a change (it has a negative control), and a census whose expectation is edited to match.
</preflight>

## 0. THE CELL

`lib/research/corpus/substrate.py::_pick_stored(table, partition, wanted_inputs, current_method_version, client)` (line 121) returns, per stored table partition, the object whose `inputs` equal today's (`current` True, through `continuation._select_stored`), and when NO object's `inputs` match it falls back to `docs[sorted(docs)[-1]]` (line 158: the lexicographically LAST KEY, `current` False). The key is a content hash, so that pick is arbitrary; it is the same class of defect as the fallback `HVST-ch-1` fixed in `_select_stored` (row `AMGT_HARVST-D1-W165-S3`). **How many partitions fall to it is not measured except for the continuation table (`no_input_match=0` before `HVST-ch-7`).** This cell measures it over every table the substrate reads, read-only, and changes no file.

## 1. THE BUILD (a read-only script; no product code)

Work in your worktree. Change only the files named in `<paths>`.
a. Read `lib/research/corpus/substrate.py` lines 121-290 first. The substrate calls `_pick_stored` for FOUR tables: `continuation.TABLE` (partition per security), `sector_template.TABLE` (partition per business type), `fund_form.TABLE` (partition per fund) and `typecast.TABLE` (one fixed partition). **The dossier table is NOT among them** (a dossier is built from the substrate's picks; it is not picked by it).
b. Write `ci1_census.py` in your deliverables folder (start from `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~165/ch1_census.py`, which already lists the continuation partitions, reads every object, computes `wanted` and applies the gateway's rule; read it) and run it once in the FOREGROUND with `python -u`, stdout to `ci1_census.out` (open the output file with `newline="\n"`).
c. For EVERY partition of EACH of the four tables (enumerate the partitions by listing the table prefix `gold.table_prefix(<table>)`; the securities, business types and funds come from the listing, never from a typed list): list its objects, read every object (each carries `method_version` and `inputs`), compute `wanted` EXACTLY as substrate.py does for that table (the same function call with the same arguments), and count the objects whose `inputs` equal `wanted`. Print one line per table `TABLE <name> partitions=<n> objects=<n> input_match=<partitions with at least one matching object> no_input_match=<partitions with none>`. For EVERY partition with NO matching object print `FALLBACK <table> <partition> objects=<n> methods=<comma-separated method_version integers> old=<first 8 characters of the object name>/<method_version integer> rule=<...>/<...> moves=<yes|no>` where OLD is the key-order pick reimplemented in the census (`sorted(docs)[-1]`, never read from the changed module), RULE is: the highest `method_version` (the INTEGER after the last `/`; a missing or unparsable value counts as -1), then the last written (the greater `LastModified`, the key breaking an exact tie; a missing value never outranks a present one), and `moves` is `yes` when OLD and RULE name different objects.
d. **The controls (rule 22: a census needs both).** POSITIVE: print `CONTROL-POSITIVE continuation MNST_US_Equity input_match=yes fallback=no` after computing it with the SAME code path as step c (MNST is at the current method and its inputs match). NEGATIVE: build in memory four objects shaped like UNH's (object names `28404359eb0645c4.json` method `.../3`, `4d837586380648bd.json` `.../4`, `98a4883c1b099e6b.json` `.../1`, `f174f7092a2d358e.json` `.../2`, last-modified rising in the order /1, /2, /3, /4) none of whose inputs match, run them through the SAME OLD and RULE code as step c, and print `CONTROL-NEGATIVE synthetic old=f174f709/2 rule=4d837586/4 moves=yes`.
e. The final line, exactly: `CENSUS-FALLBACK tables=4 partitions=<n over all tables> no_input_match=<n> moves=<n> gets=<requests> bytes=<bytes>`. **The issuer expects `tables=4`.** The counts are the FINDING: do NOT change anything to make them read 0; print every partition plainly. If the census would exceed its budget, STOP at the budget, print `BUDGET-EXCEEDED gets=<n>` and file a row.
f. If any partition falls to the fallback, file ONE surprise row summarising them (counts per table, whether any `moves=yes`, and the reason you can read: for example a producer's inputs moved after the stored objects were written). Do not guess a reason you cannot read. Do not touch any source file. A surprise is a row; keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~169/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ci-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~169/ci1_census.out</invocation><expect>(?m)^CENSUS-FALLBACK tables=4 partitions=\d+ no_input_match=\d+ moves=\d+ gets=\d+ bytes=\d+$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ci-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~169/ci1_census.out</invocation><expect>(?m)^CONTROL-POSITIVE continuation MNST_US_Equity input_match=yes fallback=no$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ci-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~169/ci1_census.out</invocation><expect>(?m)^CONTROL-NEGATIVE synthetic old=f174f709/2 rule=4d837586/4 moves=yes$</expect></criterion>
</proof_of_spec>

- AC1 is the shape (and the 4 tables the issuer expects); its counts are the finding. AC2 and AC3 are the controls: the census sees a matching partition as matching, and sees a key-order pick and the rule disagree when they do. **If a control prints another line, DO NOT edit the expectation or the code to match: print the actual line, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-18 ~05:4xZ):** all three FAIL as expected (`cat` of a file that does not exist). If a base state differs, say so and do not weaken a pattern.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W169-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~169/AMGT_HARVST.TO-HVST-ci-1.census-of-substrate-partitions-with-no-input-matching-object.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ci-1.census-of-substrate-partitions-with-no-input-matching-object` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ci-1.census-of-substrate-partitions-with-no-input-matching-object.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line (a commentary on the matched line breaks the `$` anchor).
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-93 analysis (`ledger/ROUND_ANALYSIS.round93.md` @5ef0dd0efd, msg 7921) item 1 ("a read-only census over every stored table the substrate reads ... with the denominator printed"). **My correction to the CTO's list, in the face:** he wrote "(continuation, fund form, dossier)"; `substrate.py` calls `_pick_stored` for continuation, sector_template, fund_form and typecast, not the dossier (lines 216, 250, 270, 282). The order reads the four the substrate reads; the CTO is told.
- Chain A of round 94: this cell, then `HVST-ci-2` (the change, same worker queue `~169`: the second depends on the first's census).
- Slot ~169, worktree `C:/dev/wk-harvst-169`, branch `wk-AMGT_HARVST-169`. Widen the sparse set at provision with `lib/research`, `.claude/agents`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922`, `infra/aws/ec2/opal-gateway/app` and `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~165`.
- **SENT:** with the round-94 issuance.
- **AMENDMENT 1 (issuer, 2026-10-18 ~06:0xZ; worker `~169` row `D1-W169-S1`, BLOCKING, INERT): MY AC3 EXPECTATION WAS WRONG.** The face defines OLD as the key-order fallback `sorted(docs)[-1]` (the LAST key; substrate.py line 158) and the synthetic four have keys `28404359...`, `4d837586...`, `98a4883c...`, `f174f709...`: the LAST key is `f174f7092a2d358e.json`, method `/2`, so OLD reads `f174f709/2`. I copied `old=28404359/3` from `HVST-ch-1`, whose OLD rule was `min` by key (the FIRST key), a different rule. The worker's census printed `old=f174f709/2` and did not edit anything to match; `HVST-ci-2`'s order already says `f174f7092a2d358e.json`. **The AC3 expectation and the step 1d sentence read `old=f174f709/2` from this amendment; the census output is unchanged** (I re-ran `ci1_census.py` from the worker's worktree: identical to the worker's, line for line). Gate: this is a modification of a non-terminal order that declares `<placeholders>NONE</placeholders>`; no gate limb graded it (the commit result is stated in the amendment commit). The worker regrades AC3 and re-runs the checker; the earlier FAIL stays in its instance as history.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>94</round>
<workstream>PICK2-CENSUS</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
