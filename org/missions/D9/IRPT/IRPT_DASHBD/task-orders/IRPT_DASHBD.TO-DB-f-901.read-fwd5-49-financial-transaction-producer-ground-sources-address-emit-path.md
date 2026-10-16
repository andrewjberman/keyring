# TO IRPT_DASHBD.TO-DB-f-901 -- the FWD-5 PRODUCER GROUND READ for 49 Financial: for each of the 14 columns the backend brief names for `account_transaction`, the custody-silver source column the code reads (or ABSENT), the existing producer to copy, the address the naming builder gives a third gold table, and what emitting it would touch; a read of code and tracked records, nothing written

<to_id>IRPT_DASHBD.TO-DB-f-901</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~901</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>123</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the round-119 analysis for F-SHIP ruling 3 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_119_20261016.md`: `~F2` writes `IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json` and its producer "from the custody transaction silver per firm") and the round-121 analysis (msg 8991: the first account read is a 49 Financial one) | **Rows:** IRPT_DASHBD-D2-W901-S<k> | **Decomp cell:** `DB-f-901` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R123_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-901` (branch `wk-IRPT_DASHBD-901`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~901/`. The folders `lib/`, `data/assets/scripts/gold/irpt_reporting`, `docs/briefs`, `org/standards`, `infra/logic`, `infra/aws/lambda/investor-reporting` and `infra/aws/terraform/investor-reporting` are materialized in your worktree for reading (if one is missing, run `git sparse-checkout add <folder>` for it: that is not a grant to edit). Never push; never commit the workspace `portal` gitlink. This is a READ of repository files plus one LOCAL call of the naming builder (`python -I -c` over `lib/opal_naming.py`, no AWS): no AWS call, no network, no vendor call, no secret read. No real client, household or account id and no client figure is ever written in the repo, a row or your report.

**Why.** FWD-5 needs a new gold table, `account_transaction`, and a producer from the custody transaction silver; the first firm served is 49 Financial (Cottonwood and Inflection read absent). The words that fill `action` and `txn_type` are being ratified (round 122, `deliverables/0.9.0_WK_IRPT_DASHBD~802/FWD5_WORDS_PROPOSAL_R121.json`), but the contract's SHAPE and the producer's SOURCE MAPPING do not depend on them. This cell measures that ground so the contract-and-producer cell is cut on measured facts: which of the brief's 14 columns have a source in the silver and which have none.

**The cell (`DB-f-901`).**
1. **The 14 targets.** The brief line is `docs/briefs/reporting-dashboard-backend-brief-20260930.md` line 78: `trade_date`, `settle_date`, `action`, `txn_type`, `symbol`, `asset_name`, `units`, `price`, `amount`, `fee`, `custodian`, `flow_class`, `source_txn_id`, `coverage`. For each, in that order, find the 49 Financial transaction-silver column that supplies it. The round-120 record `deliverables/0.9.0_WK_IRPT_DASHBD~701/RD_FWD5_FIELDS_R120.json` lists the 14 columns the code reads (`account_id`, `business_date`, `debit_credit`, `gross_amount`, `tran_srcde`, `tr_cd`, `sb_cd`, `transaction_detail_description`, `quantity`, `price`, `cusip`, `dividend_interest_share_quantity`, `trade_typcd`, `ticker_symbol`); read where the code names them (`data/assets/scripts/gold/irpt_reporting/sources.json`, `account_return_daily.py` about lines 510-532, `account_activity_lots.py`). A target the silver columns supply: `source` is that column name and the cited line holds it. A target NO column supplies (for example a settle date, a fee, a source transaction id, an asset name, if the code names none): `source` is null, `claim` is `absent`, and `words` says what is missing and, if a different column could feed it, which (as `inferred`, never as the source). `action` and `txn_type` source from `tr_cd` and `sb_cd` by the ratified words (claim `inferred`); `flow_class` and `coverage` are derived (say from what); `custodian` is the firm's constant (say where the code holds it). Use `comp-find --files '<term>' <folder> --limit 20` for any search and print each denominator you cite.
2. **The pattern producer.** The existing gold producer whose structure the new producer should copy (it writes one account-grain table beside `account_return_daily`: read `account_class_daily.py` and `account_activity_lots.py`): `pattern_producer` {`file`, `line` (the line holds `def `, `ARROW_SCHEMA`, `emit` or `TABLE_`), `words`, `claim`}.
3. **The silver source.** `silver_source` {`file`, `line` (holds `fact_trn`, `transaction` or `trn`), `words`, `claim`}: where the code reads the 49 Financial transaction silver and its prefix.
4. **The address.** Run, locally, `python -I -c "import sys; sys.path.insert(0,'lib'); import opal_naming; print(opal_naming.address('irpt','49financial','gold','account_transaction','date=2000-01-03'))"` from your worktree root and record the output exactly as `address.uri` (or the builder's refusal in `words`, if it refuses: a refusal is a missing registry row, never a workaround). `address.registry_row_exists` (boolean): whether `infra/logic/registry/` holds a row for the table `account_transaction` (search it, print the denominator).
5. **The emit path.** What emitting a third table beside `account_class_daily` would touch: the reporting-gold handler (`infra/aws/lambda/investor-reporting/reporting-gold/handler.py`, where `account_class_daily` is emitted and its prefix located), the Terraform role/policy that lets the function write the class prefix (`infra/aws/terraform/investor-reporting/`), and the never-widen packet. `emit_path` {`file`, `line` (holds `account_class_daily`, `class`, `emit`, `put` or `prefix`), `words` (each touch-point, with its file and line), `claim`}.
6. **Record** `RD_FWD5_PRODUCER_GROUND_R123.json` in your folder with EXACTLY these top-level fields: `as_of` (ISO date), `firm` ("49financial"), `targets` (the 14 objects, in the brief's order: `target`, `source` (string or null), `file`, `line`, `words`, `claim`; for a null source, `file` and `line` still name the code that would have named the column, the nearest place, and `claim` is `absent`), `absent_count` (the number of targets whose source is null), `pattern_producer`, `silver_source`, `address`, `emit_path`, `reads` {`s3_reads` 0, `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}, and the false flags `files_in_repo`, `served_values_changed`, `pushed`, `deployed`. Every `claim` is one of `measured` (you read the line), `inferred`, `held`, `absent` (with the reason in the words; never invented). No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `vintage` or `uri` field.

