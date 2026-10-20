# AMGT_HARVST task order -- `HVST-co-2` -- ROUND 100, workstream GOLD-SCHEDULE (step 1 of 3): A READ-ONLY CELL MEASURES THE GOLD CHATTER REBUILD -- ITS IMPORT CLOSURE AGAINST THE LAMBDA LIMIT, ITS NEWEST PARTITIONS AND LAG, ITS ROSTER SOURCE AND ITS WRITE RULE (CTO round-99 analysis item 2; row `AMGT_HARVST-D1-S67`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-co-2.the-gold-chatter-rebuild-is-measured-its-import-closure-its-newest-partitions-its-roster-and-its-write-rule</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-co-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~186</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- READ-ONLY S3 list calls (and `head_object`) on the bucket `opal-data-harvest` under `amgt/harvest/gold/` ONLY, through `lib.research.harvest.store._default_client()`; never `put`, `delete`, `copy`, `sync` or a bare `aws` call. NO gold, silver or bronze writer is RUN (`write_gold`, `build_mention`, `build_daily` and `build_event` are NEVER called; you only import `publication_gold` to measure its closure and read its constants). NO Bloomberg, NO model call. NO edit of any source file, NO edit outside `<paths>`; you DO NOT call the live gateway.
comp-adversary: RUN at L5 -- the adversary is a closure measured on a different entry than the one the rebuild runs (the entry is `lib.research.harvest.publication_gold`, whose `main` is what a scheduled rebuild would call), a closure that counts a package the entry only needs inside a function as if it loaded at import (credit each package to the module whose import loaded it, as the earlier measurement did), a "newest partition" read from the wrong table prefix or the wrong date (the `date=` partition is the BUILD date, not a row's own date), a roster source named from a comment instead of from the code that loads it, a write rule asserted without reading `write_gold`, and a measurement with no control.
</preflight>

## 0. THE CELL

The gold tables `chatter_daily` and `chatter_event` stopped on 2026-10-08 and 2026-10-03, and no schedule on this box rebuilds them (row `AMGT_HARVST-D1-S67`). The CTO wants a scheduled rebuild on its own clock, on the estate's pattern: a container task on Fargate if the entry's import closure is over the 250 MB unzipped Lambda limit, measured, not assumed. **This cell measures four things and builds nothing**: (1) the closure of the rebuild's entry, `lib.research.harvest.publication_gold` (its CLI is `main` with the subcommands `build-mention`, `build-daily`, `build-event`, each taking `--securities-json` and `--as-of`); (2) the write rule of `write_gold`; (3) how far behind each gold table is; (4) where the `--securities-json` roster comes from. The next cells (build, then apply) read your output.

## 1. THE BUILD (a read-only script; no product code)

Work in your worktree. Change only the files named in `<paths>`.
a. Read first: `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~181/cn4_closure.py` and `cn4_closure.out` (the closure method, its `LIBIMPORT` and `LAMBDA-CLOSURE` lines and its two controls: REUSE THE METHOD UNCHANGED, pointed at the new entry), `lib/research/harvest/publication_gold.py` (the imports, `write_gold` at line 534, the table constants `GOLD_TABLE`, `GOLD_DAILY_TABLE`, `GOLD_EVENT_TABLE`, and `main` at the end), `lib/research/harvest/store.py` (`table_prefix`, `address_of`, `date_partition`), `lib/trading_calendar.py` (the trading-day frontier) and `lib/research/coverage/covered_universe.py` (`covered_security_keys`).
b. **Write `co2_gold.py`** in your deliverables folder and run it once in the FOREGROUND with `python -u`, stdout to `co2_gold.out` (open it with `newline="\n"`), printing in this order:
   1. The two closure controls first, then the closure of the ENTRY, in the earlier measurement's exact shape: `CONTROL-POSITIVE target=lib.research.harvest.store pyarrow_in_closure=yes`, `CONTROL-NEGATIVE target=json third_party_tops=0`, then `GOLD-CLOSURE entry=lib.research.harvest.publication_gold lib_modules=<n> third_party_pkgs=<n> third_party_mb=<x> lib_code_mb=<x> total_mb=<x> limit_unzipped_mb=250 verdict=<OVER|UNDER> biggest=<pkg:mb,pkg:mb,pkg:mb> removable_by_lazy=<none|list>`.
   2. `GOLD-WRITE key_shape=<the object key template `write_gold` builds, with `<table>`, `<date>` and `<run_stamp>` as placeholders, no spaces> add_only=<yes|no> full_snapshot=<yes|no>`: from reading `write_gold` (its `IfNoneMatch`, its key, whether each build writes the whole table), never from its docstring alone; print on its own line `NOTE write_gold evidence: <the line numbers you read>`.
   3. `GOLD-NEWEST chatter_daily=<YYYY-MM-DD> chatter_event=<YYYY-MM-DD> article_security_mention=<YYYY-MM-DD> trading_days_behind=<n>`: the newest `date=` partition of each of the three tables under `amgt/harvest/gold/` (list with the S3 client, no `get` of any object body), and `trading_days_behind` = the number of trading days from `chatter_daily`'s newest partition date to the last completed trading day, by `lib/trading_calendar.py` (print the two dates beside it on a `NOTE` line).
   4. `GOLD-ROSTER source=<the file path and function that produce the securities list a build takes, no spaces> names=<n>`: find where the `--securities-json` roster of a gold build comes from. Start from `covered_universe.covered_security_keys()`, from native Grep of the words `securities-json`, `build-daily` and `build_daily` over `lib/`, `integrations/` and `org/missions/D5/AMGT/AMGT_HARVST/deliverables/`, and from the `README`/runbook text you find; also count the distinct `security_key` values in ONE newest `chatter_daily` object (read that one object's `security_key` column) and print `NOTE roster newest_chatter_daily_distinct_keys=<n> covered_universe_keys=<n> equal=<yes|no>`. If you cannot name the source from the repo, print `GOLD-ROSTER source=UNKNOWN names=0`, file a BLOCKING row saying what you read, and report: that is a finding, not a failure to hide.
c. File ONE surprise row if anything read differently from this face (for example a closure UNDER the limit, a table with no partition, or a write that is not add-only). A surprise is a row; keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~186/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-co-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~186/co2_gold.out</invocation><expect>(?ms)^CONTROL-POSITIVE target=lib\.research\.harvest\.store pyarrow_in_closure=yes$.*^CONTROL-NEGATIVE target=json third_party_tops=0$.*^GOLD-CLOSURE entry=lib\.research\.harvest\.publication_gold lib_modules=\d+ third_party_pkgs=\d+ third_party_mb=[\d.]+ lib_code_mb=[\d.]+ total_mb=[\d.]+ limit_unzipped_mb=250 verdict=(OVER|UNDER) biggest=\S+ removable_by_lazy=\S+$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-co-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~186/co2_gold.out</invocation><expect>(?ms)^GOLD-WRITE key_shape=\S+ add_only=(yes|no) full_snapshot=(yes|no)$.*^GOLD-NEWEST chatter_daily=\d{4}-\d\d-\d\d chatter_event=\d{4}-\d\d-\d\d article_security_mention=\d{4}-\d\d-\d\d trading_days_behind=\d+$.*^GOLD-ROSTER source=\S+ names=[1-9]\d*$</expect></criterion>
</proof_of_spec>

- AC1 is the host verdict (OVER means a container task, not a Lambda); AC2 is the write rule, the lag and the roster source. **If a line reads otherwise (including `source=UNKNOWN`), DO NOT edit the expectation or the script to match: print the actual line, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-20 ~16:46Z):** both FAIL as expected (`cat` of a file that does not exist). If a base state differs, say so and do not weaken a pattern.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your first row id is `AMGT_HARVST-D1-W186-S1`. The channel file has MIXED line endings and is append-only: READ ITS TAIL for the id sequence, append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body AND run the gate against your row WITHOUT the override first.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~186/AMGT_HARVST.TO-HVST-co-2.the-gold-chatter-rebuild-is-measured-its-import-closure-its-newest-partitions-its-roster-and-its-write-rule.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-co-2.the-gold-chatter-rebuild-is-measured-its-import-closure-its-newest-partitions-its-roster-and-its-write-rule` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-co-2.the-gold-chatter-rebuild-is-measured-its-import-closure-its-newest-partitions-its-roster-and-its-write-rule.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-99 analysis item 2 ("Its host is the estate pattern cm-6 settled (Fargate if its closure is over the Lambda limit; measure it, as cn-4 did)"; grade: one deliberate run writing the trading-day-current `chatter_daily` partition, read in S3; then the first scheduled fire read; never triggered by the upstream landing).
- Chain B of round 100, step 1 of 3. Steps 2 and 3 are DEFINED, NOT CUT (decomposition section 142): `co-5`, the rebuild driver and container recipe and Terraform on the cm-5/cn-5 pattern, is cut when THIS order merges and its `GOLD-CLOSURE` verdict and `GOLD-ROSTER` source are read; `co-6`, the seat order (apply, canary, deliberate run, schedule, first fire), is cut under its own never-widen pair after `co-5`. Slot ~186, worktree `C:/dev/wk-harvst-186`, branch `wk-AMGT_HARVST-186`. **Sparse set at provision (each named file CHECKED BY NAME, and `python -c "import lib.research.harvest.publication_gold, lib.trading_calendar, lib.research.coverage.covered_universe"` RUN in the worktree after the add):** `.claude/agents`, `lib`, `integrations`, `infra/logic`, `org/standards`, and the deliverables folders `0.9.0_WK_AMGT_HARVST~181` and `~178`.

- **COMPLETE (issuer, 2026-10-20 ~18:1xZ):** worker `~186`, branch merged `c356ff5849` (output and rows `25bef7b24d`, proof `ee7764cfeb` VALID rc 0). THE FINDING: `GOLD-CLOSURE entry=lib.research.harvest.publication_gold ... total_mb=138.86 limit_unzipped_mb=250 verdict=UNDER` (pyarrow 86.40, numpy 51.94); `GOLD-WRITE key_shape=amgt/harvest/gold/<table>/date=<date>/part-<run_stamp>.parquet add_only=yes full_snapshot=yes`; `GOLD-NEWEST chatter_daily=2026-10-08 chatter_event=2026-10-03 article_security_mention=2026-10-08 trading_days_behind=8`; `GOLD-ROSTER source=lib/research/harvest/universe_securities.py:build names=242` (the roster file `deliverables/0.9.0_WK_AMGT_HARVST~129/securities.universe.r75.json` has 242 entries; `covered_universe` has 95; 147 names of the newest chatter_daily object are outside it). **MY PREMISE WAS WRONG:** I expected OVER (and a Fargate task); the module alone is UNDER. **THE CAVEAT THAT KEEPS THE HOST OPEN:** this is the closure of the ENTRY MODULE alone. A rebuild driver also needs the trading-day gate (`lib/trading_calendar`, which `cn-4` measured pulling pandas 62.31 MB, numpy and the exchange-calendar family) and the roster loader (`universe_securities` imports `lib.research.metrics.chatter_axis`, unmeasured), so the DRIVER's closure and its WALL TIME (a Lambda stops at 15 minutes; a full-snapshot build over every silver part since 2026-01-01 is unmeasured) are not known: `co-5` measures both before any host is chosen. READ BY ME: the output lines in the branch, and `universe_securities.build` (line 1099) with its imports; I did NOT re-run the closure or the S3 listings.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>100</round>
<workstream>GOLD-SCHEDULE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
