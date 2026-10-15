# TO IRPT_DASHBD.TO-DB-i-14 -- the SCOPE FEED MODULE ON CONTRACT 0.4.2: Orion PRESENT rows write return_basis TWR (provenance stays in `source`), market_value_eod_claim is a declared column of the table, contract_version reads 0.4.2; the W311-S3 test line; fixtures only, nothing to AWS

<to_id>IRPT_DASHBD.TO-DB-i-14</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~314</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>127</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_125_20261015.md` (round 127: msg 8695, 8698 and the 0.4.2-landed message) and `2.0.0_SA_COO~D2` (contract 0.4.2 landed, merge 6ac152c83a).

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-314`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~314/`. Never touch a path outside the `<paths>` block below.

**Why.** Round 125 made the module green against contract 0.4.1, which required `VENDOR_REPORTED` on an Orion row and had no claim column. Contract 0.4.2 has now landed: `return_basis` is `TWR` or `NOT_MEASURABLE` only (provenance is the `source` column, mapped to vendor-computed in the contract's `source_provenance`), and the optional column `market_value_eod_claim` (`measured` or `inferred`) is REQUIRED on a PRESENT Orion row and null on an ABSENT row. A 0.4.1 Orion row no longer validates, so four module tests are red on trunk. This order flips the module to 0.4.2. Everything runs on fixtures; nothing touches AWS.

**What you do (edit four existing files; add nothing else).**
1. `data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_adapter.py` (the pure adapter; standard library only, no I/O).
2. `data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_run.py` (the wrapper; standard library, `pyarrow`, the sibling adapter, and the one contract file it already reads).
3. `data/assets/scripts/gold/irpt_reporting/tests/test_inflection_scope_feed_adapter.py` and 4. `data/assets/scripts/gold/irpt_reporting/tests/test_inflection_scope_feed_run.py`: update so every test passes on the new behaviour; the wrapper's file keeps a `test_mutant_...` test.

**Read first (read only).** `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` (version 0.4.2: `enums.return_basis`, the optional column `market_value_eod_claim` with its `rule`, `source_provenance`, `schema_hash_with_optional`); `data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_042.py` (the validator `row_problems`, which the checker uses); the checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r127/p127_run042.py` and, for its helpers, `.../checks/r124/p124_run.py` and `.../checks/r123/p123_adapter.py` (its synthetic world is the golden; read it before you write code and run it as you go; where an older checker differs, the r127 checker rules; the round-125 checker `checks/r125/` graded 0.4.1 and is superseded).

**The cell (`DB-i-14`).** Text of the owned cell: *"Flip the Scope feed adapter and run wrapper to contract 0.4.2: Orion PRESENT rows write return_basis TWR with provenance in source; the end-of-day claim market_value_eod_claim is a declared column of the table (required on PRESENT rows, null on ABSENT rows), so the run record's claim_placement retires; contract_version reads 0.4.2 from the contract file; an account seen only on a dropped day is still counted; fixtures only, no AWS."*

### The adapter

- A PRESENT row's `return_basis` is `TWR` (not `VENDOR_REPORTED`); remove the `VENDOR_REPORTED` constant and every comment or docstring that says the module writes it. `source` stays `orion`; `day_quality` `MEASURED` and `guard_state` `GUARD_NOT_REACHED` stay.
- The claim: a PRESENT row carries `market_value_eod_claim` `inferred` (the end-of-day value came from the next calendar day's start value) or `measured` (it came from the day's own end value), as today; an ABSENT row carries None. Nothing else in the adapter changes: the rules, the ABSENT shape, the `domain` and `accounts` parameters, the manifest and the refusals stand.

### The wrapper

- The table's fields come from the contract file (columns then optional columns), as today. The claim is therefore written to the table as a declared column. **If the contract file does not declare `market_value_eod_claim`, REFUSE** with a `ValueError` whose message carries the count 1 and names the contract version it read, and write nothing (a writer never runs ahead of its contract, and never behind it).
- The run record KEEPS: `contract_version` (read from the file), `calendar_days_read`, `calendar_days_incomplete`, `incomplete_days`, `rows_present`, `rows_absent`, `partitions_written`, `absent_by_reason`, `accounts_in_feed`, `accounts_mapped`, `accounts_unmapped`, `trading_days_unaccounted`, `market_value_eod_claim_counts` and `manifest`. The key `claim_placement` RETIRES. All five refusals and the complete-day rule stand as in round 125.
- **Row W311-S3 as a test line:** a test where an account appears ONLY on a dropped day still counts it in `accounts_in_feed` and `accounts_mapped`.

