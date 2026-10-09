# TO ADVI_COTBKF.TO-CB-ah-2.as-traded-basis-build -- round 34 CB-ah-2: value at the as-traded close, rebuild the FWD-3 tables locally, re-grade

<to_id>ADVI_COTBKF.TO-CB-ah-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~62</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>34</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ah-2` (`decompositions/ADVI_COTBKF_DECOMP.round34.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3's daily chain (`data/assets/scripts/silver/`) values each holding-day at a price from one store:
`s3://opal-data-cot/silver/prices/canonical_prices.parquet`, read through `commonwealth_price_census` STORES[0] in
`commonwealth_daily_valuation.py`, around `load_price_store` :133 and `security_day_prices` :207.

Round 33's census (`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~60/price_basis_census.csv`, one row per ticker)
classed the store's `yahoo_finance` series as follows: 2,079 tickers `dividend_adjusted`, 79 `mixed`, 175 `as_traded`, 872
`indistinguishable`, 266 `other` and 109 `no_yahoo`. 38% of served account-days rest on the adjusted ones.

**The ruling (CTO ADDENDUM 8).** Valuation uses the AS-TRADED close: Yahoo `Close`, split-adjusted, never dividend-adjusted. Dividends
and distributions enter ONLY as cash, which the chain already does (`dv` / `dvr`). Round 28's `method_r28` split scaling still turns a
split-adjusted `Close` into as-traded before a split. The cached Yahoo pulls (both `Close` and `Adj Close`) for all 3,580 tickers are at
`.scratch/advi_cotbkf/yahoo_census/` (copied into your worktree). Do NOT call Yahoo again.

**Your item.** Add a price basis to the chain, in this order.

1. **Rule commit FIRST, alone, before any real run** (CVO note, D2-S47).
   - Add an option `price_basis` with values `store` (today's behaviour) and `as_traded`.
   - For a ticker the census classes `dividend_adjusted` or `mixed`, `as_traded` replaces the store's `yahoo_finance` points with the
     cached Yahoo `Close` on the same dates. It re-derives that ticker's `linear_interpolation` days between the replaced points by the
     store's own interpolation rule (linear in the date between neighbouring points). Every other ticker and source label is unchanged.
   - `as_traded` becomes the DEFAULT.
   - Write one test that shows a dividend-adjusted series replaced and its interpolated days re-derived.
2. **Wire it through.**
   - `commonwealth_sweep_regrade.py` gains `--before-price-basis` / `--after-price-basis` (default `as_traded`).
   - `commonwealth_fwd3_serve.py` `--build` gains `--price-basis` (default `as_traded`) and prints it on its FWD3-BUILD line.
   - The builder's ABSENT list reason generalises from `REGRESSED_UNDER_R28` to `REGRESSED_UNDER_<after rule>`: MATCH under the before
     build, DIFF under the after build. Print the list.
3. **Hold option.** `--hold-cusips <comma list>` (default empty) on the build blanks every holding-day of those CUSIPs with reason
   `HELD_SOURCE_UNDER_REVIEW`. Round 34's `CB-ah-1` may require it for the three `bd_txn_price` bonds.
4. **Persist the price input.** Write the as-traded price input the build used to `.scratch/advi_cotbkf/r34_price_input.parquet`, with
   columns ticker, date, price, source, basis, as_of. Print its sha256. The pair's COO half names it.
5. **Re-grade the served build against the as-traded build.**
   `--before-list v1 --after-list v1 --before-cash-leg method_r28 --after-cash-leg method_r28 --before-price-basis store
   --after-price-basis as_traded --data-dir .scratch/advi_cotbkf/r34`. Print MATCH/DIFF/UNGRADABLE both sides, regressions and movers
   back, and the 4 round-28 ABSENT months' grades under as-traded. Print SCHB (808524102) and SCHZ (808524839) on 2022-10-12 beside the
   round-31 evidence key
   `s3://opal-data-assets/commonwealth/cottonwood/silver/price_evidence/date=2022-10-12/part-00000.parquet`. Nothing is tuned to fit
   them.
6. **Build locally:** `--build --price-basis as_traded` into `.scratch/advi_cotbkf/fwd3_serve_r34`, then `--dry-run`. Do NOT `--apply`.
   The served mint is `CB-ah-3`, on the applier.

### ACCEPTANCE

<criterion id="CB34ah2-AC1" cell_refs="CB-ah-2"><invocation>python data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1 --after-list v1 --before-cash-leg method_r28 --after-cash-leg method_r28 --before-price-basis store --after-price-basis as_traded --data-dir .scratch/advi_cotbkf/r34 --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~62</invocation><expect>price_basis_after=as_traded</expect></criterion>
`CB34ah2-AC1` -- the re-grade runs store -> as_traded, and its LAST line carries `price_basis_after=as_traded`, the grade counts and
`regressions=<n>`.

<criterion id="CB34ah2-AC2" cell_refs="CB-ah-2"><invocation>python data/assets/scripts/silver/commonwealth_fwd3_serve.py --build --data-dir .scratch/advi_cotbkf/r34 --out .scratch/advi_cotbkf/fwd3_serve_r34</invocation><expect>FWD3-BUILD daily_rows=</expect></criterion>
`CB34ah2-AC2` -- the three tables are built locally; the FWD3-BUILD line is the builder's own vocabulary. That the line also carries
`price_basis=as_traded` is read under AC3.

<criterion id="CB34ah2-AC3" cell_refs="CB-ah-2" judgment="true"/>
`CB34ah2-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded:
- the rule commit precedes every run's output in git;
- the FWD3-BUILD line carries `price_basis=as_traded`;
- the substitution follows the census classes exactly;
- SCHB and SCHZ on 2022-10-12 are read against the evidence key and are not tuned.

<expected_criteria>CB34ah2-AC1,CB34ah2-AC2,CB34ah2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Large output goes under `.scratch/`,
  uncommitted.
- **No S3 write.** Reads are limited to the buckets the chain already reads and the round-31 evidence key. No Yahoo call, because the
  cache is the input. Never read `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Hygiene.** The silver test suite (`pytest data/assets/scripts/silver/tests`) stays green. Fix any test the new default turns red
  inside the grant, and name it.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W62-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/commonwealth_sweep_regrade.py
data/assets/scripts/silver/commonwealth_fwd3_serve.py
data/assets/scripts/silver/commonwealth_sweeps.py
data/assets/scripts/silver/tests/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round34.md</decomp_doc> (round 34), cell `CB-ah-2`.
<owned_cells>CB-ah-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB34ah2-AC1, CB34ah2-AC2, CB34ah2-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~62/ADVI_COTBKF.TO-CB-ah-2.as-traded-basis-build.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB34ah2-AC1,CB34ah2-AC2,CB34ah2-AC3` BEFORE the flip. Mechanical:
AC1, AC2. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:**
- the two LAST lines (SWEEP-REGRADE and FWD3-BUILD) and the dry run's addresses, rows and hashes;
- the ABSENT list under as-traded;
- the 4 round-28 months' grades;
- SCHB and SCHZ against the evidence;
- the price input's sha256;
- commits, with the rule commit first.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local build; the served mint is CB-ah-3.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; no write.
comp-adversary: RUN -- rule commit alone before any run; substitution keyed on the census classes; the cached Yahoo pulls are the only price input (no second pass); SCHB read, not tuned; BLIND: the 266 'other' and 109 'no_yahoo' tickers keep the store price (named in the report).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 8 @bff4e48547 (the as-traded ruling) and ADDENDUM 9 @cf58046f35 (msg 3180, the rebuild); row D2-S50.
