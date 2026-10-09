# TO MDPF_SECCLASS.TO-SC-e81 -- round 16 SC-e-81: the seed script's dry-run summary says DRY RUN and "would write N"

<to_id>MDPF_SECCLASS.TO-SC-e81</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~71</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-81` (`decompositions/MDPF_SECCLASS_DECOMP_R16.md`) |
**outcome_ref:** FWD-14 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-81`, row MDPF_SECCLASS-D1-S18. `infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py` `seed_table()` guards only
`batch.put_item` with `if not dry_run`. Every summary line after the write loop is unconditional, so a `--dry-run` prints
"Writing 15 item(s) to DynamoDB...", "OK: Seeding complete!" and "Items written : 15" while it puts nothing. The per-50 "[DRY RUN]"
progress line never prints below 50 items.

**Build:**
1. Under `dry_run`, print the closing summary as a dry run:
   - "Writing N item(s)" becomes a "DRY RUN -- would write N item(s)" line;
   - "OK: Seeding complete!" becomes a dry-run line (e.g. "DRY RUN complete -- nothing written");
   - "Items written : N" becomes "Would write : N".
   Every line printed after the MERGE SUMMARY under `--dry-run` must say DRY RUN or "would write", and none may say "Items written".
2. A real run (no `--dry-run`) prints exactly what it prints today, including "Items written : N".
3. Change no write path, no merge logic and no exit code.

### ACCEPTANCE

<criterion id="SC16-e81-AC1" cell_refs="SC-e-81"><invocation>python -m pytest -q org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R16_CHECKS/test_r16_seed_dry_run_words.py</invocation><expect>2 passed</expect></criterion>
`SC16-e81-AC1` -- the dry run says "would write", carries DRY RUN after the MERGE SUMMARY, never says "Items written", and puts nothing;
the real run still reports "Items written" (control). The test stubs boto3 and the table read, so it makes no AWS call. Do not edit
this test file.

<expected_criteria>SC16-e81-AC1</expected_criteria>

Dry-run at the base (dell1 box/dell1, 2026-10-09 ~09:0xZ): SC16-e81-AC1 FAIL, as expected. 1 failed (the dry-run arm: "a dry run must not
report items written") and 1 passed (the real-run control).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **Do not run the seed script against AWS**, in any mode. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W71-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken the test.

<paths>
infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R16.md</decomp_doc> (round 16), cell `SC-e-81`.
<owned_cells>SC-e-81</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC16-e81-AC1. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~71/MDPF_SECCLASS.TO-SC-e81.seed-dry-run-summary-words.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC16-e81-AC1`.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), the criterion's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a manually run script; nothing schedules it. Risk WORLD: the file sits under infra/ (the L6 floor), though this cell changes printed words only.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call in the cell (stubbed test).
comp-adversary: RUN -- the real-run summary changed (control arm); a put path touched (bounds); a dry-run line still saying "written" (arm 1)
lane: the <paths> block IS the grant.
</preflight>

Source: CTO rounds 13-15 analysis section 3 item 3 (msg 2139); row D1-S18; DECOMP_R16.
