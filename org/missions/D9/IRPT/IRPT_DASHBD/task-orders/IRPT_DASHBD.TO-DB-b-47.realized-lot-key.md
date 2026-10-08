# TO IRPT_DASHBD.TO-DB-b-47 -- E1: the realized-lot key measured on the 175 rows and fixed in the contracts and the stage; a true duplicate still refuses (FWD-4)

<to_id>IRPT_DASHBD.TO-DB-b-47</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~27</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>28</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 round-27 analysis @7fa28c7d6d (msg 1222) item E1 ("the 175 rows are read and the minimal distinguishing column set is printed, with the count unique under it (175 of 175); the contracts and the stage use that key; a planted true duplicate still refuses (control)") | **Decomp cell:** `DB-b-47`
(decomposition section 29) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-46 (merged @acb7066605).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-27`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~27/`.

**The cell (`DB-b-47`).** Round 27 (DB-b-46, record `deliverables/0.9.0_WK_IRPT_DASHBD~26/SIZING_S31.json` and `REALIZED_ID_REPEAT_COUNTS.json`) ran the extended reporting-gold handler (`infra/aws/lambda/investor-reporting/reporting-gold/handler.py`) over all 7,597 49F accounts for 2026-10-06. The lots stage (`data/assets/scripts/gold/irpt_reporting/account_activity_lots.py`) REFUSED in `realized_rows`: 87 realized lot ids repeat within the day's frame (175 rows, 36 accounts, 0 ids spanning accounts, 0 rows identical in every column), so they are distinct lots sharing an id. Its peak reached at least 2,759.5 MB against the served function's 2,048 MB. This cell fixes the key.

1. Read the 175 rows (the realized lot source for 2026-10-06, the 87 repeated ids; the round-27 helper
   `deliverables/0.9.0_WK_IRPT_DASHBD~26/realized_id_repeat_counts.py` finds them). Find the SMALLEST set of columns, beginning with the
   current key, under which all 175 are unique. Measure it; never guess. Write `LOT_KEY_E1.json`: `rows_read` 175, `key_columns`,
   `unique_under_key` 175, `minimality` [{dropped: <column>, unique: <count>}] for each key column (each count below 175), the columns
   you tried, and the 36 accounts' counts.
2. Use that key: the realized lot contract's `primary_key` (and the unrealized contract's, if the same id repeats there), and the
   producer's uniqueness check in `realized_rows`. KEEP the refusal for a true duplicate (identical in every column).
3. Tests in `tests/test_account_activity_lots.py`: one whose name contains `shared_id` (two distinct lots sharing an id are both kept),
   one whose name contains `true_duplicate` (a planted row identical in every column still refuses). Keep every other test passing.
   Write `LOT_KEY_E1.md`, COUNTS ONLY.

<criterion id="DB28-1-AC1" cell_refs="DB-b-47"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r28/p28_key_batch.py" . DB28-1-AC1</invocation><expect>DB28-1-AC1 PASS</expect></criterion>
`DB28-1-AC1` -- the minimal key measured: 175 of 175 unique, each key column necessary. Base: FAIL.

<criterion id="DB28-1-AC2" cell_refs="DB-b-47"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r28/p28_key_batch.py" . DB28-1-AC2</invocation><expect>DB28-1-AC2 PASS</expect></criterion>
`DB28-1-AC2` -- the contract and the stage use the key; shared ids kept, true duplicates refused. Base: FAIL.

<expected_criteria>DB28-1-AC1,DB28-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. `account_return_daily.py` is read, never edited.
- **AWS:** S3 reads only. No S3 write, no Lambda invoke, no deploy, no vendor call, no bun, no download of any package, script or program.
- **Refusal clause.** An S3 write, a deploy, a relaxed refusal for true duplicates, a memory or timeout change, or a client figure in a
  committed `.md` is a defect: stop and file a row.

<paths>
data/assets/scripts/gold/irpt_reporting/account_activity_lots.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_activity_lots.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~27/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/standards/IRPT_DASHBD_ACCOUNT_LOT_REALIZED_CONTRACT.json
org/standards/IRPT_DASHBD_ACCOUNT_LOT_UNREALIZED_DAILY_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-47.realized-lot-key.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 29 (round 28, workstream B), cell `DB-b-47`.
<owned_cells>DB-b-47</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB28-1-AC1, DB28-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~27/IRPT_DASHBD.TO-DB-b-47.realized-lot-key.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB28-1-AC1,DB28-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, what you changed, the numbers each criterion prints, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a key fix in a producer that serves nothing yet; no S3 write.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB28-1-AC1 and AC2 base FAIL (no record), dry-run at base 7fa28c7d6d 2026-10-08 ~07:3xZ.
lane: the <paths> block IS the grant.
</preflight>
