# TO ADVI_COTBKF.TO-CB-aj-1.cot-price-rewrite-build -- round 36 CB-aj-1: build the 38 cot price files without the 49F rows, locally, with a per-key diff

<to_id>ADVI_COTBKF.TO-CB-aj-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~64</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>36</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-aj-1` (`decompositions/ADVI_COTBKF_DECOMP.round36.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

Thirty-eight keys in Cottonwood's bucket `opal-data-cot` carry rows that 49 Financial's price override wrote on 2026-06-09. Their
`source` label is spelled `bd` + `_txn_price`. The rows price three corporate bonds at 49F's constants:

| CUSIP | issuer | 49F constant |
|---|---|---|
| 05613L3H2 | BNP Paribas | 1.0188 |
| 95000U2D4 | Wells Fargo 4.15% 2029 | 0.9804 |
| 651639AX4 | Newmont 2.8% 2029 | 0.9037 |

The 38 keys, each with its current VersionId, are in section 5 of
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~63/bd_txn_provenance.md`:
- 37 daily files `silver/prices/2026-04-14.parquet` .. `2026-06-05.parquet`, 3 such rows each;
- `silver/prices/canonical_prices.parquet`, 1,623 such rows out of 11,291,021.

Every key is a FULL price file holding all of Cottonwood's other prices too.

CTO ADDENDUM 10 rules a REWRITE, not a delete:
- remove the 49F-sourced rows;
- re-price the three bonds from Cottonwood's source of record, Yahoo as-traded (yfinance first);
- leave every other row byte-identical.

**Your item.** No S3 write; the write is `CB-aj-2`, on the applier. Write
`data/assets/scripts/silver/commonwealth_cot_price_rewrite.py --out <dir>`. It does the following.

1. **Reads each of the 38 keys AT THE NAMED VersionId** (`get_object` with `VersionId`), and stops if any key's current version differs
   from section 5. Print `key`, `version`, `rows`.
2. **Yahoo for the bonds.** Find a Yahoo series for each bond by a rule written BEFORE the run.
   - Allowed: a CUSIP-keyed or bond-specific symbol that Yahoo returns. The issuer's EQUITY ticker is never allowed, because that is
     what mis-priced them originally.
   - If one is found, re-price each of that bond's rows on the same dates from the as-traded `Close` (`auto_adjust=False`), with
     `source=yahoo_finance`.
   - If none is found, the bond's 49F rows are REMOVED with no replacement (the bond reads unpriced), and a BLOCKING surprise row asks
     for a source ruling.
   - Call Yahoo gently: at most a few calls, and print the count.
3. **Writes each rewritten file locally** under `.scratch/advi_cotbkf/cot_price_rewrite/<key>` with the same schema, column order and
   dtypes. Print its sha256.
4. **Per-key diff.** Compare old and new, keyed on (date, ticker or asset_name, source). Print rows_before, rows_after, removed,
   repriced, and `other_rows_identical=True|False`. That last value is True only when every row that is not a 49F row has
   byte-identical values.
5. **Writer census.** Name, by file and line from the repo, every writer of `opal-data-cot` `silver/prices/` and its schedule (SSM
   association, EventBridge or cron in `infra/aws/terraform/cot-pipeline/`). A scheduled writer would overwrite the rewrite. Print the
   count of writers and whether any is scheduled and enabled. Use a live `describe` of the named schedule resource, which is a single
   read.
6. **Rule commit first:** commit the script with its Yahoo rule and its diff rule in its OWN commit, before the first run.

Write `cot_price_rewrite.md` and `cot_price_rewrite_manifest.json` (per key: version_before, sha256_after, rows, removed, repriced).
LAST line exactly:
`COT-PRICE-REWRITE keys=38 rows_removed=<n> rows_repriced=<m> other_rows_identical=<True|False> bonds_priced=<p>/3 writers=<w> scheduled=<s>`.

### ACCEPTANCE

<criterion id="CB36aj1-AC1" cell_refs="CB-aj-1"><invocation>python data/assets/scripts/silver/commonwealth_cot_price_rewrite.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~64</invocation><expect>COT-PRICE-REWRITE keys=38</expect></criterion>
`CB36aj1-AC1` -- the 38 rewritten files are built locally, the per-key diff is printed, and the bonds are re-priced or removed by the
rule.

<criterion id="CB36aj1-AC2" cell_refs="CB-aj-1" judgment="true"/>
`CB36aj1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded:
- `other_rows_identical=True` on all 38;
- the bond rule committed before the run;
- no equity ticker used for a bond;
- the writer census complete.

<expected_criteria>CB36aj1-AC1,CB36aj1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. The rewritten files go under `.scratch/`,
  uncommitted.
- **No S3 write.** Reads only the 38 named versions in `opal-data-cot`, the cot schedule resource (one `describe`), and Yahoo for the
  bonds. NEVER read or list `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Naming gate.** If it refuses typed firm tokens, derive them from `lib/opal_naming` as ~61 did.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W64-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_cot_price_rewrite.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round36.md</decomp_doc> (round 36), cell `CB-aj-1`.
<owned_cells>CB-aj-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB36aj1-AC1, CB36aj1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~64/ADVI_COTBKF.TO-CB-aj-1.cot-price-rewrite-build.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB36aj1-AC1,CB36aj1-AC2` BEFORE the flip. Mechanical: CB36aj1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:**
- the COT-PRICE-REWRITE line;
- per key: version_before, rows, removed, repriced, sha256_after;
- the bonds' Yahoo outcome and the symbol used, or why none;
- the writer census;
- commits, with the rule commit first.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- issuer pre-scan of infra/aws/terraform/cot-pipeline: 17 .tf files, 5 schedule_expression rules (bd_cot_keepalive 15m, etf_ownership 10:30Z, satellites x2, aws_scheduler cot_bd_session_daily_et 07:30 ET) + 3 event-pattern rules (session/bronze/silver complete) that chain to the gold run; BLIND: which of them write silver/prices/ and whether each is ENABLED live -- the cell's census reads that (the store has not moved since 2026-06-09).
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; no write.
comp-adversary: RUN -- versioned reads at the named VersionIds; the bond rule is written before the run and never uses the equity ticker; the other-rows identity is proven per key; BLIND: a reader that pins an old VersionId (none known).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 10 (msg 3266); row D2-S52.
