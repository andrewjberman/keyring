# AMGT_HARVST task order -- `HVST-co-3` -- ROUND 100, workstream DRIVER-BRANCHES: THE TWO BRANCHES THE STANDING DOSSIER FIRE HAS NOT YET HIT (A NON-TRADING DAY, AND A NAME WITH NO MODEL BLOCK FOR TODAY) ARE DRIVEN ON DEMAND IN DRY MODE AGAINST LIVE DATA (CTO round-99 analysis item 3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-co-3.the-two-unfired-branches-of-the-refresh-driver-are-driven-on-demand-in-dry-mode-against-live-data</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-co-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~187</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- the driver `lib/research/corpus/dossier_refresh.py` is run ONLY in its DRY mode (never `--write`), through its own `main(argv, now=...)`, reading the bucket `opal-data-harvest` through its `ReadOnlyClient` (it refuses `put`, `delete` and `copy` by name). Your own `list_objects_v2` calls on `amgt/harvest/gold/research_dossier/security_key=UNH_US_Equity/` (before and after, to prove nothing moved) go through `lib.research.harvest.store._default_client()`; never `put`, `delete`, `copy`, `sync` or a bare `aws` call. NO Bloomberg, NO model call. NO edit of any source file, NO edit outside `<paths>`; you DO NOT call the live gateway.
comp-adversary: RUN at L5 -- the adversary is a "skipped" read from a run that never reached the gate (print the driver's own `REFRESH-SKIPPED` line and the S3 request count of that call), a `now` that does not fall on the day you say (the driver uses the America/New_York date of `now`: print `run_local_date(now)`), a "no model block for today" that is really an empty pool or a wrong bucket (the positive control reads the same name on a real day), a dry run that wrote (compare the object listing before and after), a census line edited to match, and a control that cannot fail.
</preflight>

## 0. THE CELL

The standing refresh (a scheduled ECS task each Monday to Friday 10:00 America/New_York) has fired once, on a normal day. Two of the driver's branches have not run for real: (1) **a non-trading day**: `--require-trading-day` makes the driver print `REFRESH-SKIPPED not_a_trading_day` and exit 0 before it reads anything; (2) **a name whose model block has no entry for today**: the driver reports `no_today_model_block` for it and leaves its stored dossier untouched. The CTO wants both driven NOW, on demand, in dry mode against live data, so tomorrow's organic fire is a read and not a wait. This cell writes nothing to S3 and changes no source file.

## 1. THE BUILD (a read-only script; no product code)

Work in your worktree. Change only the files named in `<paths>`.
a. Read first: `lib/research/corpus/dossier_refresh.py` (`main(argv=None, now=None)` at its end, `run_local_date`, `run_names`, `census_line`, the status names and `ReadOnlyClient`), `lib/trading_calendar.py` (`is_trading_day`) and the driver's tests `lib/research/corpus/tests/test_dossier_refresh.py` if present. The driver takes its clock from the `now` argument of `main`; you inject it.
b. **Write `co3_branches.py`** in your deliverables folder and run it once in the FOREGROUND with `python -u`, stdout to `co3_branches.out` (open it with `newline="\n"`). It calls `dossier_refresh.main([...], now=<an aware UTC datetime>)` with stdout captured (`contextlib.redirect_stdout`), always in dry mode (never pass `--write`), and prints:
   1. `BRANCH-NONTRADING now=2026-10-24T14:00:00Z skipped=<yes|no> exit=<rc> s3_gets=<n> s3_puts=0` from `main(["--require-trading-day"], now=2026-10-24T14:00:00Z)` (a Saturday); `skipped=yes` only if the captured output holds the line `REFRESH-SKIPPED not_a_trading_day`; count the S3 requests the call made by wrapping `store._default_client` for the call (expect 0 gets) and print the captured driver line on its own `NOTE` line.
   2. `BRANCH-NOTODAY <the driver's own census line, verbatim>` from `main(["--only", "UNH_US_Equity", "--require-trading-day"], now=2026-11-02T14:00:00Z)` (a Monday, a trading day on which no model block exists yet); print `NOTE run_local_date=<date>` beside it. The issuer expects `no_today_model_block=1 written=0 errors=0 mode=dry-run`; if the driver reports another status for this name on that day (for example `no_new_model_block`), print the actual census line unchanged and file a row.
   3. `BRANCH-NOTODAY-STORED before_after_equal=<yes|no> objects=<n>`: list `amgt/harvest/gold/research_dossier/security_key=UNH_US_Equity/` (key, size, ETag of every object) before and after call 2, and compare the two lists.
c. **The controls (rule 22):** POSITIVE: the same name on a real day, `main(["--only", "UNH_US_Equity", "--require-trading-day"], now=2026-10-20T20:00:00Z)`, prints `CONTROL-POSITIVE now=2026-10-20T20:00:00Z only=UNH_US_Equity no_today_model_block=0 skipped=no` (take the zero from the census line, `skipped=no` from the absence of `REFRESH-SKIPPED`); NEGATIVE for the gate: `main(["--require-trading-day"], now=2026-10-20T20:00:00Z)` must NOT print `REFRESH-SKIPPED` but you must not run all 95 names: pass `--only UNH_US_Equity` and print `CONTROL-NEGATIVE now=2026-10-20T20:00:00Z require_trading_day skipped=no`.
d. The last line, exactly: `BRANCHES gets=<requests> bytes=<bytes>` (the total S3 requests and bytes of the calls that reached S3; zero for the skipped call).
e. File ONE surprise row if anything read differently from this face. A surprise is a row; keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~187/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-co-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~187/co3_branches.out</invocation><expect>(?ms)^BRANCH-NONTRADING now=2026-10-24T14:00:00Z skipped=yes exit=0 s3_gets=0 s3_puts=0$.*^BRANCH-NOTODAY REFRESH-CENSUS names=1 written=0 would_write=0 unchanged=0 no_new_model_block=0 no_today_model_block=1 skipped_allowed=0 skipped_guard=0 errors=0 mode=dry-run$.*^BRANCH-NOTODAY-STORED before_after_equal=yes objects=\d+$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-co-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~187/co3_branches.out</invocation><expect>(?ms)^CONTROL-POSITIVE now=2026-10-20T20:00:00Z only=UNH_US_Equity no_today_model_block=0 skipped=no$.*^CONTROL-NEGATIVE now=2026-10-20T20:00:00Z require_trading_day skipped=no$.*^BRANCHES gets=\d+ bytes=\d+$</expect></criterion>
</proof_of_spec>

- AC1 is the two branches driven (the skip before any read, and the no-today-block census with the stored dossier untouched). AC2 holds the controls (the same name on a real day does not hit either branch) and the totals. **If a line reads otherwise, DO NOT edit the expectation or the script to match: print the actual line, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-20 ~16:46Z):** both FAIL as expected (`cat` of a file that does not exist). If a base state differs, say so and do not weaken a pattern.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your first row id is `AMGT_HARVST-D1-W187-S1`. The channel file has MIXED line endings and is append-only: READ ITS TAIL for the id sequence, append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body AND run the gate against your row WITHOUT the override first.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~187/AMGT_HARVST.TO-HVST-co-3.the-two-unfired-branches-of-the-refresh-driver-are-driven-on-demand-in-dry-mode-against-live-data.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-co-3.the-two-unfired-branches-of-the-refresh-driver-are-driven-on-demand-in-dry-mode-against-live-data` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-co-3.the-two-unfired-branches-of-the-refresh-driver-are-driven-on-demand-in-dry-mode-against-live-data.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-99 analysis item 3 ("Tomorrow's organic fire is a read, not a wait"). Dates chosen by the issuer: Saturday 2026-10-24 (not a trading day), Monday 2026-11-02 (a trading day, 13 days ahead, so no model block can exist for it), Tuesday 2026-10-20 20:00Z (the real day the standing fire already wrote, for the controls). I did not run the driver at any of these clocks; the face's `main(argv, now=...)` signature is read from `dossier_refresh.py` line 499.
- Chain C of round 100 (its own worker `~187`: no dependency on another chain; disjoint write set). Slot ~187, worktree `C:/dev/wk-harvst-187`, branch `wk-AMGT_HARVST-187`. **Sparse set at provision (each named file CHECKED BY NAME, and `python -c "import lib.research.corpus.dossier_refresh"` RUN in the worktree after the add):** `.claude/agents`, `lib`, `integrations/bloomberg/research`, `infra/aws/ec2/opal-gateway/app`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922`, `infra/logic`, `org/standards`.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>100</round>
<workstream>DRIVER-BRANCHES</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
