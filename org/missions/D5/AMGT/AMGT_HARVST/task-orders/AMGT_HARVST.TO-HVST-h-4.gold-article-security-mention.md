# AMGT_HARVST task order -- `HVST-h-4` -- H4: gold `article_security_mention`, one row per (article, security) graded A-D by a first-match partition over the stored text, absolute figures only, built from silver and re-derivable; written under builder-output addresses in `opal-data-harvest`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-h-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~4</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on any harvest surface (C1=23 C2=7 C3=12 C4=21 C5=334); gold objects at new prefixes are not a deploy and nothing reads them yet.
comp-iam: RUN at L5 on the DESIRED plane only; this box's S3 write to amgt/harvest/gold/ is measured by AC4's own conditional PUT, and a refusal is a BLOCKING row.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~4`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/` and every EXISTING path in section 3 exist. It also tests that
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~10/RUN_REPORT.md` exists, which is the Lenovo run's
  report. If any is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~4;`.
- **NEVER RUN AN INSTALL. NEVER CALL A PUBLISHER.** AWS is allowed only as S3 reads of `opal-data-harvest` silver and
  conditional writes under `amgt/harvest/gold/`.

## 1. THE CELL, inlined in full -- `HVST-h-4` (manifest row H4, outcome FWD-4)

**The contract, verbatim** (PRD v0.2 @9102ccfe81, `C-HV-MENTION-GRADE`):
- The gold `article_security_mention` table has one row per (article, security), at
  `amgt/harvest/gold/article_security_mention/date=<d>/`.
- Each row carries:
  - `mention_count`, `mention_in_title`, `mention_in_lead` (the first three blocks) and `first_mention_block`;
  - `blocks_hit` and `blocks_total` (absolute counts; the share of blocks is computed where the tier is assigned and is
    never stored);
  - `match_forms`;
  - `vendor_tagged_primary` and `vendor_tagged_secondary`;
  - `co_mentioned_securities`, `co_mention_count` and `is_roundup`;
  - `signal_tier` (A-D) and `signal_weight`;
  - the three clocks and `lag_hours`;
  - lineage.
- **The tier rule is a partition that assigns every case,** evaluated A then B then C then D, first match wins. "Lead" is
  the first three blocks and "share" is `blocks_hit / blocks_total`:

  | tier | rule | working weight |
  |---|---|---|
  | A | named in the title AND in the lead | 1.0 |
  | B | named in the title, OR in the lead, OR share >= 0.3 | 0.6 |
  | C | named 2 or more times | 0.3 |
  | D | everything else | 0.1 |

  The weights and the 0.3 are working defaults. The roundup threshold is `co_mention_count >= 5`.

**The other contracts:**
- `C-HV-LINK-IS-GOLD`: *"Which company an article is about is Opal's judgement, so it lives in gold, never in silver."*
- `C-HV-GOLD-REBUILDABLE`: *"Gold is built from silver only. A rebuild from the same silver reproduces identical rows."*
- `C-HV-ABSOLUTE-ONLY`: *"No gold table of this project stores a relative figure: no ratio, share, z-score or normalised
  score."*
- `C-HV-KEY`: *"Every gold row carries `security_key`, and `composite_figi` wherever the crosswalk holds it."*

**Outcome FWD-4, DONE WHEN:** *"every (article, company) pair carries whether the company is in the headline, in the
opening, how often it is named, how much of the article names it, which other covered companies it names, and a strength
grade; the grade is re-derived from the stored text and matches"*.

**THE STATE you start from** (read at your branch HEAD):
- The silver `article` tables for the five sources exist in `opal-data-harvest`, built by `HVST-h-2` and loaded by
  `HVST-h-9` (the pilots) and `HVST-h-10` (Lenovo).
- **Read their column set from `lib/opal_data_harvest/silver_from_bronze.py`** (`title`, `text_blocks`, the three
  clocks, `discovered_for`, and the vendor fields).
