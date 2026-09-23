# AMGT_HARVST task order -- `HVST-r-3` -- ROUND 2: the gold mention table gains an EXPLICIT publisher column (row `-Z-S2`), settled with a PRINTED SHAPE READ beside the count; then all three gold snapshots are REBUILT offline so Lenovo's 14 new silver rows are reflected; NO vendor call

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-r-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~13</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on any harvest surface (C1=23 C2=7 C3=12 C4=21 C5=334); a gold snapshot at an existing prefix is not a deploy, and nothing served reads these tables yet (the chatter switch is held).
comp-iam: RUN at L5 on the DESIRED plane only; this box's write to amgt/harvest/gold/ was exercised in round 1 and is re-exercised here by the rebuild's own conditional PUT. A refusal is a BLOCKING row.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~13`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/` and every path in section 3 exist. If any is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~13;`.
- **NEVER RUN AN INSTALL. NEVER CALL A PUBLISHER.** AWS is allowed as S3 reads of `opal-data-harvest` and conditional
  writes under `amgt/harvest/gold/` ONLY.

## 1. THE CELL, inlined in full -- `HVST-r-3` (manifest row H4; outcomes FWD-4, FWD-7)

**WHY THIS CELL EXISTS -- row `AMGT_HARVST-Z-S2`, and the story is the evidence.** The gold
`article_security_mention` table carries **NO publisher column**: 23 columns, none of them `publisher` or
`publisher_code`. Yet `C-HV-DAILY-DENSE` requires `publishers_distinct` and `C-HV-EVENT-SPINE` requires
*">= 2 publishers"*. Both consumers get the publisher by PARSING `article_key`'s prefix (`barrons:WP-BAR-...`).

**The issuer's own first re-derivation of the event table read a `publisher` field, got `None` on all 86 rows, and
computed 0 events per security against the 5 actually written.** A key-prefix parse is a schema in disguise, and a
consumer who misses it gets silent zeros. `1.0.0_SA_CTO~Z`'s lean, in the round-1 analysis: the column, not a named parse
rule.

**RULED -- what you build, in order:**
1. **An explicit `publisher` column on every `article_security_mention` row**, carried from the silver row rather than
   parsed at the consumer. Keep the parse as the single fallback for a row whose silver lacks it, and name the fallback
   in one comment line.
2. **`daily_rows` and `event_rows` read the COLUMN**, not the prefix. The prefix parse survives in exactly ONE place (the
   fallback above) or nowhere.
3. **THE SETTLEMENT CONDITION, which the analysis attached to this row: a PRINTED SHAPE READ BESIDE THE COUNT.** Before
   and after, print the snapshot's actual column list (its SHAPE) next to the row count, so a reader can see the column
   exists rather than infer it from a number. A count alone does not settle this row.
4. **THE REBUILD, offline.** Today's gold snapshots PREDATE the Lenovo articles: the mention snapshot has 86 pairs over 3
   securities, and Lenovo's 14 silver rows landed after it. Rebuild all three tables from silver, in order:
   `build-mention`, then `build-daily`, then `build-event`, with the securities list at
   `deliverables/0.9.0_WK_AMGT_HARVST~4/securities.json`. **No vendor call: silver already holds everything.**
5. **The coverage axis will change and that is CORRECT, not a defect.** Round 1's 1590 `chatter_daily` rows all graded
   `DENIED` because silver `listing_hit` was empty. There is now 1 listing_hit row, so some days for the WSJ leg may grade
   PARTIAL. **Print the `data_status` distribution before and after and explain any change in one line.**

**What this cell does NOT do:**
- it does not touch silver, bronze, the harvester package, or anything served;
- it does not flip the chatter axis's source (that switch is held, decomposition section 11);
- it does not delete a previous snapshot. Gold snapshots ACCUMULATE, and a rebuild writes a new part.

## 2. WHERE THIS CAME FROM
Round 2, decomposition v1.1 @04a235adb7 section 10a, cell 3 of 5. Independent of the other four. `2.0.0_SA_COO~Z` was told
this rebuild rides this recut, so its trial report reads Lenovo's gold correctly.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/test_publication_gold_mention.py
lib/research/harvest/tests/test_publication_gold_daily.py
lib/research/harvest/tests/test_publication_gold_event.py
lib/research/harvest/store.py
lib/research/identity/crosswalk.py
lib/opal_data_harvest/silver_from_bronze.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~4/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~13/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-r-3.publisher-column-and-the-gold-rebuild.md
</paths>

- **Only `publication_gold.py` and its three test files may CHANGE.** `store.py`, `crosswalk.py` and
  `silver_from_bronze.py` are READ-ONLY. AC4 fails otherwise.
- Scratch goes in `<your worktree>/.scratch/r3/`.
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~13 <0.9.0_WK_AMGT_HARVST~13@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **The code and tests come first**; the rebuild after they pass.
- **A refused PUT is a BLOCKING row.** Never hand-type a key; every address is builder output.
- **Pure ASCII.** Baselines at this cut: mention 12 arms, daily 10, event 8, store 11. None may regress.
- **Surprise rows:** `AMGT_HARVST-Z-W13-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC0" cell_refs="HVST-r-3"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r3/shape_before.py</invocation><expect>BEFORE any edit: the newest article_security_mention snapshot's COLUMN LIST printed beside its row count, showing 23 columns with NO publisher column and 86 rows over 3 securities -- the shape read that row -Z-S2's settlement requires</expect></criterion>
  <criterion id="AC1" cell_refs="HVST-r-3"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in test_publication_gold_mention test_publication_gold_daily test_publication_gold_event; do echo "$t :: $(python -m pytest lib/research/harvest/tests/$t.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>each file passes with at least its baseline count (12, 10, 8) and no "failed"; the mention file gains an arm asserting the publisher COLUMN is present and equals the silver publisher, and the daily and event files each gain an arm asserting they read the COLUMN rather than parsing article_key</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-r-3"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.harvest.publication_gold build-mention --securities-json org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~4/securities.json --as-of "$(date -u +%Y-%m-%d)" && python -m lib.research.harvest.publication_gold build-daily --securities-json org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~4/securities.json --as-of "$(date -u +%Y-%m-%d)" && python -m lib.research.harvest.publication_gold build-event --securities-json org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~4/securities.json --as-of "$(date -u +%Y-%m-%d)"</invocation><expect>three JSON lines, each with a key under amgt/harvest/gold/; the mention line's securities_with_rows now INCLUDES 992_HK_Equity and its pairs exceed 86, because Lenovo's 14 silver rows landed after the round-1 snapshot</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-r-3"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r3/shape_after.py</invocation><expect>the rebuilt snapshot's COLUMN LIST printed beside its row count, now INCLUDING a publisher column; the per-security row counts including 992_HK_Equity; and the chatter_daily data_status distribution BEFORE and AFTER with one line explaining any change</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-r-3"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r3/ac4.py</invocation><expect>"outside_allowed []" -- only publication_gold.py and its three test files changed, nothing else under lib; each prints "compiles True crlf 0 non_ascii 0"</expect></criterion>
  <criterion id="AC5" cell_refs="HVST-r-3"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r3/rederive.py</invocation><expect>"symmetric_difference 0" for the mention table and for the event table, recomputed from the same silver excluding only run_stamp -- the rebuild is still deterministic (C-HV-GOLD-REBUILDABLE)</expect></criterion>
</proof_of_spec>

Write the four scratch scripts: `shape_before.py` and `shape_after.py` (the printed SHAPE READ beside the count, plus the
data_status distribution), `ac4.py` (the allowed-set diff and per-file compile, CRLF and non-ASCII), and `rederive.py` (the
determinism check).

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~13/AMGT_HARVST.TO-HVST-r-3.publisher-column-and-the-gold-rebuild.proof_of_spec.json`.
2. Grade with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5`, which must return rc 0.
3. Flip to `complete` only if every criterion passes.
4. Commit with `--only`.
5. Report once, with the before and after SHAPE lines quoted, Lenovo's gold row counts, and the data_status distribution.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **AC0 runs BEFORE the edit on purpose and is a SHAPE read, not a count.** The analysis attached that condition to this
   row precisely because a count cannot show a missing column.
2. **The data_status change is expected**, since round 1 had zero listing_hit rows and now has one. Requiring it to be
   explained in one line stops a later reader treating the shift as a regression.
3. **Snapshots accumulate.** The rebuild adds a part; nothing is deleted, and no delete is authorised anywhere in this
   project.

<status>pending</status>
<round>2</round>
<slot>~13</slot>
<fabric>site-z</fabric>