<criterion id="DBF123-1-AC1" cell_refs="DB-f-901"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r123/p123_ground.py" . DBF123-1-AC1</invocation><expect>DBF123-1-AC1 PASS</expect></criterion>
`DBF123-1-AC1` -- `RD_FWD5_PRODUCER_GROUND_R123.json` has exactly the form of step 6; the 14 targets are exactly the brief's columns in the brief's order; a target with a source cites a line that holds that column name, and a target without one is `absent` with a null source; `absent_count` equals the count the checker computes; `pattern_producer`, `silver_source` and `emit_path` cite lines holding their tokens; `address.uri` is an s3 uri for 49financial and account_transaction with `registry_row_exists` a boolean; every claim is in the four-word set; the reads block is all zero, the flags false and no run of 8 or more digits stands outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DBF123-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every code file, brief, contract, Terraform root, registry file, the round-120 and round-122 records and the issuer's check.
- **A READ.** Nothing is deployed, applied, published, pushed or changed outside your folder; no AWS call; no network. A fact only the live data could answer (a column the silver holds that no file names) is `absent` with that reason, never a guess. Do not add a registry row.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A zero is never read as "does not exist" without the tool's printed denominator beside it. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W901-S<k>` (D2 is the device coordinate, never F2), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~901/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-901.read-fwd5-49-financial-transaction-producer-ground-sources-address-emit-path.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R123_F.md</decomp_doc> round 123, workstream ~F2 (F-SHIP), cell `DB-f-901`.
<owned_cells>DB-f-901</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF123-1-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~901/IRPT_DASHBD.TO-DB-f-901.read-fwd5-49-financial-transaction-producer-ground-sources-address-emit-path.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF123-1-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; how many of the 14 targets have a source and which are absent; the pattern producer; the address the builder gave (or its refusal) and whether a registry row exists; the touch-points of the emit path; anything off-task (as row ids). No real id and no client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and a record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant is changed; the Terraform role is read, not edited.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF123-1-AC1 FAILS at base (no record) and the checker's helpers are exercised by its self-test (9 arms).
lane: the <paths> block IS the grant.
</preflight>
