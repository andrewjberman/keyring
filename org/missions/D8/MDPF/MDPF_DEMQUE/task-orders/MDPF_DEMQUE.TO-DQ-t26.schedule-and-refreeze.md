# TO MDPF_DEMQUE.TO-DQ-t26 -- round 8 DQ-t-26: the quote counts only days a drawer fires, and a frozen quote is re-frozen beside the old one
<to_id>MDPF_DEMQUE.TO-DQ-t26</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~21</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-26` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 8 -- CUT) |
**outcome_ref:** FWD-4 | **depends_on:** DQ-t-25 (the same worker, second in its queue: `bbg_quote.py` carries t-25's tier rule when you start)

---

## WORKER FACE

### THE CELL

`DQ-t-26` (FWD-3, FWD-4; CTO round-7 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round7.md` R2, read it; row
`MDPF_DEMQUE-D1-C-S17`). Two facts. (1) A quote must promise only days a drawer will draw: today the walk counts every non-trading day, and a
STANDING drawer (DQ-t-27, site Z) will fire on exactly those days. (2) The TR request's frozen quote
(`org/missions/D8/MDPF/MDPF_DEMQUE/requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.quote.json`, finish 2026-10-13, frozen under the retired weekday rule) must
be RE-FROZEN under the rule in force, and the old one KEPT. This order builds the tools; the re-freeze of the real file is the issuer's act.

