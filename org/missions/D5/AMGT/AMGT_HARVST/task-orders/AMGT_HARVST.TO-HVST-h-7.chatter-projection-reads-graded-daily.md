# AMGT_HARVST task order -- `HVST-h-7` -- H7: the chatter axis can rank from the graded `chatter_daily` table through its ONE read adapter, with relative figures computed at serve time; the DEFAULT stays the legacy read, so nothing served moves; CODE ONLY, no deploy, no Terraform, no DynamoDB write

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-h-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~7</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on lib/research/metrics or lib/research/coverage (C1=23 C2=7 C3=12 C4=21 C5=334); this cell deploys nothing.
comp-iam: RUN at L5 -- amgt-resapp-chatter-axis-lambda-role grants s3:GetObject and a prefix-conditioned s3:ListBucket on the harvest pool prefixes only (DESIRED plane); the gold prefixes are NOT granted, which is why the served switch is out of this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~7`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/`, every EXISTING path in section 3, and `lib/research/harvest/tests/test_publication_gold_event.py` exist.
  - That last file is the predecessor's. If it is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~7;`.
- **NEVER RUN AN INSTALL. NEVER CALL AWS. NEVER RUN `terraform`, `safe-apply`, a Lambda deploy or the chatter
  producer's `main` against real stores.** Every read in your tests is a stub.

## 1. THE CELL, inlined in full -- `HVST-h-7` (manifest row H7, outcome FWD-7)

**The contract, verbatim** (PRD v0.2 @9102ccfe81, `C-HV-AXIS-PROJECTION`):
- This REPLACES, in `AMGT_RESAPP`'s ratified `C-ONE-STORE`, the read path of the chatter-axis producer and the coverage
  reader.
- Today they read the association from `publication-links/v1/` and the body from `publications/v1/` through one adapter.
- Once H5 (`chatter_daily`) and H4 (`article_security_mention`) land, both read THOSE gold tables through that same
  single adapter.
- The served chatter ranks (the DynamoDB TRENDING and BREAKOUT rows) become a projection of `chatter_daily`, with their
  relative figures computed at serve time, never a separate count.
- `publication-links/v1/` and `publications/v1/` retire under `AMGT_RESAPP`'s `C-FORMAT-SEQUENCE`: readers switched,
  writers stopped and the read grant removed, in ONE window, with that move's never-widen pair. Until then
  `C-ONE-STORE` binds as written.

**Outcome FWD-7, DONE WHEN:** *"the chatter ranks on the page are computed from the graded daily table, and a company
named once in passing in many articles no longer outranks one that was the subject of a few"*.
- **This cell builds and proves the ranking change IN CODE.**
- The served switch (the DynamoDB rows) is a never-widen act in `C-FORMAT-SEQUENCE`'s single window. It is NOT this
  cell's.

**THE MEASURED STATE at SITEZ @9fbf337a74** (re-read at your HEAD):
- **The ONE read adapter is `lib/research/coverage/pool_reader.py`** (INTERFACE P-1, 593 lines). `window_read(identity,
  start, end)` (`:461-550`) returns `counts` plus the four failure states. `daily_counts` is at `:581-593`, and
  `STATE_NAMES` is used by the producer.
- **The producer is `lib/research/metrics/chatter_axis.py`** (864 lines):
  - `default_daily_article_counts` (`:355-375`) calls `pool_reader.window_read`, stashes `READ_DETAIL`, and returns
    `{date: count}`;
  - `count_all_tickers(tickers, start, end, count_fn=default_daily_article_counts)` (`:387-393`);
  - `dense_series` (`:396-403`);
  - `normalize_scores` (`:411-438`), `rank_top_n` (`:445-464`), `build_rows` (`:472-522`);
  - `compute_chatter_axis` (`:538-667`);
  - `main` (`:783-860`).
- The baselines at the cut:

  | test file | result |
  |---|---|
  | `lib/research/metrics/tests/test_chatter_axis.py` | 45 passed |
  | `lib/research/metrics/tests/test_producer_axis_registry.py` | 5 passed |
  | `lib/research/coverage/tests/test_pool_reader.py` | 25 passed |
- **The gold table** (by `HVST-h-5`) is `amgt/harvest/gold/chatter_daily/date=<build date>/part-<stamp>.parquet` in
  `opal-data-harvest`, one full snapshot per build. Its columns are in `lib/research/harvest/publication_gold.py`
  (`daily_rows`), including `mention_score` and `data_status`.

**RULED -- what you build:**
1. **In `pool_reader.py`:** a new `gold_window_read(identity, start, end, client=None)`, with the SAME return shape as
   `window_read`.
   - `counts` is `{date: mention_score}`, read from the NEWEST `chatter_daily` snapshot's rows for that security.
   - The four failure states map from `data_status`: `DENIED` and `PARTIAL` days are reported in `states`, and are NEVER
     silently zero.
   - `window_read` itself is NOT changed.
2. **In `chatter_axis.py`:** a new count function `gold_daily_mention_scores(identity, start, end)`, which calls
   `pool_reader.gold_window_read` and fills `READ_DETAIL` as the legacy one does.
   - A new `--source {legacy,gold}` flag in `main`, **default `legacy`**.
   - `compute_chatter_axis` takes the count function from it.
   - `normalize_scores`, the breakout ratio and every relative figure stay computed HERE, at serve time, on whichever
     series was read. Nothing relative is written back to gold.
