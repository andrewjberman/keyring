# TO IRPT_DASHBD.TO-DB-f-1201 -- the FWD-5 PRODUCER GROUND READ for Cottonwood and Inflection: for each of the 14 columns the backend brief names for `account_transaction`, the source column each firm's code reads (or ABSENT), the producer to copy, the address the naming builder gives, and what emitting it would touch; one record per firm; a read of code and tracked records, nothing written

<to_id>IRPT_DASHBD.TO-DB-f-1201</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1201</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>126</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the round-119 analysis for F-SHIP ruling 3 (`~F2` writes `IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json` and its producer "from the custody transaction silver per firm") | **Rows:** IRPT_DASHBD-D2-W1201-S<k> | **Decomp cell:** `DB-f-1201` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R126_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-1201` (branch `wk-IRPT_DASHBD-1201`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1201/`. The folders `lib/`, `data/assets/scripts/gold/irpt_reporting`, `data/inf`, `docs/briefs`, `org/standards`, `infra/logic`, `infra/aws/lambda/investor-reporting` and `infra/aws/terraform/investor-reporting` are materialized in your worktree for reading (if one is missing, run `git sparse-checkout add <folder>` for it: that is not a grant to edit). Never push; never commit the workspace `portal` gitlink. This is a READ of repository files plus one LOCAL call of the naming builder per firm (`python -I -c` over `lib/opal_naming.py`, no AWS): no AWS call, no network, no vendor call, no secret read. No real client, household or account id and no client figure is ever written in the repo, a row or your report.

**Why.** Round 123 measured the 49 Financial ground (`deliverables/0.9.0_WK_IRPT_DASHBD~901/RD_FWD5_PRODUCER_GROUND_R123.json`): 7 of the brief's 14 columns have a silver source. The contract and the per-firm producers must also state Cottonwood's and Inflection's sources and absences, in the same form, so the contract is written on measured facts for all three firms. The round-120 record `deliverables/0.9.0_WK_IRPT_DASHBD~701/RD_FWD5_FIELDS_R120.json` lists the columns the code reads: Cottonwood 5 (`AccountID`, `Trade Date`, `External Flow`, `Transaction Type`, `Market Value`; `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py` about line 430), Inflection 11 (`id`, `accountId`, `clientId`, `householdId`, `transTypeId`, `transDate`, `transAmount`, `noUnits`, `navPrice`, `ticker`, `transactionDescription`; `data/inf/manual_api/pull_inflection_transactions_rest.py` about line 99). Those are what the CODE reads; a source may carry more, and a column the code does not name is `absent` here with that reason, never a guess.