- `lib/research/harvest/store.py`:
  - `silver_latest(source, table, record_key_fields, client=None)` reads the latest row per key;
  - `address_of(source, tier, table, partition, object_name=None)` is the builder: it prints
    `s3://opal-data-harvest/amgt/harvest/gold/article_security_mention/date=2026-09-22` for
    (`amgt`, `gold`, `article_security_mention`, `date=2026-09-22`), as measured at the cut;
  - `form_c_object`.
- There is no gold writer in `store.py`, and you do not edit it.
- **The covered securities** are the five `pilot_securities` in `lib/opal_data_harvest/config.json` plus Lenovo from
  `HVST-h-10`'s deliverables (`lenovo.security.json`, or the universe record its `RUN_REPORT.md` names). Names and
  aliases are read from there.
- **The crosswalk** is `lib/research/identity/crosswalk.py`. Read `composite_figi` for a `security_key` only where it
  holds one; otherwise it is None, never guessed.

**RULED -- what you build:**
1. **A new module, `lib/research/harvest/publication_gold.py`:**
   - `mention_rows(article_row, securities, weights=WEIGHTS, share_b=0.3, roundup_at=5)` is PURE and returns one row per
     covered security the article names at least once.
     - It uses the SAME word-bounded match as the harvester's floor:
       `(?<!\w)` + `re.escape(alias)` + `(?!\w)`, case-insensitive, over each alias.
     - `match_forms` lists which aliases matched.
     - The vendor tags come from a documented per-publisher `VENDOR_TAG_FIELDS` table (for example, SA
       `primaryTickers` and `secondaryTickers`), matched to the security by ticker. Where a publisher sends none, the
       value is None.
     - `lag_hours` = (`first_discovered_at` or `fetched_at`) minus `published_utc`, in hours.
     - Lineage is the silver `article_key`, `bronze_key` and `record_hash`.
     - The share is computed in a local variable for the tier and NEVER returned.
   - `WEIGHTS = {"A": 1.0, "B": 0.6, "C": 0.3, "D": 0.1}`. The working defaults sit at the top of the module with one
     comment line naming them working defaults.
   - `write_gold(table, rows, as_of_date, run_stamp, client=None)` writes ONE parquet snapshot at
     `address_of("amgt", "gold", table, date_partition(as_of_date), form_c_object("part-" + run_stamp, "parquet"))`
     with `IfNoneMatch="*"`, then reads it back (a HEAD, and a length match). **The `date=` partition of a gold table
     is the BUILD date**, and each build is a full snapshot (the working rule of this round).
   - A CLI: `python -m lib.research.harvest.publication_gold build-mention --securities-json FILE --as-of YYYY-MM-DD`.
     It reads every source's silver `article` through `silver_latest`, builds the rows, writes the snapshot, and prints
     `{"articles_read", "pairs", "tier_counts", "securities_with_rows", "key"}`.
2. **New test file `lib/research/harvest/tests/test_publication_gold_mention.py`,** pure fixtures, with a stub S3 client
   for `write_gold`. Exactly twelve arms:
   - `test_tier_a_title_and_lead`
   - `test_tier_b_title_only`
   - `test_tier_b_lead_only`
   - `test_tier_b_share_at_threshold`
   - `test_tier_c_two_mentions_outside_title_and_lead`
   - `test_tier_d_single_passing_mention`
   - `test_partition_assigns_every_case` (an exhaustive grid over title x lead x count x share assigns exactly one tier
     each)
   - `test_share_never_stored` (no key of any row contains "share", "ratio", "pct" or "norm")
   - `test_co_mention_and_roundup`
   - `test_vendor_tags_mapped_or_none`
   - `test_same_match_as_harvester_floor`
   - `test_write_gold_key_is_builder_output`

**What this cell does NOT change:**
- silver;
- `store.py`;
- the harvester package;
- the chatter axis;
- any served object.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @9fbf337a74, chain A position 6 of 9. After `HVST-h-10`. `HVST-h-5` (`chatter_daily`)
reads your table next and extends your module.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/test_publication_gold_mention.py
lib/research/harvest/store.py
lib/research/harvest/tests/test_store.py
lib/research/identity/crosswalk.py
lib/opal_data_harvest/silver_from_bronze.py
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/config.json
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~10/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/universe.json
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~4/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-h-4.gold-article-security-mention.md
</paths>

