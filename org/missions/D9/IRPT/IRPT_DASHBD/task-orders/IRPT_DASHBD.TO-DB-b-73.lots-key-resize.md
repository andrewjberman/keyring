# TO IRPT_DASHBD.TO-DB-b-73 -- E1: the realized-lot key -- name what differs between the 2026-10-07 repeat pairs, extend the key by the column that separates them, then re-size the lots stage over the population on the pandas 2.2.3 kit for 2026-10-06 and 2026-10-07 with 0 refusals

<to_id>IRPT_DASHBD.TO-DB-b-73</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~50</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>37</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-36 ADDENDUM 5 (on ADJUDICATION_v21 @37daf4f637; PRD v0.9 @e8f96f579c), enrichment item E1 | **Decomp cell:** `DB-b-73` (decomposition section 39) | **outcome_ref:** FWD-4 | **depends_on:** none (the release was rolled back @c212a8be27).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-50`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~50/`.

**The cell (`DB-b-73`).** Round 36's release sizing read failed. The deployed lots producer refused 2026-10-07 at batch 2 of 8 with
`REFUSED: realized lot id ... repeats with the same closing date and quantity: the key is not unique` (row D2-W47-S5). That refusal is raised by
`realized_rows()` at `C:/dev/wk-irpt-dashbd-50/data/assets/scripts/gold/irpt_reporting/account_activity_lots.py` lines ~308-326. The
realized key is `(firm, account_id, business_date, lot_id, quantity)` (`org/standards/IRPT_DASHBD_ACCOUNT_LOT_REALIZED_CONTRACT.json`
`primary_key`; the producer's `PRIMARY_KEYS`, line ~178). The release was rolled back, and this cell is its first repair.

1. **Read the repeats.** Read the custodian realized-lot partition for 2026-10-07 through the producer's own declaration (`sources.json`
   `lot_source`, addresses by `lib/opal_naming.py`), over every population account. List each pair of rows that shares the whole key, and
   name every column whose value differs within the pair. Record `repeat_census` {day, pairs, differing_columns}. Use hashed account keys only.
2. **Extend the key** by the smallest set of source columns that separates every pair. A real second closing event (e.g. a distinct
   closing trade or order id) is kept as its own row. Never collapse two real events, and never drop a row to make the key unique.
   - Change the producer's `PRIMARY_KEYS` and the refusal, so a true duplicate still refuses by name.
   - Change the contract's `primary_key` to match.
   - Add one test that builds a repeat pair and passes under the new key, plus the identical-row case that still refuses.
   - Record `new_key` and `tests` {passed, failed, new_test "<file>::<function>"}.
3. **Re-size on the kit.** **The kit (pandas 2.2.3, the served runtime).** Its path is in `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/relay/KIT_PATH_PY312_PANDAS223.txt`. Build a venv in
`.scratch/` with `C:/Users/Test/AppData/Local/Programs/Python/Python312/python.exe`, then run `pip install --no-index --find-links <kit>
-r <pin file>`. Side-load boto3, psutil and pytest from dell2's own site-packages through a `.pth` file, offline (rows W44-S1 and W46-S2).
The runner is round 30's `deliverables/0.9.0_WK_IRPT_DASHBD~31/lots_750_run.py` (default batch). Count `refusals` as the REFUSED,
LOTS_SKIPPED and CLASS_SKIPPED lines in its log. Run the extended handler `--local` over the population for 2026-10-06 and 2026-10-07. Record
   `kit_runs[<day>]` {accounts, refusals, lots_rows, peak_mb, total_s}, and `runtime` printed from the kit process.

Record everything in `LOTS_KEY_E1.json` in your folder.

<criterion id="DB37-1-AC1" cell_refs="DB-b-73"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r37/p37_round37.py" . DB37-1-AC1</invocation><expect>DB37-1-AC1 PASS</expect></criterion>
`DB37-1-AC1` -- the 2026-10-07 repeat pairs counted with the columns that differ, and the key extended to separate them, the contract equal. Base: FAIL.

<criterion id="DB37-1-AC2" cell_refs="DB-b-73"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r37/p37_round37.py" . DB37-1-AC2</invocation><expect>DB37-1-AC2 PASS</expect></criterion>
`DB37-1-AC2` -- the kit runs for 2026-10-06 and 2026-10-07 each cover the population with 0 refusals and lots rows, peak and time printed. Base: FAIL.

<criterion id="DB37-1-AC3" cell_refs="DB-b-73"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r37/p37_round37.py" . DB37-1-AC3</invocation><expect>DB37-1-AC3 PASS</expect></criterion>
`DB37-1-AC3` -- the producer tests pass, with a new test for the repeat pair. Base: FAIL.

<expected_criteria>DB37-1-AC1,DB37-1-AC2,DB37-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** you edit the lots producer, its tests folder and the realized-lot contract named in `<paths>`. Nothing is
  deployed: the producer's bytes reach the Lambda only through the release cell that follows.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~50/
data/assets/scripts/gold/irpt_reporting/account_activity_lots.py
data/assets/scripts/gold/irpt_reporting/tests/
org/standards/IRPT_DASHBD_ACCOUNT_LOT_REALIZED_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-73.lots-key-resize.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 39 (round 37), cell `DB-b-73`.
<owned_cells>DB-b-73</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB37-1-AC1, DB37-1-AC2, DB37-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~50/IRPT_DASHBD.TO-DB-b-73.lots-key-resize.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB37-1-AC1,DB37-1-AC2,DB37-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the repeat census, the new key and why it is the smallest, the test result, and both kit days' accounts, refusals, lots rows, peak and time, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the producer change reaches served output only through the next signed release; this cell deploys nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB37-1-AC1/AC2/AC3 FAIL at base (no record). Row D2-W47-S5 (the lots-key refusal), CTO msg 2393 and ADDENDUM 5.
lane: the <paths> block IS the grant.
</preflight>
