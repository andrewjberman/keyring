# TO MDPF_SECCLASS.TO-SC-e88 -- round 20 SC-e-88: trace C_06's firm-daily total-vs-class-sum gap to its cause (a read)

<to_id>MDPF_SECCLASS.TO-SC-e88</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~78</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-88` (`decompositions/MDPF_SECCLASS_DECOMP_R20.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-88`, row MDPF_SECCLASS-D1-S27. This cell is a READ: it names a cause and writes one record. It fixes nothing.

C_06 (`data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py`) publishes a firm-daily snapshot at
`s3://opal-data-bd/gold/views/mix_daily_summary.json`, key `firm`, one entry per date: `{equity, fixed_income, alternatives, commodities,
structured, cash, unclassified, other, total}` in dollars. For the newest three dates the snapshot's `total` differs from the sum of its
class values:

| date | total | sum of classes | gap (total minus sum) |
|---|---|---|---|
| 2026-10-06 | 2,019,548,567.60 | 2,019,548,572.31 | -4.71 |
| 2026-10-07 | 2,013,270,405.35 | 2,013,270,277.29 | +128.06 |
| 2026-10-08 | 2,014,814,865.45 | 2,014,814,994.02 | -128.57 |

About 6e-8 of $2.0B, with a sign that flips day to day. D_04's `Unclassified` line is `total` minus the six canonical classes, so it
carries that gap by design (CTO ADDENDUM 1); the question here is where the gap comes from.

**Battery finding (the issuer's reading of the code; confirm or refute it, do not assume it).** In `process_date` (:497-624), each
relationship's mix share is `mix[ac] = round(class_mv / total_mv, 6)` (:595), and the firm snapshot accumulates
`firm[date][ac] += data['mix'][ac] * total_mv` per relationship and `firm[date]['total'] += total_mv` (:737-743 incremental, :857-863
full). So the firm class sum is the sum of ROUNDED SHARES times each relationship's dollars, while `total` is the exact dollar sum.
Hypothesis H1: the gap equals the sum over relationships of `total_mv * (1 - sum of that relationship's rounded shares)`, a rounding
residual that is large on a few big relationships and changes sign day to day. A relationship with `total_mv <= 0` is skipped (:582) from
both sides. The alternative, H2, is a MEMBERSHIP difference: some position or relationship counted in `total` and in no class (or the
reverse). The record must say which, with numbers.

**How to recompute (read-only; nothing is written).** C_06's `process_date(key, date_str, prices_grouped, acct_rel_dict, ap_last_seen,
...)` runs in process and returns `{relationship_id: {'mix': {...}, 'conc': [...], 'total_mv': ...}}` without writing. Existing read-only
examples that load the module by path, build its static tables and call `process_date` on a canonical holdings partition are
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/bd_mix_multi_asset_check.py` and `cot_mix_multi_asset_check.py` (read
how they load C_06 and its static tables; the BD partition keys are `gold/canonical/holdings/<date>.parquet` in `opal-data-bd`). For each
of the three dates: recompute the per-relationship results, then compute the firm total and class sum the way :737-743 does, the
published-gap comparison, and `sum(total_mv * (1 - sum(mix.values())))` (the rounding residual). Rank relationships by absolute
residual and keep only each one's `total_mv` and `residual`, never its id.

### THE RECORD

Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/C06_TOTAL_GAP_TRACE_20261011.json` with exactly this shape (the checker
reads these field names):

```
{"method": "<one sentence on what you ran>",
 "cause": "<one or two sentences naming the cause with the numbers that show it>",
 "membership_differs": false,
 "positions": [],
 "dates": {"2026-10-06": {"published_total": 0.0, "published_class_sum": 0.0, "published_gap": 0.0,
                          "recomputed_total": 0.0, "recomputed_class_sum": 0.0, "recomputed_gap": 0.0,
                          "relationships": 0, "share_rounding_residual_sum": 0.0,
                          "top_residuals": [{"total_mv": 0.0, "residual": 0.0}]},
           "2026-10-07": {...}, "2026-10-08": {...}}}