3. **New test file `lib/research/metrics/tests/test_chatter_axis_gold.py`,** with stub readers. Exactly seven arms:
   - `test_gold_read_returns_mention_score_series`
   - `test_gold_read_reports_partial_and_denied_not_zero`
   - `test_default_source_is_legacy` (`main`'s parsed default, and `compute_chatter_axis` called without a source,
     both still use `default_daily_article_counts`)
   - `test_passing_mentions_no_longer_outrank_subject`
   - `test_relative_figures_computed_at_serve_not_stored`
   - `test_legacy_path_output_unchanged` (the same stub legacy input gives byte-identical rows to the pinned module,
     loaded from `git show 9fbf337a74:lib/research/metrics/chatter_axis.py` into a temp file)
   - `test_one_adapter_for_both_reads` (chatter_axis imports no S3 client for gold; it goes through `pool_reader`)

   The `test_passing_mentions_no_longer_outrank_subject` fixture has two securities:
   - X appears in 10 articles, each once in passing (tier D, weight 0.1, score 1.0);
   - Y is the subject of 3 (tier A, weight 1.0, score 3.0).

   The arm asserts that the legacy count ranks X over Y, and the gold `mention_score` ranks Y over X.

**What this cell does NOT change:**
- `window_read`;
- the legacy default;
- `infra/`;
- any Terraform or Lambda packaging;
- DynamoDB;
- the coverage route's served reader;
- anything served.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @9fbf337a74, chain A position 9 of 9. After `HVST-h-6` (placed there only to keep one
worker on the chain; you read `HVST-h-5`'s table). **The served switch waits on:**
- a never-widen pair (the CTO and COO halves);
- the chatter role's two S3 limbs widened to the gold prefixes;
- `AMGT_RESAPP`'s single retirement window.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/coverage/pool_reader.py
lib/research/metrics/chatter_axis.py
lib/research/metrics/tests/test_chatter_axis_gold.py
lib/research/metrics/tests/test_chatter_axis.py
lib/research/metrics/tests/test_producer_axis_registry.py
lib/research/coverage/tests/test_pool_reader.py
lib/research/harvest/publication_gold.py
lib/research/harvest/store.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~7/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-h-7.chatter-projection-reads-graded-daily.md
</paths>

- **Only `pool_reader.py`, `chatter_axis.py` and the new test file may change.** AC3 fails otherwise.
- **`chatter_axis.py` is packaged into a Lambda by Terraform.** You do not build, zip or deploy it.
- Scratch goes in `<your worktree>/.scratch/hv7/`.
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~7 <0.9.0_WK_AMGT_HARVST~7@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **CODE ONLY.** The legacy path is byte-identical in behaviour. **Pure ASCII.**
- **Surprise rows:** `AMGT_HARVST-Z-W7-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC0" cell_refs="HVST-h-7"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in lib/research/metrics/tests/test_chatter_axis.py lib/research/metrics/tests/test_producer_axis_registry.py lib/research/coverage/tests/test_pool_reader.py; do echo "$t :: $(python -m pytest $t -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>BEFORE any edit, three baselines recorded (measured at the cut: 45 passed; 5 passed; 25 passed)</expect></criterion>
  <criterion id="AC1" cell_refs="HVST-h-7"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/metrics/tests/test_chatter_axis_gold.py -v --color=no -p no:cacheprovider 2>&1 | tail -11</invocation><expect>"7 passed" and no "failed" -- the seven arms named in section 1 item 3, including the passing-mention fixture ranking Y over X on gold and X over Y on legacy</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-h-7"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in lib/research/metrics/tests/test_chatter_axis.py lib/research/metrics/tests/test_producer_axis_registry.py lib/research/coverage/tests/test_pool_reader.py; do echo "$t :: $(python -m pytest $t -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>each line's passed and failed counts EQUAL its AC0 line</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-h-7"><invocation>cd "$(git rev-parse --show-toplevel)" && git diff --name-only "$(git merge-base HEAD SITEZ)" HEAD -- lib infra && git status --porcelain -- lib infra && echo "--- end"</invocation><expect>before "--- end", ONLY lib/research/coverage/pool_reader.py, lib/research/metrics/chatter_axis.py and lib/research/metrics/tests/test_chatter_axis_gold.py, and nothing under infra</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-h-7"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.metrics.chatter_axis --help 2>&1 | tr -s ' ' | grep -i -A2 -- '--source'</invocation><expect>the help text shows --source with choices legacy and gold and default legacy</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~7/AMGT_HARVST.TO-HVST-h-7.chatter-projection-reads-graded-daily.proof_of_spec.json`.
2. Grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4`, which must return rc 0.
3. Flip only on all PASS.
4. Commit with `--only`.
5. Report once.

**MUTATION DISCIPLINE:** snapshot the working-tree bytes to `.scratch/hv7/` first. Never `git checkout --`, `stash` or
`git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **Why a default-legacy flag and not a switch.** The switch is a served move that `C-FORMAT-SEQUENCE` puts in ONE
   window with the writers stopped and the grant removed, under a never-widen pair. A code default that changed on
   merge would move the served ranks at the next deploy, outside that window.
2. **The served act is a later cell or a direct act.** It rides the pair `1.0.0_SA_CTO~Z` and this seat sign, with
   `2.0.0_SA_COO~Z` for the retirement window (decomposition s.9).

<status>pending</status>
<round>1</round>
<slot>~7</slot>
<fabric>site-z</fabric>