- **Only `publication_gold.py` and its new test file may change.** AC3 fails otherwise.
- Scratch goes in `<your worktree>/.scratch/hv4/`.
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~4 <0.9.0_WK_AMGT_HARVST~4@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **The code and tests come first** (AC1-AC3). The live build (AC4, AC5) comes after they pass.
- **The weights, 0.3 and 5 are working defaults.** State them in your report and never tune them.
- **A refused PUT is a BLOCKING row.**
- **Pure ASCII.**
- **Surprise rows:** `AMGT_HARVST-Z-W4-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

Write the securities file `.scratch/hv4/securities.json` (the five pilots plus Lenovo, as section 1 names them). Save
a byte-identical copy to `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~4/securities.json`,
which `HVST-h-5` and `HVST-h-6` read. Then write
`.scratch/hv4/rederive.py`, which:
- reads the snapshot key AC4 printed;
- recomputes `mention_rows` from `silver_latest` for every source;
- compares the two as sets of row tuples, excluding only `run_stamp`;
- prints `rows_written <w> rows_rederived <r> symmetric_difference <d>`.

<proof_of_spec>
  <criterion id="AC0" cell_refs="HVST-h-4"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests/test_store.py -q --color=no -p no:cacheprovider 2>&1 | tail -1</invocation><expect>BEFORE any edit, the baseline recorded (measured at the cut: 11 passed)</expect></criterion>
  <criterion id="AC1" cell_refs="HVST-h-4"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests/test_publication_gold_mention.py -v --color=no -p no:cacheprovider 2>&1 | tail -16</invocation><expect>"12 passed" and no "failed" -- the twelve arms named in section 1 item 2</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-h-4"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests/test_store.py -q --color=no -p no:cacheprovider 2>&1 | tail -1</invocation><expect>equal to AC0</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-h-4"><invocation>cd "$(git rev-parse --show-toplevel)" && git diff --name-only "$(git merge-base HEAD SITEZ)" HEAD -- lib && git status --porcelain -- lib && echo "--- end"</invocation><expect>before "--- end", ONLY lib/research/harvest/publication_gold.py and lib/research/harvest/tests/test_publication_gold_mention.py (each file once or twice across the two listings), and nothing else under lib</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-h-4"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.harvest.publication_gold build-mention --securities-json .scratch/hv4/securities.json --as-of "$(date -u +%Y-%m-%d)"</invocation><expect>a JSON line with articles_read at least 1, pairs at least 1, securities_with_rows including 992_HK_Equity when the Lenovo run accepted any article (else the RUN_REPORT's zero is cited in the instance), and a key beginning "amgt/harvest/gold/article_security_mention/date="</expect></criterion>
  <criterion id="AC5" cell_refs="HVST-h-4"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/hv4/rederive.py</invocation><expect>"symmetric_difference 0" with rows_written equal to rows_rederived -- the grade re-derived from the stored text matches (FWD-4)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~4/AMGT_HARVST.TO-HVST-h-4.gold-article-security-mention.proof_of_spec.json`.
2. Grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5`, which must return rc 0.
3. Flip only on all PASS.
4. Commit with `--only`.
5. Report once, with the tier counts per security.

**MUTATION DISCIPLINE:** snapshot the working-tree bytes to `.scratch/hv4/` first. Never `git checkout --`, `stash` or
`git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **The gold partition is the BUILD date, taken as a full snapshot.** This is a working rule of this round, which the
   PRD leaves open. It is stated here so the CTO's round analysis can amend it.
2. **The CVO's carry item** ("tier D: at most one mention") changes no behaviour here. The first-match partition already
   gives D only to at most one mention outside title and lead, with share < 0.3.
3. **The same word-bounded match as the floor** keeps gold from grading articles retrieval would never have kept.

<status>pending</status>
<round>1</round>
<slot>~4</slot>
<fabric>site-z</fabric>
