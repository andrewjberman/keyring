# AMGT_CORPUS task order -- `CRPS-ao-1` -- ROUND 39: the daily refresh's same-day skip keys on the PULL date (row Z-S88)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ao-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<direct_act>true</direct_act>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the cell changes code only; the scheduled task's re-pin is the issuer's CRPS-ao-2.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the check runs against an in-memory S3 stub.
comp-adversary: RUN by the issuer at the cut -- skip_key_check.py build 0/1 (the same-day re-derive name is skipped) control 2/2.
EGRESS CLASS, declared: NONE. NO Bloomberg call, NO vendor call, NO S3 read or write.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 39.

## 1. THE CELL -- `CRPS-ao-1`

`cmd_refresh(dry_run=False)` in `integrations/bloomberg/research/model_block_pull.py` (about line 2227) is the daily refresh: it
re-pulls from Bloomberg, then re-derives, every registered name that has a model block. It skips a name when
`_model_block_latest_stamps(s3)` (about line 2198, the newest DERIVED stamp under `derived/model_block/<key>/`) starts with today's
UTC date (about line 2243). The intent (its docstring) is that the same run's `admit` and a same-day re-fire never pull twice.

The defect (row `AMGT_CORPUS-Z-S88`): a same-day RE-DERIVE also writes a today-dated derived stamp. On 2026-10-06 a re-derive at
03:20Z made the 13:00Z scheduled fire skip all 96 names and pull 0 ("refresh population registered 96 with_block 96
already_current 96 pulled 0 bloomberg_calls 0").

**Build, in `model_block_pull.py` only:**
1. The skip keys on the name's last PULL date: the newest stamp a pull landed for that name. A pull lands two things with the
   same stamp: the pull-log state object under `_state_pull_log_prefix(sec_key)` (about line 677) and the bronze refdata/histdata
   objects under `_bronze_prefix(request, sec_key)` (`_bronze_stamp_set`, about line 682). Read either one with ONE paginated
   prefix listing per population (as `_model_block_latest_stamps` does), never one call per name per file.
2. A name whose last pull is today (UTC) is still skipped, with the same `REFRESH SKIP: <key> already_current` line. A name
   re-derived today but last pulled on an earlier day is pulled. The summary line's shape and the rc contract do not change.
3. Update the docstring and the comment at the skip so they say "pulled today", and add an `AMENDMENT (CRPS-ao-1, round 39):`
   comment naming row Z-S88.
4. Write `integrations/bloomberg/research/tests/test_refresh_skip_key_round39.py`: offline, a stub S3, `cmd_refresh(dry_run=True)`:
   derived today + pulled yesterday -> pulled; derived today + pulled today -> skipped; both yesterday -> pulled.
5. `integrations/bloomberg/research/tests/test_model_block_round34.py` plants its "current" names through derived keys only
   (`_arrange`, about line 141). Amend the planting so a current name also carries a today pull stamp, with an
   `AMENDMENT (CRPS-ao-1, round 39):` comment. Change no assertion.

## 2. BOUNDS

1. NO Bloomberg call, NO vendor call, NO AWS call of any kind. Never run `refresh` or `admit` without `--dry-run`.
2. Only the files in `<paths>` change. In `model_block_pull.py`, change only `cmd_refresh` and the stamp helper it reads (a new
   helper is fine). Never edit `stage_pull`, `stage_derive`, `cmd_admit`, a field list or a key builder.
3. Write code with the Edit/Write tools, never a shell heredoc or `python -c`. ASCII only. Run python from your worktree root as
   `PYTHONPATH=<worktree root> python ...`.
4. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner
   2.0.0_SA_COO~X` and `surfaced_at` from `date -u +%FT%TZ` at filing.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_refresh_skip_key_round39.py
integrations/bloomberg/research/tests/test_model_block_round34.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-ao-1.skip-keys-on-the-pull-date.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ao-1.skip-keys-on-the-pull-date.md
</paths>

Read-only: the whole repository, in particular the issuer's check
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round39/skip_key_check.py` (never edit it). It stubs
`list_objects_v2` (Prefix, ContinuationToken) and `get_paginator("list_objects_v2")`; your listing must use one of those.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ao-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round39/skip_key_check.py"</invocation><expect>(?m)^skip build 1/1 control 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ao-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python -m pytest integrations/bloomberg/research/tests/test_refresh_skip_key_round39.py integrations/bloomberg/research/tests/test_model_block_round34.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^[0-9]+ passed(, [0-9]+ warnings?)? in [0-9.]+s$</expect></criterion>
</proof_of_spec>

- AC1 (the REAL `cmd_refresh`, dry run, stub S3): build -- a name re-derived today and pulled yesterday is pulled; control -- a
  name pulled today is skipped, a stale name is pulled.
- AC2: your new test and the amended round-34 refresh tests pass.

## 5. WHEN YOU ARE DONE

1. Run every `integrations/bloomberg/research/tests/` file whose name contains `model_block` or `refresh`. Every test passes.
2. Write the instance at the proof path, with its mutant control from the start. Then run `python .tools/proof-of-spec-check.py
   <instance> AC1,AC2 --governing-order <this order>` AFTER your final commit. It must return rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file, in the SAME commit as your
   instance.
4. Report ONCE: which stamp the skip now reads and how, every criterion's output line, the pytest summary lines, your commit hashes
   and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-38 analysis @`9619211bcf` ruling 6 + s.4 item 1 (CTO msg 30045). Base: skip build 0/1 control 2/2. The
served proof (re-pin, the BA plant, the 2026-10-07 13:00Z fire read) is the issuer's paired CRPS-ao-2.
<risk>LOCAL</risk>
<status>pending</status>
<round>39</round>
<slot>~1</slot>
<fabric>site-z</fabric>