**Build** (all under `data/mdpf/scripts/demque/`):
1. NEW `drawer_schedule.py`: `is_fire_day(d)` is True on every NON-trading day (`lib/trading_calendar.py` `is_trading_day`; put the repo root on
   `sys.path` as `bbg_quote._calendar()` does); `fire_days(start, end)` returns the ISO dates `start..end` inclusive for which it is True,
   ascending (ValueError when `end < start`); `HORIZON_DAYS = 14`; `FIRE_RULE` a constant naming the rule ("one fire on every non-trading day,
   drawing open backfill requests in rank order up to the measured ceiling"). CLI `--from YYYY-MM-DD --days N` prints one JSON line
   `{"fires": [...]}`.
2. `bbg_quote.py`: `quote(request, allowance, drawn_today, today, producer_path=None, fire_days=None)`. `fire_days` is None (the standing
   schedule: `drawer_schedule.is_fire_day`) or an iterable of ISO dates. In the backfill non-trading walk (`_finish_non_trading`) a day adds the
   ceiling only if it is a fire day, and `allowance_today` is 0 on a day that is not one. With the default the output is byte-for-byte what
   DQ-t-25 produced. `HISTORY_BASIS` gains the clause "; counted only on days a scheduled drawer fires (drawer_schedule.py)".
3. NEW `refreeze.py`: `refreeze(request_id, requests_dir, as_of, reason, allowance_path=None, now=None, frozen_by=None) -> dict`. It reads
   `<id>.json` (the request) and `<id>.quote.json` (the frozen quote) from `requests_dir`. If the frozen quote already carries `supersedes` it
   changes nothing and returns `{"status": "ALREADY_REFROZEN"}`. Otherwise:
   - it copies the old quote's content, plus `superseded_reason` (the `reason`), `superseded_on` (`now`'s date) and `superseded_by`
     (`<id>.quote.json`), to `<id>.quote.superseded-<YYYY-MM-DD>.json` (when that name exists it uses `-2`, `-3`; never overwrites);
   - it quotes the request with `bbg_quote.quote(request, allowance, 0, as_of)` and writes `<id>.quote.json` with `request_id`, `channel`, `cells`,
     `finish_date`, `finish_date_claim`, `claim` (= `finish_date_claim`), `basis` (the quote's basis + "; re-frozen under the rule in force: " +
     reason), `quoted_as_of` (`as_of`), `refrozen_at` (`now` ISO), `frozen_by`, and `supersedes` (the superseded file's name).
   `as_of` is the day the original quote was frozen, so the two quotes differ only by the rule. CLI `--request-id ID --requests-dir DIR --as-of D
   --reason TEXT [--frozen-by S] [--now ISO]` (default `frozen_by` the `OPAL_AGENT_SERIAL` env var, `now` the UTC clock; `allowance_path`
   defaults to `bbg_quote.ALLOWANCE_PATH`) prints the result as one JSON line.
4. `quote_vs_actual.py`: `read()` gains `superseded`, the list (name-sorted) of `{"finish_date", "superseded_on", "reason", "file"}` from every
   `<id>.quote.superseded-*.json` in the requests folder (`[]` when none). The verdict logic is unchanged: it grades `<id>.quote.json` only.
   `--all` still globs `*.quote.json` and must not read a superseded file.
5. NEW `test_demque_refreeze.py` (pytest; `tmp_path`, no network; stub allowance written to a file) with exactly these names:
   `test_quote_counts_only_scheduled_non_trading_days` (a 150-cell history request, tier 4, ceiling 100 `measured`, quoted Friday 2026-10-09:
   the default schedule finishes 2026-10-11; with `fire_days` = `{"2026-10-10", "2026-10-17", "2026-10-18"}`, which omits Sunday 2026-10-11, it
   finishes 2026-10-17; and `allowance_today` is 0 on Sunday 2026-10-11 under that set), `test_refreeze_writes_beside_and_keeps_the_superseded_quote` (new quote has `supersedes`, old file kept with its
   reason and original `finish_date`; a second call returns ALREADY_REFROZEN and writes nothing) and
   `test_quote_vs_actual_grades_the_refrozen_quote_and_prints_both` (verdict from the new finish; `superseded` lists the old finish).

### ACCEPTANCE

<criterion id="DQ8-t26-AC1" cell_refs="DQ-t-26"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R8_CHECKS/dq_t26_tests.py</invocation><expect>RF-OK</expect></criterion>
<criterion id="DQ8-t26-AC2" cell_refs="DQ-t-26"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R8_CHECKS/dq_t26_real.py</invocation><expect>REFRZ-OK</expect></criterion>
`DQ8-t26-AC1` -- the three named tests. `DQ8-t26-AC2` -- the REAL TR request re-frozen in a scratch copy of the requests folder (the real folder is
untouched): new finish 2026-10-17, the 2026-10-13 quote kept with "rule changed, round 6 R1", `quote_vs_actual` on 2026-10-11 reads OPEN against
2026-10-17 with 5,858 drawn and prints the superseded finish.

<expected_criteria>DQ8-t26-AC1,DQ8-t26-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `RF-BAD no file ...`, `REFRZ-BAD no file ...refreeze.py`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **You never write the real requests folder.** Tests and AC2 use scratch copies. The real re-freeze is the issuer's act after the merge.
- **No AWS write, no Bloomberg call, no deploy.**
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W21-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/drawer_schedule.py
data/mdpf/scripts/demque/refreeze.py
data/mdpf/scripts/demque/bbg_quote.py
data/mdpf/scripts/demque/quote_vs_actual.py
data/mdpf/scripts/demque/test_demque_refreeze.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 8), cell `DQ-t-26`.
<owned_cells>DQ-t-26</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ8-t26-AC1, DQ8-t26-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~21/MDPF_DEMQUE.TO-DQ-t26.schedule-and-refreeze.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ8-t26-AC1,DQ8-t26-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the re-frozen and superseded quotes verbatim, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is registered here; `drawer_schedule.py` is a calendar function the site-Z order (DQ-t-27) registers a task against.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE LOCAL quote and record tools over scratch files.
risk: LOCAL -- code, tests and records.
direct_act: false -- a worker order.
</preflight>

Source: CTO round-7 analysis @f5553ca3d5 R2; row D1-C-S17 (REMEDIATION_v6); decomposition round 8.
