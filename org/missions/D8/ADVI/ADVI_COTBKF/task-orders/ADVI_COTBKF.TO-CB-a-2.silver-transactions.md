# TO ADVI_COTBKF.TO-CB-a-2 -- round 1 CB-a-2: the silver transactions table, every row and column typed, each row carrying its file of origin

<to_id>ADVI_COTBKF.TO-CB-a-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~2</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-06</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~C</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `CB-a-2` (`decompositions/ADVI_COTBKF_DECOMP.md`) | **outcome_ref:** FWD-1 |
**depends_on:** none (the lineage contract is fixed in the decomposition)

---

## WORKER FACE

### THE CELL

`CB-a-2`, hop 3 of the round-1 thread: the Commonwealth transactions file becomes Opal's silver transactions table. You build the
converter and prove it on the real file into a LOCAL directory. You write NOTHING to S3: the `--apply` run is the issuer's act.

**The input, measured at the base.** `$HOME/Downloads/Files.zip` (the Box download; READ ONLY) holds the zip
`Cottonwood Capital Advisors_Portfolio_Accounting_Performance_ClientDelivery.zip` (23,833,956 bytes, SHA-256
`a3a2772efa3447fd3adaa4b6eb5dacdf400667743c4f4040e2d0cad3296d658b`), whose member
`CFN_SCTASK0548380_Portfolio_Accounting_Performance/CFN_SCTASK0548380_Historical_Transactions_20260623_102751.txt` (308,186,603 bytes) is
the transactions file:
- pipe-delimited, one header line, 20 columns: `Advisor_ID|Account_Number|Transaction_Type|Transaction_Description|Cusip|FundCode|Symbol|
  Quantity|Amount|AI|Trade_Date|Cost_Date|Settle_Date|Asset_Type|CA_Event_Id|LongShort_Indicator|Position_Type|Security_Description|
  Transaction_Note|AsOfDate`;
- 1,416,501 PHYSICAL lines (header + 1,416,500), against the brief's 1,416,497 rows. **The 3-line difference is unexplained: account for
  every physical line** (blank lines, a trailer, a line break inside a field, or real rows) and print the count of each kind. Never drop a
  line silently; a line you cannot parse is counted as `unexplained`;
- `Account_Number` carries leading zeros (`acct#c9405219`): a STRING, never a number; `Cusip` and `FundCode` likewise strings;
- the brief measures trade dates 2013-04-03 to 2026-06-22 and 1,533 distinct accounts.

**Build `data/assets/scripts/silver/commonwealth_transactions.py`:**
1. CLI: `--source <path or s3://...>` (the inner zip, or with `--outer-member <name>` the outer Box zip holding it), `--data-date 2026-06-23`,
   `--out <local dir>` (dry run writes here), `--apply` (writes to S3 at the builder key instead; written and unit-tested, never run by you),
   `--verify-sample <n>` (default 50). Device-free: no path or user name in the code (LD-0405).
2. Typing: dates (`Trade_Date`, `Cost_Date`, `Settle_Date`, `AsOfDate`) as `date32`; `Quantity`, `Amount`, `AI` as `float64` parsed from
   the text exactly as written; every other column a string. Keep EVERY vendor column and EVERY row (doctrine R10). De-duplicate only rows
   identical in all 20 vendor columns, and COUNT them (`dropped_dup`).
3. Lineage columns (the decomposition's LINEAGE CONTRACT, exactly): `source_zip` (the zip's name as shipped), `source_zip_sha256`
   (lowercase hex, computed from the zip's bytes), `source_file` (the member path as shipped), `source_line` (int, the 1-based PHYSICAL
   line number in the member file; the header is line 1). A row kept after de-duplication carries its FIRST occurrence's line.
4. Key from the naming builder only (rule 30): `address('commonwealth','cottonwood','silver','transactions','date=<data-date>')`; under
   it, parquet files partitioned `trade_year=<YYYY>/` (hive style), written with pyarrow. The local `--out` run writes the same relative
   layout under `<out>/`.
5. Self-verify after writing: read the output back; re-read `--verify-sample` rows chosen at random (seeded) from the member file BY
   `source_line` and compare the raw line text with the row's 20 vendor values re-joined by `|`; count matches.
