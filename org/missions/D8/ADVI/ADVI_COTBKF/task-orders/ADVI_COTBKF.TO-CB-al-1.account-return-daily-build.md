# TO ADVI_COTBKF.TO-CB-al-1.account-return-daily-build -- round 38 CB-al-1: Cottonwood account_return_daily, built locally through its one producer

<to_id>ADVI_COTBKF.TO-CB-al-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~66</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>38</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-al-1` (`decompositions/ADVI_COTBKF_DECOMP.round38.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

The investor-reporting gold table `account_return_daily` is empty for Cottonwood. Its address comes from the builder:
`lib/opal_naming.address("irpt", "cottonwood", "gold", "account_return_daily", "date=<D>")`, which gives
`s3://opal-data-cottonwood/irpt/cottonwood/gold/account_return_daily/date=<D>`, with `/data.parquet` and `/manifest.json` per day.

The table has ONE producer: `data/assets/scripts/gold/irpt_reporting/account_return_daily.py`. It owns the schema (`COLUMNS`,
`ARROW_SCHEMA` at :247-275), the enum check (`_check_enums` :1688) and the writer (`emit_day` :1714). One adapter per firm is declared
in `sources.json` beside it.

Cottonwood's daily returns already exist as ADVI_COTBKF's served as-traded FWD-3 tables:
`s3://opal-data-assets/commonwealth/cottonwood/silver/{daily_returns,account_day_value,month_grades}/date=2026-06-23/part-00000.parquet`.
- They hold 1,691,729 daily rows.
- 5 account-months are ABSENT (`REGRESSED_UNDER_AS_TRADED`).
- 988 account-days of three bonds are held (`HELD_SOURCE_UNDER_REVIEW`).

**Your item (CTO ADDENDUM 11.2).** No S3 write: the write is `CB-al-2`, on the applier. Do NOT edit the producer, because it is
another project's code. Write `data/assets/scripts/silver/commonwealth_account_return_daily.py --out <dir>`, an ADAPTER that does the
following.

1. **Reads the served FWD-3 tables.** Print each key's VersionId; read only the columns needed.
2. **Maps each Cottonwood account-day to the producer's `COLUMNS`,** exactly the producer's names, types and enum values.
   - `firm=cottonwood`; `account_id`; `business_date`; `market_value_eod` (FWD-3 day value); `external_flow`; `income_received`;
     `total_return_daily` (FWD-3 daily return); and so on.
   - A column FWD-3 cannot fill is null with its `_reason` column set, where the producer has one. It is never zero.
3. **The two exceptions are blanks with reasons:** the 5 ABSENT account-months' days, and the held bond days where they change the
   account's value. Use the producer's own `day_quality` / `guard_state` enum values where one fits. Print the counts.
4. **Declares the method.** FWD-3 values are rebuilt from positions at the as-traded close. The producer's method reads the custodian's
   whole-account value and is "not rebuilt from positions". The rows must carry this claim in a field a consumer can reject on
   (`return_basis` or `history_scope`).
   - If the producer's enum check refuses every value that would say it truthfully, STOP that branch.
   - File a BLOCKING row naming the gap: a new enum value, or a Cottonwood adapter entry in `sources.json`, is IRPT_DASHBD's change.
   - Never write a value that claims the custodian method.
5. **Builds every day through the producer's own path.**
   - Validate with `_check_enums`.
   - Call `emit_day(s3, frame, "cottonwood", day, upload=False, ...)` for every business day, and print the addresses it returns.
   - Write the frames locally as `.scratch/advi_cotbkf/ard_cottonwood/date=<D>/data.parquet` using the producer's `ARROW_SCHEMA`, and
     record each file's sha256 in a manifest `ard_cottonwood_manifest.json`.
   - Print the day count, the row count and the first and last day.
6. **Rule first.** Commit the adapter with its mapping and exception rule in its OWN commit before the first run.

Write `account_return_daily_build.md`. LAST line exactly:
`ARD-COTTONWOOD days=<n> rows=<r> absent_days=<a> held_days=<h> enum_ok=<True|False> addresses_from_builder=<True|False>`.

### ACCEPTANCE

<criterion id="CB38al1-AC1" cell_refs="CB-al-1"><invocation>python data/assets/scripts/silver/commonwealth_account_return_daily.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~66</invocation><expect>ARD-COTTONWOOD days=</expect></criterion>
`CB38al1-AC1` -- the partitions are built locally through the producer's schema and `emit_day(upload=False)`, with exceptions and
method claim printed.

<criterion id="CB38al1-AC2" cell_refs="CB-al-1" judgment="true"/>
`CB38al1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded:
- every row's method claim is truthful (never the custodian method);
- the two exceptions read as blanks with reasons, never zeros;
- the producer is unedited.

<expected_criteria>CB38al1-AC1,CB38al1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Built files go under `.scratch/`,
  uncommitted.
- **Read-only and no S3 write.** Reads are limited to the served FWD-3 keys and the producer's own inputs, if it needs any. NEVER read
  or list `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **The producer is never edited.** A needed producer change is a BLOCKING row.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W66-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_account_return_daily.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round38.md</decomp_doc> (round 38), cell `CB-al-1`.
<owned_cells>CB-al-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB38al1-AC1, CB38al1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~66/ADVI_COTBKF.TO-CB-al-1.account-return-daily-build.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB38al1-AC1,CB38al1-AC2` BEFORE the flip. Mechanical: CB38al1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:**
- the ARD-COTTONWOOD line;
- the column mapping, with each null and its reason;
- the method claim's field and value, or the BLOCKING gap;
- the exception counts;
- the first and last addresses;
- commits, with the rule commit first.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time local build; any schedule for this firm is IRPT_DASHBD's.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; no write.
comp-adversary: RUN -- the one producer's schema, enum check and writer path only (no shadow writer); a truthful method claim or a BLOCKING gap; exceptions as reasoned blanks; BLIND: a producer field whose meaning FWD-3 cannot reproduce (named null with reason).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 11.2 @43bbe32935 (msg 3363); IRPT_DASHBD row S43.
