# TO IRPT_DASHBD.TO-DB-b-87 -- E5: the 2026-10-08 realized-lot repeat (row S40) -- read every pair, print the differing columns, decide by the producer's rule (extend the key by the minimal real lot attribute under a rule-24 record, or file a source duplicate; never dedupe silently), and re-size both kit days with the full lots stage

<to_id>IRPT_DASHBD.TO-DB-b-87</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~62</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>42</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 10 (msg 3225; row S40 BLOCKING @a1ca17786a), enrichment item E5 | **Decomp cell:** `DB-b-87` (decomposition section 44, round 42) | **outcome_ref:** FWD-4 | **depends_on:** none (R37 live; row S40).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-62`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~62/`.

**The cell (`DB-b-87`).** R37 is live. Its first scheduled fire (11:41:45Z) logged:
- `LOTS_SKIPPED 2026-10-08: REFUSED: realized lot id ... repeats with the same closing date, quantity and proceeds`;
- returns and class landed (Branch B; row IRPT_DASHBD-S40, BLOCKING).

The key is `(firm, account_id, business_date, lot_id, quantity, proceeds)`, extended by DB-b-73 for a 2026-10-07 wash-sale pair
(`deliverables/0.9.0_WK_IRPT_DASHBD~50/LOTS_KEY_E1.json`). The refusal is in `realized_rows()`,
`C:/dev/wk-irpt-dashbd-62/data/assets/scripts/gold/irpt_reporting/account_activity_lots.py`.

The CTO ruled (ADDENDUM 10):

1. **Read the 2026-10-08 realized-lot partition** through the producer's declaration, over every population account. For each pair sharing the
   whole current key, record `per_pair` [{differing_columns}], with hashed account keys only. Record `repeat_census` {day, pairs, per_pair}.
2. **Decide by the producer's rule.**
   - **The pairs differ on a real lot attribute** (for example the open date, cost basis or a tax-lot / close-event id): set `decision`
     "EXTEND_KEY".
     - Extend `PRIMARY_KEYS` and the contract's `primary_key` by the MINIMAL such column, so a true duplicate still refuses by name.
     - Write the rule-24 record (four postulates, word-boundary token census, the effect) as a file in your folder, and name it in
       `rule24_record`.
     - Add a test for the new pair.
   - **Every pair is identical in every column:** set `decision` "SOURCE_DUPLICATE".
     - Keep the refusal.
     - File the duplicate as a row to the source's owner and name it in `source_row`.
     - Change no key. Nothing is collapsed by Opal.
3. **Re-size on the kit with the FULL lots stage**, for 2026-10-07 and 2026-10-08 over the population. **The kit (pandas 2.2.3).** Its path is in `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/relay/KIT_PATH_PY312_PANDAS223.txt`. Build the venv in `.scratch/` with
`C:/Users/Test/AppData/Local/Programs/Python/Python312/python.exe` and `pip install --no-index --find-links <kit> -r <pin file>`, side-loading
boto3, psutil and pytest offline (rows W44-S1, W46-S2). Use DB-b-73's day wrapper `deliverables/0.9.0_WK_IRPT_DASHBD~50/kit_run_day.py`
(round 30's runner, default batch). `refusals` counts REFUSED, LOTS_SKIPPED and CLASS_SKIPPED lines. Record
   `kit_runs[<day>]` {accounts, refusals, lots_rows, peak_mb, total_s}. Both days must be under 765 s and 1,740.8 MB. On SOURCE_DUPLICATE,
   2026-10-08 still refuses by name.
4. Record `tests` {passed, failed, new_test} in `LOTS_KEY_R41.json`.

<criterion id="DB41b-1-AC1" cell_refs="DB-b-87"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r41b/p41b_lotkey.py" . DB41b-1-AC1</invocation><expect>DB41b-1-AC1 PASS</expect></criterion>
`DB41b-1-AC1` -- the 2026-10-08 repeat pairs are read with their differing columns, and the decision follows the producer's rule (a minimal key extension with a rule-24 record, or a source duplicate filed). Base: FAIL.

<criterion id="DB41b-1-AC2" cell_refs="DB-b-87"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r41b/p41b_lotkey.py" . DB41b-1-AC2</invocation><expect>DB41b-1-AC2 PASS</expect></criterion>
`DB41b-1-AC2` -- both kit days run the full lots stage over the population under 765 s and 1,740.8 MB, with refusals as the decision implies. Base: FAIL.

<criterion id="DB41b-1-AC3" cell_refs="DB-b-87"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r41b/p41b_lotkey.py" . DB41b-1-AC3</invocation><expect>DB41b-1-AC3 PASS</expect></criterion>
`DB41b-1-AC3` -- the producer tests pass with a new test. Base: FAIL.

<expected_criteria>DB41b-1-AC1,DB41b-1-AC2,DB41b-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** you edit the lots producer, its tests folder and the realized-lot contract. Nothing is deployed: DB-b-88 releases
  it.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~62/
data/assets/scripts/gold/irpt_reporting/account_activity_lots.py
data/assets/scripts/gold/irpt_reporting/tests/
org/standards/IRPT_DASHBD_ACCOUNT_LOT_REALIZED_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-87.lots-key-1008.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 44 (round 42, lot-key chain), cell `DB-b-87`.
<owned_cells>DB-b-87</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB41b-1-AC1, DB41b-1-AC2, DB41b-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~62/IRPT_DASHBD.TO-DB-b-87.lots-key-1008.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB41b-1-AC1,DB41b-1-AC2,DB41b-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the pair census with differing columns, the decision and why, the key or source row, both kit days' figures, and the tests, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the producer change reaches served output only through DB-b-88's release under the R37 half.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only; no role changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB41b-1-AC1/AC2/AC3 FAIL at base (no record). Row S40; CTO ADDENDUM 10.
lane: the <paths> block IS the grant.
</preflight>
