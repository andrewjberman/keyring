# TO MDPF_DEMQUE.TO-DQ-t45 -- round 9 DQ-t-45: the Yahoo side of the queue refuses an undeclared or over-window request, and the standing extension declares itself
<to_id>MDPF_DEMQUE.TO-DQ-t45</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~38</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>YCLASS</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-45` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 11) |
**outcome_ref:** C-QUOTE, C-YAHOO, C-PRICES, FWD-4 | **depends_on:** DQ-t-44 (merged @900406e221)

---

## WORKER FACE

### THE CELL

Law, Andrew-direct 2026-10-13 (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_141xZ_BACKFILL_FLOOR_2012_AND_EARLIEST_CLIENT_RECORD.md`, read it
with ADDENDUM 1 and 2): every queue request DECLARES its need class and window start; the queue REFUSES an undeclared request, a start before 2012-01-01, or a
start before the declared window; a non-client need takes 365 days back from its need date; never trimmed silently. DQ-t-44 landed this on the Bloomberg side
(`bbg_quote.py` `_validate`, `--check-declared`; read it first and reuse its rule, do not copy it). **This cell lands the same rule on the Yahoo side.** It makes no
vendor call and writes no store.

**Build** (in `data/mdpf/scripts/demque/demand_queue.py`, `extend_frontier.py` and a NEW test file):
1. **Declarations and refusal in `demand_queue.validate`.** A Yahoo request carries `need_class` (`"client"` or `"non_client"`), `window_start` (ISO date) and, for
   `non_client`, `need_date` (ISO). `validate` raises `ValueError`, naming the request id and the rule, when: `need_class` is missing or not one of the two;
   `window_start` is missing; `window_start` or the request's `start` is before 2012-01-01; the request's `start` is before its `window_start`; `non_client` and
   `window_start` is more than 365 days before `need_date`. It never trims. Use the same wording stem as `bbg_quote` so one record reads both.
2. **`demand_queue.py --check-declared DIR`** (read only): over every `*.json` in DIR with a `securities` list and no Bloomberg vendor, run `validate`; print ONE JSON
   line `{"checked": N, "refused": [{"request_id", "why"}], "accepted": N}`.
3. **The standing extension declares itself.** `extend_frontier._request` adds `need_class` `"client"` and `window_start` = the earliest `start` among its
   securities' windows (never before 2012-01-01); `--plan` prints both as top-level keys `need_class` and `window_start` beside `frontier`. Nothing else in the plan's
   output changes.
4. **Existing request files are already declared** by the issuer (the six Yahoo requests in the repo and the device queue carry `need_class` and `window_start`);
   you do not edit any `requests/*.json`.
5. NEW `test_demque_yahoo_need_class.py` (pytest; stubs, no network, no S3) with exactly these names:
   `test_a_yahoo_request_without_a_declared_need_class_or_window_start_is_refused_at_validate`,
   `test_a_yahoo_window_before_2012_or_a_security_start_before_the_declared_window_start_is_refused_never_trimmed`,
   `test_the_standing_extension_request_declares_client_and_a_window_start_on_or_after_the_floor`.
   Existing demque test files that build a stub Yahoo request and now fail the refusal may take the declarations in that stub and NOTHING else (the grant names
   `test_demque_*.py` for exactly that): the failing assertion, not a rewrite.

### ACCEPTANCE

<criterion id="DQ9-t45-AC1" cell_refs="DQ-t-45"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t45_tests.py</invocation><expect>YCLASS-OK</expect></criterion>
<criterion id="DQ9-t45-AC2" cell_refs="DQ-t-45"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t45_real.py</invocation><expect>YCLASS-REAL-OK</expect></criterion>
`DQ9-t45-AC1` -- the three named tests. `DQ9-t45-AC2` -- on the REAL repo requests and the device queue: no Yahoo request is refused, and the standing extension's plan
declares client from a window start on or after 2012-01-01. Report the whole folder `pytest data/mdpf/scripts/demque` once (156 passed at the t-44 merge, plus these 3).

<expected_criteria>DQ9-t45-AC1,DQ9-t45-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `YCLASS-BAD no file ...`; `demand_queue.py: error: unrecognized arguments: --check-declared ...`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: no Yahoo call, no Bloomberg call, no write to S3, the ledger, the queue directory or any pacer state; never run `extend_frontier.py --apply`,
  `daily_draw.py` or `run_daily_draw.sh`; no AWS write, no deploy, no timer.** The scheduled 22:30 ET draw runs from the shared tree: your change must keep every
  currently queued request VALID (AC2 arm 1 proves it).
- **Account ids never enter a committed file.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W38-S<k>`, `fabric`
  `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file below, and do not weaken a check or the rule. Rows are
  APPEND-ONLY. Merge `box/dell1` into your branch (a merge, never a rebase) before you append rows.

<paths>
data/mdpf/scripts/demque/demand_queue.py
data/mdpf/scripts/demque/extend_frontier.py
data/mdpf/scripts/demque/test_demque_yahoo_need_class.py
data/mdpf/scripts/demque/test_demque_*.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-45`.
<owned_cells>DQ-t-45</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t45-AC1, DQ9-t45-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~38/MDPF_DEMQUE.TO-DQ-t45.yahoo-side-need-class-refusal.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t45-AC1,DQ9-t45-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, each real-check arm's line verbatim, which existing tests took a stub declaration and why, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed; the nightly draw runs the same task from the merged code.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE a validation rule and a printed declaration; nothing draws or serves.
risk: LOCAL -- code and tests. The refusal could stop a nightly draw if a queued request were undeclared; AC2 arm 1 and the issuer's pre-declared queue copies guard that.
direct_act: false -- a worker order.
</preflight>

Source: Andrew-direct 2026-10-13 and addenda (CTO msgs 4881, 4884, 4889); DQ-t-44 merged @900406e221; decomposition round 9.