### The tests

Update the red tests (the PRESENT `return_basis`; the claim-in-the-run-record test becomes a claim-in-the-table test; the copy-of-the-contract test becomes the refusal when a copy lacks the column) and add the W311-S3 line. Keep the schema-hash test (the written fields hash to `schema_hash_with_optional`), the validator test over every written row (use `row_problems` from `test_account_return_contract_042.py`) and the 299-day chain. ASCII only. Run `python -I -m pytest -q <file>` on both files until green.

<criterion id="DBI127-1-AC1" cell_refs="DB-i-14"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r127/p127_run042.py" . DBI127-1-AC1</invocation><expect>DBI127-1-AC1 PASS</expect></criterion>
`DBI127-1-AC1` -- the golden through the wrapper: 17 PRESENT rows (`TWR`, PRESENT, source orion, the claim `measured` on the window's last day and `inferred` otherwise) and 11 ABSENT rows in the table (claim null), the run record (`contract_version` read from the contract file, no `claim_placement` key, the claim counts, `trading_days_unaccounted` 0). Base: FAIL on trunk (the merged module writes VENDOR_REPORTED).

<criterion id="DBI127-1-AC2" cell_refs="DB-i-14"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r127/p127_run042.py" . DBI127-1-AC2</invocation><expect>DBI127-1-AC2 PASS</expect></criterion>
`DBI127-1-AC2` -- every written partition holds only its own date, its fields and types equal the contract's declared fields (the claim is one of them) and hash to `schema_hash_with_optional`, every row passes the 0.4.2 validator, the wrapper imports no AWS or network module, names no `s3://` address and types no contract version, and nothing is written outside the output directory. Base: FAIL on trunk.

<criterion id="DBI127-1-AC3" cell_refs="DB-i-14"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r127/p127_run042.py" . DBI127-1-AC3</invocation><expect>DBI127-1-AC3 PASS</expect></criterion>
`DBI127-1-AC3` -- the repairs still hold (both edge-day fixtures read 0 unaccounted, the five refusals carry a count and write nothing, the 299-day chain equals the source product to 1e-12), an account seen only on a dropped day is still counted (W311-S3), and the adapter and wrapper test files together pass at least 30 tests and name a mutant test. Base: FAIL on trunk (4 module tests are red).

<expected_criteria>DBI127-1-AC1,DBI127-1-AC2,DBI127-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the contract, the contract test modules, `lib/`, `infra/` and every issuer check.
- **No AWS, no network.** The wrapper reads the frames it is handed and the one contract file, and writes local files under `out_dir`. Landing the table and reading the real silver are a later cell.
- **Client data.** None. Every row in your tests and record is synthetic; no run of 8 or more digits in anything you write except a `sha256` value or a path. Your tests write only to pytest's temp area.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A rule that seems wrong, or a case the rules do not cover, is a surprise ROW and you keep the rule as written; never invent a reason class, a fill or a field.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W314-S<k>`, with the real current UTC time (`date -u +%FT%TZ`, run at filing; never typed by hand); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_adapter.py
data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_run.py
data/assets/scripts/gold/irpt_reporting/tests/test_inflection_scope_feed_adapter.py
data/assets/scripts/gold/irpt_reporting/tests/test_inflection_scope_feed_run.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~314/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-14.inflection-scope-feed-module-on-contract-042-twr-and-claim-column.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 13, cell `DB-i-14`.
<owned_cells>DB-i-14</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI127-1-AC1, DBI127-1-AC2, DBI127-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~314/IRPT_DASHBD.TO-DB-i-14.inflection-scope-feed-module-on-contract-042-twr-and-claim-column.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI127-1-AC1,DBI127-1-AC2,DBI127-1-AC3` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the three criteria's last lines; the number of tests passed in each test file; any case the rules did not cover (as row ids); the line counts of the adapter and the wrapper. No client value, no account or household id, no date.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: edits to four existing local files whose only importers are their own tests (nothing is wired, scheduled, served or deployed).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call, no secret, no grant; the wrapper reads one repository file and writes local files under a directory it is handed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; all three criteria FAIL on trunk (the merged module writes VENDOR_REPORTED and keeps the claim in the run record), the checker passed a reference flip on all three, and six single-rule mutants of it (a PRESENT row VENDOR_REPORTED, the claim not written, the claim always measured, claim_placement kept, the contract version typed, the dropped-day account count regressed) each failed the checker before the cut.
</preflight>