**The cell (`DB-f-1201`).** Do steps 1 to 5 once for `cottonwood` and once for `inflection`.
1. **The 14 targets.** `docs/briefs/reporting-dashboard-backend-brief-20260930.md` line 78: `trade_date`, `settle_date`, `action`, `txn_type`, `symbol`, `asset_name`, `units`, `price`, `amount`, `fee`, `custodian`, `flow_class`, `source_txn_id`, `coverage`. For each, in that order, find the firm's source column the code reads. A target a column supplies: `source` is that column name (exactly as the file spells it) and the cited line holds it, claim `measured`. A target no column supplies: `source` null, claim `absent`, `words` saying what is missing and which column could feed it (as `inferred`, never as the source). A target the producer would COMPUTE from measured inputs (`custodian` from the firm's constant, `flow_class` from the type, `coverage`) is claim `absent` with a null source ONLY when the checker's form forces it; say in `words` "computed: inferred, method <how>" so the contract can carry it as `inferred` with a method (CTO round-123 analysis ruling 1). Use `comp-find --files '<term>' <folder> --limit 20` for any search and print each denominator you cite.
2. **The pattern producer.** The firm's existing code path that reads its transactions into the gold returns table (Cottonwood: the adapter; Inflection: the pull and its silver/gold step), and the shape to copy for a gold writer (`account_class_daily.py` `emit_class_day`): `pattern_producer` {`file`, `line` (holds `def `, `ARROW_SCHEMA`, `emit` or `TABLE_`), `words`, `claim`}.
3. **The source.** `silver_source` {`file`, `line` (holds `fact_trn`, `fact_transactions`, `transaction` or `trn`), `words`, `claim`}: where the code reads the firm's transactions and from which prefix or API (do not copy a bucket or account value).
4. **The address.** Run, locally, `python -I -c "import sys; sys.path.insert(0,'lib'); import opal_naming; print(opal_naming.address('irpt','<firm>','gold','account_transaction','date=2000-01-03'))"` from your worktree root and record the output exactly as `address.uri` (or the builder's refusal in `words`: a refusal is a missing registry row, never a workaround). `address.registry_row_exists` (boolean): whether `infra/logic/registry/` holds a row for the table `account_transaction` (search it, print the denominator, and say whether the registry names any gold table at all).
5. **The emit path.** What emitting a third gold table for this firm would touch: the reporting-gold handler, the Terraform role and policy for that firm's prefix, and the never-widen packet (read `infra/aws/lambda/investor-reporting/reporting-gold/handler.py` and `infra/aws/terraform/investor-reporting/`; say whether the firm's class prefix exists, since the CTO's live read found Cottonwood's and Inflection's class prefixes empty): `emit_path` {`file`, `line` (holds `account_class_daily`, `class`, `emit`, `put` or `prefix`), `words` (each touch-point with its file and line), `claim`}.
6. **Records.** `RD_FWD5_GROUND_COTTONWOOD_R126.json` and `RD_FWD5_GROUND_INFLECTION_R126.json` in your folder, each with EXACTLY these top-level fields: `as_of` (ISO date), `firm` ("cottonwood" or "inflection"), `targets` (the 14 objects in the brief's order: `target`, `source` (string or null), `file`, `line`, `words`, `claim`; for a null source, `file` and `line` still name the code that would have named the column, the nearest place), `absent_count` (the number of targets whose source is null), `pattern_producer`, `silver_source`, `address`, `emit_path`, `reads` {`s3_reads` 0, `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}, and the false flags `files_in_repo`, `served_values_changed`, `pushed`, `deployed`. Every `claim` is one of `measured`, `inferred`, `held`, `absent`. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `vintage` or `uri` field.

<criterion id="DBF126-1-AC1" cell_refs="DB-f-1201"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r126/p126_ground2.py" . DBF126-1-AC1</invocation><expect>DBF126-1-AC1 PASS</expect></criterion>
`DBF126-1-AC1` -- both records have exactly the form of step 6; for each firm the 14 targets are exactly the brief's columns in the brief's order; a target with a source cites a line that holds that column name, and a target without one is `absent` with a null source; `absent_count` equals the count the checker computes; `pattern_producer`, `silver_source` and `emit_path` cite lines holding their tokens; `address.uri` is an s3 uri for that firm and account_transaction with `registry_row_exists` a boolean; every claim is in the four-word set; the reads block is all zero, the flags false and no run of 8 or more digits stands outside the exempt fields. Base: FAIL (no records).

<expected_criteria>DBF126-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every code file, brief, contract, Terraform root, registry file, the round-120 and round-123 records and the issuer's check.
- **A READ.** Nothing is deployed, applied, published, pushed or changed outside your folder; no AWS call; no network. Do not add a registry row.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A zero is never read as "does not exist" without the tool's printed denominator beside it. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W1201-S<k>` (D2 is the device coordinate, never F2), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1201/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-1201.read-fwd5-cottonwood-and-inflection-transaction-producer-ground-sources-address-emit-path.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R126_F.md</decomp_doc> round 126, workstream ~F2 (F-SHIP), cell `DB-f-1201`.
<owned_cells>DB-f-1201</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF126-1-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1201/IRPT_DASHBD.TO-DB-f-1201.read-fwd5-cottonwood-and-inflection-transaction-producer-ground-sources-address-emit-path.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF126-1-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; per firm how many of the 14 targets have a source and which are absent; the pattern producer; the address the builder gave (or its refusal) and whether a registry row exists; the touch-points of the emit path and whether the firm's class prefix exists in the code's view; anything off-task (as row ids). No real id and no client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and records in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant is changed; the Terraform role is read, not edited.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF126-1-AC1 FAILS at base (no records) and the checker's helpers are exercised by its self-test (9 arms).
lane: the <paths> block IS the grant.
</preflight>
