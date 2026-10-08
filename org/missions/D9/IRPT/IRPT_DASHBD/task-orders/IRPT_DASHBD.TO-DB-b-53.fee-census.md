# TO IRPT_DASHBD.TO-DB-b-53 -- E2: Opal's advisory-fee leg measured -- a census of Schwab's fee rows for the 1,528 right-half misses, how account_return_daily classes them (from source lines), and one account traced

<to_id>IRPT_DASHBD.TO-DB-b-53</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~32</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>30</round>
<workstream>BD</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-29 analysis @72ae174b3c
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_29_20261008.md` section 3, item E2), as recast by
msg 1641 (E2 is E1's input, one chain) | **Decomp cell:** `DB-b-53` (decomposition section 32) | **outcome_ref:** FWD-8 |
**depends_on:** DB-b-49 (merged @a556d87e79).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-32`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~32/`.

**The cell (`DB-b-53`).** Over 1,528 accounts, Opal's served return is above Black Diamond's after 2025-01-10 (median +0.567 pp
against BD's add-back gross; median +2.92 pp against BD net). The lead is the advisory fee. `account_return_daily.py`
(`data/assets/scripts/gold/irpt_reporting/`) treats a `FEE-MANAGEMENT` debit as capital crossing the account boundary (external
flow), so Opal's return is gross of it, while BD's is net. This cell measures Opal's fee leg from the custodian rows.

**Population:** the rows of `deliverables/0.9.0_WK_IRPT_DASHBD~28/TIEOUT_SPLIT_E1.json` with `right.tied == false` AND
`recompose.within == true` (1,528). Each row's `right.range` {start, end} is that account's window. Take the set from the record; do not
re-derive it.

**Sources (read only):**
- The custodian declaration is `data/assets/scripts/gold/irpt_reporting/sources.json`, key `schwab_08335338`. It names:
  - the bucket `opal-data-assets`, transactions `schwab/08335338/silver/fact_trn/date=YYYY-MM-DD/`, balances `.../dim_balance/`;
  - the key columns `tran_srcde, tr_cd, sb_cd`, money `gross_amount`, direction `debit_credit`;
  - the classification table.
- The producer's partition-to-class map is `FINAL_BY_PARTITION` (near line 200). The boundary rule is near line 626-640.
- The served gold is `s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/date=<YYYY-MM-DD>/data.parquet`
  (external_flow, total_return_daily, market_value_eod).

1. For each population account over its right-half window, collect every fact_trn row whose key classes (through the classification
   table and `FINAL_BY_PARTITION`) to `FEE-MANAGEMENT` or `FEE-ADMIN`. Write `census` {by_key: [{key, partition, final_class, rows,
   amount}], rows_total, amount_total, accounts_with_fee}. Amount is signed by `debit_credit` (debit negative).
2. Write `classification` {FEE-MANAGEMENT: "external_flow" | "return", FEE-ADMIN: "external_flow" | "return"}: what the producer does
   with each today. Give `source_lines` [{file, line, text}], where each `text` is a substring of that line at your HEAD.
3. Trace one population account with fee rows: `trace` {account, fee_days: [{business_date, fee_amount, served_external_flow,
   served_total_return_daily}]}, plus one sentence on the return effect.
4. Write `FEE_CENSUS_E2.json` (`population`, `census`, `classification`, `source_lines`, `trace`, `files_read`) and
   `FEE_CENSUS_E2.md`, COUNTS AND TOTALS ONLY. No account number, name or balance in the `.md`; `trace.account` lives in the `.json`
   only.
5. Keep a per-account, per-day fee table for your next order (DB-b-54): `FEE_ROWS_E2.parquet` in your folder, with columns account,
   business_date, final_class, amount. It is a deliverable.

<criterion id="DB30-1-AC1" cell_refs="DB-b-53"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r30/p30_round30.py" . DB30-1-AC1</invocation><expect>DB30-1-AC1 PASS</expect></criterion>
`DB30-1-AC1` -- the census covers exactly the 1,528; its by-key rows sum to the totals; every class is FEE-MANAGEMENT or FEE-ADMIN. Base: FAIL.

<criterion id="DB30-1-AC2" cell_refs="DB-b-53"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r30/p30_round30.py" . DB30-1-AC2</invocation><expect>DB30-1-AC2 PASS</expect></criterion>
`DB30-1-AC2` -- each fee class is mapped to external_flow or return, and every cited source line contains its quoted text at HEAD. Base: FAIL.

<criterion id="DB30-1-AC3" cell_refs="DB-b-53"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r30/p30_round30.py" . DB30-1-AC3</invocation><expect>DB30-1-AC3 PASS</expect></criterion>
`DB30-1-AC3` -- one population account traced, each fee day carrying the fee and the served flow and return. Base: FAIL.

<expected_criteria>DB30-1-AC1,DB30-1-AC2,DB30-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. The producer, sources.json, the classification table and earlier rounds' files are read, never
  edited.
- **AWS:** S3 reads only. No Black Diamond or vendor call, no secret read, no S3 write, no bun, no download of any package, script or
  program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a producer edit, a filled figure, or an account number, name or balance
  in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~32/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-53.fee-census.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 32 (round 30), cell `DB-b-53`.
<owned_cells>DB-b-53</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB30-1-AC1, DB30-1-AC2, DB30-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~32/IRPT_DASHBD.TO-DB-b-53.fee-census.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB30-1-AC1,DB30-1-AC2,DB30-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the census totals by class, the classification with its lines, the trace in one
sentence, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only census over landed silver and served gold; no S3 write.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB30-1-AC1..AC3 base FAIL (no record) at base 74730695dc; positive control on a planted record PASS (1,528; the source-line verifier read account_return_daily.py's FEE-MANAGEMENT boundary line at HEAD).
lane: the <paths> block IS the grant.
</preflight>