6. LAST line, exactly this field order:
   `SILVER-TRANSACTIONS lines=<physical> rows_out=<n> dropped_dup=<k> blank=<b> unexplained=<u> accounts=<distinct Account_Number> columns=<n> min_trade=<date> max_trade=<date> lineage_sample=<ok>/<n>`.
7. Tests `data/assets/scripts/silver/tests/test_commonwealth_transactions.py` (pytest, a small fixture zip in `tmp_path`): leading zeros
   kept; dates typed; an exact duplicate dropped and counted, its first line kept; a blank line counted, not a row; lineage columns and
   `source_line` correct; partition layout; the sample verification catches a tampered line (difference control).

### ACCEPTANCE

<criterion id="CB2-AC1" cell_refs="CB-a-2"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_transactions.py</invocation><expect>passed</expect></criterion>
`CB2-AC1` -- the converter's behaviour on a fixture, including the tampered-line difference control.

<criterion id="CB2-AC2" cell_refs="CB-a-2"><invocation>python data/assets/scripts/silver/commonwealth_transactions.py --source "$HOME/Downloads/Files.zip" --outer-member "Cottonwood Capital Advisors_Portfolio_Accounting_Performance_ClientDelivery.zip" --data-date 2026-06-23 --out .scratch/advi_cotbkf/silver --verify-sample 50</invocation><expect>unexplained=0 accounts=1533 columns=24 min_trade=2013-04-03 max_trade=2026-06-22 lineage_sample=50/50</expect></criterion>
`CB2-AC2` -- the seam with the real neighbour: the real transactions file converts with every physical line accounted for, 1,533 accounts,
20 vendor + 4 lineage columns, the measured date span, and 50 of 50 sampled rows traced back to their raw line.

<expected_criteria>CB2-AC1,CB2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. The local output goes under `.scratch/`,
  uncommitted (it is about a gigabyte of rows; never commit it).
- **No S3 write, no `--apply`, no AWS call** (the tests stub the client). The apply is the issuer's act under a ledger entry.
- **The input is read-only.** Never write into `Downloads`.
- **Rule 13:** a DS-lane script; your commit is a candidate; no `safe-deploy`.
- **Within 120 seconds:** CB2-AC2 runs under the worker's `timeout 120`; read the member as a stream and write with pyarrow (no row-by-row
  Python object build), or the criterion records a timeout.
- **Refusal clause.** If a criterion cannot be met as written (the real file has 1,532 accounts, or 2 lines are a trailer you cannot type),
  stop, write the reason in your report and a surprise row (id `ADVI_COTBKF-W2-S<k>`) with the measured values, and do not weaken the test
  or the expected value.

<paths>
data/assets/scripts/silver/commonwealth_transactions.py
data/assets/scripts/silver/tests/test_commonwealth_transactions.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit (`lib/opal_naming.py`, `data/assets/scripts/silver/tests/conftest.py` included).

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.md</decomp_doc> (round 1), cell `CB-a-2`.
<owned_cells>CB-a-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB2-AC1, CB2-AC2. Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~2/ADVI_COTBKF.TO-CB-a-2.silver-transactions.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB2-AC1,CB2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the `SILVER-TRANSACTIONS` line, what the line accounting found (each kind of non-row line and where), the schema as written,
the partition listing of the local output, the test list, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time backfill, run by hand (C-ONE-TIME); no schedule is created.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the issuer's apply runs under the laptop profile into a new prefix of opal-data-assets.
comp-adversary: RUN -- cross-firm (cottonwood scope from the builder, C-FIRM); sensitive fields (the transactions file carries none of C-SENSITIVE's four: no tax ID, birth date, license or passport column); every vendor column kept (R10); no shadow pipeline; BLIND: the 3 unexplained physical lines (the worker accounts for them).
lane: the <paths> block IS the grant (worker RULING 1); data/assets/scripts/silver/ is DS-lane under rule 13.
</preflight>

Source: PRD v0.3 @5567e751f1 section 2 hop 3, C-SILVER; decomposition @c10cf0c76a (the lineage contract).
