# TO IRPT_DASHBD.TO-DB-b-42 -- E2 part 2: can a served input to classify_and_sum carry a repeated index label? Read the served partitions; if it can, the function refuses with a named reason (row W22-S5) (FWD-4)

<to_id>IRPT_DASHBD.TO-DB-b-42</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~24</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-25 analysis @3543da2f4d item E2
criterion (2) ("a read of whether a served input can carry a repeated index label, over the served partitions with the count printed: if
it can, the function refuses with a named reason (a test); if it cannot, the read is the evidence") | **Decomp cell:** `DB-b-42`
(decomposition section 26) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-40 (merged @5ffd7b740d).

E2 criterion (1), the None-hardening test on pandas 2.2.3, is NOT in this order: no pandas 2.2.3 environment exists on dell2 (Python 3.14
with pandas 3.0.6 only) and nothing is downloaded. It is cut as its own order when the environment arrives from the laptop.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-24`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~24/`.

**The cell (`DB-b-42`).** `classify_and_sum` in the served producer
`data/assets/scripts/gold/irpt_reporting/account_return_daily.py` raises `ValueError` on a frame with a repeated index label (row
IRPT_DASHBD-W22-S5; the round-25 hardening did not change that). Find out whether a SERVED input can ever give it one.

1. Read how the served producer builds the frame it passes to `classify_and_sum` (the flow rows of a day, from the custodian's
   transaction source declared in `data/assets/scripts/gold/irpt_reporting/sources.json`), and which index that frame carries.
2. Over the served partitions of that source for the 49 Financial firm (S3 reads only; the bucket and prefix come from the declaration,
   never typed), build each day's frame exactly as the producer does, for every trading day from 2026-01-02 through 2026-10-05
   (`lib/trading_calendar.py`), and count the frames whose index has a repeated label. Write `REPEATED_INDEX_E2.json`:
   `partitions_read`, `frames_read`, `repeated_label_frames`, up to 20 example `{day, account_id, label, count}`, the index's source
   (column or construction), and `verdict` `CAN` when any frame repeats a label, else `CANNOT`.
3. On `CAN`: make `classify_and_sum` refuse such a frame with a `ValueError` whose message names the cause (repeated index label, with
   the first label), BEFORE any other work, changing nothing else; add a test whose name contains `repeated_index` to
   `data/assets/scripts/gold/irpt_reporting/tests/test_account_return_daily_none.py`. Its outputs on frames without a repeated label must
   not move. On `CANNOT`: edit no code; the read is the evidence.
4. Write `REPEATED_INDEX_E2.md`, COUNTS ONLY.

<criterion id="DB26-2-AC1" cell_refs="DB-b-42"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r26/p26_release.py" . DB26-2-AC1</invocation><expect>DB26-2-AC1 PASS</expect></criterion>
`DB26-2-AC1` -- the served partitions read with the count printed; the verdict agrees with the count; on CAN, the named refusal's test
passes. Base: FAIL.

<expected_criteria>DB26-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** S3 reads only. No write, no deploy, no vendor call, no bun, no download of any package, script or program.
- **Refusal clause.** An S3 write, a deploy, a change to `classify_and_sum`'s output on a frame without a repeated label, or a client
  figure in a committed `.md` is a defect: stop and file a row.

<paths>
data/assets/scripts/gold/irpt_reporting/account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_daily_none.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~24/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-42.repeated-index-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 26 (round 26, workstream B), cell `DB-b-42`.
<owned_cells>DB-b-42</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB26-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~24/IRPT_DASHBD.TO-DB-b-42.repeated-index-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB26-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, the criterion's last line, the counts, the verdict, any code change, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read over served sources; a refusal, if any, is a source-only change to the served producer, shipped by a later release under its own halves; no S3 write.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB26-2-AC1 base FAIL (no record), dry-run at base c246d6a180 2026-10-07 ~20:5xZ.
lane: the <paths> block IS the grant.
</preflight>
