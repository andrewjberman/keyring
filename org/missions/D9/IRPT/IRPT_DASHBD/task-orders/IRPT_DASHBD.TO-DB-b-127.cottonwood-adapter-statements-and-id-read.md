# TO IRPT_DASHBD.TO-DB-b-127 -- the Cottonwood adapter's two stale statements corrected, method row 3 read for a sentence false for Cottonwood, and ONE measured read of the account id the gold carries against the id the directory mints

<to_id>IRPT_DASHBD.TO-DB-b-127</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~102</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>68</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-68 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_68_20261011.md` @0005d9fd9a, section 4 item 4, answering `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v27.md` @806d057711 | **Rows:** IRPT_DASHBD-D2-W89-S1, IRPT_DASHBD-D2-W96-S3 | **Decomp cell:** `DB-b-127` (decomposition section 70) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-124 (its read of rows W89-S1 and W96-S3).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-102` (branch `wk-irpt-dashbd-68-102`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~102/`. Read first: section 4 (item 4) of the analysis above, and each row named above in
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/remediations/REMEDIATION_v27.md` (the reviewer's statement of it) and in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md` (the original row).

**The cell (`DB-b-127`).** Three parts.
1. **Two stale statements** (row W89-S1) in `data/assets/scripts/silver/commonwealth_account_return_daily.py`: its docstring and its
   `COLUMNS_NULL` entry say `method_version` is NULL on purpose, while the code stamps 3. Correct both to what the code does
   (`stale_statements`: [{where, before, after}]). Comments and one data literal only: if correcting `COLUMNS_NULL` changes what the adapter
   WRITES or what its verify expects, STOP with a row instead (the table is minted and a re-mint is not this cell).
2. **Method row 3, read for Cottonwood.** Run the producer's dry run for the `_commonwealth_delivery` entry
   (`emit_method_row(None, firm_scope(entry), thresholds, upload=False, src=entry)` in `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`) and read EVERY
   sentence-bearing member of the row it returns and of the manifest beside it (`row3_sentences.read` = how many). For each sentence, is it
   true of the Cottonwood channel? The row names two worries: it does not state as-traded close or net of fees, and it inherits a flow
   convention measured for the custodian channel. List each sentence that is false or unstated for Cottonwood with a `disposition`:
   `ROW_FOR_ISSUER` (file a row; an edit to row 3 needs its own rule-24 record and is NOT made in this cell) or `TRUE_AS_WRITTEN`.
   Today's income change (income stated ABSENT with its reason) is already in; the next cell rewords that reason and is not yours.
3. **The account id** (row W96-S3). One measured read: the FORM of `account_id` in one Cottonwood gold partition against the FORM of the key
   the directory mints its opaque ids from (`infra/aws/lambda/investor-reporting/_ids/raw_keys.json` declares the directory's raw key per
   firm; `raw_account_for` in `infra/aws/lambda/investor-reporting/reporting/entry.py` is the join). Mint opaque ids from the gold's ids the
   way the reporting read does and count how many equal an id in the directory artifact. `account_id`: {measured, gold_form,
   directory_form, joins, how, counts_only: true, counts {gold_ids, directory_ids, joined}}. FORMS are described in words ("a custodian
   account number, 8 digits", "a vendor key with a firm prefix"); NO id is written anywhere.
`tests` {passed, failed}: the adapter's existing tests under `data/assets/scripts/silver/tests/` still pass.

<criterion id="DB68-4-AC1" cell_refs="DB-b-127"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r68/p68_round68.py" . DB68-4-AC1</invocation><expect>DB68-4-AC1 PASS</expect></criterion>
`DB68-4-AC1` -- the adapter's two stale statements are corrected, method row 3's sentences are read for Cottonwood, and the account-id join is measured or stated not established, in counts only. Base: FAIL.

<expected_criteria>DB68-4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. AWS reads are limited to what the account-id read needs and NOTHING else: ONE Cottonwood gold `account_return_daily` partition's `account_id` COLUMN ONLY (read with a column projection; no other column leaves the object), and the directory artifact the reporting read mints ids from. If either read is DENIED (dell2 seats have been denied on Cottonwood prefixes before), record the denial verbatim, do not retry another way, and `joins` reads NOT_ESTABLISHED.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~102/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W102-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~102/
data/assets/scripts/silver/commonwealth_account_return_daily.py
data/assets/scripts/silver/tests/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-127.cottonwood-adapter-statements-and-id-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 70 (round 68), cell `DB-b-127`.
<owned_cells>DB-b-127</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB68-4-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~102/IRPT_DASHBD.TO-DB-b-127.cottonwood-adapter-statements-and-id-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB68-4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the two stale statements before and after; how many sentences of method row 3 and its manifest you read and which, if any, are false for Cottonwood with what you did about each; the account-id read -- what you read, the two id FORMS in words (never an id), the counts, and whether they join; the tests; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; two comments in an adapter and one counts-only read; nothing served is written.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; two governed reads; a denial is a result and is not widened.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
