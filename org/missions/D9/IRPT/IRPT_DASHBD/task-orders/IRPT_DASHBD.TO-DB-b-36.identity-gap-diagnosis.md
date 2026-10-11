# TO IRPT_DASHBD.TO-DB-b-36 -- E1: diagnose the activity-identity gaps of round 23 (row W20-S2) -- the ~1.1M account term by term, a census of transaction types, and the 39 gaps classed (FWD-4)

<to_id>IRPT_DASHBD.TO-DB-b-36</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~21</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>24</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-23 analysis @9f285400cf item E1 ("Diagnose the
identity gaps (W20-S2). Read the ~1.1M account's window term by term, then classify the other 38"; a census of unsigned transaction types,
because "an unsigned type moves nothing", the D2-S24 defect class) | **Decomp cell:** `DB-b-36` (decomposition section 24) |
**outcome_ref:** FWD-4 | **depends_on:** DB-b-35 (merged @a8df9a5880).

THIS CELL DIAGNOSES. It edits no producer; the fix is DB-b-37, after this cell drains.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-21`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/`.

**The cell (`DB-b-36`).** Round 23 built `account_activity_daily` and the lot tables with
`data/assets/scripts/gold/irpt_reporting/account_activity_lots.py`. Its record
`deliverables/0.9.0_WK_IRPT_DASHBD~20/ACTIVITY_LOTS_LOCAL_RUN.json` carries `window_identity`: 91 accounts graded over 2026-09-01..
2026-10-05; 52 tie within one cent; 39 do not (`accounts_above_one_cent`, each with its `gap`). The identity is beginning_value +
contributions - withdrawals + realized + unrealized_change + income = ending_value. The largest gap is account `acct#f0faa651`, about
1,108,912.92. Find out why, without changing the producer:

1. **The largest gap, term by term.** For `acct#f0faa651` over the same window, recompute each of the seven terms from the producer's own
   sources (`s3://opal-data-assets/schwab/08335338/silver/`: `fact_trn`, `fact_rld`, `fact_uln`/`fact_ult`, `dim_position`,
   `dim_balance`), each with the source rows it summed and their count. Name the cause and the rows that show it.
2. **A census of transaction types** in the 91 accounts' window source (`fact_trn`): every type, its row count, its sign as the activity
   rule reads it (`+`, `-`, or `UNSIGNED` when the rule assigns none), the term it maps to (or null), and whether it moves value. ADVI_COTBKF
   met the same class today: a type the rule does not sign moves nothing (row D2-S24, another firm's data). List every type that moves value
   and maps to no term.
3. **The 39 gaps classed.** TOLERANCE, STATED HERE BEFORE THE RUN: **0.05 per account-window** (rounding of daily figures over 24 trading
   days). A gap with |gap| <= 0.05 is `ROUNDING`; any other is `MISSING-TERM` with the type or cause that explains it. Do not change the
   tolerance after seeing the gaps.

Write `GAP_DIAGNOSIS_E1.json` with: `largest_gap_window` `{account_id, window, terms: {<term>: {value, row_count, source_rows}}, cause,
evidence_rows}`; `type_census` `[{type, row_count, sign, maps_to_term, moves_value}]` and `unmapped_value_movers` `[types]`;
`gap_classes` `{tolerance: 0.05, rows: [{account_id, gap, class, cause}]}`. `source_rows` may be row keys or row ids, enough to find the
rows again. Write `GAP_DIAGNOSIS_E1.md`, COUNTS ONLY (no client figure, no account balance). A helper script, if you write one, goes in
your folder.

<criterion id="DB24-1-AC1" cell_refs="DB-b-36"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r24/p24_identity.py" . DB24-1-AC1</invocation><expect>DB24-1-AC1 PASS</expect></criterion>
`DB24-1-AC1` -- the largest-gap window printed term by term, each term with its source rows and count, the cause named with its rows.
Base: FAIL.

<criterion id="DB24-1-AC2" cell_refs="DB-b-36"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r24/p24_identity.py" . DB24-1-AC2</invocation><expect>DB24-1-AC2 PASS</expect></criterion>
`DB24-1-AC2` -- every transaction type censused with count, sign, mapped term and whether it moves value; the unmapped movers listed.
Base: FAIL.

<criterion id="DB24-1-AC3" cell_refs="DB-b-36"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r24/p24_identity.py" . DB24-1-AC3</invocation><expect>DB24-1-AC3 PASS</expect></criterion>
`DB24-1-AC3` -- the 39 gaps classed ROUNDING (within 0.05) or MISSING-TERM (with its cause), counts printed. Base: FAIL.

<expected_criteria>DB24-1-AC1,DB24-1-AC2,DB24-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. The producer `account_activity_lots.py` and every served producer are read, never edited.
- **AWS:** S3 reads only. No write, no vendor call, no bun, no download.
- **Refusal clause.** An edit to a producer, a tolerance changed after the run, an S3 write, or a client figure in a committed `.md` is a
  defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-36.identity-gap-diagnosis.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 24 (round 24, workstream B), cell `DB-b-36`.
<owned_cells>DB-b-36</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB24-1-AC1, DB24-1-AC2, DB24-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~21/IRPT_DASHBD.TO-DB-b-36.identity-gap-diagnosis.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB24-1-AC1,DB24-1-AC2,DB24-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the cause of the largest gap, the unmapped value-moving types, the class counts,
and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a diagnosis over landed silver; no producer edited; no S3 write.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB24-1-AC1, AC2 and AC3 base FAIL (no record), dry-run at base c2b4cbb412 2026-10-07 ~15:1xZ; the denominator read from round 23's record: 91 graded, 39 above one cent, largest acct#f0faa651 (1,108,912.92), 30 of the 39 within 0.05.
lane: the <paths> block IS the grant.
</preflight>