```
- `published_*` come from the served snapshot as printed above; `recomputed_*` from your in-process run.
- `share_rounding_residual_sum` is `sum(total_mv * (1 - sum(mix.values())))` over the relationships; `top_residuals` holds at most five.
- If H1 holds, `share_rounding_residual_sum` equals `recomputed_gap` within $0.05 and `cause` says rounding of the per-relationship
  shares at 6 decimals, citing :595 and :737-743. If instead a membership difference exists, set `membership_differs` true and list each
  differing position in `positions` as `{ticker, asset_name, market_value}` (security level only).
- **No relationship id, account id or client name goes in the record, in any field or string.** The checker refuses keys named like
  rid, relationship, account, client or household and any value shaped like `z` plus 8 digits or an 8-digit number.
- If the recomputed gap does not match the published gap for a date (the served snapshot may have been written from a different
  partition set), say so in `cause`, keep the numbers, and file a surprise row; the criterion then fails and that is the honest result.

### ACCEPTANCE

<criterion id="SC20-e88-AC1" cell_refs="SC-e-88"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R20_CHECKS/c06_gap_record_check.py gap</invocation><expect>C06-GAP ok=True</expect></criterion>
`SC20-e88-AC1` -- the record's three published gaps equal the served ones; at least one date reproduces from today's partitions (its
recomputed total equals the published total within $0.05) with its recomputed gap within $0.05 and every listed residual inside the
6-decimal rounding bound; a date that does not reproduce is drift, not a failure; a cause is shown. (Amended, see AMENDMENT 1.)
<criterion id="SC20-e88-AC2" cell_refs="SC-e-88"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R20_CHECKS/c06_gap_record_check.py scope</invocation><expect>C06-SCOPE ok=True</expect></criterion>
`SC20-e88-AC2` -- the record holds no relationship id, account id or client name.

<expected_criteria>SC20-e88-AC1,SC20-e88-AC2</expected_criteria>

Dry-run at the base (dell1 box/dell1, 2026-10-11 ~03:3xZ):
- SC20-e88-AC1: FAIL, as expected (`C06-GAP ok=False dates=0 ... basis=none`, the record is absent).
- SC20-e88-AC2: FAIL, as expected (`C06-SCOPE ok=False bad=NA (no record)`).
- Positive and negative controls run on a synthetic record before the cut: a record built from the served numbers reads `C06-GAP ok=True`
  and `C06-SCOPE ok=True`; a record carrying a `relationship_id` key reads `C06-SCOPE ok=False`; a record with one recomputed gap off by
  $3 reads `C06-GAP ok=False`.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding (your recompute script, its
  output) goes under `.scratch/`, uncommitted; keep any client-level intermediate there and never commit it.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY** (get, list, head, scan): no write to any table or bucket, no deploy, no invoke, no model call. Never push.
- **Never edit** C_06 or any gold script; this cell writes the one record and nothing else.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W78-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken the record to pass.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/C06_TOTAL_GAP_TRACE_20261011.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R20.md</decomp_doc> (round 20), cell `SC-e-88`.
<owned_cells>SC-e-88</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC20-e88-AC1, SC20-e88-AC2. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~78/MDPF_SECCLASS.TO-SC-e88.c06-total-vs-class-sum-trace.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC20-e88-AC1,SC20-e88-AC2`.
</proof_of_spec>

**REPORT:** the method in two lines, the cause with its numbers per date, whether H1 held, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read; no producer changes and no run of a gold script that writes.
comp-iam: DECLARED-NOT-APPLICABLE no grant change (read-only get/list under the seat's role).
comp-adversary: RUN -- a recompute that matches the gap by construction (the residual must come from the per-relationship shares, not from the published total); a cause stated without numbers (the checker requires the residual sum within $0.05 of the gap or a non-empty positions list); client identifiers leaking into the record (AC2)
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-19 analysis section 3 item 2 (msg 3419); row D1-S27; DECOMP_R20.

## AMENDMENT 1 (2.0.0_SA_COO~M1, 2026-10-11 ~04:0xZ) -- AC1 reads the dates that reproduce

The cut assumed all three served firm-daily snapshots reproduce from today's canonical holdings partitions. Worker ~78 measured that
2026-10-08 reproduces to the cent and that 2026-10-06 and 2026-10-07 do not (their partitions were rewritten after the snapshot; row
`MDPF_SECCLASS-D1-W78-S1`). That is a premise defect in the cut, not in the worker's record. AC1's checker
(`R20_CHECKS/c06_gap_record_check.py gap`) now grades a date that reproduces on its gap AND on the rounding bound (each listed residual
at most `total_mv * 4.5e-6`, which out-of-class mass would break by orders of magnitude), counts a non-reproducing date as drift, and
needs at least one reproducing date. Worker ~78's record is unchanged by this amendment. Record text that says the criterion is left to
fail predates it. AC2 is unchanged. Gate limb: none graded this modification (an issuer amendment of its own criterion, no
`<placeholders>`, not a newly-added order).
