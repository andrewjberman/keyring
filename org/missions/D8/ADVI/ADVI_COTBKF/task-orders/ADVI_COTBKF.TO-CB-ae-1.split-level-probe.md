# TO ADVI_COTBKF.TO-CB-ae-1.split-level-probe -- round 31 CB-ae-1: one outside as-traded close settles D2-S45

<to_id>ADVI_COTBKF.TO-CB-ae-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~58</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>31</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ae-1` (`decompositions/ADVI_COTBKF_DECOMP.round31.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

Two methods of FWD-3's daily chain disagree on the pre-2024-10-11 price level of two CUSIPs held by accounts acct#79d02c2c and acct#4a890dd1.
`method_r28` applied splits dated 2024-10-11 from the account rows; `method_r26` did not. On 2022-10-12 (from
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~57/scale_trace.md`):

| CUSIP | split | r26 close | r28 close |
|---|---|---|---|
| 808524102 | x3 | 13.3302 | 39.9906 |
| 808524839 | x2 | 19.7181 | 39.4362 |

One outside, as-traded close per CUSIP on that day decides which is right (row ADVI_COTBKF-D2-S45).

**Your item (CTO ADDENDUM 6, msg 2968).** Write `data/assets/scripts/silver/commonwealth_split_level_probe.py --out <dir>`.

1. **Resolve each CUSIP to a Yahoo symbol, printing the source.**
   - 808524839 is `SCHZ` per the delivery's own symbol column, as listed in
     `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/PRICE_NEED/COTTONWOOD_PRICE_NEED_RANKED.csv`.
   - Find 808524102's symbol in the delivery's rows the same way `data/assets/scripts/silver/commonwealth_price_need.py` reads symbols.
   - Never guess a ticker. An unresolved CUSIP is a BLOCKING surprise row.
2. **Read Yahoo via `yfinance`** (installed; egress open). Get daily history spanning 2022-10-12 and the split series for each symbol.
   Be gentle: one history call per symbol.
3. **TRAP:** Yahoo's `Close` is split-ADJUSTED, so a raw `Close` reads the r26 level by construction.
   - Compute `as_traded = Close(2022-10-12) x product of every split ratio dated after 2022-10-12`, from Yahoo's own split series.
   - Print `Close`, the split list, the factor and `as_traded`.
   - Also print whether Yahoo's split series names a split on 2024-10-10/11 with the same ratio as the rows (x3, x2).
4. **Branch, by a rule written in the script BEFORE its run.** Per CUSIP, compare `as_traded` to the r28 and r26 closes above, within
   2%.
   - Both match r28: branch `A`.
   - Both match r26: branch `B`.
   - Anything else: `OTHER`, plus a BLOCKING surprise row.
5. **Store the evidence.** Write one parquet: cusip, symbol, symbol_source, close, split list, factor, as_traded, as_of (the fetch
   UTC), source=`yahoo/yfinance`.
   - Write it to the key from `lib/opal_naming.address("commonwealth", "cottonwood", "silver", "price_evidence", "date=2022-10-12",
     "part-00000.parquet")`. Use the builder's output, never a typed path.
   - Read the key back and print `readback_rows`.
   - Also write `split_level_probe.md` to `--out`.

LAST line exactly: `LEVEL-PROBE cusips=2 branch=<A|B|OTHER> key=<s3 key> readback_rows=2`.

### ACCEPTANCE

<criterion id="CB31ae1-AC1" cell_refs="CB-ae-1"><invocation>python data/assets/scripts/silver/commonwealth_split_level_probe.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~58</invocation><expect>LEVEL-PROBE cusips=2</expect></criterion>
`CB31ae1-AC1` -- both CUSIPs priced as-traded from Yahoo, the branch printed by the pre-written rule, and the evidence stored and read back.

<expected_criteria>CB31ae1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **S3 writes:** exactly ONE new key, the `price_evidence` key above, and nothing else. No overwrite of any existing key: check
  `head-object` first, and if it exists, stop and file a row.
- Reads: the delivery's buckets that the chain already reads, plus Yahoo. Never read `opal-data-bd`, `opal-data-49financial`,
  `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`. No Bloomberg.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W58-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_split_level_probe.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round31.md</decomp_doc> (round 31), cell `CB-ae-1`.
<owned_cells>CB-ae-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB31ae1-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~58/ADVI_COTBKF.TO-CB-ae-1.split-level-probe.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB31ae1-AC1` BEFORE the flip. Mechanical.
</proof_of_spec>

**REPORT:** the LEVEL-PROBE line, per CUSIP the symbol and its source, Close, the splits, as_traded, and the branch; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-shot evidence read.
comp-iam: DECLARED-NOT-APPLICABLE dell2 identity; one PutObject to a new key under the project's address() prefix; BLIND: none.
comp-adversary: RUN -- Yahoo's Close is split-adjusted (the trap, named in the cell); the branch rule is written before the run; BLIND: a Yahoo split series that is itself wrong (printed beside the rows' ratio).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 6 @d6e3227fd7 (msg 2968); row D2-S45.
