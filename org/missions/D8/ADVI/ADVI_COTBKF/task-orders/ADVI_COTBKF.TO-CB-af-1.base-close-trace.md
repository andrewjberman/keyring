# TO ADVI_COTBKF.TO-CB-af-1.base-close-trace -- round 32 CB-af-1: where the chain's base close for SCHB and SCHZ comes from, and why it sits under as-traded

<to_id>ADVI_COTBKF.TO-CB-af-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~59</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>32</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-af-1` (`decompositions/ADVI_COTBKF_DECOMP.round32.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3's daily chain (`data/assets/scripts/silver/`) values each holding at a stored close.

On 2022-10-12 the chain's close for two ETFs sits under Yahoo's split-adjusted `Close` by a different amount for each. The same gap
appears under both cash-leg methods, before any split scaling (row ADVI_COTBKF-D2-W58-S1):

| CUSIP | symbol | chain close (r26) | Yahoo Close (split-adj.) | ratio |
|---|---|---|---|---|
| 808524102 | SCHB | 13.3302 | 13.98 | 0.954 |
| 808524839 | SCHZ | 19.7181 | 22.465 | 0.878 |

The Yahoo values are stored at
`s3://opal-data-assets/commonwealth/cottonwood/silver/price_evidence/date=2022-10-12/part-00000.parquet`. That file was written by
`data/assets/scripts/silver/commonwealth_split_level_probe.py`.

The chain's price path is in `data/assets/scripts/silver/commonwealth_daily_valuation.py`:
- `load_price_store` at line 133;
- `read_sechist` at line 152 (accepted field names `_SECHIST_PRICE` at line 147);
- `resolve_series` at line 187;
- `security_day_prices` at line 207.

**Your item (CTO ADDENDUM 7, msg 3005).** READ-ONLY: no rule change; no S3 write. Write a script
`data/assets/scripts/silver/commonwealth_base_close_trace.py --data-dir <dir> --out <dir>`.

1. For each CUSIP, name the chain's price source for 2022-10-12. Print the store or prefix, the series key, the FIELD read, and the
   series' own date for that row (or the carry-forward source date, if the price is carried).
2. Over the held window, print the chain's close beside:
   - Yahoo `Close` (split-adjusted);
   - Yahoo `Adj Close` (split- and dividend-adjusted).

   Use one `yfinance` history call per symbol with `auto_adjust=False`, so both columns arrive. Sample at least the first trading day
   of each quarter plus 2022-10-12. Print the ratio chain / Close and chain / Adj Close per sampled day.
3. Classify each CUSIP by a rule written in the script BEFORE its run, to one of:
   - `adj_close_base`: the chain matches `Adj Close` within 0.5% on at least 80% of sampled days;
   - `stale_carry`: the chain's price is carried from an earlier date, and that date's Yahoo `Close` matches within 0.5%;
   - `other_source:<what>`;
   - `untraced:<what was checked>`.

Write `base_close_trace.md`. LAST line exactly:
`BASE-TRACE cusips=2 adj_close_base=<a> stale_carry=<b> other_source=<c> untraced=<d>`.

### ACCEPTANCE

<criterion id="CB32af1-AC1" cell_refs="CB-af-1"><invocation>python data/assets/scripts/silver/commonwealth_base_close_trace.py --data-dir .scratch/advi_cotbkf/r28 --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~59</invocation><expect>BASE-TRACE cusips=2</expect></criterion>
`CB32af1-AC1` -- both CUSIPs traced to a class from printed rows. Data-dir `.scratch/advi_cotbkf/r28` is the built input; rebuild it
with the default re-grade if absent.

<criterion id="CB32af1-AC2" cell_refs="CB-af-1" judgment="true"/>
`CB32af1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the class follows from the printed per-day rows by the
pre-written rule, and the named source is the one the chain actually reads.

<expected_criteria>CB32af1-AC1,CB32af1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Large output goes under `.scratch/`,
  uncommitted.
- **Read-only.** No rule change and no S3 write.
- **Reads:** the buckets the chain already reads, the round-31 evidence key, and Yahoo (one call per symbol). Never read
  `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`. No Bloomberg.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W59-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_base_close_trace.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round32.md</decomp_doc> (round 32), cell `CB-af-1`.
<owned_cells>CB-af-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB32af1-AC1, CB32af1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~59/ADVI_COTBKF.TO-CB-af-1.base-close-trace.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB32af1-AC1,CB32af1-AC2` BEFORE the flip. Mechanical: CB32af1-AC1. A judgment
criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the BASE-TRACE line; per CUSIP the source, field and series date, the sampled ratios, and the class; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only trace.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- class by a rule written before the run; Close and Adj Close both printed so neither basis is assumed; BLIND: a source the chain reads that Yahoo cannot reproduce (named as other_source).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 7 @2a140ad0bb (msg 3005); row D2-W58-S1.
